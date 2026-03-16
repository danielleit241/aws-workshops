---
title: "Cập nhật dữ liệu"
date: "2025-09-09"
weight: 6
chapter: false
pre: " <b> 2.6. </b> "
---

#### Mục tiêu

Một trong những lợi thế lớn nhất của RAG so với Fine-tuning (huấn luyện lại) mô hình là khả năng cập nhật dữ liệu nhanh chóng. Khi doanh nghiệp có quy định mới, bạn chỉ cần nhập chúng vào Knowledge Base, và AI sẽ "học" chúng ngay lập tức.

Trong phần này, chúng ta sẽ mô phỏng kịch bản sau:

1.  Hỏi AI về một thông tin không tồn tại (AI sẽ trả lời là không biết).
2.  Cung cấp thông tin đó cho hệ thống bằng cách tải lên file mới.
3.  Hỏi lại câu hỏi tương tự để chứng kiến AI trả lời đúng ngay lập tức.

#### Các Bước Thực hiện

**Bước 1: Xác minh "thiếu kiến thức" ban đầu**

Chúng ta cần xác nhận rằng AI hiện tại không biết gì về thông tin bí mật mà chúng ta sắp tạo.

1.  Quay lại giao diện **Streamlit Chatbot** (được tạo trong Phần 5) hoặc sử dụng cửa sổ **Test Knowledge Base** trên Console.
2.  Đặt một câu hỏi về thông tin giả định không có thật.
    - _Ví dụ:_ _"Mã kích hoạt cho Dự án Omega là gì?"_
3.  **Quan sát kết quả:** AI sẽ trả lời rằng không thể tìm thấy thông tin trong các tài liệu được cung cấp hoặc sẽ cố gắng đưa ra câu trả lời chung chung (nếu không bị hạn chế).

![Hình minh họa AI không biết về Dự án Omega](/images/Workshop/2.6-Update-Data/01.png)

**Bước 2: Tạo dữ liệu mới**

Chúng ta sẽ tạo một file văn bản chứa "bí mật" này để nhập vào hệ thống.

1.  Trên máy tính của bạn, mở **Notepad** (Windows) hoặc **TextEdit** (Mac).
2.  Sao chép và dán nội dung sau vào file:
    ```text
    THÔNG BÁO MẬT:
    Dự án Omega bí mật chính thức khởi động vào ngày 01/12/2025.
    Mã kích hoạt là: "AWS-ROCKS-2025-SINGAPORE".
    Người Quản lý Dự án là Ông Robot.
    Vui lòng giữ thông tin này tuyệt đối bí mật.
    ```
3.  Lưu file với tên: `secret-project.txt`.

Bạn có thể tải file tại đây: <a href="/files/Workshop/secret-project.txt" download>Tệp định dạng TXT</a>
 
**Bước 3: Tải lên và Đồng bộ**

Bây giờ, chúng ta sẽ cung cấp kiến thức mới này vào "bộ não" của AI.

1.  Truy cập **S3 Console**, điều hướng đến bucket cũ của bạn (`rag-workshop-demo`).

2.  Nhấp **Upload** -> **Add files** -> Chọn file `secret-project.txt` -> **Upload**.

![Hình minh họa file tải lên thành công vào S3](/images/Workshop/2.6-Update-Data/02.png)

3.  Chuyển sang **Amazon Bedrock Console** -> Chọn **Knowledge bases** từ menu bên trái.
4.  Nhấp vào tên Knowledge Base của bạn.
5.  Cuộn xuống phần **Data source**, chọn nguồn dữ liệu (`s3-datasource`).
6.  Nhấp vào nút **Sync** (Màu cam).
7.  **Chờ đợi:** Chờ khoảng 30 giây đến 1 phút cho đến khi cột **Status** chuyển từ `Syncing` sang `Available`.

![Hình minh họa quá trình Sync hoàn tất trên Bedrock Console](/images/Workshop/2.6-Update-Data/03.png)

**Bước 4: Xác minh lại (Khoảnh khắc "Wow")**

Hệ thống hiện đã có kiến thức mới. Hãy thách thức AI một lần nữa.

1.  Quay lại giao diện **Streamlit Chatbot** (Không cần tải lại trang hoặc khởi động lại server).
2.  Hỏi chính xác câu hỏi tương tự như trước: _"Mã kích hoạt cho Dự án Omega là gì?"_
3.  **Kết quả mong đợi:**
    - AI trả lời chính xác: _"Mã kích hoạt là AWS-ROCKS-2025-SINGAPORE"_.
    - AI trích dẫn nguồn là file `secret-project.txt`.

![Hình minh họa AI trả lời chính xác sau khi cập nhật dữ liệu](/images/Workshop/2.6-Update-Data/04.png)

#### Kết luận

Bạn vừa chứng kiến sức mạnh thực sự của RAG!

- **Không cần chỉnh sửa code.**
- **Không cần huấn luyện lại mô hình.**
- **Chỉ cần Sync dữ liệu.**

Chatbot của bạn đã trở nên thông minh hơn và cập nhật với thông tin mới nhất chỉ trong vài bước đơn giản. Đây chính là lý do tại sao các doanh nghiệp chọn giải pháp này để xây dựng trợ lý ảo nội bộ.
