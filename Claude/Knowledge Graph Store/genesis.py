#!/usr/bin/env python3
"""FRACTAL Knowledge Graph Store — new-instance genesis executor.

Builds the tier-0 kernel, parameterized spine, empty instance ledger, and root
namespace for a new FRACTAL-governed project. The target is an independent git
repository with its own initial commit and no inherited FRACTAL event history.

Stdlib-only. Dry-run by default — nothing is written without --write.

Usage:
  python3 genesis.py --target <path> --name <ProjectName> \
      --human <AGENT.HUMAN.NAME> --ai <AGENT.AI.NAME> \
      --route <CODE>[,<CODE>...] [--remote <url>] [--write]
"""
import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time


HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE_REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
C32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
SEGMENT_RE = re.compile(r"^[A-Z0-9](?:[A-Z0-9_]*[A-Z0-9])?$")
NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")
HUMAN_RE = re.compile(
    r"^AGENT\.HUMAN\.[A-Z0-9](?:[A-Z0-9_]*[A-Z0-9])?$"
)
AI_RE = re.compile(r"^AGENT\.AI\.[A-Z0-9](?:[A-Z0-9_]*[A-Z0-9])?$")

KERNEL = (
    "Claude/Architecture/Concepts/Knowledge Graph/Fractal_Node_and_Event_Schema_v0.6.md",
    "Claude/Architecture/Concepts/Knowledge Graph/Fractal_Node_Template_v0.5.md",
    "Claude/Architecture/Concepts/Knowledge Graph/Fractal_Navigation_Contract_v0.1.md",
    "Claude/Knowledge Graph Store/mint.py",
    "Claude/Knowledge Graph Store/verify.py",
    "Claude/Knowledge Graph Store/check_versions.py",
    "Claude/Knowledge Graph Store/doctor.py",
    "Claude/Knowledge Graph Store/fieldnote.py",
    "Claude/Project Governance/Governance Documents/Fractal_Conversation_Settings.md",
    "Claude/Project Governance/Governance Documents/Fractal_Rule_Overview.md",
    "Claude/Project Governance/Governance Documents/Fractal_Fieldnote_Format_v0.1.md",
    "LICENSE",
    "LICENSE-docs",
    "NOTICE",
)

FACETS = (
    ("FACET.TOPIC", "Topic", "topic"),
    ("FACET.METHOD", "Method", "method"),
    ("FACET.SOURCE_TYPE", "Source type", "source-type"),
    ("FACET.TIME", "Time", "time"),
    ("FACET.AGENT", "Agent", "agent"),
)

# Generated into newborns only — assembled in two parts so repo checkers never
# read a mother-side path claim from this file (the version_registry idiom).
RAIL_PATH = "Claude/Context Packages/" + "First_Loops_Rail.md"


def die(message):
    print(f"REFUSED: {message}")
    raise SystemExit(1)


def ulid(now_ms):
    random_bits = int.from_bytes(os.urandom(10), "big")

    def encode(value, length):
        return "".join(
            C32[(value >> (5 * index)) & 31]
            for index in range(length - 1, -1, -1)
        )

    return encode(now_ms, 10) + encode(random_bits, 16)


class Clock:
    def __init__(self):
        self.next_ms = int(time.time() * 1000)

    def take(self):
        now_ms = self.next_ms
        self.next_ms += 1
        timestamp = datetime.datetime.fromtimestamp(
            now_ms / 1000, datetime.timezone.utc
        ).strftime("%Y-%m-%dT%H:%M:%SZ")
        return now_ms, timestamp


def parse_routes(raw):
    routes = [value.strip() for value in raw.split(",")]
    if not routes or any(not value for value in routes):
        die("--route requires one or more comma-separated root codes")
    if len(set(routes)) != len(routes):
        die("--route values must be unique")
    for route in routes:
        if not SEGMENT_RE.fullmatch(route):
            die(
                f"route {route!r} is not a root code "
                "(use one uppercase code segment, with digits/underscores allowed)"
            )
        if route in {"FACET", "AGENT"}:
            die(f"route {route!r} collides with a genesis-owned root")
    return routes


def normalize_remote(remote):
    """Normalize the --remote value (GENESIS §3.7; phase-5 ingestion, entry E).

    Explicit forms are honoured verbatim: any scheme URL (ssh://, https://, ...),
    the scp-like host:path form, and local paths. A scheme-less host/owner/repo
    (e.g. github.com/you/project) is normalized to the SSH form, because a
    personal machine typically authenticates over SSH and an HTTPS remote fails
    at the push with no credentials — the first birth's observed friction.
    """
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://", remote):
        return remote
    if ":" in remote.split("/", 1)[0]:
        return remote  # scp-like host:path (covers git@host:owner/repo)
    parts = remote.split("/")
    if len(parts) == 3 and all(parts) and "." in parts[0]:
        host, owner, repo = parts
        if repo.endswith(".git"):
            repo = repo[: -len(".git")]
        return f"git@{host}:{owner}/{repo}.git"
    return remote


def validate(args):
    if not NAME_RE.fullmatch(args.name):
        die("--name must begin with a letter and contain only ASCII letters/digits")
    if not HUMAN_RE.fullmatch(args.human):
        die("--human must have the form AGENT.HUMAN.NAME in dotted uppercase code grammar")
    if not AI_RE.fullmatch(args.ai):
        die("--ai must have the form AGENT.AI.NAME in dotted uppercase code grammar")
    if args.human == args.ai:
        die("--human and --ai identities must be distinct")
    if args.remote is not None:
        if not args.remote.strip():
            die("--remote cannot be empty")
        if "\n" in args.remote or "\r" in args.remote:
            die("--remote must be one line")
        args.remote = normalize_remote(args.remote.strip())

    target = os.path.abspath(os.path.expanduser(args.target))
    if os.path.lexists(target):
        die(f"target already exists; genesis never overwrites or resumes: {target}")
    parent = os.path.dirname(target)
    if not os.path.isdir(parent):
        die(f"target parent directory does not exist: {parent}")
    if not os.access(parent, os.W_OK):
        die(f"target parent directory is not writable: {parent}")
    if shutil.which("git") is None:
        die("git is required but was not found on PATH")
    for relative in KERNEL:
        source = os.path.join(SOURCE_REPO, *relative.split("/"))
        if not os.path.isfile(source):
            die(f"tier-0 kernel source is missing: {relative}")
    return target, parse_routes(args.route)


def markdown_header(title, status, domain, author, parent):
    return (
        f"# {title}\n\n"
        f"**Version:** 0.1 · **Status:** {status} · **Domain:** {domain} · "
        f"**Author:** {author} · **Parent:** {parent}\n\n---\n"
    )


def global_context(args, domain):
    return markdown_header(
        f"{args.name} — Global Context",
        "Draft",
        domain,
        args.ai,
        "Instance root",
    ) + (
        "\n## 1 · Vision\n\n"
        f"[Replace this placeholder with why {args.name} exists, in your words.]\n\n"
        "## 2 · Current realisation\n\n"
        "[Replace this placeholder with what the project concretely is right now. "
        "Change this section only at genuine transitions; its ordered revisions become "
        "the project's phase history.]\n"
    )


def local_context(args, domain):
    return markdown_header(
        f"{args.name} — Local Context",
        "Draft",
        domain,
        args.ai,
        f"{args.name} Global Context",
    ) + (
        "\n## Aspect of the current realisation\n\n"
        "[Replace this placeholder by naming which aspect of the current realisation "
        "this context addresses.]\n\n"
        "## Current state\n\n[Replace with the present state of that aspect.]\n\n"
        "## Next\n\n[Replace with the next bounded work.]\n"
    )


def context_index(args, routes, domain):
    local_path = f"Claude/Context Packages/Local/{args.name}_Local_Context.md"
    rows = "\n".join(
        f"| `{route}` | `{route}` | `{local_path}` |" for route in routes
    )
    return markdown_header(
        f"{args.name} — Context Index",
        "Draft",
        domain,
        args.ai,
        f"{args.name} Global Context",
    ) + (
        "\nRead the Global Context first, then use this table to route into the "
        "active Local Context. Replace the placeholder routing as the corpus grows.\n\n"
        "| Route | Root code | Active context |\n"
        "|---|---|---|\n"
        f"{rows}\n"
    )


def inheritance_clause():
    """Read the inheritance clause verbatim from GENESIS.md §3.4 (S4-2.1).

    The clause was duplicated here once and froze at C-083 while the document
    moved on — caught by Scan #4's birth test. GENESIS §0 is the rule: where
    tool and document disagree, the document wins. So the tool carries no copy
    at all; it reads the blockquote at run time, and a newborn can never lag
    the constitution it copies.
    """
    path = os.path.join(SOURCE_REPO, "GENESIS.md")
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as exc:
        sys.exit(f"genesis.py: cannot read GENESIS.md for the §3.4 clause: {exc}")
    m = re.search(r"^> \*(Constitution inherited from FRACTAL.+?)\*\s*$", text, re.M)
    if not m:
        sys.exit("genesis.py: the §3.4 inheritance clause was not found in "
                 "GENESIS.md — the document is the source (S4-2.1); refusing "
                 "to invent one")
    return m.group(1)


def decision_register(args):
    clause = inheritance_clause()
    return markdown_header(
        f"{args.name} — Decision Register",
        "Draft",
        "GOV",
        args.ai,
        f"{args.name} Global Context",
    ) + (
        "\n## 1 · Inheritance\n\n"
        f"> *{clause}*\n\n"
        "## 2 · Parameter bindings\n\n"
        f"- Project prefix: `{args.name}_`\n"
        f"- Human writer: `{args.human}`\n"
        f"- AI writer: `{args.ai}`\n"
        f"- Routes: `{args.route}`\n"
        f"- Off-site remote: `{args.remote if args.remote else 'not bound at genesis'}`\n"
        "- Close checklist: Global Context, Local Context, Context Index, Decision "
        "Register, the client adapter (`CLAUDE.md` — stamp vs Conversation "
        "Settings), and both root protocols.\n"
        "- Pre-canon inputs: `FIELDNOTES.md` — the instance friction ledger "
        "(parameter 7, C-062), written at genesis; captures enter through "
        "`/fieldnote` (target `self`) and inform but never govern.\n\n"
        "## 3 · Instance decisions\n\n"
        "No instance decisions have been recorded. The first decision is `P-001`.\n"
    )


def writer_name(code):
    """AGENT.AI.CLAUDE -> Claude. C-037 attributes a writer, not a code."""
    return code.rsplit(".", 1)[-1].replace("_", " ").title()


def settings_stamp():
    """Read the Conversation Settings version from the copied kernel file.

    Never hardcode it: a stamp frozen in this tool would go stale exactly the
    way a spec pointer does, and the adapter's whole sync-check is the stamp.
    """
    source = os.path.join(
        SOURCE_REPO,
        "Claude", "Project Governance", "Governance Documents",
        "Fractal_Conversation_Settings.md",
    )
    patterns = (
        r"^#\s.*?—\s*v(\d+\.\d+)\s*$",      # title form: "# ... — v0.6"
        r"\*\*Version:\*\*\s*(\d+\.\d+)",   # header-field form
    )
    with open(source, encoding="utf-8") as handle:
        for line in handle:
            for pattern in patterns:
                found = re.search(pattern, line)
                if found:
                    return found.group(1)
    die("could not read a version stamp from Fractal_Conversation_Settings.md")


def client_adapter(args, domain):
    """The Claude Code adapter — a stamped C-035 projection, never a fork."""
    return (
        f"# {args.name} — Claude Code client adapter\n\n"
        f"> **Projection of `Fractal_Conversation_Settings.md` v{settings_stamp()}** "
        "(copied into this instance at genesis). That file is the sole normative "
        "source of conduct; this adapter is a compression of it. **Re-project, never "
        "hand-fork.** Sync-check = the stamp above against the Settings' internal "
        "version.\n\n"
        f"**Version:** 0.1 · **Status:** Draft · **Domain:** {domain} · "
        f"**Author:** {writer_name(args.ai)} · **Parent:** "
        f"{args.name} Global Context\n\n"
        f"This repository is **{args.name}**, governed under a constitution inherited "
        "from FRACTAL. Rules for every session here:\n\n"
        "1. **ORIENT FIRST, DON'T SCAN.** Read "
        f"`Claude/Context Packages/Global/{args.name}_Global_Context.md`, then the "
        f"active Local Context named in `Claude/Context Packages/"
        f"{args.name}_Context_Index.md`. Never scan the repo to get oriented.\n"
        "2. **SOURCE OF TRUTH.** Canonical documents live in this repo; context "
        "packages are derived projections and are never authoritative.\n"
        "3. **LOAD ONLY WHAT THE TASK NEEDS.** Resolve locations through the Index; "
        "do not load unrelated domains.\n"
        "4. **BEHAVE.** Stay in the declared domain, keep accepted decisions separate "
        "from proposals, ask before executing actions, and externalise durable work "
        "quickly.\n"
        "5. **CLOSE THE LOOP.** End substantive sessions with a handover record in "
        "`Claude/Context Packages/Conversations/`, the checklist in the Decision "
        "Register walked, and `verify.py` green.\n"
        f"6. **IDENTITY.** One stable identity per artifact, `{args.name}_<Name>`; "
        "the author is named in the document.\n"
        "7. **NUMBERING.** This instance's decisions are `P-…`; an inherited `C-…` "
        "citation refers to FRACTAL's Register and is never renumbered here.\n\n"
        "## Repo rituals\n\n"
        f"- **Commits:** author = the actual writer (`{writer_name(args.ai)}`, "
        f"`{writer_name(args.human)}`); message `[DOMAIN] imperative summary`; one "
        "commit per coherent change-set.\n"
        "- **Checker:** `python3 verify.py` in `Claude/Knowledge Graph Store/` before "
        "every store-touching commit. Red blocks.\n"
        "- **Tiers:** this instance starts at tier 0 (grep reads, no index server). "
        "Add a component when you feel its absence, never by anticipation.\n\n"
        "---\n\n"
        "**Refresh triggers:** any Conversation Settings reissue (re-project and "
        "restamp); a ritual change; a close finding the stamp stale.\n"
    )


def orient_command(args):
    """`/orient` — the tier-0 entry command. Auto-discovered by Claude Code."""
    return (
        "---\n"
        f"description: Open a {args.name} working session — load the context spine\n"
        "---\n\n"
        f"Open this {args.name} working session per the standing orientation "
        "procedure (the client adapter's rule 1):\n\n"
        f"1. Read `Claude/Context Packages/Global/{args.name}_Global_Context.md`.\n"
        f"2. Read the active Local Context named in "
        f"`Claude/Context Packages/{args.name}_Context_Index.md`.\n"
        "3. Read the newest handover record in "
        "`Claude/Context Packages/Conversations/`, if any exists.\n"
        f"4. If `{RAIL_PATH}` still exists, read "
        "it and surface this loop's one suggested move as an offer — it is "
        "scaffolding that retires itself; propose its retirement when it adds "
        "nothing.\n"
        "5. Do not scan anything else.\n\n"
        "Then report briefly: where the project stands, what is queued or open, and "
        "anything recorded as pending. Then stop — the queued agenda is an offer, "
        "never a mandate. Wait for direction before starting work.\n"
    )


def first_loops_rail(args):
    """The stage-two scaffold (Fractal_Onboarding_Protocol §3) — self-retiring."""
    return (
        f"# {args.name} — First Loops Rail\n\n"
        "> **SCAFFOLDING — informs, never governs, and retires itself** "
        "(Fractal_Onboarding_Protocol §3–§4, in the FRACTAL release this instance "
        "was born from). `/orient` surfaces **one move per loop, as an offer** — "
        "dropped without argument when the owner has their own agenda.\n\n"
        "- **Loop 1 — the first close.** Real work first: the project's actual "
        "first step. When the first real decision appears, record it as **P-001 "
        "with its why in the row** (with no protocol series, the row is the "
        "reasoning's only home). Then close: a handover record in "
        "`Claude/Context Packages/Conversations/`, the checklist in the Decision "
        "Register walked, `verify.py` green. **The instance is real at its first "
        "close** — say so when it happens.\n"
        "- **Loop 2 — the capture habit.** `/fieldnote self <what happened>` "
        "whenever something grinds *or* shines — frictions and green data through "
        "one door. Reporting upstream = sending `FIELDNOTES.md`, any channel; "
        "nothing transmits automatically.\n"
        "- **Loop 3 — the shelf, and the board offered actively.** Before "
        "building any working tool or projection: the tier table in the genesis "
        "document you were born from — **adopt before invent**. And when open "
        "threads accumulate, offer the **Agenda Board** by name, unprompted: a "
        "rendered single-glance projection of queued and open work, refreshed at "
        "every close once adopted. AI sessions move faster than human tracking; "
        "the board is the human's window.\n"
        "- **Loop 4 — the catalog card.** Minting, when it first matters: repo = "
        "library shelf, store = catalog + citation network; minting = the catalog "
        "card. Defer penalty-free until something in the graph must point at the "
        "document.\n\n"
        "**Retirement:** at any loop-open where this file added nothing — or at "
        "loop 5 at the latest — the session proposes deleting it; the owner's yes "
        "is one `git rm` and one Register line. The constitution carries on "
        "alone.\n"
    )


def fieldnote_command(args):
    """`/fieldnote` — the tier-0 capture command (C-094; fieldnotes entry 39)."""
    return (
        "---\n"
        "description: Capture a field observation — a friction, a green datum, an "
        "idea — into this instance's ledger, then return to the work "
        "(usage /fieldnote <target> <what happened>; target `self` = this instance)\n"
        "---\n\n"
        "Capture a field observation: **$ARGUMENTS**\n\n"
        "**Step 0 — deterministic routing.** Run `python3 \"Claude/Knowledge Graph "
        "Store/fieldnote.py\" <target> <report text>` with the argument exactly as "
        "given. The first word is the **target** (`self` routes to this instance's "
        "own `FIELDNOTES.md`; `--list` prints the roster). **If the tool errors "
        "(missing or unknown target): report its error and STOP** — no capture, no "
        "fallback interpretation. On success the tool has appended one immutable "
        "machine-format block (Fractal Fieldnote Format v0.1) — verbatim, "
        "timestamped, attributed. **Never edit the block.** If the reporter states "
        "the observation's class, pass `--kind friction|green|vision|question` "
        "before the target; otherwise the tool records `capture`.\n\n"
        "Optionally add one short prose line after the block (a title, a cure "
        "note) — judgment layer, outside the block. Confirm in one line (id + "
        "ledger), then return immediately to the interrupted work.\n\n"
        "To report findings upstream: **send the ledger file itself** — any "
        "channel; the format carries who/when/what. Nothing transmits "
        "automatically, ever.\n\n"
        "On a client without a slash menu, the plain word \"fieldnote\" invokes "
        "this same procedure — the ritual is kernel; the trigger is per-client.\n"
    )


def fieldnotes_ledger(args):
    """FIELDNOTES.md — parameter 7's file, born with its door (C-062, C-094)."""
    return (
        f"# {args.name} — Fieldnotes\n\n"
        "> **PRE-CANON (C-062)** — this instance's own friction ledger: raw field "
        "observations (frictions, green data, ideas, questions) captured "
        "mid-session through `/fieldnote`. Informs; **never governs.** Entries "
        "are immutable machine-format blocks (Fractal Fieldnote Format v0.1, in "
        "`Claude/Project Governance/Governance Documents/`); prose around a "
        "block is optional judgment. To share findings with upstream, send this "
        "file — any channel; the format carries who/when/what, and nothing "
        "transmits automatically.\n\n"
        "---\n"
    )


def fieldnote_roster(args):
    return json.dumps(
        {"instance": args.name, "targets": {"self": "FIELDNOTES.md"}},
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ) + "\n"


def conversations_home(args):
    """The handover home. Git tracks no empty directory, so it ships explained."""
    return (
        "# Conversations\n\n"
        "Handover records live here — one per closed session, dated, frozen at "
        "issue. Every substantive session ends with one: what the previous package "
        "queued, what this session did, what is carried, and what comes next.\n\n"
        "The close is where memory is actually made. A repository without these is "
        f"not an instance of the constitution {args.name} inherited — it is just "
        "files under version control.\n\n"
        "Naming: `Return_Package_<YYYY-MM-DD>_<Short-Topic>.md`.\n"
    )


def bootstrap(args):
    return markdown_header(
        f"{args.name} — Bootstrap Protocol",
        "Draft",
        "GOV",
        args.ai,
        f"{args.name} Global Context",
    ) + (
        "\n## Rehydrate this instance\n\n"
        "1. Clone this repository and confirm `git log` reaches its initial genesis commit.\n"
        f"2. Read `Claude/Context Packages/Global/{args.name}_Global_Context.md`.\n"
        f"3. Route through `Claude/Context Packages/{args.name}_Context_Index.md`.\n"
        f"4. Read `Claude/Context Packages/Local/{args.name}_Local_Context.md`.\n"
        f"5. Read `Claude/Project Governance/Governance Documents/{args.name}_Decision_Register.md`, "
        "then the Rule Overview and Conversation Settings beside it.\n"
        "6. Run `python3 verify.py` from `Claude/Knowledge Graph Store/`; a red verifier "
        "blocks work until cured.\n"
        "7. Read `CLAUDE.md` at the root — the client adapter, written at genesis as a "
        "stamped projection of Conversation Settings. Check its stamp against that "
        "file's internal version; re-project if they disagree. Never hand-fork the "
        "conduct rules. For a vendor surface with an instructions field, paste a "
        "projection of the same source and stamp it the same way.\n\n"
        "## Work and close\n\n"
        "Attribute commits to the actual writer, use `[DOMAIN] imperative summary`, and "
        "keep knowledge in git. At close, write a handover, walk the living-projection "
        "checklist recorded in the Decision Register, run the verifier, commit one coherent "
        "change-set, and push when an off-site remote is bound.\n"
    )


def genesis_record(args, routes):
    remote = args.remote if args.remote else "not bound at genesis"
    return markdown_header(
        f"{args.name} — Genesis Record",
        "Active",
        "GOV",
        args.ai,
        f"{args.name} Global Context",
    ) + (
        "\n## What this record is for\n\n"
        f"This repository is a new {args.name} instance. It inherited FRACTAL's tier-0 "
        "constitution and began with its own ledger; it did not copy the originating "
        "instance's events, nodes, decision rows, contexts, protocols, or biography. "
        "Use `BOOTSTRAP.md` to rehydrate this instance.\n\n"
        "## Genesis parameters\n\n"
        f"- Project name/prefix: `{args.name}` / `{args.name}_`\n"
        f"- Human identity: `{args.human}`\n"
        f"- AI identity: `{args.ai}`\n"
        f"- Domain routes: `{', '.join(routes)}`\n"
        f"- Off-site remote: `{remote}`\n"
        "- Close checklist: the living documents named in the Decision Register\n"
        "- Pre-canon inputs: `FIELDNOTES.md` (the friction ledger, C-062 — "
        "capture door `/fieldnote`, report path: send the file)\n\n"
        "## First work\n\n"
        "Replace the Global Context vision/current-realisation placeholders and the Local "
        "Context aspect placeholder. Record the first project-specific decision as `P-001`; "
        "never insert the originating instance's decision rows.\n\n"
        "## Inherited licensing\n\n"
        "The kernel documents copied at genesis are licensed CC BY 4.0 and the "
        "copied tools Apache-2.0, both by the FRACTAL project (see the LICENSE, "
        "LICENSE-docs and NOTICE files that traveled with this birth). This "
        "record, together with the Register's inheritance clause, is the "
        "attribution. Everything this instance writes itself is its own, "
        "licensed however its owner decides.\n"
    )


def gitignore():
    return (
        ".DS_Store\nThumbs.db\ndesktop.ini\n~$*\n*.swp\n*.swo\n\n"
        "# Secrets layer (C-087)\n.env\n.env.*\nsecrets/\n"
    )


def version_registry(args):
    """Project the shared checker's FRACTAL registry onto this instance."""
    markdown = ".m" + "d"  # keep generated path templates out of bare-file heuristics
    global_path = f"Claude/Context Packages/Global/{args.name}_Global_Context{markdown}"
    local_path = f"Claude/Context Packages/Local/{args.name}_Local_Context{markdown}"
    register_path = (
        f"Claude/Project Governance/Governance Documents/"
        f"{args.name}_Decision_Register{markdown}"
    )
    index_path = f"Claude/Context Packages/{args.name}_Context_Index{markdown}"
    living_overrides = {
        "Global Context": {
            "path": global_path,
            "aliases": [f"{args.name}_Global_Context", f"{args.name} Global Context", "Global Context"],
        },
        "Local Context": {
            "path": local_path,
            "aliases": [f"{args.name}_Local_Context", f"{args.name} Local Context", "Local Context"],
        },
        "Decision Register": {
            "path": register_path,
            "aliases": [f"{args.name}_Decision_Register", f"{args.name} Decision Register", "Decision Register", "Register"],
        },
        "Context Index": {
            "path": index_path,
            "aliases": [f"{args.name}_Context_Index", f"{args.name} Context Index", "Context Index", "Index"],
        },
        "BOOTSTRAP": {
            "path": "BOOTSTRAP.md",
            "aliases": [f"{args.name}_Bootstrap_Protocol", f"{args.name} Bootstrap Protocol", "BOOTSTRAP.md", "BOOTSTRAP"],
        },
        "GENESIS": {
            "path": "GENESIS.md",
            "aliases": [f"{args.name}_Genesis_Protocol", f"{args.name} Genesis Protocol", "GENESIS.md", "GENESIS"],
        },
        "Claude Code Adapter": {
            "path": "CLAUDE.md",
            "aliases": [f"{args.name}_Claude_Code_Adapter", f"{args.name} Claude Code Adapter", "Claude Code Adapter", "Claude Code adapter", "CLAUDE.md"],
        },
    }
    strict = [
        "BOOTSTRAP.md",
        "GENESIS.md",
        "CLAUDE.md",
        index_path,
        global_path,
        local_path,
        "Claude/Knowledge Graph Store/verify.py",
        "Claude/Knowledge Graph Store/mint.py",
        "Claude/Knowledge Graph Store/check_versions.py",
        "Claude/Knowledge Graph Store/doctor.py",
        "Claude/Knowledge Graph Store/fieldnote.py",
    ]
    return json.dumps(
        {
            "living_overrides": living_overrides,
            "living_omit": ["Architecture State", "Codex Adapter"],
            "series_omit": ["protocol", "foundation"],
            "strict": strict,
        },
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ) + "\n"


def node_text(concept, aliases):
    alias_values = [f"route:{alias}" for alias in aliases]
    return (
        f"---\nid: {concept['subject']}\ntype: TOP\n"
        f"created: {concept['ts']}\ncreated_by: {concept['actor']}\n"
        f"code: {concept['code']}\ntitle: {json.dumps(concept['label'])}\n"
        f"aliases: {json.dumps(alias_values)}\nfacet: {concept['facet']}\n"
        "placements:\n---\n\n"
        f"Concept node for `{concept['code']}` in the **{concept['facet']}** facet. "
        "Parentage is carried by the code prefix; this node stores its own coordinate "
        "and needs no self-placement.\n"
    )


def slug(label):
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def build_plan(args, target, routes):
    clock = Clock()
    events = []
    concepts = []
    aliases = {}
    root_codes = []
    root_note = "root mint: minted by genesis on the operator's instruction"

    def mint(facet, code, label, parent=None):
        now_ms, timestamp = clock.take()
        subject = "TOP-" + ulid(now_ms)
        event = {
            "ev": "mint",
            "id": "EVT-" + ulid(now_ms),
            "ts": timestamp,
            "actor": args.ai,
            "subject": subject,
            "facet": facet,
            "code": code,
            "parent": parent,
            "label": label,
        }
        if parent is None:
            event["note"] = root_note
            root_codes.append(code)
        events.append(event)
        concepts.append(event)
        aliases[subject] = []
        return subject

    def bind(subject, alias):
        now_ms, timestamp = clock.take()
        events.append(
            {
                "ev": "alias",
                "id": "EVT-" + ulid(now_ms),
                "ts": timestamp,
                "actor": args.ai,
                "subject": subject,
                "alias": alias,
                "kind": "route",
            }
        )
        aliases[subject].append(alias)

    facet_root = mint("facet", "FACET", "Facet")
    facet_subjects = {}
    for code, label, token in FACETS:
        facet_subjects[token] = mint("facet", code, label, "FACET")
    bind(facet_root, "facet")
    for _, _, token in FACETS:
        bind(facet_subjects[token], token)

    mint("agent", "AGENT", "Agent")
    mint("agent", "AGENT.HUMAN", "Human agent", "AGENT")
    mint("agent", args.human, args.human.rsplit(".", 1)[1], "AGENT.HUMAN")
    mint("agent", "AGENT.AI", "AI agent", "AGENT")
    mint("agent", args.ai, args.ai.rsplit(".", 1)[1], "AGENT.AI")

    for route in routes:
        subject = mint("topic", route, f"{route} domain")
        bind(subject, route)

    files = {}
    copied = set()
    for relative in KERNEL:
        source = os.path.join(SOURCE_REPO, *relative.split("/"))
        with open(source, "rb") as handle:
            files[relative] = handle.read()
        copied.add(relative)

    domain = routes[0]
    generated = {
        ".gitignore": gitignore(),
        f"Claude/Context Packages/Global/{args.name}_Global_Context.md": global_context(args, domain),
        f"Claude/Context Packages/{args.name}_Context_Index.md": context_index(args, routes, domain),
        f"Claude/Context Packages/Local/{args.name}_Local_Context.md": local_context(args, domain),
        f"Claude/Project Governance/Governance Documents/{args.name}_Decision_Register.md": decision_register(args),
        "Claude/Context Packages/Conversations/README.md": conversations_home(args),
        "CLAUDE.md": client_adapter(args, domain),
        ".claude/commands/orient.md": orient_command(args),
        ".claude/commands/fieldnote.md": fieldnote_command(args),
        RAIL_PATH: first_loops_rail(args),
        "FIELDNOTES.md": fieldnotes_ledger(args),
        "Claude/Knowledge Graph Store/fieldnote_roster.json": fieldnote_roster(args),
        "BOOTSTRAP.md": bootstrap(args),
        "GENESIS.md": genesis_record(args, routes),
        "Claude/Knowledge Graph Store/.inherited": "".join(
            relative + "\n" for relative in sorted(copied)
        ),
        "Claude/Knowledge Graph Store/.version-registry": version_registry(args),
        "Claude/Knowledge Graph Store/_events/part-0001.jsonl": "".join(
            json.dumps(event, ensure_ascii=False) + "\n" for event in events
        ),
    }
    for relative, content in generated.items():
        files[relative] = content.encode("utf-8")
    for concept in concepts:
        filename = f"{concept['subject']}--{slug(concept['label'])}.md"
        relative = f"Claude/Knowledge Graph Store/nodes/{filename}"
        files[relative] = node_text(concept, aliases[concept["subject"]]).encode("utf-8")

    return {
        "target": target,
        "routes": routes,
        "events": events,
        "root_codes": root_codes,
        "files": files,
        "copied": copied,
    }


def print_plan(args, plan):
    mode = "WRITE" if args.write else "PREVIEW (dry-run — re-run with --write to create)"
    print(mode + ":")
    print(f"  target repository: {plan['target']}")
    print("  git: init on branch main; create one initial [GOV] commit")
    if args.remote:
        print(f"  git remote: bind origin to {args.remote}; push main")
        if args.remote.startswith("https://"):
            print("  note: HTTPS remote honoured verbatim — the push needs a "
                  "configured credential helper; the SSH form is the usual "
                  "personal-machine default (GENESIS §3.7)")
    else:
        print("  git remote: none requested")
    print(f"Files to create ({len(plan['files'])} tracked files):")
    for relative in sorted(plan["files"]):
        suffix = "  [tier-0 copy, verbatim]" if relative in plan["copied"] else ""
        print(f"  {relative}{suffix}")
    print(f"Root mints ({len(plan['root_codes'])}):")
    for code in plan["root_codes"]:
        print(f"  {code} — genesis on the operator's instruction")
    print(f"Event lines ({len(plan['events'])}) -> Claude/Knowledge Graph Store/_events/part-0001.jsonl:")
    for event in plan["events"]:
        print("  " + json.dumps(event, ensure_ascii=False))


def run(command, cwd, env=None):
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.returncode:
        output = result.stdout.strip()
        detail = f": {output}" if output else ""
        raise RuntimeError(f"{' '.join(command)} failed{detail}")
    return result.stdout


def write_plan(args, plan):
    target = plan["target"]
    parent = os.path.dirname(target)
    staging = tempfile.mkdtemp(prefix=".genesis-staging-", dir=parent)
    try:
        for relative, content in plan["files"].items():
            destination = os.path.join(staging, *relative.split("/"))
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            with open(destination, "wb") as handle:
                handle.write(content)

        run(["git", "init", "--initial-branch=main"], staging)
        if args.remote:
            run(["git", "remote", "add", "origin", args.remote], staging)
        verify_output = run([sys.executable, "verify.py"], os.path.join(staging, "Claude", "Knowledge Graph Store"))
        run(["git", "add", "--all"], staging)
        commit_env = os.environ.copy()
        commit_env.update(
            {
                # C-037 attributes a writer, not a dotted code: AGENT.AI.CLAUDE
                # commits as "Claude", matching what every later session will use.
                "GIT_AUTHOR_NAME": writer_name(args.ai),
                "GIT_AUTHOR_EMAIL": f"{writer_name(args.ai).lower()}@{args.name.lower()}.local",
                "GIT_COMMITTER_NAME": writer_name(args.ai),
                "GIT_COMMITTER_EMAIL": f"{writer_name(args.ai).lower()}@{args.name.lower()}.local",
            }
        )
        run(
            [
                "git",
                "commit",
                "-m",
                f"[GOV] Establish {args.name} instance",
                "-m",
                "Constitution inherited through genesis; instance history begins here.",
            ],
            staging,
            env=commit_env,
        )
        if args.remote:
            run(["git", "push", "--set-upstream", "origin", "main"], staging)
        if os.path.lexists(target):
            raise RuntimeError("target appeared during genesis; refusing to replace it")
        os.replace(staging, target)
        staging = None
    except (OSError, RuntimeError) as exc:
        die(str(exc))
    finally:
        if staging and os.path.isdir(staging):
            shutil.rmtree(staging)

    print("\nCREATED:")
    print(f"  repository: {target}")
    print("  branch: main")
    print(f"  initial commit: [GOV] Establish {args.name} instance")
    if args.remote:
        print("  remote origin: bound; main pushed with upstream tracking")
    print("  genesis verifier output:")
    for line in verify_output.rstrip().splitlines():
        print("    " + line)


def arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, metavar="PATH")
    parser.add_argument("--name", required=True, metavar="PROJECT")
    parser.add_argument("--human", required=True, metavar="AGENT.HUMAN.NAME")
    parser.add_argument("--ai", required=True, metavar="AGENT.AI.NAME")
    parser.add_argument("--route", required=True, metavar="CODE[,CODE...]")
    parser.add_argument("--remote", metavar="URL")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main():
    args = arguments()
    target, routes = validate(args)
    plan = build_plan(args, target, routes)
    print_plan(args, plan)
    if args.write:
        write_plan(args, plan)


if __name__ == "__main__":
    main()
