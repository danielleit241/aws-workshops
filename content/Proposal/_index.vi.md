---
title: "Proposal"
date: "2025-09-09"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

## Nội dung

**Tóm tắt dự án (Executive Summary)**

- Tóm tắt: Dự án này nhằm xây dựng một hệ thống xử lý dữ liệu tự động (Data Analytics Pipeline) trên nền tảng đám mây Amazon Web Services (AWS). Hệ thống được thiết kế theo kiến trúc Event-Driven và Serverless, chuyên biệt để xử lý, làm sạch và phân tích tập dữ liệu lớn về hồ sơ chuyến đi của taxi (TLC Trip Record Data - Yellow Taxi). Mục đích cuối cùng là chuyển đổi dữ liệu thô thành các thông tin chi tiết (insights) có giá trị cao, phục vụ cho việc ra quyết định kinh doanh thông qua các Dashboard trực quan.
- Mục tiêu:
  - Tự động hóa hoàn toàn quy trình thu thập và xử lý dữ liệu (ETL) từ nguồn đến Data Warehouse.
  - Đảm bảo chất lượng dữ liệu (Data Quality) thông qua cơ chế tự động phát hiện lỗi, loại bỏ dữ liệu rác (outliers, missing values) trước khi phân tích.
  - Cung cấp nền tảng phân tích linh hoạt: Hỗ trợ cả truy vấn nhanh (Ad-hoc query) và phân tích chuyên sâu (OLAP).
  - Trực quan hóa dữ liệu kinh doanh (Nhu cầu chuyến đi, Doanh thu, Phân bổ không gian) cho ban lãnh đạo.
- Phạm vi:
  - Xây dựng Data Lake (Raw & Processed Layer) trên Amazon S3.
  - Triển khai quy trình ETL tự động bằng AWS Step Functions, Lambda và Glue DataBrew.
  - Tích hợp kho dữ liệu Amazon Redshift và lớp truy vấn Amazon Athena.
  - Xây dựng hệ thống báo cáo BI (Business Intelligence) trên Amazon QuickSight.
  - Thiết lập hệ thống bảo mật, giám sát và cảnh báo lỗi (CloudWatch, CloudTrail, SNS).

**Tuyên bố vấn đề (Problem Statement)**

Vấn đề hiện tại (Current Challenges): Tập dữ liệu Yellow Taxi từ New York City Taxi and Limousine Commission chứa lượng thông tin khổng lồ nhưng mang nhiều "nhiễu" và bất thường ở dạng thô:

- Chất lượng dữ liệu kém: Xuất hiện các cuốc xe không có hành khách (`passenger_count = null`), khoảng cách bằng 0 (`trip_distance = 0`), hoặc cước phí bị âm (`fare_amount < 0`).
- Thiếu tự động hóa: Việc xử lý dữ liệu thủ công hoặc bằng các hệ thống cũ tốn nhiều thời gian, dễ gây sai sót và không có khả năng mở rộng (scale) khi dung lượng dữ liệu tăng lên hàng tháng (file Parquet/CSV mới).
- Phân mảnh thông tin: Dữ liệu không được tập trung tại một nguồn duy nhất (Single Source of Truth), khiến việc lập báo cáo doanh thu và phân tích hành vi khách hàng gặp khó khăn, độ trễ cao.

Giải pháp kỹ thuật (Technical Solution): Triển khai kiến trúc Modern Data Lakehouse trên AWS:

- Tự động kích hoạt (Event-driven): Sử dụng Amazon EventBridge để tự động bắt sự kiện khi có file dữ liệu mới được upload, loại bỏ thao tác thủ công.
- Kiểm soát chất lượng chặt chẽ: Sử dụng AWS Glue DataBrew để Profiling (phân tích cấu trúc) và AWS Lambda để rẽ nhánh logic (Ví dụ: Tự động cảnh báo nếu tỷ lệ lỗi dữ liệu > 20%, ngược lại tiếp tục quy trình).
- Chuẩn hóa và Tối ưu: Làm sạch dữ liệu, tạo thêm các biến có ý nghĩa (Feature Engineering như `trip_duration`, `trip_speed`) và lưu trữ dưới định dạng Columnar (Parquet) theo phân vùng (Partitioning) để tối ưu chi phí và tốc độ truy vấn.

**Kiến trúc giải pháp (Solution Architecture)**

![overview](/images/Proposal/diagram-architecture.jpg)

Kiến trúc hệ thống đi theo luồng xử lý:
Raw &rarr; Processing &rarr; Analytics &rarr; Visualization.

Kiến trúc Kỹ thuật (Workflow Overview)

- Ingestion: Dữ liệu thô (Parquet/CSV) được đẩy vào Data Lake S3 Raw Bucket.
- Trigger: Sự kiện `ObjectCreated` từ S3 kích hoạt EventBridge.
- Orchestration: EventBridge gọi Step Functions để điều phối toàn bộ vòng đời pipeline (Retry, Logging).
- Profiling: Glue DataBrew phân tích dataset, tìm ra các điểm bất thường (missing, outliers, mismatch).
- Validation: Lambda đọc kết quả Profiling để quyết định bước tiếp theo hoặc gửi cảnh báo lỗi.
- Transformation: Glue DataBrew Recipe thực thi ETL (làm sạch dữ liệu, chuẩn hóa kiểu dữ liệu, Feature Engineering).
- Processed Storage: Dữ liệu sạch được lưu vào S3 Processed Bucket (định dạng Parquet, phân vùng theo Year/Month/Day).
- Data Warehousing: Sử dụng lệnh `COPY` để nạp dữ liệu từ S3 vào bảng `fact_taxi_trip` trong Amazon Redshift phục vụ OLAP. Song song, Amazon Athena hỗ trợ truy vấn Ad-hoc trực tiếp trên S3.
- Visualization: Amazon QuickSight kết nối với Redshift/Athena để hiển thị Dashboard (Trip Demand, Revenue, Spatial Analysis).

Technology Stack:

| Lớp (Layer)           | Dịch vụ AWS                      | Mục đích / Vai trò                                              |
| --------------------- | -------------------------------- | --------------------------------------------------------------- |
| Storage / Data Lake   | Amazon S3                        | Lưu trữ Raw Data và Curated/Processed Data.                     |
| Event & Orchestration | EventBridge, Step Functions      | Kích hoạt tự động, điều phối quy trình (State Machine).         |
| Compute / Logic       | AWS Lambda                       | Xử lý logic điều hướng (Orchestration & Validation logic).      |
| Data Processing (ETL) | AWS Glue DataBrew                | Profiling dữ liệu, làm sạch, biến đổi (No-code ETL).            |
| Data Warehouse        | Amazon Redshift                  | Kho dữ liệu tập trung (OLAP), lưu trữ bảng Fact/Dimension.      |
| Ad-hoc Query          | Amazon Athena                    | Truy vấn SQL trực tiếp không cần load vào Warehouse.            |
| BI / Visualization    | Amazon QuickSight                | Xây dựng Dashboard báo cáo quản trị.                            |
| Security & Monitoring | IAM, CloudTrail, CloudWatch, SNS | Phân quyền, lưu vết, giám sát pipeline và gửi cảnh báo (Alert). |

**Kế hoạch triển khai (Implementation Plan)**

Lộ trình và Milestones (Dự kiến 8 tuần)

- Phase 1: Foundation & Data Ingestion (Tuần 1-2)
  - Thiết lập môi trường AWS, cấu hình IAM Roles và Security.
  - Tạo S3 Buckets (Raw & Processed).
  - Thiết lập EventBridge trigger S3 `ObjectCreated`.
- Phase 2: Orchestration & Data Processing (Tuần 3-5)
  - Tạo Glue DataBrew Profiles để phân tích cấu trúc schema của Taxi data.
  - Viết DataBrew Recipes thực hiện ETL (Xóa null, lọc giá trị âm, tạo biến `trip_duration`, `trip_speed`).
  - Lập trình AWS Lambda function để đọc rules và rẽ nhánh.
  - Đóng gói quy trình vào AWS Step Functions.
- Phase 3: Data Warehousing & Querying (Tuần 6)
  - Thiết lập Amazon Redshift Cluster, tạo schema `fact_taxi_trip`.
  - Tạo luồng tự động `COPY` dữ liệu từ S3 Processed vào Redshift.
  - Cấu hình Amazon Athena trỏ vào S3 Processed bucket.
- Phase 4: BI Visualization & Handover (Tuần 7-8)
  - Phát triển QuickSight Dashboards (Trip Demand, Revenue per Vendor, Heatmaps).
  - Thiết lập CloudWatch Alarms & SNS (cảnh báo qua Email/Slack khi ETL failed).
  - Kiểm thử toàn trình (UAT) và bàn giao tài liệu hệ thống.

Ước lượng chi phí (Cost Estimation Model)

Hệ thống tận dụng tối đa kiến trúc Serverless, chi phí sẽ tính theo dạng Pay-as-you-go (Dùng bao nhiêu trả bấy nhiêu). Cơ cấu chi phí hàng tháng dự kiến phân bổ như sau:

- AWS Services:
  - AWS Amplify Hosting: $0.00 trong gói Free Tier: 500 phút build, 5 GB dữ liệu được phân phối. Sau khi hết Free Tier: khoảng $0.01/phút × 500 = $5.00/tháng.
  - AWS Lambda: $0.00/month (20,000 requests/ngày, 128 MB, 200 ms trung bình).
  - Amazon API Gateway: $0.00/month (600,000 requests/tháng, dưới mức Free Tier).
  - Amazon DynamoDB: $0.00/month (5 GB dữ liệu, 100K đọc/ghi mỗi ngày).
  - Amazon S3 (Lưu ảnh): $0.12/month (10 GB lưu trữ, 5,000 yêu cầu GET/PUT).
  - Amazon SES (Gửi email): $0.00/month (2,000 email/tháng trong Free Tier).
  - Amazon Personalize: $0.00 trong 2 tháng đầu (20 GB dữ liệu, 50 ngàn lượt tương tác). Sau đó: khoảng $8.00/tháng với batch inference (với tập dữ liệu nhỏ và huấn luyện lại hàng tuần $0.067 per 1 ngàn lượt tương tác).
  - Bảng điều khiển tùy chỉnh (Amplify + Chart.js): $0.00/month (sử dụng Amplify hiện có, dữ liệu từ S3/DynamoDB).
  - Amazon Location Service: $0.00/month (10,000 yêu cầu bản đồ, 1,000 yêu cầu định vị).
  - Amazon EventBridge (Scheduler): $0.00/month (10 quy tắc kích hoạt hàng ngày/giờ).
  - AWS IAM + KMS + WAF: $0.00/month (xác thực, mã hóa và bảo mật cơ bản).
- Tổng chi phí ước tính:
  - Tháng 1: $0.12/month (Tất cả nằm trong Free Tier)
  - Tháng 2: $5.12/month (Personalize vẫn trong Free Tier, Amplify bắt đầu tính phí)
  - Sau khi hết Free Tier: $13.12/month, ≈ $157.44/năm
