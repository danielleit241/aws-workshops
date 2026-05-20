---
title: "Dọn Dẹp"
date: "2026-05-20"
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

Trang này là **tùy chọn**. Dùng khi bạn đã tạo các tài nguyên Glue tạm chỉ để xử lý sự cố hoặc khôi phục.

## Xóa Crawler Tạm

Nếu bạn đã tạo crawler chỉ cho luồng khôi phục Athena này, bạn có thể xóa nó sau khi kiểm tra xong.

![Delete temporary crawler](/images/Workshop/5.1%20Athena/41.png)

## Xóa Database Tạm

Nếu bạn cũng đã tạo một Glue database tạm, hãy xóa nó sau khi dùng xong.

![Delete temporary Glue database](/images/Workshop/5.1%20Athena/43.png)

Xác nhận rằng database tạm không còn xuất hiện trong danh sách.

![Temporary Glue database deleted](/images/Workshop/5.1%20Athena/45.png)

{{% notice tip %}}
Không xóa các tài nguyên Glue dùng chung nếu chúng vẫn cần cho các bước sau của workshop như Redshift Spectrum hoặc QuickSight.
{{% /notice %}}
