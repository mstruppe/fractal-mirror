# Fractal Governance Protocol — Claude Series v0.13

**Topic:** Multi-writer safety (workstream E): the mint-collision policy with first-mint-wins and root ceremony (C-049), and the canonized verification ritual + repo-resident tools (C-050) — OQ-19 resolved, the single-writer caveat retired
**Status:** Ratified (2026-08-13 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-13 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.12

---

## 1. Context

Workstream E was the queued *Next* since the facet layer closed (v0.10). The store ran under the last standing structural caveat: single-writer until a mint-collision policy and a fold-verification ritual exist (OQ-19, v0.7 caveat 2; scan 4.1/8.2). C-044's global root namespace had widened the collision surface it guards — deliberately — and the workstream-C/D verifier scripts existed only as in-conversation improvisations, exactly the "improvised regeneration" pattern C-048 had just cured for the board.

## 2. Questions Investigated

- What actually collides between concurrent writers — identities, codes, or both — and what does git catch?
- How is a collision resolved without editing the append-only log, and by whom?
- Does minting need ceremony, and how much, at which depth?
- What form does the verification ritual take, where do the tools live, and what governs tool files?

## 3. Human Input (Max)

Max drove the framing mid-flight with two inputs: **(a)** the root race is a *process* question — "multiple people could mint the same name and we need a process in place… that hints that minting a new name can't be done willy-nilly?" — and **(b)** the prevention idea: "we can build a tool which gives the user naming options to make sure no duplicates can be selected." He also exercised C-008 exactly as designed: skipped premature actions, then asked for the workstream to be rolled out anew against his updated thinking. His three structuring calls: **first mint wins** (deterministic cure rule); **build the mint guard now**; **root ceremony = tool flag + recorded call** (not per-root human approval, not nothing).

## 4. AI Input (Claude)

- Grounded the workstream in a verified-green baseline: built the fold verifier as a durable script and ran it over the full live store on Max's machine — 130 events / 37 nodes, every invariant holds, all 22 external canonical-file hashes recompute (first whole-corpus hash pass).
- Separated the collision surface: **identity cannot collide** (80-bit ULID randomness); only *codes* can, only across unmerged clones, and never destructively — a collision is two valid events whose combination violates rule 3, visible to any fold.
- Proposed the three-layer shape: **prevent** locally (Max's guard idea, which also automates "write #2" — today's real single-writer risk), **detect** at the C-037 boundary (the ritual), **cure** append-only (first-mint-wins + re-mint, the same machinery as a C-045 reparent).
- Proposed depth-grading the ceremony: deep mints stay cheap (decentralised minting is the point); root mints are vocabulary legislation in the one shared namespace and carry the flag + recorded call.

## 5. Jointly Derived Conclusions

1. **Safety by mechanism, not discipline.** Every prior multi-writer claim rested on writers never erring (scan 4.1). Prevention makes local duplicates impossible; detection makes remote ones visible; deterministic cure makes resolution reproducible from the log alone. No layer asks anyone to be careful.
2. **Git is a carrier, not a referee.** JSONL appends merge textually; the semantic merge check is the ritual. Naming this in the Schema ends the "merge surfaces clashes" ambiguity the scan flagged.
3. **Ceremony belongs where the namespace is shared.** Minting depth is a good proxy for blast radius: sibling checks are local, root mints legislate globally (C-044). The guard's `--root` flag plus a recorded call prices that correctly — mechanical, not bureaucratic.
4. **Tools follow the board's precedent.** `verify.py`/`mint.py` are repo-resident code artifacts (C-006 exception, not DOC-minted, C-042 mint-on-reuse) — the C-048 pattern generalised from a rendered surface to executable ones.

## 6. Current Decisions

- **C-049 — Concurrency & collision policy (Working Decision).** Identity cannot collide (ULID randomness); only codes can. When the merged log holds two `mint` events binding one code to different subjects, **the earlier event wins** (`ts`, event-ULID tie-break) — mechanical, reproducible, no adjudication (Max may overrule a specific outcome as a recorded decision producing ordinary reparent events). **Cure is mandatory and append-only:** re-mint the losing subject under a fresh code (note citing the collision + winning event id) and re-point its intended placements (`unplace` + `place`; the verifier lists every placement against the contested code — binding is deterministic, intent is split explicitly by its writers). **Root mints carry ceremony** from the pin (2026-08-13) forward: minted through the guard's explicit `--root` flag with a `note` recording whose call it was; the verifier errors on bare post-pin roots; pre-pin roots grandfathered (`GBL`/`CTX`/`FACET` already conform). **The C-032 single-writer caveat is retired.** Resolves OQ-19 (with C-050). Normative home: Node & Event Schema v0.4 §5.4.

- **C-050 — Verification ritual + tools canonized (Working Decision, executed).** `verify.py` (fold verifier, read-only: log integrity, mint grammar incl. the collision tripwire and root-note check, references, full fold-vs-nodes comparison, all hashes) and `mint.py` (mint guard: naming options, full validation, coherent ULIDs, `--root` enforcement, event + node stub in one move — §4.5 automated) live **in the store beside the README**: stdlib-only, C-006-exception code artifacts, **not** DOC-minted, git-versioned. **The ritual is a duty: `verify.py` runs and passes before every store-touching commit and after every merge that touches the store** (the C-037 boundary); red blocks the commit. The README's two imprecise trace recipes are corrected in the same stroke (scan 5.3: authorship = `role: by` + agent-prefix; subtree scans drop the closing quote). Normative home: Schema v0.4 §5.5.

- **Ratification record (2026-08-13, in-conversation per C-033).** Max made the three structuring calls explicitly (first-mint-wins; build the guard now; root ceremony = flag + recorded call) and ratified C-049/C-050 as drafted after the walkthrough.

## 7. Alternatives Considered

- **Human adjudication per collision.** Rejected as the default: the store stays red until someone decides, and the outcome is not reproducible from the log. Preserved as the overrule path on top of the deterministic rule.
- **Both-re-mint (burn the contested code).** Rejected: maximally fair but burns good names and doubles the placement blast radius.
- **Governance-level root approval (Max approves every root in-conversation).** Offered; Max chose the lighter tool-flag + recorded-call form. The `note` still names the human call, so provenance is equivalent.
- **Spec-only guard (orthodox C-021).** Offered; Max called the build now — his proposal of the tool is the observed need, and the guard closes the *single*-writer discipline gap (forgetting write #2) that predates any second writer.
- **A lock/reservation scheme for minting.** Never seriously entertained: requires coordination infrastructure, violating substrate-B zero-infra (C-018/C-021); detection + deterministic cure achieves the invariant without it.

## 8. Assumptions

- Collision frequency will be low (small writer count, deep mints dominant); first-mint-wins is priced for that regime. If collisions become common, the policy revisits (observed need).
- The verifier's runtime stays trivial at current volumes; when the log outgrows it, the C-021 step-3 index inherits these invariants as its spec.
- The C-049 pin instant (2026-08-13T12:00:00Z in `verify.py`) precedes every post-pin root mint; the six existing roots are all pre-pin and grandfathered.

## 9. Consequences

- **Node & Event Schema → v0.4** (new; v0.3 banner: superseded): §5.4 concurrency & collision policy; §5.5 verification ritual & tools; §4.1 "near-conflict-free" precision; OQ-19 closed in §6.
- **New in the store:** `verify.py`, `mint.py` (beside the README). **README → v2:** guard + ritual sections, multi-writer status, corrected traces (scan 5.3).
- Decision Register → **v0.9**: C-049/C-050 added; OQ-19 → Resolved; v0.7 caveat 2 discharged.
- Rule Overview → **v0.7**: multi-writer row added; grammar rule 9; single-writer caveat removed.
- Context Index → **v0.8**: Schema v0.4 rows; KG row status; store row lists the tools; PROT range v0.13.
- Local Context → **v0.14** (E complete; **Next: workstream F**); Agenda Board regenerated file-first (C-048) and republished.
- Knowledge Graph Store: **+1 node (38), +8 events (138)** — this protocol's DOC mint (create, route alias, two placements) and four living-doc revisions (Schema path/hash, Register, Rule Overview, Context Index). Committed per C-037; `verify.py` run green before each store commit (first exercise of the C-050 duty on its own birth batch).

## 10. Decision Ledger Changes

Added **C-049** (collision policy: first-mint-wins, append-only cure, root ceremony) and **C-050** (ritual + tools canonized). **OQ-19 resolved** — the single-writer caveat on C-032 is retired; v0.7 caveat 2 discharged. Scan findings 4.1, 5.3, 8.2 retired. No new OQs open.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None new. Standing items carry unchanged: workstream F (scan 2.1/2.2; OQ-12; C-046 residual), OQ-3, OQ-4, OQ-18, OQ-21; C-038 acceptance test unexercised; C-047's Settings-escalation watch-item.

## 12. Next Line of Research

**Workstream F** (Architecture State hole: forge-clean vs pointer-only; Galaxy/Operator reconciliation; rule-3 wording + OQ-12; bind `AST`/`ONT`/`WS`/`PROT`) is the queued *Next*. The repo-resident skill and the C-021 step-3 index remain standing offers — the index now inherits a precise spec: the invariants `verify.py` enforces.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.13 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.13 |
| Status | Ratified (2026-08-13, in-conversation per C-033) |
| Domain | Project Governance — Knowledge Graph / Multi-writer safety |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-13, this protocol) |
| Date | 2026-08-13 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.12 |
| Related Documents | Fractal Node & Event Schema v0.4; Fractal Decision Register v0.9; Fractal Rule Overview v0.7; Fractal Context Index (v0.8); Knowledge Graph Store `verify.py` / `mint.py` / `README.md` |
| Revision Trigger | Any change to C-049/C-050, the collision-cure semantics, the root-ceremony form, or the verification duty |
| Document ID | DOC-01KZXE0ATR01RGDFTQMCP8H8CA |
