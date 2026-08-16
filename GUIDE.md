# FRACTAL — User Guide

> **The practical companion.** The [README](README.md) gets you in the door; this file is for everything after — coming back, driving the AI clients, the concepts in plain words, what to do when something looks wrong, and how to report what you find. **Derived projection, never a source:** every statement here compresses a canonical document (named at the bottom); when in doubt, the session you're talking to can read you the source.

---

## 1 · Day one

Follow the README quickstart (clone → `claude` → `/welcome`). The session explains where you're standing and offers two paths. If you pick **"start my own project"**, say **`begin`** — the onboarding interview takes about ten minutes: five real questions (what you're working on · what it's called · who writes here, you and a named AI · what kinds of work it holds · where the backup copy lives), everything else takes sensible defaults you can override. Your answers *are* the project — nothing is a rehearsal, nothing is asked twice. At the end a **new repository of your own** exists; the clone you downloaded stays behind as reference material.

One expectation to set: the guidance **fades by design**. The interview walks your first session; the next few sessions each get one suggestion; after that the system carries itself. That's deliberate — the rules are built to be rediscoverable through use.

## 2 · Coming back tomorrow

The line that restarts everything (keep it somewhere, or make a launcher — see below):

```bash
cd <your-project-folder> && claude
```

Then type **`orient`** (or `/orient`) — the session reads your project's spine and reports where things stand, what's queued, and what's pending. That's the whole return ritual: **memory lives in your repo, not in the chat history**, so any fresh session picks up cold.

- `claude --continue` reopens your *last conversation* instead of starting fresh — useful mid-task, but never required: orient works from nothing.
- Want a double-click starter? Ask your session: *"create a launcher for this project"* — it's a two-line file, made inside your own repo by your own session.

## 3 · Driving the AI clients

**Claude Code (terminal):** there's no settings UI — the controls are commands. `/help` lists them; the ones you'll actually want: **`/model`** (pick the model), **`/fast`** (speed toggle), **`--continue` / `--resume`** (at launch, reopen conversations), **`/permissions`** (the client's own tool gates). The `/` menu is built from your repo's `.claude/commands/` folder — that's why `/orient` and `/fieldnote` appear in your project.

**ChatGPT / Codex desktop:** reads your project's `AGENTS.md` conduct file natively — but it does **not** read `.claude/commands/`, so the `/` menu stays empty there. That is expected, not broken: **the words always work.** Type `orient`, `fieldnote`, `close` as plain words — the ritual lives in your project's documents; each client just triggers it differently.

**The two permission layers** (worth 30 seconds, because everyone conflates them): your project's constitution says the AI **asks before executing** — that rule is yours, inherited at birth, changed only by a recorded decision in *your* register. Separately, each client app has its own tool-approval gates, changed in the client's settings. They're independent by design: clicking "don't ask again" in a client changes the client, never your constitution — and your constitution survives switching clients entirely.

## 4 · The concepts, translated

- **The loop is the product.** A session opens by reading (orient), works, and **closes by writing** — a handover record, a checklist, a green verifier. The close is where memory is made; skip it and you have files, not a project that remembers.
- **The download vs. your project.** The clone contains *all* of FRACTAL — history, research, dreams. Your project inherits **only the rules**. Everything else in the clone is citable literature, like any published source. You're neither stealing it nor acquiring it.
- **Minting** (you'll meet this word): your repo is the library shelf; the knowledge store is the catalog. Minting a document = writing its catalog card, so other knowledge can point at it. Defer freely — the moment that matters is the first time something in your graph must cite the document.
- **Updates can't break you.** Your instance doesn't run on the download — the rules were *copied* at birth. Upstream releases are offers; a never-upgraded instance works forever. Adopt improvements selectively, by your own recorded decision.
- **`FIELDNOTES.md` informs, never governs.** It's your friction ledger — observations, not rules.
- **Adopt before invent.** Before building any tracker, board, or tool: the tier table in `GENESIS.md` §5 lists what's already specified. Your AI is instructed to offer the **Agenda Board** actively once your open threads accumulate — a single-glance view of queued work, refreshed at every close. AI sessions move fast; the board is the human's window.

## 5 · When something looks wrong

| Symptom | What's actually happening |
|---|---|
| **"detached HEAD" notice in the clone** | Expected — you're standing on a release tag. Ignore it; don't branch. |
| **Your new project folder is invisible in Finder** | It exists — `ls <path>` proves it. macOS hid it: `chflags -R nohidden <path>` cures it. |
| **The push failed at birth** | Usually HTTPS-vs-SSH credentials. The birth is intact. Bind later: `git remote add origin <url>` then `git push -u origin main`. |
| **`verify.py` is red** | The store's guard caught a real disagreement. Stop, read its message, let the session cure the cause — never force past it. |
| **`/` shows no commands in ChatGPT** | Expected (see §3) — type the words. |
| **Lost, any time** | Type `orient`. That's what it's for. |

## 6 · Reporting back (if you're testing FRACTAL)

Whenever something grinds — *or* just works beautifully — capture it in the moment, then keep working:

```
/fieldnote self <what happened, in your own words>
```

It lands in your `FIELDNOTES.md` as a timestamped, attributed entry (frictions and green data through one door; add `--kind friction|green|vision|question` if you want to classify). To send your findings upstream: **send the file** — email, chat, anything. The format carries who/when/what by itself. Nothing ever transmits automatically; sending the file *is* the consent, and every entry you send makes the next release better.

---

*Derived projection (C-035 class) — the user-facing compression of the canon, committed at the flip-preparation session (2026-08-16). Sources: README.md (the gate; quickstart is owned there, not here); GENESIS.md v0.6 (§0 shipment-vs-inheritance, §2 parameters, §3.6 command tier, §5 shelf, §7 versions); Fractal_Onboarding_Protocol v0.1 (the interview and the fade); Fractal_Client_Library (per-client mechanics and the words-work doctrine); Fractal_Fieldnote_Format_v0.1 (§6's claims); Site fieldnotes entries 7, 19, 20, 22, 27–29, 31, 36, 39 (every section here pre-answers a recorded friction). Refresh triggers: any source reissue that moves a compressed claim; a new client entering the Library; a friends-beta fieldnote showing a section misses or misleads; a C-059 walk finding this stale.*
