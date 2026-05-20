---
title: "Mở Athena Và Duyệt Catalog"
date: "2026-05-20"
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

Sau khi Athena đã có nơi lưu kết quả, bước tiếp theo là mở giao diện truy vấn và xác nhận rằng các đối tượng Glue catalog của dữ liệu đã xử lý đang hiển thị đúng.

## Bước 1: Mở Amazon Athena

Từ AWS Console, tìm **Athena** và mở dịch vụ.

![Open Amazon Athena](/images/Workshop/5.1%20Athena/5.png)

Chọn **Launch query editor**.

![Launch Athena Query Editor](/images/Workshop/5.1%20Athena/6.png)

## Bước 2: Xác Nhận Glue Database

Trong thanh bên trái:

- Giữ **Data source** là `AwsDataCatalog`
- Chọn database của workshop

![Choose the workshop database in Athena](/images/Workshop/5.1%20Athena/31.png)

## Bước 3: Xác Nhận Bảng Dữ Liệu Đã Xử Lý

Sau khi chọn đúng database, bảng dữ liệu đã xử lý sẽ xuất hiện trong danh sách bảng.

![Verify the processed table is available](/images/Workshop/5.1%20Athena/32.png)

Nếu database hoặc table của bạn không xuất hiện, hãy chuyển sang trang khôi phục trước khi thử chạy truy vấn.
