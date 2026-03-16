---
title: "Workshop"
date: "2025-09-09"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Building a RAG Application using Knowledge Bases for Amazon Bedrock

#### Overview

**Knowledge Bases for Amazon Bedrock** is a fully managed feature that helps you implement RAG (Retrieval-Augmented Generation) techniques by connecting Foundation Models to your internal data sources to deliver accurate, cited, and contextually relevant responses.

> RAG is a technique to optimize Large Language Model (LLM) output by retrieving information from a trusted external database (Retrieval) and adding it to the context (Augmentation) before generating the answer (Generation). This method helps overcome limitations regarding outdated training data and ensures the AI answers based on the actual provided information.

In this lab, we will learn how to build an AI assistant capable of "reading and understanding" proprietary enterprise documents. You will perform the process from data ingestion and creating vector indexes to configuring the model to answer questions based on those documents without managing any servers.

We will use three main components to set up a complete RAG processing workflow:

- **Data Source (Amazon S3)** - Acts as the repository of "truth". You will upload documents (PDF, Word, Text) to an S3 bucket. The Knowledge Base will use this source to synchronize data.
- **Vector Store (OpenSearch Serverless)** - The place to store vector embeddings (numerically encoded data). When a user asks a question, the system will perform a semantic search here to extract the most relevant text segments instead of standard keyword searching.
- **Foundation Model (Claude 3)** - The Large Language Model acting as the processing brain. It receives the user's question along with information found from the Vector Store, then synthesizes and generates a natural, accurate answer accompanied by source citations.

#### Outcomes

By the end of the workshop, you will have a practical, functioning Chatbot system with the following features:

- Q&A chat regarding proprietary document content.
- Accurate answers, no hallucinations.
- Source citations (knowing exactly which page the answer comes from).
- Rapid deployment without writing complex data processing code.

#### Contents

1. [Workshop Overview](2.1-Workshop-overview/)
2. [Environment Preparation](2.2-Prerequiste/)
3. [Create and Configure Knowledge Base](2.3-Knowledge-Base/)
4. [Test Chatbot (RAG)](2.4-Test-Chatbox/)
5. [Client Application Integration (Optional)](2.5-Client-Integration/)
6. [Update Data](2.6-Update-Data/)
7. [Clean Up Resources](2.7-Cleanup/)