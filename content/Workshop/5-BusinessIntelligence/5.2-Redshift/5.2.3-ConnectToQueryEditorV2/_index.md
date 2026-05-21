---
title: "Connect to Query Editor v2"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 2.3. </b> "
---

![Connect to editorv2](/images/Workshop/5.2-Redshift/3-QueryEditorV2/1-Connect/open-editorv2.png)

1. From Redshift console, click "Query data"
2. Select "Query editor v2"

# Connect to Workgroup

In Query Editor v2:

1. Select Serverless workgroup: manhattan-redshift-workgroup
2. Database: dev
3. Authentication: Federated user (using IAM credentials)

![Connect to workgroup](/images/Workshop/5.2-Redshift/3-QueryEditorV2/1-Connect/connect-to-workgroup.png)

# Verify Connection

Run test query:

```sql
SELECT current_database();
```

Expected result: dev

![Current database result](/images/Workshop/5.2-Redshift/3-QueryEditorV2/2-Validation/current-database-dev.png)

Also run:

```sql
SELECT current_user();
```

Query Editor v2 uses temporary credentials to connect to the database via IAM.
