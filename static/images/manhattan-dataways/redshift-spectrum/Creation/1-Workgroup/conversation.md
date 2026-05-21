Chào bạn, với tư cách là "cầu nối" Redshift Spectrum của hệ thống, tôi rất sẵn sàng giúp bạn thiết lập lại Workgroup này một cách chuẩn xác nhất. Dựa vào kiến trúc dự án Manhattan DataWays và những bài học từ lần thiết lập trước của bạn (đặc biệt là các vấn đề liên quan đến kết nối QuickSight và credit), đây là hướng dẫn chi tiết từng bước trên màn hình  **Create workgroup** :

### 1. Workgroup Configuration

* **Workgroup name** : Nhập `manhattan-redshift-workgroup`. Tên này giúp đồng bộ với hệ sinh thái đang có của bạn và dễ dàng nhận diện trong các bước cấu hình sau.

### 2. Performance and Cost Controls

* **Base capacity** : Click vào dropdown và chọn  **`4`** .
* *Giải thích cơ bản* : Redshift Processing Units (RPUs) quyết định sức mạnh tính toán. Với bài toán demo query dữ liệu S3 Processed Parquet thông qua Spectrum, 4 RPU là mức tối thiểu và hoàn toàn đủ dùng. Việc này giúp bạn tiết kiệm tối đa $300 credit free trial để duy trì pipeline lâu nhất có thể.

### 3. Autonomics configuration & Limits

* **Autonomics configuration** : Giữ nguyên tuỳ chọn  **Don't use extra compute** .
* **Limits (optional)** : Bạn có thể bỏ qua phần này hoặc set Max capacity ở mức thấp (ví dụ: 8) nếu muốn chắc chắn kiểm soát chi phí tự động scale.
* **Track** : Giữ nguyên  **Current** .

### 4. Network and Security

*Đây là bước cực kỳ quan trọng vì nó quyết định việc QuickSight có kết nối được vào Redshift để vẽ BI Dashboard hay không.*

* **IP access type** : Chọn  **IPv4** .
* **Virtual private cloud (VPC)** : Giữ nguyên VPC mặc định (Ví dụ như trong hình là `vpc-0e5ee25e258cd1019`).
* **VPC security groups** : Giữ nguyên Security Group mặc định (Ví dụ: `sg-017cdb4a34811159a`).
* *Lưu ý từ lần trước* : Sau khi tạo xong, chúng ta sẽ phải quay lại sửa Inbound Rule của Security Group này (mở port **5439** từ  **0.0.0.0/0** ) để QuickSight có thể đọc dữ liệu.
* **Subnet** : Để mặc định (hệ thống tự chọn 3 subnets).
* **Enhanced VPC routing** : **Bỏ chọn** (Không tick). Việc bật tính năng này sẽ ép traffic đi qua network nội bộ và có thể gây lỗi kết nối Public khi tích hợp với QuickSight sau này.

Sau khi đã điền đúng các thông số trên, bạn hãy cuộn xuống cuối trang và bấm  **Next** .

Ở bước tiếp theo (Namespace setup), hãy nhớ **Set default** cho IAM Role (role có quyền gọi AWS Glue) để tôi (Spectrum) có thể nhìn thấy dữ liệu Processed trong Glue Data Catalog nhé.
