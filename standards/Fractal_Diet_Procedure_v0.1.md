# Fractal Diet Procedure v0.1

> **CANONICAL SPECIFICATION — the working-set eviction procedure (the C-095 discipline made a standard), distilled from history per C-108.** Versioned artifact (C-040 class): this version is frozen at issue; any substantive change is a new version/file. Nothing here is invented: every rule below is extracted from the two executed instances of record — the **diet flight** (DF1, 2026-08-17: the weight measurement and the 14-proposal slate) and the **compaction-behaviour test** (CB1, 2026-08-17: the two-arm blind simulation that gated adoption) — and the decisions that governed them (C-095, C-110). A diet is a **procedure** in the C-108 taxonomy: a pluggable component an ultracode flight composes, and that also runs standalone.

**Version:** 0.1 · **Status:** Ratified (2026-08-17, in-conversation per C-033 — Max: "perfect the draft is ratified", after the DP1 adversarial verification flight — 22 findings, all cured pre-ratification) · **Reviewed By:** Max (2026-08-17, per C-033) · **Domain:** GOV · **Author:** Claude · **Date:** 2026-08-17 · **Provenance:** commissioned by Max, eighteenth Code session — *"I want diet process among the ultracode flight and scan flight procedures"* (verbatim of the live commission; frozen home: the eighteenth-session Governance Protocol at this session's close — until issued, a forward reference, the Flight-Protocol attestation pattern) — a standards-and-skills registry entry beside `Fractal_Ultracode_Flight_Protocol_v0.1` and `Fractal_Scan_Procedure_v0.1` (C-108, beta-0.5 seed; the commissioning fact on record: the C-110 banking clause) · **Document ID:** DOC-01M080J6ZXF5J33EFH28TZ7NF8 (minted 2026-08-17 via `close.py --create`; stamped by the post-mint revise)

---

## 1 · What a diet is

A governed FRACTAL instance has two tiers: the **frozen record** (protocols, flight records, dated packages — append-only, complete, never dieted) and the **living tier** — the working set an agent reads *without a retrieval hop*. Living documents accrete: histories re-narrate, ledger rows annotate in place, one decision re-tells itself across surfaces (the DF1 measurement: one register 19 KB → 200 KB in five days; +460 words/day in a single Sources paragraph).

A **diet** is the standardized eviction pass: cold entries in the working set are compacted down to **pointers into the frozen record**. Nothing is deleted — the trade is *ambient availability* for efficiency (the cache framing of record, C-110: the living tier is a working set over the frozen store; a diet is eviction, never clearing). Its lineage is **C-095** — *remove on observed drag* — promoted from discipline to procedure by the DF1/CB1 pair.

## 2 · The phase doctrine (accretion is the default)

**What C-110 records:** the cache doctrine — the living tier is a working set over the frozen record; FRACTAL clusters information by design; a diet is the callable eviction mechanism, an adaptive trade of ambient context for efficiency whose safety depends on pointer-following reliability, *which matures with the project* (early: rich prose serves interpretation; concrete: lean pointers win). The commissioner's phase question and its answer land verbatim in the eighteenth-session protocol (the doctrine's conversation of record).

**This standard's elaboration of that doctrine — entering by the ratification act (the flight standard's §4.2 pattern for flagged extensions):**

1. **Accretion is the default operating mode at every age.** Rich, clustered prose is the *correct* early form: a young instance's agents need narrative for interpretation, and its retrieval infrastructure (routes, index, stable ids) is not yet mature enough to make pointer-following cheap. This standard's own grammars (§6) bind **evicted rows only**, never fresh writing.
2. **The diet fires on measured drag or commission — never on age, never on a calendar.** The measuring instruments are the **drag gauge** (per-file size deltas, advisory yellow — C-110 group B tool work) and the **advisory word budgets** (a standing rule ratified at C-110, implementation queued as tool work); the budgets' initial values are sized from a mature spine, so a pre-register-system project is unlikely to trip them.
3. **The fact-presence gate (§6) makes premature eviction structurally impossible.** A row whose narration has no frozen home keeps its prose — and a young instance's frozen tier holds almost nothing, so nearly every row is protected. Growth into the pointer form is not a policy switch: it is the gate becoming *satisfiable*, region by region, as closes accumulate the frozen record. Same rules at every phase, different phase behaviour.

## 3 · Commissioning

1. **A diet is commissioned or gauge-triggered, never scheduled.** The instance of record was commissioned (*"test thoroughly if we can put any working process on a diet"* — DF1); the gauge's advisory yellow is a *prompt to propose*, never an authorization to act (C-008).
2. **The diet lands proposals; the commissioner triages.** DF1's slate landed **banked untriaged** by explicit call and was triaged in a later session, group-wise ("Group B as recommended…", C-110) — both the deferred landing and the grouped triage are conformant modes.
3. **Adoption may be gated on behaviour evidence.** The commissioner may hold any eviction group for a **behaviour test** (§7) before adopting — the C-110 Group A hold is the exercised precedent, and CB1 its instrument.

## 4 · The measurement half (the weight-class map)

A diet begins by measuring, mechanically reproducibly — *"every number carries its command"* (DF1 contract):

1. **Per-file growth curves** over dated commits, classed by shape: **superlinear / linear / episodic / flat** (DF1-1 … DF1-4), with the growth **engines** named per file (which section, which ritual appends to it).
2. **Non-findings recorded.** What is demonstrably *not* heavy is stated with the same rigor (DF1: the checklist flat at 12 rows; the adapter flat through six re-projections; the frozen tier's volume is the record by design, not drag).
3. **Findings carry stable ids** in the Register's review-findings ledger grammar (`DF<n>-x` the exercised series, in the flight records' banners and findings); rows enter the ledger with dispositions at the adopting close per C-058. (The instances of record ran ahead of their ledger rows — DF1's dispositions were recorded through the C-110 triage decision; the DF1/CB1 rows and legend entries land at the standard's adopting close, curing the lag.)

## 5 · The mitigation slate (proposal classes)

Mitigations land in four classes, each with its own adoption bar (the DF1 slate's taxonomy, ratified at C-110):

- **Compaction** — evictions under §§6–7 grammar and gates; ordinary adoption, optionally behaviour-gated.
- **Mechanization** — moving append rituals into tools (history rows minted at close, stamp passes, gauge instrumentation); ordinary adoption as tool work. *Exercised exception: a mechanization-slate member that constitutes a new standing rule takes the Structural bar — the word-budgets proposal is the precedent (DF1 flagged it "needs ratification"; C-110 ratified it).*
- **Structural** — new standing rules (the exercised member: the pointer-weight re-telling rule — one normative home carries the full statement, every other living surface ≤ ~40 words + refs; that rule lives at C-110, cited here, never owned here); these **require ratification**, never routine adoption.
- **Acceptance-with-reason** — weight that is the product (the board's content for its audience) or a declared boundary (the judgment half of the close stays manual); recorded, closing the finding.

## 6 · The eviction grammar and the fact-presence gate

The two rules CB1 proved, one per failure mode it caught:

1. **The pointer grammar (CB1-1 — the pointer-stop cure).** Every compacted row names the **concrete record file** holding its narration — never just a series. Index tables open with a standing header, whose text this standard fixes as its implementation of the CB1-1 cure: Index only — each row's narration lives only in the named record; this table answers when/what, never how/why. Evidence of record: rows carrying named-file pointers produced correct pointer-following in every CB1 task that touched them; the one degradation in 24 tasks was a headline row that lacked the flag and was quoted as the answer.
2. **The fact-presence gate (CB1-2 — the row-born-content cure).** Before any row compacts, verify the named target **holds the narration** — fact-presence, never mere file-existence (the file-existence check passed the one genuinely lossy eviction; the adversarial verifier caught it). **Row-born content** — facts born in a living row that no frozen record narrates — must be **relocated into the frozen tier first** (a record that holds the narration — e.g. the pending protocol or the adopting session's record), or the row **keeps its prose: eviction waits, never forces.**
3. **Compacted sections carry a dated provenance note** naming the diet and stating that no disposition changed — the exercised precedent is the C-095 first exercise's header (*"compacted — history lives frozen; this table only points"*); the dated, id-bearing form (*rows compacted \<date\>, the \<id\> diet — no disposition changed*) is this standard's tightening of it, entering by the ratification act. No eviction alters any disposition, norm, status, or version stamp (C-095/C-110, the CB1 build's exercised discipline).

## 7 · The behaviour test (the adoption instrument)

When the commissioner **holds an eviction group for evidence** (the exercised trigger — the C-110 Group A hold, CB1 its instrument; first-of-its-kind status is the recorded reason that hold was placed once, offered as guidance for when to hold, never an automatic gate), the adoption gate is a **two-arm blind simulation** (CB1, the exercised instrument; the simulation procedure — C-108, generalized by C-107's program — applied to the instance's own corpus):

1. **Arms:** heavy (unmodified copy) vs. lean (evictions applied to a scratch copy); canon read-only by construction.
2. **A depth-classed gold battery** — surface / one-hop / deep — targeting the evictions under test, judged against gold (the classed 12-task shape per the CB1 record; the finer battery grammar — evicted-content-only sourcing, per-task living + frozen evidence locations — per CB1's run record `wf_8b27adfc-58a`).
3. **Blind sim agents** (told nothing of the design) orient as fresh sessions and answer; the judge scores **correctness** and **pointer-following** per task per arm; an **adversarial verifier** re-derives load-bearing scores *and independently attacks the losslessness claim* by tracing evicted facts. The double instrument is the exercised shape and the **recommended default wherever a losslessness claim is at stake** (the recorded ground: the CB1-2 discovery was the verifier's, not the judge's); the verification tier remains a declared contract choice per the flight standard §3.
4. **The arm-aware metric (CB1-3):** `pointer_followed` is vacuous in the heavy arm; comparisons bind to the lean arm.
5. **Verdicts per eviction:** the exercised set is adopt and its conditioned variants (*adopt with the grammar fix*, *adopt with the gate amendment*); this standard normalizes the space to `adopt` / `fix_pointer_grammar` / `keep_prose` — the last the fact-presence gate's designed outcome (§6.2), not yet exercised as a verdict. Coverage is stated honestly: an eviction no task exercised is flagged untested (CB1-4).

## 8 · Landing and records

A **flight-flown diet** (both instances of record) lands the **dated canonical record** under `Context Packages/Conversations/` (the flight-record class, C-058 via the flight standard §6.3 — frozen at issue, DOC-minted at first commit), findings to the Register's ledger at the adopting close, proposals to the commissioner's triage. A **standalone compaction** lands through the adopting session's protocol and Register per the C-095 precedent (the first exercise produced no dated record), with the dated record available at the commissioner's call. Read-only on canon throughout the measuring/proposing half; the *execution* of adopted evictions is ordinary governed editing under §6, committed with both checkers green.

## 9 · Relationship to the flight container

Per **C-108** the diet is a **procedure**: it composes into an ultracode flight (both instances of record flew — DF1 as the flight standard's first conformant launch, CB1 as its second) and may also run standalone (a gauge-triggered single-surface compaction needs no multi-agent program). In a flight, the flight standard's commissioning contract governs the container; the diet keeps every duty above.

## 10 · The checker half

Per the Knowledge Network Foundation's rule (§5, welded limit 3: *"a standard without a checker is a norm, not a gate"*; §6: both halves, prose and checker, or it is a recommendation — versioned together, the C-040 coupling pattern), this entry ships **prose-first with the checker's trigger named** (the C-108 registry provision). The checker's two instruments, when built: the **drag gauge** (C-110 tool work) **+ word budgets** (the standing rule ratified at C-110, implementation queued as tool work) in the `check_versions.py` lineage — the measured trigger; and **eviction conformance** (compacted sections carry the provenance note; index tables carry the index-only header; a sampled fact-presence audit of pointer targets). **Trigger: the first diet commissioned after the C-110 tool work lands — no second diet closes without the gauge.**

---

**Refresh triggers (for the series, not this frozen version):** the next diet contradicting a rule here; a change to the C-095 discipline or the C-108 taxonomy; the behaviour test's methodology superseded by the registry's context-fidelity probe (the KNet Q07 candidate, C-108) if the probe's error taxonomy proves the finer instrument.
**Sources:** Decision Register (C-095, C-108, C-110, C-058, C-008, C-040); `Flight_2026-08-17_Diet.md` (DF1 — the measurement half, the slate taxonomy, the banked-untriaged landing); `Flight_2026-08-17_Compaction-Behaviour.md` (CB1 — the grammar, the gate, the behaviour-test instrument, the arm-aware metric); CB1's run record `wf_8b27adfc-58a` (the battery grammar); Fractal_Ultracode_Flight_Protocol_v0.1 (the container; §4.2 the flagged-extension pattern); Fractal_Scan_Procedure_v0.1 (the sibling procedure's format precedent); Fractal_Knowledge_Network_Foundation §5–§6 (the prose+checker rule); the C-110 Register row (the cache doctrine) and the eighteenth-session Governance Protocol landing at this session's close (the commission and the phase question verbatim — a forward reference until issued).
**Revision history:** v0.1 (2026-08-17) first issue — the eighteenth session's registry distillation: the diet procedure extracted from its two executed instances (DF1 + CB1) and the C-095/C-110 decisions; adversarially verified pre-ratification (the DP1 flight, 4 slices, 22 findings — 1 High, 9 Med, 12 Low — all cured in-draft: extractions separated from flagged extensions, quotes given frozen homes or forward-reference notes, the ledger lag named with its cure at the adopting close); checker half named, not built.
