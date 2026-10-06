# Khảo sát pháp lý Y tế số / Phần mềm y tế VN — góc THỜI GIAN

> Mốc tham chiếu: **2026-10-05**. Phạm vi: HIS, EMR/HSBA điện tử, phần mềm phòng khám, LIS/RIS-PACS, dược/đơn thuốc, KCB từ xa, sổ sức khỏe điện tử (SKĐT), liên thông BHYT, dữ liệu sức khỏe, an ninh mạng, AI.
>
> **Quy ước mức xác minh**
> - **Gốc**: đã đọc toàn văn (PDF/DOCX trên datafiles/congbao/congbaocdn hoặc file ký số của cơ quan nhà nước) và thấy đúng điều khoản.
> - **Gốc-CSDL**: đọc qua cơ sở dữ liệu pháp luật bên thứ ba có toàn văn (caselaw.vn), khớp số hiệu.
> - **Thứ cấp**: chỉ đọc qua báo / cổng tin / trang tóm tắt (chưa thấy toàn văn điều khoản).
> - **Chưa xác minh**: chỉ thấy trong kết quả search hoặc suy luận; KHÔNG dùng để trích dẫn.
>
> Cột "Link OK" = URL đã được mở thành công (WebFetch/curl) và nội dung khớp số hiệu. `N` = link chưa kiểm tra được / bị chặn (thuvienphapluat 403, vbpl.vn render JS) hoặc PDF scan không đọc được chữ.

---

## 0. TL;DR — 10 điều phần mềm y tế phải nhớ

1. **31/12/2026**: mọi cơ sở KCB còn lại (không phải bệnh viện) có điều trị nội trú/ban ngày/ngoại trú phải xong HSBA điện tử (TT 13/2025/TT-BYT). **01/01/2027**: bệnh viện (công + tư) không còn dùng bệnh án giấy (QĐ 586/QĐ-BYT, CT 04/CT-BYT).
2. **01/01/2027**: chậm nhất phải **liên thông, sử dụng kết quả cận lâm sàng** giữa các cơ sở KCB BHYT (Luật 51/2024/QH15, Điều 3 khoản 4 — gốc). Kèm dự thảo TT danh mục ~441 dịch vụ CLS dùng lại.
3. **Dự thảo TT thay TT 48/2017/TT-BYT** (trích chuyển dữ liệu BHYT): gửi dữ liệu XML ký số **trong 03 giờ** sau khi kết thúc lượt khám; góp ý đến **07/10/2026**, dự kiến hiệu lực **01/01/2027**; có chế tài xử phạt khi chậm.
4. **01/07/2027**: hết 12 tháng chuyển tiếp của **Luật An ninh mạng 116/2025/QH15** — HTTT đã xác định cấp độ theo luật cũ phải đáp ứng điều kiện/biện pháp theo luật mới (Điều 45 — gốc). NĐ 331/2026 thay NĐ 85/2016 (thứ cấp): HT xử lý DLCN nhạy cảm ≥ 10.000 chủ thể → cấp độ 3 trở lên.
5. **01/09/2027**: hệ thống AI **lĩnh vực y tế** đã vận hành trước 01/03/2026 phải tuân thủ Luật Trí tuệ nhân tạo 134/2025/QH15 (Điều 35 — gốc; 18 tháng).
6. **Luật BVDLCN 91/2025/QH15 + NĐ 356/2025** hiệu lực **01/01/2026**, NĐ 13/2023 hết hiệu lực. Miễn trừ 5 năm cho DN nhỏ/khởi nghiệp **KHÔNG áp dụng** nếu trực tiếp xử lý DLCN nhạy cảm (sức khỏe) → phần mềm y tế gần như không được miễn. "Dịch vụ thu thập, xử lý DLCN qua phần mềm chăm sóc sức khỏe, dịch vụ y tế" là **dịch vụ xử lý DLCN** (NĐ 356 Điều 21 khoản 4) → điều kiện kinh doanh + giấy chứng nhận. Phạt theo NĐ 330/2026 (đến 3 tỷ — thứ cấp).
7. Kê đơn điện tử: bệnh viện trước **01/10/2025**, cơ sở khác trước **01/01/2026** (TT 26/2025, gốc) — **đã bắt buộc**. Thuốc cổ truyền: TT 55/2025 (hiệu lực 01/03/2026) thay TT 44/2018.
8. Chuẩn dữ liệu BHYT: QĐ 130/QĐ-BYT vẫn là gốc, sửa bởi 4750/2023, 3176/2024 và **QĐ 1931/QĐ-BYT (áp dụng 01/07/2026)**; **QĐ 1804/QĐ-BYT** mã loại hình KCB + mã khoa áp dụng chậm nhất **01/08/2026** (thay QĐ 824/2023 & 2010/2025).
9. Sổ SKĐT trên VNeID: QĐ 1551/QĐ-BYT (31/5/2026) — dữ liệu khám sức khỏe định kỳ/sàng lọc phải đẩy về CSDL sức khỏe cá nhân BYT **trong 24 giờ** sau đợt khám, ký số, API REST (`api.emrhub.vn`). Đồng bộ tồn đọng trước **15/7/2026**.
10. Chuỗi thay thế hay trích nhầm: TT 46/2018 → TT 13/2025; TT 52/2017 + 27/2021 (+18/2018, 04/2022) → TT 26/2025; TT 53/2017 → TT 33/2025; NĐ 146/2018 → NĐ 188/2025; NĐ 13/2023 → NĐ 356/2025; Luật ATTTM 2015 + Luật ANM 2018 → Luật ANM 2025; NĐ 85/2016 → NĐ 331/2026; Luật PCBTN 2007 → Luật Phòng bệnh 2025.

---

## 1. DÒNG THỜI GIAN (2025 → các mốc xa nhất tìm được)

### 1A. Mốc ĐÃ QUA (2025 – 05/10/2026) — phần mềm phải đáp ứng rồi

| Ngày | Sự kiện / nghĩa vụ | Văn bản – điều khoản | Đối tượng | Hệ quả phần mềm | Mức XM |
|---|---|---|---|---|---|
| 01/01/2025 | Phiếu hẹn khám lại / phiếu chuyển cơ sở KCB BHYT bản giấy **hoặc điện tử** (ký số bác sĩ); bãi bỏ TT 40/2015 | TT 01/2025/TT-BYT, Điều 15 | Cơ sở KCB BHYT | HIS sinh phiếu hẹn/chuyển điện tử có ký số | Gốc |
| 01/01/2025 | Phần chuyển tuyến/cấp CMKT/thủ tục KCB BHYT của luật BHYT sửa đổi có hiệu lực sớm | Luật 51/2024/QH15, Điều 3 khoản 2 | Cơ sở KCB BHYT | Logic xác định quyền lợi theo cấp CMKT | Gốc |
| 10/04/2025 | NĐ 23/2025/NĐ-CP chữ ký điện tử & dịch vụ tin cậy hiệu lực | NĐ 23/2025 | Mọi bên ký số | Phần mềm ký/kiểm tra phải kết nối cổng kiểm tra chữ ký số công cộng | Thứ cấp |
| 01/06/2025 | Thẻ BHYT giấy chỉ cấp cho 3 trường hợp (không cài được VssID/VNeID, không có CCCD gắn chip) | CV 168/BHXH-QLT (theo BHXH VN) | Tiếp đón | Tiếp đón bằng CCCD/VNeID/VssID, tra cứu cổng BHXH | Thứ cấp |
| 01/06/2025 | Quy định hóa đơn KCB: lập HĐ cho BHXH khi được thanh/quyết toán; được tổng hợp lập HĐ cuối ngày từ phần mềm KCB | NĐ 70/2025/NĐ-CP | Cơ sở KCB | Module hóa đơn điện tử | Thứ cấp |
| 01/07/2025 | Luật BHYT sửa đổi có hiệu lực chung; thẻ BHYT bản điện tử = bản giấy | Luật 51/2024/QH15 Điều 3 khoản 1; Điều 1 khoản 14 (Đ16 sửa) | Toàn hệ thống BHYT | — | Gốc |
| 01/07/2025 | NĐ 102/2025 quản lý dữ liệu y tế: mã định danh y tế = số định danh cá nhân; cơ sở y tế phải kết nối CSDL quốc gia về y tế + Sổ SKĐT trên VNeID | NĐ 102/2025/NĐ-CP Điều 6, 23, 25 | Mọi cơ sở y tế | Dùng số ĐDCN làm khóa bệnh nhân; API liên thông | Gốc |
| 01/07/2025 | Luật Dữ liệu + NĐ 165/2025 hướng dẫn | NĐ 165/2025/NĐ-CP (ban hành 30/6/2025) | Mọi tổ chức | Quản trị dữ liệu, dữ liệu quan trọng/cốt lõi | Thứ cấp (metadata vanban) |
| 01/07/2025 | TT 26/2025 đơn thuốc ngoại trú; TT 52/2017, 18/2018, 04/2022, 27/2021 hết hiệu lực | TT 26/2025/TT-BYT Điều 13 | Cơ sở KCB, nhà thuốc | Mẫu đơn mới, mã đơn `xxxxxyyyyyyy-z`, gửi Hệ thống đơn thuốc quốc gia | Gốc |
| 01/07/2025 | TT 33/2025 thời hạn lưu trữ hồ sơ ngành y tế (áp dụng cả tài liệu điện tử); TT 53/2017 hết hiệu lực | TT 33/2025/TT-BYT Điều 1, 2 | Mọi cơ sở y tế | Chính sách retention | Gốc |
| 01/07/2025 | NĐ 163/2025 hướng dẫn Luật Dược (thay NĐ 54/2017) | NĐ 163/2025/NĐ-CP | Dược | — | Thứ cấp (metadata congbao gốc) |
| 01/07/2025 & 15/08/2025 | NĐ 188/2025 hướng dẫn Luật BHYT: thẻ BHYT điện tử mặc định, giấy khi có đề nghị; cơ sở KCB phải nâng cấp HIS theo chuẩn dữ liệu đầu vào/đầu ra; NĐ 146/2018, 75/2023, 02/2025 bị bãi bỏ (một phần từ 01/7, toàn bộ từ 15/8/2025) | NĐ 188/2025 Điều 70 | Cơ sở KCB BHYT | — | Gốc |
| 21/07/2025 | TT 13/2025 HSBA điện tử hiệu lực; TT 46/2018 + Mục VIII TT 54/2017 hết hiệu lực | TT 13/2025/TT-BYT | Cơ sở KCB | — | Gốc-CSDL |
| 15/08/2025 | Quy trình thủ tục KCB BHYT mới (xuất trình VNeID mức 2/VssID/CCCD) | QĐ 2555/QĐ-BYT (12/8/2025) | Tiếp đón | — | Thứ cấp |
| 30/09/2025 | **Bệnh viện** phải triển khai HSBA điện tử | TT 13/2025 (điều lộ trình) | Cơ sở có GPHĐ hình thức bệnh viện | — | Gốc-CSDL |
| trước 01/10/2025 | **Bệnh viện** kê đơn điện tử | TT 26/2025 Điều 13 khoản 3a | Bệnh viện | — | Gốc |
| 31/12/2025 | Hết dùng mẫu giấy hẹn/chuyển tuyến theo NĐ 146/2018 | TT 01/2025 Điều 15 khoản 5 điểm đ | Cơ sở KCB BHYT | — | Gốc |
| trước 01/01/2026 | **Cơ sở KCB khác** (phòng khám…) kê đơn điện tử | TT 26/2025 Điều 13 khoản 3b | Phòng khám, cơ sở KCB không phải BV | — | Gốc |
| 01/01/2026 | Luật BVDLCN 91/2025 + NĐ 356/2025 hiệu lực; NĐ 13/2023 hết hiệu lực | Luật 91/2025 Điều 38; NĐ 356/2025 Điều 42 | Mọi bên xử lý DLCN | Đồng ý, DPIA, dịch vụ xử lý DLCN | Gốc |
| 01/01/2026 | NQ 261/2025/QH15 (cơ chế đột phá sức khỏe nhân dân) hiệu lực; miễn viện phí cơ bản từ 2030 | NQ 261/2025/QH15 | — | — | Thứ cấp |
| 01/01/2026 (QĐ ký 06/01/2026) | Dữ liệu Sổ SKĐT trên VNeID thay sổ giấy trong TTHC; cơ sở KCB liên thông dữ liệu Sổ SKĐT | QĐ 31/QĐ-BYT (số hiệu theo search; bài Tuổi Trẻ không nêu số) | Cơ sở KCB | — | Thứ cấp / số hiệu chưa xác minh |
| 10/02/2026 | Giám định BHYT do Bộ Tài chính quy định: gửi qua `gdbhyt.baohiemxahoi.gov.vn`, ký số, mẫu 01/BH–03/BH | TT 12/2026/TT-BTC | Cơ sở KCB BHYT | — | Thứ cấp (PDF gốc là bản scan) |
| 01/03/2026 | Luật Trí tuệ nhân tạo 134/2025/QH15 hiệu lực | Luật 134/2025 Điều 34 | Nhà cung cấp/triển khai AI | — | Gốc |
| 01/03/2026 | TT 55/2025 kê đơn thuốc cổ truyền hiệu lực; TT 44/2018 hết hiệu lực; e-Rx theo lộ trình CP/BYT | TT 55/2025 Điều 12 | YHCT | Đơn điện tử lưu CSDL, liên thông CSDL quốc gia & Sổ SKĐT (Điều 10) | Gốc |
| 09/03/2026 | QĐ 586/QĐ-BYT: KH triển khai HSBA điện tử toàn quốc 2026 | QĐ 586/QĐ-BYT | — | — | Thứ cấp |
| 07/04/2026 | Chỉ thị 04/CT-BYT đẩy mạnh HSBA điện tử | CT 04/CT-BYT | — | — | Thứ cấp |
| 10/04/2026 | QĐ 965/QĐ-BYT: KH HSBA điện tử 2026–2030 (đến 2030: 100% cơ sở KCB dùng HSBA không giấy) | QĐ 965/QĐ-BYT | — | — | Thứ cấp |
| 31/05/2026 | QĐ 1551/QĐ-BYT: liên thông dữ liệu khám sức khỏe ↔ Sổ SKĐT VNeID; **24 giờ** sau đợt khám; ký số; REST API | QĐ 1551/QĐ-BYT | Cơ sở KCB làm khám SK định kỳ/sàng lọc | Tích hợp API CSDL sức khỏe toàn dân | Gốc |
| 15/07/2026 | Hạn đồng bộ dữ liệu khám SK đã thực hiện trước ngày ban hành HD | QĐ 1551/QĐ-BYT, HD mục 3d | như trên | — | Gốc |
| 01/07/2026 | Luật An ninh mạng 116/2025 hiệu lực; Luật ATTTM 2015 + Luật ANM 2018 hết hiệu lực | Luật 116/2025 Điều 44 | Chủ quản HTTT | — | Gốc |
| 01/07/2026 | Luật Phòng bệnh 114/2025 hiệu lực (thay Luật PCBTN 2007); HTTT phòng bệnh kết nối CSDL y tế | Luật 114/2025 Điều 12, 38, 45 | YTDP, cơ sở KCB | Báo cáo bệnh truyền nhiễm/tiêm chủng | Gốc |
| 01/07/2026 | Luật Chuyển đổi số (148/2025/QH15) hiệu lực | — | — | Nguyên tắc kết nối, chia sẻ dữ liệu | Thứ cấp (số hiệu theo search) |
| 01/07/2026 | Luật Dân số 113/2025 hiệu lực (sửa Luật KCB — VBHN 26/VBHN-VPQH) | — | — | — | Thứ cấp |
| 01/07/2026 | QĐ 1931/QĐ-BYT (29/6/2026) sửa chuẩn dữ liệu đầu ra: `MUC_HUONG` tối đa 4 ký tự; quy tắc mã `SO_DANG_KY` thuốc hiếm UBND tỉnh cấp phép NK | QĐ 1931/QĐ-BYT (2026) — lưu ý trùng số với QĐ 1931/QĐ-BYT năm 2016 (khác nội dung) | HIS gửi XML BHYT | Sửa schema XML | Thứ cấp |
| 08/07–15/10/2026 | Chiến dịch 100 ngày lập/cập nhật Sổ SKĐT trên VNeID; chiến dịch 90 ngày làm sạch 12 CSDL | (theo VietnamPlus) | — | — | Thứ cấp |
| 01/08/2026 | QĐ 1804/QĐ-BYT (19/6/2026): 16 mã loại hình KCB (có 12 tại nhà, 14 từ xa…) + 60 mã khoa K01–K60; thay QĐ 824/QĐ-BYT (2/2023) và QĐ 2010/QĐ-BYT (6/2025) | QĐ 1804/QĐ-BYT | Cơ sở KCB, BHXH | Cập nhật danh mục mã | Thứ cấp |
| 15/08/2026 | QĐ 33/2026/QĐ-TTg danh mục 46 hệ thống AI rủi ro cao (y tế: robot/hệ thống AI hỗ trợ/điều khiển phẫu thuật…) | QĐ 33/2026/QĐ-TTg (ký 30/6/2026) | Nhà cung cấp AI | — | Thứ cấp |
| 19/08/2026 | NĐ 330/2026 xử phạt VPHC an ninh mạng & BVDLCN (đến 3 tỷ đồng; thời hiệu 1 năm) | NĐ 330/2026/NĐ-CP | Mọi bên | — | Thứ cấp (ngày ban hành báo đưa không thống nhất 19/8 vs 26/8) |
| 19/08/2026 | NĐ 331/2026 bảo vệ ANM đối với HTTT theo 5 cấp độ (thay NĐ 85/2016) | NĐ 331/2026/NĐ-CP | Chủ quản HTTT | Hồ sơ đề xuất cấp độ | Thứ cấp (PDF gốc là bản scan) |

### 1B. Mốc SẮP TỚI (sau 05/10/2026)

| Ngày | Nghĩa vụ / sự kiện | Văn bản – điều khoản | Đối tượng | Hệ quả phần mềm | Mức XM |
|---|---|---|---|---|---|
| **07/10/2026** | Hết hạn góp ý **dự thảo TT** về ứng dụng CNTT, CĐS, chia sẻ dữ liệu trong BHYT (thay TT 48/2017) | Dự thảo BYT | HIS vendor, cơ sở KCB | Xem mục 3 | Thứ cấp |
| tháng 10/2026 | BYT phải hoàn thiện Sổ SKĐT trên VNeID, kết nối dữ liệu y tế xã → tỉnh | NQ 221/NQ-CP (thực hiện KL 76-KL/TW) | BYT, địa phương | Kết nối kho dữ liệu y tế địa phương | Thứ cấp |
| 15/10/2026 | Kết thúc chiến dịch 100 ngày Sổ SKĐT | — | — | — | Thứ cấp |
| 10/2026 (Kỳ họp thứ 2 của Quốc hội — theo báo) | Trình **Luật sửa 6 luật y tế** (KCB, Dược, BHYT, Trẻ em, NKT, NCT) | Dự án luật | — | Xem mục 3 | Thứ cấp |
| **31/12/2026** | **Hạn chót HSBA điện tử** cho các cơ sở KCB khác có điều trị nội trú/ban ngày/ngoại trú; mục tiêu 100% cơ sở KCB | TT 13/2025/TT-BYT (lộ trình); QĐ 586/QĐ-BYT; CT 04/CT-BYT | Phòng khám, TTYT, cơ sở tư nhân… | EMR đầy đủ, ký số, lưu trữ, sao lưu, ATTT | Gốc-CSDL |
| **01/01/2027** | **Bệnh viện công + tư không sử dụng hồ sơ bệnh án giấy** | QĐ 586/QĐ-BYT; CT 04/CT-BYT | Bệnh viện | Paperless hoàn toàn | Thứ cấp |
| **01/01/2027** | **Chậm nhất**: thực hiện liên thông, sử dụng kết quả cận lâm sàng liên thông giữa các cơ sở KCB BHYT | **Luật 51/2024/QH15 Điều 3 khoản 4** | Cơ sở KCB BHYT | LIS/RIS-PACS phải chia sẻ kết quả, có định danh, thời điểm, người thực hiện | **Gốc** |
| 01/01/2027 (dự kiến) | TT mới thay TT 48/2017 (gửi dữ liệu trong 03 giờ…) | Dự thảo | HIS | — | Thứ cấp |
| 01/01/2027 (dự kiến) | TT thanh toán BHYT KCB y học gia đình, tại nhà, từ xa | Dự thảo (CV 7411/SYT-NV Đồng Nai 03/10/2026 xin ý kiến) | Cơ sở KCB | Module telemedicine, gói YHGĐ | Thứ cấp |
| 01/01/2027 | Điều kiện hạ tầng CNTT (điểm d khoản 2 Điều 52 Luật KCB) áp dụng cho hồ sơ xin GPHĐ nộp từ 01/01/2027 | Luật 15/2023/QH15, Điều 120 | Cơ sở KCB mới | Kết nối Hệ thống thông tin quản lý hoạt động KCB | Thứ cấp (chưa đọc được bản gốc — PDF scan) |
| ~01/01/2027 | NĐ 331/2026: HTTT xây dựng trước 01/7/2026 phải hoàn thành phê duyệt cấp độ trong 6 tháng (cách tính mốc chưa rõ) | NĐ 331/2026 chuyển tiếp | Chủ quản HTTT | Hồ sơ cấp độ | Chưa xác minh (thứ cấp, diễn giải) |
| 01/03/2027 | Hạn tuân thủ hệ thống AI rủi ro cao **ngoài** y tế/giáo dục/tài chính | Luật 134/2025 Điều 35 khoản 1b; QĐ 33/2026/QĐ-TTg | — | — | Gốc (luật) |
| **01/07/2027** | Hết 12 tháng: HTTT đã xác định cấp độ theo Luật ATTTM phải đáp ứng điều kiện, tiêu chuẩn, biện pháp bảo vệ ANM tương ứng theo luật mới; sản phẩm/giải pháp ATTT đang dùng phải đáp ứng điều kiện ANM | **Luật 116/2025/QH15 Điều 45 khoản 1, 3** | Chủ quản HTTT (BV, SaaS y tế…) | Giám sát ANM, phòng chống mã độc tập trung (Điều 40), báo cáo sự cố | **Gốc** |
| **01/09/2027** | Hệ thống AI **trong lĩnh vực y tế** đã đưa vào hoạt động trước 01/3/2026 phải tuân thủ Luật AI | **Luật 134/2025/QH15 Điều 35 khoản 1a** (18 tháng); QĐ 33/2026/QĐ-TTg | Nhà cung cấp & bên triển khai AI y tế | Phân loại rủi ro, minh bạch, đánh giá | **Gốc** |
| 01/01/2029 | Chậm nhất: cơ sở KCB đã có GPHĐ trước 01/01/2027 phải đáp ứng điều kiện hạ tầng CNTT | Luật 15/2023/QH15 Điều 120 | Cơ sở KCB hiện hữu | — | Thứ cấp |
| 2030 | 100% HSBA không giấy ở mọi cơ sở KCB (QĐ 965); 100% người dân có Sổ SKĐT, 100% trạm y tế xã dùng nền tảng số (CTMTQG – QĐ 1709/QĐ-BYT); miễn viện phí mức cơ bản trong phạm vi BHYT theo lộ trình (NQ 261/2025 – từ 01/01/2030) | — | — | — | Thứ cấp |
| 01/01/2031 | Hết 05 năm DN nhỏ/khởi nghiệp được chọn không thực hiện Điều 21, 22, khoản 2 Điều 33 Luật BVDLCN — **trừ** DN xử lý DLCN nhạy cảm/dịch vụ xử lý DLCN/quy mô lớn (NĐ 356: ≥100.000 chủ thể tích lũy) | Luật 91/2025 Điều 38 khoản 2–3; NĐ 356/2025 Điều 41 | DN nhỏ | Vendor y tế xử lý dữ liệu sức khỏe: **không hưởng miễn trừ** | Gốc |

---

## 2. BẢNG VĂN BẢN CHƯA HIỆU LỰC / HIỆU LỰC TỪNG PHẦN / CÓ LỘ TRÌNH SAU 05/10/2026

| # | Số hiệu – tên | Ngày BH | Hiệu lực | Mốc hạn chót sau 05/10/2026 (điều khoản) | Hệ quả phần mềm | URL nguồn | Link OK | Mức XM |
|---|---|---|---|---|---|---|---|---|
| 1 | TT 13/2025/TT-BYT hướng dẫn triển khai HSBA điện tử | 06/06/2025 | 21/07/2025 | 31/12/2026 – cơ sở KCB khác hoàn thành HSBA ĐT (điều lộ trình; bệnh viện 30/9/2025). Chuyển tiếp: người bệnh vào trước 21/7/2025 ra viện sau đó được tiếp tục dùng bệnh án giấy đã lập | EMR: hạ tầng (máy trạm, mạng, máy chủ, lưu trữ dự phòng), phục hồi dữ liệu, ATTT; ký/xác nhận điện tử của NVYT/người bệnh (chữ ký số, sinh trắc học, hình thức khác theo Luật GDĐT) | https://caselaw.vn/van-ban-phap-luat/587211-thong-tu-so-13-2025-tt-byt-ngay-06-06-2025-cua-bo-truong-bo-y-te-huong-dan-trien-khai-ho-so-benh-an-dien-tu ; tóm tắt: https://xaydungchinhsach.chinhphu.vn/lo-trinh-trien-khai-ho-so-benh-an-dien-tu-tai-cac-benh-vien-119250610163849953.htm ; vbpl (chưa kiểm tra được): https://vbpl.vn/TW/Pages/vbpq-van-ban-goc.aspx?ItemID=178219 | Y / Y / N | Gốc-CSDL (số điều cụ thể của khoản lộ trình chưa ghi nhận) |
| 2 | Luật 51/2024/QH15 sửa đổi Luật BHYT | 27/11/2024 | 01/07/2025 (một số khoản 01/01/2025) | **01/01/2027** liên thông, sử dụng kết quả CLS giữa cơ sở KCB BHYT (Điều 3 khoản 4) | LIS/PACS/HIS chia sẻ kết quả CLS, tra cứu kết quả cơ sở khác | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat51.pdf | Y | Gốc |
| 3 | QĐ 586/QĐ-BYT KH triển khai HSBA ĐT toàn quốc | 09/03/2026 | ký | 31/12/2026: 100% cơ sở KCB; 01/01/2027: 100% bệnh viện không dùng bệnh án giấy | — | https://luatvietnam.vn/y-te/quyet-dinh-586-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-427964-d1.html ; https://luatvietnam.vn/tin-van-ban-moi/tu-01-01-2027-100-benh-vien-khong-su-dung-benh-an-giay-186-107560-article.html | Y / Y | Thứ cấp |
| 4 | Chỉ thị 04/CT-BYT đẩy mạnh HSBA ĐT | 07/04/2026 | ký | như trên | — | https://luatvietnam.vn/y-te/chi-thi-04-ct-byt-2026-day-manh-trien-khai-ho-so-benh-an-dien-tu-tai-co-so-kham-chua-benh-431124-d1.html | Y | Thứ cấp |
| 5 | QĐ 965/QĐ-BYT KH HSBA ĐT 2026–2030 | 10/04/2026 | ký | 2030: 100% HSBA không giấy; liên thông Sổ SKĐT VNeID, liên thông khi chuyển viện; danh mục thuật ngữ lâm sàng/chỉ số XN chuẩn; tiêu chuẩn bệnh viện thông minh | Chuẩn thuật ngữ, interop | https://luatvietnam.vn/y-te/quyet-dinh-965-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-431556-d1.html | Y | Thứ cấp (quan hệ 586 ↔ 965 chưa rõ: không thấy ghi thay thế) |
| 6 | Luật 116/2025/QH15 An ninh mạng | 10/12/2025 | 01/07/2026 | **01/07/2027** (Điều 45 khoản 1 & 3) | Đáp ứng biện pháp ANM theo cấp độ; kết nối giám sát ANM & phòng chống mã độc tập trung về TT ANM quốc gia/tỉnh (Điều 40 k1b); HT dùng NSNN phải có phương án ANM được thẩm định (Điều 40 k2) | https://congbao.chinhphu.vn/van-ban/luat-so-116-2025-qh15-468678.htm (kèm DOCX/PDF) | Y | Gốc |
| 7 | NĐ 331/2026/NĐ-CP bảo vệ ANM đối với HTTT | 19/08/2026 | 19/08/2026 | Chuyển tiếp: 6 tháng hoàn thành phê duyệt cấp độ, 12 tháng đáp ứng tiêu chuẩn (mốc tính chưa rõ) | Cấp độ 2: DV trực tuyến < 100.000 chủ thể DL cơ bản hoặc < 10.000 chủ thể DL nhạy cảm; ≥ ngưỡng → cấp 3+; khi số người dùng vượt ngưỡng phải đánh giá lại & đề xuất cấp cao hơn; cấm chia nhỏ hệ thống để hạ cấp | https://vanban.chinhphu.vn/?docid=219243&pageid=27160 (PDF scan) ; https://bocongan.gov.vn/chinh-sach-phap-luat/bai-viet/quy-dinh-moi-ve-bao-ve-an-ninh-mang-doi-voi-he-thong-thong-tin-1788941596 ; https://luatvietnam.vn/an-ninh-quoc-gia/nghi-dinh-331-2026-nd-cp-bao-ve-an-ninh-mang-cho-he-thong-thong-tin-hieu-qua-445072-d1.html | Y(metadata) / Y / Y | Thứ cấp |
| 8 | Luật 134/2025/QH15 Trí tuệ nhân tạo | 10/12/2025 | 01/03/2026 trừ Điều 35 | **01/09/2027** AI y tế (Điều 35 k1a); 01/03/2027 AI khác (k1b); trong thời hạn được tiếp tục hoạt động trừ khi bị yêu cầu dừng (k2) | CDSS, đọc ảnh AI, chatbot y tế… | https://congbao.chinhphu.vn/van-ban/luat-so-134-2025-qh15-468694.htm | Y | Gốc |
| 9 | QĐ 33/2026/QĐ-TTg Danh mục hệ thống AI rủi ro cao | 30/06/2026 | 15/08/2026 | 01/09/2027 (y tế, GD, TC); 01/03/2027 (còn lại) | Kiểm tra sản phẩm có thuộc danh mục | https://mst.gov.vn/46-he-thong-ai-duoc-xep-vao-nhom-rui-ro-cao-phai-quan-ly-nghiem-ngat-197260703152945179.htm | Y | Thứ cấp (NĐ 142/2026/NĐ-CP hướng dẫn Luật AI: chưa xác minh) |
| 10 | Luật 91/2025/QH15 BVDLCN | 26/06/2025 | 01/01/2026 | 01/01/2031 hết miễn trừ DN nhỏ (không áp dụng cho DN xử lý DL nhạy cảm) – Điều 38 | Điều 26: DL sức khỏe phải có đồng ý; cấm cung cấp cho bên thứ ba là tổ chức dịch vụ CSSK/bảo hiểm sức khỏe, nhân thọ trừ yêu cầu bằng văn bản của chủ thể; nhà phát triển ứng dụng y tế phải tuân thủ đầy đủ | https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf | Y | Gốc |
| 11 | NĐ 356/2025/NĐ-CP hướng dẫn Luật BVDLCN | 31/12/2025 | 01/01/2026 | Không có chuyển tiếp riêng cho dịch vụ xử lý DLCN | Điều 21 k4: dịch vụ thu thập/xử lý DLCN qua web/app/phần mềm chăm sóc, theo dõi sức khỏe, dịch vụ y tế = dịch vụ xử lý DLCN → điều kiện (Điều 22), giấy chứng nhận (Điều 24–26); DPIA cập nhật định kỳ 06 tháng, thay đổi lớn cập nhật trong 10 ngày (Điều 20) | https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm | Y | Gốc |
| 12 | Luật 15/2023/QH15 KCB (đã sửa bởi Luật 112/2025, 113/2025 – VBHN 26/VBHN-VPQH) | 09/01/2023 | 01/01/2024 | 01/01/2027 (hồ sơ GPHĐ mới) và chậm nhất 01/01/2029 (cơ sở hiện hữu) phải đáp ứng điều kiện hạ tầng CNTT (Đ52 k2 điểm d), theo Điều 120 | Kết nối Hệ thống thông tin quản lý hoạt động KCB | Bản gốc (PDF scan, không đọc được chữ): https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/02/15luat.signed.pdf ; tóm tắt: https://vi.lawlinkvn.com/post/diem-moi-luat-kham-benh-chua-benh-2023-phan-1 ; VBHN: https://luatvietnam.vn/y-te/van-ban-hop-nhat-26-vbhn-vpqh-2026-hop-nhat-luat-kham-benh-chua-benh-427352-d5.html | N(scan) / Y / Y | Thứ cấp — **cần đối chiếu bản gốc Điều 120** |
| 13 | NQ 261/2025/QH15 cơ chế đặc biệt bảo vệ, CSSK nhân dân | 11/12/2025 | 01/01/2026; miễn viện phí cơ bản từ 01/01/2030 | 2030 | Logic mức hưởng 100% cho một số nhóm; đầu tư CSDL y tế quốc gia | https://luatvietnam.vn/y-te/nghi-quyet-261-2025-qh15-co-che-dot-pha-bao-ve-va-nang-cao-suc-khoe-nhan-dan-422070-d1.html | Y | Thứ cấp |
| 14 | QĐ 1551/QĐ-BYT HD liên thông dữ liệu khám SK & Sổ SKĐT VNeID | 31/05/2026 | ký | Liên tục: 24 giờ sau mỗi đợt khám định kỳ/sàng lọc (HD mục 4a) | REST API (`api.emrhub.vn`, sandbox `api-sandbox.emrhub.vn`), `POST /api/auth/login`, `POST /api/platform/data-sync/push`; ký số trước khi đồng bộ; cơ sở chưa có phần mềm dùng `csdlksk.vn` | https://syt.quangngai.gov.vn/upload/2006968/20260716/2026_05_31_QD_ban_hanh_HD_ket_noi_lien_thong_du_lieu_KSK_Final.signed.pdf | Y | Gốc |

---

## 3. BẢNG DỰ THẢO / DỰ ÁN ĐANG LẤY Ý KIẾN – ĐANG TRÌNH (ảnh hưởng 12 tháng tới)

| # | Dự thảo | Cơ quan | Trạng thái / hạn | Dự kiến hiệu lực | Nội dung ảnh hưởng phần mềm | URL | Link OK | Mức XM |
|---|---|---|---|---|---|---|---|---|
| D1 | **TT quy định ứng dụng CNTT, chuyển đổi số và chia sẻ dữ liệu trong lĩnh vực BHYT** (thay **TT 48/2017/TT-BYT**) | Bộ Y tế | Lấy ý kiến đến **07/10/2026** | **01/01/2027** | Bộ mã dùng chung, chuẩn & định dạng dữ liệu, ký số, giao dịch điện tử; gửi dữ liệu chi phí KCB BHYT lên cổng giám định **≤ 03 giờ** sau khi kết thúc lượt khám; 15 ngày rà soát/đề nghị thanh toán; cổng giám định trả kết quả chi tiết trong 15 ngày; nhắc nhở → cảnh báo → văn bản BHXH → **xử phạt VPHC** khi chậm lặp lại | https://vtv.vn/de-xuat-co-so-y-te-phai-gui-du-lieu-bhyt-trong-vong-3-gio-sau-kham-cham-nhieu-lan-co-the-bi-xu-phat-100261001082022915.htm ; https://www.vietnamplus.vn/co-so-kham-chua-benh-gui-du-lieu-dien-tu-cham-co-the-bi-xu-phat-hanh-chinh-post1139262.vnp | Y / Y | Thứ cấp (chưa thấy toàn văn dự thảo) |
| D2 | **TT thanh toán BHYT đối với KCB y học gia đình, tại nhà, từ xa** | Bộ Y tế | Đang xin ý kiến (Sở YT Đồng Nai CV 7411/SYT-NV ngày 03/10/2026) | 01/01/2027 (theo báo) | Thanh toán theo gói (lập/cập nhật hồ sơ, quản lý sức khỏe YHGĐ); 7 nhóm đối tượng KCB tại nhà; ~50 bệnh/tình trạng (mã ICD-10) KCB từ xa được BHYT chi trả; yêu cầu video, HSBA ĐT, ký số, định danh | https://syt.dongnai.gov.vn/vi/news/thong-bao/xin-y-kien-gop-y-du-thao-thong-tu-quy-dinh-thanh-toan-bao-hiem-y-te-doi-voi-kham-benh-chua-benh-y-hoc-gia-dinh-tai-nha-tu-xa-44038.html ; https://baolamdong.vn/de-xuat-danh-muc-benh-tinh-trang-benh-duoc-kham-chua-benh-tu-xa-thuoc-pham-vi-thanh-toan-cua-quy-bao-hiem-y-te-457620.html | Y / Y | Thứ cấp |
| D3 | **TT danh mục xét nghiệm, dịch vụ CLS và điều kiện sử dụng kết quả khi liên thông** giữa cơ sở KCB BHYT (~441 dịch vụ: 21 hóa sinh, 27 huyết học, 26 vi sinh, 367 điện quang) | Bộ Y tế | Lấy ý kiến (báo 24/08/2026) | Gắn với mốc luật 01/01/2027 (suy luận) | Kết quả phải có định danh người bệnh, thời điểm lấy mẫu, người thực hiện; thời hạn giá trị 24h → 60 ngày tùy dịch vụ → LIS/PACS phải lưu & phát metadata này | https://tuoitre.vn/de-xuat-nhieu-xet-nghiem-chup-chieu-khong-phai-thuc-hien-lai-khi-chuyen-vien-10026082416552496.htm | Y | Thứ cấp |
| D4 | **Luật sửa đổi, bổ sung một số điều của 6 luật y tế** (KCB, Dược, BHYT, Trẻ em, Người khuyết tật, Người cao tuổi) | Bộ Y tế → QH | Trình Kỳ họp thứ 2 (10/2026) | Chưa rõ | KCB: sắp xếp lại hình thức tổ chức KCB, phân cấp cấp phép kỹ thuật, giá dịch vụ chung theo cấp CMKT, bổ sung quản lý TBYT; Dược: giá thuốc. Cần theo dõi có đụng Điều 120 (mốc CNTT 2027/2029) hay HSBA ĐT không | https://baochinhphu.vn/bo-y-te-chuan-bi-trinh-quoc-hoi-4-du-an-luat-trong-do-co-1-luat-sua-nhieu-luat-102261001180003719.htm | Y | Thứ cấp |
| D5 | **TT thay TT 54/2017/TT-BYT** (bộ tiêu chí ứng dụng CNTT tại cơ sở KCB) + Bộ tiêu chuẩn chất lượng bệnh viện nâng cao (8 chương, 113 tiêu chuẩn) | Bộ Y tế (Cục KHCN&ĐT) | Kế hoạch hoàn thành Quý II/2026 — **chưa thấy ban hành** tính đến 05/10/2026 | Chưa rõ | Tiêu chí bệnh viện thông minh, thay mức 6 TT 54 | (search: vnpt.vn, suckhoedoisong) — chưa mở bài gốc | N | Chưa xác minh |
| D6 | Danh mục dữ liệu chủ, dữ liệu tham chiếu, từ điển dữ liệu dùng chung ngành y tế (13 CSDL) | Bộ Y tế | Hạn nội bộ tháng 8/2026 theo CT 07/CT-BYT; tháng 10/2026 vẫn "chưa hoàn thiện" | — | Mã danh mục dùng chung cho HIS | https://www.vietnamplus.vn/bo-y-te-yeu-cau-day-manh-xu-ly-dut-diem-cac-diem-nghen-chuyen-doi-so-y-te-post1136364.vnp ; https://suckhoedoisong.vn/bo-y-te-day-nhanh-tien-do-cac-nhiem-vu-chuyen-doi-so-thao-go-diem-nghen-du-lieu-va-dich-vu-so-169261003100416305.htm | Y / Y | Thứ cấp |
| D7 | TT hướng dẫn CTMTQG CSSK, dân số & phát triển 2026–2035 (bác sĩ gia đình gắn HSSK ĐT, nền tảng tư vấn từ xa) | Bộ Y tế | Lấy ý kiến (2026) | Chưa rõ | Mô hình "mỗi người dân một bác sĩ", HSSK ĐT liên tục | (search: dantri 18/07/2026) — chưa mở | N | Chưa xác minh |

---

## 4. CHUỖI THAY THẾ 2024–2026 (tránh trích văn bản cũ)

| Văn bản CŨ (không trích nữa) | → | Văn bản MỚI | Ngày cũ hết hiệu lực | Ghi chú | URL đã mở | Link OK | Mức XM |
|---|---|---|---|---|---|---|---|
| TT 46/2018/TT-BYT (HSBA điện tử) + **Mục VIII** TT 54/2017/TT-BYT | → | **TT 13/2025/TT-BYT** | 21/07/2025 | TT 54/2017 phần còn lại vẫn hiệu lực (đang soạn thay) | caselaw.vn (mục 2 #1) | Y | Gốc-CSDL |
| TT 52/2017/TT-BYT; TT 18/2018/TT-BYT; TT 04/2022/TT-BYT; **TT 27/2021/TT-BYT** (kê đơn điện tử) | → | **TT 26/2025/TT-BYT** | 01/07/2025 | E-Rx lộ trình nằm ở Điều 13 k3 TT 26 | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf | Y | Gốc |
| TT 44/2018/TT-BYT (kê đơn thuốc cổ truyền) | → | **TT 55/2025/TT-BYT** (BH 31/12/2025) | 01/03/2026 | — | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/55-byt.pdf | Y | Gốc |
| TT 53/2017/TT-BYT (thời hạn bảo quản hồ sơ) | → | **TT 33/2025/TT-BYT** (BH 01/07/2025) | 01/07/2025 | **Bẫy**: TT 26/2025 Điều 11 vẫn dẫn chiếu TT 53/2017 → áp dụng TT 33/2025 theo điều khoản tham chiếu (Điều 14 TT 26). PDF datafiles chỉ có 2 trang thân, không kèm Phụ lục thời hạn | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf | Y | Gốc |
| TT 40/2015/TT-BYT (đăng ký KCB ban đầu, chuyển tuyến); Điều 6 TT 30/2020/TT-BYT; Điều 3, 4, k2 Điều 5 TT 36/2021/TT-BYT | → | **TT 01/2025/TT-BYT** | 01/01/2025 | "Chuyển tuyến" → "chuyển cơ sở KCB"; phiếu hẹn/chuyển điện tử | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/01-byt.pdf | Y | Gốc |
| NĐ 146/2018/NĐ-CP; NĐ 75/2023/NĐ-CP; NĐ 02/2025/NĐ-CP (BHYT) | → | **NĐ 188/2025/NĐ-CP** (BH 01/07/2025) | Một phần 01/07/2025; toàn bộ 15/08/2025 | — | https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-188-2025-nd-cp-45593.htm | Y | Gốc |
| Luật BHYT 25/2008 (các điều bị sửa) | → | Luật 51/2024/QH15 (sửa đổi) | 01/07/2025 | Không thay toàn bộ, là luật sửa | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat51.pdf | Y | Gốc |
| **NĐ 13/2023/NĐ-CP** (BVDLCN) | → | **Luật 91/2025/QH15 + NĐ 356/2025/NĐ-CP** | 01/01/2026 | Chuyển tiếp: đồng ý đã thu theo NĐ 13 vẫn có giá trị; hồ sơ DPIA đã nộp tiếp tục dùng (Luật 91 Điều 39) | congbaocdn (Luật 91); congbao (NĐ 356) | Y / Y | Gốc |
| Luật ATTTM 86/2015/QH13 (sửa 2018) + **Luật ANM 24/2018/QH14** | → | **Luật ANM 116/2025/QH15** | 01/07/2026 | Cấp độ đã phê duyệt giữ nguyên, 12 tháng nâng chuẩn | congbao (Luật 116) | Y | Gốc |
| **NĐ 85/2016/NĐ-CP** (bảo đảm an toàn HTTT theo cấp độ) | → | **NĐ 331/2026/NĐ-CP** | 19/08/2026 | TT 12/2022/TT-BTTTT hướng dẫn NĐ 85: tình trạng **chưa xác minh** | bocongan.gov.vn; luatvietnam | Y / Y | Thứ cấp |
| NĐ 130/2018/NĐ-CP (chữ ký số & dịch vụ chứng thực) và văn bản sửa đổi | → | **NĐ 23/2025/NĐ-CP** | 10/04/2025 | Danh sách văn bản bị thay thế đầy đủ: chưa đọc bản gốc | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-23-2025-nd-cp-quy-dinh-ve-chu-ky-dien-tu-va-dich-vu-tin-cay-119250225073330307.htm | Y | Thứ cấp |
| NĐ 54/2017/NĐ-CP (hướng dẫn Luật Dược) | → | **NĐ 163/2025/NĐ-CP** (BH 29/06/2025) | 01/07/2025 | DOCX congbao bị cắt, chưa đọc được điều hiệu lực | https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-163-2025-nd-cp-45343.htm | Y (metadata) | Thứ cấp |
| Luật Phòng, chống bệnh truyền nhiễm 03/2007/QH12 | → | **Luật Phòng bệnh 114/2025/QH15** | 01/07/2026 | — | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat114-2025.pdf | Y | Gốc |
| QĐ 824/QĐ-BYT (02/2023) + QĐ 2010/QĐ-BYT (06/2025) — mã loại hình KCB, mã khoa | → | **QĐ 1804/QĐ-BYT** (19/06/2026) | áp dụng chậm nhất 01/08/2026 | — | https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=26715&CateID=169 ; https://suckhoedoisong.vn/bo-y-te-quy-dinh-moi-nhat-danh-muc-ma-kham-chua-benh-ma-khoa-cho-kham-bhyt-169260628130847556.htm | Y / Y | Thứ cấp |
| QĐ 4210/QĐ-BYT (2017) chuẩn dữ liệu đầu ra BHYT | → | QĐ 130/QĐ-BYT (18/01/2023) **sửa bởi** 4750/QĐ-BYT (29/12/2023), 3176/QĐ-BYT (29/10/2024, áp dụng thống nhất từ 01/01/2025), 1931/QĐ-BYT (29/06/2026, từ 01/07/2026) | (cũ) | **Bẫy**: đừng trích "QĐ 130" như bản nguyên gốc — phải dùng bản đã sửa 4750 + 3176 + 1931 | https://caselaw.vn/van-ban-phap-luat/508520-quyet-dinh-so-3176-qd-byt-ngay-29-10-2024-cua-bo-truong-bo-y-te-sua-doi-quyet-dinh-4750-qd-byt-sua-doi-quyet-dinh-130-qd-byt-quy-dinh-chuan-va-dinh-dang-du-lieu-dau-ra-phuc-vu-viec-quan-ly-giam-dinh-thanh-toan-chi-phi-kham-benh-chua-benh-va-giai-quyet-cac-che-do-lien-quan ; https://suckhoetreem.vn/cuoc-song-so/cap-nhat-chuan-du-lieu-phuc-vu-giam-dinh-kham-chua-benh-va-thanh-toan-bhyt-tu-01-7-2026-131048.html | Y / Y | Gốc-CSDL (3176) / Thứ cấp (1931) |
| TT 48/2017/TT-BYT (trích chuyển dữ liệu BHYT) | → (dự thảo) | TT mới về CNTT, CĐS, chia sẻ dữ liệu BHYT | **Chưa** — TT 48 vẫn hiệu lực đến khi TT mới có hiệu lực (dự kiến 01/01/2027) | — | vtv.vn | Y | Thứ cấp |
| NĐ 98/2021/NĐ-CP (TBYT) | — | **Không bị thay**; sửa bởi NĐ 07/2023, NĐ 04/2025; VBHN 08/VBHN-BYT 2026 | — | Phần mềm là TBYT (SaMD) vẫn theo NĐ 98 hợp nhất | (search) | N | Chưa xác minh |
| Giám định BHYT (trước do BHXH VN ban hành quy trình) | → | **TT 12/2026/TT-BTC** (BTC quản lý BHXH) | 10/02/2026 | Văn bản bị thay/bãi bỏ: **chưa xác minh** (PDF gốc scan) | https://luatvietnam.vn/y-te/thong-tu-12-2026-tt-btc-quy-dinh-giam-dinh-chi-phi-kham-chua-benh-bao-hiem-y-te-426504-d1.html | Y | Thứ cấp |

---

## 5. KẾ HOẠCH / CHƯƠNG TRÌNH QUỐC GIA CÓ CHỈ TIÊU CNTT Y TẾ

| Văn bản | Ngày | Chỉ tiêu / mốc liên quan CNTT | Nguồn | Link OK | Mức XM |
|---|---|---|---|---|---|
| NQ 72-NQ/TW (Bộ Chính trị) — giải pháp đột phá CSSK nhân dân | 09/09/2025 | Từ 2026: khám SK định kỳ/sàng lọc miễn phí ≥ 1 lần/năm, **lập Sổ SKĐT** quản lý theo vòng đời; "vận hành hiệu quả sổ SKĐT, bệnh án điện tử, đơn thuốc điện tử"; "khẩn trương xây dựng CSDL quốc gia về y tế, hệ thống kết nối liên thông dữ liệu y tế, BHYT"; AI, blockchain, dữ liệu lớn. (Câu "Trong năm 2026 hoàn thành xây dựng các CSDL y tế…" — mốc năm **chưa xác minh** nguyên văn) | https://xaydungchinhsach.chinhphu.vn/nghi-quyet-72-nq-tw-cua-bo-chinh-tri-ve-mot-so-giai-phap-dot-pha-tang-cuong-bao-ve-cham-soc-va-nang-cao-suc-khoe-nhan-dan-119250912060746502.htm | Y | Thứ cấp (trích qua tóm tắt tự động) |
| NQ 282/NQ-CP — Chương trình hành động của CP thực hiện NQ 72 | 15/09/2025 | Hoàn thành Sổ SKĐT cho toàn dân; HSBA ĐT là nhiệm vụ cốt lõi | Ngày/số xác nhận qua căn cứ trong QĐ 1551/QĐ-BYT (gốc) | Y | Gốc (số, ngày) / Thứ cấp (nội dung) |
| NQ 261/2025/QH15 | 11/12/2025 | Đầu tư CSDL y tế quốc gia; miễn viện phí cơ bản từ 01/01/2030 | luatvietnam | Y | Thứ cấp |
| QĐ 586/QĐ-BYT | 09/03/2026 | 31/12/2026 100% cơ sở KCB xong HSBA ĐT; 01/01/2027 bệnh viện bỏ bệnh án giấy | luatvietnam | Y | Thứ cấp |
| QĐ 965/QĐ-BYT — KH HSBA ĐT 2026–2030 | 10/04/2026 | Đến 2030 100% cơ sở KCB dùng HSBA không giấy; liên thông dữ liệu lâm sàng/CLS; kết nối Sổ SKĐT VNeID; chuyển viện dùng dữ liệu HSBA | luatvietnam | Y | Thứ cấp |
| QĐ 826/QĐ-TTg — Đề án 06 giai đoạn 2026–2030 | 11/05/2026 | Tiếp nối Đề án 06 (QĐ 06/QĐ-TTg 2022); ứng dụng định danh, dữ liệu dân cư | chỉ có trong kết quả search | N | Chưa xác minh |
| QĐ 1709/QĐ-BYT — Chương trình MTQG CSSK, dân số & phát triển 2026–2035 (GĐ I 2026–2030) | 12/06/2026 | 2030: 100% người dân có Sổ SKĐT (gắn VNeID); 100% trạm y tế xã dùng nền tảng số quản lý; tư vấn KCB từ xa cho mọi người dân | https://ninhbinh.gov.vn/tin-trong-nuoc-quoc-te/phe-duyet-chuong-trinh-muc-tieu-quoc-gia-ve-cham-soc-suc-khoe-dan-so-va-phat-trien-giai-doan-202-382026 | Y | Thứ cấp (lạ: CTMTQG thường do TTg/QH phê duyệt — cần kiểm lại cấp ban hành) |
| NQ 221/NQ-CP (thực hiện KL 76-KL/TW ngày 28/07/2026) | 2026 | Tháng 10/2026: BYT hoàn thiện Sổ SKĐT trên VNeID, kết nối dữ liệu y tế xã → tỉnh | https://vietbao.vn/hoan-thien-ho-so-suc-khoe-dien-tu-tren-vneid-trong-thang-102026-602850.html | Y | Thứ cấp |
| Chỉ thị 07/CT-BYT (2026) — tháo gỡ điểm nghẽn CĐS | 2026 | Danh mục dữ liệu chủ/tham chiếu/từ điển dữ liệu: 08/2026; hoàn thiện cấu trúc CSDL quốc gia về y tế: 09/2026; chiến dịch 100 ngày Sổ SKĐT; di chuyển hệ thống về Trung tâm Dữ liệu quốc gia | https://www.vietnamplus.vn/bo-y-te-yeu-cau-day-manh-xu-ly-dut-diem-cac-diem-nghen-chuyen-doi-so-y-te-post1136364.vnp | Y | Thứ cấp |
| Tiến độ thực tế (để tham chiếu) | 09/2025 → 09/2026 | 09/2025: 881/1.645 BV (53,6%) có HSBA ĐT; ~mid-2026: 1.263 BV, >34 triệu Sổ SKĐT; 30/09/2026: 1.272 cơ sở y tế triển khai BAĐT | vietnamplus (tiến độ), thethaovanhoa 30/09/2026 | Y | Thứ cấp |

---

## 6. CHI TIẾT KỸ THUẬT ĐÁNG CHÚ Ý CHO NGƯỜI VIẾT PHẦN MỀM

- **Khóa định danh bệnh nhân**: số định danh cá nhân (CCCD) là mã định danh y tế (NĐ 102/2025 Điều 6 — gốc). Thẻ BHYT điện tử mặc định (NĐ 188/2025 Điều về cấp thẻ — gốc); tiếp đón tra cứu trên Cổng tiếp nhận dữ liệu BHXH; nếu cổng không tra được vẫn phải tiếp nhận, tra lại sau (NĐ 188 — gốc); mã thẻ tạm cấp tự động qua cổng cho trẻ chưa có thẻ.
- **Mã đơn thuốc điện tử**: định dạng `xxxxxyyyyyyy-z` (5 ký tự mã cơ sở KCB…) — phụ lục TT 26/2025 và TT 55/2025 (gốc). Phải gửi lên Hệ thống đơn thuốc quốc gia và gửi đơn/mã đơn cho người bệnh qua phương tiện điện tử.
- **NĐ 188/2025**: cơ sở KCB phải "thiết lập hạ tầng CNTT, nâng cấp, hoàn thiện phần mềm quản lý bệnh viện" theo chuẩn dữ liệu đầu vào/đầu ra, trích chuyển dữ liệu, giao dịch điện tử; gửi dữ liệu sau khi kết thúc lượt KCB, ký số bảng tổng hợp hằng tháng/quý; hồ sơ hợp đồng BHYT phải có **bảng kê thiết bị phần mềm, phần cứng bảo đảm kết nối liên thông** (Mẫu số 8) — gốc.
- **Luật ANM 2025 Điều 40**: chủ quản HTTT phải kết nối hệ thống giám sát ANM & phòng chống mã độc tập trung về TT ANM quốc gia (Bộ Công an) hoặc TT ANM tỉnh; báo cáo sự cố; HT dùng NSNN cần phương án ANM được thẩm định khi thiết lập/mở rộng/nâng cấp — gốc. Điều 41: doanh nghiệp cung cấp dịch vụ trên không gian mạng phải định danh địa chỉ IP người dùng dịch vụ internet (áp dụng cho DN viễn thông/Internet; phạm vi với SaaS chưa rõ).
- **QĐ 1551/QĐ-BYT**: dữ liệu phải "đúng, đủ, sạch, sống", ký số; BHXH chia sẻ dữ liệu khám bệnh thông thường cho CSDL sức khỏe cá nhân qua Nền tảng chia sẻ điều phối dữ liệu của Trung tâm Dữ liệu quốc gia (XML ký số) — gốc.

---

## 7. CHỖ CHƯA XÁC MINH / CẦN ĐỐI CHIẾU THÊM

1. **Luật KCB 15/2023 Điều 120 — mốc 01/01/2027 & 01/01/2029** về hạ tầng CNTT (điểm d khoản 2 Điều 52): mới thấy qua lawlinkvn + snippet search; PDF gốc trên datafiles là bản scan. Cần đối chiếu toàn văn (congbao docx hoặc VBHN 26/VBHN-VPQH).
2. **TT 13/2025/TT-BYT**: chưa xác định số Điều chứa lộ trình 30/9/2025 & 31/12/2026 (đọc qua caselaw tóm lược). vbpl.vn không fetch được; datafiles không tìm được URL.
3. **QĐ 1931/QĐ-BYT (2026)**: chỉ 1 nguồn báo (suckhoetreem); trùng số với QĐ 1931/QĐ-BYT năm 2016 (tẩy sán lá gan) → khi trích phải ghi "ngày 29/6/2026".
4. **QĐ 1804/QĐ-BYT**: số hiệu các QĐ bị thay (824/QĐ-BYT 2023, 2010/QĐ-BYT 2025) theo báo SKĐS; chưa đọc bản gốc.
5. **NĐ 331/2026/NĐ-CP**: cách tính mốc chuyển tiếp 6/12 tháng (từ 01/07/2026 hay từ ngày NĐ hiệu lực) chưa rõ; PDF gốc scan. Ngưỡng 100.000 / 10.000 chủ thể theo luatvietnam.
6. **NĐ 330/2026/NĐ-CP**: ngày ban hành báo đưa lệch (19/8 vs 26/8/2026); mức phạt tối đa 3 tỷ theo luatvietnam (tiêu đề), chưa đọc bản gốc.
7. **NĐ 142/2026/NĐ-CP** (hướng dẫn Luật AI) — chỉ thấy trong snippet search.
8. **QĐ 31/QĐ-BYT ngày 06/01/2026** (Sổ SKĐT thay sổ giấy) — số hiệu chỉ thấy trong snippet search.
9. **QĐ 826/QĐ-TTg ngày 11/05/2026** (Đề án 06 giai đoạn 2026–2030) — chỉ snippet.
10. **QĐ 1709/QĐ-BYT** phê duyệt CTMTQG — cấp ban hành bất thường, cần kiểm.
11. **NQ 72-NQ/TW**: mốc "trong năm 2026 hoàn thành các CSDL y tế…" chưa trích được nguyên văn có năm.
12. **Luật Chuyển đổi số 148/2025/QH15**: số hiệu theo luatvietnam (snippet); hiệu lực 01/07/2026 theo mst.gov.vn. Luật này có thay Luật CNTT 2006 hay không: chưa xác minh.
13. **TT 49/2017/TT-BYT** (hoạt động y tế từ xa) — còn hiệu lực hay đã bị thay: **chưa xác minh**; không tìm thấy TT mới thay thế.
14. **TT 12/2022/TT-BTTTT** (hướng dẫn NĐ 85/2016) — tình trạng sau NĐ 331/2026: chưa xác minh.
15. **TT 54/2017/TT-BYT** — dự thảo thay thế hạn Q2/2026 nhưng chưa thấy ban hành; phần còn lại vẫn hiệu lực (theo báo).
16. **NQ 221/NQ-CP** — số hiệu & năm theo vietbao, chưa đọc gốc.
17. Quan hệ **QĐ 586 ↔ QĐ 965** (cùng chủ đề HSBA ĐT 2026): không thấy ghi thay thế; coi như song song (586: năm 2026; 965: 2026–2030).
18. Hóa đơn: NĐ 70/2025 — dịch vụ y tế **không** thuộc nhóm bắt buộc HĐ từ máy tính tiền theo tóm tắt xaydungchinhsach; nhưng hộ kinh doanh doanh thu ≥ 1 tỷ thì có — áp cho phòng khám hộ kinh doanh: chưa xác minh.

---

## 8. NGUỒN (chỉ liệt kê link đã mở thành công & nội dung khớp)

### Bản gốc (datafiles / congbao / congbaocdn / file ký số cơ quan nhà nước)
- Luật 116/2025/QH15 An ninh mạng — https://congbao.chinhphu.vn/van-ban/luat-so-116-2025-qh15-468678.htm
- Luật 134/2025/QH15 Trí tuệ nhân tạo — https://congbao.chinhphu.vn/van-ban/luat-so-134-2025-qh15-468694.htm
- Luật 91/2025/QH15 BVDLCN — https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf
- Luật 51/2024/QH15 sửa Luật BHYT — https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat51.pdf
- Luật 114/2025/QH15 Phòng bệnh — https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat114-2025.pdf (metadata: https://vanban.chinhphu.vn/?pageid=27160&docid=216498&classid=1&orggroupid=1)
- NĐ 356/2025/NĐ-CP — https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm
- NĐ 188/2025/NĐ-CP — https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-188-2025-nd-cp-45593.htm
- NĐ 102/2025/NĐ-CP — https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-102-2025-nd-cp-44865.htm
- NĐ 163/2025/NĐ-CP (metadata) — https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-163-2025-nd-cp-45343.htm
- NĐ 165/2025/NĐ-CP (metadata) — https://vanban.chinhphu.vn/?docid=214331&pageid=27160
- NĐ 331/2026/NĐ-CP (metadata; PDF scan) — https://vanban.chinhphu.vn/?docid=219243&pageid=27160
- TT 26/2025/TT-BYT — https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf
- TT 55/2025/TT-BYT — https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/55-byt.pdf
- TT 33/2025/TT-BYT — https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf
- TT 01/2025/TT-BYT — https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/01-byt.pdf
- QĐ 1551/QĐ-BYT — https://syt.quangngai.gov.vn/upload/2006968/20260716/2026_05_31_QD_ban_hanh_HD_ket_noi_lien_thong_du_lieu_KSK_Final.signed.pdf

### Gốc qua CSDL bên thứ ba
- TT 13/2025/TT-BYT — https://caselaw.vn/van-ban-phap-luat/587211-thong-tu-so-13-2025-tt-byt-ngay-06-06-2025-cua-bo-truong-bo-y-te-huong-dan-trien-khai-ho-so-benh-an-dien-tu
- QĐ 3176/QĐ-BYT — https://caselaw.vn/van-ban-phap-luat/508520-quyet-dinh-so-3176-qd-byt-ngay-29-10-2024-cua-bo-truong-bo-y-te-sua-doi-quyet-dinh-4750-qd-byt-sua-doi-quyet-dinh-130-qd-byt-quy-dinh-chuan-va-dinh-dang-du-lieu-dau-ra-phuc-vu-viec-quan-ly-giam-dinh-thanh-toan-chi-phi-kham-benh-chua-benh-va-giai-quyet-cac-che-do-lien-quan

### Thứ cấp (cổng CP, BHXH, bộ ngành, báo, luatvietnam)
- https://xaydungchinhsach.chinhphu.vn/lo-trinh-trien-khai-ho-so-benh-an-dien-tu-tai-cac-benh-vien-119250610163849953.htm
- https://xaydungchinhsach.chinhphu.vn/nghi-quyet-72-nq-tw-cua-bo-chinh-tri-ve-mot-so-giai-phap-dot-pha-tang-cuong-bao-ve-cham-soc-va-nang-cao-suc-khoe-nhan-dan-119250912060746502.htm
- https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-23-2025-nd-cp-quy-dinh-ve-chu-ky-dien-tu-va-dich-vu-tin-cay-119250225073330307.htm
- https://xaydungchinhsach.chinhphu.vn/mot-so-noi-dung-moi-cua-nghi-dinh-so-70-2025-nd-cp-ve-hoa-don-chung-tu-119250403074719995.htm
- https://xaydungchinhsach.chinhphu.vn/nghi-dinh-330-2026-nd-cp-ve-xu-phat-vi-pham-hanh-chinh-trong-linh-vuc-an-ninh-mang-119260824172446407.htm
- https://baochinhphu.vn/muc-xu-phat-vi-pham-hanh-chinh-doi-voi-hanh-vi-vi-pham-ve-bao-ve-du-lieu-ca-nhan-102260822154959691.htm
- https://baochinhphu.vn/bo-y-te-chuan-bi-trinh-quoc-hoi-4-du-an-luat-trong-do-co-1-luat-sua-nhieu-luat-102261001180003719.htm
- https://bocongan.gov.vn/chinh-sach-phap-luat/bai-viet/quy-dinh-moi-ve-bao-ve-an-ninh-mang-doi-voi-he-thong-thong-tin-1788941596
- https://mst.gov.vn/46-he-thong-ai-duoc-xep-vao-nhom-rui-ro-cao-phai-quan-ly-nghiem-ngat-197260703152945179.htm
- https://mst.gov.vn/tu-01-7-2026-viet-nam-co-khung-phap-ly-moi-cho-chuyen-doi-so-va-cong-nghe-chien-luoc-197260630135640793.htm
- https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=26715&CateID=169 (QĐ 1804)
- https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=25292&CateID=169 (QĐ 2555)
- https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=24571&CateID=169 (thẻ BHYT giấy từ 1/6/2025)
- https://syt.dongnai.gov.vn/vi/news/thong-bao/xin-y-kien-gop-y-du-thao-thong-tu-quy-dinh-thanh-toan-bao-hiem-y-te-doi-voi-kham-benh-chua-benh-y-hoc-gia-dinh-tai-nha-tu-xa-44038.html
- https://ninhbinh.gov.vn/tin-trong-nuoc-quoc-te/phe-duyet-chuong-trinh-muc-tieu-quoc-gia-ve-cham-soc-suc-khoe-dan-so-va-phat-trien-giai-doan-202-382026
- https://luatvietnam.vn/y-te/chi-thi-04-ct-byt-2026-day-manh-trien-khai-ho-so-benh-an-dien-tu-tai-co-so-kham-chua-benh-431124-d1.html
- https://luatvietnam.vn/y-te/quyet-dinh-586-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-427964-d1.html
- https://luatvietnam.vn/tin-van-ban-moi/tu-01-01-2027-100-benh-vien-khong-su-dung-benh-an-giay-186-107560-article.html
- https://luatvietnam.vn/y-te/quyet-dinh-965-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-431556-d1.html
- https://luatvietnam.vn/y-te/thong-tu-12-2026-tt-btc-quy-dinh-giam-dinh-chi-phi-kham-chua-benh-bao-hiem-y-te-426504-d1.html
- https://luatvietnam.vn/an-ninh-quoc-gia/nghi-dinh-331-2026-nd-cp-bao-ve-an-ninh-mang-cho-he-thong-thong-tin-hieu-qua-445072-d1.html
- https://luatvietnam.vn/y-te/nghi-quyet-261-2025-qh15-co-che-dot-pha-bao-ve-va-nang-cao-suc-khoe-nhan-dan-422070-d1.html
- https://luatvietnam.vn/y-te/van-ban-hop-nhat-26-vbhn-vpqh-2026-hop-nhat-luat-kham-benh-chua-benh-427352-d5.html
- https://vi.lawlinkvn.com/post/diem-moi-luat-kham-benh-chua-benh-2023-phan-1
- https://vtv.vn/de-xuat-co-so-y-te-phai-gui-du-lieu-bhyt-trong-vong-3-gio-sau-kham-cham-nhieu-lan-co-the-bi-xu-phat-100261001082022915.htm
- https://www.vietnamplus.vn/co-so-kham-chua-benh-gui-du-lieu-dien-tu-cham-co-the-bi-xu-phat-hanh-chinh-post1139262.vnp
- https://www.vietnamplus.vn/tang-toc-trien-khai-benh-an-so-suc-khoe-dien-tu-trong-chuyen-doi-so-y-te-post1132296.vnp
- https://www.vietnamplus.vn/bo-y-te-yeu-cau-day-manh-xu-ly-dut-diem-cac-diem-nghen-chuyen-doi-so-y-te-post1136364.vnp
- https://suckhoedoisong.vn/bo-y-te-quy-dinh-moi-nhat-danh-muc-ma-kham-chua-benh-ma-khoa-cho-kham-bhyt-169260628130847556.htm
- https://suckhoedoisong.vn/bo-y-te-day-nhanh-tien-do-cac-nhiem-vu-chuyen-doi-so-thao-go-diem-nghen-du-lieu-va-dich-vu-so-169261003100416305.htm
- https://suckhoetreem.vn/cuoc-song-so/cap-nhat-chuan-du-lieu-phuc-vu-giam-dinh-kham-chua-benh-va-thanh-toan-bhyt-tu-01-7-2026-131048.html
- https://ngaymoionline.com.vn/chuan-hoa-ma-kham-chua-benh-bhyt-tu-thang-82026-65385.html
- https://tuoitre.vn/de-xuat-nhieu-xet-nghiem-chup-chieu-khong-phai-thuc-hien-lai-khi-chuyen-vien-10026082416552496.htm
- https://tuoitre.vn/so-suc-khoe-dien-tu-tren-vneid-chinh-thuc-thay-the-so-giay-trong-thu-tuc-hanh-chinh-20260106164303444.htm
- https://afamily.vn/kham-suc-khoe-xong-du-lieu-se-tu-dong-len-vneid-236260603133658231.chn
- https://vietbao.vn/hoan-thien-ho-so-suc-khoe-dien-tu-tren-vneid-trong-thang-102026-602850.html
- https://thethaovanhoa.vn/chuyen-doi-so-y-te-benh-an-dien-tu-ket-noi-du-lieu-nang-cao-hieu-qua-kham-chua-benh-20260930163218365.htm
- https://baolamdong.vn/de-xuat-danh-muc-benh-tinh-trang-benh-duoc-kham-chua-benh-tu-xa-thuoc-pham-vi-thanh-toan-cua-quy-bao-hiem-y-te-457620.html
- https://lsvn.vn/de-xuat-benh-vien-hang-i-co-them-02-nam-de-trien-khai-ho-so-benh-an-dien-tu-a150260.html (bối cảnh 11/2024: dự thảo cũ đặt mốc 2025/2028 — đã bị TT 13/2025 thay bằng 30/9/2025 & 31/12/2026)

### Link KHÔNG kiểm tra được (không dùng làm nguồn xác minh)
- thuvienphapluat.vn — HTTP 403 với bot (mọi trang).
- vbpl.vn — trang render JS, WebFetch trả về trang chủ trống (vd https://vbpl.vn/TW/Pages/vbpq-van-ban-goc.aspx?ItemID=178219).
- PDF bản scan, không trích được chữ: https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/02/15luat.signed.pdf (Luật KCB), https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat134.signed.pdf (Luật AI — đã dùng bản DOCX congbao thay thế), https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/8/331_2026_nd-cp_19082026-signed.signed.pdf (NĐ 331), https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-btc.pdf (TT 12/2026/TT-BTC).
