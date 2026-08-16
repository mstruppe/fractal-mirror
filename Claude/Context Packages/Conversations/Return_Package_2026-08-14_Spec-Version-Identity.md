# Return Package — 2026-08-14 · Spec-Version Identity (S2-5.1 → C-061; rider S2-6.1 → C-062)

> **DERIVED PROJECTION — conversation handover record (C-001).** Sources: Governance Protocol — Claude Series v0.19 (Ratified); Decision Register v0.17; Local Context v0.23; Knowledge Graph Store (60 nodes / 253 events).

**Parent:** Return_Package_2026-08-14_Version-Agreement-Checker.md · **Local Context:** v0.22 → **v0.23**

---

## 1. Handover (C-059 auditable line)

**Previous package queued:** S2-5.1 — spec-version identity in the store, with the pre-canon labeling call (S2-6.1/OQ-10) riding along. **This conversation did:** decided both (Max's explicit picks from presented arms), executed the store work and the rider, issued Protocol v0.19, and closed. The standing sequence is done through its last queued item — **nothing is queued next**.

## 2. Acts & decisions of record (Protocol v0.19, Ratified)

- **C-061 — spec-version identity: per-version DOCs (executed).** One rule replaces two treatments: **DOC identity mirrors file identity.** Living docs = one revised DOC node; versioned artifacts = **one DOC per version file**, as the protocol series always had. Nine retro mints (Schema v0.1–v0.5, Template v0.1–v0.4), each with a version-labeled `route` alias (`Fractal_<Name>_vX.Y`) and its own frozen hash; no cross-version edges. The two living DOC ids stay as **series pointers** (versionless alias, hash tracks newest via `revise`; bodies re-scoped, bytes unchanged → no events). **A spec reissue = one series `revise` + one per-version mint.** "Schema v0.4" is a citable identity again. Fixes S2-5.1. Alternatives (living-docs; mint-on-cite; alias-rebind) recorded in v0.19 §4.
- **C-062 — pre-canon label at first contact (executed).** BOOTSTRAP §0 names `Vision thought scramble.docx` pre-canon (informs, never governs — the OQ-22 ruling made visible on disk). No identity, no mint, no move; the archive-move go/no-go stays OQ-10. Fixes S2-6.1.
- **Max's calls:** arm (b) over (a)/(c) · series ids kept (no alias re-binding) · BOOTSTRAP line over folder move · full close in one pass.

## 3. Change summary (one `[GOV]` commit, Claude-authored per C-037; push = Max)

Protocol **v0.19** issued + DOC-minted · Register → **v0.17** (C-061/C-062; S2-5.1 + S2-6.1 → Fixed; OQ-10 annotated) · Rule Overview → **v0.15** · BOOTSTRAP → **v0.6** (§0 line) · Architecture State → **v0.4** · Context Index → **v0.12** · Local Context → **v0.23** · Agenda Board republished (stamp → v0.23) · store: **+45 events** (9 retro mints ×4 + protocol mint ×4 + 5 revises) and **+10 node files**, two series bodies re-scoped → **60 nodes / 253 events**, `verify.py` PASS + `check_versions.py` PASS.

## 4. Refresh list

The full C-059 checklist was walked — see Local Context v0.23 §Standing refresh items for every row's mark (notable: Schema→Template coupling **checked, no reissue** — C-061 changes the store's representation, not the spec's text; store tools **checked — unchanged**). Project mirrors refreshed: Register, Rule Overview, Local Context, Context Index (Global unchanged, v0.3). Cowork board artifact republished from the file.

## 5. Unresolved / carried

- **Open findings (review ledger):** S2-6.2 / S2-6.3 (Max's manual hygiene) — S2-5.1 and S2-6.1 leave the open set this close.
- **Standing OQs:** OQ-4, OQ-6, OQ-9, OQ-10 (archive-move half only), OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27.
- **Pending on Max:** review the commit and `git push`; empty `_to_delete/`; the three `~$*.docx` owner-files at the root (optional).
- **Standing note:** the next Schema reissue documents the C-061 store treatment in the spec's own text (and rides the C-059 Schema→Template coupling).

## 6. Next

**Nothing queued** *(auditable line: the previous package queued S2-5.1 + the rider; this conversation closed both)*. The **G offers and H roadmap stand**: the index server triggers when tracing-by-grep gets slow; the WS forge at the first WS build; **Scan #3 penciled** after the build track — earlier if the checker and the C-059 checklist start disagreeing. Open the next conversation with Global + Local Context v0.23 + this package.
