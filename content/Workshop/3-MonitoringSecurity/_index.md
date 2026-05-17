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

1. [Set up an Alert System with Amazon SNS](/content/Workshop/3-MonitoringSecurity/3.1-AWS_SNS/_index.md)

- Initialize an SNS Topic that serves as the notification hub for receiving and distributing messages.

2. [Create IAM Role for AWS Glue](/content/Workshop/3-MonitoringSecurity/3.2-AWS_IAM/_index.md)
- Set up an IAM Role to grant permissions for the AWS Glue service to retrieve data, process it, and write logs.

3. [Track your system with AWS CloudTrail](/content/Workshop/3-MonitoringSecurity/3.3-AWS_CloudTrail/_index.md) 

- Enable CloudTrail to begin the audit process for the entire project.

4. [Set up Data Pipeline Error Alerts with Amazon EventBridge (CloudWatch)](/content/Workshop/3-MonitoringSecurity/3.4-AWS_EventBridge_(CloudWatch)/_index.md)

- Set up EventBridge (CloudWatch) rules to monitor the status of Glue Jobs. If a Job reports a failure (FAILED), a signal is immediately sent to SNS to dispatch an alert email.

