---
title: "Workshop"
date: "2025-09-09"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Xây dựng ứng dụng RAG sử dụng Knowledge Bases cho Amazon Bedrock

#### Tổng quan

**Knowledge Bases for Amazon Bedrock** là một tính năng được quản lý hoàn toàn giúp bạn triển khai kỹ thuật RAG (Retrieval-Augmented Generation) bằng cách kết nối các Foundation Models với nguồn dữ liệu nội bộ của bạn để cung cấp các phản hồi chính xác, có trích dẫn và phù hợp với ngữ cảnh.

> RAG là một kỹ thuật để tối ưu hóa đầu ra của Large Language Model (LLM) bằng cách truy xuất thông tin từ cơ sở dữ liệu bên ngoài đáng tin cậy (Retrieval) và thêm nó vào ngữ cảnh (Augmentation) trước khi tạo ra câu trả lời (Generation). Phương pháp này giúp khắc phục những hạn chế về dữ liệu huấn luyện lỗi thời và đảm bảo AI trả lời dựa trên thông tin thực tế được cung cấp.

Trong bài lab này, chúng ta sẽ học cách xây dựng một trợ lý AI có khả năng "đọc và hiểu" các tài liệu doanh nghiệp độc quyền. Bạn sẽ thực hiện quy trình từ việc nhập dữ liệu và tạo chỉ mục vector đến cấu hình mô hình để trả lời câu hỏi dựa trên những tài liệu đó mà không cần quản lý bất kỳ máy chủ nào.

Chúng ta sẽ sử dụng ba thành phần chính để thiết lập quy trình xử lý RAG hoàn chỉnh:

- **Nguồn dữ liệu (Amazon S3)** - Đóng vai trò là kho lưu trữ "sự thật". Bạn sẽ tải các tài liệu (PDF, Word, Text) lên một S3 bucket. Knowledge Base sẽ sử dụng nguồn này để đồng bộ hóa dữ liệu.
- **Vector Store (OpenSearch Serverless)** - Nơi lưu trữ các embeddings vector (dữ liệu được mã hóa bằng số). Khi người dùng đặt câu hỏi, hệ thống sẽ thực hiện tìm kiếm ngữ nghĩa tại đây để trích xuất các đoạn văn bản liên quan nhất thay vì tìm kiếm từ khóa tiêu chuẩn.
- **Foundation Model (Claude 3)** - Large Language Model đóng vai trò là bộ não xử lý. Nó nhận câu hỏi của người dùng cùng với thông tin tìm thấy từ Vector Store, sau đó tổng hợp và tạo ra câu trả lời tự nhiên, chính xác kèm theo trích dẫn nguồn.

#### Kết quả đạt được

Khi kết thúc workshop, bạn sẽ có một hệ thống Chatbot thực tế, hoạt động với các tính năng sau:

- Trò chuyện hỏi đáp về nội dung tài liệu độc quyền.
- Câu trả lời chính xác, không có ảo giác (hallucinations).
- Trích dẫn nguồn (biết chính xác câu trả lời đến từ trang nào).
- Triển khai nhanh chóng mà không cần viết mã xử lý dữ liệu phức tạp.

#### Nội dung

1. [Tổng quan về Workshop](2.1-Workshop-overview/)
2. [Chuẩn bị môi trường](2.2-Prerequiste/)
3. [Tạo và cấu hình Knowledge Base](2.3-Knowledge-Base/)
4. [Kiểm tra Chatbot (RAG)](2.4-Test-Chatbox/)
5. [Tích hợp ứng dụng Client (Tùy chọn)](2.5-Client-Integration/)
6. [Cập nhật dữ liệu](2.6-Update-Data/)
7. [Dọn dẹp tài nguyên](2.7-Cleanup/)
