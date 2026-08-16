# Fractal Governance Protocol — Claude Series v0.23

**Topic:** Project-spine mirrors retired (C-067): the mirror *mechanism* of C-002/C-030/C-036 ends — every client reads the context package from the repo; context-package membership now means *routed in the Index + read in-repo*. OQ-6 resolved (mooted). Motivated by this session's live specimen of the S2-3.1 deterioration class: the mirror row was the C-059 checklist's last un-mechanizable duty, and it went stale and mismarked the very session the operating surface changed.
**Status:** Ratified (2026-08-14 — ratified in the conversation it records, per C-033) · **Date:** 2026-08-14 · **Parent Protocol:** Fractal Governance Protocol — Claude Series v0.22

---

## 1. Context

Same conversation as v0.20–v0.22. Max asked whether the drill's close had run the full loop, recalling Scan #2's finding that loop closings had deteriorated to context-package-only updates (S2-3.1, High — cured by the C-059 checklist, mechanized by C-060). The audit found the ritual held *except one row*: **Project mirrors**. The vendor-held copies in the Cowork Project spine cannot be scanned by `check_versions.py` and cannot be refreshed from the Code surface; they went several versions stale during this session's ledger churn, and the checklist row was mismarked "refreshed" (the marks were made against the repo canonicals, not the vendor copies). Exactly the scan's mechanism: **what the checker can't verify deteriorates first.** Max weighed refresh-on-next-open against retirement, asked for confirmation of the recommendation, and called: **retire it.**

## 2. Questions investigated

1. What did the mirrors still buy? *(→ Availability fallback only — context readable if the repo connection failed. Better carried by the off-site copy (C-056) and the drill-proven rehydrate (C-038); a vendor snapshot is the weakest of the three and the only one that silently rots.)*
2. Does retirement change context-package membership? *(→ No — C-030/C-036 membership stands; the mechanism changes from copy-into-Project to read-in-repo. The Cowork instructions-field adapter is untouched (C-035; adapter-stamps row).)*
3. What happens to OQ-6 (mirror Return Packages?)? *(→ Mooted — nothing is mirrored anymore.)*

## 3. Decision of record

- **C-067 — Project-spine mirrors retired (OQ-6 resolved — mooted).** No living projection is copied into a vendor Project spine; every client reads the context package **from the repo** — the Code surface natively, Cowork via its file access, `/fractal` automating the reads. Context-package **membership** (C-030/C-036) is unchanged and now means *routed in the Index + read in-repo*. The C-059 checklist's mirror row is **retired** (this session's mismark corrected in the Local Context); the checklist is now **fully walk-or-machine-verifiable** — no row rests on a duty the default surface can neither execute nor check. The instructions-field adapters remain the only vendor-held artifacts, walked in the adapter-stamps row. **Pending on Max:** delete the stale mirrors from the Cowork Project at next open (they are misleading snapshots, several versions behind). *(Working Decision.)*

## 4. Executed this close (one `[GOV]` commit, C-037; push = Claude, C-064)

- **Decision Register → v0.21** — C-067 entered; OQ-6 → Resolved; header's mirror clause reworded; Sources and revision history.
- **Rule Overview → v0.19** — anchoring row reworded (read-in-repo; C-067 joins its sources); header clause; ledger caveat → Register v0.21.
- **Context Index → v0.16** — the three "this Project +" entry-point cells → repo paths (read in-repo, C-067).
- **BOOTSTRAP → v0.11** — §2.1 step 3 rewritten (read-in-repo, mirror step retired with its rationale); §2.4 mirror mention dropped.
- **Local Context → v0.32** — mirror row retired with the mismark correction on the record; postscript 6.
- **Store** — this protocol DOC-minted; four `revise` events (Register, Rule Overview, Index, BOOTSTRAP); **67 nodes / 300 events**; both checkers green before commit.
- **Agenda Board** — republished (stamp → v0.32) · **Return Package** — postscript 6.

## 5. Calls recorded (Max, 2026-08-14, this conversation)

1. **The finding:** surfaced by Max's own audit question ("did we do a full loop close after the drill?") and his recall of the Scan #2 deterioration — the row that rotted was the un-mechanizable one.
2. **The disposition:** retire (over refresh-on-next-open), after asking for and receiving the recommendation with its counterpoint stated.

## 6. Ratification record (2026-08-14, in-conversation per C-033)

Max asked the audit question, connected it to S2-3.1 himself, requested confirmation of the recommended move, and called "retire it" / "go ahead." Claude executed the sweep, committed as attributed author (C-037), pushed per C-064. Ratified in the conversation it records; no caveats.

## 11. Open Questions (TBD)

*(Per C-034 these are entered in the Register's cumulative ledger.)*

- None opened. **OQ-6 → Resolved** (mooted by C-067). Standing items carry: OQ-4, OQ-9, OQ-13, OQ-16, OQ-17, OQ-18, OQ-20, OQ-23, OQ-25, OQ-26, OQ-27. The review ledger stays fully green.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.23 |
| Document Type | Governance Protocol (historical artifact, dated identity — C-012) |
| Version | v0.23 |
| Status | Ratified (2026-08-14, in-conversation per C-033) |
| Domain | GOV |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-14, this conversation) |
| Date | 2026-08-14 |
| Parent Protocol | Fractal Governance Protocol — Claude Series v0.22 |
| Related Documents | Decision Register v0.21; Rule Overview v0.19; Context Index v0.16; BOOTSTRAP.md v0.11; Local Context v0.32; Review_2026-08-14_LooseEnds-Scan-2.md §3 (S2-3.1, the deterioration class); Return_Package_2026-08-14_First-Code-Session.md (postscript 6) |
| Document ID | DOC-01M00EE786TWWEJ0ZJ29MVH3QX (minted 2026-08-14, C-041, per this protocol) |
