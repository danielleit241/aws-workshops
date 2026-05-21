---
title: "AWS Glue ETL Job"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---
### Overview

In this section, we will create and run an **AWS Glue ETL Job** using the **PySpark Script Editor** to process Yellow Taxi trip data. The ETL Job will read raw data from Amazon S3, perform data cleaning, schema standardization, data quality validation, and separate valid records from invalid records before writing the results back to Amazon S3.

Unlike Glue Visual ETL, this section uses a fully custom PySpark Script to control the entire ETL and validation workflow.

After completing this section, you will be able to:

- Create an AWS Glue ETL Job using Script Editor
- Configure runtime parameters for a Glue Job
- Read Parquet files from Amazon S3 using PySpark
- Perform Data Cleaning and Data Transformation
- Build Feature Engineering logic using PySpark
- Implement a rule-based validation pipeline
- Separate valid and invalid datasets
- Write partitioned output datasets using `year/month`
- Monitor ETL Job execution in AWS Glue

---

### Key Concepts

Before creating the ETL Job, you should understand the main components used in this section.

---

#### AWS Glue ETL Job

AWS Glue ETL Job is a fully managed Apache Spark job running on AWS for large-scale data processing.

Glue ETL supports two modes:

- Visual Editor
- Script Editor

In this workshop, we will use **Script Editor** with **PySpark** to build the ETL pipeline.

Advantages of Script Editor:
- Full control over ETL logic
- Easier implementation of complex validation rules
- Scalable distributed processing using Spark
- Flexible pipeline customization

---

#### Amazon S3 Data Lake

The pipeline uses Amazon S3 as the Data Lake with three main buckets:

| Bucket | Purpose |
|---|---|
| Raw Bucket | Store raw input datasets |
| Processed Bucket | Store cleaned and validated datasets |
| Quarantine Bucket | Store invalid or abnormal records |

---

#### Partition-based Processing

Datasets are processed using partition structure:

```text
year=YYYY/month=MM