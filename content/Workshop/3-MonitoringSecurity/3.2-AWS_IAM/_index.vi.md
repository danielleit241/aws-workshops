---
title: "Tạo IAM Role cho AWS Glue"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

### Các bước cấu hình IAM cho AWS Glue

Trong phần này, chúng ta sẽ tạo IAM service role để AWS Glue sử dụng cho cả **Crawler** và **ETL Job** trong workshop.

Role này cho phép Glue:

- đọc dữ liệu đầu vào từ Amazon S3
- ghi dữ liệu đã xử lý trở lại Amazon S3
- ghi log vào Amazon CloudWatch Logs
- truy cập AWS Glue Data Catalog trong quá trình crawler và job chạy

Chúng ta sẽ tạo một role dùng chung cho workshop:

- **Tên role:** `glue-role-manhattan-workshop`

{{% notice info %}}
Trang này chỉ tập trung vào **Glue service role** dùng cho crawler và ETL job.  
Nó khác với IAM role sẽ được gắn cho Amazon Redshift Serverless ở các phần sau.
{{% /notice %}}

**Bước 1: Mở IAM Console**

Tại thanh tìm kiếm trong AWS Management Console, hãy mở **IAM**.

Sau đó chọn **Roles** ở menu bên trái và nhấn **Create role**.

**Bước 2: Chọn AWS Service làm Trusted Entity**

Tại bước chọn trusted entity:

- **Trusted entity type:** `AWS service`
- **Service or use case:** `Glue`

Trust relationship này cho phép AWS Glue assume role trong lúc chạy.

Nhấn **Next**.

**Bước 3: Gắn Managed Policy cơ bản cho Glue**

Tìm và gắn managed policy:

- `AWSGlueServiceRole`

Policy này cung cấp các quyền cơ bản để Glue chạy crawler, ETL job và các thao tác liên quan.

Sau khi chọn xong, nhấn **Next**.

**Bước 4: Thêm quyền truy cập S3 cho dữ liệu workshop**

Glue cũng cần quyền truy cập các S3 bucket được sử dụng trong workshop này.

Trong môi trường workshop, có hai cách:

- **Option A — Thiết lập nhanh cho workshop:** `AmazonS3FullAccess`
- **Option B — An toàn hơn:** tạo custom policy chỉ giới hạn trong các workshop bucket

Nếu bạn muốn đi theo luồng workshop nhanh nhất, hãy gắn:

- `AmazonS3FullAccess`

Nếu tài khoản AWS của bạn yêu cầu policy hẹp hơn, hãy tạo customer-managed policy tương tự như ví dụ sau rồi gắn vào cùng role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::your-raw-bucket",
        "arn:aws:s3:::your-processed-bucket",
        "arn:aws:s3:::your-script-bucket"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::your-raw-bucket/*",
        "arn:aws:s3:::your-processed-bucket/*",
        "arn:aws:s3:::your-script-bucket/*"
      ]
    }
  ]
}
```

Trong workshop này, role nên truy cập được:

- vị trí **raw data**
- vị trí **processed data**
- vị trí **ETL script** nếu script Glue job được lưu trên S3
- thư mục **temporary directory** dùng cho Glue job

**Bước 5: Review và đặt tên Role**

Tại màn hình review cuối cùng:

- **Role name:** `glue-role-manhattan-workshop`

Bạn có thể thêm mô tả như:

`Service role for AWS Glue crawler and ETL job in the Manhattan DataWay workshop`

Sau đó nhấn **Create role**.

**Bước 6: Kiểm tra Trust Relationship**

Mở role vừa tạo và xác nhận trust relationship cho phép Glue assume role.

Nó cần tham chiếu tới:

- `glue.amazonaws.com`

Nếu bạn mở tab **Trust relationships**, nội dung sẽ tương tự:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Bước 7: Sử dụng role trong AWS Glue**

Ở các phần sau của workshop, hãy tái sử dụng role này cho:

- **AWS Glue Crawler** — quét dữ liệu trong S3 và cập nhật Data Catalog
- **AWS Glue ETL Job** — đọc raw data, biến đổi và ghi ra processed data

Khi tạo các tài nguyên đó, hãy chọn:

- `glue-role-manhattan-workshop`

**Bước 8: Checklist xác minh nhanh**

Trước khi chuyển tiếp, hãy kiểm tra:

- role đã tồn tại trong IAM
- trusted service là **AWS Glue**
- `AWSGlueServiceRole` đã được gắn
- quyền S3 đã được gắn cho các workshop bucket
- bạn có thể chọn role này trong màn hình cấu hình Glue Crawler và Glue Job

{{% notice tip %}}
Nếu Glue bị lỗi **AccessDenied** ở các bước sau, nguyên nhân thường là do thiếu quyền S3 trên role, không phải do cấu hình Glue.
{{% /notice %}}

### Tổng kết

Trong phần này, bạn đã tạo IAM service role cần thiết cho AWS Glue.

Role này sẽ được tái sử dụng ở các bước tiếp theo để Glue có thể:

- crawl schema từ dữ liệu trên S3
- chạy ETL transformation
- ghi log lên CloudWatch
- làm việc với Glue Data Catalog
