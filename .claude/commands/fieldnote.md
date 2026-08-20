---
description: Capture an off-topic observation into the RAM buffer — extraction, read-back, Max's ratification, then back to the work — C-094/C-121 (usage /fieldnote <what happened>)
---
Capture a field observation per C-094 under the C-121 RAM model: **$ARGUMENTS**

**What this command means (the off-topic jump, Format v0.2 §5):** this is a **normal chat turn, never an interrupt** — Max is deliberately jumping off the current task's topic, and the command itself tells you why: *capture this, don't re-aim the work.* Park the running task's thread untouched; the fieldnote's content is **never** instruction for the work in flight. There is no target word — the whole argument is the raw report.

**The capture loop (the write gate is Max's ratification):**

1. **Extract.** Derive clear, structured information from the raw report: what happened, what it implies, where it might belong. Your extraction routine is yours to develop — only this contract is fixed.
2. **Read back.** Present to Max: the raw report exactly as it will land in the block, your derived reading, and a **first categorisation proposal** (non-binding, best-effort — *no category fitting is explicitly fine*; work-down decides later).
3. **On his ratification — and only then** — run `python3 "Claude/Knowledge Graph Store/fieldnote.py" --kind <friction|green|vision|question> <report text>` when Max stated the class, or without the flag when he didn't (the tool defaults to `capture`). **`--kind` is recognized only as the first argument** — a trailing flag is refused, never silently joined into the block (S6-4.2). The tool appends the **machine-format block** (Fractal Fieldnote Format v0.2 — six keys, verbatim raw report, content-immutable) to the buffer (`Site/Fieldnotes.md`) and maintains the id high-water line. **If the tool errors: report its error and stop — no fallback, nothing written.** Then add the ratified derived reading as the **judgment layer** beneath the block (never inside it).
4. **Return.** Confirm in **one line** — id + the tool's depth reading (it prints the C-121 **YELLOW pressure advisory** when the buffer stands over budget; relay it, never suppress it — but a full buffer still captures: the plug is a warning, never a gate). Then return immediately to the parked work. Minimal disturbance is the point.

**The buffer is RAM (Format v0.2 §4):** entries are worked off soon — solved by **dissolving into the project** (a Register row, a document reissue, a concept, a transfer), the absorbing artifact citing the `FN-` id, the entry then deleted whole. Solving is a governance act on Max's word; this command only captures. **Do not commit** — the entry rides the session's next close.

---
*Stamped-procedure projection (C-035 class): compresses Fractal_Fieldnote_Format_v0.2 §5 (the capture contract) — sources: the v0.2 standard + the C-121 row in the Decision Register (Max's design of record, 2026-08-18: the RAM buffer, the single-word command as intent marker, the extraction + read-back + ratification gate, the pressure plug). Re-projected 2026-08-18 (C-121 — the v0.1 target roster retired; deterministic routing ended with the lanes; ratification became the write gate). Refresh triggers: a Format reissue, a C-094/C-121 amendment, a `fieldnote.py` behavior change, a buffer relocation.*
