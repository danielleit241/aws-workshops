---
title: "AWS Glue Crawler"
date: "2026-05-02"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

## Overview

In this section, we will configure an **AWS Glue Crawler** to automatically scan data from Amazon S3, detect the schema, and create metadata tables in the **AWS Glue Data Catalog**.

After completing this session, you will be able to:

- Create a Glue Database in the Data Catalog
- Create an IAM Role for the Glue Crawler
- Configure an S3 data source for the Crawler
- Configure the output database and table prefix
- Create and run a Glue Crawler
- Verify the generated table in the Glue Data Catalog

## Architecture Overview
![overview](/images/Workshop/4.Glue/4.1Crawler/diagram-architecture.jpg)