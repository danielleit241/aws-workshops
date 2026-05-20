---
title: "Connect to Query Editor v2"
date: "2026-05-02"
weight: 3
chapter: false
pre: " <b> 2.3. </b> "
---
1. From Redshift console, click "Query data"
2. Select "Query editor v2"

# Connect to Workgroup

In Query Editor v2:

1. Select Serverless workgroup: manhattan-redshift-workgroup
2. Database: dev
3. Authentication: Federated user (using IAM credentials)

![Connect to workgroup](/images/manhattan-dataways/redshift-spectrum/15-connect-to-workgroup.png)

# Verify Connection

Run test query:

```sql
SELECT current_database();
```

Expected result: dev

![Current database result](/images/manhattan-dataways/redshift-spectrum/07-current-database-dev.png)

Also run:

```sql
SELECT current_user();
```

Query Editor v2 uses temporary credentials to connect to the database via IAM.
