---
title: "Kết nối tới Query Editor v2"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 2.3. </b> "
---
1. Từ Redshift console, nhấn **Query data**
2. Chọn **Query editor v2**

# Kết nối tới Workgroup

![Connect to editorv2](/images/Workshop/5.2-Redshift/3-QueryEditorV2/1-Connect/open-editorv2.png)

Trong Query Editor v2:

1. Chọn Serverless workgroup: `manhattan-redshift-workgroup`
2. Database: `dev`
3. Authentication: **Federated user** (dùng IAM credentials)

![Connect to workgroup](/images/Workshop/5.2-Redshift/3-QueryEditorV2/1-Connect/connect-to-workgroup.png)

# Xác minh kết nối

Chạy câu lệnh kiểm tra:

```sql
SELECT current_database();
```

Kết quả mong đợi: `dev`

![Current database result](/images/Workshop/5.2-Redshift/3-QueryEditorV2/2-Validation/current-database-dev.png)

Tiếp tục chạy:

```sql
SELECT current_user();
```

Query Editor v2 sử dụng temporary credentials để kết nối tới cơ sở dữ liệu thông qua IAM.
