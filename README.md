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
│   └── project3-governance-cicd/   # CI/CD configs & Security documentation
└── README.md                  # Portfolio Home Page
```


---

## 🚀 Project Summaries

### [Project 1: Energy BI & Analytics Solution](./projects/project1-energy-bi/README.md)

A full business intelligence solution built using Power BI and Fabric semantic models. Includes data modelling using a **Star Schema**, calculation groups, and energy-sector KPIs (production, demand, emissions).


---

### [Project 2: End-to-End Fabric Data Pipeline & Automation](./projects/project2-fabric-pipeline/README.md)

An end-to-end data engineering workflow using **PySpark** and **Medallion Architecture**. It covers Lakehouse-based ingestion, dimensional modeling, and pipeline orchestration with automated quality gates.


---

### [Project 3: Fabric Governance, Security and CI/CD Framework](./projects/project3-governance-cicd/docs/project3_governance_framework.md)

Illustrates enterprise management of Fabric: Workspace strategy (Dev/Test/Prod), **RLS/OLS** security models, and **CI/CD** using deployment pipelines and Git integration.

---

## Documentation

All architecture, governance, and design materials are located in [/docs](./docs).

Key documents include:

- [Fabric architecture diagrams](./docs/architecture/overall_fabric_architecture.md)
- [Security and access models](./docs/architecture/project2_pipeline_architecture.md#6-governance-and-security)
- [Naming standard](./docs/architecture/project3_governance_architecture.md#62-naming-convention)
- [CI/CD process documentation](./docs/architecture/project3_governance_architecture.md)

These documents are written to reflect enterprise standards.

---

## 🧭 How to Navigate This Repository

1. Start with the [/docs](./docs) folder to understand the architecture and governance design.

2. **Explore Engineering:** See [Project 2](./projects/project2-fabric-pipeline) for the Spark ingestion and transformation pipelines.

3. **Explore Analytics:** See [Project 1](./projects/project1-energy-bi) for the BI solution and Star Schema.

4. **Explore Operations:** See [Project 3](./projects/project3-governance-cicd) for governance and deployment artefacts.

---

## 📧 Contact & Professional Context

This repository is a demonstration of architectural capability in the Microsoft Fabric ecosystem. It reflects a commitment to code-first engineering, rigorous governance, and high-performance data delivery.


