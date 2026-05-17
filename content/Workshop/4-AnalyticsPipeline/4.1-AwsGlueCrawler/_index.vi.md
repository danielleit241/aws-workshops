---
title: "AWS Glue Crawler"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---
## Tổng quan
Trong phần này, chúng ta sẽ cấu hình AWS Glue Crawler để tự động quét dữ liệu từ Amazon S3, phát hiện schema và tạo các bảng metadata trong AWS Glue Data Catalog.

Sau khi hoàn thành phiên này, bạn sẽ có thể:
- Tạo Glue Database trong Data Catalog
- Tạo IAM Role cho Glue Crawler
- Cấu hình nguồn dữ liệu S3 cho Crawler
- Cấu hình database đầu ra và tiền tố bảng
- Tạo và chạy Glue Crawler
- Xác minh bảng được tạo trong Glue Data Catalog

### Kiến trúc tổng quan
![overview](/images/Workshop/4.Glue/4.1.Crawler/diagram-architecture.jpg)

Kiến trúc của bài lab này được thiết kế để minh họa một mô hình khám phá dữ liệu phổ biến trên AWS.

Dữ liệu thô được lưu trữ trong Amazon S3 dưới định dạng Parquet. AWS Glue Crawler quét nguồn dữ liệu, xác định cấu trúc file, phát hiện schema và tạo các bảng metadata bên trong AWS Glue Data Catalog. Sau khi metadata đã có sẵn, AWS Glue ETL Job có thể sử dụng thông tin catalog đó để đọc, chuyển đổi và ghi dữ liệu đã xử lý trở lại Amazon S3.

>Quan trọng: AWS Glue Crawler không di chuyển hoặc sao chép dữ liệu của bạn vào Data Catalog.
>Dữ liệu thực tế vẫn nằm trong Amazon S3. Data Catalog chỉ lưu trữ metadata như tên bảng, schema, kiểu dữ liệu của cột, partition và vị trí S3.

Luồng hoạt động đơn giản hóa là:
![workflow](/images/Workshop/4.Glue/4.1.Crawler/aws-glue-crawler-etl-flow.png)

