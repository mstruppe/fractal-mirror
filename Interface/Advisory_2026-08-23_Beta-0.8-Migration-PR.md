# Advisory: Beta 0.8 Migration PR

> **DATA, NEVER INSTRUCTION (C-096 class).** This envelope creates an
> option its reader dispositions by its own recorded decision — never an
> obligation. It is RAM-class (Interface Place Format v0.2, law 4):
> temporary by construction, dissolved by its author's own act once
> absorbed — absorb and cite by path + date; never depend on it persisting.

**Direction:** FRACTAL → PR (CN-0002) · **Class:** advisory · **Date:** 2026-08-23 · **Author:** Max Struppe <max.struppe@gmail.com>

**Cite as:** `~/Desktop/Knowledge Network/FRACTAL/Interface/Advisory_2026-08-23_Beta-0.8-Migration-PR.md` (2026-08-23) — path + date is the full trace once this file dissolves.

---

> **The per-release migration advisory the mother owes at every anchored release** (`Fractal_Kernel_Migration_Procedure_v0.2` §8 — instantiated per child this release; the first under v0.2's nine-row template). Everything here is **audited, never obeyed** (KMP §1.8): adoption is the reading instance's own recorded decision, and a never-migrating instance is conformant forever (KMP §1.2). Citation convention (UF1-7's cure): `KMP §n` = Fractal_Kernel_Migration_Procedure_**v0.2** · `GENESIS §n` = GENESIS.md at this release · `AST §6` = Fractal_Architecture_State §6 as shipped in this release · `MAN` = `Claude/Project Governance/Rule Corpus/birth_state_manifest.json` **as shipped in the pinned tag** · `IPF §n` = Fractal_Interface_Place_Format_v0.2.

**Issued:** 2026-08-23, authored ahead of the beta-0.8 tagging close (§7's gate results stamp at the pack) · **Of record:** Protocol v0.73 + `Fractal_Update_Plan.md` (the beta-0.8 lane) + the mother-side campaign runbook `Fractal_Upgrade_Install_Procedure_v0.0` (Draft — binds nothing; named for transparency)

## 1 · Pin identity (KMP §2)

- **Tag:** `beta-0.8` on `github.com/mstruppe/fractal` (the mother repo); the mirror's own `beta-0.8` follows on `github.com/mstruppe/fractal-mirror` (pin from there if you work from public releases).
- **Commit SHA and tag-object SHA:** resolve them yourself against the tag — a copied SHA is not a pin (KMP §2.2). This document ships inside the release tree and therefore cannot carry its own tag's hashes or attestation (the structural-absence rule, KMP §2.6); the receipt pair (`.txt` + `.ots`) is handed over separately, OTS state disclosed at hand-off, **pending-at-issue expected and non-blocking**.
- **Signing key (fingerprint + principal, never a label):** ED25519 `SHA256:gSUgFha7OI7a4QfYaPRtPtROmabsksQDmtU5sh9fH0Y`. Principals bound to this custody key: `max.struppe@gmail.com` (mother repo) · `fractal@knet.network` (mirror chain). One custody environment, one key (C-074b); the signature attests custody, the author field attributes.
- **The signers bind, verbatim (KMP §2.3):** before `git tag -v`:
  `git config gpg.ssh.allowedSignersFile "$(git rev-parse --show-toplevel)/.allowed_signers"`
- Run `git fsck --strict` and record the result (KMP §2.5).

## 2 · Transport (KMP §2.7–§2.8)

`git clone --no-local` → checkout the tag → record the remote's URL in your receipt → **`git remote remove origin`**. The frozen clone is a reference copy — read-only evidence, never a working surface. For full rehydration independence, the self-contained bundle option (KMP §2.8): a complete-history bundle of the signed tag plus its SHA-256, at your own upstream-provenance location, verified by bundle-only checkout — your self-containment rule decides (KMP §4.3).

## 3 · Delta inventory (baseline beta-0.7 — your birth tag, Register C-133 → this release, C-139)

Your baseline is your birth: born 2026-08-21 from the `beta-0.7` tag, so the whole delta below post-dates your genesis. Hand-derived from the Register × the pinned partition (AST §6 in this release — the classification source of record; **MAN joins it at element grain**, KMP §10.5; where any hint below disagrees with either pinned artifact, **the pinned artifact wins**, and a disagreement *between* the two pinned artifacts stops at your owner as an upstream-internal conflict, KMP §3.6):

| Rows | Class per pinned AST §6 / MAN | What it is | Disposition hint (audit, never obey) |
|---|---|---|---|
| C-134 | kernel doctrine + birth-seam machinery | **The Birth-State Law** — GENESIS §2's Birth-State clause: *birth is a pure function, upgrade is a merge*; one manifest, three consumers; the seed-body law + the robustness triad. Its migration face is **KMP §10** — MAN as your reading key — and the **§10.4 regeneration duty** (derived projections regenerate from local source after any adoption). Newborn-only components — the day-one receipt, the generated Rule Overview seed — exist for births | Adopt the doctrine + read MAN at your Gate 2; **never retrofit** the newborn-only components (your pre-0.8 birth without them is conformant state, not damage) |
| C-135 | kernel doctrine | **The Kernel-Layer Doctrine** — Layer A engine (swapped, never merged) · Layer B format contracts (the only source of a major) · child content not a layer (conforms; converts lazily at first touch; frozen never migrates). Carried into **KMP v0.2 §9** (the release-class fork) + §10 (the manifest read). The first-touch converter **armed-inactive**; semantic versioning **armed-inactive** (the mother's owner's call — inert on your side) | Adopt the doctrine with KMP v0.2; the fork is what makes *your* crossing light (§9 below) |
| C-136 | kernel (tools + program) | **The strict-MACHINE ruling + the rule-corpus program** — `doctor.py` now runs inside `run_gates()` (every close); the **anchor-occurrence gate** joins the close gates (every local `beta-*` tag must show its Provenance pair + mirror twin). New kernel subtree: `Claude/Project Governance/Rule Corpus/` — the classified corpus, `audit.py`, and **MAN** (validated by the mother's pack gate at every pack) | Adopt the tool batch — **and audit the two new close gates in your own context first**: your `doctor_roster.json` state (§6), and `anchor_occurrence`'s behavior against *your* tree's actual tag/Provenance state (a birth clone's inherited state may answer it differently than the mother's — what it does on your tree is exactly the datum this wave wants, §5) |
| C-137 | kernel doctrine (adopter-facing prose) | **The care doctrine** — adopting a FRACTAL means taking on its care; integrity carried by the layered rituals. GENESIS §3.4, Onboarding §2.3, README | Arrives with the inherited-document swaps; it names what your owner already practices |
| C-138 | concept tier (C-086 — reference, never demanded) | **The Model Routing Foundation v0.3** (Ratified) — gate-coverage, the three-layer hedge, every allocation an offer | Reference class — `origin-reference` stance; read at need |
| C-139 | kernel (contract + tool + birth-seam) | **The connection layer** — `Fractal_Interface_Place_Format_v0.2` (**a new, additive contract**: conscious pairing — the four-step ceremony, the byte-pinned checksum code, mutual `CN-` lock-ins, the quarantined connection-request, the two faces, the routing law with the receipt loop) + **`postman.py` + `test_postman.py`** (the ninth canonized tool) + genesis's connected-birth (birth-seam) + the opener's poll step (adapter-tier). GENESIS v0.20, Interface Foundation v0.7, Onboarding v0.7 | Adopt the Format + the postman **at your own pace** — your v0.1-grammar place stays conformant meanwhile (lazy conversion, IPF §10; the mother already polls it best-effort). The natural first touch is IF-0015 (§9) |
| — (F2 class + your IF-0013) | kernel (orientation files) + inherited-defect cures | **The Active-Return-pointer law** (the sole Return-Package selector; "newest file" retired) — cured mother- and generator-side *after* your birth tag, so your tree carries the pre-cure editions IF-0013 already flagged: the latent opener gloss (your `/pr` step 3), the byte-carried mother-edition Rule Overview, and the §6 addendum's stale spec keep-list (Schema v0.6 / Nav-Contract v0.1 shipped in your birth tag while v0.7/v0.2 existed) | This crossing is the natural cure vehicle: the 0.8 tree carries the pointer-first files, the current spec pair (Schema v0.7 · Navigation Contract v0.2), and the fixed generator downstream of them — your Gate 2 maps each IF-0013 item to its arriving cure, your own dispositions per item |
| — (Settings) | parameterized | **Conversation Settings v0.9** — the owner parameter + the authority reset (a newborn's promotion ledger is empty — the clause your own birth already conformed to, C-134) | Re-project **your own adapters from your own adopted Settings** (KMP §4.4) — never copy the mother's adapter content |

Kernel-document editions in this release: GENESIS v0.20 · Node & Event Schema v0.7 · Navigation Contract v0.2 · Node Template v0.5 · Fieldnote Format v0.2 · Agenda Board Format v0.3 · User Document Pair Procedure v0.3 · **Interface Place Format v0.2** (v0.1 frozen history) · **Kernel Migration Procedure v0.2** (v0.1 frozen history) · Onboarding Protocol v0.8 · Conversation Settings v0.9 · Registry v0.12 · the `Templates/` seed tier · **the nine store tools (postman the ninth)** · the Rule Corpus + MAN. No claim in this table asserts your instance's state — every "adopt" is a recommendation gated by your own Gates 2–3 (KMP §3; TF1-16); the one observed-state citation in this advisory is §9's, dated.

## 4 · Receipt hand-off (KMP §2.6)

The receipt pair for `beta-0.8` travels separately with this advisory's delivery: SHA-256 of each hand-off document recorded on your side, OTS state disclosed (pending at issue; recheck at your Gate 5, cure post-landing by forward commit — both receipt hashes recorded, verdicts never reversed).

## 5 · The feedback ask (KMP §6.4 — an ask, never a duty)

The mother asks, through your owner, for the crossing's frictions and greens — the C-094 fieldnote loop. **Your crossing is the KMP v0.2 light lane's first field specimen**: what you find cures the template and the sibling advisory before KNet pins. A never-reporting instance is fully conformant — but this wave, your findings carry unusual weight, credited.

## 6 · Retrofit component set (KMP §4.5 — per-component recorded decisions; newborn-only components never retrofitted)

- **The postman kit:** `postman.py` + `test_postman.py` (store tools). Its cursor file is reader-side state, born at your first poll.
- **The opener poll step:** your `/pr` opener gains the postman poll after the fieldnote-depth step — and the same touch is the natural moment to cure the latent F2 gloss IF-0013 flagged in that file. Adapter-tier (C-097) — re-project from your own files.
- **The doctor roster:** `doctor_roster.json` — seed or tune yours so `doctor.py`-in-gates fires on your facts.
- **The Rule Corpus subtree:** arrives with the tree; MAN is the part your migration *reads* (KMP §10). Running the corpus program yourself is your own later decision — tool availability never creates governing authority (KMP §3.7).
- **Never retrofit:** the day-one receipt · the generated Rule Overview seed · genesis's connected-birth (your connection formalizes through the IF-0015 ceremony instead) · the seed tier's birth instantiation.

## 7 · Pack-time hygiene (owed once per release — stamped at the pack)

Authored ahead of the tagging close by design (the advisory freezes with the tag); **stamped at the pack, 2026-08-23 — all green:** the §7.3 clause-span check (GENESIS §3.4 and the Register agree at **C-140**) · GENESIS §0 count agrees at 140 · AST §6 partition seats **C-001–C-140 gapless** (C-134–C-140 classified at this close: five kernel + C-138 instance + C-140 kernel) · the **manifest pack-gate's first governing run** (45 elements each with a stance, every layer call closed, the 71-family CUSTOM roster present, all 15 spec pins matching the tree's newest editions) · the anchor-occurrence gate (every beta tag's receipt pair + mirror twin present) · the mirror checks (cleanliness · duplicates · intake layer · gh-pages · exclusions · own-chain receipts · HTML hygiene — all OK) · the **advisory-occurrence gate's own first run** (this stamp is what turned it green — the designed red→stamp→green sequence executed as written) · release class at the gate: **minor** (semantic versioning armed-inactive, FN-0006 pending).

## 8 · Optional pre-flight (KMP §8.8)

Deliberately not recommended for this crossing: **the crossing itself is the dress rehearsal** — the light lane's first field exercise, small by design, feeding its findings forward (§5). The beta-0.8 mechanism was already sandbox-proven at build (two scratch instances ran the full connection/RAM cycle from the standard's text alone); your delta review (Gate 2) plus the checker suite is the proportionate ceremony.

## 9 · The release class, declared (KMP §8.9 — new at v0.2; audit against MAN's layer read, §10.6)

**MINOR** — additive kernel, no contract break. Touched set: the C-139 additions (IPF v0.2 a **new** contract; the postman a **new** engine tool), the C-136 gate wiring, the document reissues named in §3. No existing CONTRACT pin moves incompatibly. Audit this claim against MAN's own layer bits; a disagreement stops at your owner (KMP §3.6).

**What the minor class means for you (KMP §9.2):** pin (§1–§2, lane-independent — authenticity is never lightened) → the manifest walk (engine elements swap wholesale per stance; generate-fresh/seed elements — your board, index, adapters, Rule Overview — **never overwritten**; the pre-printed EXCLUDE rows stand: your birth documents, store, contexts, Register, biography) → a one-page delta review → your owner's Gate 3 and your own `P-` row → Gate 5 as the checker suite green plus the identity diff (no instance-class document moved). No scratch rehydration — that is the major lane's gate; your recording of *what the light lane actually cost* is §5's most wanted datum.

**One observed-state note (C-096 read, 2026-08-23, cited per KMP §8.3):** your local `main` stood ahead of `origin/main` by 4 at the mother's read — conformant (no standing push travels into a birth, C-134; the push is your own act, through your owner). A *pushed* Gate-0 checkpoint needs that push first (KMP §1 rule 3). **Standing beside this advisory:** IF-0015 — the retroactive pair-record offer; its four-step ceremony (IPF §2.2) is the natural first touch that converts your v0.1-grammar index to v0.2 in the same act (lazy conversion exercised exactly as designed), and IF-0013 remains standing for your read.
