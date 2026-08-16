# Vision Capture — 2026-08-15 · The network thesis, the landscape, and a monetization sketch

> **PRE-CANON (C-062 class) — formally non-governing.** Idea capture from a whiteboard session, not a source of truth and not orientation-loaded. Nothing here is decided; anything that matures gets canonized through the ordinary loop (conversation → decision → canonical update). **Primary source:** Max's notebook — `Vision thought scramble.docx` (live pre-canon, C-085), the scaling-law paragraph of 2026-08-15, rewritten here into presentable prose with Max's permission. Secondary sources: the live web scan and strategy discussion of the seventh Code session (this conversation).
>
> **Author:** Claude · **Idea provenance:** Max (notebook) · **Status:** Pre-canon sketch, frozen at issue · **Domain:** none (pre-canon carries no route)

---

## 1. The network thesis (Max's paragraph, made presentable)

*Rewritten from the notebook; the original wording remains Max's and lives only there.*

Systems that scale **superlinearly** — organisms, cities — share one property: every new node profits from infrastructure the existing nodes already paid for. Knowledge work today has the opposite shape. Every research project begins by rebuilding context: reading into terminology, chasing references, reconstructing what the field already knows. A meaningful fraction of all research labor is context reconstruction, repeated per project, per person.

A connected knowledge environment inverts this. When a new investigation starts inside the network, the existing knowledge *is already its starting state* — nothing to rebuild. The project plugs into the graph, makes its genuinely new findings, and reports them back through a standardized government procedure. Any other instance can then check that interface, see the new finding, and register it into its own graph; anyone needing to know *why* the finding holds can descend through the standardized provenance infrastructure to the full reasoning chain.

The sharpest part of the thesis is the **marginal-increment hypothesis**: the true contribution of most research artifacts is a small, decisive increment — tiny relative to the document that carries it. And that increment is **angle-dependent**: an astrophysicist and a biologist extract *different* decisive increments from the same paper. So the unit of exchange should not be the document but the extracted increment, standardized and recorded **at the face of the node** — each face noting what was extracted and from which context the extraction was initiated. After the first extraction from any angle, no one from that angle reads the whole paper again; scanners read faces.

The long-term consequence is a **scaling law for the network itself**: each instance joins warm (context cost → 0) and contributes its increment (network value ↑). The USP, in the literal sense, becomes the network's scaling behavior — value that no single instance, and no competitor without the network, can replicate.

## 2. Why FRACTAL is unusually well-shaped for this

The thesis requires primitives FRACTAL already has, built for other reasons:

| Thesis element | Existing primitive |
|---|---|
| Faces per angle at one node | Facet layer — context separate from identity (C-016/C-043); angle-scoped coordinates on a single Entity |
| Standardized reporting of findings | The governed session loop — close ritual, Return Package, Decision Register |
| "Check the interface, register the finding" | Federation's origin layer (arc 3, OQ-31): foreign graphs arrive namespaced; equivalence asserted by minted bridges, never inferred |
| "Dig deeper into why" | Navigation Contract — derivation as role-filtered trace over provenance edges |
| Tamper-evident history | Append-only event log, commit-as-event-boundary, signed custody |

One doctrinal brake, priced in deliberately: **meaning stays human** (C-018). A foreign finding is asserted into a graph by a human-ratified bridge, not auto-merged. Slower than the frictionless picture — and it is the trust layer that makes network content worth registering at all (OQ-27's territory).

## 3. The landscape (live scan, 2026-08-15)

The vision is shared; the winning execution does not exist. Three living relatives, one consistent failure mode:

- **Nanopublications** (nanopub.net) — assertion + provenance + publication info as a citable micro-unit; almost exactly the marginal increment. Millions exist (life sciences); after ~15 years still niche — hard to find, rarely cited. Knowledge Pixels now pitches nanopubs for researcher + AI-agent collaboration: the closest relative.
- **ORKG** (orkg.org) — EU-backed structured scholarly knowledge graph, "from documents to data," AI-assisted extraction, now with a foundation. Centralized, curator-driven.
- **Discourse Graphs** (discoursegraphs.com, Joel Chan) — claims/evidence/questions as modular shareable graph units. Chan's lab practice *is* the warm-start vision at lab scale ("I give new students my notes graph").

**The consistent failure mode: extraction labor.** Humans will not hand-write standardized claim-units; no career incentive rewards it; the network is worthless below critical mass.

**Why now / FRACTAL's angle:**
1. **The labor problem has a worker.** In FRACTAL the increment is a *byproduct of the governed session* — the AI collaborator writes the face-record as part of a close it already performs. The piece every predecessor lacked.
2. **Provenance became law.** EU AI Act high-risk obligations at full enforcement since 2026-08-02; the market needs tamper-evident, decision-linked audit trails — the substrate's native output.
3. **FRACTAL standardizes the *government*, not the artifact.** Predecessors standardized formats and hoped behavior would follow; FRACTAL standardizes behavior and lets the artifact fall out. Decentralized, git-native, no central platform to fund or trust.

## 4. SWOT (as discussed, compressed)

- **S:** vendor-independent substrate · dogfooded proof (self-governing repo, birthed instances, drills) · near-zero infra cost · provenance-complete by construction.
- **W:** n = 1 (one user, one governed project) · ceremony weight (~20k words kernel prose — OQ-28 is the recorded risk) · no UI · the product is currently a practice, not software.
- **O:** context-engineering wave (17+ context-layer platforms, memory as a benchmark discipline — all single-agent; none governed/federated) · AI-decision auditability as procurement need · kernel model as inheritable-boilerplate play · federation as the only network-effect layer.
- **T:** platform absorption (vendor-native memory/teams features commoditizing the continuity layer) · zero technical moat (readable plain text; defenses are brand, community, lead) · better models needing less ceremony.

**Wheel verdict:** the spokes exist (markdown+git, ADRs, event sourcing, adapter files, claim-units); the vehicle — a self-instantiating, provenance-complete, AI-operated project government with a federation path — does not.

## 5. Monetization ladder (realism-ranked, none decided)

1. **Methodology** — book/course/templates for governed AI collaboration; low build, rides the context-engineering wave.
2. **Open-core framework** — kernel + tier-0 tools free; paid tier = the already-specified tier-1 layer (index server, hosted UI, team features). C-079's tiering is accidentally an open-core pricing model.
3. **Vertical product** — audit-grade AI project governance for compliance-sensitive teams; where provenance becomes procurement.
4. **Consulting/installation** — n > 1 validation; funds the above; doesn't scale.

**The three-layer pitch:** warm start = the product story (week one) · audit-grade provenance = the why-now story (regulation) · the network scaling law = the moat story (arc 3). Never lead with the network — the cold start is brutal; FRACTAL must stay single-player-valuable first, and is.

## 6. Profiles — creators, roles, and the responsibility collapse (Max, same session)

A new agenda item, raised by Max after the strategy discussion: **profiles** — a node describing a creator (AI or human), carrying tiers of types. The sketch, with its FRACTAL-sense mapping:

- **Two categories, cleanly split.** *Descriptive* roles (**author**, **committer**) are attributed automatically by action — in FRACTAL terms they should be **folds of the event log, never assigned fields** (C-024 discipline applied to identity): "is X an author?" is a query the log answers, so it can neither lie nor stale. *Granted* roles (**owner**, **co-owner**, **editor**, **reader**) are normative: assigned, revocable, and new to the corpus.
- **The responsibility collapse.** Owner is the accountability terminus: every authority a non-owner exercises — including all AI permissions — is a delegation traceable to an owner grant. Already latent in C-084 (committer = whoever authorized; standing authority) and C-064; profiles would promote it from implicit to explicit doctrine.
- **Mechanics sketch:** profiles = the existing `AGENT.*` Entities, enriched; grants = placement events (append-only → full grant/revocation audit history for free); enforcement layered like custody (C-057) — the store records the truth of grants, the host and adapters enforce what they physically can.
- **Reader tier ⇒ private/public instances** — the role that makes the public-flip decision expressible, and the federation-facing role (a foreign instance reading a published graph is a reader by construction, OQ-31).
- **Open within it:** one owner + co-owner tier vs. true multi-owner (lean: single accountability terminus, co-owners granted); taxonomy = kernel rule / holders = instance value (an eighth parameterized decision); intersections with OQ-27 (per-writer keys attach to profiles) and C-066 (the drone tier is a role in disguise).

**The social extension (Max, same session): profiles as gates to knowledge worlds.** Profiles carry a **private ID** (the existing `AGENT-<ULID>` plus key material — cryptographic identity: what you sign is yours, verifiably) and optionally a **public profile** — a published *projection* of the private node (the C-035 pattern applied to a person). Public profiles then compose a **social network over the knowledge network**: a profile is the entry point over everything that identity has published (the Navigation Contract applied to a person); **selective disclosure falls out of the facet layer natively** (publish per-domain, per-facet, per-node — C-016's separation doing social work); and social actions — follow, endorse, critique — are signed placement events, making a "like" a citable assertion and **reputation a fold of the log rather than a gameable score**. The accumulation point of the marginal-increment thesis: a profile is where one's decisive increments live, each with provenance. Known scientists could research without boundaries *and* interact socially, on infrastructure where the interaction itself carries provenance. **Cautions of record:** impersonation → bridge to existing identity (ORCID, institutional keys) via minted bridge events, never inferred; private-ID/key hygiene belongs to OQ-30's secrets doctrine; trust and moderation are OQ-27 at human scale; and sequence discipline holds — this is arc-3-and-beyond vision whose *present* value is strategic: it is the cold-start answer the network thesis lacked (networks bootstrap on people; scientists join for peers, and the knowledge graph comes with them).

**Log-ins (Max, same session — "pull earlier, but not before necessary").** Entered the way the corpus handles all anticipation: as an **armed trigger, not machinery**. Today's protective layer already exists and is delegated — possession of keys down the C-057 custody ladder (device, remote SSH, signing key), coarse because repo access is all-or-nothing. A *native* login layer fires on either of two named triggers: **(1) the first FRACTAL-owned serving process** (tier-1 index server, a hosted published-instance — the moment authentication stops being the git host's problem), or **(2) the first reader grant to someone outside custody** (selective disclosure needs to know who is asking; repo visibility cannot express per-facet reads). Design constraints already fixed by doctrine: identity = the profile's key material (login is proving possession of the profile key — signature-based, custody doctrine extended from writing to reading); sessions/tokens are C-019 derived disposables; nothing canonical ever holds a secret (OQ-30) — the *fact* of every grant is a placement event, the credential never. Login is thus not a new pillar but the **enforcement face of the reader tier**, keyed by profiles, governed by the secrets doctrine.

**The economic layer — knowledge mining (Max, same session, at the close's edge).** The incentive diagnosis: knowledge is a public good (non-rival, non-excludable), so markets underfund it and R&D funding chases *direct* utility — most scientific work is not directly useful, and the extraction labor the network thesis needs has no reward anywhere today. The idea: **whoever verifiably adds genuine knowledge to the network is mining currency** — contribution *is* the issuance mechanism. Prior art in fragments: DeSci (ResearchHub's token rewards, VitaDAO), Filecoin's useful-work precedent (mechanically verifiable storage); the unsolved core is the **oracle problem** — chains verify computation, not truth, and every naive reward-for-content system (Steemit) died of Goodhart's law, a failure mode now existential in the LLM era of zero-cost plausible junk. **Why the idea is stronger inside FRACTAL than anywhere it has been tried: the verification process already exists and is the scarce signal.** Reward not submission but **registration** — a stranger's instance binding an increment into its own graph, signed, at cost to itself (it now builds on the increment: skin in the game) — weighted by the registrar's own earned standing (reputation-as-fold, §6). That is proof-of-useful-knowledge with the oracle answered *socially*, by the same meaning-stays-human doctrine (C-018) that runs the stack. Note also: the append-only signed log is already blockchain-adjacent — a chain adds nothing for *integrity* (git + signatures cover it), only for *scarce issuance*, so the chain question fires only if a currency does. **Cautions of record:** issuance design, collusion rings, securities/regulatory exposure — real dragons, deliberately unexplored. **Sequence:** the fifth layer of the stack (instance → portfolio → federation → society → **economy**), strictly behind the social layer whose registration signal it monetizes; entered as vision with that single named trigger, never machinery.

**The setup question, answered (Max, same session): a stranger does not inherit FRACTAL's custody posture.** Device encryption is OS hygiene FRACTAL recommends, never kernel setup; signing arms only at the second-writer trigger; drills, protection, and the drone tier are all tier-1. What remains (environment check, git identities per C-084, remote binding, the `.allowed_signers` rebind once signing fires, tier-appropriate checker runs) is **`doctor.py` — a sixth-store-tool candidate and a natural drone brief** (the `close.py`/`genesis.py` class: bounded, spec-complete, gated inside a birthed scratch instance per C-081/C-082). Design principle: **the doctor diagnoses by tier** — it checks only what the instance has adopted, making the tier system legible and serving OQ-28 by keeping un-adopted weight invisible. Hard line: it configures the deterministic and *reports* the privileged — device encryption and host 2FA are detected and instructed per platform, never performed (a trust-first project never asks for an OS password).

## 7. Open threads (offers, nothing queued)

- Naming/trademark check before any public flip ("Fractal" is crowded: Fractal Analytics, Fractal Design, …).
- Positioning one-pager; brand sketch (visual language latent in the ontology: galaxies, recursion, self-similarity).
- The specimen decision for the research-project experiment — in-repo folder vs birthed instance (recommendation on record: birthed instance beside the repo).
- Arc 2 re-framed by Max this session: deferred, to serve as the shippable-beta test case.
- `README.md` drafted at the root (derived projection, C-035 class) — the accidental first marketing artifact.

---

*Frozen at issue. If any thread above matures into a decision, it enters the Register through the ordinary loop and this sketch stays behind as its pre-canon trace. Scan sources (URLs) live in the conversation transcript of the seventh Code session; the durable pointers are the project names above.*
