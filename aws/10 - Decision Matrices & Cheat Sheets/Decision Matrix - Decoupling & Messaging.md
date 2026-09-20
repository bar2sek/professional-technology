---
tags:
  - aws/matrix
  - aws/messaging
  - aws/integration
  - aws/exam-high-priority
status: evergreen
---

# Decision Matrix: Decoupling & Messaging

> [!abstract] Overview
> Guide to choosing the right integration pattern across SQS, SNS, EventBridge, Kinesis, and Step Functions based on communication style (Queue vs PubSub vs Event Bus vs Workflow vs Streaming).

---

## 🧭 Messaging Pattern Decision Tree

```mermaid
graph TD
    Req[Integration Requirement] --> Comm{Communication Style}
    
    Comm -->|Pull Queue / Buffer / Decouple 1:1| SQS[[Amazon SQS (Standard, FIFO, DLQ)]]
    Comm -->|Push Pub/Sub / Broadcast 1:Many / Push Notifications| SNS[[Amazon SNS & Fan-Out Pattern]]
    Comm -->|Event-Driven Bus / SaaS Partner / JSON Content Filtering| EB[[Amazon EventBridge]]
    Comm -->|Multi-Step Stateful Workflow / Saga Orchestration| SF[[AWS Step Functions]]
    Comm -->|Real-Time Big Data Streaming / Replayable Multi-Consumer| Kinesis[[Amazon Kinesis (Streams, Firehose, Analytics)]]
    Comm -->|Legacy On-Prem Message Broker Migration JMS/AMQP| MQ[Amazon MQ: ActiveMQ / RabbitMQ]
```

---

## 📊 Comprehensive Messaging Comparison

| Dimension | Amazon SQS | Amazon SNS | Amazon EventBridge | Amazon Kinesis Streams | AWS Step Functions | Amazon MQ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Model** | **Pull (Queue)** | **Push (Pub/Sub)**| **Push (Event Bus)**| **Pull (Shard Sharding)**| **Stateful Orchestrator**| **Broker (JMS/AMQP)** |
| **Message Ordering** | FIFO (optional) | FIFO (optional) | No strict order | **Strict per shard** | Sequential execution | Supported |
| **Delivery Model** | 1 consumer per msg | Broadcast to all | Filtered route | Multi-consumer | Orchestrated tasks | Queue / Topic |
| **Data Retention**| 1 min - 14 days | Transient (none) | 1 - 24 hrs (Archive)| **24 hrs - 365 days** | Up to 1 year | Configurable |
| **Payload Size** | 256 KB | 256 KB | 256 KB | 1 MB / record | 256 KB | Broker dependent |
| **Serverless?** | **Yes** | **Yes** | **Yes** | On-Demand or Shards | **Yes** | ❌ Managed servers |

---

## ⚡ Instant Exam Clues

| Exam Clue / Keyword | Correct Architecture Decision |
| :--- | :--- |
| *"Decouple web frontend from batch worker tier to prevent dropped requests"* | **Amazon SQS** |
| *"Send one event to multiple distinct queues for parallel independent processing"* | **SNS + SQS Fan-Out Pattern** |
| *"Trigger AWS Lambda or Step Functions based on changes in SaaS tools (Datadog/Shopify)"* | **Amazon EventBridge (Partner Bus)** |
| *"Complex multi-step order checkout workflow with error handling and compensating rollbacks"* | **AWS Step Functions (Saga Pattern)** |
| *"Multiple analytics consumers reading real-time streaming data at their own individual pace"* | **Amazon Kinesis Data Streams** |
| *"Migrate existing enterprise application using Apache ActiveMQ or RabbitMQ with zero rewrite"*| **Amazon MQ** |
| *"Deliver real-time clickstream data directly to S3 or Redshift with zero consumer code"* | **Amazon Kinesis Data Firehose** |

---

## 🔗 Related Notes
- [[Integration MOC]]
- [[Amazon SQS (Standard, FIFO, DLQ)]]
- [[Amazon SNS & Fan-Out Pattern]]
- [[Amazon EventBridge]]
- [[AWS Step Functions]]
- [[Amazon Kinesis (Streams, Firehose, Analytics)]]
