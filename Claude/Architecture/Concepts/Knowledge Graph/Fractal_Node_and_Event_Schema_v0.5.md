# Fractal Node & Event Schema

> **CANONICAL — Claude-era format specification (Domain KG).** Fixes the plain-text on-disk format that makes FRACTAL hand-usable with zero infrastructure: the node front-matter schema, the append-only event-log line format, and the facet-code allocation rules. Derived directly from the two-relation core of `Fractal_Knowledge_Path_Foundation_v0.1.md`; this document is the source of truth for the format. Project docs and context packages are derived projections of it.

**Fractal_Node_and_Event_Schema** · **Version:** 0.5 · **Status:** Ratified (2026-08-13, in-conversation per C-033; event-log layout by C-055) · **Updated:** 2026-08-13 · **Domain:** KG · **Author:** Claude · **Parent:** Fractal Knowledge Path Foundation v0.1 · **Supersedes:** Fractal_Node_and_Event_Schema_v0.4.md

**Decision status legend:** *Principle* (accepted, load-bearing) · *Working Decision* (accepted) · *Deferred* · *TBD*.

> **Why v0.5 exists (version-bump discipline, C-040).** v0.4 carried OQ-3 open: the event log's partition interval was TBD, with monthly buckets standing in as an illustration that had leaked into practice (`_events/2026-08.jsonl`; `mint.py` derived the bucket from the month). This reissue resolves OQ-3 the fractal way — **by eliminating the specification**: the log is **one append-only file**, partitioning becomes a *latent capability* rather than a standing scheme, and brackets materialize only on observed need. Concretely (C-055): a single active partition; an advisory **50,000-event volume tripwire** checked by `verify.py` at the ritual that already runs at every store-touching commit; and a **roll ceremony** — a deliberate, recorded commit on merged state — as the only way a new partition ever opens (writer-local automatic rolling would diverge across unmerged clones, silently re-importing the problem C-049 retired). Nothing else in the format changes.

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

- **Identity** — *a thing exists.* One Entity, one immutable `TYPE-ULID` key. Topics/concepts are Entities too (`TOP-…`); the taxonomy is made of the same stuff it classifies — **including, since v0.3, the facets themselves (C-043)**.
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
- **Canonical documents are minted as `DOC` nodes.** A canonical document's persistent ID **is its `DOC-…` node id**; its `Fractal_<Name>` identity is bound to that node as an **alias** — from v0.3 forward of **`kind: route`**, because a `Fractal_<Name>` is a machine token (control tables, filenames, citations), not a display name; under C-045's newest-label rule a `label` binding would displace the title. (The 2026-08-12 corpus batch bound them as `label`, pre-pin — grandfathered as materialized.) The DOC node's `content_hash` freezes the file's current version; its body carries the repo-relative path.
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
title: "Facet Registry — C-026/C-027"      # OPTIONAL. Human label. An alias, not identity (newest label-kind alias, §4.3).
aliases: []                                # OPTIONAL. Other labels / routing codes (fold of `alias` events).
code: ~                                     # TOP nodes only: the concept's own CURRENT code (newest `mint`, §5.3 rule 6).
                                            #   Parentage is the code PREFIX (PHY.QM.QFT's parent is PHY.QM).
facet: ~                                    # TOP nodes only: the facet the code lives in (mirrors its `mint`).
                                            #   The facet token itself resolves to a minted FACET.* concept (C-043).

# ── Placements (MATERIALIZED FOLD of the log for this id) ─────────
# Each entry = one outward edge: this entity --role--> a coordinate (facet+code) or an entity (§3.5).
# This block is a projection of the event log; the log is canonical (§4.5).
# Codes are materialized at their CURRENT canonical form — the fold resolves redirects (§5.3 rule 6).
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

**TOP nodes carry `code:` *and* `facet:`** — both mirror the `mint` event(s), and both follow the canonical-source rule: on disagreement with the log, **the log wins** (they are *not* part of the §4.5 identity exception). After a reparent (§5.3 rule 6), `code:` carries the newest mint's code; superseded codes appear in `aliases:` marked as redirects.

### 3.3 Role vocabulary (v0.3 — unchanged from v0.1)

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

Placements are written **outward** (subject → target). The reverse view (target → its subjects) is not stored in nodes; it is recovered by folding the log (or, later, from the index's inverted table). At zero infra you find "everything placed at `PHY.QM.QFT`" by grepping the log / node front-matter for that code — after first checking the redirect list if the concept has been reparented (§5.3 rule 6; store README).

### 3.7 `content_hash` (pinned, C-040)

`content_hash` is `sha256:<64 lowercase hex digits>` and freezes **one version** of an entity's content. What is hashed:

- **Store node with a body** — the byte-exact UTF-8 **body**: everything after the front-matter's closing `---` delimiter *and its trailing newline*, through end-of-file. Hashing the body only (never the front-matter) keeps the hash stable while the mutable fold (`placements:`, `aliases:`) and the hash field itself change.
- **DOC node representing an external canonical file** (§2.2) — the **whole file's bytes** at the recorded version, exactly as committed to git. The node body states the repo-relative path.

A `create` event may carry the first version's hash; each subsequent version is recorded by a `revise` event (§4.3). Verification = recompute and compare; the first worked example is the store's facet-registry DOC (hashed 2026-08-12, C-042).

---

## 4. The event log

### 4.1 Shape

*Working Decision (plain-text log and this line format — C-023).* One **append-only JSONL** stream: one JSON object per line, one event per line, **never edited or deleted**. To change anything you append a new event (§4.6). This is the canonical record of identity births and every placement.

- **Physical layout (C-055, resolving OQ-3):** the log is **one append-only file** — the store's single active partition (`_events/part-0001.jsonl`; the bootstrap-era monthly name was retired at the C-055 commit). Partitioning is a **latent capability, not a standing scheme**: `verify.py` carries an advisory **volume tripwire — 50,000 events per file** (~15 MB at the observed ~290 B/event; ~decades away at observed pace) — and when it fires, the next partition (`part-0002.jsonl`, …) is opened by the **roll ceremony**: a deliberate, recorded commit on *merged* state, in the C-049 ceremony pattern — never an automatic per-writer act, since writer-local rolling would produce divergent partition boundaries across unmerged clones. Closed partitions are immutable (§4.6 applies file-wide); every reader (`verify.py`, `mint.py`, grep tracing) consumes `_events/*.jsonl` and is partition-agnostic, so if machine-rate writing one day makes rolls routine, that observed friction is the C-008 trigger to automate the roll — decided then, from real volume, applying from its commit forward with **no migration ever**. Semantic clashes between concurrent appends (two writers minting one code) remain invisible to git and are caught by the §5.5 ritual (C-049/C-050), exactly as before.
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
| `mint`   | `facet`, `code`, `parent`, `label` | allocates a new concept code, binding it to `subject` (a `TOP-…`) — including a **new code for an existing concept** (reparent, §5.3 rule 6) |
| `alias`  | `alias`, `kind` (`label`/`route`/`redirect`) | binds/rebinds a human label, routing code, or redirect marker to `subject` |
| `revise` | `content_hash`, `supersedes` | records a new version of a living Entity |
| `run`    | `operator`, `inputs:[id]`, `outputs:[id]` | records an Operator execution; appends `derived-from` edges output→input (§4.4) |

**`revise.supersedes` referent (pinned, C-040):** `supersedes` names the **event id** (`EVT-…`) of the prior version's `revise` (or, for the first revision, the `create`). One supersede semantics everywhere in the log — never a content hash. The version *chain* is walked through events; the hashes hang off them.

**`alias` kinds and fold rules (pinned, C-045).** Three registered kinds:

- **`label`** — a human display name. The fold rule for `title:` is **newest label wins**: the most recent `label` alias is materialized as the node's `title:`; all bound labels (including superseded ones) accumulate in `aliases:`. Nothing is ever unbound without an explicit superseding event. *(Applied from v0.3 forward; the corpus batch's 2026-08-12 label bindings predate this rule and stand as materialized — the same treatment the bootstrap batch's `actor` ambiguity received in v0.2.)*
- **`route`** — a **machine token** bound to an identity: an Index routing code (`KG`, `GOV`, …, per §5.3 rule 7), a facet's event-field token (`topic`, `source-type`, …, per C-043), or a canonical document's `Fractal_<Name>` (§2.2). A route token means exactly one thing because it resolves to exactly one node.
- **`redirect`** — marks a **superseded coordinate code** after a reparent (§5.3 rule 6): the alias string is the old code, which remains permanently valid and resolves — via this marker — to the same `TOP-…` subject, whose newest mint carries the current code. Redirects are the one-grep list of moved codes (`"kind": "redirect"`).

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

> **Accepted (C-026 / C-027, 2026-08-12; facet layer completed by C-043–C-046, 2026-08-13).** The facet registry is the **browsable, log-derived projection of the concept nodes (`TOP-…`) that serve as coordinates**, grouped by facet — not a separately-authored control file (consistent with C-019 "index is a derived cache" and C-024 "log is canonical"). It has two tiers: a small set of **facets** (independent axes) and an open, growing **vocabulary of coordinates** minted within them; the "browsable library / source-style index" is the inverted fold over these. **Since v0.3 both tiers are made of the same stuff: the facets themselves are minted concepts (C-043)**, so the registry — top to bottom — is a fold of the log. The role vocabulary (§3.3), weight, and the allocation rules (§5.3) are **accepted** (grammar fixed; vocabularies extend on observed need).

### 5.1 Facets are independent namespaces — and minted concepts (C-043)

*Working Decision (Foundation §5; minting C-043).* Coordinates live in several **independent axes** at once, not one master tree. **Each facet is itself a `TOP-…` concept, minted under the root `FACET` in the meta-facet whose token is `facet`** — the axis in which facet definitions live. The event-field token (the exact string written in `facet:` fields, e.g. `topic`, `source-type`) is bound to its concept as an `alias` (`kind: route`), so the token resolves to an identity exactly as a routing code does (rule 7). Registered facets (v0.3 — **this table is a derived projection of the store's `FACET.*` mints; the log is canonical**):

| Facet token | Concept code | Axis | Root code(s) of its vocabulary |
|---|---|---|---|
| `facet` | `FACET` (root) | facet definitions (meta) | `FACET` itself — children are the facets |
| `topic` | `FACET.TOPIC` | subject matter | domain roots: `KG`, `GOV`, `GBL`, `CTX`, `PHY`, `ECON`, `BIO`, … |
| `method` | `FACET.METHOD` | how it was produced/investigated | `METH` (e.g. `METH.EXPERIMENT`, `METH.SIMULATION`) |
| `source-type` | `FACET.SOURCE_TYPE` | what kind of source it is | `SRC` (e.g. `SRC.PAPER.PREPRINT`, `SRC.DATASET`) |
| `time` | `FACET.TIME` | temporal placement | `TIME` (e.g. `TIME.2026.Q3`) |
| `agent` | `FACET.AGENT` | actors (authorship/provenance) | `AGENT`, **branched by kind:** `AGENT.HUMAN.<name>`, `AGENT.AI.<name>` |

An Entity carries coordinates in as many facets as are honestly true of it. **A new facet is created by minting it** (`mint` under parent `FACET`) and binding its token (`alias`, kind `route`) — an ordinary vocabulary extension on observed need, no schema edit required; this table is refreshed as a projection. Nothing about existing events changes: `facet:` fields keep carrying the tokens they always carried — the tokens simply resolve to identities now. *(Genesis note: the `FACET` root's own mint names the token `facet` before that token's binding exists in the log — the same batch-scoped self-reference the agent bootstrap recorded and accepted; true by end of batch.)*

**Agent facet — branched by kind (C-026).** The `agent` axis is confirmed as a facet: authorship is the `by` *role*, and the facet is the browsable *who*. Its top branch is the human/AI distinction — every agent is minted under `AGENT.HUMAN` or `AGENT.AI` — so "everything by a human" (`AGENT.HUMAN.*`) or "by an AI" (`AGENT.AI.*`) is a one-pass prefix filter. No separate `agent-kind` facet: kind is intrinsic to the agent, so a parallel axis would only duplicate it and risk drift.

### 5.2 Code shape

A code is a **dotted path** of uppercase segments — `PHY.QM.QFT`, `ECON.ENERGY.NUCLEAR` — of arbitrary depth. Each segment matches `[A-Z0-9]([A-Z0-9_]*[A-Z0-9])?`; segments are joined by `.`. The **code is a stable token, not a label**: it references a concept `TOP-…`, and the concept's human name is a separate alias. Renaming "Economics" touches zero placements.

Because codes are hierarchical and kept sorted, "everything under physics" is a **prefix scan** `PHY.*` — O(log n), not a full scan. **Concept parentage is carried by the code prefix itself** (`PHY.QM.QFT`'s parent is `PHY.QM`), not by a separate placement edge; the `mint` event's `parent` field only records and validates that binding at birth. A `TOP` node therefore stores its own coordinate in the front-matter `code:` (and `facet:`) fields and needs no self-placement.

### 5.3 Allocation rules

1. **Mint before use.** A new segment is created by a `mint` event that binds a fresh `code` under a `parent` to a new `TOP-…` id with an initial `label`. The concept then exists as a node like any other. (At pure zero-infra you may place against a not-yet-minted code and mint it lazily, but the log should not stay long without the matching `mint`.)
2. **Immutable, never reused.** Once minted, a code segment is permanent and is never repointed to a different concept or recycled — exactly like an ID. This is what lets placements reference it forever.
3. **Unique under parent; roots unique globally (C-044).** Sibling segments must be unique within their parent, so `PHY.QM.STATE` and `BIO.CELL.STATE` coexist. **Root segments (`parent: null`) form one global namespace across *all* facets** — one root, one meaning, in every grep and every trace. (A topic root `TIME` can never be minted alongside the time facet's `TIME`.) Because a full dotted path begins with its root, global root-uniqueness makes every full code globally unambiguous too. Checked at mint time: a root mint must match no existing root in the log.
4. **Label is separate.** The displayed name lives as an `alias` (`kind: label`) over the `TOP-…`; changing it is an `alias` event and touches no code and no placement.
5. **Honest depth + weight.** Place at the most precise true segment; express looser relevance with a lower `weight`, not a vaguer code. Prefix scans still catch the precise placements from a broad query.
6. **Reparent by redirect, never in place (semantics pinned, C-045).** To move a concept: **(a)** append a `mint` event whose `subject` is the **existing** `TOP-…` and whose `code` is the new path under the new `parent` — a reparent is a mint because the new code must be parent-validated and uniqueness-checked like any other; **(b)** in the same commit, append an `alias` event of **`kind: redirect`** whose alias string is the **old code** — the explicit, one-grep marker that the code has moved. The old code is never deleted and never re-pointed: it resolves through the redirect to the same concept forever, so every log line that names it stays valid history. **The fold resolves codes through the redirect chain:** the newest mint's code is the concept's canonical code (`code:` in its node); materialized `placements:` blocks in *other* nodes are regenerated at the canonical code (legal — front-matter is a fold, §4.5; the log lines themselves are never touched); prefix scans over materialized state therefore see the tree as it currently stands. Chains are walked transitively; each hop is one `redirect` alias. Zero log events are edited, superseded, or re-placed — rule 6's "touch zero placements" holds at the log layer, which is the canonical one.
7. **Routing codes derive from identity (exercised, C-046).** Index-style routes (`GBL`, `KG`, …) are `alias` bindings (`kind: route`) over concept ids — projections of placements, never independent strings. **Live since 2026-08-13:** the Context Index's four minted domain routes (`KG`, `GOV`, `GBL`, `CTX`) are bound in the store; the Index's routing table is a projection of those bindings. (`AST`, `ONT`, `WS`, `PROT` follow when workstream F settles their canonical ground.) Facet tokens use the same mechanism (§5.1, C-043).

**Grammar vs. style (C-027).** Rules 1–7 are the **grammar** — universal and fixed; every FRACTAL repository shares them, which is what makes any two interoperable. How segments are *spelled or abbreviated* (`QM` vs `QUANTUM`, 3-letter vs full word) is **naming style**: a *recommended project-level convention, not a mandated rule*. Its job is legibility and reducing accidental duplicate coordinates for one concept — never correctness, since codes resolve by identity, not spelling. Teams may adopt different styles and still interoperate.

### 5.4 Concurrency & collision policy (C-049)

*Working Decision (C-049, resolving OQ-19 together with §5.5).* Multiple writers work on independent clones; git merges their logs textually. What keeps one meaning per code:

1. **Identity cannot collide.** ULIDs carry 80 bits of randomness (§2.1) — two writers can never mint the same *identity*. Only **codes** (names) can collide, and only when two clones mint the same code before merging. Nothing is corrupted when they do: a collision is two individually valid events whose *combination* violates rule 3 — visible to any fold, never a data loss.
2. **First mint wins (deterministic fold rule).** When the merged log holds two `mint` events binding one code to different subjects, the code binds to the **earlier** event — by `ts`, with the event ULID breaking ties. The later mint does not bind. The rule is mechanical and reproducible from the log alone: any two readers of the same log agree on every binding, with no adjudication step. (Max may still overrule a specific outcome — that is a recorded decision producing ordinary reparent events, not an exception to the rule.)
3. **Cure is mandatory and append-only.** A losing mint is cured in the next store-touching commit: **(a)** re-`mint` the losing subject under a fresh code — the same machinery as a C-045 reparent — with a `note` citing the collision and the winning event id; **(b)** re-point the placements that *intended* the losing concept, by appended `unplace` + `place` at the new code. Binding is deterministic, but **intent is not**: the verifier lists every placement against the contested code, and the writers who authored them split them explicitly. No log line is edited; the collision stays in the log as history. Until cured, the verifier fails (§5.5) and blocks store commits like any other broken invariant.
4. **Root mints carry ceremony (the C-044 corollary).** Deep mints stay cheap — decentralised minting in the territory you are working is the point, and uniqueness there is a local sibling check. A **root** mint (`parent: null`) legislates in the one global namespace all facets share, so from the C-049 pin (2026-08-13) forward it must be **deliberate and attributed**: minted through the guard's explicit `--root` flag (§5.5) with a `note` recording whose call it was. The verifier errors on post-pin root mints lacking such a note. (Pre-pin roots are grandfathered; `GBL`/`CTX`/`FACET` already conform.)
5. **The single-writer caveat is retired.** With prevention (the guard), detection (the ritual at every C-037 boundary), and deterministic cure (this rule), multi-writer work is safe **by mechanism, not by discipline** — the v0.7 caveat 2 on C-032 is discharged.

### 5.5 Verification ritual & tools (C-050)

*Working Decision (C-050).* Two repo-resident, dependency-free (stdlib-only) tools live in the Knowledge Graph Store beside the README — code artifacts under the declared C-006 exception (like the Agenda Board's HTML, C-048), **not** DOC-minted (tool category, C-042 mint-on-reuse), versioned by git like everything else:

- **`verify.py` — the fold verifier (read-only).** Replays the full log and checks: **log integrity** (every line parses; verbs and required fields; ULID coherence; event-id uniqueness; `ts` ordering) · **mint grammar** (code shape; parent = code prefix; mint-before-use; sibling uniqueness; global root-uniqueness; the collision tripwire with first-wins/cured discrimination; post-pin root notes) · **references** (placement targets exist; roles and weights; alias kinds; route-token uniqueness; redirect wiring; revise chains) · **the fold** (every node file's identity fields, TOP `code:`/`facet:`, title, aliases, and placements match the log, redirect-resolved) · **hashes** (store-node body hashes and external canonical-file hashes recompute).
- **`mint.py` — the mint guard.** Makes local duplicates *impossible* rather than forbidden: it reads the log, lists what is taken under the chosen parent (naming options), validates the candidate code, refuses a root mint without the explicit `--root "whose call"` flag, generates a coherent ULID, and writes the `mint` line and the node stub in one move — §4.5's “two writes, one truth” automated. Dry-run by default; `--write` appends.

**The ritual is a duty, not an option: `verify.py` must run and pass before every store-touching commit and after every merge that touches the store.** The C-037 commit boundary is the checkpoint — the same boundary that turns working edits into committed events. A red verifier blocks the commit until the store is cured. This closes the gap the Loose-Ends Scan named (4.1/8.2): git merges JSONL appends without understanding them, so the semantic merge check is this ritual, never git.


---

## 6. Open questions & deferred

*TBD:* whether `time` placements should auto-derive from `created` (OQ-18 — non-blocking); a compact binary/columnar projection for very large logs. *Resolved in v0.5 (2026-08-13):* the event-log physical layout — one append-only file, 50,000-event advisory tripwire, roll-by-ceremony (C-055, closing OQ-3; interval-based brackets retired unchosen). *Deferred:* the `place`/`trace`/`query-by-facet` MCP index and the Galaxy UI (build only on observed need, C-021). *Resolved in v0.4 (2026-08-13):* the concurrency & collision policy — first-mint-wins, append-only cure, root-mint ceremony (C-049); the verification ritual + repo-resident tools (C-050); OQ-19 closed, the single-writer caveat retired. *Resolved in v0.3 (2026-08-13):* facet minting under the `FACET` root + meta-facet token binding (C-043); global root-uniqueness (C-044); reparent/redirect semantics + the `redirect` alias kind + label/route/redirect fold rules (C-045); rule 7 exercised via live route bindings (C-046). *Resolved in v0.2 (2026-08-12):* the ULID profile, `content_hash` input, `revise` referent, `actor` semantics, TOP `facet:` field, entity-target placements (C-040); the C-015 scheme itself (C-039, closing OQ-14); the identity bridge to canonical documents (C-041).

## 7. Decisions captured

Carried from v0.1–v0.4: **C-022** (node file), **C-023** (event log; physical layout now fixed by C-055), **C-024** (log-canonical), **C-025** (supersede + commit granularity; boundary = the git commit per C-037), **C-026** (facet registry + vocabularies), **C-027** (allocation grammar vs style), **C-039** (C-015 confirmed), **C-040** (format pins), **C-041** (identity bridge), **C-042** (canonical corpus minted); **C-043–C-046** (facet layer — see v0.3); **C-049–C-050** (concurrency policy + verification ritual — see v0.4). New in v0.5 (recorded in Governance Protocol — Claude Series v0.15):

- **C-055** — **Event-log physical layout: one file, tripwire, roll-by-ceremony.** The log is a single append-only active partition; `verify.py` warns (never fails) past 50,000 events per file; a new partition opens only through the roll ceremony — one recorded commit on merged state, Max's or a recorded delegate's call — and closed partitions are immutable. Partition brackets are thereby eliminated as a standing specification and preserved as a latent, on-need capability (C-008 escalation: first roll → routine rolls → automate, each triggered by observation). Resolves OQ-3; cures `mint.py`'s monthly bucket derivation; the bootstrap partition `2026-08.jsonl` is renamed `part-0001.jsonl` at the C-055 commit (git-tracked rename; log lines untouched).

---

**Refresh triggers:** a change to the two-relation core, the canonical-source rule, the verb set, the role vocabulary, the facet-minting or code-allocation rules, the concurrency/collision policy, the verification duty, the ULID profile, or the hash definition. *(The §5.1 facet table refreshes as a projection whenever a facet is minted — that alone is not a version bump.)*
**Sources:** Fractal Knowledge Path Foundation v0.1; Fractal Node & Event Schema v0.1–v0.4 (superseded); Governance Protocol — Claude v0.4, v0.6, v0.8–v0.10, v0.13 & v0.15; Decision Register v0.10; this conversation (2026-08-13, OQ-3 resolution — Max's call: no standing brackets, one file with an obnoxiously high cap, brackets only if ever necessary).
**Revision history:** v0.1 (2026-08-07) initial node & event format specification; (2026-08-12) in-place revision at facet-registry acceptance — retroactively recognized as a C-005 violation (scan 1.2). · v0.2 (2026-08-12) reissue under version-bump discipline: C-015 confirmed (C-039); ULID profile, `content_hash`, `revise` referent, `actor` semantics, TOP `facet:`, entity-target placements pinned (C-040); identity bridge (C-041). · v0.3 (2026-08-13) facet-layer completion (workstream D): facets minted under `FACET` (C-043); global root-uniqueness (C-044); redirect semantics + alias-kind fold rules (C-045); route binding exercised (C-046). · v0.4 (2026-08-13) multi-writer safety (workstream E): concurrency & collision policy — first-mint-wins, append-only cure, root ceremony (C-049); verification ritual + repo-resident tools `verify.py`/`mint.py` (C-050); OQ-19 closed, single-writer caveat retired. · v0.5 (2026-08-13) event-log layout (OQ-3 resolution): one append-only file, 50k-event advisory tripwire, roll-by-ceremony (C-055); monthly illustration retired; `mint.py` appends to the single active partition.
