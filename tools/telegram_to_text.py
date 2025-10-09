#!/usr/bin/env python3
"""Convert Telegram JSON exports into plain-text transcripts."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterator, List, Sequence

WHITESPACE_RE = re.compile(r"\s+")

Message = dict[str, object]


def _iter_part_files(path: Path) -> List[Path]:
    if path.is_file():
        return [path]

    def sort_key(p: Path):
        match = re.search(r"(\d+)$", p.stem)
        return int(match.group()) if match else p.stem

    files = sorted(path.glob("input_part*.json"), key=sort_key)
    if not files:
        raise FileNotFoundError(
            f"No Telegram export parts found in {path}. Expected files named input_partXYZ.json."
        )
    return files


def load_messages(path: Path) -> Sequence[Message]:
    """Load Telegram messages from a single file or a directory of export parts."""

    part_files = _iter_part_files(path)
    raw_bytes = b"".join(p.read_bytes() for p in part_files)
    export = json.loads(raw_bytes.decode("utf-8"), strict=False)
    messages = export.get("messages", [])
    if not isinstance(messages, list):
        raise TypeError("Expected 'messages' to be a list in the Telegram export")
    return messages


def _flatten_text(message: Message) -> str:
    text = message.get("text")
    if isinstance(text, str):
        return WHITESPACE_RE.sub(" ", text).strip()

    if isinstance(text, list):
        parts: List[str] = []
        for chunk in text:
            if isinstance(chunk, str):
                parts.append(chunk)
            elif isinstance(chunk, dict):
                value = chunk.get("text")
                if isinstance(value, str):
                    parts.append(value)
        combined = "".join(parts)
        return WHITESPACE_RE.sub(" ", combined).strip()

    return ""


def _describe_service(message: Message) -> str:
    actor = message.get("actor") or message.get("from") or "Unknown"
    action = message.get("action", "performed an action")
    details: List[str] = []
    title = message.get("title")
    if isinstance(title, str) and title:
        details.append(f"title='{title}'")
    members = message.get("members")
    if isinstance(members, list) and members:
        members_str = ", ".join(str(m) for m in members)
        details.append(f"members=[{members_str}]")
    return f"[SERVICE] {actor} {action}{' (' + '; '.join(details) + ')' if details else ''}"


def _format_message(message: Message, include_service: bool) -> str | None:
    msg_type = message.get("type")
    timestamp = str(message.get("date", "Unknown time"))

    if msg_type == "service":
        return _describe_service(message) if include_service else None

    sender = message.get("from") or message.get("actor") or "Unknown"
    body = _flatten_text(message)

    if not body:
        for key in ("media_type", "photo", "file", "mime_type"):
            value = message.get(key)
            if isinstance(value, str) and value:
                body = f"<{value}>"
                break

    if not body:
        return None

    return f"[{timestamp}] {sender}: {body}"


def iter_transcript_lines(
    messages: Sequence[Message],
    include_service: bool,
    limit: int | None = None,
) -> Iterator[str]:
    count = 0
    for message in messages:
        formatted = _format_message(message, include_service=include_service)
        if formatted:
            yield formatted
            count += 1
            if limit is not None and count >= limit:
                break


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert Telegram JSON exports into plain-text transcripts.")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/raw/telegram_exports/vesc_help_group"),
        help="Path to an export directory or a single Telegram JSON part.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write the transcript. Defaults to stdout when omitted.",
    )
    parser.add_argument(
        "--include-service",
        action="store_true",
        help="Include Telegram service messages such as joins and title changes.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit the number of transcript lines that are emitted.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    messages = load_messages(args.input)
    lines = iter_transcript_lines(
        messages,
        include_service=args.include_service,
        limit=args.limit,
    )

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("w", encoding="utf-8") as fh:
            for line in lines:
                fh.write(line)
                fh.write("\n")
    else:
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()
