---
title: "AZ-305 High-Yield Exam Cheat Sheet"
date: 2026-09-19
tags:
  - azure/cheatsheet
  - azure/exam
  - az-305
status: evergreen
aliases:
  - "AZ-305 Cheat Sheet"
  - "Azure Exam Cheat Sheet"
---

# 🎯 AZ-305 High-Yield Exam Cheat Sheet

> [!abstract] Exam Keyword Associations & Traps
> Instant trigger words, high-probability answer mappings, and common distractor traps for the **Microsoft AZ-305: Designing Microsoft Azure Infrastructure Solutions** certification.

---

## ⚡ Instant Scenario Keyword Trigger Mappings

| If Scenario Requirement mentions... | The Correct Azure Architectural Choice is... |
| :--- | :--- |
| *"Just-In-Time role elevation with approval workflow and MFA"* | **Microsoft Entra Privileged Identity Management (PIM)** |
| *"Enforce compliance rules, tags, or allowed SKUs across subscriptions"* | **Azure Policy / Policy Initiatives** (not RBAC) |
| *"Grant a specific group ability to restart VMs in a resource group"* | **Azure RBAC** (Virtual Machine Contributor role) |
| *"Zero credentials in app code accessing Azure Key Vault or SQL"* | **Managed Identity** (System-Assigned or User-Assigned) |
| *"Synchronize on-prem AD passwords with cloud leak detection"* | **Password Hash Synchronization (PHS)** |
| *"Lift-and-shift legacy SQL Server requiring SQL Agent & Cross-DB queries"* | **Azure SQL Managed Instance** |
| *"SQL database with automatic scaling, auto-pause during idle"* | **Azure SQL Database Serverless tier** |
| *"Relational database scaling beyond 16 TB up to 100 TB with rapid restore"* | **Azure SQL Database Hyperscale tier** |
| *"Globally distributed NoSQL with multi-region active-active writes & <10ms latency"* | **Azure Cosmos DB** |
| *"Cosmos DB strict ordering and guaranteed max bounded lag"* | **Bounded Staleness consistency** |
| *"High-performance computing (HPC) or SAP HANA requiring extreme sub-ms IOPS"* | **Azure NetApp Files (ANF)** |
| *"SMB/NFS shares accessible by multiple VMs and on-prem branch cache"* | **Azure Files + Azure File Sync** |
| *"Storage archival at lowest cost, acceptable hours retrieval delay"* | **Azure Blob Archive Tier** |
| *"Prevent ransomware from deleting or modifying storage data"* | **Immutable Blob Storage with time-based retention / Legal Hold** |
| *"Global web app routing, edge caching, instant regional failover"* | **Azure Front Door** |
| *"Regional Layer 7 routing with cookie affinity and WAF inspection"* | **Azure Application Gateway v2** |
| *"Layer 4 high-throughput load balancer with internal IP"* | **Azure Load Balancer (Standard SKU)** |
| *"Private IP access to PaaS services without internet traversal"* | **Azure Private Endpoint (Azure Private Link)** |
| *"Route all outbound VNet traffic through central firewall"* | **User-Defined Route (UDR) with `0.0.0.0/0` next-hop to Virtual Appliance** |
| *"Dedicated high-speed, private fiber connection bypassing public internet"* | **Azure ExpressRoute** |
| *"Test disaster recovery without stopping replication or affecting production"* | **Azure Site Recovery (ASR) Test Failover** |
| *"Application performance monitoring, distributed tracing, dependency map"* | **Application Insights** |
| *"Query across millions of log records from multiple resources using KQL"* | **Azure Monitor Log Analytics Workspace** |
| *"Agentless discovery, dependency mapping, and sizing assessment for migration"* | **Azure Migrate** |

---

## ⚠️ Common Exam Traps & Pitfalls

> [!warning] Trap 1: RBAC vs Azure Policy
> If the question asks to prevent administrators from deploying VMs in unauthorized regions, **Azure Policy** is the answer. RBAC defines *who* can deploy, not *where* or *under what guardrails*.

> [!warning] Trap 2: Cosmos DB Consistency Levels
> - Default is **Session** (guarantees read-your-writes for the same client session).
> - If the question requires monotonic reads and linearizability across *all* global clients, choose **Strong** (note: single-region write limit).
> - If it requires deterministic staleness bounded by time or updates, choose **Bounded Staleness**.

> [!warning] Trap 3: Application Gateway vs Azure Front Door
> - **Application Gateway**: Regional Layer 7 load balancer. Cannot route traffic across multiple Azure regions.
> - **Azure Front Door**: Global Anycast Layer 7 routing and CDN. Routes traffic across multiple global Azure regions.

> [!warning] Trap 4: Azure SQL DB vs Managed Instance
> - If an application depends on **SQL Server Agent**, **Database Mail**, or cross-database `JOIN`s, **Azure SQL Database** will NOT work—you must select **Azure SQL Managed Instance**.

> [!warning] Trap 5: Storage Tier Minimum Retention Charges
> - Cool: 30 days.
> - Cold: 90 days.
> - Archive: 180 days.
> Deleting or moving blobs before the retention period incurs early deletion penalty charges.
