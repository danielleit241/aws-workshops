---
title: "Dọn dẹp Tài nguyên"
date: "2025-09-09"
weight: 7
chapter: false
pre: " <b> 2.7. </b> "
---

#### Mục tiêu

Để tránh phát sinh chi phí không mong muốn sau khi hoàn thành bài thực hành, chúng ta cần xóa các tài nguyên đã tạo.

> ⚠️ **CẢNH BÁO:**
> Xóa **Knowledge Base** KHÔNG tự động xóa **Vector Store (OpenSearch Serverless)**. Bạn phải xóa thủ công OpenSearch Serverless Collection vì đây là dịch vụ tốn chi phí nhất trong Lab này.

#### Các Bước Thực hiện

**Bước 1: Xóa Knowledge Base**

1.  Truy cập **Amazon Bedrock Console** -> **Knowledge bases**.
2.  Chọn nút radio bên cạnh tên Knowledge Base của bạn.

3.  Nhấp vào nút **Delete**.
4.  Hộp thoại xuất hiện, nhập tên Knowledge Base để xác nhận (hoặc gõ `delete`).
5.  Nhấp **Delete**. Quá trình này mất 10-15 phút mới xóa thành công. Nên bạn thư giản nhé

![Hình minh họa thao tác xóa Knowledge Base](/images/Workshop/2.7-Clean-up/01.jpg)

**Bước 2: Xóa Vector Store**

1.  Truy cập **Amazon OpenSearch Service**.
2.  Trong menu bên trái, ở phần **Serverless**, chọn **Collections**.
3.  Bạn sẽ thấy một Collection có tên dạng `bedrock-knowledge-base-...`.
4.  Chọn nút radio bên cạnh tên Collection đó.
5.  Nhấp vào nút **Delete**.
6.  Gõ `confirm` hoặc tên collection để xác nhận xóa.
7.  Nhấp **Delete**.

![Hình minh họa thao tác xóa OpenSearch Collection](/images/Workshop/2.7-Clean-up/02.jpg)

**Bước 3: Xóa Dữ liệu trên S3**

1.  Truy cập dịch vụ **Amazon S3**.
2.  Chọn bucket `rag-workshop-demo`.
3.  Nhấp vào nút **Empty** trước tiên.
    - Gõ `permanently delete` để xác nhận xóa tất cả các file bên trong.
4.  Sau khi bucket rỗng, quay lại danh sách Buckets.
5.  Chọn lại bucket đó và nhấp vào nút **Delete**.
6.  Nhập tên bucket để xác nhận.

![Hình minh họa thao tác Empty và Delete S3 Bucket](/images/Workshop/2.7-Clean-up/03.jpg)

#### Hoàn thành

Chúc mừng bạn đã hoàn thành đầy đủ Workshop **"Xây dựng Ứng dụng RAG với Amazon Bedrock"**. Hệ thống của bạn đã được dọn dẹp và an toàn!
