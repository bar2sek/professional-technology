---
tags:
  - aws/cheatsheet
  - aws/exam-high-priority
  - aws/saa-c03
status: evergreen
---

# SAA-C03 High-Yield Exam Cheat Sheet

> [!abstract] Overview
> High-yield, rapid-review cheat sheet containing high-frequency exam keyword pairings, architectural axioms, and trap avoidance rules for the **AWS Solutions Architect - Associate (SAA-C03)** exam.

---

## 🎯 Instant Keyword-to-Service Pairings

| Exam Keyword / Scenario Clue | The Immediate Answer |
| :--- | :--- |
| *"Zero downtime deployment with immediate rollback capability"* | **Blue/Green Deployment** or **Beanstalk Immutable** |
| *"Microsecond latency for DynamoDB read-heavy traffic"* | **DynamoDB Accelerator (DAX)** |
| *"High read traffic on Amazon RDS MySQL causing slowdown"* | **ElastiCache (Redis)** or **RDS Read Replicas** |
| *"Overcome database connection limits caused by serverless Lambda"* | **Amazon RDS Proxy** |
| *"Audit API calls across all AWS regions to find who deleted a resource"* | **AWS CloudTrail Multi-Region Trail** |
| *"Identify EC2 RAM / Memory utilization or free disk space"* | **CloudWatch Unified Agent** (installed on OS) |
| *"Scale EC2 instances based on backlog of SQS messages"* | **Target Tracking ASG** on `ApproximateNumberOfMessages` |
| *"Enforce encryption in transit for S3 uploads"* | Bucket Policy denying requests where `aws:SecureTransport: false` |
| *"Strict compliance: no one (including root) can delete objects for 7 years"* | **S3 Object Lock in Compliance Mode** |
| *"Accelerate static/dynamic web content globally"* | **Amazon CloudFront** |
| *"Accelerate non-HTTP (TCP/UDP) or provide 2 fixed static Anycast IPs"* | **AWS Global Accelerator** |
| *"Connect thousands of VPCs and on-premise networks with transitive routing"* | **AWS Transit Gateway** |
| *"Private connection to S3/DynamoDB without NAT Gateway or data charges"* | **VPC Gateway Endpoint** (Free) |
| *"Share microservice privately across accounts with overlapping CIDRs"* | **AWS PrivateLink (Interface Endpoint)** |
| *"Run containers without provisioning or managing EC2 servers"* | **AWS Fargate** |
| *"Tightly coupled HPC / MPI workloads requiring lowest network latency"* | **Cluster Placement Group + Elastic Fabric Adapter (EFA)** |
| *"Longest retention, lowest cost storage for compliance (12h retrieval OK)"* | **S3 Glacier Deep Archive** |
| *"Automated remediation of non-compliant security group changes"* | **AWS Config Rule + SSM Automation Runbook** |
| *"Detect compromised EC2 instance communicating with crypto-mining pool"*| **Amazon GuardDuty** |
| *"Scan container images in ECR for CVE software vulnerabilities"* | **Amazon Inspector** |
| *"Scan S3 buckets for sensitive PII, credit card numbers, and credentials"* | **Amazon Macie** |
| *"Decouple one publisher to multiple independent parallel worker queues"* | **SNS + SQS Fan-Out Pattern** |
| *"Coordinate distributed microservices with automated rollback (Saga)"* | **AWS Step Functions** |
| *"Central governance: prevent member accounts from disabling CloudTrail"* | **AWS Organizations SCP (Service Control Policy)** |
| *"SSH-less, secure browser terminal access to private EC2 without Port 22"*| **AWS Systems Manager Session Manager** |

---

## ⚠️ 10 Golden Architectural Axioms (Never Forget on Exam)

1. **Stateful vs Stateless Firewalls**:
   - **Security Groups** are *Stateful* (Inbound return traffic automatically allowed; Allow rules only).
   - **NACLs** are *Stateless* (Must allow ephemeral ports `1024-65535` on return; Allow & Deny rules).
2. **Subnet Bounds**:
   - A Subnet **NEVER spans multiple Availability Zones**. It resides strictly in **1 AZ**.
3. **Multi-AZ vs Read Replicas**:
   - **Multi-AZ** = High Availability & Disaster Recovery (Synchronous, standby is passive).
   - **Read Replicas** = Scalability & Performance (Asynchronous, replicas serve reads).
4. **NAT Gateway Placement**:
   - NAT Gateways **MUST be placed in a Public Subnet** and have an **Elastic IP (EIP)** attached.
5. **Gateway Endpoints vs Interface Endpoints**:
   - **Gateway Endpoints** are **FREE** and support **ONLY S3 and DynamoDB**.
   - **Interface Endpoints (PrivateLink)** cost money and support almost all AWS services + SaaS.
6. **Spot Instances**:
   - Spot instances can be terminated with **2 minutes notice**. Use ONLY for stateless, fault-tolerant, batch workloads.
7. **KMS Envelope Encryption**:
   - Customer Master Key (CMK) never leaves KMS. CMK encrypts Data Encryption Key (DEK). DEK encrypts data.
8. **IAM Evaluation**:
   - `Explicit Deny > Explicit Allow > Default Deny`.
9. **SQS Extended Client**:
   - For messages $> 256\text{ KB}$ up to $2\text{ GB}$, store message body in **Amazon S3** and send pointer via SQS.
10. **Disaster Recovery Hierarchy**:
    - `Backup & Restore` (Hours/Days, \$) $\rightarrow$ `Pilot Light` (10s mins, \$\$) $\rightarrow$ `Warm Standby` (Minutes, \$\$\$) $\rightarrow$ `Active-Active` (Seconds, \$\$\$\$).

---

## 🔗 Related Notes
- [[00 - Home|Master Index]]
- [[Well-Architected Framework MOC]]
- [[Decision Matrix - Database Selection]]
- [[Decision Matrix - Storage Services]]
- [[Decision Matrix - Decoupling & Messaging]]
- [[Decision Matrix - Hybrid Connectivity]]
