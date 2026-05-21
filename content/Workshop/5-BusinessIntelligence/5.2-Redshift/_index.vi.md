---
title: "Redshift"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

Trong phần này, chúng ta giới thiệu **Amazon Redshift Spectrum** như lựa chọn phân tích tiếp theo sau Athena để truy vấn dữ liệu đã được curate trong data lake.

Amazon Redshift Spectrum mở rộng **Amazon Redshift** để các truy vấn SQL có thể truy cập trực tiếp dữ liệu lưu trong **Amazon S3**. Trong workshop này, Spectrum hoạt động cùng với **AWS Glue Data Catalog**, cho phép Redshift hiểu các external table mà không cần phải nạp toàn bộ dataset vào storage của data warehouse trước.

### Vì Sao Redshift Spectrum Quan Trọng

Athena rất phù hợp cho việc khám phá dữ liệu nhanh theo mô hình serverless. Tuy nhiên, nhiều nhóm phân tích còn cần một môi trường theo hướng data warehouse hơn để hỗ trợ workflow SQL rộng hơn, công cụ truy vấn dùng chung, và tích hợp với các nền tảng BI phía sau.

Redshift Spectrum giúp kết nối hai nhu cầu đó bằng cách kết hợp:

- **Phân tích SQL theo phong cách data warehouse**
- **Truy cập trực tiếp dữ liệu data lake trên S3**
- **Tái sử dụng metadata từ AWS Glue Data Catalog**
- **Khả năng tích hợp với các công cụ báo cáo và BI**

{{% notice info %}}
Redshift Spectrum không thay thế Glue pipeline. Nó sử dụng dữ liệu đầu ra đã xử lý và metadata catalog được tạo ở các bước trước trong workshop.
{{% /notice %}}

### Redshift Spectrum Phù Hợp Với Workshop Này Như Thế Nào

Sơ đồ dưới đây cho thấy Redshift Spectrum nằm ở đâu trong kiến trúc workshop và luồng truy vấn:

![Redshift Spectrum Workflow](/images/Workshop/5.2-Redshift/1-Overview/3-Flows/redshift_spectrum_workflow.png)

Điều đó có nghĩa là:

- **Amazon S3** vẫn là lớp lưu trữ dữ liệu
- **AWS Glue Data Catalog** cung cấp schema và metadata của bảng
- **Redshift Spectrum** truy vấn dữ liệu external thông qua giao diện SQL của Redshift

### Bạn Sẽ Làm Gì Trong Phần Này

Trong các bước thực hành tiếp theo, bạn sẽ:

1. Xem các khái niệm cốt lõi của Redshift Spectrum
2. Thiết lập **Amazon Redshift Serverless**
3. Kết nối với **Query Editor v2**
4. Tạo **external schema** liên kết với Glue Data Catalog
5. Truy vấn các external table được Glue quản lý từ Redshift
6. Xem các lỗi thường gặp, lưu ý về chi phí, và hướng dẫn cleanup

### Lợi Ích Khi Sử Dụng Redshift Spectrum

| Lợi ích | Giải thích |
|---|---|
| External Querying | Truy vấn dữ liệu trên S3 mà không cần nạp hết vào bảng Redshift |
| Glue Integration | Tái sử dụng schema đã được khám phá trong Data Catalog |
| Familiar SQL Experience | Dùng công cụ truy vấn Redshift và workflow quen thuộc theo hướng warehouse |
| Scalable Analytics | Hỗ trợ các workload phân tích lớn hơn trên dữ liệu đã được curate |
| BI Readiness | Chuẩn bị pattern truy cập dữ liệu phù hợp với các công cụ báo cáo |

### Redshift Spectrum So Với Athena

Athena và Redshift Spectrum đều có thể truy vấn dữ liệu trong Amazon S3, nhưng chúng thường phù hợp với các tình huống khác nhau:

- Dùng **Athena** khi bạn cần phân tích SQL ad-hoc, trực tiếp và gọn nhẹ
- Dùng **Redshift Spectrum** khi bạn muốn workflow phân tích theo hướng warehouse hơn
- Dùng **QuickSight** khi bạn muốn dashboard và trực quan hóa thay vì kết quả truy vấn thô

Ba dịch vụ này cùng cho thấy một dataset đã được curate có thể được khai thác theo nhiều mô hình tiêu thụ dữ liệu khác nhau.

### Kết Quả Học Tập

Sau khi hoàn thành phần này, bạn nên hiểu:

- Amazon Redshift Spectrum là gì
- Redshift Spectrum tích hợp với Amazon S3 và AWS Glue Data Catalog như thế nào
- Vì sao Redshift Spectrum bổ sung tốt cho Athena trong lớp BI
- Amazon Redshift Serverless có thể được dùng ra sao để truy vấn dữ liệu đầu ra từ data lake
