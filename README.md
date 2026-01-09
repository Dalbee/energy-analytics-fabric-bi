# Energy Analytics Fabric BI Platform

This repository contains a set of three demonstration projects designed to showcase modern data engineering, reporting, and governance capabilities using Microsoft Fabric. The work is structured to represent the responsibilities of a Senior / Lead Analytics Engineer within a large energy company operating at scale.

The repository is organised into three primary projects:

1. **[Project 1: Energy BI & Analytics Solution](./projects/project1-energy-bi/README.md)**

2. **[Project 2: End-to-End Fabric Data Pipeline & Automation](./projects/project2-fabric-pipeline/README.md)**

3. **[Project 3: Fabric Governance, Security and CI/CD Framework](./projects/project3-governance-cicd/docs/project3_governance_framework.md)**

Together, these projects demonstrate a complete, production-aligned Fabric ecosystem including ingestion, transformation, modelling, reporting, governance, operations, and deployment automation.

---

## 🎯 Key Objectives

- **Scalability:** Design a platform capable of handling millions of rows of operational energy data.

- **Single Source of Truth:** Compute complex KPIs upstream in Spark to ensure consistency across all downstream tools.

- **Governance:** Implement a "Least Privilege" security model and a structured release process.

- **Performance:** Balance the heavy lifting of Spark with the lightning-fast interactivity of Power BI.

---

## 🛠️ Technology Stack

- **Storage:** Microsoft Fabric OneLake & Lakehouse (Delta Lake format).

- **Compute:** Spark (PySpark Notebooks) & SQL Analytics Endpoints.

- **Orchestration:** Fabric Data Pipelines.

- **Reporting:** Power BI (Import Mode, DAX, Calculation Groups).

- **DevOps:** GitHub Repository Integration & Fabric Deployment Pipelines.


---

## 📁 Repository Structure

```
energy-analytics-fabric-bi/
├── docs/                      # Global Architecture & Governance Blueprints
├── projects/
│   ├── project1-energy-bi/    # BI Artifacts (PBIX, Semantic Model metadata)
│   ├── project2-engineering/  # PySpark Notebooks & Pipeline JSONs
│   └── project3-governance/   # CI/CD configs & Security documentation
└── README.md                  # Portfolio Home Page
```


---

## Project 1 — Energy BI & Analytics Solution

A full business intelligence solution built using Power BI and Fabric semantic models.  
It demonstrates:

- Data modelling using a star schema
- Calculation groups and measure definitions
- Data quality and transformation logic
- A clean, production-ready BI report
- Energy-sector KPIs (production, demand, emissions, district heating, etc.)

The project includes sample datasets, semantic model documentation, and a Power BI report.

---

## Project 2 — Microsoft Fabric Data Engineering Pipeline

This project implements an end-to-end **data engineering workflow using Microsoft Fabric**, providing the foundation for reliable analytics and reporting in an energy-sector context.  

The workflow covers:

- **Lakehouse-based ingestion** of operational energy datasets (production, district heating, CO₂ emissions)  
- **PySpark-based transformations** and KPI computation  
- **Dimensional modeling** with star-schema-inspired curated tables  
- **Data quality validation** through dedicated notebooks  
- **Pipeline orchestration** to automate the end-to-end workflow  
- **Preparation of clean, analysis-ready datasets** for consumption by Power BI semantic models (Project 1)  

Artifacts include transformation and validation notebooks, pipeline definitions, curated Delta tables, and architecture documentation. This project reflects enterprise-grade data engineering practices suitable for a **Senior / Tech Lead–level role**.


---

## Project 3 — Governance, Security and CI/CD Framework

This project illustrates how to manage Fabric in a controlled enterprise environment:

- Workspace strategy (Development, Test, Production)
- Naming conventions and certification processes
- Dataset governance
- Tenant-level governance recommendations
- Gateway configuration and data connections
- CI/CD using YAML-based deployment pipelines
- Monitoring model and supporting report

This project reflects modern, mature Fabric governance practices that scale across teams.

---

## Documentation

All architecture, governance, and design materials are located in `/docs`.

Key documents include:

- Fabric architecture diagrams
- Governance blueprint
- Security and access models
- Naming standard
- CI/CD process documentation
- RLS/OLS implementation guide
- Release procedure

These documents are written to reflect enterprise standards.

---

## Technology Stack

- Microsoft Fabric (Lakehouse, Pipelines, Dataflows, Notebooks, Semantic Models)
- Power BI
- Git integration with Fabric
- SQL / PySpark
- GitHub Actions for CI/CD

---

## How to Navigate This Repository

Start with the `/docs` folder to understand the architecture and governance design.

Then explore each project:

- `/projects/project1-energy-bi` for the BI solution
- `/projects/project2-fabric-pipeline` for the ingestion and transformation pipeline
- `/projects/project3-governance-cicd` for governance and deployment artefacts

The `/website` folder contains optional public-facing material for publishing the portfolio as a static site.

---

## 📧 Contact & Professional Context

This repository is a demonstration of architectural capability in the Microsoft Fabric ecosystem. It reflects a commitment to code-first engineering, rigorous governance, and high-performance data delivery.


