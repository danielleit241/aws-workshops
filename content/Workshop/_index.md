---
title: "Data Pipeline with AWS Glue"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

## Overview 

In this workshop, we will build an automated data analytics pipeline on AWS for processing TLC Yellow Taxi trip records. The solution follows a serverless, event-driven architecture that starts with raw data in Amazon S3 and uses Amazon EventBridge, AWS Step Functions, AWS Lambda, and AWS Glue DataBrew to orchestrate ingestion, profiling, cleaning, validation, and transformation.

After the data is curated, it will be stored in a processed S3 layer and loaded into Amazon Redshift for OLAP workloads, while Amazon Athena will support fast ad-hoc SQL queries directly on S3. Finally, Amazon QuickSight will be used to build interactive dashboards for business insights, and IAM, CloudTrail, CloudWatch, and SNS will provide security, auditing, monitoring, and alerting throughout the workflow.

![Architecture](/images/Workshop/Architecture/Architecutre_final.png)

## Content

1. [Introduction](1-Introduction/)
2. [Preparation](2-Preparation/)
3. [Monitoring & Security](3-MonitoringSecurity/)
4. [Analytics Pipeline](4-AnalyticsPipeline/)
5. [Business Intelligence](5-BusinessIntelligence/)


