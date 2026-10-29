# Changelog

## 0.2.4 — 2026-10-29

- **SKDT**: QĐ 1551/QĐ-BYT thêm link bản gốc trên trang Cục Quản lý Khám, chữa bệnh (kcb.vn), giữ bản SYT Lai Châu làm dự phòng; hai bản cùng 224 trang, cùng nội dung. SKDT-R17 thêm bẫy: chữ "EMR" trong QĐ 1551 chỉ là tên miền `emrhub.vn` và khối trong sơ đồ PL03, không phải nghĩa vụ gửi bệnh án điện tử.

## 0.2.3 — 2026-10-28

Đợt xác minh thứ hai từ các ghi chú field BHYT 04–08 và NĐ 161/2026 (`research/field/2026-10-27-bhyt04-tro-di.md`, `2026-10-28-luong-co-so-nd161-2026.md`).

- **9 yêu cầu mới BHYT-GD-R37–R45**: chi phí một lần KCB thấp (15% LCS, vẫn nhân tỷ lệ nơi KCB theo CV 2275); trần gói TBYT 45 tháng LCS × mức hưởng và stent phủ thuốc (TT 04/2017 sửa bởi TT 24/2025); lương cơ sở theo giai đoạn (NĐ 161/2026: 2.530.000 đ từ 01/07/2026; NĐ 188 Đ57, Đ18 k2 c); quyền lợi nhóm quân đội, công an, cơ yếu (NĐ 70/2015 sửa bởi NĐ 74/2025); ngày giường và giường lưu (TT 35 Đ4c, Luật KCB Đ77 k2); nhiều can thiệp trong một lần phẫu thuật (TT 35 Đ4d k2); vận chuyển người bệnh (NĐ 188 Đ14, Luật Đ21 k1 b); máu, chế phẩm máu (TT 15/2023); kháng sinh (*) (TT 37/2024 Đ10 k5). Checklist A34–A38.
- **Sửa BHYT-DATA-R03**: miễn check-in XML0 theo từng ca được cơ sở khác chuyển người bệnh/mẫu đến làm CLS (QĐ 4750 Đ2 k2 c, NĐ 188 Đ44), không theo loại cơ sở.
- **BHYT-DATA**: QĐ 1931 lên bản ký số (R11, R12 thành BẮT BUỘC; mẫu `SO_DANG_KY` thuốc hiếm `UBND.YYYY.X.S`); phạm vi ký `GIAMDINHHS` và định dạng XMLDSig (R07); endpoint `Qd4750` → `Qd3176` (R22); không có dung sai tổng XML1 (R10); CV 4059 vào R20; ô (16)–(18) bảng kê (R21). Thêm CV 3700, 7506, 4040, 3055, 4059, Tài liệu kỹ thuật TT 12 vào bảng văn bản.
- **BHYT-GD**: R18 bẫy "ký từ 01/12/2024 theo CV 3700" sai căn cứ; R25 bẫy mã loại hình 10–16 chưa có chỗ trong 01/BH; R35 bẫy nhóm quân đội, công an.
- **Supersession**: NĐ 73/2024 → NĐ 161/2026; TT 17/2020 → TT 15/2023; QĐ 124/2004 → QĐ 19/2025; TT 22/2023 không làm mất quy tắc ngày giường; bẫy số hiệu "NĐ 70" thêm NĐ 70/2015.
- Quy trình: chủ repo ủy quyền agent tự review và merge PR, kể cả PR sửa luật.

## 0.2.2 — 2026-10-27

Xác minh trên bản gốc các điểm tester nêu khi đối chiếu đặc tả BHYT 02, 03 (`research/field/2026-10-27-bhyt02-*.md`, `*-bhyt03-*.md`).

- **BHYT-GD-R36 mới**: tiền khám nhiều chuyên khoa (lần 1 = 100%, lần 2–4 = 30%, lần 5 = 10%, từ lần 6 = 0%; khám lại trong ngày tính lần 2+) và định mức 65 lượt/bàn khám/08 giờ (BHXH trả 50% từ lượt 66, không giảm cùng chi trả của người bệnh). Căn cứ TT 35/2016 Đ4b, Đ4d sửa bởi TT 39/2024 Đ1 k4; TT 22/2023 hết HL không làm mất hai quy tắc này. Checklist BHYT-GD-A33.
- **Sửa BHYT-DATA-R21**: tỷ lệ khám theo PL QĐ 697 Phần Một IV.3 là 100/30/30/30/10/0, không phải "100/30/10/0". VP-KH-10 chuyển phần tính tiền sang `[LUẬT]`.
- **BHYT-GD-R10**: cấp cứu được hưởng 100% **mức hưởng** của thẻ (Luật Đ22 k5), không phải quỹ trả 100% chi phí; ánh xạ NĐ 188 Đ19 k1–k4 → mã 1.12/1.13/1.14/1.18, Đ22 k4 b → 3.6.
- **Thẻ BHYT**: thêm CV 497/BHXH-CNTT (bảng mã kết quả tra thẻ, hàm `KQNhanLichSuKCB2019`) vào BHYT-GD-R02, BHYT-DATA-R04; Luật BHYT Đ16 k4 a (thẻ hết hạn lúc đến khám không có giá trị, không có "ân hạn"; bẫy ở R08); QĐ 1666/QĐ-BHXH (mẫu thẻ 2021), QĐ 1351 sửa bởi 1697, CV 1804/BHXH-QLT và CV 2036/BHXH-CSYT vào bảng văn bản và R01; TT 09/2026/TT-BTC, QĐ 2555/QĐ-BYT nâng từ thứ cấp lên bản gốc.
- **Dữ liệu XML**: BHYT-DATA-R04 thêm quy tắc `MA_DKBD`, `GT_THE_TU`, `GT_THE_DEN` khi chưa có thẻ/thẻ tạm; R16 thêm bẫy "không còn thông tuyến" (`MA_LYDO_VVIEN` thuộc QĐ 4210 đã hết HL) và `MA_KHUVUC` ↔ mã 3.6; R03 ghi rõ không có cách hủy check-in XML0. QĐ 3176 nâng lên bản ký số đủ phụ lục.
- Luật KCB Đ7 k2 (cấm từ chối, cố ý chậm cấp cứu) vào BHYT-GD-R06, SKDT-R10.
- Bẫy mới: CV 1804/BHXH-QLT ≠ QĐ 1804/QĐ-BYT; ba hệ "mức hưởng"; API thẻ của QĐ 241/QĐ-BTC ≠ API Cổng giám định; trang BHXH VN cần TLS cũ nên `check_links.py` có thể báo chết giả.
- `contributing.md`: push xong phải kiểm có PR; không có `gh` thì đưa link "Create pull request"; nhánh đã merge thì tạo nhánh mới.

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
