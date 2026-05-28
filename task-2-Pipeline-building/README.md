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

### pipeline_operations

1) How would you schedule this pipeline to run automatically?
   
-->To move this pipeline from a local manual execution to an automated production environment, I would use Apache Airflow
-->Apache Airflow is an open-source tool used to schedule, automate, and manage data workflows.

How It Work - Instead of manually running the Python script every day, I would place the script inside an Apache Airflow DAG (Directed Acyclic Graph). A DAG represents the workflow pipeline and defines the order of tasks, such as fetching data, cleaning data, and uploading it to BigQuery. Airflow understands which task should run first and which tasks depend on others. The DAG would be scheduled using a Cron expression so the pipeline runs automatically at fixed intervals, such as every day, every hour, or every week, without requiring manual execution.

--> Directed Acyclic Graph = WorkFlow Pipeline
-->A Cron expression is a time schedule format used to tell systems when to run automatically.

2) How would you know if it failed?

-->I would monitor the pipeline using logs and task status monitoring. If the pipeline were running in Apache Airflow, failed tasks would be visible in the Airflow dashboard, along with detailed error logs. I would also configure automatic alerts such as email so failures can be identified and resolved quickly.

3) What would you add or change if this pipeline needed to scale to 10x the data volume?

-->If the pipeline needed to handle 10x more data, I would improve scalability by using Apache Airflow for orchestration,processing tasks in parallel where possible. I would also use scalable storage and data warehouse solutions such as Google Cloud BigQuery with partitioned tables and optimized queries to efficiently manage larger datasets. Additionally, I would add stronger monitoring, retries, and logging to improve reliability for higher workloads.



   


