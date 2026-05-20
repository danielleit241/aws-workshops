---
title: "Cleanup"
date: "2026-05-20"
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

This page is **optional**. Use it if you created temporary Glue resources only for troubleshooting or recovery.

## Delete the Temporary Crawler

If you created a crawler just for this Athena recovery flow, you can remove it after validation.

![Delete temporary crawler](/images/Workshop/5.1%20Athena/41.png)

## Delete the Temporary Database

If you also created a temporary Glue database, delete it after use.

![Delete temporary Glue database](/images/Workshop/5.1%20Athena/43.png)

Confirm that the temporary database is no longer listed.

![Temporary Glue database deleted](/images/Workshop/5.1%20Athena/45.png)

{{% notice tip %}}
Do not delete shared Glue resources if they are still needed by later workshop steps such as Redshift Spectrum or QuickSight.
{{% /notice %}}
