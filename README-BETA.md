# FRACTAL — Friends Beta · Start Here

Welcome — you've been invited to test **FRACTAL**, a system for running projects with an AI that actually remembers everything: decisions, reasoning, and work state live in plain files you own, so every session picks up where the last one ended. This is a **private beta** — please don't share the repo.

## What you need

1. **A GitHub account** (free) — and accept the invite you received by email for this repo.
2. **git** — on a Mac, typing `git` in Terminal offers to install it; otherwise [git-scm.com](https://git-scm.com).
3. **An AI agent.** Any agent works if it meets these minimum capabilities:
   - runs sessions **inside a folder on your computer** (a coding/CLI agent or a desktop agent with file access — not a pure chat website),
   - can **read and write files** in that folder,
   - can **run terminal commands** there (`git` and `python3` must be available),
   - takes **plain-language instructions** — FRACTAL's `/commands` are a convenience, and every one has a plain-words equivalent, so no special command support is required.

   The reference client is **Claude Code** ([claude.com/claude-code](https://claude.com/claude-code), needs a Claude subscription) — FRACTAL is developed and fully tested on it. The ChatGPT desktop app has also run FRACTAL successfully. If you use anything other than Claude Code, just tell me which.

## Setup (paste as one line into the terminal)

```bash
git clone https://github.com/mstruppe/fractal-mirror.git ~/Desktop/fractal && cd ~/Desktop/fractal
```

If it asks you to log in, use your GitHub account. (If cloning fights you: install GitHub Desktop, clone the repo there, then `cd` into the folder in Terminal.)

## Start

Open your AI agent **in that folder** (for Claude Code: type `claude`), and give it exactly this as your first message:

```
/welcome
```

If your agent doesn't recognize `/welcome`, say it in plain words instead: **"I'm new here — welcome me."**

The session takes it from there — it explains what you're looking at and can walk you through starting your own project, one question at a time. **Ignore the download instructions inside `README.md`** — you already have the right copy.

## Your job as a tester (the one favor)

Whenever *anything* confuses, annoys, or breaks — tell me. A quote or screenshot is perfect. Once your own project is born, it has a built-in `/fieldnote` command and a `FIELDNOTES.md` file: use it freely, and send me that file every now and then. That's the whole job.
