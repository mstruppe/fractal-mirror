# FRACTAL Registry — the standards library

> **CANONICAL DOCUMENT — the standards-and-skills registry (C-108's commission, executed at beta-0.5).** Identity: `Fractal_Registry` — living document, stable filename, version tracked below. This is the library the Knowledge Network Foundation §6 envisioned, first implemented: a catalog of **adoptable standards** — procedures, formats, content conventions, mechanisms, and the session-command tier. **Every entry is an offer, never a mandate:** an instance adopts an entry by its **own recorded decision** (GENESIS §7.4 — upstream improvements adopted selectively, on felt need); the registry itself governs nothing.

**Version:** 0.1 · **Status:** Ratified (2026-08-17, in-conversation per C-033 — Max: *"ratified and close"*; decision C-113, per Protocol v0.50) · **Domain:** GOV · **Author:** Claude · **Parent:** Fractal_Knowledge_Network_Foundation §6 (vision tier) · C-108 (the commission) · **Document ID:** DOC-01M084YBNH6B261H40Y3KZRSY3 (minted 2026-08-17 via `close.py --create`; stamped by the post-mint revise)

---

## 1 · The contract

1. **Statuses are honest.** Every entry carries exactly one: **shipped** (ratified and in this tree at the named path) · **forging** (being built, in a named place — possibly another instance's jurisdiction) · **named** (demanded with recorded provenance, not started). A registry that fakes a status has broken its one job.
2. **Prose + checker, or it is a norm.** Per the Network Foundation's rule (§5, welded limit 3): *a standard without a checker is a norm, not a gate.* Each shipped entry names its checker half — or says **prose-first** and names the checker's build trigger. Both are legitimate; silence is not.
3. **Adopt before invent — the registry is the shelf.** C-092 extends here: before building any procedure, format, or convention, a session checks this catalog first and offers the existing entry. Build new only knowingly, after the check.
4. **Growth is by ratified decision.** An entry joins when the instance that forged it ratifies it; demand joins as a **named** row citing its provenance (finding ids, fieldnote entries, wishlist items). Foreign forges are listed honestly with their jurisdiction (the KNet precedent).
5. **Adoption is sovereign and recorded.** To adopt: read the standard at its canonical path → record the adoption as your own decision (`P-…`) → copy or bind any tool half → run its checker if one ships. A never-adopting instance is fully conformant; a silently-adopting one is not.

## 2 · Procedure standards

| Entry | Version | Status | Canonical path | Checker half |
|---|---|---|---|---|
| **Ultracode Flight Protocol** — the container standard for governed multi-agent programs | v0.2 | **shipped** | `Claude/Project Governance/Governance Documents/Fractal_Ultracode_Flight_Protocol_v0.2.md` | prose-first; trigger named (§9: first off-machine flight record, or a conformance dispute) |
| **Scan Procedure** — the loose-end review | v0.1 | **shipped** | `…/Fractal_Scan_Procedure_v0.1.md` | prose-first; the Scan-#5 conformance checker is the armed gate (C-108 — no next Scan closes without it) |
| **Diet Procedure** — working-set eviction | v0.1 | **shipped** | `…/Fractal_Diet_Procedure_v0.1.md` | prose-first; the drag-gauge gate is armed (no second diet closes without it) |

## 3 · Format standards

| Entry | Version | Status | Canonical path | Checker half |
|---|---|---|---|---|
| **Fieldnote Format** — machine-parsable field capture | v0.1 | **shipped** | `…/Fractal_Fieldnote_Format_v0.1.md` | **shipped** — `fieldnote.py` (capture + `parse` intake) |
| **Agenda Board Format** — the board standard | v0.1 | **shipped** | `…/Fractal_Agenda_Board_Format_v0.1.md` | prose-first; trigger named in the standard |

## 4 · Content conventions

The class the first simulated users demanded (flight RF1: every persona's High frictions were missing content standards; 27 registry-shaped wishlist entries).

| Entry | Status | Where | Provenance |
|---|---|---|---|
| **Scholarly Source Convention** v0.1 — the DOC shape for papers: identifier route aliases, external authors, edition pinning, claim citation | **shipped** | `Claude/Architecture/Concepts/Knowledge Graph/Fractal_Scholarly_Source_Convention_v0.1.md` | RF1-1 (High); prose-first, trigger in the standard |
| **Paper Information-Extraction Protocol** — the per-paper interview whose output is a standard event batch | **forging** — KNet (its jurisdiction; the mother lists, never reaches in) | upstreams via the C-094 loop | RF1 wishlist ×3 — independently specified by the researcher sim and queued in KNet |
| **Research-Question Queue Standard** — KNet's R-numbered open-research-queue format, generalized | **forging** — KNet's format exists; extraction as a standard is queued | arc-3 grab material (OQ-31) | RF1-7; the C-109 look |
| **Video Source Convention** — SRC.VIDEO.* vocabulary, source node shape, binary-asset policy | **named** | — | RF1-8 (High); the media policy paragraph ships in GUIDE/GENESIS at beta-0.5 |
| **Citation-Locator Standard** — pointing *inside* any source (page, timecode, section) | **named** | — | RF1-10 |
| **Speaker/Person Identity Convention** — cited people as PER entities, distinct from AGENT writers | **named** | — | RF1 byproduct; OQ-32-adjacent |

## 5 · Mechanisms and tools

| Entry | Status | Where | Provenance |
|---|---|---|---|
| **Vocabulary Extension Procedure** v0.1 — governed instance-side extension of inherited checker vocabularies | **shipped** — prose + checker both (the `vocabulary_local.json` hook in `verify.py`) | `…/Governance Documents/Fractal_Vocabulary_Extension_Procedure_v0.1.md` | RF1-2 (High) |
| **Argumentation Role Pack** — supports · contradicts · answers · qualifies · replicates | **named** — adoptable via the extension procedure once forged | — | RF1 wishlist |
| **Zotero/BibTeX Bridge** — import/export between reference managers and the store | **named** | — | RF1 wishlist; P-003 (Zotero adopted in KNet) |
| **Batch Placement Tool** — many guarded events in one write | **named** | — | RF1-4 |
| **Publication Ledger / Content Lifecycle Board** — pipeline formats for content work | **named** | — | RF1-16 + creator wishlist |

## 6 · The session-command tier (skills)

The shipped commands are the skill tier's first members — `/welcome` · `/begin` · the named opener · `/close` · `/look` · `/fieldnote` (`.claude/commands/`; the catalog of record is `Fractal_Command_Index.md`, `Claude/Context Packages/`). A newborn receives its tier-0 set at genesis (GENESIS §3.6); the words always work where menus don't.

## 7 · Contributing back

Forge in your own instance, under your own governance; capture the need and the result through the fieldnote door (C-100); upstream by sending the file. What proves out in the field joins this catalog by ordinary decision — the loop that built every standard above.

---

**Refresh triggers:** an entry ratified, a status change (forging → shipped), a new demand with provenance, a checker half landing, a Network Foundation §6 reissue that moves the vision this implements.
**Sources:** C-108 (the commission — beta-0.5 the registry release); Knowledge Network Foundation v0.3 §5–§6 (the standards-library vision and the prose+checker rule); `Flight_2026-08-17_Refinement.md` (RF1 — the demand evidence: three persona wishlists); the Decision Register (C-092, C-094, C-100); GENESIS §5/§7 (the shelf and the sovereignty rule).
**Revision history:** v0.1 (2026-08-17) first issue — the beta-0.5 registry release (C-113): structure + contract + the seed catalog (three procedure standards, two formats, the first content convention, the first mechanism — plus the demand rows from RF1, honestly *named*).
