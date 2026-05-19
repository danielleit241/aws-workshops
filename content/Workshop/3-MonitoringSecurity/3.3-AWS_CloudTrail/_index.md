---
title: "Track your system with AWS CloudTrail."
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

### AWS CloudTrail configuration steps

We will run a quick test to ensure your account is ready, then proceed with the AWS CloudTrail setup steps.

**Step 1: Access the AWS Console**

First, use the search bar to open the [AWS CloudTrail Console](https://console.aws.amazon.com/cloudtrailv2/home).

![3.3.1](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.1.svg)

Click **Create trail**.

{{% notice warning %}}
Choose **Create trail** -> not **Create a trail** (avoid confusing with Quick Create).
{{% /notice %}}

![3.3.2](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.2.svg)

**Step 2: Configure CloudTrail**

- **Trail name:** Enter `DataPipeline-Audit-Trail`.
- **Storage location:** Select **Create new S3 bucket**.
- **Trail log bucket and folder:** Enter `aws-workshop-audit-logs-glue`.
- **Log file SSE-KMS encryption:** Disable (do not enable).

![3.3.3](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.3.svg)

- Under **CloudWatch Logs**, check **Enabled** (this option sends logs to CloudWatch for easier querying).
- **Log group:** Leave the default name or set `DataPipeline/CloudTrail`.
- **IAM Role:** Choose **New** so AWS creates a role with write permissions for logs.
- Click **Next**.

![3.3.4](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.4.svg)

- Keep Management events logging enabled.
- Click **Next** again.

![3.3.5](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.5.svg)

- Click **Create trail**.

![3.3.6](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.6.svg)

- Verify the trail was created **Successfully** and that its **Status** shows **Logging**.

![3.3.7](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.7.svg)

**Congratulations — you have completed the AWS CloudTrail setup.**

