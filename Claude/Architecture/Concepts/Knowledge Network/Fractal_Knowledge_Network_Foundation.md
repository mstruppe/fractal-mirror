# Fractal Knowledge Network Foundation

> **CANONICAL CONCEPT DOCUMENT — Draft, explicitly non-binding (C-086).** This is the maturing home of the network vision: the layer stack from a single governed instance to a knowledge economy. It is **vision, not architecture** — nothing here binds a build; pieces enter the Architecture State only through ordinary decisions when their named triggers fire. It stands to the Global Context §1 as extension, never replacement: §1 owns *why FRACTAL exists*; this document owns *how far the same rules compose*. The Knowledge Path Foundation is its structural precedent — the concept paper that seeded the KG before any of it was architecture. Living document: stable filename, version tracked below (C-012). Any public blueprint or whitepaper is a **stamped C-035 projection of this document**, never a second source.

**Version:** 0.2 · **Status:** Draft (canonical concept — vision tier; issued 2026-08-15, per Governance Protocol — Claude Series v0.34; first external-evidence revision 2026-08-16) · **Domain:** GBL · **Author:** Claude · **Idea provenance:** Max (the notebook, C-085; the seventh Code session's exploration) · **Parent:** Fractal Global Context · **Document ID:** DOC-01M02SKWXHP3M2FB6G2K3KH4XB (minted 2026-08-15 via `close.py --create`; stamped by the post-mint revise)

---

## 0 · What this document is for

FRACTAL today governs projects. This document describes what the same small rule-set becomes when instances **connect**: a knowledge network with verified contributors, a social layer, and — at the horizon — an economy that pays for the work science currently starves. It exists for three reasons:

1. **To let the vision mature in one place** across sessions, instead of fragmenting into frozen conversation captures.
2. **To constrain present design cheaply** — each far layer back-propagates requirements the near layers can satisfy now, at near-zero cost, as armed triggers.
3. **To be publishable as a blueprint.** The deliverable does not have to be the built network; a blueprint precise enough that strangers could build it is itself a success condition (the whitepaper precedent). Publication, if ever, is a stamped projection of this document at a ship-boundary decision.

**Standing limit on everything below:** entries here are *triggers and constraints*, never build orders. The corpus's discipline — build on observed need, arm anticipation as named tripwires — applies to the vision itself.

## 1 · The problem

Research is fragmented twice over. **Within a project**, context is rebuilt at every tool switch and every session boundary — FRACTAL's founding problem, §1 of the Global Context, already addressed by the governed instance. **Between projects and between people**, the fragmentation is worse and unaddressed: every new investigation pays a context tax (reading in, terminology, references) before contributing anything; the decisive contribution of most research artifacts is a small increment buried in a large document; and the labor of extracting, verifying, and connecting knowledge is **systematically unpaid**. Knowledge is a public good — non-rival, non-excludable — so markets underfund it, funding chases direct utility, and the most verification-critical work in science (replication) earns nearly nothing. Prior attempts at structured scholarly exchange — nanopublications, ORKG, discourse graphs — share the vision and share one failure mode: **the extraction labor has no worker and no wage.**

## 2 · The thesis

Systems that scale superlinearly — organisms, cities — share one property: every new node profits from infrastructure existing nodes already paid for. A network of FRACTAL instances gives knowledge work that shape:

- **Warm starts.** A new project plugs into the existing graph as its starting context; the context tax trends toward zero.
- **The marginal increment.** The unit of exchange is not the document but the **decisive increment** — the small, *angle-dependent* contribution a work makes, extracted once per discipline and recorded at the face of the node (the facet layer, C-016, doing exactly what it was built for). After the first extraction from an angle, no one from that angle re-reads the whole artifact; scanners read faces. **Armed caveat (KNet R-02):** "only the delta is new" assumes an increment's value *separates* from the corpus it lands in; the record-value literature finds an externality between pooled records that complicates exactly that. The first foreign instance has the thread open against its own §6 — its answer transfers here.
- **The worker exists.** In a governed instance, extraction is a *byproduct of the session ritual* — the AI collaborator records the increment as part of the close it already performs. This is the piece every predecessor lacked.
- **The network law.** Each instance joins warm (cost → 0) and contributes increments (value ↑): the long-term USP is the scaling behavior of the network itself, which no single instance and no competitor without the network can replicate.

## 3 · The layer stack

Five layers, each riding the one below. Layers 1–2 exist; each higher layer is vision with named triggers.

| # | Layer | What it is | Status / trigger |
|---|---|---|---|
| 1 | **Instance** | One governed project: kernel + ledger + store + close ritual | **Live, proven** (arc 1: birth + close demonstrated) |
| 2 | **Portfolio** | One owner's instances sharing warmth | Arc 2 (deferred; the shippable-beta test case) |
| 3 | **Federation** | Instances exchanging increments — origin layer, import verb, bridge aliases | Arc 3; two instances must exist (OQ-31) |
| 4 | **Society** | Profiles as gates to knowledge worlds; social actions as provenance events | Behind federation (OQ-32 holds the doctrine) |
| 5 | **Economy** | Verified contribution mints currency | Behind society — its registration signal is what gets monetized |

## 4 · Profiles — identity, roles, responsibility (→ OQ-32)

A creator (human or AI) is a first-class node. Two role categories, never conflated:

- **Descriptive roles** (*author*, *committer*) are **folds of the event log, not assigned fields** — attribution by action, so the role can neither lie nor go stale (the C-024 discipline applied to identity).
- **Granted roles** (*owner*, *co-owner*, *editor*, *reader*) are **placement events** — assigned, revocable, append-only auditable. Grant history is free by construction.

**The responsibility collapse:** every authority a non-owner exercises — all AI permissions included — is a delegation traceable to an owner grant (latent in C-064/C-084; promoted to explicit doctrine here). Lean: a single accountability terminus per instance; co-ownership is granted, not plural. **Private ID** = the existing `AGENT-<ULID>` plus key material; a **public profile** is a published *projection* of it (C-035 applied to a person). Selective disclosure is native: publication can be per-domain, per-facet, per-node, because context was separated from identity from the beginning. **Log-ins** are the enforcement face of the reader tier — identity is proving possession of the profile key; sessions are C-019 disposables; nothing canonical ever holds a secret (OQ-30). Triggers: the first FRACTAL-owned serving process, or the first outside-custody reader grant.

## 5 · Verification — the two-layer gate

The network's load-bearing invention, and the place where the sharpest limits are welded on.

**Layer one — conformance gates *eligibility*.** Verification of *conduct* collapses to a check of adherence to an explicit standard: pre-registration before data, methods declared, provenance complete, data attached, analysis reproducible. Standards live in a **library** (§6); adherence is checkable — increasingly mechanically. This layer is cheap, parallelizable, and automatable; it is the same pattern as `verify.py`/`check_versions.py` (*red blocks*), pointed at experimental conduct instead of governance conduct. **Open quantity (KNet R-12):** the network's scaling arithmetic is denominated in the *cost structure of verification* — the sublinearity the whole warm-start law assumes — and the first literature scan found nothing for it. Instance-scale checkers are the tier-0 evidence; the network-scale claim is currently unproven, and either has a home literature (proof systems, complexity) or must be established by the network itself.

**Layer two — stake gates *value*.** What standards can never check: does it replicate, does it matter. Here verification is scarce and must be *costly*:

- **Registration** — a stranger's instance binding an increment into its own graph, signed, at cost to itself (it now builds on the increment: skin in the game). The unfakeable scarce event.
- **Replication** — a researcher testing another's hypothesis; the scientific gold standard, today chronically unrewarded. Approval of a replication is a **bet, not an opinion**: approvers stake standing they lose if the approval is later overturned (the prediction-market result — ~70–85% accuracy on replication forecasts — is the evidence this works).

**Limits welded on (each one load-bearing):**
1. **Vote on process, never on truth.** A community that must *agree with conclusions* before minting is an orthodoxy engine with money attached. The graph records who asserted what on what evidence; **disagreement is recorded, never resolved** (C-018 at network scale). Refutations and failed replications mint too — a negative result is knowledge, and paying only for confirmation buys confirmation.
2. **Standards gate eligibility; only skin-in-the-game gates value.** Conformance is exactly what LLMs fake best; a perfectly conformant claim earns *consideration*, never reward.
3. **A standard without a checker is a norm, not a gate** (the C-060 lineage). Library entries ship prose + checker, versioned together (the C-040 coupling pattern).

## 6 · The standards library — governance collapses to selection

The generalization of C-079's tiering: kernel components, R&D standards, and domain conventions form a **catalog**, and a project's government is composed at genesis by *selection* rather than inheritance-of-everything. Genesis gains one question: *which standards does this project adopt?* Adoption is an event (dated, attributable); conformance is thereafter checkable against a declared baseline; the setup tool diagnoses by adopted standard, keeping un-adopted weight invisible (the OQ-28 answer generalized: there is no single minimum — each project composes its floor). **Standards are themselves knowledge nodes** — versioned, DOC-minted, forked, registered, and improved by the network like any other increment: the governance layer becomes content of the network it governs. Recursive simplicity, one scale up. Domain communities contribute entries — both halves, prose and checker, or it is a recommendation, not infrastructure.

## 7 · The economy — knowledge mining

**The idea:** whoever verifiably adds genuine knowledge is minting currency — contribution *is* issuance. **Why it can work here and nowhere it has been tried:** the oracle problem (chains verify computation, never truth) is answered *socially* by §5 — minting attaches to **layer-two events** (registration, survived replication), weighted by the registrar's earned standing (reputation as a fold), with layer-one conformance as the unpaid eligibility floor.

Constraints fixed now, cheap:
- **The chain is a notary and a mint, never a database.** Knowledge, evidence, and identity stay in instances (git, signed); on-chain go event *hashes* and issuance. The existing append-only signed log is already anchor-ready; a chain matters only if a currency does.
- **Genesis imports mint nothing.** Translating existing scientific consensus into the network is a **genesis endowment** — attributed, unrewarded (the inheritance-clause logic at corpus scale). Coins exist only for new verified increments after genesis; otherwise bulk-import races follow.
- **Bootstrap from existing identity.** The initial node set inherits verification from the existing scientific network (ORCID/institutional bridges — asserted by minted bridge events, never inferred): a proof-of-authority genesis that blunts Sybil attacks where they are cheapest.
- **Keep the coin non-cash as long as possible.** First form: non-transferable standing (the reputation fold made countable). Transferability only if a genuine economic sink emerges — every step toward cash raises the attack budget against every mechanism above it.
- **What it pays for is the point:** the replication crisis exists because verification labor is unpaid. This economy's first product is a wage for exactly that labor.

**Dragons, named and unexplored by design:** issuance schedule, collusion rings, securities and regulatory exposure. They are layer-five problems and stay unexamined until a layer-five decision exists to need them.

**Dragons named by the network's own first child (2026-08-15, KNet session two — no longer unexamined, under live research in the child's queue):**
- **Distributional inversion** (KNet `P-002` / `R-08`): the mint may reproduce the funding gradient it exists to correct — under competition, agents share *less*, selectively less with the peers best able to use what they know, and raising the reward does not fully offset it (Chiplunkar, Kelley & Lane, NBER 32171). Instances competing to mint may withhold precisely from the instances positioned to build on their work. This is aimed at the vision's own distributional claim, not at a mechanism detail — which is why the child accepted it as a load-bearing risk by decision rather than a queue entry.
- **The ledger as strategic history** (KNet `R-06`): the event log is the revealed-preference data future incentive rules would be set from — so *can an instance shape the ledger to move tomorrow's rules in its favour?* An attack class on §7's minting governance that this document did not carry.

That the first foreign instance is performing the network's due diligence against the network's own vision — natively, under inherited rules, with sources verified before entry — is itself the strongest evidence yet for §2's thesis that extraction and verification labor can be a byproduct of the governed session.

## 8 · What this constrains today

The vision's present value is back-propagation, all of it already satisfied or armed: profiles need external identity bridges (bridge-event pattern exists); registration events must be anchorable (the signed log already is); OQ-30's secrets doctrine covers three future key classes (broker, profile, login) before the first key exists; the reader tier makes the public-flip decision expressible; and nothing — nothing — is built before its trigger fires.

## 9 · Open questions (pointers, not duplicates)

Ledgered: **OQ-27** (outside-custody trust — per-writer keys attach to profiles) · **OQ-28** (the weight dial — resolved in the limit by §6's composition-by-selection) · **OQ-29** (code as governed artifact) · **OQ-30** (secrets — three clients) · **OQ-31** (federation namespace — the origin layer) · **OQ-32** (profiles & roles — §4's doctrine home). Held here without numbers, awaiting their layer: issuance design; collusion resistance; standards-library governance (who admits an entry); the identity-bridge ceremony.

---

**Refresh triggers:** any session that materially advances the network vision (revise through the ordinary loop — this is a living document); a layer transitioning from vision to architecture (its section compresses to a pointer at the Architecture State's gain); a ship-boundary decision to project a public blueprint from this source.
**Sources:** Fractal Global Context §1 (v0.3); `Vision thought scramble.docx` (idea provenance — C-085, informs never governs); Vision_2026-08-15_Network-Thesis.md (the seventh session's frozen trace); Architecture State §6 (the instantiation seam); Decision Register (stamp inside — OQ-27–OQ-32); GENESIS.md (stamp inside); the seventh Code session's exploration (per Protocols v0.33–v0.34); KNet session two, reported by Max 2026-08-15 (the child's `P-002`, `KNet_Open_Research_Queue.md` `R-01`–`R-12` — external evidence, its own jurisdiction; `github.com/mstruppe/knet`).
**Revision history:** v0.1 (2026-08-15) first issue (C-086, per Protocol v0.34): the five-layer stack, profiles and the responsibility collapse, the two-layer verification gate with its welded limits, the standards library as governance-by-selection, knowledge mining with the oracle problem answered socially, and the back-propagated constraints — consolidated from the seventh Code session's whiteboard exploration (network thesis → profiles → social → log-ins → economy → standards), Max's framings preserved from the conversation of record. · v0.2 (2026-08-16) **first external-evidence revision — the network's first child reports back** (KNet session two, relayed by Max; the ordinary loop, this document's own refresh trigger): §7 gains the child-named dragons — distributional inversion (KNet `P-002`/`R-08`, the first empirically-grounded risk aimed at the vision's own distributional claim) and the ledger-as-strategic-history attack (`R-06`); §2's increment thesis gains the separability caveat (`R-02`, armed); §5's layer one gains the open verification-cost quantity (`R-12` — the scaling law's denominator, currently without a literature). Nothing here resolves in the mother: the threads live in the child's queue, and their answers transfer when they close.
