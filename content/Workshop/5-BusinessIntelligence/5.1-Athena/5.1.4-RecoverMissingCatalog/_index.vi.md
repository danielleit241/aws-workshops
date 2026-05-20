---
title: "Khôi Phục Catalog Bị Thiếu"
date: "2026-05-20"
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

Trang này là **tùy chọn**. Chỉ dùng khi database hoặc table dự kiến trong Glue không xuất hiện trong Athena, hoặc khi schema bị sai.

## Khôi Phục A: Tạo Glue Database

Nếu database của workshop chưa tồn tại, hãy tạo nó trong AWS Glue.

![Create Glue database for Athena](/images/Workshop/5.1%20Athena/24.png)

## Khôi Phục B: Chạy Glue Crawler

Nếu metadata của table còn thiếu, hãy chạy crawler để quét vị trí S3 của dữ liệu đã xử lý.

![Run the Glue crawler](/images/Workshop/5.1%20Athena/28.png)

Chờ đến khi crawler hoàn tất thành công.

![Crawler completed successfully](/images/Workshop/5.1%20Athena/30.png)

## Khôi Phục C: Kiểm Tra Schema

Nếu table đã xuất hiện nhưng schema không nhất quán, hãy mở định nghĩa table trong Glue và kiểm tra schema.

![Open the Glue table schema](/images/Workshop/5.1%20Athena/33.png)

Nếu bạn sửa các trường không hợp lệ hoặc bị trùng lặp, hãy lưu một phiên bản schema mới.

![Save the corrected table schema](/images/Workshop/5.1%20Athena/37.png)

{{% notice warning %}}
Chỉ áp dụng luồng khôi phục này khi output bình thường của Glue pipeline bị thiếu hoặc không chính xác.
{{% /notice %}}
