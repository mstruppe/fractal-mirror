# Fractal Governance Protocol — Claude Series v0.9

**Topic:** Identity & schema consolidation (workstream C): C-015 confirmed (C-039, resolving OQ-14); the Node & Event Schema reissued as v0.2 with the format's open pins fixed (C-040); the identity bridge between `Fractal_<Name>` artifacts and `DOC` nodes (C-041); the full canonical corpus minted into the Knowledge Graph Store (C-042)
**Status:** Ratified (2026-08-12 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-12 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.8

---

## 1. Context

Workstream B left the substrate real but the identity layer inconsistent, exactly as the Loose-Ends Scan had mapped: the Schema had been substantively revised without a version bump (scan 1.2, High); the Node Template still taught agent codes the accepted C-026 grammar forbids and ULID placeholders no tool would accept (1.3/3.1, High); the live store carried a `facet:` field the Schema never defined (6.1); `content_hash`, the `revise` referent, and `actor` semantics were relied upon but undefined (3.2/3.5); two identity systems coexisted with no bridge, leaving every protocol's "Document ID: TBD" dangling (5.2); and beneath all of it, C-015 — the ID scheme the entire store is minted under — was still formally a Working Hypothesis (OQ-14, hardened de facto by C-032). This protocol records the conversation that consolidated all of it.

## 2. Questions Investigated

- Does the C-015 scheme get confirmed, amended, or grandfathered, now that the live store has made it expensive to reject (OQ-14)?
- What exactly does `content_hash` hash, and what does `revise.supersedes` name — an event or a hash?
- What is the pinned ULID profile, and how does a hand-author generate a valid one?
- How do the two identity systems — `Fractal_<Name>_v…` (C-005) and `TYPE-ULID` (C-015) — relate, and which canonical documents get minted as `DOC` nodes now?
- How does a placement target an entity (for `cites`/`member-of`/`derived-from`) when the event format only carries `facet`+`code`?

## 3. Human Input (Max)

Max took up the queued workstream directly ("let's continue with C") and made the two structuring calls: (a) **confirm C-015 now** — the scheme flips to a Working Decision; the store is working evidence and every alternative now costs a migration; no grandfathering clause needed; (b) **mint the full canonical corpus** — all Claude-era canonicals as DOC nodes in one act, retiring every "Document ID: TBD" at once rather than mint-on-touch. He also verified his own model of the commit convention mid-conversation (when does a change warrant a commit), confirming C-037's semantic trigger — a commit per coherent change-set — is how he intends to work in the repo by hand.

## 4. AI Input (Claude)

- Proposed the reissue-not-patch route for the Schema (curing scan 1.2) and the explicit version-bump discipline: canonical specifications are C-005 versioned artifacts, not C-012 living projections.
- Proposed the technical pins (C-040): standard 26-char Crockford ULID with the **coherence rule** (id prefix must decode into the recorded `ts`/`created` second); `content_hash` = sha256 of the node **body** after the closing front-matter delimiter (stable under fold changes), or of the **whole file** for DOC nodes representing external canonical files; `revise.supersedes` = prior **event id** (one supersede semantics everywhere); `actor` = the agent that **committed** the event, provenance in `note`; TOP `facet:` registered with log-wins; entity-target placements carry the target's `TYPE-ULID` in the `code` field (ids and codes are disjoint shapes — no new mechanism).
- Proposed the identity bridge (C-041): store node files *are* the identity system and exempt from C-005 rule-7 naming; a canonical document's ID is its DOC node, with the `Fractal_<Name>` bound as an alias — first live use of the `alias` verb.
- Proposed minting `GBL` and `CTX` as new topic roots (observed need: the corpus includes orientation and routing documents that honestly belong to neither `KG` nor `GOV`).

## 5. Jointly Derived Conclusions

1. The identity layer is now one system viewed twice: a `Fractal_<Name>` is a human alias over a `DOC-ULID`, exactly as a facet code is an alias over a `TOP-ULID` — Principle 6 applied to the project's own documents.
2. A spec that hand-authors will copy from must itself pass its own validation: every example ULID in Schema/Template v0.2 decodes correctly, because invalid examples mint malformed permanent identities.
3. Confirming C-015 (rather than grandfathering) keeps the store regular: nothing in it predates its own rules.
4. The scan's "claimed but unenforced" pattern shrinks again: hashes now have a definition and a first verified example; the alias mechanism has its first live bindings; what remains open (route binding, redirect folds, facet minting, collision policy) is explicitly parked in workstreams D and E.

## 6. Current Decisions

- **C-039 — C-015 confirmed (Working Decision; resolves OQ-14).** The persistent-identity scheme — opaque `TYPE-ULID` keys for living entities, content hashes per version, names/codes as aliases — flips from Working Hypothesis to **confirmed Working Decision**. The live store's contents were minted under the now-confirmed scheme; no grandfathering clause is required. The v0.7 caveat 1 is discharged.

- **C-040 — Schema v0.2: format pins (Working Decision).** The Node & Event Schema is reissued as v0.2 (curing scan 1.2), with: **version-bump discipline** — canonical specifications are C-005 versioned artifacts; every substantive change is a new version; **ULID profile** — standard 26-char Crockford base32 (48-bit ms timestamp + 80-bit randomness), uppercase, with the coherence rule (id prefix decodes into the recorded `ts`/`created` second) and a named generation method in the store README; **`content_hash`** — `sha256:<hex>` over the byte-exact node body after the closing `---` (store nodes) or the whole committed file (external canonical docs); **`revise.supersedes`** = the prior version's event id, never a hash; **`actor`** = the committing agent, decision provenance in `note`; **TOP `facet:`** registered in §3.2, governed by log-wins (not the identity exception); **entity-target placements** — the target's `TYPE-ULID` in the `code` field, `facet` omitted; shapes are disjoint, so greps stay unambiguous. Node Template reissued as v0.2 to match (branched agent codes, valid coherent ULIDs, `EVT` type, `facet:` example, mint-before-use honored).

- **C-041 — Identity bridge (Working Decision).** Store node files carry `TYPE-ULID` identity and are **exempt** from C-005 rule-7 `Fractal_<Name>` naming — they are the identity system, not exported artifacts. Canonical documents are minted as **DOC nodes**: the document's persistent ID *is* its `DOC-…` id; the `Fractal_<Name>` identity is bound as an `alias` (`kind: label`); `content_hash` freezes the committed file's bytes; the node body records the repo-relative path. "Document ID: TBD" placeholders are retired — control tables now record the minted id; new canonical documents are minted at or shortly after first commit.

- **C-042 — Canonical-corpus minting (Working Decision, executed).** The full Claude-era canonical corpus is minted into the Knowledge Graph Store as 18 DOC nodes: `BOOTSTRAP.md`, Global Context, Context Index, Conversation Settings, Decision Register, Rule Overview, Knowledge Path Foundation v0.1, Node & Event Schema, Node Template, and Governance Protocols v0.1–v0.9 — each with `create` (+hash) + `alias` (Fractal name) + `place`(topic) + `place`(by). Two topic roots minted on observed need: **`GBL`** (Global orientation) and **`CTX`** (Context & routing). The facet-registry DOC receives its `content_hash` (first `revise`; first exercise of Principle 4) and `cites` placements to Schema and Protocol v0.6 (first entity-target edges; cures scan 6.2). The active Local Context and Return Packages are **not** minted (dynamic pole / hand-off records; mint-on-reuse).

- **Ratification record (2026-08-12, in-conversation per C-033).** Max ratified C-039–C-042 in this conversation after the walkthrough. The two structuring calls (§3) were made explicitly; the technical pins were accepted as proposed.

## 7. Alternatives Considered

- **Grandfathering C-015** (record store contents as pre-confirmation). Rejected by Max: it preserves an option whose price only rises; confirming makes the de facto state de jure with zero migration.
- **Amending the scheme before confirming.** Rejected: no observed deficiency to amend for; the store's 19 events validate the scheme as specified.
- **Extending C-012 to cover canonical specs** (making the Schema a living document, curing scan 1.2 the other way). Rejected: specs are cited by version everywhere; a mutable spec under a stable name would make every citation ambiguous — the opposite of the identity system's point.
- **Mint-on-touch scope** (living docs only, protocols on first reuse). Rejected by Max in favor of the full corpus: one act, no lingering placeholders, the store becomes the project's real index at once.
- **A hash referent for `revise.supersedes`.** Rejected: two referent kinds for one field; the event chain already orders versions, and hashes remain available on the events themselves.
- **A new `target` field or `entity` pseudo-facet for entity placements.** Rejected: the id-in-`code` rule adds no field and no facet; shape disjointness already guarantees unambiguity — minimal necessary complexity.
- **Minting the active Local Context as a DOC node.** Rejected for now: it changes every conversation; a hash-per-close would be churn without a consumer. Mint when an observed need appears.

## 8. Assumptions

- The sha256 of a file "as committed to git" is well-defined because the commit convention (C-037) fixes the byte content; line-ending drift is assumed absent (repo authored consistently in LF).
- Editing the "Document ID" line in ratified protocols v0.1–v0.8 is **completing a declared placeholder, not rewriting history**: the field itself said "TBD — assigned by Identity System," and git preserves the pre-assignment state.
- The `GBL`/`CTX` topic roots are honest coordinates (orientation, routing) — not routing codes; binding the Index's *route* codes to concepts stays a workstream-D item.

## 9. Consequences

- Schema **v0.2** and Node Template **v0.2** are canonical; v0.1 files remain in place as history with a superseded banner.
- The Knowledge Graph Store grows from 8 to 28 nodes and from 11 to 88 events; every canonical document now has a real ID, and every "Document ID: TBD" is filled with its minted `DOC-…` id (protocols v0.1–v0.9, Conversation Settings).
- The store README gains the pinned ULID generation method.
- Decision Register → **v0.5**: C-039–C-042; OQ-14 resolved; C-015 caveat discharged.
- Rule Overview → **v0.3**: C-015 row unqualified; standing-caveat list updated; new identity-bridge row.
- Context Index → **v0.6**: Schema/Template v0.2 rows; PROT row v0.1–v0.9.
- Local Context → **v0.10**: workstream C recorded complete; next queued item set.
- Workstream C is complete; scan findings 1.2, 1.3, 3.1, 3.2, 3.5, 4.2, 5.2, 6.1, 6.2 are retired.

## 10. Decision Ledger Changes

Added **C-039** (C-015 confirmed; resolves OQ-14), **C-040** (Schema v0.2 format pins), **C-041** (identity bridge; node files exempt from C-005 rule 7; canonical docs minted as DOC nodes), **C-042** (canonical-corpus minting executed; `GBL`/`CTX` roots). Ledger: OQ-14 → resolved. No prior decision content changed; C-015's type annotation updates from "Working Hypothesis (scheme)" to "Working Decision (confirmed, C-039)".

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- Carried to **workstream D:** facets minted under a `FACET` root vs deliberately meta; root-uniqueness scope; fold-through-redirect + a `redirect` alias kind; binding the Index's routing codes via `alias(route)` (scan 3.3/3.4/8.1).
- Carried to **workstream E:** OQ-19 (mint-collision policy + fold-verification ritual; single-writer caveat stands); README grep-precision fixes (scan 5.3).
- Carried: OQ-3 (partition interval), OQ-4 (genuine transition — does the corpus-minted store qualify? Max's call, offered not presumed), OQ-18 (`time` auto-derivation), OQ-21 (off-site host).
- New, minor: should DOC nodes for **new** canonical documents be minted in the same commit as the document's first version, or in the conversation's closing store commit? Practice this conversation: closing commit; revisit if drift is observed.

## 12. Next Line of Research

Per the scan agenda: workstream **D** (facet-layer design: `FACET` root, root-uniqueness, redirects, route binding) or **F** (the Architecture State hole — the empty `Architecture State/` directory cited as "full current architecture") are the natural next consolidation steps; **E** (multi-writer safety) unlocks a second writer. The repo-resident **skill** (shipping tier 1, would dissolve OQ-16) stands as an offer alongside all of them — it can slot in whenever Max calls it.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.9 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.9 |
| Status | Ratified (2026-08-12, in-conversation per C-033) |
| Domain | Project Governance — Identity & Schema |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, this protocol) |
| Date | 2026-08-12 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.8 |
| Related Documents | Fractal Node & Event Schema v0.2; Fractal Node Template v0.2; Fractal Decision Register v0.5; Fractal Rule Overview v0.3; Fractal Context Index v0.6; Loose-Ends Scan (2026-08-12) |
| Revision Trigger | Any change to C-039–C-042, the ULID profile, the hash definition, or the identity bridge |
| Document ID | DOC-01KZVYR37GACAHBD8H1FDKKFGD |
