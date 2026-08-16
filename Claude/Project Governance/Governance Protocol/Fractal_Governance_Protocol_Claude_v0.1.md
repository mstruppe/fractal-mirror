# Fractal Governance Protocol — Claude Series v0.1

**Topic:** Migration to Claude & Establishment of the Context Persistence Workflow
**Series:** Claude-era Governance Protocol (opens a new series; the ChatGPT-era sequential protocol patches were closed at v0.11)
**Status:** Ratified (2026-08-12, per Claude Series v0.7)
**Date:** 2026-08-01

---

## 1. Context

The FRACTAL project was constructed with ChatGPT up to the sequential protocol patch v0.11 and the Governance Protocol v0.2. The project owner (Max) is migrating the working relationship to Claude. Two conditions motivated this protocol. First, the **token bottleneck**: carrying full project context in a single conversation does not scale. Second, the need — already identified in the ChatGPT-era "proposed workflow" document — for a workflow in which **no relevant information is lost across conversations**. This protocol records the migration and establishes the Context Persistence Workflow as the first governed process of the Claude era.

## 2. Questions Investigated

- Where should the canonical context packages (Global / Domain / Task / Return) live and be read from?
- How should the workflow be introduced — design the rules first, or build a working artifact first?
- How is the project history preserved while starting the Claude-era work cleanly?
- What file format keeps the system lean, diff-friendly, and machine-readable?
- How much of the load/return cycle should be automated, and when?
- How is the stable identity of exported artifacts guaranteed?

## 3. Human Input (Max)

- **Anchor: hybrid.** Canonical documents remain the source of truth in the FRACTAL folder; a compact Global Context package is mirrored into the Claude Project so every conversation is oriented even when the folder is not connected. Domain / Task / Return material is pulled from the folder as needed.
- **First pass: design the protocol first.** Agree the rules before automating anything.
- **Identity stability (remark on Principle 2).** Naming conventions and taxonomy exist to keep the system's output stable: whatever is transported outside a conversation must have exactly one identity.
- **Priority: lean.** Max declined to trade away quality, but noted the system's quality *depends on* its robustness and scalability, and that leanness serves both. Where quality is not compromised, lean is the tie-breaker.
- **Format: unify on `.md`.** Markdown everywhere, with transformation back to `.docx` when a document later needs to be presentable.
- **Folder split.** Divide the FRACTAL folder into two sections: the ChatGPT-era construction (preserved intact for perfect project history) and a new `Claude` section replicating the basic folder architecture. The Claude-era governance-protocol series begins here.
- **Automation boundary.** At the start, Claude asks before executing; Max asks when he needs something executed. Automation is introduced gradually. The process should be simplified, optimised to a point, and robust *before* it becomes fully automated.

## 4. AI Input (Claude)

- The ChatGPT-era four-layer model (Global → Domain → Task → Return) is structurally sound and ports to Claude almost one-to-one.
- Claude adds native mechanics the earlier design had to simulate: the **Project** provides cross-conversation persistence with no MCP dependency (natural home for the Global/active-Domain packages); the **MCP folder bridge** turns the document library into retrievable working memory; memory and subagents can later carry heavier retrieval/return steps.
- The projection-vs-source discipline must be binding: context packages are derived projections, never authoritative. Canonical documents are the only source of truth; a conversation is both consumer and producer.
- Automation should be incremental, consistent with Max's "robust before automated" position.

## 5. Jointly Derived Conclusions

1. A conversation represents one bounded working context, not "the project."
2. Context is an external dependency that is loaded, not history carried in the chat.
3. The project history is preserved by splitting the folder; the Claude era starts in a replicated architecture.
4. `.md` is the working format; `.docx` is an export target.
5. Leanness is the default tie-breaker under fixed quality standards.
6. The workflow is designed and governed before it is automated, and automation is introduced gradually.

## 6. Current Decisions

- **C-001 — Context Persistence Workflow adopted.** Conversations load Global → Domain → Task context, stay within their declared domain, and end by producing durable outputs, a change summary, a Return Package, a refresh list, and an unresolved list. *(Working Decision, High confidence.)*
- **C-002 — Hybrid anchoring.** Canonical documents live in the FRACTAL folder; the Global Context package is mirrored into the Claude Project. *(Working Decision.)*
- **C-003 — Projection integrity.** Context packages are labelled derived projections, cite their source documents and last-updated date, and never become the source of truth. *(Principle.)*
- **C-004 — Update ordering.** Conversation → canonical document update → protocol update (if governance/history requires) → context-package refresh. *(Principle.)*
- **C-005 — Stable artifact identity.** Every artifact transported outside a conversation carries exactly one stable identity: `Fractal_<Name>_v<major>.<minor>`, Claude-era artifacts located under `/Claude/`. Naming and taxonomy exist to keep external output unambiguous. *(Principle.)*
- **C-006 — Format.** Governed documents and packages are authored in `.md`; `.docx` is generated on demand for presentation. *(Working Decision.)*
- **C-007 — Folder split.** ChatGPT-era work is preserved intact; Claude-era work lives under `/Claude/` in a replicated architecture. *(Working Decision.)*
- **C-008 — Manual-first automation.** Claude asks before executing actions; automation is added only after the workflow is simplified, optimised, and proven robust. *(Working Decision.)*

## 7. Alternatives Considered

- **Project-only or MCP-only anchoring.** Rejected in favour of hybrid: Project-only detaches from the canonical folder; MCP-only fails when the desktop is not connected.
- **Build a working artifact before agreeing rules.** Deferred: Max chose to design the protocol first.
- **Keep `.docx` throughout.** Rejected for working documents: heavier, less diff-friendly, less machine-readable; retained only as an export target.
- **Automate the load/return cycle immediately.** Rejected: robustness must precede automation.

## 8. Assumptions

- The document corpus will keep growing; AI-assisted navigation and stable identity become more important over time.
- The Claude-era folder architecture may be renamed or reorganised as the workflow is exercised.
- The Global Context package can orient a new conversation without the full Architecture State being loaded.

## 9. Process Consequences

The Claude era operates on a bounded-conversation model with an explicit persistence loop. Project memory is preserved across conversations through canonical documents (source), context packages (projection), and return packages (transfer). The folder split gives a clean provenance boundary between the ChatGPT and Claude eras.

## 10. Decision Ledger Changes

Opened the Claude-era Governance Protocol series. Added decisions C-001 through C-008.

## 11. Open Questions (TBD)

- Whether Return Packages should also be mirrored into the Project (currently folder-only for leanness) or remain folder-only.
- When the Context Persistence Workflow should be promoted from decisions in this protocol to a standalone normative Governance Document.
- The exact trigger set and cadence for Domain-package refresh.
- The point at which specific load/return steps are judged robust enough to automate.
- Whether the ChatGPT-era files are moved into a dedicated archive subfolder (pending Max's go/no-go) or left in place.

## 12. Next Line of Research

Exercise the workflow on a real domain (candidate: Knowledge Graph or the Architecture State Master Index) so Max can observe how loading, bounded work, and return operate in practice. Calibrate the automation boundary based on that run. Promote the workflow to a standalone Governance Document once it has been run and found robust.

---

| Field | Value |
|---|---|
| Document Title | Fractal Governance Protocol — Claude Series v0.1 |
| Document Type | Governance Protocol (reasoning / decision record) |
| Version | v0.1 |
| Status | Ratified (2026-08-12, per v0.7) |
| Domain | Project Governance — Documentation & Workflow |
| Prepared By | Claude |
| Reviewed By | Max (2026-08-12, per v0.7) |
| Date | 2026-08-01 |
| Parent Protocol | ChatGPT-era Governance Protocol v0.2 (predecessor series) |
| Related Documents | proposed workflow (ChatGPT-era); Fractal Global Context v0.1; Architecture State v0.1 |
| Revision Trigger | Change to any decision C-001–C-008, or promotion of the workflow to a Governance Document |
| Document ID | DOC-01KZVYQ3ZGCT004S0AWF0N30JB (minted 2026-08-12, C-041/C-042, per v0.9) |
