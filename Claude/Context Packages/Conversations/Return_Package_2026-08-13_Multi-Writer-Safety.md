# Return Package — 2026-08-13 — Multi-Writer Safety (Workstream E)

> **DERIVED PROJECTION — conversation hand-off record.** Historical artifact, dated filename (C-012). Domain: KG (with GOV consequences). Author: Claude. Sources: this conversation (2026-08-13); Governance Protocol — Claude Series v0.13; Decision Register v0.9.

---

## 1. What this conversation was

The queued workstream **E** from the post-D agenda, taken up by Max directly ("let's continue with Multi-writer safety (KG)"). Domain: KG. All four agenda items executed: mint-collision policy (incl. root-mint races under C-044), fold-verification ritual canonized, single-writer caveat retired (OQ-19 resolved), README grep precision fixed. Scan findings 4.1, 5.3, 8.2 retired.

## 2. Decisions made (ratified in-conversation per C-033, recorded in Protocol v0.13)

- **C-049** — **Concurrency & collision policy.** Identity cannot collide (80-bit ULIDs) — only codes can, only across unmerged clones, never destructively. **First mint wins** (`ts`, event-ULID tie-break), reproducible from the log alone; cure is **mandatory + append-only** (re-mint the losing subject + re-point its intended placements, verifier-listed); **root mints are deliberate** from the pin forward — guard `--root` flag + a `note` naming whose call (pre-pin roots grandfathered). Single-writer caveat retired.
- **C-050** — **Verification ritual + tools canonized.** `verify.py` (fold verifier) and `mint.py` (mint guard) are repo-resident in the store — stdlib-only, C-006-exception code artifacts, not DOC-minted. **Duty:** `verify.py` passes before every store-touching commit and after every merge (C-037 boundary); git merges JSONL textually, so the semantic merge check is the ritual.

Max's three structuring calls (recorded in v0.13 §3): first-mint-wins; build the guard now; root ceremony = tool flag + recorded call. Both his mid-flight inputs shaped the design: the root race as a *process* question ("minting can't be done willy-nilly?" → depth-graded ceremony) and the naming-options tool (→ `mint.py --list`, the prevention layer). Ratification happened in this conversation (walkthrough + explicit acceptance).

## 3. Worth remembering (method notes)

- **E opened with verification, not authoring:** the verifier ran green over the whole store *before* any design was settled — 130 events / 37 nodes, and the first whole-corpus external-hash pass (all 22 canonical files recomputed on Max's machine). Design conversations start from a proven baseline.
- **C-008 exercised mid-flight:** Max skipped premature actions and asked for the workstream rolled out anew against his updated thinking — the manual-first boundary working exactly as designed, at conversation speed.
- **The three-layer shape** (prevent / detect / cure) is the reusable pattern: no layer asks anyone to be careful — safety by mechanism, not discipline.

## 4. Changes to the canonical layer (the repo)

| Artifact | Change |
|---|---|
| Node & Event Schema | **v0.4 new** (v0.3 banner: superseded). §5.4 concurrency & collision policy (C-049); §5.5 verification ritual & tools (C-050); §4.1 "near-conflict-free" precision; OQ-19 closed in §6. |
| KG Store tools | **New:** `verify.py` (fold verifier, A–E check suite) and `mint.py` (mint guard) beside the README. |
| KG Store README | Rewritten: guard + ritual sections; multi-writer status; corrected traces (scan 5.3); C-049/C-050 rules. |
| Governance Protocol Claude v0.13 | **New** — records C-049–C-050; Ratified in-conversation. |
| Decision Register | v0.8 → **v0.9** (C-049–C-050; OQ-19 resolved; C-032 + review-pass caveats discharged). |
| Rule Overview | v0.6 → **v0.7** (multi-writer row; grammar rule 9; single-writer caveat removed). |
| Context Index | v0.7 → **v0.8** (Schema v0.4 rows; KG status; tools on the store row; PROT v0.1–v0.13). |
| KG Store | +8 events (138 total), +1 node file (38 total): Protocol v0.13 DOC mint (create, route alias, 2 placements) + 4 living-doc revisions (Schema path/hash, Register, Rule Overview, Context Index). |
| Local Context (KG) | v0.13 → **v0.14** (E complete; **Next: workstream F**). |
| Agenda Board | Regenerated **file-first** (C-048), stamp v0.14; artifact republished. |

Commits (C-037, author Claude): `[KG]` Schema v0.4 + tools + README → `[GOV]` governance layer → `[KG]` store events + node updates → `[CTX]` close. `verify.py` run green before each store-touching commit — first exercise of the C-050 duty, on its own birth batch.

## 5. Refresh list (project mirrors, per C-004)

Refreshed this conversation: `Fractal_Decision_Register.md`, `Fractal_Rule_Overview.md`, `Fractal_Context_Index_v0.1.md`, `Fractal_Local_Context_Knowledge_Graph.md`. Unchanged: Global Context, Loose-Ends Scan mirror. Custom-Instructions stamp: unchanged (Conversation Settings still v0.3 — no action).

## 6. Unresolved / carried

- **Workstream F (queued next):** the Architecture State hole (scan 2.1/2.2; OQ-12 residual); bind `AST`/`ONT`/`WS`/`PROT` routes (C-046 residual).
- Carried: OQ-3 (partition interval), OQ-4 (genuine transition), OQ-18 (`time` auto-derivation), OQ-21 (off-site host); C-038 acceptance test unexercised.
- Minor: a projected one-page facet-registry view — on observed need.
- The repo-resident **skill** (shipping tier 1) stands as an offer — would dissolve OQ-16.

## 7. Next

**Workstream F — Architecture State hole** (see Local Context v0.14 agenda): forge-clean vs pointer-only; Galaxy/Operator reconciliation; rule 3 + OQ-12; bind the four remaining routes. The skill tier and the C-021 step-3 index (spec = the `verify.py` invariants) remain standing offers.
