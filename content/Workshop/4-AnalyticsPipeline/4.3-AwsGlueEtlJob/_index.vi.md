---
title: "AWS Glue ETL Job"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

### Tổng quan

Trong phần này, chúng ta sẽ tạo và chạy một **AWS Glue ETL Job** để đọc dữ liệu thô từ **AWS Glue Data Catalog**, áp dụng các phép biến đổi và ghi kết quả đã xử lý trở lại **Amazon S3**.

Sau khi hoàn thành phần này, bạn sẽ có thể:

- Tạo AWS Glue ETL Job bằng Visual Editor
- Cấu hình nguồn dữ liệu từ Glue Data Catalog
- Áp dụng các phép biến đổi cơ bản cho bộ dữ liệu
- Cấu hình đích đầu ra trong Amazon S3
- Chạy ETL Job và xác minh kết quả đầu ra

### Tổng quan kiến trúc

![overview](/images/Proposal/diagram-architecture.jpg)

Ở các phần trước, chúng ta đã dùng **AWS Glue Crawler** để quét các tệp Parquet thô lưu trong Amazon S3 và đăng ký schema vào **AWS Glue Data Catalog**.

Trong phần này, **AWS Glue ETL Job** sẽ đọc metadata từ catalog đó để xác định vị trí và cấu trúc dữ liệu thô, áp dụng các phép biến đổi, rồi ghi kết quả đã làm sạch vào một vị trí S3 đích.

Luồng xử lý rút gọn như sau:

![workflow](/images/Workshop/4.Glue/4.2.ETL/4.2.1.png)

> Lưu ý quan trọng: ETL Job đọc dữ liệu từ Amazon S3 bằng cách sử dụng schema được định nghĩa trong Data Catalog.  
> Bản thân Data Catalog không lưu dữ liệu. Nó chỉ cung cấp metadata cho job biết dữ liệu nằm ở đâu và có cấu trúc như thế nào.

### Các khái niệm chính

Trước khi tạo ETL Job, bạn cần hiểu các thành phần chính trong phần này.

**AWS Glue ETL Job**

AWS Glue ETL Job là một Apache Spark job được quản lý, chạy trên hạ tầng AWS. Job có thể đọc dữ liệu từ nhiều nguồn khác nhau, áp dụng các phép biến đổi và ghi kết quả ra đích đầu ra.

Glue ETL Job hỗ trợ hai chế độ tạo job:

- Visual Editor — giao diện kéo thả để xây dựng pipeline mà không cần viết code
- Script Editor — viết trực tiếp script PySpark hoặc Scala

Trong workshop này, chúng ta sẽ dùng **Visual Editor**.

**Nguồn dữ liệu**

ETL Job đọc dữ liệu từ bảng trong **AWS Glue Data Catalog** được tạo bởi crawler ở phần 4.1.

Bảng catalog chứa:
- Vị trí S3 của các tệp Parquet thô
- Định nghĩa schema và cột
- Định dạng tệp

**Các phép biến đổi**

Phép biến đổi là các thao tác được áp dụng lên dữ liệu trước khi ghi kết quả đầu ra. Một số ví dụ phổ biến:

- Chọn hoặc xóa cột
- Đổi tên cột
- Lọc hàng
- Thay đổi kiểu dữ liệu
- Kết hợp các bộ dữ liệu

**Đích đầu ra**

Kết quả của ETL Job được ghi trở lại **Amazon S3** tại một vị trí được chỉ định. Định dạng đầu ra có thể cấu hình là Parquet, CSV, JSON hoặc các định dạng được hỗ trợ khác.

### Cấu hình

Trong workshop này, chúng ta sẽ dùng cấu hình mẫu sau.

| Tài nguyên            | Giá trị                                      |
| --------------------- | -------------------------------------------- |
| Glue Job Name         | `glue_etl_job_taxi`                          |
| IAM Role              | `AWSGlueServiceRole-Crawlers`                |
| Data Source           | Glue Data Catalog — `craw_data_catalog`      |
| Source Table          | `table_yellow_taxi_trip_demo_fcaj`           |
| Output S3 Path        | `s3://yellow-taxi-trip-demo-fcaj/output/`    |
| Output Format         | Parquet                                      |
| Glue Version          | Glue 4.0                                     |

Bạn có thể điều chỉnh các giá trị này theo môi trường AWS của riêng bạn.

**Bước 1: Tạo ETL Job mới**

1. Truy cập [AWS Glue Console](https://console.aws.amazon.com/glue/home)
2. Ở thanh điều hướng bên trái, chọn **ETL Jobs**
3. Chọn **Visual ETL**

![CreateJob](/images/Workshop/4.Glue/4.2.ETL/4.2.2.png)

**Bước 2: Cấu hình nguồn dữ liệu**

1. Trong Visual Editor, nhấn vào node **Source** để mở bảng cấu hình
2. Trong phần **Data source properties**, chọn **AWS Glue Data Catalog** làm loại nguồn
3. Chọn **Database** đã tạo ở phần 4.1 (ví dụ: `craw_data_catalog`)
4. Chọn **Table** được tạo bởi crawler (ví dụ: `table_yellow_taxi_trip_demo_fcaj`)

![ConfigureSource](/images/Workshop/4.Glue/4.2.ETL/4.2.3.png)

{{% notice tip %}}
Nếu bạn không thấy database hoặc table trong danh sách thả xuống, hãy đảm bảo Glue Crawler ở phần 4.1 đã chạy thành công và bảng đã xuất hiện trong Data Catalog.
{{% /notice %}}

**Bước 3: Thêm node Transform**

1. Nhấn nút **+** để thêm node mới sau source
2. Chọn **Transform** và chọn **ApplyMapping**
3. Trong bảng mapping, xem lại các cột được phát hiện và kiểu dữ liệu của chúng
4. Bạn có thể đổi tên cột, thay đổi kiểu dữ liệu hoặc xóa các cột không cần thiết

![AddTransform](/images/Workshop/4.Glue/4.2.ETL/4.2.4.png)

{{% notice info %}}
ApplyMapping là phép biến đổi phổ biến nhất trong Glue Visual ETL. Nó cho phép bạn kiểm soát những cột nào được truyền đến đầu ra và cách chúng được ánh xạ.
{{% /notice %}}

**Bước 4: Cấu hình đích đầu ra**

1. Nhấn nút **+** để thêm node mới sau transform
2. Chọn **Target** và chọn **Amazon S3**
3. Đặt **Format** là `Parquet`
4. Đặt **S3 Target Location** thành đường dẫn đầu ra của bạn, ví dụ:

```text
s3://yellow-taxi-trip-demo-fcaj/output/
```

5. Trong phần **Data Catalog update options**, chọn **Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions** nếu bạn muốn kết quả đầu ra cũng được đăng ký vào catalog

![ConfigureTarget](/images/Workshop/4.Glue/4.2.ETL/4.2.5.png)

**Bước 5: Cấu hình thuộc tính job**

1. Nhấn tab **Job details** ở đầu Visual Editor
2. Đặt **Name** cho job (ví dụ: `glue_etl_job_taxi`)
3. Trong phần **IAM Role**, chọn role đã tạo ở phần 4.1 (ví dụ: `AWSGlueServiceRole-Crawlers`)
4. Đặt **Glue version** là `Glue 4.0 - Supports spark 3.3, Scala 2, Python 3`
5. Giữ nguyên các cài đặt còn lại theo mặc định

![JobProperties](/images/Workshop/4.Glue/4.2.ETL/4.2.6.png)

{{% notice tip %}}
Hãy đảm bảo IAM Role có quyền đọc từ S3 bucket nguồn và ghi vào đường dẫn S3 đầu ra. Bạn đã cấu hình điều này ở phần 4.1 khi thiết lập role cho crawler.
{{% /notice %}}

**Bước 6: Lưu và chạy job**

1. Nhấn **Save** để lưu cấu hình job
2. Nhấn **Run** để bắt đầu ETL Job

![RunJob](/images/Workshop/4.Glue/4.2.ETL/4.2.7.png)

3. Job sẽ xuất hiện trong tab **Runs** với trạng thái **Running**
4. Chờ trạng thái chuyển sang **Succeeded**

{{% notice info %}}
Lần chạy đầu tiên có thể mất 2–3 phút để khởi động do Glue cần cấp phát môi trường Spark. Đây là hành vi bình thường.
{{% /notice %}}

### Xác minh kết quả đầu ra

Sau khi job hoàn thành thành công, hãy xác minh rằng các tệp đầu ra đã được ghi vào S3.

1. Truy cập [Amazon S3 Console](https://s3.console.aws.amazon.com/s3/home)
2. Điều hướng đến bucket và đường dẫn đầu ra của bạn (ví dụ: `s3://yellow-taxi-trip-demo-fcaj/output/`)
3. Xác nhận rằng các tệp Parquet đã được tạo trong thư mục đầu ra

![VerifyOutput](/images/Workshop/4.Glue/4.2.ETL/4.2.8.png)

{{% notice tip %}}
Nếu thư mục đầu ra trống hoặc job thất bại, hãy kiểm tra **Error logs** trong tab Runs. Các lỗi thường gặp bao gồm thiếu quyền S3 hoặc đường dẫn S3 đầu ra không đúng.
{{% /notice %}}

### Tổng kết

Trong phần này, chúng ta đã tạo một AWS Glue ETL Job bằng Visual Editor.

Job đọc dữ liệu Parquet thô từ Glue Data Catalog, áp dụng phép biến đổi ánh xạ cột và ghi kết quả đã xử lý trở lại Amazon S3.

| Bước | Thao tác                                              |
| ---- | ----------------------------------------------------- |
| 1    | Tạo Visual ETL Job mới                                |
| 2    | Cấu hình Glue Data Catalog làm nguồn dữ liệu          |
| 3    | Thêm phép biến đổi ApplyMapping                       |
| 4    | Cấu hình Amazon S3 làm đích đầu ra                    |
| 5    | Thiết lập thuộc tính job và IAM role                  |
| 6    | Chạy job và xác minh kết quả trên S3                  |

Trong phần tiếp theo, chúng ta sẽ dùng **Amazon Athena** để truy vấn dữ liệu đã xử lý trực tiếp từ Amazon S3 bằng metadata lưu trong Glue Data Catalog.
