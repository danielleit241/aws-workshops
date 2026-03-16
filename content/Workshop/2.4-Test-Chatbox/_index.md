---
title: "Testing Chatbot (RAG)"
date: "2025-09-09"
weight: 4
chapter: false
pre: " <b> 2.4. </b> "
---

#### Target

After successfully ingesting data into the Vector Store, it is time to verify the results. In this section, you will act as an end-user, asking the Chatbot questions directly within the AWS Console interface to observe how the RAG system operates.

We will focus on 2 factors:

1.  **Accuracy:** Does the AI answer correctly based on the documents?
2.  **Transparency:** Can the AI cite the source (Citation) of the information?

#### Implementation Steps

**Step 1: Configure the test window**

To start chatting, we need to select a Foundation Model that will act as the "responder".

1.  In your Knowledge Base details interface, look at the right panel titled **Test knowledge base**.
![Open KB](/images/Workshop/2.4-Test-Chatbox/01_Test_KB.jpg)

2.  Click the **Select model** button.

![Select Model](/images/Workshop/2.4-Test-Chatbox/02_Select_Model.jpg)

3.  In the selection panel that appears:
    - **Category:** Select `Anthropic`.
    - **Model:** Select `Claude 3 Sonnet` (or _Claude 3.5 Sonnet_ / _Haiku_ depending on the model you enabled).
    - **Throughput:** Keep `On-demand`.
4.  Click **Apply**.

![Image illustrating Claude 3 Model selection configuration panel](/images/Workshop/2.4-Test-Chatbox/03_Test_KB.jpg)

**Step 2: Conduct conversation (Chat)**

Now, try asking a question related to the document content you uploaded.

1.  In the input box (Message input), type your question.
    - _Example:_ If you uploaded the "AWS Overview" document, ask: _"Can you explain to me what EC2 is?"_.
2.  Click **Run**.
3.  **Observe the result:**
    - The AI will think for a few seconds (querying the Vector Store).
    - Then, it will answer in natural language, summarizing the found information.

![Image illustrating AI question and answer in chat interface](/images/Workshop/2.4-Test-Chatbox/04_Promt_test_01.jpg)

**Step 3: Verify data source**

This is the most important feature of RAG that distinguishes it from standard ChatGPT: the ability to prove the source of information.

1.  In the AI's response, pay attention to the small numbers (footnotes) or the text **Show source details**.
2.  Click on those numbers or the details button.
3.  A **Source details** window will appear, displaying:
    - **Source chunk:** The exact original text segment that the AI found in the document.
    - **Score:** Similarity score (relevance).
    - **S3 Location:** Path to the original file.

![Image illustrating Source Details window showing original text segment](/images/Workshop/2.4-Test-Chatbox/05_Promt_test_01.jpg)

_Seeing this original text segment proves that the AI is not "hallucinating" but is actually reading your documents._

**Step 4: Test with irrelevant questions (Optional)**

To see how the system reacts when information is not found.

1.  Ask a question completely unrelated to the documents.
    - _Example:_ _"Can you explain some knowledge about personal finance?"_ (While your documents are about Cloud Computing).
2.  **Expected Result:**
    - The AI might answer based on its general knowledge (if not restricted).
    - OR the AI will answer _"Sorry, I am unable to answer your question based on the retrieved data"_ - This is the ideal behavior for an enterprise RAG application.

![Image illustrating response when asking off-topic questions](/images/Workshop/2.4-Test-Chatbox/06_Promt_test_01.jpg)
