# Fractal Node & Event Schema

> **CANONICAL — Claude-era format specification (Domain KG).** Fixes the plain-text on-disk format that makes FRACTAL hand-usable with zero infrastructure: the node front-matter schema, the append-only event-log line format, and the facet-code allocation rules. Derived directly from the two-relation core of `Fractal_Knowledge_Path_Foundation_v0.1.md`; this document is the source of truth for the format. Project docs and context packages are derived projections of it.

**Fractal_Node_and_Event_Schema** · **Version:** 0.1 · **Status:** Accepted · **Updated:** 2026-08-12 · **Domain:** KG · **Author:** Claude · **Parent:** Fractal Knowledge Path Foundation v0.1

> **SUPERSEDED (2026-08-12):** reissued as `Fractal_Node_and_Event_Schema_v0.2.md` (C-040, per Protocol v0.9). Retained as history under C-012; do not author against this version.

**Decision status legend:** *Principle* (accepted, load-bearing) · *Working Decision* (accepted in a prior session) · *Working Hypothesis* (proposed here, not yet accepted) · *Deferred* · *TBD*.

---

## 0. What this document is (and is not)

This is step 1 of the KG build sequence (C-021): **spec the format first, defer code and UI to observed need.** It specifies exactly enough for a human — or a model reading the folder — to *place* an item and *trace* it by reading plain text, with no index server and no database. Everything here is a block added back onto the essential rule of the Foundation (§3: *two relations, one log*); nothing here introduces a new rule.

It fixes three things and only these three:

1. the **node** — how an Entity is written on disk (§3);
2. the **event log** — how every placement and change is recorded, append-only (§4);
3. the **facet codes** — how the coordinate namespaces are allocated and evolved (§5).

It does **not** specify the ID-generation algorithm internals, the index/MCP server, or the UI. Those remain Deferred/TBD per the Foundation.

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

## 2. Types & identifiers (recap of the accepted scheme)

*Principle (separation) · Working Hypothesis (scheme).* Two handles per Entity, per Foundation §4:

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

---

## 3. The node file

### 3.1 File & naming

A node is one UTF-8 text file: **YAML front-matter** (the identity + materialized placements) followed by an optional Markdown **body** (the human content, for `DOC`/`TOP`; may be empty for `NUM`/`PER`/etc.).

- **Filename:** `<id>.md`, optionally `<id>--<slug>.md` where `<slug>` is a lowercase human hint. The `id` prefix makes the file greppable and stable; the slug is an alias and may change freely (renaming the file never changes identity). Example: `DOC-01J9Z3K8QF7Q2A6M--nuclear-cross-section.md`.
- **Location:** under the repository's node store. Physical foldering is navigation only, never identity — a node's *real* placements live in its `placements:` block and the log, not in which directory it happens to sit.

### 3.2 Front-matter schema

```yaml
---
# ── Identity (immutable; mirrors the `create` event) ──────────────
id: DOC-01J9Z3K8QF7Q2A6M          # REQUIRED. Persistent Object ID. TYPE-ULID. Never changes.
type: DOC                          # REQUIRED. Must equal the id prefix. One registered type.
created: 2026-08-07T14:32:00Z      # REQUIRED. Birth timestamp, ISO-8601 UTC.
created_by: AGENT.HUMAN.MAX        # REQUIRED. Authoring agent (agent-facet code; kind branch marks human/AI).

# ── Version / integrity (per version; optional for pure concepts) ─
content_hash: sha256:9f2b…          # OPTIONAL. Hash of THIS version's frozen body. Omit for TOP.
version_of: ~                       # OPTIONAL. If this file is a frozen snapshot, the living id it snapshots.

# ── Aliases (mutable; human-facing) ──────────────────────────────
title: "Neutron cross-section of U-235"   # OPTIONAL. Human label. An alias, not identity.
aliases: []                                # OPTIONAL. Other labels / routing codes for this entity.
code: ~                                     # OPTIONAL. TOP nodes only: the concept's own code (mirrors its `mint`).
                                            #   Parentage is the code PREFIX (PHY.QM.QFT's parent is PHY.QM) — no separate edge.

# ── Placements (MATERIALIZED FOLD of the log for this id) ─────────
# Each entry = one outward edge: this entity --role--> a coordinate (facet+code).
# This block is a projection of the event log; the log is canonical (§4.5).
placements:
  - facet: topic          # which independent namespace/axis (§5.1)
    code: PHY.QM.QFT       # coordinate in that facet: a dotted concept code (§5)
    role: about            # role of the edge (§3.3)
    weight: 1.0            # centrality in [0,1] (§3.4)
  - facet: topic
    code: ECON.ENERGY
    role: about
    weight: 0.4
  - facet: source-type
    code: SRC.PAPER.PREPRINT
    role: is-a
    weight: 1.0
  - facet: agent
    code: AGENT.HUMAN.MAX
    role: by
    weight: 1.0
---
```

Only `id`, `type`, `created`, `created_by` are required. Everything else is added back as the item warrants it. A bare stub (identity only, empty `placements`) is a valid node.

### 3.3 Role vocabulary (v0.1)

One edge, differentiated by `role`. Registered roles:

| Role | Meaning | Typical target facet |
|---|---|---|
| `about` | subject / classification | `topic` |
| `in` | containment — subject is inside target | `topic` or another entity (a `TBL`, a `DOC`) |
| `cites` | subject cites target | any entity |
| `by` | authorship — subject authored by target | `agent` |
| `member-of` | subject is a member of a collection | a `SET` |
| `is-a` | typing within a facet | `source-type`, `method` |
| `derived-from` | provenance — subject was produced from target (written by `run`, §4.4) | any entity |

New roles are added by registering them here in a later version; the machinery does not change.

### 3.4 Weight

`weight ∈ [0,1]` — how central the placement is. `1.0` = definitive / core; lower = looser / peripheral. It is what distinguishes *central to* a topic from *merely tagged*, and lets a trace rank neighbours. Default when omitted: `1.0`.

### 3.5 Edge direction & the inverted view

Placements are written **outward** (subject → target). The reverse view (target → its subjects) is not stored in nodes; it is recovered by folding the log (or, later, from the index's inverted table). At zero infra you find "everything placed at `PHY.QM.QFT`" by grepping the log / node front-matter for that code.

---

## 4. The event log

### 4.1 Shape

*Working Decision (plain-text log) · Working Hypothesis (this line format).* One **append-only JSONL** stream: one JSON object per line, one event per line, **never edited or deleted**. To change anything you append a new event (§4.6). This is the canonical record of identity births and every placement.

- **Physical layout:** the log is **partitioned** into time-bucketed files `_events/<bucket>.jsonl`. "One log" is conceptual; partitioning keeps files small and makes git merges of concurrent appends near-conflict-free. **The partition interval is TBD** (C-023): monthly (`_events/2026-08.jsonl`) is a candidate shown for illustration, not a fixed decision — the bracket size is chosen later from observed volume. That partitioning happens is accepted; *by what interval* is open.
- **Ordering:** events are applied in `ts` order. `EVT-ULID` ids are themselves time-sortable, breaking ties deterministically.
- **What counts as an event (commit granularity):** the log records **committed** facts, not keystrokes. Editing a node's body while drafting — fixing typos, revising prose — produces **no** events until the change is deliberately committed/saved, at which point one `revise` event records the new version. This maps directly to a git commit: the working edit is invisible to history until committed. The append-only/never-edit rule (§4.6) therefore governs *committed events*, not in-progress editing.

### 4.2 Common fields (every line)

| Field | Req | Meaning |
|---|---|---|
| `ev`  | ✔ | verb (§4.3) |
| `id`  | ✔ | this event's own id, `EVT-<ULID>` — events are addressable Entities |
| `ts`  | ✔ | ISO-8601 UTC timestamp |
| `actor` | ✔ | agent-facet code performing it, e.g. `AGENT.HUMAN.MAX`, `AGENT.AI.CLAUDE` |
| `subject` | ✔ | the primary Entity id the event is about |
| `supersedes` | — | id of a prior event this one overrides (§4.6) |
| `note` | — | free-text human rationale |

Verb-specific fields are added on top, below.

### 4.3 Verbs

| Verb | Adds fields | Effect |
|---|---|---|
| `create` | `type`, `content_hash?`, `title?` | births an Entity (mirrors node identity front-matter) |
| `place`  | `facet`, `code`, `role`, `weight` | adds one placement edge from `subject` |
| `unplace`| `facet`, `code`, `role` (or `supersedes`) | retracts a placement previously added |
| `mint`   | `facet`, `code`, `parent`, `label` | allocates a new concept code, binding it to `subject` (a `TOP-…`) |
| `alias`  | `alias`, `kind` (`label`/`route`) | binds/rebinds a human label or routing code to `subject` |
| `revise` | `content_hash`, `supersedes` (prior version hash/event) | records a new version of a living Entity |
| `run`    | `operator`, `inputs:[id]`, `outputs:[id]` | records an Operator execution; appends `derived-from` edges output→input (§4.4) |

The set is intentionally small; new verbs are added only when an observed need forces one.

### 4.4 Operator runs = provenance

*Working Decision (from Foundation §6).* When an Operator runs, a single `run` event records `inputs`, the `operator`, and `outputs`. From it the fold materializes `derived-from` placements on each output pointing at its inputs. Trace backward from any `NUM` through its `derived-from` chain to recover the full derivation to sources — "preserve the entire reasoning process, not just results," delivered by the same one mechanism.

### 4.5 Canonical-source rule (the load-bearing decision here)

*Accepted — C-024 (load-bearing).* **The event log is authoritative. Node `placements:` is a materialized fold of the log for that node.**

- To **place by hand at zero infra:** append a `place` line to the current month's log, then reflect the same edge in the node's `placements:` block. Two writes, one truth.
- On any disagreement, the **log wins**; the front-matter is regenerated from the log (by hand, or by the index once it exists).
- Identity fields (`id`, `type`, `created`, `created_by`) are the exception: they are canonical *in the node* and merely mirrored by the `create` event — identity is born with the file.

*Alternative considered (open, §6):* make front-matter the hand-authored primary and treat the log as a journal generated from front-matter diffs. Rejected as the default because it demotes the event log below Principle 5; recorded here so Max can overturn the default with one decision.

### 4.6 Supersede semantics

Append-only means **correction is a new event, never an edit or delete.** To override, append an event whose `supersedes` points at the prior event's `id` (or, for placements, an `unplace` naming the same `facet`+`code`+`role`). The **current state** of any Entity is the fold: apply its events in `ts` order; a later event with `supersedes` replaces the effect of the one it names. Nothing is ever lost — the superseded event stays in the log as history. This is how reclassification, reweighting, retitling and reparenting all happen without breaking a single reference.

---

## 5. Facet codes

> **Accepted (C-026 / C-027, 2026-08-12).** The facet registry is resolved: it is the **browsable, log-derived projection of the concept nodes (`TOP-…`) that serve as coordinates**, grouped by facet — not a separately-authored control file (consistent with C-019 "index is a derived cache" and C-024 "log is canonical"). It has two tiers: a small set of **facets** (independent axes) and an open, growing **vocabulary of coordinates** minted within them; the "browsable library / source-style index" is the inverted fold over these. The facet set, the role vocabulary (§3.3), weight, and the allocation rules (§5.3) below are **accepted** (grammar fixed; vocabularies extend on observed need). Ratified in Governance Protocol — Claude Series v0.6.

### 5.1 Facets are independent namespaces

*Working Decision (Foundation §5).* Coordinates live in several **independent axes** at once, not one master tree. Registered facets (v0.1):

| Facet | Axis | Root code(s) |
|---|---|---|
| `topic` | subject matter | domain roots: `PHY`, `ECON`, `BIO`, `KG`, `GOV`, … |
| `method` | how it was produced/investigated | `METH` (e.g. `METH.EXPERIMENT`, `METH.SIMULATION`) |
| `source-type` | what kind of source it is | `SRC` (e.g. `SRC.PAPER.PREPRINT`, `SRC.DATASET`) |
| `time` | temporal placement | `TIME` (e.g. `TIME.2026.Q3`) |
| `agent` | actors (authorship/provenance) | `AGENT`, **branched by kind:** `AGENT.HUMAN.<name>`, `AGENT.AI.<name>` (e.g. `AGENT.HUMAN.MAX`, `AGENT.AI.CLAUDE`) |

An Entity carries coordinates in as many facets as are honestly true of it. New facets are registered here when an observed need appears.

**Agent facet — branched by kind (C-026).** The `agent` axis is confirmed as a facet: authorship is the `by` *role*, and the facet is the browsable *who*. Its top branch is the human/AI distinction — every agent is minted under `AGENT.HUMAN` or `AGENT.AI` — so "everything by a human" (`AGENT.HUMAN.*`) or "by an AI" (`AGENT.AI.*`) is a one-pass prefix filter. No separate `agent-kind` facet: kind is intrinsic to the agent, so a parallel axis would only duplicate it and risk drift.

### 5.2 Code shape

A code is a **dotted path** of uppercase segments — `PHY.QM.QFT`, `ECON.ENERGY.NUCLEAR` — of arbitrary depth. Each segment matches `[A-Z0-9]([A-Z0-9_]*[A-Z0-9])?`; segments are joined by `.`. The **code is a stable token, not a label**: it references a concept `TOP-…`, and the concept's human name is a separate alias. Renaming "Economics" touches zero placements.

Because codes are hierarchical and kept sorted, "everything under physics" is a **prefix scan** `PHY.*` — O(log n), not a full scan. **Concept parentage is carried by the code prefix itself** (`PHY.QM.QFT`'s parent is `PHY.QM`), not by a separate placement edge; the `mint` event's `parent` field only records and validates that binding at birth. A `TOP` node therefore stores its own coordinate in the front-matter `code:` field and needs no self-placement.

### 5.3 Allocation rules

1. **Mint before use.** A new segment is created by a `mint` event that binds a fresh `code` under a `parent` to a new `TOP-…` id with an initial `label`. The concept then exists as a node like any other. (At pure zero-infra you may place against a not-yet-minted code and mint it lazily, but the log should not stay long without the matching `mint`.)
2. **Immutable, never reused.** Once minted, a code segment is permanent and is never repointed to a different concept or recycled — exactly like an ID. This is what lets placements reference it forever.
3. **Unique under parent.** Sibling segments must be unique within their parent. Uniqueness is scoped to the parent, so `PHY.QM.STATE` and `BIO.CELL.STATE` coexist.
4. **Label is separate.** The displayed name lives as an `alias` (`kind: label`) over the `TOP-…`; changing it is an `alias` event and touches no code and no placement.
5. **Honest depth + weight.** Place at the most precise true segment; express looser relevance with a lower `weight`, not a vaguer code. Prefix scans still catch the precise placements from a broad query.
6. **Reparent by redirect, never in place.** To move a concept, append an `alias` (or `mint` of the new path) so the old code and the new code both resolve to the same `TOP-…`; the old code remains valid as a redirect and is never deleted. References survive because the identity underneath is unchanged.
7. **Routing codes derive from identity.** Index-style routes (`GBL`, `KG`, …) are `alias` bindings (`kind: route`) over concept ids — projections of placements, never independent strings. A route and its concept cannot drift because one is generated from the other (Foundation §5).

**Grammar vs. style (C-027).** Rules 1–7 are the **grammar** — universal and fixed; every FRACTAL repository shares them, which is what makes any two interoperable. How segments are *spelled or abbreviated* (`QM` vs `QUANTUM`, 3-letter vs full word) is **naming style**: a *recommended project-level convention, not a mandated rule*. Its job is legibility and reducing accidental duplicate coordinates for one concept — never correctness, since codes resolve by identity, not spelling. Teams may adopt different styles and still interoperate.

---

## 6. Open questions & deferred

*TBD:* exact ULID parameters and the `mint` collision policy under concurrent git branches (beyond "unique under parent, merge surfaces clashes"); whether `time` placements should auto-derive from `created` (carried — non-blocking); a compact binary/columnar projection for very large logs. *Deferred:* the `place`/`trace`/`query-by-facet` MCP index and the Galaxy UI (build only on observed need, C-021). *Resolved (2026-08-12):* the **canonical-source rule** (§4.5) is accepted as C-024; the **facet registry, the role and facet vocabularies, and the code-allocation rules** are accepted as C-026/C-027 (Governance Protocol — Claude Series v0.6).

## 7. Decisions captured (proposed this session)

- **C-022** — Node file = UTF-8 Markdown + YAML front-matter; required identity `{id, type, created, created_by}`; optional `{content_hash, title, aliases, code, placements}`. Filename `<id>[--slug].md`; physical foldering is navigation, not identity. *(Accepted — Governance Protocol Claude v0.4.)*
- **C-023** — Event log = append-only JSONL, one event per line, **partitioned** (interval **TBD** — monthly is a candidate, not fixed); verbs `{create, place, unplace, mint, alias, revise, run}`; events are addressable (`EVT-ULID`). *(Accepted — Governance Protocol Claude v0.4; partition interval open.)*
- **C-024** — Canonical-source rule: the event log is authoritative; node `placements:` is a materialized fold (log-canonical). *(Accepted — Governance Protocol Claude v0.4.)*
- **C-025** — Supersede semantics: no edit/delete; correction is a new event with `supersedes`; current state = fold in `ts` order. **Events are recorded at commit/save, not per keystroke** — in-progress editing is untraced until committed. *(Accepted — Governance Protocol Claude v0.4.)*
- **C-026** — Facet registry: the browsable, log-derived projection of coordinate-concepts (`TOP-…`) grouped by facet (a projection, not a control file). Facets `{topic, method, source-type, time, agent}`; the **agent facet is branched by kind** (`AGENT.HUMAN.<name>` / `AGENT.AI.<name>`); role vocabulary `{about, in, cites, by, member-of, is-a, derived-from}`; `weight ∈ [0,1]` = central vs merely tagged. Vocabularies are seeds, extended on observed need. *(Accepted — Governance Protocol Claude v0.6.)*
- **C-027** — Facet-code allocation (the **grammar**, universal & fixed): mint-before-use; immutable & never reused; unique under parent; label separate; honest-depth+weight; reparent-by-redirect; parentage = code prefix; routes derive from identity. Naming **style** (spelling/abbreviation) is a *recommended project-level convention, not a mandated rule*. *(Accepted — Governance Protocol Claude v0.6.)*

---

**Refresh triggers:** a change to the two-relation core, the canonical-source rule, the verb set, the role/facet vocabularies, or the code-allocation rules.
**Sources:** Fractal Knowledge Path Foundation v0.1; Fractal Global Context v0.2; Fractal Local Context — Knowledge Graph; Governance Protocol — Claude v0.2, v0.4 & v0.6; this conversation (2026-08-12).
**Revision history:** v0.1 (2026-08-07) initial node & event format specification. · (2026-08-12) C-026/C-027 accepted — facet registry resolved as a log-derived projection; agent facet branched by kind (`AGENT.HUMAN`/`AGENT.AI`); grammar-vs-style split added to §5.3; §4.5 canonical-source rule marked accepted (C-024); status Draft (Proposal) → Accepted. First live store bootstrapped at `/Claude/Knowledge Graph Store/`.
