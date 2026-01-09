# Monitoring Dashboard Specification (Fabric + Power BI)

This dashboard allows platform teams to monitor operations across ingestion, transformation, model refresh, and workspace health.

---

## 1. Purpose

To provide visibility into:
- Pipeline failures  
- Refresh latency  
- Dataflow status  
- Lakehouse table sizes  
- Capacity usage  
- Gateway connectivity (if used)  

---

## 2. Metrics

### **Operational**
- **Pipeline Health:** Success/failure rate of the orchestration suite.

- **Spark Performance:** Execution duration trends for PySpark notebooks.

- **Refresh Latency:** Time taken to import Gold tables into the Semantic Model.

### **Data Quality**
- **Row Count Anomalies:** Comparison of Bronze vs. Gold record counts.

- **Energy Metrics:** Out-of-bounds checks (e.g., negative production, unrealistic carbon intensity).

### **Semantic Model**
- Refresh duration  
- Refresh failures  
- Dataset size growth  

### **Capacity**
- CPU and memory usage  
- Concurrency peaks  
- Throttling events  

---

## 3. Dashboard Layout

### **Top Section**
- KPIs (Failures Today, Success Rate, Avg Run Time)

### **Left Column**
- Pipeline success/failure chart  
- Notebook runtime trend  
- Model refresh history  

### **Right Column**
- Lakehouse table sizes  
- Data anomaly alerts  
- Capacity usage  

---

## 4. Data Sources
- Fabric pipeline logs (monitoring API)  
- Semantic model refresh history  
- Lakehouse table metadata  
- Fabric capacity metrics  

---

## 5. Summary

This dashboard supports continuous operations and proactive issue resolution for Fabric-based analytics platforms.
