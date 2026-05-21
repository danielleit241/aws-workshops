---
title: "Thiết lập Redshift Serverless"
date: "2026-05-02"
weight: 2
chapter: false
pre: " <b> 2.2. </b> "
---

Để sử dụng Redshift Spectrum, chúng ta cần tạo một môi trường Redshift Serverless. Redshift Serverless phù hợp để truy vấn dữ liệu từ S3/Glue mà không phải tự quản lý hạ tầng.

## Bước 1: Truy cập Redshift Console

1. Mở Amazon Redshift console.
2. Trong khu vực Redshift Serverless, bắt đầu quy trình tạo một workgroup mới.
3. Khi màn hình **Get started with Amazon Redshift Serverless** xuất hiện, chọn **Customize settings** thay vì dùng cấu hình nhanh mặc định.

![Redshift Serverless Dashboard](/images/Workshop/5.2-Redshift/2-Creation/0-Precheck/existing-glue-stack-overview.png)

{{% notice info %}}
Chúng ta chọn **Customize settings** vì workshop này cần mức compute chi phí thấp hơn, đúng IAM role cho Spectrum, và các tùy chọn mạng vẫn cho phép kết nối BI ở các bước sau.
{{% /notice %}}

## Bước 2: Bắt đầu luồng thiết lập tùy chỉnh

Tại thời điểm này, Redshift mở luồng tạo tài nguyên có hướng dẫn. Thay vì điền thật nhanh mọi thứ, hãy xem quá trình này như ba điểm kiểm tra:

1. **Workgroup settings**: xác định compute, mạng, và khả năng truy cập
2. **Namespace settings**: xác định môi trường cơ sở dữ liệu logic và quyền IAM
3. **Review and create**: xác nhận lại các giá trị quan trọng trước khi cấp phát tài nguyên

![Start Redshift Serverless custom setup](/images/Workshop/5.2-Redshift/2-Creation/1-Workgroup/1.png)

Cấu trúc này quan trọng vì Redshift Serverless tách riêng:

- **workgroup**, phần kiểm soát cách môi trường compute vận hành
- **namespace**, phần kiểm soát ngữ cảnh cơ sở dữ liệu và IAM role được gắn kèm

Hiểu được sự tách biệt này sẽ giúp việc cấu hình Redshift Spectrum ở bước sau dễ hơn nhiều.

## Bước 3: Cấu hình Workgroup

Màn hình đầu tiên tập trung vào cách môi trường compute của Redshift Serverless sẽ hoạt động.

### 3.1 Đặt danh tính cho Workgroup

Nhập tên workgroup:

- **Workgroup name**: `manhattan-redshift-workgroup`
![Workgroup name](/images/Workshop/5.2-Redshift/2-Creation/1-Workgroup/1.png)

Tên này không ảnh hưởng trực tiếp đến logic truy vấn, nhưng rất quan trọng cho vận hành và xử lý sự cố. Việc dùng tên rõ ràng, gắn với dự án sẽ giúp bạn nhận diện đúng môi trường ở các bước sau khi kết nối Query Editor v2, QuickSight, hoặc khi xem log và quyền truy cập.

### 3.2 Giảm Base Capacity để kiểm soát chi phí

Trong phần hiệu năng, thay đổi:

- **Base capacity**: từ giá trị mặc định sang **`4 RPU`**

![Set base capacity to 4 RPU](/images/Workshop/5.2-Redshift/2-Creation/1-Workgroup/2.png)

Vì sao là `4 RPU`?

- Workshop này chủ yếu chạy các truy vấn minh họa và xác thực, không phải workload data warehouse nặng.
- Redshift Spectrum truy vấn dữ liệu đã xử lý từ S3 thông qua Glue Catalog, nên chúng ta không cần một mức compute nền quá lớn.
- Base capacity thấp hơn giúp bảo toàn AWS credit và giảm nguy cơ phát sinh chi phí không cần thiết trong quá trình thực hành.

{{% notice tip %}}
Trong bối cảnh workshop và lab, `4 RPU` thường đủ để xác minh kết nối, duyệt metadata, và chạy các câu lệnh SQL tiêu biểu mà không bị cấp phát dư thừa.
{{% /notice %}}

### 3.3 Giữ các tùy chọn tự động và mặc định ở mức thận trọng

Xem lại các tùy chọn liên quan đến auto scaling trên cùng màn hình.

- **Autonomics / extra compute**: giữ ở chế độ thận trọng hoặc mặc định
- **Limits (optional)**: để trống nếu bạn chưa muốn áp giới hạn RPU tối đa
- **Track**: giữ nguyên giá trị hiện tại/mặc định, trừ khi tài khoản của bạn yêu cầu khác

![Autonomics configuration](/images/Workshop/5.2-Redshift/2-Creation/1-Workgroup/3.png)

![Optional max capacity limit](/images/Workshop/5.2-Redshift/2-Creation/1-Workgroup/4.png)

![Track setting](/images/Workshop/5.2-Redshift/2-Creation/1-Workgroup/5.png)

Mục tiêu ở đây là tính dự đoán được. Với workshop, chúng ta ưu tiên hành vi ổn định và chi phí thấp hơn là auto scaling quá mạnh.

### 3.4 Cấu hình mạng và quyền truy cập cẩn thận

Chuyển đến khu vực networking và xem lại các trường sau:

- **IP access type**: `IPv4`
- **VPC**: giữ VPC mặc định, trừ khi môi trường workshop của bạn yêu cầu VPC riêng
- **Security group**: tạm thời giữ security group mặc định
- **Subnet selection**: giữ các subnet mặc định/tự động được chọn
- **Enhanced VPC routing**: để tắt

![Network and security settings](/images/Workshop/5.2-Redshift/2-Creation/1-Workgroup/6.png)

Vì sao các lựa chọn này quan trọng:

- Giữ VPC mặc định và subnet mặc định giúp đơn giản hóa việc thiết lập trong môi trường workshop.
- Để **Enhanced VPC routing** ở trạng thái tắt giúp tránh tăng thêm độ phức tạp mạng khi chưa cần.
- Security group đã chọn có thể điều chỉnh sau nếu bạn cần mở cổng `5439` cho kết nối BI từ bên ngoài.

### 3.5 Giữ Workgroup sẵn sàng cho công cụ BI ở bước sau

Ở phần cuối của cấu hình workgroup, hãy đặc biệt chú ý tới khả năng truy cập công khai.

- **Publicly accessible**: bật nếu workshop này sẽ kết nối từ các công cụ bên ngoài như Query Editor v2 hoặc QuickSight thông qua public networking

Đây là một trong những thiết lập thực tế nhất trong toàn bộ quy trình. Nếu tắt public accessibility, các bước tích hợp sau có thể thất bại dù IAM role và đối tượng cơ sở dữ liệu đều đã đúng.

Sau khi kiểm tra xong các thiết lập của workgroup, nhấn **Next**.

## Bước 4: Cấu hình Namespace và quyền IAM

Màn hình tiếp theo xác định môi trường cơ sở dữ liệu logic mà workgroup sẽ sử dụng.

### 4.1 Tạo Namespace nhất quán

Điền phần namespace với các giá trị:

- **Namespace name**: `manhattan-redshift-namespace`

![Namespace name](/images/Workshop/5.2-Redshift/2-Creation/2-Namespace/1.png)

- **Database name**: `dev`

![Database name and admin credentials](/images/Workshop/5.2-Redshift/2-Creation/2-Namespace/2.png)

Vì sao nên giữ `dev`?

- `dev` là tên cơ sở dữ liệu mặc định phổ biến trong các ví dụ và công cụ của Redshift.
- Nhiều hướng dẫn SQL ở các môi trường workshop giả định cơ sở dữ liệu này đã tồn tại.
- Giữ mặc định sẽ giảm ma sát khi dùng Query Editor và các câu lệnh mẫu.

### 4.2 Gắn IAM Role mà Redshift Spectrum cần

Đây là phần quan trọng nhất của màn hình namespace.

Mở luồng quản lý IAM role và gắn role cho phép Redshift đọc:

- các tệp đã xử lý trong Amazon S3
- metadata schema trong AWS Glue Data Catalog

![Open IAM role association](/images/Workshop/5.2-Redshift/2-Creation/2-Namespace/3.png)

Sau đó tiếp tục quy trình gắn role.

![Choose IAM role to associate](/images/Workshop/5.2-Redshift/2-Creation/2-Namespace/4.png)

Sau khi role được gắn, hãy chắc chắn rằng nó xuất hiện như một associated role của namespace.

![IAM role attached to namespace](/images/Workshop/5.2-Redshift/2-Creation/2-Namespace/5.png)

Nếu thiếu đúng IAM role, Redshift Spectrum có thể vẫn tạo kết nối nhưng sẽ thất bại khi đọc external schema, Glue metadata, hoặc dataset trên S3.

### 4.3 Giữ cấu hình mã hóa ở mặc định được quản lý

Xem lại phần thiết lập mã hóa:

- giữ tùy chọn mã hóa mặc định do AWS quản lý cho Redshift, trừ khi tổ chức của bạn yêu cầu khóa KMS tự quản lý

![Encryption and security defaults](/images/Workshop/5.2-Redshift/2-Creation/2-Namespace/6.png)

Đây là lựa chọn phù hợp cho workshop vì:

- an toàn theo mặc định
- tránh thêm công việc cấu hình KMS
- giúp tutorial tập trung vào phân tích dữ liệu thay vì quản lý khóa mã hóa

### 4.4 Xác nhận namespace và tiếp tục

Trước khi sang bước tiếp theo, hãy kiểm tra nhanh:

- tên namespace đã đúng
- tên cơ sở dữ liệu vẫn là `dev`
- IAM role đã được gắn thành công

Sau đó nhấn **Next** để chuyển tới trang review.

## Bước 5: Rà soát toàn bộ trước khi tạo

Màn hình cuối cùng là nơi bạn xác minh rằng các thiết lập workgroup và namespace khớp với kiến trúc của workshop này.

![Review configuration overview](/images/Workshop/5.2-Redshift/2-Creation/3-Review/1.png)

Hãy dùng checklist này trước khi tạo môi trường:

- **Workgroup name** = `manhattan-redshift-workgroup`
- **Base capacity** = `4 RPU`
- **Public accessibility** = bật khi cần kết nối BI từ công cụ bên ngoài
- **Enhanced VPC routing** = tắt
- **Namespace name** = `manhattan-redshift-namespace`
- **Database name** = `dev`
- **IAM role** = đã gắn và sẵn sàng cho truy cập S3 + Glue

![Final review before create](/images/Workshop/5.2-Redshift/2-Creation/3-Review/2.png)

Nếu mọi thứ đều đúng, nhấn **Create workgroup**.

## Bước 6: Chờ môi trường sẵn sàng

Sau khi tạo, AWS sẽ cấp phát cả namespace lẫn workgroup. Quá trình này thường mất vài phút.

Chờ đến khi trạng thái workgroup chuyển thành **Available**.

![Workgroup available](/images/Workshop/5.2-Redshift/2-Creation/4-PostCreate/redshift-workgroup-available.png)

![Redshift Serverless Setup Flow](/images/Workshop/5.2-Redshift/1-Overview/3-Flows/redshift_setup_flow.png)

## Vì sao cấu hình này phù hợp

- Capacity 4 RPU đủ cho truy vấn kiểm thử mà không tốn chi phí cao
- IAM role có đủ quyền đọc S3/Glue cần thiết
- Public access có thể bật để hỗ trợ kết nối BI ở bước sau khi workshop dùng công cụ bên ngoài
