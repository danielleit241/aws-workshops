---
title: "Prepare source data"
date: "2025-09-09"
weight: 2
chapter: false
pre: " <b> 2.2.2 </b> "
---

#### Overview

Initialize an object storage (S3 Bucket) to hold original documents (PDF, Word, Text). This acts as the "Source of Truth" that the Knowledge Base will access to read, analyze, and synchronize knowledge for the AI. You can store knowledge related to your field to use in creating your own personal assistant or Chatbot.

#### Data Preparation

We will create an S3 Bucket to store original documents, acting as the knowledge source for the Chatbot.

**Step 1. Create S3 Bucket**

- Access the [S3](https://us-east-1.console.aws.amazon.com/s3/get-started?region=us-east-1) service from the search bar.
- **AWS Region:** Select `United States (N. Virginia us-east-1)`.

![Access S3](/images/Workshop/2.2-Prerequisite/04_S3.jpg)

- Click **Create bucket**.

![Create S3 Bucket](/images/Workshop/2.2-Prerequisite/05_S3_Create_Bucket.jpg)

- Configure Bucket information:
    - **Bucket Type:** Click `General purpose`
    - **Bucket name:** Enter `rag-workshop-demo`
    - **Object Ownership:** Keep default `ACLs disabled`.
    - **Block Public Access settings:** Keep default (Selected `Block all public access`).

![Configure S3 Bucket](/images/Workshop/2.2-Prerequisite/06_Configure_S3_Bucket.jpg)

- Scroll to the bottom of the page, Click **Create bucket**.

![Image illustrating S3 Bucket creation interface and Region selection](/images/Workshop/2.2-Prerequisite/07_Finished_Create_bucket.jpg)

- Check that the S3 Bucket has been created successfully.

![Create S3 Bucket Successful](/images/Workshop/2.2-Prerequisite/08_Create_S3_Successful.jpg)


**Step 2. Upload sample documents**

- This is a sample document, relevant to overview of AWS cloud computing knowledge. You can use it to run demos or upload your data.

<a href="/files/2-Workshop/aws-overview.pdf" download>PDF format file</a>

- In the Buckets list, Click on the **bucket name** you just created.
![Click_S3_Bucket](/images/Workshop/2.2-Prerequisite/09_Click_S3_Bucket.jpg)

- Click **Upload**.
![Upload_file_to_Bucket](/images/Workshop/2.2-Prerequisite/10_Upload_file_to_Bucket.jpg)

- In the Upload interface:
    - Click **Add files**.
    - Select the sample document file attached above or a file from your computer (PDF or Word file with a lot of text is recommended).
- Scroll to the bottom of the page, Click **Upload**.

![Upload_file_to_Bucket_02](/images/Workshop/2.2-Prerequisite/11_Click_to_Uploadfile.jpg)

- When you see the green "Upload succeeded" notification, Click **Close**.

![Upload file successfully](/images/Workshop/2.2-Prerequisite/12_Successfully.jpg)