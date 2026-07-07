#!/usr/bin/env python3
"""Report-only health checks for OSL affiliated projects.

The script intentionally exits 0 by default. It is a signal-gathering tool for
human reviewers, not an automated removal mechanism.
"""

from __future__ import annotations

import argparse
import base64
import dataclasses
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Iterable

DEFAULT_SOURCE = "data/affiliated-projects.json"
DEFAULT_REPO = "OpenScienceLabs/affiliation-requests"
GITHUB_API = "https://api.github.com"
USER_AGENT = "osl-affiliation-health-check/1.0"

LICENSE_PATHS = (
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    "LICENCE",
    "LICENCE.md",
    "COPYING",
    "COPYING.md",
)
CODE_OF_CONDUCT_PATHS = (
    "CODE_OF_CONDUCT.md",
    "CODE-OF-CONDUCT.md",
    ".github/CODE_OF_CONDUCT.md",
    "docs/CODE_OF_CONDUCT.md",
    "docs/code-of-conduct.md",
)
README_PATHS = (
    "README.md",
    "README.rst",
    "README.txt",
    "README",
)
SECURITY_PATHS = (
    "SECURITY.md",
    ".github/SECURITY.md",
    "docs/SECURITY.md",
)
CONTRIBUTING_PATHS = (
    "CONTRIBUTING.md",
    ".github/CONTRIBUTING.md",
    "docs/CONTRIBUTING.md",
)
ACK_RE = re.compile(r"open\s+science\s+labs|\bOSL\b", re.IGNORECASE)
AFFILIATION_RE = re.compile(r"affiliat", re.IGNORECASE)


@dataclasses.dataclass(frozen=True)
class CheckResult:
    status: str
    check: str
    detail: str


class GitHubClient:
    def __init__(self, token: str | None = None, api_url: str = GITHUB_API) -> None:
        self.token = token
        self.api_url = api_url.rstrip("/")

    def get_json(self, path_or_url: str) -> tuple[Any | None, str | None]:
        if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
            url = path_or_url
        else:
            url = f"{self.api_url}/{path_or_url.lstrip('/')}"

        request = urllib.request.Request(url)
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("User-Agent", USER_AGENT)
        request.add_header("X-GitHub-Api-Version", "2022-11-28")
        if self.token:
            request.add_header("Authorization", f"Bearer {self.token}")

        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return json.loads(response.read().decode(charset)), None
        except urllib.error.HTTPError as exc:
            return None, f"HTTP {exc.code}: {exc.reason}"
        except urllib.error.URLError as exc:
            return None, f"URL error: {exc.reason}"
        except TimeoutError:
            return None, "request timed out"
        except json.JSONDecodeError as exc:
            return None, f"invalid JSON response: {exc}"

    def get_file_text(
        self,
        owner: str,
        repo: str,
        path: str,
        ref: str | None = None,
    ) -> tuple[str | None, str | None]:
        quoted_path = urllib.parse.quote(path, safe="/")
        api_path = f"/repos/{owner}/{repo}/contents/{quoted_path}"
        if ref:
            api_path += "?" + urllib.parse.urlencode({"ref": ref})

        payload, error = self.get_json(api_path)
        if error:
            return None, error
        if not isinstance(payload, dict):
            return None, "path is not a file"
        if payload.get("type") != "file":
            return None, f"path is {payload.get('type', 'not a file')}"

        content = payload.get("content")
        encoding = payload.get("encoding")
        if isinstance(content, str) and encoding == "base64":
            try:
                return base64.b64decode(content).decode("utf-8", errors="replace"), None
            except ValueError as exc:
                return None, f"could not decode file content: {exc}"

        download_url = payload.get("download_url")
        if isinstance(download_url, str) and download_url:
            return read_url_text(download_url)
        return "", None


def read_url_text(url: str) -> tuple[str | None, str | None]:
    request = urllib.request.Request(url)
    request.add_header("User-Agent", USER_AGENT)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace"), None
    except urllib.error.HTTPError as exc:
        return None, f"HTTP {exc.code}: {exc.reason}"
    except urllib.error.URLError as exc:
        return None, f"URL error: {exc.reason}"
    except TimeoutError:
        return None, "request timed out"


def load_projects(source: Path) -> tuple[list[dict[str, Any]], str]:
    if not source.exists():
        return [], (
            f"Source file `{source}` does not exist. Create it as JSON with a "
            "top-level `projects` array to enable project checks."
        )

    if source.suffix.lower() not in {".json", ""}:
        return [], (
            f"Source file `{source}` is not JSON. This first version uses only "
            "the Python standard library; use `data/affiliated-projects.json` "
            "or convert the source to JSON."
        )

    try:
        payload = json.loads(source.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [], f"Could not parse `{source}` as JSON: {exc}"

    if isinstance(payload, dict):
        raw_projects = payload.get("projects", [])
    elif isinstance(payload, list):
        raw_projects = payload
    else:
        return [], f"`{source}` must contain a JSON object or array."

    projects: list[dict[str, Any]] = []
    for index, item in enumerate(raw_projects, start=1):
        if isinstance(item, dict):
            projects.append(item)
        else:
            projects.append({"name": f"Invalid project #{index}", "_error": "entry is not an object"})
    return projects, f"Loaded {len(projects)} project(s) from `{source}`."


def github_slug(repository: str) -> tuple[str, str] | None:
    repository = repository.strip()
    ssh_match = re.match(r"git@github\.com:([^/]+)/(.+?)(?:\.git)?$", repository)
    if ssh_match:
        return ssh_match.group(1), ssh_match.group(2).removesuffix(".git")

    shorthand_match = re.match(r"^([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)$", repository)
    if shorthand_match:
        return shorthand_match.group(1), shorthand_match.group(2).removesuffix(".git")

    parsed = urllib.parse.urlparse(repository)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return None
    return parts[0], parts[1].removesuffix(".git")


def first_present_file(
    client: GitHubClient,
    owner: str,
    repo: str,
    paths: Iterable[str],
    ref: str | None,
) -> tuple[str | None, str | None, str | None]:
    last_error = None
    for path in paths:
        text, error = client.get_file_text(owner, repo, path, ref=ref)
        if error is None:
            return path, text or "", None
        last_error = error
    return None, None, last_error


def parse_github_datetime(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def check_url(url: str) -> CheckResult:
    request = urllib.request.Request(url, method="HEAD")
    request.add_header("User-Agent", USER_AGENT)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.getcode()
        if 200 <= status < 400:
            return CheckResult("OK", "website", f"{url} returned HTTP {status}")
        return CheckResult("WARN", "website", f"{url} returned HTTP {status}")
    except urllib.error.HTTPError as exc:
        if exc.code in {405, 403}:
            return check_url_get(url)
        return CheckResult("WARN", "website", f"{url} returned HTTP {exc.code}: {exc.reason}")
    except urllib.error.URLError as exc:
        return CheckResult("WARN", "website", f"{url} URL error: {exc.reason}")
    except TimeoutError:
        return CheckResult("WARN", "website", f"{url} timed out")


def check_url_get(url: str) -> CheckResult:
    request = urllib.request.Request(url, method="GET")
    request.add_header("User-Agent", USER_AGENT)
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.getcode()
        if 200 <= status < 400:
            return CheckResult("OK", "website", f"{url} returned HTTP {status}")
        return CheckResult("WARN", "website", f"{url} returned HTTP {status}")
    except urllib.error.HTTPError as exc:
        return CheckResult("WARN", "website", f"{url} returned HTTP {exc.code}: {exc.reason}")
    except urllib.error.URLError as exc:
        return CheckResult("WARN", "website", f"{url} URL error: {exc.reason}")
    except TimeoutError:
        return CheckResult("WARN", "website", f"{url} timed out")


def project_name(project: dict[str, Any]) -> str:
    value = project.get("name") or project.get("project") or project.get("repository") or "Unnamed project"
    return str(value)


def repository_url(project: dict[str, Any]) -> str | None:
    value = project.get("repository") or project.get("repo") or project.get("url")
    return str(value).strip() if value else None


def homepage_url(project: dict[str, Any], repo_payload: dict[str, Any] | None = None) -> str | None:
    value = project.get("website") or project.get("homepage") or project.get("docs")
    if not value and repo_payload:
        value = repo_payload.get("homepage")
    if value:
        value = str(value).strip()
    return value or None


def maintainer_handles(project: dict[str, Any]) -> list[str]:
    raw = project.get("maintainers") or []
    handles: list[str] = []
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                github = item.get("github") or item.get("handle")
                if github:
                    handles.append(str(github).lstrip("@"))
            elif isinstance(item, str) and item.startswith("@"):
                handles.append(item.lstrip("@"))
    return handles


def check_github_user(client: GitHubClient, handle: str) -> CheckResult:
    _, error = client.get_json(f"/users/{urllib.parse.quote(handle)}")
    if error:
        return CheckResult("WARN", "maintainer", f"@{handle} could not be verified: {error}")
    return CheckResult("OK", "maintainer", f"@{handle} exists")


def check_project(
    project: dict[str, Any],
    client: GitHubClient,
    max_inactive_days: int,
    now: dt.datetime,
) -> list[CheckResult]:
    results: list[CheckResult] = []

    if project.get("_error"):
        return [CheckResult("FAIL", "project data", str(project["_error"]))]

    repo_url = repository_url(project)
    if not repo_url:
        return [CheckResult("FAIL", "repository", "missing repository URL")]

    slug = github_slug(repo_url)
    if not slug:
        results.append(CheckResult("WARN", "repository", f"non-GitHub repository; manual review needed: {repo_url}"))
        site = homepage_url(project)
        if site:
            results.append(check_url(site))
        return results

    owner, repo = slug
    repo_payload, repo_error = client.get_json(f"/repos/{owner}/{repo}")
    if repo_error or not isinstance(repo_payload, dict):
        return [CheckResult("FAIL", "repository", f"GitHub API could not read {owner}/{repo}: {repo_error}")]

    results.append(CheckResult("OK", "repository", f"{owner}/{repo} is reachable"))

    if repo_payload.get("private"):
        results.append(CheckResult("FAIL", "visibility", "repository is private"))
    else:
        results.append(CheckResult("OK", "visibility", "repository is public"))

    if repo_payload.get("archived"):
        results.append(CheckResult("FAIL", "archived", "repository is archived"))
    else:
        results.append(CheckResult("OK", "archived", "repository is not archived"))

    default_branch = repo_payload.get("default_branch")
    if isinstance(default_branch, str) and default_branch:
        results.append(CheckResult("OK", "default branch", default_branch))
    else:
        default_branch = None
        results.append(CheckResult("WARN", "default branch", "could not determine default branch"))

    pushed_at = parse_github_datetime(repo_payload.get("pushed_at"))
    if pushed_at:
        inactive_days = (now - pushed_at).days
        if inactive_days > max_inactive_days:
            results.append(
                CheckResult(
                    "WARN",
                    "activity",
                    f"last push was {inactive_days} days ago ({pushed_at.date().isoformat()})",
                )
            )
        else:
            results.append(
                CheckResult(
                    "OK",
                    "activity",
                    f"last push was {inactive_days} days ago ({pushed_at.date().isoformat()})",
                )
            )
    else:
        results.append(CheckResult("WARN", "activity", "could not determine last push date"))

    if repo_payload.get("has_issues"):
        results.append(CheckResult("OK", "collaboration path", "GitHub Issues are enabled"))
    elif project.get("communication") or project.get("contact"):
        results.append(CheckResult("OK", "collaboration path", "alternate communication/contact path listed in source data"))
    else:
        results.append(CheckResult("WARN", "collaboration path", "GitHub Issues are disabled; verify alternate public path"))

    license_path, _, _ = first_present_file(client, owner, repo, LICENSE_PATHS, default_branch)
    if license_path:
        results.append(CheckResult("OK", "license", f"found `{license_path}`"))
    else:
        results.append(CheckResult("FAIL", "license", "no common license file found"))

    coc_path, _, _ = first_present_file(client, owner, repo, CODE_OF_CONDUCT_PATHS, default_branch)
    if coc_path:
        results.append(CheckResult("OK", "code of conduct", f"found `{coc_path}`"))
    else:
        results.append(CheckResult("FAIL", "code of conduct", "no common Code of Conduct file found"))

    readme_path, readme_text, _ = first_present_file(client, owner, repo, README_PATHS, default_branch)
    if readme_path:
        results.append(CheckResult("OK", "readme", f"found `{readme_path}`"))
        if readme_text and ACK_RE.search(readme_text) and AFFILIATION_RE.search(readme_text):
            results.append(CheckResult("OK", "acknowledgement", "README appears to mention OSL affiliation"))
        else:
            results.append(CheckResult("WARN", "acknowledgement", "README acknowledgement not detected; verify if accepted"))
    else:
        results.append(CheckResult("FAIL", "readme", "no common README file found"))

    security_path, _, _ = first_present_file(client, owner, repo, SECURITY_PATHS, default_branch)
    if security_path:
        results.append(CheckResult("OK", "security", f"found `{security_path}`"))
    else:
        results.append(CheckResult("WARN", "security", "no common security policy file found"))

    contributing_path, _, _ = first_present_file(client, owner, repo, CONTRIBUTING_PATHS, default_branch)
    if contributing_path:
        results.append(CheckResult("OK", "contributing", f"found `{contributing_path}`"))
    else:
        results.append(CheckResult("WARN", "contributing", "no common contribution guide found"))

    site = homepage_url(project, repo_payload)
    if site:
        results.append(check_url(site))
    else:
        results.append(CheckResult("INFO", "website", "no website/homepage listed"))

    handles = maintainer_handles(project)
    if handles:
        for handle in handles:
            results.append(check_github_user(client, handle))
    else:
        results.append(CheckResult("INFO", "maintainer", "no maintainer GitHub handles listed in source data"))

    return results


def escape_md(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_report(
    projects: list[dict[str, Any]],
    source_message: str,
    args: argparse.Namespace,
    client: GitHubClient,
) -> str:
    now = dt.datetime.now(dt.timezone.utc)
    lines: list[str] = [
        "# Affiliated Project Health Check",
        "",
        f"Generated: {now.isoformat(timespec='seconds')}",
        f"Repository: `{args.repo}`",
        f"Source: `{args.source}`",
        f"Maximum inactive days: {args.max_inactive_days}",
        "",
        f"> {source_message}",
        "",
    ]

    if not projects:
        lines.extend(
            [
                "No projects were checked.",
                "",
                "To enable checks, create `data/affiliated-projects.json` with this shape:",
                "",
                "```json",
                "{",
                "  \"projects\": [",
                "    {",
                "      \"name\": \"Example Project\",",
                "      \"repository\": \"https://github.com/example/project\",",
                "      \"website\": \"https://example.org\",",
                "      \"maintainers\": [{\"github\": \"maintainer1\"}],",
                "      \"status\": \"affiliated\"",
                "    }",
                "  ]",
                "}",
                "```",
                "",
            ]
        )
        return "\n".join(lines)

    totals = {"OK": 0, "WARN": 0, "FAIL": 0, "INFO": 0}
    project_reports: list[tuple[str, str, list[CheckResult]]] = []

    for project in projects:
        results = check_project(project, client, args.max_inactive_days, now)
        for result in results:
            totals[result.status] = totals.get(result.status, 0) + 1
        project_reports.append((project_name(project), repository_url(project) or "", results))

    lines.extend(
        [
            "## Summary",
            "",
            f"- Projects checked: {len(project_reports)}",
            f"- OK: {totals.get('OK', 0)}",
            f"- Warnings: {totals.get('WARN', 0)}",
            f"- Failures: {totals.get('FAIL', 0)}",
            f"- Informational: {totals.get('INFO', 0)}",
            "",
        ]
    )

    for name, repo_url, results in project_reports:
        lines.extend(
            [
                f"## {escape_md(name)}",
                "",
                f"Repository: {escape_md(repo_url) if repo_url else '_not listed_'}",
                "",
                "| Status | Check | Details |",
                "| --- | --- | --- |",
            ]
        )
        for result in results:
            lines.append(
                f"| {escape_md(result.status)} | {escape_md(result.check)} | {escape_md(result.detail)} |"
            )
        lines.append("")

    lines.append(
        "Human reviewers should verify failures and warnings before changing affiliation status."
    )
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=DEFAULT_REPO, help="Repository owning this workflow.")
    parser.add_argument(
        "--source",
        default=DEFAULT_SOURCE,
        help="JSON file containing affiliated project entries.",
    )
    parser.add_argument(
        "--max-inactive-days",
        type=int,
        default=180,
        help="Warn when last push is older than this many days.",
    )
    parser.add_argument("--output", help="Optional Markdown report path.")
    parser.add_argument(
        "--token",
        default=os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"),
        help="GitHub token. Defaults to GITHUB_TOKEN or GH_TOKEN.",
    )
    parser.add_argument("--api-url", default=GITHUB_API, help="GitHub API base URL.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    projects, source_message = load_projects(Path(args.source))
    client = GitHubClient(token=args.token, api_url=args.api_url)
    report = render_report(projects, source_message, args, client)
    print(report)
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
