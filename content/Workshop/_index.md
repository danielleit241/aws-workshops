---
title: "Data Pipeline with AWS Glue"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
## Contents

### Executive Summary

- Summary:  
This project aims to build an automated Data Analytics Pipeline on Amazon Web Services (AWS) using a Data Lakehouse architecture. The system is designed to process large-scale New York Yellow Taxi trip record datasets through data ingestion, metadata management, ETL processing, data warehousing, and visualization workflows.

- Objectives:
  - Build a Data Lake system on Amazon S3.
  - Automate ETL and data processing workflows.
  - Automatically manage schema and metadata.
  - Clean and standardize data before analytics.
  - Support direct SQL querying on S3 using Amazon Athena.
  - Build a Data Warehouse for OLAP workloads using Amazon Redshift.
  - Create interactive dashboards using Amazon QuickSight.
  - Establish monitoring and security mechanisms for the entire pipeline.

- Scope:
  - Build a Data Lake on Amazon S3.
  - Implement workflow orchestration using AWS Step Functions.
  - Use AWS Glue Crawler, AWS Glue Data Catalog, and AWS Glue ETL Job for metadata management and ETL processing.
  - Integrate Amazon Athena, Amazon Redshift, and Amazon QuickSight for analytics workloads.
  - Configure Monitoring & Security services using IAM, CloudTrail, CloudWatch, and SNS.

### Problem Statement

Current Challenges:  
The Yellow Taxi dataset contains a massive amount of continuously growing trip data. However, raw data contains multiple issues that negatively impact analytics quality:

- Missing or invalid values:
  - `passenger_count = null`
  - `trip_distance = 0`
  - `fare_amount < 0`
- Unstandardized schema across datasets.
- Difficulties in manually processing large-scale data.
- Lack of automated ETL and metadata management workflows.
- Poor query performance when querying raw data directly.
- Absence of a centralized platform for analytics and visualization workloads.

Technical Solution:  
The system implements a Data Lakehouse architecture on AWS:

- Input datasets are stored in the Amazon S3 Raw Bucket.
- AWS Step Functions orchestrates the data processing workflow.
- AWS Glue Crawler scans raw datasets to detect schema and metadata.
- AWS Glue Data Catalog stores metadata for ETL processing and query engines.
- AWS Glue ETL Job performs:
  - Data Cleaning
  - Data Transformation
  - Schema Standardization
  - Feature Engineering
- Processed datasets are stored in the S3 Processed Bucket in Parquet format.
- Amazon Athena supports direct SQL querying on processed datasets stored in S3.
- Amazon Redshift serves as the OLAP Data Warehouse.
- Amazon QuickSight provides data visualization and business dashboards.

### Solution Architecture

![overview](/images/Workshop/Architecture/Architecutre_final.png)

The system architecture follows the processing flow:

Raw &rarr; Metadata & ETL Processing &rarr; Analytics &rarr; Visualization.

**Technical Workflow Overview:**

- Ingestion: Input datasets (CSV/Parquet) are uploaded into the Amazon S3 Raw Bucket.
- Schema Crawling: AWS Glue Crawler scans raw datasets to detect schema and metadata.
- Metadata Management: AWS Glue Data Catalog stores metadata used for ETL processing and analytical query engines.
- ETL Processing: AWS Glue ETL Job performs:
  - Data Cleaning
  - Data Type Standardization
  - Missing Value Handling
  - Outlier Removal
  - Feature Engineering
- Processed Storage: Cleaned datasets are stored in the Amazon S3 Processed Bucket in Parquet format.
- Data Warehousing: Amazon Redshift loads processed datasets from S3 for OLAP and analytical workloads.
- Visualization: Amazon QuickSight connects to Amazon Redshift to create business intelligence dashboards.
- Ad-hoc Query: Amazon Athena supports direct SQL queries on processed datasets stored in S3.

**Technology Stack:**

| Layer                   | AWS Service                               | Purpose / Role                                      |
| ----------------------- | ----------------------------------------- | --------------------------------------------------- |
| Storage / Data Lake     | Amazon S3                                 | Store Raw Data and Processed Data                   |
| Workflow Orchestration  | AWS Step Functions                        | Orchestrate the data processing workflow            |
| Metadata Management     | AWS Glue Crawler, AWS Glue Data Catalog   | Manage schema and metadata                          |
| Data Processing (ETL)   | AWS Glue ETL Job                          | ETL and data transformation                         |
| Query Engine            | Amazon Athena                             | Direct SQL querying on S3                           |
| Data Warehouse          | Amazon Redshift                           | OLAP Data Warehouse                                 |
| BI / Visualization      | Amazon QuickSight                         | Dashboards and business reports                     |
| Security & Monitoring   | IAM, CloudTrail, CloudWatch, SNS          | Monitoring, logging, and alerting                   |

### Workflow Overview

- Step 1 — Data Ingestion:
  - Input datasets are uploaded into the Amazon S3 Raw Bucket.

- Step 2 — Schema Crawling:
  - AWS Glue Crawler scans datasets to detect schema and metadata.

- Step 3 — Metadata Management:
  - AWS Glue Data Catalog stores metadata used for ETL and query engines.

- Step 4 — ETL Processing:
  - AWS Glue ETL Job performs:
    - Data Cleaning
    - Schema Transformation
    - Missing Value Handling
    - Outlier Removal
    - Feature Engineering

- Step 5 — Processed Storage:
  - Processed datasets are stored in the Amazon S3 Processed Bucket in Parquet format.

- Step 6 — Data Warehousing:
  - Amazon Redshift loads datasets from the S3 Processed Bucket for analytical workloads.

- Step 7 — Visualization:
  - Amazon QuickSight connects to Redshift to create business intelligence dashboards.

- Step 8 — Ad-hoc Query:
  - Amazon Athena supports direct SQL querying on processed datasets stored in S3.

### Cost Estimation Model

The system uses a Pay-as-you-go pricing model to optimize operational costs.

Deployment region:
- `us-east-2`

Estimated weekly cost allocation:

| AWS Service                      | Weekly Cost |
| -------------------------------- | ------------ |
| Amazon S3                        | $1.50        |
| AWS Step Functions               | $0.15        |
| AWS Glue (Crawler + ETL Job)     | $8.00        |
| Amazon Athena                    | $0.50        |
| Amazon Redshift                  | $11.00       |
| Amazon QuickSight                | $8.00        |
| IAM, CloudTrail, CloudWatch, SNS | $1.00        |
| **Total**                        | **$30.15**   |
## Content

1. [Introduction](1-Introduction/)
2. [Preparation](2-Preparation/)
3. [Monitoring & Security](3-MonitoringSecurity/)
4. [Analytics Pipeline](4-AnalyticsPipeline/)
5. [Business Intelligence](5-BusinessIntelligence/)


