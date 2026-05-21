---
title: "AWS Glue ETL Job"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

### Overview

In this section, we will create and run an **AWS Glue ETL Job** to read raw data from the **AWS Glue Data Catalog**, apply transformations, and write the processed output back to **Amazon S3**.

After completing this section, you will be able to:

- Create an AWS Glue ETL Job using the Visual Editor
- Configure the data source from the Glue Data Catalog
- Apply basic transformations to the dataset
- Configure the output target in Amazon S3
- Run the ETL Job and verify the output


### Key Concepts

Before creating the ETL Job, it is helpful to understand the main components involved in this section.

**AWS Glue ETL Job**

An AWS Glue ETL Job is a managed Apache Spark job that runs on AWS infrastructure. It can read data from various sources, apply transformations, and write the output to a target destination.

Glue ETL Jobs support two authoring modes:

- Visual Editor — a drag-and-drop interface for building pipelines without writing code
- Script Editor — write PySpark or Scala scripts directly

In this workshop, we will use the **Visual Editor**.

**Data Source**

The ETL Job reads data from the **AWS Glue Data Catalog** table created by the crawler in section 4.1.

The catalog table contains:
- The S3 location of the raw Parquet files
- The schema and column definitions
- The file format

**Transformations**

Transformations are operations applied to the data before writing the output. Common examples include:

- Selecting or dropping columns
- Renaming columns
- Filtering rows
- Changing data types
- Joining datasets

**Data Target**

The output of the ETL Job is written back to **Amazon S3** in a specified location. The output format can be configured as Parquet, CSV, JSON, or other supported formats.

### Configuration

In this workshop, we will use the following sample configuration.

| Resource              | Value                                        |
| --------------------- | -------------------------------------------- |
| Glue Job Name         | `glue_etl_job_taxi`                          |
| IAM Role              | `AWSGlueServiceRole-Crawlers`                |
| Data Source           | Glue Data Catalog — `craw_data_catalog`      |
| Source Table          | `table_yellow_taxi_trip_demo_fcaj`           |
| Output S3 Path        | `s3://yellow-taxi-trip-demo-fcaj/output/`    |
| Output Format         | Parquet                                      |
| Glue Version          | Glue 4.0                                     |

You can adjust these values based on your own AWS environment.

**Step 1: Create a new ETL Job**

1. Go to the [AWS Glue Console](https://console.aws.amazon.com/glue/home)
2. In the left navigation pane, choose **ETL Jobs**
3. Choose **Visual ETL**

![CreateJob](/images/Workshop/4.Glue/4.2.ETL/4.2.2.png)

**Step 2: Configure the data source**

1. In the Visual Editor, click the **Source** node to open its configuration panel
2. Under **Data source properties**, select **AWS Glue Data Catalog** as the source type
3. Choose the **Database** created in section 4.1 (e.g., `craw_data_catalog`)
4. Choose the **Table** created by the crawler (e.g., `table_yellow_taxi_trip_demo_fcaj`)

![ConfigureSource](/images/Workshop/4.Glue/4.2.ETL/4.2.3.png)

{{% notice tip %}}
If you do not see your database or table in the dropdown, make sure the Glue Crawler from section 4.1 has been run successfully and the table appears in the Data Catalog.
{{% /notice %}}

**Step 3: Add a Transform node**

1. Click the **+** button to add a new node after the source
2. Select **Transform** and choose **ApplyMapping**
3. In the mapping panel, review the detected columns and their data types
4. You can rename columns, change data types, or drop columns that are not needed

![AddTransform](/images/Workshop/4.Glue/4.2.ETL/4.2.4.png)

{{% notice info %}}
ApplyMapping is the most common transform used in Glue Visual ETL. It lets you control which columns are passed to the output and how they are mapped.
{{% /notice %}}

**Step 4: Configure the data target**

1. Click the **+** button to add a new node after the transform
2. Select **Target** and choose **Amazon S3**
3. Set the **Format** to `Parquet`
4. Set the **S3 Target Location** to your output path, for example:

```text
s3://yellow-taxi-trip-demo-fcaj/output/
```

5. Under **Data Catalog update options**, choose **Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions** if you want the output to also be registered in the catalog

![ConfigureTarget](/images/Workshop/4.Glue/4.2.ETL/4.2.5.png)

**Step 5: Configure job properties**

1. Click the **Job details** tab at the top of the Visual Editor
2. Set the **Name** of the job (e.g., `glue_etl_job_taxi`)
3. Under **IAM Role**, select the role created in section 4.1 (e.g., `AWSGlueServiceRole-Crawlers`)
4. Set **Glue version** to `Glue 4.0 - Supports spark 3.3, Scala 2, Python 3`
5. Leave the remaining settings as default

![JobProperties](/images/Workshop/4.Glue/4.2.ETL/4.2.6.png)

{{% notice tip %}}
Make sure the IAM Role has permission to read from the source S3 bucket and write to the output S3 path. You configured this in section 4.1 when setting up the crawler role.
{{% /notice %}}

**Step 6: Save and run the job**

1. Click **Save** to save the job configuration
2. Click **Run** to start the ETL Job

![RunJob](/images/Workshop/4.Glue/4.2.ETL/4.2.7.png)

3. The job will appear in the **Runs** tab with a status of **Running**
4. Wait for the status to change to **Succeeded**

{{% notice info %}}
The first run may take 2–3 minutes to start as Glue provisions the Spark environment. This is normal behavior.
{{% /notice %}}

### Verify the Output

After the job completes successfully, verify that the output files have been written to S3.

1. Go to the [Amazon S3 Console](https://s3.console.aws.amazon.com/s3/home)
2. Navigate to your output bucket and path (e.g., `s3://yellow-taxi-trip-demo-fcaj/output/`)
3. Confirm that Parquet files have been created in the output folder

![VerifyOutput](/images/Workshop/4.Glue/4.2.ETL/4.2.8.png)

{{% notice tip %}}
If the output folder is empty or the job failed, check the **Error logs** in the Runs tab. Common issues include missing S3 permissions or an incorrect S3 output path.
{{% /notice %}}

### Summary

In this section, we created an AWS Glue ETL Job using the Visual Editor.

The job reads raw Parquet data from the Glue Data Catalog, applies column mapping transformations, and writes the processed output back to Amazon S3.

| Step | Action                                      |
| ---- | ------------------------------------------- |
| 1    | Created a new Visual ETL Job                |
| 2    | Configured the Glue Data Catalog as source  |
| 3    | Added an ApplyMapping transform             |
| 4    | Configured Amazon S3 as the output target   |
| 5    | Set job properties and IAM role             |
| 6    | Ran the job and verified the S3 output      |

In the next section, we will use **Amazon Athena** to query the processed data directly from Amazon S3 using the metadata stored in the Glue Data Catalog.
