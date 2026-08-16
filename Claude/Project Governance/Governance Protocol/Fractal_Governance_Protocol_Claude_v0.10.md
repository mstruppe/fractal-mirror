# Fractal Governance Protocol — Claude Series v0.10

**Topic:** Facet-layer completion (workstream D): facets minted as concepts under a `FACET` root (C-043); global root-uniqueness (C-044); reparent/redirect semantics and the alias-kind fold rules (C-045); the Index's routing codes bound via `alias(route)` — §5.3 rule 7 exercised (C-046)
**Status:** Ratified (2026-08-13 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-13 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.9

---

## 1. Context

Workstream C closed the identity layer, and Schema v0.2 annotated exactly what remained open in the facet layer it anchors (scan 3.3/3.4/8.1): the facets themselves were magic strings defined in a hand-authored table — structurally the control file C-026 rejected; root-code uniqueness had no declared scope, so a topic root `TIME` could silently collide with the time facet in every grep; rule 6's reparent-by-redirect had no representation (an `alias` of no registered kind?) and no fold semantics, leaving two flagship properties — stable references and prefix-scan retrieval — in unresolved tension; and rule 7's "routes cannot drift" was asserted with zero `route` aliases in the log. This protocol records the conversation that resolved all four.

## 2. Questions Investigated

- Do facets stay deliberately meta (like the verb set), or get minted under a `FACET` root so the registry is log-derived top to bottom?
- What is the scope of root-code uniqueness — per facet or global?
- How is a reparent represented in the append-only log, and how does the fold keep prefix scans truthful after a move?
- Which of the Index's routing codes get bound via `alias(kind: route)` now, and which wait for workstream F?

## 3. Human Input (Max)

Max took up the queued workstream directly ("let's continue with D") and made the four structuring calls, accepting each recommendation as presented: **(a) mint facets** under the `FACET` root rather than keep them meta; **(b) global** root-uniqueness; **(c) re-mint + explicit redirect alias** as the reparent mechanism (rejecting both the implicit newest-mint-wins variant and the alias-only variant); **(d) bind the four minted domain routes now** (`KG`, `GOV`, `GBL`, `CTX`), leaving `AST`/`ONT`/`WS`/`PROT` to workstream F.

## 4. AI Input (Claude)

- Framed the D1 choice through C-027's own grammar-vs-dictionary distinction: verbs and roles are *grammar* (small, fixed, schema-registered); facets were always designed as an *extensible vocabulary* — and extensible vocabularies are what minting is for. Proposed the meta-facet construction: token `facet`, root `FACET`, children `FACET.TOPIC` … `FACET.AGENT`; event-field tokens bind as `alias(kind: route)`, so existing log lines change not at all and tokens resolve to identities exactly as routing codes do.
- Surfaced the D1/D2 interlock: under global root-uniqueness, facets minted as bare roots (`TOPIC`, `AGENT`, `TIME`) would collide with their own vocabularies' roots — the `FACET.` prefix is forced, and "list all facets" becomes the prefix scan `FACET.*`.
- Proposed the three-part redirect design (C-045): mint-on-same-subject (parent-validated), explicit `redirect` alias (one-grep list of moved codes), fold-resolves-through-redirects (log untouched; materialized front-matter regenerated at canonical codes — legal because front-matter is a fold, §4.5). Noted rule 6's "touch zero placements" holds at the log layer, which is the canonical one.
- Proposed pinning the full alias-kind set while registering `redirect`: `label` (newest label materializes as `title:`; all labels accumulate in `aliases:`) / `route` / `redirect` — closing the previously unspecified title-update semantics with a fold rule instead of a new field.
- Recommended not minting `AST`/`ONT`/`WS`/`PROT` concept roots ahead of workstream F, whose forge-clean-vs-pointer-only decision is exactly about their canonical ground.

## 5. Jointly Derived Conclusions

1. **The registry is now made of the same stuff top to bottom.** Facet → coordinate → placement is one construction repeated at three scales — the recursive-simplicity credo applied to the classification system itself. The Schema's §5.1 table drops from control file to derived projection.
2. **One root, one meaning.** Global root-uniqueness is what keeps the zero-infra promise honest: a grep over codes can never cross-match roots from different facets, and full dotted paths become globally unambiguous for free.
3. **Append-only and prefix-scan retrieval are compatible** once the fold is the place where redirects resolve: history keeps every old code valid; current state materializes every placement at its canonical code. The tension scan 8.1 identified was between the log and the *fold*, not within the log.
4. **Rule 7 moves from asserted to exercised** with four live bindings; the same mechanism (route tokens over identities) now carries the Index's domain routes and the facet tokens — one rule, two uses, no new machinery.

## 6. Current Decisions

- **C-043 — Facets are minted concepts (Working Decision, executed).** Each facet is a `TOP-…` minted under the root `FACET` in the meta-facet (event-field token `facet`); its token binds as an `alias` (`kind: route`). Minted this conversation: `FACET` + `FACET.TOPIC`, `FACET.METHOD`, `FACET.SOURCE_TYPE`, `FACET.TIME`, `FACET.AGENT`, each with its token bound (`facet`, `topic`, `method`, `source-type`, `time`, `agent`). New facets are vocabulary extensions (mint + token binding), never schema edits; the Schema §5.1 table is a projection refreshed on mint. Existing events are untouched — the tokens they carry now resolve to identities.

- **C-044 — Global root-uniqueness (Working Decision).** Sibling uniqueness remains scoped to the parent (§5.3 rule 3), but root segments (`parent: null`) form **one namespace across all facets**. Checked at mint time against the log's existing roots. Verified against the live store: `AGENT`, `KG`, `GOV`, `GBL`, `CTX`, `FACET` — no collisions; the schema-reserved roots (`METH`, `SRC`, `TIME`, `PHY`, …) remain available.

- **C-045 — Redirect semantics + alias-kind fold rules (Working Decision).** Reparent = **(a)** a `mint` whose `subject` is the existing `TOP-…` and whose `code` is the new path (parent-validated, uniqueness-checked) + **(b)** an `alias` of **`kind: redirect`** on the old code, in the same commit. Old codes are never deleted or re-pointed; the **fold resolves codes through the redirect chain** — newest mint = canonical `code:`; materialized `placements:` in other nodes regenerate at canonical codes; log lines are never touched. Alias kinds pinned: **`label`** (newest label = `title:`; all labels accumulate in `aliases:`) · **`route`** (machine token → identity: Index routes, facet tokens, and — from v0.3 forward — the C-041 `Fractal_<Name>` bindings, which are machine tokens, not display names; the corpus batch's `label` bindings are grandfathered) · **`redirect`** (superseded coordinate code). The newest-label rule was validated mechanically this conversation: the first draft bound this protocol's `Fractal_<Name>` as `label` and the fold verifier flagged it displacing the title — the `route` re-classification is the cure, caught before commit.

- **C-046 — Route binding exercised (Working Decision, executed).** The Index's four minted domain routes — `KG`, `GOV`, `GBL`, `CTX` — are live `alias(kind: route)` bindings over their topic-root concepts; the Context Index's routing table is a projection of these bindings and says so. `AST`, `ONT`, `WS`, `PROT` are bound when workstream F settles their canonical ground; until then their Index rows remain hand-maintained and are marked as such.

- **Ratification record (2026-08-13, in-conversation per C-033).** Max ratified C-043–C-046 in this conversation after the walkthrough. The four structuring calls (§3) were made explicitly; the technical constructions were accepted as proposed.

## 7. Alternatives Considered

- **Facets deliberately meta** (like the verb set). Defensible — the scan itself offered it — but rejected: it leaves the facet set as the one hand-authored tier of a registry whose whole point is log-derivation, and every new facet becomes a schema edit rather than a vocabulary event.
- **Facets as bare roots in the meta-facet** (`TOPIC`, `AGENT`, …). Rejected: collides with vocabulary roots under global root-uniqueness (D2); the `FACET.` prefix also gives "all facets" as a prefix scan.
- **Per-facet root uniqueness.** Rejected: semantically sufficient but breaks one-grep retrieval — the flagship zero-infra property — whenever two facets share a root spelling.
- **Implicit reparent (newest-mint-wins, no marker).** Rejected: readers must diff mint histories to discover a move; no one-grep redirect list.
- **Alias-only redirect (no re-mint).** Rejected: the new code would never pass parent validation or uniqueness checking — it weakens rule 1's mint-before-use grammar exactly where structure changes.
- **Minting + binding all 8 domain routes now.** Rejected: `AST`/`ONT`/`WS`/`PROT` have no settled canonical layer; minting their concepts now would pre-empt workstream F's forge-clean-vs-pointer-only decision.

## 8. Assumptions

- The `FACET` root's genesis self-reference (its mint names the token `facet` whose binding lands later in the same batch) is acceptable under the zero-infra clause — the same batch-scoped self-reference the agent bootstrap recorded and accepted; true by end of batch.
- Facet tokens are lowercase and may contain characters illegal in code segments (`source-type`); the `route` alias binding is what bridges token to concept, so no code-shape rule is bent.
- Until the deferred index exists, "the fold resolves redirects" is a *reader's rule* executed by hand exactly like folding placements — the store currently contains zero redirects, so the cost is nil until first exercised.

## 9. Consequences

- Node & Event Schema **v0.3** and Node Template **v0.3** are canonical; the v0.2 files remain in place as history with superseded banners. The Template gains the reparent worked example (§E).
- The Knowledge Graph Store grows from 28 to **35 nodes** (six `FACET.*` concept nodes + this protocol's DOC node) and from 88 to **118 events** (6 facet mints, 6 token bindings, 4 route bindings, 5 canonical-doc revisions with 5 title rebinds, this protocol's mint). Store total: first live `route` aliases; still zero redirects.
- **Living-document DOC titles go versionless** on the five docs revised this conversation ("Fractal Node & Event Schema", not "… (v0.2)") — under C-045's newest-label rule a versioned title would demand an alias event per version; the version lives in the `revise` chain where it belongs. Practice extends to the remaining living-doc DOC nodes on next touch.
- The store README gains the redirect-check line and the facet-minting note.
- Decision Register → **v0.6**: C-043–C-046; scan findings 3.3, 3.4, 8.1 retired.
- Rule Overview → **v0.4**: grammar rules 3/6/8 updated; alias kinds registered; facet-minting row.
- Context Index → **v0.7**: routing table marked as a projection of the store's route bindings (four live, four pending F); Schema/Template v0.3 rows; PROT row v0.1–v0.10.
- Local Context → **v0.11**: workstream D recorded complete; next queued item set (E).

## 10. Decision Ledger Changes

Added **C-043** (facets minted; `FACET` root + meta-facet; executed), **C-044** (global root-uniqueness), **C-045** (redirect semantics; alias kinds label/route/redirect + fold rules), **C-046** (route binding exercised for `KG`/`GOV`/`GBL`/`CTX`; rest pending F). No prior decision content changed; C-026/C-027 gain completion annotations. Scan findings 3.3, 3.4, 8.1 retired. No numbered OQs resolve; no new OQs open — the D items entered as scan findings and leave as decisions.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- Carried to **workstream E:** OQ-19 (mint-collision policy + fold-verification ritual; single-writer caveat stands — now also covering root-mint races under C-044); README grep-precision fixes (scan 5.3).
- Carried to **workstream F:** the Architecture State hole (scan 2.1/2.2; OQ-12 residual); binding the remaining domain routes (`AST`, `ONT`, `WS`, `PROT`) once their canonical ground exists (C-046 residual).
- Carried: OQ-3 (partition interval), OQ-4 (genuine transition), OQ-18 (`time` auto-derivation), OQ-21 (off-site host).
- New, minor: whether the facet-token `route` aliases should also appear in a projected one-page facet-registry view once one is generated (a projection question, not a format one; on observed need).

## 12. Next Line of Research

Per the scan agenda: workstream **E** (multi-writer safety — mint-collision policy, fold-verification ritual, retiring the single-writer caveat) or **F** (the Architecture State hole, which now also gates the four unbound domain routes) are the natural next consolidation steps. The repo-resident **skill** (shipping tier 1, would dissolve OQ-16) stands as an offer alongside both — it can slot in whenever Max calls it.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.10 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.10 |
| Status | Ratified (2026-08-13, in-conversation per C-033) |
| Domain | Project Governance — Knowledge Graph facet layer |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-13, this protocol) |
| Date | 2026-08-13 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.9 |
| Related Documents | Fractal Node & Event Schema v0.3; Fractal Node Template v0.3; Fractal Decision Register v0.6; Fractal Rule Overview v0.4; Fractal Context Index v0.7; Loose-Ends Scan (2026-08-12) |
| Revision Trigger | Any change to C-043–C-046, the alias-kind set, or the redirect fold rule |
| Document ID | DOC-01KZX7157GQ0YP1NGFBF7ZS3HE |
