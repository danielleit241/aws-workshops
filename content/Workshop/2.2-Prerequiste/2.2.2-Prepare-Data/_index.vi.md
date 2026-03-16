---
title: "Chuẩn bị dữ liệu nguồn"
date: "2025-09-09"
weight: 2
chapter: false
pre: " <b> 2.2.2 </b> "
---

#### Tổng quan

Khởi tạo một kho lưu trữ đối tượng (S3 Bucket) để chứa các tài liệu gốc (PDF, Word, Text). Đây đóng vai trò là "nguồn sự thật" (Source of Truth) mà Knowledge Base sẽ truy cập để đọc hiểu, phân tích và đồng bộ hóa kiến thức cho AI. Bạn có thể lưu trữ kiến thức liên quan đến lĩnh vực của bạn sử dụng trong việc tạo trợ lý cá nhân hoặc Chatbot cho riêng bạn. 

#### Chuẩn bị dữ liệu

Chúng ta sẽ tạo một S3 Bucket để lưu trữ tài liệu gốc, đóng vai trò là nguồn tri thức cho Chatbot.

**Bước 1. Tạo S3 Bucket**

- Truy cập dịch vụ [S3](https://us-east-1.console.aws.amazon.com/s3/get-started?region=us-east-1) từ thanh tìm kiếm.
- **AWS Region:** Chọn `United States (N. Virginia us-east-1)`.

![Truy cập S3](/images/Workshop/2.2-Prerequisite/04_S3.jpg)

- Click **Create bucket**.

![Create S3 Bucket](/images/Workshop/2.2-Prerequisite/05_S3_Create_Bucket.jpg)


- Cấu hình thông tin Bucket:
    - **Bucket Type:** Chọn `General purpose`
    - **Bucket name:** Nhập `rag-workshop-demo`
    - **Object Ownership:** Giữ mặc định `ACLs disabled`.
    - **Block Public Access settings:** Giữ mặc định (Đã chọn `Block all public access`).

![Configure S3 Bucket](/images/Workshop/2.2-Prerequisite/06_Configure_S3_Bucket.jpg)

- Kéo xuống cuối trang, Click **Create bucket**.

![Ảnh minh họa giao diện tạo S3 Bucket và chọn Region](/images/Workshop/2.2-Prerequisite/07_Finished_Create_bucket.jpg)

- Kiểm tra tạo S3 Bucket thành công.

![Create S3 Bucket Successful](/images/Workshop/2.2-Prerequisite/08_Create_S3_Successful.jpg)

**Bước 2. Tải lên tài liệu mẫu**
- Đây tài liệu mẫu, liên quan để tổng quan về kiến thức điện toán đám mây của AWS. Bạn có thể sử dụng để chạy demo hoặc upload dữ liệu của bạn.

<a href="/files/2-Workshop/aws-overview.pdf" download>Tệp định dạng PDF</a>

- Tại danh sách Buckets, Click vào **tên bucket** bạn vừa tạo.

![Click_S3_Bucket](/images/Workshop/2.2-Prerequisite/09_Click_S3_Bucket.jpg)

- Click **Upload**.

![Upload_file_to_Bucket](/images/Workshop/2.2-Prerequisite/10_Upload_file_to_Bucket.jpg)

- Tại giao diện Upload:
  - Click **Add files**.
  - Chọn file tài liệu mẫu đính kèm ở phần trên hoặc file từ máy tính của bạn (Khuyên dùng file PDF hoặc Word có nhiều nội dung văn bản).
- Khi upload file xong, chọn file vừa upload, kéo xuống cuối trang, Click **Upload**.

![Upload_file_to_Bucket_02](/images/Workshop/2.2-Prerequisite/11_Click_to_Uploadfile.jpg)

- Khi thấy thông báo màu xanh "Upload succeeded", Click **Close**.

![Upload file successfully](/images/Workshop/2.2-Prerequisite/12_Successfully.jpg)