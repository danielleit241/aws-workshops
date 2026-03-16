---
title: "Create and Configure Knowledge Base"
date: "2025-09-09"
weight: 3
chapter: false
pre: " <b> 2.3. </b> "
---

#### Objectives

After completing the environment and data preparation, the next step is to set up the core component of the RAG architecture. In this section, we will initialize the **Knowledge Base**, acting as an intelligent intermediary mechanism that connects unstructured data sources with the reasoning capabilities of foundation models.

We will accomplish 3 key technical objectives:

1.  **Establish an Automated Pipeline:** Configure the Knowledge Base to automate the entire RAG data processing workflow (including extraction, text chunking, and vector creation) to eliminate manual processing tasks.
2.  **Initialize Vector Store:** Deploy a collection on **Amazon OpenSearch Serverless** to store semantic vectors, serving accurate and efficient information retrieval.
3.  **Data Synchronization (Data Ingestion):** Perform the initial data ingestion process, converting static documents from S3 into searchable vectors within the system.

#### Key Components

During this configuration process, we will interact with and connect the following services:

- **Knowledge Bases for Amazon Bedrock:** A managed service acting as the orchestrator of data flow, connecting information sources, and executing semantic queries.
- **Amazon Titan Embeddings G1 - Text v2:** A specialized model for converting text data into numerical vectors (Embeddings) with high accuracy and multi-language support.
- **Amazon OpenSearch Serverless:** A fully managed vector database responsible for storage and executing similarity search algorithms (k-NN).

#### Implementation Steps

1. [Initialize Knowledge Base](2.3.1-Create-KB/)
2. [Check Vector Store and Sync Data](2.3.2-Sync-Data/)