# Templates — the seed tier (C-131)

> **CANONICAL — the kernel's built-but-empty structure.** The seed-tree principle (C-131, ratified 2026-08-20): the kernel consists of exactly two artifact kinds — **instructions** (the standards, formats, guides) and **built-but-empty structure** (the tools, and these seed editions). Filled content is *always* instance growth — instance-class by definition, even in kernel document series. From this seed tree, each FRACTAL-governed project grows however it needs to grow.

## The seeds (the bounded set — the kernel trio's halves + the shared buffer)

| Seed | Instantiates as | Pair (C-124) |
|---|---|---|
| `Fractal_Agenda_Board_Seed_v0.0.html` | `User Documents/<Name>_Agenda_Board.html` | Local Context ↔ Board (dynamic pole) |
| `Fractal_Roadmap_Seed_v0.0.html` | `User Documents/<Name>_Roadmap.html` | Global Context ↔ Roadmap (stable pole) |
| `Fractal_Fieldnote_Handout_Seed_v0.0.html` | `User Documents/<Name>_Fieldnote_Handout.html` | buffer ↔ Handout (the manual — pure instructions) |
| `Fractal_Fieldnote_Buffer_Seed_v0.0.md` | the instance's buffer file (`FIELDNOTES.md` at birth) | the kernel pair's governance original (C-121) |

**The set is bounded to the kernel trio (Discipline B):** every seed is a standing migration obligation for all future kernels — three pairs is cheap, an open-ended set is a tax. Extensions (an instance's own pairs, e.g. the mother's Update Plan and Gas pairs) are instance-tier by the five-step Pair Procedure and never get kernel seeds. The named second candidate for a future seed, taken deliberately at its next natural touch, is the Context Index (its seed lives embedded in `genesis.py` today).

## The disciplines (what makes seeds an upgrade path, not a burden)

1. **Seed editions are frozen, versioned artifacts (C-040 class).** A structural change is a new edition (`_v0.1`, …), the old file retained as history. A kernel upgrade ships the new edition; the migration delta is the mechanical diff between two seed files.
2. **Every grown document carries a "Grown from:" stamp** naming its seed edition (the adapters' *Projection of* stamp, same shape). Migration logic: `hash(instance file) == hash(seed edition)` ⇒ ungrown ⇒ auto-replace, zero judgment; grown ⇒ the judgment path, guided by the seed diff.
3. **The coupling row:** a Format reissue (e.g. the Agenda Board Format) triggers a seed-edition check — the C-059 walk's pair-series row carries it (the Schema → Template coupling precedent).

## Placeholder grammar

`{{INSTANCE}}` — the instance's name · `{{DATE}}` — the birth date (ISO) · `{{OPENER}}` — the named opener word (C-106) · `{{BUFFER_PATH}}` — the buffer's repo-relative path · `{{BUFFER_HREF}}` — the buffer's href from `User Documents/`. `genesis.py` fills every placeholder at instantiation and refuses a seed with any left unfilled.

---

*Born 2026-08-20 (C-131 — the seed-tree ratification; Scan #6's session). The seeds' structure was extracted from the mother's grown documents — the mother's own files now carry Grown-from stamps naming these editions, which is retroactively true by construction: the empty form is what her growth grew on.*
