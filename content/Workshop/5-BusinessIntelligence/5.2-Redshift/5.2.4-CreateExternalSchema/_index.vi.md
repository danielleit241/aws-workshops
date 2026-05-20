---
title: "Tạo External Schema cho Glue Data Catalog"
date: "2026-05-02"
weight: 4
chapter: false
pre: " <b> 2.4. </b> "
---

Để truy vấn dữ liệu từ Glue Data Catalog thông qua Redshift Spectrum, chúng ta cần tạo external schema.

## Schema cho Processed Data

Vì mục tiêu là query processed data, chúng ta tạo schema trỏ vào processed database.

![Schema cho processed data](/images/manhattan-dataways/redshift-spectrum/19-schema-processed-data.png)

Trước tiên, cần tạo Glue Crawler cho processed S3 bucket.

### Tạo IAM Role cho Crawler

1. Vào IAM console
2. Tạo role với trusted entity: Glue
3. Attach policies: AWSGlueServiceRole, AmazonS3ReadOnlyAccess
4. Tên role: glue-role-manhattan-processed-crawler

![Tạo IAM role](/images/manhattan-dataways/redshift-spectrum/18-create-iam-role.png)

### Tạo Glue Crawler

1. Vào Glue console → Crawlers
2. Create crawler:
   - Name: glue-crawler-processed-yellow-taxi
   - Data source: S3, path s3://processed-yellow-taxi-trip-data/
   - IAM role: glue-role-manhattan-processed-crawler
   - Target database: redshift_database (tạo mới)
3. Run crawler

![Tạo Glue crawler](/images/manhattan-dataways/redshift-spectrum/20-create-glue-crawler.png)

![Crawler succeeded](/images/manhattan-dataways/redshift-spectrum/10-crawler-succeeded.png)

### Tạo External Schema trong Redshift

```sql
CREATE EXTERNAL SCHEMA IF NOT EXISTS taxi_processed
FROM DATA CATALOG
DATABASE 'redshift_database'
IAM_ROLE 'arn:aws:iam::878796852481:role/service-role/AmazonRedshift-CommandsAccessRole-20260429T193922'
REGION 'us-east-2';
```

![Tạo external schema](/images/manhattan-dataways/redshift-spectrum/16-create-external-schema.png)

Kiểm tra tables:

```sql
SELECT schemaname, tablename
FROM svv_external_tables
WHERE schemaname = 'taxi_processed';
```

![Kiểm tra tables](/images/manhattan-dataways/redshift-spectrum/17-check-tables.png)

## Sửa lỗi Duplicate Columns

Nếu gặp lỗi "column year duplicated", cần sửa Glue table schema.

Vào Glue console → Tables → processed_yellow_taxi_trip_data → Edit schema

Xóa year và month khỏi normal columns, giữ ở Partition keys.

![Sửa duplicate columns](/images/manhattan-dataways/redshift-spectrum/11-glue-schema-edit-duplicate.png)

Sau đó refresh Redshift metadata và query lại.
