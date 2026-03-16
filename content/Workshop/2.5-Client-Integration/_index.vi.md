---
title: "Tích hợp ứng dụng Client (Tùy chọn)"
date: "2025-09-09"
weight: 5
chapter: false
pre: " <b> 2.5. </b> "
---

#### Mục tiêu

Bạn sẽ biến dòng code Python thành một **Giao diện Web Chatbot (GUI)** chuyên nghiệp, thân thiện với người dùng cuối (tương tự như giao diện ChatGPT) chỉ trong vài phút.

Chúng ta sử dụng:

- **Backend:** Python.
- **Frontend:** Streamlit.
- **AI Model:** **Claude 3.5 Sonnet**.

#### Các Bước Thực hiện

**Phần I: Cấu hình AWS Credentials**

**Bước 1: Cài đặt AWS CLI**

Mở Terminal trên máy tính của bạn.

```bash
# macOS
brew install awscli

# Linux
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

**Bước 2: Cấu hình credentials**

```bash
aws configure
```

Nhập thông tin khi được hỏi:

- AWS Access Key ID: `YOUR_ACCESS_KEY`
- AWS Secret Access Key: `YOUR_SECRET_KEY`
- Default region name: `us-east-1`
- Default output format: `json`

**Bước 3: Kiểm tra cấu hình**

```bash
# Kiểm tra credentials
aws sts get-caller-identity

# Kiểm tra kết nối Bedrock
aws bedrock-agent-runtime list-knowledge-bases --region ap-southeast-1
```

**Lưu ý bảo mật:**

- KHÔNG commit credentials vào Git
- KHÔNG share credentials với người khác
- Sử dụng IAM roles khi có thể
- Rotate credentials định kỳ

**Permissions cần thiết:**

IAM User cần có các quyền sau:

- `bedrock:InvokeModel`
- `bedrock:RetrieveAndGenerate`
- `bedrock:Retrieve`
- `s3:GetObject` (cho Knowledge Base)

**Troubleshooting:**

_Lỗi "Unable to locate credentials":_

- Kiểm tra file ~/.aws/credentials tồn tại
- Kiểm tra format file đúng
- Thử chạy `aws configure` lại

_Lỗi "AccessDeniedException":_

- Kiểm tra IAM permissions
- Đảm bảo region đúng (ap-southeast-1)
- Kiểm tra Knowledge Base ID đúng

_Lỗi "ExpiredToken":_

- Credentials đã hết hạn
- Cần tạo credentials mới từ AWS Console

**Phần II: Clone Project từ GitHub đã tạo sẵn**

**Bước 1: Truy cập vào link GitHub sau**

Bạn hãy tải về và mở folder trên bằng Visual Studio Code:

`https://github.com/DazielNguyen/chatbot_with_bedrock.git`

**Bước 2: Tải các thư viện và môi trường Python**

1.  Tải môi trường:

    - MacOS: `python3 -m venv .venv`
    - Win: `python -m venv .venv`

2.  Kích hoạt môi trường:

    - MacOS: `source .venv/bin/activate`
    - Win: `.venv\Scripts\activate`

3.  Tải thư viện:
    - MacOS/ Win: `pip install -r requirements.txt`

**Bước 3: Lấy ID của Knowledge Base đã tạo**

1.  Truy cập Amazon Bedrock -> Knowledge Base -> knowledge-base-demo

![Take_ID_KB](/images/Workshop/2.5-Client-Integration/01.jpg)

2.  Cập nhật "KB_ID="YOUR_KNOWLEDGE_BASE_ID""

![Take_ID_KB](/images/Workshop/2.5-Client-Integration/02.png)

**Bước 4: Chạy Streamlit - UI của Chatbot và Trải nghiệm**

1.  Run Terminal:

```bash
streamlit run start.py
```

2.  Khi chạy xong lệnh sẽ xuất hiện trang sau:

![Take_ID_KB](/images/Workshop/2.5-Client-Integration/03.png)

3.  Hãy thử hỏi một số câu hỏi bạn đã upload lên Knowledge Base trước đó.

![Take_ID_KB](/images/Workshop/2.5-Client-Integration/04.png)

4.  Kết quả Chabot đã trả về kết quả dựa trên file dữ liệu mà bạn đã cung cấp, có trích nguồn của dữ liệu của bạn.

#### Kết luận

Chúc mừng bạn đã xây dựng thành công một Web Chatbot được xây dựng từ Amazon Bedrock
