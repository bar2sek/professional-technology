---
title: "Identity, Governance & Security MOC"
date: 2026-09-19
tags:
  - azure/security
  - azure/identity
  - azure/governance
  - azure/moc
status: evergreen
aliases:
  - "Identity & Governance MOC"
  - "Azure Security MOC"
---

# 🔐 Identity, Governance & Security MOC

> [!abstract] AZ-305 Domain 1 Core
> Covers identity lifecycle, hybrid identity, enterprise governance hierarchies, access control, secrets management, and cloud security posture.

---

## 🏛️ Governance Hierarchy Architecture

```mermaid
graph TD
    Tenant[Root Tenant / Microsoft Entra ID]
    RMG[Root Management Group]
    Tenant --> RMG
    
    RMG --> MG_Platform[Platform MG]
    RMG --> MG_Workloads[Workloads MG]
    RMG --> MG_Sandbox[Sandbox MG]

    MG_Platform --> Sub_Identity[Identity Subscription]
    MG_Platform --> Sub_Net[Connectivity Subscription]
    MG_Platform --> Sub_Sec[Management / Security Sub]

    MG_Workloads --> Sub_Prod[Prod Subscriptions]
    MG_Workloads --> Sub_NonProd[Non-Prod Subscriptions]

    Sub_Prod --> RG1[App-Prod-RG]
    Sub_Prod --> RG2[Data-Prod-RG]

    classDef mg fill:#0078D4,stroke:#005A9E,color:#fff;
    classDef sub fill:#2D7D9A,stroke:#1A536B,color:#fff;
    classDef rg fill:#388E3C,stroke:#1B5E20,color:#fff;
    class RMG,MG_Platform,MG_Workloads,MG_Sandbox mg;
    class Sub_Identity,Sub_Net,Sub_Sec,Sub_Prod,Sub_NonProd sub;
    class RG1,RG2 rg;
```

---

## 🔑 Core Services & Concepts

### 1. Microsoft Entra ID (formerly Azure Active Directory)
- **Tenants & Directories**: Flat organization boundary.
- **Hybrid Identity Models**:
  - **Password Hash Synchronization (PHS)**: Recommended for most enterprises (easiest, supports leaked credential detection).
  - **Pass-through Authentication (PTA)**: Password validated against on-prem domain controller without storing hashes in cloud.
  - **Federation (AD FS / Ping / Okta)**: Real-time authentication redirect; high operational overhead.
- **Conditional Access**: Zero Trust policy engine evaluating user, device, location, client app, and risk level before granting access.
- **Privileged Identity Management (PIM)**: Just-In-Time (JIT) role activation, time-bound access, approval workflows, MFA enforcement on elevation.

### 2. Azure RBAC vs Azure Policy
| Dimension | Azure RBAC | Azure Policy |
| :--- | :--- | :--- |
| **Purpose** | *Who* can perform actions (*Authentication/Authorization*) | *What* can be created or configured (*Compliance & Guardrails*) |
| **Enforcement** | Grants permissions (User/Group/SPN/Managed Identity) | Blocks non-compliant requests or remediates settings |
| **Example** | Grant User A `Virtual Machine Contributor` on Resource Group B | Deny VM creation outside `eastus` or without tag `CostCenter` |

### 3. Managed Identities for Azure Resources
- **System-Assigned**: Tied directly to the lifecycle of the Azure resource (e.g. VM, Function). Deleted when the resource is deleted.
- **User-Assigned**: Standalone Azure resource lifecycle, can be assigned to multiple VMs or containers.
- **Key Advantage**: Zero credentials in code, automated token rotation via Azure IMDS endpoint (`http://169.254.169.254/metadata/identity/oauth2/token`).

### 4. Secrets & Key Management
- **Azure Key Vault**: Secrets, SSL/TLS certificates, and cryptographic keys (backed by FIPS 140-2 Level 2 validated HSMs).
- **Azure Dedicated / Managed HSM**: Single-tenant, FIPS 140-2 Level 3 validated hardware security modules for strict regulatory compliance.

### 5. Posture & Threat Detection
- **Microsoft Defender for Cloud**: Cloud Security Posture Management (CSPM) and Cloud Workload Protection Platform (CWPP).
- **Microsoft Sentinel**: Cloud-native SIEM and SOAR solution ingesting logs from Entra ID, Azure Activity Log, firewalls, and multi-cloud sources.
