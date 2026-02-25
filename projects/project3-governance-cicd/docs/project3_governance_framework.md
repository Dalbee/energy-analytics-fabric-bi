# Project 3 — Fabric Governance, Security & Data Product Framework

**Role:** Lead Data Engineer / Platform Architect  
**Objective:** Define the governance, security, and lifecycle management required to transform raw telemetry into a trusted, executive-grade Data Product.

---

## 1. Purpose

This governance framework ensures that the Energy Analytics Platform operates with enterprise-grade reliability:

- **Security:** Fabric environments are hardened, well-organised, and compliant with energy-sector standards.
- **Consistency:** Data products follow strict naming and architectural standards.
- **Separation of Concerns:** Workspaces support a clear division of responsibilities (Dev/Test/Prod).
- **Automation:** Pipelines are deployed safely through Git integration and CI/CD.
- **Trust:** Business teams can consume "Certified" assets with 100% confidence in the underlying KPIs.

---

## 2. Core Principles (Hybrid Model)

### Enterprise Principles
- **Environment Isolation:** Physical separation (Dev → Test → Prod).
- **Standards:** Strict naming conventions, versioning, and documentation.
- **Least Privilege:** Access controlled through role-based security.
- **Auditability:** End-to-end lineage and historical audit logs.

### Modern Data Product Principles
- **Domain Ownership:** Specialized streams for Energy Production, Heating, and Emissions.
- **Reusability:** Discoverable datasets designed for cross-functional use.
- **Semantic Consistency:** KPIs defined once in Spark, consumed everywhere.
- **Automation:** Proactive quality gates and iterative delivery.

---

## 3. Workspace Strategy

The ecosystem is partitioned into three distinct environments to protect the production "Single Source of Truth."

```text
/Analytics-Platform-Dev   - Development, PySpark drafting, and Sandbox
/Analytics-Platform-Test  - QA, UAT, and Performance Benchmarking
/Analytics-Platform-Prod  - Certified Executive Dashboards & Gold Tables
```

### Workspace Roles

| Role | Responsibility |
| :--- | :--- |
| **Admin** | Security, CI/CD, and governance enforcement. |
| **Member** | Build and iterate on notebooks, pipelines, and models. |
| **Contributor** | Modify dataflows and curated Gold tables. |
| **Viewer** | Read-only access to certified models and reports. |

---

### 4. Data Zones & Layering (Medallion Architecture)

#### **Raw Zone (Bronze)**
- **Lakehouse Files:** Immutable datasets ingested from source systems.
- **Governance:** Native formats (CSV/Parquet) maintained for auditability. Restricted to Engineers to protect data integrity.

#### **Curated Zone (Gold)**
- **Lakehouse Tables:** Cleaned, validated, and dimensionally modeled Delta tables.
- **Governance:** Version-controlled transformations handled by PySpark.

#### **Semantic Layer**
- **Import Mode Models:** High-performance models with governed KPI definitions.
- **Security:** RLS and OLS applied at this layer to ensure data privacy.



---

### 5. Naming Standards

Consistency across all Fabric items is enforced using the pattern: `<prefix>_<project>_<subject>_<grain>`

* `fact_heating_emissions_daily`
* `fact_energy_analytics_kpi_daily`
* `dim_date`
* `dim_plant`

---

### 6. Security Model

The platform implements a multi-layered security strategy to ensure the **"Principle of Least Privilege."**

#### **6.1 Data Access by Zone**
* **Raw Zone:** Restricted to Data Engineering to protect source integrity.
* **Curated Zone:** Accessible to Analysts for ad-hoc SQL discovery via the SQL Analytics Endpoint.
* **Semantic Layer:** The primary entry point for business users, fully governed by RLS.

#### **6.2 Row-Level Security (RLS) Implementation**
Access is filtered dynamically based on the user's organizational role via **Active Directory (AD)**:
* **Plant-Level Filtering:** Plant Managers only see operational data for their specific sites (e.g., Tampere vs. Oulu).
* **Role-Based Access:** Centralized management for seamless onboarding and secure offboarding.

#### **6.3 Sensitive Data and Compliance (OLS)**
* **Confidentiality:** Object-Level Security (OLS) is used to hide specific financial recovery columns (€) from unauthorized viewers.
* **Auditability:** All access to Production is logged via Fabric's audit logs to meet energy-sector regulatory requirements.

---

### 7. GitHub Integration & Version Control

Fabric Git integration ensures every change is tracked and validated as code.

**Branch Strategy:**
* `main` → Production (Single Source of Truth)
* `dev` → Development (Feature work and experimentation)

> **Quality Control:** Pull Requests (PRs) enforce mandatory code reviews before any logic affecting the **€4.9M recovery figure** is merged into the production branch.



---

### 8. CI/CD Release Process

1.  **Commit:** Developer pushes PySpark or DAX changes to the `dev` branch.
2.  **CI Validation:** GitHub Actions automatically validate YAML, JSON, and Notebook syntax.
3.  **Approval:** Lead Analytics Engineer review ensures logic matches business requirements and HSEQ standards.
4.  **Promotion:** Fabric Deployment Pipeline promotes artifacts to **Test**, then **Prod**.
5.  **Automation:** Production refresh triggers and monitoring alerts feed operational health dashboards.

> 💡 **Detailed Technical Spec:** For a deep dive into the environment synchronization and release stages, see the [Fabric Deployment Pipeline Specification](./fabric_deployment_pipeline.md).


---

### 9. Data Product Lifecycle

* **Draft:** Early development and testing in the Dev workspace.
* **Validated:** All QA checks passed in the Test environment.
* **Certified:** Approved for business adoption and executive sign-off.
* **Retired:** Deprecated assets identified for decommissioning to maintain environment cleanliness.

* **Documentation Requirement:** Every certified product must include a defined owner, schema, transformation logic, and refresh schedule.


> 📊 **Monitoring Framework:** Detailed metrics for refresh health, capacity consumption, and usage tracking are documented in the [Monitoring Dashboard Specification](./monitoring_dashboard_spec.md).
---

### 10. Summary

This framework represents a robust approach to building scalable data platforms. By combining **Enterprise Governance** with **Modern Data Product principles**, we ensure the Energy Analytics Platform is both secure and agile—protecting the **€4.9M** identified recovery and supporting future portfolio growth.

---

### 🧭 Navigation

- **[View Project 1: Energy BI & Analytics Solution](../../project1-energy-bi/README.md)**
- **[View Project 2: End-to-End Fabric Data Pipeline & Automation](../../project2-fabric-pipeline/README.md)**
- **[Back to Portfolio Home](../../../README.md)**

