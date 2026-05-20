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

### Bạn Sẽ Làm Gì Trong Phần Này

Trong các bước thực hành tiếp theo, bạn sẽ:

1. Chuẩn bị một bucket S3 để lưu kết quả truy vấn Athena
2. Mở Athena Query Editor và xác nhận các đối tượng trong Glue catalog
3. Chạy một truy vấn kiểm tra trên dataset đã xử lý
4. Khôi phục metadata catalog nếu bị thiếu
5. Dọn dẹp các tài nguyên tạm nếu chúng chỉ được tạo cho bài lab

### Kết Quả Học Tập

Sau phần này, bạn nên hiểu:

- Amazon Athena là gì
- Vì sao Athena tích hợp tự nhiên với AWS Glue và Amazon S3
- Athena hỗ trợ phân tích ad-hoc trên dataset của workshop như thế nào
- Cách xác nhận dữ liệu đã xử lý đã sẵn sàng để truy vấn

### Nội Dung Phần Này

1. [Chuẩn Bị Kết Quả Athena](5.1.1-PrepareAthenaResults/)
2. [Mở Athena Và Duyệt Catalog](5.1.2-OpenAthenaAndBrowseCatalog/)
3. [Chạy Truy Vấn Kiểm Tra](5.1.3-RunValidationQueries/)
4. [Khôi Phục Catalog Bị Thiếu](5.1.4-RecoverMissingCatalog/)
5. [Dọn Dẹp](5.1.5-Cleanup/)

Đến cuối phần này, bạn sẽ có một luồng Athena rõ ràng theo từng bước mà không làm một trang duy nhất bị quá tải bởi quá nhiều ảnh chụp màn hình.
