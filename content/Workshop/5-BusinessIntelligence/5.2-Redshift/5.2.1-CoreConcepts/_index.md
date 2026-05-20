---
title: "Core Concepts of Redshift Serverless"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 2.1. </b> "
---
## What is a Namespace?

A namespace contains all database-related components:

- Database objects (schemas, tables, views)
- Users and permissions
- IAM roles
- Data warehouse metadata
- Encryption settings

In our case, the "manhattan-redshift-namespace" contains the "dev" database.

## What is a Workgroup?

A workgroup is the compute part for running queries:

- Base capacity (RPU - Redshift Processing Units)
- Endpoint for connection
- VPC/subnet/security group
- Query monitoring
- Cost/performance controls

The "manhattan-redshift-workgroup" has 4 base RPU and an endpoint for Query Editor v2 connection.

## The Difference

- **Namespace**: The "storage/metadata" part of the database
- **Workgroup**: The "compute/query engine" part

They are separated to manage storage and compute independently.

![Redshift Serverless Architecture](/images/manhattan-dataways/redshift-spectrum/redshift_serverless_architecture.png)

# Capacity and RPU

## What is RPU?

RPU (Redshift Processing Unit) measures the compute power of Redshift Serverless, including CPU, memory, network, and query processing power.

## Capacity Levels

- 4 RPU: Minimum, suitable for light tests/queries
- 8 RPU: Medium, more comfortable
- 16-32 RPU: For larger data queries
- 128 RPU: Default, powerful but expensive

We chose 4 RPU because we're only testing queries on taxi data (~a few hundred MB).

## Cost

Redshift Serverless charges based on RPU-hours used. Higher capacity means higher costs for heavy queries. For hands-on work, 4 RPU helps save money.

# IAM Role

Redshift needs an IAM role to:

- Read data from S3 buckets (yellow-taxi-trip-demo-fcaj, processed-yellow-taxi-trip-data)
- Access Glue Data Catalog
- Perform operations like COPY, UNLOAD

The role is created with AmazonS3ReadOnlyAccess and AWSGlueServiceRole permissions to read S3 and Glue.

# Free Trial

Redshift Serverless has a $300 free trial credit for 90 days for new accounts. This is separate from the AWS Free Tier $200.

We use this credit to avoid charges during learning.
