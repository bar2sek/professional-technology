---
tags:
  - aws/service
  - aws/storage
domain: Storage
status: evergreen
exam_priority: ⭐⭐⭐⭐⭐
---

# Amazon EFS & FSx

> [!abstract] Overview
> AWS managed file storage services offer shared, concurrent access for multiple compute instances. **Amazon EFS** is built for Linux NFS workloads, while the **Amazon FSx** family provides specialized file systems (Windows SMB, Lustre HPC, NetApp ONTAP, OpenZFS).

---

## 🌲 File Storage Selection Decision Tree

```mermaid
graph TD
    FileNeed[Shared File System Requirement] --> OS{Workload / OS}
    
    OS -->|Linux NFS POSIX| EFS[[Amazon EFS & FSx|Amazon EFS]]
    OS -->|Windows SMB / Active Directory| FSxW[FSx for Windows File Server]
    OS -->|HPC / High Throughput / S3 Linked| FSxL[FSx for Lustre]
    OS -->|Multi-Protocol NFS+SMB / SnapMirror| FSxO[FSx for NetApp ONTAP]
```

---

## 1. Amazon EFS (Elastic File System)
- **Protocol**: NFSv4.1 / NFSv4.0 (Linux only).
- **Scale**: Scales automatically up to petabytes without provisioning storage.
- **Availability**: **Regional Multi-AZ** (replicated across 3 AZs) or **One Zone** (cheaper for non-critical dev).
- **Performance Modes**:
  - *General Purpose*: Default; lowest latency for web serving, CMS, home directories.
  - *Max I/O*: High aggregate throughput and IOPS for big data and parallel processing.
- **Throughput Modes**:
  - *Elastic*: Automatically scales throughput based on workload demand.
  - *Provisioned*: Dedicated throughput regardless of stored volume size.
- **EFS Lifecycle Management**: Automatically moves files not accessed for X days to **EFS Infrequent Access (EFS-IA)** or **EFS Archive**.

---

## 2. Amazon FSx Family Comparison

| FSx Service | Native Protocol | Integration / Features | Best Use Case |
| :--- | :--- | :--- | :--- |
| **FSx for Windows File Server** | **SMB (2.0 to 3.1.1)** | Microsoft Active Directory, Windows ACLs, DFS Namespaces, Multi-AZ | Windows applications, SharePoint, IIS, enterprise file shares |
| **FSx for Lustre** | **POSIX / Lustre** | **Direct link with Amazon S3** (reads from and writes back to S3) | High Performance Computing (HPC), financial modeling, ML training |
| **FSx for NetApp ONTAP** | **NFS, SMB, iSCSI** | Snapshot clones, deduplication, NetApp SnapMirror replication | Enterprise migration from on-prem NetApp, multi-protocol access |
| **FSx for OpenZFS** | **NFS** | ZFS snapshots, compression, single-digit microsecond latencies | High IOPS Linux workloads migrating from ZFS |

---

## ⚡ High-Yield Exam Tips

> [!tip] Exam Triggers
> - **"Shared file storage across thousands of EC2 instances and Lambda functions running Linux"** $\rightarrow$ **Amazon EFS**.
> - **"Enterprise Windows application requiring Active Directory domain join and SMB shares"** $\rightarrow$ **FSx for Windows File Server**.
> - **"HPC workload that needs to process huge datasets stored in Amazon S3 at hundreds of GB/s throughput"** $\rightarrow$ **FSx for Lustre**.
> - **"Multi-protocol (NFS + SMB + iSCSI) storage with block-level deduplication"** $\rightarrow$ **FSx for NetApp ONTAP**.

---

## 🔗 Related Notes
- [[Amazon EBS & Instance Store]]
- [[Amazon S3 Deep Dive]]
- [[Decision Matrix - Storage Services]]
- [[Performance Efficiency Pillar]]
