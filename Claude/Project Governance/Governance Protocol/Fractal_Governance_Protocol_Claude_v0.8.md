# Fractal Governance Protocol — Claude Series v0.8

**Topic:** Substrate realization (workstream B): the FRACTAL repository initialized under git (realizing C-018/C-019/C-020); the commit convention (C-037, resolving OQ-15); the Bootstrap Protocol with the client-adapter step (C-038); the Rule Overview joins the context package (C-036)
**Status:** Ratified (2026-08-12 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-12 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.7

---

## 1. Context

Workstream A closed with everything ratified and nothing enforced: the event log's append-only guarantee, the portability doctrine, and C-025's commit granularity were all discipline, not substrate — the Loose-Ends Scan rated the missing `git init` the highest-severity B item. Two further items were queued with it: the bootstrap/rehydrate protocol ("laptop in the ocean" cannot run without it), whose scope had just been widened by the shipping thread at A's close (effortless setup ⇒ bootstrap must include installing the client adapter, since vendor surfaces are swappable clients per C-018 and the rules live in the repo per C-020/C-035); and a housekeeping line — whether the new Rule Overview joins the context package like the Register (C-030). This protocol records the conversation that executed all three.

## 2. Questions Investigated

- How is the 'Rule Overview joins the context package' decision recorded — a numbered decision or a protocol footnote?
- What does the repository contain — the whole FRACTAL folder or only the Claude era — and what is hygiene vs knowledge?
- What is the commit convention, and how does it bind to the identity system (`AGENT.HUMAN.MAX` / `AGENT.AI.CLAUDE`) and to C-025's commit boundary (OQ-15)?
- Where does the bootstrap protocol live so a bare clone finds it with zero prior knowledge, and what exactly is the client-adapter step?

## 3. Human Input (Max)

Max opened the conversation by making the housekeeping call directly ("add the rule overview to the context package like the Register") and connected the FRACTAL folder. On the four structuring questions he chose: (a) a **numbered decision** (C-036) — it changes the context-package composition exactly as C-030 did; (b) repo scope = **everything + hygiene .gitignore** — the repository is FRACTAL (C-020), ChatGPT-era included, with only OS/app noise (`.DS_Store`, `~$*` lock files) excluded; (c) commit authorship = **actual author, mirrored to the KG** — one identity system across git and the event log; (d) bootstrap at the **repo root** (`BOOTSTRAP.md`) with the Governance Documents layer routing to it, so the bare clone surfaces it unaided.

## 4. AI Input (Claude)

- Framed the Rule Overview question as C-030's exact precedent: mirror to the Project spine + route in the Context Index + a context-package line in the document's own header.
- Proposed the baseline-then-changes commit sequence (a `[GBL]` snapshot of the pre-B state before any B edits land), so the repo's first history cleanly separates "what existed" from "what B changed."
- Proposed the convention: author = actual author (`Max Struppe <max.struppe@gmail.com>` / `Claude <claude@fractal.local>`), message `[DOMAIN] imperative summary` with decision refs, one commit per coherent change-set = the C-025 event boundary — resolving OQ-15 without new machinery.
- Drafted `BOOTSTRAP.md` as a canonical living document at the root: rehydrate-by-hand first (git + editor suffice, per C-032's zero-infrastructure result), then the client-adapter step (Claude reference adapter per C-035/C-030/C-036; the queued skill → plugin tier from the shipping thread; the cross-vendor pattern), then the commit convention, then the off-site-copy note.

## 5. Jointly Derived Conclusions

1. The substrate now enforces what governance previously only asserted: append-only history, integrity, portability (C-018/C-019/C-020 realized).
2. Identity is one system: a git author line and an `AGENT.*` code are the same fact in two projections.
3. Bootstrap is not complete at "clone and read" — a working FRACTAL environment includes the client adapter, and the adapter is always a stamped projection, never a fork of the rules.
4. The context package now has a fixed composition rule: Global Context + active Local Context + Context Index + Decision Register (C-030) + Rule Overview (C-036), mirrored to the Project spine.

## 6. Current Decisions

- **C-036 — Rule Overview joins the context package (Working Decision).** `Fractal_Rule_Overview.md` is part of the context package exactly as the Decision Register is (C-030): mirrored into the Project spine, routed in the Context Index as a behavioural entry point, maintained as a living projection (C-012), refreshed per update ordering (C-004), never overriding its sources (C-003). Rule Overview reissued as v0.2 with the context-package line; its v0.1 housekeeping question is retired.

- **C-037 — Repository realization + commit convention (Working Decision).** The FRACTAL folder is a git repository (branch `main`), initialized 2026-08-12 with a `[GBL]` baseline snapshot of the full pre-B state; `.gitignore` excludes OS/app noise only (`.DS_Store`, `~$*`) — knowledge is never ignored. Convention: **author = the actual author of the change** (`Max Struppe <max.struppe@gmail.com>` or `Claude <claude@fractal.local>`), mirroring `AGENT.HUMAN.MAX` / `AGENT.AI.CLAUDE`; **message** = `[DOMAIN] imperative summary` using Context Index domain codes, body citing touched decisions/OQs; **granularity** = one commit per coherent change-set, and the commit **is** the C-025 event boundary (knowledge-store events recorded at commit — **resolves OQ-15**); no history rewriting on shared state.

- **C-038 — Bootstrap Protocol (Working Decision).** `BOOTSTRAP.md` at the repo root is the canonical bootstrap/rehydrate protocol (identity `Fractal_Bootstrap_Protocol`, living document, stable root filename per C-012; ships in-repo per C-020). Contents: hand-rehydrate steps (orient → route → local context → rules → integrity check), the **client-adapter step** (Claude reference adapter: connect folder + stamped Custom-Instructions projection per C-035 + context-package mirror per C-030/C-036; queued skill/plugin tier; cross-vendor pattern for GPTs/Gems), the commit convention (C-037), and the off-site-copy recommendation. Acceptance criterion: the "laptop in the ocean" test.

- **Ratification record (2026-08-12, in-conversation per C-033).** Max ratified C-036–C-038 in this conversation after the walkthrough (decisions + findings held against each), with **one caveat recorded**: the C-038 acceptance test ("laptop in the ocean") is **not yet exercised** — no second clone exists. C-038 is ratified as written; its acceptance test is first exercised when OQ-21 resolves or the skill tier is built. Findings accepted into the record without caveat status: the `.git/` bridge leftovers (cosmetic, one-time local `git gc`), the marker address `claude@fractal.local`, and single-disk enforcement until OQ-21.

## 7. Alternatives Considered

- **Protocol-footnote recording for the Rule Overview.** Rejected by Max: composition of the context package is ledger-worthy, per the C-030 precedent.
- **Claude-era-only repository.** Rejected: contradicts C-020 ("the repository *is* FRACTAL"); the ChatGPT era is heritage inside the same portability boundary.
- **Verbatim tracking of OS noise.** Rejected: `.DS_Store`/lock files are Finder/Word artifacts, not knowledge; tracking them buys nothing and dirties every diff.
- **Always-Max authorship with a Claude trailer.** Rejected: splits the identity system git already models; the store and the history should agree on who acted.
- **Bootstrap under Governance Documents only.** Rejected: a bare clone must surface it with zero prior knowledge; a governed root file with the governance layer routing to it serves both masters.

## 8. Assumptions

- The mounted-filesystem quirk (no file deletion via the session bridge) leaves stale git lock files and temp objects behind; these are cosmetic. Assumed acceptable until a one-time local cleanup (`git gc` or deleting `.git/stale/` and `tmp_obj_*` leftovers on the Mac) — noted, not blocking.
- `claude@fractal.local` is a project-internal marker address, not a routable mailbox; assumed sufficient for identity marking.

## 9. Consequences

- The FRACTAL repo exists: baseline commit `[GBL] Baseline snapshot … pre-substrate-realization`, followed by this conversation's B commits under C-037.
- `BOOTSTRAP.md` v0.1 at the root; Context Index routes to it.
- Rule Overview → **v0.2** (context-package line; new C-037/C-038 rows; C-036 in the Anchoring row).
- Decision Register → **v0.4**: C-036–C-038 added; OQ-15 resolved; OQ-21 (off-site remote choice) added.
- Context Index → **v0.5**: Rule Overview + Bootstrap entry points; GOV package includes the Rule Overview; PROT row v0.1–v0.8.
- Local Context → **v0.9**: workstream B recorded complete; next queued item set.
- Workstream B is complete; the scan's B items (git init [High], bootstrap [Med], Rule Overview housekeeping [Low]) are retired.

## 10. Decision Ledger Changes

Added **C-036** (Rule Overview joins the context package), **C-037** (repository realization + commit convention; resolves OQ-15), **C-038** (Bootstrap Protocol with client-adapter step). Ledger: OQ-15 → resolved; **OQ-21** added (choice of off-site remote/host — open, non-blocking). No prior decision content changed.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- **OQ-21 (new):** where the off-site copy lives — second machine, private Git host, or both; nothing depends on the choice (C-018 portability).
- Whether the repo-resident **skill** (the queued first automation candidate, C-008 boundary; would dissolve OQ-16) is the next B-adjacent build — offered to sequencing, not scheduled here.
- Carried: OQ-3 (partition interval — git history may now supply the observed volume), OQ-14 (workstream C), OQ-19 (workstream E).

## 12. Next Line of Research

Per the scan agenda, workstream **C** (identity & schema consolidation) is next: reissue the Schema as v0.2, refresh the Node Template, pin the ULID profile, define `content_hash` input + `supersedes` referent, bridge `DOC-…` ↔ `Fractal_<Name>_v…` (mint canonical docs as DOC nodes), and resolve OQ-14 (C-015 confirm vs grandfather). The repo-resident skill (shipping thread) stands as an offer alongside it.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.8 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.8 |
| Status | Ratified (2026-08-12, in-conversation per C-033) |
| Domain | Project Governance — Substrate & Infrastructure |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, this protocol) |
| Date | 2026-08-12 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.7 |
| Related Documents | BOOTSTRAP.md (Fractal_Bootstrap_Protocol v0.1); Fractal Decision Register v0.4; Fractal Rule Overview v0.2; Fractal Context Index v0.5; Loose-Ends Scan (2026-08-12) |
| Revision Trigger | Any change to C-036–C-038, the commit convention, or the bootstrap contents |
| Document ID | DOC-01KZVYQZAGDJFAQAPESXND2HXF (minted 2026-08-12, C-041/C-042, per v0.9) |
