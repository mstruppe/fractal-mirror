# Flight record — the Beta-0.6 Delta Review (Scan #6's carrier)

> **CANONICAL FLIGHT RECORD (C-108 class — dated observation, never revised; the container's story under `Fractal_Ultracode_Flight_Protocol_v0.2`).** The commissioned ultracode flight that carried Loose-Ends Scan #6: the whole beta-0.5→beta-0.6 delta functionally tested and audited, findings adversarially verified. The scan's own artifact — findings, verdicts, green slate, byproducts — is `Review_2026-08-20_LooseEnds-Scan-6.md`; this record carries the commissioning contract, the as-flown execution, the cost honesty, and the recorded deviations (§2/§7 of the standard).

**Version:** 1.0 · **Status:** Ratified (2026-08-20, in-conversation per C-033 — the landing accepted in the cure-slate ratification, "as recommended") · **Reviewed By:** Max (2026-08-20) · **Domain:** GOV · **Author:** Claude (orchestrator) · **Document ID:** DOC-01M0FY211G7W8HG6K459MGZG71 (minted at this close via `close.py --create`; stamped by the post-mint revise)

---

## 1 · Commission and contract (as ratified)

**The commission (Max, verbatim):** *"for the ultracode flight we need to review what happened between beta 0.5 and 0.6, all new features, we want to test them and give them a thorough scan for loose ends"* — with the addendum: the kernel/custom partition audited across the four surfaces (tag · mirror · newborn · site), and the essence restated as *"see what issues 0.6 carried with it and form a refined beta 0.7 out of it."*

**The contract (all seven §2 fields, proposed → extended → ratified):** scope the delta only (C-116–C-130), governing tree read-only, mutations in scratch clones; five phases (functional test · served-surface audit · projection-drift + partition · loose-end scan · adversarial verify + assemble); agent structure derived — 15 finder lanes + 1 assembler fixed, refuters dynamic (~20–35 estimated); per-phase efforts declared; **adversarial verification tier** (one refuter per finding, the alternative declined on the record); landing proposal-only; **continuous mode** (one go, one landing). **The launch (compressed, the DP1 provision):** Max's *"green light for all flights with recommended effort level +1 … rather overspend … ready for take off"* carried agreement and go in one word; the as-flown efforts restated at launch (testers/sweepers/scanners HIGH, the partition auditor XHIGH, the link-checker MEDIUM, refuters MEDIUM with HIGH on High-severity, the assembler XHIGH). **Cost estimate at launch:** 1.9–2.4M tokens (basis: Scan #5's as-flown 1.62M + the dynamic tail).

## 2 · As flown

| Metric | Contracted | As flown |
|---|---|---|
| Finder lanes | 15 | 15 — all returned, zero failures |
| Refuters | ~20–35 (1 per finding) | 44 (44 lane findings raised) |
| Assembler | 1 | 1 |
| **Agents total** | ~36–52 | **60** |
| Wall clock | — | ~21 minutes |
| **Cost** | **1.9–2.4M tokens** | **4.04M tokens (≈1.7× over)** |
| Verification | adversarial, per finding | 44 refutations run: **0 refuted outright, 4 adjusted** |
| Findings landed | — | 44 lane findings → deduped **36 unique: 0 High · 16 Med · 20 Low** |

**Cost honesty (§7.2):** the ≈1.7× miss decomposes into the commissioner's +1 effort bump (authorized pre-launch, explicitly accepting overspend) and the refuter tail landing at 44 against the ~20–35 band. Both feed the next contract's estimate: a delta-review at raised effort with adversarial verification prices at ≈4M, not ≈2M. The Gas Ledger carries the row (tool-reported, exact).

## 3 · Recorded deviations (§2 — honest, none silent)

1. **Concurrent lanes:** the four finder phases flew concurrently (declared at launch — independent lanes; §5.3 held: refuters consumed only settled findings, the assembler only verified ones).
2. **Stats-label miscount, orchestrator-side:** the run's raw stats printed "16 lanes contracted / 15 flown" — the 16 was the fixed-role count (15 finders + assembler) mislabeled in the orchestration script. No lane went silent; diagnosed against the journal before reporting.
3. **The refuter wave refuted nothing outright** (4 adjustments only). Read honestly two ways: the finder lanes reported conservatively (their briefs demanded evidence an independent verifier could reproduce), and the refuter briefs may sit too close to the finder posture — a calibration question banked for the next flight's contract.
4. **One environmental boundary:** Bitcoin-final OTS verification was impossible without a node everywhere it arose — recorded as the stranger's own honest view, not a finding.

## 4 · Conduct

Jurisdiction held: the governing tree read-only to every agent; all mutations in scratchpad clones; the real mirror never touched by the pack tests (a stand-in mirror built for the seven failure-mode exercises); KNet and the annex untouched. Landing proposal-only — the cure program executed only after the commissioner's per-decision ratification ("as recommended" on the six Wave-0 decisions; "ratified" on C-131, the seed-tree principle the partition lane's findings resolved into). Byproducts handed over whole (25 items, the Review §5), none silently fixed.

## 5 · What the flight proved beyond its findings

The delta-review class works as a release ritual: a whole release boundary swept in ~21 minutes of flight plus one session of cures, with the pack gate ending four checks stronger — and the first live run of the new partition-seat check out-sweeping the flight itself (C-080's missing seat, found by the gate the flight proposed). The adversarial tier's 0-refuted result, paired with 36/36 findings surviving into executed cures, is the strongest finder-precision datum the flight series has produced.

---

*Author: Claude (AGENT.AI.CLAUDE) · The thirty-first Code session. Companion: `Review_2026-08-20_LooseEnds-Scan-6.md` (the scan artifact). Frozen at issue; corrections land in later records.*
