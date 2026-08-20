# Fractal Context Index

> **DERIVED PROJECTION — routing table, not a source of truth.** The lookup layer for the Context Persistence Workflow: it maps each domain to a short code, its canonical location, and its current context package, so a conversation resolves *exactly what to load* in one glance instead of scanning the folder. Living document: stable filename, version tracked below. Update it whenever a location or package changes — it is the single place routing is maintained. Canonical copy: `FRACTAL/Claude/Context Packages/`.

**Version:** 0.52 · **Status:** Living (derived projection) · **Updated:** 2026-08-20 (the thirty-second session — the beta-0.7 tagging close: the Schema v0.7 + Navigation Contract v0.2 rows, the second Index diet) · **Document ID:** DOC-01KZVYP8MGAH66JSVDDPNZ1PTR
**How to use:** identify the aspect/domain of your task → read its context package (or, if none yet, the canonical documents at its path) → load nothing outside that row unless a dependency requires it.

**Route provenance (C-046, completed by C-053):** **all eight domain codes** — `KG`, `GOV`, `GBL`, `CTX`, `AST`, `ONT`, `WS`, `PROT` — are **live `alias(kind: route)` bindings in the Knowledge Graph Store**; this table projects them and cannot drift from their concepts (Schema v0.7 §5.3 rule 7).

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
| **The user-document pair series** (the human's windows, C-122/C-124) | all user halves: **`User Documents/`** at the repo root (C-126) — kernel: Board · Roadmap · Handout; extensions: the **Update Plan pair** + the **Gas pair** (originals in `/Claude/Context Packages/`); the standard: `Fractal_User_Document_Pair_Procedure` (Governance Documents; the C-131 seed law) |
| **The standards library** (adoptable procedures, formats, conventions — statuses honest) | `Registry/README.md` (repo root — canonical, C-113) |
| **The shipping site** (LIVE since 2026-08-18, C-120) | `Site/` — source of record; the section contract (C-130): Home · Guide · Concepts (+ `concepts/` detail tier) · Blog · `labs.html` + `legal.html`. Served from the mirror's `gh-pages` through the gate `knet.network`; refreshes push `gh-pages`, pull-before-push (S5-8.2) |
| Why the current state exists (history) | Governance Protocols (see PROT row) |

## Active Local Context

| Aspect | Canonical location | Document |
|---|---|---|
| **Knowledge Graph / code system** (current focus) | `/Claude/Context Packages/Local/` | `Fractal_Local_Context_Knowledge_Graph.md` |

## Domain routing

| Domain | Code | Canonical location | Context package | Status |
|---|---|---|---|---|
| Global / orientation (stable) | `GBL` ⚭ | `/Claude/Context Packages/Global/` | Fractal_Global_Context | Current |
| Knowledge Graph | `KG` ⚭ | `/Claude/Architecture/Concepts/Knowledge Graph/` · store: `/Claude/Knowledge Graph Store/` | Local Context (KG) | Active — format v0.7, read side contracted (C-068–C-070), multi-writer safe (C-049–C-050); live store holds the canonical corpus (C-042) |
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
| Knowledge Network Foundation **v0.4** (living concept, Draft — non-binding vision tier, C-086; the network stack) | GBL | `/Claude/Architecture/Concepts/Knowledge Network/` |
| **Value Model** (living concept, Draft — vision tier, C-086; public projection `Site/value-model.html`) | GBL | `/Claude/Architecture/Concepts/Value Model/` |
| Workspace Foundation **v0.2** (living concept, Draft — C-086; first build slice `Workbench/`) | WS | `/Claude/Architecture/Concepts/Workspace/` |
| **Interface Foundation v0.5** (living concept, Draft — C-086; directions-never-context; §8 PR + the transport; §9 the place) | GBL | `/Claude/Architecture/Concepts/Interface/` |
| Node & Event Schema **v0.7** (v0.1–v0.6 superseded, retained as history; every version its own DOC identity, C-061; `Reviewed By` since v0.7 — C-133's first exercise) | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| Node Template **v0.5** (v0.1–v0.4 superseded, retained as history; every version its own DOC identity, C-061) | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| Navigation Contract **v0.2** (the read-side companion of the Schema — entry, hops, trace, ranking, history; C-068–C-070; v0.1 superseded) | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| Knowledge Graph Store (live: nodes/ + _events/; DOC nodes, facet layer, route bindings; the eight canonized tools — the store README is the roster, C-050…C-118) | KG | `/Claude/Knowledge Graph Store/` |
| Architecture State (living canonical map; ONT §3, WS §4) | AST | `/Claude/Architecture/Architecture State/` |
| Decision Register (C-001 → C-n) | GOV | `/Claude/Project Governance/Governance Documents/` |
| Rule Overview (one-page rule-book; context package per C-036) | GOV | `/Claude/Project Governance/Governance Documents/` |
| Bootstrap Protocol (`BOOTSTRAP.md`, stable root filename) | GOV | repo root (`Desktop/FRACTAL/`) |
| Genesis Protocol (`GENESIS.md`, stable root filename — version stamped inside; canonical, STRICT-guarded — BOOTSTRAP's forward sibling; §3 executable via `genesis.py`; pack-checked at every tagging close) | GOV | repo root (`Desktop/FRACTAL/`) |
| **Onboarding Protocol** (`Fractal_Onboarding_Protocol.md` — the guided first loop: the interview, the rail, the fade; C-101; `/begin` its command projection) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Fieldnote Format v0.2** (the RAM-buffer format, C-100/C-121; `fieldnote.py`; buffer `Site/Fieldnotes.md`; v0.1 superseded, lanes frozen) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Agenda Board Format v0.3** (the board standard — contract, section grammar, skeleton; C-104/C-122/C-126/C-128 — the `User Documents/` home, the extension pills, the rolling done bar; earlier versions frozen history; adoption by own decision, newborns at genesis) | CTX | `/Claude/Project Governance/Governance Documents/` |
| **Interface Place Format v0.1** (the interface place standard — the communication organ's shape: place + index contract, index grammar, envelope minimum, skeleton; C-123; counterpart navigation deliberately unspecified until two children, the transport candidate of record banked — git/HTTPS, the proven class; genesis births the place) | GBL | `/Claude/Project Governance/Governance Documents/` |
| **User Document Pair Procedure v0.3** (the pair-series standard — the doctrine, the C-125 takeover gate, the kernel trio, the five-step extension process, the C-126 location law, the C-131 seed law; kernel-shipped; earlier versions frozen history) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **The seed tier** (`Templates/` — C-131: the four frozen v0.0 seed editions + the tier README; `genesis.py` instantiates them at birth; the set bounded to the kernel trio) | GOV | repo root (`Templates/`) |
| **Ultracode Flight Protocol v0.2** (the flight container standard; C-108; registry seed) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Scan Procedure v0.1** (the loose-end review standard; C-108; `check_scan.py` its shipped gate) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Diet Procedure v0.1** (the working-set eviction standard — the eviction grammar, the fact-presence gate, the behaviour test; C-111) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **The Registry** (`Registry/README.md` — the standards library, C-113: five-rule contract, honest statuses) | GOV | repo root (`Registry/`) |
| **Vocabulary Extension Procedure v0.1** (instance-side role extension, checker-hooked; C-114) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Kernel Migration Procedure v0.1** (the release seam's demand side; C-117; the §8 advisory template — first instantiated at beta-0.6, `Interface/Advisory_2026-08-20_beta-0.6.md`) | GOV | `/Claude/Project Governance/Governance Documents/` |
| **Scholarly Source Convention v0.1** (the first content convention; C-115) | KG | `/Claude/Architecture/Concepts/Knowledge Graph/` |
| **The Capture — Vision to Horizon** (C-103 — approved public-identity raw material; dossiers at `Site/Capture Materials/`) | GOV | `Conversations/Capture_2026-08-16_Vision-to-Horizon.md` |
| **License layer** (C-099 — Apache-2.0 · CC BY 4.0 · `NOTICE`; the name not licensed; terms travel with newborns) | GOV | repo root |
| Claude Code client adapter (`CLAUDE.md`, stable root filename; canonical per C-065 — content a C-035 compression of Conversation Settings) | GOV | repo root (`Desktop/FRACTAL/`) |
| **Client Library** (canonical living catalog of vendor surfaces, **C-097** — per-client discovery, adapter template, mechanics; no runtime API, currency via the C-094 loop; the Codex entry complete since v0.3) | GOV | `/Claude/Project Governance/Governance Documents/` (`Fractal_Client_Library.md`) |
| Codex drone adapter (`AGENTS.md`, stable root filename; canonical per C-065 class, installed per C-066 — drone-scoped C-035 compression) | GOV | repo root (`Desktop/FRACTAL/`) |
| Loose-Ends Scans #1–#6 (C-058) · Stranger Test #1 · the Flight records (Refinement · Diet pair · Migration-Test · Updatability · Scan-5 Gas-Metering · the beta-0.6 delta review) | GOV | `/Claude/Context Packages/Conversations/` |
| **Release provenance anchors** (C-090 — per-release tag attestation + OpenTimestamps receipt pairs; first member `beta-0.1`; receipts upgrade to Bitcoin-final mechanically at any later session) | GOV | repo root (`Provenance/`) |

*The canonical document rows above carry minted `DOC-…` identities (C-041/C-042; infrastructure rows the C-006-adjacent exception); alias binding per C-061, the versionless alias only where a series pointer exists (S5-2.3). Facets under the `FACET` root (C-043).*

## Naming convention (decision C-012)

**Living projections** use a **stable filename**, version inside — no filename version tokens, machine-enforced since C-080. **Historical / sequential artifacts** (Governance Protocols, Return Packages) carry versioned or dated filenames. **Canonical specifications** are versioned artifacts (C-040), each version its own DOC identity, the versionless alias tracking the newest (C-061). The ChatGPT-era files live under `Archive/` (C-063); this file is the one place their paths are maintained.

---

**Sources:** the Governance Protocol series (`Claude/Project Governance/Governance Protocol/`, route `PROT`) and the Decision Register (stamp inside, C-012) — the of-record homes of every session narrative this table once carried; the routed documents themselves (stamps inside, C-012); the Knowledge Graph Store route bindings (C-046/C-053).
*(Sources narrative retired 2026-08-17, the C-110 diet, first conformant exercise of Fractal_Diet_Procedure_v0.1 — index only, **no disposition changed**; rows further trimmed 2026-08-20, the beta-0.7 diet — no disposition changed; per-session narration lives frozen in the protocol files `Governance Protocol/Fractal_Governance_Protocol_Claude_v<X.Y>.md` and the dated `Conversations/Return_Package_<date>_<topic>.md` — the concrete patterns per Diet §6.1, S5-5.2's cure.)*
