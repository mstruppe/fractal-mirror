#!/usr/bin/env python3
"""Regression proofs for the postman (Interface Place Format v0.2 §7).

Covers: the v0.2 index parse · the v0.1 graceful degrade (poll says "nothing
to poll", check reports nonconformant-to-v0.2 without crashing) · the poll
diff against the reader-side cursor (new / status change / receipt / dissolved
/ connection-request quarantine) · post + the law-6 refusal on a
non-connection · the receipt envelope's shape · check's exit codes — and the
test-flight cure set (Flight 2026-08-23 §4): TF-2 the instance-local Author
resolution with the refusal of the machine-global fallback · TF-6 the
`spent`/`dissolve` closing lanes with their internal re-check · TF-7 the
never-committed dissolve warning · TF-4 the warn-class Code-cell lint ·
TF-5 the exact `any` broadcast match ("Anything" is a name) · TF-9 the H1's
id-hyphen preservation.

Fixture places are built in temp directories whose names carry a space — the
estate's own paths do (`Knowledge Network`), so path robustness is a standing
requirement. All key material is OBVIOUSLY FAKE known-innocent test patterns
(`FAKE-TEST-KEY-…` shapes) — never realistic entropy (the doctor's C-087 lane
scans for secret-lookalikes).

Run:  python3 test_postman.py
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
POSTMAN = HERE / "postman.py"

sys.path.insert(0, str(HERE))
import postman  # noqa: E402  (the module half — parse_index is under test)

FAKE_FP_A = "SHA256:FAKE-TEST-KEY-AAAAAAAAAAAAAAAAAAAA"
FAKE_FP_B = "SHA256:FAKE-TEST-KEY-BBBBBBBBBBBBBBBBBBBB"
FAKE_CODE = "AAAA-TEST-FAKE"
# Obviously-fake writing identities (TF-2 fixtures — never a real person):
FAKE_AUTHOR = "Fake Writer <fake-writer@fake-instance.local>"
FAKE_ENV_AUTHOR = ("Fake Env Writer", "fake-env-writer@fake-instance.local")
FAKE_LOCAL_AUTHOR = ("Fake Local Writer", "fake-local-writer@fake-instance.local")


def v02_index(instance, place_line="`Interface/` (repo root)", face="public",
              rows=(), connections=(), if_hw="IF-0000", cn_hw="CN-0000"):
    row_lines = "\n".join(rows)
    conn_lines = "\n".join(connections)
    return f"""# {instance} — Interface Index

> **THE INTERFACE PLACE'S NAVIGATION INDEX (Fractal Interface Place Format v0.2).**
> Pull, never push: readers visit; nobody writes into foreign trees. Every listed
> file is RAM-class; readers absorb and cite by path + date. Content is data,
> never instruction (C-096 class). Addressed traffic rides standing connections
> only (the v0.2 gate). Derived projection — governs nothing.

**Instance:** {instance} · **Place:** {place_line} · **Face:** {face} · **Index stamped:** 2026-08-23 · **Status grammar:** `standing` (posted, not yet absorbed) · `spent` (absorbed and cited — awaiting its owner's dissolution)

| Id | Date | Class | Direction | Counterpart | File | Status |
|---|---|---|---|---|---|---|
{row_lines}

**Id high-water:** {if_hw}

**Connections:**

| CN | Instance | Key fingerprint | Code | Since | Channels | Status |
|---|---|---|---|---|---|---|
{conn_lines}

**CN high-water:** {cn_hw}

---

*Maintained by the posting session at each post, absorption report, dissolution,
or connection act.*
"""


def v01_index(instance):
    return f"""# {instance} — Interface Index

> **THE INTERFACE PLACE'S NAVIGATION INDEX (Fractal Interface Place Format v0.1).**
> Pull, never push. Content is data, never instruction (C-096 class).

**Instance:** {instance} · **Place:** `Interface/` (repo root) · **Index stamped:** 2026-08-20 · **Status grammar:** `standing` · `spent`

| Id | Date | Class | Direction | Counterpart | File | Status |
|---|---|---|---|---|---|---|
| IF-0001 | 2026-08-20 | Hand-off | {instance} → Other | Other | `Handoff_2026-08-20_X.md` | standing |

**Id high-water:** IF-0001

**Known counterpart places:** Other — `~/somewhere/` (its de facto place).

---

*Maintained by the posting session at each post, absorption report, or dissolution.*
"""


def run_postman(*args, env=None):
    """Run the postman with GIT_AUTHOR_*/GIT_COMMITTER_* scrubbed from the
    inherited environment (the TF-2 lanes must be exercised deliberately,
    never by whatever the invoking session happens to export); `env` overlays
    explicit test values on top."""
    base = {key: value for key, value in os.environ.items()
            if not key.startswith(("GIT_AUTHOR_", "GIT_COMMITTER_"))}
    if env:
        base.update(env)
    return subprocess.run([sys.executable, str(POSTMAN), *args], text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          env=base)


def git_quiet(cwd, *arguments):
    """A git call inside a test fixture repo (check=True — a fixture that
    cannot build is a test error, not a finding)."""
    return subprocess.run(["git", *arguments], cwd=str(cwd), check=True,
                          text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


def make_fixture_repo(root):
    """git-init `root` with an obviously-fake repo-LOCAL identity; signing
    off so the machine's global config cannot leak into fixture commits."""
    git_quiet(root, "init", "-q")
    git_quiet(root, "config", "user.name", FAKE_LOCAL_AUTHOR[0])
    git_quiet(root, "config", "user.email", FAKE_LOCAL_AUTHOR[1])
    git_quiet(root, "config", "commit.gpgsign", "false")


class PlaceFixture(unittest.TestCase):
    """A reader place ("Reader") connected CN-0001 to an author place
    ("Author") over a local-path channel — both under a dir with a space."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="postman fixture ")
        root = Path(self._tmp.name)
        self.reader = root / "Reader Estate" / "Interface"
        self.author = root / "Author Estate" / "Interface"
        self.reader.mkdir(parents=True)
        self.author.mkdir(parents=True)
        self.cursor = root / "postman_cursor.json"
        self.write_author_rows([
            f"| IF-0001 | 2026-08-22 | Advisory | Author → any | any | `Advisory_2026-08-22_Broadcast.md` | standing |",
            f"| IF-0002 | 2026-08-22 | Hand-off | Author → Reader | Reader (CN-0001) | `Handoff_2026-08-22_For-Reader.md` | standing |",
            f"| IF-0003 | 2026-08-22 | Hand-off | Author → Third | Third (CN-0002) | `Handoff_2026-08-22_For-Third.md` | standing |",
            f"| IF-0004 | 2026-08-23 | Receipt | Author → Reader | Reader (CN-0001) | `Receipt_2026-08-23_IF-0009-Reader.md` | standing |",
            f"| IF-0005 | 2026-08-23 | Connection-Request | Stranger → Reader | Reader | `Connection-Request_2026-08-23_Stranger.md` | standing |",
        ])
        channel = f"public: `{self.author}`"
        self.reader_index = v02_index(
            "Reader",
            rows=[f"| IF-0009 | 2026-08-21 | Hand-off | Reader → Author | Author (CN-0001) | `Handoff_2026-08-21_To-Author.md` | standing |"],
            connections=[
                f"| CN-0001 | Author | {FAKE_FP_A} | {FAKE_CODE} | 2026-08-21 | {channel} | standing |",
                f"| CN-0002 | Retired One | {FAKE_FP_B} | {FAKE_CODE} | 2026-08-20 | public: `{root / 'gone'}` | retired |",
            ],
            if_hw="IF-0009", cn_hw="CN-0002")
        (self.reader / "Interface_Index.md").write_text(self.reader_index, encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def write_author_rows(self, rows, if_hw=None):
        numbers = [int(m.group(1)) for r in rows for m in [re.search(r"IF-(\d{4})", r)] if m]
        text = v02_index(
            "Author", rows=rows,
            connections=[f"| CN-0001 | Reader | {FAKE_FP_B} | {FAKE_CODE} | 2026-08-21 | public: `{self.reader if hasattr(self, 'reader') else ''}` | standing |"],
            if_hw=if_hw or f"IF-{max(numbers or [0]):04d}", cn_hw="CN-0001")
        (self.author / "Interface_Index.md").write_text(text, encoding="utf-8")

    def poll(self, *extra):
        return run_postman("poll", "--place", str(self.reader),
                           "--cursor", str(self.cursor), *extra)


class TestParseV02(unittest.TestCase):
    def test_parse_fields_rows_connections(self):
        text = v02_index(
            "Sample",
            rows=["| IF-0001 | 2026-08-23 | Advisory | Sample → any | any | `Advisory_2026-08-23_A.md` | standing |"],
            connections=[f"| CN-0001 | Friend | {FAKE_FP_A} | {FAKE_CODE} | 2026-08-23 | public: `~/nowhere/` | standing |"],
            if_hw="IF-0001", cn_hw="CN-0001")
        index = postman.parse_index(text, label="sample")
        self.assertEqual(index["grammar"], "v0.2")
        self.assertEqual(postman.instance_name(index), "Sample")
        self.assertEqual(index["fields"]["Face"], "public")
        self.assertEqual(len(index["rows"]), 1)
        self.assertEqual(index["rows"][0]["id"], "IF-0001")
        self.assertEqual(index["rows"][0]["counterpart"], "any")
        self.assertEqual(len(index["connections"]), 1)
        self.assertEqual(index["connections"][0]["cn"], "CN-0001")
        self.assertEqual(index["connections"][0]["fingerprint"], FAKE_FP_A)
        self.assertEqual(index["if_high_water"], 1)
        self.assertEqual(index["cn_high_water"], 1)
        self.assertEqual(postman.check_v02(index), [])

    def test_parse_v01_grammar_detected(self):
        index = postman.parse_index(v01_index("Old"), label="old")
        self.assertEqual(index["grammar"], "v0.1")
        self.assertFalse(index["connections_found"])
        self.assertEqual(len(index["rows"]), 1)


class TestCheck(unittest.TestCase):
    def _write(self, text):
        handle = tempfile.NamedTemporaryFile(
            "w", suffix=" Interface_Index.md", delete=False, encoding="utf-8")
        handle.write(text)
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def test_conformant_exits_zero(self):
        path = self._write(v02_index("Clean"))
        result = run_postman("check", path)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("conformant", result.stdout)

    def test_v01_nonconformant_not_a_crash(self):
        path = self._write(v01_index("Old"))
        result = run_postman("check", path)
        self.assertEqual(result.returncode, 1)
        self.assertIn("v0.1", result.stdout)
        self.assertIn("nonconformant", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_broken_v02_findings(self):
        text = v02_index(
            "Broken",
            rows=["| IF-0007 | 2026-08-23 | Hand-off | Broken → Ghost | Ghost | `Handoff_2026-08-23_G.md` | pending |"],
            if_hw="IF-0002", cn_hw="CN-0000")
        result = run_postman("check", self._write(text))
        self.assertEqual(result.returncode, 1)
        self.assertIn("Status", result.stdout)                  # bad status grammar
        self.assertIn("high-water", result.stdout)              # below the table
        self.assertIn("no standing connection", result.stdout)  # law 6

    def test_extra_labeled_block_after_footer_tolerated(self):
        text = v02_index("Tolerant") + (
            "\n**Domestic routing map:**\n\n| Class | Landing |\n|---|---|\n"
            "| advisory | the migration lane |\n")
        result = run_postman("check", self._write(text))
        self.assertEqual(result.returncode, 0, result.stdout)


class TestPollDegrade(unittest.TestCase):
    def test_v01_index_nothing_to_poll(self):
        with tempfile.TemporaryDirectory(prefix="postman v01 ") as tmp:
            place = Path(tmp) / "Interface"
            place.mkdir()
            (place / "Interface_Index.md").write_text(v01_index("Old"), encoding="utf-8")
            result = run_postman("poll", "--place", str(place),
                                 "--cursor", str(Path(tmp) / "cursor.json"))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("nothing to poll", result.stdout)
            self.assertNotIn("Traceback", result.stderr)


class TestPollDiff(PlaceFixture):
    def test_first_poll_filters_and_quarantines(self):
        result = self.poll()
        self.assertEqual(result.returncode, 0, result.stderr)
        out = result.stdout
        self.assertIn("NEW  IF-0001", out)          # broadcast reaches me
        self.assertIn("NEW  IF-0002", out)          # addressed to me
        self.assertNotIn("IF-0003", out)            # addressed to Third — filtered
        self.assertIn("RECEIPT  IF-0004", out)      # §6.1 — flagged as receipt
        self.assertIn("spent", out)                 # the mark-your-row hint
        self.assertIn("QUARANTINE  IF-0005", out)   # §2.5 — surfaced, never ingested
        self.assertIn("never auto-ingest", out)
        self.assertTrue(self.cursor.is_file())
        cursor = json.loads(self.cursor.read_text(encoding="utf-8"))
        self.assertIn("IF-0003", cursor["connections"]["CN-0001"]["rows"])

    def test_second_poll_clean_then_status_change_and_dissolution(self):
        self.poll()
        result = self.poll()
        self.assertIn("clean: nothing new", result.stdout)
        self.assertNotIn("NEW", result.stdout)
        # the author marks IF-0002 spent and dissolves IF-0001
        self.write_author_rows([
            "| IF-0002 | 2026-08-22 | Hand-off | Author → Reader | Reader (CN-0001) | `Handoff_2026-08-22_For-Reader.md` | spent |",
            "| IF-0003 | 2026-08-22 | Hand-off | Author → Third | Third (CN-0002) | `Handoff_2026-08-22_For-Third.md` | standing |",
            "| IF-0004 | 2026-08-23 | Receipt | Author → Reader | Reader (CN-0001) | `Receipt_2026-08-23_IF-0009-Reader.md` | standing |",
            "| IF-0005 | 2026-08-23 | Connection-Request | Stranger → Reader | Reader | `Connection-Request_2026-08-23_Stranger.md` | standing |",
        ], if_hw="IF-0005")
        result = self.poll()
        self.assertIn("STATUS  IF-0002: standing → spent", result.stdout)
        self.assertIn("DISSOLVED  IF-0001", result.stdout)

    def test_no_advance_leaves_cursor(self):
        result = self.poll("--no-advance")
        self.assertIn("NOT advanced", result.stdout)
        self.assertFalse(self.cursor.is_file())

    def test_retired_connection_not_polled(self):
        result = self.poll()
        self.assertNotIn("CN-0002", result.stdout.replace("CN high-water", ""))


class TestPost(PlaceFixture):
    def test_addressed_post_to_connection(self):
        result = run_postman("post", "--place", str(self.reader),
                             "--class", "hand-off", "--to", "Author",
                             "--title", "Test-Packet", "--body", "A test body.",
                             "--author", FAKE_AUTHOR)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("posted: IF-0010", result.stdout)
        text = (self.reader / "Interface_Index.md").read_text(encoding="utf-8")
        self.assertIn("**Id high-water:** IF-0010", text)
        self.assertRegex(text, r"\| IF-0010 \| \d{4}-\d{2}-\d{2} \| Handoff \| "
                               r"Reader → Author \| Author \(CN-0001\) \|")
        envelopes = list(self.reader.glob("Handoff_*_Test-Packet.md"))
        self.assertEqual(len(envelopes), 1)
        body = envelopes[0].read_text(encoding="utf-8")
        self.assertIn("DATA, NEVER INSTRUCTION", body)          # §5.1 the floor
        self.assertIn("Reader → Author (CN-0001)", body)        # §5.2 direction + CN
        self.assertIn("**Class:** hand-off", body)              # §5.3
        self.assertIn(f"**Author:** {FAKE_AUTHOR}", body)       # §5.4 (TF-2)
        self.assertIn("**Cite as:**", body)                     # §5.5
        # the reshaped index stays v0.2-conformant after the post
        check = run_postman("check", str(self.reader / "Interface_Index.md"))
        self.assertEqual(check.returncode, 0, check.stdout)

    def test_addressed_post_refused_without_connection(self):
        result = run_postman("post", "--place", str(self.reader),
                             "--class", "hand-off", "--to", "Nobody",
                             "--title", "Should-Refuse", "--body", "x")
        self.assertEqual(result.returncode, 1)
        self.assertIn("REFUSED", result.stderr)
        self.assertIn("no standing connection", result.stderr)
        self.assertEqual(list(self.reader.glob("*Should-Refuse*")), [])
        text = (self.reader / "Interface_Index.md").read_text(encoding="utf-8")
        self.assertIn("**Id high-water:** IF-0009", text)       # untouched

    def test_addressed_post_refused_on_v01_index(self):
        with tempfile.TemporaryDirectory(prefix="postman v01 post ") as tmp:
            place = Path(tmp) / "Interface"
            place.mkdir()
            (place / "Interface_Index.md").write_text(v01_index("Old"), encoding="utf-8")
            result = run_postman("post", "--place", str(place), "--class", "ask",
                                 "--to", "Other", "--title", "X", "--body", "x")
            self.assertEqual(result.returncode, 1)
            self.assertIn("no connections block", result.stderr)

    def test_broadcast_needs_no_connection(self):
        result = run_postman("post", "--place", str(self.reader),
                             "--class", "advisory", "--to", "any",
                             "--title", "To-All", "--body", "Broadcast body.",
                             "--author", FAKE_AUTHOR)
        self.assertEqual(result.returncode, 0, result.stderr)
        text = (self.reader / "Interface_Index.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"\| IF-0010 \|.*\| any \| `Advisory_.*_To-All\.md` \| standing \|")

    def test_broadcast_refused_on_private_face(self):
        private = self.reader.parent / "Private Interface"
        private.mkdir()
        (private / "Interface_Index.md").write_text(
            v02_index("Reader", face="private"), encoding="utf-8")
        result = run_postman("post", "--place", str(private), "--class", "advisory",
                             "--to", "any", "--title", "Leak", "--body", "x")
        self.assertEqual(result.returncode, 1)
        self.assertIn("public face", result.stderr)


class TestReceipt(PlaceFixture):
    def test_receipt_shape(self):
        # built at runtime so no path-shaped literal sits in this source file
        # (check_versions.py's path heuristic would flag a fixture path as a claim)
        cite = f"`{self.author / 'Handoff_2026-08-22_For-Reader.md'}` (2026-08-23)"
        result = run_postman("receipt", "--place", str(self.reader),
                             "--absorbed", "IF-0002", "--to", "Author",
                             "--cite", cite, "--author", FAKE_AUTHOR)
        self.assertEqual(result.returncode, 0, result.stderr)
        envelopes = list(self.reader.glob("Receipt_*_IF-0002-Author.md"))
        self.assertEqual(len(envelopes), 1)
        body = envelopes[0].read_text(encoding="utf-8")
        self.assertIn("**Class:** receipt", body)
        self.assertIn("Absorbed id:** IF-0002", body)
        self.assertIn(cite, body)
        self.assertIn("`spent` by your own act", body)
        self.assertIn("Reader → Author (CN-0001)", body)
        text = (self.reader / "Interface_Index.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"\| IF-0010 \|.*\| Receipt \|.*\| Author \(CN-0001\) \|")

    def test_receipt_refused_without_connection(self):
        result = run_postman("receipt", "--place", str(self.reader),
                             "--absorbed", "IF-0002", "--to", "Stranger",
                             "--cite", "`x` (2026-08-23)")
        self.assertEqual(result.returncode, 1)
        self.assertIn("no standing connection", result.stderr)

    def test_receipt_rejects_malformed_id(self):
        result = run_postman("receipt", "--place", str(self.reader),
                             "--absorbed", "IF-12", "--to", "Author",
                             "--cite", "`x` (2026-08-23)")
        self.assertEqual(result.returncode, 1)
        self.assertIn("IF-NNNN", result.stderr)


class TestAuthorResolution(PlaceFixture):
    """TF-2: the envelope Author is the instance's own writing identity —
    explicit flag → GIT_AUTHOR_* environment (the genesis write-time
    convention) → the place's repo-LOCAL git config; the machine-global git
    config never decides (refusal, naming the flag). All identities fake."""

    def author_of(self, glob_pattern):
        envelopes = list(self.reader.glob(glob_pattern))
        self.assertEqual(len(envelopes), 1)
        body = envelopes[0].read_text(encoding="utf-8")
        match = re.search(r"\*\*Author:\*\* ([^\n]+)", body)
        self.assertIsNotNone(match, body)
        return match.group(1).strip()

    def test_explicit_flag_beats_environment(self):
        result = run_postman(
            "post", "--place", str(self.reader), "--class", "advisory",
            "--to", "any", "--title", "Flag-Wins", "--body", "x",
            "--author", FAKE_AUTHOR,
            env={"GIT_AUTHOR_NAME": FAKE_ENV_AUTHOR[0],
                 "GIT_AUTHOR_EMAIL": FAKE_ENV_AUTHOR[1]})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.author_of("Advisory_*_Flag-Wins.md"), FAKE_AUTHOR)

    def test_environment_convention_resolves(self):
        result = run_postman(
            "post", "--place", str(self.reader), "--class", "advisory",
            "--to", "any", "--title", "Env-Writer", "--body", "x",
            env={"GIT_AUTHOR_NAME": FAKE_ENV_AUTHOR[0],
                 "GIT_AUTHOR_EMAIL": FAKE_ENV_AUTHOR[1]})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.author_of("Advisory_*_Env-Writer.md"),
                         f"{FAKE_ENV_AUTHOR[0]} <{FAKE_ENV_AUTHOR[1]}>")

    def test_repo_local_config_resolves(self):
        estate = Path(self._tmp.name) / "Local Estate"
        place = estate / "Interface"
        place.mkdir(parents=True)
        make_fixture_repo(estate)
        (place / "Interface_Index.md").write_text(
            v02_index("Localinst"), encoding="utf-8")
        result = run_postman("post", "--place", str(place), "--class",
                             "advisory", "--to", "any", "--title",
                             "Local-Writer", "--body", "x")
        self.assertEqual(result.returncode, 0, result.stderr)
        envelope = next(place.glob("Advisory_*_Local-Writer.md"))
        self.assertIn(
            f"**Author:** {FAKE_LOCAL_AUTHOR[0]} <{FAKE_LOCAL_AUTHOR[1]}>",
            envelope.read_text(encoding="utf-8"))

    def test_global_only_refused_naming_flag(self):
        # The fixture place sits in no git repo, the env is scrubbed, no flag:
        # only the machine-global git config would remain — refusal (TF-2).
        result = run_postman("post", "--place", str(self.reader),
                             "--class", "advisory", "--to", "any",
                             "--title", "No-Identity", "--body", "x")
        self.assertEqual(result.returncode, 1)
        self.assertIn("REFUSED", result.stderr)
        self.assertIn("--author", result.stderr)
        self.assertIn("machine-global", result.stderr)
        self.assertEqual(list(self.reader.glob("*No-Identity*")), [])
        text = (self.reader / "Interface_Index.md").read_text(encoding="utf-8")
        self.assertIn("**Id high-water:** IF-0009", text)       # untouched


class TestSpentDissolve(PlaceFixture):
    """TF-6: the §6.1 closing lanes — spent records the evidence reference in
    the envelope and re-checks the index; dissolve removes file + row,
    preserves the Id high-water, refuses a non-spent row, and warns (TF-7,
    never blocks) when git holds no commit of the envelope."""

    OWN_FILE = "Handoff_2026-08-21_To-Author.md"

    def make_own_envelope(self):
        path = self.reader / self.OWN_FILE
        path.write_text("# Handoff: To Author\n\nEnvelope body.\n",
                        encoding="utf-8")
        return path

    def read_index(self):
        return (self.reader / "Interface_Index.md").read_text(encoding="utf-8")

    def test_spent_marks_row_records_evidence_and_rechecks(self):
        envelope = self.make_own_envelope()
        evidence = "the counterpart's receipt IF-0004 (2026-08-23)"
        result = run_postman("spent", "IF-0009", "--place", str(self.reader),
                             "--evidence", evidence)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("re-checked conformant", result.stdout)
        text = self.read_index()
        self.assertRegex(text, r"\| IF-0009 \|.*\| spent \|")
        self.assertIn("**Id high-water:** IF-0009", text)
        body = envelope.read_text(encoding="utf-8")
        self.assertIn("**Spent (", body)
        self.assertIn(evidence, body)
        check = run_postman("check", str(self.reader / "Interface_Index.md"))
        self.assertEqual(check.returncode, 0, check.stdout)

    def test_spent_refuses_unknown_id(self):
        self.make_own_envelope()
        result = run_postman("spent", "IF-0042", "--place", str(self.reader),
                             "--evidence", "x")
        self.assertEqual(result.returncode, 1)
        self.assertIn("no IF-0042 row", result.stderr)

    def test_spent_refuses_already_spent(self):
        self.make_own_envelope()
        run_postman("spent", "IF-0009", "--place", str(self.reader),
                    "--evidence", "x")
        result = run_postman("spent", "IF-0009", "--place", str(self.reader),
                             "--evidence", "x")
        self.assertEqual(result.returncode, 1)
        self.assertIn("already spent", result.stderr)

    def test_spent_refuses_when_envelope_file_missing(self):
        result = run_postman("spent", "IF-0009", "--place", str(self.reader),
                             "--evidence", "x")
        self.assertEqual(result.returncode, 1)
        self.assertIn("envelope file missing", result.stderr)
        self.assertRegex(self.read_index(), r"\| IF-0009 \|.*\| standing \|")

    def test_spent_fails_loudly_when_result_nonconformant(self):
        envelope = self.make_own_envelope()
        # A pre-existing index defect: the CN high-water line is gone.
        broken = self.read_index().replace("**CN high-water:** CN-0002\n", "")
        (self.reader / "Interface_Index.md").write_text(broken, encoding="utf-8")
        result = run_postman("spent", "IF-0009", "--place", str(self.reader),
                             "--evidence", "x")
        self.assertEqual(result.returncode, 1)
        self.assertIn("nonconformant", result.stderr)
        self.assertRegex(self.read_index(), r"\| IF-0009 \|.*\| standing \|")
        self.assertNotIn("Spent", envelope.read_text(encoding="utf-8"))

    def test_dissolve_refuses_standing_row(self):
        envelope = self.make_own_envelope()
        result = run_postman("dissolve", "IF-0009", "--place", str(self.reader))
        self.assertEqual(result.returncode, 1)
        self.assertIn("not spent", result.stderr)
        self.assertTrue(envelope.is_file())
        self.assertRegex(self.read_index(), r"\| IF-0009 \|")

    def test_dissolve_removes_row_and_file_preserving_high_water(self):
        envelope = self.make_own_envelope()
        run_postman("spent", "IF-0009", "--place", str(self.reader),
                    "--evidence", "x")
        result = run_postman("dissolve", "IF-0009", "--place", str(self.reader))
        self.assertEqual(result.returncode, 0, result.stderr)
        # the fixture place sits in no git repo — the TF-7 warn must fire
        self.assertIn("WARN", result.stdout)
        self.assertIn("trace", result.stdout)
        self.assertFalse(envelope.exists())
        text = self.read_index()
        self.assertNotIn("IF-0009 |", text)
        self.assertIn("**Id high-water:** IF-0009", text)   # ids never reuse
        check = run_postman("check", str(self.reader / "Interface_Index.md"))
        self.assertEqual(check.returncode, 0, check.stdout)

    def _repo_place(self):
        """A place inside a real (fixture) git repo, one broadcast row +
        its envelope on disk."""
        estate = Path(self._tmp.name) / "Committed Estate"
        place = estate / "Interface"
        place.mkdir(parents=True)
        make_fixture_repo(estate)
        (place / "Interface_Index.md").write_text(v02_index(
            "Solo",
            rows=["| IF-0001 | 2026-08-23 | Advisory | Solo → any | any | `Advisory_2026-08-23_B.md` | standing |"],
            if_hw="IF-0001"), encoding="utf-8")
        (place / "Advisory_2026-08-23_B.md").write_text(
            "# Advisory: B\n\nBody.\n", encoding="utf-8")
        return estate, place

    def test_dissolve_warns_when_envelope_never_committed(self):
        estate, place = self._repo_place()
        git_quiet(estate, "add", "Interface/Interface_Index.md")
        git_quiet(estate, "commit", "-q", "-m", "index only")
        run_postman("spent", "IF-0001", "--place", str(place),
                    "--evidence", "x")
        result = run_postman("dissolve", "IF-0001", "--place", str(place))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("WARN", result.stdout)
        self.assertIn("no commit", result.stdout)

    def test_dissolve_quiet_when_envelope_committed(self):
        estate, place = self._repo_place()
        git_quiet(estate, "add", "--all")
        git_quiet(estate, "commit", "-q", "-m", "everything")
        run_postman("spent", "IF-0001", "--place", str(place),
                    "--evidence", "x")
        result = run_postman("dissolve", "IF-0001", "--place", str(place))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("WARN", result.stdout)
        self.assertFalse((place / "Advisory_2026-08-23_B.md").exists())


class TestBroadcastMatch(PlaceFixture):
    """TF-5: broadcast is exactly `any` or `any <qualifier>` — an instance
    named "Anything" is a name, never a broadcast."""

    def test_broadcast_shapes(self):
        self.assertTrue(postman.is_broadcast_name("any"))
        self.assertTrue(postman.is_broadcast_name("Any"))
        self.assertTrue(postman.is_broadcast_name("any beta-cohort"))
        self.assertFalse(postman.is_broadcast_name("Anything"))
        self.assertFalse(postman.is_broadcast_name("anywhere"))
        self.assertFalse(postman.is_broadcast_name(""))
        self.assertTrue(postman.is_broadcast("`any` (broadcast)"))
        self.assertFalse(postman.is_broadcast("Anything (CN-0009)"))

    def test_poll_does_not_treat_anything_as_broadcast(self):
        self.write_author_rows([
            "| IF-0001 | 2026-08-22 | Advisory | Author → any | any | `Advisory_2026-08-22_Broadcast.md` | standing |",
            "| IF-0006 | 2026-08-23 | Advisory | Author → Anything | Anything | `Advisory_2026-08-23_Nobody.md` | standing |",
        ])
        result = self.poll()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("NEW  IF-0001", result.stdout)    # true broadcast
        self.assertNotIn("IF-0006", result.stdout)      # a name, not `any…`

    def test_post_to_anything_requires_connection(self):
        result = run_postman("post", "--place", str(self.reader),
                             "--class", "advisory", "--to", "Anything",
                             "--title", "Not-A-Broadcast", "--body", "x",
                             "--author", FAKE_AUTHOR)
        self.assertEqual(result.returncode, 1)
        self.assertIn("no standing connection", result.stderr)
        self.assertEqual(list(self.reader.glob("*Not-A-Broadcast*")), [])


class TestCodeLint(unittest.TestCase):
    """TF-4: warn-class Code-cell lint in check — a cell that looks like a
    connection code must be the full xxxx-xxxx-xxxx lowercase shape; prose
    (pending) cells stay silent; warnings never flip the exit code."""

    def _write(self, text):
        handle = tempfile.NamedTemporaryFile(
            "w", suffix=" Interface_Index.md", delete=False, encoding="utf-8")
        handle.write(text)
        handle.close()
        self.addCleanup(os.unlink, handle.name)
        return handle.name

    def test_code_shape_deviations_warn_without_failing(self):
        text = v02_index(
            "Warned",
            connections=[
                f"| CN-0001 | Friend | {FAKE_FP_A} | abcd-ef01-2345 | 2026-08-23 | public: `~/nowhere/` | standing |",
                f"| CN-0002 | Buddy | {FAKE_FP_B} | abcd-EF01-2345 | 2026-08-23 | public: `~/elsewhere/` | standing |",
                f"| CN-0003 | Shorty | {FAKE_FP_A} | abcd-ef01 | 2026-08-23 | public: `~/nope/` | standing |",
            ], cn_hw="CN-0003")
        result = run_postman("check", self._write(text))
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("conformant", result.stdout)
        self.assertEqual(result.stdout.count("WARNING"), 2)
        self.assertIn("abcd-EF01-2345", result.stdout)  # uppercase deviation
        self.assertIn("'abcd-ef01'", result.stdout)     # truncated shape

    def test_full_code_and_prose_stay_silent(self):
        text = v02_index(
            "Quiet",
            connections=[
                f"| CN-0001 | Friend | {FAKE_FP_A} | abcd-ef01-2345 | 2026-08-23 | public: `~/nowhere/` | standing |",
                f"| CN-0002 | Pal | {FAKE_FP_B} | pending — ceremony not yet walked | 2026-08-23 | public: `~/elsewhere/` | standing |",
            ], cn_hw="CN-0002")
        result = run_postman("check", self._write(text))
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn("WARNING", result.stdout)


class TestH1Preservation(PlaceFixture):
    """TF-9: generated envelope H1s keep an id's exact hyphenated form —
    `IF-0002` never mangles to `IF 0002`."""

    def test_post_h1_keeps_id_hyphenation(self):
        result = run_postman("post", "--place", str(self.reader),
                             "--class", "hand-off", "--to", "Author",
                             "--title", "About-IF-0009-Follow-Up",
                             "--body", "x", "--author", FAKE_AUTHOR)
        self.assertEqual(result.returncode, 0, result.stderr)
        envelope = next(self.reader.glob("Handoff_*_About-IF-0009-Follow-Up.md"))
        first = envelope.read_text(encoding="utf-8").splitlines()[0]
        self.assertEqual(first, "# Handoff: About IF-0009 Follow Up")

    def test_receipt_h1_keeps_absorbed_id(self):
        result = run_postman("receipt", "--place", str(self.reader),
                             "--absorbed", "IF-0002", "--to", "Author",
                             "--cite", "`x` (2026-08-23)",
                             "--author", FAKE_AUTHOR)
        self.assertEqual(result.returncode, 0, result.stderr)
        envelope = next(self.reader.glob("Receipt_*_IF-0002-Author.md"))
        first = envelope.read_text(encoding="utf-8").splitlines()[0]
        self.assertEqual(first, "# Receipt: IF-0002 Author")


if __name__ == "__main__":
    unittest.main(verbosity=2)
