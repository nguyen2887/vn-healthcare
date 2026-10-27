# 2026-10-27 — Đặc tả "BHYT 03. Tiếp đón người bệnh có BHYT theo lượt" dẫn văn bản hết hiệu lực và thiếu một số nghĩa vụ trong skill

> Người ghi: NganNgocChau · Vai: BA · Trạng thái: cần xác minh luật

## Thấy gì
Đối chiếu tài liệu đặc tả "BHYT 03. Tiếp đón người bệnh có BHYT theo lượt" (file `BHYT 03.docx`; 24 quy tắc R-TD-01…24, 15 ca KT-TD-01…15) với `references/domains/bhyt-gd.md`, `bhyt-data.md`, `tc-ms.md`, `chuyenkhoa.md`, `skdt.md` (kiểm tra lần cuối 2026-10-06).

Phần khớp skill: lý do đến KCB thuộc lượt; hạn phiếu chuyển 10 ngày làm việc / 01 năm bệnh PL III / còn giá trị đến hết đợt (BHYT-GD-R11); xuất trình thẻ muộn tách khoản trước–sau, cấp cứu xuất trình trước khi kết thúc đợt (R06); cấp cứu không bắt giấy tờ, nhận người vô danh (SKDT-R10); 7 nhóm ưu tiên Luật KCB Đ3 k2 (CHUYENKHOA-R39); cấp cứu không check-in XML0 (BHYT-DATA-R03); thẻ hết hạn khi đang điều trị tối đa 15 ngày (R08).

Tài liệu này dùng chung cơ chế tra thẻ với BHYT 02, nên lặp lại 3 lỗi đã ghi ở `research/field/2026-10-27-bhyt02-the-tra-cuu-cong.md` (nhánh `field/ngan-bhyt02-the-tra-cuu`): A2, A3, B1 bên dưới.

### A. Đặc tả lệch so với nghĩa vụ đã có ID trong skill

| # | Đặc tả viết | Lệch ở đâu | ID skill |
|---|---|---|---|
| A1 | R-TD-17, R-TD-18, R-TD-19 dẫn TT 22/2023/TT-BYT (giá BHYT, khám nhiều chuyên khoa 100/30/30/30/10/0%, định mức 65 lượt/bàn khám/ngày) | TT 13, 21, 22/2023 hết HL từ 01/01/2025 (TT 21/2024 Đ11 k2). Giá lấy theo văn bản phê duyệt giá của chính cơ sở (Luật KCB Đ110; NĐ 96 Đ119). Skill ghi tỷ lệ khám theo PL QĐ 697/2026 Phần IV là "100/30/10/0%" | TC-MS-R17, BHYT-DATA-R21 |
| A2 | R-TD-13, KT-TD-09: Cổng lỗi phải có lý do và ảnh màn hình mới tạo lượt | NĐ 188 Đ38 k2: ghi nhận mã thẻ, vẫn tiếp nhận, tra lại sau; ảnh màn hình chỉ gửi kèm khi kết thúc lượt vẫn lỗi. Bắt ảnh lúc tiếp nhận là thêm thủ tục (Đ38 k3; NĐ 90 Đ95 k1 a) | BHYT-GD-R03, R04 |
| A3 | R-TD-15: trẻ < 6 tuổi dùng giấy chứng sinh, không qua Cổng | NĐ 188 Đ50 k1 a: tra mã thẻ tạm trên Cổng; chưa có thì nhập thông tin để Cổng cấp tự động | BHYT-GD-R05 |
| A4 | R-TD-11: mã đối tượng KCB suy ngay tại quầy, chỉ tính lại khi đổi lý do đến/giấy tờ/chẩn đoán | QĐ 3276 PL1 ghi chú: mã xác định sau khi kết thúc khám/điều trị; mã ở XML0 là tạm, mã cuối ở XML1 → bắt buộc tính lại khi đóng lượt | BHYT-DATA-R16 |
| A5 | R-TD-07: cấp cứu không check-in XML0, căn cứ ghi QĐ 3176 | Nội dung đúng, căn cứ đúng là QĐ 4750 Đ2 k2 (`MA_DOITUONG_KCB = 2`). QĐ 4750 diễn giải `MA_THE_BHYT`: cấp cứu tra thẻ trước khi ra viện, không buộc tra Cổng khi tạo lượt | BHYT-DATA-R03, R04 |

### B. Đặc tả thiếu nghĩa vụ đã có ID trong skill

| # | Thiếu | Căn cứ | ID skill |
|---|---|---|---|
| B1 | R-TD-12 dẫn QĐ 3176 và NĐ 188 Đ38 k2 cho nghĩa vụ tra thẻ; căn cứ đúng là TT 12/2026 Đ4 k1 và TT 48 Đ13 k2. "Lần tra của hôm nay" là quy ước nội bộ | TT 12/2026 Đ4 k1; TT 48 Đ13 k2 | BHYT-GD-R02 |
| B2 | Mức hưởng theo cấp CMKT và lộ trình 01/07/2026 (50% ngoại trú tại một số cơ sở); đặc tả chỉ ghi "tỷ lệ theo nơi KCB" | NĐ 188 Đ19 k2–4; Luật 51 Đ1 k17 | BHYT-GD-R10 |
| B3 | Phiếu hẹn khám lại: mỗi phiếu dùng 01 lần, chỉ hẹn một lần sau khi kết thúc một đợt, có thể ghi trong đơn thuốc/giấy ra viện, bản điện tử ký số. R-TD-06 chưa kiểm phiếu đã dùng | TT 01/2025 Đ11; TT 06/2026 Đ5 k2 | BHYT-GD-R12 |
| B4 | Phiếu chuyển điện tử: ký số cơ sở thay đóng dấu từ 01/06/2026; phiếu trên VNeID ký số đủ tương đương bản giấy. Đặc tả chỉ nhập tay số giấy | TT 01/2025 PL VI; TT 06/2026 Đ5 k2 | BHYT-GD-R11 |
| B5 | Cờ "đổi nơi cư trú": TT 01/2025 Đ4 tính lưu trú dưới 30 ngày, chứng minh được bằng VNeID mức 2, không chỉ giấy xác nhận | TT 01/2025 Đ4 | BHYT-GD-R10 |
| B6 | Người vô danh: sau 48 giờ chưa xác định thân nhân thì thông báo UBND cấp xã; biên bản tài sản | Luật KCB Đ72 k1, k2 | SKDT-R10 |
| B7 | Dịch vụ ngoài phạm vi BHYT (KT-TD-15): thông báo trước, ghi nhận người bệnh đồng ý; tách `T_BNTT` với `T_BNCCT` | NĐ 188 Đ20 k2 | BHYT-GD-R35 |
| B8 | Xuất trình thẻ muộn (R-TD-20): in chứng từ phần tự trả trước mốc xuất trình để người bệnh làm thanh toán trực tiếp | NĐ 188 Đ50 k6, Đ55–57 | BHYT-GD-R06 |
| B9 | Hủy lượt / đổi BHYT → dịch vụ sau khi đã check-in hoặc đã gửi XML (R-TD-21, R-TD-22): hiệu chỉnh dữ liệu đã gửi phải nêu lý do, thống nhất BHXH | TT 48 Đ13 k9 | BHYT-GD-R20 |

### C. Quy tắc nội bộ đang ghi như luật
- R-TD-23 (không nhận lượt mới khi đang nội trú chưa ra viện): căn cứ là quy tắc cũ R-TN-08 của dự án, không phải văn bản → nên gắn `[THÔNG LỆ]`/`[HỎI]`.

## Ở đâu
Tài liệu đặc tả nghiệp vụ nội bộ của một dự án HIS (không nêu tên) · Loại cơ sở: bệnh viện có chi nhánh, khoa khám bệnh và cấp cứu · Tỉnh: không rõ · Có BHYT.

## Bằng chứng
- Tài liệu `BHYT 03.docx` (không đưa vào repo; dữ liệu kiểm thử trong đó là dữ liệu giả).
- Đối chiếu nội bộ với skill; không tra web thêm cho tài liệu này.

## Tần suất / mức ảnh hưởng
Mọi lượt BHYT qua tiếp đón. A1 ảnh hưởng tiền công khám mỗi lượt khám nhiều chuyên khoa và mọi lượt vượt định mức; A2 có thể từ chối tiếp nhận khi Cổng lỗi; A4, B2 làm sai `MA_DOITUONG_KCB` và mức hưởng trên XML1 → xuất toán.

## Theo người ghi, đây là
- [x] Luật/BHYT bắt buộc (phần A, B — đã có ID trong skill)
- [x] Thói quen của cơ sở (phần C)
- [x] Không rõ (phần "Cần xác minh luật" dưới đây)

## Cần chủ repo xác minh luật
1. **Định mức 65 lượt khám/bàn khám/ngày (8 giờ), từ lượt 66 quỹ trả 50%, vượt liên tục 3 tháng thì không trả**: đặc tả dẫn TT 22/2023 (đã hết HL). Skill chưa có căn cứ hiện hành; cần tìm văn bản đang áp dụng (QĐ/NQ giá, NĐ 188 hoặc văn bản BYT khác).
2. **Tỷ lệ thanh toán khám nhiều chuyên khoa**: đặc tả 100/30/30/30/10/0%; skill tóm tắt PL QĐ 697/2026 Phần IV là "100/30/10/0%". Cần đối chiếu bản gốc để biết lần khám thứ 2–4 cùng 30% hay khác.
3. **Lý do đến "thông tuyến"**: Luật 51/2024 bỏ khái niệm tuyến; cần xem PL1 QĐ 3276 còn mã tương ứng không hay đã thay bằng quy tắc theo cấp CMKT (NĐ 188 Đ19).
4. **Luật KCB 15/2023 Đ7 k2** (cấm từ chối, cố ý chậm cấp cứu): đặc tả dẫn, skill mới ghi Đ7 k17, k20, k21 trong CHUYENKHOA → nên bổ sung sau khi đối chiếu VBHN 26/VBHN-VPQH.
5. **Hủy lượt đã check-in XML0**: chưa thấy hướng dẫn hủy/điều chỉnh XML0 trên Cổng (BHYT-DATA-R03 chỉ nói check-in là thông báo trạng thái).

## Gợi ý cho skill (tùy chọn)
- `business/variation-points.md` VP-KH-10: căn cứ đang trỏ BHYT-DATA-R21 cho tỷ lệ 100/30/10/0 — giữ, thêm ghi chú "TT 22/2023 hết HL, đừng dẫn" (nguồn: field/2026-10-27-bhyt03-tiep-don-theo-luot.md).
- `business/flows/ngoai-tru.md` (tiếp đón): thêm "Dấu hiệu lệch chuẩn" cho A1, A2, A4; nhắc cấp cứu tra thẻ trước khi ra viện, không chặn lúc tạo lượt.
- `elicitation/questions-by-role.md` (tiếp đón, kế toán BHYT): "Cơ sở đang đếm định mức lượt khám theo bác sĩ hay theo bàn khám, theo văn bản nào?"; "Phiếu hẹn đã dùng có bị chặn dùng lại không?" (`[HỎI]`).
- `deliverables/templates.md` (UAT): ca cấp cứu có thẻ không bị buộc tra Cổng khi tạo lượt; ca phiếu hẹn dùng lần 2 bị chặn; ca đóng lượt tính lại mã đối tượng.
- Chủ repo: bổ sung bẫy "TT 22/2023 còn bị đặc tả dẫn cho tỷ lệ khám và định mức lượt khám" vào `supersession.md` nếu xác minh xong mục 1–2.
