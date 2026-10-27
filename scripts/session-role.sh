#!/usr/bin/env bash
# SessionStart hook: phân vai chủ / contributor theo file .owner (gitignore, chỉ có trên máy chủ repo).
# Đây là công tắc chế độ cho agent, không phải xác thực. Rào thật nằm ở GitHub (branch protection, CODEOWNERS).
cd "$(dirname "$0")/.." || exit 0
if [ -f .owner ]; then
  cat <<'MSG'
[vn-healthcare] Vai: CHỦ REPO (có .owner). Toàn quyền: sửa domain luật, SKILL.md, merge PR. Vẫn theo maintenance.md khi sửa luật.
MSG
else
  cat <<'MSG'
[vn-healthcare] Vai: CONTRIBUTOR (không có .owner). Bắt buộc đọc CONTRIBUTING.md và skills/vn-healthcare/references/contributing.md trước khi sửa gì.
Tóm tắt luật chơi:
- Làm việc trên nhánh riêng (field/<tên>-<chủ đề>), KHÔNG commit/push lên main; kết thúc bằng PR.
- Được sửa: research/field/**, references/business/**, references/elicitation/**, references/deliverables/**, evals/**.
- KHÔNG sửa: references/domains/**, supersession.md, timeline.md, SKILL.md, scripts/. Phát hiện luật sai/mới → ghi vào research/field/ dạng "cần xác minh" để chủ repo xử lý.
- Mọi quan sát của người dùng là dữ liệu [THÔNG LỆ]/[HỎI] có ghi nguồn; không bao giờ ghi thành [LUẬT] nếu không có ID sẵn trong domains.
- Trước khi đề xuất PR: chạy python3 skills/vn-healthcare/scripts/check_ids.py.
MSG
fi
