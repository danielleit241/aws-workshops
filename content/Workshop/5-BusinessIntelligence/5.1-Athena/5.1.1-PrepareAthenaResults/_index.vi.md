---
title: "Chuẩn Bị Kết Quả Athena"
date: "2026-05-20"
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

Trước khi Athena có thể chạy truy vấn, nó cần một **vị trí đầu ra trên Amazon S3** để lưu kết quả truy vấn.

Trong trang này, bạn sẽ tạo bucket đó và kết nối nó với Athena.

## Bước 1: Mở Amazon S3

Từ AWS Console, tìm **Amazon S3** và mở dịch vụ.

![Open Amazon S3](/images/Workshop/5.1%20Athena/1.png)

## Bước 2: Tạo Bucket Riêng Cho Kết Quả

Trong danh sách bucket của S3, chọn **Create bucket**.

![Create bucket from S3 console](/images/Workshop/5.1%20Athena/2.png)

Tạo một **general purpose bucket** và đặt tên riêng để lưu kết quả truy vấn Athena.

![Configure bucket type and name](/images/Workshop/5.1%20Athena/3.png)

Sau khi kiểm tra các thiết lập mặc định, kéo xuống dưới và chọn **Create bucket**.

![Finalize Athena result bucket creation](/images/Workshop/5.1%20Athena/4.png)

## Bước 3: Cấu Hình Output Cho Athena

Sau khi bucket đã sẵn sàng, mở Athena Query Editor và chọn **Edit settings**.

![Open Athena settings](/images/Workshop/5.1%20Athena/7.png)

Chọn bucket S3 mà bạn vừa tạo để lưu kết quả truy vấn, sau đó lưu cấu hình.

![Save Athena query result location](/images/Workshop/5.1%20Athena/11.png)

Athena sẽ xác nhận rằng vị trí lưu kết quả đã được cập nhật thành công.

![Verify Athena query settings](/images/Workshop/5.1%20Athena/12.png)

{{% notice tip %}}
Athena không thể chạy truy vấn cho đến khi output location trên S3 được cấu hình.
{{% /notice %}}
