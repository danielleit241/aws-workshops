---
title: "Monitoring & Security"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

### Objectives

In the Data Pipeline architecture, the movement of data from ***Source (S3) -> Processing (Glue ETL) -> Analysis (Athena/Redshift)*** requires robust security and monitoring mechanisms. The objectives of this section aim to help learners:

1. **Access Control Management (AWS IAM):** Ensure the principle of least privilege. Precisely allocate the necessary Roles so that AWS Glue and Redshift can securely communicate with the S3 Data Lake.

2. **Auditing and Logging (AWS CloudTrail):** Track and record all operations (API Calls) that interact with the system, enabling quick tracing when misconfigurations or unauthorized access occur.

3. **Pipeline Status Monitoring (Amazon CloudWatch / EventBridge):** Capture the system status in real-time. Catch important event streams such as when a data processing job completes or fails.

4. **Automated Alerting (Amazon SNS):** Automate the distribution of notifications (via Email/SMS) to the Data Engineering/Admin team immediately when the Data Pipeline encounters an issue.

### Security & Monitoring Workflow

1. [Set up an Alert System with Amazon SNS](/workshop/3-monitoringsecurity/3.1-aws_sns/)
2. [Create IAM Role for AWS Glue](/workshop/3-monitoringsecurity/3.2-AWS_IAM)
3. [Track your system with AWS CloudTrail](3.3-AWS_CloudTrail/) 
4. [Set up Data Pipeline Error Alerts with Amazon EventBridge (CloudWatch)](/workshop/3-monitoringsecurity/3.4-AWS_EventBridge_(CloudWatch))
