---
title: "Query Glue Catalog with Redshift Spectrum"
date: "2026-05-02"
weight: 5
chapter: false
pre: " <b> 2.5. </b> "
---

After the external schema is created and duplicate errors are fixed, we can query the data.

## Sample Query

```sql
SELECT *
FROM taxi_processed.processed_yellow_taxi_trip_data
LIMIT 30;
```

![Query limit 30](/images/manhattan-dataways/redshift-spectrum/12-final-query-limit-30.png)

## Query by Partition

```sql
SELECT vendorid, tpep_pickup_datetime, passenger_count, trip_distance, total_amount, trip_duration_min
FROM taxi_processed.processed_yellow_taxi_trip_data
WHERE year = '2025' AND month = '01'
LIMIT 20;
```

## Statistical Query

```sql
SELECT year, month, COUNT(*) AS total_trips
FROM taxi_processed.processed_yellow_taxi_trip_data
GROUP BY year, month
ORDER BY year, month;
```

## Analytics Query

```sql
SELECT year, month, payment_type, COUNT(*) AS total_trips,
       ROUND(SUM(total_amount), 2) AS total_revenue,
       ROUND(AVG(total_amount), 2) AS avg_revenue,
       ROUND(AVG(trip_distance), 2) AS avg_trip_distance,
       ROUND(AVG(trip_duration_min), 2) AS avg_trip_duration_min
FROM taxi_processed.processed_yellow_taxi_trip_data
GROUP BY year, month, payment_type
ORDER BY year, month, payment_type;
```

![Query results](/images/manhattan-dataways/redshift-spectrum/13-query-results.png)

Redshift Spectrum allows direct queries of Parquet data from S3 through Glue metadata without loading data into Redshift native tables.
