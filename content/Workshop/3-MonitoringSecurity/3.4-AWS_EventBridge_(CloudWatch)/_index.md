---
title: "Set up Data Pipeline Error Alerts with Amazon EventBridge (CloudWatch) (OPTIONAL)"
date: "2026-05-02"
weight: 4
chapter: false
pre: " <b> 4. </b> "
---
> **Note:** Using Amazon EventBridge together with CloudWatch is optional. If the system does not require event-driven architecture or complex event routing, CloudWatch can still be used independently for monitoring, logging, and alerting as usual.

### Objectives

Set up an automated event-driven mechanism and end-to-end monitoring for the Data Pipeline lifecycle. Specifically, the system will perform two core tasks:

1. **Automatic Trigger:** Detect when new data files (**Raw Data**) are uploaded to Amazon S3 and immediately trigger AWS Step Functions (State Machine) to run the ETL workflow.
2. **Centralized Error Alerting:** Monitor the status of the entire AWS Step Functions workflow. If any step (Crawler/Glue Job) fails and causes the pipeline to fail (**FAILED**, **TIMED_OUT**, **ABORTED**), the system will extract the error and send an alert email through **Amazon SNS**.

### Architecture Logic Overview

* **S3 Upload Event (Rule 1):** The S3 bucket acts as the event source. When a new object is created (**Object Created**), EventBridge captures the event stream and invokes the target service, AWS Step Functions, so the system can run automatically without manual intervention.
* **Step Functions Error Event (Rule 2):** Instead of handling small errors in each Glue Job separately, Step Functions acts as the conductor. If an error occurs in any node, Step Functions changes the overall status to **FAILED**. EventBridge detects this status, uses an **Input Transformer** to extract the **executionArn**, and formats a clear alert message before sending it to **Amazon SNS**.

### Detailed Amazon EventBridge (CloudWatch) Setup

We will set up the two EventBridge rules sequentially based on the two architecture logics above.

{{% notice note %}}
**Requirement:** You must have already created the Amazon SNS Topic in section 3.1 and completed the AWS Step Functions State Machine setup in the previous section.
{{% /notice %}}

### Part 1: Create Rule 1 - Monitor Step Functions Errors
**Step 1: Open Amazon EventBridge**

First, use the search bar to open [Amazon EventBridge](https://console.aws.amazon.com/events/home)

![3.4.1](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.1.svg)

**Step 2: Create the EventBridge Rule (Rule 1)**

1. From the left menu, choose **Rules** -> **Create rule**.

![3.4.2](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.2.svg)

2. **Builder mode:** Choose **Advanced builder**
3. **Name:** Enter `monitor-stepfunctions-errors`.
4. **Description:** `Monitors AWS Step Functions state machine execution changes and triggers an SNS alert if the orchestration pipeline fails, times out, or is aborted.`
5. **Event bus:** Keep **default**.
6. Click **Next**

![3.4.3](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.3.svg)

**Step 3: Configure the Event Filter (Rule 1)**

1. **Events:** Choose **AWS events or EventBridge partner events**.

![3.4.4](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.4.svg)

2. Scroll down to the **Event pattern** section:
* **Creation method:** Choose **Use pattern form**
* **Event source:** Choose **AWS services**.
* **AWS service:** Choose **Step Functions**.
* **Event type:** Choose **Step Functions Execution Status Change**.
* **Event Type Specification 1:** Select **Specific state(s)** and choose **FAILED**, **TIMED_OUT**, and **ABORTED**.

3. Click **Next**.

![3.4.5](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.5.svg)

**Step 4: Select the Target and Configure the Input Transformer**

1. **Target types:** Choose **AWS service**.
2. **Select a target:** Search for and choose **SNS topic**.
3. **Topic:** Open the list and select your **SNS-Alerts** topic.
4. Expand **Additional settings**

![3.4.6](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.6.svg)

In **Configure target input**, choose **Input transformer** -> click **Configure input transformer**.

![3.4.7](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.7.svg)

5. **Part 1: Input Path** - Copy and paste the following JSON:

```json
{
	"pipelineName": "$.detail.stateMachineArn",
	"executionArn": "$.detail.executionArn",
	"status": "$.detail.status"
}

```

![3.4.8](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.8.svg)

6. **Part 2: Template** - Copy and paste the following text:

{{% notice warning %}}
**IMPORTANT WARNING:** The entire text below **MUST BE WRAPPED IN DOUBLE QUOTES `" "`**.
{{% /notice %}}

```text
"WARNING: The Step Functions Data Pipeline execution has failed! \n\n- State Machine: <pipelineName>\n- Execution ID: <executionArn>\n- Status: <status>\n\nPlease review the logs in the AWS Step Functions Console to identify which Glue Job encountered an issue."

```

![3.4.9](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.9.svg)

7. Click **Confirm** -> **Next** -> skip Tags -> click **Create rule**.

![3.4.10](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.10.svg)

---

### Part 2: Create Rule 2 - Automatic Trigger from S3

{{% notice note %}}
**Required:** Go to your S3 bucket (Raw Data) -> **Properties** tab -> scroll down to **Amazon EventBridge** and turn it **On** before continuing with the steps below.
{{% /notice %}}

![3.4.11](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.11.svg)

**Step 5: Create the EventBridge Rule (Rule 2)**

1. Return to the **Rules** page and click **Create rule**.
2. **Name:** Enter `trigger-on-s3-upload`.
3. **Description:** `Automatically triggers the AWS Step Functions data orchestration pipeline whenever a new raw data object is uploaded to the landing S3 bucket`
4. **Event bus:** Keep **default**.
5. Click **Next**.

![3.4.12](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.12.svg)

**Step 6: Configure the Event Filter (Rule 2)**
1. **Events:** Choose **AWS events or EventBridge partner events**.

![3.4.4](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.4.svg)

2. Scroll down to the **Event pattern** section:

- **Event source:** Choose **AWS services**.
- **AWS service:** Choose **Simple Storage Service (S3)**.
- **Event type:** Choose **Amazon S3 Event Notification**.
- **Specific event(s):** Select **Object Created**.
- **Specific bucket(s) by name:** Enter the exact name of your raw data S3 bucket: `yellow-taxi-trip-demo-fcaj `

3. The JSON format in the validation box on the right will look similar to the following:

```json
{
	"source": ["aws.s3"],
	"detail-type": ["Object Created"],
	"detail": {
		"bucket": {
			"name": ["your-s3-bucket-name"]
		}
	}
}

```

![3.4.13](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.13.svg)

4. Click **Next**.

**Step 7: Select the Target (Invoke Step Functions)**

1. **Select a target:** Choose **AWS service**.
2. **Select a target:** Search for and choose **Step Functions state machine**.
3. **State machine:** Select **DataPipeline-Orchestrator**.
4. Expand **Additional settings**

![3.4.14](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.14.svg)

In **Configure target input**, choose **Input transformer** -> click **Configure input transformer**.

![3.4.7](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.7.svg)

5. **Part 1: Input Path** - Copy and paste the following JSON:

```json
{
	"pipelineName": "$.detail.stateMachineArn",
	"executionArn": "$.detail.executionArn",
	"status": "$.detail.status"
}

```

![3.4.8](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.8.svg)

6. **Part 2: Template** - Copy and paste the following text:

{{% notice warning %}}
**IMPORTANT WARNING:** The entire text below **MUST BE WRAPPED IN DOUBLE QUOTES `" "`**.
{{% /notice %}}

```text
"WARNING: The Step Functions Data Pipeline execution has failed! \n\n- State Machine: <pipelineName>\n- Execution ID: <executionArn>\n- Status: <status>\n\nPlease review the logs in the AWS Step Functions Console to identify which Glue Job encountered an issue."

```

![3.4.9](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.9.svg)

7. Click **Confirm** -> **Next** -> skip Tags -> click **Create rule**.

![3.4.15](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.15.svg)

8. Click **Next** -> skip Tags -> click **Create rule**.

### Done!

Your Data Pipeline is now fully automated. As soon as you upload a data file to S3, Step Functions will automatically run the entire ETL workflow. At the same time, any errors that occur in the system chain will be collected and delivered neatly to your inbox.
