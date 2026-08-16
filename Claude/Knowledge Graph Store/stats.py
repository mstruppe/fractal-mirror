#!/usr/bin/env python3

import json
from pathlib import Path


def main() -> None:
    event_dir = Path(__file__).with_name("_events")
    event_count = 0
    entities = set()
    codes = set()

    for event_path in sorted(event_dir.glob("*.jsonl")):
        with event_path.open(encoding="utf-8") as event_file:
            for line in event_file:
                if not line.strip():
                    continue

                event_count += 1
                event = json.loads(line)
                if event.get("ev") in {"mint", "create"}:
                    entities.add(event["subject"])
                if event.get("ev") == "mint":
                    codes.add(event["code"])

    roots = sorted(code for code in codes if "." not in code)
    print(
        f"{len(entities)} nodes / {event_count} events · "
        f"roots: {','.join(roots)} · {len(codes)} codes"
    )


if __name__ == "__main__":
    main()
