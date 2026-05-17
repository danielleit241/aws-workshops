---
title: "Monitoring & Security"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

### Mục tiêu 

Trong kiến trúc Data Pipeline, việc dữ liệu được lưu chuyển từ ***Nguồn (S3) -> Xử lý (Glue ETL) -> Phân tích (Athena/Redshift)*** đòi hỏi một cơ chế bảo mật và giám sát chặt chẽ. Mục tiêu của phần này nhằm giúp người học:

1. **Quản lý quyền truy cập (AWS IAM):** Đảm bảo nguyên tắc đặc quyền tối thiểu (Least Privilege). Cấp phát chính xác các Roles cần thiết để AWS Glue và Redshift có thể giao tiếp an toàn với S3 Data Lake.

2. **Kiểm toán và Ghi vết (AWS CloudTrail):** Theo dõi và ghi nhận lại mọi thao tác (API Calls) tương tác với hệ thống, giúp truy vết nhanh chóng khi có hành vi cấu hình sai hoặc truy cập trái phép.

3. **Giám sát trạng thái Pipeline (Amazon CloudWatch / EventBridge):** Nắm bắt tình trạng của hệ thống theo thời gian thực. Bắt các luồng sự kiện (Events) quan trọng như khi một tiến trình chạy dữ liệu hoàn thành hoặc thất bại.

4. **Cảnh báo tự động (Amazon SNS):** Tự động hóa việc phân phối thông báo (qua Email/SMS) cho đội ngũ Data Engineer/Admin ngay khi Data Pipeline gặp sự cố.

### Luồng hoạt động Security & Monitoring

1. [Thiết lập Hệ thống Cảnh báo với Amazon SNS](/content/Workshop/3-MonitoringSecurity/3.1-AWS_SNS/_index.vi.md)
2. [Tạo IAM Role cho AWS Glue](/content/Workshop/3-MonitoringSecurity/3.2-AWS_IAM/_index.vi.md)
3. [Ghi vết Hệ thống với AWS CloudTrail](/content/Workshop/3-MonitoringSecurity/3.3-AWS_CloudTrail/_index.vi.md) 
4. [Thiết lập Báo động Lỗi Data Pipeline với Amazon EventBridge (CloudWatch)](/content/Workshop/3-MonitoringSecurity/3.4-AWS_EventBridge_(CloudWatch)/_index.vi.md)



