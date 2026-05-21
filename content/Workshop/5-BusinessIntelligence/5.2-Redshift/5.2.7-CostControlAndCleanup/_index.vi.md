---
title: "Kiểm soát chi phí và dọn dẹp"
date: "2026-05-02"
weight: 7
chapter: false
pre: " <b> 2.7. </b> "
---

Redshift Serverless có $300 credit free trial trong 90 ngày cho tài khoản chưa từng dùng Redshift Serverless.

- Credit này riêng biệt với AWS Free Tier $200
- Áp dụng cho compute usage (RPU-hours)
- Tự động hết sau 90 ngày hoặc khi dùng hết $300
![Redshift Serverless free trial](/images/Workshop/5.2-Redshift/3-QueryEditorV2/1-Connect/query-editor-v2-connected.png)
![Redshift Serverless free trial](/images/Workshop/5.2-Redshift/7-CostControl/1-FreeTrial/redshift-freetrial.png)

# Kiểm soát chi phí

## Capacity

- Sử dụng base capacity thấp (4 RPU) cho hand-on
- Tăng lên khi cần query nặng, nhưng giảm ngay sau
- Monitor usage trong Redshift console

## Query Optimization

- Sử dụng LIMIT trong queries test
- Filter theo partition (year, month) để giảm scan data
- Tránh query toàn bộ dataset không cần thiết

# Dọn dẹp Resources

Sau khi hoàn thành workshop:

1. **Delete Redshift workgroup và namespace**:
   - Redshift console → Serverless dashboard
   - Chọn workgroup → Delete
   - Chọn namespace → Delete

2. **Delete Glue resources** (nếu không cần):
   - Crawlers: glue-crawler-processed-yellow-taxi
   - Databases: redshift_database
   - Tables: processed_yellow_taxi_trip_data

3. **Delete IAM roles**:
   - AmazonRedshift-CommandsAccessRole-...
   - glue-role-manhattan-processed-crawler

4. **Empty S3 buckets** nếu không cần data (nhưng giữ lại cho ETL pipeline)

# Lưu ý

- Redshift Serverless chỉ tính phí khi query chạy
- Nếu workgroup tồn tại mà không dùng, vẫn có thể phát sinh phí nhỏ
- Theo dõi Billing console để track usage
