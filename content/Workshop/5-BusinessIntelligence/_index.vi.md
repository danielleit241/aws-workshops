---
title: "Business Intelligence"
date: "2026-05-02"
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

Trong chương này, chúng ta chuyển từ **chuẩn bị dữ liệu** sang **khai thác dữ liệu**. Sau khi dataset đã được khám phá, đăng ký metadata và biến đổi bằng AWS Glue, bước tiếp theo là truy vấn dữ liệu và chuyển nó thành thông tin phục vụ phân tích kinh doanh.

Mục tiêu của chương này là giới thiệu cách dữ liệu đã xử lý có thể được sử dụng bởi nhiều dịch vụ phân tích khác nhau, tùy theo nhu cầu:

- **Amazon Athena** để chạy truy vấn SQL serverless trực tiếp trên dữ liệu trong Amazon S3
- **Amazon Redshift Spectrum** để thực hiện phân tích theo hướng data warehouse nhưng vẫn tận dụng data lake
- **Amazon QuickSight** để xây dựng dashboard và báo cáo trực quan

{{% notice info %}}
Chương này tập trung vào lớp khai thác dữ liệu. Các bước data engineering để chuẩn bị dataset đã được hoàn thành trong chương Analytics Pipeline.
{{% /notice %}}

### Vị Trí Của Chương Này Trong Toàn Bộ Workshop

Luồng end-to-end của workshop lúc này là:

![Business Intelligence Flow](/images/Workshop/5-BusinessIntelligence/business_intelligence_flow.png)

Ở giai đoạn này:

- **Dataset taxi trip thô** đã được lưu trong Amazon S3
- **AWS Glue Crawler** đã phát hiện schema
- **AWS Glue Data Catalog** đã lưu metadata
- **AWS Glue ETL** đã làm sạch và biến đổi dữ liệu sang dạng sẵn sàng cho phân tích
- Lớp BI giờ có thể truy vấn và trực quan hóa kết quả

### Vì Sao Business Intelligence Quan Trọng

Xây dựng pipeline mới chỉ là một phần của bài toán. Giá trị thực sự xuất hiện khi người dùng có thể khám phá dữ liệu, trả lời câu hỏi và đưa ra quyết định từ dữ liệu đó.

Trong lớp business intelligence, chúng ta thường cần:

- Truy vấn dữ liệu mà không cần xây dựng ứng dụng riêng
- So sánh xu hướng, tổng giá trị và nhóm dữ liệu
- Điều tra các giá trị bất thường hoặc chênh lệch
- Chia sẻ kết quả qua dashboard và báo cáo
- Hỗ trợ cả phân tích ad-hoc lẫn báo cáo lặp lại

Đó là lý do workshop giới thiệu nhiều dịch vụ thay vì chỉ một query engine duy nhất.

{{% notice tip %}}
Hãy xem chương này là điểm mà dữ liệu đã được xử lý trở thành thông tin kinh doanh có thể sử dụng.
{{% /notice %}}

### Các Dịch Vụ Chính Trong Chương Này

| Dịch vụ | Vai trò chính |
|---|---|
| Amazon Athena | Truy vấn trực tiếp dữ liệu trên S3 bằng SQL chuẩn |
| Amazon Redshift Spectrum | Mở rộng phân tích theo mô hình warehouse tới dữ liệu trên S3 |
| Amazon QuickSight | Xây dựng dashboard và trực quan hóa dữ liệu phân tích |

### Bạn Sẽ Học Được Gì

Sau khi hoàn thành chương này, bạn sẽ hiểu:

- Khi nào nên dùng **Athena** cho phân tích nhẹ, serverless
- Vì sao **Redshift Spectrum** phù hợp với các workflow phân tích lớn hơn
- **QuickSight** kết nối với dữ liệu phân tích như thế nào để trực quan hóa
- Lớp BI phụ thuộc ra sao vào metadata và dữ liệu đầu ra đã được tạo ở các chương trước

### Nội Dung Chương

1. [Athena](5.1-Athena/)
2. [Redshift](5.2-Redshift/)
3. [QuickSight](5.3-Quickshight/)

Kết thúc chương này, bạn sẽ có cái nhìn hoàn chỉnh về cách dữ liệu đi từ bước ingest và transform tới truy vấn, khám phá và tạo insight qua dashboard.
