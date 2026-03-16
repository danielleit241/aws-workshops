---
title: "Services"
date: "2025-09-09"
weight: 2
chapter: false
pre: " <b> 2.1.2 </b> "
---

The solution architecture is built upon the coordination of the following 4 key service components:

#### Knowledge Bases for Amazon Bedrock

This is a fully managed capability that helps connect Foundation Models to the enterprise's internal data sources.

- **RAG workflow automation:** Manages the entire end-to-end workflow, including ingestion, chunking, embedding, and retrieval.
- **Contextual connection:** Enables AI applications to answer questions based on private data rather than relying solely on generic training data.
- **No infrastructure management:** Eliminates the need to build and maintain complex data pipelines.

#### Amazon Simple Storage Service (Amazon S3)

An object storage service with scalability, 99.999999999% (11 nines) data durability, and top-tier security.

- **Data Source Role:** Acts as the "source of truth".
- **Document storage:** Contains unstructured files such as PDF, Word, or Text that the business wants the AI to learn.
- **Synchronization:** The Knowledge Base will periodically scan this S3 bucket to synchronize and update the latest knowledge.

#### Amazon OpenSearch Serverless

A serverless deployment option for Amazon OpenSearch Service that helps run search and analytics workloads without managing clusters.

- **Vector Store Role:** Stores vector embeddings generated from original documents.
- **Semantic Search:** Performs similarity search algorithms (k-NN) to identify text segments with meanings closest to the user's question.
- **Auto-scaling:** Automatically adjusts compute and storage resources based on actual demand.

#### Amazon Bedrock Foundation Models (FMs)

Provides access to leading AI models via a unified API. In this architecture, we use two types of models with distinct roles:

- **Embedding Model (Amazon Titan Embeddings v2):**
  - Converts text (documents from S3 and user questions) into numerical vectors.
  - Enables computers to compare semantic similarity between text segments.
- **Text Generation Model (Anthropic Claude 3):**
  - Acts as the reasoning "brain".
  - Receives the question along with contextual information retrieved from the Vector Store.
  - Synthesizes information and generates natural, accurate answers with source citations.