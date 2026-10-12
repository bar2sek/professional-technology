# Ryan Bartusek
### Enterprise Cloud Architecture | Cloud Platform Engineering
Des Moines, IA | [linkedin.com/in/bar2sek](https://linkedin.com/in/bar2sek) | [github.com/bar2sek](https://github.com/bar2sek)

---
## Professional Summary
Cloud Infrastructure Leader and Enterprise Cloud Architect with 10+ years of experience driving cloud platform maturity across public-sector, financial, and enterprise domains. Proven track record leading engineering teams of 6–10, architecting enterprise multi-account AWS environments across production and non-production, and operationalizing statewide Terraform mandates through engineer enablement and automated change-control governance.

Specializes in aligning strategic business goals with scalable cloud foundations, automated account vending pipelines, and Infrastructure as Code (IaC) delivery models. Demonstrated success establishing architectural standards, multi-environment security guardrails, and modern DevSecOps practices that accelerate developer velocity while maintaining strict compliance and operational resilience. Trusted advisor to executive leadership, security teams, and delivery partners for translating organizational vision into scalable, secure, and sustainable cloud platforms.

---
## Core Competencies
- **Cloud:** AWS, Microsoft Azure, VMware Tanzu & vSphere
- **Infrastructure as Code:** Terraform, Azure Bicep & ARM, PowerShell, Bash
- **CI/CD:** GitHub Actions (Org Administrator), Azure DevOps, Concourse CI, Docker
- **Identity & Networking:** SAML/SSO federation (Okta, Entra ID), Aviatrix multicloud networking
- **Observability:** Prometheus, Grafana, Azure Monitor, CloudWatch
- **Architecture Communication:** Lucidchart, Miro, Visio

## Experience

### State of Iowa – Department of Management
**Cloud Infrastructure Team Lead** | *April 2025 – Present*
- **Enterprise Multi-Account & OU Hierarchy:** Designed the State's greenfield multi-account AWS platform, now **38 accounts across 6 agencies** and growing quickly as the migration ramps up, with **Security, Core Infrastructure, Workloads (Prod / Non-Prod / Sandbox), Exceptions, and Suspended OUs** isolating blast radius and inheriting **Service Control Policies (SCPs)**.
- **Automated Account Vending & Baselines:** Deployed **AWS Control Tower** and **Account Factory for Terraform (AFT)** so new accounts are requested in Git and provisioned by pipeline with a security baseline (CloudTrail, Config, Security Hub, GuardDuty), IAM Identity Center access, and transit networking.
- **Engineering Leadership & IaC Enablement:** Lead and coordinate a team of **6–10 cloud engineers and technicians**; up-skilled longtime systems administrators into Infrastructure as Code, who now enforce the IaC standard as new agency teams onboard; instituted agile ceremonies and serve as GitHub Administrator for change control.
- **Architectural Decisions & Standards:** Led technical trade-off evaluations (e.g., **Terraform vs. Azure Bicep & CloudFormation**) and documented decision rationale to establish Terraform and policy-as-code as enterprise standards across the State's multi-cloud environments; built modular reference architectures that accelerated agency project intake.
- **Enterprise Naming Standard:** Authored the State's cloud naming standard, extending Microsoft's Azure naming conventions to a multi-cloud, multi-agency scope; serve as the standing authority on naming decisions.
- **FinOps & Cost Governance:** Evaluated **Apptio Cloudability** and AWS Cost Management tools to establish enterprise tagging governance, cost attribution, and multi-agency budget visibility.
- **Large-Scale Cloud Migration (In Progress):** Lead the infrastructure team partnering with AWS Professional Services on a statewide migration off VMware, committed to **1,400+ machines by end of 2026** and on track, including VMware Horizon virtual desktops moving to **Amazon WorkSpaces**; my team reviews and applies the vendor-authored Terraform as the sole team with production access.
- **Generative AI Initiative (Early Stage):** Helped scope the State's **Amazon Bedrock** initiative, breaking down the work and setting up the repository structure separating the platform and application layers.
- **Multicloud Networking & Security Strategy:** Led the technical strategy for **Aviatrix** multicloud transit networking and distributed firewalls, building on the proof of concept I ran at HHS, for centralized visibility, hybrid connectivity, and security segmentation.
- **Architecture Communication:** Created the architecture diagrams for the AWS landing zone and Aviatrix initiatives and presented them to leadership and stakeholder groups, scoping each diagram to its audience so everyone from executives to engineers understood the design at the right level during the greenfield project's early stages.

### State of Iowa – Department of Health and Human Services
**Lead Platform Engineer** | *April 2021 – April 2025*
- **Azure Landing Zone Architecture:** Architected enterprise Azure landing zones aligned with the Microsoft Cloud Adoption Framework (CAF) and authored the original naming standard; when a reorganization shifted modernization priorities to AWS, the design and standards carried forward into the State's AWS platform.
- **Virtual Desktop Infrastructure (AVD):** As the agency's sole Azure engineer, designed, deployed, and administered the Azure Virtual Desktop environment for **~75 users**, still heavily used today; adopted Nerdio for management, iterated on an image-build approach around legacy contractor tooling, and partnered with the Windows and M365 teams on Entra ID and Intune integration.
- **Identity Federation & Access Governance:** Engineered enterprise identity federation and SSO workflows, integrating Okta, Microsoft Entra ID (Azure AD), SAML authentication, and on-premises Active Directory; implemented least-privilege RBAC, conditional access policies, and centralized authorization across hybrid environments.
- **Multicloud Networking POC:** Led proof-of-concept (POC) evaluations for Aviatrix multicloud transit networking to enhance network visibility, security segmentation, and hybrid cloud connectivity.
- **PaaS Platform Engineering:** Orchestrated greenfield configuration and deployment of VMware Tanzu Application Service (TAS) via BOSH on legacy on-premises vSphere infrastructure, partnering with VMware consultants to host refactored state assistance applications (e.g., Rent Reimbursement).
- **CI/CD Automation & Mentorship:** Built CI/CD pipelines utilizing Concourse CI, Platform Automation, and GitOps workflows under strict pull-request controls; drove team growth through technical screening, onboarding, and structured mentorship.

### Principal Financial Group
**Platform Engineer & Developer Support** | *July 2019 – April 2021*
- **AWS IaC & CI/CD Automation:** Built reusable AWS CDK stacks deployed through GitHub Actions pipelines, and Concourse automation enforcing semantic versioning and Git tagging for container images.
- **Platform Integration Service:** Built a Python and Docker-based service connecting a Pivotal Cloud Foundry application to a legacy on-premises SOAP service for identity lookups.
- **Synthetic Monitoring & Observability:** Built containerized Python/Selenium synthetic tests for authentication paths, with Grafana and Prometheus dashboards and xMatters alerting.
- **Platform Operations & Disaster Recovery:** Managed platform lifecycles with BOSH on vSphere and automated disaster recovery with BOSH Backup and Restore (BBR) to on-premises MinIO storage; wrote the runbooks and onboarding guides in Confluence.

### Corteva Agriscience
**Cloud Engineer & Developer Support** | *October 2017 – July 2019*
- **Automation & Test-Driven Development:** Engineered automation scripts using PowerShell and Pester unit testing for Azure Automation Runbooks, streamlining mass virtual machine backups, automated patching schedules, and systems management.
- **Enterprise Workload Optimization:** Supported enterprise workloads in Azure, optimizing virtual machine performance for mission-critical SAP, HANA, Oracle, and SQL deployments running on Red Hat Enterprise Linux (RHEL) and Windows Server.
- **Monitoring & Alerting Frameworks:** Implemented infrastructure monitoring and alerting frameworks using Azure Monitor, Log Analytics, and Azure Alerts to proactively detect and remediate backup and system failures.
- **Offshore Team Enablement:** Onboarded and trained offshore engineering teams (including Accenture and TCS) with standard operating procedures and runbooks, and served as their primary technical escalation point.

---
## Projects
*Public source and documentation: [github.com/bar2sek](https://github.com/bar2sek)*

### Hybrid Homelab Platform (Ongoing)
*Talos Linux · Kubernetes · Terraform · GitHub Actions · AWS · Azure · Cloudflare*
- **Declarative Kubernetes Platform:** Run a multi-node **Talos Linux** Kubernetes cluster managed through Sidero Omni, with **Rook-Ceph** tiered storage and Prometheus/Grafana observability, all defined in code.
- **Infrastructure as Code End to End:** Network VLANs, firewall rules and DNS managed with **Terraform**; an AWS multi-account landing zone built with Organizations and IAM Identity Center; a declarative macOS workstation with nix-darwin.
- **Keyless Multi-Cloud GitOps:** A dedicated deployment repository applies AWS, Azure and Cloudflare infrastructure through GitHub Actions using **OIDC federation**, with PR-time plans and approval-gated production applies.
- **Identity & Zero-Trust Access:** Self-hosted identity provider (Authentik) federated with AWS and Entra ID, with remote access through Cloudflare Tunnel and Access policies instead of open inbound ports.

### Bedrock AI Gateway (Personal Learning Project, 2026)
*Amazon Bedrock · API Gateway · Lambda · AWS CDK · GitHub Actions*
- **Retrieval-Augmented Generation API:** Built a serverless question-answering API over a document knowledge base using **Bedrock Knowledge Bases** and the Converse API, returning answers with source citations.
- **Layered Safety Controls:** Applied **Bedrock Guardrails** (prompt-attack, PII, denied-topic and grounding checks), per-consumer API keys, and usage-plan quotas; red-team testing exposed a gap where input filters weren't evaluating the user's question, which I fixed and verified.
- **Delivery & Least Privilege:** Same keyless GitHub Actions model as the homelab, plus automated tests and a scoped deploy role with a permissions boundary.
- **Observability:** Published latency, token, and guardrail-block metrics with an alarm and dashboard, plus a per-consumer usage log that records metadata rather than prompt text.

---
## Earlier Experience
- **Lean TECHniques** | Software Developer (*October 2016 – May 2017*)
- **EMC Insurance** | Software Developer (*May 2016 – October 2016*)
- **LightEdge Solutions** | Data Center Technician (*January 2014 – May 2016*)
- **IdentoGO by MorphoTrust USA** | Remote & On-Site Support Technician (*August 2011 – December 2013*)

---
## Education
- **Iowa State University** – Bachelor of Arts (BA), Visual Studies
- **Des Moines Area Community College** – Associate of Science (AS), Business Information Systems

---
## Certifications
- **Aviatrix Certified Engineer (ACE)** – Multicloud Network Professional
- **Aviatrix Certified Engineer (ACE)** – Multicloud Network Associate
- **Microsoft Certified:** Azure Fundamentals (AZ-900)
- **Microsoft Certified:** Azure Data Fundamentals (DP-900)
- **AWS Certified Solutions Architect – Associate (SAA-C03)** *(In Progress)*
