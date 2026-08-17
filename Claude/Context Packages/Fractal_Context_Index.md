# Fractal Context Index

> **DERIVED PROJECTION — routing table, not a source of truth.** The lookup layer for the Context Persistence Workflow: it maps each domain to a short code, its canonical location, and its current context package, so a conversation resolves *exactly what to load* in one glance instead of scanning the folder. Living document: stable filename, version tracked below. Update it whenever a location or package changes — it is the single place routing is maintained. Canonical copy: `FRACTAL/Claude/Context Packages/`.

**Version:** 0.40 · **Status:** Living (derived projection) · **Updated:** 2026-08-17 · **Document ID:** DOC-01KZVYP8MGAH66JSVDDPNZ1PTR
**How to use:** identify the aspect/domain of your task → read its context package (or, if none yet, the canonical documents at its path) → load nothing outside that row unless a dependency requires it.

**Route provenance (C-046, completed by C-053):** **all eight domain codes** — `KG`, `GOV`, `GBL`, `CTX`, `AST`, `ONT`, `WS`, `PROT` — are **live `alias(kind: route)` bindings in the Knowledge Graph Store**; this table projects them and cannot drift from their concepts (Schema v0.6 §5.3 rule 7).

---

## Behavioural entry points

| Need | Read this |
|---|---|
| Orientation (vision + current realisation) | `Fractal_Global_Context.md` (`/Claude/Context Packages/Global/` — read in-repo, C-067) |
| Where we're looking right now (active aspect) | the active Local Context, below |
| How a conversation must behave | `Fractal_Conversation_Settings.md` (`/Claude/Project Governance/Governance Documents/`) |
| The decision ledger (all numbered C-decisions, one index) | `Fractal_Decision_Register.md` (`/Claude/Project Governance/Governance Documents/` — read in-repo, C-067) |
| The whole rule-set at a glance (one-page rule-book) | `Fractal_Rule_Overview.md` (`/Claude/Project Governance/Governance Documents/` — read in-repo, C-067) — part of the context package per C-036 |
| Rebuilding FRACTAL from a bare clone (rehydrate + client adapters) | `BOOTSTRAP.md` (repo root — ships in-repo per C-020/C-038) |
| **Starting a new project under FRACTAL's government** (birth an instance) | `GENESIS.md` (repo root — BOOTSTRAP's forward sibling, arc 1 of C-078) — **guided path: `Fractal_Onboarding_Protocol.md`** (Governance Documents, C-101; trigger `/begin`) |
| **The repo gate for strangers** (what FRACTAL is, compressed) | `README.md` (repo root — derived projection, never a source; committed per Protocol v0.33) |
| **The user guide** (day two onward, per-client driving, troubleshooting) | `GUIDE.md` (repo root — derived projection, never a source; landed per v0.45) |
| **All session commands at a glance** (the sextet + the child tier) | `Fractal_Command_Index.md` (`/Claude/Context Packages/` — derived projection over the stamped command files; issued 2026-08-16; the move-2 website section projects from it) |
| **The standards library** (adoptable procedures, formats, conventions — statuses honest) | `Registry/README.md` (repo root — canonical, C-113; the beta-0.5 registry release's spine) |
| **The shipping page** (explanation + setup guide, for sharing by link) | `Site/fractal-site.html` (source of record — **rebuilt 2026-08-17 from the approved capture** on Max's design brief, per v0.47; hosting queued with the flip: GitHub Pages under `knet.network`) |
| Why the current state exists (history) | Governance Protocols (see PROT row) |

## Active Local Context

| Aspect | Canonical location | Document |
|---|---|---|
| **Knowledge Graph / code system** (current focus) | `/Claude/Context Packages/Local/` | `Fractal_Local_Context_Knowledge_Graph.md` |

## Domain routing

| Domain | Code | Canonical location | Context package | Status |
|---|---|---|---|---|
| Global / orientation (stable) | `GBL` ⚭ | `/Claude/Context Packages/Global/` | Fractal_Global_Context | Current |
| Knowledge Graph | `KG` ⚭ | `/Claude/Architecture/Concepts/Knowledge Graph/` · store: `/Claude/Knowledge Graph Store/` | Local Context (KG) | Active — format v0.6, read side contracted (C-068–C-070), multi-writer safe (C-049–C-050); live store holds the canonical corpus (C-042) |
| Governance & Workflow | `GOV` ⚭ | `/Claude/Project Governance/` · (ChatGPT-era: `/Archive/Foundation with ChatGPT/Project Governance/`) | Conversation Settings + Governance Protocols + Decision Register + Rule Overview | Active |
| Architecture State (canonical current model) | `AST` ⚭ | `/Claude/Architecture/Architecture State/` (`Fractal_Architecture_State.md`) · (ChatGPT-era stub + Master Index: `/Archive/Foundation with ChatGPT/Architecture/`, pointer-only C-029) | Architecture State (living canonical map, C-051) | Active — forged clean 2026-08-13 |
| Information / Context Packages | `CTX` ⚭ | `/Claude/Context Packages/` · (concept drafts: `/Architecture/Concepts/Information Package/`) | Global Context + this Index | Active |
| Ontology & Shells (Galaxy / Operator) | `ONT` ⚭ | Architecture State §3 (`AST.ONT`) · (ChatGPT-era Parts IV–V: pointer-only) | — (within AST) | Settled — C-017 two-faces model; supersession recorded (C-052) |
| Workspace, Navigation & UI | `WS` ⚭ | `/Claude/Architecture/Concepts/Workspace/` (`Fractal_Workspace_Foundation`, C-086 class) · Architecture State §4 (`AST.WS`) · (ChatGPT-era Parts VI–VIII + UI-vision note: pointer-only reservoir) | Workspace Foundation (concept, Draft) | **Active — forged (C-093, per v0.39):** OQ-23 fired on observed need; first build slice landed (`Workbench/` — working tool, homepage-nested) |
| Protocols (development history) | `PROT` ⚭ | `/Claude/Project Governance/Governance Protocol/` (`GOV.PROT`) · (ChatGPT-era: `/Archive/Foundation with ChatGPT/Initial Protocols until v11/`) | n/a (history layer) | Series open (Claude v0.1–v0.30) |

*Paths are relative to `Desktop/FRACTAL/`. Rows without a dedicated package resolve to their canonical location or the relevant Architecture State index range. ⚭ = route bound in the store via `alias(kind: route)` (C-046).*

## Canonical documents of note

| Document | Domain | Canonical location |
|---|---|---|
| Knowledge Path Foundation v0.1 | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| Knowledge Network Foundation (living concept, **Draft — non-binding vision tier**, C-086; the network stack: profiles, verification gate, standards library, knowledge mining; **v0.2 — first external-evidence revision: the child's dragons, per v0.39**) | GBL | `/Claude/Architecture/Concepts/Knowledge Network/` |
| Workspace Foundation (living concept, **Draft — non-binding vision tier**, C-086 second member; the WS forge of record — coupled panes over `resolve`, the archive reservoir governed, the workbench §7-landed; first build slice: `Workbench/` at the repo root, working tool; **v0.2 — first observed-use revision: §6 carries the vehicle decision's first datum, per v0.40**) | WS | `/Claude/Architecture/Concepts/Workspace/` |
| Node & Event Schema **v0.6** (v0.1–v0.5 superseded, retained as history; every version its own DOC identity, C-061) | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| Node Template **v0.5** (v0.1–v0.4 superseded, retained as history; every version its own DOC identity, C-061) | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| Navigation Contract **v0.1** (the read-side companion of the Schema — entry, hops, trace, ranking, history; C-068–C-070) | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| Knowledge Graph Store (live: nodes/ + _events/; canonical-corpus DOC nodes, facet layer, route bindings; seven tools `verify.py` + `mint.py` + `check_versions.py` + `close.py` + `genesis.py` + `doctor.py` + `fieldnote.py`, C-050/C-060/C-073/C-078/C-087/C-088/C-100) | KG | `/Claude/Knowledge Graph Store/` |
| Architecture State (living canonical map; ONT §3, WS §4) | AST | `/Claude/Architecture/Architecture State/` |
| Decision Register (C-001 → C-n) | GOV | `/Claude/Project Governance/Governance Documents/` |
| Rule Overview (one-page rule-book; context package per C-036) | GOV | `/Claude/Project Governance/Governance Documents/` |
| Bootstrap Protocol (`BOOTSTRAP.md`, stable root filename) | GOV | repo root (`Desktop/FRACTAL/`) |
| Genesis Protocol (`GENESIS.md` **v0.8**, stable root filename; canonical, DOC-minted, STRICT-guarded — the forward sibling of BOOTSTRAP; §3 executable since `genesis.py`; the registry-release reissue per v0.50 — the §5 registry row, the root-mint escape hatch, the materials line; clause current to C-106) | GOV | repo root (`Desktop/FRACTAL/`) |
| **Onboarding Protocol** (`Fractal_Onboarding_Protocol.md` — the guided first loop: the interview, the rail, the fade; C-101; `/begin` its command projection) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Fieldnote Format v0.1** (the machine-parsable capture format — the friends-beta collection interface; C-100; reference implementation `fieldnote.py`; **roster now four lanes** — `knet` · `beta` · `publish` · `general`, authority `fieldnote_roster.json`) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Agenda Board Format v0.1** (the board standard — contract + section grammar + instance-neutral skeleton; C-104; existing instances adopt by own decision, newborns at genesis) | CTX | `/Claude/Project Governance/Governance Documents/` |
| **Ultracode Flight Protocol v0.2** (the flight container standard — commissioning contract incl. the gating-mode field + derived agent counts, the launch sequence with mechanical effort-setting, verification tiers, landing + reporting incl. cost honesty; C-108, reissued per the v0.2 cures; v0.1 frozen history; registry seed, beta-0.5) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Scan Procedure v0.1** (the loose-end review procedure standard — distilled from Scans #1–#4; standalone-first, flight-pluggable; the Scan-#5 checker gate armed; C-108; registry seed, beta-0.5) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Diet Procedure v0.1** (the working-set eviction procedure standard — C-095 made standard; distilled from DF1 + CB1; the eviction grammar, the fact-presence gate, the behaviour test; DP1-verified; C-111; registry seed, beta-0.5) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **The Registry** (`Registry/README.md` — the standards library, C-113: the five-rule contract, the seeded catalog, honest statuses; C-108's declaration executed at beta-0.5) | GOV | repo root (`Registry/`) |
| **Vocabulary Extension Procedure v0.1** (governed instance-side role extension — the `vocabulary_local.json` hook in `verify.py`, decision-ref gated; prose + checker complete; C-114; RF1-2's cure) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Scholarly Source Convention v0.1** (the first content convention — paper DOC shape, identifier routes, PER-not-AGENT authors, the interim locator rule; C-115; RF1-1's cure) | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| **The Capture — Vision to Horizon** (C-103, the capture-review class's first member — **approved raw material of the public identity**; verified dossiers at `Site/Capture Materials/`, pre-canon) | GOV | `/Claude/Context Packages/Conversations/` (`Capture_2026-08-16_Vision-to-Horizon.md`) |
| **License layer** (C-099 — `LICENSE` Apache-2.0 · `LICENSE-docs` CC BY 4.0 · `NOTICE`; the name not licensed, stated in README; terms travel with newborns) | GOV | repo root (`Desktop/FRACTAL/`) |
| Claude Code client adapter (`CLAUDE.md`, stable root filename; canonical per C-065 — content a C-035 compression of Conversation Settings) | GOV | repo root (`Desktop/FRACTAL/`) |
| **Client Library** (canonical living catalog of vendor surfaces, **C-097** — per client: discovery convention, session-capable adapter template, mechanics; no runtime API — currency via the C-094 loop; Codex/ChatGPT entry harvest-pending on KNet's ratified adapter) | GOV | `/Claude/Project Governance/Governance Documents/` (`Fractal_Client_Library.md`) |
| Codex drone adapter (`AGENTS.md`, stable root filename; canonical per C-065 class, installed per C-066 — drone-scoped C-035 compression) | GOV | repo root (`Desktop/FRACTAL/`) |
| Loose-Ends Scans #1 (2026-08-12), #2 (2026-08-14), #3 & #4 (2026-08-15) — canonical reviews, sequential/dated (C-058; #3 carries the first Scan-riding restore drill, C-076; **#4 the pre-pack gate — the series' first birth test, full slate in-pass**) · **Stranger Test #1 (2026-08-17)** — the family's simulated-stranger shape: the public tree onboarded end-to-end, six findings cured generator-side in-session · **Flight Record — Refinement #1 (2026-08-17)** — the Ultracode Flight Protocol's first conformance specimen: three persona sims (`RF1-…` slate — the registry validated as the adoption gate), the held capture v1.2 draft, the applied site slate | GOV | `/Claude/Context Packages/Conversations/` |
| **Release provenance anchors** (C-090 — per-release tag attestation + OpenTimestamps receipt pairs; first member `beta-0.1`; receipts upgrade to Bitcoin-final mechanically at any later session) | GOV | repo root (`Provenance/`) |

*Every canonical document above carries a minted `DOC-…` identity in the Knowledge Graph Store (C-041/C-042); the store's alias events bind each `Fractal_<Name>` to its id — and, for versioned artifacts, each `Fractal_<Name>_vX.Y` to its own per-version DOC (C-061), the versionless alias staying on the series pointer. Facets themselves are minted under the `FACET` root (C-043).*

## Naming convention (decision C-012)

**Living projections** (Global Context, this Index, Conversation Settings, Architecture State, Local Contexts, Decision Register) use a **stable filename**; version lives inside the document. **Historical / sequential artifacts** (Governance Protocols, Return Packages) carry versioned or dated filenames. **Canonical specifications** (Schema, Template) are versioned artifacts: every substantive change is a new version/file (C-040), each version carrying its own DOC identity in the store while the versionless alias tracks the newest (C-061). **No living projection's filename carries a version token** — the grandfathered `_v0.1` orientation names were retired 2026-08-15 (C-080), and `check_versions.py` now errors on any that reappear. The ChatGPT-era files **were moved to the archive subfolder `Archive/` on 2026-08-14 (C-063, OQ-10 resolved)** — this file is the one place the paths are maintained, and it was updated in the same pass.

---

**Sources:** the Governance Protocol series (`Claude/Project Governance/Governance Protocol/`, route `PROT`) and the Decision Register (stamp inside, C-012) — the of-record homes of every session narrative this table once carried; the routed documents themselves (stamps inside, C-012); the Knowledge Graph Store route bindings (C-046/C-053).
*(Sources narrative retired 2026-08-17, the C-110 diet, first conformant exercise of Fractal_Diet_Procedure_v0.1 — index only; per-session narration lives frozen in the protocol series and the dated Return Packages.)*
