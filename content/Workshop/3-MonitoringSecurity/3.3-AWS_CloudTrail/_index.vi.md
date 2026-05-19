---
title: "Ghi vết Hệ thống với AWS CloudTrail"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

### Các bước cấu hình AWS CloudTrail

Chúng ta sẽ thực hiện một bài kiểm tra nhanh (Test Run) để đảm bảo tài khoản của bạn đã sẵn sàng. Và thực hiện các bước set-up cho AWS CloudTrail. 

**Bước 1: Truy cập AWS Console**

Đầu tiên ở thanh tìm kiếm, truy cập vào [AWS CloudTrail Console](https://console.aws.amazon.com/cloudtrailv2/home)

![3.3.1](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.1.svg)


Nhấn chọn **Create trail** 

{{% notice warning %}}
Chọn **Create trail** -> không phải **Create a trail** (Tránh nhầm với tính năng Quick Create)
{{% /notice %}}


![3.3.2](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.2.svg)


**Bước 2: Cấu hình CloudTrail**

- **Trail name:** Nhập `DataPipeline-Audit-Trail`
- **Storage location:** Chọn **Create new S3 bucket**. 
- **Trail log bucket and folder:** Nhập: `aws-workshop-audit-logs-glue`
- **Log file SSE-KMS encryption:** Tắt Enable


![3.3.3](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.3.svg)

- Ở phần **CloudWatch Logs**, check vào ô **Enabled** (Tùy chọn này đưa logs lên bảng điều khiển CloudWatch để dễ dàng query).
- **Log group:** Để tên như mặc định
- **IAM Role:** Chọn New để AWS tự động tạo Role cấp quyền ghi log.
- Nhấn **Next**. 

![3.3.4](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.4.svg)

- Giữ nguyên cấu hình ghi log các **Management events**
- Nhấn **Next** thêm lần nữa

![3.3.5](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.5.svg)

- Nhấn **Create trail**.

![3.3.6](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.6.svg)

- Kiểm tra Trail đã được tạo **Successfully**
- Và **Status** ở trạng thái **Logging**

![3.3.7](/images/Workshop/3-Monitoring&Security/3.3-AWS_CloudTrail/3.3.7.svg)

**Chúc mừng bạn đã hoàn thành bước setup AWS CloudTrail.**
