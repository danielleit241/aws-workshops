---
title: "Tạo External Schema cho Glue Data Catalog"
date: "2026-05-02"
weight: 4
chapter: false
pre: " <b> 2.4. </b> "
---

Để truy vấn dữ liệu từ Glue Data Catalog thông qua Redshift Spectrum, chúng ta cần tạo một external schema.

## Schema cho dữ liệu đã xử lý

Vì mục tiêu của chúng ta là truy vấn dữ liệu đã được xử lý, ta sẽ tạo một schema trỏ tới database chứa dữ liệu processed.

![Schema for processed data](/images/Workshop/5.2-Redshift/4-ExternalSchema/1-Prerequisites/schema-processed-data.png)

Trước tiên, chúng ta cần tạo một Glue Crawler cho bucket S3 đã xử lý.

### Tạo IAM Role cho Crawler

1. Vào IAM console
2. Tạo role với trusted entity: Glue
3. Gắn các policy: `AWSGlueServiceRole`, `AmazonS3ReadOnlyAccess`
4. Tên role: `glue-role-manhattan-processed-crawler`

![Create IAM role](/images/Workshop/5.2-Redshift/4-ExternalSchema/1-Prerequisites/create-iam-role.png)

### Tạo Glue Crawler

1. Vào Glue console → Crawlers
2. Tạo crawler:
   - Name: `glue-crawler-processed-yellow-taxi`
   - Data source: S3, đường dẫn `s3://processed-yellow-taxi-trip-data/`
   - IAM role: `glue-role-manhattan-processed-crawler`
   - Target database: `redshift_database` (tạo mới)
3. Chạy crawler

![Create Glue crawler](/images/Workshop/5.2-Redshift/4-ExternalSchema/1-Prerequisites/create-glue-crawler.png)

![Crawler succeeded](/images/Workshop/5.2-Redshift/4-ExternalSchema/3-Troubleshooting/crawler-succeeded.png)

### Tạo External Schema trong Redshift

```sql
CREATE EXTERNAL SCHEMA IF NOT EXISTS taxi_processed
FROM DATA CATALOG
DATABASE 'redshift_database'
IAM_ROLE 'arn:aws:iam::878796852481:role/service-role/AmazonRedshift-CommandsAccessRole-20260429T193922'
REGION 'us-east-2';
```

![Create external schema](/images/Workshop/5.2-Redshift/4-ExternalSchema/2-SchemaCreation/create-external-schema.png)

![External Schema Creation Flow](/images/Workshop/5.2-Redshift/4-ExternalSchema/2-SchemaCreation/external_schema_flow.png)

Kiểm tra các bảng:

```sql
SELECT schemaname, tablename
FROM svv_external_tables
WHERE schemaname = 'taxi_processed';
```

![Check tables](/images/Workshop/5.2-Redshift/4-ExternalSchema/2-SchemaCreation/check-tables.png)

## Sửa lỗi cột bị trùng lặp

Nếu bạn gặp lỗi `column year duplicated`, hãy chỉnh lại schema của Glue table.

Vào Glue console → Tables → `processed_yellow_taxi_trip_data` → Edit schema

Xóa `year` và `month` khỏi nhóm cột thông thường, chỉ giữ chúng trong **Partition keys**.

![Fix duplicate columns](/images/Workshop/5.2-Redshift/4-ExternalSchema/3-Troubleshooting/glue-schema-edit-duplicate.png)

Sau đó làm mới metadata của Redshift và truy vấn lại.
