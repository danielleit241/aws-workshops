---
title: "Introduction"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---
This workshop will use the following AWS resources and services:

**Amazon S3:**  
Amazon Simple Storage Service (S3) is used as the Data Lake foundation for the entire system. S3 stores Yellow Taxi datasets at multiple stages, including Raw Data, Processed Data, and Quarantine/Error Data. In addition, S3 acts as the primary data source for Athena, Redshift, and Glue ETL Jobs.

**AWS Step Functions:**  
AWS Step Functions is used to orchestrate the entire data processing workflow. The service organizes ETL stages using a State Machine architecture, making the pipeline easier to manage, monitor, and extend with additional processing steps in the future.

**AWS Glue Crawler and AWS Glue Data Catalog:**  
AWS Glue Crawler is used to automatically scan datasets stored in Amazon S3 to detect schema and metadata. The discovered metadata is then stored inside AWS Glue Data Catalog, which is later used by ETL processing and analytical query services such as Amazon Athena.

**AWS Glue ETL Job:**  
AWS Glue ETL Job uses Apache Spark and PySpark Script to process large-scale datasets. The ETL pipeline performs:
- Data Cleaning
- Missing Value Handling
- Financial Data Standardization
- Feature Engineering
- Rule-based Data Validation
- Partition-based Data Processing

The processed datasets are written back to Amazon S3 in Parquet format.

**Amazon Athena:**  
Amazon Athena is used to directly query processed datasets stored in Amazon S3 using standard SQL without provisioning infrastructure. Athena supports exploratory analysis and ad-hoc querying on partitioned datasets inside the Data Lake.

**Amazon Redshift:**  
Amazon Redshift acts as the Data Warehouse for OLAP and analytical workloads. Processed datasets from S3 are loaded into Redshift to optimize query performance and support business intelligence dashboards.

**Amazon QuickSight:**  
Amazon QuickSight is a cloud-based business intelligence service used to visualize data through dashboards and analytical charts. QuickSight connects to Redshift to display:
- Trip Demand Analysis
- Revenue Analysis
- Vendor Performance
- Spatial Analysis

**IAM, CloudTrail, CloudWatch, and SNS:**  
AWS Identity and Access Management (IAM) is used to manage permissions and secure interactions between AWS services within the system.

AWS CloudTrail records API activities and resource operations for auditing and security tracking purposes.

Amazon CloudWatch is used to monitor ETL Jobs, Glue Logs, and workflow execution status.

Amazon SNS is used to send alerts and notifications when pipeline failures or processing errors occur.

> **Note:** Using Amazon EventBridge together with CloudWatch is optional. If the system does not require event-driven architecture or complex event routing, CloudWatch can still be used independently for monitoring, logging, and alerting as usual.