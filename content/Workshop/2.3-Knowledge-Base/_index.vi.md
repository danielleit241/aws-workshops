---
title: "Tạo và Cấu hình Knowledge Base"
date: "2025-09-09"
weight: 3
chapter: false
pre: " <b> 2.3. </b> "
---

#### Mục tiêu

Sau khi hoàn thành việc chuẩn bị môi trường và dữ liệu, bước tiếp theo là thiết lập thành phần cốt lõi của kiến trúc RAG. Trong phần này, chúng ta sẽ khởi tạo **Knowledge Base**, đóng vai trò là cơ chế trung gian thông minh kết nối các nguồn dữ liệu phi cấu trúc với khả năng suy luận của các foundation models.

Chúng ta sẽ thực hiện 3 mục tiêu kỹ thuật chính:

1.  **Thiết lập Pipeline Tự động:** Cấu hình Knowledge Base để tự động hóa toàn bộ quy trình xử lý dữ liệu RAG (bao gồm trích xuất, phân đoạn văn bản và tạo vector) nhằm loại bỏ các tác vụ xử lý thủ công.
2.  **Khởi tạo Vector Store:** Triển khai một collection trên **Amazon OpenSearch Serverless** để lưu trữ các vector ngữ nghĩa, phục vụ việc truy xuất thông tin chính xác và hiệu quả.
3.  **Đồng bộ hóa Dữ liệu (Data Ingestion):** Thực hiện quy trình nhập dữ liệu ban đầu, chuyển đổi các tài liệu tĩnh từ S3 thành các vector có thể tìm kiếm trong hệ thống.

#### Các Thành phần Chính

Trong quá trình cấu hình này, chúng ta sẽ tương tác và kết nối các dịch vụ sau:

- **Knowledge Bases for Amazon Bedrock:** Dịch vụ được quản lý đóng vai trò là bộ điều phối luồng dữ liệu, kết nối các nguồn thông tin và thực thi các truy vấn ngữ nghĩa.
- **Amazon Titan Embeddings G1 - Text v2:** Mô hình chuyên dụng để chuyển đổi dữ liệu văn bản thành các vector số (Embeddings) với độ chính xác cao và hỗ trợ đa ngôn ngữ.
- **Amazon OpenSearch Serverless:** Cơ sở dữ liệu vector được quản lý hoàn toàn, chịu trách nhiệm lưu trữ và thực thi các thuật toán tìm kiếm tương đồng (k-NN).

#### Các Bước Thực hiện

1. [Khởi tạo Knowledge Base](2.3.1-Create-KB/)
2. [Kiểm tra Vector Store và Đồng bộ Dữ liệu](2.3.2-Sync-Data/)
