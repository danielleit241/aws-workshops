---
title: "AWS Glue Catalog"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

## AWS Glue Data Catalog

### Tổng quan

AWS Glue Data Catalog là kho metadata tập trung dùng để lưu trữ thông tin về các nguồn dữ liệu trong data lake.

Trong workshop này, bộ dữ liệu thực tế được lưu trong **Amazon S3**, còn **AWS Glue Data Catalog** chỉ lưu metadata mô tả bộ dữ liệu đó.

{{% notice info %}}
AWS Glue Data Catalog không lưu dữ liệu thực tế.  
Dịch vụ này lưu metadata giúp các dịch vụ AWS hiểu được dữ liệu đang nằm ở đâu và có cấu trúc như thế nào.
{{% /notice %}}

### Data Catalog Lưu Những Gì?

Khi AWS Glue Crawler quét dữ liệu từ Amazon S3, nó sẽ tạo hoặc cập nhật các bảng metadata trong Glue Data Catalog.

Data Catalog có thể lưu các thông tin như:

- Tên database
- Tên bảng
- Tên cột
- Kiểu dữ liệu của cột
- Định dạng tệp
- Vị trí S3
- Thông tin partition
- Thuộc tính bảng

Ví dụ, nếu bộ dữ liệu thô được lưu tại:

```text
s3://yellow-taxi-trip-demo-fcaj
```

Bảng trong Data Catalog có thể lưu metadata mô tả:
- Vị trí: s3://yellow-taxi-trip-demo-fcaj
- Định dạng: Parquet
- Các cột: vendorid, trip_distance, total_amount, ...
- Kiểu dữ liệu: bigint, double, timestamp, ...

Các tệp Parquet thực tế vẫn nằm trong Amazon S3.

### Data Catalog Là Lớp Metadata

Mối quan hệ giữa các thành phần có thể hiểu như sau:

![DataCatalog](/images/Workshop/4.Glue/4.1.Crawler/4.1.15.png)

{{% notice tip %}}
Bạn có thể hình dung Amazon S3 là lớp lưu trữ và AWS Glue Data Catalog là bản đồ của dữ liệu.
{{% /notice %}}

### Database và Table trong Data Catalog

Trong AWS Glue Data Catalog, metadata được tổ chức thành các database và table.

**Database**

Database là một container logic dùng để nhóm các bảng metadata liên quan lại với nhau.

Ví dụ:

![DataCatalog](/images/Workshop/4.Glue/4.1.Crawler/4.1.17.png)

Database này không chứa dữ liệu thực tế. Nó chỉ chứa các định nghĩa bảng.

**Table**

Table đại diện cho cấu trúc của một bộ dữ liệu.

Một Glue table thường chứa:

- Đường dẫn S3 của bộ dữ liệu
- Định dạng tệp
- Schema
- Các cột và kiểu dữ liệu
- Thông tin partition, nếu có

Ví dụ, một bảng được tạo bởi crawler có thể trỏ đến các tệp Parquet lưu trong S3.

### Tại Sao Data Catalog Quan Trọng?

Data Catalog cho phép nhiều dịch vụ phân tích AWS dùng chung một định nghĩa metadata.

Thay vì phải định nghĩa schema thủ công cho từng dịch vụ, bạn chỉ cần định nghĩa một lần trong Data Catalog và tái sử dụng trên nhiều dịch vụ khác nhau.

Cùng một bảng trong Data Catalog có thể được sử dụng bởi:

- **AWS Glue ETL Job** để chuyển đổi dữ liệu
- **Amazon Athena** để truy vấn dữ liệu bằng SQL
- **Amazon EMR** để xử lý dữ liệu quy mô lớn
- **Amazon Redshift Spectrum** để truy vấn dữ liệu trực tiếp từ S3

Điều này giúp data lake dễ quản lý hơn và giảm thiểu cấu hình trùng lặp.

### Data Catalog Không Thay Thế S3

Điều quan trọng cần hiểu là sự khác biệt giữa Amazon S3 và AWS Glue Data Catalog.

| Thành phần            | Trách nhiệm                              |
| --------------------- | ---------------------------------------- |
| Amazon S3             | Lưu trữ các tệp dữ liệu thực tế         |
| AWS Glue Crawler      | Quét dữ liệu và phát hiện schema         |
| AWS Glue Data Catalog | Lưu metadata về dữ liệu                  |
| AWS Glue ETL Job      | Đọc, chuyển đổi và ghi dữ liệu          |

Data Catalog chỉ cho các dịch vụ AWS biết cách hiểu dữ liệu. Nó không sở hữu hay lưu trữ vật lý bộ dữ liệu.

### Ví Dụ Thực Tế

Bạn có thể hình dung Data Catalog giống như mục lục của một thư viện.

Sách được xếp trên kệ.
Mục lục không chứa bản thân những cuốn sách.
Nó chỉ cho bạn biết:

- Những cuốn sách nào đang có
- Chúng nằm ở đâu
- Chúng thuộc thể loại gì
- Chúng được sắp xếp như thế nào

Tương tự:
- Amazon S3 lưu dữ liệu thực tế
- Data Catalog lưu mô tả của dữ liệu đó

### Tổng Kết

AWS Glue Data Catalog là lớp metadata quan trọng trong kiến trúc data lake trên AWS.

Trong workshop này, nó giúp chúng ta:
- Lưu thông tin schema được crawler phát hiện
- Tổ chức metadata bằng database và table
- Cho phép Glue ETL Job và các dịch vụ phân tích khác hiểu được dữ liệu trên S3
- Tách biệt lưu trữ dữ liệu vật lý khỏi quản lý metadata

Trong phần tiếp theo, chúng ta sẽ sử dụng lớp metadata này làm nguồn dữ liệu cho AWS Glue ETL Job.
