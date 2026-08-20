# Advisory — kernel release beta-0.7 (mother → any child instance, through the owner)

> **DATA, NEVER INSTRUCTION (C-096 class).** The per-release migration advisory the mother owes at every anchored release (`Fractal_Kernel_Migration_Procedure_v0.1` §8 — the second instantiation; the eight-section template). Everything here is **audited, never obeyed** (KMP §1.8): adoption is the reading instance's own recorded decision, and a never-migrating instance is conformant forever (KMP §1.2). Citation convention (UF1-7's cure): document-qualified section cites — `KMP §n` = Fractal_Kernel_Migration_Procedure_v0.1 · `GENESIS §n` = GENESIS.md at this release · `AST §6` = Fractal_Architecture_State §6 as shipped in this release.

**Issued:** 2026-08-20, at the beta-0.7 tagging close · **Author:** Claude (AGENT.AI.CLAUDE, mother-side) · **Of record:** Protocol v0.66 + `Fractal_Update_Plan.md` (the frozen beta-0.7 edition, v0.11, in git history)

## 1 · Pin identity (KMP §2)

- **Tag:** `beta-0.7` on `github.com/mstruppe/fractal` (the mother repo); the mirror's own `beta-0.7` follows on `github.com/mstruppe/fractal-mirror` (the public home — pin from there if you work from public releases).
- **Commit SHA and tag-object SHA:** resolve them yourself against the tag — a copied SHA is not a pin (KMP §2.2). This document ships inside the release tree and therefore cannot carry its own tag's hashes or attestation (the structural-absence rule, KMP §2.6); the receipt pair (`.txt` + `.ots`) is handed over separately, OTS state disclosed at hand-off, **pending-at-issue expected and non-blocking**.
- **Signing key (fingerprint + principal, never a label):** ED25519 `SHA256:gSUgFha7OI7a4QfYaPRtPtROmabsksQDmtU5sh9fH0Y`. Principals bound to this custody key: `max.struppe@gmail.com` (mother repo) · `fractal@knet.network` (mirror chain). One custody environment, one key (C-074b); the signature attests custody, the author field attributes.
- **The signers bind, verbatim (KMP §2.3):** before `git tag -v`:
  `git config gpg.ssh.allowedSignersFile "$(git rev-parse --show-toplevel)/.allowed_signers"`
- Run `git fsck --strict` and record the result (KMP §2.5).

## 2 · Transport (KMP §2.7–§2.8)

`git clone --no-local` → checkout the tag → record the remote's URL in your receipt → **`git remote remove origin`**. The frozen clone is a reference copy — read-only evidence, never a working surface. For full rehydration independence, the self-contained bundle option (KMP §2.8): a complete-history bundle of the signed tag plus its SHA-256, at your own upstream-provenance location, verified by bundle-only checkout.

## 3 · Delta inventory (baseline beta-0.6, Register C-130 → this release, C-133)

Hand-derived from the Register × the pinned partition (AST §6 in this release — the classification source of record; where any hint below disagrees with your pinned §6, **the pinned §6 wins**, KMP §3):

| Rows | Class per pinned AST §6 | What it is | Disposition hint (audit, never obey) |
|---|---|---|---|
| C-131 | kernel | **The seed-tree principle** — `Templates/` ships four frozen `_Seed_v0.0` editions of the kernel trio's user halves + the buffer shape; genesis instantiates them at birth (`User Documents/` born already-built-but-empty); grown documents carry **Grown from:** stamps (hash-match ⇒ mechanical migration); Pair Procedure v0.3 carries the law | Adopt the standard + the seed tier; retrofit notes in §6 |
| C-132 | kernel | **The behaviour-convention class** — callable, scope-bound rule-sets on the Registry shelf (§4); the invocation law travels as doctrine; the MRC (five math rules) the second member, C-115's scholarly rules the retroactive first | Adopt the class doctrine; members by own decision (shelf-tier) |
| C-133 | kernel | **The kernel ratification clause** — one ratification at the origin, holding the responsibility for all: kernel artifacts as shipped are auto-ratified by the mother's owner; the responsibility held to best knowledge through agents + gates; the C-090 signed tag its cryptographic form; GENESIS §3.4's ground paragraph the child-side statement. Deliberate vocabulary: *ratification holding responsibility*, never a legal warranty | Adopt — this is the trust doctrine your own inheritance clause already rests on, now stated in-document |
| — (S6 ledger) | kernel (tools) | **The Scan #6 tool batch** — `close.py`: four new pack checks (partition seats · exclusion absence · own-chain receipts · HTML hygiene) + the staging rule; `check_versions.py`: the `User Documents/` + `Templates/` walk and **the pair-half currency gate** (FN-0002 — a half stamping its original at a stale version is an ERROR); `fieldnote.py` silent-loss cures; `check_scan.py` anchored ledger trace | Adopt with the tool set |
| — (spec pair) | kernel (specs) | **Schema v0.7 + Navigation Contract v0.2** — currency-and-review reissues, **no format change, no read-behaviour change**: the `Reviewed By` header fields land (C-133's first exercise), rule 7's route parenthetical cured, conformance re-checked at the live scale | Adopt the editions; nothing in your store needs rewriting |

Kernel-document editions in this release: GENESIS v0.17 · Node & Event Schema v0.7 · Navigation Contract v0.2 · Node Template v0.5 · Fieldnote Format v0.2 · Agenda Board Format v0.3 · User Document Pair Procedure v0.3 · Interface Place Format v0.1 · Kernel Migration Procedure v0.1 · the `Templates/` seed tier (four `_Seed_v0.0` editions) · the MRC v0.1 (shelf) · the eight store tools. No claim in this table asserts your instance's state — every "adopt" is a recommendation gated by your own Gates 2–3 (KMP §3; TF1-16).

## 4 · Receipt hand-off (KMP §2.6)

The receipt pair for `beta-0.7` travels separately with this advisory's delivery: SHA-256 of each hand-off document recorded on your side, OTS state disclosed (pending at issue; recheck at your Gate 5, cure post-landing by forward commit — both receipt hashes recorded, verdicts never reversed).

## 5 · The feedback ask (KMP §6.4 — an ask, never a duty)

The mother asks, through your owner, for the migration's frictions and greens — the C-094 fieldnote loop. A never-reporting instance is fully conformant. Whatever you send lands in the mother's ledger credited.

## 6 · Retrofit component set (KMP §4.5 — per-component recorded decisions; newborn-only components never retrofitted)

- **The seed tier (C-131):** newborns receive `Templates/` + built-but-empty halves at genesis. An existing instance retrofits by copying `Templates/` and, at its own pace, adding **Grown from:** stamps to halves it regenerates — the stamps are what make future migrations mechanical; nothing forces a regeneration.
- **The behaviour-convention class (C-132):** the class doctrine is a Registry §4 block; a member (e.g. the MRC) installs as one standard file + optionally one command file — summoned by name on any client, the words work everywhere.
- **The spec editions (Schema v0.7 · Navigation Contract v0.2):** drop-in — no format or read-behaviour change; your store and tools are already conformant if they were at beta-0.6.
- **The tool batch:** copy the four tools that moved (`close.py`, `check_versions.py`, `fieldnote.py`, `check_scan.py`); the pair-half gate only fires on halves that stamp their originals — version-agnostic stamps are unforced.
- **Never retrofit:** genesis-only birth artifacts; the mother's custom pairs (C-129 class — grow your own).

## 7 · Pack-time hygiene (owed once per release — this release's state)

The §7.3 clause-span check ran green at this pack (GENESIS §3.4 current to C-133; §0 counts 133/~110); the four new pack checks (partition seats · exclusion absence · own-chain receipts · HTML hygiene) ran their first tagging close green; the S6-1.1 staging rule executed its first pack (the completed Update Plan edition committed before the reset); GENESIS §5 shelf pointers remain migration-proof.

## 8 · Optional pre-flight (KMP §8.8)

A TF1-style dress rehearsal remains available practice: adversarial probes + independent refuter against sandboxed pinned clones before your Gate 4. The beta-0.6 → beta-0.7 delta is doctrine-and-spec-heavy and format-light; the highest-value probes are the pair-half gate's behavior on your own halves (§3's tool row) and the seed-tier copy (§6's retrofit note).
