---
title: "Truy vấn Glue Catalog với Redshift Spectrum"
date: "2026-05-02"
weight: 5
chapter: false
pre: " <b> 2.5. </b> "
---

Sau khi external schema đã được tạo và sửa lỗi duplicate, chúng ta có thể query dữ liệu.

## Query mẫu

```sql
SELECT *
FROM taxi_processed.processed_yellow_taxi_trip_data
LIMIT 30;
```

![Query limit 30](/images/Workshop/5.2-Redshift/5-QueryGlueCatalog/1-RunQueries/final-query-limit-30.png)

## Query theo partition

```sql
SELECT vendorid, tpep_pickup_datetime, passenger_count, trip_distance, total_amount, trip_duration_min
FROM taxi_processed.processed_yellow_taxi_trip_data
WHERE year = '2025' AND month = '01'
LIMIT 20;
```

## Query thống kê

```sql
SELECT year, month, COUNT(*) AS total_trips
FROM taxi_processed.processed_yellow_taxi_trip_data
GROUP BY year, month
ORDER BY year, month;
```

## Query analytics

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

![Kết quả query](/images/Workshop/5.2-Redshift/5-QueryGlueCatalog/1-RunQueries/query-results.png)

Redshift Spectrum cho phép query trực tiếp dữ liệu Parquet từ S3 thông qua Glue metadata mà không cần load data vào Redshift native tables.
