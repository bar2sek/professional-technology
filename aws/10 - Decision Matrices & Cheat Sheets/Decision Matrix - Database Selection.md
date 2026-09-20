---
tags:
  - aws/matrix
  - aws/database
  - aws/exam-high-priority
status: evergreen
---

# Decision Matrix: AWS Database Selection

> [!abstract] Overview
> Fast-lookup decision matrix to select the optimal AWS database engine based on data model, scaling requirements, query patterns, and latency constraints.

---

## 🧭 Master Database Decision Flowchart

```mermaid
graph TD
    Start[Database Workload] --> Model{What is the primary Data Model?}
    
    Model -->|Relational SQL / Joins / ACID| SQL{Access & Scale Requirements}
    SQL -->|Complex enterprise SQL / Managed| RDS[[Amazon RDS & Aurora|Amazon RDS: Postgres/MySQL/Oracle/SQLServer]]
    SQL -->|Cloud-native / Auto-scale / 5x throughput| Aurora[[Amazon RDS & Aurora|Amazon Aurora]]
    SQL -->|Serverless / Bursty / Intermittent| AuroraServ[[Amazon RDS & Aurora|Aurora Serverless v2]]
    
    Model -->|Key-Value / Document / Unstructured| NoSQL{Performance Requirement}
    NoSQL -->|Single-digit ms / Massive horizontal scale| DDB[[Amazon DynamoDB]]
    NoSQL -->|MongoDB compatibility| DocDB[Amazon DocumentDB]
    NoSQL -->|Cassandra compatibility| Keyspaces[Amazon Keyspaces]
    
    Model -->|In-Memory / Microsecond Latency| InMem{Use Case}
    InMem -->|Caching & Session Store| Cache[[ElastiCache & MemoryDB|ElastiCache Redis / Memcached]]
    InMem -->|Primary DB + Durable ACID Multi-AZ| MemDB[[ElastiCache & MemoryDB|Amazon MemoryDB for Redis]]
    
    Model -->|Analytics / OLAP / Columnar / Aggregations| DW{Query Target}
    DW -->|Petabyte Data Warehouse| RS[[Specialized Databases (Redshift, Neptune, OpenSearch)|Amazon Redshift]]
    DW -->|Serverless SQL directly on S3 data lake| Athena[Amazon Athena]
    
    Model -->|Graph / Highly Connected Relationships| Neptune[[Specialized Databases (Redshift, Neptune, OpenSearch)|Amazon Neptune]]
    Model -->|Full-Text Search & Log Analytics| OpenSearch[[Specialized Databases (Redshift, Neptune, OpenSearch)|Amazon OpenSearch Service]]
    Model -->|Time-Series / IoT Telemetry| Timestream[Amazon Timestream]
    Model -->|Immutable Cryptographic Ledger| QLDB[Amazon QLDB]
```

---

## 📊 Comprehensive Database Comparison

| Database Service | Primary Model | Replication / HA | Storage Scaling | Latency | Key Use Cases |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[[Amazon RDS & Aurora|Amazon RDS]]** | Relational (OLTP) | Multi-AZ (Sync), Read Replicas (Async) | Up to 64 TB (auto-grow) | Milliseconds | Traditional web apps, ERP, CRM, ACID transactions |
| **[[Amazon RDS & Aurora|Amazon Aurora]]** | Relational (Cloud-Native) | Multi-AZ (6 copies across 3 AZs), Global DB | **Auto-scales to 128 TB** | Milliseconds ($3\times-5\times$ RDS) | High-throughput OLTP, mission-critical SQL |
| **[[Amazon DynamoDB]]** | Key-Value & Document | Multi-AZ by default, Global Tables | **Virtually Unlimited** | **Single-digit ms** | High-scale mobile backends, shopping carts, gaming |
| **[[ElastiCache & MemoryDB|ElastiCache]]** | In-Memory (Redis/Memcached) | Multi-AZ failover (Redis) | Memory-bound (GBs to TBs)| **Microseconds** | Read caching, session state, leaderboards |
| **[[ElastiCache & MemoryDB|Amazon MemoryDB]]** | In-Memory Database | Multi-AZ Transaction Log | Memory + Multi-AZ Log | **Microseconds** | Primary database for ultra-low latency transactional apps |
| **[[Specialized Databases (Redshift, Neptune, OpenSearch)|Amazon Redshift]]** | Columnar OLAP | Multi-node cluster, RA3 managed storage | Petabytes (RA3 to exabytes)| Seconds | Business Intelligence, complex joins on historical data |
| **[[Specialized Databases (Redshift, Neptune, OpenSearch)|Amazon Neptune]]** | Graph | Multi-AZ 6 copies (Aurora storage engine)| Up to 128 TB | Milliseconds | Fraud detection, social networks, knowledge graphs |
| **[[Specialized Databases (Redshift, Neptune, OpenSearch)|OpenSearch]]** | Search / Index | Multi-AZ master/data nodes | Terabytes to Petabytes | Milliseconds | Log analytics, autocomplete search bar, monitoring |

---

## ⚡ Instant Exam Clues

| Exam Clue / Keyword | Correct Architecture Decision |
| :--- | :--- |
| *"Unpredictable or spiky database traffic with zero maintenance"* | **Aurora Serverless v2** |
| *"Multi-Region active-active relational replication with RPO < 1s"* | **Aurora Global Database** |
| *"Multi-Region active-active NoSQL with local write speeds"* | **DynamoDB Global Tables** |
| *"Microsecond read response for DynamoDB"* | **DynamoDB Accelerator (DAX)** |
| *"Offload read queries from overloaded PostgreSQL database"* | **Amazon ElastiCache (Redis)** or **Read Replicas** |
| *"Ad-hoc serverless SQL queries on raw CSV/JSON/Parquet files in S3"* | **Amazon Athena** |
| *"Query data in S3 directly from Redshift warehouse without loading"* | **Amazon Redshift Spectrum** |
| *"Prevent database connection exhaustion caused by AWS Lambda spikes"* | **Amazon RDS Proxy** |

---

## 🔗 Related Notes
- [[Databases MOC]]
- [[Amazon RDS & Aurora]]
- [[Amazon DynamoDB]]
- [[ElastiCache & MemoryDB]]
