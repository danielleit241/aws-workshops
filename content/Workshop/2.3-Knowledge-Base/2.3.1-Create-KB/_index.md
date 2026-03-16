---
title: "Initialize Knowledge Base"
date: "2025-09-09"
weight: 1
chapter: false
pre: " <b> 2.3.1 </b> "
---

#### Target

We will use the Amazon Bedrock Wizard to set up the entire RAG architecture. This process will connect the S3 data source, the Embedding model, and automatically initialize the Vector storage (OpenSearch Serverless).

#### Implementation Steps

1.  Log in to the **AWS Management Console** and access the **Amazon Bedrock** service.
2.  In the left-hand menu, select **Knowledge bases**.

![Click_Knowledge_base](/images/Workshop/2.3-Knowledge-Base/01_Click_Knowledge_base.jpg)

3.  Click the **Create knowledge base** button in the top right corner of the screen.

![Create Knowledge Base](/images/Workshop/2.3-Knowledge-Base/02_Create_Knowledge_base.jpg)

**Step 1: Configure Knowledge Base**

On the first configuration screen:

1. **Knowledge base name:** Enter `knowledge-base-demo`
2. **Knowledge Base description - optional:** Enter `Knowledge Base from AWS Overview` (This section requires you to describe the data you have previously uploaded to S3).
3. **IAM permissions:** Select the option **Create and use a new service role**.
4. **Service role name:** Keep the default value suggested by AWS (starting with `AmazonBedrockExecutionRoleForKnowledgeBase_...`).

![Configure Knowledge Base](/images/Workshop/2.3-Knowledge-Base/03_Configure_KB.jpg)

5.  Click **Next**.

![Configure Knowledge Base_02](/images/Workshop/2.3-Knowledge-Base/04_Configure_KB_2.jpg)

**Step 2: Configure Data Source**

Connect to the S3 Bucket containing the documents:

1.  **Data source name:** Enter`knowledge-base-demo`
![Configure KB Step 2](/images/Workshop/2.3-Knowledge-Base/05_Step_2.jpg)

2.  **S3 URI:**
    - Click the **Browse S3** button.
    - In the pop-up window, select the bucket `rag-workshop-demo` you created in the previous section.
    - Click **Choose**.
![Configure S3 URI](/images/Workshop/2.3-Knowledge-Base/06_Configure_S3_URI.jpg)

3. Keep Default configurations. Click **Next**.

![Finished Step 2](/images/Workshop/2.3-Knowledge-Base/07_Finished_Step_2.jpg)

**Step 3: Storage & Processing**

This is the most critical step to define the AI model and vector storage location:

1.  **Embeddings model:**
    - Click **Select model**.
    ![Configure Step 3](/images/Workshop/2.3-Knowledge-Base/08_Config_Step_3.jpg)

    - Select model: **Titan Embeddings G1 - Text v2**.
    ![Configure Step 3](/images/Workshop/2.3-Knowledge-Base/09_Config_Step_3.jpg)

2.  **Vector Store:**
    - **Vector store creation method:** Choose `Quick create a new vector store - Recommended`
    - **Vector store type - new:** Choose `Amazon OpenSearch Serverless`
    - _Note:_ This option allows AWS to automatically create an **Amazon OpenSearch Serverless** cluster to store data, saving you from manual infrastructure management.
3.  Click **Next**.
![Configure Step 3](/images/Workshop/2.3-Knowledge-Base/10_Config_Step_3.jpg)

**Step 4: Review and Create Knowledge Base**

1.  Review all configuration information on the Review page.
2.  Ensure the S3 URI and Model items are correct.
3.  Scroll to the bottom of the page and click the **Create knowledge base** button.

![Step 4](/images/Workshop/2.3-Knowledge-Base/11_Step_4.jpg)

**Step 5: Wait for Initialization**

After clicking Create, the system will begin the background infrastructure initialization process for the Vector Store.

- **Wait time:** Approximately **2 - 5 minutes**.
- **Note:** Please do not close the browser during this time.
- **Success:** When the screen displays a green notification **"Knowledge base created successfully"**, you have completed this step and are ready for the next section.

![Step 5](/images/Workshop/2.3-Knowledge-Base/12_Step_5.jpg)
