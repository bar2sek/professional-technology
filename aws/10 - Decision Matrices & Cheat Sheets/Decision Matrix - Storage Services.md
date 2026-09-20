---
tags:
  - aws/matrix
  - aws/storage
  - aws/exam-high-priority
status: evergreen
---

# Decision Matrix: AWS Storage Services

> [!abstract] Overview
> Quick-reference comparison of Object Storage (S3), Block Storage (EBS, Instance Store), and File Storage (EFS, FSx family) to determine the right storage choice for cost, performance, and accessibility.

---

## 🧭 Storage Selection Decision Flowchart

```mermaid
graph TD
    Req[Storage Requirement] --> Type{Storage Type}
    
    Type -->|Object: Web, Backup, Media, Data Lake| S3[[Amazon S3 Deep Dive]]
    Type -->|Block: Dedicated Disk for Single EC2| Block{Persistence Need}
    Type -->|File: Concurrent Shared Access| File{OS & Protocol}
    Type -->|Hybrid: On-Prem Integration| Hybrid[[AWS Storage Gateway & DataSync]]
    
    Block -->|Persistent across reboots/stops| EBS[[Amazon EBS & Instance Store|EBS: gp3 / io2]]
    Block -->|Temporary / Ephemeral / Ultra-fast NVMe| InstStore[[Amazon EBS & Instance Store|Instance Store]]
    
    File -->|Linux / POSIX / NFS| EFS[[Amazon EFS & FSx|Amazon EFS]]
    File -->|Windows / SMB / Active Directory| FSxW[[Amazon EFS & FSx|FSx for Windows File Server]]
    File -->|High Performance Compute / Lustre / S3 Linked| FSxL[[Amazon EFS & FSx|FSx for Lustre]]
    File -->|Multi-Protocol NFS+SMB / NetApp ONTAP| FSxO[[Amazon EFS & FSx|FSx for NetApp ONTAP]]
```

---

## 📊 Comprehensive Storage Feature Comparison

| Storage Service | Protocol | Access Scope | Max Throughput / IOPS | Durability | Key Differentiator |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[[Amazon S3 Deep Dive|Amazon S3]]** | HTTPS / REST | Global (Internet / VPC) | 3,500 PUT / 5,500 GET per prefix | **11 9s (99.999999999%)** | Unlimited scale, tiering lifecycle, lowest cost |
| **[[Amazon EBS & Instance Store|Amazon EBS gp3]]** | Block | Single EC2 (AZ-bound) | 1,000 MB/s / 16,000 IOPS | 99.8% - 99.9% | Boot volumes, general applications |
| **[[Amazon EBS & Instance Store|Amazon EBS io2]]** | Block | Single EC2 (Multi-Attach) | 4,000 MB/s / 256,000 IOPS | **99.999%** | Sub-ms latency, mission-critical DBs |
| **[[Amazon EBS & Instance Store|Instance Store]]** | Block | Single EC2 (Physical NVMe)| Millions of IOPS | **Ephemeral** (0 durability) | Ultra-low latency caches, scratch buffers |
| **[[Amazon EFS & FSx|Amazon EFS]]** | NFSv4 | Thousands of Linux EC2/ECS | Elastic (GB/s scale) | **11 9s (Multi-AZ)** | Shared Linux POSIX file system |
| **[[Amazon EFS & FSx|FSx for Windows]]** | SMB | Windows & Linux instances | Up to 12 GB/s | High (Multi-AZ) | Native Microsoft AD, DFS, shadow copies |
| **[[Amazon EFS & FSx|FSx for Lustre]]** | Lustre (POSIX)| Thousands of compute nodes | **Hundreds of GB/s & Millions IOPS**| High | High-throughput HPC linked to S3 |

---

## ⚡ Instant Exam Clues

| Exam Clue / Keyword | Correct Storage Decision |
| :--- | :--- |
| *"Shared file storage mounted concurrently across multiple Linux EC2 instances in different AZs"* | **Amazon EFS** |
| *"Windows application requiring Active Directory integration and shared SMB storage"* | **FSx for Windows File Server** |
| *"High-performance machine learning training or HPC computing directly on S3 data"* | **FSx for Lustre** |
| *"Highest possible IOPS for a temporary video processing scratch disk at lowest cost"* | **EC2 Instance Store** |
| *"Migrate on-prem virtual tape backups to AWS without changing backup software"* | **AWS Storage Gateway (Tape Gateway)** |
| *"Lowest cost long-term archival for compliance where 12-hour retrieval delay is acceptable"* | **S3 Glacier Deep Archive** |
| *"WORM storage compliance where no one (including root) can delete objects for 7 years"* | **S3 Object Lock in Compliance Mode** |

---

## 🔗 Related Notes
- [[Storage MOC]]
- [[Amazon S3 Deep Dive]]
- [[S3 Storage Classes & Lifecycle]]
- [[Amazon EBS & Instance Store]]
- [[Amazon EFS & FSx]]
