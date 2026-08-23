# Fractal Interface Place Format v0.2

> **CANONICAL SPECIFICATION (Ratified 2026-08-23, the thirty-ninth session — in-conversation per C-033; Max's words of record: *"amend the interface change to 0.8 … let's build this thing"*, the game-plan agreement *"let's go"*, the build gate *"go"*).** The standard of record for the interface place: `Fractal_Interface_Place_Format_v0.1` is **superseded, retained as frozen history** (its own DOC identity kept, the C-061 pattern). This reissue is the **§5 deferral of v0.1 firing as designed** ("a reissue, not a patch"): the two-children condition was met 2026-08-22 (PR real at `78997cf`), and the commission that answers it was given in this session. v0.2 carries the whole v0.1 standard forward and adds the three layers the commission designed: the **connection layer** (conscious setup — introduce, verify, lock in), the **two faces** (a public interface and a hidden private one), and the **routing law** (how the right information reaches the right place). One standard, not two: the connection is the place's own gate, not a separate protocol. The binding **Fractal Interface Protocol** still distills whole at its own named trigger (Foundation §8, unchanged); this format folds into it when it does.

**Version:** 0.2 · **Status:** Ratified (2026-08-23, in-conversation per C-033 — Max's *"amend the interface change to 0.8 … let's build this thing"*; the game-plan agreement *"let's go"*; the build gate *"go"*) · **Reviewed By:** Max (2026-08-23 — the commission directives verbatim stand in the banner block) · **Domain:** GBL · **Author:** Claude · **Date:** 2026-08-23 · **Parent:** Fractal_Interface_Foundation (§8–§9 the forge of record) · **Supersedes:** Fractal_Interface_Place_Format_v0.1 (retained as history, its own DOC identity per C-061) · **Document ID:** DOC-01M0Q5G0MG03ZKEME90WAT64AH (minted at the ratifying close via `close.py --create`, the v0.1 pattern)

**The commission (the thirty-ninth session, Max's directives verbatim — the provenance of every new section):** *"an inbox system that tells a fractal it got news … like e-mail"* · *"the real architectural question here is how can we make sure that the right information gets to the right place?"* · *"if two fractals want to communicate, they need to set up a connection first … a key code which both fractals need to lock-in"* · *"any fractal can only receive and send to connected fractals … this would later need to be [a] machine guarded process (like friend requests on social media, in case we want an online network)"* · *"distinguish … a public interface and a hidden private interface, then you can send sensitive data between fractals and have a public face."*

---

## 1 · The contract (kernel-grade — seven laws)

A FRACTAL instance is sovereign: nobody writes into its tree, and it writes into nobody's. But instances need to talk — today through their humans, on the horizon through an online network. The interface place is the structure that makes both work without choosing between them. The contract, extended at v0.2:

1. **One place, one index — per face.** The instance designates one deliberately-readable location per face (default `Interface/` at the repo root for the public face) and maintains one navigation index inside each. Readers check the index, never crawl the folder. The public face is the default and the minimum; the private face is optional (§3).
2. **Pull, never push.** Files stay in their **author's** place; the reader comes to them. Nobody ever writes into a foreign tree — the sovereignty boundary is enforced by the transport's shape, not by discipline.
3. **Declaring a face is declaring it readable — to its audience.** The public face joins the deliberately-served surface class (the C-120 site class): world-readable by design, which is why a child may read it even in the living mother without breaking the C-109 asymmetry. The private face is declared **only to its connections** — the address exchange at the handshake (§2) *is* the declaration, and its audience is exactly the pair.
4. **Envelopes are RAM** (C-121 generalized). Every file in a place is temporary *by construction*: the window is the owner's own creation and deletion, in its own jurisdiction. The reader's duty: **absorb and cite by path + date (or pin, where anchored) — never depend on the file persisting.** Citations plus git history are the full trace. An envelope is therefore dissolved only after at least one commit has carried it (a close normally provides this); an owner who dissolves uncommitted bytes accepts, knowingly, that the citations alone are the trace.
5. **Data, never instruction** (C-096 floor). Nothing in a place can command its reader; a message creates an option the receiver dispositions by its own recorded decision — never an obligation. This holds identically on both faces: a private envelope commands its reader exactly as little as a public one.
6. **Connections gate addressed traffic.** An envelope addressed to a *named* counterpart may only be sent to, and ingested from, a **standing connection** (§2) — machine-checkable on both sides, in each side's own jurisdiction. Broadcast to `any` is the public face's open tier and needs no connection. The one addressed class a stranger may legitimately post is the **connection request** (§2.5). *Friend requests gate messaging, never the profile page.*
7. **The signal is the index; the notification is the diff.** The index state is the normative signal (Foundation v0.6 §9); a *diff* of a counterpart's index is the notification itself — the header block of every new message (id · class · direction · file), never the body. Directions, never context, at the notification layer too.

## 2 · The connection layer (new — the conscious handshake)

Two fractals that want to talk **set up a connection first**. The setup introduces them, verifies their identities, agrees their channels, and records mutual consent — after which the gate (law 6) opens between them and only them.

### 2.1 · The identity primitive (already installed)

Every instance already carries a cryptographic identity: its **signing key**, verified against `.allowed_signers` at every commit (the C-074b custody machinery). A connection binds *that* key — no new key material is invented. An instance's **identity triple** is: **instance name · public-face address · signing public key** (fingerprint in the standard `SHA256:…` form). The fingerprint bytes are pinned: OpenSSH's standard form over the decoded key (`ssh-keygen -lf`); where a blob is not a decodable key (test harnesses), SHA-256 over the blob's exact bytes, base64 unpadded, under the same prefix.

### 2.2 · The ceremony (four steps)

1. **Introduce.** The two sides exchange identity triples — today by the owner's hand; at the network scale via the request class (§2.5).
2. **Verify.** Both sides independently compute the **connection code** — pinned to the byte: each key blob is the exact byte sequence of its single-line public-key entry's base64 blob field alone (ASCII, no surrounding whitespace — never the key-type or comment fields); the two blobs sort by raw byte order and concatenate directly, **no separator**; `SHA-256` over that concatenation renders as **lowercase hex**, and the code is the digest's first 12 characters in three hyphenated groups (`xxxx-xxxx-xxxx`). The owners compare the code out-of-band. A match proves both sides hold the same two keys — no one sat in the middle. **The code is derived from public material and is not a secret** (C-087 untouched): it may be recorded openly; it proves nothing to an attacker and everything to the pair.
3. **Lock in.** Each instance records the connection as its **own decision** (the P-row pattern — own act, own tree, own jurisdiction), citing: the counterpart's identity triple, the code, the date, and the channel agreement (step 4). Mutual consent = two records that cite each other. Each side adds a row to its connections block (§4, block 5) under its own `CN-NNNN` series — ids never reuse (the high-water law).
4. **Agree the channels.** The pair names where it talks: public↔public (the default), and/or a **private channel** — at which point the private face's address is exchanged (§3). The channel agreement is part of the connection record.

### 2.3 · What the gate enforces (and where)

Enforcement is each side's own machinery in its own jurisdiction — no foreign enforcement exists or is needed:

- **Receive-side:** the postman (§7) polls **only** standing connections, and treats an envelope as authentic only if its commits verify against the connection-recorded key. Unknown places and unknown keys are simply not on the reading list.
- **Send-side:** the postman refuses to post an envelope addressed to a non-connection.
- **Honesty about visibility:** the gate governs the *trusted ingestion path*, not sight. A public face is world-readable by design — strangers reading it is intended (the site class). Sending and receiving are gated; looking is not.

### 2.4 · Lifecycle

**Retire** (disconnect): each side retires its record by its own act — the row goes `retired`, the id stays in the high-water memory. **Key rotation:** a new key means a new code — the pair re-verifies (step 2) and each side re-records; the old record retires with a pointer. **Birth is the introduction:** genesis seeds the newborn's `CN-0001` — the mother — with the mother's identity triple travelling in the kernel; the mother records her side at the birth act; the code computes once the child's key exists. A newborn is born connected to its mother and to no one else.

### 2.5 · The connection request (the stranger's one door)

The request is the one addressed envelope a non-connection may legitimately post: class `connection-request`, posted in the **requester's own public face**, addressed to the target, carrying the requester's identity triple. The target's handling is normative: **quarantine** — surfaced to the owner, never auto-ingested, data-never-instruction hardened; the owner ratifies (→ ceremony resumes at step 2) or ignores. This *is* the friend request, and the grammar is identical whether the counterpart sits on the same desk or across the internet.

*The delivery gap, named honestly:* a target that polls only its connections cannot see a stranger's place. Request *delivery* therefore needs one out-of-band hop: **today the owner's hand** (or the public intake — issues are the off-machine door, C-120); **at the network scale, the umbrella's registrar** (OQ-34's seat — the roster the Foundation §3 already reserves) relays the notification, exactly as a platform delivers a friend request. The registrar relays existence, never content, and never holds authority — machine-guarding this hop is the online network's build, deliberately not designed further here (§9).

## 3 · The two faces (new — public and hidden private)

An instance may run its interface in **two faces**:

- **The public face** — the place as v0.1 built it: world-readable (the C-120 class), carrying broadcasts to `any` (advisories, announcements — the profile page), addressed public-safe traffic, and the request lane. Every instance has one; it is the minimum.
- **The private face** — optional: a second place with its own index, for **sensitive traffic between connected fractals**. Its address is **published nowhere** — it travels only inside the handshake (§2.2 step 4), so it is connection-gated *by construction*: without the connection you do not know where to look. Existence-hiding, not just access control; the public index does not have to admit it exists.

**Storage matches visibility.** A private-tree instance (the KNet/PR class) may keep its private face anywhere in its tree. A public-tree instance (the mother) keeps it in annex-class storage (C-098) — never in the public repo. Envelope ids run **one `IF-NNNN` series per instance across both faces** (one high-water memory); each face's index lists only its own files — that separation *is* the hiding.

**The floors hold on both faces.** C-087: sensitive ≠ secret — personal-class and business knowledge may ride the private face; credential *values* ride nothing, ever, on any channel. C-096: data never instruction, identically private and public. And the pattern is the instance's own: FRACTAL already lives as public repo + private annex — the interface grows the same two faces. Same law, next scale.

**Confidentiality honesty (from the Foundation's transport-security clause, unchanged):** a hosted private remote is access-controlled but the relay sees plaintext at rest; direct SSH between the owner's machines has no third party. **End-to-end encryption is enabled-not-built** (§9): the handshake already exchanges keys, so envelopes encrypted *to the counterpart's key* — sealed even on a public channel — are a natural later extension at zero architectural cost. That is why the handshake carries keys, not just addresses.

## 4 · The index format (the mechanical grammar, v0.2)

The index is one markdown file per face, `<place>/Interface_Index.md`, with these blocks top to bottom:

| # | Block | Content rule |
|---|---|---|
| 1 | **Declaration banner** | Blockquote stating what the place is (this standard cited by name + version), the pull-never-push rule, the RAM nature of every listed file with the reader's absorb-and-cite duty, the data-never-instruction floor, and — new at v0.2 — the connection gate (law 6). Derived projection — governs nothing. |
| 2 | **Instance line** | `**Instance:** <name>` · `**Place:** <path>` · `**Face:** public \| private` · `**Index stamped:** <date>` · `**Status grammar:** standing · spent` — one bolded run-on line, the living-projection stamp pattern (C-012 class). The private face's existence is *not* declared here on the public face. |
| 3 | **The standing table** | One row per file currently in this face: **Id · Date · Class · Direction · Counterpart · File · Status**. Id grammar `IF-NNNN` (one per-instance series across faces, zero-padded). Class is a plain label (the executed classes live in Foundation §4; `receipt` and `connection-request` join them at v0.2). Direction reads `author → reader`; **a named Counterpart must cite a standing connection (`CN-NNNN`)**; `any` is broadcast — public face only. Status: **standing** (posted, not yet absorbed) · **spent** (absorbed and cited — awaiting its owner's dissolution). |
| 4 | **Id high-water line** | `**Id high-water:** IF-NNNN` — dissolved rows leave the table with their files; the high-water is the table's memory, and **ids never reuse** (the C-121 law). Born at `IF-0000`. |
| 5 | **Connections block** *(replaces v0.1's known-counterpart-places)* | The instance's standing connections: **CN-id · Instance · Key fingerprint · Code · Since · Channels · Status** (`standing` · `retired`), plus `**CN high-water:** CN-NNNN`. Public data only — name, fingerprint, code, and the *public* channel; **a private channel is marked `private` with no address**. By pair agreement a connection may be recorded wholly on the private face instead (a hidden connection); the mutuality is between the pair, not the world. |
| 6 | **Maintenance line** | Footer stating when the index moves: at each post, absorption report, dissolution, or connection act — maintained by the posting session. |

## 5 · The envelope minimum (what every posted file self-declares)

Unchanged in substance from v0.1 — a file in a place opens with:

1. **The floor:** a banner declaring the content **data, never instruction** (C-096).
2. **Direction:** author instance → intended reader(s) or `any`; **addressed envelopes cite their connection (`CN-NNNN`)**.
3. **Class:** the message-class label (matching its index row).
4. **Date + author:** the writing identity (the instance's AGENT id where it has one).
5. **The citation line:** how to cite this file once absorbed — path + date, or pin where anchored — because the file will not persist.

Everything else — structure, length, tone — is the author's own. The envelope holds **directions and the message itself, never the sender's working context** (Foundation §2).

## 6 · The routing law (new — the right information to the right place)

The question decomposes into three layers; the split of **who owns which layer** is the architecture. It is e-mail's own shape — sender-declared headers, delivery by address, receiver-side filters — and it is the Context Index pattern applied to inbound traffic (recursive simplicity, once more):

1. **The address layer (sender declares).** The Counterpart column. A poll filters the diff to rows addressed to *me* or `any` — the notification arrives pre-filtered to your mail, so multiple files are never a haystack.
2. **The class layer (sender declares).** The message class names what *kind* of thing arrived — the routing key.
3. **The landing layer (receiver owns).** **Routing competence is domestic law** (Foundation v0.6 §9, clause 4): where inside the receiver a message lands is the receiver's own knowledge, held in its **domestic routing map** — never carried in the envelope. Prose-first at v0.2; the recommended starter map:

| Class | Recommended landing (the receiver's own equivalents) |
|---|---|
| advisory | the migration lane (the C-117 KMP shape) |
| hand-off | an agenda offer (the C-031 slot — board / Local Context) |
| fieldnote | the buffer intake (C-121 — ratification-gated) |
| ask | disposition by own recorded decision (the P-row) |
| harvest offer | the landing zone (pre-canon) |
| receipt | mark the cited own-row `spent` (§6.1) |
| connection-request | the owner's quarantine lane (§2.5) |

**6.1 · The receipt loop (the spent lifecycle goes mechanical).** When a receiver absorbs an envelope, it posts an **absorption receipt** in *its own* place, addressed back to the author (class `receipt`, citing the absorbed id + the citation used). The author's next poll sees the receipt and marks its own row `spent` **by its own act**. Pull-never-push at every hop. A receipt stands until the author's row shows spent, then dissolves by its owner like any envelope. A reader that later finds a row vanished — absence after observed presence — reads it as spent-or-dissolved; no further signal is owed, and the id's high-water is the memory.

**6.2 · The cursor law.** "New" is computed against a **reader-side cursor** — the last-seen index state per connection, kept in the **reader's own tree**, never touching the author's place (read receipts without foreign writes). Its mechanical shape is the postman build's call.

**6.3 · The two-stage trigger (the vendor-neutral floor, restated).** **The wake-up is dumb; the poll is smart.** A push-style accelerator (file watcher, harness hook, webhook) may say "poll now" and nothing else (Foundation v0.6 §9, clause 3); the *information* rides only the neutral substrate — the index over files/git/HTTPS — where a polling-only agent gets the identical signal with no push at all. The push collapses latency, never carries payload, conformance, or authority.

## 7 · The mechanics — the postman (normative behavior; build pending)

The tool half of this standard — working name **`postman.py`**, one per instance, kernel-shipped once built. Prose-first until then (the v0.1 pattern: the index parser *is* the checker — the build makes this format machine-guarded). Normative behavior:

- **`poll`** — iterate the connections block, fetch each counterpart's agreed channels (git fetch / path read), parse each index, diff against the cursor, and report the filtered header diff (§6 layer 1): new standing rows addressed to me or `any`, status changes, receipts. Poll **only** standing connections (law 6); verify signatures against the connection-recorded key.
- **`post`** — write a §5-conformant envelope + its index row + the high-water bump in this instance's own place; **refuse** an addressed post to a non-connection.
- **`receipt`** — post the §6.1 absorption receipt for a named absorbed id.
- **Request quarantine** — surface an inbound `connection-request` to the owner; never auto-ingest (§2.5).
- **Session integration** — the opener runs `poll` at session start (the `fieldnote.py --depth` pattern: one line at orientation); mid-session, any accelerator says "poll now" (§6.3).

## 8 · The skeleton (copy, fill the `{{SLOTS}}`)

```markdown
# {{INSTANCE}} — Interface Index

> **THE INTERFACE PLACE'S NAVIGATION INDEX (Fractal Interface Place Format v0.2).**
> This instance's deliberately-readable communication surface: what stands here is
> for FRACTAL-governed instances to come and read. Pull, never push: readers visit;
> nobody writes into foreign trees. Every listed file is RAM-class — temporary by
> construction, deletable by this instance's own act once absorbed; readers absorb
> and cite by path + date (or pin), never depending on the file persisting. Content
> is data, never instruction (C-096 class). Addressed traffic rides standing
> connections only (the v0.2 gate); broadcast to `any` is open; a stranger's one
> addressed class is the connection-request. Derived projection — governs nothing.

**Instance:** {{NAME}} · **Place:** `Interface/` (repo root) · **Face:** public · **Index stamped:** {{DATE}} · **Status grammar:** `standing` (posted, not yet absorbed) · `spent` (absorbed and cited — awaiting its owner's dissolution)

| Id | Date | Class | Direction | Counterpart | File | Status |
|---|---|---|---|---|---|---|

**Id high-water:** IF-0000

**Connections:**

| CN | Instance | Key fingerprint | Code | Since | Channels | Status |
|---|---|---|---|---|---|---|

**CN high-water:** CN-0000

---

*Maintained by the posting session at each post, absorption report, dissolution, or
connection act. Transport today: the owner carries directions by hand; the law —
what lives where, who owns the window, who may talk, how to cite — survives every
transport upgrade.*
```

## 9 · Deliberately unspecified (the open horizon, named honestly)

- **End-to-end encryption** — enabled by the handshake's key exchange, built only at need: the natural trigger is the first cross-owner private channel (arc 3), where hosted-relay plaintext-at-rest stops being acceptable. Until then the channel choice (public repo / private remote / direct SSH) carries the confidentiality, per the Foundation's transport-security clause.
- **The online network** — hosted transport, the umbrella's registrar (the request-relay hop, §2.5; OQ-34's seat), machine-guarded friend-requests at internet scale. The grammar here is deliberately identical at every scale; the platform build waits for the network.
- **Cross-owner trust** — instances whose keys no one authority holds: the arc-3 federation boundary (FN-0003's banked question). Today all keys sit in one custody, which makes the ceremony rehearsal + ingestion hygiene; its full security weight arrives exactly when custody splits — the correct order to build trust machinery in.
- **Group channels** — v0.2 connections are pairwise; a group is many pairs until observed need says otherwise.
- **Message-class and execution semantics** — Foundation §4/§10, concept tier, until the binding Fractal Interface Protocol distills at its named trigger (Foundation §8 — this format changes nothing about that trigger).

## 10 · Adoption

- **An existing instance** (KNet, PR): a session in *that* instance reads this file from the mother's tree, records the adoption as its own decision (`P-…`), reshapes its index to the v0.2 grammar, and — with the mother — walks the ceremony to formalize the standing de-facto pair. **The two live pairs (FRACTAL↔KNet, FRACTAL↔PR) formalize retroactively**, each side's own act; **KNet↔PR would be the first conscious sibling handshake** — the ceremony's true first specimen.
- **A newborn:** hardwire path — genesis ships this format in the kernel, births the public face (`Interface/Interface_Index.md`, the §8 skeleton at `IF-0000`/`CN-0000`), and seeds `CN-0001` = the mother (§2.4: birth is the introduction). Binds at the build (the C-134 pattern — the grammar ratifies now, the machinery binds when built).
- **The mother:** first mover at the build — index reshaped to v0.2, the domestic routing map written, the retroactive pair records offered to both children.

**Checker half:** prose-first. The postman's parser is the checker (§7); its build trigger is the polling slice — now commissioned — or a conformance dispute, whichever fires first (Registry rule 2).

---

**Refresh triggers:** the postman build landing (the cursor grammar + checker finalize); the first executed handshake (ceremony friction feeds back, C-094); the first cross-owner connection (arc 3 — E2E + registrar arm); the Fractal Interface Protocol's distillation (this format folds in); a field-proven grammar change (C-094).
**Sources:** the thirty-ninth session's commission (Max's directives verbatim, in the banner block); `Fractal_Interface_Place_Format_v0.1` (the carried standard — its own sources: Foundation §9, the mother's executed index, the four founding specimens, the three-leg KNet exchange); Fractal_Interface_Foundation v0.6 §8 (the transport-security clause — the per-channel confidentiality this reissue structures into faces; the counterpart parameter this reissue closes) + §9 (the live seam: the doorbell, the vendor-neutral floor, routing-competence-as-domestic-law); `.allowed_signers` + C-074b (the identity primitive); C-087 (secrets never; the code is public material) · C-096 (data never instruction) · C-098 (annex-class storage — the private face's home in a public tree) · C-109 (the asymmetry the readable-surface class preserves) · C-115 (cite the edition) · C-117 (the advisory lane) · C-120 (the deliberately-served class; issues the off-machine request door) · C-121 (RAM; the high-water law) · C-134 (ratify-now-bind-at-build); the P-row pattern (lock-in as own recorded decision); FN-0003 (the arc-3 trust boundary, deliberately outside); C-021 (nothing built ahead of need — E2E and the registrar named, not built).
**Revision history:** v0.1 (2026-08-19) first issue — the interface-build session: the place contract compressed from Foundation §9, the index grammar distilled from the mother's executed index, the envelope minimum from the four standing specimens; counterpart navigation and transport automation deliberately unspecified (the two-children deferral); ratified as the C-123 slate on Max's *"perfect, go."* · v0.2 (2026-08-23, the thirty-ninth session — **ratified in-conversation per C-033**: Max's *"amend the interface change to 0.8 … let's build this thing"*, the game-plan *"let's go"*, the build gate *"go"*) **the connection reissue — the §5 deferral firing:** the seven-law contract (the connection gate, law 6; the signal-is-the-diff, law 7); the connection layer (§2 — the identity primitive on `.allowed_signers`, the four-step ceremony, the verification-checksum code (public material, C-087 clean), lock-in as mutual P-row records, the `CN` series + high-water, lifecycle, birth-is-the-introduction, the connection-request quarantine lane + the delivery-hop honesty); the two faces (§3 — public + hidden private, address-exchange-as-declaration, storage-matches-visibility, one id series across faces, E2E enabled-not-built); the routing law (§6 — the three layers by owner, the domestic map, the receipt loop, the cursor law, the dumb-wake-up/smart-poll restatement); the postman specified (§7, build pending); the skeleton regrown (§8); counterpart navigation **answered**: a reader navigates its connections — the connections block is the reading list. Drafted whole on Max's "go"; ratified the same session — his amendment of the build into beta-0.8 (*"amend the interface change to 0.8 … let's build this thing"*) the ratification act of record. Same session, at the test flight's landing: four precision pins (TF-1/3/7/8 — the code construction byte-pinned, the fingerprint bytes named, the commit-before-dissolve duty, the vanished-row reading; C-094 — the flight fed the standard before its first commit).
