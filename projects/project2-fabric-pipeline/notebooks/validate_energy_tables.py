# Notebook: validate_energy_tables
# Purpose: Validate curated Lakehouse tables before analytics consumption
# Executed as a Fabric Pipeline quality gate

curated_tables = [
    "dimdate",
    "dimplant",
    "factenergydaily",
    "factheatingdaily",
    "factco2daily",
    "fact_energy_kpi_daily",
    "fact_heating_kpi_daily",
    "fact_heating_emissions_daily"
]

validation_errors = []

for table in curated_tables:
    try:
        df = spark.table(table)
        row_count = df.count()

        if row_count == 0:
            validation_errors.append(f"{table} exists but is empty.")
        else:
            print(f"✓ {table}: {row_count} rows")

    except Exception as e:
        validation_errors.append(f"{table} missing or unreadable: {str(e)}")

if validation_errors:
    print("Validation failed:")
    for err in validation_errors:
        print(f"- {err}")
    raise Exception("Curated data validation failed.")

print("All curated tables passed validation.")
