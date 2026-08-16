# Fractal Navigation Contract

> **CANONICAL — Claude-era read-side specification (Domain KG).** Fixes how the FRACTAL graph is *read*: entry, hops, trace semantics, ranking, redirect discipline, and history walks. Companion to the Node & Event Schema — the Schema fixes what is **written**, this contract fixes how it is **navigated**; the two refresh independently. Derived from the two-relation core of the Knowledge Path Foundation; it introduces **no new stored structure** — every clause is a query shape over blocks the Schema already fixes. This document is the source of truth for read behaviour; every implementation tier (the zero-infra grep ritual, the index server, the Galaxy UI) is a derived realisation checked against it.

**Fractal_Navigation_Contract** · **Version:** 0.1 · **Status:** Ratified (2026-08-14, in-conversation per C-033) · **Updated:** 2026-08-14 · **Domain:** KG · **Author:** Claude · **Parent:** Fractal Knowledge Path Foundation v0.1 · **Companion:** Fractal Node & Event Schema v0.6

**Decision status legend:** *Principle* (accepted, load-bearing) · *Working Decision* (accepted) · *Deferred* · *TBD*.

---

## 0. What this document is (and is not)

The Foundation named the deferred index server's verbs (`place`, `trace`, `query-by-facet`) but never wrote their contracts; entry — where a navigator *starts* — was never specified at all. This document closes both gaps **on paper, ahead of any build**: navigation is solid when its behaviour is fixed independently of implementation, cheap when it adds no machinery, and scalable when its cost bounds follow from the substrate's own design (sorted codes → prefix scans).

It fixes three things and only these three:

1. the **entry rule** — how navigation begins (§1);
2. the **hop table and trace contract** — how the graph is traversed and results ranked (§2–§3);
3. the **read surface** — the four verbs any conforming reader exposes (§5).

It does **not** specify storage (the Schema's job), and it does **not** mandate a build: the index server and the UI remain Deferred per C-021, built on observed need. A conforming implementation at any tier must return the same answers this contract defines — grep by hand and the index server disagree with each other only if one of them is wrong.

---

## 1. The entry rule — entry is a query shape (C-068)

*Working Decision (Max's call of record, 2026-08-14).* **The graph has no entrance; it has lobbies everywhere.** Entry is not a designated node, a home screen, or any stored structure — it is three query moves over structure that already exists:

1. **Enumerate the axes.** The meta-facet `FACET` is the lobby of lobbies: the fold of `FACET.*` lists every axis that exists (`topic`, `agent`, `method`, `source-type`, `time`, …). C-043 made the facets minted concepts; this move is why that mattered.
2. **Descend an axis.** Children of a code are a one-level prefix scan — parentage *is* the code prefix (Schema §5.2). `GOV` → `GOV.*` one segment deeper, recursively, to any depth.
3. **Surface the landmarks.** At any coordinate, rank its inhabitants by **weight** (desc), then recency, then id (the §3.2 order). A landmark is nothing but a high-weight placement at a shallow code — `weight: 1.0` at `KG` *means* "central to the Knowledge Graph domain," and that is exactly what an arriving navigator sees first. Weight (Schema §3.4) exists to distinguish *central* from *tagged*; entry is its first systematic consumer.

**Consequences of record:**

- **No home node, ever.** Which lobby a client opens on is presentation configuration, not graph structure. The natural default is `FACET` itself — the root of roots. The Architecture State's "entry-point nodes" idea (WS) resolves into UI defaults over this rule, not into new node types.
- **The inverted view becomes load-bearing.** Moves 2–3 read *coordinate → inhabitants* — the direction the node files deliberately do not materialize (Schema §3.6). This is the honest trigger for the index tier (§6): not "grep got slow" in the abstract, but "the inverted view became a routine first-class read."
- **The Context Index is a curated lobby.** It hand-maintains, for the governance corpus, exactly the projection moves 2–3 define. Its status is unchanged (derived projection, C-012); the mechanism it hand-implements is now a contract any client can run against any domain.

## 2. The hop table

*Working Decision (C-069).* The traversal primitive is the **hop**. Four hop types, each reading a block the Schema already fixes; no hop writes anything.

| Hop | Direction | Reads | Weight of the hop |
|---|---|---|---|
| **out** | entity → its placement targets | the fold (`placements:`) | the placement's `weight` |
| **in** | coordinate/entity → subjects placed at/in it | the inverted fold of the same edges | the placement's `weight` (same edge, reverse view) |
| **up / down** | code ↔ parent / children | the code string itself (prefix) | `1.0` (structural — the tree is definitional) |
| **resolve** | alias / route / stale code → id + canonical code | `alias` events, redirect chain | not a hop — free normalization, contributes no depth and no weight |

`resolve` accepts every handle class the Schema defines: a `TYPE-ULID` id, a dotted code in any facet, a `route` token (Index codes, facet tokens, `Fractal_<Name>`s), or a superseded code (walked transitively through `redirect` aliases, Schema §5.3 rule 6). Ids, codes, and routes resolve exactly or not at all; **label** lookup returns a candidate set — labels are aliases, not identifiers (Principle 6), and are never assumed unique.

## 3. The trace contract (C-069)

*Working Decision (ranking rule = Max's call of record, 2026-08-14).* A **trace is bounded, ranked recursion over hops.**

### 3.1 Shape

`trace(start, depth = 2, direction = both, filters = none)` returns the ranked neighbourhood of `start` within `depth` hops (`out`/`in`/`up`/`down` each count one; `resolve` counts zero). **A trace is never unbounded**: deep traversal is the caller recursing explicitly — the system's job is one honest neighbourhood at a time. Filters restrict by `role`, `facet`, and/or entity `type`; they narrow which hops participate, nothing else.

### 3.2 Ranking (the pinned order)

**Path score = the product of edge weights along the path.** Ties break by, in order:

1. higher path score;
2. shorter path (fewer hops);
3. more recent terminal placement (`ts` of the edge's event);
4. terminal id, lexicographic.

The order is total and computed from existing fields only, so **any two conforming readers return the identical ranking for the same log** — the same determinism standard C-049 set for the fold. Semantics come free: a chain of *central* placements (1.0 × 1.0) outranks anything routed through a loose tag (× 0.3). There is **no per-hop decay constant**: depth is already bounded, and a tunable we have not observed a need for is exactly what the credo says not to add (revisit trigger in §7).

**Deduplication:** a node reachable by several paths within depth appears **once**, at its best path under the order above. Cycles terminate by the same rule — bounded depth plus visit-once.

### 3.3 Facets are independent; entities are the junctions

**No edge links coordinates across facets** — parentage is intra-facet prefix, and placements target coordinates *or* entities, never coordinate-pairs. An **entity is the junction where axes meet**: a trace crosses from `PHY.*` to `ECON.*` only by passing through an entity placed in both. This is the Foundation's nuclear-paper story made a rule: the physicist and the economist meet *at the entity*, and cross-facet traversal is well-defined rather than accidental.

### 3.4 Derivation is a filter, not a verb

"Where did this come from" = `trace(id, roles = [derived-from], direction = out)` — walking the edges `run` events materialize (Schema §4.4), output → input, backward to sources. `direction = in` from an entity finds its products. The reasoning-process promise is delivered by a *filter parameter*; no provenance machinery exists beyond the one edge type.

### 3.5 Redirect discipline — accept stale, emit canonical

Any code accepted anywhere in the read surface resolves through the redirect chain before use; **results always carry current canonical codes** (with the redirect noted when the input was stale). Result entries carry the id, the canonical presentation from the fold (title, canonical codes), the best path, and its score — never a superseded code as if current. Links stay immortal at the query layer exactly as C-045 made them at the log layer.

## 4. History — the log walk (outside trace)

*Working Decision (C-069).* "How did this thing change" is a **log question, not a placement question**, and gets its own small verb: `history(id)` returns the events whose `subject` is the id, in `ts` order, with the version chain made explicit — `create` → `revise` → … walked via `supersedes` (Schema §4.3), each version with its `content_hash`. No hop, no ranking, no depth: the answer *is* the chain. Keeping it out of `trace` keeps both contracts one-purpose.

## 5. The read surface

Four verbs; a conforming reader exposes exactly these semantics (naming may adapt to the client):

| Verb | Question it answers | Defined in |
|---|---|---|
| `resolve(handle)` | *what is this?* → id + canonical code(s) | §2 |
| `enter(nothing \| facet \| code)` | *where am I / what's here?* → axes · root vocabulary · children + ranked inhabitants | §1 |
| `trace(start, …)` | *what is this near, and how?* → ranked neighbourhood with paths | §3 |
| `history(id)` | *how did this change?* → version/event chain | §4 |

The Foundation's heritage triple maps cleanly: **`query-by-facet` ≡ `enter` at a coordinate with filters**; `trace` is refined above; **`place` is a write verb** and stays on the Schema's side of the line (§4–§5 there, guarded by `mint.py`). This contract is read-only end to end.

## 6. Implementation tiers & the sharpened trigger

*Working Decision (C-070 context; build discipline unchanged — C-021).* The contract has tiers of realisation, all checked against the same clauses:

- **Tier 0 — the grep ritual (live today).** Axes = grep `mint` events with `parent: FACET`; children = grep the code prefix in mints; inhabitants = grep the code across log + front-matter, redirect list first (Schema §3.6); ranking by hand. At the current scale (67 nodes / 300 events) Tier 0 is conformant by inspection, and remains the fallback at any scale — the contract is *executable by a human reading plain text*, which is the zero-infra promise kept.
- **Tier 1 — the index server (Deferred).** The persisted fold: `verify.py` already replays the log and builds the complete fold in memory on every run; the index is that fold persisted (SQLite — Python stdlib, zero new dependencies) and exposed as the four verbs. It is a **disposable projection rebuilt on boot** (C-019) — no incremental sync, no cache invalidation, no drift *by construction*; rebuild-on-boot stays sub-second well past the 50k-event tripwire. Spec for any build (including a C-066 drone brief): **the `verify.py` invariant suite + this contract.**
- **Tier 2 — the Galaxy UI (Deferred, OQ-23).** Opening a node's container face = `enter`; the split-screen dream is `trace` rendered spatially. Rides the WS forge.

**The build trigger, sharpened:** the index tier is built when **inverted-view reads (entry moves 2–3, `in` hops) become routine work rather than occasional lookups** — the store materializes only the outward direction, so these are the first reads grep stops serving at honest cost. "Tracing-by-grep gets slow" remains the umbrella; this names the mechanism that will make it fire.

## 7. Open questions & deferred

*TBD:* none blocking. *Revisit triggers:* a per-hop decay constant — add only if weight-product ranking observably misorders real traces (§3.2); mixing recency into `enter`'s primary landmark rank — observe first. *Implementation-tier concerns, out of contract scope:* result pagination/limits; label full-text search (an index-tier convenience — the contract's `resolve` handles labels only as candidate sets). *Deferred:* Tier 1 and Tier 2 builds (C-021, trigger per §6).

## 8. Decisions captured (proposed this session, 2026-08-14)

- **C-068 — Entry is a query shape, not a structure.** No entry nodes, no home screen in the graph: entry = enumerate the axes (`FACET.*`) · descend by prefix · rank landmarks by weight. Client default lobby is presentation configuration; the WS entry-point idea resolves into UI defaults over this rule.
- **C-069 — The trace contract.** Four hops (out / in / up-down / resolve); trace = bounded ranked recursion (default depth 2); **path score = product of edge weights**, ties by length → recency → id, dedup at best path; facets independent, entities the junctions; derivation = role-filtered trace; redirects accept-stale / emit-canonical; history is a separate log-walk verb.
- **C-070 — The read side is its own canonical contract.** Navigation lands as `Fractal_Navigation_Contract` (versioned artifact, C-012/C-061) under the Foundation, companion to the Schema: Schema = what is written, Contract = how it is read, cross-linked, refreshing independently. Schema v0.6 registers the companion; read-contract churn never forces a Schema reissue.

---

**Refresh triggers:** a change to the entry rule, the hop table, the ranking order, the facet-junction rule, the redirect discipline, the verb surface, or the tier/trigger doctrine. *(A new facet or new role changes nothing here — the contract quantifies over whatever the Schema registers.)*
**Sources:** Fractal Knowledge Path Foundation v0.1 (§5 efficient tracing, §6 shells); Fractal Node & Event Schema v0.5→v0.6 (§3.4 weight, §3.6 inverted view, §4.4 runs, §5.2 code shape, §5.3 redirects); verify.py (the fold it replays); this conversation (2026-08-14 — Max's calls: entry as query shape; weight-product ranking with length/recency tie-breaks; dedicated contract doc with Schema v0.6 linking).
**Revision history:** v0.1 (2026-08-14) initial read-side contract: entry rule, hop table, trace contract, history verb, read surface, tiers + sharpened trigger (C-068–C-070 proposed).
