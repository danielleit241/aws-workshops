---
title: "Analytics Pipeline với AWS Glue"
date: "2026-05-02"
weight: 4
chapter: false
pre: " <b> 4. </b> "
---

Trong chương này, chúng ta sẽ tìm hiểu các khái niệm cơ bản của một analytics pipeline sử dụng **Amazon S3**, **AWS Glue Crawler**, **AWS Glue Data Catalog** và **AWS Glue Visual ETL**.

Mục tiêu của chương này là giúp bạn hiểu cách các dịch vụ AWS này phối hợp với nhau trước khi bắt đầu các bài lab thực hành.

{{% notice info %}}
Trang này tập trung vào khái niệm và kiến trúc. Các bước cấu hình chi tiết sẽ được trình bày trong các phần tiếp theo.
{{% /notice %}}

### Analytics Pipeline Là Gì?

**Analytics pipeline** là một quy trình lấy dữ liệu thô, chuẩn bị, chuyển đổi và đưa dữ liệu đó vào trạng thái sẵn sàng để phân tích hoặc báo cáo.

Trong workshop này, pipeline theo luồng sau:

```txt
Amazon S3 - Dữ liệu thô
        ↓
AWS Glue Crawler
        ↓
AWS Glue Data Catalog
        ↓
AWS Glue Visual ETL Job
        ↓
Amazon S3 - Dữ liệu đã xử lý
```

Kiến trúc rút gọn được minh họa bên dưới:

![Analytics Pipeline Overview](/images/Workshop/4.Glue/4.1.Crawler/aws-glue-crawler-etl-flow.png)

Tổng quan:

- Amazon S3 lưu trữ các tệp dữ liệu thô.
- AWS Glue Crawler quét dữ liệu và khám phá cấu trúc của nó.
- AWS Glue Data Catalog lưu trữ metadata.
- AWS Glue Visual ETL đọc dữ liệu đã được catalog hóa và thực hiện chuyển đổi.
- Amazon S3 lưu trữ kết quả đầu ra đã xử lý.

### Tại Sao Cần Pipeline Này?

Dữ liệu thô lưu trong Amazon S3 có giá trị, nhưng bản thân nó không phải lúc nào cũng sẵn sàng để phân tích.

Ví dụ, nếu chỉ có các tệp Parquet trong S3, một dịch vụ xử lý vẫn cần biết:
- Dữ liệu nằm ở đâu
- Dữ liệu sử dụng định dạng tệp nào
- Bộ dữ liệu có những cột nào
- Kiểu dữ liệu của từng cột là gì
- Dữ liệu có được phân vùng không
- Kết quả đã xử lý nên được ghi vào đâu

AWS Glue giúp giải quyết vấn đề này bằng cách cung cấp khả năng khám phá metadata, quản lý catalog và xử lý ETL.

{{% notice tip %}}
Một data pipeline tốt tách biệt ba trách nhiệm:
- **Lưu trữ**: nơi dữ liệu tồn tại.
- **Metadata**: cách dữ liệu được mô tả.
- **Xử lý**: cách dữ liệu được chuyển đổi.
{{% /notice %}}

### Các Dịch Vụ Cốt Lõi Trong Pipeline

Workshop này sử dụng bốn thành phần chính.

| Dịch vụ               | Vai trò trong Pipeline                                              |
| --------------------- | ------------------------------------------------------------------- |
| Amazon S3             | Lưu trữ dữ liệu thô và dữ liệu đã xử lý                           |
| AWS Glue Crawler      | Quét dữ liệu nguồn và phát hiện schema                             |
| AWS Glue Data Catalog | Lưu metadata như database, table, schema và vị trí S3              |
| AWS Glue Visual ETL   | Xây dựng luồng xử lý trực quan để chuyển đổi dữ liệu              |

### Amazon S3: Lớp Lưu Trữ Dữ Liệu

Amazon S3 được dùng làm lớp lưu trữ của data pipeline.

Trong workshop này, dữ liệu thô được lưu trong S3 ở định dạng Parquet.

Parquet thường được dùng cho các bài toán phân tích vì:
- Có cấu trúc cột
- Nén tốt
- Hiệu quả cho xử lý dữ liệu quy mô lớn
- Được hỗ trợ tốt bởi AWS Glue và các ETL job dựa trên Spark

Một cấu trúc S3 phổ biến trong data lake trông như sau:

```txt
s3://data-lake/raw/
s3://data-lake/processed/
s3://data-lake/curated/
```

{{% notice info %}}
Trong workshop này, dữ liệu thô được lưu vào S3 trước. AWS Glue không thay thế S3. Nó chỉ khám phá và xử lý dữ liệu được lưu ở đó.
{{% /notice %}}

### AWS Glue Crawler: Lớp Khám Phá Schema

AWS Glue Crawler chịu trách nhiệm quét dữ liệu thô trong S3.

Crawler đọc các tệp và cố gắng hiểu cấu trúc của chúng.

Crawler có thể phát hiện:
- Định dạng tệp
- Tên cột
- Kiểu dữ liệu
- Cấu trúc partition
- Vị trí S3
- Metadata của bảng

Sau khi quét các tệp, crawler tạo hoặc cập nhật các bảng trong AWS Glue Data Catalog.

{{% notice warning %}}
AWS Glue Crawler không di chuyển dữ liệu từ S3 vào Data Catalog.
Dữ liệu thực tế vẫn nằm trong Amazon S3.
Crawler chỉ tạo metadata mô tả dữ liệu đó.
{{% /notice %}}

Ví dụ:

```txt
Dữ liệu thô:
s3://yellow-taxi-trip-demo-fcaj/

Kết quả của Crawler:
Database: craw_data_catalog
Table: table_yellow_taxi_trip_demo_fcaj
Location: s3://yellow-taxi-trip-demo-fcaj/
Format: Parquet
```

### AWS Glue Data Catalog: Lớp Metadata

AWS Glue Data Catalog là kho metadata tập trung.

Nó lưu thông tin về các bộ dữ liệu của bạn, chẳng hạn như:
- Tên database
- Tên bảng
- Tên cột
- Kiểu dữ liệu
- Partition key
- Định dạng tệp
- Vị trí S3

Data Catalog không lưu các hàng dữ liệu thực tế.

Thay vào đó, nó cho các dịch vụ AWS biết cách tìm và đọc dữ liệu từ S3.

{{% notice tip %}}
Hãy hình dung Data Catalog như một bản đồ. S3 lưu dữ liệu thực tế. Data Catalog cho Glue biết dữ liệu nằm ở đâu và cách hiểu nó.
{{% /notice %}}

Ví dụ metadata:

```txt
Database: craw_data_catalog
Table: table_yellow_taxi_trip_demo_fcaj
Format: Parquet
Location: s3://yellow-taxi-trip-demo-fcaj/
Columns: vendor_id, pickup_datetime, dropoff_datetime, total_amount, ...
```

### AWS Glue Visual ETL: Lớp Chuyển Đổi

Sau khi dữ liệu được catalog hóa, chúng ta có thể dùng AWS Glue Visual ETL để xây dựng luồng chuyển đổi.

Visual ETL cho phép thiết kế ETL job bằng giao diện trực quan thay vì phải viết toàn bộ code Spark thủ công.

ETL job có thể:
- Đọc dữ liệu nguồn từ bảng trong Glue Data Catalog
- Chọn hoặc đổi tên cột
- Lọc bản ghi
- Làm sạch dữ liệu không hợp lệ
- Áp dụng các phép biến đổi
- Ghi kết quả đầu ra vào một vị trí S3 khác

Điểm quan trọng là ETL job sử dụng bảng trong Data Catalog để hiểu dữ liệu nguồn.

Tuy nhiên, khi job chạy, nó vẫn đọc các tệp Parquet thực tế từ Amazon S3.

```txt
Bảng trong Glue Data Catalog
        ↓
Glue ETL Job hiểu schema và vị trí S3
        ↓
Glue ETL Job đọc tệp thực tế từ S3
        ↓
Glue ETL Job chuyển đổi dữ liệu
        ↓
Glue ETL Job ghi dữ liệu đã xử lý vào S3
```

### Cách Các Dịch Vụ Phối Hợp Với Nhau

Toàn bộ luồng hoạt động như sau:

1. Các tệp Parquet thô được tải lên Amazon S3.
2. AWS Glue Crawler quét đường dẫn S3.
3. Crawler phát hiện schema và metadata tệp.
4. Crawler tạo hoặc cập nhật bảng trong AWS Glue Data Catalog.
5. AWS Glue Visual ETL sử dụng bảng catalog làm đầu vào.
6. ETL job đọc dữ liệu thực tế từ S3.
7. ETL job chuyển đổi dữ liệu.
8. Kết quả đã chuyển đổi được ghi trở lại Amazon S3.

{{% notice note %}}
Data Catalog đóng vai trò là điểm kết nối giữa dữ liệu thô trong S3 và ETL job.
{{% /notice %}}

### Những Điều Cần Nắm Trước Khi Bắt Đầu

Trước khi chuyển sang các bài lab thực hành, hãy đảm bảo bạn hiểu các ý chính sau:

| Khái niệm                        | Giải thích                                                        |
| -------------------------------- | ----------------------------------------------------------------- |
| S3 lưu trữ dữ liệu               | Các tệp thô và đã xử lý được lưu vật lý trong S3                 |
| Crawler khám phá metadata        | Quét tệp và phát hiện schema                                      |
| Data Catalog lưu metadata        | Lưu định nghĩa bảng, không lưu bản ghi thực tế                   |
| Visual ETL chuyển đổi dữ liệu    | Dùng metadata catalog để đọc và xử lý dữ liệu S3                 |
| Kết quả đầu ra ghi về S3         | Dữ liệu đã xử lý được ghi vào S3 bucket đích                     |

### Cấu Trúc Chương

Chương này bao gồm các phần sau:

| Phần                  | Mục đích                                                          |
| --------------------- | ----------------------------------------------------------------- |
| AWS Glue Crawler      | Tạo crawler để khám phá schema từ dữ liệu thô trên S3            |
| AWS Glue Catalog      | Xem lại database và metadata bảng đã được tạo                    |
| AWS Glue ETL Job      | Xây dựng luồng Visual ETL để chuyển đổi dữ liệu                  |

### Tóm Tắt

Sau khi đọc phần giới thiệu này, bạn cần hiểu rằng:

- Amazon S3 là lớp lưu trữ.
- AWS Glue Crawler là lớp khám phá schema.
- AWS Glue Data Catalog là lớp metadata.
- AWS Glue Visual ETL là lớp chuyển đổi.
- Pipeline bắt đầu từ dữ liệu thô và kết thúc bằng dữ liệu đã xử lý trong S3.

{{% notice tip %}}
Cách đơn giản để nhớ pipeline: Lưu trữ → Khám phá → Catalog hóa → Chuyển đổi → Lưu trữ
{{% /notice %}}
