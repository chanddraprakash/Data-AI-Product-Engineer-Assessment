import os
import requests
import pandas as pd
import logging
from google.cloud import bigquery
from config import PROJECT_ID, DATASET_ID, TABLE_ID, LATITUDE, LONGITUDE

# Block to get credentials
KEY_PATH = "bigquery-key.json"
if os.path.exists(KEY_PATH):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath(KEY_PATH)
else:
   logging.warning(f"Could not find '{KEY_PATH}' in this workspace.")

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_weather_data():
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={LATITUDE}&longitude={LONGITUDE}"
        f"&hourly=temperature_2m,relative_humidity_2m"
    )

    try:
        logging.info("Fetching weather data from API")

        response = requests.get(url)

        if response.status_code != 200:
            logging.error(f"API request failed: {response.status_code}")
            return None

        return response.json()

    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return None


def transform_data(data):
    logging.info("Transforming data")

    hourly = data["hourly"]

    df = pd.DataFrame({
        "timestamp": hourly["time"],
        "temperature_celsius": hourly["temperature_2m"],
        "humidity": hourly["relative_humidity_2m"]
    })

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Handle null values
    df = df.fillna(0)

    # Derived field
    df["temperature_fahrenheit"] = (
        df["temperature_celsius"] * 9/5
    ) + 32

    return df


def load_to_bigquery(df):
    logging.info("Loading data to BigQuery")

    client = bigquery.Client(project=PROJECT_ID)

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    # Explicit schema definition
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("timestamp", "TIMESTAMP"),
            bigquery.SchemaField("temperature_celsius", "FLOAT"),
            bigquery.SchemaField("humidity", "INTEGER"),
            bigquery.SchemaField("temperature_fahrenheit", "FLOAT"),
        ],
        write_disposition="WRITE_APPEND",
    )

    job = client.load_table_from_dataframe(
        df,
        table_ref,
        job_config=job_config
    )

    job.result()

    logging.info("Data loaded successfully")


def main():
    logging.info("Starting weather pipeline")

    raw_data = fetch_weather_data()

    if raw_data:
        transformed_df = transform_data(raw_data)

        load_to_bigquery(transformed_df)

        logging.info("Pipeline completed successfully")

    else:
        logging.error("Pipeline failed")


if __name__ == "__main__":
    main()