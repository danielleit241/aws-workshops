---
title: "Kiểm thử Chatbot (RAG)"
date: "2025-09-09"
weight: 4
chapter: false
pre: " <b> 2.4. </b> "
---

#### Mục tiêu

Sau khi đã nhập dữ liệu thành công vào Vector Store, đã đến lúc xác minh kết quả. Trong phần này, bạn sẽ đóng vai trò là người dùng cuối, đặt câu hỏi cho Chatbot trực tiếp trong giao diện AWS Console để quan sát cách hệ thống RAG hoạt động.

Chúng ta sẽ tập trung vào 2 yếu tố:

1.  **Độ chính xác:** AI có trả lời đúng dựa trên tài liệu không?
2.  **Tính minh bạch:** AI có thể trích dẫn nguồn (Citation) của thông tin không?

#### Các Bước Thực hiện

**Bước 1: Cấu hình cửa sổ kiểm thử**

Để bắt đầu trò chuyện, chúng ta cần chọn một Foundation Model sẽ đóng vai trò là "người trả lời".

1.  Trong giao diện chi tiết Knowledge Base của bạn, hãy xem bảng điều khiển bên phải có tiêu đề **Test knowledge base**.
![Open KB](/images/Workshop/2.4-Test-Chatbox/01_Test_KB.jpg)

2.  Nhấp vào nút **Select model**.

![Select Model](/images/Workshop/2.4-Test-Chatbox/02_Select_Model.jpg)

3.  Trong bảng điều khiển lựa chọn xuất hiện:
    - **Category:** Chọn `Anthropic`.
    - **Model:** Chọn `Claude 3 Sonnet` (hoặc _Claude 3.5 Sonnet_ / _Haiku_ tùy thuộc vào model bạn đã kích hoạt).
    - **Throughput:** Giữ nguyên `On-demand`.
4.  Nhấp **Apply**.

![Hình minh họa bảng cấu hình lựa chọn Claude 3 Model](/images/Workshop/2.4-Test-Chatbox/03_Test_KB.jpg)

**Bước 2: Tiến hành hội thoại (Chat)**

Bây giờ, hãy thử đặt một câu hỏi liên quan đến nội dung tài liệu bạn đã tải lên.

1.  Trong ô nhập liệu (Message input), gõ câu hỏi của bạn.
    - _Ví dụ:_ Nếu bạn đã tải lên tài liệu "Tổng quan về AWS", hãy hỏi: _"Bạn có thể giải thích cho tôi EC2 là gì không?"_.
2.  Nhấp **Run**.
3.  **Quan sát kết quả:**
    - AI sẽ suy nghĩ trong vài giây (truy vấn Vector Store).
    - Sau đó, nó sẽ trả lời bằng ngôn ngữ tự nhiên, tóm tắt thông tin tìm được.

![Hình minh họa câu hỏi và câu trả lời của AI trong giao diện chat](/images/Workshop/2.4-Test-Chatbox/04_Promt_test.jpg)

**Bước 3: Xác minh nguồn dữ liệu**

Đây là tính năng quan trọng nhất của RAG giúp phân biệt với ChatGPT thông thường: khả năng chứng minh nguồn thông tin.

1.  Trong câu trả lời của AI, hãy chú ý đến các số nhỏ (chú thích) hoặc văn bản **Show source details**.
2.  Nhấp vào các số đó hoặc nút chi tiết.
3.  Một cửa sổ **Source details** sẽ xuất hiện, hiển thị:
    - **Source chunk:** Đoạn văn bản gốc chính xác mà AI tìm thấy trong tài liệu.
    - **Score:** Điểm tương đồng (mức độ liên quan).
    - **S3 Location:** Đường dẫn đến file gốc.

![Hình minh họa cửa sổ Source Details hiển thị đoạn văn bản gốc](/images/Workshop/2.4-Test-Chatbox/05_Promt_test.jpg)

_Việc nhìn thấy đoạn văn bản gốc này chứng minh rằng AI không "ảo tưởng" mà đang thực sự đọc tài liệu của bạn._

**Bước 4: Kiểm thử với câu hỏi không liên quan (Tùy chọn)**

Để xem hệ thống phản ứng như thế nào khi không tìm thấy thông tin.

1.  Đặt một câu hỏi hoàn toàn không liên quan đến tài liệu.
    - _Ví dụ:_ _"Hãy giải thích cho tôi một số kiến thức về tài chính cá nhân?"_ (Trong khi tài liệu của bạn là về Điện toán đám mây).
2.  **Kết quả mong đợi:**
    - AI có thể trả lời dựa trên kiến thức tổng quát của nó (nếu không bị hạn chế).
    - HOẶC AI sẽ trả lời _"Xin lỗi, tôi không thể trả lời câu hỏi của bạn dựa trên dữ liệu truy xuất được"_ - Đây là hành vi lý tưởng cho một ứng dụng RAG doanh nghiệp.

![Hình minh họa phản hồi khi đặt câu hỏi ngoài chủ đề](/images/Workshop/2.4-Test-Chatbox/06_Promt_test.jpg)
