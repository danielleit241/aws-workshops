---
title: "Preparation"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

### Overview

In this section, we will set up all the necessary AWS resources before starting the main workshop. This includes creating an S3 bucket to store the raw dataset, uploading the TLC Yellow Taxi trip data, and verifying that the required permissions are in place.

After completing this section, you will be able to:

- Create an Amazon S3 bucket to store the raw dataset
- Upload the TLC Yellow Taxi trip data in Parquet format
- Verify the uploaded files in the S3 console
- Confirm that your AWS account has the necessary permissions to proceed


### Prerequisites

Before starting, make sure you have the following:

- An active **AWS account** with sufficient permissions to create S3 buckets and IAM roles
- The **AWS Management Console** accessible in your browser
- The **TLC Yellow Taxi trip dataset** in Parquet format, ready to upload

{{% notice info %}}
If you do not have the dataset, you can download a sample from the [TLC Trip Record Data page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).  
For this workshop, we recommend using a single month of Yellow Taxi trip data in Parquet format.
{{% /notice %}}

### Configuration

In this workshop, we will use the following sample configuration.

| Resource        | Value                             |
| --------------- | --------------------------------- |
| S3 Bucket Name  | `yellow-taxi-trip-demo-fcaj`      |
| AWS Region      | `us-east-1` (Ohio)      |
| Dataset Format  | Parquet                           |
| Folder Path     | `/` (bucket root)                 |

You can adjust the bucket name and region based on your own AWS environment.

---

**Step 1: Sign in to the AWS Management Console**

1. Open your browser and go to [https://console.aws.amazon.com](https://console.aws.amazon.com)
2. Sign in with your AWS account credentials
3. In the top-right corner, confirm that you are in the correct **AWS Region** (e.g., `us-east-2`)

{{% notice tip %}}
You can change the region by clicking the region name in the top-right corner of the console and selecting the desired region from the dropdown.
{{% /notice %}}

---

**Step 2: Create an Amazon S3 Bucket**

1. In the AWS Management Console, search for **S3** in the search bar and open the S3 service
2. Click **Create bucket**
3. Under **Bucket name**, enter a unique name for your bucket (e.g., `yellow-taxi-trip-demo-fcaj`)

{{% notice info %}}
S3 bucket names must be globally unique across all AWS accounts. If the name is already taken, try adding a suffix such as your initials or a random number.
{{% /notice %}}

4. Under **AWS Region**, select the region you are using for this workshop (e.g., `us-east-2`)
5. Leave all other settings as default
6. Scroll down and click **Create bucket**

After the bucket is created, it will appear in your S3 bucket list.

---

**Step 3: Upload the Dataset to S3**

1. Click on the bucket name you just created to open it
2. Click **Upload**
3. Click **Add files** and select the Parquet file(s) from your local machine

{{% notice tip %}}
If your dataset is split into multiple Parquet files inside a folder, you can click **Add folder** to upload the entire folder at once. AWS Glue Crawler can scan all files within a folder path.
{{% /notice %}}

4. Review the list of files to be uploaded
5. Leave all other settings as default
6. Click **Upload** to start the upload process
7. Wait for the upload to complete. The status will show **Succeeded** when done.

---

**Step 4: Verify the Uploaded Files**

1. After the upload completes, return to the bucket view
2. Confirm that the Parquet file(s) appear in the bucket

You should see the uploaded files listed with their file size and last modified date.

{{% notice info %}}
If you uploaded a folder, click into the folder to confirm the Parquet files are present inside.  
The S3 path will look something like: `s3://yellow-taxi-trip-demo-fcaj/yellow_tripdata_2024-01.parquet`
{{% /notice %}}

---

**Step 5: Verify Account Permissions**

Before proceeding to the next section, confirm that your AWS account has the permissions needed for this workshop.

At a minimum, your account should have access to:

- **Amazon S3** — to read and write data
- **AWS Glue** — to create crawlers, databases, and ETL jobs
- **AWS IAM** — to create and attach roles and policies
- **Amazon Athena** — to run SQL queries on S3 data
- **Amazon CloudWatch** — to view logs from Glue jobs

{{% notice tip %}}
If you are using an IAM user or role with limited permissions, ask your AWS administrator to attach the `AdministratorAccess` policy for the duration of this workshop, or ensure the specific service permissions listed above are granted.
{{% /notice %}}

---

### Summary

In this section, we prepared the AWS environment for the workshop.

| Step | Action                                                    |
| ---- | --------------------------------------------------------- |
| 1    | Signed in to the AWS Management Console                   |
| 2    | Created an Amazon S3 bucket                               |
| 3    | Uploaded the TLC Yellow Taxi dataset in Parquet format    |
| 4    | Verified the uploaded files in the S3 console             |
| 5    | Confirmed the required account permissions                |

The raw dataset is now stored in Amazon S3 and ready to be processed. In the next section, we will set up **Monitoring and Security** resources before building the analytics pipeline.
