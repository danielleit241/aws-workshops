---
title: "AWS Glue Crawler"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---
### Tổng quan

Trong phần này, chúng ta sẽ cấu hình **AWS Glue Crawler** để tự động quét dữ liệu từ Amazon S3, nhận diện lược đồ (schema) và tạo các bảng metadata trong **AWS Glue Data Catalog**.

Sau khi hoàn thành phần này, bạn sẽ có thể:

- Tạo Glue Database trong Data Catalog
- Tạo IAM Role cho Glue Crawler
- Cấu hình nguồn dữ liệu S3 cho Crawler
- Cấu hình database đầu ra và tiền tố bảng
- Tạo và chạy Glue Crawler
- Xác minh bảng được tạo trong Glue Data Catalog

### Tổng quan kiến trúc

![overview](/images/Proposal/diagram-architecture.jpg)

Kiến trúc của bài lab này được thiết kế để minh họa một mô hình khám phá dữ liệu phổ biến trên AWS.

Dữ liệu thô được lưu trong **Amazon S3** ở định dạng Parquet. **AWS Glue Crawler** quét nguồn dữ liệu, xác định cấu trúc tệp, phát hiện schema và tạo các bảng metadata trong **AWS Glue Data Catalog**. Sau khi metadata sẵn sàng, **AWS Glue ETL Job** có thể dùng thông tin trong catalog để đọc, chuyển đổi và ghi dữ liệu đã xử lý trở lại Amazon S3.

> Lưu ý quan trọng: AWS Glue Crawler không di chuyển hay sao chép dữ liệu của bạn vào Data Catalog.  
> Dữ liệu thực tế vẫn nằm trong Amazon S3. Data Catalog chỉ lưu metadata như tên bảng, schema, kiểu dữ liệu cột, partition và vị trí S3.

Luồng xử lý rút gọn như sau:

![workflow](/images/Workshop/4.Glue/4.1.Crawler/aws-glue-crawler-etl-flow.png)

### Các khái niệm chính

Trước khi tạo crawler, bạn cần hiểu các thành phần chính trong bài lab này.

**Amazon S3**

Amazon S3 được dùng làm lớp lưu trữ data lake. Trong workshop này, bộ dữ liệu thô được lưu trên S3 dưới dạng tệp Parquet.

Ví dụ: `s3://yellow-taxi-trip-demo-fcaj`

Parquet thường được dùng trong các bài toán phân tích vì có cấu trúc cột, nén tốt và hiệu quả cho xử lý dữ liệu quy mô lớn.

**AWS Glue Crawler**

AWS Glue Crawler tự động quét dữ liệu lưu trên S3 và phát hiện thông tin schema.

Crawler có thể nhận diện:

- Định dạng tệp
- Tên cột
- Kiểu dữ liệu
- Cấu trúc partition
- Vị trí S3
- Metadata của bảng

Sau đó, crawler ghi metadata này vào AWS Glue Data Catalog.

**AWS Glue Data Catalog**

AWS Glue Data Catalog là kho metadata tập trung. Dịch vụ này lưu các database và table mô tả dữ liệu của bạn.

Ví dụ, sau khi crawler quét S3, nó có thể tạo một bảng tham chiếu đến các tệp Parquet của bạn.

Bảng này sau đó có thể được sử dụng bởi:

- AWS Glue ETL Jobs
- Amazon Athena
- Amazon EMR
- Amazon Redshift Spectrum
- Các dịch vụ phân tích khác

**AWS Glue ETL Job**

AWS Glue ETL Job được dùng để chuyển đổi dữ liệu. ETL Job có thể đọc dữ liệu từ S3 bằng cách sử dụng định nghĩa bảng từ Glue Data Catalog.

### Cấu hình

Trong workshop này, chúng ta sẽ dùng cấu hình mẫu sau.

| Tài nguyên          | Giá trị                           |
| ------------------- | --------------------------------- |
| Source S3 Bucket    | `s3://yellow-taxi-trip-demo-fcaj` |
| Glue Crawler Name   | `glue_crawler_data`               |
| Glue Database Name  | `craw_data_catalog`               |
| IAM Role            | `AWSGlueServiceRole-Crawlers`     |
| Table Prefix        | `table_`                          |
| Crawler Schedule    | `On demand`                       |

Bạn có thể thay đổi các tên này theo môi trường AWS của riêng bạn.

**Bước 1: Thiết lập thuộc tính crawler**

1. Truy cập [AWS Glue Console](https://console.aws.amazon.com/glue/home)
2. Ở thanh điều hướng bên trái, chọn **Crawlers**
3. Chọn **Add crawler**

![OpenCrawlers](/images/Workshop/4.Glue/4.1.Crawler/create_crawler.png)

**Bước 2: Chọn Data Source và Classifiers**

1. Nhấn nút thêm data source

![DataSrc](/images/Workshop/4.Glue/4.1.Crawler/add_data_src.png)

2. Nhấn **Browse S3**

![BrowseS3](/images/Workshop/4.Glue/4.1.Crawler/browse_pathS3.png)

3. Chọn S3 Bucket rồi nhấn nút **Choose**

![ChooseBucket](/images/Workshop/4.Glue/4.1.Crawler/choose_s3_path.png)

4. Nhấn nút **Add S3 Data Source** rồi chọn **Next**

**Bước 3: Cấu hình bảo mật**

1. Nhấn nút **Create new IAM Role** và đặt tên

![IAMrole](/images/Workshop/4.Glue/4.1.Crawler/create_iam_button.png)

![IAMRole2](/images/Workshop/4.Glue/4.1.Crawler/set_name_iam_role.png)

2. Nhấn nút **View to configure role access** để cấp quyền đọc và ghi dữ liệu trong S3

![ViewRole](/images/Workshop/4.Glue/4.1.Crawler/view_role.png)

3. Nhấn vào tên **Permission policy** để chỉnh sửa

![EditPolicy](/images/Workshop/4.Glue/4.1.Crawler/tick_button_permission.png)

4. Nhấn **Edit** để chỉnh quyền:

- Trong phần Action, bạn cần bật quyền S3:GetObject và S3:PutObject để có quyền truy xuất dữ liệu từ S3.
- Trong phần Resource, vì tệp Parquet của tôi có nhiều tệp con, tôi thêm `/*` để có thể đọc các tệp bên trong.

![EditPermission](/images/Workshop/4.Glue/4.1.Crawler/edit_permission.png)

**Bước 4: Thiết lập đầu ra và lịch chạy**

1. Nhấn nút **Add Database**

![AddDB](/images/Workshop/4.Glue/4.1.Crawler/click_button_add_DB.png)

2. Tạo một Glue database chuẩn trong Data Catalog.

{{% notice tip %}}
S3 lưu dữ liệu thực tế, Glue Data Catalog lưu "bản đồ/schema" của dữ liệu, và Glue ETL dùng bản đồ đó để xử lý dữ liệu.
{{% /notice %}}

![DataBaseInDataCatalog](/images/Workshop/4.Glue/4.1.Crawler/create_database_data_catalog(10-11).png)

3. Nhấn **Next** để xem lại cấu hình crawler

![ViewOutputScheduling](/images/Workshop/4.Glue/4.1.Crawler/next_step.png)

### Xem lại và tạo

1. Xem lại toàn bộ cấu hình và nhấn **Create crawler**

![ReviewAndCreate](/images/Workshop/4.Glue/4.1.Crawler/create_success_crawler.png)

