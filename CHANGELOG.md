# Changelog

## 0.1.1 — 2026-10-06

- Audit: bắt buộc lần theo tới chỗ thực thi (hàm có được gọi không, cấu hình hiệu lực khi module khởi tạo) trước khi kết luận một cơ chế đang hoạt động hay ghi "điểm làm tốt".
- Audit: codebase lớn chia ít nhất 3 lượt (pháp lý / luồng nghiệp vụ / bảo mật-vận hành), chạy song song bằng subagent nếu có, rồi gộp; ghi rõ phần repo đã/chưa đọc.

## 0.1.0 — 2026-10-06

- Audit: đọc luồng nghiệp vụ; báo cáo gọn (chỉ lỗi thật, câu hỏi gửi khách, điểm xuyên suốt không được bỏ sót).
- Trả lời: mọi nghĩa vụ kèm link văn bản; tóm tắt không nói chắc hơn chi tiết; chép số liệu nguyên vẹn; luôn có mục chưa rõ.

- Bản đầu tiên: 15 domain, 457 yêu cầu pháp lý (ảnh chụp pháp luật tại 2026-10-06).
- Tài liệu dùng chung: applicability, supersession, timeline, audit-procedure, maintenance.
- Script kiểm tra link (`check_links.py`) và ID dẫn chiếu (`check_ids.py`).
- Research gốc (khảo sát, danh mục 225 văn bản, đào sâu 15 cụm) trong `research/`.
