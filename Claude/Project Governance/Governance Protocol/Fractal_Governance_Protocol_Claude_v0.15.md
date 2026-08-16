# Fractal Governance Protocol — Claude Series v0.15

**Topic:** OQ-3 resolved — the event log's physical layout: one append-only file, an advisory 50,000-event volume tripwire, and roll-by-ceremony (C-055); interval-based partition brackets eliminated as a standing specification and preserved as a latent, on-need capability
**Status:** Ratified (2026-08-13 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-13 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.14

---

## 1. Context

OQ-3 had stood open since C-023 (v0.4, 2026-08-07): the event log was specified as "partitioned (interval TBD — monthly is illustrative, not fixed)," with the decision deferred until real volume data existed. Max had asked that the discussion be informed by observation, and the store now offered it: one bootstrap-heavy month — the heaviest the project will plausibly ever see by hand, containing the entire corpus minting, facet layer, and route layer — produced **159 events in a 46 KB file (~290 bytes/event)**. Meanwhile the illustrative monthly bracket had quietly leaked into practice: `mint.py` derived its bucket from the current month, and the store's only partition was named `2026-08.jsonl`. This conversation was opened by Max directly on OQ-3, from the standing agenda's G offers (C-031: expected, not steered).

## 2. Questions Investigated

- What is a "reasonable volume" per partition, grounded in the store's observed event size?
- Is any partition bracket friction-free under multi-writer operation (C-049), or do some schemes re-import the coordination problem?
- Is the monthly partition necessary at all — or is it a specification that can be eliminated per the FRACTAL credo?
- Does a single file with a high cap scale — what happens if the cap is one day reached routinely?

## 3. Human Input (Max)

Max drove the resolution in three steps. First: assuming brackets hold no friction, simply separate by a reasonable volume size — asking for the number, since he had no basis for it. Second, the structuring challenge: **why is the monthly partition even necessary?** Divide by events and hard-cap "with an obnoxiously high limit" — while explicitly offering to commit to monthly if it was the leanest version for a reason he didn't yet see. Third, the scalability probe: if the cap were one day reached "now and then," the design should still yield brackets — *but only if necessary*. He then ratified the resolution as outlined ("yes").

## 4. AI Input (Claude)

- Grounded the discussion in the store first: ~290 B/event empirically; monthly partitioning over-fine by roughly an order of magnitude at any plausible hand pace; the tools inspected — `verify.py` fully partition-agnostic (globs `_events/*.jsonl`), the monthly scheme living in exactly one `mint.py` line marked "partition interval TBD (OQ-3)."
- Initially argued that only *time-derived* brackets are friction-free — automatic volume-based rolling is writer-dependent and diverges across unmerged clones. Then, under Max's challenge, conceded the sharper point: that objection applies only to *automatic* rolling. A cap that in practice never fires, cured by a **deliberate ceremony on merged state** when it does, is both leaner and equally safe — and the more fractal answer, since partitioning was a specification to eliminate.
- Confirmed scalability as a property of the mechanism, not the number: the design degrades into partitioning exactly on demand (first roll → routine rolls = observed friction → automate per C-008, decided then from real data); closed partitions are immutable and readers partition-agnostic, so no future scheme ever requires migration.
- Proposed the concrete numbers: tripwire at 50,000 events (~15 MB; ~25 years away at bootstrap-month pace), advisory (WARN, never a failure), checked by the ritual that already runs at every store-touching commit so the cap lives in a tool, not only in prose.

## 5. Jointly Derived Conclusions

1. **Eliminating the specification *is* the resolution.** OQ-3 asked "which interval?"; the answer is "no interval." Brackets exist in the design as a latent capability that materializes per observed need — the C-021/C-008 pattern applied to the log's own physique.
2. **Ceremony is what makes a volume cap multi-writer safe.** Writer-local automatic rolling re-imports the divergence problem C-049 retired; a roll that is one recorded commit on merged state cannot diverge. The C-049 root ceremony supplied the pattern.
3. **A tripwire nobody checks is prose, not a mechanism.** The cap lives in `verify.py`, which already runs at every C-037 boundary — noticed by ritual, at zero added workflow cost.
4. **The number isn't what scales — the mechanism is.** 50,000 is a recorded constant (one-line edit + register note to change), not architecture.

## 6. Current Decisions

- **C-055 — Event-log physical layout: one file, tripwire, roll-by-ceremony (Working Decision, executed).** The event log is **one append-only file** — a single active partition (`_events/part-0001.jsonl`). `verify.py` carries an advisory **volume tripwire: 50,000 events per file** — a WARN, never a failure. A new partition opens **only through the roll ceremony**: close the active file, open the next (`part-0002.jsonl`, …), in one recorded commit on *merged* state — never an automatic per-writer act. Closed partitions are immutable; all readers consume `_events/*.jsonl` and are partition-agnostic, so any future bracket rule applies from its commit forward with no migration. If rolls ever become routine (machine-rate writing), that observed friction is the C-008 trigger to automate — decided then, from real volume data. **Resolves OQ-3.** Executed alongside: `mint.py` appends to the single active partition (lexically last `_events/*.jsonl`) instead of deriving a monthly bucket; the bootstrap partition `2026-08.jsonl` renamed `part-0001.jsonl` (git-tracked rename; log lines untouched); Schema reissued as **v0.5**; monthly brackets retired unchosen.

- **Ratification record (2026-08-13, in-conversation per C-033).** The resolution followed Max's own structuring calls (no standing brackets; obnoxiously high cap; brackets later only if necessary), was laid out in full — schema note, register disposition, protocol entry, two tool edits, verify-green commit — and Max ratified it explicitly ("yes").

## 7. Alternatives Considered

- **Keep monthly (status quo).** Defensible — the cost of over-fine partitions is only file count. Rejected: it fixes a bracket no observed problem requires, and the "monthly" in practice was an illustration that leaked, not a decision.
- **Time-derived brackets sized by volume (yearly, guardrail to refine).** Claude's initial proposal; friction-free but not necessary. Rejected as less lean than no brackets at all: it keeps a standing scheme where a latent capability suffices.
- **Automatic volume-based rolling.** Rejected: writer-dependent roll points diverge across unmerged clones — re-imports the C-049 problem.
- **No tripwire (cap in prose only).** Rejected: a cap no tool checks won't be noticed at the moment it matters; the WARN rides an existing ritual for free.

## 8. Assumptions

- Hand-writing pace stays within orders of magnitude of the observed bootstrap month; the tripwire fires, if ever, in the machine-writing era (index/run layer appending provenance edges), at which point automation of the roll is on the table per C-008.
- The rename of the bootstrap partition is navigation, not identity (C-022 spirit): log lines, event ids and hashes are untouched; git tracks the rename.
- `verify.py`'s tripwire constant is a recorded convention; changing it is an ordinary recorded edit, not a schema migration.

## 9. Consequences

- **Schema → v0.5** (new canonical file; §4.1 physical layout rewritten; §6 OQ-3 moved to resolved; §7 C-055 captured; DOC node re-pathed + revised).
- **`mint.py`** — bucket derivation replaced by single-active-partition append (lexically last `_events/*.jsonl`). **`verify.py`** — per-file event counts + the 50,000-event advisory tripwire.
- **`_events/2026-08.jsonl` → `_events/part-0001.jsonl`** (git-tracked rename; content append-only as ever).
- Decision Register → **v0.11**: C-055; OQ-3 resolved. Rule Overview → **v0.9**: event-log row. Store README — layout + rules-in-force updated to C-055; spec pointer → v0.5.
- Local Context → **v0.16** (OQ-3 leaves the G offers; agenda updated); Agenda Board regenerated file-first (C-048) and republished.
- Knowledge Graph Store: **+1 node (45), +7 events (166)** — one DOC mint (this protocol) with route alias + two placements; three living-doc revisions (Schema re-pathed to v0.5, Register, Rule Overview). Committed per C-037; `verify.py` green before the store commit (C-050 duty).

## 10. Decision Ledger Changes

Added **C-055** (event-log physical layout — one file, advisory tripwire, roll-by-ceremony; **OQ-3 resolved**). No new OQs open.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None new. Standing items carry unchanged: OQ-4, OQ-6, OQ-9, OQ-10, OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-21; C-038 acceptance test unexercised; the WS forge waits on observed need (Architecture State §4).

## 12. Next Line of Research

The G offers shrink by one: OQ-4 (genuine transition — a candidate stands observed), OQ-21 (off-site host) and the C-038 acceptance test remain, alongside the H roadmap (KG index; entry-point interface tier; the repo-resident skill → plugin). Nothing is force-queued (C-031).

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.15 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.15 |
| Status | Ratified (2026-08-13, in-conversation per C-033) |
| Domain | Project Governance — Knowledge Graph / Event-Log Layout |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-13, this protocol) |
| Date | 2026-08-13 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.14 |
| Related Documents | Fractal Node & Event Schema v0.5; Fractal Decision Register v0.11; Fractal Rule Overview v0.9; Knowledge Graph Store README; `mint.py` / `verify.py` (C-050 tools) |
| Revision Trigger | Any change to C-055 — the single-file layout, the tripwire constant, or the roll ceremony |
| Document ID | DOC-01KZXX37YRFPT2Q81VTT0K9X4B |
