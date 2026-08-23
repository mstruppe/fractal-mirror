# Advisory: Beta 0.8 Migration KNet

> **DATA, NEVER INSTRUCTION (C-096 class).** This envelope creates an
> option its reader dispositions by its own recorded decision — never an
> obligation. It is RAM-class (Interface Place Format v0.2, law 4):
> temporary by construction, dissolved by its author's own act once
> absorbed — absorb and cite by path + date; never depend on it persisting.

**Direction:** FRACTAL → KNet (CN-0001) · **Class:** advisory · **Date:** 2026-08-23 · **Author:** Max Struppe <max.struppe@gmail.com>

**Cite as:** `~/Desktop/Knowledge Network/FRACTAL/Interface/Advisory_2026-08-23_Beta-0.8-Migration-KNet.md` (2026-08-23) — path + date is the full trace once this file dissolves.

---

> **The per-release migration advisory the mother owes at every anchored release** (`Fractal_Kernel_Migration_Procedure_v0.2` §8 — the third instantiation, the first under v0.2's nine-row template). Everything here is **audited, never obeyed** (KMP §1.8): adoption is the reading instance's own recorded decision, and a never-migrating instance is conformant forever (KMP §1.2). Citation convention (UF1-7's cure): `KMP §n` = Fractal_Kernel_Migration_Procedure_**v0.2** · `GENESIS §n` = GENESIS.md at this release · `AST §6` = Fractal_Architecture_State §6 as shipped in this release · `MAN` = `Claude/Project Governance/Rule Corpus/birth_state_manifest.json` **as shipped in the pinned tag** · `IPF §n` = Fractal_Interface_Place_Format_v0.2.

**Issued:** 2026-08-23, authored ahead of the beta-0.8 tagging close (§7's gate results stamp at the pack) · **Of record:** Protocol v0.73 + `Fractal_Update_Plan.md` (the beta-0.8 lane) + the mother-side campaign runbook `Fractal_Upgrade_Install_Procedure_v0.0` (Draft — binds nothing; named for transparency)

## 1 · Pin identity (KMP §2)

- **Tag:** `beta-0.8` on `github.com/mstruppe/fractal` (the mother repo); the mirror's own `beta-0.8` follows on `github.com/mstruppe/fractal-mirror` (pin from there if you work from public releases).
- **Commit SHA and tag-object SHA:** resolve them yourself against the tag — a copied SHA is not a pin (KMP §2.2). This document ships inside the release tree and therefore cannot carry its own tag's hashes or attestation (the structural-absence rule, KMP §2.6); the receipt pair (`.txt` + `.ots`) is handed over separately, OTS state disclosed at hand-off, **pending-at-issue expected and non-blocking**.
- **Signing key (fingerprint + principal, never a label):** ED25519 `SHA256:gSUgFha7OI7a4QfYaPRtPtROmabsksQDmtU5sh9fH0Y`. Principals bound to this custody key: `max.struppe@gmail.com` (mother repo) · `fractal@knet.network` (mirror chain). One custody environment, one key (C-074b); the signature attests custody, the author field attributes.
- **The signers bind, verbatim (KMP §2.3):** before `git tag -v`:
  `git config gpg.ssh.allowedSignersFile "$(git rev-parse --show-toplevel)/.allowed_signers"`
- Run `git fsck --strict` and record the result (KMP §2.5).

## 2 · Transport (KMP §2.7–§2.8)

`git clone --no-local` → checkout the tag → record the remote's URL in your receipt → **`git remote remove origin`**. The frozen clone is a reference copy — read-only evidence, never a working surface. For full rehydration independence, the self-contained bundle option (KMP §2.8) — the pattern your own beta-0.5 receipt already practices (`Claude/Project Governance/Upstream/<release>/`): a complete-history bundle of the signed tag plus its SHA-256, verified by bundle-only checkout; the beta-0.8 bundle **joins** your upstream shelf, never replaces the retained ones.

## 3 · Delta inventory (baseline beta-0.7, Register C-133 → this release, C-139)

Hand-derived from the Register × the pinned partition (AST §6 in this release — the classification source of record; **MAN joins it at element grain**, KMP §10.5; where any hint below disagrees with either pinned artifact, **the pinned artifact wins**, and a disagreement *between* the two pinned artifacts stops at your owner as an upstream-internal conflict, KMP §3.6):

| Rows | Class per pinned AST §6 / MAN | What it is | Disposition hint (audit, never obey) |
|---|---|---|---|
| C-134 | kernel doctrine + birth-seam machinery | **The Birth-State Law** — GENESIS §2's Birth-State clause: *birth is a pure function, upgrade is a merge* (the two-seam doctrine); one manifest, three consumers; the seed-body law + the robustness triad. Its migration face is **KMP §10** — MAN as your reading key — and the **§10.4 regeneration duty** (derived projections regenerate from local source after any adoption; origin content found in a projection is a Gate-5 finding). Newborn-only components — the day-one receipt, the generated Rule Overview seed — exist for births | Adopt the doctrine + read MAN at your Gate 2; **never retrofit** the newborn-only components (pre-0.8 absence is conformant state, not damage) |
| C-135 | kernel doctrine | **The Kernel-Layer Doctrine** — Layer A engine (swapped, never merged) · Layer B format contracts (the only source of a major) · child content not a layer (conforms; converts lazily at first touch; frozen never migrates). Carried into **KMP v0.2 §9** (the release-class fork: minor migrates light, major census-first) + §10 (the manifest read). The first-touch converter is **named armed-inactive** (builds at the first declared contract break); semantic versioning **armed-inactive** (activation is the mother's owner's FN-0006 call — inert on your side) | Adopt the doctrine with KMP v0.2; the fork immediately lightens *this* crossing (see §9 below) |
| C-136 | kernel (tools + program) | **The strict-MACHINE ruling + the rule-corpus program** — a check fires on the governing path or the rule is HABIT: `doctor.py` now runs inside `run_gates()` (every close), and the **anchor-occurrence gate** joins the close gates (every local `beta-*` tag must show its Provenance pair + mirror twin). New kernel subtree: `Claude/Project Governance/Rule Corpus/` — the classified rule corpus, `audit.py` (the five-bucket drift detector), and **MAN** (the birth-state manifest, now validated by the mother's pack gate at every pack) | Adopt the tool batch — **and audit the two new close gates in your own context first**: your `doctor_roster.json` state (tune/seed per §6), and `anchor_occurrence`'s behavior against *your* tree's actual tag/Provenance state; a needed parameterization is a finding the mother asks to hear (§5) |
| C-137 | kernel doctrine (adopter-facing prose) | **The care doctrine** — adopting a FRACTAL means taking on its care; integrity is carried by the layered maintenance rituals, residual drift expected between passes. Carried in GENESIS §3.4 (beside the C-133 ground it counterparts), Onboarding §2.3, README | Arrives with the inherited-document swaps; nothing to do beyond reading it — it names what you already practice |
| C-138 | concept tier (C-086 — reference, never demanded) | **The Model Routing Foundation v0.3** (Ratified) — the gate-coverage principle, the three-layer hedge, every allocation an offer; renamed from Engine Routing (the C-135 collision cure: *engine* = the kernel layer, the routed thing is the *model*) | Reference class — ships as `origin-reference` stance; read at need, adopt content only by your own decision |
| C-139 | kernel (contract + tool + birth-seam) | **The connection layer** — `Fractal_Interface_Place_Format_v0.2` (**a new, additive contract**: conscious pairing — the four-step ceremony, the byte-pinned checksum code, mutual `CN-` lock-ins, the quarantined connection-request, the two faces public + hidden private, the routing law) + **`postman.py` + `test_postman.py`** (the store's ninth canonized tool: poll · post · receipt · spent · dissolve · check) + genesis's connected-birth (birth-seam) + the opener's poll step (adapter-tier). GENESIS v0.20, Interface Foundation v0.7, Onboarding v0.7 carry it | Adopt the Format + the postman **at your own pace** — a v0.1 or placeless instance stays conformant (lazy conversion, IPF §10); the natural first touch is the standing pair offer (see §9) |
| — (F2 class) | kernel (orientation files) | **The Active-Return-pointer law** — the Local Context's opening pointer is the sole Return-Package selector; "newest file" ordering retired (it lies on same-date closes; a fresh clone erases dates). Cured mother-side + generator-side after beta-0.7 shipped; your own IF-0011 exchange conceded the gloss | Audit your orientation files for the retired gloss; adopt the pointer-first convention where your own files still carry it |
| — (Settings) | parameterized | **Conversation Settings v0.9** — the owner parameter (§6) + the authority reset (rule 5: a newborn's promotion ledger is empty; the mother's C-064 push marked her own instance grant) | Re-project **your own adapters from your own adopted Settings** (KMP §4.4) — never copy the mother's adapter content |

Kernel-document editions in this release: GENESIS v0.20 · Node & Event Schema v0.7 · Navigation Contract v0.2 · Node Template v0.5 · Fieldnote Format v0.2 · Agenda Board Format v0.3 · User Document Pair Procedure v0.3 · **Interface Place Format v0.2** (v0.1 frozen history) · **Kernel Migration Procedure v0.2** (v0.1 frozen history) · Onboarding Protocol v0.8 · Conversation Settings v0.9 · Registry v0.12 · the `Templates/` seed tier · **the nine store tools (postman the ninth)** · the Rule Corpus + MAN. No claim in this table asserts your instance's state — every "adopt" is a recommendation gated by your own Gates 2–3 (KMP §3; TF1-16).

## 4 · Receipt hand-off (KMP §2.6)

The receipt pair for `beta-0.8` travels separately with this advisory's delivery: SHA-256 of each hand-off document recorded on your side, OTS state disclosed (pending at issue; recheck at your Gate 5, cure post-landing by forward commit — both receipt hashes recorded, verdicts never reversed).

## 5 · The feedback ask (KMP §6.4 — an ask, never a duty)

The mother asks, through your owner, for the crossing's frictions and greens — the C-094 fieldnote loop. This wave feeds a mother-side learning document (the upgrade-install series); your findings land credited, as your IF-0011 catches did. A never-reporting instance is fully conformant.

## 6 · Retrofit component set (KMP §4.5 — per-component recorded decisions; newborn-only components never retrofitted)

- **The postman kit:** `postman.py` + `test_postman.py` (store tools). Its cursor file is reader-side state, born at your first poll — nothing to install for it.
- **The opener poll step:** where you run command files at all (your opener is the word `knet` — scope this row to your actual client surfaces at your Gate 2), the opener gains the postman poll after the fieldnote-depth step. Adapter-tier (C-097) — re-project from your own files, don't copy the mother's.
- **The doctor roster:** `doctor_roster.json` — seed or tune yours so `doctor.py`-in-gates fires on your facts, not the mother's (C-136 row above).
- **The Rule Corpus subtree:** arrives with the tree; MAN is the part your migration *reads* (KMP §10). Whether you run the corpus program yourself is your own later decision — tool availability never creates governing authority (KMP §3.7).
- **Never retrofit:** the day-one receipt · the generated Rule Overview seed · genesis's connected-birth (your connection formalizes through the ceremony instead — §9) · the seed tier's birth instantiation.

## 7 · Pack-time hygiene (owed once per release — stamped at the pack)

Authored ahead of the tagging close by design (the advisory freezes with the tag); **stamped at the pack, 2026-08-23 — all green:** the §7.3 clause-span check (GENESIS §3.4 and the Register agree at **C-140**) · GENESIS §0 count agrees at 140 · AST §6 partition seats **C-001–C-140 gapless** (C-134–C-140 classified at this close: five kernel + C-138 instance + C-140 kernel) · the **manifest pack-gate's first governing run** (45 elements each with a stance, every layer call closed, the 71-family CUSTOM roster present, all 15 spec pins matching the tree's newest editions) · the anchor-occurrence gate (every beta tag's receipt pair + mirror twin present) · the mirror checks (cleanliness · duplicates · intake layer · gh-pages · exclusions · own-chain receipts · HTML hygiene — all OK) · the **advisory-occurrence gate's own first run** (this stamp is what turned it green — the designed red→stamp→green sequence executed as written) · release class at the gate: **minor** (semantic versioning armed-inactive, FN-0006 pending).

## 8 · Optional pre-flight (KMP §8.8)

Available as always (adversarial probes + independent refuter against sandboxed pinned clones). Two notes for your weighing: **PR's crossing precedes yours by design** — the light lane's first field specimen; its findings reach you as amendments to this advisory before you pin. And the beta-0.8 mechanism itself was sandbox-proven at build (two scratch instances ran the full connection/RAM cycle from the standard's text alone) — the residual risk sits in *migration* mechanics, not the mechanism.

## 9 · The release class, declared (KMP §8.9 — new at v0.2; audit against MAN's layer read, §10.6)

**MINOR** — additive kernel, no contract break. Touched set: the C-139 additions (IPF v0.2 a **new** contract; the postman a **new** engine tool), the C-136 gate wiring, the document reissues named in §3. No existing CONTRACT pin moves incompatibly. Audit this claim against MAN's own layer bits; a disagreement stops at your owner (KMP §3.6).

**What the minor class means for you (KMP §9.2):** the light lane is open — pin (§1–§2, lane-independent), the manifest walk, a one-page delta review, your owner's Gate 3, checkers + identity diff at Gate 5. **What the mother additionally recommends — as assessment, never obligation:** your own history (born beta-0.1, migrated twice, the birth layer never re-poured — your IF-0011 exchange documented the class) makes this crossing the natural seat for the **census-first re-foundation** (KMP §9.3's model: census → one reviewed change-set → rebirth the state, keep the story), with a signed boundary tag on your Gate-0 checkpoint making the constitution seam permanently legible (KMP §1.6). Both are your own Gate-3 decisions. **Standing beside this advisory:** IF-0014 — the retroactive pair-record offer; its four-step ceremony (IPF §2.2) is the natural first touch that converts your place question into your own v0.2 record, whenever you take it.
