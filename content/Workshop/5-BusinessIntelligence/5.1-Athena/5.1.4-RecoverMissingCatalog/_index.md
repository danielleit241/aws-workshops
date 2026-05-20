---
title: "Recover Missing Catalog"
date: "2026-05-20"
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

This page is **optional**. Use it only if the expected Glue database or table does not appear in Athena, or if the schema is incorrect.

## Recovery A: Create the Glue Database

If the workshop database does not exist yet, create it in AWS Glue.

![Create Glue database for Athena](/images/Workshop/5.1%20Athena/24.png)

## Recovery B: Run the Glue Crawler

If the table metadata is missing, run the crawler that scans the processed S3 location.

![Run the Glue crawler](/images/Workshop/5.1%20Athena/28.png)

Wait until the crawler completes successfully.

![Crawler completed successfully](/images/Workshop/5.1%20Athena/30.png)

## Recovery C: Review the Schema

If the table appears but the schema is inconsistent, open the Glue table definition and inspect the schema.

![Open the Glue table schema](/images/Workshop/5.1%20Athena/33.png)

If you fix invalid or duplicated fields, save a new schema version.

![Save the corrected table schema](/images/Workshop/5.1%20Athena/37.png)

{{% notice warning %}}
Only apply this recovery flow when the normal Glue pipeline output is missing or incorrect.
{{% /notice %}}
