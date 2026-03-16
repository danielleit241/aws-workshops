---
title: "Prerequiste"
date: "2025-09-09"
weight: 2
chapter: false
pre: " <b> 2.2. </b> "
---

#### Objectives

Before building the application, we need to establish a solid foundation. Similar to preparing ingredients before cooking, this section ensures your AWS account is ready with the necessary permissions and data.

In this section, we will complete 3 key initialization objectives:

1.  **Select Region:** Set up the working environment in the **United States N. Virginia (us-east-1)** region to optimize connection speed and ensure service availability.
2.  **Enable Model (Model Access):** Check and ensure the account has permission to invoke the **Anthropic Claude 3** model – the main linguistic "brain" of the system.
3.  **Prepare Data (Data Setup):** Initialize storage (S3 Bucket) and upload source documents to serve the knowledge ingestion process later.

#### Key Components

In this preparation section, we will interact with the following components:

- **AWS Management Console (Region Selector):** The general management interface to switch the working Region to United States N. Virginia.
- **Amazon Bedrock (Model Access & Playground):** The place to manage access to Foundation Models and the chat tool to quickly test AI response capabilities.
- **Amazon S3 (Simple Storage Service):** Object storage service where we will create a Bucket to hold original document files (PDF, Word, Text).

#### Implementation Steps

1.  [Check Model Access](2.2.1-Model-Access/)
2.  [Prepare Source Data](2.2.2-Prepare-Data/)