# 2026-10-27 — Đặc tả "BHYT 02. Thẻ BHYT và tra cứu Cổng giám định" lệch và thiếu so với luật trong skill; nhiều căn cứ chưa xác minh

> Người ghi: NganNgocChau · Vai: BA · Trạng thái: cần xác minh luật

## Thấy gì
Đối chiếu tài liệu đặc tả nghiệp vụ "BHYT 02. Thẻ BHYT và tra cứu Cổng giám định" (file `BHYT 02.docx`, 25 quy tắc R-THE-01…25, 15 ca kiểm thử KT-THE-01…15) với `references/domains/bhyt-gd.md` và `bhyt-data.md` (kiểm tra lần cuối 2026-10-06), có tra web bổ sung ngày 2026-10-27.

Phần khớp skill: tra Cổng và lưu nguyên văn kết quả, nhật ký lần tra chỉ ghi thêm (BHYT-GD-R02, P01); Cổng lỗi vẫn tiếp nhận, tra lại tự động (R03); thẻ hết hạn khi đang điều trị tối đa 15 ngày (R08, NĐ 188 Đ50 k4); mốc đủ 5 năm lấy theo Cổng (R09, NĐ 188 Đ18 k2 b); bắt buộc tra lại trước khi kết thúc lượt (R07); hiển thị rõ kết quả từ Cổng giả lập.

### A. Đặc tả lệch so với nghĩa vụ đã có ID trong skill

| # | Đặc tả viết | Lệch ở đâu | ID skill |
|---|---|---|---|
| A1 | R-THE-24: tra lại khác lần đầu → "tính lại BHYT cả lượt" | Mức hưởng mới tính từ khi thẻ mới có giá trị (tách giai đoạn); nhiều thẻ lấy mức cao nhất. NĐ 188 Đ21 k1, k2; TT 48 Đ4 k3 b | BHYT-GD-R07 |
| A2 | R-THE-12, KT-THE-11: Cổng lỗi mà thiếu ảnh màn hình → không lưu lượt | NĐ 188 Đ38 k2: Cổng không tra được thì ghi nhận mã số, vẫn tiếp nhận, tra lại sau; ảnh màn hình chỉ gửi kèm khi kết thúc lượt vẫn lỗi. Bắt ảnh lúc tiếp nhận là thêm thủ tục (Đ38 k3; NĐ 90 Đ95 k1 a). Skill chấp nhận "ảnh màn hình hoặc log có timestamp, mã lỗi" | BHYT-GD-R03, R04 |
| A3 | KT-THE-13: trẻ < 6 tuổi dùng giấy chứng sinh → "không bắt tra Cổng"; R-THE-17 dẫn NĐ 188 Đ37 k2 | NĐ 188 Đ50 k1 a: tra mã thẻ tạm trên Cổng; chưa có thì nhập thông tin để Cổng cấp tự động. Đặc tả thiếu luồng đề nghị Cổng cấp mã; căn cứ mã thẻ tạm là Đ50 k1 a, không phải Đ37 k2 | BHYT-GD-R05, BHYT-DATA-R04 |
| A4 | R-THE-20, KT-THE-15: lũy kế nhập tay ghi đè được, giá trị Cổng không ghi đè số đã có | NĐ 188 Đ18 k2 b: BHXH công bố lũy kế và thời điểm đủ 5 năm trên Cổng, cơ sở căn cứ vào đó → Cổng là nguồn chính, nhập tay chỉ khi Cổng không trả, lệch thì cảnh báo | BHYT-GD-R09 |
| A5 | R-THE-06, R-THE-08: Cổng trả 050 (không tìm thấy) → chặn lượt BHYT | NĐ 188 Đ37 k1 b: quân đội, công an chưa có thông tin thẻ trên hệ thống vẫn xuất trình thẻ giấy → cần nhánh riêng, không chặn cứng | BHYT-GD-R01 |

### B. Đặc tả thiếu nghĩa vụ đã có ID trong skill

| # | Thiếu | Căn cứ | ID skill |
|---|---|---|---|
| B1 | Căn cứ chính của tra cứu: tra ở 3 thời điểm (tiếp đón, khi cần trong điều trị, trước kết thúc lượt); Cổng trả thẻ thu hồi/tạm giữ/tạm khóa. Đặc tả không nhắc TT 12/2026; R-THE-07 dẫn QĐ 3176 và NĐ 188 Đ38 (không phải căn cứ của nghĩa vụ tra). "Lần tra phải trong ngày" là quy ước nội bộ | TT 12/2026 Đ4 k1, k2; TT 48 Đ13 k2 | BHYT-GD-R02 |
| B2 | Xuất trình thẻ muộn (quỹ trả từ thời điểm xuất trình, trừ cấp cứu) và cấp cứu (xuất trình trước kết thúc đợt; tra trước khi ra viện). Có trường "thời điểm xuất trình thẻ" nhưng không có quy tắc dùng | NĐ 188 Đ38 k1, Đ50 k6, Đ37 k5; QĐ 4750 diễn giải `MA_THE_BHYT` | BHYT-GD-R06, BHYT-DATA-R04 |
| B3 | Lịch sử KCB tối thiểu 06 tháng, hiển thị cho bác sĩ; đặc tả chỉ hiện 5 lần ở màn tiếp đón (R-THE-22) | TT 48 Đ6 k2 a; TT 12 Đ4 k2 | BHYT-GD-R02 |
| B4 | Trẻ vừa sinh: cha mẹ/thân nhân ký xác nhận trên HSBA; người hiến bộ phận cơ thể | NĐ 188 Đ37 k2, k4 | BHYT-GD-R01, R05 |
| B5 | Thẻ chưa có ảnh → kiểm giấy tờ nhân thân (đặc tả chỉ áp cho mã 001, 002) | NĐ 188 Đ37 k1 | BHYT-GD-R01 |
| B6 | Kết thúc lượt mà Cổng vẫn lỗi: gửi kèm thông tin liên hệ người bệnh (R-THE-14 chưa có) | NĐ 188 Đ38 k2 | BHYT-GD-R03 |
| B7 | Báo BHXH khi phát hiện vi phạm sử dụng thẻ (thu hồi, nghi mượn thẻ) | NĐ 188 Đ12 k4; NĐ 90 Đ84 | BHYT-GD-R32 |
| B8 | Không đòi thẻ giấy; sao chụp giấy tờ phải có đồng ý, không thu phí | Luật 51 Đ1 k14; NĐ 188 Đ11 k1, Đ38 k3 | BHYT-GD-R01, R04 |
| B9 | Chặn chế độ Cổng giả lập ở production; hồ sơ dùng kết quả giả lập không được gửi (R-THE-25 chỉ dừng ở hiển thị nhãn) | audit-procedure.md mục 2 (mock ở production) | — |

## Ở đâu
Tài liệu đặc tả nghiệp vụ nội bộ của dự án HIS (không có tên phiên bản) · Loại cơ sở: không rõ (đặc tả có cả ngoại trú, nội trú, kiosk) · Tỉnh: không rõ · Có BHYT.

## Bằng chứng
- Tài liệu `BHYT 02.docx` (không đưa vào repo; dữ liệu kiểm thử trong đó là dữ liệu giả).
- Tra web 2026-10-27, toàn bộ là nguồn thứ cấp:
  - CV 1804/BHXH-QLT: [EY tax alert 08/2025](https://www.ey.com/content/dam/ey-unified-site/ey-com/vi-vn/technical/tax/documents/people-advisory-services-tax-alert-august-2025-official-letter-1804bhxh-qlt-regarding-the-replacement-of-social-insurance-number-by-citizen-identification-number-and-management-code-vn.pdf) · [lsvn](https://lsvn.vn/su-dung-so-dinh-danh-ca-nhan-can-cuoc-cong-dan-thay-ma-so-bhxh-a161464.html)
  - QĐ 1351/QĐ-BHXH (16/11/2015): [caselaw](https://caselaw.vn/van-ban-phap-luat/150943-quyet-dinh-so-1351-qd-bhxh-ngay-16-11-2015-ve-ma-so-ghi-tren-the-bao-hiem-y-te-do-tong-giam-doc-bao-hiem-xa-hoi-viet-nam-ban-hanh) · [luatvietnam](https://luatvietnam.vn/tin-phap-luat/giai-ma-15-ky-tu-trong-ma-so-cua-the-bao-hiem-y-te-moi-nhat-230-18323-article.html)
  - CV 468/BHXH-GĐĐT (tra cứu thẻ theo QĐ 1666): [BHXH Bình Thuận](https://binhthuan.baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/4549/CV%20468%20BHXH%20VN%20HD%20Tra%20cuu%20thong%20tin%20the%20BHYT%20theo%20QD%201666.pdf)

## Tần suất / mức ảnh hưởng
Ảnh hưởng mọi lượt BHYT qua tiếp đón. A1 làm sai tiền khi đổi thẻ giữa lượt; A2, A5 có thể từ chối người có quyền hưởng (rủi ro NĐ 90 Đ95 k1 a); A4 có thể tính sai thời điểm miễn cùng chi trả.

## Theo người ghi, đây là
- [x] Luật/BHYT bắt buộc (phần A, B — đã có ID trong skill)
- [ ] Thói quen của cơ sở / của giám định viên địa phương
- [x] Không rõ (phần "Cần xác minh luật" dưới đây)

## Cần chủ repo xác minh luật
Các văn bản đặc tả dẫn mà skill chưa có, hoặc tra không ra:

1. **CV 497/BHXH-CNTT (21/02/2019)**: đặc tả dùng làm căn cứ bảng mã kết quả tra thẻ (000, 001, 002, 003, 004, 010, 050–053, 060, 061, 070, 100, 101, 110, 120–124, 130) và cấu trúc lịch sử KCB. Tra web không tìm thấy; chỉ thấy CV 366/BHXH-CNTT (31/01/2018) về trường vào/ra API tra cứu và CV 3928/BHXH-CNTT (2016). Cần bản gốc hoặc tài liệu API trên Cổng (mục Trợ giúp, cần tài khoản).
2. **CV 1804/BHXH-QLT (04/8/2025, áp dụng 01/8/2025)**: số định danh/CCCD thay mã số BHXH; PL I mã đối tượng kèm mức hưởng. Chỉ có nguồn thứ cấp; skill chưa có. Dễ nhầm với **QĐ 1804/QĐ-BYT** (mã loại hình KCB, mã khoa) — nên thêm vào bẫy trích dẫn.
3. **QĐ 1351/QĐ-BHXH (16/11/2015)**: cấu trúc mã thẻ 15 ký tự (2 chữ đối tượng + 1 số mức hưởng + 2 số mã tỉnh + 10 số). Nguồn thứ cấp ghi Đ2 được bổ sung bởi QĐ 1697/QĐ-BHXH năm 2023 — chưa kiểm.
4. **QĐ 1666/QĐ-BHXH (03/12/2020)**: mẫu thẻ mới 10 chữ số, áp dụng 01/04/2021; theo nguồn thứ cấp không còn mã mức hưởng trên số thẻ. Đặc tả (R-THE-03) dẫn CV 1804 cho thẻ mẫu mới và bắt nhập "mức hưởng 1–5 theo thẻ in" — cần xác định thẻ mẫu mới có in mức hưởng/mã quyền lợi không.
5. **Thẻ tạm trẻ < 6 tuổi**: quy tắc `MA_DKBD` = mã tỉnh 2 số + "000"; hạn thẻ = ngày vào/ra của lượt (R-THE-17). Skill không có căn cứ; có thể nằm trong diễn giải QĐ 4750/3176 — cần đối chiếu.
6. **Mã khu vực K1/K2/K3** (`MA_KHUVUC` XML1, dùng suy mã đối tượng KCB 3.6): skill chưa có căn cứ chi tiết (QĐ 3176, 3276).
7. **"Không có ân hạn khi tiếp đón" (R-THE-15)**: đặc tả dẫn Luật BHYT nhưng chưa có điều khoản; skill chỉ có NĐ 188 Đ50 k4 (hết hạn khi đang điều trị).
8. **TT 09/2026/TT-BTC, QĐ 2555/QĐ-BYT**: đặc tả không dẫn; skill đang để "thứ cấp, chưa mở bản gốc" (BHYT-GD mục 7 câu 6) — liên quan trực tiếp thẻ điện tử, VssID, VNeID.

## Gợi ý cho skill (tùy chọn)
- `business/flows/ngoai-tru.md` hoặc `variation-points.md`: thêm "Dấu hiệu lệch chuẩn" cho A1–A5 (đều có ID, nhãn `[LUẬT]`).
- `elicitation/questions-by-role.md` (tiếp đón): câu hỏi về xử lý thẻ quân đội/công an không tìm thấy trên Cổng; khi lệch họ tên/ngày sinh/giới thì chặn hay cho tiếp nhận sau khi kiểm giấy tờ (`[HỎI]`).
- `deliverables/templates.md` (UAT): ca đổi thẻ giữa lượt → tách giai đoạn mức hưởng; ca Cổng lỗi không có ảnh vẫn tiếp nhận; ca trẻ < 6 tuổi đề nghị Cổng cấp mã tạm.
- Chủ repo: bổ sung các văn bản ở mục "Cần xác minh luật" vào BHYT-GD/BHYT-DATA và bẫy "CV 1804/BHXH-QLT ≠ QĐ 1804/QĐ-BYT" vào `supersession.md`.
