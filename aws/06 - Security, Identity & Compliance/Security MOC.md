---
tags:
  - aws/moc
  - aws/security
status: evergreen
---

# 🛡️ Security, Identity & Compliance Map of Content

> [!abstract] Overview
> AWS Security services protect data, identities, and workloads with fine-grained access control (IAM, Organizations, SCPs), cryptographic protection (KMS, Secrets Manager), and automated intelligence (GuardDuty, Inspector, Macie, Security Hub).

---

## 🧭 AWS Security Landscape

```mermaid
graph TD
    Security[AWS Security Ecosystem]
    
    Security --> Identity[1. Identity & Governance]
    Security --> DataProtection[2. Data Protection & Cryptography]
    Security --> ThreatDetection[3. Threat Detection & Audit]
    Security --> NetworkSec[4. Perimeter Security]
    
    Identity --> IAM[[AWS IAM (Policies, Roles, Delegation)]]
    Identity --> Orgs[[AWS Organizations & SCPs]]
    DataProtection --> KMS[[KMS & Secrets Manager]]
    ThreatDetection --> SecServices[[AWS Security Services (GuardDuty, Inspector, Macie, Security Hub)]]
    NetworkSec --> NetSec[[Network Security (Security Groups, NACLs, WAF, Shield)]]
```

---

## 📂 Security Notes Directory

1. **[[AWS IAM (Policies, Roles, Delegation)]]**:
   - Policy evaluation logic (Explicit Deny > Allow > Default Deny), Permission Boundaries, IAM Roles, STS, Instance Profiles.
2. **[[AWS Organizations & SCPs]]**:
   - Multi-account structure, Service Control Policies (SCPs), Consolidated Billing, AWS Control Tower.
3. **[[KMS & Secrets Manager]]**:
   - KMS key types (Customer Managed vs AWS Managed), Envelope encryption, Secrets Manager automatic rotation vs SSM Parameter Store.
4. **[[AWS Security Services (GuardDuty, Inspector, Macie, Security Hub)]]**:
   - GuardDuty (ML threat detection), Inspector (Vulnerability CVE scanning), Macie (PII discovery in S3), Security Hub (Posture aggregation).

---

## ⚡ High-Yield Security Comparison

| Service | Category | Core Input Sources | Primary Output / Action |
| :--- | :--- | :--- | :--- |
| **[[AWS Security Services (GuardDuty, Inspector, Macie, Security Hub)|Amazon GuardDuty]]** | Intelligent Threat Detection | VPC Flow Logs, CloudTrail, DNS Logs, EKS Logs, S3 Events | Security findings on compromised instances, unauthorized behavior |
| **[[AWS Security Services (GuardDuty, Inspector, Macie, Security Hub)|Amazon Inspector]]** | Automated Vulnerability Assessment | EC2 software inventory, ECR container images, Lambda code | CVE vulnerability reports and remediation guidance |
| **[[AWS Security Services (GuardDuty, Inspector, Macie, Security Hub)|Amazon Macie]]** | Data Privacy & Sensitive Data Scanner | Amazon S3 object contents | Identifies PII, credit card numbers, credentials in S3 |
| **[[AWS Security Services (GuardDuty, Inspector, Macie, Security Hub)|AWS Security Hub]]** | Centralized Security Posture (CSPM) | Aggregates findings from GuardDuty, Inspector, Macie, Config | Single pane of glass compliance score against CIS / PCI-DSS |

---

## 🔗 Related Notes
- [[00 - Home|Master Index]]
- [[Security Pillar]]
- [[Network Security (Security Groups, NACLs, WAF, Shield)]]
