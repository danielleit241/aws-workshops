---
title: "Setting up Redshift Serverless"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2.2. </b> "
---

To use Redshift Spectrum, we need to create a Redshift Serverless environment. Redshift Serverless is suitable for querying data from S3/Glue without managing infrastructure.

## Step 1: Access Redshift Console

1. Go to Amazon Redshift console
2. On the dashboard, you'll see no existing namespaces/workgroups

![Redshift Serverless Dashboard](/images/manhattan-dataways/redshift-spectrum/01-existing-glue-stack-overview.png)

3. Click "Create workgroup"

## Step 2: Customize Configuration

In the "Get started with Amazon Redshift Serverless" screen, click "Customize settings" for detailed configuration instead of defaults.

![Get started customize screen](/images/manhattan-dataways/redshift-spectrum/02-redshift-get-started-customize.png)

### Namespace Configuration

- **Namespace name**: manhattan-redshift-namespace
- **Database name**: dev
- **Admin credentials**: Created based on IAM credentials (use current IAM user)

### Workgroup Configuration

- **Workgroup name**: manhattan-redshift-workgroup

### Capacity and Cost Controls

Reduce Base capacity from 128 to 4 RPU to save costs for hands-on work.

![Reduce capacity from 128 to 4](/images/manhattan-dataways/redshift-spectrum/03-redshift-capacity-128-to-4.png)

### IAM Role

Create a new IAM role for Redshift to read S3 and Glue:

1. Select "Create IAM role"
2. Select buckets: yellow-taxi-trip-demo-fcaj, processed-yellow-taxi-trip-data, quarantine-yellow-taxi-trip-data
3. Set as default role

![Workgroup and IAM role](/images/manhattan-dataways/redshift-spectrum/04-redshift-workgroup-iam-default.png)

### Network and Security

- VPC: default VPC
- Publicly accessible: No (for security)
- SSL: Enable

## Step 3: Create and Wait for Available

Click "Save configuration". AWS will create the namespace and workgroup.

Wait until workgroup status becomes "Available".

![Workgroup available](/images/manhattan-dataways/redshift-spectrum/05-redshift-workgroup-available.png)

![Redshift Serverless Setup Flow](/images/manhattan-dataways/redshift-spectrum/redshift_setup_flow.png)

## Why This Configuration

- 4 RPU capacity sufficient for test queries without high costs
- IAM role with necessary S3/Glue read permissions
- No public access enabled for security
