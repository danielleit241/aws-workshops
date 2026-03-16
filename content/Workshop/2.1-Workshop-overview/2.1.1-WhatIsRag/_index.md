---
title: "What is Retrieval-Augmented Generation (RAG)"
date: "2025-09-09"
weight: 1
chapter: false
pre: " <b> 2.1.1 </b> "
---

#### Brief Definition

**RAG (short for Retrieval-Augmented Generation)** is a technique or software architecture in the field of Artificial Intelligence (AI), designed to optimize the output of a Large Language Model (LLM).

In essence, RAG is a combination of two mechanisms:

- **Information Retrieval Mechanism**: Searching for data from a highly reliable External Knowledge Base.
- **Text Generation Mechanism**: Using the LLM's language understanding and synthesis capabilities to generate natural responses.

The goal of RAG is to provide the LLM with accurate, up-to-date, and specific context, helping the model overcome the limitations of static training data.

#### Why is RAG needed?

Traditional LLM models often face 3 major problems that RAG can solve:

- **Information Updates (Freshness)**: The LLM does not need Re-training or Fine-tuning yet can still answer the latest information, simply by updating the search database.
- **Data Ownership (Proprietary Data)**: Allows AI to answer questions regarding private enterprise data (internal documents, code base, customer information) that the original model does not know.
- **Authenticity (Grounding)**: Minimizes "Hallucination" (AI fabricating information) by forcing the AI to cite or rely on actual text passages found.

#### Operational Architecture

The process of handling a question in RAG proceeds as follows:

| Step  | Name                          | Action Description                                                                                                            |
| :---- | :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Retrieval** (Truy xuất)     | The system searches for text segments most relevant to the question in the data repository (usually using a Vector Database). |
| **2** | **Augmentation** (Tăng cường) | Combine the user's question + The data just found into a complete "prompt".                                                   |
| **3** | **Generation** (Tạo sinh)     | Send that prompt to the AI (LLM) for it to synthesize and write out the final answer for the user.                            |

![RAG](/images/Workshop/2.1-Workshop-overview/rag-initial-01.jpg)