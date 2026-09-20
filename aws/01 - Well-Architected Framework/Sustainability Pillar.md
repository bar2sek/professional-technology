---
tags:
  - aws/well-architected
  - aws/sustainability
status: evergreen
exam_priority: ⭐⭐⭐
---

# Sustainability Pillar

> [!abstract] Core Definition
> The Sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads. Key topics include reducing energy consumption, maximizing resource utilization, and adopting efficient hardware and architectures.

---

## 🧭 Key Design Principles
1. **Understand your impact**: Measure emissions and resource consumption using the AWS Customer Carbon Footprint Tool.
2. **Maximize utilization**: Right-size workloads, consolidate instances, and eliminate idle resources.
3. **Anticipate and adopt new, more efficient hardware and software**: Migrate to **AWS Graviton** processors (up to 60% less energy for the same performance).
4. **Use managed services**: Multi-tenant shared services achieve higher efficiency and utilization than dedicated servers.
5. **Reduce the downstream impact of your cloud workloads**: Optimize data movement, cache static assets at the edge using [[CloudFront & Global Accelerator]], and use efficient serialization formats (Parquet, ORC).

---

## ⚡ High-Yield Exam Tips

> [!tip] Exam Keywords
> - **"Reduce carbon footprint & improve price-performance"** $\rightarrow$ Adopt **AWS Graviton (ARM-based)** instances.
> - **"Minimize storage footprint and energy use"** $\rightarrow$ Implement **S3 Lifecycle rules** to transition or expire unneeded data, compress logs, and use columnar formats.
> - **"Eliminate compute resources during idle periods"** $\rightarrow$ Use **Serverless architecture ([[AWS Lambda]])** or Auto Scaling with min size 0.

---

## 🔗 Related Notes
- [[Well-Architected Framework MOC]]
- [[Cost Optimization Pillar]]
- [[AWS Lambda]]
- [[Compute MOC]]
