---
title: "Kết nối với Query Editor v2"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 2.3. </b> "
---

1. Từ Redshift console, click "Query data"
2. Chọn "Query editor v2"

# Kết nối đến Workgroup

Trong Query Editor v2:

1. Chọn Serverless workgroup: manhattan-redshift-workgroup
2. Database: dev
3. Authentication: Federated user (sử dụng IAM credentials)

![Connect to workgroup](/images/Workshop/5.2-Redshift/3-QueryEditorV2/1-Connect/connect-to-workgroup.png)

# Xác nhận kết nối

Chạy query test:

```sql
SELECT current_database();
```

Kết quả mong đợi: dev

![Kết quả current_database](/images/Workshop/5.2-Redshift/3-QueryEditorV2/2-Validation/current-database-dev.png)

Chạy thêm:

```sql
SELECT current_user();
```

Query Editor v2 sử dụng temporary credentials để connect vào database thông qua IAM.
