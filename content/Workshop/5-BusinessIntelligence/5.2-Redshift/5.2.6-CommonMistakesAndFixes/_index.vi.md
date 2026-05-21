---
title: "Sai lầm phổ biến và cách khắc phục"
date: "2026-05-02"
weight: 6
chapter: false
pre: " <b> 2.6. </b> "
---

![Đường dẫn sai và đúng với Spectrum](/images/Workshop/5.2-Redshift/6-CommonMistakes/1-PathIssues/spectrum_query_paths.png)

## Sai lầm 1: Sử dụng "Load data" thay vì External Schema

Khi mới vào Query Editor v2, có thể nhầm click "Load data" để import data vào Redshift native table.

![Load data - đường dẫn sai](/images/Workshop/5.2-Redshift/6-CommonMistakes/1-PathIssues/load-data-wrong-path.png)

### Tại sao sai?

Load data dùng để COPY data từ S3 vào Redshift internal tables, phù hợp khi muốn store data trong Redshift.

Nhưng mục tiêu của chúng ta là query external data từ S3/Glue mà không copy.

### Cách khắc phục

- Cancel Load data
- Sử dụng CREATE EXTERNAL SCHEMA để reference Glue Catalog
- Query thông qua external tables

## Sai lầm 2: Map sai Glue Database

Ban đầu có thể tạo external schema trỏ vào craw_data_catalog (raw data) thay vì processed database.

### Dấu hiệu

```sql
SELECT schemaname, tablename FROM svv_external_tables WHERE schemaname = 'taxi_raw';
```

![Không có external tables](/images/Workshop/5.2-Redshift/6-CommonMistakes/2-MetadataIssues/no-external-tables.png)

### Khắc phục

- Tạo Glue Crawler cho processed S3 bucket
- Tạo external schema trỏ vào processed database
- Đảm bảo database name chính xác

## Sai lầm 3: Duplicate Columns trong Glue Table

Glue table có year/month xuất hiện cả ở normal columns và partition keys.

### Lỗi

External table "taxi_processed.processed_yellow_taxi_trip_data" has column "year" duplicated

### Nguyên nhân

ETL job ghi year/month vào Parquet data, đồng thời S3 path dùng Hive partition year=.../month=...

Glue Crawler infer duplicate.

### Khắc phục

Edit Glue table schema: xóa year/month khỏi normal columns, giữ ở partition keys.

Sau đó refresh Redshift metadata.

## Sai lầm 4: IAM Role không có quyền

Nếu query lỗi access denied, kiểm tra IAM role có quyền đọc S3 buckets và Glue catalog.

Role cần: AmazonS3ReadOnlyAccess, AWSGlueServiceRole policies.

## Sai lầm 5: Wrong Region

Đảm bảo tất cả resources ở cùng region us-east-2.

## Best Practices

- Luôn test với LIMIT trước khi query toàn bộ
- Sử dụng partition filters để tối ưu performance
- Kiểm tra svv_external_schemas và svv_external_tables để verify metadata
