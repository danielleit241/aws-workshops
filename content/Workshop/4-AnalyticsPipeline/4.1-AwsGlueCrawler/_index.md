---
title: "AWS Glue Crawler"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

## Overview

In this section, we will configure an **AWS Glue Crawler** to automatically scan data from Amazon S3, detect the schema, and create metadata tables in the **AWS Glue Data Catalog**.

After completing this session, you will be able to:

- Create a Glue Database in the Data Catalog
- Create an IAM Role for the Glue Crawler
- Configure an S3 data source for the Crawler
- Configure the output database and table prefix
- Create and run a Glue Crawler
- Verify the generated table in the Glue Data Catalog

## Architecture Overview
![overview](/images/Workshop/4.Glue/4.1Crawler/diagram-architecture.jpg)
The architecture of this lab is designed to demonstrate a common data discovery pattern on AWS.

Raw data is stored in **Amazon S3** in Parquet format. **AWS Glue Crawler** scans the data source, identifies the file structure, detects the schema, and creates metadata tables inside the **AWS Glue Data Catalog**. After the metadata is available, an **AWS Glue ETL Job** can use that catalog information to read, transform, and write processed data back to Amazon S3.

> Important: AWS Glue Crawler does not move or copy your data into the Data Catalog.  
> The actual data still stays in Amazon S3. The Data Catalog only stores metadata such as table name, schema, column types, partitions, and S3 location.

The simplified workflow is:


![workflow] (/images/Workshop/4.Glue/4.1Crawler/aws-glue-crawler-etl-flow.png)

Key Concepts

Before creating the crawler, it is important to understand the main components involved in this lab.

Amazon S3

Amazon S3 is used as the data lake storage layer. In this workshop, the raw dataset is stored in S3 as Parquet files.

Example:

s3://yellow-taxi-trip-demo-fcaj

Parquet is commonly used in analytics workloads because it is columnar, compressed, and efficient for large-scale data processing.

AWS Glue Crawler

AWS Glue Crawler automatically scans data stored in S3 and detects schema information.

The crawler can identify:

File format
Column names
Data types
Partition structure
S3 location
Table metadata

The crawler then writes this metadata into the AWS Glue Data Catalog.

AWS Glue Data Catalog

AWS Glue Data Catalog is a centralized metadata repository. It stores databases and tables that describe your data.

For example, after the crawler scans S3, it may create a table that points to your Parquet files.

This table can later be used by:

AWS Glue ETL Jobs
Amazon Athena
Amazon EMR
Amazon Redshift Spectrum
Other analytics services
AWS Glue ETL Job

AWS Glue ETL Job is used to transform data. It can read data from S3 by using the table definition from Glue Data Catalog.

In this lab, we only prepare the crawler and Data Catalog layer. The ETL Job will be used in the next stage of the workshop.

Lab Configuration

In this workshop, we will use the following sample configuration.

Resource	Value
Source S3 Bucket	s3://yellow-taxi-trip-demo-fcaj
Glue Crawler Name	glue_crawler_data
Glue Database Name	craw_data_catalog
IAM Role	AWSGlueServiceRole-Crawlers
Table Prefix	table_
Crawler Schedule	On demand

You can change these names based on your own AWS environment.

### Configuration
In this workshop, we will use the following sample configuration.

| Resource           | Value                             |
| ------------------ | --------------------------------- |
| Source S3 Bucket   | `s3://yellow-taxi-trip-demo-fcaj` |
| Glue Crawler Name  | `glue_crawler_data`               |
| Glue Database Name | `craw_data_catalog`               |
| IAM Role           | `AWSGlueServiceRole-Crawlers`     |
| Table Prefix       | `table_`                          |
| Crawler Schedule   | `On demand`                       |

You can change these names based on your own AWS environment.

####  1.Open AWS Glue Crawlers
        1. Go to the [AWS Glue Console](https://console.aws.amazon.com/glue/home)
        2. In the left navigation pane, choose **Crawlers**
        3. Choose **Add crawler**
![OpenCrawlers](/images/Workshop/4.Glue/4.1Crawler/create_crawler.png.png)

#### 2. Choose Data Source Configuration
        1.Click add a data source button

![DataSrc](/images/Workshop/4.Glue/4.1Crawler/add_data_src.png)

