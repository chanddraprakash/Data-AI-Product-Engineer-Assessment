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
