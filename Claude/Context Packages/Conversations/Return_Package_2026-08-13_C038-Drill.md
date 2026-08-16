# Return Package — 2026-08-13 — The C-038 Drill (Shipping & System Integrity)

> **DERIVED PROJECTION — conversation hand-off record.** Historical artifact, dated filename (C-012). Domain: GOV (substrate). Author: Claude. Sources: this conversation (2026-08-13); Decision Register v0.14; BOOTSTRAP.md v0.3; the live drill outputs (cloud-session clone).

---

## 1. What this conversation was

Max took up the queued item — **architecture integrity & safety** (C-031 foreknowledge) — through the shipping lens: *"when we ship FRACTAL I need to understand what and how we ship it."* The map answered from settled canon: **the repository is the shipping unit at every scale** (C-020) — three concentric rings (the **seed**: private remote, C-056 · the **tooling wrapper**: skill → plugin, roadmap H · the **network horizon**: fork/PR, pre-canon), one unit, different recipients and guarantees per ring. Integrity as currently built: `verify.py` (store content) · git + off-site (history) · the C-057 ladder (custody) · the C-038 acceptance test (rehydration — the proof of shippability, then still never exercised). The item's first call — **postpone or act now** — went to **act now**: prove the shipment.

## 2. Acts executed (no new C-decisions — both acts execute ratified ones)

- **C-056 completed at Max's terminal:** private repo `mstruppe/fractal` created; first push done; `origin` bound **over SSH** after the HTTPS-credential dead end (no `gh`, no brew, no stored credential) — an SSH key was minted and registered as the durable push credential (no expiring write tokens; C-057 layer 2/3 hygiene). The remote-URL swap incidentally exercised the C-018 one-line migration property. **Every commit now ends with a push.**
- **C-038 acceptance test exercised — green:** cloud-session clone via a C-057-conformant fine-grained token (single-repo, Contents read-only, expiring — **revoked after the drill**) → BOOTSTRAP §1 rehydrate → `verify.py`. Results: 26 commits unbroken to the 2026-08-12 baseline; clone HEAD = source HEAD; both C-037 author identities in the log; **all nine §1 paths resolved**; `verify.py` **PASS, 0 warnings**; byte-parity 46 nodes / 176 events on both ends. *"Laptop in the ocean" is demonstrated fact.*

## 3. Worth remembering (method notes)

- **A claim is not a capability.** "We can ship" was doctrine for a day and fact only after the drill. The gap between *armed* and *exercised* cost one afternoon to close and would have cost everything to discover in a real recovery.
- **The drill audited more than the store:** it exercised the token profile (C-057), the §1 path map (BOOTSTRAP as a real document, not a hope), the network property (a non-Max machine received FRACTAL), and the projections — and it was the projections that flinched: the Local Context's headline said **174** events; the log held **176**. First live specimen of projection drift — the store is machine-verified, projections are checked by nobody. Carried into the integrity remainder as its first observed datum, not patched away silently.
- **Friction is data:** the push failed first because no credential path existed on a clean Mac — exactly the kind of fact a shipping story must include. The durable fix (SSH keys) is also the infrastructure the C-057 signing trigger will want later.

## 4. Changes to the canonical layer (the repo)

| Artifact | Change |
|---|---|
| BOOTSTRAP.md | v0.2 → **v0.3** — status: acceptance test **exercised green**; §4 carries the drill record; restore-drill cadence flagged open. |
| Decision Register | v0.13 → **v0.14** — C-038 and C-056 caveats **discharged**; drill + drift finding recorded; no new decision numbered. |
| Rule Overview | v0.11 → **v0.12** — §5 armed-caveat retired; integrity & safety remainder recorded as a standing offer. |
| KG Store | **+3 revise events (179 total, 46 nodes):** BOOTSTRAP, Register, Rule Overview revisions hashed into the log. `verify.py` green. |
| Local Context (KG) | v0.18 → **v0.19** — queued item consumed (act-now call recorded); **174→176 headline drift corrected**; integrity remainder as G offer. |
| Agenda Board | Regenerated file-first (C-048), stamp v0.19; artifact republished. |

Commit (C-037, author Claude): one coherent change-set `[GOV]`; `verify.py` green before the commit (C-050 duty); the push rides it (C-056 — its first ordinary ride).

## 5. Refresh list (project mirrors, per C-004)

Refreshed this conversation: `Fractal_Decision_Register.md`, `Fractal_Rule_Overview.md`, `Fractal_Local_Context_Knowledge_Graph.md`.

## 6. Unresolved / carried

- **Integrity & safety — remainder (G offer):** whole-repo verification / projection-drift checking (datum: 174/176) · restore-drill cadence (the drill is repeatable at will; no cadence chosen) · C-057 ladder vs. the network horizon · OQ-20 heavier-review fold-in · safety once other writers exist.
- Carried: OQ-4 (reaffirmed), OQ-9, OQ-16, OQ-18, OQ-20; signing trigger = first second writer (C-057).
- **WS remains the declared open part** — forge on observed need (Architecture State §4).

## 7. Next

**Nothing is force-queued.** Next conversation follows Max: **G** (OQ-4 · the integrity remainder) or **H** (the build track — the repo-resident skill is the natural shipping-tier next step, now wrapping a *proven* seed). Open with Global + Local Context v0.19 + this package.
