---
tags:
  - aws/moc
  - aws/integration
  - aws/messaging
status: evergreen
---

# 📨 Application Integration & Messaging Map of Content

> [!abstract] Overview
> Application integration services enable decoupled, asynchronous communication between microservices, distributed systems, and serverless architectures.

---

## 🧭 Messaging & Integration Decision Map

```mermaid
graph TD
    Message[Integration Need] --> Type{Pattern}
    
    Type -->|Point-to-Point Queue / Buffer / Decouple| SQS[[Amazon SQS (Standard, FIFO, DLQ)]]
    Type -->|Pub/Sub 1-to-Many / Fan-Out / Push Notifications| SNS[[Amazon SNS & Fan-Out Pattern]]
    Type -->|Event Bus / Content Filtering / SaaS Integrations| EventBridge[[Amazon EventBridge]]
    Type -->|Visual Workflow Orchestration / Sagas| StepFunctions[[AWS Step Functions]]
    Type -->|Real-Time Streaming / Multi-Consumer Shards| Kinesis[[Amazon Kinesis (Streams, Firehose, Analytics)]]
    
    SNS -->|Fan-out to multiple queues| SQS
    EventBridge -->|Route events| StepFunctions
    EventBridge -->|Route events| SQS
```

---

## 📂 Integration Notes Directory

1. **[[Amazon SQS (Standard, FIFO, DLQ)]]**:
   - Standard vs FIFO queues, Visibility Timeout, Long Polling vs Short Polling, Dead-Letter Queues (DLQ).
2. **[[Amazon SNS & Fan-Out Pattern]]**:
   - Pub/Sub topics, Fan-Out architectural pattern, Message filtering policies, SNS FIFO.
3. **[[Amazon EventBridge]]**:
   - Event buses (Default, Custom, Partner), Schema Registry, Event filtering & content matching, API Destinations.
4. **[[AWS Step Functions]]**:
   - State Machines, Standard vs Express workflows, Task / Choice / Map states, Distributed Saga pattern.
5. **[[Amazon Kinesis (Streams, Firehose, Analytics)]]**:
   - Kinesis Data Streams vs Data Firehose vs Data Analytics, Shard capacity, Kinesis vs SQS.

---

## 📊 Integration Comparison Matrix

| Feature | Amazon SQS | Amazon SNS | Amazon EventBridge | Amazon Kinesis Streams | AWS Step Functions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Model** | **Pull (Queue)** | **Push (Pub/Sub)** | **Push (Event Bus)** | **Pull (Partition/Shard)**| **Orchestration** |
| **Ordering** | FIFO (optional) | FIFO (optional) | No strict order | **Strict order per shard**| Workflow sequence |
| **Data Retention**| 1 min - 14 days (default 4d)| Transient (no storage)| 1 - 24 hours (Archive) | **24 hours - 365 days** | Up to 1 year |
| **Multiple Consumers**| 1 message consumed by 1 worker | Broadcast to all subscribers | Route based on rules | Multi-consumer replay | Orchestrates multiple tasks |
| **Best For** | Work queue, decoupling, burst smoothing | Fan-out, instant alerts, push SMS/Email | Enterprise events, SaaS triggers | Real-time clickstreams, IoT telemetry | Multi-step business workflows, sagas |

---

## 🔗 Related Notes
- [[00 - Home|Master Index]]
- [[Decision Matrix - Decoupling & Messaging]]
- [[Reliability Pillar]]
