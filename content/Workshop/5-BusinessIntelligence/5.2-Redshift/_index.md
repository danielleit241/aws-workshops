---
title: "Redshift"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

In this section, we introduce **Amazon Redshift Spectrum** as the next analytical option after Athena for querying curated data in the data lake.

Amazon Redshift Spectrum extends **Amazon Redshift** so that SQL queries can access data stored directly in **Amazon S3**. In this workshop, Spectrum works together with the **AWS Glue Data Catalog**, allowing Redshift to understand external tables without requiring the dataset to be fully loaded into warehouse storage first.

### Why Redshift Spectrum Matters

Athena is excellent for quick, serverless exploration. However, many analytics teams also need a warehouse-oriented environment for broader SQL workflows, shared query tools, and integration with downstream BI platforms.

Redshift Spectrum helps bridge that gap by combining:

- **Warehouse-style SQL analysis**
- **Direct access to S3-based data lake files**
- **Metadata reuse from AWS Glue Data Catalog**
- **Integration with reporting and BI tools**

{{% notice info %}}
Redshift Spectrum does not replace the Glue pipeline. It consumes the processed outputs and catalog metadata created earlier in the workshop.
{{% /notice %}}

### How Redshift Spectrum Fits in This Workshop

The following diagram shows how Redshift Spectrum fits into the workshop architecture and query flow:

![Redshift Spectrum Workflow](/images/manhattan-dataways/redshift-spectrum/redshift_spectrum_workflow.png)

This means:

- **Amazon S3** remains the storage layer
- **AWS Glue Data Catalog** provides schema and table metadata
- **Redshift Spectrum** queries the external data through Redshift SQL interfaces

### What You Will Do in This Section

In the hands-on steps that follow, you will:

1. Review the core concepts behind Redshift Spectrum
2. Set up **Amazon Redshift Serverless**
3. Connect to **Query Editor v2**
4. Create an **external schema** linked to the Glue Data Catalog
5. Query the Glue-managed external tables from Redshift
6. Review common mistakes, cost considerations, and cleanup guidance

### Benefits of Using Redshift Spectrum

| Benefit | Explanation |
|---|---|
| External Querying | Query S3 data without fully loading it into Redshift tables |
| Glue Integration | Reuse discovered schema from the Data Catalog |
| Familiar SQL Experience | Use Redshift query tools and warehouse-style workflows |
| Scalable Analytics | Support larger analytical workloads across curated datasets |
| BI Readiness | Prepare data access patterns that connect naturally to reporting tools |

### Redshift Spectrum and Athena

Athena and Redshift Spectrum both query data in Amazon S3, but they are usually used in different situations:

- Use **Athena** for lightweight, direct, ad-hoc SQL analysis
- Use **Redshift Spectrum** when you want a more warehouse-oriented analytics workflow
- Use **QuickSight** when you want dashboards and visual storytelling from analytical results

Together, they show how the same curated dataset can support multiple consumption patterns.

### Learning Outcome

After completing this section, you should understand:

- What Amazon Redshift Spectrum is
- How it integrates with Amazon S3 and AWS Glue Data Catalog
- Why it complements Athena in the BI layer
- How Redshift Serverless can be used to query curated data lake outputs
