# Notebook: transform_energy_data.py
# Purpose:
# Transform raw energy datasets into curated Lakehouse tables
# with business KPIs precomputed for Power BI consumption.

from pyspark.sql.functions import (
    col, to_date, when, lit, lower
)

# -------------------------------------------------------
# 1. Load raw fact tables
# -------------------------------------------------------

fact_energy_raw = (
    spark.table("factenergydaily")
    .withColumn("date", to_date(col("date")))
)

fact_heating_raw = (
    spark.table("factheatingdaily")
    .withColumn("date", to_date(col("date")))
)

fact_co2_raw = (
    spark.table("factco2daily")
    .withColumn("date", to_date(col("date")))
)

# -------------------------------------------------------
# 2. Create DimDate
# -------------------------------------------------------

dimdate = (
    fact_energy_raw
    .select("date")
    .dropDuplicates()
)

dimdate.write.mode("overwrite").format("delta").saveAsTable("dimdate")

# -------------------------------------------------------
# 3. Create and enrich DimPlant
# -------------------------------------------------------

# Base DimPlant from energy production
dimplant_base = (
    fact_energy_raw
    .select("plant_id", "plant_name", "energy_source")
    .dropDuplicates()
)

# Load plant capacity reference (master data)
capacity = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("Files/plant_capacity.csv")
)

# Remove duplicate semantic column
capacity_clean = capacity.drop("plant_type")

# Enrich DimPlant
dimplant = (
    dimplant_base
    .join(capacity_clean, on="plant_id", how="left")
)

dimplant.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("dimplant")

# -------------------------------------------------------
# 4. Curated FactEnergyDaily
# -------------------------------------------------------

factenergydaily_curated = fact_energy_raw

factenergydaily_curated.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("factenergydaily")

# -------------------------------------------------------
# 5. Energy KPI Fact (capacity, renewables, utilization)
# -------------------------------------------------------

f = fact_energy_raw.alias("f")
p = dimplant.alias("p")
c = fact_co2_raw.alias("c")

fact_energy_kpi_daily = (
    f
    .join(p, col("f.plant_id") == col("p.plant_id"), "left")
    .join(
        c,
        (col("f.plant_id") == col("c.plant_id")) &
        (col("f.date") == col("c.date")),
        "left"
    )
    .withColumn(
        "theoretical_max_mwh",
        col("installed_capacity_mw") * lit(24)
    )
    .withColumn(
        "load_factor",
        when(
            col("theoretical_max_mwh") > 0,
            col("mwh_produced") / col("theoretical_max_mwh")
        )
    )
    .withColumn(
        "capacity_utilization_pct",
        col("load_factor") * 100
    )
    .withColumn(
        "is_renewable",
        lower(col("p.energy_source")).isin("wind", "solar", "hydro", "biomass")
    )
    .withColumn(
        "renewable_mwh",
        when(col("is_renewable"), col("mwh_produced")).otherwise(0)
    )
    .withColumn(
        "non_renewable_mwh",
        when(~col("is_renewable"), col("mwh_produced")).otherwise(0)
    )
)

fact_energy_kpi_daily.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("fact_energy_kpi_daily")

# -------------------------------------------------------
# 6. Curated FactHeatingDaily
# -------------------------------------------------------

factheatingdaily_curated = (
    fact_heating_raw
    .withColumn(
        "heating_balance_mwh",
        col("heating_produced_mwh") - col("heating_consumed_mwh")
    )
)

factheatingdaily_curated.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("factheatingdaily")

# -------------------------------------------------------
# 7. Heating KPI Fact
# -------------------------------------------------------

fact_heating_kpi_daily = factheatingdaily_curated

fact_heating_kpi_daily.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("fact_heating_kpi_daily")

# -------------------------------------------------------
# 8. Heating CO₂ Emissions Fact
# -------------------------------------------------------

h = fact_heating_kpi_daily.alias("h")
c = fact_co2_raw.alias("c")

fact_heating_emissions_daily = (
    h
    .join(
        c,
        (col("h.plant_id") == col("c.plant_id")) &
        (col("h.date") == col("c.date")),
        "left"
    )
    .withColumn(
        "co2_kg_per_mwh_heat",
        when(
            col("h.heating_produced_mwh") > 0,
            col("c.co2_kg") / col("h.heating_produced_mwh")
        )
    )
)

fact_heating_emissions_daily.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .format("delta") \
    .saveAsTable("fact_heating_emissions_daily")

# -------------------------------------------------------
# 9. Basic data quality checks
# -------------------------------------------------------

print("DimPlant rows:", dimplant.count())
print("FactEnergy KPI rows:", fact_energy_kpi_daily.count())
print("Heating Emissions rows:", fact_heating_emissions_daily.count())
