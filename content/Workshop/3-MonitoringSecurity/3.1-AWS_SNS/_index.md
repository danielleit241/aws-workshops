---
title: "Set up an Alert System with Amazon SNS"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

### AWS SNS configuration steps

We will perform a quick test run to ensure your account is ready, and then complete the setup steps for Amazon SNS.

**Step 1: Access the AWS Console**

First, use the search bar to navigate to [Amazon Simple Notification Service](https://console.aws.amazon.com/sns/home)

![3.1.1](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.1.svg)

**Step 2: Open Topics**

From the left menu, choose **Topics -> Create topic**

![3.1.2](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.2.svg)

**Step 3: Configure the Topic**

- **Type:** Choose **Standard**.
- **Name:** `SNS Alerts`
- Keep other settings as **Default**.

![3.1.3](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.3.svg)

Scroll down and click **Create topic**.

![3.1.4](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.4.svg)

Verify that the topic was created successfully.

![3.1.5](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.5.svg)

**Step 4: Open Subscriptions**

From the left menu, choose **Subscriptions -> Create subscription**

![3.1.6](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.6.svg)

**Step 5: Configure the Subscription**

- **Topic ARN:** Select the `SNS Alerts` topic you created earlier.
- **Protocol:** Choose **Email**.
- **Endpoint:** Enter your email address.
- Click **Create subscription**.

![3.1.7](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.7.svg)

- **Confirmation:** Open your email inbox and find the message from **AWS Notifications** (it may be in the spam folder).
- Click **Confirm subscription** to activate the channel.

![3.1.8](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.8.svg)

- You should receive a confirmation that the subscription is successful.

![3.1.9](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.9.svg)

**Step 6: Verify Subscription Status**

Confirm that the subscription status shows **Confirmed**.

![3.1.10](/images/Workshop/3-Monitoring&Security/3.1-AWS_SNS/3.1.10.svg)

**Congratulations — you have completed the AWS SNS configuration.**

