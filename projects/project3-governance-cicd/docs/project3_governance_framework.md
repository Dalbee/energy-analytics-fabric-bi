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
### Raw Zone

- Immutable datasets from ingestion (Dataflow Gen2)
- Stored as Delta tables
- No business logic applied

### Curated Zone

- Cleaned, validated tables
- Join-ready star schemas
- Version-controlled transformations

### Semantic Layer

- Reusable models across dashboards
- Governed KPI definitions
- RLS applied here (not in the raw zone)

---

## 5. Naming Standards

```
raw.FactEnergyProduction
raw.DimDate
curated.FactEnergyDaily
model.EnergyAnalytics
pipeline.ETL_Energy
```

Consistent naming ensures:
- Dependency discovery
- Lineage clarity
- Governance compliance

---

## 6. Security Model
### Access

- Raw Zone: restricted to engineering
- Curated Zone: wider access but controlled
- Semantic Layer: governed by RLS

### Row-Level Security

Examples:

- Region-based filtering
- Plant-based filtering
- Role-based access using AD groups

### Sensitive Data

- No personal data stored
- Emission and operational data classified as confidential
- Workspace-level protection applied

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

This framework provides a hybrid approach combining:

- Enterprise governance
- Modern data product principles
- Fabric-native workflows
- CI/CD validation
- Secure, scalable workspace architecture

This framework represents how to think about/plan building real, scalable data platforms — practical, robust, and ready for future expansion.