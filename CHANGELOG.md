# Changelog

## 0.2.1 — 2026-10-27

- Chế độ ĐÓNG GÓP: `references/contributing.md`, `CONTRIBUTING.md`, hộp thư `research/field/` với mẫu 5 ô.
- Hook Claude Code trong repo: SessionStart phân vai chủ/contributor theo file `.owner` (gitignore); PreToolUse chặn mềm commit/push lên main khi là contributor.
- CODEOWNERS và CI: kiểm ID, VP-id, evals.json; chặn PR của người không phải chủ repo đụng vùng luật/SKILL/scripts.

## 0.2.0 — 2026-10-27

Chuyển trọng tâm từ "auditor pháp lý" sang **BA nghiệp vụ + tuân thủ**. Phần luật giữ nguyên (15 domain, 457 yêu cầu, ảnh chụp 2026-10-06).

- Thêm `references/business/variation-points.md`: ba nhãn `[LUẬT]`/`[THÔNG LỆ]`/`[HỎI]`, bảng điểm biến thiên `VP-*` cho luồng ngoại trú (tiếp đón, khám, CLS, kê đơn, viện phí–BHYT, giấy tờ, danh mục–vận hành), bảng "đặc thù khách xin mà thực ra lệch luật".
- Thêm luồng tham chiếu `references/business/flows/`: `ngoai-tru.md`, `cls.md`, `ke-don-cap-phat.md`, `vien-phi-bhyt.md`, `giay-to.md`.
- Thêm `references/elicitation/`: `questions-by-role.md` (câu hỏi theo vai, câu bẫy, tài liệu cần xin), `khao-sat.md` (chuẩn bị, ghi chú, tổng hợp, điều kiện kết thúc).
- Thêm `references/deliverables/templates.md`: báo cáo khảo sát, as-is/to-be, gap analysis 3 chiều, user story + AC + truy vết, bảng VP bàn giao thiết kế, UAT, change request, bảng giả định.
- SKILL.md viết lại: persona BA; chế độ KHẢO SÁT / MÔ HÌNH LUỒNG / GAP (gồm audit cũ) / ĐẶC TẢ / HỎI ĐÁP; nguyên tắc nghiệp vụ (nhãn, hỏi trước khi khẳng định, không bịa quy trình, nói thẳng khi khách xin lệch luật). Chế độ THIẾT KẾ cũ gộp vào ĐẶC TẢ và không ra schema nữa — thiết kế phần mềm tách sang skill khác; mục "Pattern thiết kế" trong domain giữ làm tư liệu.
- Evals: thêm 3 bài BA và ghi chú khảo sát mẫu `evals/files/khao-sat-sample/ghi-chu.md`.
- `scripts/check_ids.py` quét cả thư mục con của `references/`.
- Phạm vi: ngoại trú. Nội trú (BV) là đợt sau.

## 0.1.3 — 2026-10-06

- Audit nhiều lượt: người gộp tự kiểm file kết quả của từng lượt thay vì chỉ chờ thông báo hoàn tất.

## 0.1.2 — 2026-10-06

- Audit nhiều lượt: mỗi subagent ghi kết quả lượt ra file để bước gộp không phụ thuộc vào tin nhắn trả về.

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
