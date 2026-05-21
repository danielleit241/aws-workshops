---
title: "Create External Schema for Glue Data Catalog"
date: "2026-05-02"
weight: 4
chapter: false
pre: " <b> 2.4. </b> "
---

To query data from Glue Data Catalog through Redshift Spectrum, we need to create an external schema.

## Schema for Processed Data

Since our goal is to query processed data, we create a schema pointing to the processed database.

![Schema for processed data](/images/Workshop/5.2-Redshift/4-ExternalSchema/1-Prerequisites/schema-processed-data.png)

First, we need to create a Glue Crawler for the processed S3 bucket.

### Create IAM Role for Crawler

1. Go to IAM console
2. Create role with trusted entity: Glue
3. Attach policies: AWSGlueServiceRole, AmazonS3ReadOnlyAccess
4. Role name: glue-role-manhattan-processed-crawler

![Create IAM role](/images/Workshop/5.2-Redshift/4-ExternalSchema/1-Prerequisites/create-iam-role.png)

### Create Glue Crawler

1. Go to Glue console → Crawlers
2. Create crawler:
   - Name: glue-crawler-processed-yellow-taxi
   - Data source: S3, path s3://processed-yellow-taxi-trip-data/
   - IAM role: glue-role-manhattan-processed-crawler
   - Target database: redshift_database (create new)
3. Run crawler

![Create Glue crawler](/images/Workshop/5.2-Redshift/4-ExternalSchema/1-Prerequisites/create-glue-crawler.png)

![Crawler succeeded](/images/Workshop/5.2-Redshift/4-ExternalSchema/3-Troubleshooting/crawler-succeeded.png)

### Create External Schema in Redshift

```sql
CREATE EXTERNAL SCHEMA IF NOT EXISTS taxi_processed
FROM DATA CATALOG
DATABASE 'redshift_database'
IAM_ROLE 'arn:aws:iam::878796852481:role/service-role/AmazonRedshift-CommandsAccessRole-20260429T193922'
REGION 'us-east-2';
```

![Create external schema](/images/Workshop/5.2-Redshift/4-ExternalSchema/2-SchemaCreation/create-external-schema.png)

![External Schema Creation Flow](/images/Workshop/5.2-Redshift/4-ExternalSchema/2-SchemaCreation/external_schema_flow.png)

Check tables:

```sql
SELECT schemaname, tablename
FROM svv_external_tables
WHERE schemaname = 'taxi_processed';
```

![Check tables](/images/Workshop/5.2-Redshift/4-ExternalSchema/2-SchemaCreation/check-tables.png)

## Fix Duplicate Columns Error

If you encounter "column year duplicated" error, fix the Glue table schema.

Go to Glue console → Tables → processed_yellow_taxi_trip_data → Edit schema

Remove year and month from normal columns, keep them in Partition keys.

![Fix duplicate columns](/images/Workshop/5.2-Redshift/4-ExternalSchema/3-Troubleshooting/glue-schema-edit-duplicate.png)

Then refresh Redshift metadata and query again.
