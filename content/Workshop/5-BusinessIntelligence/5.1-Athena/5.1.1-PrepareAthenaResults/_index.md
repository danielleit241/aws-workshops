---
title: "Prepare Athena Results"
date: "2026-05-20"
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

Before Athena can run queries, it needs an **Amazon S3 output location** to store query results.

In this page, you will create that bucket and connect it to Athena.

## Step 1: Open Amazon S3

From the AWS Console, search for **Amazon S3** and open the service.

![Open Amazon S3](/images/Workshop/5.1%20Athena/1.png)

## Step 2: Create a Dedicated Result Bucket

In the S3 bucket list, choose **Create bucket**.

![Create bucket from S3 console](/images/Workshop/5.1%20Athena/2.png)

Create a **general purpose bucket** and give it a dedicated name for Athena query results.

![Configure bucket type and name](/images/Workshop/5.1%20Athena/3.png)

After reviewing the default settings, scroll down and choose **Create bucket**.

![Finalize Athena result bucket creation](/images/Workshop/5.1%20Athena/4.png)

## Step 3: Configure Athena Output Settings

After the bucket is ready, open Athena Query Editor and choose **Edit settings**.

![Open Athena settings](/images/Workshop/5.1%20Athena/7.png)

Choose the S3 bucket you created for query results, then save the configuration.

![Save Athena query result location](/images/Workshop/5.1%20Athena/11.png)

Athena should confirm that the result location has been updated successfully.

![Verify Athena query settings](/images/Workshop/5.1%20Athena/12.png)

{{% notice tip %}}
Athena cannot run queries until an output S3 location is configured.
{{% /notice %}}
