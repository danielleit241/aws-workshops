---
title: "Kiểm soát chi phí và dọn dẹp"
date: "2026-05-02"
weight: 7
chapter: false
pre: " <b> 2.7. </b> "
---

Redshift Serverless có khoản credit dùng thử miễn phí $300 trong 90 ngày dành cho các tài khoản chưa từng sử dụng Redshift Serverless trước đó.

- Khoản credit này tách biệt với AWS Free Tier $200
- Áp dụng cho mức sử dụng compute (RPU-hours)
- Tự động hết hạn sau 90 ngày hoặc khi dùng hết $300
![Redshift Serverless free trial](/images/Workshop/5.2-Redshift/3-QueryEditorV2/1-Connect/query-editor-v2-connected.png)
![Redshift Serverless free trial](/images/Workshop/5.2-Redshift/7-CostControl/1-FreeTrial/redshift-freetrial.png)

# Kiểm soát chi phí

## Capacity

- Dùng base capacity thấp (4 RPU) cho phần thực hành
- Chỉ tăng khi cần chạy truy vấn nặng, sau đó giảm lại ngay
- Theo dõi mức sử dụng trong Redshift console

## Tối ưu truy vấn

- Dùng `LIMIT` trong các truy vấn kiểm thử
- Lọc theo partition (`year`, `month`) để giảm lượng dữ liệu phải scan
- Tránh các truy vấn toàn bộ dataset khi không cần thiết

# Dọn dẹp tài nguyên

Sau khi hoàn thành workshop:

1. **Xóa Redshift workgroup và namespace**:
   - Redshift console → Serverless dashboard
   - Chọn workgroup → Delete
   - Chọn namespace → Delete

2. **Xóa các tài nguyên Glue** (nếu không còn cần):
   - Crawlers: `glue-crawler-processed-yellow-taxi`
   - Databases: `redshift_database`
   - Tables: `processed_yellow_taxi_trip_data`

3. **Xóa các IAM role**:
   - `AmazonRedshift-CommandsAccessRole-...`
   - `glue-role-manhattan-processed-crawler`

4. **Làm trống các bucket S3** nếu không còn cần dữ liệu (nhưng giữ lại nếu vẫn dùng cho ETL pipeline)

# Lưu ý

- Redshift Serverless chỉ tính phí khi truy vấn đang chạy
- Nếu workgroup vẫn tồn tại dù không sử dụng, vẫn có thể phát sinh một khoản phí nhỏ
- Theo dõi Billing console để kiểm soát mức sử dụng
