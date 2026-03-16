---
title: "Kiểm tra Vector Store và Đồng bộ Dữ liệu"
date: "2025-09-09"
weight: 2
chapter: false
pre: " <b> 2.3.2 </b> "
---

#### Mục tiêu

Trước khi AI có thể trả lời, dữ liệu phải được nhập vào kho lưu trữ vector (Vector Store). Chúng ta sẽ thực hiện kiểm tra "Trước và Sau" để thấy rõ cách Bedrock tự động mã hóa và lưu trữ dữ liệu vào OpenSearch.

#### Các Bước Thực hiện

**Bước 1: Kiểm tra Vector Store (Trạng thái Rỗng)**

Chúng ta sẽ truy cập trực tiếp vào Amazon OpenSearch Serverless để xác nhận rằng chưa có dữ liệu nào tồn tại.

1.  Trong thanh tìm kiếm AWS Console, gõ `Amazon OpenSearch Service` và chọn **Amazon OpenSearch Service**.
![13_Open_AOS](/images/Workshop/2.3-Knowledge-Base/13_Open_AOS.jpg)

2.  Trong menu bên trái, ở phần **Serverless**, chọn **Collections**.
![14_collection](/images/Workshop/2.3-Knowledge-Base/14_collection.jpg)

3.  Nhấp vào tên Collection mới được tạo bởi Bedrock (thường có tên dạng `bedrock-knowledge-data...`).
![15_collection](/images/Workshop/2.3-Knowledge-Base/15_collection.jpg)


4.  Trên trang chi tiết Collection, nhấp vào nút **Open Dashboard** (nằm ở góc trên bên phải màn hình).
   - _Lưu ý:_ Nếu được yêu cầu đăng nhập, hãy sử dụng thông tin đăng nhập AWS hiện tại của bạn.

![16_collection](/images/Workshop/2.3-Knowledge-Base/16_collection.jpg)

5.  Trong giao diện OpenSearch Dashboard:
   - Nhấp vào biểu tượng **Menu (3 đường ngang)** ở góc trên bên trái.
   ![17](/images/Workshop/2.3-Knowledge-Base/17.jpg)

   - Chọn **Dev Tools** (thường nằm ở cuối danh sách menu).
   ![18](/images/Workshop/2.3-Knowledge-Base/18.jpg)

6.  Trong ngăn **Console** (bên trái), nhập lệnh sau để kiểm tra dữ liệu:
    ```
    GET _search
    {
      "query": {
        "match_all": {}
      }
    }
    ```
![19](/images/Workshop/2.3-Knowledge-Base/19.jpg)

7.  Nhấp vào nút **Play (Run)** (tam giác nhỏ bên cạnh dòng lệnh).
8.  **Kết quả:** Quan sát ngăn bên phải, `hits` -> `total` -> `value` là **0**.

![20](/images/Workshop/2.3-Knowledge-Base/20.jpg)

**Bước 2: Đồng bộ Dữ liệu**

Bây giờ chúng ta sẽ kích hoạt Bedrock để đọc các file từ S3 và tải chúng vào OpenSearch.

1.  Quay lại tab **Amazon Bedrock** trên trình duyệt.
2.  Chọn **Knowledge bases** trong menu bên trái và nhấp vào tên KB bạn vừa tạo.
3.  Cuộn xuống phần **Data source**, đánh dấu vào ô (tick) bên cạnh tên nguồn dữ liệu (`s3-datasource`).
4.  Nhấp vào nút **Sync** (Màu cam).

![Hình minh họa chọn Data Source và nhấp nút Sync](/images/Workshop/2.3-Knowledge-Base/21.jpg)

5.  **Chờ đợi:**
    - Quá trình này sẽ mất **5 - 10 phút** tùy thuộc vào kích thước tài liệu mẫu.
    - Chờ cho đến khi cột **Sync status** chuyển từ `Syncing` sang `Available`.

![Hình minh họa trạng thái Sync thành công Available](/images/Workshop/2.3-Knowledge-Base/22.jpg)

**Bước 3: Kiểm tra lại Vector Store (Đã có Dữ liệu)**

Sau khi Bedrock báo hoàn tất Sync, chúng ta quay lại kho lưu trữ để xác minh dữ liệu đã được nhập thành công.

1.  Chuyển sang tab **OpenSearch Dashboard** (vẫn còn mở từ Bước 1).
2.  Trong **Dev Tools**, nhấp lại nút **Play (Run)** với lệnh cũ:
    ```
    GET _search
    {
      "query": {
        "match_all": {}
      }
    }
    ```
3.  **Kết quả:**
    - Phần `hits` -> `total` -> `value` sẽ lớn hơn **0** (ví dụ: 10, 20... tùy thuộc vào số lượng đoạn văn bản).
    - Bạn sẽ thấy chi tiết các vector (mảng số) và nội dung văn bản được lưu trữ trong trường `_source`.

![Hình minh họa kết quả Dev Tools hiển thị dữ liệu đã đồng bộ](/images/Workshop/2.3-Knowledge-Base/23.jpg)

**Chúc mừng!** Bạn đã hoàn thành việc xây dựng "bộ não" cho AI. Dữ liệu đã được mã hóa và nằm an toàn trong Vector Database, sẵn sàng cho việc truy xuất.
