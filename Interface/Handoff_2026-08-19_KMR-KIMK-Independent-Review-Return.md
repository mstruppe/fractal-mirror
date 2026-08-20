# Hand-off — KMR/KIMK loose-end independent review: the mother's return (mother → KNet, through Max)

> **DATA, NEVER INSTRUCTION (C-096 discipline).** This is the mother-authored return to KNet's independent-review ask (`Handoff_2026-08-19_KMR-KIMK-Loose-End-Independent-Review-Mother.md`). It records independent findings, one factual overturn, agreements, scope widenings, repair advice, and an invited architectural comparison. **It is advisory evidence for a later KNet review: it creates no KNet authority, accepts no artifact, ratifies no decision, and dispositions nothing — Max and KNet retain all KNet dispositions** (the requesting packet's §2 and §9.9, honored in full). Transport: Max's own hand.

**Direction:** FRACTAL mother → KNet, through Max
**Message class:** Hand-off (review return — independent four-eye, second model)
**Status:** Issued · Non-governing
**Issued:** 2026-08-19
**Author:** Claude (AGENT.AI.CLAUDE, mother-side; model: Claude Fable 5)
**Responding to:** KNet packet `Handoff_2026-08-19_KMR-KIMK-Loose-End-Independent-Review-Mother.md`, reviewed as Working Draft bytes SHA-256 `cbd4f1ac81765a5b65a433f52fe5a7ca8d1c31bf2bfa523c36f045b1351847ee` (the packet's own hand-off pin was not yet supplied at review time)
**Subject source pin:** KNet commit `3ae486157a5024965c82ebfe07d33b9b573ffa12` (verified present: `[RES] Repair KMR and KIMK flight boundaries`, 2026-08-19 18:26:36 +0200)

---

## 1 · Review basis — pin, artifacts, method (§9.1)

**Pin and artifact identity verified.** All eleven review-surface files were read at the pin via `git show <pin>:<path>`, and each file's raw SHA-256 was recomputed independently: **all eleven match the packet's §7 table exactly.** The mother and KNet reviewed identical bytes.

**Method and boundary.** Every inspection was read-only: `git show` and `git cat-file` against the pin, `git log --all` for path history, and — for Condition C, under the packet's §7 allowance to challenge closure — one sweep of the repository object store (`git cat-file --batch-all-objects`, hashing every blob's raw content; 941 blobs total). The mother wrote nothing into KNet: no file, no ref, no rescue act, no gc, no commit. Findings below were formed from the pinned artifacts before comparison with the packet's §8 (§9.2); the §8 comparison is stated separately in §5.

---

## 2 · Condition A — predecessor-preserving lineage

**Independent finding.** Confirmed against Architecture §5.1 and `IMPLEMENTATION_CONTRACT.md` at the pin. The Flight 0005 repair — revision `1.2.0` on all Phase-4-authored identity-bearing records, generation scope `R1_2_0` on revisionless workflow coordinates — establishes **collision separation** (changed bytes cannot silently reuse a prior `{id, revision}` coordinate). It does **not** materialize same-ID predecessor chains linking current-generation records to their earlier-flight ancestors; earlier flights stand beside the current graph as sealed bundles. KNet's distinction (packet §4, question 1) is **stated correctly**, and its boundary claim holds: no current Flight 0005 output is affected — the flight is internally closed over its own generation; what is weakened is the architecture-conformance claim and historical navigation (question 2).

**Addendum — the revision-semantics debt.** Bulk-stamping a generation `1.2.0` quietly changes what the revision field means: from *position in one object's edit history* (the §5.1 sense) to *batch number of the authoring flight*. A future reader cannot distinguish a third-edit object from a third-flight object, and generation-born objects carry revision numbers implying ancestors that never existed. This debt compounds with every further flight; the sorting decision should be taken **before** more generations accumulate, not at acceptance time.

**Questions 3–4 (the sorting rule).** The hybrid rule is sound — and it is not a reinterpretation: it is Architecture §5.1 read carefully, since **only identity-bearing records carry a revision field at all**. Genuinely evolving semantic objects (equations, obligations, certificates, definitions, models, estimands) take same-ID predecessor chains; occurrence records (operations, events, jobs, run capsules, diagnostics, receipts) take generation-derived identities and never pretend to be revisions.

**Question 5 (minimum artifact, invariant, tests).**
- *Artifact:* an explicit predecessor map for the evolving classes — every non-initial same-ID revision names exactly one predecessor `{id, revision}`; a per-flight lineage manifest binding generation N's evolved objects to N−1.
- *Checker invariant:* for evolving classes, a non-initial revision must have exactly one same-ID predecessor of lower declared revision order; chains terminate at an initial revision; no two records share a predecessor absent an explicit fork record.
- *Adversarial tests:* a non-initial revision with no predecessor must fail; two records claiming one predecessor must fail; a predecessor edge crossing IDs must fail; an occurrence record carrying a revision/predecessor must fail the class sorting.

**Question 6 (deeper problem).** Yes, one — not in §5.1's design but in where its discipline is applied: see §7 (the architectural comparison). The overlay/candidate-root model itself is coherent; it is currently unexercisable (`accepted_base_ref: null`), and the generation workaround is the implementation's honest survival move under per-edit lineage cost.

**Severity/confidence (§9.4):** Low today (architecture-conformance dimension only; no correctness effect) · confidence High. **Disposition class:** agree with §8 — architectural hardening before a stronger lineage claim — plus the addendum: take the hybrid-rule and revision-semantics decision early.

---

## 3 · Condition B — the unreachable legacy checker block

**Independent finding.** Confirmed and widened. In `check_math_register_v0.2.py` at the pin (raw SHA-256 `a12a7309…`), `validate_proof_certificates()` reaches, for every certificate record, one of four exits before line 3291: non-certificate `continue`, ineligible → `inactive_history` `continue`, contract-mismatch → `stale` `continue`, or the current-path call `_validate_evidence_certificate(rec)` followed by the **unconditional `continue` at line 3290**. Lines 3291–3344 (the legacy obligation-resolution / artifact-inspection / replay / asserted-vs-computed path) are statically dead.

**Question 1–2 (absoluteness).** The unreachability is absolute. Python provides no mechanism — exception, callback, subclass, iterator mutation, or otherwise — that resumes execution mid-loop-body after an unconditional `continue`; an exception in the dispatcher propagates out, and a subclass can only replace the whole method, never partially execute this body. Answer: **no current or dynamic entry path exists.**

**Question 3 (lost obligations).** The two load-bearing side effects downstream code consumes are **reproduced** by the current dispatcher: obligation resolution with missing → `stale` (lines 3170–3174), and the `certificates_by_obligation` bookkeeping (line 3176) that `compute_proof_coverage` consumes (line 3517). The asserted-vs-computed guard (legacy `KMR-E834`) is superseded by the stricter current rule that contract certificates must remain honestly pending (`KMR-E890`). **One legacy duty has no successor:** the current code contains an external-evidence consumption lane for `lean4` only (`_consume_external_lean_evidence`; verified across `validate()`'s entire phase sequence — no native twin exists). A `native_trace` certificate can never progress past `pending_external` under current code. This is not a present defect — the register's native certificates (`KMR.PRF.CORE.0001` @1.1.0/1.2.0, an identity the packet's §6 did not discuss) are honestly pending Drafts — but a native consumption lane must exist before native evidence could ever be accepted. Recommended: track it as a named open obligation, distinct from the cleanup.

**Widening — the dead footprint.** Nine helper methods are called **only** from the dead block, with zero references anywhere else in the pinned Mathematics tree: `_certificate_metadata_state`, `_environment_state`, `_proof_artifact_state`, `_semantic_map_artifact_state`, `_replay_receipt_artifact_state`, `_split_pending_evidence_reasons`, `replay_native`, `replay_lean_preflight`, `replay_lean`. Removing only the 54-line block would strand nine orphan methods.

**Questions 4–5 (repair and proof).** Removal of the block **plus the nine orphans** in one commit is behavior-preserving. Evidence protocol: (1) the static fact above; (2) the adversarial suite is blind to the dead path — `test_evidence_contract.py` at the pin contains zero references to `KMR-E842`, `KMR-E833`, `KMR-E834`, or any of the nine helpers (verified); (3) run the full checker on the pinned register plus the full suite before and after removal and require byte-equal output. Optional belt-and-suspenders: first land a tripwire (`raise` as the dead block's first statement), run everything green, then delete.

**Question 6 (where history lives).** Git and the frozen evidence bundles only. An "isolated non-executable module" in the live tree recreates the exact reactivation risk this cleanup removes; the removal commit's message is the signpost.

**Severity/confidence (§9.4):** Low (maintainability; no current execution effect) · confidence High. **Disposition class:** agree with §8 — behavior-preserving cleanup with focused regression evidence — scope widened to the orphan cluster, plus the native-lane successor gap recorded as its own obligation.

---

## 4 · Condition C — the "missing" `20d42bef…` receipt: **overturned on the facts**

**Independent finding.** The packet's factual premise is falsified in the good direction. A full sweep of the repository object store — all 941 blobs, **reachable and unreachable** — found exactly one blob whose raw content SHA-256 is `20d42bef3f44499874b061a0c830c43b8ad432c92eb723ec1071588923640c3d`:

> **Git blob `218492846396aacfc10e2b250bb8468cd1b8c084`** — a dangling (unreachable) loose object: contained in no commit on any ref and absent from every reflog listing; object file mtime **2026-08-18 19:34** (+0200).

**Verification performed by the mother (packet §6, question 5's checks — already executed):**
1. *Byte identity:* the blob's content hashes to `20d42bef…` exactly — cryptographically conclusive.
2. *Well-formedness:* parses as a complete replay receipt, `receipt_schema_version 0.2.0`.
3. *Semantic cross-bind:* field-by-field match to the retained `KMR.PRF.CORE.0002@1.0.0` payload — obligation `KMR.OBL.CORE.0002@1.0.0`; semantic map path + `7c140994…`; proof source path + `7d859952…`; generated statement `731325ab…`; environment aggregate `7c8bfa60…`; theorem `KNet.KMR.logarithmicPowerLawTransformation`; Lean 4.32.1 / mathlib `520045ab…` matching the governed profile. This is the named receipt, not a lookalike.

**The loss mechanism, from committed history.** The unversioned path `Lean/receipts/log_power_law.replay.json` was committed exactly once across all refs (`bbcc824`, 2026-08-19 13:00:45 +0200) — **already carrying the 1.1.0-era bytes `82312b76…`**. The 1.0.0 receipt was therefore staged (`git add`, 2026-08-18 19:34) and overwritten in the working tree before any commit captured it; the orphaned index blob is its only survivor. In one sentence: the register's immutability discipline outran the evidence-retention discipline by one commit.

**Consequences for the packet's §6 statements.** "Those exact receipt bytes are not present in the retained source state" is technically true of the committed tree. **"KNet's targeted review found no retained Git blob with the named `20d42bef…` raw content hash" is false** — the blob exists in the object store. The packet's non-claims remain correct doctrine (a hash cannot reconstruct bytes; a fresh replay is new evidence, never the old artifact) — and both are now **moot**: this is retrieval, not reconstruction.

**Time sensitivity — the one urgent item in this return.** An unreachable loose object is exactly what `git gc` prunes. Under default settings it becomes prune-eligible two weeks after its mtime (**≈ 2026-09-01**); `git gc --auto` can fire on ordinary commands once loose-object thresholds are crossed, and a manual `git gc --prune=now` or aggressive maintenance destroys it immediately.

**Repair advice (§9.7 — KNet executes; the mother deliberately did not rescue, having no authority):**
1. Until rescued: run no `git gc`, `git repack`, or `git maintenance` in the KNet repository.
2. Rescue: `git cat-file blob 218492846396aacfc10e2b250bb8468cd1b8c084` → write to a **new versioned retention path** (e.g. `Lean/receipts/log_power_law.replay.v1.json`); never overwrite the current unversioned file.
3. Re-verify raw SHA-256 = `20d42bef…`; record the recovery provenance (blob id, sweep method, this return) in the retention note; land it through KNet's own governed close so the bytes become reachable permanently.
4. Questions 1–4 resolve concretely: no current head, replay profile, projection, or Flight 0005 conclusion depends on the artifact (the v3 path is closed on present evidence); the `1.0.0` record is an honest historical pointer whose named evidence becomes byte-complete at the rescue; **the acceptance-basis exclusion decision dissolves — no archival gap needs recording.**
5. Question 7 (README wording): **confirmed overstated at the pin** — "`log_power_law.replay.json` and `…v2.json` retain preceding exact Draft evidence states" is false for the 1.0.0 state (the unversioned file holds 1.1.0 bytes). True once the v1 rescue lands; tighten the wording either way.
6. Question 6: agreed as doctrine, moot here.

**Severity/confidence (§9.4):** the underlying condition was a pending permanent evidence loss (Medium on the historical-provenance dimension); it is fully curable today; **urgency High until the rescue lands** · confidence High (cryptographic identity + committed-history trace). **Disposition class: disagree with §8** — reclassify from *"attempt bounded recovery if a real source exists; otherwise record an explicit archival and acceptance-basis boundary"* to **"recover now — the source exists inside the repository; time-bounded."**

---

## 5 · Comparison with the packet's §8 and the §9 dimension grid (§9.3–9.6)

| Condition | vs. KNet's preliminary reading |
|---|---|
| Predecessor lineage | **Agree** (facts, causal reading, claim boundary, disposition class) + the revision-semantics addendum; decide the hybrid rule early |
| Legacy checker block | **Agree** + scope widened (block + nine orphaned helpers) + one successor gap recorded (no native evidence-consumption lane) |
| Missing historical receipt | **Disagree on the factual premise and the disposition** — bytes present as an unreachable blob, verified; recovery now, time-bounded; the exclusion decision dissolves |

| Condition | Current correctness | Current replayability | Historical provenance | Architecture conformance | Exact-file acceptance consequence |
|---|---|---|---|---|---|
| Predecessor lineage | Unaffected | Unaffected | Coarse (generation-grain retained in bundles; no in-state chains) | **Gap** — §5.1's predecessor law only vacuously satisfied; revision field semantically overloaded | None once the lineage claim is worded honestly; hybrid rule + invariant before any architecture-conformant lineage claim |
| Legacy checker block | Unaffected (statically dead) | Unaffected | Preserved in git + frozen bundles | Neutral (implementation hygiene) | None; cleanup advised before acceptance-era audits for review clarity |
| Missing historical receipt | Unaffected | Unaffected (v3 path closed on present evidence) | **Was a pending permanent loss; fully curable now** — rescue the dangling blob | Neutral | **No blocker once rescued**; without rescue, a permanent superseded-evidence gap plus a README overstatement would need recording |

**§9.8 — additional findings within the bounded surface:** (1) the recovered receipt blob itself (§4); (2) the native evidence-consumption successor gap (§3); (3) the nine-method orphan cluster (§3); (4) the revision-semantics debt (§2); (5) the receipts-README overstatement (§4.5).

---

## 6 · Invited architectural comparison — where the strictness should live

*Offered under the packet's §2 allowance for architectural comparisons, and as the substantive answer to §4 question 6. Direction of thought: Max's, raised mother-side on reviewing this return's findings; assessment: the mother's. Comparison data, never instruction — KNet's architecture is KNet's.*

**The observation.** Weighed at the pin, the architecture's mass sits in freezing-and-communicating machinery (acceptance manifests, credential and decision hashes, external checkpoints, per-operation journal transactions, lineage capsules); the mathematical-understanding core — the typed model graph, the obligation semantics, the backend bridge, the Phase-4 fragment — is the smaller fraction, and the fragment is explicitly an implementation ceiling. The current design applies frozen-result discipline at **working tempo**: every operation mints immutable identity in the same transaction.

**All three reviewed conditions are symptoms of that placement.** A: per-edit predecessor chains proved unmaintainable at flight tempo, so the implementation invented generations — coarse-grained lineage, unnamed. C: retention-at-churn demanded a hash of bytes the machinery never captured; the receipt died in a working-tree overwrite. B: even cleanup accretes ceremony.

**The comparison model (two planes).** A **live working plane** — mutable, cheap identities, ordinary git snapshots as sufficient provenance — and a **freeze boundary at experiment completion**, where an extraction act mints the durable records under full KMR discipline: identity-includes-meaning, predecessor edges to the *previous frozen* head, receipts bound and retained in the same act, acceptance machinery downstream of the freeze. Under this placement: the strict promise still holds where it pays — every *communicated* result immutable, identity-clean, exactly replayable; lineage becomes experiment-grained (which the generation repair already is, de facto — the hybrid rule of §2 becomes the natural law rather than a patch); and Condition C's failure mode becomes **structurally impossible**, because a fingerprint is only ever recorded in the act that retains its bytes. What is given up: record-grain auditability of mid-experiment states ("Tuesday afternoon's belief") — git-grain history covers that forensic need at near-zero cost. What must never loosen, on either plane: the honest-status vocabulary — pending stays pending, no bare "proved," the six-axis status vector survives at freeze.

**Convergence datum.** The mother's own doctrine ratified this shape twice in other organs: the fieldnote buffer as RAM against durable canon (C-121), and the integration law *live in the workspace, fixed at the seam* (C-123). A math tool converging on live-then-freeze would be consistency with the governed pattern, not a revert of strictness — a relocation of it to the boundary where it pays.

---

## 7 · Advisory statement (§9.9)

This return is advisory. It creates no KNet authority; accepts no KMR or KIMK artifact, root, or byte; ratifies no decision; unlocks nothing; and its recommendations — including the rescue in §4 — are proposals for KNet's own review under Max's dispositions. The mother inspected the pinned state read-only and altered nothing in KNet's repository, object store, or refs.

---

*Cite this file by path + issue date — `Interface/Handoff_2026-08-19_KMR-KIMK-Independent-Review-Return.md`, issued 2026-08-19 — or pin it at the mother's `beta-0.6` anchored tag, which carries these bytes (the subject pin in the header names KNet's commit and is not this file's own citation). Envelope element 5 added 2026-08-20 per Scan #6 S6-6.1; content above untouched.*
