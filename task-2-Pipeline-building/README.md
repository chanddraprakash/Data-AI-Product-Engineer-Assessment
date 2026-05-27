# Pipeline Building Assessment

## Objective

Build a complete ETL pipeline using a public API and BigQuery.

---

## API Chosen

Open-Meteo API

Reason:
- Free to use
- No authentication required
- Provides structured JSON weather data
- Good for demonstrating ETL concepts

---

## Pipeline Workflow

API → Python → Transformation → BigQuery

---

## Features Implemented

- API data extraction
- Error handling
- Logging
- Data transformation
- Derived analytical fields
- BigQuery loading
- SQL analysis

---

## Transformations Applied

- Flattened nested JSON structure
- Converted timestamps
- Handled null values
- Added temperature_fahrenheit derived field

---

## BigQuery Setup

- Created dataset: marketing_pipeline
- Loaded transformed data into weather_data table
- Used BigQuery Sandbox environment

---

## SQL Summary Query

```sql
SELECT
    DATE(timestamp) AS weather_date,
    ROUND(AVG(temperature_celsius), 2) AS avg_temperature_c,
    MAX(temperature_celsius) AS max_temperature_c,
    ROUND(AVG(humidity), 2) AS avg_humidity
FROM
    `pipeline-assessment-sandbox.marketing_pipeline.weather_data`
GROUP BY
    weather_date
ORDER BY
    weather_date;
```

### Insight

This query shows:
- Daily average temperature
- Maximum temperature recorded
- Average humidity trend

---

