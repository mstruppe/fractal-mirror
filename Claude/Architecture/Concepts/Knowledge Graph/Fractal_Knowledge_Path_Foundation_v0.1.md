# Fractal Knowledge Path — Clean-era Foundation

> **CANONICAL — Claude-era foundation document.** Identity, relationships, shells, substrate and portability for the FRACTAL knowledge system. Forged clean *from* the ChatGPT-era Knowledge Graph Architecture v0.1, restating its accepted principles in the distilled two-relation core. This document is the source of truth for its domain; Project docs and context packages are derived projections of it.

**Fractal_Knowledge_Path_Foundation** · **Version:** 0.1 · **Status:** Ratified (2026-08-12, per Protocol v0.7 review pass; status field corrected 2026-08-14, per v0.17 — scan S2-2.1) · **Reviewed By:** Max (2026-08-12, per v0.7) · **Updated:** 2026-08-14 · **Domain:** KG · **Author:** Claude · **Parent:** Fractal Global Context

**Decision status legend (from Architecture State):** *Principle* (accepted, load-bearing) · *Working Decision* (accepted this session) · *Working Hypothesis* (proposed, not yet accepted) · *Deferred* · *TBD*.

---

## 1. Purpose & scope

FRACTAL needs one simple, robust, future-proof mechanism to give every piece of information a stable identity and to trace it *within context* across many domains at once — the way a filesystem locates a file, but where a single item can live in many places and every link is preserved. This document fixes that mechanism (the **Knowledge Path**), the two behavioural faces a node can take (the **shells**), the technical **substrate** it runs on, and the **portability** doctrine that keeps FRACTAL from being locked to one machine or one person.

It deliberately does *not* prescribe implementation detail beyond accepted decisions. It is the blueprint from which the simplest implementation is later derived block by block — per the FRACTAL credo of recursive simplicity.

## 2. Relationship to accepted architecture

This foundation **inherits, does not replace**, the accepted *Knowledge Graph Architecture v0.1* (author: ChatGPT; reviewed: Max). Its six core principles are carried forward verbatim as *Principles*:

1. Identity is immutable.
2. Relationships are independent from identity.
3. Version history preserves continuity.
4. Integrity is verified through hashes.
5. Provenance is recorded by an event log.
6. Names are aliases, not identifiers.

The ChatGPT-era Governance Protocol v0.2 (pointer-only, C-029) already rejected embedding relationships into IDs and separated identity / versioning / relationships into independent layers. Everything below is consistent with that; it distils the eight enumerated components (Identity Generator, Identity Registry, Metadata Store, Relationship Store, Version Registry, Integrity Store, Event Log, Replication Layer) down to their essential rule and re-derives the components as blocks added back.

## 3. The essential rule — two relations, one log

*Working Decision.* Pushed to its minimum, the whole system is **two relations recorded in one append-only log**:

- **Identity** — *a thing exists.* Every piece of information — a document, a number, a function, a person, an image, **and every topic/context node itself** — is an **Entity** with one stable identifier. Topics are not special structure; they are Entities of a topic type. (This is the recursion: the taxonomy is made of the same stuff it classifies.)
- **Placement** — *a thing is placed within another thing, with a role and a weight.* This single **Relationship** edge expresses classification ("this paper is *about* QFT"), containment ("this number is *in* that table is *in* that document"), citation, authorship, and membership — they differ only by *role*, not by machinery.

Folders, tags, citations and "belongs-to" are therefore not four features but one edge with four role values. A filesystem hard-link — one inode, many directory entries — is exactly a multi-homed item; FRACTAL generalises "directory" to "any Entity" and allows arbitrarily many independent facets.

Everything else in this document (identity scheme, facets, shells, integrity, provenance) is a block added back onto this core, not a new rule.

## 4. Identity — the Persistent Object ID

*Working Hypothesis (scheme); Principle (separation).* Two handles per Entity:

- **Canonical key (immutable, opaque):** `<TYPE>-<ULID>` — e.g. `DOC-01J9Z3K8QF…`, `NUM-…`, `FN-…`, `PER-…`, `IMG-…`, `TOP-…` (topic). A ULID is time-sortable, collision-resistant, and needs no central coordinator. The type prefix keeps the ID space self-describing and open-ended for "any type later."
- **Names / codes (mutable, derived):** every human-facing label or routing code is an **alias** over the canonical key — never the key itself (Principle 6).

**The choosing rule (git's lesson):** *does the thing's identity survive a change to its content?*

- Yes → a living document, a person → **stable random identity** (ULID); v2 is still "the same document."
- No → a frozen artifact, a specific value, a specific version → **content hash**; changing it makes it a different thing.

So a living document gets a stable `DOC-…` identity, and *each version* is content-hashed underneath it (integrity + dedup + append-only provenance). Never bake context into the key: context is unbounded and mutable, identity is fixed — you cannot put the first inside the second without the updating paradox that breaks every reference on reclassification.

## 5. Context — the Knowledge Path

*Working Decision.* Context is a separate layer of Relationships pointing at stable identities.

- **Independent facets.** Concepts are organised in **multiple independent namespaces / axes** (e.g. topic, method, source-type, time), not one master tree. An Entity carries coordinates in several axes at once. (This answers the accepted doc's open "namespace design" question.)
- **Coordinates as paths.** A Concept's public handle is a stable dotted **code path** built from its parents — `PHY.QM.QFT`, `ECON.ENERGY.NUCLEAR` — of arbitrary depth. Codes reference Concepts by code, never by label, so renaming "Economics" touches zero Placements.
- **Efficient tracing.** Because codes are hierarchical dotted paths kept in sorted order, "everything under physics" is a **prefix range scan** (`PHY.*`) — O(log n), not a scan of millions. The Placement store is indexed both directions: `Entity → its contexts` and `context → its Entities` (inverted index). Tracing = from an item walk its Placements to Concepts, then prefix-hop to sibling items; `weight` distinguishes *central to* a topic from merely *tagged*.

**Routing codes derive from identity.** *Working Decision — resolves the Local Context open question.* The Index-style lookup codes (`GBL`, `KG`, …) become projections of Placements over Persistent Object IDs; a lookup code and a Concept ID can never drift apart because one is generated from the other.

**Worked example — the nuclear paper.** One `DOC-…` identity; N Placements at honest depth — precise `PHY.QM.QFT`, looser `ECON.ENERGY`; each reachable by prefix. The physicist enters at `PHY.QM.QFT`, the economist at `ECON.ENERGY.NUCLEAR`, and they meet at the same Entity without either scanning the other's domain. Nothing is baked into the ID; all of it is append-only, so the full reasoning trail is preserved.

## 6. Shells — two faces of one node

*Working Decision.* A node's **shell** is how it behaves/presents, not what it is. The same Entity, one ID, can wear either face — as a Mac `.app` is literally a folder (a bundle) you can also run:

- **Galaxy (container face)** — you open it and see what is placed inside (containment edges pointing *in*). This is the folder/space shell of the Architecture State UI vision (the "GS").
- **Operator (application face)** — you invoke it; it has input edges and output edges, consuming some nodes and producing others (edges flowing *through*). This is the application shell (the "OS").

Crucially, when an **Operator runs it appends edges** — "these inputs went through this operator to produce these outputs." So the log records not just where things *sit* but how they were *made*: trace backward from any number and recover its full derivation chain to sources. That is the vision's "preserve the entire reasoning process, not just results," delivered by the same one mechanism. The split-screen navigation dream (roam the Galaxy, the doc viewer jumps to the right place, *reversibly*) is possible **only because** both faces are the same Entity with shared Relationships.

## 7. Substrate — a thin layer over open primitives

*Working Decision (substrate B).* FRACTAL is realised **not** as bespoke platform software but as a thin layer over open, portable primitives. Most of the accepted component list already exists commoditised:

| FRACTAL component | Realised by |
|---|---|
| Integrity Store (content hashes) | **git** objects (content-addressed) |
| Event Log (provenance) | **git** history / commits |
| Version Registry / continuity | **git** |
| Replication Layer + Synchronisation | **git** remotes (answers two accepted TBDs) |
| Names as aliases | git refs / tags over object hashes |
| Operator shell (a tool with typed I/O) | an **MCP server** (open standard; Claude *and* ChatGPT speak it) |
| Composable rules / building blocks | **Skills** (as files in the repo) |
| Context spine (Global / Local / Domain) | **Projects + Memory** — as *swappable clients*, never canonical |
| AI-as-transparent-collaborator | the model, with human/AI authorship marked by a metadata/commit convention |

Only **two genuinely new artifacts** remain to build: (1) the **Knowledge Path index** — the Entities + Relationships registry, exposed as a small MCP server with verbs like `place`, `trace`, `query-by-facet`; and (2) eventually the **Galaxy UI** (*Deferred* — no native equivalent; ships as code in the repo when wanted).

**Canonical data is plain text; the database is a derived cache.** *Working Decision.* Relationships and the event log live as human-readable, git-mergeable text (append-only JSONL and/or per-node front-matter). The index database (e.g. SQLite) is a **disposable projection** rebuilt on boot — the DB is to the text log what a Project is to the folder. Everything canonical stays diffable, mergeable, and reconstructible anywhere.

## 8. Portability — the repository *is* FRACTAL

*Working Decision.* FRACTAL must not be locked to one machine, account, or vendor. The doctrine generalises the existing rule "canonical documents live in the folder; Project docs are derived projections" from *documents* to *the whole system*:

- **The repository is the product.** Nodes (plain files), the Knowledge Path index source, the Operators (MCP server code), the rules (skills/governance as files), and the full provenance (git history) are one git repository. Everything vendor-shaped — the Project, installed skills, account memory, client config — is a **projection** regenerable from the repo, never canonical.
- **Pack / ship / boot.** Pack = the repo. Ship = `git push` / `git bundle` / hand over the folder. Boot = clone, start the MCP servers, point *any* MCP-capable client (Claude, ChatGPT, a local model, the future Galaxy UI) at them. The client is swappable; the repo is constant.
- **Bootstrap protocol.** A rehydrate script/protocol ships *inside* the repo to re-project vendor conveniences (re-create the Project, re-install skills from repo files) on a fresh host. *TBD to author.*
- **Excluded from the repo:** secrets and credentials (supplied by the host at boot); per-ecosystem glue may be a thin adapter re-authored per brain, but it lives in the repo too.
- **Acceptance test — "laptop in the ocean":** could someone reconstitute FRACTAL from the repo alone — same nodes, same graph, same rules, same history — supplying only their own machine, AI client, and credentials? If yes, it is not locked to any person. The host is context, not identity — the same identity-vs-context separation as §4, lifted one scale up.

## 9. Open questions & deferred

*TBD:* final ID generation algorithm and namespace registry format; event/edge schema (roles, weights, supersede semantics); Concept-code allocation and reparenting rules; migration of ChatGPT-era material into the clean foundation; bootstrap protocol contents. *Deferred:* Galaxy/Operator UI; multi-user conflict-resolution policy beyond git defaults. *Working Hypothesis to confirm:* ULID-vs-hash split exactly as in §4.

## 10. Decisions captured (proposed this session)

C-013 forge a clean Claude-era foundation from ChatGPT-era material (not retrofit) · C-014 essential core = two relations (Identity + Placement) in one Event Log · C-015 Persistent Object ID = opaque `TYPE-ULID` for living entities, content-hash per version, names/codes are aliases · C-016 facets are independent namespaces; routing codes derive from identity · C-017 shells = two faces of one node (Galaxy / Operator) · C-018 substrate B — thin layer over git + files + MCP + Skills; vendor surfaces are swappable clients · C-019 canonical data is plain text in git; the index DB is a derived cache · C-020 portability doctrine — the repo *is* FRACTAL; bootstrap protocol ships in-repo; "laptop in the ocean" acceptance test.

---

**Refresh triggers:** a change to the identity model, the two-relation core, the substrate decision, or the portability doctrine.
**Sources:** Fractal Knowledge Graph Architecture v0.1; Fractal Architecture State v0.1 (Vision + UI vision); Fractal Local Context — Knowledge Graph; ChatGPT-era Governance Protocol v0.2 (pointer, C-029); this conversation (2026-08-07).
**Revision history:** v0.1 (2026-08-07) initial clean-era foundation. *(2026-08-14, per v0.17: status field corrected Draft → Ratified — the 2026-08-12 review pass ratified C-013–C-020 but never flipped this field (scan S2-2.1); protocol-series misattribution in §2/Sources corrected to the ChatGPT-era lineage (scan S1-1.5). No substantive change; v0.1 identity retained.)*
