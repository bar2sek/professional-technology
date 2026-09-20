---
tags:
  - aws/service
  - aws/networking
  - aws/edge
domain: Networking
status: evergreen
exam_priority: ⭐⭐⭐⭐⭐
---

# CloudFront & Global Accelerator

> [!abstract] Overview
> AWS edge networking services accelerate content delivery and global application performance using AWS's worldwide network of Points of Presence (PoPs).

---

## 🥊 CloudFront vs Global Accelerator

```mermaid
graph TD
    Client[Global User Traffic] --> Decision{Workload Profile}
    Decision -->|HTTP/S, Static/Dynamic Web, Caching, WAF| CF[[CloudFront & Global Accelerator|Amazon CloudFront]]
    Decision -->|Non-HTTP TCP/UDP, Gaming, VoIP, Static Anycast IPs, Fast Failover| GA[[CloudFront & Global Accelerator|AWS Global Accelerator]]
    
    CF --> S3[(Amazon S3 via OAC)]
    CF --> ALB[ALB / EC2 Origin]
    GA --> Endpoints[ALB / NLB / EC2 in Multiple Regions]
```

### Direct Feature Comparison

| Feature | Amazon CloudFront | AWS Global Accelerator |
| :--- | :--- | :--- |
| **Core Function** | **Content Delivery Network (CDN) with Edge Caching** | **Network Layer Anycast Proxy & Accelerator** |
| **OSI Layer** | **Layer 7** (HTTP/HTTPS) | **Layer 4** (TCP/UDP) & Layer 7 |
| **Caching** | **Yes** (caches HTML, images, videos at edge) | **No caching** (pure proxy traffic acceleration) |
| **IP Addresses** | Dynamic DNS names | **2 Static Anycast IPv4 Addresses** |
| **Edge Compute** | **CloudFront Functions** & **Lambda@Edge** | None |
| **DDoS & Security** | AWS WAF, AWS Shield, Origin Access Control (OAC)| AWS Shield |
| **Failover Time** | DNS TTL dependent (seconds to minutes) | **Instant health-check failover (< 1 minute)** |
| **Best For** | Websites, video streaming, API caching, static assets | Gaming (UDP), VoIP, IoT, multi-region instant failover |

---

## 🔐 CloudFront Security Features
1. **Origin Access Control (OAC)**:
   - Modern replacement for Origin Access Identity (OAI).
   - Enforces that S3 buckets can **ONLY** be read via CloudFront (blocks direct public S3 URLs).
2. **Signed URLs vs Signed Cookies**:
   - **Signed URLs**: Access to 1 individual file (e.g., paid video download link).
   - **Signed Cookies**: Access to multiple files / entire subscriber portal without modifying URLs.
3. **Field-Level Encryption**: Encrypts sensitive user input (like credit card numbers) at the edge using public keys before forwarding to the backend.

---

## ⚡ High-Yield Exam Tips

> [!tip] Exam Triggers
> - **"Provide 2 static public IP addresses as a single fixed entry point for a global application"** $\rightarrow$ **AWS Global Accelerator**.
> - **"Accelerate non-HTTP UDP traffic for real-time multiplayer gaming"** $\rightarrow$ **AWS Global Accelerator**.
> - **"Restrict direct public access to S3 so users must go through CloudFront"** $\rightarrow$ **CloudFront Origin Access Control (OAC)** + S3 Bucket Policy.
> - **"Provide premium subscribers temporary access to multiple private streaming video files"** $\rightarrow$ **CloudFront Signed Cookies**.

---

## 🔗 Related Notes
- [[Amazon S3 Deep Dive]]
- [[Amazon Route 53 Routing Policies]]
- [[Network Security (Security Groups, NACLs, WAF, Shield)]]
- [[Performance Efficiency Pillar]]
