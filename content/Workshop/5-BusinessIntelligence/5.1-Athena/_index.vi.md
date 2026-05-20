---
title: "Athena"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

Trong phần này, chúng ta giới thiệu **Amazon Athena** như cách nhanh nhất để bắt đầu phân tích dataset đã được xử lý từ pipeline AWS Glue.

Athena là một **dịch vụ truy vấn tương tác theo mô hình serverless** cho phép chạy SQL trực tiếp trên dữ liệu lưu trong **Amazon S3**. Nhờ tích hợp với **AWS Glue Data Catalog**, Athena có thể sử dụng ngay metadata bảng đã được khám phá và quản lý từ các bước trước trong workshop.

### Vì Sao Athena Được Học Trước

Athena là bước khởi đầu tự nhiên trong lớp business intelligence vì nó:

- Không cần provision hạ tầng
- Không cần quản trị database server
- Không cần nạp dữ liệu vào một analytics engine riêng

Khi dữ liệu đã được xử lý và lưu trong Amazon S3, đồng thời đã được đăng ký trong Glue Data Catalog, Athena có thể truy vấn trực tiếp.

{{% notice info %}}
Athena rất phù hợp cho việc kiểm tra kết quả ETL, khám phá dữ liệu, và phân tích ad-hoc trước khi chuyển sang các mô hình phân tích thiên về data warehouse hơn.
{{% /notice %}}

### Athena Phù Hợp Với Workshop Này Như Thế Nào

Ở chương trước, pipeline đã tạo ra một dataset sạch và có cấu trúc. Athena nằm phía trên kết quả đó và dùng metadata đã được catalog để hiểu đúng định dạng dữ liệu.

Luồng hoạt động là:

![Athena Query Flow](/images/Workshop/5-BusinessIntelligence/athena_query_flow.png)

Điều đó có nghĩa là Athena không thay thế AWS Glue. Thay vào đó:

- **Amazon S3** lưu các file dữ liệu thực tế
- **AWS Glue Data Catalog** lưu định nghĩa bảng và schema
- **Athena** đọc cả hai để thực thi truy vấn SQL

### Athena Phù Hợp Với Những Nhu Cầu Nào

Athena thường được dùng cho:

- Kiểm tra nhanh kết quả ETL
- Phân tích SQL ad-hoc trên file trong data lake
- Khám phá dữ liệu mà chưa cần xây dựng data warehouse
- Kiểm tra số lượng bản ghi, phân phối dữ liệu, và các phép tổng hợp
- Phân tích theo partition hoặc các tập dữ liệu đã được lọc

Trong workshop này, Athena giúp xác nhận rằng dữ liệu taxi trip đã sẵn sàng cho analytics và có thể trả lời các câu hỏi kinh doanh phổ biến.

### Ví Dụ Các Câu Hỏi Athena Có Thể Trả Lời

Với Athena, bạn có thể chạy các truy vấn như:

- Có bao nhiêu taxi trip trong dataset đã xử lý?
- Giá trị fare trung bình theo từng payment type là bao nhiêu?
- Ngày pickup nào tạo ra doanh thu cao nhất?
- Khoảng cách chuyến đi thay đổi ra sao theo từng giai đoạn thời gian?
- Mẫu passenger count phổ biến nhất là gì?

Đây là các ví dụ điển hình về **câu hỏi nghiệp vụ** có thể được trả lời trực tiếp từ data lake.

### Lợi Ích Khi Sử Dụng Athena

| Lợi ích | Giải thích |
|---|---|
| Serverless | Không cần cluster hoặc database instance |
| SQL-based | Dùng ngôn ngữ SQL quen thuộc để phân tích |
| Glue Integration | Tái sử dụng metadata từ Data Catalog |
| S3-native | Truy vấn dữ liệu trực tiếp tại nơi nó được lưu |
| Pay-per-query | Chi phí dựa trên dữ liệu được scan thay vì hạ tầng nhàn rỗi |

{{% notice tip %}}
Athena hoạt động hiệu quả nhất khi dữ liệu nguồn được lưu ở các định dạng tối ưu như Parquet và được tổ chức bằng partition rõ ràng. Đó cũng là lý do thiết kế pipeline Glue ở chương trước rất quan trọng.
{{% /notice %}}

### Athena So Với Redshift Và QuickSight

Athena không phải là dịch vụ BI cuối cùng trong workshop. Đây là **điểm bắt đầu cho việc truy vấn dữ liệu**.

- Dùng **Athena** khi bạn cần truy cập trực tiếp, đơn giản, bằng SQL vào dữ liệu trên S3
- Dùng **Redshift Spectrum** khi bạn cần workflow phân tích theo hướng warehouse hơn
- Dùng **QuickSight** khi bạn muốn dashboard thay vì kết quả truy vấn thô

Ba dịch vụ này cùng cho thấy nhiều cách khác nhau để khai thác cùng một dataset đã được curate.

### Kết Quả Học Tập

Sau phần này, bạn nên hiểu:

- Amazon Athena là gì
- Vì sao Athena tích hợp tự nhiên với AWS Glue và Amazon S3
- Athena hỗ trợ phân tích ad-hoc trên dataset của workshop như thế nào
- Vì sao Athena là công cụ đầu tiên quan trọng trong lớp business intelligence
