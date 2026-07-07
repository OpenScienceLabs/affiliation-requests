#!/usr/bin/env python3
"""Lightweight issue-template validation.

If PyYAML is installed, this script parses the issue-template YAML files and
checks a few expected GitHub issue-form fields. Without PyYAML, it falls back to
basic text checks and exits successfully so local development does not require an
extra dependency.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

TEMPLATE_DIR = Path(".github/ISSUE_TEMPLATE")
FORM_FILES = {
    "affiliation-request.yml",
    "maintenance-review.yml",
    "removal-review.yml",
    "reactivation-request.yml",
}
CONFIG_FILE = "config.yml"


def load_yaml_module() -> Any | None:
    try:
        import yaml  # type: ignore[import-not-found]
    except ImportError:
        return None
    return yaml


def basic_text_check(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return [f"{path}: file is empty"]
    if path.name == CONFIG_FILE:
        for token in ("blank_issues_enabled:", "contact_links:"):
            if token not in text:
                errors.append(f"{path}: missing `{token}`")
    else:
        for token in ("name:", "description:", "title:", "labels:", "body:"):
            if token not in text:
                errors.append(f"{path}: missing `{token}`")
    return errors


def parsed_check(path: Path, yaml_module: Any) -> list[str]:
    errors: list[str] = []
    try:
        data = yaml_module.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - depends on optional PyYAML
        return [f"{path}: YAML parse error: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: top-level YAML value must be a mapping"]

    if path.name == CONFIG_FILE:
        if "blank_issues_enabled" not in data:
            errors.append(f"{path}: missing `blank_issues_enabled`")
        if "contact_links" not in data:
            errors.append(f"{path}: missing `contact_links`")
        return errors

    for key in ("name", "description", "title", "labels", "body"):
        if key not in data:
            errors.append(f"{path}: missing `{key}`")
    if not isinstance(data.get("labels"), list):
        errors.append(f"{path}: `labels` must be a list")
    if not isinstance(data.get("body"), list):
        errors.append(f"{path}: `body` must be a list")
    return errors


def main() -> int:
    if not TEMPLATE_DIR.is_dir():
        print(f"Missing template directory: {TEMPLATE_DIR}", file=sys.stderr)
        return 1

    expected = {CONFIG_FILE, *FORM_FILES}
    present = {path.name for path in TEMPLATE_DIR.glob("*.yml")}
    errors = [f"Missing issue template: {name}" for name in sorted(expected - present)]

    yaml_module = load_yaml_module()
    if yaml_module is None:
        print("PyYAML is not installed; running basic text checks only.")

    for path in sorted(TEMPLATE_DIR.glob("*.yml")):
        if yaml_module is None:
            errors.extend(basic_text_check(path))
        else:
            errors.extend(parsed_check(path, yaml_module))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("Issue template checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
