---
title: "Create IAM Role for AWS Glue"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
### AWS IAM configuration steps for Glue

In this section, we create the IAM service role that AWS Glue uses to run both the crawler and the ETL job in this workshop.

This role allows Glue to:

- read raw input data from Amazon S3
- write processed output data back to Amazon S3
- create logs in Amazon CloudWatch Logs
- access the AWS Glue Data Catalog during crawler and job execution

We will create one reusable role for the workshop:

- **Role name:** `glue-role-manhattan-workshop`

{{% notice info %}}
This page focuses only on the **Glue service role** used by the crawler and ETL job.
It is different from the IAM role later attached to Amazon Redshift Serverless.
{{% /notice %}}

**Step 1: Open the IAM Console**

From the AWS Management Console search bar, open **IAM**.

Then choose **Roles** from the left navigation pane and click **Create role**.

**Step 2: Choose AWS Service as the Trusted Entity**

In the trusted entity step:

- **Trusted entity type:** `AWS service`
- **Service or use case:** `Glue`

This trust relationship allows AWS Glue to assume the role at runtime.

Click **Next**.

**Step 3: Attach the Base Glue Managed Policy**

Search for and attach the managed policy:

- `AWSGlueServiceRole`

This policy provides the baseline permissions Glue needs to run crawlers, jobs, and related service operations.

Click **Next** after selecting the policy.

**Step 4: Add S3 Access for Workshop Data**

Glue also needs access to the S3 buckets used in this workshop.

For a workshop environment, the easiest approach is to attach one of these options:

- **Option A Simple workshop setup:** `AmazonS3FullAccess`
- **Option B Safer setup:** a custom policy limited to only your workshop buckets

If you want the fast workshop path, attach:

- `AmazonS3FullAccess`

If your AWS account requires a narrower policy, create a customer-managed policy similar to this example and attach it to the same role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-raw-bucket",
        "arn:aws:s3:::your-processed-bucket",
        "arn:aws:s3:::your-script-bucket"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::your-raw-bucket/*",
        "arn:aws:s3:::your-processed-bucket/*",
        "arn:aws:s3:::your-script-bucket/*"
      ]
    }
  ]
}
```

For this workshop, the role should be able to access:

- the **raw data** location
- the **processed data** location
- the **ETL script** location if your Glue job script is stored in S3
- the **temporary directory** used by Glue job execution

**Step 5: Review and Name the Role**

On the final review screen:

- **Role name:** `glue-role-manhattan-workshop`

Optionally add a description such as:

`Service role for AWS Glue crawler and ETL job in the Manhattan DataWay workshop`

Then click **Create role**.

**Step 6: Verify the Trust Relationship**

Open the newly created role and confirm that the trust relationship allows Glue to assume it.

It should reference:

- `glue.amazonaws.com`

If you open the **Trust relationships** tab, the document should look similar to:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Step 7: Use the Role in AWS Glue**

Later in this workshop, reuse this role in:

- **AWS Glue Crawler** to scan datasets in S3 and update the Data Catalog
- **AWS Glue ETL Job** to read raw data, transform it, and write processed output

When creating those resources, select:

- `glue-role-manhattan-workshop`

**Step 8: Quick Validation Checklist**

Before continuing, verify that:

- the role exists in IAM
- the trusted service is **AWS Glue**
- `AWSGlueServiceRole` is attached
- S3 permissions are attached for your workshop buckets
- you can select this role from the Glue Crawler and Glue Job configuration screens

{{% notice tip %}}
If Glue fails later with **AccessDenied**, the cause is usually missing S3 permissions on the role rather than a Glue configuration error.
{{% /notice %}}

### Summary

In this section, you created the IAM service role required by AWS Glue.

This role will be reused by the next workshop components so Glue can:

- crawl schema from S3 data
- run ETL transformations
- write logs to CloudWatch
- interact with the Glue Data Catalog
