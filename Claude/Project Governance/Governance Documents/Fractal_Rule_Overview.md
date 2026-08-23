# Fractal Rule Overview

> **DERIVED PROJECTION — the one-page rule-book, not a source of truth.** Every rule below is defined authoritatively in the document named in its *Source*; this overview only collects them so the whole system's rule-set can be read at once (per C-003 it cites and never overrides). Living document: stable filename, version tracked below. Canonical copy: `/Claude/Project Governance/Governance Documents/`. **Part of the context package (C-036):** routed in the Context Index as a standing guideline of work and read in-repo, exactly like the Decision Register (C-030; the mirror mechanism retired 2026-08-14, C-067). **The mother's own grown edition (the C-134 seed-body law):** a newborn never receives this file — genesis generates a kernel-scoped seed edition of its own; the grown rows below are this instance's biography.

**Version:** 0.59 · **Status:** Living (derived projection) · **Updated:** 2026-08-23 · **Domain:** GOV · **Author:** Claude · **Parent:** Fractal Global Context · **Document ID:** DOC-01KZVYPMBGEY2HV35F32631G0C

**Why this document:** FRACTAL's credo is that the most complex structures arise from the simplest set of rules. This page is that set, made visible — five layers, each small, each traced to its decision of record.

---

## 0 · The meta-rule (philosophy)

**Recursive simplicity / minimal necessary complexity.** Begin from the smallest abstraction; add only what an observed problem requires; the same pattern repeats at every scale. Corollaries: lean wins ties under fixed quality; build on observed need, never anticipation. *Source: Global Context §1; Protocol v0.1; C-021.*

## 1 · Conversation rules (how every session behaves)

*Source of truth: Conversation Settings v0.9, §4 rules 1–10.*

| # | Rule | Anchor |
|---|---|---|
| 1 | Orient from the Global Context first; never scan the whole folder to orient. | CS §4.1 |
| 2 | Canonical documents in the folder are the sole source of truth; packages and Project docs are derived projections. | CS §4.2 / C-003 |
| 3 | Load only what the task needs — Global → Local; Domain, Task and Return are scopes of the Local pole. Resolve through the Context Index. | CS §4.3 / C-009, C-054 |
| 4 | Stay in the declared domain; keep accepted decisions separate from proposals; externalise durable work promptly. | CS §4.4 |
| 5 | Ask before executing until the workflow is calibrated — calibration = recorded per-action promotion, each covering exactly the action it names. | CS §4.5 / C-008, C-064, C-071 |
| 6 | Close substantive conversations with a Return Package, change summary, and refresh list. | CS §4.6 / C-001 |
| 7 | Every exported artifact carries exactly one stable identity, `Fractal_<Name>_v<major>.<minor>`, authored in `.md` (store node files exempt). | CS §4.7 / C-005, C-041 |
| 8 | Continuity & primacy: the queued *Next* is genuine foreknowledge — expected when taken up, an offer when not. The user's request is primary. | CS §4.8 / C-031 |
| 9 | Reference copies govern nothing: a session in a release copy never closes, edits canon, writes the store, or pushes — it reads, explains, and midwifes. | CS §4.9 / C-091 |
| 10 | Adopt before invent: check the Registry (`Registry/README.md`) and the shelf of specified components (GENESIS §5; here, this overview + the Architecture State) before building any new working tool or projection. | CS §4.10 / C-092 (the shelf check) · Registry rule 3 / C-113 (the registry-first clause — normative home the Registry contract; the Settings fold-in awaits the next conduct reissue) |

## 2 · Governance rules (how decisions and documents behave)

*Norms only; each row's history lives in its Decision Register rows and the cited protocols.*

| Rule | Content | Source |
|---|---|---|
| Projection integrity | Projections are labelled, cite sources + date, never become authoritative. | C-003 |
| Update ordering | Conversation → canonical update → protocol (if needed) → context-package refresh. | C-004 |
| Living-document naming | Living projections: stable filename, internal version. Historical artifacts: dated/versioned filenames. Canonical specifications are versioned artifacts — every substantive change is a new version, never an in-place revision. | C-012, C-040 |
| Review act | Review = explicit in-conversation acceptance after a walkthrough, recorded in the next protocol; status flips Draft → Ratified; `Review Owner` until reviewed, dated `Reviewed By` after. | C-033 |
| Open-question ledger | The Decision Register's OQ section is cumulative; items enter with a disposition and leave only by recorded disposition. | C-034 |
| Reviews are canonical | Whole-project reviews are canonical, sequential, dated artifacts — DOC-minted, never revised; findings carry stable ids dispositioned in the Register's review-findings ledger. Four procedure variants: the Loose-Ends Scan (`Fractal_Scan_Procedure_v0.1`), the capture-review, the simulation, the diet (`Fractal_Diet_Procedure_v0.1`). | C-058, C-103, C-108, C-111 |
| Ultracode flights (multi-agent programs) | A governed multi-agent program is a flight under `Fractal_Ultracode_Flight_Protocol_v0.2`: fixed launch sequence with mechanically enforced per-phase effort, declared gating mode (gated/continuous) and verification tier, derived agent counts, proposal-only landings, dated flight record with cost honesty. | C-108 |
| Cross-instance data grants | A child instance receives a frozen copy of an anchored release state (the C-090 tag is the grant unit) — never a window into the living mother. First execution: the Register's C-109 row. | C-109, C-096 |
| Close checklist | Every close walks the full living-projection table — stamps *and* content (C-077) — each row marked *changed* or *checked — unchanged*; Return Packages open *Next* with the auditable handover; every close = Return Package + protocol or recorded reason none. | C-059, C-077 |
| Version agreement | The close runs both checkers — `verify.py` (store fold) and `check_versions.py` (corpus claims + path existence); red from either blocks the close; frozen artifacts exempt from currency, never existence; the SUPPRESS list stays short and Max-ratified. | C-050, C-060 |
| Stamped projections | Every client adapter carries a governed projection of Conversation Settings with a version stamp naming source + date; sync-check = stamp comparison; re-project, never hand-fork. No vendor-held projection currently exists. | C-035, C-065, C-071, C-089 |
| Close mechanics | The mechanical tail of a close may be driven by `close.py` (the fourth store tool); dry-run by default; judgment is never delegated to it; both checkers remain the only gate. | C-073 |
| The adaptive close | The close touches only what needs renewal: file hashes drive the mechanical half, the Register is the judgment dirty-flag, narration scales with the change-set — a small session's close is the micro shape. A close of any size ends its conversation. | C-112, C-106 |
| The diet (working-set eviction) | Living-tier eviction runs under `Fractal_Diet_Procedure_v0.1`: measured or commissioned trigger, the pointer grammar (named record, index-only headers), the fact-presence gate (relocate row-born content or keep prose), optional behaviour test. | C-111, C-095, C-110 |
| The Registry (the standards library) | `Registry/README.md` catalogs adoptable standards under the five-rule contract: honest statuses (shipped/forging/named), prose + checker or it's a norm, registry-first shelf check, growth by ratified decision, adoption sovereign by the instance's own recorded decision. | C-113, C-108, C-092 |
| Vocabulary extension (instance-side) | Placement roles extend via `vocabulary_local.json` — each role names its adopting decision, collisions and silent growth are checker errors; verbs/alias kinds are interchange-layer and stay frozen. The file is an instance value; migrations preserve it. | C-114 |
| Sources & materials | A source file (PDF, video, dataset) is material, not knowledge (adoptable content doctrine per Architecture State §6): it lives outside the repo; the repo holds the catalog card (URL/content hash) and the extractions. Scholarly shapes per `Fractal_Scholarly_Source_Convention_v0.1` — pinned editions, identifier routes, PER-not-AGENT authors. | C-115 |
| The mirror rider (the release seam, supply side) | Every C-090 tagging close carries the public-home update, Claude-executed under standing authorization: curated sync from the fresh tag → rebuild commit → the mirror's own signed tag under the public identity → OTS receipt → push. Between betas the mirror deliberately lags; the flip act stays Max's own hand. | C-116, C-105, C-064 |
| The engine sketch (the public site's model) | The site exposes the machine's real parts verbatim from the shipped baseline, downloadable (`Site/commands/` + `Site/standards/`); every mirror command has a library entry; prose command mentions link their anchors (illustrations stay plain); parts folders refresh at each tagging close (C-116 sub-step); the rule register stays concept-level. | C-119, C-116 |
| The section contract (the site's floor plan) | Three sections, three reader intents: **Concepts** the dictionary/manual (full roster of commands + central concepts, a short description each, depth one click away; the register explained, never enumerated) · **Blog** the story (idea → origins → development → heading; the value model its forward chapter) · **the Research Labs** the research record (dated citable publications, own minimal layout, born empty; the KNet name waits on OQ-34's clearance — the pipeline interface-shaped when it opens). Sorting: updated-in-place → Concepts · dated-and-telling → Blog · dated-and-citable → Labs. Public prose implies its character, never announces it (the benched eighth conduct candidate). | C-130, C-119, C-021 |
| The public serving layer (live since 2026-08-18) | The site serves from the mirror's `gh-pages` branch — refreshes are ordinary pushes at any pace, pull-before-push as multi-writer hygiene (the domain rides the gate repo, not a `gh-pages` `CNAME` — the v0.58 correction); `main` keeps the pure release rhythm; the release rebuild preserves `.github/` + `gh-pages`. Public issues are the off-machine fieldnote door; PRs are proposals, never merges (cures ship upstream, credited); merge-commit-only; no web-UI commits ever. The gate (`knet.network`) is the umbrella's address, never FRACTAL's brand — its repo outside this jurisdiction. | C-120, C-116, C-094, C-084 |
| Kernel migration (the release seam, demand side) | A child adopts a newer anchored release only by its own recorded decision, under `Fractal_Kernel_Migration_Procedure_v0.1`: pin-and-verify, the sub-row adoption matrix classified by the pinned Architecture State §6, manifest growth paired to matrix rows, the semantic validation gate (green checkers insufficient), the per-release advisory template. A never-migrating instance is conformant forever. | C-117, GENESIS §7 |
| Scan conformance (the §12 gate) | `check_scan.py` red-blocks any Scan #5+ whose report or Register ledger integration diverges from the Scan Procedure — filename/header/state-block/id grammar/seed table, and no ledger row without a disposition. Frozen historical Scans warn, never error. | C-118, C-108, C-058 |
| Pointer-weight re-telling | One normative home carries a decision's full statement; every other living surface carries ≤ ~40 words + refs. Session-table rows: headline + of-record pointer; era-rows collapse at phase boundaries. | C-110 |
| Spine word budgets | Advisory tripwires on the living spine (Local Context ≤3,500 words, Index ≤2,000, session table ≤40 rows) plus the per-file drag gauge — the C-095 trigger measured, never felt; advisory yellow prompts a proposal, never an act. | C-110, C-095 |
| Settings upstream currency | The C-059 checklist carries a Conversation Settings row: any conduct-touching decision reissues Settings in the same close, projections restamp after — the source moves first. | C-071 |
| Agenda Board | The board is a standing stamped projection of the Local Context's agenda — repo file `User Documents/Fractal_Agenda_Board.html` (the dedicated user-documents folder, C-126), file-first refresh, never authoritative, offered actively by name when open threads accumulate; format canonized as `Fractal_Agenda_Board_Format_v0.3` (v0.2: the user-document bar, C-122, + the coequal-branch provision; v0.3: the `User Documents/` home + the extension-pill provision + **the rolling done bar, C-128** — newest ten chips on the surface, older ones fall verbatim to the sibling archive file, one standing link; the LC keeps its own era-compaction discipline, uncoupled). | C-047, C-048, C-035, C-089, C-102, C-104, C-122, C-126, C-128 |
| The user-document pair series | Every human window is the derived half of a pair whose original is a governance document (the original governs; one home, pointers elsewhere; the sorting rule). Kernel tier fixed at three pairs — Global ↔ Roadmap · Local ↔ Board · buffer ↔ Handout (the buffer governance-side); **all user halves live together in `User Documents/` at the repo root** (C-126 — the human's own folder; **born at genesis already built but empty since C-131** — the seeds instantiated, superseding born-on-first-use; originals stay in their natural homes); extensions are instance-tier by the five-step standard `Fractal_User_Document_Pair_Procedure_v0.3` (kernel-shipped); the mother's first: the Update Plan pair — the release lane's one home, the board slimmed to status-plus-link. | C-122, C-124, C-126, C-131 |
| The seed tree | The kernel is two artifact kinds — instructions, and built-but-empty structure: the `Templates/` seed tier ships frozen v0.0 editions of the kernel trio's halves + the buffer shape; genesis instantiates them at birth; every grown document carries a **Grown from:** stamp naming its seed edition (hash-match ⇒ mechanical migration; grown ⇒ judgment guided by the seed diff); the set is bounded to the kernel trio, extensions never get seeds; *empty form = kernel, growth = instance* is the partition test. | C-131, C-124, C-126, C-040 |
| Behaviour conventions | A convention is a callable rule-set shaping how one class of output is represented — summoned into a scope by name (sandbox style: `/mrc` the first shortcut), binding the named task, composing with Conversation Settings, never overriding them, released at task end; members live on the Registry shelf (§4), adopted by recorded decision — the class kernel, the members shelf-tier; C-115's scholarly-source rules the retroactive first member, the MRC (five math rules) the second. | C-132, C-115, C-113, C-092 |
| The kernel ratification clause | Every instance's owner answers for everything inside their instance — and the kernel itself answers to the mother's owner: kernel artifacts as shipped are **auto-ratified at the origin**, one standing ratification holding the responsibility for all (the C-090 signed tag its cryptographic form; GENESIS §3.4's inheritance clause the child-side mirror). The responsibility is held to best knowledge, discharged through agents and gates — diligence delegated, the responsibility not; auto-ratification assigns responsibility and never bypasses review (C-033 unchanged). The vocabulary is deliberate: *ratification holding responsibility*, a governance concept, never a legal warranty. First exercise: the `Reviewed By` fields (Schema v0.7 · Navigation Contract v0.2). | C-133, C-090, C-074, C-033 |
| The Birth-State Law | No element enters the kernel without a declared birth-state on four axes — value (every jurisdiction-bound value a stamped GENESIS §2 parameter, the owner included), artifact (five stances), authority (**a newborn's promotion ledger is empty**; no standing authorization travels in a copy or a birth), tool-config (per-instance configs genesis writes). Backbone: the two-seam doctrine — birth a pure function, upgrade a merge; one manifest, three consumers (genesis · KMP · the release gate). Riders: the seed-body law (a newborn knows the shelf exists, carries no trace of any specific shelf object) and the robustness triad (defaults-on-silence · genesis.py the vendor-neutral contract · the day-one set-vs-defaulted receipt). | C-134, C-091, C-131, C-092 |
| The kernel layers | Layer A, the engine (tools, checkers, commands — never grow child tissue; swapped, never merged; engine-only release = **minor**) · Layer B, the format contracts (the shapes child content conforms to; an incompatible change here alone = **major**) · child content is not kernel — it conforms to contract editions and crosses a major break lazily, per living document, at first touch (frozen artifacts never migrate; the C-012 stamp is the conversion field). The layer bit rides the birth-state manifest; the KMP forks minor/major; semantic versioning stands **armed-inactive** — no meaning attaches to beta-0.x; activation is the owner's hold-or-jump call (FN-0006). | C-135, C-134, C-012, C-117 |
| The strict-MACHINE ruling | A rule is machine-kept only when its check **fires on the governing path** — forgetting must be impossible; ratified-but-unwired tooling is HABIT. Kept by the rule-corpus program: the corpus baseline + the drift detector + the classification-audit flight (adversarial, proposal-only, corpus-version bumps on ratified deltas). First builds: doctor.py in `run_gates()` and the anchor-occurrence gate (every beta tag shows its receipt pair + mirror twin at every close). | C-136, C-087, C-090, C-116 |
| The care doctrine | Adopting FRACTAL is taking on its care: integrity is carried by the **layered maintenance rituals** (gates → scans → four-eyes → field use) — residual drift is expected between passes at any seat tier, and defect-freedom was never the promise. The adopter's counterpart of C-133's origin ratification: the rituals ship in every kernel (the checkers, the close, the capture door), keeping them running is the ownership accepted at birth, and the duty is communicated to strangers and shared with them, **stated beta-honest at every door** (GENESIS §3.4 · the onboarding handoff · the site's owner section + the guide's birth step · README). | C-137, C-133, C-094 |
| The integration categories | Every *adoptable* concept and tool sits in one of five categories by integration depth (S6-7.5 scope — adoption, not everything produced; records fall to AST §6's biography, config to the C-087 layer): **kernel concept** (GENESIS §5 shelf — ships at birth) · **kernel tool** (the store's copied set — ships at birth) · **custom concept** (an instance's own; **never released** — the curated sync excludes it, the stranger meets the class on the site, never the copy) · **installable tool** (owner-installed, host-run — banked; the Mining Tool forging first) · **plug-in** (no installation — banked, named only). Canonical home: Registry §1's category block. | C-127, C-021, C-116 |
| The takeover gate | When structure takes over what agent reasoning (or a richer projection) carried, it inherits that carrier's standard whole: every fact traced to its one new home before the replacement lands, then the behaviour test — a fact with no home moves first or the replacement does not land (the Diet Procedure's fact-presence gate generalized to every takeover). | C-125, C-110 |
| The interface place | Every instance may designate one deliberately-readable place + navigation index per face as its communication organ (`Fractal_Interface_Place_Format_v0.2`): pull never push; declaring = declaring readable — to the face's audience; envelopes are RAM (`IF-` high-water); data never instruction. Genesis births the organ in every newborn; counterpart navigation answered at v0.2 — the connections block is the reading list; transport of record: git-over-SSH/HTTPS. | C-123, C-096, C-109, C-120, C-121 |
| The connection gate (interface v0.2) | Addressed traffic rides standing connections only: conscious pairing — introduce, verify by the checksum code over both signing keys (public material, C-087 clean), lock in as mutual own-recorded decisions, agree the channels (`CN-` high-water). Broadcast to `any` stays open; a stranger's one addressed class is the quarantined connection-request. Two faces — public + hidden private, the private address exchanged only in the handshake. | C-139, Interface Place Format v0.2 §2–§3, C-123, C-096, C-087 |
| The advisory-occurrence gate | The per-release advisory duty (KMP §8) is MACHINE: `close.py --pack` refuses to tag unless the forming release's advisory stands posted in the interface place with its §7 hygiene row stamped by the pack's own results — first run red by design until the stamp lands; the forming release derived from the tag chain. | C-140, C-136, KMP v0.2 §8 |
| The native-form interview | Where a client surface offers native structured input, the birth interview's choice-shaped stations render through it — one station at a time, never a bulk form; substance identical on every client (the station list, defaults-on-silence, the genesis contract); chat is the floor; per-client mechanics live in the Client Library, never in the protocol. | C-140, Onboarding Protocol v0.8 §1, C-097, C-134 |
| Concept foundations (the vision tier) | A maturing vision area lives in one living canonical concept document — Draft, non-binding; promotion is by ordinary decision on a named trigger; session captures stay frozen traces; a public blueprint is a stamped C-035 projection of it. | C-086 |
| Field testing (the proving process) | Every development landing for real use is proven by a field run: observations captured to the pre-canon fieldnote **buffer** (temporary memory — one per instance, worked off soon; capture is the off-topic jump, ratification the write gate; solved entries dissolve into the project, the pressure plug warns over budget), triage and ingestion at phase boundaries, fixes in the generator. Capture layer: `Fractal_Fieldnote_Format_v0.2` + `fieldnote.py`. | C-094, C-100, C-121 |
| Remove on observed drag (compaction) | Living projections compact at phase boundaries: narrative already frozen in Protocols / Return Packages / Scans is replaced by pointers to it — lossless by construction; the trigger is observed drag, per-document, never a sweep. | C-095 |
| Onboarding (the guided first loop) | A newcomer's first loop runs on one canonical script — `Fractal_Onboarding_Protocol`: the interview, the GENESIS birth, the midwife's exit, the child-side three-stage fade. Projections render from the script and never fork it. | C-101 |
| Distribution & the public home (release content) | The mother repo stays private; the curated mirror (`fractal-mirror`) is the permanent public home, carrying its own anchor chain; personal-class material routes to the private annex; publishing fires on observed need, never at a version point. | C-098, C-105, C-107, C-108 |
| Licensing | Free use, attribution preserved: code Apache-2.0 · documents CC BY 4.0 · NOTICE carries attribution; the name and marks are not licensed; terms travel with every newborn. Personal pre-canon is not licensed for reuse. | C-099, C-090 |
| Lineage | ChatGPT-era material is pointer-only — cited, never renumbered into the C-series. | C-029 |
| Anchoring | Canonical docs in the folder; the context package is read in-repo by every client; the mirror mechanism is retired and no vendor-held artifact exists — a future vendor client carries exactly one stamped adapter. | C-002, C-030, C-036, C-067, C-089 |
| Phasing | The Global current-realisation line changes only at genuine transitions (criterion TBD, OQ-4); the sequence is the phase history. | C-009, C-010 |
| Commit convention | Git author = the actual author of the change; message = `[DOMAIN] imperative summary` (+ refs); one commit per coherent change-set — the commit is the C-025 event boundary; committer semantics per §3's attribution row. | C-037, C-074, C-084 |
| Bootstrap | The repo rehydrates from `BOOTSTRAP.md` at the repo root, including the client-adapter step; acceptance = the "laptop in the ocean" test. | C-038 |
| Off-site copy | The off-site copy is a private GitHub repository (remote `origin`); the push rides every close under Max's standing authorization; the host is a C-018 swappable convenience. | C-056, C-064 |
| Protection model | Custody is layered — device · account · authorship (attribution never authenticates; custody-scoped signing, verification bound at root) · knowledge (append-only, hashed, verified, no-rewrite): alteration is evident and reversible, never hidden. Detail: the Register rows; BOOTSTRAP §4. | C-057, C-074, C-075 |
| Secrets | No canonical artifact ever holds a secret value; the fact of a credential is recorded, the value lives in the environment layer; deliberately non-durable — rebuild = re-issue against the recorded facts. Guard: `doctor.py`. | C-087 |
| Provenance anchor (releases) | Every shipped release tag is externally anchored at pack time — an OpenTimestamps attestation, receipt committed into the repo; the anchor-authority set is the ninth genesis parameter (GENESIS §2). | C-090 |
| Document identity | A canonical document's persistent ID is its minted `DOC-…` node; `Fractal_<Name>` is a route alias over it; DOC identity mirrors file identity — one DOC per version file, series pointers for living ids; client adapters are canonical artifacts. | C-041, C-042, C-045, C-061, C-065 |

## 3 · Knowledge-Graph format rules (how knowledge is recorded)

| Rule | Content | Source |
|---|---|---|
| Two relations, one log | Identity + Placement in one append-only Event Log; everything else is blocks added back. | C-014 |
| Identity ≠ context | A thing's identity is separate from where it sits; names and codes are aliases; the `TYPE-ULID` scheme is confirmed. | C-015, C-039 |
| Node file | Markdown + YAML front-matter; required identity `{id, type, created, created_by}`; foldering is navigation, not identity. TOP nodes carry `code:` + `facet:` (log-wins). | C-022, C-040 |
| Event log | Append-only JSONL, one event per line, one active file — only the recorded roll ceremony opens a new partition; verbs `{create, place, unplace, mint, alias, revise, run}`; alias kinds `{label, route, redirect}`. | C-023, C-045, C-055 |
| Log-canonical | The event log is authoritative; node `placements:` is a materialized fold of it, resolving codes through redirect chains. | C-024, C-045 |
| Supersede, never edit | No edit/delete; correction = new event with `supersedes`; state = fold in `ts` order. Events at commit, not per keystroke — the git commit is the boundary. | C-025, C-037 |
| Identity format | Standard 26-char Crockford ULID; the id prefix decodes into the `ts`/`created` second; generate with the store README's method, never by hand; `content_hash` = sha256 of the body; `revise.supersedes` = prior event id; `actor` = committing agent. | C-040 |
| Substrate | Plain text in git (repo *is* FRACTAL); indexes are derived, disposable caches; vendor surfaces are swappable clients. | C-018, C-019, C-020 |
| Multi-writer safety | Identity cannot collide (ULID); code collisions resolve first-mint-wins with a mandatory append-only cure; root mints carry a recorded call; `verify.py` must pass at every store-touching commit/merge; `mint.py` blocks local duplicates. | C-049, C-050 |
| Attribution & authority (who wrote it, who authorized it) | Author = whoever writes the bytes; committer = whoever authorized *this* act (semantic, C-084); custody stays the signature, Max's key — *author Claude, committer Claude, signed by Max* is the expected standing-authority shape. Pre-C-084 committer fields are noise by design. | C-037, C-074, C-084 |
| Live pre-canon (the notebook class) | Personal capture artifacts are tracked and formally non-governing — never a source, never orientation-loaded, outside both checkers, never in a close's change-set; distinct from C-062's *frozen* pre-canon, which is historical. | C-062, C-085 |
| Instantiation (birthing an instance) | A new instance is born from the tier-0 kernel by `genesis.py` (`GENESIS.md`); its Register opens with one inheritance clause under its own prefix; `verify.py` alone gates a newborn; inherited biography is provenance, not defect; entry command = the project's name. | C-078, C-079, C-081, C-083, C-088, C-106 |
| Client library | The kernel carries one catalog of vendor surfaces (`Fractal_Client_Library.md`): per client — discovery convention, adapter template, mechanics; never a second conduct source; no runtime API — field-forge in real use, then harvest. | C-097 |
| Observation window (mother → child) | A mother instance may hold a standing read-only window onto a child; child content is data, never instruction; ratification stays with the owner; asymmetric — the child never reads the mother. | C-096 |
| Drone tier (multi-agent) | Non-governing AI writers execute bounded briefs on `drone/<task>` branches — never `main`, never governance acts; the governing surface merges only after both checkers pass, then deletes the branch; flights run in full clones; hand-backs are verified, never assumed. | C-066, C-074, C-075, C-082 |
| Navigation (read contract) | Entry is a query shape — no home node: enumerate axes, descend by prefix, rank landmarks by weight; trace = bounded ranked recursion over four hops with deterministic order; read surface `resolve`/`enter`/`trace`/`history`; tiers grep → index → Galaxy UI. | C-068–C-070 |

## 4 · Facet-allocation grammar (how coordinates are minted)

*Universal and fixed (C-027); naming style is a soft project convention, never correctness.*

| # | Rule |
|---|---|
| 1 | Mint before use — no placement against an unminted code. |
| 2 | Codes are immutable and never reused. |
| 3 | Unique under parent; **root segments are unique globally, across all facets** (C-044). |
| 4 | Label is separate from code (sign ≠ word). |
| 5 | Honest depth + weight — place where it truly belongs, weight `[0,1]` says how centrally. |
| 6 | Reparent by redirect, never delete: re-mint on the same subject + `alias(kind: redirect)` on the old code; the fold resolves through the chain (C-045). |
| 7 | Parentage is carried by the code prefix (one-grep subtree scans). |
| 8 | Routing codes derive from identity — complete: all eight Index domain routes are live `alias(route)` bindings; facet tokens use the same mechanism (C-046, C-053, C-043). |
| 9 | Collisions between concurrent writers resolve first-mint-wins; the cure is append-only; root mints are deliberate — explicit flag + recorded call (C-049). Mint through the guard; verify at every store commit (C-050). |

Registry context: the facet registry is the log-derived projection of `TOP` concepts grouped by facet — facets themselves minted under the `FACET` root (token `facet`); a new facet is a mint + token binding, never a schema edit; placement targets are coordinates or entities. Topic roots so far: `KG`, `GOV`, `GBL`, `CTX`, `AST` (C-026, C-043, C-049, C-053; Schema §3.5).

## 5 · Standing caveats (rules about the rules' limits)

- The C-038 acceptance test is exercised green (2026-08-13) — "laptop in the ocean" is demonstrated fact; the drill rides every Loose-Ends Scan plus any custody/host change (C-076); whole-repo version agreement is mechanized at every close (C-060). Detail: the Register rows.
- Full open-question ledger: the Decision Register (stamp inside, C-012) — **the standing-open rows are the Register's OQ ledger, never an enumeration here** (the ledger is the count; this line stopped naming rows 2026-08-18 after the list went stale twice at this exact locus — CAP1-LAW-1, then S5-3.4); the review-findings ledger (C-058, including S3-2.2 held open and the `CAP1-…` rows) lives there too; pre-canon vision material informs, never governs (OQ-22). Per-item dispositions: the Register's ledgers and their protocols of record.
- **WS is the declared open part of the architecture** — no Claude-era canonical yet; forge on observed need (Architecture State §4).

---

**Refresh triggers:** any change to Conversation Settings, a new C-decision that adds/retires a rule, or resolution of a standing caveat.
**Sources:** Fractal Global Context; Conversation Settings (stamp inside, C-012); Governance Protocols — Claude Series v0.1 through the newest issue (stamps inside); Knowledge Path Foundation v0.1; Node & Event Schema v0.7; Navigation Contract v0.2; Fractal_Architecture_State (stamp inside, C-012); Decision Register (stamp inside, C-012); BOOTSTRAP.md (stamp inside, C-012); GENESIS.md (stamp inside, C-012); Loose-Ends Scans #2 (2026-08-14), #3 & #4 (2026-08-15); Capture_2026-08-16_Vision-to-Horizon.md (C-103).
**Revision history** *(compacted 2026-08-17, the C-110 diet, first conformant exercise of Fractal_Diet_Procedure_v0.1 — index only, one row per history entry, answering when/what, never how/why; the full narration of every change lives frozen in its of-record pointer)*

| Version | Date | Headline | Of record |
|---|---|---|---|
| v0.1 | 2026-08-12 | first consolidation, five layers, all rules traced | Decision Register (the entry's C-refs) |
| v0.2 | 2026-08-12 | joined the context package by Max's decision (C-036, per Protocol v0.8); added the substrate-realization rules … | Protocol v0.8 |
| v0.3 | 2026-08-12 | identity & schema consolidation (per Protocol v0.9) | Protocol v0.9 |
| v0.4 | 2026-08-13 | facet-layer completion (per Protocol v0.10) | Protocol v0.10 |
| v0.5 | 2026-08-13 | Agenda Board row added (C-047, per Protocol v0.11) — the C-035 stamped-projection rule exercised at … | Protocol v0.11 |
| v0.6 | 2026-08-13 | board row updated (C-048, per Protocol v0.12) — repo-resident file, artifact demoted to display surface, … | Protocol v0.12 |
| v0.7 | 2026-08-13 | multi-writer safety (C-049/C-050, per Protocol v0.13) | Protocol v0.13 |
| v0.8 | 2026-08-13 | workstream F (C-051–C-054, per Protocol v0.14) | Protocol v0.14 |
| v0.9 | 2026-08-13 | event-log layout (C-055, per Protocol v0.15) | Protocol v0.15 |
| v0.10 | 2026-08-13 | off-site copy & protection (C-056/C-057, per Protocol v0.16) | Protocol v0.16 |
| v0.11 | 2026-08-13 | OQ-22 resolved (Max's call | Decision Register (the entry's C-refs) |
| v0.12 | 2026-08-13 | C-038 drill | Decision Register (the entry's C-refs) |
| v0.13 | 2026-08-14 | loose-ends pass (C-058/C-059, per Protocol v0.17) | Protocol v0.17 |
| v0.14 | 2026-08-14 | checker canonized (C-060, per Protocol v0.18) | Protocol v0.18 |
| v0.15 | 2026-08-14 | spec-version identity (C-061/C-062, per Protocol v0.19) | Protocol v0.19 |
| v0.16 | 2026-08-14 | first Code session (C-063/C-064, per Protocol v0.20) | Protocol v0.20 |
| v0.17 | 2026-08-14 | adapter canonization (C-065, per Protocol v0.21) | Protocol v0.21 |
| v0.18 | 2026-08-14 | the drone doctrine (C-066, per Protocol v0.22) | Protocol v0.22 |
| v0.19 | 2026-08-14 | mirrors retired (C-067, per Protocol v0.23) | Protocol v0.23 |
| v0.20 | 2026-08-14 | the navigation close (C-068–C-071, per Protocols v0.24–v0.25) | Protocol v0.24–v0.25 |
| v0.21 | 2026-08-14 | Cowork write capability (C-072, per Protocol v0.26) | Protocol v0.26 |
| v0.22 | 2026-08-14 | close.py canonized (C-073, per Protocol v0.27) | Protocol v0.27 |
| v0.23 | 2026-08-14 | the custody session (C-074–C-076, per Protocol v0.28) | Protocol v0.28 |
| v0.24 | 2026-08-14 | custody-session postscript | Decision Register (the entry's C-refs) |
| v0.25 | 2026-08-15 | the Scan #3 session (C-077, per Protocol v0.29) | Protocol v0.29 |
| v0.26–v0.28 | 2026-08-15 | : instantiation rows (C-078/C-079/C-081/C-083), the drone row's C-082 amendment, the attribution & authority row (C-084 … | Decision Register (the entry's C-refs) |
| v0.29 | 2026-08-15 | the postscript protocol (C-086, per v0.34) | Decision Register (the entry's C-refs) |
| v0.30 | 2026-08-15 | the punch-list close (C-087–C-089, per v0.35) | Decision Register (the entry's C-refs) |
| v0.31 | 2026-08-15 | Scan #4, the pre-pack gate | Decision Register (the entry's C-refs) |
| v0.32 | 2026-08-15 | the phase-5 ingestion (C-091/C-092, per Protocol v0.38) | Protocol v0.38 |
| v0.33 | 2026-08-16 | the second-client-trial session (C-094/C-095, per Protocol v0.40) | Protocol v0.40 |
| v0.34 | 2026-08-16 | the postscript (C-096, per Protocol v0.41) | Protocol v0.41 |
| v0.35 | 2026-08-16 | the second postscript (C-097, per Protocol v0.42) | Protocol v0.42 |
| v0.36 | 2026-08-16 | the flip-preparation session (C-098–C-102, per Protocol v0.45) | Protocol v0.45 |
| v0.37 | 2026-08-16 | the capture session (C-103–C-104, per Protocol v0.46) | Protocol v0.46 |
| v0.38 | 2026-08-17 | the publishing-identity session (C-105–C-106, per Protocol v0.47) | Protocol v0.47 |
| v0.39 | 2026-08-17 | Flight-tier and data-grant rows added; reviews row gains the Scan standard; distribution row gains the necessity-trigger and registry-release clauses. (History entry reconstructed at v0.40 — the v0.48 close bumped without appending; the Register-v0.49 defect class.) | Protocol v0.48 |
| v0.40 | 2026-08-17 | Rule rows compacted to ≤40-word norms + refs and this history evicted to a pointer table — the C-110 diet, first conformant exercise of Fractal_Diet_Procedure_v0.1; no norm changed. | Register C-110/C-111 rows (protocol at this session's close) |
| v0.41 | 2026-08-17 | The diet session: adaptive-close, diet-procedure, pointer-weight, and word-budget rows added; flights row to v0.2; reviews row gains the diet variant (C-110–C-112). | Protocol v0.49 |
| v0.42 | 2026-08-17 | The registry release: Registry, vocabulary-extension, and sources-&-materials rows added; rule 10 registry-first (C-113–C-115). | Protocol v0.50 |
| v0.43 | 2026-08-17 | The twentieth-session close: the release-seam rows (mirror rider C-116; kernel migration C-117) + the scan-conformance gate (C-118); the materials row's class aligned to §6. | Protocols v0.52–v0.54 |
| v0.44 | 2026-08-18 | The engine-sketch close: the site-model row added (C-119 — parts exposed verbatim, refresh rides C-116, register concept-level). | Protocol v0.56 |
| v0.45 | 2026-08-18 | The go-live close: the public-serving-layer row added (C-120 — the gh-pages split, the intake doctrine, the gate as address-not-brand). | Protocol v0.57 |
| v0.46 | 2026-08-18 | The Scan #5 slate: §5's OQ enumeration replaced by the Register-ledger pointer (S5-3.4 — the CAP1-LAW-1 class ended at its locus); rule 10's source cell corrected to the registry-first clause's normative home (S5-4.1); the serving-layer row's CNAME claim cured to the gate-repo truth (S5-8.2); Sources made version-agnostic (S5-9.2). | Scan #5 + this session's protocol |
| v0.47 | 2026-08-19 | the field-testing row rewritten to the C-121 buffer model | v0.60 |
| v0.48 | 2026-08-19 | the board row to Format v0.2 (the user-document bar + branch provision) + the C-122 ref | v0.61 |
| v0.49 | 2026-08-19 | three rows added: the pair series (C-124) · the takeover gate (C-125) · the interface place (C-123) | v0.62 |
| v0.50 | 2026-08-19 | the board and pair-series rows carry C-126 — the `User Documents/` folder (the location law; Board Format v0.3, Pair Procedure v0.2) | protocol at this session's close |
| v0.51 | 2026-08-19 | the integration-categories row (C-127 — five categories, two banked; the custom-class mirror exclusion; the Mining Tool forging) | protocol at this session's close |
| v0.52 | 2026-08-19 | the board row carries C-128 (the rolling done bar + archive); the gas pair (C-129) rides the pair-series row's extension class | protocol at this session's close |
| v0.53 | 2026-08-20 | the section-contract row (C-130) | v0.64 |
| v0.54 | 2026-08-20 | the seed-tree + behaviour-convention rows; the C-127 row scoped to adoptables (S6-7.5) | Protocol v0.65 |
| v0.55 | 2026-08-20 | the C-133 rule row; spec-pointer currency to v0.7/v0.2 | Protocol v0.66 |
| v0.56 | 2026-08-22 | three rows: the Birth-State Law, the kernel layers, the strict-MACHINE ruling | v0.71 |
| v0.57 | 2026-08-22 | the care-doctrine row (C-137) | protocol at this session's close |
| v0.58 | 2026-08-23 | the connection-gate row added + the interface-place row to Format v0.2 (the interface v0.2 ratification ripple, Update Plan v0.16 row 5); the banner's grown-edition line (the C-134 seed-body law — newborns receive a generated seed, never this file); the C-139 ref seated at the mint | Protocol v0.73 |
| v0.59 | 2026-08-23 | two rows added at the beta-0.8 tagging close (C-140): the advisory-occurrence gate (the KMP §8 duty MACHINE — no tag without the posted, stamped advisory) and the native-form interview (choice-shaped stations through native client input, chat the floor) | Protocol v0.74 |
