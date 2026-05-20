---
title: "Khái niệm cốt lõi của Redshift Serverless"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 2.1. </b> "
---

## Namespace là gì?

Namespace chứa tất cả các thành phần thuộc về database:

- Database objects (schemas, tables, views)
- Users và permissions
- IAM roles
- Data warehouse metadata
- Encryption settings

Trong trường hợp này, namespace "manhattan-redshift-namespace" chứa database "dev".

## Workgroup là gì?

Workgroup là phần compute để chạy queries:

- Base capacity (RPU - Redshift Processing Units)
- Endpoint để connect
- VPC/subnet/security group
- Query monitoring
- Cost/performance controls

Workgroup "manhattan-redshift-workgroup" có base capacity 4 RPU và endpoint để Query Editor v2 connect.

## Sự khác biệt

- **Namespace**: Phần "storage/metadata" của database
- **Workgroup**: Phần "compute/query engine"

Chúng ta tách biệt để quản lý storage và compute độc lập.

# Capacity và RPU

## RPU là gì?

RPU (Redshift Processing Unit) là đơn vị đo lường sức mạnh compute của Redshift Serverless. Bao gồm CPU, memory, network và processing power cho queries.

## Mức capacity

- 4 RPU: Thấp nhất, phù hợp test/query nhẹ
- 8 RPU: Trung bình, thoải mái hơn
- 16-32 RPU: Query nhiều dữ liệu
- 128 RPU: Mặc định, mạnh nhưng tốn kém

Chúng ta chọn 4 RPU vì chỉ query thử nghiệm trên dữ liệu taxi ~ vài trăm MB.

## Chi phí

Redshift Serverless tính phí theo RPU-hours sử dụng. Capacity càng cao thì chi phí càng tăng nếu query nặng. Với hand-on, 4 RPU giúp tiết kiệm.

# IAM Role

Redshift cần IAM role để:

- Đọc dữ liệu từ S3 buckets (yellow-taxi-trip-demo-fcaj, processed-yellow-taxi-trip-data)
- Truy cập Glue Data Catalog
- Thực hiện các operations như COPY, UNLOAD

Role được tạo với quyền AmazonS3ReadOnlyAccess và AWSGlueServiceRole để đọc S3 và Glue.

# Free Trial

Redshift Serverless có $300 credit free trial trong 90 ngày cho tài khoản mới. Đây là credit riêng biệt với AWS Free Tier $200.

Chúng ta sử dụng credit này để tránh chi phí phát sinh trong quá trình học tập.
