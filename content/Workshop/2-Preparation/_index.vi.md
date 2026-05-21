---
title: "Preparation"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

### Tổng quan

Trong phần này, chúng ta sẽ thiết lập tất cả các tài nguyên AWS cần thiết trước khi bắt đầu workshop chính. Bao gồm việc tạo S3 bucket để lưu trữ bộ dữ liệu thô, tải lên dữ liệu TLC Yellow Taxi trip và xác minh rằng các quyền cần thiết đã được cấu hình đúng.

Sau khi hoàn thành phần này, bạn sẽ có thể:

- Tạo Amazon S3 bucket để lưu trữ bộ dữ liệu thô
- Tải lên dữ liệu TLC Yellow Taxi trip ở định dạng Parquet
- Xác minh các tệp đã tải lên trong S3 console
- Xác nhận rằng tài khoản AWS của bạn có đủ quyền để tiếp tục



### Điều kiện tiên quyết

Trước khi bắt đầu, hãy đảm bảo bạn có những thứ sau:

- Một **tài khoản AWS** đang hoạt động với đủ quyền để tạo S3 bucket và IAM role
- **AWS Management Console** có thể truy cập trên trình duyệt của bạn
- **Bộ dữ liệu TLC Yellow Taxi trip** ở định dạng Parquet, sẵn sàng để tải lên

{{% notice info %}}
Nếu bạn chưa có bộ dữ liệu, bạn có thể tải mẫu từ [trang TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).  
Trong workshop này, chúng tôi khuyến nghị sử dụng dữ liệu Yellow Taxi trip của một tháng bất kỳ ở định dạng Parquet.
{{% /notice %}}

### Cấu hình

Trong workshop này, chúng ta sẽ dùng cấu hình mẫu sau.

| Tài nguyên      | Giá trị                           |
| --------------- | --------------------------------- |
| S3 Bucket Name  | `yellow-taxi-trip-demo-fcaj`      |
| AWS Region      | `ap-southeast-1` (Singapore)      |
| Dataset Format  | Parquet                           |
| Folder Path     | `/` (bucket root)                 |

Bạn có thể điều chỉnh tên bucket và region theo môi trường AWS của riêng bạn.

---

**Bước 1: Đăng nhập vào AWS Management Console**

1. Mở trình duyệt và truy cập [https://console.aws.amazon.com](https://console.aws.amazon.com)
2. Đăng nhập bằng thông tin tài khoản AWS của bạn
3. Ở góc trên bên phải, xác nhận rằng bạn đang ở đúng **AWS Region** (ví dụ: `ap-southeast-1`)

{{% notice tip %}}
Bạn có thể thay đổi region bằng cách nhấn vào tên region ở góc trên bên phải của console và chọn region mong muốn từ danh sách thả xuống.
{{% /notice %}}

---

**Bước 2: Tạo Amazon S3 Bucket**

1. Trong AWS Management Console, tìm kiếm **S3** trên thanh tìm kiếm và mở dịch vụ S3
2. Nhấn **Create bucket**
3. Trong phần **Bucket name**, nhập tên duy nhất cho bucket của bạn (ví dụ: `yellow-taxi-trip-demo-fcaj`)

{{% notice info %}}
Tên S3 bucket phải là duy nhất trên toàn bộ tài khoản AWS. Nếu tên đã được sử dụng, hãy thử thêm hậu tố như chữ viết tắt tên bạn hoặc một số ngẫu nhiên.
{{% /notice %}}

4. Trong phần **AWS Region**, chọn region bạn đang dùng cho workshop này (ví dụ: `ap-southeast-1`)
5. Giữ nguyên tất cả các cài đặt còn lại theo mặc định
6. Cuộn xuống và nhấn **Create bucket**

Sau khi bucket được tạo, nó sẽ xuất hiện trong danh sách S3 bucket của bạn.

---

**Bước 3: Tải bộ dữ liệu lên S3**

1. Nhấn vào tên bucket vừa tạo để mở bucket đó
2. Nhấn **Upload**
3. Nhấn **Add files** và chọn tệp Parquet từ máy tính của bạn

{{% notice tip %}}
Nếu bộ dữ liệu của bạn được chia thành nhiều tệp Parquet trong một thư mục, bạn có thể nhấn **Add folder** để tải lên toàn bộ thư mục cùng một lúc. AWS Glue Crawler có thể quét tất cả các tệp trong một đường dẫn thư mục.
{{% /notice %}}

4. Xem lại danh sách các tệp sẽ được tải lên
5. Giữ nguyên tất cả các cài đặt còn lại theo mặc định
6. Nhấn **Upload** để bắt đầu quá trình tải lên
7. Chờ quá trình tải lên hoàn tất. Trạng thái sẽ hiển thị **Succeeded** khi hoàn thành.

---

**Bước 4: Xác minh các tệp đã tải lên**

1. Sau khi tải lên hoàn tất, quay lại giao diện bucket
2. Xác nhận rằng các tệp Parquet xuất hiện trong bucket

Bạn sẽ thấy các tệp đã tải lên được liệt kê cùng với kích thước tệp và ngày chỉnh sửa lần cuối.

{{% notice info %}}
Nếu bạn đã tải lên một thư mục, hãy nhấn vào thư mục đó để xác nhận các tệp Parquet có bên trong.  
Đường dẫn S3 sẽ trông giống như: `s3://yellow-taxi-trip-demo-fcaj/yellow_tripdata_2024-01.parquet`
{{% /notice %}}

---

**Bước 5: Xác minh quyền tài khoản**

Trước khi chuyển sang phần tiếp theo, hãy xác nhận rằng tài khoản AWS của bạn có đủ quyền cần thiết cho workshop này.

Tối thiểu, tài khoản của bạn cần có quyền truy cập vào:

- **Amazon S3** — để đọc và ghi dữ liệu
- **AWS Glue** — để tạo crawler, database và ETL job
- **AWS IAM** — để tạo và gắn role và policy
- **Amazon Athena** — để chạy truy vấn SQL trên dữ liệu S3
- **Amazon CloudWatch** — để xem log từ Glue job

{{% notice tip %}}
Nếu bạn đang dùng IAM user hoặc role với quyền hạn chế, hãy nhờ quản trị viên AWS của bạn gắn policy `AdministratorAccess` trong thời gian diễn ra workshop, hoặc đảm bảo các quyền dịch vụ cụ thể được liệt kê ở trên đã được cấp.
{{% /notice %}}

---

### Tổng kết

Trong phần này, chúng ta đã chuẩn bị môi trường AWS cho workshop.

| Bước | Thao tác                                                       |
| ---- | -------------------------------------------------------------- |
| 1    | Đăng nhập vào AWS Management Console                           |
| 2    | Tạo Amazon S3 bucket                                           |
| 3    | Tải lên bộ dữ liệu TLC Yellow Taxi ở định dạng Parquet         |
| 4    | Xác minh các tệp đã tải lên trong S3 console                   |
| 5    | Xác nhận các quyền tài khoản cần thiết                         |

Bộ dữ liệu thô hiện đã được lưu trong Amazon S3 và sẵn sàng để xử lý. Trong phần tiếp theo, chúng ta sẽ thiết lập các tài nguyên **Monitoring và Security** trước khi xây dựng analytics pipeline.
