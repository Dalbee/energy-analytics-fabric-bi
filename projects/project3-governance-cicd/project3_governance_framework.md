# Project 3 — Fabric Governance, Security & Data Product Framework

This document defines the governance, security, workspace strategy, and lifecycle management approach for Microsoft Fabric.
It blends enterprise architectural requirements with modern data product design.

---

## 1. Purpose

This governance framework ensures that:

- Fabric environments are secure, well-organised, and compliant
- Data products follow consistent standards
- Workspaces support clear separation of responsibilities
- Pipelines can be deployed safely through Git + CI/CD
- Business teams can consume trusted analytics assets
- Platform operations can monitor, optimise, and scale workloads

---

## 2. Core Principles (Hybrid Model)

### Enterprise Principles

- Separation of environments (Dev → Test → Prod)
- Standards for naming, versioning, and documentation
- Access controlled through least privilege
- Clear ownership of datasets, models, and pipelines
- End-to-end lineage and auditability

### Modern Data Product Principles

- Domain ownership (energy production, heating, emissions)
- Reusable and discoverable datasets
- Semantic consistency across reports and models
- Automated quality checks
- Incremental, iterative delivery

---

## 3. Workspace Strategy

```
/Analytics-Platform-Dev
/Analytics-Platform-Test
/Analytics-Platform-Prod
```

### Workspace Roles

| Role        | Responsibility                          |
| ----------- | --------------------------------------- |
| Admin       | Security, CI/CD, governance enforcement |
| Member      | Build notebooks, pipelines, models      |
| Contributor | Modify dataflows, curated tables        |
| Viewer      | Read-only access to models and reports  |


---

## 4. Data Zones & Layering
### Raw Zone (Bronze)

- **Lakehouse Files:** Immutable datasets ingested from source systems.

- Native formats (CSV/Parquet) maintained for auditability.

### Curated Zone (Gold)

- **Lakehouse Tables:** Cleaned, validated, and dimensionally modeled Delta tables.

- Version-controlled transformations handled by PySpark.

### Semantic Layer

- **Import Mode Models:** High-performance models with governed KPI definitions.

- **Security:** RLS and OLS applied at this layer to ensure data privacy.

---

## 5. Naming Standards
To ensure scannability and governance, the following pattern is enforced:
`<prefix>_<project>_<subject>_<grain>`

- prefix – Type of table: `fact`, `dim`, `stg` (staging), etc.

- project – Project name (optional if schema implies project)

- subject – What the table is about: `energy`, `heating`, `co2`, etc.

- grain – Aggregation or granularity: `daily`, `monthly`, etc.

**Example:**
```
fact_heating_emissions_daily
fact_energy_analytics_kpi_daily
dim_date
dim_plant
```

---

## 6. Security Model

The platform implements a multi-layered security strategy to ensure the "Principle of Least Privilege" across the Medallion architecture.

### 6.1 Data Access by Zone

- **Raw Zone (Bronze):** Restricted exclusively to Data Engineering and Platform Admins to maintain data integrity.

- **Curated Zone (Gold):** Accessible to Data Analysts for ad-hoc SQL discovery and cross-functional validation via the SQL Analytics Endpoint.

- **Semantic Layer:** The primary entry point for business users, fully governed by Row-Level Security (RLS).

### 6.2 Row-Level Security (RLS) Implementation

Access is filtered dynamically based on the user's organizational role:

- **Plant-Level Filtering:** Plant Managers only see operational data for their specific sites.

- **Region-Level Filtering:** Regional Directors see aggregated metrics for their geographic area.

- **Role-Based Access:** Managed via Active Directory (AD) groups for seamless onboarding and offboarding.

### 6.3 Sensitive Data and Compliance

- **Confidentiality:** Emissions and financial data are classified as confidential; **Object-Level Security (OLS)** is used to hide specific columns from unauthorized viewers.

**Data Privacy:** No PII (Personally Identifiable Information) is stored within the Lakehouse.

**Auditability:** All access to the Production workspace is logged via Fabric's audit logs to meet energy-sector regulatory standards.

---

## 7. GitHub Integration & Version Control

Fabric Git integration ensures:

- Every change is tracked
- Workspace assets are stored as code
- PRs enforce quality before deployment
- Code reviews validate pipelines, notebooks, and metadata

### Branch Strategy

```css
main  → Production
dev   → Development
```

Promotions to ```main``` use:

- PR approvals
- Automated validation
- Deployment Pipelines

---

## 8. CI/CD Release Process

1. Developer commits change to ```dev```

2. GitHub CI validates:

- YAML

- JSON

- Notebook syntax

3. Pull request opens to ```main```

4. Reviewer approves

5. Fabric Deployment Pipeline promotes:

- Notebook

- Pipeline

- Dataflow

- Semantic model

6. Prod refresh triggers

7. Monitoring alerts feed operational dashboards

---

## 9. Data Product Lifecycle
### Lifecycle Stages

- *Draft:* Early development in Dev
- *Validated:* QA checks passed in Test
- *Certified:* Approved for business adoption
- *Retired:* Deprecated tables or dashboards

### Documentation Required

- Purpose & owner
- Schema
- Transformations
- Refresh schedule
- RLS rules

---

## 10. Summary

This framework represents a practical, robust approach to building scalable data platforms. By combining **Enterprise Governance** with **Modern Data Product principles**, we ensure the Energy Analytics Platform remains a "Single Source of Truth" that is both secure and agile