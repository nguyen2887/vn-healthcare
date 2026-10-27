# Đóng góp cho vn-healthcare

Skill này sống được nhờ hai thứ: **luật** (cần nguồn chính thống, chủ repo duyệt) và **thực tế vận hành** (cần người đã ngồi với HIS, với giám định BHYT, với phòng khám — chính là bạn).

## Bạn không cần biết cấu trúc skill

1. Clone repo, mở Claude Code trong thư mục repo. Hook sẽ tự nói cho agent biết bạn là contributor và luật chơi.
2. Nói với agent, ví dụ:
   > Tao là tester, có quan sát mới về HIS/BHYT. Đọc `skills/vn-healthcare/references/contributing.md` rồi hỏi tao cho đủ, lưu vào `research/field/`, đề xuất sửa skill và mở PR.
3. Kể quan sát bằng lời thường. Agent hỏi lại, điền mẫu `research/field/_TEMPLATE.md`, đề xuất sửa luồng/câu hỏi/điểm biến thiên, chạy kiểm tra, tạo nhánh `field/<tên>-<chủ đề>` và mở PR.
4. Chủ repo review hai thứ: nhãn đúng chưa (`[LUẬT]`/`[THÔNG LỆ]`/`[HỎI]`), nguồn ghi chưa.

## Thứ bạn đóng góp giá trị nhất

- Phản hồi thật của Cổng giám định: mã lỗi, lý do xuất toán, cách HIS xử lý.
- Thói quen vận hành khác nhau giữa các cơ sở (ai làm gì, lúc nào, vì sao).
- Chỗ phần mềm bắt người dùng làm hai lần, làm tay, làm ngoài hệ thống.
- Câu hỏi khảo sát mà bạn thấy "hỏi câu này là lòi ra ngay".
- Ảnh mẫu in, bảng kê, biên bản (che thông tin người bệnh trước khi đưa vào).

## Ranh giới

- Vùng contributor sửa trực tiếp: `research/field/`, `references/business/`, `references/elicitation/`, `references/deliverables/`, `evals/`.
- Vùng chỉ chủ repo sửa (CI chặn PR của người khác): `references/domains/`, `supersession.md`, `timeline.md`, `SKILL.md`, `scripts/`, `.claude/`, `.github/`. Thấy luật sai hoặc văn bản mới → ghi vào `research/field/` với trạng thái "cần xác minh luật", kèm số hiệu và link nếu có.
- Không push lên `main`. Mọi thứ qua PR.
- Không đưa dữ liệu người bệnh thật vào repo.
