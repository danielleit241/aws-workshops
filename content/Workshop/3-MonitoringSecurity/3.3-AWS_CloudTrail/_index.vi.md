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

![3.2.1](/images/Workshop/3-Monitoring&Security/3.2.1.svg)


Nhấn chọn **Create trail** 

{{% notice warning %}}
Chọn **Create trail** -> không phải **Create a trail** (Tránh nhầm với tính năng Quick Create)
{{% /notice %}}


![3.2.2](/images/Workshop/3-Monitoring&Security/3.2.2.svg)


**Bước 2: Cấu hình CloudTrail**

- **Trail name:** Nhập `DataPipeline-Audit-Trail`
- **Storage location:** Chọn **Create new S3 bucket**. 
- **Trail log bucket and folder:** Nhập: `aws-workshop-audit-logs-glue`

![3.2.3](/images/Workshop/3-Monitoring&Security/3.2.3.svg)

- Ở phần **CloudWatch Logs**, check vào ô **Enabled** (Tùy chọn này đưa logs lên bảng điều khiển CloudWatch để dễ dàng query).
- **Log group:** Để tên như mặc định
- **IAM Role:** Chọn New để AWS tự động tạo Role cấp quyền ghi log.
- Nhấn **Next**. Giữ nguyên cấu hình ghi log các Management events

![3.2.4](/images/Workshop/3-Monitoring&Security/3.2.4.svg)

- Nhấn **Next** thêm lần nữa -> Create trail.

