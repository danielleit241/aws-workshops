---
title: "Update data"
date: "2025-09-09"
weight: 6
chapter: false
pre: " <b> 2.6. </b> "
---

#### Target

One of the biggest advantages of RAG compared to Fine-tuning (retraining) a model is the ability to update data quickly. When a business has new regulations, you simply need to ingest them into the Knowledge Base, and the AI will "learn" them immediately.

In this section, we will simulate the following scenario:

1.  Ask the AI for a piece of non-existent information (The AI will answer that it doesn't know).
2.  Provide that information to the system by uploading a new file.
3.  Ask the same question again to witness the AI answer correctly immediately.

#### Implementation Steps

**Step 1: Verify the initial "lack of knowledge"**

We need to confirm that the current AI knows nothing about the confidential information we are about to create.

1.  Return to the **Streamlit Chatbot** interface (created in Part 5) or use the **Test Knowledge Base** window on the Console.
2.  Ask a question about hypothetical fake information.
    - _Example:_ _"What is the activation code for Project Omega?"_
3.  **Observe the result:** The AI will answer that it cannot find the information in the provided documents or will attempt a generic answer (if not restricted).

![Image illustrating AI not knowing about Project Omega](/images/Workshop/2.6-Update-Data/01.png)

**Step 2: Create new data**

We will create a text file containing this "secret" to ingest into the system.

1.  On your computer, open **Notepad** (Windows) or **TextEdit** (Mac).
2.  Copy and paste the following content into the file:
    ```text
    CONFIDENTIAL NOTICE:
    The secret Project Omega officially launches on 01/12/2025.
    The activation code is: "AWS-ROCKS-2025-SINGAPORE".
    The Project Manager is Mr. Robot.
    Please keep this information strictly confidential.
    ```
3.  Save the file as: `secret-project.txt`.

You can download the file here: <a href="/files/Workshop/secret-project.txt" download>TXT format file</a>

**Step 3: Upload and Sync**

Now, we will feed this new knowledge into the AI's "brain".

1.  Access the **S3 Console**, navigate to your old bucket (`rag-workshop-demo`).

2.  Click **Upload** -> **Add files** -> Select the `secret-project.txt` file -> **Upload**.

![Image illustrating file successfully uploaded to S3](/images/Workshop/2.6-Update-Data/02.png)

3.  Switch to the **Amazon Bedrock Console** -> Select **Knowledge bases** from the left menu.
4.  Click on your Knowledge Base name.
5.  Scroll down to the **Data source** section, select the data source (`s3-datasource`).
6.  Click the **Sync** button (Orange).
7.  **Wait:** Wait for about 30 seconds to 1 minute until the **Status** column changes from `Syncing` to `Available`.

![Image illustrating Sync process completion on Bedrock Console](/images/Workshop/2.6-Update-Data/03.png)

**Step 4: Verify again (The "Wow" Moment)**

The system now possesses the new knowledge. Let's challenge the AI once again.

1.  Return to the **Streamlit Chatbot** interface (No need to reload the page or restart the server).
2.  Ask the exact same question as before: _"What is the activation code for Project Omega?"_
3.  **Expected Result:**
    - The AI answers correctly: _"The activation code is AWS-ROCKS-2025-SINGAPORE"_.
    - The AI cites the source as the `secret-project.txt` file.

![Image illustrating AI answering correctly after data update](/images/Workshop/2.6-Update-Data/04.png)

#### Conclusion

You have just witnessed the true power of RAG!

- **No code editing required.**
- **No model retraining required.**
- **Simply Sync the data.**

Your Chatbot has become smarter and updated with the latest information in just a few simple steps. This is exactly why businesses choose this solution to build internal virtual assistants.
