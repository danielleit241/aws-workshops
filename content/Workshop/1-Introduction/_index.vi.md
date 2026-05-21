---
title: "Introduction"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---
Workshop này sẽ sử dụng các AWS resources và công cụ sau:

**Amazon S3:**  
Amazon Simple Storage Service (S3) được sử dụng làm nền tảng Data Lake cho toàn bộ hệ thống. S3 lưu trữ dữ liệu Yellow Taxi ở nhiều giai đoạn khác nhau bao gồm dữ liệu thô (Raw Data), dữ liệu đã xử lý (Processed Data), và dữ liệu lỗi hoặc bất thường (Quarantine Data). Ngoài ra, S3 còn đóng vai trò là nguồn dữ liệu cho Athena, Redshift và Glue ETL Job.

**AWS Step Functions:**  
AWS Step Functions được sử dụng để điều phối toàn bộ workflow xử lý dữ liệu. Dịch vụ này giúp tổ chức các bước ETL theo dạng State Machine, đảm bảo pipeline có thể chạy tuần tự, dễ theo dõi và dễ mở rộng khi hệ thống phát triển thêm các bước xử lý mới.

**AWS Glue Crawler và AWS Glue Data Catalog:**  
AWS Glue Crawler được sử dụng để tự động quét dữ liệu trong Amazon S3 nhằm phát hiện schema và metadata của dataset. Metadata sau đó được lưu vào AWS Glue Data Catalog để phục vụ cho ETL processing và các dịch vụ truy vấn dữ liệu như Amazon Athena.

**AWS Glue ETL Job:**  
AWS Glue ETL Job sử dụng Apache Spark và PySpark Script để xử lý dữ liệu quy mô lớn. Pipeline ETL sẽ thực hiện:
- Data Cleaning
- Missing Value Handling
- Financial Data Standardization
- Feature Engineering
- Rule-based Data Validation
- Partition-based Data Processing

Dữ liệu sau xử lý sẽ được ghi trở lại Amazon S3 dưới định dạng Parquet.

**Amazon Athena:**  
Amazon Athena được sử dụng để truy vấn trực tiếp dữ liệu đã xử lý trên Amazon S3 bằng SQL tiêu chuẩn mà không cần xây dựng hạ tầng riêng. Athena hỗ trợ exploratory analysis và ad-hoc query trên các dataset partitioned trong Data Lake.

**Amazon Redshift:**  
Amazon Redshift đóng vai trò là Data Warehouse phục vụ OLAP và analytical workloads. Dữ liệu đã xử lý từ S3 sẽ được load vào Redshift để tối ưu hiệu năng truy vấn và phục vụ các dashboard business intelligence.

**Amazon QuickSight:**  
Amazon QuickSight là dịch vụ business intelligence trên cloud được sử dụng để trực quan hóa dữ liệu thông qua dashboard và biểu đồ phân tích. QuickSight kết nối với Redshift để hiển thị:
- Trip Demand Analysis
- Revenue Analysis
- Vendor Performance
- Spatial Analysis

**IAM, CloudTrail, CloudWatch và SNS:**  
AWS Identity and Access Management (IAM) được sử dụng để kiểm soát quyền truy cập giữa các dịch vụ AWS trong hệ thống.

AWS CloudTrail ghi lại toàn bộ hoạt động API và thao tác trên tài nguyên AWS nhằm phục vụ audit và security tracking.

Amazon CloudWatch được sử dụng để giám sát ETL Jobs, Glue Logs và trạng thái workflow.

Amazon SNS hỗ trợ gửi cảnh báo khi pipeline thất bại hoặc phát sinh lỗi trong quá trình xử lý dữ liệu.

> **Lưu ý:** Việc sử dụng Amazon EventBridge kết hợp với CloudWatch là tùy chọn (optional). Nếu hệ thống không yêu cầu cơ chế event-driven hoặc event routing phức tạp, CloudWatch vẫn có thể được sử dụng độc lập để monitoring, logging và alerting như thông thường.