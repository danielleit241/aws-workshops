---
title: "Client Application Integration (Optional)"
date: "2025-09-09"
weight: 5
chapter: false
pre: " <b> 2.5. </b> "
---

#### Target

You will turn Python code into a professional **Web Chatbot GUI (Graphical User Interface)** that is user-friendly (similar to the ChatGPT interface) in just a few minutes.

We use:

- **Backend:** Python.
- **Frontend:** Streamlit.
- **AI Model:** **Claude 3.5 Sonnet**.

#### Implementation Steps

**Part I: Configure AWS Credentials**

**Step 1: Install AWS CLI**

Open Terminal on your computer.

```bash
# macOS
brew install awscli

# Linux
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**Step 2: Configure credentials**

```bash
aws configure
```

Enter the information when prompted:

- AWS Access Key ID: `YOUR_ACCESS_KEY`
- AWS Secret Access Key: `YOUR_SECRET_KEY`
- Default region name: `us-east-1`
- Default output format: `json`

**Step 3: Verify configuration**

```bash
# Check credentials
aws sts get-caller-identity

# Check Bedrock connection
aws bedrock-agent-runtime list-knowledge-bases --region ap-southeast-1
```

**Security notes:**

- DO NOT commit credentials to Git
- DO NOT share credentials with others
- Use IAM roles when possible
- Rotate credentials periodically

**Required permissions:**

IAM User needs the following permissions:

- `bedrock:InvokeModel`
- `bedrock:RetrieveAndGenerate`
- `bedrock:Retrieve`
- `s3:GetObject` (for Knowledge Base)

**Troubleshooting:**

_Error "Unable to locate credentials":_

- Check if ~/.aws/credentials file exists
- Check file format is correct
- Try running `aws configure` again

_Error "AccessDeniedException":_

- Check IAM permissions
- Ensure region is correct (ap-southeast-1)
- Check Knowledge Base ID is correct

_Error "ExpiredToken":_

- Credentials have expired
- Need to create new credentials from AWS Console

**Part II: Clone Project from pre-made GitHub**

**Step 1: Access the following GitHub link**

Please download and open the folder above using Visual Studio Code:

`https://github.com/DazielNguyen/chatbot_with_bedrock.git`

**Step 2: Install libraries and Python environment**

1.  Install environment:

    - MacOS: `python3 -m venv .venv`
    - Win: `python -m venv .venv`

2.  Activate environment:

    - MacOS: `source .venv/bin/activate`
    - Win: `.venv\Scripts\activate`

3.  Install libraries:
    - MacOS/ Win: `pip install -r requirements.txt`

**Step 3: Get the ID of the created Knowledge Base**

1.  Access Amazon Bedrock -> Knowledge Base -> knowledge-base-demo

![Take_ID_KB](/images/Workshop/2.5-Client-Integration/01.jpg)

2.  Update "KB_ID="YOUR_KNOWLEDGE_BASE_ID""

![Take_ID_KB](/images/Workshop/2.5-Client-Integration/02.png)

**Step 4: Run Streamlit - Chatbot UI and Experience**

1.  Run Terminal:

```bash
streamlit run start.py
```

2.  When the command finishes running, the following page will appear:

![Take_ID_KB](/images/Workshop/2.5-Client-Integration/03.png)

3.  Try asking some questions you uploaded to the Knowledge Base earlier.

![Take_ID_KB](/images/Workshop/2.5-Client-Integration/04.png)

4.  The Chatbot has returned results based on the data file you provided, with citations of your data sources.

#### Conclusion

Congratulations on successfully building a Web Chatbot built with Amazon Bedrock
