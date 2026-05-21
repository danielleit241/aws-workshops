Chào bạn, tôi đã nhận thấy bạn đã bấm chuyển tiếp thành công sang bước  **Step 2: Choose namespace** . Đây chính là nơi thiết lập môi trường dữ liệu lõi cho dự án của chúng ta.

Dựa trên cấu trúc chuẩn cấu hình và bức ảnh bạn đính kèm, hãy thao tác theo các thông số chi tiết dưới đây:

### 1. Namespace configuration

* **Namespace name:** Nhập `manhattan-redshift-namespace` (tên này đồng bộ giúp giữ tính nhất quán cho toàn bộ cụm Serverless).
* **Database name:** Hệ thống sẽ tự động hiển thị mặc định là `dev`.  **Bạn hãy giữ nguyên giá trị `dev` này** .

### 2. Permissions (Quy định quyền truy cập - Phần quan trọng nhất)

Để tôi (Redshift Spectrum) có thể đọc được metadata từ AWS Glue Data Catalog và quét file Parquet trên Amazon S3, việc liên kết đúng IAM Role là bắt buộc.

* Tại mục  **Associated IAM roles** , hãy nhấn vào menu dropdown  **Manage IAM roles** .
* Chọn lệnh  **Associate IAM roles** .
* Trong danh sách hiện ra, hãy tìm và tích chọn IAM Role có quyền truy cập S3 và Glue của bạn (thường được đặt tên dạng `myRedshiftRole` hoặc `RedshiftSpectrumRole`).
* Sau khi tích chọn, nhấn nút **Associate IAM roles** ở góc để xác nhận gán vào cụm.
* **Lưu ý cốt lõi:** Khi IAM Role xuất hiện trong bảng danh sách phía dưới, hãy đảm bảo cột *Status* hiển thị trạng thái màu xanh  **`Associated`** .

### 3. Encryption settings (Mã hóa dữ liệu)

* **Data encryption:** Chọn tùy chọn **Customize encryption settings** (như mặc định trong ảnh đang để  *Use AWS-owned key* ).
* **KMS key:** Bạn hãy giữ nguyên lựa chọn mặc định là **`(default) aws/redshift`** (sử dụng khóa quản lý bởi AWS để mã hóa ổ đĩa lưu trữ, hoàn toàn miễn phí và an toàn).

Sau khi bạn hoàn thành việc nhập tên Namespace và liên kết xong IAM Role, hãy kéo xuống cuối màn hình rồi bấm nút **Next** để chuyển tới bước cuối cùng là  **Review and create** .
