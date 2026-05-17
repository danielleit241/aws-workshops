---
title: "Ghi vết Hệ thống với AWS CloudTrail"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3.3 </b> "
---

Lưu nhật ký bảo mật xem ai đã chỉnh sửa các tác vụ trên AWS Management Console.

### Các bước cấu hình AWS CloudTrail


**Step 1: Access the AWS Console**

Đầu tiên ở thanh tìm kiếm, truy cập vào [AWS CloudTrail Console](https://console.aws.amazon.com/cloudtrailv2/home)

![3.2.1](/images/Workshop/3-Monitoring&Security/3.2.1.svg)




Lưu nhật ký bảo mật xem ai đã chỉnh sửa các tác vụ trên AWS Management Console.

Truy cập AWS CloudTrail Console.

Nhấn chọn Create trail (Tránh nhầm với tính năng Quick Create).

Trail name: Nhập DataPipeline-Audit-Trail.

Storage location: Chọn Create new S3 bucket. Đặt tên bucket duy nhất (VD: aws-workshop-audit-logs-[tên-của-bạn]).

Ở phần CloudWatch Logs, check vào ô Enabled (Tùy chọn này đưa logs lên bảng điều khiển CloudWatch để dễ dàng query).

Log group: Để mặc định hoặc đặt DataPipeline/CloudTrail.

IAM Role: Chọn New để AWS tự động tạo Role cấp quyền ghi log.

Nhấn Next. Giữ nguyên cấu hình ghi log các Management events và nhấn Next -> Create trail.