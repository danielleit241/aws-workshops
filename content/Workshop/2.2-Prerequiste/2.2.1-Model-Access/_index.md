---
title: "Verify Model Access"
date: "2025-09-09"
weight: 1
chapter: false
pre: " <b> 2.2.1 </b> "
---

#### Overview

According to AWS's new policy, Foundation Models are often automatically enabled. However, for third-party partner models like **Anthropic (Claude)**, first-time users in a new Region must declare usage information (Use Case) to be able to invoke the model.

Ensure your AWS account has permission to access and use the **Anthropic Claude 3 Sonnet** model. This is a mandatory step to avoid `AccessDenied` errors when the Chatbot operates later. If this is the first time you are using this model in a new Region, you need to declare the intended use (Use Case).

#### Access Check

We will perform a quick test (Test Run) to ensure your account is ready.

In the search bar, access the [Amazon Bedrock](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/overview).

![Access Amazon Bedrock](/images/Workshop/2.2-Prerequisite/00_Amazon_Bedrock.jpg)

**Step 1. Access Chat Playground**

- In the left menu of the Bedrock Console, find **Playgrounds**.
- Click **Chat**.

![Image illustrating Playgrounds menu on the left](/images/Workshop/2.2-Prerequisite/01_Play_ground.jpg)

**Step 2. Select Test Model**

- Click **Select model** (above the chat box).
- Category: Select **Anthropic**.
- Model: Select **Claude 3 Sonnet** (or Claude 3.5 Sonnet).
- Throughput: Select **On-demand**.
- Click **Apply**.

![Image illustrating Claude 3 Model selection panel](/images/Workshop/2.2-Prerequisite/02_Select_Test_Model.jpg)

**Step 3. Send Activation Message**

- In the chat box: Enter `Hello`.
- Click **Run**.
- **Observe result:**
  - If AI answers: **Success** (Proceed immediately to section 2.2.2).
  - If a red error or "Submit use case details" popup appears: **Information declaration required** (Continue to step 4 below).

![Image illustrating chat interface and error message if any](/images/Workshop/2.2-Prerequisite/03_Send_Activation_Message.jpg)

**Step 4. Submit Use Case (Only perform if error occurred in step 3)**

- Click **Submit use case details** (in the error message).
- Fill in the form:
  - Company Name: Enter `Personal Learning`.
  - Industry: Select `Technology`.
  - Intended Use: Select `Research & Development`.
- Click **Submit**.
- Wait 1 minute, return to the chat box, Click **Run** on the `Hello` message again to confirm success.

![Image illustrating Use Case information form](/images/Workshop/2.2-Prerequisite/04_Use_case.jpg)
