---
title: "Thiết lập Báo động Lỗi Data Pipeline với Amazon EventBridge (CloudWatch)"
date: "2026-05-02"
weight: 4
chapter: false
pre: " <b> 4. </b> "
---


### Mục tiêu

Thiết lập cơ chế điều phối tự động (Event-Driven) và giám sát trạng thái toàn diện cho vòng đời Data Pipeline. Cụ thể, hệ thống sẽ thực hiện 2 nhiệm vụ cốt lõi:

1. **Trigger Tự động:** Nhận diện khi có file dữ liệu mới (**Raw Data**) được tải lên Amazon S3 và lập tức kích hoạt AWS Step Functions (State Machine) để chạy chuỗi ETL.
2. **Báo động Lỗi Tập trung:** Theo dõi trạng thái của toàn bộ AWS Step Functions. Nếu có bất kỳ bước nào (Crawler/Glue Job) bên trong gặp sự cố dẫn đến Pipeline thất bại (**FAILED**, **TIMED_OUT**, **ABORTED**), hệ thống sẽ trích xuất lỗi và gửi email cảnh báo qua **Amazon SNS**.

### Trình bày Logic kiến trúc.

* **Sự kiện S3 Upload (Rule 1):** S3 bucket đóng vai trò là nguồn phát sự kiện. Khi một Object mới được tạo (**Object Created**), EventBridge sẽ hứng luồng sự kiện này và gọi API khởi chạy dịch vụ đích (Target) là AWS Step Functions, giúp hệ thống vận hành hoàn toàn tự động mà không cần can thiệp thủ công.
* **Sự kiện Step Functions Error (Rule 2):** Thay vì bắt lỗi lặt vặt ở từng Glue Job, Step Functions sẽ đóng vai trò nhạc trưởng. Nếu có lỗi xảy ra ở bất kỳ node nào, Step Functions sẽ chuyển trạng thái tổng thành **FAILED**. EventBridge nhận diện trạng thái này, sử dụng **Input Transformer** để trích xuất **executionArn** và định dạng thành một thư cảnh báo dễ hiểu trước khi đẩy sang **Amazon SNS**.

### Cấu hình chi tiết các bước về Amazon EventBridge (CloudWatch)

Chúng ta sẽ thực hiện tuần tự việc thiết lập 2 EventBridge Rules tương ứng với 2 logic kiến trúc ở trên.

{{% notice note %}}
**Yêu cầu:** Bạn đã hoàn thành việc tạo Amazon SNS Topic ở phần 3.1 và đã thiết kế xong AWS Step Functions State Machine ở phần trước.
{{% /notice %}}

### Phần 1: Tạo Rule 1 - Giám sát lỗi Step Functions
**Bước 1: Truy cập Amazon EventBridge**

Đầu tiên ở thanh tìm kiếm, truy cập vào [Amazon EventBridge](https://console.aws.amazon.com/events/home)

![3.4.1](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.1.svg)

**Bước 2: Khởi tạo EventBridge Rule (Rule 1)**

1. Ở menu bên trái, chọn **Rules** -> **Create rule**.

![3.4.2](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.2.svg)

2. **Builder mode:** Chọn **Advanced builder**
3. **Name:** Nhập tên `monitor-stepfunctions-errors`.
4. **Description:** `Monitors AWS Step Functions state machine execution changes and triggers an SNS alert if the orchestration pipeline fails, times out, or is aborted.`
5. **Event bus:** Giữ nguyên **default**.
6. Nhấn **Next**


![3.4.3](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.3.svg)

**Bước 3: Thiết lập Bộ lọc Sự kiện (Rule 1)**

1. **Events:** Chọn **AWS events or EventBridge partner events**.

![3.4.4](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.4.svg)

2. Kéo xuống phần **Event pattern**:
* **Creation method:** Chọn **Use pattern form**
* **Event source:** Chọn **AWS services**.
* **AWS service:** Chọn **Step Functions**.
* **Event type:** Chọn **Step Functions Execution Status Change**.
* **Event Type Specification 1:** Tích chọn **Specific state(s)**: Chọn **FAILED**, **TIMED_OUT**, và **ABORTED**.

3. Nhấn **Next**.

![3.4.5](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.5.svg)

**Bước 4: Chỉ định Đích đến (Select Targets) và Input Transformer**

1. **Target types:** Chọn **AWS service**.
2. **Select a target:** Tìm và chọn **SNS topic**.
3. **Topic:** Mở danh sách và chọn Topic **SNS-Alerts** của bạn.
4. Mở rộng phần **Additional settings**

![3.4.6](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.6.svg)

Tại mục **Configure target input**, chọn **Input transformer** -> Nhấn **Configure input transformer**.

![3.4.7](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.7.svg)

5. **Phần 1: Input Path** - Copy và paste đoạn JSON sau:

```json
{
  "pipelineName": "$.detail.stateMachineArn",
  "executionArn": "$.detail.executionArn",
  "status": "$.detail.status"
}

```

![3.4.8](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.8.svg)

6. **Phần 2: Template** - Copy và paste đoạn text sau:

{{% notice warning %}}
**CẢNH BÁO QUAN TRỌNG:** Toàn bộ đoạn văn bản này **BẮT BUỘC PHẢI ĐƯỢC BAO BỌC BỞI CẶP DẤU NGOẶC KÉP `" "**`.
{{% /notice %}}

```text
"CẢNH BÁO: Tiến trình Step Functions Data Pipeline đã thất bại! \n\n- State Machine: <pipelineName>\n- ID Thực thi: <executionArn>\n- Trạng thái: <status>\n\nVui lòng kiểm tra lại log trên AWS Step Functions Console để xác định Glue Job nào gặp sự cố."

```

![3.4.9](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.9.svg)

7. Nhấn **Confirm** -> **Next** -> Bỏ qua Tags -> Nhấn **Create rule**.

![3.4.10](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.10.svg)

---

### Phần 2: Tạo Rule 2 - Kích hoạt tự động từ S3

{{% notice note %}}
**Bắt buộc:** Bạn phải vào S3 Bucket (Raw Data) của mình -> Tab **Properties** -> Kéo xuống phần **Amazon EventBridge** và bật **On** trước khi thực hiện các bước dưới đây.
{{% /notice %}}

![3.4.11](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.11.svg)

**Bước 5: Khởi tạo EventBridge Rule (Rule 2)**

1. Quay lại trang **Rules**, nhấn **Create rule**.
2. **Name:** Nhập tên `trigger-on-s3-upload`.
3. **Description:** `Automatically triggers the AWS Step Functions data orchestration pipeline whenever a new raw data object is uploaded to the landing S3 bucket`
4. **Event bus:** Giữ nguyên **default**.
5. Nhấn **Next**.

![3.4.12](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.12.svg)

**Bước 6: Thiết lập Bộ lọc Sự kiện (Rule 2)**
1. Events: Chọn AWS events or EventBridge partner events.

![3.4.4](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.4.svg)

2. Kéo xuống phần **Event pattern**:

- **Event source:** Chọn **AWS services**.
- **AWS service:** Chọn **Simple Storage Service (S3)**.
- **Event type:** Chọn **Amazon S3 Event Notification**.
- **Specific event(s):** Tích chọn **Object Created**.
- **Specific bucket(s) by name:** Nhập chính xác tên S3 Bucket chứa dữ liệu thô của bạn: `yellow-taxi-trip-demo-fcaj `

3. Định dạng JSON ở ô kiểm tra bên cạnh sẽ hiển thị tương tự như sau:

```json
{
  "source": ["aws.s3"],
  "detail-type": ["Object Created"],
  "detail": {
    "bucket": {
      "name": ["ten-bucket-s3-cua-ban"]
    }
  }
}

```

![3.4.13](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.13.svg)

4. Nhấn **Next**.

**Bước 7: Chỉ định Đích đến (Gọi Step Functions)**

1. **Select a target:** Chọn **AWS service**.
2. **Select a target:** Tìm và chọn **Step Functions state machine**.
3. **State machine:** Chọn **DataPipeline-Orchestrator**.
4. Mở rộng phần **Additional settings**

![3.4.14](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.14.svg)

Tại mục **Configure target input**, chọn **Input transformer** -> Nhấn **Configure input transformer**.

![3.4.7](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.7.svg)

5. **Phần 1: Input Path** - Copy và paste đoạn JSON sau:

```json
{
  "pipelineName": "$.detail.stateMachineArn",
  "executionArn": "$.detail.executionArn",
  "status": "$.detail.status"
}

```

![3.4.8](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.8.svg)

6. **Phần 2: Template** - Copy và paste đoạn text sau:

{{% notice warning %}}
**CẢNH BÁO QUAN TRỌNG:** Toàn bộ đoạn văn bản này **BẮT BUỘC PHẢI ĐƯỢC BAO BỌC BỞI CẶP DẤU NGOẶC KÉP `" "**`.
{{% /notice %}}

```text
"CẢNH BÁO: Tiến trình Step Functions Data Pipeline đã thất bại! \n\n- State Machine: <pipelineName>\n- ID Thực thi: <executionArn>\n- Trạng thái: <status>\n\nVui lòng kiểm tra lại log trên AWS Step Functions Console để xác định Glue Job nào gặp sự cố."

```

![3.4.9](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.9.svg)

7. Nhấn **Confirm** -> **Next** -> Bỏ qua Tags -> Nhấn **Create rule**.

![3.4.15](/images/Workshop/3-Monitoring&Security/3.4-AWS_EventBridge_(CloudWatch)/3.4.15.svg)

8. Nhấn **Next** -> Bỏ qua Tags -> Nhấn **Create rule**.

### Hoàn tất!

Hệ thống Data Pipeline của bạn giờ đây đã hoàn toàn tự động hóa. Chỉ cần upload một file dữ liệu lên S3, Step Functions sẽ tự động chạy toàn bộ quy trình ETL. Đồng thời, bất kỳ lỗi nào xuất hiện trong chuỗi hệ thống đều sẽ được thu thập và báo cáo đẹp mắt về hòm thư của bạn.

