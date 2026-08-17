# Fractal Scholarly Source Convention v0.1

> **CANONICAL SPECIFICATION (registry-entry class, content-convention tier) — the shapes for scholarly sources in a FRACTAL store.** The first content convention in the registry: what a *paper* looks like as a DOC node, how its identifiers become citable routes, how cited people differ from writers, and how an extracted claim points back into its source. Exists so a research instance's first session extracts knowledge instead of inventing information architecture (RF1-1, High: *"my core workflow — dozens of papers in, structured claims out — must be invented from scratch on day one"*). **An offer, never a mandate:** adopt by your own recorded decision (Registry contract §1.5); every shape below composes from the Schema's existing grammar — nothing here extends the interchange layer. Versioned artifact (C-040 class): frozen at issue; substantive change is a new version.

**Version:** 0.1 · **Status:** Ratified (2026-08-17, in-conversation per C-033 — Max: *"ratified and close"*; decision C-115, per Protocol v0.50) · **Domain:** KG · **Author:** Claude · **Date:** 2026-08-17 · **Provenance:** RF1-1 + the researcher persona's wishlist (`Flight_2026-08-17_Refinement.md`); P-003 (Zotero adopted in KNet — the live demand) · **Document ID:** DOC-01M084YMGM6ESY0AW9HFPB4HSY (minted 2026-08-17 via `close.py --create`; stamped by the post-mint revise)

---

## 1 · The paper node

One **DOC entity per paper** — the catalog card (GUIDE §4's minting rule applies: mint when something must cite it).

- **Title** = the paper's title. **Body** = the bibliographic facts in prose or a small front-matter block: authors as written, venue, year, and the **edition pinned** — *which version you read* (arXiv v2 ≠ v1; preprint ≠ camera-ready). A claim cited against an unpinned paper is a claim your corpus cannot check.
- **The file is material, not knowledge** (the media policy, beta-0.5): the PDF lives **outside the repo** (reference manager, annex, URL); the DOC node carries its `content_hash` when you hold the file — the hash binds the exact edition you cite — or its URL/identifier when you don't.
- **Source-type**: place the DOC under your source-type facet (`SRC.PAPER.JOURNAL`, `SRC.PAPER.PREPRINT`, `SRC.PAPER.CONFERENCE` — a starter set; **you mint these**, they are your roots' children, minted on adoption not inherited).

## 2 · Identifiers as routes

Bind each stable identifier as an **`alias(kind: route)`** on the paper's DOC node, in a flat lowercase grammar:

```
doi:10.1038/s41586-024-00001-1
arxiv:2401.01234v2
pmid:38000000
```

Route uniqueness is already machine-guarded (verify.py rule C) — two papers can never silently share a DOI, and `resolve("doi:…")` becomes a collision-free entry point into your graph. Pin the version *in* the token where the authority versions (arXiv); the DOI names the published edition.

## 3 · Cited people are not writers

**External authors are `PER` entities**, placed `by` on the paper's DOC. The `AGENT` facet is for *your instance's own writers* (the identity layer — commits, event actors); a cited author has authored knowledge, not events in your store. The two never mix: an AGENT places events; a PER is placed. (The general person-identity convention — speakers, interviewees — is a named registry entry; this section is its scholarly instance.)

## 4 · Claims and citation

An **extracted claim is its own entity** (a concept node in your domain, or a row in a per-paper note — your instance's style; the per-paper interview script that standardizes extraction is the *Paper Information-Extraction Protocol*, forging in KNet). The binding rules:

- The claim is placed **`cites`** against the paper's DOC — the edge your synthesis will trace (`trace(roles=[cites])` walks a conclusion back to its sources).
- **Locator**: until the cross-media Citation-Locator Standard ships (named in the registry), record the in-source position in the placement's note field — `p. 4`, `§3.2`, `Fig. 2` — stated here as the blessed interim convention (RF1-10's cure: officially *in the note field*).
- **Argumentation roles** (`supports`, `contradicts`, `qualifies`, …) are **not shipped here**: adopt them via the Vocabulary Extension Procedure (v0.1, beta-0.5) when your synthesis needs them — the pack itself is a named registry entry, and `cites` + weights carries a review's first weeks honestly (weight ≈ relevance grading: central evidence vs. merely-tagged).

## 5 · What this convention deliberately leaves out

The **Zotero/BibTeX bridge** (import/export tooling — named, unbuilt; adopting this convention first makes the bridge a mechanical translation later, which is the right build order) · the **research-question queue** (KNet's R-format, forging) · **PDF full-text policy** beyond the material rule (annex-class storage, copyright posture — instance values). Each is a registry row; none blocks day one.

## 6 · Conformance

Prose-first; the checker trigger is named: **the first adopting instance's first conformance dispute, or the bridge landing, whichever comes first** (the checker would validate: route-token grammar, edition pinning present, PER-not-AGENT on `by`, locator presence on `cites`). Until then: the store's own `verify.py` already guards the load-bearing halves (route uniqueness, placement grammar, hash recompute).

---

**Refresh triggers:** the locator standard shipping (§4's interim note-field rule retires into it); the extraction protocol landing from KNet (its event batch becomes this convention's §4 worked example); the bridge landing; a second adopting instance contradicting a shape here.
**Sources:** RF1-1/RF1-10 + the researcher wishlist (the demand of record); Node & Event Schema v0.6 (§3 grammar, §5.3 routes — every shape composes, none extends); Navigation Contract v0.1 (trace/resolve semantics cited); the media policy (GUIDE/GENESIS, beta-0.5); Fractal_Vocabulary_Extension_Procedure_v0.1; the Registry contract.
**Revision history:** v0.1 (2026-08-17) first issue — the beta-0.5 registry release: the paper DOC shape, identifier routes, PER/AGENT split, claim citation with the interim locator rule, the deliberate leave-outs.
