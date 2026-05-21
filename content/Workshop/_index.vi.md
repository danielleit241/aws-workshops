---
title: "Quy trình dữ liệu với AWS Glue"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
## Nội dung

### Tóm tắt dự án (Executive Summary)

- Tóm tắt:  
Dự án này nhằm xây dựng một hệ thống xử lý và phân tích dữ liệu tự động (Data Analytics Pipeline) trên nền tảng Amazon Web Services (AWS) theo kiến trúc Data Lakehouse. Hệ thống được thiết kế để xử lý tập dữ liệu lớn về hồ sơ chuyến đi taxi New York Yellow Taxi thông qua quy trình ingest, metadata management, ETL processing, data warehousing và visualization.

- Mục tiêu:
  - Xây dựng hệ thống Data Lake trên Amazon S3.
  - Tự động hóa quy trình ETL và xử lý dữ liệu.
  - Tự động quản lý schema và metadata.
  - Làm sạch và chuẩn hóa dữ liệu trước khi phân tích.
  - Hỗ trợ truy vấn dữ liệu trực tiếp trên S3 bằng Athena.
  - Xây dựng Data Warehouse phục vụ OLAP trên Amazon Redshift.
  - Xây dựng Dashboard trực quan hóa dữ liệu bằng Amazon QuickSight.
  - Thiết lập hệ thống monitoring và security cho pipeline.

- Phạm vi:
  - Xây dựng Data Lake trên Amazon S3.
  - Triển khai workflow xử lý dữ liệu bằng AWS Step Functions.
  - Sử dụng AWS Glue Crawler, Glue Data Catalog và Glue ETL Job cho metadata management và ETL.
  - Tích hợp Amazon Athena, Amazon Redshift và Amazon QuickSight phục vụ phân tích dữ liệu.
  - Thiết lập hệ thống Monitoring & Security bằng IAM, CloudTrail, CloudWatch và SNS.

### Tuyên bố vấn đề (Problem Statement)

Vấn đề hiện tại (Current Challenges): Tập dữ liệu Yellow Taxi chứa khối lượng dữ liệu lớn và tăng trưởng liên tục theo thời gian. Tuy nhiên dữ liệu ở trạng thái thô tồn tại nhiều vấn đề ảnh hưởng đến chất lượng phân tích:

- Xuất hiện dữ liệu thiếu hoặc không hợp lệ:
  - `passenger_count = null`
  - `trip_distance = 0`
  - `fare_amount < 0`
- Dữ liệu chưa được chuẩn hóa schema.
- Khó khăn trong việc xử lý dữ liệu thủ công với dữ liệu có kích thước lớn.
- Thiếu cơ chế ETL tự động và metadata management.
- Truy vấn trực tiếp trên dữ liệu thô có hiệu năng thấp.
- Chưa có hệ thống tập trung phục vụ analytical workloads và visualization.

Giải pháp kỹ thuật (Technical Solution): Triển khai kiến trúc Data Lakehouse trên AWS:

- Dữ liệu đầu vào được lưu tại Amazon S3 Raw Bucket.
- AWS Step Functions điều phối workflow xử lý dữ liệu.
- AWS Glue Crawler quét dữ liệu từ S3 Raw Bucket để phát hiện schema và metadata.
- AWS Glue Data Catalog lưu trữ metadata phục vụ ETL processing và query engine.
- AWS Glue ETL Job thực hiện:
  - Data Cleaning
  - Data Transformation
  - Schema Standardization
  - Feature Engineering
- Dữ liệu sau xử lý được lưu tại S3 Processed Bucket dưới định dạng Parquet.
- Amazon Athena hỗ trợ truy vấn trực tiếp trên S3 Processed Data.
- Amazon Redshift phục vụ phân tích OLAP.
- Amazon QuickSight trực quan hóa dữ liệu thông qua Dashboard.

### Kiến trúc giải pháp (Solution Architecture)

![overview](/images/Workshop/Architecture/Architecutre_final.png)

Kiến trúc hệ thống đi theo luồng xử lý:

Raw &rarr; Metadata & ETL Processing &rarr; Analytics &rarr; Visualization.

**Kiến trúc Kỹ thuật (Workflow Overview):**

- Ingestion: Dữ liệu đầu vào (CSV/Parquet) được upload vào Amazon S3 Raw Bucket.
- Schema Crawling: AWS Glue Crawler quét dữ liệu từ S3 Raw Bucket để phát hiện schema và metadata.
- Metadata Management: AWS Glue Data Catalog lưu trữ metadata phục vụ ETL processing và analytical query engine.
- ETL Processing: AWS Glue ETL Job thực hiện:
  - Làm sạch dữ liệu
  - Chuẩn hóa kiểu dữ liệu
  - Xử lý missing values
  - Loại bỏ dữ liệu bất thường
  - Feature Engineering
- Processed Storage: Dữ liệu sau xử lý được lưu tại Amazon S3 Processed Bucket dưới định dạng Parquet.
- Data Warehousing: Amazon Redshift nạp dữ liệu từ S3 Processed Bucket phục vụ OLAP và analytical workloads.
- Visualization: Amazon QuickSight kết nối với Amazon Redshift để xây dựng Dashboard trực quan hóa dữ liệu.
- Ad-hoc Query: Amazon Athena hỗ trợ truy vấn SQL trực tiếp trên dữ liệu tại S3 Processed Bucket.

**Technology Stack:**

| Lớp (Layer)           | Dịch vụ AWS                                | Mục đích / Vai trò                                      |
| --------------------- | ------------------------------------------ | ------------------------------------------------------- |
| Storage / Data Lake   | Amazon S3                                  | Lưu trữ Raw Data và Processed Data                      |
| Workflow Orchestration| AWS Step Functions                         | Điều phối pipeline xử lý dữ liệu                        |
| Metadata Management   | AWS Glue Crawler, AWS Glue Data Catalog    | Quản lý schema và metadata                              |
| Data Processing (ETL) | AWS Glue ETL Job                           | ETL và Data Transformation                              |
| Query Engine          | Amazon Athena                              | Truy vấn SQL trực tiếp trên S3                          |
| Data Warehouse        | Amazon Redshift                            | Kho dữ liệu phục vụ OLAP                                |
| BI / Visualization    | Amazon QuickSight                          | Dashboard và báo cáo                                    |
| Security & Monitoring | IAM, CloudTrail, CloudWatch, SNS           | Monitoring, logging và alerting                         |

### Luồng đi của dự án (Workflow Overview)

- Bước 1 — Data Ingestion:
  - Dữ liệu đầu vào được upload vào Amazon S3 Raw Bucket.

- Bước 2 — Schema Crawling:
  - AWS Glue Crawler quét dữ liệu để phát hiện schema và metadata.

- Bước 3 — Metadata Management:
  - AWS Glue Data Catalog lưu trữ metadata phục vụ ETL và query engine.

- Bước 4 — ETL Processing:
  - AWS Glue ETL Job thực hiện:
    - Data Cleaning
    - Schema Transformation
    - Missing Value Handling
    - Outlier Removal
    - Feature Engineering

- Bước 5 — Processed Storage:
  - Dữ liệu sau xử lý được lưu tại Amazon S3 Processed Bucket dưới định dạng Parquet.

- Bước 6 — Data Warehousing:
  - Amazon Redshift nạp dữ liệu từ S3 Processed Bucket phục vụ analytical workloads.

- Bước 7 — Visualization:
  - Amazon QuickSight kết nối với Redshift để xây dựng Dashboard trực quan hóa dữ liệu.

- Bước 8 — Ad-hoc Query:
  - Amazon Athena hỗ trợ truy vấn SQL trực tiếp trên S3 Processed Data.

### Ước lượng chi phí (Cost Estimation Model)

Hệ thống sử dụng mô hình Pay-as-you-go nhằm tối ưu chi phí vận hành.

Region triển khai dự kiến:
- `us-east-2`

Cơ cấu chi phí dự kiến phân bổ như sau:

| Dịch vụ AWS                      | Chi phí / tuần |
| -------------------------------- | --------------- |
| Amazon S3                        | $1.50           |
| AWS Step Functions               | $0.15           |
| AWS Glue (Crawler + ETL Job)     | $8.00           |
| Amazon Athena                    | $0.50           |
| Amazon Redshift                  | $11.00          |
| Amazon QuickSight                | $8.00           |
| IAM, CloudTrail, CloudWatch, SNS | $1.00           |
| **Tổng cộng**                    | **$30.15**      |

## Nội dung

1. [Giới thiệu](1-Introduction/)
2. [Chuẩn bị](2-Preparation/)
3. [Giám sát và Bảo mật](3-MonitoringSecurity/)
4. [Pipeline phân tích dữ liệu](4-AnalyticsPipeline/)
5. [Trí tuệ doanh nghiệp](5-BusinessIntelligence/)
