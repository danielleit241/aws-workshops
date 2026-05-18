---
title: "AWS Glue Catalog"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

## AWS Glue Data Catalog

### Overview

AWS Glue Data Catalog is a centralized metadata repository used to store information about data sources in a data lake.

In this workshop, the actual dataset is stored in **Amazon S3**, while the **AWS Glue Data Catalog** stores only the metadata that describes that dataset.

{{% notice info %}}
AWS Glue Data Catalog does not store the actual data.  
It stores metadata that helps AWS services understand where the data is located and how the data is structured.
{{% /notice %}}

### What Does the Data Catalog Store?

When an AWS Glue Crawler scans data from Amazon S3, it creates or updates metadata tables in the Glue Data Catalog.

The Data Catalog can store information such as:

- Database name
- Table name
- Column names
- Column data types
- File format
- S3 location
- Partition information
- Table properties

For example, if the raw dataset is stored in:

```text
s3://yellow-taxi-trip-demo-fcaj
```

The Data Catalog table may store metadata that describes:
- Location: s3://yellow-taxi-trip-demo-fcaj
- Format: Parquet
- Columns: vendorid, trip_distance, total_amount, ...
- Data types: bigint, double, timestamp, ...

The actual Parquet files still remain in Amazon S3.
Data Catalog as a Metadata Layer

The relationship can be understood like this:

![DataCatalog](/images/Workshop/4.Glue/4.1.Crawler/4.1.15.png)

{{% notice tip %}}
You can think of Amazon S3 as the storage layer and AWS Glue Data Catalog as the map of the data.
{{% /notice %}}

### Database and Table in Data Catalog

In AWS Glue Data Catalog, metadata is organized into databases and tables.

Database

A database is a logical container used to group related metadata tables.
For example: 
![DataCatalog](/images/Workshop/4.Glue/4.1.Crawler/4.1.17.png)

This database does not contain the actual data. It only contains table definitions.

Table

A table represents the structure of a dataset.

A Glue table usually contains:

- The S3 path of the dataset
- The file format
- The schema
- The columns and data types
- Partition information, if available

For example, a table created by the crawler may point to Parquet files stored in S3.

### Why Is the Data Catalog Important?

The Data Catalog allows multiple AWS analytics services to use the same metadata definition.

Instead of manually defining the schema for each service, you can define it once in the Data Catalog and reuse it across different services.

The same Data Catalog table can be used by:

- *** AWS Glue ETL Job ***  to transform data
- *** Amazon Athena *** to query data using SQL
- *** Amazon EMR *** to process large-scale data
- *** Amazon Redshift Spectrum *** to query data directly from S3
This makes the data lake easier to manage and reduces duplicated configuration.


### Data Catalog Does Not Replace S3
It is important to understand the difference between Amazon S3 and AWS Glue Data Catalog.

| Component             | Responsibility                     |
| --------------------- | ---------------------------------- |
| Amazon S3             | Stores the actual data files       |
| AWS Glue Crawler      | Scans data and detects schema      |
| AWS Glue Data Catalog | Stores metadata about the data     |
| AWS Glue ETL Job      | Reads, transforms, and writes data |

The Data Catalog only tells AWS services how to understand the data. It does not own or physically store the dataset.

### Simple Analogy
You can imagine the Data Catalog like a library catalog.

The books are stored on shelves.
The catalog does not contain the books themselves.
It only tells you:

- What books are available
- Where they are located
- What category they belong to
- How they are organized

Similarly:
- Amazon S3 stores the real data
- Data Catalog stores the description of that data

### Summary 
AWS Glue Data Catalog is an important metadata layer in an AWS data lake architecture.

In this workshop, it helps us:
- Store schema information detected by the crawler
- Organize metadata using databases and tables
- Allow Glue ETL Jobs and other analytics services to understand S3 data
- Separate physical data storage from metadata management
In the next section, we will use this metadata layer as the source for an AWS Glue ETL Job.