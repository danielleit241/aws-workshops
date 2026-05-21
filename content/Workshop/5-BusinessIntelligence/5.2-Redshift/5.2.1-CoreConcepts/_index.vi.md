---
title: "Các khái niệm cốt lõi của Redshift Serverless"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 2.1. </b> "
---
## Namespace là gì?

Một namespace chứa toàn bộ các thành phần liên quan đến cơ sở dữ liệu:

- Đối tượng cơ sở dữ liệu (schema, table, view)
- Người dùng và quyền truy cập
- IAM role
- Metadata của data warehouse
- Thiết lập mã hóa

Trong trường hợp của chúng ta, `manhattan-redshift-namespace` chứa cơ sở dữ liệu `dev`.

## Workgroup là gì?

Một workgroup là phần compute dùng để chạy truy vấn:

- Base capacity (RPU - Redshift Processing Units)
- Endpoint để kết nối
- VPC/subnet/security group
- Giám sát truy vấn
- Kiểm soát chi phí/hiệu năng

`manhattan-redshift-workgroup` có 4 base RPU và một endpoint để kết nối từ Query Editor v2.

## Sự khác nhau

- **Namespace**: Phần “lưu trữ/metadata” của cơ sở dữ liệu
- **Workgroup**: Phần “compute/query engine”

Hai phần này được tách riêng để có thể quản lý lưu trữ và compute một cách độc lập.

# Capacity và RPU

## RPU là gì?

RPU (Redshift Processing Unit) đo năng lực compute của Redshift Serverless, bao gồm CPU, bộ nhớ, mạng, và khả năng xử lý truy vấn.

## Các mức capacity

- 4 RPU: Mức tối thiểu, phù hợp cho kiểm thử/truy vấn nhẹ
- 8 RPU: Mức trung bình, thoải mái hơn
- 16-32 RPU: Dành cho truy vấn dữ liệu lớn hơn
- 128 RPU: Mặc định, mạnh nhưng tốn kém

Chúng ta chọn 4 RPU vì chỉ kiểm thử truy vấn trên dữ liệu taxi (~vài trăm MB).

## Chi phí

Redshift Serverless tính phí dựa trên số RPU-giờ sử dụng. Capacity càng cao thì chi phí cho các truy vấn nặng càng lớn. Với phần thực hành, 4 RPU giúp tiết kiệm chi phí.

# IAM Role

Redshift cần một IAM role để:

- Đọc dữ liệu từ các bucket S3 (`yellow-taxi-trip-demo-fcaj`, `processed-yellow-taxi-trip-data`)
- Truy cập Glue Data Catalog
- Thực hiện các thao tác như COPY, UNLOAD

Role này được tạo với quyền `AmazonS3ReadOnlyAccess` và `AWSGlueServiceRole` để đọc S3 và Glue.

# Free Trial

Redshift Serverless có khoản credit dùng thử miễn phí trị giá $300 trong 90 ngày cho tài khoản mới. Khoản này tách biệt với AWS Free Tier $200.

Chúng ta dùng credit này để tránh phát sinh chi phí trong quá trình học.
