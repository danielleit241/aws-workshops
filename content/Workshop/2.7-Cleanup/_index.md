---
title: "Clean Resources"
date: "2025-09-09"
weight: 7
chapter: false
pre: " <b> 2.7. </b> "
---

#### Target

To avoid incurring unwanted costs after finishing the practice lab, we need to delete the created resources.

> ⚠️ **WARNING:**
> Deleting the **Knowledge Base** DOES NOT automatically delete the **Vector Store (OpenSearch Serverless)**. You must manually delete the OpenSearch Serverless Collection as this is the costliest service in this Lab.

#### Implementation Steps

**Step 1: Delete Knowledge Base**

1.  Access the **Amazon Bedrock Console** -> **Knowledge bases**.
2.  Select the radio button next to your Knowledge Base name.

3.  Click the **Delete** button.
4.  A dialog box appears, enter the Knowledge Base name to confirm (or type `delete`).
5.  Click **Delete**. This process takes 10-15 minutes to complete successfully, so please be patient.

![Image illustrating Knowledge Base deletion action](/images/Workshop/2.7-Clean-up/01.jpg)

**Step 2: Delete Vector Store**

1.  Access the **Amazon OpenSearch Service**.
2.  In the left menu, under **Serverless**, select **Collections**.
3.  You will see a Collection named like `bedrock-knowledge-base-...`.
4.  Select the radio button next to that Collection name.
5.  Click the **Delete** button.
6.  Type `confirm` or the collection name to confirm deletion.
7.  Click **Delete**.

![Image illustrating OpenSearch Collection deletion action](/images/Workshop/2.7-Clean-up/02.jpg)

**Step 3: Delete Data on S3**

1.  Access the **Amazon S3** service.
2.  Select the bucket `rag-workshop-demo`.
3.  Click the **Empty** button first.
    - Type `permanently delete` to confirm deleting all files inside.
4.  After the bucket is empty, return to the Buckets list.
5.  Select that bucket again and click the **Delete** button.
6.  Enter the bucket name to confirm.

![Image illustrating S3 Bucket Empty and Delete actions](/images/Workshop/2.7-Clean-up/03.jpg)

#### Completion

Congratulations on fully completing the Workshop **"Building a RAG Application with Amazon Bedrock"**. Your system has been cleaned up and is safe!
