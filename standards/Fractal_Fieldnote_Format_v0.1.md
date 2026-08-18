# Fractal Fieldnote Format v0.1

> **CANONICAL SPECIFICATION — the machine-parsable entry format for field observations (C-094).** Versioned artifact (C-040 class): this version is frozen at issue; any substantive change is a new version/file. The format is the whole interface of the collection pipeline (fieldnotes entry 39): a ledger file that travels by any channel — a sent file is enough — because who/when/what ride inside the entries, deterministically. The reference implementation is `Claude/Knowledge Graph Store/fieldnote.py` (capture + parse); where tool and this document disagree, this document wins.

**Version:** 0.1 · **Status:** Ratified (2026-08-16, per Protocol v0.45 — C-100) · **Domain:** GOV · **Author:** Claude · **Parent:** Fractal Conversation Settings (C-094 — field testing is the standard proving process) · **Document ID:** DOC-01M05JPXQ5SVNDNE0YJMTF6YFW (minted 2026-08-16 via `close.py --create`; stamped by the post-mint revise)

---

## 1 · What an entry is

A **fieldnote entry** is a fenced code block with the info string `fieldnote`, appended to a markdown ledger file. The block is the **fact layer**: machine-written, machine-parsable, and **immutable once written** — a correction is a new entry whose report names the corrected id. Everything outside the blocks (titles, cures, guide implications, prose) is the **judgment layer**: optional, human/AI-written, never parsed (the C-073 division — routing and attribution are machine facts; interpretation stays judgment).

## 2 · The block grammar

````
```fieldnote
id: FN-0007
ts: 2026-08-16T14:22:31+0200
author: Max Struppe <max.struppe@gmail.com>
instance: KNet
target: self
kind: friction
report:
  the verbatim report text, exactly as given,
  each line indented by exactly two spaces.

  blank lines inside the report are allowed.
```
````

Rules, in order:

1. **Fences.** The opening fence is a line reading exactly `` ```fieldnote ``; the closing fence a line reading exactly `` ``` ``. Nothing else on either line.
2. **Keys.** Exactly seven keys, in this fixed order: `id`, `ts`, `author`, `instance`, `target`, `kind`, `report`. Each on its own line as `key: value` (single space after the colon). Unknown or missing keys, or a changed order, make the block invalid — **strictness is the interface**; loosening it is a new version, never a tolerant parser.
3. **`id`** — `FN-` plus a four-digit zero-padded sequence number. Ids are unique and strictly ascending **per ledger file**. The sequence counts machine blocks only; any prose numbering a ledger also carries is judgment-layer and independent.
4. **`ts`** — ISO-8601 local time with numeric UTC offset: `YYYY-MM-DDTHH:MM:SS±HHMM`. Written by the capture tool's clock, never by hand.
5. **`author`** — `Name <email>`, read from `git config user.name` / `user.email` at capture time: the machine identity fact (C-037's attribution doctrine at the capture layer). Capture refuses to run when either is unset.
6. **`instance`** — the capturing instance's declared name, read from the roster file (`fieldnote_roster.json` beside the tool), never typed per capture.
7. **`target`** — the resolved roster target word (Max's determinism ruling of record, 2026-08-16: a missing or unknown target is a hard error and nothing is written).
8. **`kind`** — one of `friction` · `green` · `vision` · `question` · `capture`. Classification is judgment: the tool writes what the reporter states (`--kind`) and defaults to `capture` (unclassified) — it never invents one. Parsers MUST accept unknown kind values (forward compatibility) and SHOULD treat them as `capture`.
9. **`report`** — the key line is exactly `report:` (no inline value). The verbatim report follows: every line indented by exactly two spaces, blank lines allowed (empty or two-space). The report ends at the closing fence. A report line whose stripped form begins with a backtick fence is refused at capture (it cannot round-trip).

## 3 · The parse contract (the intake half)

`python3 fieldnote.py parse <file> [<file>…]`:

- Extracts every `fieldnote` fence from each file; validates every block against §2, including per-file id uniqueness and ascension.
- **All blocks valid:** exit 0; a JSON array on stdout — one object per entry: `{"file", "id", "ts", "author", "instance", "target", "kind", "report"}` (report with indentation stripped, lines joined by `\n`), in file-then-sequence order. A summary line on stderr.
- **Any block invalid:** exit 1; every error on stderr with file and line; **no partial JSON on stdout**. An intake either succeeds whole or fails loudly — a silently dropped entry would break the deterministic who/when/what claim the pipeline exists to make.
- Files are UTF-8. Content outside fenced `fieldnote` blocks is ignored (the judgment layer, and any legacy prose entries).

## 4 · Collection (why this is the whole pipeline)

A tester's instance captures through `/fieldnote` (or the plain word on clients without a slash menu) into its own ledger — genesis ships the door (`FIELDNOTES.md`, parameter 7's file). To report back, **the tester sends the ledger file — any channel, no hosting, no remote, no phone-home** (the constitution model forbids runtime coupling; collection runs by pull/send, with the consent that sending is). The mother validates with `parse` and ingests at a phase boundary (C-094: fixes land in the generator, never the field instance). The C-096 observation window remains an optional richer channel, never a prerequisite.

---

**Refresh triggers (for the series, not this frozen version):** a parse-breaking need observed in the field (new version); the friends-beta's first real intake contradicting a rule here.
**Sources:** Decision Register (C-094, C-073, C-037, C-062); Site/Fieldnotes_2026-08-15_First-Shipping-Run.md entries 39 + 41 (the sent-file collection floor; the determinism ruling); Protocol v0.44 §1.3 (the testing pipeline's enumeration).
**Revision history:** v0.1 (2026-08-16) first issue — the flip-preparation session: the entry grammar (seven fixed keys, fenced blocks, immutable fact layer), the parse contract (whole-or-nothing intake), and the sent-file collection floor.
