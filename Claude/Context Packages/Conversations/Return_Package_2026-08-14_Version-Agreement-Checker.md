# Return Package — 2026-08-14 · The Version-Agreement Checker (OQ-24 → C-060)

> **DERIVED PROJECTION — conversation handover record (C-001).** Sources: Governance Protocol — Claude Series v0.18 (Ratified); Decision Register v0.16; Local Context v0.22; `check_versions.py` (C-060).

**Parent:** Return_Package_2026-08-14_LooseEnds-Scan-2.md · **Local Context:** v0.21 → **v0.22**

---

## 1. Handover (C-059 auditable line)

**Previous package queued:** the version-agreement checker (OQ-24), by Max's post-push call. **This conversation did:** built it, acceptance-tested it against the Scan #2 drift specimens, canonized it (C-060, Protocol v0.18), cured its first live catch, and advanced the queue to S2-5.1.

## 2. Acts & decisions of record (Protocol v0.18, Ratified)

- **C-060 — the version-agreement checker canonized (executed).** `check_versions.py` = the third canonized store tool (C-050 family, C-006 code-artifact exception); **the C-059 close ritual runs both checkers — red from either blocks.** Checks: self-agreement (series stamps vs filenames), claim agreement (every attributable `<Document> vX.Y` claim vs the named document's internal stamp; phantom versions error everywhere, frozen sources included), path existence. Severity: objective disagreements error, currency heuristics warn. Source classes: frozen / strict / tolerant.
- **Max's spec calls (pre-build):** errors block, heuristics warn · frozen docs exempt from currency, never existence · scope = Claude-era corpus + root · standalone sibling of `verify.py`. **Calibration ratified (in-build):** Rule Overview + Settings tolerant; Agenda Board HTML in scope; 2-entry SUPPRESS list (Schema v0.5 preamble narrative).
- **Acceptance:** all nine catchable Scan #2 §1 specimens re-detected on seeded drift; phantom version caught in a frozen source; self-agreement break caught. Live: PASS on the real repo, `verify.py` simultaneously green.
- **First live catch, cured:** the Local Context's own C-059 checklist row sat at "changed → v0.20" while the doc was v0.21 (the post-push amendment updated prose, not the row). The close's ripple discipline also fired live: issuing Protocol v0.18 obliged the Index's PROT row and four Sources lines forward — the checker refused to pass until they moved.
- **OQ-24 → Resolved** · **S2-5.2 → Fixed** (Register v0.16 ledgers both).

## 3. Change summary (one `[GOV]` commit, Claude-authored per C-037; push = Max)

`check_versions.py` new (C-060) · Protocol **v0.18** issued + DOC-minted · Register → **v0.16** · Rule Overview → **v0.14** · BOOTSTRAP → **v0.5** · Architecture State → **v0.3** · Context Index → **v0.11** · store README updated · Local Context → **v0.22** · Agenda Board republished (stamp → v0.22) · store: +9 events (DOC mint ×4 events + 5 revises) → **50 nodes / 208 events**, `verify.py` PASS + `check_versions.py` PASS.

## 4. Refresh list

The full C-059 checklist was walked — see Local Context v0.22 §Standing refresh items for every row's mark. Project mirrors refreshed: Register, Rule Overview, Local Context (Global + Index mirrors: Global unchanged; Index refreshed with v0.11). Cowork board artifact republished from the file.

## 5. Unresolved / carried

- **Open findings (review ledger):** S2-5.1 (spec-version identity — queued next) · S2-6.1 (pre-canon labeling, rides with OQ-10) · S2-6.2 / S2-6.3 (Max's manual hygiene).
- **Standing OQs:** OQ-4, OQ-6, OQ-9, OQ-10, OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27.
- **Pending on Max:** review the commit and `git push`; empty `_to_delete/`; the three `~$*.docx` owner-files at the root (optional).
- **Checker calibration note (standing):** quoting a version-claim pattern verbatim in prose will trip the checker — that is inherent to a text-matching tool; write illustrative mentions behind an "e.g." (the example guard) or without the marker word. The SUPPRESS list is the escape hatch of last resort and stays Max-ratified.

## 6. Next

**Queued next (Max's standing sequence): S2-5.1 — spec-version identity in the store** (living-DOC vs per-version DOCs; Scan #2 §5 lays out both arms), with the **pre-canon labeling call (S2-6.1/OQ-10)** riding along. **Scan #3 penciled** after the build track — or earlier if the checker and the C-059 checklist start disagreeing. Open with Global + Local Context v0.22 + this package (add Register v0.16 and Scan #2 §5).

---

**Postscript (2026-08-14, same day, post-push).** Max pushed — `main` == `origin/main` at `421dc89`; the C-059 loop is closed. One board-only amendment on Max's ask: a **provenance legend** ("where the numbers root": C-# / OQ-# / S*n*-x.y → their defining documents and ledgers) added to the Agenda Board and republished. Display-only on a derived projection — no decision made, no rule changed, so **no protocol** (recorded reason per C-059); store untouched, no verify duty; Local Context unchanged (the legend is board furniture, not agenda content).
