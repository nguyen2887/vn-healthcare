# Chế độ ĐÓNG GÓP — biến quan sát thực địa thành thay đổi trong skill

> Kiểm tra lần cuối: 2026-10-27 · Dành cho agent khi người dùng là contributor (hook SessionStart báo "Vai: CONTRIBUTOR") hoặc khi chủ repo muốn nhập quan sát theo cùng quy trình.

Người đóng góp điển hình: tester đang nghịch HIS và đọc tài liệu BHYT, người triển khai, BA của khách. Họ có trải nghiệm, không có thời gian học cấu trúc skill. Việc của agent: **hỏi cho đủ, phân loại đúng, sửa đúng chỗ, ghi nguồn, mở PR**. Không bắt họ học VP-id hay ID luật.

## 0. Ranh giới cứng

- Chỉ sửa: `research/field/**`, `references/business/**`, `references/elicitation/**`, `references/deliverables/**`, `evals/**`.
- Không sửa: `references/domains/**`, `supersession.md`, `timeline.md`, `SKILL.md`, `scripts/`. CI sẽ chặn PR của người không phải chủ repo đụng các vùng này.
- Không commit trên `main`; nhánh `field/<tên>-<chủ đề>`; kết thúc bằng PR có mô tả theo mục 5.
- Không ghi dữ liệu người bệnh thật (tên, số định danh, số thẻ, ảnh chưa che).

## 1. Tiếp nhận: hỏi cho đủ 5 ô

Người dùng kể tự do. Agent lắng nghe rồi hỏi bù cho đủ mẫu `research/field/_TEMPLATE.md`: thấy gì · ở đâu (phần mềm, loại cơ sở, tỉnh, BHYT) · bằng chứng · tần suất · họ nghĩ là luật hay thói quen. Hỏi theo kiểu BA: "lần gần nhất xảy ra là khi nào, màn hình nào, Cổng trả về chữ gì?". Tối đa 5–7 câu hỏi bù; không có thì ghi "không rõ", không ép.

Lưu thành `research/field/YYYY-MM-DD-<chu-de>.md`, trạng thái "mới".

## 2. Phân loại — quyết định sửa gì

| Quan sát thuộc loại | Làm gì | Nhãn |
|---|---|---|
| Thói quen vận hành (ai làm gì, lúc nào, bằng gì) | Thêm/sửa dòng trong `variation-points.md` hoặc bước trong `flows/*.md`; thêm câu hỏi vào `questions-by-role.md` nếu quan sát gợi ra câu hỏi tốt | `[THÔNG LỆ]` nếu người dùng thấy ở ≥2 cơ sở hoặc nói "chỗ nào cũng vậy" (ghi rõ số cơ sở); `[HỎI]` nếu một nơi |
| Phản hồi Cổng giám định / lý do xuất toán | Thêm vào `flows/vien-phi-bhyt.md` bước xử lý phản hồi hoặc "Dấu hiệu lệch chuẩn"; nếu lý do xuất toán trỏ về một nghĩa vụ có ID trong domain → ghi kèm ID; nếu không tìm thấy ID → mục "Câu hỏi mở" + field "cần xác minh luật" | `[LUẬT]` **chỉ khi** có ID sẵn; còn lại `[THÔNG LỆ]` "giám định địa phương yêu cầu" |
| "BHYT/Sở bắt phải làm X" | `grep` trong `references/domains/` tìm ID. Có → trỏ ID, không thêm nội dung luật mới. Không có → **không ghi thành luật**; ghi field trạng thái "cần xác minh luật", nêu trong PR để chủ repo tra | — |
| Phát hiện luật trong skill sai / văn bản mới | Không sửa domain. Ghi field "cần xác minh luật" kèm số hiệu + link nếu có; nêu trong PR | — |
| Lỗi/thiếu của phần mềm họ đang test | Nếu là lệch luật có ID → thêm vào bảng "khách xin mà thực ra lệch luật" hoặc "Dấu hiệu lệch chuẩn"; nếu là thiếu tính năng thông thường → thêm VP hoặc câu hỏi | theo trên |
| Câu hỏi khảo sát hay | Thêm vào vai tương ứng trong `questions-by-role.md`, đánh 🪤 nếu là câu bẫy | — |
| Kịch bản test hay | Thêm ca vào mẫu UAT trong `templates.md` hoặc eval mới trong `evals/` | — |

Quy tắc không đổi: **không bịa**, **không nâng nhãn** (thói quen một nơi không thành thông lệ, thông lệ không thành luật), **mọi dòng sinh ra ghi nguồn** `(nguồn: field/<tên file>)`.

## 3. Sửa skill

- Giữ nguyên ID cũ (VP-id, ID luật). VP mới đánh số tiếp theo trong nhóm. Không xóa dòng, chỉ sửa hoặc đánh dấu "không còn đúng từ <ngày> (nguồn: …)".
- Giọng và format khớp file đang sửa (đọc 30–50 dòng xung quanh trước khi viết).
- Một PR một chủ đề. Nhiều quan sát khác nhau → nhiều PR nhỏ.
- Cập nhật trạng thái file field: "đã đưa vào skill (PR #…)".

## 4. Kiểm tra trước khi mở PR

```bash
python3 skills/vn-healthcare/scripts/check_ids.py
git diff --stat   # chỉ được chạm vùng cho phép
```

## 5. Mở PR

Nhánh `field/<tên>-<chủ đề>`, push, `gh pr create`.

**Push xong chưa phải là xong.** Nội dung chỉ vào `main` (và hiện trên GitHub ở trang chính) khi PR được chủ repo merge. Trước khi kết thúc phiên, kiểm tra PR đã tồn tại (`gh pr view` hoặc mở trang nhánh):
- Không có `gh`, hoặc `gh` chưa đăng nhập: **không dừng im lặng**. Đưa người dùng link `https://github.com/nguyen2887/vn-healthcare/compare/main...<nhánh>?expand=1`, bảo họ bấm "Create pull request" và dán sẵn mô tả bên dưới để họ copy.
- Ghi thêm vào nhánh đã có PR mở: chỉ cần push, PR tự cập nhật. Nhánh có PR đã merge: tạo nhánh mới từ `main` mới nhất, đừng push tiếp lên nhánh cũ.
- Nói rõ với người dùng trạng thái cuối: "đã push, PR #…, chờ chủ repo duyệt" hoặc "đã push, CHƯA có PR, bấm link này".

Mô tả PR:

```
## Quan sát
(1–3 dòng, link tới research/field/<file>)
## Thay đổi trong skill
- <file>: thêm/sửa gì, nhãn gì, vì sao nhãn đó
## Cần chủ repo xác minh luật
- (số hiệu/link nếu có; hoặc "không")
## Đã chạy check_ids: có/không
```

Không yêu cầu chủ repo merge ngay; không tự merge.

## 6. Khi người dùng muốn làm ngoài ranh giới

Nói rõ: việc đó thuộc chủ repo (sửa luật, SKILL.md, hook…), ghi yêu cầu vào field "cần xác minh" hoặc mục "Cần chủ repo" trong PR, rồi tiếp tục phần trong ranh giới. Không tranh luận về quyền; chỉ chuyển đúng ngăn.
