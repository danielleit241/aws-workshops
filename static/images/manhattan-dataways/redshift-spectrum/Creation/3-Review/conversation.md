Màn hình **Step 3: Review and create** này là bước cuối cùng để kiểm tra lại toàn bộ cấu hình trước khi kích hoạt cụm Redshift Serverless. Dựa trên thông tin chuẩn từ các bước trước của bạn, hãy đối chiếu nhanh bảng tổng hợp (Review) trên màn hình của bạn xem đã khớp chính xác với checklist dưới đây chưa nhé:

### 1. Phần Workgroup settings

* **Workgroup name:** `manhattan-redshift-workgroup`
* **Base RPU capacity:** **`4`** *(Mức tối ưu để tiết kiệm chi phí/credit demo)*
* **VPC:** `vpc-0e5ee25e258cd1019`
* **VPC security groups:** `sg-017cdb4a34811159a`
* **Enhanced VPC routing:** **`Disabled`** (hoặc hiển thị là  **`No`** ) *(Tuyệt đối không bật tính năng này để tránh chặn đường kết nối của QuickSight)*
* **Publicly accessible:** **`Enabled`** (hoặc hiển thị là  **`Yes`** ) *(Cần bật để sau này chúng ta cấu hình kết nối từ công cụ BI như QuickSight vào bằng Public IP)*

### 2. Phần Namespace settings

* **Namespace name:** `manhattan-redshift-namespace`
* **Database name:** `dev`
* **IAM roles:** Phải hiển thị tên role **`manhattan-redshift-role`** trong danh sách các role đã liên kết (Associated).

### Kết luận & Bước tiếp theo:

Nếu tất cả thông số trên màn hình của bạn đã trùng khớp hoàn toàn với checklist trên:

1. Bạn hãy tự tin kéo xuống góc cuối cùng bên phải màn hình.
2. Bấm nút **`Create workgroup`** (hoặc  **`Create`** ) màu cam để AWS tiến hành khởi tạo cụm.

*Quá trình khởi tạo cụm serverless thường mất khoảng từ 3 đến 5 phút. Khi trạng thái chuyển sang màu xanh  **`Available`** , hãy báo cho tôi biết để chúng ta chuyển sang bước cấu hình Security Group (mở port 5439) và kết nối dữ liệu nhé!*
