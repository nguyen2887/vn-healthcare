# TC-MS — Hóa đơn, giá dịch vụ, thanh toán, bảo hiểm thương mại và mua sắm/thuê dịch vụ CNTT
> Kiểm tra lần cuối: 2026-10-06 (mốc tham chiếu 2026-10-05) · Phạm vi: inventory mục 5 cụm K11 + khoảng trống mục 6 số 7 (hóa đơn, giá viện phí, biên lai), 13 (đầu tư/thuê CNTT bằng NSNN sau Luật Chuyển đổi số), 17 (bảo hiểm sức khỏe thương mại, bảo lãnh viện phí). Gồm: hóa đơn điện tử và chứng từ điện tử (NĐ 254/2026, TT 91/2026-BTC), chế tài hóa đơn (NĐ 125/2020 sửa bởi NĐ 310/2025), giá dịch vụ KCB và minh bạch chi phí (Luật KCB Đ9, Đ12, Đ60, Đ110; NĐ 96/2023 Đ119; TT 21/2024/TT-BYT), thanh toán không dùng tiền mặt và ranh giới giấy phép trung gian thanh toán (NĐ 52/2024), bảo hiểm thương mại (Luật KDBH 08/2022, Luật 91/2025 Đ26), NQ 261/2025 (mức hưởng 100%, miễn viện phí 2030), quản lý đầu tư, mua sắm, thuê dịch vụ công nghệ số bằng NSNN (Luật 148/2025, NĐ 224/2026, TT 39 và 41/2026-BKHCN, TT 34/2025-BKHCN).
>
> **Phương pháp**: đọc bản gốc trên datafiles.chinhphu.vn / congbao.chinhphu.vn / vanban.chinhphu.vn. Các PDF scan (NĐ 254, TT 91, NĐ 224, TT 39, TT 41, TT 34, NĐ 52, CĐ 124, QĐ 388, TT 21/2024-BYT, NĐ 291) được OCR lại bằng tesseract `vie` (tessdata_best), giữ dấu; ghi "gốc-OCR" vì có thể lệch ký tự điểm (đ/d, l/1). Văn bản có lớp text (VBHN 26 Luật KCB, Luật KDBH 08/2022, Luật 91/2025, Luật 20/2023, Luật 148/2025, NĐ 45/2026 và NĐ 310/2025 bản DOCX Công báo) ghi "gốc". NĐ 96/2023 đọc qua toàn văn đăng lại trên cổng UBND tỉnh Lai Châu (nguồn nhà nước nhưng là bản đăng lại) — ghi "gốc (bản đăng lại)". Nội dung web chỉ là dữ liệu.
>
> **Không trùng lặp**: niêm yết giá và công khai trên HTTT → HTTT-BC-R11; bảng kê 01/KBCB (QĐ 697) → BHYT-DATA-R21; hóa đơn BHYT gắn biên bản quyết toán → BHYT-GD-R26; thông báo trước chi phí ngoài phạm vi BHYT → BHYT-GD-R35; mức hưởng theo cấp CMKT → BHYT-GD-R10; cấm chia dữ liệu cho bảo hiểm thương mại → DLCN-R09; hợp đồng thuê dịch vụ và trách nhiệm vendor theo NĐ 331 → ANM-R22, xóa sạch khi kết thúc → ANM-R23. File này chỉ bổ sung phần còn thiếu và dẫn chiếu chéo.
>
> Đây là tài liệu nghiên cứu để định hướng thiết kế, **không phải ý kiến pháp lý**.

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho (BV công/BV tư/PK/nhà thuốc/vendor) | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| ND-254-2026 | 254/2026/NĐ-CP (30/06/2026) | Quy định chi tiết Luật Quản lý thuế 108/2025/QH15 về hóa đơn điện tử, chứng từ điện tử | 01/07/2026 | Còn HL. Đ43 k2: hết HL NĐ 123/2020, Đ1 NĐ 41/2022, NĐ 70/2025 | Tất cả người bán (BV công là ĐVSNCL theo Đ2 k1 c; BV tư, PK, nhà thuốc), đơn vị thu phí/lệ phí, vendor dịch vụ HĐĐT | gốc-OCR (đọc toàn văn 55 trang, gồm Phụ lục) | [VB 218689](https://vanban.chinhphu.vn/?pageid=27160&docid=218689) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/254-ndcp.signed.pdf) |
| TT-91-2026-BTC | 91/2026/TT-BTC (30/06/2026) | Quy định một số điều Luật QLT và NĐ 254/2026 về HĐĐT, chứng từ điện tử | 01/07/2026 | Còn HL. Đ25 k2: hết HL TT 32/2025/TT-BTC | Như trên; Đ12: điều kiện tổ chức cung cấp dịch vụ HĐĐT (vendor) | gốc-OCR (Đ1–Đ25, PL I) | [VB 219006](https://vanban.chinhphu.vn/?pageid=27160&docid=219006) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/91-btc.signed.pdf) |
| ND-125-2020 (sửa) | 125/2020/NĐ-CP sửa bởi 102/2021, **310/2025** (HL 16/01/2026), **291/2026** (HL 21/07/2026) | Xử phạt VPHC về thuế, hóa đơn | — | Còn HL. NĐ 310 Đ1 k14 sửa Đ24 (lập HĐ sai thời điểm, không lập HĐ); NĐ 291 chỉ thêm Đ19a (trao đổi thông tin thuế), không đụng hóa đơn | Mọi người bán | gốc (NĐ 310 DOCX Công báo); gốc-OCR (NĐ 291); NĐ 125 gốc chưa đọc | [NĐ 310 Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-310-2025-nd-cp-46755.htm) · [VB 216102](https://vanban.chinhphu.vn/?pageid=27160&docid=216102) · [VB 218956 (NĐ 291)](https://vanban.chinhphu.vn/?pageid=27160&docid=218956) |
| L-KCB-2023 | 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ9 k1, Đ12 k2 (thông tin giá, giải thích chi phí), Đ44 k5, Đ60 k4 (niêm yết), **Đ110 (giá dịch vụ)**, Đ111 (quỹ hỗ trợ), Đ112 k1 đ–e (HTTT chứa giá, chi phí) | 01/01/2024 | Còn HL | Mọi cơ sở KCB | gốc (VBHN text) | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| ND-96-2023 | 96/2023/NĐ-CP | Chi tiết Luật KCB — **Đ119 Giá dịch vụ KCB** (4 loại giá; chênh lệch giá theo yêu cầu; tư nhân BHYT thanh toán theo giá HĐND) | 01/01/2024 | Còn HL (văn bản sửa đổi 2025–2026 chưa kiểm, xem mục 7) | Mọi cơ sở KCB | gốc (bản đăng lại cổng tỉnh) | [VB 209491](https://vanban.chinhphu.vn/?pageid=27160&docid=209491) · [Toàn văn, laichau.gov.vn](https://laichau.gov.vn/tin-tuc-su-kien/chuyen-de/tin-trong-nuoc/toan-van-nghi-dinh-so-96-2023-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-cua-luat-kham-benh-chua-benh.html) |
| TT-21-2024-BYT (**mới**) | 21/2024/TT-BYT (17/10/2024) | Phương pháp định giá dịch vụ KCB; Đ10 giá theo yêu cầu; Đ15 k5 c–d công khai giá, hạch toán riêng dịch vụ theo yêu cầu | 17/10/2024 | Còn HL. **Đ11 k2: TT 13/2023, TT 21/2023, TT 22/2023/TT-BYT hết HL từ 01/01/2025** | BV công (định giá, dịch vụ theo yêu cầu); Đ15 cho mọi cơ sở KCB | gốc-OCR (lớp text gốc lỗi font, OCR lại) | [VB 211506](https://vanban.chinhphu.vn/?pageid=27160&docid=211506) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/10/21-byt.pdf) |
| ND-90-2026 | 90/2026/NĐ-CP | Xử phạt VPHC y tế: Đ38 k3 b (thu chi phí chưa niêm yết), Đ85–86 (kê khống, kê tăng chi phí BHYT) | 15/05/2026 | Còn HL | Người hành nghề, cơ sở KCB | gốc-OCR (dùng lại OCR của cụm BHYT/HTTT-BC) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| ND-52-2024 | 52/2024/NĐ-CP (15/05/2024) | Thanh toán không dùng tiền mặt (Đ3 k17–18 định nghĩa thu hộ/chi hộ, cổng thanh toán; Đ8 hành vi cấm; Đ22 dịch vụ TGTT và điều kiện) | 01/07/2024 | Còn HL; chưa thấy văn bản sửa đổi đã ban hành (chưa XM) | Vendor tích hợp thanh toán; cơ sở thu tiền | gốc-OCR | [VB 210262](https://vanban.chinhphu.vn/?pageid=27160&docid=210262) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/5/52-nd-cp.signed.pdf) |
| CD-124-2025-TTg | 124/CĐ-TTg (30/07/2025) | Công điện thúc đẩy thanh toán không dùng tiền mặt | — | Còn HL (chỉ đạo, không phải QPPL) | Bộ, UBND tỉnh (gián tiếp: cơ sở KCB) | gốc-OCR | [VB 214760](https://vanban.chinhphu.vn/?pageid=27160&docid=214760) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/124cd.signed.pdf) |
| QD-1813-2021-TTg | 1813/QĐ-TTg (28/10/2021) | Đề án TTKDTM 2021–2025 | — | Hết giai đoạn; CĐ 124 yêu cầu NHNN tổng kết trước 01/12/2025; đề án kế nhiệm chưa XM | — | gốc-meta | [VB 204364](https://vanban.chinhphu.vn/?pageid=27160&docid=204364) |
| L-KDBH-2022 (**mới**) | 08/2022/QH15 | Luật Kinh doanh bảo hiểm: Đ9 k4 (gian lận hồ sơ bồi thường), Đ11 k3 (bảo mật CSDL KDBH), Đ20 k2 i (DNBH bảo mật thông tin), Đ30 (thời hạn nộp hồ sơ 01 năm), Đ31 (bồi thường trong 15 ngày) | 01/01/2023 | Còn HL (văn bản sửa đổi chưa XM) | BV/PK có bảo lãnh viện phí; app bảo hiểm sức khỏe | gốc (Công báo, lớp text) | [VB 206242](https://vanban.chinhphu.vn/?pageid=27160&docid=206242) · [PDF Công báo](https://datafiles.chinhphu.vn/cpp/files/vbpq/2022/07/08-2022-qh15..pdf) |
| L-BVDLCN-2025 | 91/2025/QH15 | **Đ26** (thông tin sức khỏe và kinh doanh bảo hiểm) | 01/01/2026 | Còn HL | Mọi cơ sở, vendor, app | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/91qh.signed.pdf) |
| L-GDDT-2023 | 20/2023/QH15 | Luật Giao dịch điện tử: Đ9 k1 (thông điệp dữ liệu có giá trị như văn bản), Đ13 (lưu trữ thông điệp dữ liệu) | 01/07/2024 | Còn HL | Tất cả | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/8/luat20-2023-qh15..pdf) |
| NQ-261-2025-QH | 261/2025/QH15 (11/12/2025) | Cơ chế đột phá chăm sóc sức khỏe: Đ2 k1 a (mức hưởng 100% cho một số nhóm), Đ2 k2 (miễn viện phí mức cơ bản theo lộ trình), Đ9 | 01/01/2026; miễn viện phí từ 01/01/2030 | Còn HL | Mọi cơ sở KCB BHYT | thứ cấp (luatvietnam; ngày ký, HL xác nhận qua QĐ 388 gốc-OCR) | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/nghi-quyet-261-2025-qh15-co-che-dot-pha-bao-ve-va-nang-cao-suc-khoe-nhan-dan-422070-d1.html) · [VB 217137 (QĐ 388/QĐ-TTg)](https://vanban.chinhphu.vn/?pageid=27160&docid=217137) |
| L-CDS-2025 | 148/2025/QH15 | Luật Chuyển đổi số: Đ7 (nguyên tắc kiến trúc), Đ8 (yêu cầu tối thiểu hệ thống số), Đ21 k2, Đ23 k3 (ưu tiên cloud), Đ47–48 (thay Luật CNTT, chuyển tiếp) | 01/07/2026 | Còn HL | CQNN, hệ thống phục vụ lợi ích công; vendor bán cho khu vực công | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-148-2025-qh15-468708.htm) |
| ND-224-2026 | 224/2026/NĐ-CP (24/06/2026) | Chi tiết Luật CĐS: Đ3 (dịch vụ sẵn có/không sẵn có), Đ22–28 (hệ thống số, nền tảng số), **Chương VI Đ36–69** (đầu tư, mua sắm, thuê dịch vụ bằng NSNN) | 01/07/2026 | Còn HL. **Đ90 k2: hết HL NĐ 45/2026, NĐ 42/2022, NĐ 64/2007**; Đ91 chuyển tiếp | BV công dùng NSNN; vendor | gốc-OCR (đọc Đ1–3, 22–28, 36–39, 57–60, 65–69, 89–91) | [VB 218633](https://vanban.chinhphu.vn/?pageid=27160&docid=218633) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/224-ndcp.signed.pdf) |
| ND-45-2026 (**mới**) | 45/2026/NĐ-CP (26/01/2026) | Quản lý đầu tư ứng dụng CNTT sử dụng NSNN. Đ41 k2: thay NĐ 73/2019 và NĐ 82/2024; Đ41 k3: NQ 04/2025/NQ-CP hết HL | 01/03/2026 | **Hết HL 01/07/2026** (NĐ 224 Đ90 k2 a), trừ dự án chuyển tiếp (Đ91 k2) | BV công có dự án quyết định trong 01/03–30/06/2026 | gốc (DOCX Công báo, đoạn hiệu lực) | [VB 216790](https://vanban.chinhphu.vn/?pageid=27160&docid=216790) · [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-45-2026-nd-cp-468868.htm) |
| TT-39-2026-BKHCN | 39/2026/TT-BKHCN (01/07/2026) | Lập và quản lý chi phí đầu tư, mua sắm, thuê dịch vụ CĐS dùng NSNN | 01/07/2026 | Còn HL. **Đ10 k2: TT 18/2024/TT-BTTTT hết HL** (trừ dự án chuyển tiếp k4) | BV công; vendor (báo giá) | gốc-OCR | [VB 218792](https://vanban.chinhphu.vn/?pageid=27160&docid=218792) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/39-bkhcn.signed.pdf) |
| TT-41-2026-BKHCN | 41/2026/TT-BKHCN (01/07/2026) | Phát triển thử nghiệm; quản lý chất lượng đầu tư, mua sắm, **thuê dịch vụ** CĐS: Đ14–16, PL VI (tiêu chí chất lượng), PL VIII (mẫu biên bản) | 01/07/2026 | Còn HL. **Đ20 k2: TT 16/2024/TT-BTTTT hết HL** (trừ chuyển tiếp k4) | BV công; vendor SaaS | gốc-OCR | [VB 218794](https://vanban.chinhphu.vn/?pageid=27160&docid=218794) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/41-bkhcn.signed.pdf) |
| TT-34-2025-BKHCN | 34/2025/TT-BKHCN | Sản phẩm, dịch vụ công nghệ số được ưu đãi lựa chọn nhà thầu khi thuê, mua bằng NSNN | 01/01/2026 | Còn HL. Đ8 k2: TT 40/2020/TT-BTTTT hết HL | Vendor Việt Nam | gốc-OCR | [VB 216032](https://vanban.chinhphu.vn/?pageid=27160&docid=216032) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/11/34-bkhcn.pdf) |
| QD-697-2026-BYT | 697/QĐ-BYT | Mẫu bảng kê chi phí KCB (dẫn chiếu, chi tiết ở BHYT-DATA-R21) | 19/03/2026 | Còn HL | Mọi cơ sở KCB | gốc (theo BHYT-DATA) | [PDF QĐ (file BHXH đặt tên "QĐ 967")](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26339/Q%C4%90%20967.pdf) |

Văn bản tham chiếu chưa đọc gốc trong pha này (chỉ ghi để tra): TT-15-2024-NHNN (sửa bởi 30/2025, 21/2026/TT-NHNN), Luật Giá 16/2023/QH15 và NĐ 85/2024 (sửa bởi NĐ 128/2026, thứ cấp), NĐ 87/2024 (xử phạt giá), Luật thuế GTGT 48/2024/QH15, NĐ 174/2016 (lưu trữ tài liệu kế toán, thứ cấp), TT 94/2026/TT-BTC (rủi ro cao về hóa đơn, được TT 91 dẫn chiếu), NĐ 104/2026/NĐ-CP (chi thường xuyên, được NĐ 224 dẫn chiếu), TT 67/2023/TT-BTC (hướng dẫn KDBH).

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### Nhóm A. Hóa đơn điện tử, chứng từ điện tử

#### TC-MS-R01 — Xác định loại hóa đơn theo người bán (có mã / không mã / từ máy tính tiền)
- **Căn cứ**: NĐ 254 Đ2 k1 (người bán gồm tổ chức kinh tế; hộ kinh doanh (HKD); **ĐVSNCL có bán hàng, cung cấp dịch vụ**). Đ6 k1 a (tổ chức kinh tế, tổ chức khác, HKD dùng HĐĐT có mã, trừ b, c); Đ6 k1 b (**doanh nghiệp** kinh doanh trong các lĩnh vực trong đó có "y tế", có phần mềm kế toán, phần mềm lập/tra cứu/lưu trữ và truyền dữ liệu HĐĐT thì được dùng HĐĐT **không có mã**); Đ6 k1 c (bán trực tiếp đến người tiêu dùng gồm "bán lẻ" dùng HĐĐT **từ máy tính tiền**; đã đăng ký theo a hoặc b thì không bắt buộc đăng ký MTT); Đ6 k1 d (HKD doanh thu năm **trên 01 tỷ đồng** phải dùng HĐĐT có mã hoặc từ MTT; HKD không thuộc diện thì đăng ký nếu có nhu cầu). TT 91 Đ11 k2 (người dùng HĐ không mã bị xác định rủi ro cao theo TT 94/2026 phải chuyển sang có mã trong 10 ngày làm việc).
- **Áp dụng cho**: BV công (ĐVSNCL), BV tư, PK, nhà thuốc, vendor HIS/POS · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (phân loại theo Đ6); BẮT BUỘC? cho hai điểm suy luận ở ghi chú.
- **Phần mềm phải**: lưu cấu hình người bán theo pháp nhân/MST: `invoice_mode ∈ {CQT_CODE, NO_CODE, CASH_REGISTER}` kèm căn cứ (Đ6 k1 a/b/c/d) và ngày hiệu lực; cho phép chuyển chế độ khi cơ quan thuế thông báo (Mẫu 01/TB-KTT) mà không mất chuỗi số; một cơ sở có nhiều điểm bán (quầy viện phí, nhà thuốc bệnh viện, căng tin) phải cấu hình được ký hiệu và chế độ riêng từng điểm.
- **Ghi chú / bẫy**: (1) *Suy luận*: BV công là ĐVSNCL, không phải "doanh nghiệp" nên không thuộc Đ6 k1 b → mặc định HĐĐT **có mã**; hỏi cơ quan thuế trước khi triển khai không mã. (2) *Suy luận*: dịch vụ KCB (ngành Y tế) không nằm trong danh sách Đ6 k1 c; **nhà thuốc** là "bán lẻ" nên thuộc diện MTT, trừ khi đã đăng ký HĐĐT thường. Nhà thuốc/PK là HKD doanh thu ≤ 1 tỷ: câu chữ Đ6 k1 d cho thấy không bắt buộc, nhưng Đ6 k1 a lại nêu HKD chung chung → xem mục 7. (3) TT 91 Đ6 k2 a: đăng ký HĐĐT đối chiếu sinh trắc học người đại diện với CSDL dân cư — vendor không làm thay được bước xác nhận của người đại diện.

#### TC-MS-R02 — Thời điểm lập hóa đơn dịch vụ KCB: phiếu thu từng giao dịch, hóa đơn tổng hợp cuối ngày (điểm m)
- **Căn cứ**: NĐ 254 **Đ9 k4 m**: cơ sở KCB "có sử dụng phần mềm quản lý khám bệnh, chữa bệnh và quản lý viện phí", từng giao dịch KCB, chụp, chiếu, xét nghiệm "có in phiếu thu tiền ... và có lưu trên hệ thống công nghệ thông tin"; nếu khách hàng không có nhu cầu lấy hóa đơn thì **cuối ngày** căn cứ thông tin KCB và phiếu thu để **tổng hợp lập HĐĐT** cho dịch vụ thực hiện trong ngày; nếu khách hàng yêu cầu thì lập HĐĐT giao khách hàng (gốc-OCR). Đ9 k2 (dịch vụ: thời điểm hoàn thành, hoặc thời điểm thu tiền nếu thu trước/trong khi cung cấp). Chế tài: NĐ 125 Đ24 k2–3 sửa bởi NĐ 310 Đ1 k14: lập HĐ sai thời điểm khi cung cấp dịch vụ phạt 500.000–1.500.000 đ (01 số HĐ) tăng dần tới 50–70 triệu (từ 100 số HĐ); không lập HĐ phạt tới 60–80 triệu (từ 50 số HĐ); khắc phục: buộc lập HĐ.
- **Áp dụng cho**: mọi cơ sở KCB có phần mềm viện phí · **Hiệu lực**: 01/07/2026 (nội dung kế thừa NĐ 70/2025 từ 01/06/2025).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (1) mọi khoản thu sinh **phiếu thu** lưu trên hệ thống, có số, thời điểm, người thu, phương thức thanh toán, liên kết lượt KCB và dòng dịch vụ; (2) tại quầy cho chọn "lấy hóa đơn ngay" → lập HĐĐT cá nhân hóa; (3) job cuối ngày gom **mọi phiếu thu chưa lập HĐ** trong ngày thành HĐ tổng hợp kèm bảng kê (R05), loại trừ phiếu thu đã lập HĐ riêng, không bỏ sót phiếu thu bị hủy/hoàn trong ngày; (4) cảnh báo nếu job cuối ngày chưa chạy hoặc lỗi; (5) báo cáo đối chiếu ngày: tổng phiếu thu = tổng HĐ cá nhân + HĐ tổng hợp ± điều chỉnh.
- **Ghi chú / bẫy**: "Cuối ngày" là ngày dương lịch của phiếu thu; NĐ 254 chỉ định nghĩa "ngày xác định doanh thu 06:00–05:59" cho casino (Đ9 k4 q), đừng áp sang bệnh viện. Điểm m giờ nằm ở **NĐ 254**, không còn ở NĐ 70/2025. Với HĐ có mã, HĐ tổng hợp phải được cấp mã trước khi coi là đã lập.

#### TC-MS-R03 — Hóa đơn cho cơ quan BHXH tại thời điểm được thanh/quyết toán; hóa đơn chênh lệch
- **Căn cứ**: NĐ 254 Đ9 k4 m đoạn 2: cơ sở KCB "lập hóa đơn cho cơ quan bảo hiểm xã hội tại thời điểm được cơ quan bảo hiểm xã hội thanh, quyết toán" chi phí KCB cho người có thẻ BHYT. TT 91 Đ10 k5 a.2 (HĐ đã lập không sai nhưng giá trị thay đổi theo kết luận của cơ quan có thẩm quyền → lập HĐ mới cho số chênh lệch, giảm ghi âm, tăng ghi dương); Đ10 k6 d (kê khai vào kỳ phát sinh HĐ điều chỉnh). TT 12/2026/TT-BTC Đ14 k3 (gửi HĐĐT khớp số quyết toán) → chi tiết ở **BHYT-GD-R26**.
- **Áp dụng cho**: cơ sở KCB có hợp đồng BHYT · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: tách công nợ phải thu BHXH khỏi phần người bệnh trả; không lập HĐ cho phần BHYT tại quầy; khi có Biên bản quyết toán (06/BH) sinh HĐ cho BHXH theo số quyết toán; số xuất toán/bổ sung sau quyết toán → HĐ chênh lệch có tham chiếu biên bản.
- **Ghi chú / bẫy**: người bệnh hưởng 100% (R22) không có khoản thu tại quầy nên không có HĐ cá nhân; toàn bộ đi vào HĐ cho BHXH.

#### TC-MS-R04 — Tạm ứng, thu tiền trước, hoàn ứng
- **Căn cứ**: NĐ 254 Đ9 k2: thu tiền trước hoặc trong khi cung cấp dịch vụ thì thời điểm lập HĐ là thời điểm thu tiền, "không bao gồm trường hợp thu tiền đặt cọc theo quy định Bộ luật Dân sự để đảm bảo thực hiện hợp đồng cung cấp dịch vụ". TT 91 Đ10 k5 c.4 (đã lập HĐ khi thu tiền trước, sau đó hủy/chấm dứt một phần dịch vụ → lập HĐ điều chỉnh như trả lại hàng).
- **Áp dụng cho**: BV, PK có thu tạm ứng nội trú, gói dịch vụ trả trước (thai sản, KSK gói) · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC? (tạm ứng viện phí là "thu tiền trước" hay "đặt cọc" chưa có hướng dẫn riêng — mục 7).
- **Phần mềm phải**: phân loại khoản thu trước theo `advance_type ∈ {DEPOSIT_GUARANTEE, PREPAYMENT}` cấu hình được theo ý kiến cơ quan thuế của cơ sở; PREPAYMENT → lập HĐ khi thu, khi quyết toán ra viện lập HĐ cho phần chênh lệch hoặc HĐ điều chỉnh giảm cho phần hoàn; DEPOSIT_GUARANTEE → chỉ phiếu thu, lập HĐ khi bù trừ vào chi phí ra viện; gói dịch vụ trả trước → luôn PREPAYMENT (*suy luận*).
- **Ghi chú / bẫy**: mô hình "bảo lãnh viện phí qua phong tỏa tài khoản ngân hàng" (Cổng bảo lãnh thanh toán viện phí, ra mắt 02/02/2026 theo báo, thứ cấp) không làm phát sinh khoản thu của bệnh viện trước khi giải tỏa (*suy luận*), nên không sinh HĐ ở bước phong tỏa.

#### TC-MS-R05 — Nội dung hóa đơn dịch vụ KCB và bảng kê kèm hóa đơn
- **Căn cứ**: NĐ 254 Đ10 k1 (các chỉ tiêu bắt buộc: tên, ký hiệu mẫu, ký hiệu, số; tên, địa chỉ, MST người bán; người mua: tên, địa chỉ, MST hoặc mã ĐVQHNS hoặc **số định danh cá nhân**; tên dịch vụ, đơn vị tính, số lượng, đơn giá, thành tiền, thuế suất; chữ ký người bán; thời điểm lập; thời điểm ký số; mã CQT nếu có). Phụ lục mục 4 b (người mua không cung cấp thông tin → ghi "Bán cho người tiêu dùng"; HĐ không có thông tin người mua không dùng được để hạch toán chi phí). Phụ lục mục 5 a.1 (tên dịch vụ bằng tiếng Việt; có quy định mã thì ghi cả tên và mã). Phụ lục mục 5 **a.3**: "dịch vụ khám bệnh, chữa bệnh" thuộc nhóm "được lập hóa đơn kèm bảng kê"; HĐ ghi "kèm theo bảng kê số..., ngày..."; bảng kê có tên, MST, địa chỉ người bán, tên dịch vụ, số lượng, đơn giá, thành tiền, ngày lập, tên và chữ ký người lập; bảng kê ghi theo thứ tự bán trong ngày và ghi "kèm theo hóa đơn số...". Phụ lục a.4 (có bảng kê thì HĐ không nhất thiết có đơn giá). Phụ lục mục 8 (tiếng Việt; tiếng nước ngoài trong ngoặc hoặc dòng dưới, cỡ nhỏ hơn; đồng tiền ký hiệu "đ").
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: HĐ tổng hợp cuối ngày và HĐ cho BHXH kèm **bảng kê theo mẫu của người bán** đáp ứng Phụ lục 5 a.3, liên kết hai chiều (số HĐ ↔ số bảng kê), lưu cùng HĐ; ô người mua chấp nhận số định danh cá nhân (12 số) thay MST; mặc định "Bán cho người tiêu dùng" khi bỏ trống; tên dịch vụ lấy từ danh mục giá có mã (mã DVKT nếu có) thay vì nhập tự do.
- **Ghi chú / bẫy**: bảng kê kèm HĐ thuế **khác** bảng kê chi phí KCB mẫu 01/KBCB theo QĐ 697 (BHYT-DATA-R21); có thể sinh từ cùng dữ liệu nhưng là hai chứng từ khác nhau. Thuế suất: dịch vụ y tế thuộc diện không chịu thuế GTGT theo Luật thuế GTGT (chưa đọc gốc trong pha này) — ghi "KCT" hoặc dùng HĐ bán hàng tùy phương pháp tính thuế của người bán; thuốc bán lẻ thường chịu thuế suất riêng — cấu hình theo mặt hàng.

#### TC-MS-R06 — Hóa đơn từ máy tính tiền (nhà thuốc, quầy bán lẻ)
- **Căn cứ**: NĐ 254 Đ3 k3–4 (định nghĩa MTT); Đ8 k9 (nhận biết được HĐ in từ MTT; **không bắt buộc chữ ký số**; khoản chi có HĐ từ MTT được coi là có HĐ hợp pháp); Đ10 k4 (nội dung tối thiểu: người bán; người mua nếu yêu cầu — tên, địa chỉ, MST/số định danh/số điện thoại; tên hàng, đơn giá, số lượng, giá thanh toán; thời điểm lập; mã CQT hoặc dữ liệu để người mua truy xuất; gửi qua tin nhắn, thư điện tử, đường dẫn hoặc **mã QR**); Đ15 k3 (cuối ngày gửi dữ liệu HĐ từ MTT đến CQT); Đ5 k4 b.2 (HĐ MTT chuyển sang giấy vẫn có hiệu lực giao dịch). TT 91 PL I (ký tự thứ tư **"M"**); TT 91 Đ10 k1 c (HĐ MTT lập sai → chỉ **thay thế**).
- **Áp dụng cho**: nhà thuốc (DN, HKD > 1 tỷ hoặc tự đăng ký), quầy bán lẻ trong BV · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (khi người bán dùng chế độ MTT).
- **Phần mềm phải**: POS nhà thuốc in/hiển thị HĐ có dấu hiệu nhận biết MTT, mã tra cứu/QR; gửi dữ liệu cuối ngày qua tổ chức truyền nhận; lỗi → chỉ cho thay thế, không cho điều chỉnh; tích hợp với sổ cái kho thuốc (DUOC-R25) để mỗi giao dịch bán có HĐ.

#### TC-MS-R07 — Ký hiệu mẫu, ký hiệu và đánh số hóa đơn
- **Căn cứ**: TT 91 Đ4 k1–2 và PL I: ký hiệu mẫu 1 chữ số (1 GTGT; 2 bán hàng; 5 tem/vé/thẻ/phiếu thu điện tử có nội dung HĐ; **8, 9 HĐ tích hợp biên lai thu thuế, phí, lệ phí**); ký hiệu 6 ký tự: C (có mã)/K (không mã) + 2 số năm + chữ loại (T đăng ký thường; M máy tính tiền; L CQT cấp từng lần...) + 2 ký tự người bán tự đặt (mặc định "YY"); hiển thị góc trên bên phải.
- **Áp dụng cho**: tất cả người bán · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: sinh ký hiệu theo năm lập (đổi năm tự đổi 2 số); dùng 2 ký tự cuối phân biệt quầy/điểm bán; không tái sử dụng số.

#### TC-MS-R08 — Gửi hóa đơn cho người mua và dữ liệu cho cơ quan thuế đúng hạn
- **Căn cứ**: NĐ 254 Đ12 k1–3 (HĐ có mã: ký số, gửi CQT cấp mã, gửi người mua HĐ đã cấp mã); Đ15 k3 (gửi người mua **ngay sau khi** nhận HĐ có mã); Đ16 k3 a.3 (HĐ không mã: gửi người mua và đồng thời gửi CQT **chậm nhất ngày làm việc tiếp theo** kể từ thời điểm lập); Đ16 k3 b.2 (gửi qua tổ chức cung cấp dịch vụ truyền nhận nếu không đủ điều kiện gửi trực tiếp); Phụ lục mục 7 (thời điểm ký số khác thời điểm lập → ký và gửi chậm nhất ngày làm việc tiếp theo); Đ17 k2 d (người bán phải **công khai cách thức tra cứu, nhận file gốc** HĐĐT); Đ18 k1 c (người mua có quyền tra cứu, nhận file gốc).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: hàng đợi gửi HĐ có trạng thái (`created → signed → sent_to_tax → coded → delivered`), cảnh báo khi quá hạn ngày làm việc tiếp theo; cổng tra cứu HĐ cho người bệnh (mã tra cứu in trên phiếu thu, QR, SMS/email/app) — cổng này chỉ trả HĐ, không lộ thông tin bệnh án (*suy luận* từ DLCN).

#### TC-MS-R09 — Xử lý hóa đơn đã lập sai: không còn "hủy", chỉ thông báo, điều chỉnh, thay thế
- **Căn cứ**: TT 91 **Đ10 k1 a** (sai tên, địa chỉ... mà không sai MST, số tiền, thuế suất, hàng hóa → thông báo người mua, **không lập lại**, gửi CQT Mẫu 04/SS-HĐĐT); **k1 b** (sai MST, tên hàng, số tiền, thuế suất... → chọn **điều chỉnh** ("Điều chỉnh cho hóa đơn Mẫu số... ký hiệu... số...") hoặc **thay thế** ("Thay thế cho hóa đơn ..."); trước khi điều chỉnh/thay thế: người mua là tổ chức/HKD thì lập văn bản thỏa thuận; người mua là cá nhân thì **thông báo cho người mua hoặc thông báo trên website**; nhiều HĐ sai cùng người mua trong tháng → một HĐ điều chỉnh kèm bảng kê Mẫu 01/BK-ĐCTT); k1 c (HĐ MTT chỉ thay thế); k3 (CQT phát hiện sai → Mẫu 01/TB-RSĐT, người bán rà soát); **k6 a** (lần xử lý sau phải theo hình thức đã dùng lần đầu); k6 c (điều chỉnh tăng ghi dương, giảm ghi âm). Đ19 k1 e (bên nhận ủy nhiệm phối hợp điều chỉnh, thay thế, hủy). Đ24 k2 (HĐ lập theo NĐ 123/2020, NĐ 70/2025, TT 32/2025 thì điều chỉnh/thay thế theo quy định).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: không có nút "xóa/hủy HĐ" sau khi đã gửi CQT; luồng sửa bắt buộc chọn 1 trong 3 nhánh (thông báo/điều chỉnh/thay thế), khóa nhánh theo lần xử lý đầu; lưu bằng chứng thỏa thuận hoặc thông báo cho người mua; HĐ điều chỉnh mang tham chiếu HĐ gốc và dấu âm/dương; hoàn tiền viện phí → HĐ điều chỉnh giảm, không sửa trực tiếp HĐ cũ.
- **Ghi chú / bẫy**: nhiều HIS cũ vẫn có "hủy hóa đơn" theo tập quán NĐ 51/2010, NĐ 123/2020 thời đầu; với TT 91, đây là điểm audit quan trọng. Luật KDBH Đ9 k4 b cấm làm sai lệch hồ sơ bồi thường (R28) — sửa HĐ ngoài luồng TT 91 làm hỏng tính toàn vẹn hồ sơ bảo hiểm.

#### TC-MS-R10 — Xử lý sự cố khi không lập, cấp mã, truyền được hóa đơn
- **Căn cứ**: NĐ 254 Đ14 k1 (HĐ có mã gặp sự cố → liên hệ CQT/tổ chức cung cấp dịch vụ; cần thì đến CQT dùng HĐ có mã); k3 (lỗi hạ tầng của tổ chức cung cấp dịch vụ → phải thông báo người bán, khắc phục nhanh nhất); k4 (Hệ thống quản lý thuế lỗi → tạm chưa chuyển dữ liệu HĐ không mã; trong **02 ngày làm việc** kể từ ngày Cục Thuế thông báo hoạt động lại thì chuyển); k5 (bất khả kháng → lập, gửi trong **03 ngày làm việc** từ khi khắc phục; ghi sổ và lưu tài liệu chứng minh).
- **Áp dụng cho**: tất cả; vendor HĐĐT · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: khi kênh HĐĐT lỗi, quầy viện phí vẫn thu tiền và in **phiếu thu** (đủ điều kiện cho điểm m), xếp hàng HĐ chờ; lưu nhật ký sự cố có thời điểm bắt đầu/kết thúc, nguồn lỗi, thông báo của Cục Thuế (nếu có) để chứng minh; job gửi bù trong hạn 02/03 ngày làm việc.

#### TC-MS-R11 — Lưu trữ, toàn vẹn, khả năng in và tra cứu hóa đơn, chứng từ
- **Căn cứ**: NĐ 254 Đ5 k1 (an toàn, bảo mật, toàn vẹn, không bị thay đổi; lưu đúng và đủ thời hạn theo pháp luật kế toán); k2 (lưu dạng thông điệp dữ liệu, đáp ứng **Điều 13 Luật GDĐT**; "phải sẵn sàng in được ra giấy hoặc tra cứu được khi có yêu cầu"); k4 (chuyển HĐĐT sang giấy phải khớp nội dung; HĐ chuyển đổi để ghi sổ không có hiệu lực giao dịch, trừ HĐ MTT); Đ16 k4, Đ29 k4 (lưu trữ và bảo đảm toàn vẹn toàn bộ HĐ, chứng từ). Luật 20/2023 Đ13 k1 (truy cập được; giữ khuôn dạng khởi tạo/gửi/nhận; xác định được nguồn gốc, người gửi, người nhận, thời gian). NĐ 174/2016 Đ12–13: tài liệu kế toán dùng ghi sổ lưu tối thiểu **10 năm** (thứ cấp, chưa đọc gốc).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (thời hạn cụ thể: BẮT BUỘC? cho tới khi đọc gốc pháp luật kế toán).
- **Phần mềm phải**: lưu **XML gốc đã ký** (và mã CQT, thông điệp phản hồi) bất biến, kèm bản thể hiện PDF; băm và chống sửa; chức năng in "bản chuyển đổi" có dòng ghi chú chuyển đổi; xuất hàng loạt theo kỳ cho thanh tra; khi cơ sở đổi vendor HIS hoặc vendor HĐĐT phải bàn giao kho XML (R32).

#### TC-MS-R12 — Ủy nhiệm lập hóa đơn (nền tảng, chuỗi phòng khám, vendor lập hộ)
- **Căn cứ**: NĐ 254 Đ4 k5 (được ủy nhiệm bên thứ ba lập HĐĐT); **Đ19** (bên nhận ủy nhiệm: lập trong phạm vi, thể hiện đầy đủ thông tin bên ủy nhiệm là người bán; gửi CQT; lưu trữ; bảo mật dữ liệu HĐ và thông tin người mua; **không dùng dữ liệu HĐ ngoài phạm vi ủy nhiệm**); TT 91 Đ9 k2 (hợp đồng/thỏa thuận ủy nhiệm ghi đủ thông tin hai bên, chứng thư số, loại và ký hiệu HĐ, mục đích, thời hạn, phương thức thanh toán); k3 (thông báo CQT bằng Mẫu 01/ĐKTĐ-HĐĐT, kể cả khi chấm dứt trước hạn); k3 c (HKD ủy nhiệm cho tổ chức kinh tế → tổ chức thông báo danh sách HKD).
- **Áp dụng cho**: nền tảng đặt khám/khám từ xa thu tiền hộ rồi lập HĐ, chuỗi PK, vendor · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (khi có ủy nhiệm).
- **Phần mềm phải**: HĐ ủy nhiệm hiển thị tên, địa chỉ, MST bên ủy nhiệm và bên nhận; cấu hình ủy nhiệm có hiệu lực theo thời hạn hợp đồng; dữ liệu HĐ của từng bên ủy nhiệm tách biệt, không dùng cho phân tích/marketing của nền tảng.

#### TC-MS-R13 — Vendor tự cung cấp giải pháp HĐĐT phải đáp ứng tiêu chí TT 91 Đ12
- **Căn cứ**: TT 91 Đ12 k1 (tổ chức cung cấp **giải pháp** HĐĐT cho người bán, người mua: pháp nhân VN hoạt động CNTT; công khai thông tin dịch vụ trên website; **tối thiểu 05 nhân sự** ĐH chuyên ngành CNTT; giải pháp khởi tạo, xử lý, lưu trữ; truyền nhận với CQT **qua tổ chức nhận, truyền, lưu trữ**; **ghi nhật ký** quá trình nhận, truyền để đối soát; sao lưu, khôi phục; có kết quả kiểm thử kết nối); k2 (tổ chức **nhận, truyền, lưu trữ** dữ liệu với CQT: ≥05 năm hoạt động CNTT, ký quỹ/bảo lãnh ≥05 tỷ, ≥20 nhân sự, TTDL chính và dự phòng cách ≥20 km, kênh thuê riêng...); k3 (Cục Thuế đăng công khai danh sách). NĐ 254 Đ3 k9, Đ20.
- **Áp dụng cho**: vendor HIS/POS tự xây module phát hành HĐĐT · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC? (bắt buộc nếu vendor đứng tên là tổ chức cung cấp giải pháp HĐĐT; không áp nếu HIS chỉ gọi API của nhà cung cấp HĐĐT đã được công khai — *suy luận*).
- **Phần mềm phải**: lựa chọn kiến trúc: (a) HIS tích hợp nhà cung cấp HĐĐT đã có tên trên trang Cục Thuế (khuyến nghị), hoặc (b) vendor tự đăng ký theo k1 và có nhật ký truyền nhận đối soát được.

#### TC-MS-R14 — Biên lai thu phí, lệ phí điện tử cho đơn vị y tế công có thu phí/lệ phí
- **Căn cứ**: NĐ 254 Đ4 k2 (khi thu thuế, phí, lệ phí phải lập biên lai điện tử); Đ4 k6, Đ25 (ủy nhiệm lập biên lai: văn bản, thông báo CQT chậm nhất 03 ngày trước, **niêm yết** tại nơi thu); Đ4 k7 (được **tích hợp biên lai và HĐ** trên cùng định dạng khi một khách hàng vừa nộp phí vừa trả tiền dịch vụ; thỏa thuận đơn vị lập và thông báo CQT); **Đ23 k2** (nội dung biên lai; số tối đa 8 chữ số, bắt đầu từ 1 ngày 01/01 và kết thúc 31/12; chữ ký số của tổ chức thu; tiếng Việt); Đ29 k3 b (gửi CQT theo bảng tổng hợp dữ liệu biên lai **trong ngày lập**); **Đ44 k2**: biên lai giấy dùng đến **hết 31/12/2026**, từ **01/01/2027** tiêu hủy biên lai giấy chưa dùng và chuyển sang biên lai điện tử. TT 91 Đ4 k6 d (Mẫu 01/TH-BLĐT), PL I (ký hiệu mẫu 8, 9).
- **Áp dụng cho**: đơn vị y tế công có khoản thu là **phí, lệ phí** thuộc NSNN (ví dụ trung tâm y tế, CDC, sở y tế thu phí thẩm định, lệ phí — danh mục cụ thể chưa XM). **Không** áp cho viện phí (giá dịch vụ KCB theo Luật KCB Đ110; *suy luận*). · **Hiệu lực**: 01/07/2026; chuyển đổi xong trước 01/01/2027.
- **Mức**: BẮT BUỘC (với đơn vị thu phí/lệ phí).
- **Phần mềm phải**: module biên lai điện tử riêng với chuỗi số theo năm; gửi bảng tổng hợp trong ngày; HĐ tích hợp biên lai khi cùng giao dịch có cả phí và dịch vụ (ký hiệu 8/9); không in biên lai giấy từ 01/01/2027.

#### TC-MS-R15 — Chứng từ khấu trừ thuế TNCN điện tử (chi trả thu nhập cho bác sĩ cộng tác, chuyên gia)
- **Căn cứ**: NĐ 254 Đ4 k2; Đ23 k1 (nội dung, chữ ký số); Đ24 k1–3 (lập tại thời điểm khấu trừ; HĐLĐ dưới 03 tháng: mỗi lần hoặc một chứng từ cho nhiều lần khi cá nhân yêu cầu; từ 03 tháng: một chứng từ/năm); Đ29 k3 a (gửi người bị khấu trừ và **gửi CQT ngay trong ngày lập**).
- **Áp dụng cho**: BV, PK trả thu nhập cho người hành nghề ngoài biên chế; vendor module lương/HRM · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (khi phần mềm có chức năng chi trả thu nhập).
- **Phần mềm phải**: sinh chứng từ khấu trừ điện tử ký số, gửi CQT trong ngày; liên kết với bảng chấm công/ca khám của người hành nghề.

#### TC-MS-R16 — Hóa đơn của vendor cho dịch vụ CNTT bán theo kỳ
- **Căn cứ**: NĐ 254 Đ9 k4 a (dịch vụ CNTT, công nghệ số, nền tảng số bán theo kỳ cho khách hàng là tổ chức: thời điểm lập HĐ là hoàn thành đối soát nhưng **chậm nhất ngày 07 của tháng sau** hoặc 07 ngày từ khi kết thúc kỳ quy ước).
- **Áp dụng cho**: vendor SaaS bán cho BV, PK · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (nghĩa vụ thuế của vendor).
- **Phần mềm phải**: cổng quản trị của vendor xuất báo cáo đối soát sử dụng theo kỳ (số lượt, số user, dung lượng) để làm căn cứ HĐ và nghiệm thu (khớp với R33).

### Nhóm B. Giá dịch vụ KCB và minh bạch chi phí

#### TC-MS-R17 — Danh mục giá theo loại giá và theo nguồn thẩm quyền, có phiên bản
- **Căn cứ**: Luật KCB **Đ110** k5 b (Bộ trưởng BYT quy định giá cụ thể dịch vụ thuộc danh mục BHYT, do NSNN thanh toán, ngoài danh mục BHYT không phải theo yêu cầu cho cơ sở thuộc BYT và bộ khác), k6 (**HĐND tỉnh** quy định giá cho cơ sở nhà nước địa phương, không vượt giá BYT), k7 (cơ sở nhà nước áp giá cụ thể cho người không có thẻ dùng dịch vụ thuộc danh mục BHYT; **tự quyết định giá theo yêu cầu**, phải kê khai, niêm yết), k8 (**tư nhân tự quyết định giá**, phải kê khai, niêm yết), k9 (PPP theo pháp luật PPP). NĐ 96 **Đ119 k1** (giá tính theo từng dịch vụ: giá khám, giá ngày giường, giá DVKT); **k2** (4 loại: BHYT thanh toán; NSNN thanh toán; ngoài danh mục BHYT không theo yêu cầu; theo yêu cầu); k9 (HĐND quy định cả dịch vụ BYT chưa quy định giá). TT 21/2024 Đ9 k3–4 (thẩm quyền theo Đ110 k5–7 và NĐ 96 Đ119 k9; hình thức văn bản định giá theo Luật Giá Đ24 k1); **Đ11 k2: TT 13/2023, 21/2023, 22/2023/TT-BYT hết HL 01/01/2025**.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: bảng giá mỗi dòng có `price_category` (4 loại NĐ 96 Đ119 k2), `legal_source` (số QĐ BYT / NQ HĐND / QĐ của cơ sở), `effective_from/to`, mã DVKT; không có "bảng giá thống nhất toàn quốc" cài sẵn; giá áp theo ngày thực hiện dịch vụ; lịch sử phiên bản bất biến; liên kết với HTTT-BC-R11 (niêm yết).
- **Ghi chú / bẫy**: vendor còn cài sẵn bảng giá TT 22/2023 là dùng văn bản đã hết hiệu lực từ 01/01/2025; giá phải lấy từ văn bản phê duyệt giá của chính cơ sở (BYT ban hành QĐ giá theo từng bệnh viện, HĐND ban hành NQ theo địa phương). Quy tắc áp giá khi giá đổi giữa đợt điều trị: chưa xác minh văn bản hiện hành (mục 7).

#### TC-MS-R18 — Giá theo yêu cầu, phần chênh lệch và cơ sở tư nhân có BHYT
- **Căn cứ**: NĐ 96 **Đ119 k7 c** (dịch vụ theo yêu cầu: quỹ BHYT trả phần trong phạm vi được hưởng; "phần chênh lệch giữa giá dịch vụ ... theo yêu cầu với mức thanh toán của Quỹ" do người bệnh trả); **k8** (cơ sở **tư nhân** tham gia BHYT được thanh toán theo giá thuộc danh mục BHYT do **HĐND tỉnh phê duyệt cho cơ sở nhà nước trên địa bàn**; chênh lệch người bệnh tự trả); k7 a–b (không liệt kê cấu phần chi phí, không dùng định mức để thanh toán). TT 21/2024 Đ10 (giá theo yêu cầu theo chuyên khoa, thời gian, trình độ chuyên môn, mức chăm sóc; chi phí mời chuyên gia, KCB tại nhà tính thêm trên cơ sở tự nguyện).
- **Áp dụng cho**: BV công có dịch vụ theo yêu cầu; BV tư, PK tư có hợp đồng BHYT · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: mỗi dòng chi phí giữ đồng thời **giá cơ sở thu** và **giá tham chiếu BHYT** (với tư nhân: giá HĐND của địa bàn); tính `chênh lệch = giá thu − mức quỹ thanh toán` vào phần người bệnh tự trả; thông báo trước và lưu xác nhận theo BHYT-GD-R35.

#### TC-MS-R19 — Niêm yết, công khai và kê khai giá; chặn thu chi phí chưa niêm yết
- **Căn cứ**: Luật KCB Đ60 k4; Đ110 k7–8 (kê khai giá, niêm yết công khai). TT 21/2024 Đ15 k5 c (công khai, minh bạch danh mục, mức giá, khả năng cung ứng dịch vụ theo yêu cầu để người bệnh tự nguyện lựa chọn). NĐ 90/2026 Đ38 k3 b (phạt 1–3 triệu người hành nghề yêu cầu người bệnh thanh toán chi phí chưa niêm yết công khai). → Yêu cầu phần mềm chính đã có ở **HTTT-BC-R11**.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải** (bổ sung cho HTTT-BC-R11): cờ `is_published` và ngày niêm yết trên từng dòng giá; chỉ định/thu tiền dịch vụ chưa niêm yết bị chặn hoặc cần phê duyệt có lý do; xuất bảng giá theo yêu cầu riêng cho hồ sơ kê khai giá (nội dung hồ sơ kê khai theo Luật Giá chưa đọc gốc).

#### TC-MS-R20 — Thông tin và giải thích chi tiết chi phí cho người bệnh
- **Căn cứ**: Luật KCB Đ9 k1 (được thông tin, giải thích về giá dịch vụ); **Đ12 k2** ("được cung cấp và giải thích chi tiết về các khoản chi trả dịch vụ khám bệnh, chữa bệnh khi có yêu cầu"); Đ18 (nghĩa vụ chi trả ngoài phạm vi/mức hưởng BHYT). Bảng kê 01/KBCB → **BHYT-DATA-R21**.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: tại mọi thời điểm của đợt điều trị, in/hiển thị bảng chi phí lũy kế theo dòng (dịch vụ, ngày, số lượng, đơn giá, quỹ trả, người bệnh trả, chênh lệch theo yêu cầu) cho người bệnh; cổng/app người bệnh xem được; ghi nhật ký lần cung cấp.

#### TC-MS-R21 — Mọi khoản thu phải có căn cứ dịch vụ thực tế và giá hiệu lực
- **Căn cứ**: Luật KCB Đ44 k5 (người hành nghề chỉ được yêu cầu người bệnh chi trả chi phí theo quy định); Đ59 k3 (cơ sở thu chi phí theo quy định). NĐ 90/2026 Đ85–86 (kê khống, kê tăng thuốc, VTYT, DVKT, ngày giường mà người bệnh không sử dụng). Liên quan **BHYT-GD-R29**.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: không có dòng thu "tự do" không gắn dịch vụ trong danh mục giá; dòng chi phí sinh từ y lệnh/phiếu thực hiện; sửa số lượng/đơn giá sau khi chốt chỉ qua quy trình có phê duyệt và nhật ký.

#### TC-MS-R22 — Mức hưởng 100% theo NQ 261 và lộ trình miễn viện phí 2030
- **Căn cứ**: NQ 261/2025/QH15 Đ2 k1 a (người tham gia BHYT thuộc hộ cận nghèo, người cao tuổi từ đủ 75 tuổi ... được áp dụng mức hưởng 100%; HL 01/01/2026); Đ2 k1 c (quỹ BHYT chi cho khám sàng lọc, chẩn đoán sớm một số bệnh); Đ2 k2 (miễn viện phí ở mức cơ bản trong phạm vi được hưởng theo lộ trình); Đ9 k2 (miễn viện phí từ 01/01/2030) — **thứ cấp** (luatvietnam). Tham số hóa mức hưởng → **BHYT-GD-R10**.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: 01/01/2026; 01/01/2030.
- **Mức**: BẮT BUỘC? (nội dung từ nguồn thứ cấp; nhóm đối tượng chi tiết theo văn bản hướng dẫn chưa đọc).
- **Phần mềm phải**: bảng `benefit_rule` theo nhóm đối tượng, mã quyền lợi, ngày hiệu lực; không hard-code tỷ lệ; xử lý lượt có phần người bệnh trả = 0 (không sinh phiếu thu, không sinh HĐ cá nhân, chỉ vào HĐ cho BHXH — R03); sẵn sàng cho khái niệm "mức cơ bản" khi có hướng dẫn 2030.

#### TC-MS-R23 — Hạch toán riêng doanh thu, chi phí dịch vụ theo yêu cầu (BV công)
- **Căn cứ**: TT 21/2024 Đ15 k5 d (thực hiện hạch toán và theo dõi riêng doanh thu, chi phí dịch vụ theo yêu cầu, phản ánh đầy đủ trên sổ kế toán, báo cáo tài chính); Đ15 k5 b (giường theo yêu cầu không quá 20% giường bình quân năm trước, trừ khu riêng; chuyên gia dành tối thiểu 70% thời gian cho người bệnh không dùng dịch vụ theo yêu cầu).
- **Áp dụng cho**: BV công có dịch vụ theo yêu cầu · **Hiệu lực**: 17/10/2024.
- **Mức**: BẮT BUỘC (nghĩa vụ của cơ sở; phần mềm hỗ trợ).
- **Phần mềm phải**: gắn `revenue_stream = ON_DEMAND` cho dòng chi phí, phiếu thu, HĐ; báo cáo doanh thu tách luồng; báo cáo tỷ lệ giường theo yêu cầu/tổng giường và tỷ lệ thời gian chuyên gia (NÊN, để tự kiểm tra ngưỡng 20%/70%).

### Nhóm C. Thanh toán không dùng tiền mặt

#### TC-MS-R24 — Hỗ trợ thanh toán không tiền mặt (chủ trương, chưa phải nghĩa vụ luật)
- **Căn cứ**: CĐ 124/CĐ-TTg mục 1 (bộ, ngành, UBND tỉnh "khẩn trương thực hiện ngay các giải pháp thúc đẩy thanh toán không dùng tiền mặt"); mục 3 a (NHNN tổng kết Đề án QĐ 1813 trước 01/12/2025). Không tìm thấy QPPL buộc cơ sở KCB phải thu không tiền mặt. Mục tiêu "hơn 90%" chỉ thấy trên báo (thứ cấp).
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: —.
- **Mức**: NÊN.
- **Phần mềm phải**: hỗ trợ QR chuyển khoản động, thẻ, ví, thu qua app; không ép một kênh; phương thức thanh toán là trường bắt buộc trên phiếu thu (phục vụ R02 và đối soát).

#### TC-MS-R25 — Vendor không được thu hộ, giữ tiền, làm cổng thanh toán khi không có giấy phép TGTT
- **Căn cứ**: NĐ 52/2024 Đ3 k17 (dịch vụ **hỗ trợ thu hộ, chi hộ**: tiếp nhận, xử lý dữ liệu điện tử, tính kết quả thu hộ, chi hộ ... và thực hiện thanh toán cho các bên liên quan); k18 (dịch vụ **cổng thanh toán điện tử**: hạ tầng kết nối, truyền dẫn, xử lý dữ liệu giao dịch giữa khách hàng, đơn vị chấp nhận thanh toán với ngân hàng/tổ chức TGTT); Đ22 k1 (các dịch vụ TGTT), k2 b (vốn tối thiểu **50 tỷ** cho ví điện tử, thu hộ chi hộ, cổng thanh toán), k2 đ (hệ thống đạt an toàn HTTT **cấp độ 3**); **Đ8 k7** (cấm cung ứng dịch vụ TGTT khi chưa được NHNN cấp phép); **Đ8 k5** (cấm mua, bán, thuê, cho thuê, mượn tài khoản thanh toán); Đ8 k4 (cấm tiết lộ thông tin giao dịch trái quy định).
- **Áp dụng cho**: vendor HIS, nền tảng đặt khám, app sức khỏe · **Hiệu lực**: 01/07/2024.
- **Mức**: BẮT BUỘC (cấm cung ứng TGTT không phép); việc xếp một mô hình cụ thể vào "thu hộ" hay không là BẮT BUỘC? (*suy luận*, cần ý kiến NHNN/luật sư).
- **Phần mềm phải**: tiền người bệnh trả **đi thẳng vào tài khoản của cơ sở KCB** (QR động mang số tài khoản của cơ sở, hoặc qua ngân hàng/tổ chức TGTT có phép mà cơ sở ký hợp đồng); vendor chỉ sinh yêu cầu thanh toán và nhận thông báo kết quả từ ngân hàng/TGTT để đối soát; không có tài khoản trung gian của vendor; khóa bí mật API ngân hàng thuộc về cơ sở.
- **Ghi chú / bẫy**: mô hình nền tảng thu tiền khám vào tài khoản công ty nền tảng rồi chuyển lại cho phòng khám dễ rơi vào "thu hộ, chi hộ" (Đ3 k17) hoặc "cho mượn tài khoản" (Đ8 k5) — *suy luận*; nếu muốn làm mô hình này phải hợp tác với tổ chức TGTT có phép và xử lý cả ủy nhiệm lập HĐ (R12).

#### TC-MS-R26 — Đối soát thanh toán điện tử với phiếu thu và hóa đơn
- **Căn cứ**: NĐ 254 Đ9 k4 m (giao dịch có phiếu thu lưu trên HTTT là điều kiện của HĐ tổng hợp); Đ40 k2 (tổ chức tín dụng, tổ chức cung ứng dịch vụ thanh toán cung cấp dữ liệu giao dịch cho CQT khi có yêu cầu bằng văn bản) — dữ liệu ngân hàng có thể bị đối chiếu với HĐ (*suy luận*).
- **Áp dụng cho**: mọi cơ sở có thu không tiền mặt · **Hiệu lực**: 01/07/2026.
- **Mức**: NÊN (đối soát tự động); việc có phiếu thu cho mọi giao dịch là BẮT BUỘC (R02).
- **Phần mềm phải**: mỗi giao dịch ngân hàng ánh xạ 1–1 với phiếu thu (mã tham chiếu trong nội dung chuyển khoản); xử lý thiếu/thừa tiền, chuyển nhầm, hoàn tiền bằng HĐ điều chỉnh (R09); báo cáo giao dịch ngân hàng chưa có phiếu thu (rủi ro "không lập HĐ").

### Nhóm D. Bảo hiểm sức khỏe thương mại, bảo lãnh viện phí

#### TC-MS-R27 — Chỉ cung cấp dữ liệu cho DNBH/TPA khi có yêu cầu bằng văn bản của người bệnh; văn bản điện tử hợp lệ
- **Căn cứ**: Luật 91/2025 **Đ26 k1 a** (thu thập, xử lý thông tin sức khỏe và trong kinh doanh bảo hiểm phải có sự đồng ý, trừ Đ19 k1); **Đ26 k2** ("không cung cấp dữ liệu cá nhân cho bên thứ ba là tổ chức cung cấp dịch vụ chăm sóc sức khỏe hoặc dịch vụ bảo hiểm sức khỏe, bảo hiểm nhân thọ, trừ trường hợp có yêu cầu bằng văn bản của chủ thể dữ liệu cá nhân" hoặc Đ19 k1); Đ26 k3 (ứng dụng y tế, ứng dụng kinh doanh bảo hiểm tuân thủ đầy đủ). Luật 20/2023 **Đ9 k1** (pháp luật yêu cầu văn bản thì thông điệp dữ liệu đáp ứng nếu truy cập và sử dụng được để tham chiếu). Luật KDBH Đ20 k2 i (DNBH bảo mật thông tin), Đ11 k3 (thông tin CSDL KDBH không cung cấp cho bên thứ ba nếu không có chấp thuận). → Yêu cầu chặn luồng xuất đã ở **DLCN-R09**.
- **Áp dụng cho**: BV, PK có bảo lãnh viện phí; app/nền tảng kết nối DNBH · **Hiệu lực**: 01/01/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải** (bổ sung DLCN-R09): mẫu "Yêu cầu cung cấp thông tin cho doanh nghiệp bảo hiểm" dạng điện tử, do **người bệnh** khởi tạo/ký (chữ ký điện tử, OTP gắn định danh), ghi rõ DNBH/TPA nhận, đợt điều trị, loại tài liệu (giấy ra viện, tóm tắt HSBA, HĐ, bảng kê), thời hạn; lưu nguyên thông điệp dữ liệu (Luật 20/2023 Đ13) để tham chiếu; API sang DNBH kiểm tra token yêu cầu còn hiệu lực trước mỗi lần gửi; chỉ gửi đúng phạm vi.
- **Ghi chú / bẫy**: *suy luận*: Luật 20/2023 Đ9 k1 trả lời một phần câu hỏi mở DLCN mục 7 số 5 — yêu cầu điện tử đáp ứng điều kiện "văn bản" nếu truy cập, tham chiếu được; vẫn nên có bằng chứng xác thực người yêu cầu đúng là chủ thể. Hợp đồng bảo hiểm có điều khoản "ủy quyền cho DNBH thu thập hồ sơ y tế" do người mua bảo hiểm ký với DNBH **không thay** được yêu cầu gửi tới cơ sở KCB nếu không xuất trình được — cần luật sư (mục 7).

#### TC-MS-R28 — Toàn vẹn hồ sơ, hóa đơn dùng cho yêu cầu bồi thường bảo hiểm
- **Căn cứ**: Luật KDBH **Đ9 k4 b** (cấm "giả mạo tài liệu, cố ý làm sai lệch thông tin trong hồ sơ yêu cầu bồi thường, trả tiền bảo hiểm"), k4 a (cấm thông đồng giải quyết bồi thường trái luật). NĐ 254 Đ3 k7 (sử dụng HĐ phản ánh không đúng giá trị thực tế, HĐ khống là sử dụng không hợp pháp HĐ). TT 91 Đ10 (chỉ điều chỉnh/thay thế, R09).
- **Áp dụng cho**: mọi cơ sở KCB phát hành chứng từ cho người bệnh đi bồi thường · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: không cho in lại HĐ/bảng kê/giấy ra viện với số liệu khác bản đã phát hành; bản sao in lại ghi "bản sao" và thời điểm in; chặn tách/gộp HĐ theo yêu cầu "cho đẹp hồ sơ bảo hiểm" ngoài quy tắc R02; nhật ký mọi lần in, xuất chứng từ.

#### TC-MS-R29 — Tách khoản phải thu theo bên trả: người bệnh, BHXH, DNBH bảo lãnh, quỹ hỗ trợ
- **Căn cứ**: NĐ 254 Đ9 k4 m (HĐ cho BHXH riêng tại thời điểm quyết toán); Luật KCB Đ111 (quỹ hỗ trợ KCB); Luật KDBH Đ31 k1 (DNBH bồi thường trong thời hạn thỏa thuận, không có thỏa thuận thì 15 ngày từ khi nhận đủ hồ sơ hợp lệ).
- **Áp dụng cho**: BV, PK · **Hiệu lực**: đang áp dụng.
- **Mức**: NÊN (người mua ghi trên HĐ khi DNBH bảo lãnh chưa xác minh — mục 7).
- **Phần mềm phải**: mô hình `payer` cho từng dòng chi phí; công nợ DNBH theo thư bảo lãnh, theo dõi hạn thanh toán; HĐ cho phần bảo lãnh lập theo cấu hình người mua (người bệnh hoặc DNBH) do cơ sở chọn theo hướng dẫn thuế; phần người bệnh tự trả lập HĐ riêng.

#### TC-MS-R30 — Hỗ trợ người bệnh tự lập hồ sơ bồi thường
- **Căn cứ**: Luật KDBH Đ30 k1 (thời hạn nộp hồ sơ bồi thường **01 năm** kể từ ngày xảy ra sự kiện bảo hiểm); Luật KCB Đ12 (quyền đọc, sao chụp HSBA, nhận tóm tắt HSBA; giải thích chi phí).
- **Áp dụng cho**: BV, PK · **Hiệu lực**: đang áp dụng.
- **Mức**: NÊN.
- **Phần mềm phải**: người bệnh tự tải gói chứng từ (HĐ, bảng kê, giấy ra viện, tóm tắt HSBA) qua cổng/app sau xác thực, trong tối thiểu 01 năm sau ra viện; đây là cung cấp cho chính chủ thể nên không vướng Luật 91 Đ26 k2.

### Nhóm E. Đầu tư, mua sắm, thuê dịch vụ công nghệ số bằng NSNN (BV công)

#### TC-MS-R31 — Phân loại "dịch vụ công nghệ số sẵn có" và thủ tục tương ứng
- **Căn cứ**: NĐ 224 **Đ3 k1** (dịch vụ **sẵn có**: được nhà cung cấp phát triển, công bố và cung cấp rộng rãi cho nhiều khách hàng; dùng theo điều kiện nhà cung cấp công bố, không phải xây dựng dịch vụ mới cho yêu cầu đặc thù); **k2** (không sẵn có: xây dựng theo yêu cầu riêng); **Đ36 k4** (CQNN **ưu tiên thuê** dịch vụ sẵn có; **không thuê dịch vụ để nâng cấp, mở rộng** hệ thống đã đầu tư, mua sắm); Đ36 k1 (Chương VI áp cho dự án, nhiệm vụ có NSNN ≥ 30% hoặc lớn nhất); **Đ65 k1 b** (thuê dịch vụ sẵn có: không phải lập dự án/kế hoạch thuê; được thuê nhiều năm; giá theo báo giá tại thời điểm thuê); **Đ65 k3, Đ67** (thuê dịch vụ không sẵn có: lập, thẩm định (≤20 ngày làm việc), phê duyệt (≤03 ngày làm việc) kế hoạch thuê). Đ38 (danh mục **phần mềm phổ biến**: bộ công bố; nhà cung cấp công bố trên website tên phần mềm và **giá cung cấp**, không nâng khống giá giữa các đơn vị; mua/thuê theo thủ tục phần mềm thương mại, dịch vụ sẵn có).
- **Áp dụng cho**: BV công dùng NSNN; vendor bán HIS/EMR/LIS/PACS dạng SaaS · **Hiệu lực**: 01/07/2026 (dự án đã quyết định theo NĐ 45/2026 tiếp tục theo NĐ 45 — Đ91 k2).
- **Mức**: BẮT BUỘC (với bên dùng NSNN); vendor: BẮT BUỘC? (phải có tài liệu để bên mua chứng minh).
- **Phần mềm phải** (vendor): công bố công khai danh mục gói dịch vụ, điều kiện sử dụng, bảng giá niêm yết (NĐ 224 Đ67 k3 đ dùng "giá niêm yết của nhà cung cấp" làm căn cứ dự toán); tách rõ phần cấu hình (sẵn có) với phần phát triển riêng (không sẵn có) trong báo giá; đa tenant, cấu hình không cần sửa mã nguồn (gắn với Đ22 k5).
- **Ghi chú / bẫy**: hợp đồng "thuê HIS" nhưng thực chất là viết riêng cho một bệnh viện thì là dịch vụ **không sẵn có** → cần kế hoạch thuê theo Đ67; "thuê để nâng cấp hệ thống đã mua" bị cấm (Đ36 k4).

#### TC-MS-R32 — Sở hữu và bàn giao toàn bộ thông tin, dữ liệu khi kết thúc thuê; xóa tại nhà cung cấp
- **Căn cứ**: NĐ 224 **Đ57 k2** (sau khi kết thúc thời gian thuê, nhà thầu phải bàn giao **toàn bộ thông tin, dữ liệu hình thành** trong quá trình thuê cho chủ đầu tư); **Đ67 k2 đ** (kế hoạch thuê phải "xác định, làm rõ việc sở hữu các thông tin, dữ liệu" và phương án quản lý, chuyển giao); **Đ67 k7** (bàn giao toàn bộ khi kết thúc); Đ39 k4 b (thử nghiệm: dữ liệu thuộc sở hữu cơ quan nhà nước). TT 41 **Đ15 k4 a** (hợp đồng thuê thống nhất: phương pháp, công cụ, quy trình, vai trò chuyển giao; thống kê, phân loại, kiểm tra tình trạng dữ liệu trước chuyển giao; sao lưu, phục hồi trước chuyển giao; kiểm tra, **đối soát sau chuyển giao**; **xóa toàn bộ** thông tin, dữ liệu tại hệ thống nhà cung cấp sau chuyển giao; cam kết sau chuyển giao); Đ15 k4 b–c (an ninh mạng, dữ liệu, DLCN; bản quyền, SHTT); **Đ16 k2 c** (biên bản bàn giao dữ liệu theo Mẫu số 4 PL VIII là tài liệu nghiệm thu). → bổ sung cho **ANM-R22, ANM-R23** (NĐ 331 Đ5 k3 a; CV 365).
- **Áp dụng cho**: vendor SaaS và BV công thuê bằng NSNN; *suy luận*: NÊN áp cho cả BV tư, PK · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: chức năng **xuất toàn bộ dữ liệu của tenant** (CSDL, tệp đính kèm, HSBA đã ký, XML HĐĐT, nhật ký) ở định dạng mở có từ điển dữ liệu; báo cáo thống kê trước/sau chuyển giao (số bản ghi từng bảng, checksum) để đối soát; quy trình xóa có biên bản (gồm bản sao lưu theo vòng đời) chỉ chạy sau khi bên thuê xác nhận đối soát; dữ liệu phải lưu đủ thời hạn HSBA (K1) ở phía bên thuê trước khi xóa phía vendor.

#### TC-MS-R33 — Yêu cầu chất lượng dịch vụ (SLA), giám sát và báo cáo kết quả cung cấp dịch vụ
- **Căn cứ**: TT 41 **Đ14 k1** (6 nhóm tiêu chí: chức năng; hiệu năng; an ninh mạng, dữ liệu, DLCN; phi chức năng khác; hài lòng người dùng; quản lý dịch vụ); PL VI (ví dụ 4.2.1 khả năng **truy xuất dữ liệu** sinh ra trong quá trình sử dụng và định dạng truy xuất; 4.2.3 hỗ trợ người khuyết tật; 4.3.1 số lần gián đoạn chấp nhận được, thời gian giữa các sự cố; 4.3.2 thời gian khôi phục, tỷ lệ phục hồi, thời gian cam kết khôi phục dữ liệu; 6.3 chế độ báo cáo dịch vụ; 6.5–6.6 quản lý thay đổi, phiên bản; 7.1–7.2 khôi phục hệ thống, dữ liệu); **Đ15 k3** (bên thuê giám sát qua khảo sát, phản hồi người dùng, kiểm tra định kỳ/đột xuất; nhà cung cấp **báo cáo kết quả cung cấp dịch vụ** định kỳ/đột xuất theo hợp đồng); Đ16 (nghiệm thu dựa trên báo cáo của nhà cung cấp Mẫu 2, báo cáo giám sát Mẫu 3, biên bản bàn giao dữ liệu Mẫu 4). NĐ 224 Đ67 k6.
- **Áp dụng cho**: vendor cho thuê, BV công · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (khi thuê bằng NSNN).
- **Phần mềm phải**: đo và lưu uptime, sự cố (bắt đầu, kết thúc, ảnh hưởng, nguyên nhân), thời gian khôi phục, kết quả thử khôi phục sao lưu, thay đổi/phiên bản đã triển khai; xuất báo cáo kỳ theo cấu trúc Mẫu 2 PL VIII TT 41 (nội dung mẫu chưa đọc chi tiết); kênh thu phản hồi người dùng.

#### TC-MS-R34 — Vận hành thử trước nghiệm thu
- **Căn cứ**: TT 41 Đ15 k1 (dịch vụ trước khi đưa vào sử dụng phải được **vận hành thử tại ít nhất một đơn vị thụ hưởng**; đạt yêu cầu là cơ sở nghiệm thu; biên bản Mẫu 1 PL VIII); NĐ 224 Đ67 k5 (vận hành thử lặp lại đến khi đạt; báo cáo kết quả vận hành thử); Đ65 k7 a (hoạt động chi thường xuyên điểm a, d, đ phải vận hành thử trước nghiệm thu).
- **Áp dụng cho**: BV công; vendor · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: môi trường/tenant vận hành thử tách biệt nhưng cùng phiên bản với môi trường chính thức; bộ kịch bản kiểm thử nghiệp vụ (BHYT XML, HĐĐT, ký số) và báo cáo kết quả xuất được.

#### TC-MS-R35 — Dự án đầu tư phần mềm nội bộ: bàn giao mã nguồn, tài liệu; bảo hành
- **Căn cứ**: NĐ 224 **Đ57 k1 b** (xây dựng, nâng cấp phần mềm nội bộ: bàn giao tài liệu, thiết kế chi tiết, bộ cài đặt, **mã nguồn**, hướng dẫn cài đặt, vận hành, tài liệu đào tạo, quy trình bảo trì); Đ57 k1 a (tài liệu kỹ thuật phục vụ kết nối); **Đ59** (bảo hành tối thiểu 24 tháng (quan trọng quốc gia, nhóm A, bảo lãnh 3%) hoặc 12 tháng (nhóm B, C, bảo lãnh 5%); không áp cho thuê dịch vụ); Đ60 k3 (được chỉ định thầu nhà cung cấp sản phẩm để vận hành, bảo trì).
- **Áp dụng cho**: BV công đặt hàng phần mềm riêng bằng NSNN; vendor · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: quy trình build tái lập được từ mã nguồn bàn giao; danh mục thành phần bên thứ ba và giấy phép; tài liệu API kết nối (BHXH, HĐĐT, LIS/PACS).

#### TC-MS-R36 — Nguyên tắc kiến trúc và thiết kế hệ thống số
- **Căn cứ**: Luật 148/2025 **Đ7** (dùng nền tảng, thành phần dùng chung; cloud; chuẩn mở, API chuẩn; an ninh mạng, bảo vệ dữ liệu từ thiết kế; dữ liệu làm trung tâm, "khai báo một lần"; người dùng làm trung tâm; mô-đun) — k8: CQNN **có trách nhiệm** tuân thủ, tổ chức khác được khuyến khích. NĐ 224 **Đ23**: k2 a (cloud là giải pháp xem xét đầu tiên), **k2 b** ("thiết kế phần mềm không được giới hạn theo quy mô người sử dụng"), k3 b (thuyết minh dịch vụ API kết nối bên ngoài), k4 a (xác định cấp độ an ninh mạng khi thiết kế), **k5 a–b** (mô hình thực thể dữ liệu trong thiết kế; **dữ liệu chủ chỉ lưu tại một hệ thống số**, hệ thống khác truy cập trực tuyến), k6 a–b (cho phép người dùng **hủy bỏ thao tác** trước đó; giao diện điều chỉnh cỡ, tiếp cận), k7 a (hạn chế tính năng đặc thù của một công nghệ). Đ24 k1 (đánh giá tuân thủ trước khi phê duyệt dự án, nhiệm vụ của CQNN). Đ23 k3 (Luật 148) ưu tiên mô hình cloud trong đầu tư, mua sắm, thuê.
- **Áp dụng cho**: dự án, nhiệm vụ CĐS của CQNN; *suy luận*: BV công dùng NSNN chịu qua Chương VI NĐ 224 (Đ37); BV tư, PK: NÊN · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC? (BV công là ĐVSNCL, không phải "cơ quan nhà nước" theo nghĩa hẹp; áp qua yêu cầu tuân thủ Khung kiến trúc khi dùng NSNN — mục 7); NÊN với khu vực tư.
- **Phần mềm phải**: hồ sơ thiết kế có mô hình thực thể dữ liệu và bản đồ API; không khóa license theo số người dùng ở mức kỹ thuật (giới hạn thương mại thì để ở hợp đồng); master data (người bệnh, nhân viên, danh mục) có một nguồn chính, hệ thống vệ tinh tra cứu trực tuyến; có undo/hoàn tác cho thao tác nhập liệu khi an toàn nghiệp vụ cho phép.

#### TC-MS-R37 — Yêu cầu tối thiểu với hệ thống số, nền tảng số phục vụ lợi ích công
- **Căn cứ**: Luật 148/2025 **Đ8 k1** (bắt buộc cho hệ thống của CQNN, **hệ thống số phục vụ lợi ích công**, dịch vụ số thiết yếu, hệ thống của tổ chức được giao cung cấp dịch vụ công); k2 (an ninh mạng theo cấp độ), k3 (chuẩn dữ liệu, API), k4 (lưu trữ, sao lưu, phục hồi), k5 (mức sẵn sàng tối thiểu, dự phòng), **k6** (ghi nhận, lưu trữ, bảo vệ **nhật ký hoạt động**, truy vết phục vụ thanh tra, kiểm toán), **k7** (khả năng tiếp cận tối thiểu cho người khuyết tật, người cao tuổi), k8 (lộ trình theo phân loại rủi ro do Chính phủ quy định). NĐ 224 Đ25 k2 (chủ quản HTTT bắt buộc áp dụng tự quy định việc áp dụng theo thực tế); **Đ27 k1–2** (nền tảng số: bắt buộc với nền tảng số dùng chung của CQNN, phục vụ lợi ích công, dịch vụ số thiết yếu; áp cho nền tảng đưa vào vận hành **từ 01/07/2027**; nền tảng vận hành trước đó phải đáp ứng **không chậm hơn 31/12/2028**); Đ26 (tiêu chí nền tảng số: ≥2 bên độc lập tham gia, vai trò trung gian/giao dịch).
- **Áp dụng cho**: *suy luận*: HIS của BV công có thể là "hệ thống số phục vụ lợi ích công"; nền tảng đặt khám, khám từ xa nhiều bên có thể là "nền tảng số" · **Hiệu lực**: 01/07/2026; 01/07/2027; 31/12/2028.
- **Mức**: BẮT BUỘC? (định nghĩa "phục vụ lợi ích công" chưa có hướng dẫn BKHCN — mục 7).
- **Phần mềm phải**: nhật ký hoạt động bất biến, truy vết được; RPO/RTO công bố; WCAG-tương đương cho cổng người bệnh; kế hoạch nâng cấp trước 31/12/2028 nếu là nền tảng số.

#### TC-MS-R38 — Hồ sơ hưởng ưu đãi sản phẩm, dịch vụ công nghệ số Việt Nam
- **Căn cứ**: TT 34/2025 Đ3 (đồng thời: sở hữu/được quyền cung cấp bởi doanh nghiệp VN có trụ sở chính tại VN và không thuộc Đ23 k1 a–c Luật Đầu tư, hoặc cá nhân VN; có phương án, cam kết hỗ trợ kỹ thuật, bảo hành, bảo trì, nâng cấp, hậu mãi); Đ5 k1–2 (phần mềm: thiết kế, mã nguồn thuộc sở hữu tổ chức/cá nhân VN, hoặc phát triển trên **mã nguồn mở** mà tổ chức VN sở hữu quyền SHTT hoặc được khai thác; chứng minh bằng **GCN đăng ký quyền tác giả** hoặc tài liệu khác); Đ6 k3 (cập nhật thông tin trên **Hệ thống thông tin quốc gia về công nghiệp công nghệ số** và website); Đ7 (chuyển tiếp TT 40/2020).
- **Áp dụng cho**: vendor VN dự thầu gói NSNN · **Hiệu lực**: 01/01/2026.
- **Mức**: NÊN (điều kiện để được ưu đãi, không phải nghĩa vụ).
- **Phần mềm phải**: duy trì SBOM và hồ sơ quyền tác giả cho từng phiên bản sản phẩm; tài liệu cam kết hậu mãi.

#### TC-MS-R39 — Cung cấp thông tin hoàn thành và hiệu quả dự án, nhiệm vụ
- **Căn cứ**: NĐ 224 Đ68 k1 a (trong **20 ngày** từ nghiệm thu hoặc từ ngày đưa dịch vụ vào sử dụng, chủ đầu tư cung cấp thông tin hoàn thành); k2 a (định kỳ **tháng 01 hằng năm**, chủ sử dụng cung cấp thông tin đánh giá hoàn thành mục tiêu, hiệu quả); Đ58 (hồ sơ hoàn thành, lưu trữ).
- **Áp dụng cho**: BV công (chủ đầu tư/chủ trì thuê); vendor hỗ trợ · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (nghĩa vụ của BV công); phần mềm: NÊN.
- **Phần mềm phải**: báo cáo số liệu khai thác (người dùng hoạt động, số lượt KCB xử lý, tỷ lệ HSBA điện tử, số HĐĐT) theo năm để làm báo cáo hiệu quả.

## 3. Pattern thiết kế

### P1. Sổ phiếu thu là nguồn sự thật, máy hóa đơn là phép chiếu — giải quyết R02, R03, R04, R05, R26
- **Mô tả**: mọi dòng tiền vào tạo `receipt` (phiếu thu) trước; HĐĐT được sinh từ receipt theo quy tắc (cá nhân ngay, tổng hợp cuối ngày, BHXH khi quyết toán). Không bao giờ sinh HĐ trực tiếp từ dòng chi phí.
- **Dữ liệu**: `receipt(id, facility_id, cashier_id, encounter_id, payer_type{PATIENT,BHXH,INSURER,FUND}, amount, method{CASH,QR,CARD,TRANSFER,WALLET}, bank_ref, received_at, advance_type{NONE,DEPOSIT_GUARANTEE,PREPAYMENT}, status)`; `receipt_line(receipt_id, charge_line_id, amount)`; `invoice(id, seller_id, mode{CQT_CODE,NO_CODE,CASH_REGISTER}, template_no, series, number, kind{INDIVIDUAL,DAILY_SUMMARY,BHXH_SETTLEMENT,ADJUST,REPLACE}, buyer_*, issued_at, signed_at, cqt_code, status)`; `invoice_receipt(invoice_id, receipt_id)` với ràng buộc **UNIQUE(receipt_id)** khi kind ∈ {INDIVIDUAL, DAILY_SUMMARY}. Chỉ mục `(facility_id, received_at::date) WHERE NOT invoiced` cho job cuối ngày.
- **Luồng**: quầy thu → receipt → (khách yêu cầu) INDIVIDUAL; 23:xx → DAILY_SUMMARY cho receipt chưa gắn; BHXH 06/BH → BHXH_SETTLEMENT.
- **Đánh đổi**: hai lớp chứng từ (phiếu thu + HĐ) tăng lưu trữ nhưng là điều kiện để dùng điểm m; job cuối ngày phải idempotent.

### P2. Máy trạng thái hóa đơn chỉ-thêm và chuỗi điều chỉnh — giải quyết R09, R11, R28
- **Mô tả**: HĐ đã gửi CQT là bất biến. Sửa = tạo bản ghi mới `ADJUST` hoặc `REPLACE` trỏ `original_invoice_id`, hoặc `NOTICE_04SS` (không đổi số tiền).
- **Dữ liệu**: `invoice_correction(id, original_invoice_id, method{NOTICE,ADJUST,REPLACE}, reason, agreement_doc_id | buyer_notice_ref, created_by)`; ràng buộc: method của mọi correction cùng `original_invoice_id` phải bằng method đầu tiên (TT 91 Đ10 k6 a); `mode=CASH_REGISTER ⇒ method=REPLACE`. Lưu `xml_signed`, `xml_hash` (SHA-256), `cqt_response_xml` dạng WORM.
- **Đánh đổi**: báo cáo doanh thu phải tổng hợp theo chuỗi (gốc ± điều chỉnh), phức tạp hơn bảng "sửa tại chỗ".

### P3. Outbox gửi HĐĐT với cửa sổ sự cố — giải quyết R08, R10
- **Mô tả**: HĐ ký xong vào `invoice_outbox`; worker gửi tới nhà cung cấp/T-VAN, cập nhật trạng thái; theo dõi hạn "ngày làm việc tiếp theo" bằng lịch ngày làm việc; khi có `incident` (nguồn: CQT/nhà cung cấp/nội bộ/bất khả kháng) thì tạm dừng đếm hạn và đặt hạn gửi bù 02/03 ngày làm việc sau khi đóng sự cố.
- **Dữ liệu**: `invoice_outbox(invoice_id, attempt, last_error, due_at)`, `incident(id, source, started_at, ended_at, evidence_doc_id, tax_notice_ref)`, `workday_calendar`.
- **Đánh đổi**: cần lịch nghỉ lễ cập nhật hằng năm.

### P4. Danh mục giá có nguồn pháp lý và phiên bản — giải quyết R17, R18, R19, R21, R23
- **Dữ liệu**: `price_list(id, facility_id, legal_source_type{MOH_DECISION,PROVINCIAL_RESOLUTION,FACILITY_DECISION}, legal_ref, effective_from, effective_to)`; `price_item(price_list_id, service_code, category{BHYT,NSNN,NON_BHYT,ON_DEMAND}, unit_price, bhyt_reference_price, published_at, declared_at)`; `charge_line(…, price_item_id, unit_price_snapshot, bhyt_price_snapshot, revenue_stream)`. Ràng buộc: không chồng lấn hiệu lực cho cùng (facility, service_code, category); charge_line chỉ trỏ price_item có `published_at ≤ service_date`.
- **Đánh đổi**: tư nhân BHYT phải nạp thêm bảng giá HĐND địa bàn làm `bhyt_reference_price`.

### P5. Tách bên trả và quy tắc mức hưởng tham số — giải quyết R03, R18, R22, R29
- **Mô tả**: mỗi `charge_line` được phân bổ thành nhiều `charge_allocation(payer_type, amount, rule_id)` theo `benefit_rule` (mức hưởng, trần, đồng chi trả, chênh lệch theo yêu cầu, bảo lãnh DNBH). Phần PATIENT đi P1 tại quầy; BHXH chờ quyết toán; INSURER theo thư bảo lãnh.
- **Đánh đổi**: tái tính khi thẻ BHYT thay đổi giữa đợt (BHYT-GD-R07, R08) phải xử lý cả allocation đã thu tiền → sinh điều chỉnh.

### P6. Thanh toán thẳng vào tài khoản cơ sở (QR động) — giải quyết R24, R25, R26
- **Luồng**: HIS tạo `payment_intent(receipt_draft_id, amount, ref_code)` → sinh chuỗi QR mang **tài khoản của cơ sở** và `ref_code` → người bệnh chuyển → ngân hàng/TGTT có phép gửi webhook (hoặc HIS truy vấn sao kê qua API ngân hàng của cơ sở) → khớp `ref_code` → chốt receipt.
- **Dữ liệu**: `payment_intent`, `bank_txn(bank_ref UNIQUE, amount, ref_code, matched_receipt_id)`; khóa API ngân hàng lưu trong kho bí mật của tenant.
- **Đánh đổi**: không có tài khoản trung gian nên vendor không gộp được phí thu hộ; đổi lại tránh vùng giấy phép TGTT (NĐ 52 Đ8 k7, Đ22).

### P7. Cổng dữ liệu bảo hiểm có "token yêu cầu bằng văn bản" — giải quyết R27, R28, R30 (cùng DLCN-R09)
- **Dữ liệu**: `insurer_disclosure_request(id, patient_id, insurer_id, scope{encounter_ids, doc_types}, valid_until, signed_payload, signature_method{DIGITAL_SIG,OTP,WET_SCAN}, created_at, revoked_at)`; `disclosure_log(request_id, doc_id, doc_hash, sent_at, endpoint)`. API outbound kiểm tra `request` hợp lệ cho từng tài liệu; tài liệu gửi là bản đã phát hành (hash khớp).
- **Đánh đổi**: thêm một bước cho người bệnh tại quầy bảo lãnh; nên cho khởi tạo yêu cầu trên app trước khi nhập viện.

### P8. Bộ "rời đi" (exit kit) của tenant — giải quyết R32, R11 (cùng ANM-R22, R23)
- **Mô tả**: lệnh xuất toàn bộ dữ liệu tenant: dump CSDL ở định dạng mở (CSV/Parquet + DDL), kho tệp (HSBA PDF/A đã ký, ảnh, XML HĐĐT, XML BHYT), nhật ký; kèm `manifest.json` (bảng, số bản ghi, checksum) và từ điển dữ liệu. Biên bản đối soát hai bên (Mẫu 4 PL VIII TT 41) → chỉ sau đó mới chạy `tenant_purge` có biên bản.
- **Đánh đổi**: chi phí duy trì từ điển dữ liệu theo phiên bản; nên làm từ đầu thay vì khi hết hợp đồng.

### P9. Đo SLA và báo cáo dịch vụ định kỳ — giải quyết R33, R34, R37, R39, R16
- **Dữ liệu**: `sla_probe(ts, service, status, latency)`, `incident` (dùng chung P3), `restore_test(ts, backup_id, rto, rpo, result)`, `release(version, deployed_at, change_ticket)`; báo cáo kỳ sinh tự động: uptime, số gián đoạn, MTBF, thời gian khôi phục, kết quả thử khôi phục, thay đổi đã triển khai, số liệu khai thác.
- **Đánh đổi**: cần giám sát độc lập với hệ thống chính để số liệu đáng tin.

### P10. Biên lai và hóa đơn tích hợp cho đơn vị có thu phí/lệ phí — giải quyết R14
- **Dữ liệu**: `fee_receipt(series_year, number ≤ 99999999, fee_type, amount, payer, signed_at)` với chuỗi số reset 01/01; `invoice.kind = INTEGRATED_FEE` (ký hiệu mẫu 8/9) khi cùng giao dịch; job gửi Mẫu 01/TH-BLĐT trong ngày.

## 4. Checklist audit

| ID kiểm tra | Yêu cầu (ID R) | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| TCMS-A01 | R01 | Xem cấu hình người bán: chế độ HĐ (có mã/không mã/MTT) và căn cứ; BV công đang dùng không mã thì hỏi văn bản chấp thuận của cơ quan thuế | Ảnh cấu hình, thông báo chấp nhận đăng ký 01/TB-ĐKĐT | Bắt buộc |
| TCMS-A02 | R02 | Chọn 1 ngày: truy vấn tổng phiếu thu so với tổng HĐ cá nhân + HĐ tổng hợp; tìm phiếu thu không gắn HĐ | Truy vấn SQL, HĐ tổng hợp ngày đó | Bắt buộc |
| TCMS-A03 | R02 | Kiểm tra job cuối ngày: lịch chạy, log lỗi 30 ngày gần nhất; ngày nào không có HĐ tổng hợp dù có phiếu thu | Log job, danh sách ngày thiếu | Bắt buộc |
| TCMS-A04 | R03 | Đối chiếu HĐ cho BHXH với Biên bản quyết toán 06/BH quý gần nhất (cùng GD-A24) | Biên bản, HĐ | Bắt buộc |
| TCMS-A05 | R04 | Ca nội trú có tạm ứng: thời điểm lập HĐ, xử lý khi hoàn ứng | Phiếu thu tạm ứng, HĐ, HĐ điều chỉnh | Bắt buộc? |
| TCMS-A06 | R05 | Mở XML một HĐ tổng hợp: có ghi "kèm theo bảng kê số…"; bảng kê có đủ chỉ tiêu PL 5 a.3; người mua trống thì ghi "Bán cho người tiêu dùng" | XML, bảng kê | Bắt buộc |
| TCMS-A07 | R06 | Nhà thuốc: HĐ có ký hiệu "M", có mã tra cứu/QR; dữ liệu gửi cuối ngày; thử sửa HĐ MTT → chỉ cho thay thế | Ảnh HĐ, log gửi | Bắt buộc |
| TCMS-A08 | R07 | Kiểm tra ký hiệu năm 2026 có dạng "1C26T.." hoặc "2K26T.."; không trùng số | Danh sách ký hiệu | Bắt buộc |
| TCMS-A09 | R08 | Truy vấn HĐ không mã có `sent_to_tax` muộn hơn ngày làm việc tiếp theo; HĐ có mã gửi người mua sau khi có mã bao lâu | Truy vấn, log | Bắt buộc |
| TCMS-A10 | R08 | Thử tra cứu HĐ bằng mã in trên phiếu thu; website công khai cách tra cứu | Ảnh màn hình | Bắt buộc |
| TCMS-A11 | R09 | Thử "hủy" một HĐ đã gửi CQT; thử điều chỉnh rồi lần sau chọn thay thế cho cùng HĐ gốc | Kết quả thử, log | Bắt buộc |
| TCMS-A12 | R09 | Với HĐ điều chỉnh người mua cá nhân: có bằng chứng thông báo cho người mua (hoặc trên website) | Bằng chứng | Bắt buộc |
| TCMS-A13 | R10 | Xem sổ sự cố HĐĐT; với sự cố gần nhất, HĐ gửi bù có trong hạn 02/03 ngày làm việc không | Sổ sự cố, log gửi | Bắt buộc |
| TCMS-A14 | R11 | Lấy ngẫu nhiên 5 HĐ của năm 2026: có XML gốc đã ký, mã CQT, hash khớp; in được bản chuyển đổi | File XML, bản in | Bắt buộc |
| TCMS-A15 | R12 | Nếu nền tảng lập HĐ hộ: có hợp đồng ủy nhiệm đủ nội dung TT 91 Đ9 k2, thông báo CQT; HĐ ghi cả hai bên | Hợp đồng, Mẫu 01/ĐKTĐ-HĐĐT | Bắt buộc |
| TCMS-A16 | R13 | Vendor tự phát hành HĐĐT: có tên trên trang Cục Thuế? có nhật ký truyền nhận đối soát? | Ảnh trang Cục Thuế, log | Bắt buộc? |
| TCMS-A17 | R14 | Đơn vị thu phí/lệ phí: còn in biên lai giấy? kế hoạch chuyển trước 31/12/2026; số biên lai reset 01/01 | Mẫu biên lai, kế hoạch | Bắt buộc |
| TCMS-A18 | R15 | Chi trả bác sĩ cộng tác: có chứng từ khấu trừ TNCN điện tử gửi CQT trong ngày | Chứng từ, log | Bắt buộc |
| TCMS-A19 | R16 | HĐ vendor gửi bệnh viện: ngày lập so với kỳ đối soát (≤ ngày 07 tháng sau) | HĐ, biên bản đối soát | Bắt buộc |
| TCMS-A20 | R17 | Bảng giá: mỗi dòng có loại giá, văn bản phê duyệt, ngày hiệu lực; còn sót bảng giá TT 22/2023? | Xuất bảng giá, truy vấn | Bắt buộc |
| TCMS-A21 | R18 | Ca dịch vụ theo yêu cầu cho người có thẻ: phần chênh lệch = giá thu − mức quỹ; PK tư: giá tham chiếu là giá HĐND địa bàn | Bảng chi phí ca mẫu, NQ HĐND | Bắt buộc |
| TCMS-A22 | R19 | Thử chỉ định/thu một dịch vụ chưa niêm yết | Kết quả thử | Bắt buộc |
| TCMS-A23 | R20 | Yêu cầu bảng chi phí lũy kế giữa đợt nội trú tại quầy và trên app | Bản in, ảnh | Bắt buộc |
| TCMS-A24 | R21 | Tìm dòng thu không gắn mã dịch vụ trong danh mục; dòng sửa đơn giá/số lượng sau chốt không có phê duyệt | Truy vấn, log | Bắt buộc |
| TCMS-A25 | R22 | Ca người ≥75 tuổi/cận nghèo năm 2026: mức hưởng 100%, không sinh phiếu thu | XML1, phiếu thu | Bắt buộc? |
| TCMS-A26 | R23 | Báo cáo doanh thu tách dịch vụ theo yêu cầu; tỷ lệ giường theo yêu cầu | Báo cáo | Bắt buộc |
| TCMS-A27 | R25 | Lần theo dòng tiền QR: tiền vào tài khoản của ai? Vendor có tài khoản trung gian? | Sao kê, hợp đồng ngân hàng/TGTT | Bắt buộc |
| TCMS-A28 | R26 | Đối chiếu 1 ngày giao dịch ngân hàng với phiếu thu | Sao kê, truy vấn | Nên |
| TCMS-A29 | R27 | Liệt kê tích hợp DNBH/TPA; với 10 hồ sơ bảo lãnh, truy ra yêu cầu điện tử/giấy của người bệnh đúng phạm vi, còn hạn (cùng DLCN-A10) | Yêu cầu đã ký, disclosure_log | Bắt buộc |
| TCMS-A30 | R28 | In lại HĐ/bảng kê/giấy ra viện đã phát hành: có nhãn "bản sao", số liệu không đổi; có cách nào sửa số liệu rồi in "bản chính" mới không | Kết quả thử, log in | Bắt buộc |
| TCMS-A31 | R29 | Ca bảo lãnh viện phí: tách công nợ DNBH, HĐ phần bảo lãnh và phần tự trả | Công nợ, HĐ | Nên |
| TCMS-A32 | R31 | Hợp đồng thuê HIS bằng NSNN: dịch vụ được phân loại sẵn có hay không; nếu không sẵn có có kế hoạch thuê được duyệt; có hạng mục "thuê để nâng cấp hệ thống đã mua" không | Hợp đồng, QĐ phê duyệt | Bắt buộc |
| TCMS-A33 | R32 | Hợp đồng có điều khoản sở hữu dữ liệu và phương án chuyển giao theo TT 41 Đ15 k4 a; chạy thử xuất toàn bộ dữ liệu tenant và kiểm manifest | Hợp đồng, gói xuất thử | Bắt buộc |
| TCMS-A34 | R33 | Xem báo cáo dịch vụ kỳ gần nhất: có uptime, sự cố, thời gian khôi phục, thử khôi phục sao lưu | Báo cáo Mẫu 2 | Bắt buộc |
| TCMS-A35 | R34 | Biên bản vận hành thử tại đơn vị thụ hưởng trước nghiệm thu | Biên bản Mẫu 1 PL VIII | Bắt buộc |
| TCMS-A36 | R35 | Dự án phần mềm nội bộ: đã nhận mã nguồn, build lại được; bảo lãnh bảo hành 3%/5% | Biên bản bàn giao, kết quả build | Bắt buộc |
| TCMS-A37 | R36 | Hồ sơ thiết kế có mô hình thực thể dữ liệu, danh mục API; license có giới hạn kỹ thuật số người dùng không | Tài liệu thiết kế | Bắt buộc? |
| TCMS-A38 | R37 | Nhật ký hoạt động có bị sửa/xóa được bởi quản trị viên không; cổng người bệnh có hỗ trợ trình đọc màn hình, phóng chữ | Kết quả thử | Bắt buộc? |
| TCMS-A39 | R38 | Vendor dự thầu hưởng ưu đãi: GCN quyền tác giả, thông tin trên HTTT quốc gia về CN công nghệ số | Giấy chứng nhận, ảnh | Nên |
| TCMS-A40 | R39 | Bệnh viện đã gửi thông tin hoàn thành trong 20 ngày và báo cáo hiệu quả tháng 01 | Văn bản gửi | Bắt buộc |

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái (so với 2026-10-05) | Nội dung | Ai phải làm |
|---|---|---|---|
| 01/01/2023 | qua | Luật KDBH 08/2022 có HL | DNBH; cơ sở có bảo lãnh viện phí |
| 01/01/2024 | qua | Luật KCB: Đ12 (giải thích chi phí), Đ60 k4 (niêm yết), Đ110 (giá); NĐ 96 Đ119 | Mọi cơ sở KCB |
| 01/07/2024 | qua | NĐ 52/2024 thanh toán không dùng tiền mặt có HL | Vendor tích hợp thanh toán |
| 17/10/2024 | qua | TT 21/2024/TT-BYT có HL | BV công (định giá, dịch vụ theo yêu cầu) |
| 01/01/2025 | qua | TT 13/2023, 21/2023, 22/2023/TT-BYT hết HL — hết bảng giá thống nhất toàn quốc | Vendor: gỡ bảng giá cài sẵn |
| 30/07/2025 | qua | CĐ 124/CĐ-TTg thúc đẩy TTKDTM | Bộ, UBND tỉnh (gián tiếp cơ sở KCB) |
| 01/01/2026 | qua | Luật 91/2025 (Đ26); NQ 261 (mức hưởng 100% cho một số nhóm, thứ cấp); TT 34/2025 (ưu đãi sản phẩm số VN; TT 40/2020 hết HL) | Cơ sở KCB; vendor |
| 16/01/2026 | qua | NĐ 310/2025 sửa NĐ 125/2020 (khung phạt HĐ sai thời điểm, không lập HĐ) | Mọi người bán |
| 01/03/2026 | qua | NĐ 45/2026 thay NĐ 73/2019, NĐ 82/2024; NQ 04/2025/NQ-CP hết HL | BV công có dự án CNTT |
| 01/07/2026 | qua | **NĐ 254/2026 + TT 91/2026** (NĐ 123/2020, Đ1 NĐ 41/2022, NĐ 70/2025, TT 32/2025 hết HL); **Luật 148/2025 + NĐ 224/2026** (NĐ 45/2026, NĐ 42/2022, NĐ 64/2007 hết HL; Luật CNTT hết HL); **TT 39/2026** (TT 18/2024/TT-BTTTT hết HL); **TT 41/2026** (TT 16/2024/TT-BTTTT hết HL) | Mọi người bán; BV công; vendor |
| 21/07/2026 | qua | NĐ 291/2026 sửa NĐ 125/2020 (chỉ phần trao đổi thông tin thuế) | — |
| **31/12/2026** | tới | Hết dùng biên lai giấy tự in/đặt in (NĐ 254 Đ44 k2) | Đơn vị y tế công có thu phí/lệ phí |
| **01/01/2027** | tới | Tiêu hủy biên lai giấy chưa dùng; bắt buộc biên lai điện tử | Như trên |
| 01/07/2027 | tới | Yêu cầu tối thiểu bắt buộc với nền tảng số mới đưa vào vận hành (NĐ 224 Đ27 k2) | Chủ quản nền tảng số phục vụ lợi ích công (phạm vi chưa rõ) |
| 31/12/2028 | tới | Nền tảng số vận hành trước 01/07/2027 phải đáp ứng yêu cầu tối thiểu | Như trên |
| 01/01/2030 | tới | Miễn viện phí mức cơ bản trong phạm vi BHYT theo lộ trình (NQ 261, thứ cấp) | Cơ sở KCB BHYT; vendor HIS (module viện phí) |

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuỗi thay thế (đã xác minh trên bản gốc):**

| Cũ | → | Mới | Từ ngày | Căn cứ |
|---|---|---|---|---|
| NĐ 123/2020, Đ1 NĐ 41/2022, NĐ 70/2025 | → | NĐ 254/2026 | 01/07/2026 | NĐ 254 Đ43 k2 |
| TT 32/2025/TT-BTC | → | TT 91/2026/TT-BTC | 01/07/2026 | TT 91 Đ25 k2 |
| NĐ 125/2020 (xử phạt thuế, HĐ) | sửa bởi | NĐ 102/2021 → NĐ 310/2025 (16/01/2026) → NĐ 291/2026 (21/07/2026) | — | Trích yếu NĐ 291; NĐ 310 Điều hiệu lực |
| TT 13/2023, TT 21/2023, TT 22/2023/TT-BYT (giá) | → | hết HL, không có bảng giá thống nhất mới; giá cụ thể theo QĐ BYT / NQ HĐND / cơ sở tự quyết | 01/01/2025 | TT 21/2024 Đ11 k2 |
| NĐ 73/2019 + NĐ 82/2024 (+ NQ 04/2025/NQ-CP) | → | NĐ 45/2026 | 01/03/2026 | NĐ 45 Đ41 k1–3 (Công báo) |
| NĐ 45/2026, NĐ 42/2022, NĐ 64/2007 | → | NĐ 224/2026 | 01/07/2026 | NĐ 224 Đ90 k2; chuyển tiếp Đ91 |
| TT 18/2024/TT-BTTTT (chi phí) | → | TT 39/2026/TT-BKHCN | 01/07/2026 | TT 39 Đ10 k2, k4 |
| TT 16/2024/TT-BTTTT (triển khai, nghiệm thu, thuê theo yêu cầu riêng) | → | TT 41/2026/TT-BKHCN | 01/07/2026 | TT 41 Đ20 k2, k4 |
| TT 40/2020/TT-BTTTT (ưu tiên sản phẩm trong nước) | → | TT 34/2025/TT-BKHCN | 01/01/2026 | TT 34 Đ8 k2 |
| Luật CNTT 67/2006 | → | Luật Chuyển đổi số 148/2025 | 01/07/2026 | Luật 148 Đ47 k2; Đ48 chuyển tiếp |
| QĐ 1813/QĐ-TTg (Đề án TTKDTM 2021–2025) | → | chưa xác minh đề án kế nhiệm | — | CĐ 124 mục 3 a |

**Bẫy trích dẫn:**
1. **"Điểm m NĐ 70/2025"** → nay là **NĐ 254 Đ9 k4 m**. NĐ 70 và NĐ 123 hết HL từ 01/07/2026. TT 12/2026/TT-BTC Đ14 k6 vẫn dẫn NĐ 123/NĐ 70 (xem BHYT-GD mục 6 số 7).
2. **"Hủy hóa đơn điện tử"** không còn là cách xử lý HĐ sai trong TT 91 Đ10 (chỉ thông báo 04/SS, điều chỉnh, thay thế). Thuật ngữ "hủy" chỉ còn ở Đ19 k1 e NĐ 254 (trách nhiệm bên nhận ủy nhiệm) và ở việc tiêu hủy HĐ hết hạn lưu trữ (Đ3 k8).
3. **"Luật KCB Đ110–112 về giá, giá theo yêu cầu, niêm yết"**: chỉ **Đ110** là giá (gồm giá theo yêu cầu ở k7–k8). Đ111 là Quỹ hỗ trợ KCB. Đ112 là HTTT quản lý hoạt động KCB (k1 đ, e chỉ liệt kê thông tin giá, chi phí trong HTTT). Niêm yết giá là **Đ60 k4**.
4. **"Biên lai viện phí"**: viện phí của BV công là **giá dịch vụ** theo Luật KCB Đ110 (*suy luận*: không phải phí/lệ phí) → dùng **hóa đơn**, không dùng biên lai. Mốc 31/12/2026 của Đ44 k2 chỉ liên quan khoản phí/lệ phí.
5. **"NĐ 224/2026 thay NĐ 73/2019"** là sai trực tiếp: NĐ 73/2019 bị **NĐ 45/2026** thay từ 01/03/2026; NĐ 224 thay NĐ 45/2026. Dự án quyết định theo NĐ 45/2026 trước 01/07/2026 vẫn theo NĐ 45 (NĐ 224 Đ91 k2).
6. **"Bảng giá BHYT thống nhất theo hạng bệnh viện (TT 22/2023)"**: hết HL 01/01/2025. Đừng trích các mức giá khám 42.100/37.500... làm giá hiện hành.
7. **"Máy tính tiền bắt buộc cho phòng khám"**: NĐ 254 Đ6 k1 c không liệt kê dịch vụ y tế; phòng khám HKD chỉ chịu Đ6 k1 d (doanh thu > 1 tỷ: HĐĐT có mã **hoặc** MTT). Nhà thuốc bán lẻ mới thuộc Đ6 k1 c.
8. **"Thuê dịch vụ CNTT" (NĐ 73, TT 16/2024)** → nay là **"thuê dịch vụ công nghệ số"** sẵn có/không sẵn có (NĐ 224 Đ3 k1–2).
9. Inventory ghi "TT 39/2026 quan hệ với TT 18/2024 chưa rõ": đã rõ — TT 39 làm TT 18/2024 hết HL (trừ dự án chuyển tiếp).
10. NĐ 291/2026 **không** sửa các điều phạt về hóa đơn; khung phạt HĐ hiện hành nằm ở NĐ 125 Đ24 theo NĐ 310/2025.

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Tạm ứng viện phí** là "thu tiền trước" (phải lập HĐ khi thu, NĐ 254 Đ9 k2) hay "đặt cọc" (không lập)? Không có hướng dẫn riêng cho KCB trong NĐ 254/TT 91. **Hỏi Cục Thuế** bằng văn bản; phần mềm cấu hình hai chế độ (R04).
2. **BV công (ĐVSNCL) dùng HĐĐT có mã hay không mã**: suy luận từ Đ6 k1 a–b là có mã (Đ6 k1 b chỉ nói "doanh nghiệp"). Hỏi cơ quan thuế quản lý.
3. **HKD doanh thu ≤ 1 tỷ** (nhà thuốc, phòng khám nhỏ) có bắt buộc HĐĐT không: Đ6 k1 a và Đ6 k1 d đọc cùng nhau chưa nhất quán. Hỏi cơ quan thuế.
4. **Người mua ghi trên HĐ khi DNBH bảo lãnh viện phí** (người bệnh hay DNBH), và HĐ khi bên thứ ba (doanh nghiệp) trả tiền KSK cho nhân viên. Chưa thấy quy định riêng.
5. **Thuế GTGT với dịch vụ y tế** (không chịu thuế theo Luật thuế GTGT 48/2024) và loại HĐ (GTGT ghi KCT hay HĐ bán hàng) theo phương pháp tính thuế của cơ sở: chưa đọc gốc Luật 48/2024 trong pha này.
6. **Danh mục khoản "phí, lệ phí" mà đơn vị y tế công thu** (để biết ai chịu biên lai điện tử): cần đọc Luật Phí và lệ phí 2015 và NĐ 362/2025 (được NĐ 254 Đ23 k2 dẫn chiếu).
7. **Thời hạn lưu HĐĐT**: NĐ 174/2016 Đ12–13 (5/10 năm) mới đọc qua nguồn thứ cấp; cần kiểm tra Luật Kế toán và nghị định hướng dẫn hiện hành.
8. **Chế tài hóa đơn cho tổ chức hay cá nhân**: khung tiền NĐ 125 Đ24 (sửa bởi NĐ 310) áp cho đối tượng nào (NĐ 125 Đ7 — chưa đọc gốc).
9. **Vendor dùng QR/tài khoản ảo/đối soát thay bệnh viện** có rơi vào "dịch vụ hỗ trợ thu hộ, chi hộ" hoặc "cổng thanh toán điện tử" (NĐ 52 Đ3 k17–18) không: **cần luật sư hoặc ý kiến NHNN**. TT 15/2024/TT-NHNN và các TT sửa đổi 30/2025, 21/2026 chưa đọc; tiêu chuẩn kỹ thuật QR của NHNN chưa đọc.
10. **Đề án TTKDTM kế nhiệm QĐ 1813** và mục tiêu tỷ lệ không tiền mặt trong y tế: chưa tìm được văn bản gốc; "Cổng Bảo lãnh thanh toán viện phí" (ra mắt 02/02/2026, có ngân hàng phong tỏa/giải tỏa tiền) chỉ có nguồn báo, chưa thấy căn cứ pháp lý.
11. **NQ 261/2025** chưa đọc bản gốc (chỉ luatvietnam); nhóm hưởng 100% chính xác và hướng dẫn thi hành (NĐ/TT của Chính phủ, BYT) chưa đọc; khái niệm "miễn viện phí ở mức cơ bản" chưa có định nghĩa.
12. **Quy tắc áp giá khi giá thay đổi giữa đợt điều trị** sau khi TT 22/2023 hết hiệu lực: chưa xác định văn bản hiện hành (có thể nằm trong từng QĐ/NQ phê duyệt giá hoặc NĐ 188/2025).
13. **NĐ 96/2023** có bị sửa/thay trong 2025–2026 (báo chí 2025 nói có dự thảo nghị định thay thế, đề xuất phân quyền định giá): chưa kiểm. Đ119 trích trong file này theo bản 2023.
14. **Luật Giá 16/2023** (niêm yết, kê khai) và NĐ 85/2024 (sửa bởi NĐ 128/2026 — thứ cấp), NĐ 87/2024 (xử phạt giá): chưa đọc gốc; nội dung hồ sơ kê khai giá dịch vụ KCB chưa rõ.
15. **NĐ 224 Chương VI có áp cho BV công tự chủ chi từ nguồn thu sự nghiệp/quỹ phát triển hoạt động sự nghiệp** không (Đ36 k1 chỉ nói NSNN ≥ 30% hoặc lớn nhất). Quan hệ với Luật Đấu thầu khi ĐVSNCL dùng nguồn thu hợp pháp: **cần luật sư**.
16. **"Hệ thống số phục vụ lợi ích công"** (Luật 148 Đ8 k1; NĐ 224 Đ27) có bao gồm HIS của BV công, BV tư có BHYT không; hướng dẫn BKHCN về yêu cầu tối thiểu (NĐ 224 Đ27 k3) chưa ban hành hoặc chưa đọc.
17. **Danh mục phần mềm phổ biến ngành y tế** (NĐ 224 Đ38 k2 a) BYT đã công bố chưa: chưa tìm thấy.
18. **TT 94/2026/TT-BTC** (tiêu chí rủi ro cao về thuế, hóa đơn) và **NĐ 104/2026/NĐ-CP** (chi thường xuyên) được dẫn chiếu nhưng chưa đọc.
19. Điều khoản trong hợp đồng bảo hiểm (bên mua bảo hiểm ủy quyền cho DNBH thu thập hồ sơ y tế) có thay thế "yêu cầu bằng văn bản của chủ thể" theo Luật 91 Đ26 k2 khi DNBH trực tiếp đề nghị cơ sở KCB không: **cần luật sư**; mặc định phần mềm yêu cầu văn bản/thông điệp dữ liệu từ chính người bệnh (R27).
20. Nội dung các mẫu PL VIII TT 41 (Mẫu 1–5) và PL VI đầy đủ chưa đọc chi tiết từng ô; file này chỉ dùng tiêu đề tiêu chí.
