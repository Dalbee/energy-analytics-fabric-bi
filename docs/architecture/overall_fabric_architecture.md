# Overall Microsoft Fabric Architecture

This document describes the end-to-end architecture implemented across all three projects within this repository. The solution follows a modern data and analytics architecture aligned with enterprise design principles, Microsoft recommended patterns, and the governance requirements of a large energy-sector organisation.

---

## 1. Architectural Overview

The solution is built around Microsoft Fabric, leveraging the following core capabilities:

- Lakehouse as the primary storage and transformation layer  
- Dataflows Gen2 for lightweight ingestion and standardisation  
- Notebooks (PySpark) for scalable transformations  
- Fabric Pipelines for orchestration and automation  
- Power BI Semantic Models for governed reporting  
- Git integration for source control and CI/CD  
- Deployment Pipelines for structured release management  
- Workspace-level governance enabling separation of environments  

---

## 2. High-Level Architecture Diagram

```mermaid
flowchart LR
    A[Source Systems: API / CSV / Synthetic Data] --> B[Dataflow Gen2 Ingestion]
    B --> C[OneLake / Lakehouse Raw Zone]
    C --> D[Notebook (PySpark) Transformations]
    D --> E[Lakehouse Curated Zone]
    E --> F[Semantic Model (Power BI Dataset)]
    F --> G[Power BI Report / Dashboards]
    G --> H[Business Users]

    subgraph Deployment
        X[Git Repository] --> Y[Deployment Pipeline]
        Y --> F
        Y --> G
    end```
---

## 3. Storage Layers

### Raw Zone  
Stores ingested data exactly as received. Used for:

- Replay  
- Auditing  
- Validation  

### Curated Zone  
Stores cleaned, transformed, and model-ready data for semantic models and reporting.

---

## 4. Transformation Strategy

- Light transformations executed in Dataflows Gen2 for standardisation  
- Heavy transformations using PySpark Notebooks for scalable processing  
- Partitioning and incremental loads applied where required  

---

## 5. Semantic Layer

The semantic layer is implemented using:

- Star schema models  
- Calculation groups  
- Shared organisational measures  
- Data quality validations  
- RLS applied at the dataset level where applicable  

This ensures consistency of KPIs across reports.

---

## 6. Deployment Architecture

The deployment model uses:

- GitHub for version control  
- Fabric Git integration  
- Deployment pipelines for Dev → Test → Production  

This aligns with enterprise-grade DevOps processes.

---

## 7. Governance Considerations

Key governance elements include:

- Workspace separation  
- Naming standards  
- Dataset endorsement and certification  
- Access control (RLS/OLS)  
- Change management  
- Monitoring and observability  

Full governance details are documented in the Governance Blueprint.

---

## 8. Summary

This architecture reflects a scalable, governed, and maintainable analytics environment suitable for an enterprise operating in the energy sector. It provides a strong foundation for BI reporting, operational analytics, data governance, and long-term platform growth.
