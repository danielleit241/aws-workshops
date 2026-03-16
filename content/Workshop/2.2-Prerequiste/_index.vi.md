---
title: "Chuẩn bị môi trường"
date: "2025-09-09"
weight: 2
chapter: false
pre: " <b> 2.2. </b> "
---

#### Mục tiêu

Trước khi bắt tay vào xây dựng ứng dụng, chúng ta cần thiết lập một nền tảng vững chắc. Giống như việc chuẩn bị nguyên liệu trước khi nấu ăn, phần này đảm bảo rằng tài khoản AWS của bạn đã sẵn sàng với đầy đủ quyền hạn và dữ liệu cần thiết.

Trong phần này, chúng ta sẽ hoàn thành 3 mục tiêu khởi tạo quan trọng:

1.  **Chọn Region (Vùng):** Thiết lập môi trường làm việc tại vùng **United States N. Virginia (us-east-1)** để tối ưu hóa tốc độ kết nối và đảm bảo tính sẵn sàng của dịch vụ.
2.  **Kích hoạt Model (Model Access):** Kiểm tra và đảm bảo tài khoản có quyền gọi model **Anthropic Claude 3** – "bộ não" ngôn ngữ chính của hệ thống.
3.  **Chuẩn bị Dữ liệu (Data Setup):** Khởi tạo kho lưu trữ (S3 Bucket) và tải lên tài liệu nguồn để phục vụ cho quá trình nạp kiến thức (Ingestion) sau này.

#### Các thành phần chính

Trong phần chuẩn bị này, chúng ta sẽ tương tác với các thành phần sau:

- **AWS Management Console (Region Selector):** Giao diện quản lý chung để chuyển đổi Region làm việc sang United States N. Virginia.
- **Amazon Bedrock (Model Access & Playground):** Nơi quản lý quyền truy cập các mô hình nền tảng (Foundation Models) và công cụ chat để kiểm tra nhanh khả năng phản hồi của AI.
- **Amazon S3 (Simple Storage Service):** Dịch vụ lưu trữ đối tượng, nơi chúng ta sẽ tạo Bucket để chứa các file tài liệu gốc (PDF, Word, Text).

#### Các Bước Thực hiện

1. [Kiểm tra truy cập Model](2.2.1-Model-Access/)
2. [Chuẩn bị dữ liệu nguồn](2.2.2-Prepare-Data/)