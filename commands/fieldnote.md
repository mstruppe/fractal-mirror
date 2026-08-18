---
description: Protocol a fieldnote — a friction or a green datum — into the right ledger mid-session, then return to the work — C-094 (usage /fieldnote <target> <what happened>)
---
Protocol a field observation per C-094: **$ARGUMENTS**

**Step 0 — deterministic routing (Max's ruling of record, 2026-08-16: the target is a fact, never an interpretation).** Run `python3 "Claude/Knowledge Graph Store/fieldnote.py" <target> <report text>` with the argument exactly as given. **If the tool errors (missing or unknown target): report its error to Max and STOP — no capture happens, no fallback interpretation, ever.** On success the tool has appended one **machine-format block** (Fractal Fieldnote Format v0.1 — verbatim, timestamped, attributed, deterministically routed). **The block is the fact layer and is immutable — never edit it.**

The first word of the argument is the **target**; everything after it is **Max's report** — his words are the datum, and they live verbatim inside the block. If Max states the observation's class, pass `--kind friction|green|vision|question` before the target; otherwise the tool records `capture` — classification is judgment and is never invented.

**Target roster (PROJECTION — the machine-readable authority is `Claude/Knowledge Graph Store/fieldnote_roster.json`; edit there first, mirror here):**

| Target | Ledger | Notes |
|---|---|---|
| `knet` | `Site/Fieldnotes_2026-08-15_First-Shipping-Run.md` | KNet's use **is** the shipped beta's field test — the entry lands in the running shipping-run ledger, context-tagged KNet (surface included, e.g. the ChatGPT desktop). KNet-internal *research* frictions may additionally live in the child's own ledger (GENESIS parameter 7); the mother ingests both at a phase boundary. |
| `beta` | `Site/Fieldnotes_2026-08-15_First-Shipping-Run.md` | The shipped release under field test directly (kernel, onboarding, commands, tooling). Same ledger as `knet` while the beta is the one running subject. |
| `publish` | `Site/Fieldnotes_2026-08-16_Publishing.md` | The publishing lane (opened 2026-08-16 on Max's word): what the website and the onboarding must explain — the public-identity explanation burden. Feeds move 2 (site, tutorials, GUIDE) and the Onboarding Protocol's revisions. |
| `general` | `Site/Fieldnotes_2026-08-16_General.md` | The catch-all lane (opened 2026-08-16 on Max's word): ideas and observations fitting no registered subject — research-program seeds, vision-class captures. Entries graduate to the Register, a foundation, or their own instance on Max's word. |

An unlisted target: say so, print the roster (`--list`), stop. Adding a target (a new test subject = a new ledger) is an ordinary edit to the roster JSON, on Max's word — friend instances join here as the friends-beta grows.

**The protocol:**

1. After the tool's block: the judgment half is yours — **after** the block (never inside it), add the ledger's established prose entry (`### N. Title`, **What happened** with Max's words already carried by the block, **Cure** if one exists or was applied, **Guide implication / fix shape**), context-tagged with where it occurred. The prose numbering continues the ledger's tradition; the block's `FN-` id is the machine sequence — the two are independent layers.
2. **C-094 discipline:** any fix is a proposal for the **generator** (kernel, next release) — never patch the field instance from here. A green datum (a clean run, a thing that just worked) is equally recordable through this same door.
3. **Do not commit** — the entry rides the session's next close (or the standing post-close append pattern if Max asks for it explicitly).
4. Confirm to Max in **one line** (id + ledger), then return immediately to the interrupted work. Minimal disturbance is the point of this command.

---
*Stamped-procedure projection (C-035 class): compresses the C-094 capture step — sources: the C-094 row in the Decision Register + Protocol v0.40; the two-part steerable shape follows `/look`; the name is Max's pick of record; **the deterministic split is his ruling of record** (2026-08-16, after entry 41's omitted target — routing = the tool, machine fact; formatting = the AI surface, judgment; the C-073 division). Re-stamped 2026-08-16 (the flip-preparation session): the tool graduated beside the store tools with the intake half (entry 39's trigger), captures became immutable machine blocks (Fractal Fieldnote Format v0.1), roster authority moved to `fieldnote_roster.json`. Refresh triggers: a C-094 amendment, a roster/ledger change (JSON first, this table after), a new test subject, a fieldnote.py behavior change, a Format reissue.*
