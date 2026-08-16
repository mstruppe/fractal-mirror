# Fractal Governance Protocol — Claude Series v0.19

**Topic:** Spec-version identity in the store (scan S2-5.1 → C-061): the versioned-artifact class gets **one DOC identity per version file**, exactly as the protocol series has — nine retro mints (Schema v0.1–v0.5, Template v0.1–v0.4), the two existing living DOC ids kept as **series pointers** (append-only, Max's call); "Schema v0.4" is a citable identity again. Rider executed: the pre-canon label line in `BOOTSTRAP.md` §0 (S2-6.1 → C-062); the ChatGPT-era archive-move question stays OQ-10.
**Status:** Ratified (2026-08-14 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-14 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.18

---

## 1. Context

The C-059 auditable handover: *the previous package queued S2-5.1 (spec-version identity), with the pre-canon labeling call riding along; this conversation decided both and executed the close.* Scan #2 §5 had laid out the finding: governance (C-040) declares the canonical specifications **versioned artifacts** — five Schema files and four Template files sit on disk — while the store held each spec as **one living DOC** whose hash tracks whatever is current; the Protocols, equally sequential, get one DOC per version. Three document classes, two store treatments, and a superseded spec version ("Schema v0.4") that existed on disk but had no identity in the store.

Two developments since the scan softened the citation pain without resolving the class question: v0.17 made normative-home pointers version-agnostic, and the version-agreement checker (C-060) validates historical version-claims against the files on disk, frozen sources included. What remained was the identity question itself — and it was picked deliberately, as the scan asked.

## 2. Questions investigated

1. One store rule or two treatments? *(→ C-061: DOC identity mirrors file identity — one file, one DOC.)*
2. What becomes of the two existing living DOC ids once per-version DOCs exist? *(→ kept as series identities — append-only, no alias re-binding; Max's call.)*
3. The rider: how is the pre-canon material at the repo root labeled? *(→ C-062: one line in BOOTSTRAP §0; the folder move stays with OQ-10.)*

## 3. Decisions of record

- **C-061 — Spec-version identity: per-version DOCs (executed).** One rule replaces two treatments: **DOC identity mirrors file identity.** Living documents (one stable file, C-012) hold one living DOC node revised in place; versioned artifacts (one file per version, C-040) hold **one DOC node per version file**, exactly as the protocol series has — the specs were the anomaly, not the rule. **Executed: nine retro mints** — Schema v0.1–v0.5 and Template v0.1–v0.4 — each freezing its file's committed bytes in its own `content_hash` and binding a version-labeled **`route` alias** (`Fractal_Node_and_Event_Schema_v0.1` … ; `Fractal_Node_Template_v0.1` …). No cross-version edges: the succession is carried by the filenames and the series pointer, as in the protocol series. The two existing living DOC ids are **kept as series identities** (append-only; the versionless `Fractal_<Name>` alias stays bound to them; their hash and path keep tracking the newest issue via `revise`; body prose re-scoped — document bytes unchanged, so no revise events for the re-scope itself: the class ruling lives in this protocol, not in a hash change). **A spec reissue is now two store writes:** one `revise` on the series node + one per-version mint (the C-059 Schema→Template coupling unchanged). Foundation v0.1 already conforms (single version, one DOC). A superseded spec version is again a citable identity in-store. The Schema documents this store treatment at its next reissue (no reissue forced now — the spec's own text is unchanged by this decision). Fixes **S2-5.1**. *(Working Decision.)*
- **C-062 — Pre-canon label at first contact (executed).** `BOOTSTRAP.md` §0 gains one line naming `Vision thought scramble.docx` as **pre-canon** — biographical vision material that *informs, never governs* (the OQ-22 ruling, now visible on disk where a first-contact reader meets the file). No `Fractal_` identity, no DOC mint, no move — deliberately: the wider ChatGPT-era archive-move question remains **OQ-10** (Max's go/no-go), and this line is the cheap, honest interim whatever that call becomes. Fixes **S2-6.1**. *(Working Decision.)*

## 4. Alternatives recorded (the arms not taken)

- **(a) Specs as living documents** — declare C-040's version bump a file-naming convention and drop version pins from cross-references. Rejected: it declares the disk/store mismatch instead of curing it, permanently splits the specs from the protocols' treatment, and makes "Schema v0.4" unciteable forever.
- **(c) Mint-on-cite hybrid** — extend C-042's mint-on-reuse to superseded spec versions. Rejected: cheapest, precedented, but leaves the class ambiguity standing and the two treatments diverging; the whole point of the pick was one deliberate rule.
- **Alias-rebind variant of (b)** — versionless alias re-pointed to the newest version node at each reissue. Rejected for the series-pointer form: re-binding works against the C-045 grain and costs an alias event per reissue for nothing the series node doesn't already give.

## 5. Executed this close (one `[GOV]` commit, C-037; push = Max)

- **Store** — nine retro mints (create + route alias + `topic:KG` + `agent` placements each); this protocol DOC-minted (C-041); two series node bodies re-scoped (no events — bytes-unchanged rule above); five revise events re-freeze the edited canonicals (Register, Rule Overview, BOOTSTRAP, Architecture State, Context Index); **60 nodes / 253 events**; both checkers green before commit.
- **BOOTSTRAP → v0.6** — §0 pre-canon line (C-062).
- **Decision Register → v0.17** — C-061/C-062 entered; S2-5.1 and S2-6.1 → Fixed; OQ-10 annotated (labeling half done); Sources.
- **Rule Overview → v0.15** — document-identity row extended (per-version DOCs, series pointers); ledger caveat → v0.17.
- **Context Index → v0.12** — Schema/Template rows note per-version identities; naming-convention section extended; PROT row → v0.1–v0.19; Sources.
- **Architecture State → v0.4** — §2 document-identity clause (C-061).
- **Local Context → v0.23** — decision recorded; checklist walked; queue empties (G/H stand; Scan #3 penciled).
- **Agenda Board** — republished file-first (stamp → Local Context v0.23).
- **Return Package** — `Return_Package_2026-08-14_Spec-Version-Identity.md`.

## 6. Calls recorded (Max, 2026-08-14, this conversation)

1. **The arm:** (b) per-version DOCs — "one rule everywhere: DOC identity mirrors file identity" — over living-docs (a) and mint-on-cite (c), both presented with costs.
2. **Series ids:** kept as series nodes — versionless alias stays, hash tracks newest via revise; no re-binding, no history disruption.
3. **The rider:** the BOOTSTRAP §0 line (the scan's cheap fix); the folder move deliberately left with OQ-10.
4. **Execution:** full close in one pass ("Yes — full execution").

## 7. Ratification record (2026-08-14, in-conversation per C-033)

Max opened the conversation on the queued item, chose the arm, the series-id treatment and the rider's form by explicit selection from presented alternatives, and authorized the full close — Claude edits and commits as the attributed author per C-037; Max reviews and pushes. Ratified in the conversation it records; no caveats.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None opened. **S2-5.1 → Fixed** (C-061) · **S2-6.1 → Fixed** (C-062; archive move stays OQ-10).
- Standing items carry: OQ-4, OQ-6, OQ-9, OQ-10, OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27. Open review findings: S2-6.2, S2-6.3 (Max's manual hygiene). **Scan #3 stays penciled** after the build track — earlier if the checker and the C-059 checklist disagree.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.19 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.19 |
| Status | Ratified (2026-08-14, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-14, this conversation) |
| Date | 2026-08-14 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.18 |
| Related Documents | Review_2026-08-14_LooseEnds-Scan-2.md §5 (S2-5.1, the finding); Decision Register v0.17; Rule Overview v0.15; Local Context v0.23; Architecture State v0.4; Context Index v0.12; BOOTSTRAP.md v0.6; Return_Package_2026-08-14_Spec-Version-Identity.md |
| Document ID | DOC-01M001VQZ885R5SDPG4CT4VVZP (minted 2026-08-14, C-041, per this protocol) |
