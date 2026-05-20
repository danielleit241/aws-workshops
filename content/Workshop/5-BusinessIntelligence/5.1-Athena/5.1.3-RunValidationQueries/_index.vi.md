---
title: "Chạy Truy Vấn Kiểm Tra"
date: "2026-05-20"
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

Khi Athena đã kết nối với Glue catalog, bạn có thể xác nhận dataset đã xử lý bằng một truy vấn SQL đơn giản.

## Bước 1: Chạy Truy Vấn Mẫu

Sử dụng câu lệnh SQL sau:

```sql
SELECT *
FROM quarantine_yellow_taxi_trip_data
LIMIT 5;
```

Nhập truy vấn vào Athena và chọn **Run**.

![Enter the first Athena validation query](/images/Workshop/5.1%20Athena/38.png)

## Bước 2: Kiểm Tra Kết Quả

Nếu cấu hình chính xác, Athena sẽ trả về các dòng dữ liệu mẫu từ bảng đã xử lý.

![Successful Athena query results](/images/Workshop/5.1%20Athena/39.png)

Tại thời điểm này, bạn đã xác nhận rằng:

- Athena có thể truy cập metadata trong Glue catalog
- Bảng taxi-trip đã xử lý có thể đọc được
- Lớp truy vấn BI đã sẵn sàng cho các phân tích sâu hơn
