#!/usr/bin/env python3

from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs" / "PROJECT_DOCUMENTATION.md"
EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".githooks",
    ".idea",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    ".vscode",
    "DerivedData",
    "__pycache__",
    "build",
    "dist",
}
EXCLUDED_FILES = {
    "docs/PROJECT_DOCUMENTATION.md",
}
TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".swift",
    ".sh",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".xml",
}
SECTION_ORDER = [
    "",
    "agents",
    "projects",
    "scripts",
    "docs",
    "playbooks",
    "specs",
]


def git_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        return "uncommitted"
    return result.stdout.strip() or "uncommitted"


def should_skip(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    rel_str = rel.as_posix()
    if rel_str in EXCLUDED_FILES:
        return True
    return any(part in EXCLUDED_DIRS for part in rel.parts)


def collect_files() -> list[Path]:
    files: list[Path] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        if should_skip(path):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name != "AGENTS.md":
            continue
        files.append(path)
    return files


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return None


def first_paragraph(text: str) -> str | None:
    lines = [line.strip() for line in text.splitlines()]
    paragraph: list[str] = []
    for line in lines:
        if not line:
            if paragraph:
                break
            continue
        if line.startswith("#"):
            continue
        paragraph.append(line)
        if len(" ".join(paragraph)) >= 180:
            break
    if not paragraph:
        return None
    return " ".join(paragraph)


def extract_code_markers(text: str, suffix: str) -> list[str]:
    markers: list[str] = []
    patterns = [
        r"^\s*(struct|class|enum|protocol)\s+[A-Za-z_][A-Za-z0-9_]*",
        r"^\s*(func)\s+[A-Za-z_][A-Za-z0-9_]*",
        r"^\s*(def|class)\s+[A-Za-z_][A-Za-z0-9_]*",
    ]
    if suffix in {".md", ".yml", ".yaml", ".json", ".toml", ".xml"}:
        return markers
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if any(re.match(pattern, stripped) for pattern in patterns):
            markers.append(stripped)
        if len(markers) == 5:
            break
    return markers


def summarize(path: Path) -> str:
    text = read_text(path)
    heading = first_heading(text)
    paragraph = first_paragraph(text)
    markers = extract_code_markers(text, path.suffix.lower())
    parts: list[str] = []
    if heading:
        parts.append(f"Título: {heading}.")
    if paragraph:
        parts.append(paragraph.rstrip(".") + ".")
    if markers:
        parts.append("Elementos detectados: " + "; ".join(f"`{marker}`" for marker in markers) + ".")
    if not parts:
        parts.append("Archivo operativo sin resumen textual relevante.")
    return " ".join(parts)


def grouped(files: list[Path]) -> dict[str, list[Path]]:
    buckets: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        rel = path.relative_to(ROOT)
        top = rel.parts[0] if len(rel.parts) > 1 else ""
        buckets[top].append(path)
    return buckets


def tree(files: list[Path]) -> str:
    lines = []
    for path in files:
        lines.append(f"- `{path.relative_to(ROOT).as_posix()}`")
    return "\n".join(lines)


def build_document() -> str:
    files = collect_files()
    buckets = grouped(files)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    commit = git_commit()

    lines: list[str] = []
    lines.append("# Project Documentation")
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- Generated at: `{now}`")
    lines.append(f"- Source commit: `{commit}`")
    lines.append(f"- Consolidated file count: `{len(files)}`")
    lines.append("")
    lines.append("## Repository Structure")
    lines.append("")
    lines.append(tree(files))

    for section in SECTION_ORDER:
        if section not in buckets:
            continue
        title = "Root Files" if section == "" else section.replace("-", " ").title()
        lines.append("")
        lines.append(f"## {title}")
        lines.append("")
        for path in buckets[section]:
            rel = path.relative_to(ROOT).as_posix()
            lines.append(f"### `{rel}`")
            lines.append("")
            lines.append(summarize(path))
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_document(), encoding="utf-8")


if __name__ == "__main__":
    main()
