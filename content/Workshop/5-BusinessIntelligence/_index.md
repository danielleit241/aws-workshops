---
title: "Business Intelligence"
date: "2026-05-02"
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

In this chapter, we move from **data preparation** to **data consumption**. After the dataset has been discovered, cataloged, and transformed with AWS Glue, we are ready to query it and turn it into business insights.

The purpose of this chapter is to show how the processed data can be accessed through different analytics services, depending on the use case:

- **Amazon Athena** for fast, serverless SQL queries directly on data stored in Amazon S3
- **Amazon Redshift Spectrum** for warehouse-style analytics that still leverages the data lake
- **Amazon QuickSight** for dashboards and visual reporting

{{% notice info %}}
This chapter focuses on the consumption layer of the platform. The data engineering steps that prepare the dataset were completed in the previous Analytics Pipeline chapter.
{{% /notice %}}

### Where This Chapter Fits in the Workshop

The workshop now follows this end-to-end flow:

![Business Intelligence Flow](/images/Workshop/5-BusinessIntelligence/business_intelligence_flow.png)

At this stage:

- The **raw taxi trip dataset** has already been stored in Amazon S3.
- **AWS Glue Crawler** has discovered the schema.
- **AWS Glue Data Catalog** has registered the metadata.
- **AWS Glue ETL** has cleaned and transformed the dataset into an analytics-ready format.
- The BI layer can now query and visualize the result.

### Why Business Intelligence Matters

Building a pipeline is only part of the solution. The real value appears when users can explore the data, answer questions, and make decisions from it.

In a business intelligence layer, we typically need to:

- Query data without building a custom application
- Compare trends, totals, and categories
- Investigate anomalies or unexpected values
- Share results through dashboards and reports
- Support both ad-hoc analysis and repeatable reporting

This is why the workshop introduces multiple services instead of only one query engine.

{{% notice tip %}}
Think of this chapter as the point where engineered data becomes usable business information.
{{% /notice %}}

### Core Services in This Chapter

| Service | Main Role |
|---|---|
| Amazon Athena | Query S3 data directly using standard SQL |
| Amazon Redshift Spectrum | Extend warehouse analytics to data stored in S3 |
| Amazon QuickSight | Build dashboards and visual analytics from query results |

### What You Will Learn

By completing this chapter, you will understand:

- When to use **Athena** for lightweight, serverless analysis
- Why **Redshift Spectrum** is useful for larger-scale analytical workflows
- How **QuickSight** connects to analytical datasets for visualization
- How the BI layer depends on the metadata and processed outputs created earlier in the workshop

### Chapter Content

1. [Athena](5.1-Athena/)
2. [Redshift](5.2-Redshift/)
3. [QuickSight](5.3-Quickshight/)

By the end of this chapter, you will have a complete view of how data flows from ingestion and transformation into querying, exploration, and dashboard-driven insight.
