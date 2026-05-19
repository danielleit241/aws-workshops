---
title: "Thiết lập Báo động Lỗi Data Pipeline với Amazon EventBridge (CloudWatch)"
date: "2026-05-02"
weight: 4
chapter: false
pre: " <b> 4. </b> "
---
### Mục tiêu

Thiết lập một cơ chế tự động theo dõi trạng thái của các tiến trình xử lý dữ liệu (AWS Glue ETL Job). Khi một Job chạy thất bại (**FAILED**) hoặc quá thời gian (**TIMEOUT**), hệ thống sẽ ngay lập tức:

1. Bắt sự kiện (Event) lỗi thông qua **Amazon EventBridge**.
2. Trích xuất thông tin lỗi quan trọng (Tên Job, Trạng thái, Lỗi chi tiết) bằng **Input Transformer**.
3. Định dạng lại nội dung thân thiện, dễ đọc.
4. Gửi thông báo khẩn cấp đến Email của Quản trị viên thông qua **Amazon SNS**.

### Trình bày Logic kiến trúc.

* **AWS Glue:** Là nguồn phát sinh sự kiện (Event Source). Mỗi khi trạng thái của một Job thay đổi (ví dụ: từ **RUNNING** sang **FAILED**), Glue sẽ tự động phát ra một sự kiện lên bus mặc định (default event bus) của AWS. Sự kiện này mang một chuỗi JSON chứa toàn bộ thông tin về Job đó.

* **Amazon EventBridge (Rules):** Đóng vai trò là "Người gác cổng". Chúng ta sẽ tạo một Rule (Quy tắc) với bộ lọc (Event Pattern) chỉ "bắt" những sự kiện có nguồn từ **Glue** và trạng thái là **FAILED** hoặc **TIMEOUT**. Các trạng thái khác như **SUCCEEDED** sẽ bị bỏ qua để tránh spam thông báo.

* **Input Transformer (Bên trong EventBridge Target):** Đây là bước **quan trọng nhất** để xử lý thông tin. Thay vì gửi nguyên một cục JSON thô kệch, khó hiểu, Transformer sẽ:

* **Input Path:** Khai báo các biến (variables) để trích xuất các giá trị cụ thể từ cục JSON gốc (Ví dụ: Lấy tên Job gán vào biến **jobName**).

* **Input Template:** Định nghĩa một bộ khung tin nhắn (như một bức thư) và điền các biến đã trích xuất vào đó để tạo thành thông báo hoàn chỉnh. **Lưu ý cực kỳ quan trọng:** Chuỗi Template này **phải được đặt trong dấu ngoặc kép (" ")**, nếu không sẽ gặp lỗi Invalid Template.

* **Amazon SNS (Target):** Nhận nội dung đã được "xào nấu" đẹp đẽ từ Transformer và gửi ngay đến các Email đã đăng ký (Subscriber).

### Các bước Cấu hình Chi tiết Amazon EventBridge (CloudWatch)

Chúng ta sẽ thực hiện một bài kiểm tra nhanh (Test Run) để đảm bảo tài khoản của bạn đã sẵn sàng. Và thực hiện các bước set-up cho AWS CloudTrail. 

{{% notice note %}}
**Yêu cầu:** Bạn đã hoàn thành việc tạo Amazon SNS Topic và Subscriptions ở phần 3.1 trước.
{{% /notice %}}

**Bước 1: Truy cập Amazon EventBridge**

Đầu tiên ở thanh tìm kiếm, truy cập vào [Amazon EventBridge](https://console.aws.amazon.com/events/home)

![3.4.1](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.1.svg)

**Bước 2: Khởi tạo EventBridge Rule**

1. Truy cập **Amazon EventBridge Console**.
2. Ở menu bên trái, chọn **Rules** -> **Create rule**.

![3.4.2](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWat   ch)/3.4.2.svg)

3. **Builder mode:** Chọn **Advanced builder**

4. **Name:** Nhập tên `GlueJob-Failure-Alert`.
5. **Description:** `Triggers an Amazon SNS notification automatically whenever an AWS Glue ETL Job status changes to FAILED or TIMEOUT, enabling real-time alerting for data pipeline failures.`
6. **Event bus:** Giữ nguyên **default**.

*7. **Rule type:** Chọn **Rule with an event pattern** -> Nhấn **Next**.*. - >>>>> THỪA BƯỚC CHECK LATER

![3.4.3](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.3.svg)

**Bước 3: Thiết lập Bộ lọc Sự kiện (Build Event Pattern)**

Mục đích của bước này là chỉ bắt các lỗi từ Glue.

1. **Event source:** Chọn **AWS events or EventBridge partner events**.
2. Kéo xuống phần **Event pattern**:
* **Event source:** Chọn **AWS services**.
* **AWS service:** Chọn **Glue**.
* **Event type:** Chọn **Glue Job State Change**.

![3.4.4](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.4.svg)

3. Nhấn **Next**.

**Bước 4: Chỉ định Đích đến (Select Targets)**

Đây là nơi sự kiện sẽ được gửi tới (SNS) và cấu hình Transformer.

1. **Target types:** Chọn **AWS service**.
2. **Select a target:** Tìm và chọn **SNS topic**.
3. **Topic:** Mở danh sách và chọn Topic **SNS-Alerts** mà bạn đã tạo ở phần 3.1.
4. Mở rộng phần **Additional settings** (Đây là phần quan trọng để định dạng lại tin nhắn).

![3.4.5](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.5.svg)

5. Tại mục **Configure target input**, chọn **Input transformer**.
6. Nhấn nút **Configure input transformer**.
7. Một cửa sổ mới hiện ra:
* **Phần 1: Input Path (Khai báo biến trích xuất từ JSON gốc)**
Hãy copy và paste đoạn JSON sau vào ô **Input Path**:
```json
{
  "jobName": "$.detail.jobName",
  "state": "$.detail.state",
  "errorMessage": "$.detail.errorMessage"
}

```


*(Giải thích: Chúng ta đang lấy giá trị `jobName` từ trong JSON gốc và gán vào biến nội bộ `<jobName>`)*.
* **Phần 2: Template (Định dạng khung tin nhắn)**
Hãy copy và paste đoạn text sau vào ô **Template**.
**🚨 CẢNH BÁO QUAN TRỌNG:** Toàn bộ đoạn văn bản này **BẮT BUỘC PHẢI ĐƯỢC BAO BỌC BỞI CẶP DẤU NGOẶC KÉP `" "**` (như trong hướng dẫn khắc phục lỗi ở phút 16:11 của video). Nếu có dấu ngoặc kép ở bên trong nội dung, bạn phải dùng dấu gạch chéo ngược `\` để escape (vd: `\"`).
```text
"⚠️ CẢNH BÁO: Tiến trình AWS Glue Job đã thất bại! ⚠️\n\n- Tên Job: <jobName>\n- Trạng thái: <state>\n- Thông báo lỗi chi tiết: <errorMessage>\n\nVui lòng kiểm tra lại log trên AWS Console để xử lý sự cố."

```




8. Nhấn **Confirm** để lưu cấu hình Transformer.
9. Nhấn **Next** -> Bỏ qua phần Tags (nhấn **Next**) -> **Review and create** -> Nhấn **Create rule**.

### 🎉 Hoàn tất!

Bây giờ hệ thống cảnh báo của bạn đã hoạt động. Bất cứ khi nào một tiến trình Glue ETL Job bị thất bại, bạn sẽ nhận được một email với nội dung định dạng rất gọn gàng và chuyên nghiệp. Bạn có thể cố tình làm sai một Glue Job ở phần sau của Workshop để kiểm tra (Test) xem hệ thống EventBridge này có bắn mail về đúng hay không.