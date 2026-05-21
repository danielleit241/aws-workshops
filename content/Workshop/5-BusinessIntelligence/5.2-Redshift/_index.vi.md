---
title: "Redshift"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

Trong phần này, chúng ta giới thiệu **Amazon Redshift Spectrum** như lựa chọn phân tích tiếp theo sau Athena để truy vấn dữ liệu đã được xử lý trong data lake.

Amazon Redshift Spectrum mở rộng **Amazon Redshift** để các truy vấn SQL có thể truy cập trực tiếp dữ liệu được lưu trong **Amazon S3**. Trong workshop này, Spectrum hoạt động cùng với **AWS Glue Data Catalog**, giúp Redshift hiểu được các external table mà không cần nạp toàn bộ dataset vào kho dữ liệu trước.

### Vì sao Redshift Spectrum quan trọng

Athena rất phù hợp cho việc khám phá dữ liệu nhanh theo mô hình serverless. Tuy nhiên, nhiều nhóm phân tích cũng cần một môi trường thiên về data warehouse hơn để hỗ trợ các quy trình SQL rộng hơn, các công cụ truy vấn dùng chung, và khả năng tích hợp với những nền tảng BI ở bước sau.

Redshift Spectrum giúp lấp khoảng trống đó bằng cách kết hợp:

- **Phân tích SQL theo phong cách data warehouse**
- **Truy cập trực tiếp vào các tệp data lake trên S3**
- **Tái sử dụng metadata từ AWS Glue Data Catalog**
- **Tích hợp với các công cụ báo cáo và BI**

{{% notice info %}}
Redshift Spectrum không thay thế pipeline Glue. Nó sử dụng dữ liệu đầu ra đã được xử lý và metadata catalog được tạo ở các phần trước của workshop.
{{% /notice %}}

### Redshift Spectrum phù hợp với workshop này như thế nào

Sơ đồ dưới đây cho thấy Redshift Spectrum nằm ở đâu trong kiến trúc workshop và luồng truy vấn:

![Redshift Spectrum Workflow](/images/Workshop/5.2-Redshift/1-Overview/3-Flows/redshift_spectrum_workflow.png)

Điều đó có nghĩa là:

- **Amazon S3** vẫn là lớp lưu trữ
- **AWS Glue Data Catalog** cung cấp schema và metadata của bảng
- **Redshift Spectrum** truy vấn dữ liệu external thông qua giao diện SQL của Redshift

### Bạn sẽ làm gì trong phần này

Trong các bước thực hành tiếp theo, bạn sẽ:

1. Xem lại các khái niệm cốt lõi của Redshift Spectrum
2. Thiết lập **Amazon Redshift Serverless**
3. Kết nối tới **Query Editor v2**
4. Tạo **external schema** liên kết với Glue Data Catalog
5. Truy vấn các external table do Glue quản lý từ Redshift
6. Xem lại các lỗi thường gặp, chi phí cần lưu ý, và hướng dẫn dọn dẹp tài nguyên

### Lợi ích của Redshift Spectrum

| Lợi ích | Giải thích |
|---|---|
| Truy vấn dữ liệu external | Truy vấn dữ liệu trên S3 mà không cần nạp toàn bộ vào bảng Redshift |
| Tích hợp Glue | Tái sử dụng schema đã được phát hiện trong Data Catalog |
| Trải nghiệm SQL quen thuộc | Sử dụng công cụ truy vấn của Redshift và workflow kiểu data warehouse |
| Phân tích có khả năng mở rộng | Hỗ trợ các workload phân tích lớn hơn trên những dataset đã được xử lý |
| Sẵn sàng cho BI | Chuẩn bị mô hình truy cập dữ liệu phù hợp để kết nối với công cụ báo cáo |

### Redshift Spectrum và Athena

Athena và Redshift Spectrum đều truy vấn dữ liệu trong Amazon S3, nhưng chúng thường được dùng trong các tình huống khác nhau:

- Dùng **Athena** cho phân tích SQL trực tiếp, nhẹ, mang tính ad-hoc
- Dùng **Redshift Spectrum** khi bạn muốn một workflow phân tích thiên về data warehouse hơn
- Dùng **QuickSight** khi bạn muốn xây dựng dashboard và trực quan hóa kết quả phân tích

Kết hợp lại, chúng cho thấy cùng một dataset đã được xử lý có thể phục vụ nhiều kiểu tiêu thụ dữ liệu khác nhau.

### Kết quả học tập

Sau khi hoàn thành phần này, bạn sẽ hiểu:

- Amazon Redshift Spectrum là gì
- Cách nó tích hợp với Amazon S3 và AWS Glue Data Catalog
- Vì sao nó bổ trợ cho Athena trong lớp BI
- Cách Redshift Serverless được dùng để truy vấn dữ liệu đầu ra đã xử lý trong data lake
