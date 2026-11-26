"""Painfully honest out-of-office auto-reply.

Writes a single sentence to entry.txt. The line admits the real state
of the sender's inbox on departure, stays courteous about the wait,
and ends on a dry, quotable image of working through the backlog.
"""

import os
from pathlib import Path

REPLY = (
    "I'm away until Monday, and to be candid I left 312 unread emails "
    "behind me, so thank you for your patience while I answer them "
    "in the order I can face them."
)


def main() -> None:
    # The gate allows 1-200 characters and a single sentence only.
    cleaned = REPLY.strip()
    assert 1 <= len(cleaned) <= 200, "reply must be 1-200 characters"
    assert cleaned.count(".") == 1 and cleaned.endswith("."), (
        "reply must be exactly one sentence"
    )
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.txt"
    target.write_text(cleaned, encoding="utf-8")


if __name__ == "__main__":
    main()
