---
title: "Bedrock Review Questions"
date: 2026-10-06
tags:
  - aws/genai
  - study/bedrock
  - active-recall
status: in-progress
aliases:
  - "Bedrock Self-Check"
  - "Bedrock Study Questions"
---

# 🎯 Bedrock Review Questions — Platform & Security

> [!tip] How to use
> Answer out loud first, then expand the callout. Each answer follows the shape **mechanism → control → trade-off**, a useful structure for reasoning about any platform control. Source material: [[Amazon Bedrock - Platform Engineering Deep Dive]].

---

## 1. Model access & pricing

> [!question]- Q1. A developer says "I enabled Claude in the console." What's wrong with that mental model today?
> There's no per-model enable step any more: serverless models are **auto-enabled** in commercial Regions (Oct 2025). Anthropic still needs a **one-time use-case form** (per account, or once at the org management account). So access is *open by default*, and the platform team must **restrict** it with IAM and **SCP model allow-lists**, not grant it through a console toggle.

> [!question]- Q2. Walk me through Bedrock's pricing options and when you'd use each.
> **On-demand** per token (default). **Service tiers**: Priority (premium, latency-critical), Standard, Flex (discounted, latency-tolerant). **Batch** (~50% off, async S3 jobs). **Provisioned Throughput** (hourly model units, optional 1- or 6-month commitment; required to serve fine-tuned models; pays while idle). **Prompt caching** for repeated long context. Trade-off: guaranteed capacity vs paying for idle capacity.

> [!question]- Q3. We keep getting ThrottlingException in production. Options?
> Quotas are per model, per Region, per account (TPM/RPM). Use a **cross-Region inference profile** (`us.` prefix) to spread load; add exponential backoff with jitter; request quota increases; buy **Provisioned Throughput** or use the **Priority** tier for critical paths; move bulk work to **batch**. Monitor CloudWatch `InvocationThrottles` and token metrics.

> [!question]- Q4. Is cross-Region inference a data-residency problem for a regulated workload?
> *Geographic* profiles (`us.`, `eu.`, `apac.`) keep processing within that geography. *Global* profiles can route to any commercial Region. An organization with residency obligations allows geographic profiles only, enforced by SCP on the allowed inference-profile ARNs. Gotcha: IAM must allow `InvokeModel` on the **profile ARN and the model ARNs in every destination Region**, and any `aws:RequestedRegion` deny SCP must include those Regions.

> [!question]- Q5. How do you charge GenAI spend back to business units?
> **Application inference profiles** — tagged profiles that wrap a model, one per team or app — feeding cost-allocation tags in Cost Explorer. Combine with AWS Budgets and Cost Anomaly Detection, and separate accounts per workload in the landing zone.

---

## 2. Knowledge Bases (RAG)

> [!question]- Q6. Explain how a Bedrock Knowledge Base works end-to-end.
> Data source (S3, SharePoint, Confluence, web crawler) → **ingestion job** parses, **chunks**, and **embeds** documents with an embedding model → vectors plus text and metadata are written to a **vector store**. At query time the question is embedded, top-k similar chunks are retrieved (with optional metadata filter and reranking), and either returned (`Retrieve`) or passed to an FM that answers with **citations** (`RetrieveAndGenerate`). Sync is incremental.

> [!question]- Q7. Which vector store would you choose, and why?
> It depends on the cost profile and features needed. **S3 Vectors**: cheapest, no idle cost, semantic-only, sub-second latency — good for internal or low-QPS RAG. **OpenSearch Serverless**: hybrid search and ms latency, but an **OCU cost floor** while idle. **Aurora pgvector**: fits Postgres shops and keeps SQL + metadata together, but you run a database. Third-party stores (Pinecone etc.) move **data outside AWS** → third-party-risk review.

> [!question]- Q8. Retrieve vs RetrieveAndGenerate?
> `Retrieve` returns chunks only: you own prompt construction, model choice, and orchestration (max control, e.g. inside an agent framework). `RetrieveAndGenerate` is fully managed RAG with citations and an optional guardrail (fastest path, less control).

> [!question]- Q9. Users report wrong answers from the KB. How do you debug?
> Check the retrieval half first: call `Retrieve` and inspect the chunks. If the right chunk isn't returned, it's a **chunking / embedding / metadata** problem — try a different chunk size or hierarchical chunking, add metadata filters, add a reranker, or use hybrid search. If the right chunk *is* returned but the answer is wrong, it's a **generation** problem: prompt template, model choice, or **contextual grounding** guardrail thresholds. Use Bedrock **RAG evaluation** to measure before and after.

> [!question]- Q10. How do you secure documents that only some users may see?
> Bedrock doesn't enforce per-user document ACLs on retrieval by itself. Options: **metadata filtering** with an entitlement attribute injected server-side (never from the client); separate KBs per data classification; or for connectors that sync ACLs, filter on them. And at the root: least-privilege KB service role, KMS CMK on the source bucket and vector store, and Macie on the source bucket for PII discovery.

---

## 3. Guardrails & responsible AI

> [!question]- Q11. What can Guardrails do?
> Content filters (including **prompt-attack** detection), denied topics, word filters, **sensitive-information** filters (PII entities + regex; **block or anonymize**), **contextual grounding** (grounding + relevance scores), and **Automated Reasoning checks**. They apply to input and/or output, are **versioned**, and are usable standalone via `ApplyGuardrail` — even for models not hosted in Bedrock.

> [!question]- Q12. How do you *guarantee* every model call goes through the approved guardrail?
> IAM condition key **`bedrock:GuardrailIdentifier`** on `InvokeModel*` / `Converse*`: deny if the request doesn't reference the approved guardrail ARN and version. That moves enforcement from application code to the **authorization layer**, where it's auditable and can't be skipped by one team's bug. Pair it with an SCP so it applies org-wide.

> [!question]- Q13. Design a guardrail for a customer-facing assistant in a regulated industry.
> Denied topics: personalized investment, tax, and legal advice. PII: **anonymize** account numbers (custom regex), SSN, and card numbers in outputs; **block** on input where appropriate. Prompt-attack filter on HIGH. Contextual grounding threshold (e.g. 0.7+) for policy answers. Word filter for competitor names. Use a versioned guardrail referenced by a version number in prod, and test against a red-team prompt set before promoting.

---

## 4. Agents

> [!question]- Q14. Bedrock Agents or AgentCore?
> **AgentCore** for anything new. Bedrock Agents was renamed **Agents Classic** and put in **maintenance mode** in mid-2026 — closed to new customers, model catalog frozen. AgentCore is framework- and model-agnostic: Runtime (isolated sessions), Gateway (APIs and Lambda as **MCP** tools), Memory, Identity (OAuth vault, on-behalf-of), and Observability (OTel).

> [!question]- Q15. What's the biggest security risk with agents, and how do you control it?
> **Excessive agency** — an agent with broad tool permissions plus prompt injection (e.g. from a retrieved document) equals an attacker-controlled actor. Controls: least-privilege tool scopes in **Gateway**; agents act **on behalf of the user** with that user's entitlements via **AgentCore Identity** rather than a god-mode service role; human-in-the-loop / return-of-control for state-changing actions such as payments; prompt-attack guardrail; full trace logging.

---

## 5. Private networking & security controls

> [!question]- Q16. How do you make sure Bedrock traffic never touches the internet?
> **Interface VPC endpoints** (PrivateLink) for `bedrock-runtime`, `bedrock-agent-runtime` (and `bedrock` / `bedrock-agent` for build time), with private DNS. **Endpoint policies** limit principals and models. An IAM/SCP **deny unless `aws:SourceVpce` matches** stops calls from anywhere else, including a laptop with stolen credentials. On-prem reaches the endpoints over Direct Connect/VPN with Route 53 Resolver inbound endpoints. FIPS endpoints are available in US Regions.

> [!question]- Q17. Does AWS or the model provider see our prompts? Train on them?
> No. Prompts and completions are **not used to train** models and **not shared with providers**; models run in AWS-operated deployment accounts the provider can't access. Data is encrypted in transit and at rest (CMK supported). Data stays in-Region unless you opt into cross-Region inference.

> [!question]- Q18. What are Bedrock API keys, and how should an enterprise govern them?
> Bearer-token auth (Jul 2025). Short-term keys derive from a role session; long-term keys are IAM-user **service-specific credentials**. In a security-sensitive org, **deny them via SCP** (`iam:CreateServiceSpecificCredential`, `bedrock:CallWithBearerToken`), or allow only short-term keys via `bedrock:BearerTokenType` with a max age via `iam:ServiceSpecificCredentialAgeDays`. Gotcha: for long-term keys, SCPs evaluate against the **owning IAM user**.

> [!question]- Q19. What do you log, and what's the catch?
> **CloudTrail** for API activity (who, which model, when). **Model invocation logging** — off by default — for full prompts and responses to CloudWatch Logs and/or S3. Catch: invocation logs **contain the sensitive data** — CMK-encrypt, restrict access, set retention, ship to a log-archive account, and mask PII upstream with guardrails.

> [!question]- Q20. How would you lay out Bedrock across a multi-account landing zone?
> Workload accounts invoke Bedrock under SCP guardrails: model allow-list, guardrail enforcement, API-key deny, Region and residency limits, `aws:SourceVpce`. A **security account** owns guardrail standards and Security Hub. A **log-archive account** receives invocation logs and CloudTrail. A **shared-services network account** hosts the interface endpoints, shared via Transit Gateway and Route 53 private hosted zones. All of it is infrastructure-as-code with PR-gated plans.

> [!question]- Q21. How does model risk management apply to an FM you didn't build?
> Frameworks such as NIST AI RMF, ISO/IEC 42001, or sector rules (e.g. SR 11-7 in US financial services) all treat it as a "model" in your inventory: document intended use and limitations; **validate** with Bedrock model evaluation (automatic metrics + LLM-as-judge + human review) on *your* tasks; monitor ongoing performance and drift; control changes — pin model versions and re-validate on upgrade. Vendor documentation (model cards, AWS AI Service Cards) supports but doesn't replace your validation.

---

## 6. Terraform / IaC

> [!question]- Q22. What IAM does a CI pipeline need to deploy a Knowledge Base, and what's the trap?
> Bedrock-agent + S3 Vectors management actions, plus **`iam:PassRole`** to hand the KB its service role. The trap: unscoped `PassRole` is a **privilege-escalation path** — pass a powerful role to a service and borrow its permissions. Scope it to `role/role-aws-bedrock-*` with condition **`iam:PassedToService = bedrock.amazonaws.com`**, and cap every CI-created role with a **permissions boundary**.

> [!question]- Q23. What's not declarative about a Terraform-managed KB?
> **Ingestion** (`StartIngestionJob`) is a runtime operation, not a resource — run it as a post-apply CI step or on S3 event triggers. Also: vector index dimension and bucket encryption are **immutable** (changes force replacement), and the embedding model choice is effectively permanent for that index.

---

## 🔗 Related Notes
- [[Amazon Bedrock - Platform Engineering Deep Dive]]
- [[Generative AI MOC]]
- [[AWS Organizations & SCPs]] · [[AWS IAM (Policies, Roles, Delegation)]]
