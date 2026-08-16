# Fractal Governance Protocol — Claude Series v0.24

**Topic:** The navigation architecture lands (C-068–C-070): the read side of the Knowledge Graph gets its own canonical contract — entry is a query shape (no home node), trace is bounded ranked recursion over four hops with a deterministic weight-product order, and the contract lives as `Fractal_Navigation_Contract` v0.1 under the Foundation, companion to the Schema (reissued v0.6 to register it and to discharge the C-061 documentation note). Solid, cheap, scalable navigation — specified on paper ahead of any build; the index tier stays deferred (C-021) with its trigger sharpened.
**Status:** Ratified (2026-08-14 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-14 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.23

---

## 1. Context

The first conversation opened by `/fractal`. Max chose the KG-as-architecture thread from the standing offers: *"we need to have a solid, cheap, scalable navigation system."* The assessment found the substrate sound — sorted dotted codes make prefix scans O(log n) by construction (Foundation §5); the log-canonical doctrine (C-019/C-024) makes any index disposable; redirects (C-045) make links immortal — but the read side unspecified: the Foundation named the deferred verbs (`place`/`trace`/`query-by-facet`) without contracts, and **entry** — where a navigator starts — was specified nowhere. Two conceptual holes, closed on paper in this conversation; building stays on observed need.

## 2. Questions investigated

1. Where does a navigator start? *(→ Nowhere special — the graph has lobbies everywhere; entry is three query moves over existing structure, §3 C-068.)*
2. What exactly does `trace` return? *(→ A bounded, ranked, deterministic neighbourhood — the primitive is the hop; ranking uses only existing fields, §3 C-069.)*
3. Where does the read contract live? *(→ Its own canonical versioned artifact under the Foundation — the Schema fixes what is written, the Contract how it is read; they refresh independently, §3 C-070.)*
4. Does this fire the C-021 build trigger? *(→ No — specifying is architecture, building waits. The trigger is sharpened: the index tier is built when inverted-view reads become routine, the mechanism behind "grep gets slow.")*

## 3. Decisions of record

- **C-068 — Entry is a query shape, not a structure (Max's call).** No entry nodes, no home screen in the graph. Entry = three moves over existing machinery: **enumerate the axes** (fold `FACET.*` — why C-043 mattered) · **descend by prefix** (parentage *is* the code prefix) · **rank landmarks by weight** (a landmark is a high-weight placement at a shallow code — §3.4's *central vs tagged* taken seriously). Consequences: the default lobby (`FACET`) is client configuration; the WS "entry-point nodes" idea dissolves into UI defaults (OQ-23 annotated); the Context Index is recognized as a hand-curated lobby; the inverted view becomes the load-bearing read behind the index tier's sharpened trigger. *(Working Decision.)*
- **C-069 — The trace contract (ranking rule = Max's call).** Four hops, all reading existing blocks: **out** (the fold) · **in** (the inverted fold) · **up/down** (the code string; structural hops weigh 1.0) · **resolve** (aliases/routes/redirects — free normalization, no depth, no weight). `trace(start, depth=2, …)` = bounded ranked recursion, never unbounded. **Path score = product of edge weights**; ties by shorter path → more recent terminal placement → terminal id — a total order from existing fields only, so any two conforming readers return the identical ranking (C-049's determinism standard applied to reads). Dedup at best path; no per-hop decay constant (revisit trigger recorded). Facets are independent; **entities are the junctions** — no cross-facet coordinate edges. Derivation = a role-filtered trace (`derived-from`), not a verb. Redirects: accept stale, emit canonical. History (`revise` chains) is a separate log-walk verb, outside trace. Read surface: **`resolve` · `enter` · `trace` · `history`** (`query-by-facet` ≡ `enter` with filters; `place` stays a write verb). *(Working Decision.)*
- **C-070 — The read side is its own canonical contract (Max's call).** `Fractal_Navigation_Contract` v0.1 lands as a canonical **versioned artifact** (C-012/C-040/C-061 class) under the Foundation, **companion** to the Schema: Schema = what is written, Contract = how it is read, cross-linked, refreshing independently — read-contract churn never forces a Schema reissue. **Schema reissued v0.6** to register the companion (pointers at §0/§3.4/§3.6/§4.4) and to discharge the standing C-061 documentation note (§2.2 now states per-version DOC identity in the spec's own text); **no format change**; Template v0.4 coupling checked — unchanged (C-059). Implementation tiers pinned in the Contract §6: Tier 0 grep (live, conformant), Tier 1 index = `verify.py`'s fold persisted (spec for any build or C-066 drone brief = the invariant suite + the Contract), Tier 2 Galaxy UI (OQ-23). *(Working Decision.)*

## 4. Executed this close (one `[KG]` commit with the v0.25 rider, C-037; push = Claude, C-064)

- **`Fractal_Navigation_Contract_v0.1.md`** landed at `/Claude/Architecture/Concepts/Knowledge Graph/` — ratified in-conversation; series DOC + per-version DOC minted (C-061 treatment from birth), route aliases bound.
- **Schema v0.6** landed beside it (per-version DOC minted; series pointer revised); v0.5 stays as history with its own identity.
- **Architecture State → v0.6** — §2 gains the read-side contract line and cites the current spec versions.
- **`verify.py`** header citation cured to v0.6; **`check_versions.py`** gains the `navigation` SERIES entry (+ the v0.6 successor of a ratified SUPPRESS pair).
- Ledgers and contexts per the C-059 walk (see the Local Context v0.33 checklist and Protocol v0.25 for the GOV rider).

## 5. Calls recorded (Max, 2026-08-14, this conversation)

1. **Entry:** accept "entry is a query shape" (over adding a curated `SET` entry set — available later as ordinary structure on observed need).
2. **Ranking:** weight product with length/recency tie-breaks (over a per-hop decay constant — a tunable with no observed need).
3. **Home:** dedicated canonical doc + Schema reissue linking to it (over folding navigation into the Schema). Max's version slip corrected in-conversation to the next in sequence (v0.6).

## 6. Ratification record (2026-08-14, in-conversation per C-033)

Max opened the thread ("time to talk about the KG… solid, cheap, scalable navigation"), took the assessment, directed the design ("start with 1. and 2."), made the three calls explicitly, and ratified the drafted documents ("ratified") after review. Claude executed, committed as attributed author (C-037), pushed per C-064. No caveats.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None opened. **OQ-23 annotated** (entry-point nodes → UI defaults over C-068; the WS forge trigger itself unchanged). Standing items carry: OQ-4, OQ-9, OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27. The review ledger stays fully green.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.24 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.24 |
| Status | Ratified (2026-08-14, in-conversation per C-033) |
| Domain | KG (recorded in the GOV history layer) |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-14, this conversation) |
| Date | 2026-08-14 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.23 |
| Related Documents | Fractal_Navigation_Contract_v0.1.md; Fractal_Node_and_Event_Schema_v0.6.md; Knowledge Path Foundation v0.1; Architecture State (stamp inside, C-012); Decision Register (stamp inside, C-012); Local Context v0.33; Protocol v0.25 (the GOV rider of the same close) |
| Document ID | DOC-01M00TD1H2ZRY8YKHEPCJK6CVC (minted 2026-08-14, C-041, per this protocol) |
