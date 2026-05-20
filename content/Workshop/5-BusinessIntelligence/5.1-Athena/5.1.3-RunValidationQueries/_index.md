---
title: "Run Validation Queries"
date: "2026-05-20"
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

With Athena connected to the Glue catalog, you can now validate the processed dataset with a simple SQL query.

## Step 1: Run a Sample Query

Use the following SQL statement:

```sql
SELECT *
FROM quarantine_yellow_taxi_trip_data
LIMIT 5;
```

Enter the query in Athena and choose **Run**.

![Enter the first Athena validation query](/images/Workshop/5.1%20Athena/38.png)

## Step 2: Review the Result

If the setup is correct, Athena returns sample rows from the processed table.

![Successful Athena query results](/images/Workshop/5.1%20Athena/39.png)

At this point, you have validated that:

- Athena can access the Glue catalog metadata
- The processed taxi-trip table is readable
- The BI query layer is ready for deeper analysis
