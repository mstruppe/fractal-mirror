# Return Package — 2026-08-13 — Facet-Layer Completion (Workstream D)

> **DERIVED PROJECTION — conversation hand-off record.** Historical artifact, dated filename (C-012). Domain: KG (with GOV consequences). Author: Claude. Sources: this conversation (2026-08-13); Governance Protocol — Claude Series v0.10; Decision Register v0.6.

---

## 1. What this conversation was

The queued workstream **D** from the post-C agenda, taken up by Max directly ("let's continue with D"). Domain: KG. All four agenda items executed: facet minting, root-uniqueness scope, redirect semantics, route binding. Scan findings 3.3, 3.4, 8.1 retired.

## 2. Decisions made (ratified in-conversation per C-033, recorded in Protocol v0.10)

- **C-043** — Facets are **minted concepts**: `FACET` root + `FACET.TOPIC`/`.METHOD`/`.SOURCE_TYPE`/`.TIME`/`.AGENT` in the meta-facet (token `facet`); event-field tokens bound as `route` aliases. The Schema §5.1 table becomes a derived projection; new facets are vocabulary events, not schema edits.
- **C-044** — **Global root-uniqueness**: root segments form one namespace across all facets (one root, one meaning in every grep); full dotted codes globally unambiguous. Verified collision-free against the live store.
- **C-045** — **Redirect semantics + alias kinds**: reparent = re-`mint` on the same subject (parent-validated) + `alias(kind: redirect)` on the old code, in one commit; the fold resolves codes through redirect chains (log untouched). Kinds pinned: `label` (newest label = `title:`) / `route` (machine tokens — incl. `Fractal_<Name>` bindings from v0.3 forward; corpus `label` bindings grandfathered) / `redirect`.
- **C-046** — **Route binding exercised**: `KG`, `GOV`, `GBL`, `CTX` are live `alias(route)` bindings; the Context Index routing table is their projection (marked ⚭). `AST`/`ONT`/`WS`/`PROT` wait for workstream F.

Max's four structuring calls (recorded in v0.10 §3): mint facets; global scope; re-mint + explicit redirect; bind the four minted routes only. Ratification happened in this conversation (walkthrough + explicit acceptance).

## 3. Worth remembering (method note)

The **fold verifier caught a real design conflict before commit**: the first draft bound the new protocol's `Fractal_<Name>` as a `label` alias, which under the just-pinned newest-label rule would have displaced the protocol's title. Cure: `Fractal_<Name>` is a machine token → binds as `route` from v0.3 forward. First demonstration that the verification pass is a design instrument, not just a checksum.

## 4. Changes to the canonical layer (the repo)

| Artifact | Change |
|---|---|
| Node & Event Schema | **v0.3 new** (v0.2 banner: superseded). Facet minting (§5.1), global roots (rule 3), redirect semantics (rule 6), route rule exercised (rule 7), alias kinds + fold rules (§4.3). |
| Node Template | **v0.3 new** (v0.2 banner: superseded). Reparent-by-redirect worked example (§E). |
| Governance Protocol Claude v0.10 | **New** — records C-043–C-046; Ratified in-conversation. |
| Decision Register | v0.5 → **v0.6** (C-043–C-046; C-026/C-027 completion annotations; OQ-19 scope note). |
| Rule Overview | v0.3 → **v0.4** (grammar rules 3/6/8; alias kinds; unbound-routes caveat). |
| Context Index | v0.6 → **v0.7** (route-provenance note; ⚭ markers; v0.3 spec rows; PROT v0.1–v0.10). |
| KG Store | +30 events (118 total), +7 node files (35 total): 6 `FACET.*` TOP nodes + Protocol v0.10 DOC node; 4 topic roots gain `route:` aliases; 5 living-doc DOC nodes revised (new hashes, versionless titles). README: facet/redirect rules + redirect-check trace line. |
| Local Context (KG) | v0.10 → **v0.11** (D complete; **Next: workstream E**). |

Commits (C-037, author Claude): `[KG]` specs v0.3 + README → `[GOV]` governance layer → `[KG]` facet layer + route bindings + DOC revisions → `[CTX]` close.

**Machine verification (full store):** 118 events parse; every ULID prefix decodes into its `ts`/`created` second; global root-uniqueness holds (`AGENT`, `KG`, `GOV`, `GBL`, `CTX`, `FACET`); mint-before-use holds; every fold (placements, aliases, titles, TOP code/facet) matches the log; all six current external-doc hashes recompute; facet-registry body hash recomputes.

## 5. Refresh list (project mirrors, per C-004)

Refreshed this conversation: `Fractal_Decision_Register.md`, `Fractal_Rule_Overview.md`, `Fractal_Context_Index_v0.1.md`, `Fractal_Local_Context_Knowledge_Graph.md`. Unchanged: Global Context, Loose-Ends Scan mirror. Custom-Instructions stamp: unchanged (Conversation Settings still v0.3 — no action).

## 6. Unresolved / carried

- **Workstream E (queued next):** OQ-19 — mint-collision policy (now incl. root-mint races, C-044) + fold-verification ritual (this conversation's verifier is a working prototype); README grep precision (scan 5.3).
- **Workstream F:** the Architecture State hole (scan 2.1/2.2; OQ-12 residual); bind `AST`/`ONT`/`WS`/`PROT` routes (C-046 residual).
- Carried: OQ-3 (partition interval), OQ-4 (genuine transition), OQ-18, OQ-21.
- Minor (v0.10 §11): a projected one-page facet-registry view — on observed need.
- The repo-resident **skill** (shipping tier 1) stands as an offer — would dissolve OQ-16.

## 7. Next

**Workstream E — multi-writer safety** (see Local Context v0.11 agenda): collision policy, fold-verification ritual, single-writer retirement, README grep fixes. The skill tier and workstream F remain open offers.
