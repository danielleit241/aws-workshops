---
title: "Thiết lập Redshift Serverless"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2.2. </b> "
---

Để sử dụng Redshift Spectrum, chúng ta cần tạo một Redshift Serverless environment. Redshift Serverless là lựa chọn phù hợp cho việc query dữ liệu từ S3/Glue mà không cần quản lý infrastructure.

## Bước 1: Truy cập Redshift Console

1. Vào Amazon Redshift console
2. Ở dashboard, chúng ta sẽ thấy không có namespace/workgroup nào

![Redshift Serverless Dashboard](/images/manhattan-dataways/redshift-spectrum/01-existing-glue-stack-overview.png)

3. Click "Create workgroup"

## Bước 2: Tùy chỉnh cấu hình

Trong màn hình "Get started with Amazon Redshift Serverless", click "Customize settings" để cấu hình chi tiết thay vì dùng mặc định.

![Màn hình Get started với tùy chỉnh](/images/manhattan-dataways/redshift-spectrum/02-redshift-get-started-customize.png)

### Cấu hình Namespace

- **Namespace name**: manhattan-redshift-namespace
- **Database name**: dev
- **Admin credentials**: Created based on IAM credentials (dùng IAM user hiện tại)

### Cấu hình Workgroup

- **Workgroup name**: manhattan-redshift-workgroup

### Capacity và Cost Controls

Giảm Base capacity từ 128 xuống 4 RPU để tiết kiệm chi phí cho hand-on.

![Giảm capacity từ 128 xuống 4](/images/manhattan-dataways/redshift-spectrum/03-redshift-capacity-128-to-4.png)

### IAM Role

Tạo IAM role mới để Redshift có quyền đọc S3 và Glue:

1. Chọn "Create IAM role"
2. Chọn buckets: yellow-taxi-trip-demo-fcaj, processed-yellow-taxi-trip-data, quarantine-yellow-taxi-trip-data
3. Set default role

![Workgroup và IAM role](/images/manhattan-dataways/redshift-spectrum/04-redshift-workgroup-iam-default.png)

### Network and Security

- VPC: default VPC
- Publicly accessible: No (cho security)
- SSL: Enable

## Bước 3: Tạo và chờ Available

Click "Save configuration". AWS sẽ tạo namespace và workgroup.

Chờ đến khi workgroup status chuyển thành "Available".

![Workgroup đã available](/images/manhattan-dataways/redshift-spectrum/05-redshift-workgroup-available.png)

## Lý do cấu hình này

- Capacity 4 RPU đủ cho query thử nghiệm mà không tốn kém
- IAM role có quyền đọc S3/Glue cần thiết
- Không bật public access để đảm bảo security
