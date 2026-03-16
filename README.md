# Hugo Workshop Template

Template Hugo đầy đủ, clone từ **5-Workshop** (RAG với Amazon Bedrock) trong `aws-fcj-report`, dùng để tái sử dụng cho workshop hoặc tài liệu tương tự.

## Cấu trúc

```
hugo-workshop-template/
├── config.toml           # Cấu hình Hugo (baseURL, theme, ngôn ngữ en/vi)
├── content/
│   ├── _index.md         # Trang chủ
│   ├── Proposal/        # Phần 1 — Đề xuất dự án
│   └── Workshop/        # Phần 2 — Nội dung workshop (đánh số 2.x)
│       ├── 2.1-Workshop-overview/
│       ├── 2.2-Prerequiste/
│       ├── 2.3-Knowledge-Base/
│       ├── 2.4-Test-Chatbox/
│       ├── 2.5-Client-Integration/
│       ├── 2.6-Update-Data/
│       └── 2.7-Cleanup/
├── layouts/              # Shortcodes & partials tùy chỉnh
│   ├── shortcodes/tabs.html
│   └── partials/custom-footer.html
├── static/
│   ├── css/              # theme-mine.css, theme-workshop.css
│   ├── files/Proposal/   # File proposal (vd: PDF)
│   ├── files/Workshop/   # File tải xuống (vd: secret-project.txt)
│   └── images/           # ảnh: Proposal/, Workshop/ (giữ cấu trúc thư mục như trong content)
├── themes/
│   └── hugo-theme-learn/ # Theme Learn (đã copy sẵn)
└── README.md
```

## Yêu cầu

- [Hugo (extended)](https://gohugo.io/installation/) — bản extended để dùng SCSS nếu theme cần.

## Chạy nhanh

```bash
cd hugo-workshop-template
hugo server
```

Mở http://localhost:1313

## Build static

```bash
hugo
```

Kết quả trong thư mục `public/`.

## Tái sử dụng template

1. **Copy** cả folder `hugo-workshop-template` thành tên dự án mới (vd: `my-workshop-docs`).
2. **Sửa** `config.toml`: `baseURL`, `title`, `params.description`, `params.author`.
3. **Proposal**: chỉnh `content/Proposal/`; đặt PDF trong `static/files/Proposal/`, ảnh trong `static/images/Proposal/`.
4. **Workshop**: chỉnh `content/Workshop/` theo từng section (2.1, 2.2, …); ảnh vào `static/images/Workshop/` (vd: `2.1-Workshop-overview/`, `2.3-Knowledge-Base/`, …).
5. **File đính kèm**: proposal PDF → `static/files/Proposal/`; file workshop → `static/files/Workshop/` (link vd: `/files/Workshop/ten-file.txt`).

## Theme

- Theme **hugo-theme-learn** đã được **copy sẵn** vào `themes/hugo-theme-learn/` nên không cần cài thêm.
- Nếu muốn dùng Git submodule thay vì copy:
  1. Xóa thư mục `themes/hugo-theme-learn`.
  2. Chạy: `git submodule add https://github.com/matcornic/hugo-theme-learn.git themes/hugo-theme-learn`

## Ghi chú

- **Phần 1 — Proposal** (đề xuất dự án). **Phần 2 — Workshop** (2.1–2.7). Đường dẫn ảnh: `/images/Proposal/`, `/images/Workshop/2.x-.../`; file: `/files/Proposal/`, `/files/Workshop/`.
- Đa ngôn ngữ: mỗi section có `_index.md` (en) và `_index.vi.md` (vi). Có thể thêm ngôn ngữ trong `config.toml` và thêm file tương ứng.
