# Proposal — The Kernel-Layer Doctrine (engine · contract · content — the update lesson)

> **PROPOSAL — PRE-CANON, GOVERNS NOTHING (frozen at issue).** Drafted for Max's ratification (C-033, at a close). Commission of record — Max, the thirty-seventh session, 2026-08-22, expanding the KNet re-foundation question by deliberate horizon-widening: *"when a software product receives an update, it retains a certain structure, and updates add a feature, change a feature, delete a feature, but the system stays the same. This is an idealised state for fractal"* — with the worked example his own (Ableton 11 → 12: new engine, your files stay, each old file converted at first touch by a save-into-new-format prompt; 11.1/11.2 incremental inside a major) — and the derivation his closing sentence: *"What I derive from this, the kernel may need two layers."* Sibling and feeder of `Proposal_2026-08-21_Birth-State-Law.md` (its item 3 manifest and item 7 KMP step are this doctrine's carriers); nothing here executes before ratification.

**Issued:** 2026-08-22 · **Author:** Claude (AGENT.AI.CLAUDE), drafting to Max's direction · **Evidence:** `Review_2026-08-21_Beta-0.7-Integration-Frictions.md` (the seam law); the KNet migration record (P-008, P-024 — two merges, zero swaps); `Review_2026-08-21_Rule-Corpus-Flight.md` (KMP-* rows: every migration duty currently one undifferentiated ceremony) · **Ratification open:** §4, severable

---

## 1 · The observed ground

Every kernel update a child has ever performed was a **merge**. KNet has migrated twice (beta-0.5, beta-0.7) and never once *replaced* a kernel file wholesale — each migration compared old against new, wove deltas, recorded exclusions, and left the scar tissue the friction register catalogued. The cause is structural, not procedural: the shipped kernel is **fused** — tools, format specifications, governance contracts, and template-shaped documents travel as one undifferentiated mass, so no updater can know what is safely swappable and what would overwrite a child's tissue. Under fusion, *every* update must be treated as if it were a format break: maximal ceremony, per-file judgment, fracture-generating. The register's seam law (every fracture at a jurisdiction boundary) is this fusion observed from the outside.

The mature-software counter-model, per the commission's worked example, separates **three** things: the **engine** (the application — replaced wholesale at every update, no merge, user files untouched); the **file format** (the contract between engine and content — the *only* thing whose incompatible change defines a major version); and the **user's content** (never inside the engine, conforming to a format version stamped *inside each file*, converted across a break **lazily, per file, at first touch**, via a visible prompt). The user experience Max named as FRACTAL's idealised state — "the system stays the same" — is downstream of exactly this refusal to fuse.

## 2 · The doctrine (draft — the two kernel layers, and the third thing that is not one)

> **The Kernel-Layer Doctrine.** The kernel has two layers, and child content is not a layer of it:
>
> - **Layer A — the engine.** The tools and their tests, the checkers, the command files, the executable rituals: kernel elements that never grow child tissue. Engine elements are **swapped, never merged** — at birth and at every update alike. A release touching only Layer A is a **minor release**: mechanically adoptable, near-zero ceremony, guaranteed not to touch child content.
> - **Layer B — the format contracts.** The Schema, the Node Template, the Navigation Contract, the document formats (Board, Fieldnote, the Local Context's shape, the pair-series standard), the governance contracts: the declared shapes child content conforms to. **An incompatible change here — and only here — constitutes a major release.**
> - **Child content is not kernel.** The store, the documents, the instance's decisions belong to the child, *conform to* Layer B editions, and cross a major break **lazily**: each living document converts at first touch, prompted; frozen artifacts never convert (accretion already exempts them — history is supposed to hold old formats).

The Birth-State Law's two-seam doctrine gains its missing refinement: *birth is a pure function; upgrade is a merge* — **but under this doctrine, upgrade is a merge only at Layer B breaks.** A minor update is not a merge at all; it is engine replacement, the same pure move as birth restricted to Layer A. The merge ceremony — the KMP's full weight — is reserved for the rare, declared contract break.

## 3 · What already exists — the two prerequisites FRACTAL built without knowing it

1. **C-012 is the format field.** Every living document already carries its version stamped inside — the exact mechanism the first-touch prompt requires. A converter needs only: read the document's declared format edition, compare against the running Layer B contract, offer the conversion when the file is next touched. The stamps were designed for currency checking; they are the migration field.
2. **Frozen/living already assigns the migration duty.** Frozen artifacts (protocols, return packages, reviews, superseded spec editions) never migrate — by standing law, not by new rule. Only the living surface carries format-currency duty, and it may carry it lazily. The estate-at-once migration that made KNet's updates heavy was never required by doctrine; only fusion made it look necessary.

## 4 · The ratification slate (severable; "ratified" authorizes the named builds)

| # | Item | Class | Carrier |
|---|---|---|---|
| 1 | **The layer bit** — the birth-state manifest (Birth-State item 3) records, for every kernel element, `engine` or `contract` (child-content stances already covered by the five-stance artifact axis). One added field; the manifest becomes the updater's map as well as the birther's | manifest amendment | the manifest file (rides Birth-State item 3's build) |
| 2 | **Semantic versioning at the release seam** — a release whose delta touches no Layer B element is **minor** (checkable at pack: the delta diffed against the manifest's contract set — the guarantee is machine-verifiable); a Layer B break is **major, declared in the advisory**. The beta series graduates to **Fractal 1.0** at the first release whose contracts are declared stable; thereafter 1.x minors, 2.0 the next declared break | release-seam doctrine (C-116/C-117 class — repo ritual, not conduct) | `close.py --pack` + the §8 advisory template |
| 3 | **The KMP fork** — minor update = Layer A replacement, a thin mechanical procedure a child eventually runs self-serve; major migration = the existing ceremony, now scoped to Layer B and its dependents only. Extends Birth-State item 7 (the KMP reads the manifest) with the layer read | KMP v0.2 reissue (shared carrier with Birth-State item 7) | `Fractal_Kernel_Migration_Procedure` |
| 4 | **The first-touch converter** — the mechanized prompt: a check reading a living document's C-012 stamp against the running contract edition, offering conversion at first touch after a major; frozen artifacts exempt by law. Prose-first per the registry pattern: the ritual named now, the tool built when the first major break makes it real | procedure (checker trigger named, not built — C-108 registry class) | the KMP reissue names it; tool on first major |
| 5 | **KNet's crossing** — the re-foundation in place as KNet's transition *into* the two-layer world: census first (the fracture detectors over its tree — decide with numbers), the scope-axis pass as the retroactive manifest, then one reviewed change-set in its own chain — Layer A poured fresh from the beta-0.8 kernel, content carried and re-pointed once, both checkers green, Q07's frozen grant confirmed byte-identical. Sequenced strictly **after** beta-0.8 packs; executed in KNet's jurisdiction as its own ratified act; the first execution becomes the corpus a Re-foundation Procedure is later distilled from (C-094) | instance act + procedure seed | KNet's own session + close; mother-side only the kernel and the instruments |

Items 1–3 feed the beta-0.8 lane beside the Birth-State slate (shared carriers, no blocking); item 4 arms and waits; item 5 waits on beta-0.8 and KNet's own word.

## 5 · Boundary

Pre-canon throughout; this document mints nothing, changes no conduct, and builds nothing. It **feeds** the Birth-State slate at two named joints (items 3 and 7) rather than competing with it — one manifest, now three consumers: genesis (birth), the KMP (upgrade), and the release gate (version arithmetic). The Engine Routing Foundation candidate is untouched — "engine" there names inference routing, here the tool layer; the collision is lexical and flagged for the namer's call at ratification.

---

*Frozen at issue. Ratification, wholly or by severed item, is Max's act at a close; the ratifying Protocol becomes the reasoning of record.*
