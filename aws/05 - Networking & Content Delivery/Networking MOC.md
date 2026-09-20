---
tags:
  - aws/moc
  - aws/networking
status: evergreen
---

# 🌐 Networking & Content Delivery Map of Content

> [!abstract] Overview
> AWS Networking provides the isolated virtual network foundation (Amazon VPC), secure edge connectivity (CloudFront, Global Accelerator, Route 53), inter-network connectivity (Transit Gateway, Peering, Direct Connect, PrivateLink), and perimeter security (WAF, Shield, Security Groups, NACLs).

---

## 🗺️ AWS Global & VPC Networking Topology

```mermaid
graph TD
    User([Global Internet User]) --> Route53[[Amazon Route 53 Routing Policies]]
    Route53 --> Edge{Edge Distribution}
    Edge -->|HTTP/S Caching & WAF| CloudFront[[CloudFront & Global Accelerator]]
    Edge -->|Anycast IP / TCP/UDP Acceleration| GlobalAccel[Global Accelerator]
    
    CloudFront --> VPC[Amazon VPC]
    GlobalAccel --> VPC
    
    subgraph VPC_Structure ["VPC Subnet Architecture"]
        VPC --> IGW[[Gateways (IGW, NAT GW, Egress-Only)|Internet Gateway]]
        VPC --> PublicSubnet[Public Subnets: ALB / NAT GW]
        VPC --> PrivateSubnet[Private Subnets: App / DB]
        PrivateSubnet --> NAT[[Gateways (IGW, NAT GW, Egress-Only)|NAT Gateway]]
    end
    
    subgraph Multi_VPC ["Inter-VPC & Hybrid Connectivity"]
        VPC <--> TGW[[VPC Peering vs Transit Gateway vs PrivateLink|Transit Gateway / Peering]]
        VPC <--> DX[[Decision Matrix - Hybrid Connectivity|Direct Connect / VPN]]
    end
```

---

## 📂 Networking Notes Directory

1. **[[VPC Architecture & Subnets]]**:
   - CIDR planning, 5 reserved IPs, Public vs Private vs Isolated subnets, Route Tables.
2. **[[Gateways (IGW, NAT GW, Egress-Only)]]**:
   - Internet Gateway, NAT Gateway (HA Multi-AZ), Egress-Only IGW for IPv6, NAT Instances.
3. **[[VPC Peering vs Transit Gateway vs PrivateLink]]**:
   - Peering (non-transitive) vs Transit Gateway (hub-and-spoke) vs VPC Endpoints (Gateway vs Interface PrivateLink).
4. **[[Amazon Route 53 Routing Policies]]**:
   - Simple, Weighted, Latency, Failover (Health checks), Geolocation, Geoproximity, Multi-value answer.
5. **[[CloudFront & Global Accelerator]]**:
   - CloudFront CDN, Origin Access Control (OAC), Lambda@Edge/CloudFront Functions vs Global Accelerator (Anycast IP).
6. **[[Network Security (Security Groups, NACLs, WAF, Shield)]]**:
   - Security Groups (stateful) vs NACLs (stateless), AWS WAF Layer 7 rules, AWS Shield Standard & Advanced DDoS protection.

---

## ⚡ Core Networking Rules & Tradeoffs

| Mechanism | Scope / Layer | Routing Model | Pricing Model | Key Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **[[VPC Peering vs Transit Gateway vs PrivateLink|VPC Peering]]** | Point-to-Point (1:1) | Direct route table | Free peering (pay standard cross-AZ/Region data transfer) | Lowest cost for 2-3 VPCs |
| **[[VPC Peering vs Transit Gateway vs PrivateLink|Transit Gateway]]** | Hub-and-Spoke | Centralized route tables | Hourly attachment fee + GB data processed | Scalable for hundreds of VPCs & VPN/DX |
| **[[VPC Peering vs Transit Gateway vs PrivateLink|PrivateLink / Endpoints]]** | Service-to-VPC | Elastic Network Interface | Hourly ENI fee + GB data processed | Connects private VPC to SaaS/AWS services without IGW/NAT |
| **[[CloudFront & Global Accelerator|CloudFront]]** | Layer 7 Edge | CDN Edge Caching | Per-request + GB outbound data | Best for static/dynamic web caching |
| **[[CloudFront & Global Accelerator|Global Accelerator]]**| Layer 4 Edge | Anycast IP proxy routing | Hourly fee + Data transfer premium | Best for non-HTTP (gaming, VoIP, IoT) & instant failover |

---

## 🔗 Related Notes
- [[00 - Home|Master Index]]
- [[Decision Matrix - Hybrid Connectivity]]
- [[Security Pillar]]
