# Changelog

## 0.1.1 — 2026-10-06

- Audit: thêm phần đọc luồng nghiệp vụ (chuyển trạng thái, danh tính người thực hiện lấy từ phiên server, phân quyền endpoint nhạy cảm, xóa dây chuyền, mock ở production).
- Audit: bắt buộc lần theo tới chỗ thực thi trước khi kết luận "điểm làm tốt"; codebase lớn audit nhiều lượt rồi gộp.
- Audit: báo cáo gọn — chỉ lỗi thật, gom "chưa đủ bằng chứng" thành câu hỏi gửi khách, danh sách điểm xuyên suốt không được bỏ sót (tách dữ liệu multi-tenant, báo sự cố, đồng ý trẻ em…).
- Trả lời: mọi nghĩa vụ kèm link văn bản; tóm tắt không được nói chắc hơn chi tiết; chép số liệu nguyên vẹn; luôn có mục chưa rõ.
- Sửa cách diễn đạt sai "NĐ 331/2026 thay NĐ 85/2016" trong domain EMR.

## 0.1.0 — 2026-10-06

- Bản đầu tiên: 15 domain, 457 yêu cầu pháp lý (ảnh chụp pháp luật tại 2026-10-06).
- Tài liệu dùng chung: applicability, supersession, timeline, audit-procedure, maintenance.
- Script kiểm tra link (`check_links.py`) và ID dẫn chiếu (`check_ids.py`).
- Research gốc (khảo sát, danh mục 225 văn bản, đào sâu 15 cụm) trong `research/`.
