---
title: "Thiết lập Hệ thống Cảnh báo với Amazon SNS"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

### Các bước cấu hình Amazon SNS

Chúng ta sẽ thực hiện một bài kiểm tra nhanh (Test Run) để đảm bảo tài khoản của bạn đã sẵn sàng. Và thực hiện các bước set-up cho AWS SNS. 

**Bước 1: Truy cập AWS Console**

Đầu tiên ở thanh tìm kiếm, truy cập vào [Amazon Simple Notification Service](https://console.aws.amazon.com/sns/home) 

![3.1.1](/images/Workshop/3-Monitoring&Security/3.1.1.svg)

**Bước 2: Truy cập Topics**

Tại menu bên trái, chọn **Topics -> Create topic**

![3.1.2](/images/Workshop/3-Monitoring&Security/3.1.2.svg)

**Bước 3: Cấu hình Topics**

- **Type:** Chọn **Standard**.

- **Name:** `SNS Alerts`

- Giữ **Default** các cấu hình còn lại

![3.1.3](/images/Workshop/3-Monitoring&Security/3.1.3.svg)

- Cuộn xuống và chọn **Create topic**.

![3.1.4](/images/Workshop/3-Monitoring&Security/3.1.4.svg)

- Kiểm tra đã tạo **Topics** thành công.

![3.1.5](/images/Workshop/3-Monitoring&Security/3.1.5.svg)

**Bước 4: Truy cập Subcriptions**

Tại menu bên trái, chọn tab **Subcriptions -> Create Subcriptions**

![3.1.6](/images/Workshop/3-Monitoring&Security/3.1.6.svg)


**Bước 5: Cấu hình Subcriptions**

- **Topics ARN:** Chọn **SNS-Alerts** đã được tạo trước đó
- **Protocol:** Chọn **Email**.
- **Endpoint:** Nhập địa chỉ email của bạn. 
- Nhấn **Create subscription**.

![3.1.7](/images/Workshop/3-Monitoring&Security/3.1.7.svg)


- **Xác thực**: Mở hộp thư email của bạn, tìm thư từ **AWS Notification**, thông báo sẽ thường hay nằm trong mục Thư rác.
- Nhấn **Confirm subscription** để kích hoạt kênh. 

![3.1.8](/images/Workshop/3-Monitoring&Security/3.1.8.svg)

- Nhận thông báo **Xác thực thành công**.

![3.1.9](/images/Workshop/3-Monitoring&Security/3.1.9.svg)


**Bước 6: Kiếm tra Status của Subcriptions đã được chuyển sang Confirmed**

![3.1.10](/images/Workshop/3-Monitoring&Security/3.1.10.svg)


**Chúc mừng bạn đã hoàn thành bước setup AWS SNS.**

