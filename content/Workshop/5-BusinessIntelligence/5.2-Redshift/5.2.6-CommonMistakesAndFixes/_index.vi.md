---
title: "Các lỗi thường gặp và cách khắc phục"
date: "2026-05-02"
weight: 6
chapter: false
pre: " <b> 2.6. </b> "
---

![Wrong path vs correct Spectrum path](/images/Workshop/5.2-Redshift/6-CommonMistakes/1-PathIssues/spectrum_query_paths.png)

## Lỗi 1: Dùng "Load data" thay vì External Schema

Khi mới vào Query Editor v2, bạn có thể bấm nhầm **Load data** để nhập dữ liệu vào các native table của Redshift.

![Load data - wrong path](/images/Workshop/5.2-Redshift/6-CommonMistakes/1-PathIssues/load-data-wrong-path.png)

### Vì sao sai?

Load data dùng để COPY dữ liệu từ S3 vào các bảng nội bộ của Redshift, phù hợp khi bạn muốn lưu dữ liệu bên trong Redshift.

Nhưng mục tiêu của chúng ta là truy vấn dữ liệu external từ S3/Glue mà không sao chép.

### Cách khắc phục

- Hủy thao tác Load data
- Dùng `CREATE EXTERNAL SCHEMA` để tham chiếu Glue Catalog
- Truy vấn thông qua các external table

## Lỗi 2: Ánh xạ sai Glue database

Ban đầu, bạn có thể tạo external schema trỏ tới `craw_data_catalog` (dữ liệu raw) thay vì database đã xử lý.

### Dấu hiệu

```sql
SELECT schemaname, tablename FROM svv_external_tables WHERE schemaname = 'taxi_raw';
```

![No external tables](/images/Workshop/5.2-Redshift/6-CommonMistakes/2-MetadataIssues/no-external-tables.png)

### Cách khắc phục

- Tạo Glue Crawler cho bucket S3 chứa dữ liệu processed
- Tạo external schema trỏ tới processed database
- Bảo đảm tên database là chính xác

## Lỗi 3: Cột bị trùng trong Glue table

Glue table có `year`/`month` xuất hiện đồng thời trong cột thường và partition key.

### Lỗi hiển thị

External table "taxi_processed.processed_yellow_taxi_trip_data" has column "year" duplicated

### Nguyên nhân

ETL job đã ghi `year`/`month` vào dữ liệu Parquet, trong khi đường dẫn S3 cũng dùng Hive partition `year=.../month=...`.

Glue Crawler vì thế suy luận ra các cột bị trùng.

### Cách khắc phục

Chỉnh schema của Glue table: xóa `year` và `month` khỏi nhóm cột thường, chỉ giữ trong partition keys.

Sau đó làm mới metadata của Redshift.

## Lỗi 4: IAM Role thiếu quyền

Nếu truy vấn thất bại với lỗi `access denied`, hãy kiểm tra xem IAM role đã có quyền đọc bucket S3 và Glue catalog chưa.

Role cần có các policy: `AmazonS3ReadOnlyAccess`, `AWSGlueServiceRole`.

## Lỗi 5: Sai Region

Bảo đảm tất cả tài nguyên đều nằm trong cùng region `us-east-2`.

## Best practices

- Luôn thử với `LIMIT` trước khi chạy truy vấn toàn phần
- Dùng partition filter để tối ưu hiệu năng
- Kiểm tra `svv_external_schemas` và `svv_external_tables` để xác minh metadata
