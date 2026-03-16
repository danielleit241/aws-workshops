---
title: "Giải thích RAG"
date: "2025-09-09"
weight: 1
chapter: false
pre: " <b> 2.1.1 </b> "
---

#### Định nghĩa ngắn gọn

**RAG (viết tắt của Retrieval-Augmented Generation)** là một kỹ thuật hoặc kiến trúc phần mềm trong lĩnh vực Trí tuệ nhân tạo (AI), được thiết kế để tối ưu hóa đầu ra của một Mô hình Ngôn ngữ Lớn (LLM).

Về mặt bản chất, RAG là sự kết hợp giữa hai cơ chế:

- **Cơ chế truy xuất thông tin (Information Retrieval)**: Tìm kiếm dữ liệu từ một nguồn kiến thức bên ngoài (External Knowledge Base) có độ tin cậy cao.
- **Cơ chế tạo sinh văn bản (Text Generation)**: Sử dụng khả năng hiểu và tổng hợp ngôn ngữ của LLM để tạo ra câu trả lời tự nhiên.

Mục tiêu của RAG là cung cấp cho LLM thêm ngữ cảnh (context) chính xác, cập nhật và cụ thể, giúp mô hình vượt qua giới hạn của dữ liệu huấn luyện tĩnh (static training data).

#### Vì sao cần RAG?

Các mô hình LLM truyền thống thường gặp 3 vấn đề lớn mà RAG có thể giải quyết:

- **Cập nhật thông tin (Freshness)**: LLM không cần huấn luyện lại (Re-training) hay tinh chỉnh (Fine-tuning) mà vẫn trả lời được các thông tin mới nhất, chỉ cần cập nhật vào cơ sở dữ liệu tìm kiếm.
- **Sở hữu dữ liệu (Proprietary Data)**: Cho phép AI trả lời các câu hỏi về dữ liệu riêng tư của doanh nghiệp (tài liệu nội bộ, code base, thông tin khách hàng) mà mô hình gốc không hề biết.
- **Tính xác thực (Grounding)**: Giảm thiểu "ảo giác" (Hallucination - AI bịa thông tin) bằng cách buộc AI phải trích dẫn hoặc dựa trên đoạn văn bản thực tế được tìm thấy.

#### Kiến trúc hoạt động

Quy trình xử lý một câu hỏi của RAG diễn ra như sau:

| Bước  | Tên gọi                       | Mô tả hành động                                                                                                |
| :---- | :---------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **1** | **Retrieval** (Truy xuất)     | Hệ thống tìm kiếm các đoạn văn bản liên quan nhất đến câu hỏi trong kho dữ liệu (thường dùng Vector Database). |
| **2** | **Augmentation** (Tăng cường) | Ghép câu hỏi của người dùng + Dữ liệu vừa tìm được thành một "lời nhắc" (prompt) hoàn chỉnh.                   |
| **3** | **Generation** (Tạo sinh)     | Gửi prompt đó cho AI (LLM) để nó tổng hợp và viết ra câu trả lời cuối cùng cho người dùng.                     |

![RAG](/images/Workshop/2.1-Workshop-overview/rag-initial-01.jpg)