---
title: "Khởi tạo Knowledge Base"
date: "2025-09-09"
weight: 1
chapter: false
pre: " <b> 2.3.1 </b> "
---

#### Mục tiêu

Chúng ta sẽ sử dụng Amazon Bedrock Wizard để thiết lập toàn bộ kiến trúc RAG. Quá trình này sẽ kết nối nguồn dữ liệu S3, mô hình Embedding và tự động khởi tạo kho lưu trữ Vector (OpenSearch Serverless).

#### Các Bước Thực hiện

1.  Đăng nhập vào **AWS Management Console** và truy cập dịch vụ **Amazon Bedrock**.
2.  Trong menu bên trái, chọn **Knowledge bases**.

![Click_Knowledge_base](/images/Workshop/2.3-Knowledge-Base/01_Click_Knowledge_base.jpg)

3.  Nhấp vào nút **Create knowledge base** ở góc trên bên phải của màn hình. Chọn `Knowledge Base with vector store`

![Create Knowledge Base](/images/Workshop/2.3-Knowledge-Base/02_Create_Knowledge_base.jpg)

**Bước 1: Cấu hình Knowledge Base**

Trên màn hình cấu hình đầu tiên:

1. **Knowledge base name:** Nhập tên `knowledge-base-demo`
2. **Knowledge Base description - optional:** Nhập `Knowledge Base from AWS Overview` (Phần này bạn cần mô tả dữ liệu bạn đã upload lên S3 trước đó).
3. **IAM permissions:** Chọn tùy chọn **Create and use a new service role**.
4. **Service role name:** Giữ giá trị mặc định do AWS đề xuất (bắt đầu bằng `AmazonBedrockExecutionRoleForKnowledgeBase_...`).

![Configure Knowledge Base](/images/Workshop/2.3-Knowledge-Base/03_Configure_KB.jpg)

5.  Nhấp **Next**.

![Configure Knowledge Base_02](/images/Workshop/2.3-Knowledge-Base/04_Configure_KB_2.jpg)

**Bước 2: Cấu hình Nguồn Dữ liệu**

Kết nối đến S3 Bucket chứa các tài liệu:

1.  **Data source name:** Nhập `knowledge-base-demo`

![Configure KB Step 2](/images/Workshop/2.3-Knowledge-Base/05_Step_2.jpg)

2.  **S3 URI:**
    - Nhấp vào nút **Browse S3**.
    - Trong cửa sổ pop-up, chọn bucket `rag-workshop-demo` mà bạn đã tạo trong phần trước.
    - Nhấp **Choose**.

![Configure S3 URI](/images/Workshop/2.3-Knowledge-Base/06_Configure_S3_URI.jpg)

3. Giữ lại các cấu hình Default. Nhấp **Next**.

![Finished Step 2](/images/Workshop/2.3-Knowledge-Base/07_Finished_Step_2.jpg)

**Bước 3: Lưu trữ & Xử lý**
Đây là bước quan trọng nhất để xác định mô hình AI và vị trí lưu trữ vector:

1.  **Embeddings model:**

    - Nhấp **Select model**.
      ![Configure Step 3](/images/Workshop/2.3-Knowledge-Base/08_Config_Step_3.jpg)

    - Chọn model: **Titan Embeddings G1 - Text v2**.
      ![Configure Step 3](/images/Workshop/2.3-Knowledge-Base/09_Config_Step_3.jpg)

2.  **Vector Store:**
    - **Vector store creation method:** Chọn `Quick create a new vector store - Recommended`
    - **Vector store type - new:** Chọn `Amazon OpenSearch Serverless`
    - _Lưu ý:_ Tùy chọn này cho phép AWS tự động tạo một cluster **Amazon OpenSearch Serverless** để lưu trữ dữ liệu, giúp bạn không phải quản lý cơ sở hạ tầng thủ công.
3.  Nhấp **Next**.
    ![Configure Step 3](/images/Workshop/2.3-Knowledge-Base/10_Config_Step_3.jpg)

**Bước 4: Kiểm tra và Tạo Knowledge Base**

1.  Kiểm tra tất cả thông tin cấu hình trên trang Review.
2.  Đảm bảo các mục S3 URI và Model đều chính xác.
3.  Cuộn xuống cuối trang và nhấp vào nút **Create knowledge base**.

![Step 4](/images/Workshop/2.3-Knowledge-Base/11_Step_4.jpg)

**Bước 5: Chờ Khởi tạo**

Sau khi nhấp Create, hệ thống sẽ bắt đầu quá trình khởi tạo cơ sở hạ tầng nền cho Vector Store.

- **Thời gian chờ:** Khoảng **2 - 5 phút**.
- **Lưu ý:** Vui lòng không đóng trình duyệt trong thời gian này.
- **Thành công:** Khi màn hình hiển thị thông báo màu xanh **"Knowledge base created successfully"**, bạn đã hoàn thành bước này và sẵn sàng cho phần tiếp theo.

![Step 5](/images/Workshop/2.3-Knowledge-Base/12_Step_5.jpg)
