---
tags:
  - aws/service
  - aws/serverless
  - aws/event-driven
domain: Integration
status: evergreen
exam_priority: ⭐⭐⭐⭐⭐
---

# Amazon EventBridge

> [!abstract] Overview
> Amazon EventBridge is a serverless event bus service that makes it easy to connect applications using data from your own applications, integrated Software-as-a-Service (SaaS) applications, and AWS services.

---

## 🚌 Event Buses & Architecture

```mermaid
graph LR
    subgraph EventSources ["Event Sources"]
        AWS_Events[AWS Services: S3, EC2, GuardDuty]
        Custom_Events[Custom Microservices]
        SaaS_Events[SaaS Partners: Datadog, Zendesk, Auth0]
    end
    
    subgraph EventBus ["EventBridge Event Buses"]
        DefaultBus[Default Bus]
        CustomBus[Custom Bus]
        PartnerBus[Partner Bus]
    end
    
    subgraph RulesEngine ["Rules & Filtering"]
        Rule1[Rule 1: Pattern Match JSON]
        Rule2[Rule 2: Schema Validation]
    end
    
    subgraph Targets ["Targets (30+ Destinations)"]
        Lambda[[AWS Lambda]]
        SQS[[Amazon SQS (Standard, FIFO, DLQ)]]
        StepFunc[[AWS Step Functions]]
        APIDest[API Destinations: External REST APIs]
    end
    
    AWS_Events --> DefaultBus
    Custom_Events --> CustomBus
    SaaS_Events --> PartnerBus
    
    DefaultBus --> Rule1
    CustomBus --> Rule1
    PartnerBus --> Rule2
    
    Rule1 --> Lambda
    Rule1 --> SQS
    Rule2 --> StepFunc
    Rule2 --> APIDest
```

---

## 🥊 EventBridge vs SNS vs SQS

| Feature | Amazon EventBridge | Amazon SNS | Amazon SQS |
| :--- | :--- | :--- | :--- |
| **Model** | **Serverless Event Bus** | **Pub/Sub Notification** | **Point-to-Point Queue** |
| **Event Routing** | **Content-based JSON pattern matching** | Topic-based + Attribute filters | Direct queue consumption |
| **SaaS Integrations** | **Native integrations with 30+ SaaS partners** | None | None |
| **Schema Registry** | **Yes** (Generates code bindings) | No | No |
| **Targets** | **30+ AWS targets + HTTP API Destinations** | SQS, Lambda, HTTP, SMS, Email | EC2, Lambda, ECS workers |
| **Event Replay** | **Yes** (Archive & replay past events) | No | No |

---

## ⚡ High-Yield Exam Tips

> [!tip] Exam Triggers
> - **"React to AWS infrastructure state changes in real time (e.g., EC2 state change, S3 upload, GuardDuty finding)"** $\rightarrow$ **Amazon EventBridge Rule**.
> - **"Trigger a third-party webhook / external REST API (e.g., Stripe, Slack, PagerDuty) directly without writing custom Lambda code"** $\rightarrow$ **EventBridge API Destinations**.
> - **"Archive events and replay them for disaster recovery or testing new microservices"** $\rightarrow$ **EventBridge Event Archiving & Replay**.
> - **"Ingest events from partner SaaS applications (Zendesk, Shopify, Datadog)"** $\rightarrow$ **EventBridge Partner Event Bus**.

---

## 🔗 Related Notes
- [[Amazon SNS & Fan-Out Pattern]]
- [[AWS Step Functions]]
- [[Decision Matrix - Decoupling & Messaging]]
- [[AWS Security Services (GuardDuty, Inspector, Macie, Security Hub)]]
