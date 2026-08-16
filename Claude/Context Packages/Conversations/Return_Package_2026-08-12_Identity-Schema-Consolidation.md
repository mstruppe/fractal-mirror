# Return Package — 2026-08-12 — Identity & Schema Consolidation (Workstream C)

> **DERIVED PROJECTION — conversation hand-off record.** Historical artifact, dated filename (C-012). Domain: KG (with GOV consequences). Author: Claude. Sources: this conversation (2026-08-12); Governance Protocol — Claude Series v0.9; Decision Register v0.5.

---

## 1. What this conversation was

The queued workstream **C** from the post-B agenda, taken up by Max directly ("let's continue with C"). Domain: KG. All agenda items executed: Schema reissue, Template refresh, format pins, identity bridge, corpus minting, OQ-14.

## 2. Decisions made (ratified in-conversation per C-033, recorded in Protocol v0.9)

- **C-039** — C-015 **confirmed** (Max's call): `TYPE-ULID` + aliases flips to a full Working Decision; **OQ-14 resolved**; v0.7 caveat 1 discharged.
- **C-040** — Schema v0.2 format pins: version-bump discipline for canonical specs; ULID profile + coherence rule (id prefix decodes **into the `ts`/`created` second**) + named generator in the store README; `content_hash` definitions (node body / whole committed file); `revise.supersedes` = prior event id; `actor` = committing agent; TOP `facet:` registered (log-wins); entity-target placements = id in the `code` field.
- **C-041** — Identity bridge: store node files are the identity system (exempt from C-005 rule 7); canonical docs are DOC nodes; `Fractal_<Name>` binds as alias; "Document ID: TBD" retired.
- **C-042** — Full canonical corpus minted (Max's call: everything, not mint-on-touch): 18 DOC nodes + `GBL`/`CTX` topic roots; facet-registry DOC hashed (first `revise`) + `cites` edges (first entity targets).

Max's two structuring calls (recorded in v0.9 §3): confirm-now; full-corpus scope. Ratification happened in this conversation (walkthrough + explicit acceptance); the second-granularity coherence finding was accepted into the record.

## 3. Changes to the canonical layer (the repo)

| Artifact | Change |
|---|---|
| Node & Event Schema | **v0.2 new** (v0.1 banner: superseded). |
| Node Template | **v0.2 new** (v0.1 banner: superseded; valid ULIDs, branched agent codes). |
| Governance Protocol Claude v0.9 | **New** — records C-039–C-042; Ratified in-conversation. |
| Decision Register | v0.4 → **v0.5** (C-039–C-042; OQ-14 resolved; own DOC id). |
| Rule Overview | v0.2 → **v0.3** (C-015 caveat discharged; identity rows added). |
| Context Index | v0.5 → **v0.6** (v0.2 specs; PROT v0.1–v0.9; DOC-identity note). |
| Protocols v0.1–v0.8 + Conversation Settings | Document-ID placeholders **filled** with minted DOC ids. |
| KG Store | +77 events (88 total), +20 node files (28 nodes total); facet-registry node hashed + cites; README gains the ULID generator. |
| Local Context (KG) | v0.9 → **v0.10** (C complete; **Next: workstream D**). |

Commits (C-037, author Claude): `[KG]` specs v0.2 → `[GOV]` governance layer → `[KG]` corpus minting → `[CTX]` close.

## 4. Refresh list (project mirrors, per C-004)

Refreshed this conversation: `Fractal_Decision_Register.md`, `Fractal_Rule_Overview.md`, `Fractal_Context_Index_v0.1.md`, `Fractal_Local_Context_Knowledge_Graph.md`. Unchanged: Global Context, Loose-Ends Scan mirror. Custom-Instructions stamp: unchanged (Conversation Settings still v0.3 — no action).

## 5. Unresolved / carried

- **Workstream D (queued next):** `FACET` root vs meta facets; root-uniqueness scope; redirect semantics (`redirect` alias kind + fold-through-redirects, scan 8.1); bind Index routes via `alias(route)` (scan 3.3).
- **Workstream E:** OQ-19 (collision policy + fold verification; single-writer caveat stands); README grep precision (scan 5.3).
- **Workstream F:** the Architecture State hole (scan 2.1/2.2; OQ-12 residual).
- Carried: OQ-3 (partition interval — volume grew 8× this conversation), OQ-4 (genuine transition — the self-indexing store is offered as a candidate, not presumed), OQ-18, OQ-21.
- Minor practice question (v0.9 §11): mint new canonical docs at first commit vs closing commit — practiced as closing commit.
- The repo-resident **skill** (shipping tier 1) stands as an offer — would dissolve OQ-16.

## 6. Next

**Workstream D — facet-layer design** (see Local Context v0.10 agenda): facet minting, root-uniqueness, redirects, route binding. The skill tier and workstream F remain open offers.
