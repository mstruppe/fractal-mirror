# Flight Record — 2026-08-17 · The Compaction-Behaviour Test (CB1 — the C-110 Group A gate)

> **CANONICAL FLIGHT RECORD (C-058 class via Fractal_Ultracode_Flight_Protocol_v0.1 §6.3) — dated, frozen at issue, never revised.** Findings carry stable ids `CB1-…`. The flight's verdicts are proposals until ordinary decisions adopt them (C-008); nothing in canon moved — both corpus arms were scratch copies by construction.

**Identity:** `Fractal_Flight_Record_Compaction_Behaviour_1` · **Version:** 1.0 (frozen) · **Domain:** GOV · **Author:** Claude (orchestrator) · **Date:** 2026-08-17 (eighteenth Code session) · **Commissioned by:** Max — C-110's Group A hold: *"before simply adopting it could we make a test run checking how both translate into AI agent behaviour?"* — the cache doctrine's empirical gate · **Document ID:** DOC-01M07WKMFD9RN39AQCQ9WZ4QZE (minted at first commit via `close.py --create`; stamped by the post-mint revise)

## 1 · Commissioning contract vs. as-flown

**Second conformant launch of the C-108 sequence** (game plan → agreement → armed declaration with the effort checkpoint → "flight go"), and the first whose per-phase efforts were **set mechanically by the orchestrator at launch** — the commissioner green-lights the declared tiers, the script enforces them (banked as a Flight Protocol v0.2 note in-session, sharpening DF1-6). **Contract:** 11 agents, 4 phases (Build ×2 default → Battery ×1 high → Simulate ×6 low, 3 per arm, blind → Judge + adversarial Verify ×2 high); continuous gating; simulation procedure over two corpus arms (heavy = unmodified copy, lean = the five Group A evictions applied); read-only on canon; proposal-only landing; estimate ~450–550k tokens. **As flown:** 11 agents, 0 failures, no scope deviations, ~27 min; **~1.02M subagent tokens — roughly 2× the estimate** (the deviation is the estimate's, not the contract structure's; recorded for the v0.2 reissue's cost-estimation guidance).

## 2 · The experiment

Six blind sim agents (told nothing of pointers or the A/B design) each answered 4 of 12 gold tasks — 4 surface / 4 one-hop / 4 deep — after orienting as fresh sessions in their arm. Judge scored all 24 task×arm pairs on correctness and pointer-following; the adversarial verifier re-derived 16/24 scores against the corpora and independently traced 15+ evicted fact classes for reachability.

**Headline result: 23/24 correct.** Heavy arm 12/12; lean arm 11 correct + 1 partial. **The feared failure mode — pointer-stopping on one-hop and deep tasks — did not materialize:** lean agents followed pointers into the frozen tier in all 8 one-hop/deep tasks and matched gold, twice exceeding it in specificity. The single degradation sat in the *shallowest* class.

## 3 · Findings

- **CB1-1 [Med · the pointer-stop specimen].** Lean T04 (surface): the P1 revision-history headline row carried just enough tokens to *feel* like an answer — the agent quoted it, named the protocol, and never opened it. Mechanism identified by the judge: a headline that names WHAT was recorded without flagging that the HOW/WHY lives elsewhere invites being quoted as the answer. The P2 rows, whose clauses name the concrete record file, produced correct pointer-following every time. **Cure (the pointer grammar):** every compacted row states *"narration lives only in \<named file\>"* — name the concrete file, not the series — and index tables are marked index-only.
- **CB1-2 [High · the second failure mode — row-born content].** The verifier's discovery, and the flight's sharpest specimen: the OQ-33 row held content that existed *nowhere in the frozen tier* — Max's origin quote, the two expected tensions, the migration-candidates list were **born in the living row** in the same session as a protocol that under-narrates them. The eviction made them unreachable, and the lean row's ≤40-word clause additionally *distorted* the surviving fragment (collapsing a tension-level relation into a question-level one — which a sim agent then reproduced verbatim). The build's lossless checklist verified **file-existence, not fact-presence**, and passed it. **Cure (the fact-presence gate):** no eviction without verifying the named target *holds the narration*; row-born annotations relocate into the frozen tier first. Same defect found milder in the v0.64 row (its pointer targets predate the triage they summarize; survived only because the C-110 decision block sits in the same file).
- **CB1-3 [Low · measurement note].** `pointer_followed` is vacuous in the heavy arm (the living doc still holds the prose); the surface-class 4/4-vs-3/4 comparison measures only the lean arm. For H6 reuse: the metric needs an arm-aware definition.
- **CB1-4 [Low · coverage note].** P3 (Rule Overview) was not directly exercised — both arms navigated straight to frozen records for its tasks. Its "adopt" rests on the closest evidence (robust lean-arm frozen-tier navigation), flagged honestly as untested at the document itself.

## 4 · The verdict table (per eviction, judge + verifier combined)

| Proposal | Verdict | Basis |
|---|---|---|
| P1 · Register revision history → pointer table | **adopt with the CB1-1 grammar fix** | directly exercised (T04); the one pointer-stop; cure demonstrated by P2's grammar |
| P2 · Register OQ/findings ledgers → status + clause + pointers | **adopt with the CB1-2 gate + the OQ-33 row repaired** | most-exercised eviction (6 tasks, all gold-level); the row-born defect is the build's, not the grammar's |
| P3 · Rule Overview rows → ≤40-word norm + refs | **adopt** (untested-at-document flagged) | no degradation signal; frozen-tier navigation robust |
| P4 · Architecture State history → pointer table | **adopt** | exercised (T03) clean; verifier notes the evidentiary weight was overstated, verdict unaffected |
| P5 · Index Sources narrative → two-line pointer | **adopt** | exercised (T08): straight to the frozen Return Package, gold in full detail |

**Verification (declared tier: work-over single-pass + adversarial):** the verifier re-derived 16/24 scores — all load-bearing scores confirmed exactly, rationale-level issues only, no correctness verdict flipped. `verdicts_stand: false` **narrowly and productively**: P1/P3/P4/P5 survive the attack; P2's adopt requires the CB1-2 amendment. The verifier's meta-observation of record: *the failure mode C-110 predicted was found once; the quieter one — eviction of content the frozen tier never held — is the one the build's own checklist failed to catch.*

## 5 · What the flight proves (the cache doctrine's evidence)

The C-110 cache framing holds empirically for this agent class: **eviction is behaviourally lossless where the pointer grammar names the concrete record — including at full reasoning depth.** The two failure modes are both *grammar/gate* defects, not depth defects, and both have designed cures that generalize: (a) rows must say where the narration lives, index tables marked index-only; (b) the eviction gate checks fact-presence, never mere file-existence, relocating row-born content first. These two rules are the **diet procedure standard's** first empirical content (the candidate beta-0.5 registry entry, C-110), and the methodology — blind two-arm simulation, depth-classed gold battery, pointer-following as the core metric with CB1-3's arm-aware definition — is **portable to KNet's H6** as designed.

## 6 · Unchanged, with reasons

Canon untouched (both arms scratch copies; the governing tree never read-write by any flight agent). The shadow lean tree is a session-scratch draft: adoption regenerates it under the CB1-1/CB1-2 cures rather than promoting the draft wholesale (the OQ-33 and v0.64 rows need repair regardless; regeneration is cheap and re-gated). The C-110 Group A hold stands until Max adopts on this record.

---
*Sources: workflow run `wf_8b27adfc-58a` (11 agents; per-agent returns in the session's workflow journal); corpus arms built from the governing tree at post-`323b52f` state; gold battery, 24 scores, and the verifier's full issue lists in the run record. Frozen at issue.*
