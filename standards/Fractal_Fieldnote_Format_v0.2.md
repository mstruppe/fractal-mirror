# Fractal Fieldnote Format v0.2

> **CANONICAL SPECIFICATION — the RAM-buffer capture format for field observations (C-094, redesigned per C-121).** Versioned artifact (C-040 class): this version is frozen at issue; any substantive change is a new version/file. v0.1's lane model (per-subject ledgers, deterministic target routing) is superseded: **the fieldnote is temporary memory** — one buffer, no routing at capture, categorisation deferred to work-down. The reference implementation is `Claude/Knowledge Graph Store/fieldnote.py` (capture + depth + parse); where tool and this document disagree, this document wins.

**Version:** 0.2 · **Status:** Ratified (2026-08-18, C-121 — Max's design: *"the fieldnote should be a temporary memory, almost like RAM"*; protocol at this session's close) · **Domain:** GOV · **Author:** Claude · **Parent:** Fractal Conversation Settings (C-094 — field testing is the standard proving process) · **Supersedes:** Fractal_Fieldnote_Format_v0.1 (retained as history, its own DOC identity per C-061) · **Document ID:** DOC-01M0BJ8GVJ0SBZJV48C2ZPY28D (minted at the ratifying close via `close.py --create`; stamped by the paired revise)

---

## 1 · What a fieldnote is

A **fieldnote is RAM**: an observation captured mid-task into one instance-wide **buffer**, held there deliberately temporarily, and **worked off soon**. Nothing gets lost — but nothing *lives* there either: a fieldnote is solved by **dissolving into the project** (a decision, a rule, a document update, a concept, a transfer), at which point it leaves the buffer. The buffer's depth is therefore a pressure signal, not an archive's size.

An **entry** is a fenced code block with the info string `fieldnote`, appended to the buffer file. The block is the **fact layer**: machine-written, machine-parsable, content-immutable — a correction is a new entry naming the corrected id. Everything outside the blocks (the derived reading, categorisation, work-down notes) is the **judgment layer**: human/AI-written, never parsed (the C-073 division). New in v0.2: blocks are **content-immutable but presence-transient** — solving deletes the whole block from the buffer (§4); the frozen trace is the absorbing artifact's citation plus git history.

## 2 · The block grammar

````
```fieldnote
id: FN-0011
ts: 2026-08-18T22:10:05+0200
author: Max Struppe <max.struppe@gmail.com>
instance: FRACTAL
kind: capture
report:
  the verbatim report text, exactly as given,
  each line indented by exactly two spaces.

  blank lines inside the report are allowed.
```
````

Rules, in order (unchanged from v0.1 except where marked):

1. **Fences.** Opening fence exactly `` ```fieldnote ``; closing fence exactly `` ``` ``. Nothing else on either line.
2. **Keys — six, fixed order (v0.2 change):** `id`, `ts`, `author`, `instance`, `kind`, `report`. The v0.1 `target` key is retired — there is nothing to route. Unknown/missing keys or changed order make a block invalid; **strictness is the interface**.
3. **`id`** — `FN-` + four-digit zero-padded number, unique and strictly ascending per buffer, **never reused**. Because solving deletes blocks, ascension cannot be recomputed from surviving blocks alone: the buffer header's **Id high-water line** (§4) is the machine fact; the tool writes `max(high-water, highest surviving block) + 1` and updates the line at every capture.
4. **`ts`** — ISO-8601 local time with numeric UTC offset, written by the capture tool's clock, never by hand.
5. **`author`** — `Name <email>` from `git config` at capture time (C-037 attribution); capture refuses when unset.
6. **`instance`** — the capturing instance's declared name, read from the config file (`fieldnote_roster.json` beside the tool — the historic filename kept, its content collapsed to the v0.2 single-buffer shape, §6).
7. **`kind`** — one of `friction` · `green` · `vision` · `question` · `capture` (default `capture`); the tool writes what the reporter states, never invents. Parsers MUST accept unknown kinds (forward compatibility).
8. **`report`** — bare `report:` line, then the **verbatim raw report**, two-space indented, blank lines allowed, ends at the closing fence; fence-opening lines refused at capture. The raw wording is the datum (v0.1 doctrine unchanged) — the *derived* reading lives in the judgment layer (§5).

## 3 · The parse contract (the intake half)

`python3 fieldnote.py parse <file> [<file>…]` — unchanged in shape: whole-or-nothing, JSON array on stdout when every block is valid, every error on stderr and exit 1 otherwise. Two v0.2 provisions:

- **Both grammars are accepted at intake.** A block carrying `target:` in position five is validated against the v0.1 seven-key grammar (frozen ledgers, v0.1-kernel children send these); a block without it against §2. Emitted objects carry `"target"` only when the block did. The *writer* emits v0.2 blocks only — acceptance is for intake, never an excuse to write the old shape.
- Per-file id checks (uniqueness, ascension) apply to surviving blocks; gaps are legal (deletion, §4).

## 4 · The buffer (RAM semantics)

One buffer file per instance — the mother's is `Site/Fieldnotes.md`; a newborn's is `FIELDNOTES.md` (parameter 7's file, GENESIS §2). The buffer's header carries two machine-read lines:

- **`**Budget:** N entries`** — the pressure threshold. **Provisional at 10, calibration-pending (C-121):** the right number is found by doing (C-094); when the warning first fires wrong — too early or too late — that observation is itself a fieldnote, and the number moves by ordinary edit.
- **`**Id high-water:** FN-NNNN`** — the highest id ever issued (§2 rule 3). Tool-maintained; hand-edit never.

**Depth** = surviving `fieldnote` blocks + unchecked work-down rows (lines beginning `- [ ]`, the migrated-pointer form). **The pressure plug:** when a capture makes depth exceed the budget — and whenever depth stands above it at `/fractal` orientation or the close walk — a **YELLOW advisory** fires: *work the buffer down soon*. Three properties, ratified: **warning, never a gate** (a full buffer still captures — refusing capture would cost the quality the mechanism protects); **advisory, never a red block** (the C-110 gauge class, not the C-050/C-060 checker class); **silent below budget** (no standing overhead).

**Solving.** A fieldnote is solved when it **dissolves into the project**: a Register row, a document reissue, a concept foundation, a transfer to its jurisdiction — any durable home. The dissolving artifact **cites the id** (`FN-NNNN`); then the entry — block and its judgment prose, or the `- [ ]` row — is **deleted whole** from the buffer. The citation plus git history is the full trace; ids are never reused (§2 rule 3). Solving is a governance act of the governing surface, on Max's word per item or slate.

## 5 · The capture contract (conduct half — the two-step process)

**Step 1 — capture, at the moment it pops up:**

1. **The off-topic jump.** `/fieldnote <what happened>` is a **normal chat turn, never an interrupt** of the agent's running process. The command itself is the intent marker: *this is deliberately off-topic — capture it, don't re-aim the work.* The agent parks the current task's thread untouched; the fieldnote's content is never treated as instruction for the task in flight.
2. **Extraction.** The agent derives clear, structured information from the raw report — what happened, what it implies, where it might belong. The extraction routine is deliberately unspecified: each agent develops its own; only this contract is fixed.
3. **Read-back and ratification — the write gate.** The agent reads the derived entry back (the raw report that will land in the block, the derived reading, and a **first categorisation proposal** — non-binding, best-effort; *no category fitting is explicitly fine*, work-down handles it). **The user's ratification releases the write**; the tool then appends the block (raw report verbatim) and the agent adds the ratified derived reading as the judgment layer beneath it.
4. **Return.** One-line confirmation (id + depth, plus the YELLOW if standing), then straight back to the parked work. Minimal disturbance is the point.

**Step 2 — work-down, soon:** at any session's natural pause — or on the pressure plug's YELLOW — buffer items are worked: each dissolves (§4) or is knowingly kept waiting on a named trigger. Categorisation from step 1 is a hint, never a rail.

## 6 · Collection and the config (why this stays the whole pipeline)

The **config file** `fieldnote_roster.json` (beside the tool; historic name kept, C-012 stable-filename spirit) collapses to: `{"instance": "<Name>", "buffer": "<path>"}` — the single buffer-path parameter plus the instance's declared name. The v0.1 target roster is retired; genesis writes the v0.2 shape.

Collection is unchanged (v0.1 §4): the buffer file **travels by any channel — a sent file is enough**; who/when/what ride inside the entries. The mother validates with `parse` (which accepts a v0.1 child's ledger unchanged, §3) and ingests at a phase boundary (C-094: fixes land in the generator, never the field instance). The C-096 observation window remains an optional richer channel, never a prerequisite.

---

**Refresh triggers (for the series, not this frozen version):** a parse-breaking need observed in the field (new version); the pressure plug's first wrong firing (budget recalibration is an ordinary edit, not a reissue — only a *mechanism* change reissues); a child intake contradicting a rule here.
**Sources:** Decision Register (C-121 — the RAM redesign, Max's design of record; C-094, C-073, C-037, C-062); Fractal_Fieldnote_Format_v0.1 (the superseded lane model — grammar, attribution, and collection doctrine carried forward); the three frozen lane ledgers (`Site/Fieldnotes_2026-08-15_First-Shipping-Run.md`, `…_2026-08-16_Publishing.md`, `…_2026-08-16_General.md` — the migration's source, freeze notes inside).
**Revision history:** v0.2 (2026-08-18) the RAM redesign (C-121): one buffer, target retired (six-key grammar), presence-transient blocks (solving = dissolution + whole-block deletion, id high-water line), the pressure plug (budget line, YELLOW advisory, capture never blocked), the two-step capture contract (off-topic jump as intent marker; extraction + read-back + ratification as the write gate; categorisation proposal non-binding), dual-grammar intake. · v0.1 (2026-08-16) first issue — the lane model: seven-key grammar, deterministic target routing, whole-or-nothing intake, the sent-file collection floor.
