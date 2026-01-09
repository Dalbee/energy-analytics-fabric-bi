# Project 1: Energy BI & Analytics Architecture

This document outlines the architecture of the Energy BI & Analytics solution. The project demonstrates how structured, validated, and governed reporting can be delivered using Microsoft Fabric and Power BI.

---

## 1. Purpose

The goal is to model and visualise key energy-sector metrics including:

- Energy production volumes  
- CO₂ emissions  
- District heating consumption  
- Renewable vs non-renewable contributions  
- Operational KPIs  

The project showcases strong semantic modelling and reporting capabilities.

---

## 2. Data Model Architecture

The semantic model follows a star schema consisting of:

### Fact Tables

- **FactEnergyProduction**
- **FactDistrictHeating**
- **FactCO2Emissions**

### Dimension Tables

- **DimDate**  
- **DimPlant**  
- **DimEnergySource**

This structure enables:

- High performance  
- Reusable measures  
- Consistent KPI definitions  
- Scalability across business units  

---

## 3. Data Flow Architecture

```mermaid
flowchart LR
    A[Raw Data: CSV / API] --> B[OneLake: Lakehouse Files]
    B --> C[PySpark Transformations]
    C --> D[Lakehouse Curated Tables]
    D --> E[Power BI Semantic Model: Import Mode]
    E --> F[Energy Dashboard]
```
---

## 4. Transformation Strategy

Fabric transformations are designed to follow a layered, scalable, and code-first pattern:

- **PySpark Engineering:** All business logic, standardisation, and cleansing are implemented in Spark notebooks to handle high-volume energy datasets.

- **KPI Ingestion:** Business KPIs are computed upstream in Spark to ensure they are available to any tool consuming the Lakehouse.

- **Delta Lake Persistence:** Transformation outputs are written to the Gold layer in Delta format.

- **Validation Gates:** Automated quality checks run within the pipeline to ensure data consistency before the reporting layer is refreshed.

---

## 5. Semantic Layer

The semantic layer standardises how business metrics are defined and consumed:

- **Import Mode:** Utilizes the VertiPaq engine to provide the most responsive user experience and sub-second visual interactivity.

- **Unified Measure Library:** Centralised DAX measures ensure KPI consistency across all report pages.

- **Security:** Row-Level Security (RLS) restricts access to sensitive plant data based on user roles.

- **Certified Datasets:** Published as a "Single Source of Truth" for enterprise-wide self-service reporting.

---

## 6. Deployment Architecture

Deployment is managed using Fabric’s native DevOps capabilities:

- **Git Integration:** Version control for semantic models (BIM files), reports, and Lakehouse artifacts.

- **Deployment Pipelines:** A structured Dev → Test → Production flow ensures stability.

- **Automation:** GitHub Actions orchestrate CI/CD validation where required.

- **Release Documentation:** Maintained for audit and compliance, reflecting energy-sector standards.

---

## 7. Governance Considerations

The architecture aligns with enterprise-grade governance requirements:

- **Workspace Separation:** Dedicated environments for development and production.

- **Naming Standards:** Enforced consistency across all Fabric items.

- **Dataset Certification:** Clearly identifies validated assets for business decision-making.

- **Monitoring:** Dashboards track refresh health, capacity consumption, and usage metrics.

- **Lineage:** Full visibility from raw source files to final Power BI visuals via Fabric Lineage View.

---

## 8. Summary

This architecture provides a scalable, governed, and maintainable analytics foundation. By combining a **Spark-driven data engineering backbone** with a **high-performance Import Mode semantic layer,** it meets the high availability and reliability needs of large energy-sector organisations.

It is suitable for large energy-sector enterprises that require high availability, strong governance, and consistent KPIs across multiple business units.
