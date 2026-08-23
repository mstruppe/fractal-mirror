# FRACTAL

> **An operating system for structured knowledge.** Your project gets a memory that survives every session: decisions recorded with their reasoning, work handed over so any future session picks up cold — all plain text in git that you own.

## Quickstart — start here

You need **git** and the **Claude Code CLI** ([claude.com/claude-code](https://claude.com/claude-code)). Three steps; the session does the rest.

**1. Get FRACTAL** (paste as one line):

```bash
git clone https://github.com/mstruppe/fractal-mirror.git ~/Desktop/fractal && cd ~/Desktop/fractal && git checkout $(git describe --tags --abbrev=0)
```

You will see a **"detached HEAD" notice — that's expected**: you are standing on the newest release, and you won't commit here, so ignore it (don't create a branch; this copy is a reference, not your project).

**2. Open a session** in that folder:

```bash
claude
```

**3. Type exactly this** as your first message:

```
/welcome
```

The session takes it from there: it explains what you're looking at and offers the two paths — **start your own FRACTAL-governed project** (it walks you through the birth, one question at a time) or **look around first**. If `/welcome` doesn't autocomplete, type *"I'm new here — welcome me"* instead.

Two things worth knowing before your first session: the terminal Claude Code has no settings UI — `/help` lists the controls (`/model`, `--continue` to reopen a conversation); and **your project will not live in this folder** — the birth creates a new repository of your own, and this clone remains reference material you can read and cite.

For everything after day one — coming back, driving the AI clients, plain-words concepts, troubleshooting — **[GUIDE.md](GUIDE.md)** is the practical companion.

---

## The idea (for the evaluating reader)

This repository does not implement FRACTAL. It **is** FRACTAL — the first living instance, a project that governs itself with its own machinery. Every architectural decision in here was made *inside* the system it describes, recorded in its own knowledge graph, and closed under its own rituals.

Real investigation is fragmented: every switch between web, AI, literature, data, notebooks, code, and prose forces context to be rebuilt from nothing. FRACTAL folds that lifecycle into one workflow, treats AI as a transparent collaborator while the human retains interpretation and decisions, and views knowledge as an evolving, interconnected structure rather than isolated documents.

Its governing philosophy is **recursive simplicity**: complex understanding emerges from repeatedly applying a small set of simple, composable rules. Begin from the smallest abstraction; add only what an observed problem requires. The same pattern repeats at every scale — project → domain → component → conversation → task.

## What exists today

Three load-bearing layers, all live and machine-guarded.

### 1. The knowledge core

- **Two relations, one log.** Everything is an **Entity** with a stable identity (`TYPE-ULID`); every classification, containment, citation, authorship, or membership is a **Placement** edge in one append-only event log. The log is canonical; node files are a materialized fold of it.
- **Context is separate from identity.** Independent facet namespaces give every entity dotted coordinate codes (`GOV.PROT`, `AGENT.AI.CLAUDE`); one prefix scan traces a whole domain. Facets are themselves minted concepts in the graph.
- **Specified on both sides.** The write side is the Node & Event Schema; the read side is the Navigation Contract (`resolve` / `enter` / `trace` / `history`) — entry is a query shape, trace is bounded ranked recursion, no home node. Implementation is tiered: the grep ritual (live today) → an index server (specified, built on observed need). Any index is a derived, disposable cache — canonical truth is plain text.
- **Machine-guarded.** `verify.py` checks the store's invariants before every store-touching commit; `check_versions.py` checks that the corpus's prose claims (versions, pointers, filenames) agree with reality at every close. Both block red.

### 2. The governance loop

- **Every working session is one bounded step** in a continuing program: it opens on a context spine (Global Context → active Local Context → last Return Package), works one declared aspect, and closes with a handover a successor can pick up cold.
- **Decisions are a ledger, not folklore.** The Decision Register indexes every accepted decision (C-001 → C-n) with a cumulative open-questions ledger; the Rule Overview is the one-page rule-book; the Governance Protocol series is the history layer — *why* the current state exists.
- **One conduct source, projected per surface.** How a conversation must behave lives in one canonical document (Conversation Settings); each working surface gets a stamped compression of it (`CLAUDE.md`, `AGENTS.md`), sync-checked at every close. Duplicated rule sources are a closed failure class.
- **Commits carry meaning.** Author = whoever wrote the bytes; committer = whoever authorized the act; the signature = custody. The commit is the event boundary.

### 3. The instantiation layer

FRACTAL is built to become **the government of any project**, not just itself — and it already is one: the first foreign instance was birthed from an anchored release and closed its first session the same day. The seam between what travels and what stays is measured, not guessed:

- The decision corpus partitions into **kernel (~80%)** — inherited by any new instance as constitution — plus a small parameterized set (kernel rule, instance value: exactly the input form of genesis) and pure biography, which stays home.
- **`BOOTSTRAP.md`** answers the backward question: rebuild *this* instance from a bare clone (drill-proven). **`GENESIS.md`** answers the forward one: birth a *new* instance with an inherited constitution and an empty history — executed by `genesis.py`; the newborn ships with the secrets layer, its provenance manifest, and the tier-1 checkers ready to adopt.
- A distribution clone knows it is a distribution clone: sessions in it are **reference surfaces** by constitution — they read, explain, and assist births; they never govern (Settings rule 9).
- **Ownership is the root of trust.** Every instance has exactly one owner — the human all authority inside it traces back to; AI agents are named writers with permanent attribution, acting under grants the owner makes, and responsibility never transfers to the machine. The kernel follows the same rule one level up: it stems from one origin, and it ships **already ratified by the origin's owner** — one standing ratification that holds the responsibility for the machine, kept to best knowledge through agent review passes and the machine gates, made cryptographic by each release's signed tag and anchored timestamp. A newborn re-argues none of this; its owner's own responsibility begins where the kernel ends. **And ownership is care (C-137):** an instance's integrity is carried by its own maintenance rituals — the checkers, the close, the capture loop — which ship with every birth; adopting FRACTAL is taking on their keeping, stated honestly at every door.
- A **standards registry** rides the kernel (`Registry/`): adoptable procedures, formats, and content conventions — the scholarly-source shape, the flight and review procedures, the capture format — each adopted by an instance's own recorded decision, never imposed. Demand that isn't built yet is listed honestly as *forging* or *named*.

## The substrate is deliberately thin

Git + plain-text files + a compliant AI surface. No database, no server, no proprietary format. Vendor surfaces are swappable clients; the repository clones, rehydrates, and verifies anywhere. An off-site copy rides every close. Every shipped release tag carries an externally anchored timestamp (OpenTimestamps receipt committed in `Provenance/`) — the repo carries its own proof of priority.

## Map of the repository

| Path | What it is |
|---|---|
| `CLAUDE.md` / `AGENTS.md` | Per-surface conduct adapters (stamped projections of Conversation Settings) |
| `BOOTSTRAP.md` | Rebuild this instance from a bare clone |
| `GENESIS.md` | Birth a new instance under FRACTAL's government |
| `GUIDE.md` | The user guide — day two onward, per-client driving, troubleshooting |
| `.claude/commands/` | The shipped session commands — `/welcome` (first contact), `/begin` (the onboarding interview), `/fractal` (open a working session), `/close` (the close ritual), `/look` + `/fieldnote` (the observation and capture tier) |
| `Claude/Knowledge Graph Store/` | The live graph — nodes, the event log, and the eight tools (`verify.py`, `mint.py`, `check_versions.py`, `close.py`, `genesis.py`, `doctor.py`, `fieldnote.py`, `check_scan.py`) |
| `Claude/Architecture/` | The canonical architecture: Architecture State (the map), Schema, Template, Navigation Contract |
| `Claude/Project Governance/` | Conversation Settings, Decision Register, Rule Overview, the Governance Protocol series |
| `Claude/Context Packages/` | The context spine: Global Context, Local Contexts, the routing Index, Agenda Board, Return Packages |
| `Registry/` | **The standards library** — adoptable procedures, formats, and content conventions; every entry an offer with an honest status (*shipped · forging · named*) |
| `Provenance/` | Release provenance anchors — tag attestations + OpenTimestamps receipts |
| `Archive/` | The ChatGPT-era foundation — preserved intact, pointer-only |
| `Site/` · `Workbench/` | The mother's working surfaces (site sources, field ledgers, a workbench tool) — **excluded from release copies**; if you're reading a release and these are absent or empty, that's curation, not error |

## License

**Free use, attribution preserved** — implemented as a split by content class: **code** (the Python tools, `Workbench/`, and other executable sources) under the **Apache License 2.0** ([LICENSE](LICENSE), [NOTICE](NOTICE)); **documents** (the governed corpus — the Markdown canon, the knowledge store's nodes and event log) under **Creative Commons Attribution 4.0** ([LICENSE-docs](LICENSE-docs)). Personal pre-canon material (the C-085 class) is not licensed for reuse. A birthed instance inherits the kernel under these terms; the license files travel with every newborn, and the attribution its Genesis Record carries satisfies CC BY.

**The name is not licensed:** "FRACTAL" and the project's marks identify this project and its releases. Neither license grants rights to them — Apache-2.0 §6 says so explicitly for the code, and the same posture applies to the documents.

## The field door

A friction you hit or a win worth recording: file it as an issue in your own words — the [issue templates](https://github.com/mstruppe/fractal-mirror/issues/new/choose) are fieldnote-shaped, and they land in the same intake the project's own field notes use. Mail works too: `fractal@knet.network`.

## Where it stands, where it goes

The foundational architecture is complete — the knowledge core specified on both sides, the governance stack scan-audited under full machine guard, the kernel extracted and exercised. The realisation mode has turned once, its first recorded transition (2026-08-15): **ship it** — the first beta is packed with externally anchored provenance, the first **foreign instance** — a project FRACTAL governs that is not itself — is alive and closing its own sessions, and, once two instances have content worth merging, **federation**: merging a stranger's graph into your own (identities merge free by construction; codes are namespaced by an origin layer; meaning stays human).

---

*Derived projection (C-035 class) — a compression for the repo gate, never a source, committed per Protocol v0.33. Sources: Fractal Global Context §1; Fractal_Architecture_State; the active Local Context (stamps inside each, C-012). Stamped 2026-08-15; rewritten quickstart-first the same day at the phase-5 ingestion (fieldnotes entries 1–6: the user path leads, the evaluator content follows); guide split out + command tier grown 2026-08-16 (the flip-preparation session); quickstart retargeted to the mirror — the permanent public home — 2026-08-16 (C-105); the Registry row + the working-surfaces map note added at the registry release 2026-08-17 (beta-0.5 — RF1-13's cure); the field-door section added 2026-08-20 (Scan #6 S6-3.3 — the public intake made discoverable from the gate); the ownership bullet added 2026-08-20 (C-133 — the kernel ratification clause, projected into the instantiation layer's context); its care sentence added 2026-08-22 (C-137 — the care doctrine). Refresh triggers: a Global §2 realisation transition, an Architecture State reissue that moves a section summarized here, a change to the quickstart path (commands, adapter, GENESIS §0–§2), or a C-059 walk finding this stale.*
