---
title: "AWS Glue ETL Job"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

### Tổng quan

Trong phần này, chúng ta sẽ tạo và chạy một **AWS Glue ETL Job** sử dụng **PySpark Script Editor** để xử lý dữ liệu Yellow Taxi. ETL Job sẽ đọc dữ liệu thô từ Amazon S3, thực hiện các bước làm sạch dữ liệu, chuẩn hóa schema, kiểm tra chất lượng dữ liệu và phân tách dữ liệu hợp lệ với dữ liệu lỗi trước khi ghi kết quả trở lại Amazon S3.

Khác với Glue Visual ETL, phần này sử dụng hoàn toàn PySpark Script để kiểm soát toàn bộ logic xử lý dữ liệu và validation rules.

Sau khi hoàn thành phần này, bạn sẽ có thể:

- Tạo AWS Glue ETL Job bằng Script Editor
- Cấu hình runtime parameters cho Glue Job
- Đọc dữ liệu Parquet từ Amazon S3 bằng PySpark
- Thực hiện Data Cleaning và Data Transformation
- Tạo Feature Engineering bằng PySpark
- Xây dựng rule-based validation pipeline
- Tách dữ liệu hợp lệ và dữ liệu lỗi
- Ghi dữ liệu đầu ra theo partition `year/month`
- Theo dõi trạng thái ETL Job trên AWS Glue

---

### Các khái niệm chính

Trước khi tạo ETL Job, bạn cần hiểu các thành phần chính trong phần này.

---

#### AWS Glue ETL Job

AWS Glue ETL Job là một Apache Spark job được quản lý hoàn toàn trên AWS dùng để xử lý dữ liệu quy mô lớn.

Glue ETL hỗ trợ hai chế độ:

- Visual Editor
- Script Editor

Trong workshop này, chúng ta sẽ sử dụng **Script Editor** với ngôn ngữ **PySpark** để xây dựng ETL pipeline.

Ưu điểm của Script Editor:
- Toàn quyền kiểm soát logic ETL
- Dễ triển khai validation rules phức tạp
- Hỗ trợ xử lý dữ liệu lớn bằng Spark
- Linh hoạt trong việc mở rộng pipeline

---

#### Amazon S3 Data Lake

Pipeline sử dụng Amazon S3 làm Data Lake với ba bucket chính:

| Bucket | Vai trò |
|---|---|
| Raw Bucket | Lưu dữ liệu thô đầu vào |
| Processed Bucket | Lưu dữ liệu hợp lệ sau ETL |
| Quarantine Bucket | Lưu dữ liệu lỗi hoặc bất thường |

---

#### Partition-based Processing

Dữ liệu được xử lý theo partition:

```text
year=YYYY/month=MM