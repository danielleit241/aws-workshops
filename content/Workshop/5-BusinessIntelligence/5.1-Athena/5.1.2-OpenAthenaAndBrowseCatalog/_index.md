---
title: "Open Athena and Browse Catalog"
date: "2026-05-20"
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

Now that Athena has a result location, the next step is to open the query interface and confirm that the processed Glue catalog objects are visible.

## Step 1: Open Amazon Athena

From the AWS Console, search for **Athena** and open the service.

![Open Amazon Athena](/images/Workshop/5.1%20Athena/5.png)

Choose **Launch query editor**.

![Launch Athena Query Editor](/images/Workshop/5.1%20Athena/6.png)

## Step 2: Confirm the Glue Database

In the left sidebar:

- Keep **Data source** as `AwsDataCatalog`
- Select the workshop database

![Choose the workshop database in Athena](/images/Workshop/5.1%20Athena/31.png)

## Step 3: Confirm the Processed Table

After the correct database is selected, the processed table should appear in the table list.

![Verify the processed table is available](/images/Workshop/5.1%20Athena/32.png)

If your database or table does not appear, continue to the recovery page before attempting queries.
