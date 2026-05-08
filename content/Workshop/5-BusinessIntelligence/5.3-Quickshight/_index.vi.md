---
title: "QuickSight"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

# Amazon QuickSight Visualization cho Data Pipeline with AWS Glue

Sau khi hoàn tất quá trình xây dựng hệ thống Data Pipeline trên AWS với các thành phần như Amazon S3, AWS Glue ETL, AWS Glue Data Catalog và Amazon Redshift, bước tiếp theo là trực quan hóa dữ liệu bằng Amazon QuickSight nhằm phục vụ mục đích phân tích và xây dựng dashboard.

Trong hệ thống này:

* Dữ liệu raw được lưu trữ trên Amazon S3.
* AWS Glue Crawler thực hiện quét dữ liệu và tạo metadata.
* AWS Glue Data Catalog quản lý schema dữ liệu.
* AWS Glue ETL Job xử lý và transform dữ liệu.
* Dữ liệu processed được lưu vào Amazon Redshift.
* Amazon QuickSight kết nối tới Redshift để xây dựng dashboard phân tích dữ liệu.

---

# Vai trò của Amazon QuickSight trong hệ thống

Amazon QuickSight là dịch vụ Business Intelligence (BI) trên AWS dùng để trực quan hóa dữ liệu.

Trong pipeline này, QuickSight sẽ:

* Kết nối trực tiếp tới Amazon Redshift.
* Đọc dữ liệu đã được xử lý bởi Glue ETL Job.
* Hỗ trợ tạo dashboard analytics.
* Phân tích dữ liệu taxi trip và transaction.
* Theo dõi revenue, passenger count, trip distance và pickup time.

---

# Bước 1: Tạo tài khoản Amazon QuickSight

Đầu tiên cần kích hoạt dịch vụ Amazon QuickSight trên AWS Account.

## Thực hiện

1. Truy cập AWS Console.
2. Tìm kiếm dịch vụ:

```text
QuickSight
```

3. Chọn Amazon QuickSight.
4. Nhấn:

```text
Sign up for QuickSight
```

Ở bước này hệ thống sẽ hiển thị giao diện tạo tài khoản QuickSight lần đầu.

![Đăng ký QuickSight](/images/Workshop/5.3%20Quicksight/5.3.1.jpg)

---

# Bước 2: Hoàn tất tạo tài khoản QuickSight

Sau khi điền các thông tin như:

* Account name
* Notification email
* Edition
* AWS service permissions

Hệ thống sẽ hoàn tất quá trình khởi tạo Amazon QuickSight.

Tại đây người dùng sẽ được chuyển tới giao diện quản trị chính của QuickSight.

![Kết quả tạo tài khoản](/images/Workshop/5.3%20Quicksight/5.3.2.jpg)

---

# Bước 3: Nhập thông tin kết nối Amazon Redshift

Sau khi tạo QuickSight thành công, bước tiếp theo là tạo Data Source để kết nối tới Amazon Redshift.

Trong giao diện tạo Data Source, chọn:

```text
Amazon Redshift
```

Sau đó nhập các thông tin kết nối bao gồm:

| Trường | Ý nghĩa |
|---|---|
| Data source name | Tên Data Source |
| Connection type | Public network hoặc VPC |
| Server | Endpoint của Redshift |
| Port | Port Redshift |
| Database | Tên database |
| Username | Tài khoản đăng nhập |
| Password | Mật khẩu đăng nhập |

Ví dụ:

```text
Data source name: glue-pipeline-redshift
Connection type: Public network
Server: redshift-cluster.xxxxxx.ap-southeast-1.redshift.amazonaws.com
Port: 5439
Database: dev
Username: admin
Password: ********
```

![Nhập thông tin kết nối](/images/Workshop/5.3%20Quicksight/5.3.3.jpg)

---

# Bước 4: Hoàn tất cấu hình Data Source

Sau khi điền đầy đủ các thông tin kết nối Redshift:

1. Nhấn:

```text
Validate connection
```

2. Nếu kết nối thành công hệ thống sẽ xác nhận kết nối hợp lệ.
3. Tiếp tục nhấn:

```text
Create data source
```

để tạo Data Source cho QuickSight.

![Tạo Data Source](/images/Workshop/5.3%20Quicksight/5.3.4.jpg)

---

# Bước 5: Chọn Schema và Table dữ liệu

Sau khi kết nối thành công tới Redshift, QuickSight sẽ hiển thị danh sách:

* Database
* Schema
* Tables
* Views

Trong bước này:

1. Chọn schema:

```text
public
```

2. Chọn bảng dữ liệu đã được ETL từ AWS Glue.

Ví dụ:

```text
yellow_taxi_trip
```

![Nhập thông tin kết nối](/images/Workshop/5.3%20Quicksight/5.3.5.jpg)

---

# Bước 6: Xác nhận Dataset

Sau khi chọn table:

1. Nhấn:

```text
Select
```

2. QuickSight sẽ tạo dataset từ bảng dữ liệu trong Redshift.
3. Dataset này sẽ được sử dụng để tạo visualization và dashboard.

![Xác nhận tạo dataset](/images/Workshop/5.3%20Quicksight/5.3.6.jpg)

---

# Ví dụ Dataset sử dụng trong hệ thống

Dataset sử dụng trong dự án có thể bao gồm các trường:

| Column |
|---|
| VendorID |
| tpep_pickup_datetime |
| tpep_dropoff_datetime |
| passenger_count |
| trip_distance |
| RatecodeID |
| payment_type |
| fare_amount |
| tip_amount |
| total_amount |
| congestion_surcharge |
| Airport_fee |

---

# Bước 7: Tạo Visualization đầu tiên

Sau khi dataset được load thành công:

1. Chọn loại biểu đồ phù hợp.
2. Kéo thả các field từ panel bên trái vào khu vực visualization.

Ví dụ:

* X-axis: `payment_type`
* Value: `sum(total_amount)`

để tạo biểu đồ doanh thu theo hình thức thanh toán.

![Chọn bảng](/images/Workshop/5.3%20Quicksight/5.3.7.jpg)

---

# Bước 8: Tổ hợp Field để trực quan hóa dữ liệu

QuickSight cho phép người dùng kéo thả field nhằm tạo nhiều dạng biểu đồ khác nhau.

Ví dụ:

* `tpep_pickup_datetime`
* `fare_amount`
* `trip_distance`
* `passenger_count`

được sử dụng để xây dựng biểu đồ phân tích dữ liệu taxi trip.

![Xác nhận bảng dữ liệu](/images/Workshop/5.3%20Quicksight/5.3.8.jpg)

---

# Bước 9: Tạo Dashboard Analytics

Sau khi cấu hình visualization:

* Có thể thay đổi chart type.
* Tạo filter.
* Thêm KPI.
* Gom nhiều biểu đồ vào cùng dashboard.

Một số loại chart phổ biến:

* Bar Chart
* Line Chart
* Pie Chart
* KPI
* Area Chart
* Heatmap

![Cấu hình Visualize](/images/Workshop/5.3%20Quicksight/5.3.9.jpg)

---

# Bước 10: Hoàn thiện Dashboard trực quan hóa dữ liệu

Sau khi hoàn tất việc kéo thả field và cấu hình biểu đồ, hệ thống sẽ tạo dashboard phục vụ phân tích dữ liệu.

Dashboard có thể hỗ trợ:

* Phân tích doanh thu.
* Theo dõi tổng số chuyến đi.
* Phân tích passenger count.
* Theo dõi pickup time.
* Thống kê trip distance.
* Theo dõi payment type.

![Hoàn thành tạo biểu đồ](/images/Workshop/5.3%20Quicksight/5.3.10.jpg)

---

# Một số lỗi thường gặp

# 1. Không kết nối được Redshift

## Nguyên nhân

* Sai endpoint.
* Security Group chưa mở port 5439.
* Redshift đang private subnet.

## Cách xử lý

* Kiểm tra endpoint.
* Mở inbound port 5439.
* Kiểm tra Publicly Accessible.

---

# 2. Không hiển thị table

## Nguyên nhân

* User thiếu quyền SELECT.
* Glue ETL chưa load dữ liệu.
* Sai schema.

## Cách xử lý

```sql
GRANT SELECT ON ALL TABLES IN SCHEMA public TO username;
```

---

# 3. Visualization hiển thị null

## Nguyên nhân

* Dữ liệu ETL lỗi.
* Datatype không phù hợp.
* Dataset chưa refresh.

## Cách xử lý

* Refresh dataset.
* Kiểm tra Glue ETL Job.
* Verify datatype trong Redshift.

---

# Kết quả đạt được

Sau khi hoàn tất:

* AWS Glue xử lý dữ liệu thành công.
* Dữ liệu được load vào Amazon Redshift.
* Amazon QuickSight kết nối thành công với Data Warehouse.
* Dashboard trực quan hóa dữ liệu được xây dựng hoàn chỉnh.
* Hệ thống hỗ trợ analytics và business intelligence hiệu quả.

Pipeline hoàn chỉnh:

```text
Raw Data → Glue ETL → Redshift → QuickSight
```