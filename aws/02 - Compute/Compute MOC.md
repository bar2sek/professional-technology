---
tags:
  - aws/moc
  - aws/compute
status: evergreen
---

# 💻 Compute Map of Content

> [!abstract] Overview
> AWS offers a broad compute portfolio spanning Virtual Machines (EC2), Containers (ECS/EKS/Fargate), Serverless (Lambda), and Platform-as-a-Service (App Runner/Beanstalk).

---

## 🧭 Compute Decision Map

```mermaid
graph TD
    Workload[Compute Requirement] --> Type{Workload Type}
    
    Type -->|Short / Event-Driven < 15min| Lambda[[AWS Lambda]]
    Type -->|Containerized Microservices| Containers[[Containers (ECS, EKS, Fargate)]]
    Type -->|Full OS Control / Custom Kernels| EC2[[EC2 - Elastic Compute Cloud]]
    Type -->|Simple Web App PaaS| PaaS[[AWS App Runner & Elastic Beanstalk]]
    
    EC2 --> ASG[[EC2 Auto Scaling & Load Balancing]]
    Containers --> Fargate[Fargate - Serverless Containers]
    Containers --> EC2_Node[EC2 Launch Type - Full Control]
```

---

## 📂 Compute Notes Directory

1. **[[EC2 - Elastic Compute Cloud]]**:
   - Instance types, pricing options (Spot, RI, Savings Plans), Placement Groups, ENIs.
2. **[[EC2 Auto Scaling & Load Balancing]]**:
   - Scaling policies, Launch Templates, ALB vs NLB vs GLB, Target Groups, Health Checks.
3. **[[AWS Lambda]]**:
   - Serverless event-driven execution, concurrency, cold starts, VPC networking, SnapStart.
4. **[[Containers (ECS, EKS, Fargate)]]**:
   - ECS Task Definitions, Fargate serverless containers, Kubernetes on EKS, ECR.
5. **[[AWS App Runner & Elastic Beanstalk]]**:
   - PaaS web app hosting, deployment strategies (Blue/Green, Canary, Immutable).

---

## ⚡ High-Yield Exam Comparisons

| Service | Management Overhead | Max Execution Time | Scaling Speed | Ideal For |
| :--- | :--- | :--- | :--- | :--- |
| **[[AWS Lambda]]** | Zero (Serverless) | 15 minutes | Milliseconds | Event-driven, APIs, background ETL |
| **[[Containers (ECS, EKS, Fargate)|ECS / EKS on Fargate]]** | Low (Serverless container) | Unlimited | Seconds to minutes | Long-running microservices, web apps |
| **[[EC2 - Elastic Compute Cloud]]** | High (OS patching, maintenance) | Unlimited | Minutes | Legacy apps, monolithic, custom OS/GPU |
| **[[AWS App Runner & Elastic Beanstalk|Elastic Beanstalk]]** | Medium (Managed PaaS) | Unlimited | Minutes | Quick developer deployment on standard runtimes |

---

## 🔗 Related Notes
- [[00 - Home|Master Index]]
- [[Cost Optimization Pillar]]
- [[Performance Efficiency Pillar]]
