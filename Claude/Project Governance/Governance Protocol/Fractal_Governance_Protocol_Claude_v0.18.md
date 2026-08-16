# Fractal Governance Protocol — Claude Series v0.18

**Topic:** The version-agreement checker built and canonized (OQ-24 → C-060): `check_versions.py` joins the store tools as the third canonized tool; the C-059 close ritual now runs **both** checkers — `verify.py` for the store's internal consistency, `check_versions.py` for the corpus's prose truth; severity split (objective disagreements block, currency heuristics warn), source classes (frozen / strict / tolerant), and the SUPPRESS discipline ratified; acceptance suite green (all nine catchable Scan #2 §1 specimens re-detected on seeded drift); first live catch cured in the same close.
**Status:** Ratified (2026-08-14 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-14 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.17

---

## 1. Context

The previous package's postscript queued this conversation explicitly (the C-059 auditable handover: *previous package queued the version-agreement checker; this conversation built it*). OQ-24 entered the ledger one close earlier as the elevated first build-track item, spec'd by Scan #2's S2-5.2: `verify.py` proves internal consistency to the unit while nothing checks external truth — extract every `<Document> vX.Y` claim in the corpus, resolve each against the named document's own internal stamp, report disagreements, plus a path-existence pass. Scan #2's §1 (eleven false present-tense claims in three conversations) is the drift class the tool exists to retire, and served as its acceptance bar: catch every §1 finding except S2-1.5's dead path (the path pass catches that) and S2-1.1 (a governance question, not a string).

Max settled the four open spec points before the build (§6), the tool was developed against a full mirror of the corpus, calibrated on the live corpus, verified against a seeded-drift acceptance suite, and then run on the real repository — green, with exactly one warning, which was a true catch (§4).

## 2. Questions investigated

1. How is the C-059 checklist's hardest column — "is every projection's claim still true?" — mechanized without drowning in the corpus's legitimate historical citations? *(→ the source classes and the historical-marker heuristic, C-060.)*
2. What counts as a *claim*? *(An attributable `<alias> vX.Y` token; an alias registry is the semantic core, data-driven in-script.)*
3. How are frozen artifacts exempted from currency without blinding existence checks? *(Max's call: exempt from currency, never from existence — a phantom version errors even in a frozen Return Package.)*
4. Where does the tool live and how does the ritual invoke it? *(Sibling of `verify.py`; the close runs both; either red blocks.)*

## 3. Decisions of record

- **C-060 — The version-agreement checker is canonized (executed).** `check_versions.py` joins `verify.py`/`mint.py` as the **third canonized store tool** (C-050 family; code artifact under the C-006 exception, not DOC-minted), repo-resident at `/Claude/Knowledge Graph Store/`. Stdlib-only, read-only. **The C-059 close ritual runs both checkers; red from either blocks the close** (the C-050 discipline extended from the store to the corpus). Checks: **(A) self-agreement** — every versioned-series file's internal stamp matches its filename; every living document has a readable stamp; **(B) claim agreement** — every attributable `<Document> vX.Y` claim resolves against the named document's internal stamp (living docs) or version file (series docs); a version that exists nowhere is an error in every source, frozen included; **(C) path existence** — repo-rooted paths and named files must exist. **Severity split (Max's call):** objective disagreements are errors and block; judgment-dependent signals (stale series citations without a historical marker, unresolvable relative paths, checklist-row lag) are warnings. **Source classes (Max's calls):** *frozen* (Return Packages, canonical Reviews per C-058, superseded series files, store node bodies) — exempt from currency, never from existence; *strict* (the pointer surfaces: Context Index, BOOTSTRAP, Architecture State, Global + Local Context, Agenda Board, store README, the tools themselves) — full currency; *tolerant* (the living ledgers: Decision Register, Rule Overview, Conversation Settings, and each series' newest file) — existence everywhere, currency on their `Sources:` and `Normative home:` lines. The alias registry, class assignments and guards live as data at the top of the script; the **SUPPRESS list** (claims the checker deliberately looks away from as known-historical narrative) stays short and every entry is Max-ratified — two entries ratified today, both in Schema v0.5's preamble. Resolves **OQ-24**; fixes **S2-5.2**.

## 4. Build & acceptance record

Developed against a full corpus mirror; calibrated in three passes (the first run produced 51 errors and 66 warnings, nearly all attribution artifacts — the calibration story is itself evidence for Scan #2's thesis that the corpus's historical citations vastly outnumber its currency claims). **Acceptance suite:** the Scan #2 §1 specimens were re-seeded into a mutated copy — all nine catchable findings re-detected (stale-schema claims → WARN; living-stamp mismatches, including BOOTSTRAP's re-seeded "internal v0.3", → ERR; the Index's short series range → WARN; the Template's dead `_events/` path → WARN) — plus two classes beyond the original spec: a **phantom version** — a seeded citation of a protocol release that does not exist — caught inside a frozen Return Package, and a **self-agreement break** (a series file whose internal stamp disagrees with its filename). **Live run on the real repository:** PASS — 106 files scanned, ~900 version claims attributed, 83 path references checked, `verify.py` simultaneously green (49 nodes / 199 events). **One warning, a true catch:** the Local Context's own C-059 checklist row still marked "changed → v0.20" while the document stood at v0.21 — the post-push agenda amendment had updated the prose but not the table row. Cured this close (§5). The checker's ripple discipline also showed immediately: issuing this very protocol obliged the Context Index's PROT row and three Sources lines forward to v0.18 — exactly the class of update the old refresh habit used to miss.

## 5. Executed this close (one `[GOV]` commit, C-037; push = Max)

- **`check_versions.py`** — new, third canonized tool (C-060).
- **Store README** — tool roster + the corpus-side ritual section.
- **BOOTSTRAP → v0.5** — §4: the version-agreement pass standing (no longer "future drills add", OQ-24 resolved); knowledge layer line gains the checker.
- **Architecture State → v0.3** — §2 tooling bullet: three repo-resident tools; both rituals named.
- **Context Index → v0.11** — PROT row → v0.1–v0.18; store row tool roster; Sources.
- **Decision Register → v0.16** — C-060 entered; OQ-24 → Resolved; S2-5.2 → Fixed; Sources.
- **Rule Overview → v0.14** — version-agreement row (§2); integrity remainder updated (whole-repo verification mechanized); ledger caveat → v0.16.
- **Local Context → v0.22** — checker build recorded; the stale checklist row cured; this close's checklist walked; S2-5.1 queued next.
- **Agenda Board** — republished file-first (stamp → Local Context v0.22).
- **Store** — this protocol DOC-minted (C-041); five revise events re-freeze the edited canonicals (Register, Rule Overview, BOOTSTRAP, Architecture State, Context Index); **50 nodes / 208 events**; both checkers green before commit.

## 6. Calls recorded (Max, 2026-08-14, pre-build spec + in-build calibration)

1. **Severity:** errors block like `verify.py` red; heuristics warn (mirrors the C-050 contract).
2. **Frozen documents:** exempt from currency, not from existence — "their version claims were true when written."
3. **Scope:** the Claude-era corpus + repo root (all `.md` under `/Claude/`, `BOOTSTRAP.md`, the tools' own headers); Foundation with ChatGPT excluded (pointer-only, C-029). Calibration extension ratified: the Agenda Board **HTML is in scope** — its C-035-style stamp ("Projection of Local Context vX.Y") is a checkable currency claim.
4. **Wiring:** standalone sibling of `verify.py`; the ritual runs both; tools stay single-purpose.
5. **Calibration ratifications:** Rule Overview and Conversation Settings run *tolerant* (their bodies narrate history; their Sources/Normative-home lines stay strict); the 2-entry SUPPRESS list stands as documented in-script.
6. **The cured warn:** the Local Context checklist row lag (v0.20 vs v0.21) is drift, not convention — cured, and the row class stays checked (as a warning) every close.

## 7. Ratification record (2026-08-14, in-conversation per C-033)

Max queued the item post-push (Local Context v0.21 / RP postscript), opened the conversation on it, settled the four spec points by explicit selection, ratified the three calibration calls and the cure of the live catch, and accepted the full close ("Yes, full close") — Claude edits and commits as the attributed author per C-037; Max reviews and pushes. Ratified in the conversation it records; no caveats.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- **OQ-24 — Resolved** (C-060): shipped as `check_versions.py`; cadence = every close, riding the C-059 checklist; future restore drills include the pass (BOOTSTRAP §4).
- **Scan #3 trigger sharpened (carried from v0.17's close):** penciled after the build track lands — **or earlier if the checker and the C-059 checklist start disagreeing**; that disagreement is the signal for human-grade adversarial eyes.
- Standing items carry: OQ-4, OQ-6, OQ-9, OQ-10 (adjacent to S2-6.1), OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27. Open review findings: S2-5.1 (queued next — the spec-version identity discussion), S2-6.1, S2-6.2, S2-6.3 — see the Register's review-findings ledger.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.18 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.18 |
| Status | Ratified (2026-08-14, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-14, this conversation) |
| Date | 2026-08-14 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.17 |
| Related Documents | check_versions.py (C-060, canonized tool); Review_2026-08-14_LooseEnds-Scan-2.md (S2-5.2, the spec's source); Decision Register v0.16; Rule Overview v0.14; Local Context v0.22; Architecture State v0.3; Context Index v0.11; BOOTSTRAP.md v0.5; Return_Package_2026-08-14_LooseEnds-Scan-2.md (the queueing handover) |
| Document ID | DOC-01KZZVMZM0YCN87J7F6B49J2S7 (minted 2026-08-14, C-041, per this protocol) |
