---
tags:
  - aws/moc
  - aws/monitoring
  - aws/governance
status: evergreen
---

# 📊 Monitoring & Governance Map of Content

> [!abstract] Overview
> AWS provides deep operational visibility and governance tools: **CloudWatch** (performance metrics, logs, alarms), **CloudTrail** (API call auditing), **AWS Config** (resource compliance and drift tracking), and **Systems Manager** (operational fleet automation).

---

## 🧭 The Observability & Governance Triad

```mermaid
graph TD
    System[AWS Environment] --> Ops{Telemetry & Audit}
    
    Ops -->|Performance & Metrics| CW[[Amazon CloudWatch & CloudTrail|Amazon CloudWatch]]
    Ops -->|Who Did What & When API Audit| CT[[Amazon CloudWatch & CloudTrail|AWS CloudTrail]]
    Ops -->|Resource Configuration & Compliance Rules| Cfg[[AWS Config & Systems Manager|AWS Config]]
    Ops -->|Fleet Node Management & Automation| SSM[[AWS Config & Systems Manager|AWS Systems Manager]]
```

---

## 📂 Monitoring Notes Directory

1. **[[Amazon CloudWatch & CloudTrail]]**:
   - CloudWatch Metrics, Alarms, Logs Insights, Synthetics vs CloudTrail Management Events, Data Events, Insights, Multi-Region Trail.
2. **[[AWS Config & Systems Manager]]**:
   - AWS Config managed rules, Conformance packs, Automated remediation via SSM Automation, Session Manager (SSH-less), Patch Manager.

---

## ⚡ High-Yield Governance Rule Comparison

| Service | Answers the Question... | Retention / Storage | Primary Action |
| :--- | :--- | :--- | :--- |
| **[[Amazon CloudWatch & CloudTrail|Amazon CloudWatch]]** | *"How are my resources performing right now?"* | 15 months (metrics); configurable (logs) | Triggers Auto Scaling & SNS Alarms |
| **[[Amazon CloudWatch & CloudTrail|AWS CloudTrail]]** | *"Who made that API call, from what IP, and when?"* | 90 days (Event History) / Unlimited in S3 | Forensic security audit, compliance verification |
| **[[AWS Config & Systems Manager|AWS Config]]** | *"Are my resources configured according to compliance policies?"* | Timeline history stored in S3 | Evaluates compliance, records config drift, triggers auto-remediation |
| **[[AWS Config & Systems Manager|AWS Systems Manager]]** | *"How do I operate and patch my server fleet securely?"* | Session logs stored in S3/CloudWatch | Remote command execution, SSH-less shell, patch baselines |

---

## 🔗 Related Notes
- [[00 - Home|Master Index]]
- [[Operational Excellence Pillar]]
- [[Security Pillar]]
