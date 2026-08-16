# Fractal Node & Event Schema

> **CANONICAL — Claude-era format specification (Domain KG).** Fixes the plain-text on-disk format that makes FRACTAL hand-usable with zero infrastructure: the node front-matter schema, the append-only event-log line format, and the facet-code allocation rules. Derived directly from the two-relation core of `Fractal_Knowledge_Path_Foundation_v0.1.md`; this document is the source of truth for the format. Project docs and context packages are derived projections of it.

**Fractal_Node_and_Event_Schema** · **Version:** 0.2 · **Status:** Ratified (2026-08-12, in-conversation per C-033; contents pinned by C-039/C-040) · **Updated:** 2026-08-12 · **Domain:** KG · **Author:** Claude · **Parent:** Fractal Knowledge Path Foundation v0.1 · **Supersedes:** Fractal_Node_and_Event_Schema_v0.1.md

> **SUPERSEDED (2026-08-13):** reissued as `Fractal_Node_and_Event_Schema_v0.3.md` (C-043–C-046, per Protocol v0.10). Retained as history under C-012; do not author against this version.

**Decision status legend:** *Principle* (accepted, load-bearing) · *Working Decision* (accepted) · *Deferred* · *TBD*.

> **Why v0.2 exists (version-bump discipline).** v0.1 was substantively revised on 2026-08-12 without a version bump — a violation of C-005 flagged by the Loose-Ends Scan (finding 1.2). This reissue cures it and fixes the rule going forward: **canonical specifications are versioned artifacts under C-005 — every substantive change is a new version with a new file** (they are not on the C-012 living-projection list). v0.2 additionally pins what v0.1 left TBD: the ULID profile, `content_hash`, the `revise` referent, `actor` semantics, the TOP `facet:` field, and entity-target placements (C-040), and records the identity bridge to canonical documents (C-041).

---

## 0. What this document is (and is not)

This is step 1 of the KG build sequence (C-021): **spec the format first, defer code and UI to observed need.** It specifies exactly enough for a human — or a model reading the folder — to *place* an item and *trace* it by reading plain text, with no index server and no database. Everything here is a block added back onto the essential rule of the Foundation (§3: *two relations, one log*); nothing here introduces a new rule.

It fixes three things and only these three:

1. the **node** — how an Entity is written on disk (§3);
2. the **event log** — how every placement and change is recorded, append-only (§4);
3. the **facet codes** — how the coordinate namespaces are allocated and evolved (§5).

It does **not** specify the index/MCP server or the UI. Those remain Deferred per the Foundation and C-021.

---

## 1. Orientation — the two relations on disk

From the Foundation (§3), the whole system is two relations in one append-only log:

- **Identity** — *a thing exists.* One Entity, one immutable `TYPE-ULID` key. Topics/concepts are Entities too (`TOP-…`); the taxonomy is made of the same stuff it classifies.
- **Placement** — *a thing is placed within another thing, with a role and a weight.* One edge type expresses classification, containment, citation, authorship and membership — they differ only by `role`.

On disk this becomes exactly two kinds of text:

| Relation | On disk | Character |
|---|---|---|
| Identity | a **node file** (§3) — one per Entity, YAML front-matter + optional body | born once, immutable identity fields |
| Placement + all change | the **event log** (§4) — append-only JSONL | append-only, never edited in place |

**The load-bearing rule that ties them together (§4.5): the event log is canonical. A node's `placements:` block is a *materialized fold* of the log for that node** — a human-readable convenience carried in the node so the folder is legible without tooling. Where the two disagree, the log wins. This keeps Principle 5 (*provenance is recorded by an event log*) intact while still letting you read a node and see where it sits.

---

## 2. Types & identifiers (the confirmed scheme)

*Principle (separation) · Working Decision (scheme — **C-015 confirmed 2026-08-12 as C-039**, resolving OQ-14).* Two handles per Entity, per Foundation §4:

- **Canonical key** `<TYPE>-<ULID>` — immutable, opaque, time-sortable, no central coordinator. Registered type prefixes (open-ended):

  | Prefix | Entity |
  |---|---|
  | `DOC` | document / living text |
  | `NUM` | a specific number / measured value |
  | `FN`  | a function / operator definition |
  | `PER` | a person / agent |
  | `IMG` | an image / figure |
  | `TBL` | a table |
  | `SET` | a collection / set |
  | `TOP` | a topic / concept node (a coordinate in a facet) |
  | `EVT` | an event-log entry (events are addressable too) |

- **Names / codes** — every human label or routing code is an **alias** over the key, never the key itself (Principle 6).

**Choosing rule (git's lesson):** does identity survive a content change? Yes → stable ULID identity (living doc, person). No → content hash (a frozen version, a specific value). A living `DOC-…` keeps its ULID; *each version* is content-hashed underneath it (§3.2).

### 2.1 ULID profile (pinned, C-040)

The ULID is the **standard 26-character ULID**: 128 bits encoded in Crockford base32 (alphabet `0123456789ABCDEFGHJKMNPQRSTVWXYZ` — no `I L O U`), uppercase.

- **Characters 1–10** encode a **48-bit millisecond Unix timestamp**; **characters 11–26** encode **80 bits of randomness**.
- **Coherence rule:** the timestamp prefix of an event id must decode **into the second recorded as** that event's `ts`; the prefix of a node id likewise into its `created`. (`ts`/`created` carry second granularity; sub-second precision lives only in the id — the store's bootstrap batch, at +1 ms, is exactly conformant.) This is what makes ids time-sortable and lets any reader verify the log's internal consistency by decoding.
- **Generation method (named, so hand-authoring stays possible):** any standard ULID tool, or the dependency-free reference one-liner documented in the Knowledge Graph Store `README.md`. Hand-*writing* a ULID without a tool is not supported — 10–16-character placeholders (as in Template/Schema v0.1 examples) are **invalid** and must never be minted.

### 2.2 The identity bridge to canonical documents (C-041)

Two identity systems existed side by side: `Fractal_<Name>_v<major>.<minor>` (C-005, for exported artifacts) and `TYPE-ULID` (this schema). The bridge:

- **Node files *are* the identity system.** Files under the Knowledge Graph Store are not "exported artifacts" in the sense of C-005 rule 7 — they carry `TYPE-ULID` identity and are exempt from `Fractal_<Name>` naming.
- **Canonical documents are minted as `DOC` nodes.** A canonical document's persistent ID **is its `DOC-…` node id**; its `Fractal_<Name>` identity is bound to that node as an **alias** (`kind: label`). The DOC node's `content_hash` freezes the file's current version; its body carries the repo-relative path.
- **"Document ID: TBD" is retired.** Control tables record the minted `DOC-…` id. New canonical documents get their DOC node minted at or shortly after first commit.

---

## 3. The node file

### 3.1 File & naming

A node is one UTF-8 text file: **YAML front-matter** (the identity + materialized placements) followed by an optional Markdown **body** (the human content, for `DOC`/`TOP`; may be empty for `NUM`/`PER`/etc.).

- **Filename:** `<id>.md`, optionally `<id>--<slug>.md` where `<slug>` is a lowercase human hint. The `id` prefix makes the file greppable and stable; the slug is an alias and may change freely (renaming the file never changes identity). Example: `DOC-01KZVNA1710NXFC07PPK18X9C5--facet-registry.md`.
- **Location:** under the repository's node store. Physical foldering is navigation only, never identity — a node's *real* placements live in its `placements:` block and the log, not in which directory it happens to sit.

### 3.2 Front-matter schema

```yaml
---
# ── Identity (immutable; mirrors the `create`/`mint` event) ───────
id: DOC-01KZVNA1710NXFC07PPK18X9C5  # REQUIRED. Persistent Object ID. TYPE-ULID (§2.1). Never changes.
type: DOC                          # REQUIRED. Must equal the id prefix. One registered type.
created: 2026-08-12T18:56:12Z      # REQUIRED. Birth timestamp, ISO-8601 UTC (the id's prefix decodes into this second).
created_by: AGENT.AI.CLAUDE        # REQUIRED. Authoring agent (agent-facet code; kind branch marks human/AI).

# ── Version / integrity (per version; optional for pure concepts) ─
content_hash: sha256:9f2b…          # OPTIONAL. Hash of THIS version (§3.6). Omit for TOP.
version_of: ~                       # OPTIONAL. If this file is a frozen snapshot, the living id it snapshots.

# ── Aliases (mutable; human-facing) ──────────────────────────────
title: "Facet Registry — C-026/C-027"      # OPTIONAL. Human label. An alias, not identity.
aliases: []                                # OPTIONAL. Other labels / routing codes (fold of `alias` events).
code: ~                                     # TOP nodes only: the concept's own code (mirrors its `mint`).
                                            #   Parentage is the code PREFIX (PHY.QM.QFT's parent is PHY.QM).
facet: ~                                    # TOP nodes only: the facet the code lives in (mirrors its `mint`).
                                            #   REGISTERED in v0.2 (was store practice, unspecified — scan 6.1).

# ── Placements (MATERIALIZED FOLD of the log for this id) ─────────
# Each entry = one outward edge: this entity --role--> a coordinate (facet+code) or an entity (§3.5).
# This block is a projection of the event log; the log is canonical (§4.5).
placements:
  - facet: topic          # which independent namespace/axis (§5.1)
    code: PHY.QM.QFT       # coordinate in that facet: a dotted concept code (§5)
    role: about            # role of the edge (§3.3)
    weight: 1.0            # centrality in [0,1] (§3.4)
  - facet: agent
    code: AGENT.HUMAN.MAX
    role: by
    weight: 1.0
  - code: DOC-01KZVYPW5GQRZM0QV6450B8T3T   # entity target (§3.5): code carries the id; facet omitted
    role: cites
    weight: 1.0
---
```

Only `id`, `type`, `created`, `created_by` are required. Everything else is added back as the item warrants it. A bare stub (identity only, empty `placements`) is a valid node.

**TOP nodes carry `code:` *and* `facet:`** — both mirror the `mint` event, and both follow the canonical-source rule: on disagreement with the log, **the log wins** (they are *not* part of the §4.5 identity exception).

### 3.3 Role vocabulary (v0.2 — unchanged from v0.1)

One edge, differentiated by `role`. Registered roles:

| Role | Meaning | Typical target |
|---|---|---|
| `about` | subject / classification | `topic` coordinate |
| `in` | containment — subject is inside target | `topic` coordinate or an entity (a `TBL`, a `DOC`) |
| `cites` | subject cites target | any entity |
| `by` | authorship — subject authored by target | `agent` coordinate |
| `member-of` | subject is a member of a collection | a `SET` entity |
| `is-a` | typing within a facet | `source-type`, `method` coordinate |
| `derived-from` | provenance — subject was produced from target (written by `run`, §4.4) | any entity |

New roles are added by registering them here in a later version; the machinery does not change.

### 3.4 Weight

`weight ∈ [0,1]` — how central the placement is. `1.0` = definitive / core; lower = looser / peripheral. It is what distinguishes *central to* a topic from *merely tagged*, and lets a trace rank neighbours. Default when omitted: `1.0`.

### 3.5 Placement targets: coordinates and entities (pinned, C-040)

A placement's target is one of exactly two things, distinguished by what the `code` field holds:

- **A coordinate** — `facet` names the axis, `code` is a dotted concept code (`PHY.QM.QFT`). The normal case for `about`, `by`, `is-a`.
- **An entity** — `code` carries the target's **entity id** (`TYPE-ULID`); `facet` is omitted (or `~`). The case for `cites`, `member-of`, `derived-from`, and `in` when the container is an entity.

The two are unambiguous by shape: ids match `TYPE-<26-char ULID>`, codes are dotted uppercase paths — so one grep still finds every reference to either. No new field, no new mechanism.

### 3.6 Edge direction & the inverted view

Placements are written **outward** (subject → target). The reverse view (target → its subjects) is not stored in nodes; it is recovered by folding the log (or, later, from the index's inverted table). At zero infra you find "everything placed at `PHY.QM.QFT`" by grepping the log / node front-matter for that code.

### 3.7 `content_hash` (pinned, C-040)

`content_hash` is `sha256:<64 lowercase hex digits>` and freezes **one version** of an entity's content. What is hashed:

- **Store node with a body** — the byte-exact UTF-8 **body**: everything after the front-matter's closing `---` delimiter *and its trailing newline*, through end-of-file. Hashing the body only (never the front-matter) keeps the hash stable while the mutable fold (`placements:`, `aliases:`) and the hash field itself change.
- **DOC node representing an external canonical file** (§2.2) — the **whole file's bytes** at the recorded version, exactly as committed to git. The node body states the repo-relative path.

A `create` event may carry the first version's hash; each subsequent version is recorded by a `revise` event (§4.3). Verification = recompute and compare; the first worked example is the store's facet-registry DOC (hashed 2026-08-12, C-042).

---

## 4. The event log

### 4.1 Shape

*Working Decision (plain-text log and this line format — C-023).* One **append-only JSONL** stream: one JSON object per line, one event per line, **never edited or deleted**. To change anything you append a new event (§4.6). This is the canonical record of identity births and every placement.

- **Physical layout:** the log is **partitioned** into time-bucketed files `_events/<bucket>.jsonl`. "One log" is conceptual; partitioning keeps files small and makes git merges of concurrent appends near-conflict-free. **The partition interval is TBD** (C-023 / OQ-3): monthly (`_events/2026-08.jsonl`) is a candidate shown for illustration, not a fixed decision — the bracket size is chosen later from observed volume, which the git history now accrues.
- **Ordering:** events are applied in `ts` order. `EVT-ULID` ids are themselves time-sortable, breaking ties deterministically.
- **What counts as an event (commit granularity):** the log records **committed** facts, not keystrokes. **The git commit is the event boundary (C-037, resolving OQ-15):** working edits are invisible to history until a coherent change-set is committed, at which point the corresponding events are recorded. The append-only/never-edit rule (§4.6) therefore governs *committed events*, not in-progress editing.

### 4.2 Common fields (every line)

| Field | Req | Meaning |
|---|---|---|
| `ev`  | ✔ | verb (§4.3) |
| `id`  | ✔ | this event's own id, `EVT-<ULID>` (§2.1) — events are addressable Entities |
| `ts`  | ✔ | ISO-8601 UTC timestamp, second granularity (the id's prefix decodes into this second) |
| `actor` | ✔ | agent-facet code, e.g. `AGENT.HUMAN.MAX`, `AGENT.AI.CLAUDE` — see semantics below |
| `subject` | ✔ | the primary Entity id the event is about |
| `supersedes` | — | id of a prior event this one overrides (§4.6) |
| `note` | — | free-text human rationale |

**`actor` semantics (pinned, C-040):** `actor` is **the agent that committed the event to the log** — the executor, not the decision-maker. Decision provenance, when it differs, goes in `note` (e.g. `"note": "scope chosen by Max"`). This resolves the bootstrap batch's ambiguity (scan 3.5): those events stand as written; from v0.2 on, one convention.

### 4.3 Verbs

| Verb | Adds fields | Effect |
|---|---|---|
| `create` | `type`, `content_hash?`, `title?` | births an Entity (mirrors node identity front-matter) |
| `place`  | `facet?`, `code`, `role`, `weight` | adds one placement edge from `subject` (coordinate or entity target, §3.5) |
| `unplace`| `facet?`, `code`, `role` (or `supersedes`) | retracts a placement previously added |
| `mint`   | `facet`, `code`, `parent`, `label` | allocates a new concept code, binding it to `subject` (a `TOP-…`) |
| `alias`  | `alias`, `kind` (`label`/`route`) | binds/rebinds a human label or routing code to `subject` |
| `revise` | `content_hash`, `supersedes` | records a new version of a living Entity |
| `run`    | `operator`, `inputs:[id]`, `outputs:[id]` | records an Operator execution; appends `derived-from` edges output→input (§4.4) |

**`revise.supersedes` referent (pinned, C-040):** `supersedes` names the **event id** (`EVT-…`) of the prior version's `revise` (or, for the first revision, the `create`). One supersede semantics everywhere in the log — never a content hash. The version *chain* is walked through events; the hashes hang off them.

The verb set is intentionally small; new verbs are added only when an observed need forces one.

### 4.4 Operator runs = provenance

*Working Decision (from Foundation §6).* When an Operator runs, a single `run` event records `inputs`, the `operator`, and `outputs`. From it the fold materializes `derived-from` placements on each output pointing at its inputs. Trace backward from any `NUM` through its `derived-from` chain to recover the full derivation to sources — "preserve the entire reasoning process, not just results," delivered by the same one mechanism.

### 4.5 Canonical-source rule (the load-bearing decision here)

*Accepted — C-024 (load-bearing).* **The event log is authoritative. Node `placements:` is a materialized fold of the log for that node.**

- To **place by hand at zero infra:** append a `place` line to the current bucket's log, then reflect the same edge in the node's `placements:` block. Two writes, one truth.
- On any disagreement, the **log wins**; the front-matter is regenerated from the log (by hand, or by the index once it exists). This covers `placements:`, `aliases:`, `title:`, and — for TOP nodes — `code:`/`facet:` (§3.2).
- Identity fields (`id`, `type`, `created`, `created_by`) are the exception: they are canonical *in the node* and merely mirrored by the `create` event — identity is born with the file.

*Alternative considered (open, §6):* make front-matter the hand-authored primary and treat the log as a journal generated from front-matter diffs. Rejected as the default because it demotes the event log below Principle 5; recorded here so Max can overturn the default with one decision.

### 4.6 Supersede semantics

Append-only means **correction is a new event, never an edit or delete.** To override, append an event whose `supersedes` points at the prior event's `id` (or, for placements, an `unplace` naming the same `facet`+`code`+`role`). The **current state** of any Entity is the fold: apply its events in `ts` order; a later event with `supersedes` replaces the effect of the one it names. Nothing is ever lost — the superseded event stays in the log as history. This is how reclassification, reweighting, retitling and reparenting all happen without breaking a single reference.

---

## 5. Facet codes

> **Accepted (C-026 / C-027, 2026-08-12).** The facet registry is resolved: it is the **browsable, log-derived projection of the concept nodes (`TOP-…`) that serve as coordinates**, grouped by facet — not a separately-authored control file (consistent with C-019 "index is a derived cache" and C-024 "log is canonical"). It has two tiers: a small set of **facets** (independent axes) and an open, growing **vocabulary of coordinates** minted within them; the "browsable library / source-style index" is the inverted fold over these. The facet set, the role vocabulary (§3.3), weight, and the allocation rules (§5.3) below are **accepted** (grammar fixed; vocabularies extend on observed need). Ratified in Governance Protocol — Claude Series v0.6.

### 5.1 Facets are independent namespaces

*Working Decision (Foundation §5).* Coordinates live in several **independent axes** at once, not one master tree. Registered facets (v0.2):

| Facet | Axis | Root code(s) |
|---|---|---|
| `topic` | subject matter | domain roots: `KG`, `GOV`, `GBL`, `CTX`, `PHY`, `ECON`, `BIO`, … |
| `method` | how it was produced/investigated | `METH` (e.g. `METH.EXPERIMENT`, `METH.SIMULATION`) |
| `source-type` | what kind of source it is | `SRC` (e.g. `SRC.PAPER.PREPRINT`, `SRC.DATASET`) |
| `time` | temporal placement | `TIME` (e.g. `TIME.2026.Q3`) |
| `agent` | actors (authorship/provenance) | `AGENT`, **branched by kind:** `AGENT.HUMAN.<name>`, `AGENT.AI.<name>` (e.g. `AGENT.HUMAN.MAX`, `AGENT.AI.CLAUDE`) |

An Entity carries coordinates in as many facets as are honestly true of it. New facets are registered here when an observed need appears. *(Whether facets themselves should be minted under a `FACET` root, and the scope of root-uniqueness, are queued workstream-D questions — scan 3.4.)*

**Agent facet — branched by kind (C-026).** The `agent` axis is confirmed as a facet: authorship is the `by` *role*, and the facet is the browsable *who*. Its top branch is the human/AI distinction — every agent is minted under `AGENT.HUMAN` or `AGENT.AI` — so "everything by a human" (`AGENT.HUMAN.*`) or "by an AI" (`AGENT.AI.*`) is a one-pass prefix filter. No separate `agent-kind` facet: kind is intrinsic to the agent, so a parallel axis would only duplicate it and risk drift.

### 5.2 Code shape

A code is a **dotted path** of uppercase segments — `PHY.QM.QFT`, `ECON.ENERGY.NUCLEAR` — of arbitrary depth. Each segment matches `[A-Z0-9]([A-Z0-9_]*[A-Z0-9])?`; segments are joined by `.`. The **code is a stable token, not a label**: it references a concept `TOP-…`, and the concept's human name is a separate alias. Renaming "Economics" touches zero placements.

Because codes are hierarchical and kept sorted, "everything under physics" is a **prefix scan** `PHY.*` — O(log n), not a full scan. **Concept parentage is carried by the code prefix itself** (`PHY.QM.QFT`'s parent is `PHY.QM`), not by a separate placement edge; the `mint` event's `parent` field only records and validates that binding at birth. A `TOP` node therefore stores its own coordinate in the front-matter `code:` (and `facet:`) fields and needs no self-placement.

### 5.3 Allocation rules

1. **Mint before use.** A new segment is created by a `mint` event that binds a fresh `code` under a `parent` to a new `TOP-…` id with an initial `label`. The concept then exists as a node like any other. (At pure zero-infra you may place against a not-yet-minted code and mint it lazily, but the log should not stay long without the matching `mint`.)
2. **Immutable, never reused.** Once minted, a code segment is permanent and is never repointed to a different concept or recycled — exactly like an ID. This is what lets placements reference it forever.
3. **Unique under parent.** Sibling segments must be unique within their parent. Uniqueness is scoped to the parent, so `PHY.QM.STATE` and `BIO.CELL.STATE` coexist.
4. **Label is separate.** The displayed name lives as an `alias` (`kind: label`) over the `TOP-…`; changing it is an `alias` event and touches no code and no placement.
5. **Honest depth + weight.** Place at the most precise true segment; express looser relevance with a lower `weight`, not a vaguer code. Prefix scans still catch the precise placements from a broad query.
6. **Reparent by redirect, never in place.** To move a concept, append an `alias` (or `mint` of the new path) so the old code and the new code both resolve to the same `TOP-…`; the old code remains valid as a redirect and is never deleted. References survive because the identity underneath is unchanged. *(How the fold resolves redirect chains, and a `redirect` alias kind, are queued workstream-D questions — scan 8.1.)*
7. **Routing codes derive from identity.** Index-style routes (`GBL`, `KG`, …) are `alias` bindings (`kind: route`) over concept ids — projections of placements, never independent strings. *(Asserted as the mechanism; first exercised when the Index's routing codes are bound via `alias(route)` — a queued workstream-D item, scan 3.3.)*

**Grammar vs. style (C-027).** Rules 1–7 are the **grammar** — universal and fixed; every FRACTAL repository shares them, which is what makes any two interoperable. How segments are *spelled or abbreviated* (`QM` vs `QUANTUM`, 3-letter vs full word) is **naming style**: a *recommended project-level convention, not a mandated rule*. Its job is legibility and reducing accidental duplicate coordinates for one concept — never correctness, since codes resolve by identity, not spelling. Teams may adopt different styles and still interoperate.

---

## 6. Open questions & deferred

*TBD:* the `mint` collision policy under concurrent writers + the fold-verification ritual (OQ-19, workstream E); whether `time` placements should auto-derive from `created` (OQ-18 — non-blocking); facet minting under a `FACET` root + root-uniqueness scope + `redirect` alias kind + route binding (workstream D); a compact binary/columnar projection for very large logs; the log partition interval (OQ-3). *Deferred:* the `place`/`trace`/`query-by-facet` MCP index and the Galaxy UI (build only on observed need, C-021). *Resolved in v0.2 (2026-08-12):* the ULID profile, `content_hash` input, `revise` referent, `actor` semantics, TOP `facet:` field, entity-target placements (C-040); the C-015 scheme itself (C-039, closing OQ-14); the identity bridge to canonical documents (C-041).

## 7. Decisions captured

Carried from v0.1: **C-022** (node file), **C-023** (event log; interval TBD), **C-024** (log-canonical), **C-025** (supersede + commit granularity; boundary = the git commit per C-037), **C-026** (facet registry + vocabularies), **C-027** (allocation grammar vs style). New in v0.2 (recorded in Governance Protocol — Claude Series v0.9):

- **C-039** — C-015 **confirmed**: the `TYPE-ULID` + alias identity scheme flips Working Hypothesis → Working Decision. The live store's contents were minted under the now-confirmed scheme; no grandfathering needed. Resolves OQ-14.
- **C-040** — Schema v0.2 pins: ULID profile + named generation method (§2.1); `content_hash` input for store bodies and external canonical files (§3.7); `revise.supersedes` = prior event id (§4.3); `actor` = committing agent (§4.2); TOP `facet:` registered, log-wins (§3.2); entity-target placements via id-in-`code` (§3.5); version-bump discipline for canonical specs (header note).
- **C-041** — Identity bridge: store node files are the identity system (exempt from C-005 rule-7 naming); canonical documents are minted as `DOC` nodes with their `Fractal_<Name>` bound as an alias; "Document ID: TBD" placeholders retired (§2.2).
- **C-042** — Canonical-corpus minting executed: the full Claude-era canonical corpus minted as DOC nodes (see Protocol v0.9 §9); `GBL`/`CTX` topic roots minted; the facet-registry DOC hashed (first `revise`) and linked (first entity-target `cites`).

---

**Refresh triggers:** a change to the two-relation core, the canonical-source rule, the verb set, the role/facet vocabularies, the code-allocation rules, the ULID profile, or the hash definition.
**Sources:** Fractal Knowledge Path Foundation v0.1; Fractal Node & Event Schema v0.1 (superseded); Governance Protocol — Claude v0.4, v0.6, v0.8 & v0.9; Decision Register v0.5; Loose-Ends Scan 2026-08-12 (findings 1.2, 3.1, 3.2, 3.5, 6.1); this conversation (2026-08-12, workstream C).
**Revision history:** v0.1 (2026-08-07) initial node & event format specification; (2026-08-12) in-place revision at facet-registry acceptance — retroactively recognized as a C-005 violation (scan 1.2). · v0.2 (2026-08-12) reissue under version-bump discipline: C-015 confirmed (C-039); ULID profile, `content_hash`, `revise` referent, `actor` semantics, TOP `facet:`, entity-target placements pinned (C-040); identity bridge to canonical documents (C-041); `GBL`/`CTX` roots registered; workstream-D pointers annotated on §5.3 rules 6–7.
