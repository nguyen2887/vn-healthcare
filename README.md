# vn-healthcare

Skill cho Claude (Claude Code, Claude Agent SDK, claude.ai) đóng vai **Business Analyst phần mềm y tế tại Việt Nam**: nắm nghiệp vụ của viện và phòng khám, nắm pháp luật đang áp dụng, và không bịa. Áp dụng cho HIS, EMR/bệnh án điện tử, CIS/phần mềm phòng khám, LIS, RIS/PACS, nhà thuốc, khám chữa bệnh từ xa, app sức khỏe, AI y tế.

Hai mặt của skill:

- **Nghiệp vụ (BA)**: soạn kịch bản và câu hỏi khảo sát theo vai; tổng hợp ghi chú phỏng vấn thành luồng as-is; so luồng của khách với luồng tham chiếu, với luật và với phần mềm hiện có (gap analysis); phân lớp mọi điểm khác biệt thành `[LUẬT]` / `[THÔNG LỆ]` / `[HỎI]`; viết user story có truy vết điều luật, kịch bản UAT, change request. Đợt hiện tại phủ **ngoại trú** (phòng khám, khoa khám bệnh), có và không có BHYT; nội trú chưa làm.
- **Tuân thủ**: với mỗi nghĩa vụ pháp lý, skill cho biết văn bản nào (số hiệu, điều/khoản, link bản gốc), áp dụng cho ai, hạn chót, mức độ chắc chắn, phần mềm phải làm gì, và cách audit phần mềm có sẵn.

Skill này **không thiết kế phần mềm** (kiến trúc, multi-tenant, schema). Đầu ra của nó là *cái gì* phải có và *cái gì* được phép khác giữa các khách hàng — đội thiết kế nhận bảng đó để quyết định *làm sao*.

> **Ảnh chụp pháp luật tại 2026-10-06.** Văn bản y tế số ở Việt Nam thay đổi rất nhanh. Đây là tài liệu kỹ thuật tham khảo, **không phải tư vấn pháp lý**. Kết luận có hậu quả tiền bạc/pháp lý cần xác minh lại trạng thái văn bản và hỏi luật sư hoặc cơ quan quản lý.

*English: a Claude skill that acts as a business analyst for Vietnamese healthcare software — clinic/hospital workflow discovery, as-is/to-be modelling, gap analysis against reference workflows and current law, requirements with legal traceability — on top of a map of current Vietnamese regulation (MOH circulars, decrees, social health insurance rules, personal data and cybersecurity law). Content is in Vietnamese. Snapshot as of 2026-10-06; not legal advice.*

## Có gì bên trong

**Nghiệp vụ và BA** (`skills/vn-healthcare/references/`):

| File | Nội dung |
|---|---|
| `business/variation-points.md` | Ba nhãn `[LUẬT]`/`[THÔNG LỆ]`/`[HỎI]`; bảng điểm biến thiên giữa các cơ sở theo luồng ngoại trú, mỗi điểm có lớp, căn cứ, câu hỏi khảo sát; bảng "đặc thù khách xin mà thực ra lệch luật" |
| `business/flows/` | Luồng tham chiếu: ngoại trú, cận lâm sàng, kê đơn–cấp phát, viện phí–BHYT, giấy tờ. Mỗi bước: vai, ràng buộc luật, thông lệ, câu hỏi, dấu hiệu lệch chuẩn |
| `elicitation/` | Bộ câu hỏi theo vai (tiếp đón, bác sĩ, điều dưỡng, CLS, dược, thu ngân, kế toán BHYT, chủ cơ sở, IT), câu bẫy, tài liệu cần xin; quy trình khảo sát và cách tổng hợp ghi chú |
| `deliverables/templates.md` | Mẫu báo cáo khảo sát, as-is/to-be, gap analysis 3 chiều, user story + AC + truy vết, bảng bàn giao đội thiết kế, UAT, change request |

**Pháp luật**:

- **15 domain, 457 yêu cầu pháp lý**, mỗi yêu cầu có ID ổn định, căn cứ điều khoản, mức `BẮT BUỘC` / `BẮT BUỘC?` (có căn cứ nhưng phạm vi chưa rõ) / `NÊN`, kèm pattern thiết kế và checklist audit:

| Domain | Nội dung |
|---|---|
| EMR | Bệnh án điện tử TT 13/2025, ký số, sửa/khóa hồ sơ, thời hạn lưu |
| BHYT-DATA, BHYT-GD | Chuẩn XML QĐ 130 và sửa đổi, ký số file, danh mục mã, giám định BHYT, thời hạn gửi |
| DUOC | Đơn thuốc điện tử TT 26/2025, mã đơn, thuốc kiểm soát đặc biệt, nhà thuốc GPP |
| DLCN | Luật bảo vệ dữ liệu cá nhân 91/2025, NĐ 356/2025, nghĩa vụ vendor |
| ANM | Luật An ninh mạng 2025, cấp độ hệ thống, log, lưu trữ trong nước |
| SKDT, GIAYTO | Sổ sức khỏe điện tử/VNeID, định danh người bệnh, giấy tờ điện tử liên thông |
| HTTT-BC | TT 38/2024, điều kiện CNTT để cấp phép, báo cáo bắt buộc |
| MA-LT, CLS | ICD-10 TT 06/2026, chuẩn liên thông, LIS/PACS, phần mềm là thiết bị y tế |
| TELE | Khám chữa bệnh từ xa, thương mại điện tử, Luật AI |
| CHUYENKHOA, TC-MS, BAOMAT-CB | YHCT, chuyên khoa, quảng cáo, hóa đơn, giá, dữ liệu nhạy cảm chuyên biệt |

- `supersession.md` — văn bản nào đã bị thay, bẫy trích dẫn thường gặp (rất nhiều văn bản quen thuộc đã hết hiệu lực trong 2025–2026).
- `timeline.md` — mọi mốc hạn chót, đã qua / sắp tới.
- `applicability.md` — loại phần mềm/cơ sở → domain cần đọc.
- `audit-procedure.md` — quy trình và mẫu báo cáo audit.

## Cài đặt

**Claude Code (plugin):**

```bash
claude plugin marketplace add nguyen2887/vn-healthcare
```

```bash
claude plugin install vn-healthcare@vn-healthcare
```

**Thủ công:** chép thư mục `skills/vn-healthcare` vào `~/.claude/skills/` (dùng cho mọi project) hoặc `.claude/skills/` của project.

## Cách dùng

Skill tự kích hoạt khi bạn hỏi về phần mềm y tế tại Việt Nam. Ví dụ:

- *"Làm phần mềm phòng khám tư có BHYT, bán SaaS — luật bắt buộc phải có những gì, thiết kế bảng đơn thuốc và bệnh án sao cho đúng?"* → chế độ **thiết kế**.
- *"Audit backend EMR trong repo này theo luật VN hiện hành."* → chế độ **audit**: đọc code/schema, báo lỗi theo mức độ kèm bằng chứng file:dòng, căn cứ và link.
- *"Đơn thuốc lưu bao lâu? Có bắt buộc FHIR không?"* → **hỏi đáp nhanh**.

## Độ tin cậy

- Research từ đầu trên nguồn chính thống (vanban.chinhphu.vn, datafiles.chinhphu.vn, congbao.chinhphu.vn, moh.gov.vn, baohiemxahoi.gov.vn…), 2 pha: khảo sát độc lập 3 góc → đào sâu 15 cụm. Tài liệu research gốc nằm trong `research/`.
- Mọi link được kiểm tra bằng `scripts/check_links.py` (mở được và trang chứa đúng số hiệu văn bản); bản hiện tại 318/328 link OK, phần còn lại là bài báo về dự thảo hoặc file quá lớn đã kiểm tay.
- Câu trích từ bản scan OCR mất dấu chỉ được diễn giải, không trích nguyên văn, trừ khi đã đối chiếu bản có dấu.
- Phần pháp luật đánh giá trên 4 bài test (thiết kế, audit schema mẫu, audit codebase EMR thật, câu hỏi app khám từ xa + AI): có skill đạt 100% tiêu chí, không có skill 49% — khác biệt chủ yếu ở việc không trích văn bản đã hết hiệu lực, đúng thời hạn/mốc, và có link nguồn. Phần BA có 3 bài test (chuẩn bị khảo sát, tổng hợp as-is từ ghi chú mẫu, gap luồng khách ↔ phần mềm) trong `evals/`, chưa chạy đo.
- Phần nghiệp vụ `[THÔNG LỆ]` không có nguồn chính thống như luật: lấy từ kinh nghiệm triển khai và hướng dẫn ngành, luôn ghi nhãn và luôn phải xác nhận lại với khách.

## Cập nhật

Xem `skills/vn-healthcare/references/maintenance.md`. Tóm tắt: sửa domain (giữ nguyên ID), cập nhật `supersession.md`/`timeline.md`, chạy

```bash
python3 skills/vn-healthcare/scripts/check_links.py skills/vn-healthcare/references/*.md skills/vn-healthcare/references/domains/*.md
```

```bash
python3 skills/vn-healthcare/scripts/check_ids.py
```

rồi đổi ngày "Kiểm tra lần cuối" và ghi `CHANGELOG.md`.

Góp ý, báo sai, văn bản mới: mở issue hoặc pull request, kèm số hiệu và link văn bản gốc. Người có trải nghiệm thực địa (tester, triển khai, BA) xem `CONTRIBUTING.md`: kể quan sát cho agent, agent tự đưa vào skill và mở PR; chủ repo duyệt nhãn và nguồn.

## Giấy phép

MIT — xem `LICENSE`. Văn bản pháp luật được dẫn thuộc về cơ quan ban hành.
