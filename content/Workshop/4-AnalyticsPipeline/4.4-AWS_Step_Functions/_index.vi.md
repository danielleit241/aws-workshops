---
title: "Thiết lập AWS Step Functions (State Machine) Điều phối Pipeline"
date: "2026-05-02"
weight: 4
chapter: false
pre: " <b> 4. </b> "
---

### Mục tiêu

Xây dựng một "nhạc trưởng" (Orchestrator) sử dụng **AWS Step Functions** để tự động hóa toàn bộ chuỗi công việc. State Machine này sẽ thực hiện logic tuần tự:

1. Gọi **AWS Glue Crawler** để cập nhật schema mới nhất từ S3.
2. Liên tục kiểm tra trạng thái (Polling) xem Crawler đã chạy xong chưa.
3. Khi Crawler hoàn tất thành công, tự động kích hoạt tiến trình **AWS Glue ETL Job** để xử lý dữ liệu.

### Trình bày Logic kiến trúc

Không giống như Glue Job có hỗ trợ tích hợp chờ đồng bộ (`.sync`), API của Glue Crawler là bất đồng bộ (Asynchronous). Nghĩa là khi ta bấm "Start", nó sẽ trả về kết quả ngay lập tức dù Crawler vẫn đang chạy ngầm. Do đó, State Machine của chúng ta cần một vòng lặp (Loop) kiểm tra trạng thái:

* **Start Crawler:** Ra lệnh khởi động Crawler.
* **Wait:** Tạm nghỉ 30 giây để tránh gọi API quá nhiều lần gây lỗi (Throttling).
* **Get Crawler Status:** Lấy trạng thái hiện tại của Crawler.
* **Choice (Check Status):** Kiểm tra trạng thái.
* Nếu đang `RUNNING` hoặc `STOPPING` -> Quay lại bước **Wait**.
* Nếu đã hoàn thành (`READY`) -> Chuyển sang bước tiếp theo.
* **Run ETL Job:** Kích hoạt Glue Job với hậu tố `.sync`. Lúc này Step Functions sẽ tự động chờ cho đến khi Job chạy xong. Nếu Job lỗi, toàn bộ State Machine sẽ báo **FAILED** (và kích hoạt EventBridge Rule cảnh báo qua SNS mà chúng ta thiết lập ở phần sau).

### Các bước Cấu hình Chi tiết AWS Step Functions

**Bước 1: Truy cập AWS Step Functions**

Tại thanh tìm kiếm của AWS Console, gõ và chọn dịch vụ **Step Functions**.

![4.4.1](/images/Workshop/4.Glue/4.4.AWS_Step_Functions/4.4.1.svg)

**Bước 2: Khởi tạo State Machine**

1. Nhấn nút **Create state machine**.

![4.4.2](/images/Workshop/4.Glue/4.4.AWS_Step_Functions/4.4.2.svg)

2. Ở màn hình Create state machine
* Chọn **Create from blank** (Mẫu trống)
* **State machine name:** Nhập `DataPipeline-Orchestrator`.
* **Type:** Giữ nguyên **Standard**.
* Nhấn **Continue**

![4.4.3](/images/Workshop/4.Glue/4.4.AWS_Step_Functions/4.4.3.svg)

**Bước 3: Cấu hình Logic bằng mã ASL (Amazon States Language)**

Thay vì phải kéo thả thủ công từng khối hộp trong Workflow Studio, bạn có thể thiết lập toàn bộ quy trình chỉ trong vài giây bằng cách dán mã nguồn.

1. Tại giao diện Workflow Studio, nhìn lên góc trên cùng bên trái, chuyển từ tab **Design** sang tab **Code**.
2. Xóa toàn bộ đoạn code mặc định có sẵn trong ô.
3. Copy và dán đoạn mã JSON dưới đây vào:

```json
{
  "Comment": "Data Pipeline: Crawler -> Check Status -> ETL Job",
  "StartAt": "Start Crawler",
  "States": {
    "Start Crawler": {
      "Type": "Task",
      "Parameters": {
        "Name": "TEN_CRAWLER_CUA_BAN"
      },
      "Resource": "arn:aws:states:::aws-sdk:glue:startCrawler",
      "Next": "Wait 30s"
    },
    "Wait 30s": {
      "Type": "Wait",
      "Seconds": 30,
      "Next": "Get Crawler Status"
    },
    "Get Crawler Status": {
      "Type": "Task",
      "Parameters": {
        "Name": "TEN_CRAWLER_CUA_BAN"
      },
      "Resource": "arn:aws:states:::aws-sdk:glue:getCrawler",
      "Next": "Check Crawler State"
    },
    "Check Crawler State": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.Crawler.State",
          "StringEquals": "RUNNING",
          "Next": "Wait 30s"
        },
        {
          "Variable": "$.Crawler.State",
          "StringEquals": "STOPPING",
          "Next": "Wait 30s"
        }
      ],
      "Default": "Run ETL Job"
    },
    "Run ETL Job": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun.sync",
      "Parameters": {
        "JobName": "TEN_GLUE_JOB_CUA_BAN"
      },
      "End": true
    }
  }
}

```

{{% notice warning %}}
**CẬP NHẬT THÔNG TIN:** Bạn **BẮT BUỘC** phải tìm và thay thế các chuỗi `TEN_CRAWLER_CUA_BAN` (ở 2 vị trí) và `TEN_GLUE_JOB_CUA_BAN` (ở 1 vị trí) trong đoạn mã trên bằng đúng tên Crawler và ETL Job mà bạn đã tạo ở phần 4.1 và 4.3.
{{% /notice %}}

{{% notice note %}}
TEN_CRAWLER_CUA_BAN: `glue_crawler_data`
TEN_GLUE_JOB_CUA_BAN: `glue_etl_job_taxi`
{{% /notice %}}

4. Nhấn **Create**

![4.4.4](/images/Workshop/4.Glue/4.4.AWS_Step_Functions/4.4.4.svg)

5. Ở phần **Confirm role creation** -> Nhấn **Confirm**

![4.4.5](/images/Workshop/4.Glue/4.4.AWS_Step_Functions/4.4.5.svg)

**Bước 4: Kiểm tra State machine successfully created**

![4.4.6](/images/Workshop/4.Glue/4.4.AWS_Step_Functions/4.4.6.svg)


### Hoàn tất!

Tuyệt vời! Bạn đã có một bộ máy điều phối (State Machine) hoàn chỉnh. Nó sẽ thay con người thực hiện việc kích hoạt Crawler, ngồi kiên nhẫn chờ đợi, và ngay khi dữ liệu sẵn sàng, nó sẽ gọi Glue ETL Job.

Bây giờ, bạn đã có sẵn "Target" (State Machine) này trong tài khoản. Hãy quay lại **Bước 4.4.2** để hoàn tất việc kết nối tự động hóa EventBridge Rules từ phần trước!