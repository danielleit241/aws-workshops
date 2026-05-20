---
title: "Athena"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

In this section, we introduce **Amazon Athena** as the fastest way to start analyzing the processed dataset created by the AWS Glue pipeline.

Athena is a **serverless interactive query service** that allows us to run SQL directly on data stored in **Amazon S3**. Because it integrates with the **AWS Glue Data Catalog**, Athena can immediately use the table metadata discovered and maintained earlier in the workshop.

### Why Athena Comes First

Athena is a natural first step in the business intelligence layer because it requires:

- No infrastructure to provision
- No database server to manage
- No data loading into a separate analytics engine

Once the processed data is available in Amazon S3 and registered in the Glue Data Catalog, Athena can query it directly.

{{% notice info %}}
Athena is ideal for validation, exploration, and ad-hoc analysis before moving to more warehouse-oriented analytics patterns.
{{% /notice %}}

### How Athena Fits in This Workshop

In the previous chapter, the data pipeline produced a cleaned and structured dataset. Athena sits on top of that output and uses the cataloged metadata to interpret the files correctly.

The flow is:

![Athena Query Flow](/images/Workshop/5-BusinessIntelligence/athena_query_flow.png)

This means Athena does not replace AWS Glue. Instead:

- **Amazon S3** stores the actual data files
- **AWS Glue Data Catalog** stores the table definitions and schema
- **Athena** reads both to execute SQL queries

### What Athena Is Good For

Athena is commonly used for:

- Quick validation of ETL outputs
- Ad-hoc SQL analysis on data lake files
- Exploring data without building a data warehouse first
- Checking record counts, distributions, and aggregates
- Investigating partitions and filtered subsets of data

For this workshop, Athena helps confirm that the processed taxi trip data is ready for analytics and can answer common business questions.

### Example Questions Athena Can Answer

With Athena, you can run SQL queries such as:

- How many taxi trips exist in the processed dataset?
- What is the average fare amount by payment type?
- Which pickup dates generate the highest revenue?
- How does trip distance vary across time periods?
- What are the most common passenger count patterns?

These are useful examples of **business-facing questions** that can be answered directly from the data lake.

### Benefits of Using Athena

| Benefit | Explanation |
|---|---|
| Serverless | No cluster or database instance is required |
| SQL-based | Uses familiar query language for analysis |
| Glue Integration | Reuses metadata from the Data Catalog |
| S3-native | Queries data directly where it is stored |
| Pay-per-query | Cost is based on data scanned rather than idle infrastructure |

{{% notice tip %}}
Athena works best when the source data is stored in efficient formats such as Parquet and organized with clear partitioning. That is one reason the earlier Glue pipeline design matters.
{{% /notice %}}

### Athena in Relation to Redshift and QuickSight

Athena is not the final BI service in this workshop. It is the **entry point for querying**.

- Use **Athena** when you want simple, direct, SQL-based access to S3 data
- Use **Redshift Spectrum** when you need a broader warehouse analytics experience
- Use **QuickSight** when you want dashboards instead of raw query results

Together, these services demonstrate different ways to consume the same curated dataset.

### Learning Outcome

After this section, you should understand:

- What Amazon Athena does
- Why it integrates naturally with AWS Glue and Amazon S3
- How it supports ad-hoc analytics on the workshop dataset
- Why it is an important first tool in the business intelligence layer
