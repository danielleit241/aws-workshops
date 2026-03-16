---
title: "Giới thiệu các dịch vụ"
date: "2025-09-09"
weight: 1
chapter: false
pre: " <b> 2.1.2 </b> "
---

Kiến trúc giải pháp được xây dựng dựa trên sự phối hợp của 4 thành phần dịch vụ chính sau đây:

#### Knowledge Bases for Amazon Bedrock

Đây là một khả năng được quản lý toàn diện (fully managed capability) giúp kết nối các Mô hình Nền tảng (Foundation Models) với nguồn dữ liệu nội bộ của doanh nghiệp.

- **Tự động hóa quy trình RAG:** Quản lý toàn bộ luồng công việc từ đầu đến cuối (end-to-end), bao gồm nhập dữ liệu (ingestion), chia nhỏ văn bản (chunking), tạo vector (embedding) và truy xuất thông tin (retrieval).
- **Kết nối ngữ cảnh:** Giúp các ứng dụng AI trả lời câu hỏi dựa trên dữ liệu riêng tư thay vì chỉ dựa vào dữ liệu huấn luyện chung chung.
- **Không cần quản lý hạ tầng:** Loại bỏ nhu cầu tự xây dựng và duy trì các đường ống dữ liệu (data pipelines) phức tạp.

#### Amazon Simple Storage Service (Amazon S3)

Là dịch vụ lưu trữ đối tượng (object storage) với khả năng mở rộng, độ bền dữ liệu 99,999999999% (11 số 9) và bảo mật hàng đầu.

- **Vai trò nguồn dữ liệu (Data Source):** Đóng vai trò là kho chứa "sự thật" (source of truth).
- **Lưu trữ tài liệu:** Chứa các tệp phi cấu trúc như PDF, Word, hoặc Text mà doanh nghiệp muốn AI học.
- **Đồng bộ hóa:** Knowledge Base sẽ định kỳ quét bucket S3 này để đồng bộ hóa và cập nhật kiến thức mới nhất.

#### Amazon OpenSearch Serverless

Là tùy chọn triển khai không máy chủ (serverless) của Amazon OpenSearch Service, giúp chạy khối lượng công việc tìm kiếm và phân tích mà không cần quản lý cụm (cluster).

- **Vai trò kho lưu trữ Vector (Vector Store):** Lưu trữ các chỉ mục vector (vector embeddings) được tạo ra từ tài liệu gốc.
- **Tìm kiếm ngữ nghĩa (Semantic Search):** Thực hiện thuật toán tìm kiếm tương đồng (similarity search/k-NN) để xác định các đoạn văn bản có ý nghĩa gần nhất với câu hỏi của người dùng.
- **Tự động mở rộng:** Tự động điều chỉnh tài nguyên tính toán và lưu trữ dựa trên nhu cầu thực tế.

#### Amazon Bedrock Foundation Models (FMs)

Cung cấp quyền truy cập vào các mô hình AI hàng đầu thông qua API thống nhất. Trong kiến trúc này, chúng ta sử dụng hai loại mô hình với vai trò riêng biệt:

- **Embedding Model (Amazon Titan Embeddings v2):**
  - Chuyển đổi văn bản (tài liệu từ S3 và câu hỏi của người dùng) thành các vector số học.
  - Giúp máy tính có thể so sánh mức độ tương đồng về ý nghĩa giữa các đoạn văn.
- **Text Generation Model (Anthropic Claude 3):**
  - Đóng vai trò là "bộ não" suy luận.
  - Nhận câu hỏi kèm theo thông tin ngữ cảnh đã được truy xuất từ Vector Store.
  - Tổng hợp thông tin và sinh ra câu trả lời tự nhiên, chính xác, có kèm trích dẫn nguồn.