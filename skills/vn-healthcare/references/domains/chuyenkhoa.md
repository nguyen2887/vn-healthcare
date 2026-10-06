# CHUYENKHOA — Nghiệp vụ chuyên khoa và kênh tiếp cận người bệnh

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám chuyên khoa (YHCT, RHM, thẩm mỹ, mắt, PHCN, sản), cơ sở tiêm chủng, nhà thuốc có web/app, sàn đặt khám, vendor HIS/EMR/CMS · Research gốc: `research/deep/CHUYENKHOA.md`

Năm mảng: (A) y học cổ truyền; (B) hồ sơ phòng khám chuyên khoa; (C) tiêm chủng; (D) quảng cáo dịch vụ y tế, thuốc trên web/app/nền tảng; (E) ngôn ngữ, bộ mã, khả năng tiếp cận. Không lặp phần đã có ở domain khác: kê đơn YHCT (DUOC-R01, R17), lộ trình HSBA điện tử (EMR-R01, R02), nội dung mẫu HSBA chung (EMR-R03), viết tắt (EMR-R04), thời hạn lưu HSBA chung (EMR-R22), ICD-10 TT 06/2026 (MA-LT-R01–R04), danh mục kỹ thuật TT 23/2024 (MA-LT-R12–R15), bán thuốc TMĐT (DUOC-R29), tin nhắn tiếp thị (DLCN-R28), Sổ SKĐT (SKDT-R01, R12), báo cáo bệnh truyền nhiễm (HTTT-BC-R26–R31), bảo mật IVF/giới tính thai/ghép tạng (BAOMAT-CB-R12–R15).

## Tóm tắt nhanh

- **Bệnh án YHCT** phải theo mẫu 18, 19, 20/BV1 (TT 32/2023) với chẩn đoán kép YHHĐ (ICD-10) + YHCT (mã U của QĐ 7603 PL 07.1). Từ **01/07/2026** mã YHCT theo QĐ 1978/2026: 30 dòng sửa/bổ sung, 05 mã ngừng dùng; chuyển tiếp 60 ngày đã hết (khoảng cuối 08/2026).
- **Tiêm chủng** (Luật Phòng bệnh, TT 13/2026, từ 01/07/2026): cập nhật đối tượng "kịp thời, không trùng lặp" lên Hệ thống quốc gia; hệ thống riêng phải chia sẻ **thời gian thực**; tai biến nặng báo Sở Y tế và CDC trong **24 giờ**. Không có mốc "cập nhật trong 24 giờ" cho mũi tiêm thường.
- **Quảng cáo dịch vụ KCB** không còn thủ tục xác nhận nội dung từ 15/02/2026, nhưng phải có đủ tên, địa chỉ, số GPHĐ, giờ hoạt động, phạm vi chuyên môn (NĐ 342 Đ9). Thiếu: 15–20 triệu; vượt phạm vi chuyên môn: 40–60 triệu + tước GPHĐ/CCHN 03–06 tháng (NĐ 87/2026 Đ75; mức cá nhân, tổ chức ×2).
- **Quảng cáo trên mạng**: nhãn phân biệt, nút tắt một lần chạm, gỡ quảng cáo vi phạm **chậm nhất 24 giờ** khi có yêu cầu (phạt 50–60 triệu); người kinh doanh dịch vụ quảng cáo trên mạng lưu hồ sơ **03 năm**, báo cáo năm trước **25/11**.
- **Phạt quảng cáo y tế nằm ở NĐ 87/2026**, không ở NĐ 90/2026 (NĐ 90 chỉ phạt quảng cáo rượu bia, sữa).
- **Thẩm mỹ**: dịch vụ xâm lấn chỉ ở BV, PKĐK, PK chuyên khoa; HSBA phẫu thuật thẩm mỹ lưu **20 năm** kể cả ở phòng khám. IVF chỉ ở **bệnh viện có phạm vi chuyên khoa phụ sản** (NĐ 207/2025 Đ10, thay NĐ 10/2015).
- **Ngôn ngữ**: chỉ định điều trị và đơn thuốc ghi bằng tiếng Việt; người hành nghề nước ngoài phải có bản dịch tiếng Việt và chữ ký người phiên dịch trên đơn (NĐ 96 Đ35 k3; phạt NĐ 90 Đ38 k5 đ).
- **Hạn gần nhất**: 31/12/2026 hạn HSBA điện tử cho PK, cơ sở không phải BV (EMR-R01); 01/01/2028 kỹ thuật YHCT chỉ có ở PL 02 TT 23 mới được làm.

## Mục lục

**A. YHCT**: R01 bệnh án YHCT 18–20/BV1 · R02 mã bệnh YHCT QĐ 7603/1978 ↔ ICD-10 · R03 mã thuật ngữ YHCT QĐ 2552 · R04 kỹ thuật YHCT, mốc 01/01/2028 · R05 danh mục thuốc YHCT BHYT (TT 27/2025) · R06 dược liệu, thuốc thang, chế phẩm tự bào chế · R07 chỉ định thuốc YHCT đúng hướng dẫn · R08 kết hợp YHCT–YHHĐ
**B. PK chuyên khoa**: R09 chọn mẫu HSBA chuyên khoa · R10 hình vẽ tổn thương · R11 đồng ý phẫu thuật, thủ thuật · R12 phiếu mắt, sản · R13 thẩm mỹ: loại hình, lưu 20 năm · R14 ảnh trước/sau, đồng ý quảng cáo · R15 hỗ trợ sinh sản: chỉ bệnh viện, lưu vĩnh viễn
**C. Tiêm chủng**: R16 cập nhật Hệ thống quốc gia · R17 hệ thống riêng: thời gian thực · R18 bộ 44 trường QĐ 3891 · R19 sổ tiêm chủng · R20 sàng lọc, theo dõi 30 phút · R21 tai biến nặng 24 giờ · R22 báo cáo định kỳ · R23 danh mục vắc xin, TCMR · R24 điều kiện điểm tiêm, lưu hồ sơ · R25 tiêm chủng trên Sổ SKĐT
**D. Quảng cáo**: R26 nội dung bắt buộc QC dịch vụ KCB · R27 không vượt phạm vi chuyên môn · R28 nhãn quảng cáo, nút tắt · R29 gỡ trong 24 giờ, lưu 3 năm · R30 quảng cáo thuốc · R31 thông tin, bán thuốc trên app · R32 đánh giá, xếp hạng, KOL · R33 QC cấm (giới tính thai, tạng), livestream
**E. Ngôn ngữ, tiếp cận**: R34 tiếng Việt, đơn thuốc · R35 nhu cầu ngôn ngữ, phiên dịch · R36 ngôn ngữ đăng ký của người hành nghề nước ngoài · R37 UTF-8, TCVN 6909 · R38 WCAG · R39 ưu tiên khám

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 32/2023/TT-BYT | Chi tiết Luật KCB: Đ51–53, PL XXVIII (29 mẫu bệnh án), PL XXIX (53 mẫu giấy, phiếu) | 01/01/2024 | Còn HL; bãi bỏ QĐ 1941/2019, QĐ 3730/2021 | gốc (bản đăng lại của BV) | [Thân TT](https://bvbnd.vn/wp-content/uploads/2024/01/32-thongtuhuongdanluatkbcb31122023_91202410.pdf) · [PL XXVIII](https://benhvienbacha.vn/wp-content/uploads/2024/01/28.-Phu-luc-XVIII.-Mau-benh-an.pdf) · [PL XXIX](https://benhvienbacha.vn/wp-content/uploads/2024/01/29.-Phu-luc-XIX.-Mau-giay-phieu.pdf) |
| 7603/QĐ-BYT (2018) | Bộ mã DMDC v6; PL 07.1 mã bệnh YHCT | 15/01/2019 | Còn HL một phần; PL 07.1 sửa bởi QĐ 1978/2026 | gốc-meta (bản PL 07.1 gốc chưa đọc) | (xem BHYT-DATA) |
| 1978/QĐ-BYT (01/07/2026) | Sửa PL 07.1 QĐ 7603 theo TT 06/2026 | áp dụng 01/07/2026; chuyển tiếp 60 ngày | Còn HL | gốc | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20260807/792_Quyet-dinh-1978-QD-BYT_9535393f5e.pdf) |
| 2552/QĐ-BYT (12/08/2025) | Mã dùng chung thuật ngữ YHCT đợt 1 (4 PL) | ngày ký | Còn HL | gốc (trang tin Cục QL YDCT trả lỗi 500 ngày 06/10/2026; dùng PDF cùng máy chủ) | [Thân QĐ](https://ydct.moh.gov.vn/static/files/uploads/d2fd4d199903951ec329c789bd4fda58d894858f07f8e923471f76098fdacef1.pdf) · [PL I](https://ydct.moh.gov.vn/static/files/uploads/c42d09e85b7a5f10f40a340aef6661ef0a5a2cc2921172d9aae22c5521ce0a5f.pdf) · [PL II](https://ydct.moh.gov.vn/static/files/uploads/182e474d0bc7080a26264bdc90f640b05a5361927c5d757d293a3f560ec17ae8.pdf) · [PL III](https://ydct.moh.gov.vn/static/files/uploads/a6a0649c8572ebf35c49b23216e6d9a58872832c978edc9601f3494d899bfd0b.pdf) · [PL IV](https://ydct.moh.gov.vn/static/files/uploads/a563f07a3319970d8d146a856cf40fbe063e4a7d211fde08a1765b06c43cd7c9.pdf) |
| 27/2025/TT-BYT | Nguyên tắc danh mục, thanh toán BHYT thuốc YHCT, dược liệu | 01/09/2025; Đ9–11 chờ TT danh mục mới | Còn HL; bãi bỏ Đ4–6 TT 05/2015, TT 27/2020 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/27-byt.pdf) · [VB 214388](https://vanban.chinhphu.vn/?pageid=27160&docid=214388) |
| 05/2015/TT-BYT (VBHN 13/VBHN-BYT) | Danh mục thuốc đông y, dược liệu BHYT | 2015 | Danh mục còn dùng tới TT danh mục mới (suy luận) | gốc-meta | [VB 179475](https://vanban.chinhphu.vn/?pageid=27160&docid=179475) |
| 2149/QĐ-BYT (15/07/2026) | Sửa Đ3 QĐ 486/QĐ-BYT về QTKT YHCT | ngày ký | Còn HL | gốc (QĐ 486 chưa đọc) | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20260807/805_Quyet-dinh-2149-QD-BYT_5b043ca1b0.pdf) |
| 06/2026/TT-BYT | ICD-10; Đ6 k1 áp mã TT này từ 01/07/2026 | 01/07/2026 | Còn HL | gốc | [PDF](http://bvdkbaclieu.gov.vn/upload/1000079/20260507/731_Thong-tu-06-2026-TT-BYT_029cf354fb.pdf) |
| 33/2025/TT-BYT | Thời hạn lưu trữ tài liệu ngành y tế | 01/07/2025 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [PL](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ3 k2, Đ7 k17/k20/k21, Đ8, Đ21, Đ37 k5, Đ65, Đ85, Đ87, Đ120 k4, Đ121 k4 | 01/01/2024 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 96/2023/NĐ-CP | Chi tiết Luật KCB: Đ35, Đ36 (ngôn ngữ), Đ40 k12 (thẩm mỹ) | 01/01/2024 | Còn HL; Đ40 k9 bị NĐ 207/2025 bãi bỏ | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/01/96-nd.signed.pdf) · [VB 209491](https://vanban.chinhphu.vn/?pageid=27160&docid=209491) |
| 207/2025/NĐ-CP | Hỗ trợ sinh sản, mang thai hộ: Đ3, Đ10, Đ12, Đ15–17 | 01/10/2025 | Còn HL; thay NĐ 10/2015, NĐ 98/2016 | gốc-OCR (đối chiếu lại Đ3, Đ10, Đ12, Đ15–16) | [VB 214619](https://vanban.chinhphu.vn/?pageid=27160&docid=214619) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/207-cp.signed.pdf) |
| 114/2025/QH15 | Luật Phòng bệnh: Đ8 k7, Đ12, Đ22, Đ23, Đ38 k1 | 01/07/2026 | Còn HL; Luật PCBTN 2007 hết HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat114-2025.pdf) |
| 165/2026/NĐ-CP | Chi tiết Luật Phòng bệnh: Đ2 k7, Đ26, Đ48–58, Đ49, Đ94 | 01/07/2026 (Đ49: 01/07/2027) | Còn HL; bãi bỏ NĐ 104/2016 (Đ9–11 giữ tới 30/06/2027), NĐ 13/2024 | gốc-OCR | [VB 218169](https://vanban.chinhphu.vn/?pageid=27160&docid=218169) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/165-ndcp.signed.pdf) |
| 13/2026/TT-BYT | Hoạt động tiêm chủng: Đ2, Đ3–4, Đ10, Đ12, Đ15, Đ25–27 | 01/07/2026 | Còn HL; thay TT 34/2018, 24/2018, 05/2020, 52/2025 | gốc (tr. 1–10) + gốc-OCR (tr. 11–19); bản đăng lại | [PDF](http://bvdkbaclieu.gov.vn/upload/1000079/20260613/760_Thong-tu-13-2026-TT-BYT_92335354fb.pdf) |
| 15/2026/TT-BYT | Giám sát bệnh truyền nhiễm; bãi bỏ TT 54/2015 | 01/07/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/15-byt.pdf) |
| 3891/QĐ-BYT (18/12/2025) | 44 trường thông tin tiêm chủng, 20 bắt buộc | ngày ký | HL sau 01/07/2026 chưa xác minh (căn cứ cũ) | gốc-meta qua CV 31/TTKSBT HCDC | [Trang HCDC](https://hcdc.vn/co-so-tiem-chung-can-luu-y-cap-nhat-danh-muc-thong-tin-tiem-chung-quoc-gia-qNSBUl.html) |
| 3421/QĐ-BYT (2017) | Quy chế Hệ thống quản lý thông tin tiêm chủng | ngày ký | Chưa thấy bãi bỏ; căn cứ đã hết HL → chưa xác minh | gốc-OCR | link chưa kiểm tra được (VNCDC lỗi chứng chỉ SSL) |
| 31/QĐ-BYT (06/01/2026) | Sổ SKĐT VNeID; tiền sử tiêm chủng | ngày ký | Còn HL | gốc | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20260305/691_Quyet-dinh-31-QD-BYT_704c0ca597.pdf) |
| 90/2026/NĐ-CP | Xử phạt VPHC y tế: Đ9 (tiêm chủng), Đ38, Đ40, Đ59, Đ67 | 15/05/2026 | Còn HL; thay NĐ 117/2020 | gốc-OCR (đối chiếu lại Đ4, Đ9, Đ38) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| 16/2012/QH13 (VBHN 88/VBHN-VPQH) | Luật Quảng cáo: Đ2 k8, Đ7 k5, Đ8 k8–11, Đ15a, Đ19, Đ20 k4, Đ23 | 01/01/2013 | Còn HL | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/8/88-vbhn-vpqh.pdf) |
| 75/2025/QH15 | Sửa Luật Quảng cáo: Đ15a (KOL), Đ19, Đ23 (trên mạng, gỡ 24 giờ) | 01/01/2026 | Còn HL | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45566/57708-1-2025967-96875-2025-qh15.pdf) |
| 342/2025/NĐ-CP | Chi tiết Luật Quảng cáo: Đ3, Đ5, Đ9, Đ17–19 | 15/02/2026 | Còn HL; thay NĐ 181/2013, NĐ 70/2021 (Đ32) | gốc-OCR (đối chiếu lại Đ5, Đ9, Đ17–19, Đ32) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/342-ndcp.signed.pdf) |
| 03/2026/TT-BYT | Bãi bỏ phần lớn TT 09/2015 (xác nhận nội dung QC) | 15/02/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/03-byt.pdf) · [VBHN 09/VBHN-BYT](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/09-vbhn-byt.pdf) |
| Luật Dược 105/2016 sửa bởi 44/2024 (VBHN 76) | Đ6 k10/k15/k17–19, Đ42 k4, Đ79 | Luật 44: 01/07/2025 | Còn HL | gốc | [PDF](https://congbaocdn.chinhphu.vn/180507251028987904/2026/4/10/469206-1775705438_v1_1775787513_signed.pdf) |
| 163/2025/NĐ-CP | Đ41–42 (TMĐT thuốc), Đ103–111 (QC thuốc) | 01/07/2025 | Còn HL | gốc-OCR | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-163-2025-nd-cp-45343.htm) |
| 31/2025/TT-BYT | Chi tiết Luật Dược; Đ19–20 thông tin thuốc | 01/07/2025 | Còn HL; thay TT 07/2018 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/31-byt.pdf) |
| 122/2025/QH15 | Luật TMĐT: Đ17, Đ22, Đ24–26, Đ41 | 01/07/2026 | Còn HL | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/27/122signed-17694826033991158478619.pdf) |
| 248/2026/NĐ-CP (30/06/2026) | Chi tiết Luật TMĐT: Đ11, Đ12, Đ52–53 | 01/07/2026 (xác thực người bán 01/01/2027) | Còn HL; bãi bỏ NĐ 52/2013, NĐ 85/2021 | gốc-OCR | [VB 218747](https://vanban.chinhphu.vn/?pageid=27160&docid=218747) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/248-ndcp.signed.pdf) |
| 19/2023/QH15 | Luật BVQLNTD: Đ10, Đ22 k3, Đ39 | 01/07/2024 | Còn HL | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2023/6/39843/45917-1-2023865-86619-2023-qh15.pdf) |
| 87/2026/NĐ-CP (27/03/2026) | Xử phạt VPHC văn hóa, quảng cáo: Đ6, Đ49–51, Đ56, Đ69, Đ71, Đ75 | 15/05/2026 | Còn HL; thay NĐ 38/2021, NĐ 128/2022 | gốc (đã đối chiếu mọi điều dẫn) | [PDF Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/4/23/469359-1776912733_v1_1776913093_signed.pdf) |
| 72/2002/QĐ-TTg | Dùng bộ mã TCVN 6909:2001 | 2002 | Chưa thấy bãi bỏ (chưa xác minh) | gốc | [VB 10713](https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=10713) |
| 39/2017/TT-BTTTT | Danh mục tiêu chuẩn CNTT trong CQNN: UTF-8, TCVN 6909 bắt buộc; WCAG 2.0 khuyến nghị | 01/07/2018 | Căn cứ Luật CNTT hết HL 01/07/2026 → chưa xác minh | gốc | [PDF](https://mic.mediacdn.vn/Upload/VanBan/tt39-2017.pdf) |
| 26/2020/TT-BTTTT | Tiếp cận cho người khuyết tật: WCAG 1.0 bắt buộc với CQNN, đơn vị sự nghiệp dùng NSNN | 01/01/2021 | Như trên, chưa xác minh sau 01/07/2026 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2020/10/26-btttt.signed.pdf) · [VB 201221](https://vanban.chinhphu.vn/?pageid=27160&docid=201221) |
| 51/2010/QH12 | Luật Người khuyết tật: Đ4 k1 d, Đ43 | 01/01/2011 | Còn HL; đang có dự án sửa (trình 10/2026) | gốc | [VB 96045](https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=96045) |

## 2. Yêu cầu

### A. Y học cổ truyền

### CHUYENKHOA-R01 — Bệnh án YHCT theo mẫu 18, 19, 20/BV1 với chẩn đoán kép
- **Căn cứ**: TT 32/2023 Đ51 k1 a, PL XXVIII: 18/BV1 (nội trú YHCT), 19/BV1 (ngoại trú YHCT), 20/BV1 (nội trú nhi YHCT). Mục "Chẩn đoán" có hai cột YHHĐ/mã và YHCT/mã ở các mốc nơi chuyển đến, khoa khám bệnh, ra viện; phần "B. Y học cổ truyền": tứ chẩn (mạch tay trái, tay phải), biện chứng luận trị, chẩn đoán (bệnh danh, bát cương, nguyên nhân, tạng phủ, kinh mạch, định vị bệnh), điều trị (pháp, phương dược, không dùng thuốc). Hướng dẫn ghi (PL XXIX mục 54, 55): YHHĐ ghi tên và mã ICD-10; YHCT ghi tên và mã bệnh YHCT theo quy định BYT; một mã bệnh chính, mã kèm theo cách nhau bằng ";". TT 32 Đ53 k2 h bãi bỏ QĐ 1941/2019.
- **Áp dụng**: BV YHCT, khoa YHCT của BV đa khoa (Luật KCB Đ85 k1), PK YHCT điều trị theo đợt · **Hiệu lực/hạn**: 01/01/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: có đủ ba form; hai danh sách chẩn đoán độc lập cho mỗi mốc; đúng một bệnh chính mỗi hệ; tứ chẩn có cấu trúc; phiếu điều trị dành cho bệnh án YHCT.
- **Bẫy**: còn dùng mẫu QĐ 1941/2019 là lỗi. 19/BV1 có "Số vào viện", "Tổng số ngày điều trị": gắn với đợt điều trị, khớp EMR-R02.

### CHUYENKHOA-R02 — Mã bệnh YHCT (QĐ 7603 PL 07.1 sửa bởi QĐ 1978/2026) ánh xạ ICD-10
- **Căn cứ**: QĐ 1978/QĐ-BYT Đ1: sửa PL 07.1 QĐ 7603 để chuẩn hóa theo TT 06/2026; PL 01 có 23 dòng đổi mã ICD-10 và 7 mã bổ sung (ví dụ `U50.351` Ôn bệnh đổi từ A90 sang A97; thêm `U50.351.0/.1/.2` ứng A97.0/.1/.2); PL 02: 05 mã YHCT không dùng (`U51.631.2`, `U56.141.7`, `U58.762.6`, `U58.762.7`, `U63.501.8`). Đ2: thực hiện từ 01/07/2026; trong 60 ngày, gửi thay thế, sửa dữ liệu để chuẩn hóa mã được coi là lý do khách quan. Tên trên bảng kê dạng `Tên YHCT [Tên YHHĐ]`. TT 06/2026 Đ6 k1. Bảng chỉ tiêu QĐ 130: `MA_BENH_YHCT` (XML1, XML3) gồm mã chính và mã kèm theo tương ứng ICD-10, cách nhau ";" (xem BHYT-DATA).
- **Áp dụng**: cơ sở KCB BHYT có YHCT; vendor HIS · **Hiệu lực/hạn**: 01/07/2026; hết chuyển tiếp khoảng cuối 08/2026 (suy luận cách đếm)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bảng mã YHCT có phiên bản (`source = QD7603-PL07.1`, `amended_by = QD1978`), mỗi mã có cặp ICD-10; nạp 30 thay đổi; 05 mã PL 02 `inactive_from = 2026-07-01`; kiểm tra cặp YHCT–ICD không lệch bảng; sinh `MA_BENH_YHCT` đúng thứ tự (chính trước) và khớp `MA_BENH_CHINH`/`MA_BENH_KT`; lượt khám bắc qua 01/07/2026 theo MA-LT-R04.
- **Bẫy**: QĐ 1978 không thay toàn bộ PL 07.1; phải có bản PL 07.1 gốc làm nền (chưa đọc). Mã YHCT dạng `Uxx.xxx(.x)` thuộc bản ICD Việt Nam, khác mã U00–U85 của WHO trong TT 06.

### CHUYENKHOA-R03 — Mã dùng chung thuật ngữ YHCT (QĐ 2552/2025)
- **Căn cứ**: QĐ 2552/QĐ-BYT Đ1: 4 phụ lục để chuẩn hóa thông tin trong bệnh án điện tử, liên thông KCB–BHYT và Sổ SKĐT; Đ2: áp dụng tại mọi cơ sở KCB công và tư; Đ4: HL từ ngày ký. PL I: thể lâm sàng theo bệnh danh (mã dùng chung 7 chữ số dải 65xxxxx, kèm ICD-10, mã U, ví dụ `U62.392.5.01`); PL II: bát cương `BC.xx`, nguyên nhân `NN.xx`, vệ khí dinh huyết `VK.xx`, tạng phủ `TP.xx`, kinh lạc; PL III: huyệt; PL IV: kỹ thuật YHCT (dải 381xxxx/382xxxx, ánh xạ STT TT 23/2024), kỹ thuật dấu * (3810426 → 3820489) chỉ làm khi BYT ban hành danh mục bằng VBQPPL.
- **Áp dụng**: cơ sở có YHCT; vendor EMR · **Hiệu lực/hạn**: 12/08/2025
- **Mức**: BẮT BUỘC? (không hạn chót, không trường XML, không chế tài riêng)
- **Phần mềm phải**: nạp 4 danh mục làm hệ mã có phiên bản; chẩn đoán YHCT dùng danh sách mã thay text tự do; phiếu châm cứu ghi huyệt theo mã PL III; kỹ thuật YHCT ánh xạ ba lớp mã nội bộ ↔ mã 2552 ↔ mã TT 23 (MA-LT-R15); chặn kỹ thuật dấu *.
- **Bẫy**: tiêu đề PL IV "thực hiện đến ngày 30/06/2026" theo mốc gốc TT 23 PL 01, đã bị TT 25/2026 lùi tới 31/12/2027 (MA-LT-R12); không tự vô hiệu PL IV (suy luận). Đây là "đợt 1": cần cơ chế nạp đợt sau.

### CHUYENKHOA-R04 — Kỹ thuật YHCT: mốc PL 01 → PL 02 TT 23
- **Căn cứ**: QĐ 2149/QĐ-BYT Đ1 sửa Đ3 QĐ 486/QĐ-BYT: kỹ thuật chỉ có ở PL 02 TT 23/2024 thực hiện từ 01/01/2028; kỹ thuật chỉ có ở PL 01 tiếp tục tới khi có QTKT YHCT thay thế hoặc bãi bỏ. TT 23/2024, TT 25/2026 (MA-LT-R12, R13).
- **Áp dụng**: cơ sở có YHCT · **Hiệu lực/hạn**: 15/07/2026; 01/01/2028
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục kỹ thuật YHCT có `valid_from` (01/01/2028 cho kỹ thuật chỉ ở PL 02) và cờ "chỉ ở PL 01" không tự hết hạn; chặn chỉ định trước ngày áp dụng; liên kết phạm vi chuyên môn được duyệt (MA-LT-R14).

### CHUYENKHOA-R05 — Danh mục thuốc YHCT BHYT theo TT 27/2025
- **Căn cứ**: TT 27/2025 Đ12 k1 (thuốc dược liệu, cổ truyền ghi tên dược liệu, vị thuốc theo giấy đăng ký; không ghi tên theo tác dụng dược lý, không ghi tên thương mại), k2 (dược liệu ghi theo TT 01/2018 Đ16 k3), k3 (đường uống; đường dùng ngoài); Đ9–11 (cấu trúc danh mục; chỉ áp khi có TT danh mục mới, Đ20 k2); Đ13 k3, Đ14 k4–5 (tỷ lệ, điều kiện thanh toán; không thanh toán lô đình chỉ, thu hồi, thuốc đã kết cấu vào giá dịch vụ); Đ22 k5 a, b (cơ sở xây dựng danh mục thuốc BHYT tại đơn vị, gửi BHXH); Đ20 k3.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/09/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: master thuốc YHCT tách loại (dược liệu, cổ truyền, kết hợp, dược liệu, vị thuốc, thuốc thang, chế phẩm tự bào chế); tên theo thành phần khác tên thương mại; đường dùng theo hai nhóm; điều kiện, tỷ lệ thanh toán có cấu trúc gắn văn bản và ngày hiệu lực; cờ đình chỉ, thu hồi theo lô có `effective_from`; xuất danh mục sử dụng tại đơn vị (BHYT-DATA-R19).
- **Bẫy**: TT 27 là thông tư nguyên tắc, chưa phải danh mục. Không gỡ danh mục TT 05/2015 khỏi hệ thống (suy luận từ Đ20 k2–k3).

### CHUYENKHOA-R06 — Dược liệu, vị thuốc, thuốc thang, chế phẩm tự bào chế
- **Căn cứ**: TT 27/2025 Đ15 k1–2 (cấu phần chi phí dược liệu; người đứng đầu phê duyệt quy trình sơ chế và chi phí, gửi BHXH), Đ16, Đ17 (thuốc thang = dược liệu/vị thuốc + giá dịch vụ sắc + bao bì), Đ18 k1–3 (thành phần ngoài danh mục không thanh toán), Đ18 k4 (chế phẩm tự bào chế chỉ dùng tại chính cơ sở đó). QĐ 130 XML2 `MA_PP_CHEBIEN` (mã phương pháp chế biến, nhiều mã cách ";").
- **Áp dụng**: BV, PK YHCT có sơ chế, sắc, bào chế · **Hiệu lực/hạn**: 01/09/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: công thức (BOM) với cờ "trong danh mục BHYT" từng thành phần; phiên bản quy trình, đơn giá được duyệt (số, ngày, ngày gửi BHXH); tách dòng sắc thuốc thành DVKT; tự trừ thành phần ngoài danh mục khỏi phần BHYT; chặn bán, chuyển chế phẩm tự bào chế ra ngoài cơ sở; ghi `MA_PP_CHEBIEN`.

### CHUYENKHOA-R07 — Chỉ định thuốc YHCT phù hợp tờ hướng dẫn hoặc hướng dẫn BYT
- **Căn cứ**: TT 27/2025 Đ14 k2 (quỹ BHYT trả khi chỉ định phù hợp tờ hướng dẫn sử dụng hoặc hướng dẫn chẩn đoán, điều trị YHCT/kết hợp của BYT), k3 (dùng chéo nhóm y lý vẫn được trả nếu đúng k2).
- **Áp dụng**: cơ sở KCB BHYT
- **Mức**: BẮT BUỘC (điều kiện thanh toán) / NÊN (kiểm tra tự động)
- **Phần mềm phải**: lưu chỉ định (ICD-10 và mã YHCT) của mỗi thuốc; cảnh báo khi kê cho chẩn đoán ngoài chỉ định và yêu cầu ghi căn cứ hướng dẫn BYT.

### CHUYENKHOA-R08 — Kết hợp YHCT với YHHĐ: chỉ người đủ điều kiện
- **Căn cứ**: Luật KCB Đ87 k1 a, b: kết hợp chỉ thực hiện tại cơ sở KCB; "Chỉ người hành nghề có đủ điều kiện mới được chỉ định phương pháp chữa bệnh, kê đơn thuốc kết hợp y học cổ truyền với y học hiện đại". Ma trận chức danh: xem DUOC-R01, DUOC-R17.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: như DUOC-R01; thêm phân quyền chỉ định **kỹ thuật** YHCT và YHHĐ theo phạm vi hành nghề.

### B. Phòng khám chuyên khoa

### CHUYENKHOA-R09 — Chọn đúng mẫu HSBA chuyên khoa
- **Căn cứ**: TT 32/2023 PL XXVIII: 04/BV1 phụ khoa, 05/BV1 sản, 06/BV1 sơ sinh, 08/BV1 da liễu, 13/BV1 RHM nội trú, 15/BV1 ngoại trú chung, 16/BV1 ngoại trú RHM, 21–26/BV1 mắt, 27/BV1 PHCN, 28/BV1 PHCN nhi, 29/BV1 ngoại trú PHCN. Đ52 k1 b: bệnh án điện tử đủ trường của HSBA. Không có mẫu riêng cho thẩm mỹ, nha khoa thẩm mỹ, hỗ trợ sinh sản; nội trú dùng mẫu chuyên khoa gần nhất (suy luận).
- **Áp dụng**: PK, BV chuyên khoa (khi nào phải lập HSBA: EMR-R02)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục loại bệnh án gắn mã mẫu; chỉ bật mẫu phù hợp phạm vi chuyên môn; trường riêng (sơ đồ răng, ảnh thẩm mỹ) đặt thêm, không thay trường bắt buộc (GIAYTO-R02).
- **Bẫy**: sơ đồ răng (odontogram) không phải trường pháp định. QĐ 3730/2021 (mẫu PHCN cũ) hết HL (TT 32 Đ53 k2 i).

### CHUYENKHOA-R10 — Hình vẽ mô tả tổn thương và hình ảnh trong HSBA chuyên khoa
- **Căn cứ**: TT 32 PL XXVIII: 13/BV1, 16/BV1 có "Hình vẽ mô tả tổn thương khi vào viện"; mẫu mắt có hình vẽ; bảng "Hồ sơ, phim, ảnh" khi giao nhận. Đ52 k1 b.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: thành phần vẽ hoặc chú thích trên ảnh nền, lưu ảnh có metadata (người vẽ, thời điểm), nằm trong gói tài liệu được ký (EMR-R06); bảng kê phim, ảnh tự sinh từ PACS.

### CHUYENKHOA-R11 — Đồng ý phẫu thuật, thủ thuật và giấy cam kết PL XXIX
- **Căn cứ**: Luật KCB Đ65 k1: phẫu thuật hoặc can thiệp xâm nhập cơ thể "chỉ được thực hiện sau khi có sự đồng ý của người bệnh hoặc người đại diện của người bệnh"; k2 (người chưa thành niên, mất năng lực, không có thân nhân: theo Đ15). TT 32 PL XXIX: 01/BV2 (cam kết phẫu thuật, thủ thuật, GMHS), 40/BV2, 41/BV2 (từ chối), 45/BV2, 46/BV2, 48/BV2, 49/BV2.
- **Áp dụng**: mọi cơ sở có phẫu thuật, thủ thuật, gồm PK thẩm mỹ, nha khoa xâm lấn
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chặn bắt đầu phiếu 06/BV2 khi chưa có 01/BV2 ký hợp lệ (trừ cấp cứu có lý do theo Đ15); lưu người ký là người bệnh hay đại diện, quan hệ, giấy tờ; checklist nội dung tư vấn theo ô của mẫu; ký điện tử theo EMR-R06.
- **Bẫy**: tiêm filler, botox, laser xâm lấn là can thiệp xâm nhập nên cũng cần đồng ý (suy luận từ NĐ 96 Đ40 k12 a).

### CHUYENKHOA-R12 — Phiếu chuyên khoa mắt, sản và phiếu phẫu thuật
- **Căn cứ**: TT 32 PL XXIX: 30–35/BV2 (phẫu thuật mắt), 51/BV2 (khám thai), 50/BV2 (sơ sinh sau sinh), 06/BV2, 05/BV2.
- **Mức**: BẮT BUỘC (khi cơ sở làm kỹ thuật đó)
- **Phần mềm phải**: có form tương ứng; phiếu khám thai liên kết các lượt theo thai kỳ.

### CHUYENKHOA-R13 — Thẩm mỹ: loại hình được phép; HSBA phẫu thuật thẩm mỹ lưu 20 năm cả ở PK
- **Căn cứ**: NĐ 96/2023 Đ40 k12 (gốc-OCR, diễn giải): cơ sở cung cấp dịch vụ thẩm mỹ dùng thuốc, chất, thiết bị can thiệp vào cơ thể (phẫu thuật, thủ thuật, tiêm, chiếu tia, đốt, xâm lấn khác) và xăm, phun, thêu có dùng thuốc tê dạng tiêm phải là bệnh viện, PKĐK hoặc PK chuyên khoa. TT 33/2025 PL mục 43: HSBA điều trị đợt ghép mô, tạng, phẫu thuật thẩm mỹ **20 năm**; mục 44: HSBA nội, ngoại trú 10 năm; Đ1 k2 a áp cả tài liệu điện tử; phụ lục không phân biệt BV hay PK. NĐ 90/2026 Đ40 k1 b (không lưu trữ hồ sơ, bệnh án theo quy định: 1–3 triệu).
- **Áp dụng**: BV, PKĐK, PK chuyên khoa thẩm mỹ, RHM, da liễu · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chặn kích hoạt dịch vụ thẩm mỹ xâm lấn khi loại hình cơ sở không thuộc BV/PKĐK/PK chuyên khoa; `retention_class = 'PTTM_20Y'` cho HSBA có phẫu thuật thẩm mỹ (cơ chế chung EMR-R22); thủ thuật thẩm mỹ không phẫu thuật (tiêm, laser) không có dòng riêng: tối thiểu 10 năm, thận trọng đặt 20 năm theo Đ1 k2 b (suy luận).
- **Bẫy**: "20 năm chỉ cho bệnh viện" là sai (TT 33 quy định theo loại hồ sơ). Hồ sơ **ghép** mô, tạng cùng dòng 43 nhưng Luật 75/2006 Đ38 k4 buộc **30 năm** → áp 30 năm (xem BAOMAT-CB-R15).

### CHUYENKHOA-R14 — Ảnh trước/sau: thuộc HSBA; dùng cho quảng cáo cần đồng ý riêng
- **Căn cứ**: không có quy định bắt buộc chụp ảnh trước/sau. Nếu chụp vì chuyên môn thì là tài liệu của HSBA (Luật KCB Đ69 k2, suy luận) và là dữ liệu sức khỏe nhạy cảm (DLCN-R01). Dùng hình ảnh cá nhân trong quảng cáo khi chưa được đồng ý bị cấm (Luật Quảng cáo Đ8 k8; NĐ 87/2026 Đ50 k3 a: 20–40 triệu). Dùng thư cảm ơn, danh nghĩa người bệnh để quảng cáo thuốc bị cấm (Luật Dược Đ6 k10; NĐ 87 Đ69 k4 b: 30–40 triệu). Quảng cáo thực phẩm trích ý kiến người bệnh về tác dụng điều trị: NĐ 87 Đ71 k4 (20–30 triệu).
- **Mức**: NÊN (chụp, lưu ảnh lâm sàng) / BẮT BUỘC (đồng ý riêng trước khi dùng cho quảng cáo, truyền thông)
- **Phần mềm phải**: kho ảnh lâm sàng gắn lượt điều trị, cùng thời hạn lưu với HSBA, xem theo vai trò; cờ `marketing_consent` riêng có bằng chứng, thu hồi được (DLCN-R03); CMS/fanpage chỉ lấy ảnh có cờ này; tự làm mờ mặt nếu không có đồng ý. Ảnh trẻ em: thêm đồng ý của trẻ từ đủ 7 tuổi (BAOMAT-CB-R19).

### CHUYENKHOA-R15 — Hỗ trợ sinh sản: chỉ bệnh viện chuyên khoa phụ sản; lưu vĩnh viễn
- **Căn cứ**: NĐ 207/2025 Đ10 k1 (diễn giải, gốc-OCR): cơ sở thực hiện IVF phải có giấy phép hoạt động theo hình thức **bệnh viện** có phạm vi chuyên khoa phụ sản, làm được xét nghiệm nội tiết sinh sản và cấp cứu sản khoa; Đ10 k2–4 (đơn nguyên riêng, thiết bị, nhân sự toàn thời gian); Đ12 (mang thai hộ: ≥02 năm kinh nghiệm IVF, ≥500 chu kỳ/năm trong 02 năm gần nhất; tư vấn y tế, tâm lý, pháp lý); Đ15 k2 (bãi bỏ NĐ 10/2015, NĐ 98/2016, NĐ 96/2023 Đ40 k9); Đ16 (cơ sở đã được công nhận tiếp tục hoạt động). TT 33/2025 mục 211 (hồ sơ sinh con bằng thụ tinh nhân tạo, IVF, mang thai hộ) và 214 (hồ sơ hiến, nhận tinh trùng, noãn, phôi): **vĩnh viễn**. Vô danh người hiến–người nhận, mã hóa, chia sẻ CSDL dùng chung: xem **BAOMAT-CB-R12**.
- **Áp dụng**: BV có trung tâm hỗ trợ sinh sản; vendor phần mềm labo IVF · **Hiệu lực/hạn**: 01/10/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: `retention_class = 'PERMANENT'` cho hồ sơ IVF, mang thai hộ, cho nhận giao tử, phôi; quản lý mẫu đông lạnh gắn hợp đồng, hạn đóng phí (NĐ 207 Đ8 k2: không đóng phí sau 06 tháng cơ sở được hủy); chặn bật module IVF cho cơ sở không phải BV có phạm vi phụ sản.
- **Bẫy**: phòng khám không được làm IVF; phần mềm PK sản dừng ở tư vấn, xét nghiệm, theo dõi. Tài liệu cũ dẫn NĐ 10/2015 (gồm yêu cầu "ghi rõ đặc điểm người cho, đặc biệt yếu tố chủng tộc" của Đ3 k4) là hết HL từ 01/10/2025; NĐ 207 Đ3 chỉ còn nguyên tắc vô danh.

### C. Tiêm chủng

### CHUYENKHOA-R16 — Cập nhật đối tượng và mũi tiêm lên Hệ thống quốc gia, không trùng lặp
- **Căn cứ**: TT 13/2026 Đ2 k1 (định nghĩa Hệ thống quản lý thông tin tiêm chủng quốc gia), Đ10 k2 a, b (với tiêm bắt buộc và tự nguyện: cấp và điền sổ theo dõi tiêm chủng cá nhân; thống kê đối tượng và cập nhật đầy đủ, chính xác, kịp thời lên Hệ thống, bảo đảm không trùng lặp đối tượng), Đ10 k1 (thông tin cha, mẹ, người giám hộ), Đ14 k2. Luật 114/2025 Đ12, Đ38 k1.
- **Áp dụng**: cơ sở tiêm chủng công, tư; cơ sở KCB có tiêm · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: đồng bộ mỗi mũi tiêm lên Hệ thống (trực tiếp hoặc qua phần mềm quốc gia); tra trùng theo số định danh cá nhân hoặc bộ (họ tên, ngày sinh, giới, mẹ) trước khi tạo đối tượng; lưu `national_subject_id`; không xóa đối tượng đã có lịch sử tiêm (QĐ 3421 Đ7 k4, hiệu lực chưa xác minh).
- **Bẫy**: không văn bản nào buộc cập nhật "trong 24 giờ"; văn bản dùng "kịp thời". QĐ 3421/2017 Đ7 k2 b từng yêu cầu nhập ngay trong buổi tiêm (vùng khó: 05 ngày làm việc), k6 nhập bù trong 03 ngày làm việc: chỉ là thực hành tốt.

### CHUYENKHOA-R17 — Hệ thống riêng: liên thông, chia sẻ thời gian thực
- **Căn cứ**: TT 13/2026 Đ25 k8 (diễn giải): cơ sở dùng hệ thống riêng phải kết nối liên thông, chia sẻ dữ liệu **thời gian thực** với Hệ thống quốc gia và bảo đảm an toàn thông tin, trừ dữ liệu đối tượng do BCA, BQP quản lý. Đ15 k7 (liên thông theo hướng dẫn Cục Phòng bệnh), k8–9.
- **Áp dụng**: chuỗi tiêm dịch vụ, BV dùng HIS/phần mềm tiêm riêng; vendor · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (nghĩa vụ); đặc tả API chưa có văn bản
- **Phần mềm phải**: đẩy sự kiện mũi tiêm ngay khi xác nhận (không gom cuối ngày); hàng đợi gửi lại có giám sát độ trễ; loại trừ hồ sơ BCA, BQP; log gửi, phản hồi để chứng minh thời gian thực.

### CHUYENKHOA-R18 — Bộ 44 trường, 20 trường bắt buộc (QĐ 3891/2025)
- **Căn cứ**: QĐ 3891/QĐ-BYT qua CV 31/TTKSBT-PCBTNCT (06/01/2026) của HCDC: 44 trường, 2 nhóm. Hành chính bắt buộc (15): mã định danh đối tượng (định danh cá nhân, CCCD hoặc hộ chiếu), họ tên, ngày sinh, giới, mã dân tộc, cặp xã–tỉnh cho 5 loại địa chỉ. Mũi tiêm bắt buộc (5): vắc xin, ngày tiêm, thứ tự mũi, cơ sở tiêm, kháng nguyên.
- **Mức**: BẮT BUỘC? (căn cứ NĐ 104/2016, TT 34/2018 đã hết HL; chưa thấy văn bản thay)
- **Phần mềm phải**: schema đủ 44 trường; validate 20 trường trước khi gửi; địa chỉ 2 cấp theo danh mục hành chính mới; kháng nguyên tách khỏi tên thương mại vắc xin.

### CHUYENKHOA-R19 — Sổ theo dõi tiêm chủng cá nhân hoặc sổ tiêm chủng điện tử
- **Căn cứ**: TT 13/2026 Đ10 k2. NĐ 90/2026 Đ9 k2 b (không cấp và ghi sổ theo dõi tiêm chủng cá nhân hoặc sổ tiêm chủng điện tử: 1–3 triệu), k2 c (không thống kê danh sách đối tượng đã tiêm: 1–3 triệu).
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: in hoặc xuất sổ, phiếu xác nhận mũi tiêm; lịch sử tiêm trên app người dùng; danh sách thống kê theo buổi.
- **Bẫy**: NĐ 165/2026 Đ26 chỉ có Giấy chứng nhận quốc tế về tiêm chủng. Chưa thấy văn bản về "giấy xác nhận tiêm chủng điện tử" trong nước hay mẫu sổ mới kèm TT 13.

### CHUYENKHOA-R20 — Khám sàng lọc, theo dõi 30 phút, hướng dẫn theo dõi 24 giờ
- **Căn cứ**: TT 13/2026 Đ12 k2 a, c. NĐ 90 Đ9 k1 b, c (cảnh cáo: không tư vấn; không hướng dẫn theo dõi, xử trí phản ứng), k2 d (không theo dõi ≥30 phút và hướng dẫn theo dõi ≥24 giờ: 1–3 triệu), k3 a (không khám sàng lọc hoặc không đầy đủ: 3–5 triệu).
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phiếu sàng lọc phải hoàn tất với kết luận "đủ điều kiện tiêm" trước khi xác nhận mũi; đồng hồ 30 phút, ghi giờ rời điểm tiêm; gửi hướng dẫn theo dõi 24 giờ; ghi phản ứng sau tiêm.

### CHUYENKHOA-R21 — Tai biến nặng: dừng buổi tiêm, khóa lô, báo cáo trong 24 giờ
- **Căn cứ**: NĐ 165/2026 Đ2 k7 (định nghĩa). TT 13/2026 Đ12 k3, k5 (dừng buổi, tạm dừng lô), Đ15 k5 a (trong 24 giờ báo Sở Y tế đồng thời CDC tỉnh). NĐ 90 Đ9 k3 d (không thống kê đủ và báo Sở Y tế trong 24 giờ: 3–5 triệu), k4 b (không dừng ngay buổi tiêm: 5–10 triệu), k5 c, d, đ (không xử trí, chuyển, cấp cứu và báo cáo: 10–20 triệu), k2 đ (không chuẩn bị hồ sơ cho Hội đồng tư vấn: 1–3 triệu).
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: nút ghi nhận tai biến nặng tạo sự kiện có dấu thời gian, đếm ngược 24 giờ, mẫu báo cáo gửi Sở Y tế và CDC; tự khóa buổi đang mở và chặn xuất lô liên quan ở mọi điểm tiêm; lưu hồ sơ cho Hội đồng tư vấn.

### CHUYENKHOA-R22 — Báo cáo tiêm chủng định kỳ và chiến dịch
- **Căn cứ**: TT 13/2026 Đ15 k1 (trên Hệ thống; văn bản khi khẩn cấp hoặc hệ thống lỗi), k2, k3 (biểu mẫu theo hướng dẫn Cục Phòng bệnh), k4 a (cơ sở tiêm báo Trạm Y tế xã: tháng trước ngày 03 tháng sau; năm trước 13/01), k6 a (chiến dịch: trước 17 giờ hằng ngày). Luật 114 Đ23 k2. NĐ 90 Đ9 k1 d (cảnh cáo).
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: báo cáo ngày, tháng, năm tự sinh từ dữ liệu mũi tiêm; lịch nhắc; xuất văn bản dự phòng khi hệ thống quốc gia lỗi (cùng mô hình HTTT-BC-R26).

### CHUYENKHOA-R23 — Danh mục bệnh, vắc xin; tiêm bắt buộc, tự nguyện
- **Căn cứ**: Luật 114/2025 Đ22 k1, k3; TT 13/2026 Đ3 (14 bệnh TCMR, có HPV), Đ4 (11 bệnh tiêm chống dịch), Đ26 k1 (cơ sở có phòng sinh: viêm gan B trong 24 giờ sau sinh). NĐ 90 Đ9 k3 e (tính vào giá khoản đã được NSNN bảo đảm), k3 g (bán vắc xin TCMR): 3–5 triệu.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: master `vaccine` ↔ `antigen` ↔ `disease` ↔ `program` (TCMR, chống dịch, dịch vụ); mỗi mũi lưu `program`; bảng giá chặn tính tiền vắc xin TCMR; nhắc mũi viêm gan B sơ sinh.

### CHUYENKHOA-R24 — Điều kiện cơ sở, điểm tiêm; lưu hồ sơ tiêm chủng
- **Căn cứ**: Luật 114 Đ8 k7; NĐ 165 Đ49 (HL 01/07/2027), Đ94 k5 (Đ9–11 NĐ 104/2016 còn HL tới 30/06/2027), Đ95 k2; NĐ 90 Đ9 k5 a, b (dùng vắc xin ở cơ sở không đủ điều kiện; tiêm khi chưa công bố: 10–20 triệu), k2 e (không lưu giữ hồ sơ: 1–3 triệu). TT 13 Đ25 k10. TT 33/2025 mục 119 (hồ sơ công bố cơ sở đủ điều kiện: 20 năm), 121 (kế hoạch TCMR: 05 năm); không có dòng cho hồ sơ tiêm cá nhân.
- **Mức**: BẮT BUỘC (điều kiện, lưu giữ) / BẮT BUỘC? (thời hạn lưu hồ sơ tiêm cá nhân)
- **Phần mềm phải**: điểm tiêm có trạng thái công bố, chặn mở buổi tại điểm chưa công bố; hồ sơ mũi tiêm, sàng lọc, phản ứng không cho xóa; lưu tối thiểu bằng HSBA ngoại trú (10 năm) theo TT 33 Đ1 k2 b (suy luận); dữ liệu trên Hệ thống quốc gia không thay nghĩa vụ lưu tại cơ sở (suy luận).

### CHUYENKHOA-R25 — Tiền sử tiêm chủng trên Sổ SKĐT VNeID
- **Căn cứ**: QĐ 31/QĐ-BYT Đ2 k3 b (Sổ SKĐT có tiền sử tiêm chủng: loại vắc xin, kháng nguyên, số mũi, nơi, ngày tiêm), Đ1 k1, Đ5 (SKDT-R01).
- **Mức**: BẮT BUỘC? (chưa thấy văn bản buộc cơ sở tiêm đẩy thẳng lên VNeID; kênh hợp lý là Hệ thống tiêm chủng quốc gia, suy luận)
- **Phần mềm phải**: dùng số định danh cá nhân làm khóa đối tượng (SKDT-R05); không tự xây kênh đẩy VNeID khi chưa có hướng dẫn; có khóa chống trùng nếu gửi qua hai kênh (suy luận).

### D. Quảng cáo dịch vụ y tế, thuốc trên web, app, nền tảng

### CHUYENKHOA-R26 — Nội dung bắt buộc của quảng cáo dịch vụ KCB; hết thủ tục xác nhận
- **Căn cứ**: NĐ 342/2025 Đ9: quảng cáo dịch vụ KCB phải có (1) tên, địa chỉ, số giấy phép hoạt động, thời gian hoạt động; (2) phạm vi hoạt động chuyên môn do cơ quan y tế phê duyệt. Luật Quảng cáo Đ20 k4 đ. NĐ 87/2026 Đ75 k1 (thiếu một nội dung: 15–20 triệu; bổ sung tước GPHĐ 01–03 tháng theo k5 a), k3 (quảng cáo khi chưa có GPHĐ hoặc CCHN: 30–40 triệu). TT 03/2026 Đ2 k1: bãi bỏ TT 09/2015 trừ phần thực phẩm, sữa, sản phẩm dinh dưỡng trẻ nhỏ → không còn thủ tục xác nhận nội dung quảng cáo dịch vụ KCB.
- **Áp dụng**: BV, PK (web, fanpage, app); sàn đặt khám đăng trang cơ sở · **Hiệu lực/hạn**: 15/02/2026; phạt từ 15/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: template trang/card cơ sở tự chèn 5 trường từ hồ sơ pháp lý; chặn xuất bản bài quảng cáo thiếu trường; onboarding cơ sở trên sàn bắt nhập và đối chiếu số GPHĐ.
- **Bẫy**: mức phạt NĐ 87 là của cá nhân; tổ chức gấp 02 lần (NĐ 87 Đ6 k2–3).

### CHUYENKHOA-R27 — Không quảng cáo vượt phạm vi chuyên môn; không gian dối
- **Căn cứ**: Luật KCB Đ7 k20: cấm "Quảng cáo vượt quá phạm vi hành nghề hoặc vượt quá phạm vi hoạt động chuyên môn đã được cơ quan có thẩm quyền phê duyệt; lợi dụng kiến thức y học để quảng cáo gian dối". NĐ 87 Đ75 k4 (40–60 triệu; k5 c tước GPHĐ hoặc CCHN 03–06 tháng). Luật Quảng cáo Đ8 k9 (gây nhầm lẫn về chất lượng, công dụng; NĐ 87 Đ50 k5 c: 80–100 triệu), Đ19 k1.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục dịch vụ công khai sinh từ danh mục kỹ thuật được duyệt (MA-LT-R14), không nhập tự do; bác sĩ chỉ gắn với dịch vụ trong phạm vi hành nghề; quy trình duyệt nội dung có người chịu trách nhiệm chuyên môn, lưu phiên bản đã đăng.

### CHUYENKHOA-R28 — Nhãn quảng cáo, nút tắt, báo vi phạm; minh bạch kết quả tài trợ
- **Căn cứ**: Luật Quảng cáo Đ23 k1, k2 a–c (sửa bởi Luật 75): phải có dấu hiệu phân biệt nội dung quảng cáo; quảng cáo không cố định có nút tắt, báo vi phạm, từ chối xem. NĐ 342 Đ17 k2–4 (tắt chỉ với một lần tương tác; không có biểu tượng tắt giả; ảnh tĩnh không có thời gian chờ, video chờ tối đa 05 giây; tiếp nhận, xử lý báo vi phạm và trả kết quả), Đ19 k4 (nền tảng trung gian: hiển thị tên, địa chỉ người quảng cáo; kết quả tìm kiếm tài trợ phải phân biệt). NĐ 87 Đ56 k2 (30–40 triệu), k1 g (không minh bạch khi vận hành nền tảng trung gian: 20–30 triệu).
- **Áp dụng**: cổng BV, app đặt lịch, sàn đặt khám, app nhà thuốc có vị trí trả phí · **Hiệu lực/hạn**: 01/01/2026; 15/02/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: nhãn "Quảng cáo"/"Được tài trợ" trên mọi vị trí trả phí (kể cả bác sĩ, PK được đẩy hạng); popup có nút tắt thật; luồng báo vi phạm có mã phiếu, trạng thái; hiển thị tên người mua quảng cáo.

### CHUYENKHOA-R29 — Gỡ quảng cáo vi phạm trong 24 giờ; nghĩa vụ người kinh doanh dịch vụ quảng cáo trên mạng
- **Căn cứ**: Luật Quảng cáo Đ23 k7 (Luật 75): "phải thực hiện việc ngăn chặn, gỡ bỏ quảng cáo vi phạm chậm nhất 24 giờ kể từ khi có yêu cầu của cơ quan nhà nước có thẩm quyền"; Đ23 k3 b–d. NĐ 342 Đ18 k2 (cùng mốc 24 giờ cho mọi bên tham gia quảng cáo trên mạng), Đ19 k1 (thông báo thông tin liên hệ với Bộ VHTTDL; giấy xác nhận trong 04 ngày làm việc), k2 (lưu thông tin người quảng cáo, sản phẩm, mẫu, thời gian, vị trí, hợp đồng trong 03 năm kể từ ngày cuối cùng quảng cáo hiển thị), k3 (báo cáo năm Mẫu 04 chậm nhất 25/11). NĐ 87 Đ56 k1 (20–30 triệu), k3 (40–50 triệu), k4 (không gỡ trong 24 giờ: 50–60 triệu).
- **Áp dụng**: mọi bên tham gia quảng cáo trên mạng (24 giờ); Đ19 cho người kinh doanh dịch vụ quảng cáo trên mạng
- **Mức**: BẮT BUỘC (24 giờ) / BẮT BUỘC? (Đ19 với sàn đặt khám bán vị trí nổi bật: việc xếp vai là suy luận)
- **Phần mềm phải**: công cụ gỡ ngay theo mẫu quảng cáo hoặc theo nhà quảng cáo; log thời điểm nhận yêu cầu và gỡ; bảng `ad_record` đủ trường Đ19 k2, lưu ≥3 năm sau lần hiển thị cuối; danh sách chặn đối tác; nhắc báo cáo 25/11.

### CHUYENKHOA-R30 — Quảng cáo thuốc
- **Căn cứ**: Luật Quảng cáo Đ7 k5 (cấm quảng cáo thuốc kê đơn, thuốc không kê đơn bị khuyến cáo hạn chế hoặc cần giám sát thầy thuốc). Luật Dược Đ79 k1–2, Đ6 k10, k15. NĐ 163/2025 Đ103 k2, k4, k7 (nội dung bắt buộc, gồm câu "Đọc kỹ hướng dẫn sử dụng trước khi dùng" và số giấy xác nhận; web, app không âm thanh phải hiện đủ; cỡ chữ), Đ104 k6 (từ cấm như "chuyên trị", "an toàn", "khỏi hẳn", "khuyên dùng"…), k13, k15, k16, Đ111. TT 31/2025 Đ19–20. NĐ 87 Đ49 k1 d (quảng cáo thuốc kê đơn: 50–70 triệu), Đ69 k1–4 (5–40 triệu; k4 đ quảng cáo khi chưa có hoặc sai giấy xác nhận: 30–40 triệu). NĐ 90 Đ67 k3 (thông tin thuốc: 15–30 triệu).
- **Áp dụng**: app, web nhà thuốc; sàn; cổng BV có trang thuốc
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cờ `rx_only` (DUOC-R29) chặn mọi banner, push, bài quảng cáo; bắt nhập số giấy xác nhận và tự chèn câu "Đọc kỹ hướng dẫn sử dụng trước khi dùng"; lọc từ cấm, chặn ảnh nhân viên y tế trong creative thuốc; không đặt quảng cáo thuốc trong bài tư vấn bệnh liên quan.
- **Bẫy**: NĐ 90/2026 không có điều phạt quảng cáo thuốc hay dịch vụ KCB (chỉ quảng cáo rượu bia Đ33 và sữa); dùng NĐ 87/2026.

### CHUYENKHOA-R31 — Thông tin thuốc và bán thuốc trên app, web
- **Căn cứ**: NĐ 163/2025 Đ41 (đăng giấy chứng nhận đủ điều kiện, chứng chỉ người phụ trách chuyên môn, thông tin từng thuốc; thông tin thuốc ở chuyên mục riêng, không lẫn sản phẩm không phải thuốc), Đ42 (bao bì giao hàng in số điện thoại người tư vấn). Luật Dược Đ6 k17–19, Đ42 k4: xem DUOC-R29. NĐ 342 Đ5 k2–3 (quảng cáo thực phẩm bảo vệ sức khỏe phải có cụm "Thực phẩm bảo vệ sức khỏe" và khuyến cáo thực phẩm không phải là thuốc, không thay thế thuốc chữa bệnh). NĐ 90 Đ59 k3 m, k4 g, i, k.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: ngoài DUOC-R29: cây danh mục tách "Thuốc" khỏi TPBVSK, mỹ phẩm, thiết bị; trang nhà thuốc hiện giấy chứng nhận, chứng chỉ; nhãn giao hàng có số điện thoại dược sĩ; template TPBVSK tự chèn cụm từ và khuyến cáo.

### CHUYENKHOA-R32 — Đánh giá, xếp hạng bác sĩ, cơ sở; nội dung quy kết sự cố y khoa; KOL
- **Căn cứ**: Luật BVQLNTD Đ10 k3 b (cấm sắp xếp ưu tiên không công khai tiêu chí), k3 c (cấm ngăn hiển thị hoặc hiển thị không trung thực phản hồi, đánh giá), k1 h (cấm không công khai tài trợ người có ảnh hưởng). Luật TMĐT Đ17 k2 h, k1 đ; NĐ 248 Đ11 (công khai tiêu chí ưu tiên hiển thị). Luật Quảng cáo Đ15a k2–3 (Luật 75): người có ảnh hưởng phải xác minh người quảng cáo, kiểm tra tài liệu, chưa dùng hoặc chưa hiểu rõ thì không giới thiệu, thông báo việc quảng cáo; NĐ 87 Đ51 (40–60, 60–80, 80–100 triệu theo hành vi). Luật KCB Đ7 k17 (NĐ 90 Đ38 k5 n: 5–10 triệu), Đ7 k21 (đăng thông tin quy kết trách nhiệm khi sự cố y khoa chưa có kết luận; NĐ 90 Đ38 k7 h: 30–40 triệu). Luật Quảng cáo Đ8 k11 ("nhất", "duy nhất", "tốt nhất", "số một" không có tài liệu chứng minh; NĐ 87 Đ50 k2 a: 10–20 triệu).
- **Áp dụng**: sàn đặt khám, app có review bác sĩ; cơ sở có chương trình KOL
- **Mức**: BẮT BUỘC (hiển thị trung thực, công khai tiêu chí, nhãn tài trợ, Đ7 k21) / BẮT BUỘC? (Luật TMĐT với app chỉ đặt lịch không thanh toán, suy luận)
- **Phần mềm phải**: trang tiêu chí xếp hạng công khai; không ẩn đánh giá xấu trừ khi vi phạm pháp luật (log lý do); hàng đợi kiểm duyệt review quy kết sự cố y khoa (tạm ẩn có lý do); chỉ cho đánh giá từ tài khoản có lượt khám thật (suy luận); nhãn "Có tài trợ" cho bài KOL được trả tiền; lọc từ tuyệt đối.
- **Bẫy**: không có quy định y tế riêng về xếp hạng bác sĩ. Hành vi cấm của Luật KCB nằm ở Đ7, không phải Đ12.

### CHUYENKHOA-R33 — Quảng cáo cấm trong sản khoa, ghép tạng; livestream
- **Căn cứ**: NĐ 87/2026 Đ75 k2 (quảng cáo chẩn đoán, lựa chọn giới tính phôi, thai nhi; quảng cáo, môi giới hiến, nhận bộ phận cơ thể vì mục đích thương mại: 20–30 triệu; k5 b tước GPHĐ 03–06 tháng). Luật TMĐT Đ22 k5–7 (giấy xác nhận trước livestream hàng phải xác nhận; dừng, gỡ ngay livestream hàng cấm quảng cáo; lưu dữ liệu hình ảnh, âm thanh livestream ít nhất 01 năm), Đ24. Cấm tiết lộ giới tính thai trong kết quả: xem BAOMAT-CB-R13.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lọc từ khóa giới tính thai, "sinh con trai/gái", môi giới tạng trên mọi bài của PK sản, BV; nền tảng livestream lưu bản ghi ≥1 năm, chặn livestream thuốc kê đơn.

### E. Ngôn ngữ, bộ mã và khả năng tiếp cận

### CHUYENKHOA-R34 — Tiếng Việt là ngôn ngữ KCB; chỉ định, đơn thuốc bằng tiếng Việt
- **Căn cứ**: Luật KCB Đ21 k1: "Ngôn ngữ sử dụng trong khám bệnh, chữa bệnh là tiếng Việt", trừ k2. Đ21 k3 b: thông tin KCB ghi bằng ngôn ngữ đã đăng ký của người hành nghề nước ngoài phải đồng thời dịch sang tiếng Việt. NĐ 96/2023 Đ35 k3 (gốc-OCR, diễn giải): chỉ định điều trị, kê đơn ghi bằng tiếng Việt; người hành nghề nước ngoài ghi bằng ngôn ngữ đã đăng ký, dịch sang tiếng Việt, có chữ ký người phiên dịch trên đơn. NĐ 90/2026 Đ38 k5 đ (chỉ định, kê đơn bằng ngôn ngữ chưa đăng ký hoặc người phiên dịch chưa được công nhận: 5–10 triệu), k5 d. TT 32 Đ52 k2 c (EMR-R04).
- **Áp dụng**: mọi cơ sở KCB
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bản tiếng Việt là bản chính cho mọi văn bản pháp định; với người hành nghề nước ngoài: lưu bản gốc theo ngôn ngữ đăng ký và bản dịch tiếng Việt, ghi người dịch; đơn thuốc có vai ký thứ hai của người phiên dịch; master thuốc, dịch vụ, chẩn đoán dùng tên tiếng Việt theo danh mục BYT.
- **Bẫy**: Luật KCB Đ121 k4 giữ quy định ngôn ngữ của Luật 40/2009 với người nước ngoài tới hết 31/12/2031; Đ120 k4 điều kiện năng lực tiếng Việt từ 01/01/2032. Phương án an toàn: luôn có bản tiếng Việt và người phiên dịch (suy luận).

### CHUYENKHOA-R35 — Nhu cầu ngôn ngữ và người phiên dịch cho người bệnh
- **Căn cứ**: Luật KCB Đ21 k3 a, k4. NĐ 96 Đ35 k1, k2; Đ36 k1 (gốc-OCR, diễn giải): người nước ngoài, người dân tộc thiểu số không dùng được tiếng Việt, người khuyết tật ngôn ngữ đăng ký yêu cầu về ngôn ngữ với cơ sở để cơ sở bố trí người hành nghề hoặc phiên dịch; không bố trí được thì người bệnh tự bố trí và tự chịu trách nhiệm nội dung phiên dịch; k2 a (cấp cứu: dùng nhân viên biết ngôn ngữ, không chịu trách nhiệm kết quả phiên dịch).
- **Áp dụng**: mọi cơ sở KCB, nhất là BV, PK quốc tế
- **Mức**: BẮT BUỘC (nghĩa vụ cơ sở) / NÊN (chức năng phần mềm hỗ trợ)
- **Phần mềm phải**: `preferred_language`, `needs_interpreter`, `interpreter_source` (cơ sở / người bệnh tự bố trí / nhân viên cấp cứu), tên, GPHN người phiên dịch (khi nhân đạo, chuyển giao) gắn lượt khám; mẫu xác nhận người bệnh tự bố trí phiên dịch; app đặt lịch cho chọn ngôn ngữ khi đăng ký. Định danh người nước ngoài: SKDT-R12.

### CHUYENKHOA-R36 — Ngôn ngữ đăng ký của người hành nghề nước ngoài
- **Căn cứ**: Luật KCB Đ37 k5; NĐ 96 Đ28. NĐ 90 Đ38 k5 d (khám bằng ngôn ngữ chưa đăng ký hoặc bằng tiếng Việt khi chưa được công nhận thành thạo: 5–10 triệu).
- **Mức**: BẮT BUỘC (khi có người hành nghề nước ngoài)
- **Phần mềm phải**: hồ sơ nhân sự có ngôn ngữ đã đăng ký; cảnh báo khi khám bằng ngôn ngữ khác mà không có phiên dịch; tự đòi bản dịch tiếng Việt (R34).

### CHUYENKHOA-R37 — Bộ mã ký tự: Unicode TCVN 6909:2001, UTF-8
- **Căn cứ**: QĐ 72/2002/QĐ-TTg Đ1 (từ 01/01/2003 thống nhất dùng TCVN 6909:2001 trong trao đổi thông tin điện tử giữa tổ chức của Đảng và Nhà nước). TT 39/2017/TT-BTTTT PL: mục 2.7 UTF-8 bắt buộc; mục 3.14 TCVN 6909:2001 bắt buộc. CV 365 III.1.3 c: EMR đáp ứng TT 39/2017 (EMR, MA-LT).
- **Áp dụng**: BV công, hệ thống đầu tư/thuê bằng NSNN, EMR; vendor
- **Mức**: BẮT BUỘC? (TT 39 dựa trên Luật CNTT đã hết HL; CV 365 không phải VBQPPL) / NÊN (cơ sở tư)
- **Phần mềm phải**: lưu, truyền, xuất (XML BHYT, API, PDF) bằng UTF-8; không dùng TCVN3/VNI; chuẩn hóa Unicode NFC trước khi lưu và so khớp (suy luận kỹ thuật); font PDF nhúng đủ ký tự tiếng Việt.

### CHUYENKHOA-R38 — Khả năng tiếp cận cho người khuyết tật trên web, cổng, app
- **Căn cứ**: TT 26/2020/TT-BTTTT Đ2 k1, k2 (CQNN gồm đơn vị sự nghiệp dùng NSNN làm trang, cổng thông tin, cổng dịch vụ công), k4; Đ5 k1–2; Đ6 k2; PL mục 3: WCAG 1.0 bắt buộc với cơ quan, tổ chức tại Đ2 k2, k3; WCAG 2.0 (ISO/IEC 40500:2012), WCAG 2.1, ATAG khuyến nghị. TT 39/2017 mục 3.1: WCAG 2.0 khuyến nghị. Luật NKT Đ4 k1 d, Đ43 k1.
- **Áp dụng**: BV công dùng NSNN làm web, cổng đặt khám; BV tư, PK, app thương mại
- **Mức**: BẮT BUỘC? (WCAG 1.0 với đơn vị sự nghiệp dùng NSNN; hiệu lực sau khi Luật CNTT hết HL chưa xác minh) / NÊN (WCAG 2.1 AA cho mọi app y tế)
- **Phần mềm phải**: tối thiểu WCAG 1.0 cho BV công; nhắm WCAG 2.1 AA: văn bản thay thế, tương phản, điều khiển bàn phím, nhãn form, không chỉ dùng màu; app hỗ trợ VoiceOver, TalkBack, cỡ chữ động; không dùng CAPTCHA hình ảnh duy nhất trong luồng đặt khám (suy luận). Xem thêm TC-MS-R37 (yêu cầu tối thiểu hệ thống số).
- **Bẫy**: "TT 39/2017 bắt buộc WCAG" là sai; mức bắt buộc duy nhất tìm thấy là WCAG 1.0 trong TT 26/2020.

### CHUYENKHOA-R39 — Ưu tiên khám trong xếp hàng, đặt lịch
- **Căn cứ**: Luật KCB Đ3 k2: "Ưu tiên khám bệnh, chữa bệnh đối với trường hợp người bệnh trong tình trạng cấp cứu, trẻ em dưới 06 tuổi, phụ nữ có thai, người khuyết tật đặc biệt nặng, người khuyết tật nặng, người từ đủ 75 tuổi trở lên, người có công với cách mạng phù hợp với đặc thù của cơ sở khám bệnh, chữa bệnh."
- **Áp dụng**: mọi cơ sở KCB
- **Mức**: BẮT BUỘC (cách thực hiện do cơ sở quyết định)
- **Phần mềm phải**: hàng đợi có cờ ưu tiên theo 7 nhóm; tự gợi ý từ tuổi, thai kỳ, mức khuyết tật (XML12 `DANG_KHUYETTAT`, `MUC_DO_KHUYETTAT`); ghi lý do ưu tiên để audit.

## 3. Pattern thiết kế

### CHUYENKHOA-P01 — Chẩn đoán đa hệ mã có phiên bản
- **Giải quyết**: R01, R02, R03
- **Cách làm**: mọi hệ mã (ICD-10 TT 06, YHCT 7603, YHCT 2552 PL I/II, huyệt, kỹ thuật TT 23 PL 01/02) là `code_system` có phiên bản; ánh xạ YHCT ↔ ICD-10 ở bảng riêng; nạp đợt mới bằng dữ liệu.
- **Gợi ý dữ liệu**: `code_system(id, source_doc, version, valid_from, valid_to)`; `code(code_system_id, code, display_vi, status, inactive_from)`; `code_map(from_system, from_code, to_system, to_code, map_type, source_doc, valid_from)`; `encounter_diagnosis(encounter_id, system IN ('YHHD','YHCT'), role, code, code_system_version, display_snapshot, timepoint)` với `UNIQUE(encounter_id, system, timepoint) WHERE role='main'`; `tcm_diagnosis_detail(encounter_id, bat_cuong[], nguyen_nhan[], tang_phu[], kinh_lac[], the_lam_sang)`; hàm sinh `MA_BENH_YHCT` và tên `Tên YHCT [Tên YHHĐ]`.
- **Đánh đổi**: thêm bảng; đổi lại không sửa code khi có QĐ mã mới.

### CHUYENKHOA-P02 — Master thuốc YHCT và công thức chế phẩm
- **Giải quyết**: R05, R06, R07
- **Cách làm**: tách loại sản phẩm, công thức có phiên bản được duyệt, thu hồi theo lô có ngày hiệu lực.
- **Gợi ý dữ liệu**: `tcm_product(kind, name_by_ingredients, brand_name, route_group, reg_no, bhyt_condition JSONB, valid_from, valid_to)`; `tcm_indication(product_id, icd10, yhct_code, source)`; `formula(product_id, version, approved_by, approved_at, sent_to_bhxh_at, unit_cost)`; `formula_line(formula_id, ingredient_id, qty, in_bhyt_list, che_bien_codes[])`; `recall(product_id, lot_no, effective_from)`; `CHECK (kind <> 'che_pham_tu_bao_che' OR channel = 'internal')`.
- **Đánh đổi**: nhập liệu ban đầu nặng cho cơ sở có nhiều chế phẩm.

### CHUYENKHOA-P03 — Mẫu HSBA chuyên khoa và thành phần vẽ
- **Giải quyết**: R09, R10, R12
- **Cách làm**: danh mục mẫu theo mã TT 32, bật theo phạm vi chuyên môn; trường vẽ lưu ảnh + metadata; trường mở rộng không đè trường mẫu.
- **Gợi ý dữ liệu**: `record_template(code, specialty, allowed_facility_types[], legal_source, version)`; `facility_template_enable(facility_id, template_code)`; trường `drawing` (SVG/PNG, `base_diagram_id`, `author_id`, `drawn_at`); `extension JSONB`.
- **Đánh đổi**: phải bảo trì form khi BYT sửa mẫu.

### CHUYENKHOA-P04 — Cổng đồng ý (consent gate)
- **Giải quyết**: R11, R14
- **Cách làm**: thủ thuật không chuyển `in_progress` nếu thiếu đồng ý hợp lệ, trừ cấp cứu có người duyệt; ảnh dùng cho truyền thông lọc qua view chỉ trả ảnh có đồng ý chưa thu hồi.
- **Gợi ý dữ liệu**: `consent(patient_id, encounter_id, type IN ('01/BV2','40/BV2','41/BV2',…,'marketing_photo'), signer_role, representative_relation, checklist JSONB, signed_doc_id, signed_at, revoked_at)`; `emergency_override(reason, approver)`; `clinical_photo(encounter_id, phase, storage_ref, retention_class)`.
- **Đánh đổi**: thêm bước tại quầy; cần luồng cấp cứu rõ ràng.

### CHUYENKHOA-P05 — Lưu trữ theo loại hồ sơ chuyên khoa
- **Giải quyết**: R13, R15, R24
- **Cách làm**: mở rộng `retention_policy` của EMR-R22: `PTTM_20Y` (mục 43), `IVF_PERMANENT` (211), `GAMETE_DONATION_PERMANENT` (214), `GENDER_REASSIGN_70Y` (215), `IMMUNIZATION_RECORD` (chưa có dòng, đặt ≥10 năm, cờ "cần xác minh"). Ghép tạng: 30 năm (BAOMAT-CB-R15). Tự nâng lớp khi phát sinh thủ thuật `is_cosmetic_surgery`.
- **Gợi ý dữ liệu**: `medical_record.retention_class`, `retention_policy(code, years NULL, permanent BOOL, legal_ref)`.
- **Đánh đổi**: dung lượng lưu dài hạn; cần quy trình hủy theo lớp.

### CHUYENKHOA-P06 — Đồng bộ tiêm chủng theo sự kiện
- **Giải quyết**: R16, R17, R18, R21
- **Cách làm**: mỗi mũi tiêm ghi outbox gửi Hệ thống quốc gia; mục tiêu "thời gian thực" (ví dụ < 5 phút, tự đặt) có cảnh báo; tai biến nặng sinh báo cáo có hạn 24 giờ và khóa lô.
- **Gợi ý dữ liệu**: `immunization_subject(national_id, national_subject_id, …44 trường, dedup_key)`; `immunization_event(subject_id, vaccine_id, antigen_codes[], dose_no, program, site_id, lot_no, screening_id, given_at, observed_until)`; `outbox(aggregate, payload, status, attempt, ack_id)`; `aefi_report(event_id, severity, detected_at, deadline_at, sent_soyte_at, sent_cdc_at)`; cờ loại trừ BCA, BQP.
- **Đánh đổi**: chưa có đặc tả API chính thức; phải đổi adapter khi có.

### CHUYENKHOA-P07 — Kiểm duyệt nội dung quảng cáo và đánh giá
- **Giải quyết**: R26–R33
- **Cách làm**: trước khi đăng chạy bộ luật: trường bắt buộc NĐ 342 Đ9, từ cấm (Luật QC Đ8 k11; NĐ 163 Đ104 k6), `rx_only`, từ khóa giới tính thai, ảnh nhân viên y tế trong QC thuốc, dịch vụ ngoài phạm vi; lưu hồ sơ quảng cáo 3 năm; theo dõi gỡ trong 24 giờ.
- **Gợi ý dữ liệu**: `promo_content(type, body, media[], required_fields_ok, approval_status, approved_by_professional_id, published_at)`; `ad_record(…trường Đ19 k2, last_shown_at, retain_until)`; `takedown_request(authority, received_at, ad_id, removed_at)` cảnh báo khi quá 24 giờ; `review(author_account_id, verified_encounter_id, rating, status, moderation_reason)`; trang `ranking_criteria`.
- **Đánh đổi**: bộ lọc từ khóa dễ chặn nhầm; cần người duyệt cuối.

### CHUYENKHOA-P08 — Văn bản hai ngôn ngữ, bản tiếng Việt là bản chính
- **Giải quyết**: R34, R35, R36
- **Cách làm**: với người hành nghề nước ngoài bắt buộc có `text_vi` và người dịch trước khi ký; đơn thuốc thêm vai ký phiên dịch.
- **Gợi ý dữ liệu**: `clinical_text(lang_original, text_original, text_vi, translator_id, translated_at)`; `signature(role='translator')`; `encounter_language(encounter_id, preferred_language, interpreter_source, interpreter_name, interpreter_license_no)`.
- **Đánh đổi**: chậm luồng kê đơn của bác sĩ nước ngoài.

### CHUYENKHOA-P09 — Chất lượng dữ liệu tiếng Việt và tiếp cận
- **Giải quyết**: R37, R38, R39
- **Cách làm**: middleware chuẩn hóa NFC ở tầng nhập; cột `name_search` bỏ dấu để tìm trùng; CI chạy kiểm tra accessibility tự động (axe-core hoặc tương đương) trên luồng đặt khám; hàng đợi có lý do ưu tiên.
- **Gợi ý dữ liệu**: `queue_ticket(priority_reason IN ('cap_cuu','duoi_6_tuoi','co_thai','nkt_dac_biet_nang','nkt_nang','tu_75_tuoi','nguoi_co_cong'))`.
- **Đánh đổi**: kiểm tra tự động không thay được thử thủ công với trình đọc màn hình.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| CHUYENKHOA-A01 | R01 | So 5 bệnh án YHCT với 18, 19, 20/BV1 (hai cột chẩn đoán có mã, tứ chẩn, biện chứng); tìm mẫu QĐ 1941/2019 | Bảng so khớp, bản in | BẮT BUỘC |
| CHUYENKHOA-A02 | R02 | SQL đếm `MA_BENH_YHCT` rỗng ở khoa YHCT; tìm 05 mã PL 02 QĐ 1978 sau 01/07/2026; `U50.351` ánh xạ A97 | Kết quả truy vấn, XML mẫu | BẮT BUỘC |
| CHUYENKHOA-A03 | R02 | Tên bệnh trên bảng kê ca YHCT dạng `Tên YHCT [Tên YHHĐ]` | Bảng kê in | BẮT BUỘC |
| CHUYENKHOA-A04 | R03 | Đã nạp QĐ 2552 chưa; bát cương, tạng phủ là mã hay text; thử chỉ định kỹ thuật dấu * | Ảnh danh mục, kết quả thử | BẮT BUỘC? |
| CHUYENKHOA-A05 | R04 | Chỉ định kỹ thuật chỉ có ở PL 02 TT 23 trước 01/01/2028 | Bị chặn hay không | BẮT BUỘC |
| CHUYENKHOA-A06 | R05 | Master thuốc YHCT: tên theo thành phần, đường dùng, điều kiện thanh toán có ngày hiệu lực; còn danh mục TT 05/2015 | Xuất danh mục | BẮT BUỘC |
| CHUYENKHOA-A07 | R06 | Tạo đơn bán ra ngoài chế phẩm tự bào chế; công thức có cờ ngoài danh mục, số duyệt, ngày gửi BHXH; `MA_PP_CHEBIEN` | Kết quả thử, hồ sơ | BẮT BUỘC |
| CHUYENKHOA-A08 | R07, R08 | Kê thuốc YHCT ngoài chỉ định; tài khoản y sĩ, lương y chỉ định kết hợp | Cảnh báo, chặn | BẮT BUỘC / NÊN |
| CHUYENKHOA-A09 | R09, R10 | Liệt kê mẫu bệnh án PK đang dùng; mẫu RHM có trường hình vẽ; trường thêm có đè trường mẫu | Danh sách, bản in | BẮT BUỘC |
| CHUYENKHOA-A10 | R11 | Bắt đầu phiếu thủ thuật (kể cả filler) khi chưa có 01/BV2; người ký đại diện có quan hệ | Kết quả thử | BẮT BUỘC |
| CHUYENKHOA-A11 | R13 | Loại hình cơ sở vs dịch vụ thẩm mỹ xâm lấn; phân bố `retention_class` HSBA có PTTM | Cấu hình, truy vấn | BẮT BUỘC |
| CHUYENKHOA-A12 | R14 | Ảnh người bệnh trên web, fanpage đối chiếu bản ghi đồng ý | Danh sách ảnh, đồng ý | BẮT BUỘC |
| CHUYENKHOA-A13 | R15 | Module IVF chỉ bật ở BV có phạm vi phụ sản; `retention_class` vĩnh viễn | Cấu hình | BẮT BUỘC |
| CHUYENKHOA-A14 | R16, R17 | Độ trễ từ xác nhận mũi tiêm tới ack Hệ thống quốc gia (100 mũi); tìm đối tượng trùng định danh | Log outbox, truy vấn | BẮT BUỘC |
| CHUYENKHOA-A15 | R18 | So schema với 44 trường; gửi thiếu 1 trong 20 trường bắt buộc | Bảng so khớp | BẮT BUỘC? |
| CHUYENKHOA-A16 | R19, R20 | Xác nhận mũi khi chưa xong sàng lọc; giờ kết thúc theo dõi 30 phút; người tiêm nhận sổ | Kết quả thử, mẫu sổ | BẮT BUỘC |
| CHUYENKHOA-A17 | R21 | Diễn tập tai biến nặng: buổi bị khóa, lô bị chặn, báo cáo trong 24 giờ | Biên bản, log | BẮT BUỘC |
| CHUYENKHOA-A18 | R22 | Báo cáo tháng gần nhất gửi trước ngày 03 tháng sau | Báo cáo, thời điểm | BẮT BUỘC |
| CHUYENKHOA-A19 | R23, R24 | Vắc xin TCMR có bị tính tiền; buổi tiêm tại điểm chưa công bố | Cấu hình giá, danh sách điểm | BẮT BUỘC |
| CHUYENKHOA-A20 | R26, R27 | Duyệt 20 bài quảng cáo: đủ 5 trường NĐ 342 Đ9; dịch vụ ngoài phạm vi GPHĐ | Ảnh chụp, đối chiếu GPHĐ | BẮT BUỘC |
| CHUYENKHOA-A21 | R28, R29 | Nhãn quảng cáo trên vị trí trả phí, nút tắt, báo vi phạm; log yêu cầu gỡ và thời gian gỡ; `ad_record` 3 năm | Ảnh, log | BẮT BUỘC |
| CHUYENKHOA-A22 | R30, R31 | Tạo banner thuốc kê đơn; QC thuốc có câu bắt buộc và số xác nhận; danh mục thuốc lẫn TPBVSK | Kết quả thử | BẮT BUỘC |
| CHUYENKHOA-A23 | R32 | Trang tiêu chí xếp hạng; review bị ẩn và lý do; đăng review quy kết sự cố; nhãn tài trợ KOL | Ảnh, log kiểm duyệt | BẮT BUỘC |
| CHUYENKHOA-A24 | R33 | Tìm từ khóa giới tính thai trong nội dung đã đăng; bản ghi livestream 11 tháng trước còn không | Kết quả tìm, file | BẮT BUỘC |
| CHUYENKHOA-A25 | R34, R36 | Đơn của người hành nghề nước ngoài có bản tiếng Việt và chữ ký phiên dịch; hồ sơ nhân sự có ngôn ngữ đăng ký | Bản in, hồ sơ | BẮT BUỘC |
| CHUYENKHOA-A26 | R35 | Lượt khám người nước ngoài, dân tộc thiểu số có ghi nhu cầu ngôn ngữ, phiên dịch | Bản ghi | BẮT BUỘC / NÊN |
| CHUYENKHOA-A27 | R37 | Encoding DB, API, XML; bản ghi trùng do khác dạng Unicode | Truy vấn | BẮT BUỘC? / NÊN |
| CHUYENKHOA-A28 | R38 | Công cụ kiểm tra tự động trên trang đặt khám; thử VoiceOver, TalkBack | Báo cáo | BẮT BUỘC? / NÊN |
| CHUYENKHOA-A29 | R39 | Lấy số cho người 75 tuổi, trẻ 5 tuổi, phụ nữ có thai | Ảnh hàng đợi | BẮT BUỘC |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới |
|---|---|---|---|
| 01/01/2024 | Mẫu HSBA TT 32 (18–20/BV1 YHCT, 27–29/BV1 PHCN) thay QĐ 1941/2019, QĐ 3730/2021 | Cơ sở KCB, vendor | Đã qua |
| 01/07/2025 | TT 33/2025: PTTM 20 năm, IVF và hiến giao tử vĩnh viễn | Mọi cơ sở | Đã qua |
| 12/08/2025 | QĐ 2552 mã thuật ngữ YHCT đợt 1 | Cơ sở YHCT, vendor | Đã qua |
| 01/09/2025 | TT 27/2025 HL | Cơ sở BHYT | Đã qua |
| 01/10/2025 | NĐ 207/2025 HL; NĐ 10/2015, NĐ 98/2016, NĐ 96 Đ40 k9 hết HL | Cơ sở IVF | Đã qua |
| 01/01/2026 | Luật 75/2025 sửa Luật Quảng cáo (gỡ 24 giờ, KOL) | Mọi bên quảng cáo trên mạng | Đã qua |
| 15/02/2026 | NĐ 342/2025 HL; TT 03/2026 bỏ thủ tục xác nhận QC dịch vụ KCB | Cơ sở KCB, nền tảng | Đã qua |
| 15/05/2026 | NĐ 87/2026 (phạt QC) và NĐ 90/2026 (phạt y tế) HL | Tất cả | Đã qua |
| 01/07/2026 | Luật Phòng bệnh, NĐ 165, TT 13/2026, TT 15/2026, Luật TMĐT, NĐ 248, TT 06/2026 HL; QĐ 1978 áp dụng; NĐ 104 (trừ Đ9–11), TT 34/2018, TT 54/2015, NĐ 52/2013 hết HL | Cơ sở tiêm, cơ sở BHYT, nền tảng | Đã qua |
| 15/07/2026 | QĐ 2149 sửa mốc QTKT YHCT | Cơ sở YHCT | Đã qua |
| khoảng 30/08/2026 | Hết 60 ngày chuyển tiếp dữ liệu mã YHCT (suy luận cách đếm) | Cơ sở BHYT | Đã qua |
| 25/11/2026 | Hạn báo cáo năm của người kinh doanh dịch vụ quảng cáo trên mạng (NĐ 342 Đ19 k3) | Nền tảng | Sắp tới |
| 31/12/2026 | Hạn HSBA điện tử với PK, cơ sở không phải BV (EMR-R01) | PK | Sắp tới |
| 01/01/2027 | Nền tảng TMĐT phải xác thực danh tính người bán (NĐ 248 Đ52 k2) | Sàn TMĐT | Sắp tới |
| 30/06/2027 | Hết HL Đ9–11 NĐ 104/2016; hết chuyển tiếp web/app TMĐT xác nhận theo NĐ 52/2013 (Luật TMĐT Đ41 k1) | Cơ sở tiêm; nền tảng | Sắp tới |
| 01/07/2027 | NĐ 165 Đ49 (điều kiện cơ sở tiêm chủng mới) HL | Cơ sở tiêm | Sắp tới |
| 31/12/2027 / 01/01/2028 | TT 23 PL 01 hết; kỹ thuật YHCT chỉ có ở PL 02 bắt đầu | Mọi cơ sở, vendor | Sắp tới |
| 31/12/2031 / 01/01/2032 | Hết quy định ngôn ngữ cũ với người nước ngoài; bắt đầu điều kiện năng lực tiếng Việt | Người hành nghề nước ngoài | Sắp tới |

## 6. Bẫy trích dẫn và chuỗi thay thế

| Cũ | Mới | Từ ngày | Ghi chú |
|---|---|---|---|
| QĐ 1941/QĐ-BYT (2019) mẫu bệnh án YHCT | TT 32/2023 mẫu 18–20/BV1 | 01/01/2024 | TT 32 Đ53 k2 h |
| QĐ 3730/QĐ-BYT (2021) mẫu PHCN | TT 32/2023 mẫu 27–29/BV1 | 01/01/2024 | TT 32 Đ53 k2 i |
| QĐ 7603 PL 07.1 (một phần) | QĐ 1978/QĐ-BYT | 01/07/2026 | Phần còn lại giữ nguyên |
| TT 05/2015 Đ4–6, TT 27/2020 | TT 27/2025 | 01/09/2025 | Danh mục TT 05/2015 còn dùng |
| QĐ 486/QĐ-BYT (2026) Đ3 | QĐ 2149/QĐ-BYT | 15/07/2026 | — |
| NĐ 10/2015, NĐ 98/2016, NĐ 96 Đ40 k9 | NĐ 207/2025 | 01/10/2025 | NĐ 207 Đ15 k2 |
| Luật PCBTN 03/2007 | Luật Phòng bệnh 114/2025 | 01/07/2026 | Đ45 k2 |
| NĐ 104/2016, NĐ 13/2024 | NĐ 165/2026 | 01/07/2026 | Đ9–11 NĐ 104 giữ tới 30/06/2027 |
| TT 34/2018, 24/2018, 05/2020, 52/2025 | TT 13/2026 | 01/07/2026 | TT 13 Đ27 k2 |
| TT 54/2015 | TT 15/2026 | 01/07/2026 | Đ65 k2 |
| NĐ 181/2013, NĐ 70/2021 | NĐ 342/2025 | 15/02/2026 | NĐ 342 Đ32 k2 |
| TT 09/2015/TT-BYT | Phần lớn bãi bỏ bởi TT 03/2026 | 15/02/2026 | Còn phần thực phẩm, sữa trẻ em |
| NĐ 38/2021, NĐ 128/2022 | NĐ 87/2026 | 15/05/2026 | NĐ 87 Đ93 |
| NĐ 117/2020 | NĐ 90/2026 | 15/05/2026 | — |
| NĐ 54/2017, NĐ 88/2023; TT 07/2018 | NĐ 163/2025; TT 31/2025 | 01/07/2025 | — |
| NĐ 52/2013, NĐ 85/2021 | Luật TMĐT 122/2025 + NĐ 248/2026 | 01/07/2026 | Chuyển tiếp tới 30/06/2027 |
| TT 28/2009/TT-BTTTT | TT 26/2020/TT-BTTTT | 01/01/2021 | — |
| TT 22/2013/TT-BTTTT | TT 39/2017/TT-BTTTT | 01/07/2018 | — |

**Bẫy trích dẫn**
1. Hành vi cấm quảng cáo KCB là **Luật KCB Đ7 k20** (và k17, k21), không phải "Điều 12".
2. **NĐ 90/2026 không phạt quảng cáo thuốc, dịch vụ KCB**; dùng NĐ 87/2026 (Đ49, Đ50, Đ56, Đ69, Đ75). Mức NĐ 87 là của cá nhân; tổ chức ×2.
3. "Cập nhật dữ liệu tiêm chủng trong 24 giờ" không có căn cứ. Mốc 24 giờ chỉ cho báo cáo tai biến nặng và mũi viêm gan B sơ sinh.
4. TT 34/2018, NĐ 104/2016 hết HL; QĐ 3421/2017, QĐ 3891/2025 dựa trên căn cứ đã hết HL: trích kèm cảnh báo.
5. PL IV QĐ 2552 "thực hiện đến ngày 30/06/2026" không có nghĩa PL IV hết hiệu lực (TT 25/2026 đã lùi mốc TT 23).
6. QĐ 1978/2026 không thay toàn bộ danh mục mã YHCT.
7. TT 27/2025 là thông tư nguyên tắc; danh mục thuốc YHCT BHYT hiện vẫn theo TT 05/2015.
8. "HSBA thẩm mỹ 20 năm chỉ cho bệnh viện" là sai; "mọi hồ sơ thẩm mỹ 20 năm" cũng sai (mục 43 chỉ nêu phẫu thuật thẩm mỹ). Hồ sơ ghép tạng: 30 năm theo Luật 75/2006, không phải 20 năm.
9. "TT 39/2017 bắt buộc WCAG" là sai; chỉ WCAG 1.0 trong TT 26/2020 là bắt buộc, với CQNN và đơn vị sự nghiệp dùng NSNN.
10. Luật KCB Đ121 k4 giữ quy định ngôn ngữ của Luật 2009 với người nước ngoài tới hết 31/12/2031.
11. Dẫn NĐ 10/2015 hoặc NĐ 96 Đ40 k9 cho IVF là lỗi thời; căn cứ hiện hành là NĐ 207/2025 Đ10.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. **Bản PL 07.1 QĐ 7603 gốc** (toàn bộ mã YHCT và cặp ICD-10) chưa đọc; số lượng mã (thứ cấp nêu 4.144) chưa xác minh. Tải bản BYT hoặc BHXH.
2. **Tính bắt buộc của QĐ 2552/2025** và đợt 2: hỏi Cục Quản lý Y Dược cổ truyền.
3. **TT danh mục thuốc YHCT BHYT mới** (kích hoạt TT 27 Đ9–11): mới thấy tin dự thảo. TT 26/2026/TT-BYT (danh mục dược liệu rủi ro trung bình) chưa đánh giá.
4. **QĐ 486/QĐ-BYT** (QTKT YHCT) chưa đọc nội dung.
5. **Bảng chỉ tiêu QĐ 4750/3176** cho `MA_BENH_YHCT`, `MA_PP_CHEBIEN`: mới đối chiếu bản QĐ 130 năm 2023 (xem BHYT-DATA).
6. **Chuẩn API Hệ thống tiêm chủng quốc gia** cho hệ thống riêng; hiệu lực QĐ 3421/2017, QĐ 3891/2025 sau 01/07/2026: hỏi Cục Phòng bệnh hoặc VNCDC.
7. **Thời hạn lưu hồ sơ tiêm chủng cá nhân**: TT 33 không có dòng; hỏi Văn phòng BYT.
8. **Giấy xác nhận tiêm chủng điện tử trong nước**, mẫu sổ tiêm chủng mới: chưa thấy. TT 13/2026 chưa thấy trên datafiles, đang dùng bản BVĐK Bạc Liêu.
9. Hành vi "không cập nhật dữ liệu lên Hệ thống tiêm chủng" không có điểm phạt riêng; gần nhất là NĐ 90 Đ9 k3 c (không thực hiện đúng quy định về quản lý đối tượng tiêm chủng, 3–5 triệu) hoặc k2 c. Xếp vào điểm nào là suy luận: **cần luật sư** khi tư vấn mức phạt.
10. **Sàn đặt khám có là "người kinh doanh dịch vụ quảng cáo trên mạng"** (NĐ 342 Đ19) khi bán vị trí nổi bật, và có thuộc Luật TMĐT khi không thanh toán: **cần luật sư** hoặc hỏi Bộ VHTTDL, Bộ Công Thương. TT 12/2026/TT-BVHTTDL chỉ có nguồn thứ cấp.
11. **Ngôn ngữ trong giai đoạn chuyển tiếp** (Luật KCB Đ21 so với Đ121 k4): hỏi Cục Quản lý KCB. Văn bản sửa NĐ 96/2023 chưa đối chiếu với Đ35, Đ36, Đ40.
12. **TT 26/2020, TT 39/2017, QĐ 72/2002** sau khi Luật CNTT hết HL và BTTTT sáp nhập: hỏi Bộ KH&CN.
13. **Hỗ trợ sinh sản**: tác động của Luật Dân số 2025 lên IVF, mang thai hộ chưa xác minh. NĐ 207/2025 đã đối chiếu Đ3, Đ8, Đ10, Đ12, Đ15–17; các điều còn lại chưa đọc kỹ.
14. **Nha khoa, mắt**: không tìm thấy quy định phần mềm riêng; đơn kính của cơ sở kính thuốc (NĐ 96 Đ57) chưa khảo sát.
15. Nội dung (không phải mức phạt) của Luật Quảng cáo Đ7, Đ8, Đ15a, Đ23 k1–3; Luật Dược Đ79; NĐ 163 Đ41–42, Đ103–111; Luật TMĐT Đ17, Đ22; Luật BVQLNTD Đ10; NĐ 248 Đ11 chủ yếu do lượt phụ đọc; chưa đối chiếu lại câu chữ. Mức phạt NĐ 87 (Đ6, Đ49–51, Đ56, Đ69, Đ71, Đ75) và nội dung NĐ 342 (Đ5, Đ9, Đ17–19, Đ32) đã đối chiếu lại bản gốc.
