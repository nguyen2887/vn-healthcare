# CHUYENKHOA — Nghiệp vụ chuyên khoa và kênh tiếp cận người bệnh

> Kiểm tra lần cuối: 2026-10-06 (mốc tham chiếu 2026-10-05) · Phạm vi: các khoảng trống số 4, 5, 8, 9, 11 của inventory mục 6. Gồm năm mảng: (A) y học cổ truyền: mẫu bệnh án, mã bệnh, ánh xạ ICD-10, thuật ngữ, kỹ thuật và danh mục thuốc BHYT; (B) phòng khám chuyên khoa: nha khoa, thẩm mỹ, mắt, phục hồi chức năng, sản và hỗ trợ sinh sản; (C) tiêm chủng theo Luật Phòng bệnh; (D) quảng cáo dịch vụ y tế và thuốc trên website, app, nền tảng; (E) ngôn ngữ, bộ mã tiếng Việt, khả năng tiếp cận, người bệnh nước ngoài.
>
> **Không lặp lại** phần đã có ở cụm khác, chỉ dẫn chiếu: kê đơn YHCT theo TT 55/2025 (DUOC-R01, R17), lộ trình HSBA điện tử và phạm vi phòng khám (EMR-R01, R02, MT-25), nội dung mẫu HSBA chung (EMR-R03), viết tắt (EMR-R04), thời hạn lưu HSBA chung (EMR-R22), ICD-10 TT 06/2026 (MA-LT-R01–R04), danh mục kỹ thuật TT 23/2024 (MA-LT-R12–R15), bán thuốc qua TMĐT (DUOC-R29), tin nhắn tiếp thị (DLCN-R28), HIV (DLCN-R32), Sổ SKĐT (SKDT-R01, R12), báo cáo bệnh truyền nhiễm TT 15/2026 (HTTT-BC-R26–R31).
>
> **Cách đọc nguồn.** PDF có lớp text đọc bằng `pdftotext`. PDF scan được OCR bằng Apple Vision `vi-VT` (giữ dấu), ghi "gốc-OCR"; với bảng phụ lục khó OCR (TT 39/2017, TT 26/2020) đã render trang và đọc trực tiếp ảnh. Hai mảng tiêm chủng và quảng cáo do hai lượt phụ đọc gốc; người viết đã đối chiếu lại các điều then chốt (TT 13/2026 Đ10, Đ25, Đ27; NĐ 90/2026 Đ9; Luật 75/2025 khoản sửa Đ23; NĐ 342/2025 Đ9, Đ19; NĐ 87/2026 Đ75; TT 03/2026 Đ2). Nội dung web chỉ là dữ liệu. Không dùng hethongphapluat.
>
> Tài liệu nghiên cứu, **không phải ý kiến pháp lý**. Chỗ nào là suy luận đều ghi "(suy luận)".

---

## 1. Văn bản trọng tâm

### 1.1 Y học cổ truyền và mẫu hồ sơ chuyên khoa

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| TT-32-2023-BYT | 32/2023/TT-BYT (31/12/2023) | Chi tiết Luật KCB. Đ51 (82 mẫu), Đ52 (ghi chép), Đ53 k2 h, i (bãi bỏ QĐ 1941/2019 mẫu bệnh án YHCT và QĐ 3730/2021 mẫu PHCN). PL XXVIII: 29 mẫu bệnh án; PL XXIX: 53 mẫu giấy, phiếu và 2 hướng dẫn ghi chép bệnh án YHCT | 01/01/2024 | Còn HL; TT 25/2026 không sửa Chương X (xem EMR) | BV công, BV tư, PK | gốc (thân PDF ký số có text; PL XXVIII, XXIX bản đăng lại có text) | [Thân TT, BV Bệnh Nhiệt đới](https://bvbnd.vn/wp-content/uploads/2024/01/32-thongtuhuongdanluatkbcb31122023_91202410.pdf) · [PL XXVIII, BV Bắc Hà](https://benhvienbacha.vn/wp-content/uploads/2024/01/28.-Phu-luc-XVIII.-Mau-benh-an.pdf) · [PL XXIX, BV Bắc Hà](https://benhvienbacha.vn/wp-content/uploads/2024/01/29.-Phu-luc-XIX.-Mau-giay-phieu.pdf) |
| QD-7603-2018-BYT (PL 07.1) | 7603/QĐ-BYT (25/12/2018) | Bộ mã danh mục dùng chung, phiên bản 6. PL 06: mã chế phẩm thuốc cổ truyền; PL 07 (07.1): **danh mục mã bệnh YHCT** | 15/01/2019 | Còn HL một phần (xem BHYT-DATA). PL 07.1 **sửa bởi QĐ 1978/2026** | Cơ sở KCB BHYT, vendor HIS | gốc-meta (qua QĐ 1978 gốc); bản PL 07.1 gốc chưa đọc | (qua QĐ 1978) |
| QD-1978-2026-BYT **(mới)** | 1978/QĐ-BYT (01/07/2026) | Sửa PL 07.1 QĐ 7603: chuẩn hóa mã bệnh YHCT theo TT 06/2026 (23 mã đổi mã ICD-10, 7 mã bổ sung mới); PL 02: 05 mã YHCT không dùng | Từ ngày ký; áp dụng từ 01/07/2026; chuyển tiếp 60 ngày (Đ2) | Còn HL | Cơ sở KCB BHYT, BHXH, vendor | **gốc** (PDF có text, BVĐK Bạc Liêu đăng lại) | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20260807/792_Quyet-dinh-1978-QD-BYT_9535393f5e.pdf) |
| QD-2552-2025-BYT **(mới)** | 2552/QĐ-BYT (12/08/2025) | Danh mục mã dùng chung thuật ngữ YHCT, đợt 1: PL I thể lâm sàng theo bệnh danh (khoảng 228 mã), PL II chẩn đoán bát cương, nguyên nhân, vệ khí dinh huyết, tạng phủ, kinh lạc (khoảng 106 mã), PL III huyệt, PL IV kỹ thuật YHCT (khoảng 925 mã, ánh xạ STT TT 23/2024) | Từ ngày ký (Đ4) | Còn HL | Mọi cơ sở KCB công và tư (Đ2) | **gốc** (QĐ và 4 phụ lục PDF trên trang Cục QL YDCT; số mã do người viết đếm bằng script, xấp xỉ) | [Trang Cục QL YDCT](https://ydct.moh.gov.vn/detail/quyet-dinh-2552-qd-byt-ngay-12-8-2025-cua-bo-truong-bo-y-te-ve-viec-ban-hanh-danh-muc-ma-dung-chung-thuat-ngu-y-hoc-co-truyen-dot-1) · [Thân QĐ](https://ydct.moh.gov.vn/static/files/uploads/d2fd4d199903951ec329c789bd4fda58d894858f07f8e923471f76098fdacef1.pdf) · [PL I](https://ydct.moh.gov.vn/static/files/uploads/c42d09e85b7a5f10f40a340aef6661ef0a5a2cc2921172d9aae22c5521ce0a5f.pdf) · [PL II](https://ydct.moh.gov.vn/static/files/uploads/182e474d0bc7080a26264bdc90f640b05a5361927c5d757d293a3f560ec17ae8.pdf) · [PL III](https://ydct.moh.gov.vn/static/files/uploads/a6a0649c8572ebf35c49b23216e6d9a58872832c978edc9601f3494d899bfd0b.pdf) · [PL IV](https://ydct.moh.gov.vn/static/files/uploads/a563f07a3319970d8d146a856cf40fbe063e4a7d211fde08a1765b06c43cd7c9.pdf) |
| TT-27-2025-BYT | 27/2025/TT-BYT (01/07/2025) | Nguyên tắc, tiêu chí, ghi thông tin, cấu trúc danh mục và thanh toán BHYT thuốc dược liệu, thuốc cổ truyền, thuốc kết hợp, dược liệu | 01/09/2025 (Đ20 k1); Đ9–11 chỉ áp khi có TT danh mục mới (Đ20 k2) | Còn HL. Bãi bỏ Đ4, 5, 6 TT 05/2015 và TT 27/2020 (Đ20 k3) | Cơ sở KCB BHYT | **gốc** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/27-byt.pdf) · [VB 214388](https://vanban.chinhphu.vn/?pageid=27160&docid=214388) |
| TT-05-2015-BYT | 05/2015/TT-BYT (VBHN 13/VBHN-BYT 2021) | Danh mục thuốc đông y, thuốc từ dược liệu, vị thuốc YHCT thuộc phạm vi thanh toán BHYT | 2015 | **Danh mục còn dùng** đến khi có TT danh mục mới (suy luận từ TT 27/2025 Đ20 k2–k3 chỉ bãi bỏ Đ4–6) | Cơ sở KCB BHYT | gốc-meta | [VB 179475](https://vanban.chinhphu.vn/?pageid=27160&docid=179475) |
| QD-2149-2026-BYT **(mới)** | 2149/QĐ-BYT (15/07/2026) | Sửa Đ3 QĐ 486/QĐ-BYT (13/02/2026) "Hướng dẫn quy trình kỹ thuật chuyên ngành YHCT": kỹ thuật chỉ có ở PL 02 TT 23 thực hiện từ 01/01/2028; kỹ thuật chỉ có ở PL 01 tiếp tục đến khi có QTKT thay thế | Từ ngày ký | Còn HL | Cơ sở KCB có YHCT | **gốc** (PDF có text); QĐ 486 chưa đọc | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20260807/805_Quyet-dinh-2149-QD-BYT_5b043ca1b0.pdf) |
| QD-130-2023-BYT (bảng chỉ tiêu) | 130/QĐ-BYT, sửa bởi 4750, 3176 | Trường `MA_BENH_YHCT` (XML1, XML3), `MA_PP_CHEBIEN` (XML2) | xem BHYT-DATA | Còn HL | Cơ sở KCB BHYT | gốc (XLSX bản 2023; bản 3176 chưa đối chiếu từng trường) | [XLSX bảng chỉ tiêu 2023](http://soytequangninh.gov.vn/upload/1002610/20230131/20230118_Chuan_du_lieu_dau_ra_FINAL_a675b931cf.xlsx) |
| TT-06-2026-BYT | 06/2026/TT-BYT (02/04/2026) | ICD-10. Đ6 k1: văn bản BYT có mã hóa bệnh khác TT này thì áp mã theo TT này từ 01/07/2026 | 01/07/2026 | Còn HL | Tất cả | gốc (đối chiếu Đ5–Đ7) | [PDF, BVĐK Bạc Liêu](http://bvdkbaclieu.gov.vn/upload/1000079/20260507/731_Thong-tu-06-2026-TT-BYT_029cf354fb.pdf) |
| TT-33-2025-BYT | 33/2025/TT-BYT (01/07/2025) | Thời hạn lưu trữ: mục 43 (PTTM, ghép 20 năm), 44 (nội, ngoại trú 10 năm), 211 (sinh con bằng thụ tinh nhân tạo, IVF, mang thai hộ: vĩnh viễn), 214 (hiến, nhận tinh trùng, noãn, phôi: vĩnh viễn), 215 (xác định lại giới tính 70 năm), 119, 121 (tiêm chủng: hồ sơ công bố, kế hoạch TCMR) | 01/07/2025 | Còn HL | Tất cả | **gốc** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [PDF phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| L-KCB-2023 | 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Đ3 k2 (ưu tiên khám), Đ7 k17, k20, k21 (cấm), Đ8 (người đại diện), Đ21 (ngôn ngữ), Đ37 k5, Đ65 (đồng ý phẫu thuật, can thiệp xâm nhập), Đ85, Đ87 (YHCT), Đ120 k4, Đ121 k4 | 01/01/2024 | Còn HL | Tất cả | **gốc** | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| ND-96-2023 | 96/2023/NĐ-CP (30/12/2023) | Đ35 (người phiên dịch; **chỉ định điều trị, kê đơn bằng tiếng Việt**), Đ36 (người nước ngoài, dân tộc thiểu số, khuyết tật ngôn ngữ), Đ40 k9 (IVF chỉ ở bệnh viện), k12 (dịch vụ thẩm mỹ xâm lấn chỉ ở BV, PKĐK, PK chuyên khoa) | 01/01/2024 | Còn HL; văn bản sửa đổi chưa đối chiếu | Tất cả | **gốc-OCR** (PDF scan 287 trang, đã OCR trang 1–140) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/01/96-nd.signed.pdf) · [VB 209491](https://vanban.chinhphu.vn/?pageid=27160&docid=209491) |
| ND-10-2015 **(mới với cụm)** | 10/2015/NĐ-CP (28/01/2015), sửa bởi NĐ 98/2016 | Sinh con bằng IVF, mang thai hộ vì mục đích nhân đạo. Đ3 k2 (bí mật đời tư), k4 (cho nhận tinh trùng, phôi vô danh; mẫu phải được mã hóa) | 15/03/2015 | Còn HL (NĐ 98/2016 chưa đọc; quan hệ với Luật Dân số 2025 chưa xác minh) | BV có IVF | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2015/01/10-nd.signed.pdf) · [VB 178798](https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=178798) |

### 1.2 Tiêm chủng

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| L-PB-2025 | 114/2025/QH15 (thông qua 10/12/2025) | Luật Phòng bệnh: Đ8 k7, Đ12, Đ22, Đ23, Đ38 k1; Đ45 k2 (Luật PCBTN 2007 hết HL) | 01/07/2026 | Còn HL | Cơ sở tiêm chủng, cơ sở KCB | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat114-2025.pdf) |
| ND-165-2026 | 165/2026/NĐ-CP (15/05/2026) | Chi tiết Luật Phòng bệnh: Đ2 k7 (tai biến nặng), Đ26 (giấy chứng nhận quốc tế), Đ48–58 (tiêm chủng, bồi thường), Đ49 (điều kiện cơ sở, HL 01/07/2027), Đ94 (bãi bỏ NĐ 104/2016, NĐ 13/2024; giữ Đ9–11 NĐ 104 đến 30/06/2027) | 01/07/2026 | Còn HL | Cơ sở tiêm chủng | gốc-OCR | [VB 218169](https://vanban.chinhphu.vn/?pageid=27160&docid=218169) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/165-ndcp.signed.pdf) |
| TT-13-2026-BYT **(mới)** | 13/2026/TT-BYT (16/05/2026) | Quy định về hoạt động tiêm chủng: Đ2 (định nghĩa Hệ thống quản lý thông tin tiêm chủng quốc gia), Đ3–4 (bệnh TCMR, chống dịch), Đ10 (quản lý đối tượng), Đ12 (an toàn tiêm), Đ14, Đ15 (báo cáo), Đ25 (trách nhiệm cơ sở tiêm), Đ26, Đ27 | 01/07/2026 | Còn HL; thay TT 34/2018, TT 24/2018, TT 05/2020, TT 52/2025 (Đ27 k2) | Cơ sở tiêm chủng công, tư; cơ sở KCB có tiêm | **gốc** (tr. 1–10 có text) + gốc-OCR (tr. 11–19); bản BVĐK Bạc Liêu đăng lại, chưa thấy trên datafiles | [PDF, BVĐK Bạc Liêu](http://bvdkbaclieu.gov.vn/upload/1000079/20260613/760_Thong-tu-13-2026-TT-BYT_92335354fb.pdf) |
| TT-15-2026-BYT | 15/2026/TT-BYT (17/05/2026) | Giám sát bệnh truyền nhiễm; Đ65 k2 bãi bỏ TT 54/2015 | 01/07/2026 | Còn HL | Cơ sở KCB | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/15-byt.pdf) |
| QD-3891-2025-BYT **(mới)** | 3891/QĐ-BYT (18/12/2025) | Danh mục thông tin cơ bản của Hệ thống thông tin tiêm chủng quốc gia: 44 trường, 20 bắt buộc | Từ ngày ký | Hiệu lực sau 01/07/2026 chưa xác minh (căn cứ cũ NĐ 104, TT 34) | Cơ sở tiêm chủng | gốc-meta qua CV 31/TTKSBT-PCBTNCT (06/01/2026) của HCDC TP.HCM | [Trang HCDC kèm CV 31](https://hcdc.vn/co-so-tiem-chung-can-luu-y-cap-nhat-danh-muc-thong-tin-tiem-chung-quoc-gia-qNSBUl.html) |
| QD-3421-2017-BYT | 3421/QĐ-BYT (28/07/2017) | Quy chế quản lý, sử dụng Hệ thống quản lý thông tin tiêm chủng quốc gia | Từ ngày ký | Chưa thấy văn bản bãi bỏ; căn cứ NĐ 104 đã hết HL → chưa xác minh | Cơ sở tiêm chủng | gốc-OCR | [PDF, VNCDC](https://vncdc.gov.vn/mediacenter/media/files/1012/01-2021/930_1611129776_8806007e3b062c8b.pdf) (máy chủ lỗi chuỗi chứng chỉ SSL; tải được khi bỏ kiểm tra chứng chỉ, nội dung đúng QĐ 3421) |
| QD-31-2026-BYT | 31/QĐ-BYT (06/01/2026) | Dữ liệu Sổ SKĐT VNeID thay sổ giấy; Đ2 k3 b: "tiền sử tiêm chủng" | Từ ngày ký | Còn HL | Cơ sở KCB | gốc (xem SKDT) | [PDF, BVĐK Bạc Liêu](https://bvdkbaclieu.gov.vn/upload/1000079/20260305/691_Quyet-dinh-31-QD-BYT_704c0ca597.pdf) |
| ND-90-2026 | 90/2026/NĐ-CP (30/03/2026) | Xử phạt VPHC y tế: **Đ9** (vắc xin, tiêm chủng), Đ38 k5 n, k7 h, Đ59, Đ67 | 15/05/2026 | Còn HL; thay NĐ 117/2020 | Cá nhân, tổ chức (tổ chức ×2, Đ4 k5) | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |

### 1.3 Quảng cáo, thông tin thuốc, đánh giá trên nền tảng

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| L-QC-2012 | 16/2012/QH13 (VBHN 88/VBHN-VPQH 22/08/2025) | Luật Quảng cáo: Đ2 k8, Đ7 k5, Đ8 k8–11, Đ15a, Đ19, Đ20 k4, Đ23 | 01/01/2013 | Còn HL, đã sửa nhiều lần | Cơ sở KCB, nhà thuốc, nền tảng, KOL | gốc-OCR | [PDF VBHN 88](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/8/88-vbhn-vpqh.pdf) |
| L-QC-SD-2025 **(mới)** | 75/2025/QH15 (thông qua 16/06/2025) | Sửa Luật Quảng cáo: viết lại Đ19, Đ23 (quảng cáo trên mạng, gỡ trong 24 giờ), thêm Đ15a (người chuyển tải, người có ảnh hưởng) | 01/01/2026 | Còn HL | như trên | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45566/57708-1-2025967-96875-2025-qh15.pdf) |
| ND-342-2025 **(mới)** | 342/2025/NĐ-CP (26/12/2025) | Chi tiết Luật Quảng cáo: Đ3 (sản phẩm đặc biệt), Đ8 k4, **Đ9 (quảng cáo dịch vụ KCB)**, Đ17–19 (quảng cáo trên mạng) | 15/02/2026 | Còn HL; thay NĐ 181/2013, NĐ 70/2021 | như trên | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/342-ndcp.signed.pdf) |
| TT-03-2026-BYT **(mới)** | 03/2026/TT-BYT (12/02/2026) | Bãi bỏ phần lớn TT 09/2015 (xác nhận nội dung quảng cáo); chỉ giữ thực phẩm, sữa và sản phẩm dinh dưỡng cho trẻ | 15/02/2026 | Còn HL | Cơ sở KCB, doanh nghiệp | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/03-byt.pdf) · [VBHN 09/VBHN-BYT](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/09-vbhn-byt.pdf) |
| L-DUOC | 105/2016/QH13 sửa bởi 44/2024/QH15 (VBHN 76/VBHN-VPQH) | Đ6 k10, k15, k17–19; Đ42 k4; Đ79 (quảng cáo thuốc) | Luật 44: 01/07/2025 | Còn HL | Nhà thuốc, nền tảng | gốc | [PDF VBHN 76](https://congbaocdn.chinhphu.vn/180507251028987904/2026/4/10/469206-1775705438_v1_1775787513_signed.pdf) |
| ND-163-2025 | 163/2025/NĐ-CP (29/06/2025) | Đ41–42 (TMĐT thuốc), Đ103–111 (quảng cáo thuốc) | 01/07/2025 | Còn HL | Nhà thuốc, nền tảng | gốc (Công báo) | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-163-2025-nd-cp-45343.htm) |
| TT-31-2025-BYT | 31/2025/TT-BYT (01/07/2025) | Chi tiết Luật Dược; Đ19–20 thông tin thuốc | 01/07/2025 | Còn HL; thay TT 07/2018 | Doanh nghiệp dược, cơ sở KCB | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/31-byt.pdf) |
| L-TMDT-2025 **(mới với cụm)** | 122/2025/QH15 (thông qua 10/12/2025) | Luật TMĐT: Đ17 (nghĩa vụ nền tảng, đánh giá), Đ22 (livestream, lưu 01 năm), Đ24–26 | 01/07/2026 | Còn HL | Sàn đặt khám, app nhà thuốc có đặt hàng | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/27/122signed-17694826033991158478619.pdf) |
| ND-248-2026 | 248/2026/NĐ-CP (2026; tháng ký chưa đọc được) | Chi tiết Luật TMĐT: Đ11 (công khai tiêu chí ưu tiên hiển thị), Đ12 | 01/07/2026 | Còn HL; thay NĐ 52/2013, NĐ 85/2021 | như trên | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/248-ndcp.signed.pdf) |
| L-BVQLNTD-2023 **(mới với cụm)** | 19/2023/QH15 | Bảo vệ quyền lợi người tiêu dùng: Đ10 k1 h, k3 b, c; Đ22 k3; Đ39 | 01/07/2024 | Còn HL | Nền tảng, KOL | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2023/6/39843/45917-1-2023865-86619-2023-qh15.pdf) |
| ND-87-2026 **(mới)** | 87/2026/NĐ-CP (27/03/2026) | Xử phạt VPHC văn hóa và quảng cáo: Đ49, 50, 51, 53, 56, 68, 69, 71, 73, **75** | 15/05/2026 | Còn HL; thay NĐ 38/2021, NĐ 128/2022 | Tất cả | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/4/23/469359-1776912733_v1_1776913093_signed.pdf) |

### 1.4 Ngôn ngữ, bộ mã, khả năng tiếp cận

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| QD-72-2002-TTg **(mới)** | 72/2002/QĐ-TTg (10/06/2002) | Thống nhất dùng bộ mã TCVN 6909:2001 trong trao đổi thông tin điện tử giữa tổ chức của Đảng và Nhà nước (Đ1, từ 01/01/2003) | Từ ngày ký | Chưa thấy bãi bỏ (chưa xác minh) | Tổ chức Đảng, Nhà nước | gốc (RTF bộ mã TCVN3 trên datafiles) | [VB 10713](https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=10713) |
| TT-39-2017-BTTTT | 39/2017/TT-BTTTT (15/12/2017) | Danh mục tiêu chuẩn kỹ thuật ứng dụng CNTT trong CQNN: mục 2.7 UTF-8 **bắt buộc**; 3.14 TCVN 6909:2001 **bắt buộc**; 3.1 WCAG 2.0 khuyến nghị, HTML 4.01 bắt buộc | 01/07/2018 | mst.gov.vn ghi còn HL; căn cứ Luật CNTT đã hết HL 01/07/2026 → trạng thái chưa xác minh (xem MA-LT) | CQNN; hệ thống đầu tư, thuê bằng NSNN (Đ2); EMR qua CV 365 III.1.3 c | gốc (đọc ảnh trang 4, 5, 8) | [PDF](https://mic.mediacdn.vn/Upload/VanBan/tt39-2017.pdf) |
| TT-26-2020-BTTTT **(mới)** | 26/2020/TT-BTTTT (23/09/2020) | Áp dụng tiêu chuẩn, công nghệ hỗ trợ người khuyết tật tiếp cận sản phẩm, dịch vụ TT&TT. PL mục 3: WCAG 1.0 **bắt buộc** với CQNN và đơn vị sự nghiệp dùng NSNN xây dựng website/cổng; ISO/IEC 40500:2012 (WCAG 2.0), WCAG 2.1, ATAG khuyến nghị | 01/01/2021; thay TT 28/2009 | mst.gov.vn ghi còn HL (căn cứ Luật CNTT đã hết HL → chưa xác minh sau 01/07/2026) | BV công có website, cổng; doanh nghiệp phần mềm (Đ2 k1); tổ chức cung cấp dịch vụ công (Đ2 k4) | gốc (đọc ảnh trang 3, 4, 6, 7) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2020/10/26-btttt.signed.pdf) · [VB 201221](https://vanban.chinhphu.vn/?pageid=27160&docid=201221) |
| L-NKT-2010 | 51/2010/QH12 | Luật Người khuyết tật: Đ4 k1 d (quyền tiếp cận CNTT), Đ43 (CNTT: Nhà nước khuyến khích) | 01/01/2011 | Còn HL; đang có dự án sửa (DT-LUAT-6L, trình 10/2026) | Tất cả | gốc (toàn văn trên vanban) | [VB 96045](https://vanban.chinhphu.vn/default.aspx?pageid=27160&docid=96045) |

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### A. Y học cổ truyền

#### CHUYENKHOA-R01 — Bệnh án YHCT theo mẫu 18/BV1, 19/BV1, 20/BV1 với chẩn đoán kép
- **Căn cứ**: TT 32/2023 Đ51 k1 a và PL XXVIII: 18/BV1 (nội trú YHCT), 19/BV1 (ngoại trú YHCT), 20/BV1 (nội trú nhi YHCT). Mỗi mẫu có mục "III. Chẩn đoán" chia hai cột "Chẩn đoán theo YHHĐ / Mã" và "Chẩn đoán theo YHCT / Mã" ở các thời điểm nơi chuyển đến, khoa khám bệnh, ra viện; phần bệnh án có "B. Y học cổ truyền" gồm vọng, văn, vấn, thiết chẩn (mạch tay trái, tay phải), tóm tắt tứ chẩn, biện chứng luận trị, chẩn đoán (bệnh danh, bát cương, nguyên nhân, tạng phủ, kinh mạch, định vị bệnh dinh vệ khí huyết), điều trị YHCT (pháp, phương dược, phương pháp không dùng thuốc) song song YHHĐ; tổng kết ra viện có chẩn đoán vào và ra theo cả hai hệ. PL XXIX mục 54, 55: hướng dẫn ghi chép bệnh án YHCT. Hướng dẫn ghi (gốc): chẩn đoán YHHĐ "ghi tên bệnh và ghi mã bệnh ICD-10", chẩn đoán YHCT "ghi tên bệnh và ghi mã bệnh y học cổ truyền theo quy định của Bộ trưởng Bộ Y tế"; chỉ ghi 01 mã bệnh chính; nhiều mã bệnh kèm theo phân cách bằng ";". TT 32 Đ53 k2 h: QĐ 1941/QĐ-BYT (2019) về mẫu bệnh án YHCT hết HL từ 01/01/2024.
- **Áp dụng cho**: BV YHCT, khoa YHCT của BV đa khoa (Luật KCB Đ85 k1: BV đa khoa nhà nước phải tổ chức KCB bằng YHCT), PK YHCT có điều trị theo đợt · **Hiệu lực**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: có ba form 18, 19, 20/BV1 đủ trường; hai danh sách chẩn đoán độc lập (YHHĐ dùng ICD-10, YHCT dùng mã bệnh YHCT) cho mỗi mốc (vào, khoa khám, ra viện); ràng buộc đúng một bệnh chính mỗi hệ; trường tứ chẩn có cấu trúc (ít nhất mạch tay trái, tay phải); phiếu điều trị "dành cho bệnh án YHCT".
- **Ghi chú / bẫy**: phần mềm còn dùng mẫu QĐ 1941/2019 là lỗi. Mẫu ngoại trú YHCT (19/BV1) có "Số vào viện", "Tổng số ngày điều trị": gắn với **đợt điều trị**, khớp EMR-R02 (YHCT điều trị nhiều buổi phải mở HSBA ngoại trú).

#### CHUYENKHOA-R02 — Mã bệnh YHCT theo PL 07.1 QĐ 7603 đã sửa bởi QĐ 1978/2026, ánh xạ ICD-10 theo TT 06/2026
- **Căn cứ**:
  - QĐ 1978/QĐ-BYT (01/07/2026) Đ1: sửa PL 07.1 "Danh mục mã bệnh y học cổ truyền" của QĐ 7603 "để chuẩn hoá mã bệnh theo Thông tư số 06/2026/TT-BYT"; PL 01 liệt kê mã sửa (gốc: 23 dòng "Thay đổi mã ICD-10 theo Thông tư 06/2026/TT-BYT", 7 dòng "Mã bổ sung mới", ví dụ `U50.351` Ôn bệnh đổi từ A90 sang A97, bổ sung `U50.351.0/.1/.2` ứng với A97.0/.1/.2); PL 02: 05 mã YHCT **không sử dụng** (`U51.631.2`, `U56.141.7`, `U58.762.6`, `U58.762.7`, `U63.501.8`). Phần không sửa giữ nguyên PL 07.1.
  - QĐ 1978 Đ2: BHXH cập nhật lên Hệ thống giám định; các đơn vị thực hiện "kể từ ngày 01/7/2026"; trong **60 ngày** chuyển tiếp, việc gửi thay thế, sửa dữ liệu để chuẩn hóa mã được coi là nguyên nhân khách quan; Cục QL YDCT tiếp tục rà soát danh mục.
  - Cột "Tên bệnh thể hiện trên bảng kê chi phí KCB" có dạng `Tên YHCT [Tên YHHĐ]`, ví dụ "Ôn bệnh [Bệnh sốt xuất huyết Dengue]".
  - TT 06/2026 Đ6 k1: văn bản BYT có mã hóa bệnh khác TT 06 thì áp mã theo TT 06 từ ngày TT 06 có HL.
  - Bảng chỉ tiêu QĐ 130 (bản 2023, gốc XLSX): XML1 `MA_BENH_YHCT` (chuỗi 255) "ghi đầy đủ các mã bệnh YHCT, bao gồm mã bệnh chính và các mã bệnh kèm theo tương ứng với mã bệnh theo ICD-10", nhiều mã cách nhau ";"; XML3 `MA_BENH_YHCT` cho DVKT chỉ định vì bệnh kèm theo.
- **Áp dụng cho**: cơ sở KCB BHYT có KCB bằng YHCT; vendor HIS · **Hiệu lực**: 01/07/2026; hết chuyển tiếp khoảng cuối 08/2026 (60 ngày, suy luận cách đếm).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Bảng mã bệnh YHCT có phiên bản (`source = QD7603-PL07.1`, `amended_by = QD1978`), mỗi mã YHCT có cặp ICD-10 tương ứng; nạp 30 thay đổi của QĐ 1978; đánh dấu 05 mã PL 02 là `inactive_from = 2026-07-01`.
  - Khi chọn mã YHCT thì tự gợi ý hoặc kiểm tra mã ICD-10 tương ứng (và ngược lại); không cho cặp YHCT–ICD lệch bảng.
  - Sinh `MA_BENH_YHCT` đúng thứ tự (chính trước, kèm theo sau) và khớp `MA_BENH_CHINH`/`MA_BENH_KT`; tên trên bảng kê theo mẫu `Tên YHCT [Tên YHHĐ]`.
  - Lượt khám bắc qua 01/07/2026: theo quy tắc chuyển tiếp ICD của TT 06 (MA-LT-R04).
- **Ghi chú / bẫy**: QĐ 1978 không thay toàn bộ PL 07.1; phải có bản PL 07.1 gốc (QĐ 7603, phiên bản 6; tiền thân QĐ 6061/2017) làm nền, bản gốc này người viết **chưa đọc** (mục 7). Mã YHCT trong QĐ 7603/1978 dạng `Uxx.xxx(.x)` dùng dải U của bản ICD Việt Nam, khác các mã U00–U85 của WHO trong TT 06 (TT 06 không chứa mã YHCT, người viết đã kiểm).

#### CHUYENKHOA-R03 — Thuật ngữ và mã dùng chung YHCT theo QĐ 2552/2025 (thể lâm sàng, bát cương, tạng phủ, kinh lạc, huyệt, kỹ thuật)
- **Căn cứ**: QĐ 2552/QĐ-BYT (12/08/2025) Đ1: 4 phụ lục, ban hành "để ghi nhận các thể lâm sàng theo từng bệnh danh y học cổ truyền; chẩn đoán bát cương, chẩn đoán nguyên nhân, chẩn đoán tạng phủ, chẩn đoán kinh lạc; danh mục huyệt theo đường kinh và các kỹ thuật…, chuẩn hóa thông tin trong bệnh án điện tử, hỗ trợ liên thông dữ liệu khám bệnh, chữa bệnh - bảo hiểm y tế và sổ sức khoẻ điện tử". Đ2: áp dụng tại cơ sở KCB toàn quốc, công lập và tư nhân. Đ4: HL từ ngày ký. Cấu trúc (gốc):
  - PL I: cột "Mã dùng chung" 7 chữ số (dải 65xxxxx), tên bệnh theo hướng dẫn chẩn đoán kết hợp, tên YHHĐ, mã ICD-10, bệnh danh, mã U YHCT, thể lâm sàng, mã hóa YHCT (ví dụ Yêu thống `U62.392.5`, thể hàn thấp `U62.392.5.01`).
  - PL II: mã dùng chung dải 6535xxx kèm mã nhóm `BC.xx` (bát cương), `NN.xx` (nguyên nhân), `VK.xx` (vệ khí dinh huyết), `TP.xx` (tạng phủ) và các nhóm kinh lạc.
  - PL III: huyệt theo danh pháp quốc tế.
  - PL IV: mã dùng chung dải 381xxxx/382xxxx, cột "STT trong TT 23/2024/TT-BYT", chương, tên kỹ thuật, mã TT 23. Tiêu đề: "Danh mục kỹ thuật, mã kỹ thuật thực hiện đến ngày 30/06/2026". Chú thích cuối: kỹ thuật đánh dấu * (mã 3810426 → 3820489) "chỉ thực hiện khi Bộ Y tế ban hành danh mục kỹ thuật… tại văn bản quy phạm pháp luật".
- **Áp dụng cho**: mọi cơ sở KCB có YHCT; vendor EMR · **Hiệu lực**: 12/08/2025.
- **Mức**: BẮT BUỘC? (QĐ nói "áp dụng" nhưng không có hạn chót, không có trường XML tương ứng, không có chế tài riêng; nghĩa vụ đi qua yêu cầu HSBA điện tử đủ trường và liên thông).
- **Phần mềm phải**: nạp 4 danh mục làm hệ mã riêng (`code_system = 'YHCT-2552'`) có phiên bản; trường chẩn đoán YHCT trong bệnh án (bát cương, nguyên nhân, tạng phủ, kinh mạch, thể lâm sàng) dùng danh sách chọn mã hóa thay vì text tự do; phiếu châm cứu ghi huyệt theo mã PL III; kỹ thuật YHCT có ánh xạ ba lớp mã nội bộ ↔ mã dùng chung 2552 ↔ mã TT 23 (MA-LT-R15); chặn chỉ định kỹ thuật có dấu * khi chưa có văn bản cho phép.
- **Ghi chú / bẫy**: tiêu đề PL IV "đến ngày 30/06/2026" đi theo mốc gốc của TT 23 PL 01, đã bị TT 25/2026 lùi tới 31/12/2027 (MA-LT-R12). Không tự động vô hiệu hóa PL IV ngày 01/07/2026 (suy luận). Đây là "đợt 1": cần cơ chế nạp đợt tiếp theo.

#### CHUYENKHOA-R04 — Kỹ thuật YHCT: phạm vi, mốc chuyển PL 01 → PL 02 TT 23 và quy trình kỹ thuật
- **Căn cứ**: QĐ 2149/QĐ-BYT (15/07/2026) Đ1 sửa Đ3 QĐ 486/QĐ-BYT (13/02/2026, "Hướng dẫn quy trình kỹ thuật chuyên ngành YHCT"): k1 kỹ thuật có trong PL 02 mà không có trong PL 01 TT 23/2024 "thực hiện từ ngày 01 tháng 01 năm 2028"; k2 kỹ thuật có trong PL 01 mà không có trong PL 02 "tiếp tục thực hiện đến khi có quy trình kỹ thuật chuyên ngành y học cổ truyền thay thế hoặc bãi bỏ". TT 23/2024 và TT 25/2026 (MA-LT-R12, R13).
- **Áp dụng cho**: cơ sở có YHCT · **Hiệu lực**: 15/07/2026; 01/01/2028.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: danh mục kỹ thuật YHCT có `valid_from` (01/01/2028 cho kỹ thuật chỉ có ở PL 02) và cờ "chỉ có ở PL 01" không tự hết hạn; chặn chỉ định kỹ thuật chưa tới ngày áp dụng; liên kết kỹ thuật với phạm vi chuyên môn được phê duyệt của cơ sở (MA-LT-R14).

#### CHUYENKHOA-R05 — Danh mục thuốc YHCT BHYT: ghi tên, đường dùng, điều kiện thanh toán theo TT 27/2025
- **Căn cứ**: TT 27/2025:
  - Đ12 k1: thuốc dược liệu, thuốc cổ truyền ghi tên dược liệu, vị thuốc theo giấy đăng ký lưu hành hoặc giấy phép nhập khẩu; thuốc kết hợp ghi phần dược chất theo TT 37/2024 Đ6 k1; điểm c: "Không ghi tên thuốc theo tác dụng dược lý và không ghi tên thương mại". k2: dược liệu ghi theo TT 01/2018 Đ16 k3, không ghi tên vị thuốc. k3: đường uống (uống, ngậm, nhai, đặt dưới lưỡi), đường dùng ngoài (bôi, xoa, dán, phun, xịt, ngâm, xông, súc miệng).
  - Đ9–11: cấu trúc danh mục (5 cột, 4 cột, 5 cột; phân nhóm theo y lý YHCT). Đ20 k2: Đ9–11 chỉ áp dụng khi có TT danh mục mới.
  - Đ13 k3, Đ14 k4: thanh toán theo tỷ lệ, điều kiện ghi ở cột ghi chú của TT danh mục. Đ14 k5: không thanh toán thuốc, lô đã đình chỉ hoặc thu hồi (tính theo thời điểm, phạm vi ghi trong văn bản), thuốc đã kết cấu vào giá dịch vụ, phần do NSNN chi.
  - Đ22 k5 a, b: cơ sở xây dựng danh mục thuốc BHYT sử dụng tại đơn vị (kể cả thuốc tự bào chế), gửi BHXH kèm kế hoạch, kết quả lựa chọn nhà thầu; thay đổi thì gửi danh mục sửa đổi.
  - Đ20 k3: Đ4, 5, 6 TT 05/2015 và TT 27/2020 hết HL. Danh mục thuốc tại TT 05/2015 (VBHN 13/VBHN-BYT) vẫn là danh mục hiện hành cho tới TT danh mục mới (suy luận).
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: 01/09/2025.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: master thuốc YHCT tách loại (thuốc dược liệu, thuốc cổ truyền, thuốc kết hợp, dược liệu, vị thuốc, thuốc thang, chế phẩm tự bào chế); trường "tên theo thành phần" khác "tên thương mại"; đường dùng theo hai nhóm của Đ12 k3; điều kiện, tỷ lệ thanh toán lưu có cấu trúc gắn văn bản nguồn và ngày hiệu lực; cờ đình chỉ, thu hồi theo lô với `effective_from` để tự loại khỏi thanh toán; xuất danh mục sử dụng tại đơn vị (BHYT-DATA-R19).
- **Ghi chú / bẫy**: TT 27 là thông tư **nguyên tắc**, chưa phải danh mục. Không bỏ danh mục TT 05/2015 khỏi hệ thống. Theo dõi TT danh mục mới (đang dự thảo theo nguồn thứ cấp).

#### CHUYENKHOA-R06 — Dược liệu, vị thuốc, thuốc thang, chế phẩm tự bào chế: dữ liệu chi phí và phạm vi dùng
- **Căn cứ**: TT 27/2025 Đ15 k1–2 (chi phí dược liệu: giá mua, phụ liệu, điện nước, hao hụt sơ chế, bao bì, kiểm nghiệm theo TT 38/2021, nhân công; người đứng đầu phê duyệt quy trình sơ chế và chi phí, gửi BHXH), Đ16 (vị thuốc mua sẵn hoặc tự chế biến), Đ17 (thuốc thang: chi phí dược liệu/vị thuốc + giá dịch vụ sắc thuốc + bao bì), Đ18 k1–3 (chế phẩm tự bào chế; phần thành phần ngoài danh mục không được thanh toán), **Đ18 k4** "Thuốc chế phẩm do cơ sở khám bệnh, chữa bệnh tự chế biến, bào chế chỉ được sử dụng tại cơ sở khám bệnh, chữa bệnh đó". Bảng QĐ 130 XML2 `MA_PP_CHEBIEN`: mã phương pháp chế biến vị thuốc theo bộ mã DMDC (theo TT 30/2017), nhiều mã cách ";".
- **Áp dụng cho**: BV, PK YHCT có sơ chế, sắc thuốc, bào chế · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: công thức (BOM) chế phẩm và thuốc thang với từng thành phần có cờ "trong danh mục BHYT"; phiên bản quy trình và đơn giá được phê duyệt (số, ngày phê duyệt, đã gửi BHXH); tách dòng chi phí sắc thuốc thành DVKT; tự trừ thành phần ngoài danh mục khỏi phần BHYT; chặn bán hoặc chuyển chế phẩm tự bào chế ra ngoài cơ sở (nhà thuốc ngoài, cơ sở khác); ghi `MA_PP_CHEBIEN` cho vị thuốc.

#### CHUYENKHOA-R07 — Chỉ định thuốc YHCT phải phù hợp tờ hướng dẫn hoặc hướng dẫn chẩn đoán, điều trị YHCT của BYT
- **Căn cứ**: TT 27/2025 Đ14 k2: quỹ BHYT thanh toán khi chỉ định phù hợp (a) tờ hướng dẫn sử dụng đã được cấp phép hoặc (b) "Hướng dẫn chẩn đoán và điều trị bệnh theo y học cổ truyền, kết hợp y học cổ truyền với y học hiện đại của Bộ Y tế". k3: thuốc xếp nhóm y lý này dùng điều trị bệnh thuộc nhóm khác vẫn được thanh toán nếu chỉ định đúng k2.
- **Áp dụng cho**: cơ sở KCB BHYT · **Mức**: BẮT BUỘC (điều kiện thanh toán); kiểm tra tự động trong phần mềm là NÊN.
- **Phần mềm phải**: lưu chỉ định (theo mã ICD-10 và mã YHCT) của mỗi thuốc YHCT từ tờ hướng dẫn; cảnh báo khi kê thuốc cho chẩn đoán không có trong chỉ định và yêu cầu ghi căn cứ hướng dẫn BYT.

#### CHUYENKHOA-R08 — Kết hợp YHCT với YHHĐ: chỉ người đủ điều kiện được chỉ định, kê đơn kết hợp
- **Căn cứ**: Luật KCB Đ87 k1 a, b: kết hợp chỉ thực hiện tại cơ sở KCB; "Chỉ người hành nghề có đủ điều kiện mới được chỉ định phương pháp chữa bệnh, kê đơn thuốc kết hợp y học cổ truyền với y học hiện đại". Chi tiết ma trận chức danh theo TT 55/2025 Đ4, Đ6: xem **DUOC-R01, DUOC-R17**.
- **Mức**: BẮT BUỘC. **Phần mềm phải**: như DUOC-R01; ngoài ra phân quyền chỉ định **kỹ thuật** YHCT và YHHĐ theo phạm vi hành nghề (không chỉ kê đơn).

### B. Phòng khám chuyên khoa

#### CHUYENKHOA-R09 — Chọn đúng mẫu HSBA chuyên khoa; không có mẫu riêng cho thẩm mỹ và nha khoa tư
- **Căn cứ**: TT 32/2023 PL XXVIII (gốc, danh sách 29 mẫu): 04/BV1 phụ khoa, 05/BV1 sản khoa, 06/BV1 sơ sinh, 08/BV1 da liễu, 13/BV1 răng hàm mặt (nội trú), **15/BV1 ngoại trú chung**, **16/BV1 ngoại trú răng hàm mặt**, 21–26/BV1 mắt (chấn thương, bán phần trước, đáy mắt, glôcôm, lác, mắt trẻ em), 27/BV1 PHCN, 28/BV1 PHCN nhi, **29/BV1 ngoại trú PHCN**. Đ52 k1 b: bệnh án điện tử phải có đủ trường của HSBA.
- **Kết luận**: không có mẫu bệnh án riêng cho phẫu thuật thẩm mỹ, phòng khám thẩm mỹ, nha khoa thẩm mỹ, hỗ trợ sinh sản. Ngoại trú dùng 15/BV1 (chung) hoặc 16/BV1 (RHM), 19/BV1 (YHCT), 29/BV1 (PHCN); nội trú dùng mẫu theo chuyên khoa gần nhất (suy luận).
- **Áp dụng cho**: PK chuyên khoa, BV chuyên khoa · **Mức**: BẮT BUỘC (khi lập HSBA; khi nào phải lập xem EMR-R02).
- **Phần mềm phải**: danh mục loại bệnh án gắn mã mẫu; PK chuyên khoa chỉ được bật mẫu phù hợp phạm vi chuyên môn; trường bổ sung riêng của chuyên khoa (ví dụ sơ đồ răng, ảnh thẩm mỹ) đặt **thêm** vào mẫu, không thay trường bắt buộc của mẫu (GIAYTO-R02 cùng nguyên tắc).
- **Ghi chú / bẫy**: sơ đồ răng (odontogram) **không** phải trường pháp định; 16/BV1 chỉ có "Hình vẽ mô tả tổn thương khi vào viện" với sơ đồ phân loại khe hở môi, vòm miệng (R10). Mẫu PHCN cũ QĐ 3730/2021 hết HL (TT 32 Đ53 k2 i).

#### CHUYENKHOA-R10 — Trường "hình vẽ mô tả tổn thương" và hình ảnh trong HSBA chuyên khoa
- **Căn cứ**: TT 32 PL XXVIII: 13/BV1 và 16/BV1 có mục "Hình vẽ mô tả tổn thương khi vào viện"; mẫu mắt có hình vẽ; các mẫu có bảng "Hồ sơ, phim, ảnh" (loại, số tờ) khi giao nhận hồ sơ. Đ52 k1 b (đủ trường).
- **Mức**: BẮT BUỘC (đủ trường mẫu).
- **Phần mềm phải**: thành phần vẽ hoặc chú thích trên ảnh nền (sơ đồ khe hở, sơ đồ mắt), lưu dạng ảnh có metadata (người vẽ, thời điểm) và nằm trong gói tài liệu được ký của HSBA (EMR-R06); bảng kê phim, ảnh tự sinh từ PACS và kho ảnh lâm sàng.

#### CHUYENKHOA-R11 — Đồng ý phẫu thuật, thủ thuật và các giấy cam kết theo mẫu PL XXIX
- **Căn cứ**: Luật KCB **Đ65 k1**: phẫu thuật hoặc can thiệp có xâm nhập cơ thể "chỉ được thực hiện sau khi có sự đồng ý của người bệnh hoặc người đại diện của người bệnh" theo Đ8 k2 a–d; k2: người mất, hạn chế năng lực hành vi, người chưa thành niên, người không có thân nhân theo Đ15. TT 32 PL XXIX: 01/BV2 Giấy cam kết chấp thuận phẫu thuật, thủ thuật và gây mê hồi sức (các ô: cấp cứu/bán cấp/chương trình; bác sĩ phẫu thuật và bác sĩ GMHS; đã tư vấn chẩn đoán, lý do, rủi ro nếu không làm, kết quả dự kiến, phương pháp phẫu thuật, phương pháp vô cảm), 40/BV2 (cam kết chung nhập viện), 41/BV2 (từ chối dịch vụ), 45/BV2 (chuyển cơ sở), 46/BV2 (ra viện không theo chỉ định), 48/BV2, 49/BV2 (hóa trị, xạ trị).
- **Áp dụng cho**: mọi cơ sở có phẫu thuật, thủ thuật (gồm PK thẩm mỹ, nha khoa có thủ thuật xâm lấn) · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: chặn lập lịch hoặc bắt đầu phiếu phẫu thuật, thủ thuật (06/BV2) khi chưa có 01/BV2 ký hợp lệ (trừ luồng cấp cứu có ghi lý do theo Đ15); lưu người ký là người bệnh hay người đại diện kèm quan hệ và giấy tờ; checklist nội dung tư vấn đúng các ô của mẫu; ký điện tử theo TT 13 Đ3 (EMR-R06).
- **Ghi chú / bẫy**: tiêm filler, botox, laser xâm lấn là "can thiệp có xâm nhập cơ thể" nên cũng cần đồng ý theo Đ65 (suy luận từ định nghĩa NĐ 96 Đ40 k12 a).

#### CHUYENKHOA-R12 — Phiếu chuyên khoa mắt, sản và các phiếu phẫu thuật
- **Căn cứ**: TT 32 PL XXIX: 30/BV2 (phẫu thuật ghép giác mạc), 31/BV2 (bề mặt nhãn cầu), 32/BV2 (glôcôm), 33/BV2 (lác), 34/BV2 (túi lệ), 35/BV2 (sụp mi, mộng, thể thủy tinh, Sapejko), 51/BV2 (phiếu khám thai), 50/BV2 (điều trị trẻ sơ sinh sau sinh), 06/BV2 (phẫu thuật, thủ thuật), 05/BV2 (gây mê hồi sức).
- **Mức**: BẮT BUỘC (khi cơ sở thực hiện các kỹ thuật đó).
- **Phần mềm phải**: có form tương ứng cho cơ sở mắt, sản; phiếu khám thai lưu chuỗi lần khám theo thai kỳ (liên kết các lượt).

#### CHUYENKHOA-R13 — Thẩm mỹ: loại hình được phép, HSBA phẫu thuật thẩm mỹ lưu 20 năm cả ở phòng khám
- **Căn cứ**:
  - NĐ 96/2023 **Đ40 k12** (gốc-OCR): cơ sở cung cấp (a) dịch vụ thẩm mỹ dùng thuốc, chất, thiết bị can thiệp vào cơ thể (phẫu thuật, thủ thuật, tiêm, chích, bơm, chiếu tia, sóng, đốt, can thiệp xâm lấn khác) nhằm thay đổi màu da, hình dạng, cân nặng, khắc phục khiếm khuyết, tạo hình, tái tạo; (b) xăm, phun, thêu có dùng thuốc tê dạng tiêm, "phải được thành lập theo một trong các hình thức tổ chức là bệnh viện hoặc phòng khám đa khoa hoặc phòng khám chuyên khoa".
  - TT 33/2025 PL mục 43: "Hồ sơ bệnh án điều trị đợt ghép mô, tạng, phẫu thuật thẩm mỹ": **20 năm**; mục 44: HSBA nội, ngoại trú 10 năm. Đ1 k2 a: áp dụng cả tài liệu điện tử. Phụ lục không phân biệt bệnh viện hay phòng khám.
  - Luật KCB Đ69 k2; NĐ 90/2026 Đ40 k1 b (không lưu trữ theo quy định).
- **Kết luận (trả lời khoảng trống #5)**: thời hạn 20 năm **áp dụng cho cả phòng khám** có làm phẫu thuật thẩm mỹ, vì TT 33 quy định theo loại hồ sơ, không theo loại cơ sở (suy luận có căn cứ). Thủ thuật thẩm mỹ không phải phẫu thuật (tiêm, laser) không có dòng riêng: tối thiểu 10 năm (mục 44); thận trọng nên để 20 năm vì Đ1 k2 b yêu cầu áp nhóm tương đương "không được thấp hơn" (suy luận).
- **Áp dụng cho**: BV, PKĐK, PK chuyên khoa thẩm mỹ, RHM, da liễu có can thiệp thẩm mỹ · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: chặn kích hoạt danh mục dịch vụ thẩm mỹ xâm lấn khi loại hình cơ sở không thuộc BV/PKĐK/PK chuyên khoa; gán `retention_class = 'PTTM_20Y'` cho HSBA có phẫu thuật thẩm mỹ (EMR-R22 cơ chế chung) và cấu hình chính sách cho thủ thuật thẩm mỹ.

#### CHUYENKHOA-R14 — Ảnh trước/sau và hình ảnh người bệnh: thuộc HSBA, dùng cho quảng cáo phải có đồng ý riêng
- **Căn cứ**: không tìm thấy quy định **bắt buộc** chụp ảnh trước/sau. Nếu chụp vì mục đích chuyên môn thì là "tài liệu liên quan" của HSBA (Luật KCB Đ2 k17, Đ69 k2; suy luận) và là dữ liệu sức khỏe nhạy cảm (DLCN-R01). Dùng hình ảnh cá nhân trong quảng cáo khi chưa được đồng ý bị cấm (Luật Quảng cáo Đ8 k8, VBHN 88; phạt NĐ 87/2026 Đ50 k3 a: 20–40 triệu); dùng thư cảm ơn, danh nghĩa người bệnh để quảng cáo thuốc bị cấm (Luật Dược Đ6 k10; NĐ 163 Đ104 k16); quảng cáo thực phẩm trích ý kiến người bệnh về tác dụng chữa bệnh bị phạt (NĐ 87 Đ71 k4).
- **Mức**: NÊN (chụp, lưu); BẮT BUỘC (đồng ý riêng trước khi dùng cho quảng cáo, truyền thông).
- **Phần mềm phải**: kho ảnh lâm sàng gắn với lượt điều trị, cùng thời hạn lưu với HSBA; quyền xem theo vai trò; cờ `marketing_consent` riêng, có bằng chứng (DLCN-R03, DLCN-R28), có thu hồi; module CMS hoặc fanpage chỉ lấy được ảnh có cờ này; tự làm mờ khuôn mặt nếu không có đồng ý.

#### CHUYENKHOA-R15 — Hỗ trợ sinh sản: chỉ bệnh viện, mã hóa người cho, lưu vĩnh viễn
- **Căn cứ**: NĐ 96 Đ40 k9: cơ sở có hoạt động sinh con bằng IVF, mang thai hộ "phải được tổ chức theo hình thức bệnh viện" và đáp ứng NĐ 10/2015. NĐ 10/2015 Đ3 k2: vợ chồng nhờ mang thai hộ, người mang thai hộ, trẻ sinh ra "được bảo đảm an toàn về đời sống riêng tư, bí mật cá nhân, bí mật gia đình"; Đ3 k4: cho, nhận tinh trùng, phôi "trên nguyên tắc vô danh"; tinh trùng, phôi của người cho "phải được mã hóa để bảo đảm bí mật nhưng vẫn phải ghi rõ đặc điểm của người cho, đặc biệt là yếu tố chủng tộc" (gốc-OCR). Đ20–21: lưu giữ tinh trùng, noãn, phôi theo hợp đồng. TT 33/2025 mục 211, 214: hồ sơ sinh con bằng thụ tinh nhân tạo, IVF, mang thai hộ và hồ sơ hiến, nhận tinh trùng, noãn, phôi: **vĩnh viễn**.
- **Áp dụng cho**: BV có trung tâm hỗ trợ sinh sản · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: định danh người cho bằng mã giả danh, bảng ánh xạ danh tính tách riêng, mã hóa, quyền truy cập rất hẹp có log; hồ sơ phía người nhận chỉ thấy mã và đặc điểm (gồm chủng tộc); `retention_class = 'PERMANENT'` cho hồ sơ IVF, cho nhận giao tử, phôi; quản lý mẫu lưu trữ đông lạnh gắn hợp đồng, hạn đóng phí.
- **Ghi chú / bẫy**: phòng khám **không** được làm IVF; phần mềm cho PK sản chỉ dừng ở tư vấn, xét nghiệm, theo dõi. Không quảng cáo chẩn đoán, lựa chọn giới tính thai (R33).

### C. Tiêm chủng

#### CHUYENKHOA-R16 — Cập nhật đối tượng và mũi tiêm lên Hệ thống quản lý thông tin tiêm chủng quốc gia, không trùng lặp
- **Căn cứ**: TT 13/2026 Đ2 k1 (định nghĩa Hệ thống gồm phân hệ đối tượng, vắc xin, quy trình tiêm, thống kê báo cáo). **Đ10 k2 a, b** (gốc): với cả tiêm bắt buộc và tự nguyện, cơ sở tiêm chủng "cấp và điền sổ theo dõi tiêm chủng cá nhân; thống kê danh sách đối tượng tiêm chủng tại cơ sở và cập nhật đầy đủ, chính xác, kịp thời thông tin của đối tượng tiêm chủng lên Hệ thống quản lý thông tin tiêm chủng quốc gia bảo đảm không trùng lặp đối tượng tiêm chủng". Đ10 k1: thông tin của cha, mẹ, người giám hộ hoặc đại diện với trẻ em, người mất, hạn chế năng lực hành vi. Đ14 k2. Luật 114/2025 Đ12, Đ38 k1 (HTTT phòng bệnh, liên thông).
- **Áp dụng cho**: cơ sở tiêm chủng công, tư; cơ sở KCB có tiêm · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: đồng bộ mỗi mũi tiêm lên Hệ thống quốc gia (trực tiếp hoặc qua phần mềm quốc gia); trước khi tạo đối tượng mới phải tra trùng theo số định danh cá nhân hoặc bộ (họ tên, ngày sinh, giới, mẹ); lưu `national_subject_id`; không xóa đối tượng đã có lịch sử tiêm (QĐ 3421 Đ7 k4, hiệu lực chưa xác minh).
- **Ghi chú / bẫy**: **không có** văn bản nào bắt cập nhật "trong 24 giờ". Văn bản dùng "kịp thời" (TT 13 Đ10) và "thời gian thực" cho hệ thống riêng (R17). QĐ 3421/2017 Đ7 k2 b từng yêu cầu nhập "ngay trong buổi tiêm" (vùng khó: 05 ngày làm việc), k6 nhập bù trong 03 ngày làm việc khi hệ thống lỗi; chỉ dùng như thực hành tốt vì hiệu lực sau 01/07/2026 chưa rõ.

#### CHUYENKHOA-R17 — Hệ thống riêng phải kết nối, chia sẻ dữ liệu thời gian thực với Hệ thống quốc gia
- **Căn cứ**: TT 13/2026 **Đ25 k8** (gốc): "Trường hợp cơ sở sử dụng hệ thống riêng thì phải bảo đảm kết nối liên thông, chia sẻ dữ liệu thời gian thực với Hệ thống quản lý thông tin tiêm chủng quốc gia và bảo đảm an toàn, an ninh thông tin theo quy định, trừ dữ liệu của các đối tượng thuộc Bộ Công an, Bộ Quốc phòng quản lý". Đ15 k7: liên thông "theo hướng dẫn chuyên môn của Cục Phòng bệnh"; k8–9: an ninh mạng, bảo vệ DLCN.
- **Áp dụng cho**: chuỗi tiêm chủng dịch vụ, BV dùng HIS hoặc phần mềm tiêm riêng; vendor · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (nghĩa vụ); đặc tả API: chưa có văn bản.
- **Phần mềm phải**: đẩy sự kiện mũi tiêm ngay khi xác nhận tiêm (không theo lô cuối ngày); hàng đợi gửi lại có giám sát độ trễ; loại trừ hồ sơ thuộc BCA, BQP khỏi luồng chia sẻ (cờ đối tượng); log gửi, phản hồi để chứng minh "thời gian thực".
- **Ghi chú / bẫy**: chưa tìm thấy QĐ hay hướng dẫn của Cục Phòng bệnh về chuẩn API; vendor phải hỏi Cục Phòng bệnh hoặc VNCDC (mục 7).

#### CHUYENKHOA-R18 — Bộ trường thông tin cơ bản: 44 trường, 20 trường bắt buộc (QĐ 3891/2025)
- **Căn cứ**: QĐ 3891/QĐ-BYT (18/12/2025), theo CV 31/TTKSBT-PCBTNCT (06/01/2026) của HCDC: 44 trường, 2 nhóm (hành chính, mũi tiêm), 20 trường bắt buộc. Hành chính bắt buộc (15): mã số định danh đối tượng (mã định danh cá nhân, CCCD hoặc hộ chiếu), họ tên, ngày sinh, giới tính, mã dân tộc và cặp phường/xã–tỉnh cho 5 loại địa chỉ (nơi sinh, nơi khai sinh, quê quán, thường trú, nơi ở hiện tại). Mũi tiêm bắt buộc (5): vắc xin, ngày tiêm, thứ tự mũi, cơ sở tiêm, kháng nguyên. Không bắt buộc: nhóm máu, tình trạng (0 chưa có thông tin, 1 đang sống, 2 đã chết, 3 mất tích), loại giấy tờ, giấy tờ xuất nhập cảnh, thông tin cha, mẹ, người bảo hộ.
- **Mức**: BẮT BUỘC? (QĐ ban hành theo căn cứ NĐ 104, TT 34 đã hết HL; chưa thấy văn bản thay).
- **Phần mềm phải**: schema đối tượng tiêm có đủ 44 trường; validate 20 trường bắt buộc trước khi gửi; địa chỉ 2 cấp (xã, tỉnh) theo danh mục đơn vị hành chính sau sắp xếp; trường kháng nguyên tách khỏi tên thương mại vắc xin (một vắc xin phối hợp nhiều kháng nguyên).

#### CHUYENKHOA-R19 — Sổ theo dõi tiêm chủng cá nhân hoặc sổ tiêm chủng điện tử
- **Căn cứ**: TT 13/2026 Đ10 k2 (cấp và điền sổ). NĐ 90/2026 **Đ9 k2 b** (gốc-OCR): phạt 1–3 triệu (cá nhân) hành vi "Không cấp và ghi sổ theo dõi tiêm chủng cá nhân hoặc sổ tiêm chủng điện tử cho người đến tiêm tại cơ sở tiêm chủng"; k2 c: không thống kê danh sách đối tượng đã tiêm.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: in hoặc xuất sổ, phiếu xác nhận mũi tiêm cho người được tiêm; hiển thị lịch sử trên app người dùng (sổ điện tử); danh sách thống kê đối tượng đã tiêm theo buổi.
- **Ghi chú / bẫy**: NĐ 165/2026 Đ26 chỉ có **Giấy chứng nhận quốc tế** về tiêm chủng (Mẫu 02 PL V). Chưa thấy văn bản về "giấy xác nhận tiêm chủng điện tử" trong nước. Mẫu sổ theo dõi tiêm chủng cá nhân mới chưa thấy ban hành kèm TT 13.

#### CHUYENKHOA-R20 — Khám sàng lọc, theo dõi 30 phút, hướng dẫn theo dõi 24 giờ
- **Căn cứ**: TT 13/2026 Đ12 k2 a (khám sàng lọc theo hướng dẫn của Bộ trưởng), k2 c (theo dõi tại điểm tiêm ít nhất 30 phút; hướng dẫn tiếp tục theo dõi tại nhà ít nhất 24 giờ; ghi chép theo hướng dẫn Cục Phòng bệnh). NĐ 90 Đ9 k1 b, c (cảnh cáo: không tư vấn, không hướng dẫn theo dõi), k2 d (1–3 triệu), k3 a (3–5 triệu: không khám sàng lọc hoặc khám không đầy đủ).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: phiếu khám sàng lọc bắt buộc hoàn tất, có kết luận "đủ điều kiện tiêm" trước khi cho xác nhận mũi tiêm; đồng hồ 30 phút sau tiêm, ghi giờ rời điểm tiêm; in, gửi hướng dẫn theo dõi 24 giờ; ghi phản ứng sau tiêm.

#### CHUYENKHOA-R21 — Tai biến nặng: dừng buổi tiêm, khóa lô, báo cáo trong 24 giờ
- **Căn cứ**: NĐ 165/2026 Đ2 k7 (định nghĩa tai biến nặng). TT 13/2026 Đ12 k3 (dừng ngay buổi tiêm, cấp cứu, thống kê, báo cáo), k5 (tạm dừng lô vắc xin), **Đ15 k5 a**: trong 24 giờ kể từ khi ghi nhận tai biến nặng, báo cáo Sở Y tế đồng thời CDC tỉnh. NĐ 90 Đ9 k3 d (3–5 triệu: không thống kê đủ và báo cáo Sở Y tế trong 24 giờ), k4 b (5–10 triệu: không dừng buổi tiêm), k5 c, d, đ (10–20 triệu).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: nút ghi nhận tai biến nặng tạo ngay sự kiện có dấu thời gian, đồng hồ đếm ngược 24 giờ, mẫu báo cáo gửi Sở Y tế và CDC; tự khóa buổi tiêm đang mở và chặn xuất lô vắc xin liên quan trên mọi điểm tiêm của cơ sở; lưu hồ sơ phục vụ Hội đồng tư vấn (NĐ 90 Đ9 k2 đ).

#### CHUYENKHOA-R22 — Báo cáo tiêm chủng định kỳ và trong chiến dịch
- **Căn cứ**: TT 13/2026 Đ15 k1 (trên Hệ thống hoặc văn bản; văn bản khi khẩn cấp hoặc hệ thống lỗi), k2 (báo cáo ngày, tháng, năm, đột xuất), k3 (biểu mẫu theo hướng dẫn Cục Phòng bệnh; TT không kèm mẫu), k4 a (cơ sở tiêm báo cáo Trạm Y tế xã: tháng trước ngày 03 tháng sau; năm trước 13/01 năm sau), k6 a (chiến dịch, chống dịch: trước 17 giờ hằng ngày). Luật 114 Đ23 k2. NĐ 90 Đ9 k1 d (cảnh cáo: không báo cáo hoặc báo cáo không đúng).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: báo cáo tháng, năm, ngày sinh tự động từ dữ liệu mũi tiêm; lịch nhắc theo các mốc; xuất văn bản dự phòng khi hệ thống quốc gia lỗi (HTTT-BC-R26 cùng mô hình).

#### CHUYENKHOA-R23 — Danh mục bệnh, vắc xin và phân loại tiêm bắt buộc, tự nguyện
- **Căn cứ**: Luật 114/2025 Đ22 k1 (tiêm bắt buộc gồm cả chống dịch; tiêm tự nguyện), k3 (chỉ tiêm khi đủ điều kiện); TT 13/2026 Đ3 (14 bệnh tiêm bắt buộc trong TCMR, có HPV), Đ4 (11 bệnh tiêm chống dịch), Đ26 k1 (cơ sở có phòng sinh: viêm gan B trong 24 giờ sau sinh). NĐ 90 Đ9 k3 e, g (không tính vào giá chi phí đã được NSNN bảo đảm; không bán vắc xin TCMR).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: master `vaccine` (tên thương mại, số đăng ký) ↔ `antigen` ↔ `disease` ↔ `program` (TCMR, chống dịch, dịch vụ); mỗi mũi lưu `program`; bảng giá chặn tính tiền vắc xin TCMR; nhắc mũi viêm gan B sơ sinh trong 24 giờ cho cơ sở có phòng sinh.

#### CHUYENKHOA-R24 — Điều kiện cơ sở và điểm tiêm; lưu giữ hồ sơ tiêm chủng
- **Căn cứ**: Luật 114 Đ8 k7 (cấm tiêm tại nơi không đủ điều kiện); NĐ 165 Đ49 (điều kiện cơ sở, HL 01/07/2027), Đ94 k5 (Đ9–11 NĐ 104/2016 còn HL đến 30/06/2027), Đ95 k2 (đã công bố không phải công bố lại); NĐ 90 Đ9 k5 a, b (10–20 triệu: dùng vắc xin ở cơ sở không đủ điều kiện; tiêm khi chưa công bố). TT 13 Đ25 k10 (lưu giữ hồ sơ tiêm chủng và sự cố); NĐ 90 Đ9 k2 e (1–3 triệu: không lưu giữ). TT 33/2025: mục 119 (hồ sơ công bố cơ sở đủ điều kiện tiêm chủng: 20 năm), 121 (kế hoạch TCMR hằng năm: 05 năm); **không có dòng** cho hồ sơ tiêm chủng cá nhân.
- **Mức**: BẮT BUỘC (lưu giữ, điều kiện); thời hạn lưu hồ sơ tiêm cá nhân: BẮT BUỘC? (chưa có dòng riêng).
- **Phần mềm phải**: danh mục điểm tiêm có trạng thái công bố, chặn mở buổi tiêm tại điểm chưa công bố; hồ sơ mũi tiêm, sàng lọc, phản ứng không cho xóa; chính sách lưu tối thiểu bằng HSBA ngoại trú (10 năm) theo Đ1 k2 b TT 33 (suy luận), dữ liệu trên Hệ thống quốc gia không thay nghĩa vụ lưu tại cơ sở (suy luận).

#### CHUYENKHOA-R25 — Tiền sử tiêm chủng trên Sổ SKĐT VNeID
- **Căn cứ**: QĐ 31/QĐ-BYT (06/01/2026) Đ2 k3 b: Sổ SKĐT VNeID có "tiền sử tiêm chủng" (loại vắc xin, kháng nguyên, số mũi, nơi tiêm, ngày tiêm); Đ1 k1 (dữ liệu hiển thị trên VNeID có giá trị như bản giấy); Đ5 (cơ sở KCB liên thông Sổ SKĐT cho mọi người bệnh, xem SKDT-R01).
- **Mức**: BẮT BUỘC? Chưa thấy văn bản buộc cơ sở tiêm chủng đẩy thẳng dữ liệu tiêm lên VNeID; kênh hợp lý là Hệ thống tiêm chủng quốc gia (suy luận).
- **Phần mềm phải**: dùng số định danh cá nhân làm khóa chính đối tượng tiêm (SKDT-R05); không tự xây kênh đẩy VNeID riêng khi chưa có hướng dẫn; với cơ sở KCB đã liên thông Sổ SKĐT, không gửi trùng mũi tiêm qua hai kênh mà không có khóa chống trùng (suy luận).

### D. Quảng cáo dịch vụ y tế, thuốc trên website, app, nền tảng

#### CHUYENKHOA-R26 — Nội dung bắt buộc của quảng cáo dịch vụ KCB; không còn thủ tục xác nhận nội dung
- **Căn cứ**: NĐ 342/2025 **Đ9** (gốc-OCR): nội dung quảng cáo dịch vụ KCB phải có (1) tên, địa chỉ, số giấy phép hoạt động, thời gian hoạt động; (2) phạm vi hoạt động chuyên môn do cơ quan có thẩm quyền phê duyệt. Luật Quảng cáo Đ20 k4 đ (dịch vụ KCB phải có giấy phép). NĐ 87/2026 **Đ75** k1 (thiếu một nội dung: 15–20 triệu; bổ sung: tước GPHĐ 01–03 tháng), k3 (quảng cáo khi chưa có GPHĐ hoặc CCHN: 30–40 triệu). TT 03/2026 Đ2 k1: bãi bỏ TT 09/2015 trừ phần thực phẩm, sữa và sản phẩm dinh dưỡng cho trẻ → **không còn** thủ tục xin xác nhận nội dung quảng cáo dịch vụ KCB từ 15/02/2026 (giấy đã cấp vẫn dùng theo Đ4 TT 03, theo lượt phụ).
- **Áp dụng cho**: BV, PK (website, fanpage, app); sàn đặt khám đăng trang cơ sở · **Hiệu lực**: 15/02/2026 (NĐ 342, TT 03); 15/05/2026 (NĐ 87).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: template trang hoặc card cơ sở tự chèn 5 trường từ hồ sơ pháp lý (tên, địa chỉ, số GPHĐ, giờ hoạt động, phạm vi chuyên môn); không cho xuất bản bài quảng cáo thiếu trường; onboarding cơ sở trên sàn bắt nhập và đối chiếu số GPHĐ.

#### CHUYENKHOA-R27 — Không quảng cáo vượt phạm vi chuyên môn; không quảng cáo gian dối
- **Căn cứ**: Luật KCB **Đ7 k20**: cấm "Quảng cáo vượt quá phạm vi hành nghề hoặc vượt quá phạm vi hoạt động chuyên môn đã được cơ quan có thẩm quyền phê duyệt; lợi dụng kiến thức y học để quảng cáo gian dối". NĐ 87 Đ75 k4: 40–60 triệu, tước GPHĐ hoặc CCHN 03–06 tháng. Luật Quảng cáo Đ8 k9 (gây nhầm lẫn về chất lượng, công dụng; NĐ 87 Đ50 k5 c: 80–100 triệu), Đ19 k1 (trung thực, chính xác; sửa bởi Luật 75).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: danh mục dịch vụ hiển thị công khai sinh từ danh mục kỹ thuật được phê duyệt của cơ sở (MA-LT-R14), không cho nhập dịch vụ tự do; bác sĩ chỉ được gắn với dịch vụ trong phạm vi hành nghề (GPHN); quy trình duyệt nội dung có người chịu trách nhiệm chuyên môn ký duyệt, lưu phiên bản đã đăng.

#### CHUYENKHOA-R28 — Gắn nhãn quảng cáo, nút tắt, báo vi phạm; phân biệt kết quả tài trợ
- **Căn cứ**: Luật Quảng cáo Đ23 k1, k2 a–c (sửa bởi Luật 75/2025): quảng cáo trên mạng gồm trang thông tin điện tử, mạng xã hội, ứng dụng trực tuyến, nền tảng số; phải có dấu hiệu phân biệt nội dung quảng cáo; quảng cáo không cố định phải có nút tắt, báo vi phạm, từ chối xem. NĐ 342 Đ17 k2–4 (tắt bằng một thao tác; video chờ tối đa 5 giây; cấm nút tắt giả; tiếp nhận và trả kết quả báo vi phạm), Đ19 (nền tảng trung gian: hiển thị tên, địa chỉ người mua quảng cáo; kết quả tìm kiếm có tài trợ phải phân biệt). NĐ 87 Đ56 k2: 30–40 triệu.
- **Áp dụng cho**: cổng BV, app đặt lịch, sàn đặt khám, app nhà thuốc có hiển thị quảng cáo hoặc vị trí trả tiền · **Hiệu lực**: 01/01/2026 (Luật 75), 15/02/2026 (NĐ 342).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: nhãn "Quảng cáo"/"Được tài trợ" trên mọi vị trí trả phí (kể cả bác sĩ, phòng khám được đẩy hạng); popup có nút tắt thật; luồng báo vi phạm có mã phiếu và trạng thái xử lý; hiển thị tên người mua quảng cáo.

#### CHUYENKHOA-R29 — Gỡ quảng cáo vi phạm chậm nhất 24 giờ theo yêu cầu; nghĩa vụ của người kinh doanh dịch vụ quảng cáo trên mạng
- **Căn cứ**: Luật Quảng cáo **Đ23 k7** (gốc, Luật 75): "phải thực hiện việc ngăn chặn, gỡ bỏ quảng cáo vi phạm chậm nhất 24 giờ kể từ khi có yêu cầu của cơ quan nhà nước có thẩm quyền"; Đ23 k3 b–d (không đặt cạnh nội dung vi phạm, chặn đối tác đã bị công bố vi phạm). NĐ 342 **Đ19** (gốc-OCR): thông báo thông tin liên hệ với Bộ VHTTDL (giấy xác nhận trong 04 ngày làm việc), k2 lưu trữ thông tin người quảng cáo, sản phẩm, mẫu, thời gian, vị trí, hợp đồng "Trong 03 năm kể từ ngày cuối cùng quảng cáo được hiển thị", k3 báo cáo năm (Mẫu 04) chậm nhất 25/11. NĐ 87 Đ56 k1 (20–30 triệu), k3 (40–50 triệu), **k4** (không gỡ trong 24 giờ: 50–60 triệu).
- **Áp dụng cho**: mọi bên tham gia quảng cáo trên mạng (gỡ 24 giờ); nghĩa vụ Đ19 cho "người kinh doanh dịch vụ quảng cáo trên mạng" · **Mức**: BẮT BUỘC (24 giờ); BẮT BUỘC? (Đ19 với sàn đặt khám bán vị trí nổi bật: việc xếp vai là suy luận).
- **Phần mềm phải**: công cụ gỡ ngay theo mẫu quảng cáo hoặc theo nhà quảng cáo; log thời điểm nhận yêu cầu và thời điểm gỡ; bảng `ad_record` lưu đủ trường Đ19 k2 tối thiểu 3 năm sau lần hiển thị cuối; danh sách chặn đối tác; nhắc báo cáo 25/11.

#### CHUYENKHOA-R30 — Quảng cáo thuốc: cấm thuốc kê đơn, phải có giấy xác nhận, nội dung bắt buộc, từ ngữ và hình ảnh cấm
- **Căn cứ**: Luật Quảng cáo Đ7 k5 (cấm quảng cáo thuốc kê đơn, thuốc không kê đơn bị khuyến cáo hạn chế hoặc phải dùng dưới giám sát thầy thuốc). Luật Dược Đ79 k1–2 (chỉ quảng cáo thuốc không kê đơn, không bị khuyến cáo hạn chế, giấy đăng ký còn hiệu lực; đúng nội dung BYT xác nhận), Đ6 k10, k15. NĐ 163/2025 Đ103 k2 (nội dung bắt buộc, gồm "Đọc kỹ hướng dẫn sử dụng trước khi dùng" và số giấy xác nhận), k4 (web, app không có âm thanh phải hiện đủ), k7 (cỡ chữ); Đ104 k6 (từ cấm như "chuyên trị", "an toàn", "khỏi hẳn", "khuyên dùng", "hotline"…), k13 (hình ảnh, tên cán bộ y tế), k15, k16; Đ111 (người phát hành chỉ chạy nội dung đã xác nhận; không đặt kèm bài bệnh học dễ gây hiểu là kết quả dùng thuốc). TT 31/2025 Đ19–20 (tài liệu thông tin thuốc). NĐ 87 Đ49 k1 d (quảng cáo thuốc kê đơn: 50–70 triệu), Đ69 k1–4 (5–40 triệu). NĐ 90 Đ67 k3, k5.
- **Áp dụng cho**: app, web nhà thuốc; sàn; cổng BV có trang thuốc · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: cờ `rx_only` từ master thuốc (DUOC-R29) chặn mọi banner, push, bài quảng cáo; quảng cáo thuốc bắt nhập số giấy xác nhận và tự chèn câu "Đọc kỹ hướng dẫn sử dụng trước khi dùng"; bộ lọc từ khóa cấm và chặn ảnh nhân viên y tế trong creative thuốc; không đặt quảng cáo thuốc trong bài tư vấn sức khỏe liên quan.
- **Ghi chú / bẫy**: **NĐ 90/2026 không có điều phạt quảng cáo thuốc hay dịch vụ KCB** (chỉ rượu bia, sữa); các hành vi này bị phạt theo **NĐ 87/2026** (theo lượt phụ, tìm từ khóa trên OCR).

#### CHUYENKHOA-R31 — Thông tin thuốc và bán thuốc trên app, website
- **Căn cứ**: NĐ 163/2025 Đ41 (thông tin bắt buộc đăng: giấy chứng nhận đủ điều kiện, chứng chỉ của người chịu trách nhiệm chuyên môn, thông tin từng thuốc; thông tin thuốc ở **chuyên mục riêng, không lẫn sản phẩm không phải thuốc**), Đ42 (nộp giấy tờ cho sàn trước khi lên sàn; bao bì giao hàng in số điện thoại người tư vấn). Luật Dược Đ6 k17–19, Đ42 k4: xem **DUOC-R29**. NĐ 90 Đ59 k3 m, k4 g, i, k, l.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: ngoài DUOC-R29: cây danh mục tách "Thuốc" khỏi thực phẩm bảo vệ sức khỏe, mỹ phẩm, thiết bị; trang nhà thuốc hiển thị giấy chứng nhận và chứng chỉ; nhãn giao hàng có số điện thoại dược sĩ tư vấn. Thực phẩm bảo vệ sức khỏe phải có cụm "Thực phẩm bảo vệ sức khỏe" và câu "Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh" (NĐ 342 Đ5 k2–3).

#### CHUYENKHOA-R32 — Đánh giá, xếp hạng bác sĩ và cơ sở; nội dung quy kết sự cố y khoa; KOL
- **Căn cứ**:
  - Luật BVQLNTD 19/2023 Đ10 k3 b (cấm sắp xếp ưu tiên mà không công khai tiêu chí), k3 c (cấm ngăn hiển thị hoặc hiển thị không trung thực phản hồi, đánh giá), k1 h (cấm không công khai việc tài trợ người có ảnh hưởng); Đ22 k3; Đ39 k3 d.
  - Luật TMĐT 122/2025 Đ17 k2 h (nền tảng có đặt hàng cho người mua đánh giá, hiển thị đầy đủ, chính xác), k1 đ (kiểm duyệt thông tin trước hiển thị); NĐ 248/2026 Đ11 (công khai tiêu chí chính của ưu tiên hiển thị, gồm đánh giá của người mua và trả phí để hiển thị).
  - Luật Quảng cáo Đ2 k8, **Đ15a** k2–3 (Luật 75): người có ảnh hưởng phải xác minh người quảng cáo, kiểm tra tài liệu sản phẩm, "chưa sử dụng hoặc chưa hiểu rõ… thì không được giới thiệu", thông báo việc quảng cáo trước và trong khi quảng cáo; NĐ 87 Đ51 (40–100 triệu).
  - Luật KCB **Đ7 k17** (lợi dụng hình ảnh, tư cách người hành nghề khuyến khích phương pháp chưa được công nhận; NĐ 90 Đ38 k5 n), **Đ7 k21** (đăng thông tin quy kết trách nhiệm người hành nghề, cơ sở khi xảy ra sự cố y khoa mà chưa có kết luận của cơ quan có thẩm quyền; NĐ 90 Đ38 k7 h: 30–40 triệu theo lượt phụ).
  - Luật Quảng cáo Đ8 k11: không dùng "nhất", "duy nhất", "tốt nhất", "số một" khi không có tài liệu chứng minh (NĐ 87 Đ50 k2 a).
- **Áp dụng cho**: sàn đặt khám, app có review bác sĩ; cơ sở KCB có chương trình KOL · **Mức**: BẮT BUỘC (hiển thị trung thực, công khai tiêu chí, nhãn tài trợ, Đ7 k21); BẮT BUỘC? (phạm vi áp Luật TMĐT cho app chỉ đặt lịch không thanh toán, suy luận).
- **Phần mềm phải**: trang "tiêu chí xếp hạng" công khai; không ẩn đánh giá xấu trừ khi vi phạm pháp luật (có lý do lưu log); hàng đợi kiểm duyệt cho review có nội dung quy kết sự cố y khoa (tạm ẩn chờ xác minh, ghi rõ lý do); chỉ cho đánh giá từ tài khoản có lượt khám thật (chống review giả, suy luận); nhãn "Có tài trợ" cho bài của bác sĩ, KOL được trả tiền; bộ lọc từ tuyệt đối.
- **Ghi chú / bẫy**: **không có** quy định y tế riêng về xếp hạng bác sĩ. Hành vi cấm của Luật KCB nằm ở **Đ7**, không phải Đ12 (Đ12 là quyền được cung cấp thông tin HSBA và chi phí).

#### CHUYENKHOA-R33 — Quảng cáo bị cấm trong sản khoa, ghép tạng; livestream
- **Căn cứ**: NĐ 87/2026 Đ75 k2 (gốc): 20–30 triệu hành vi "(a) Quảng cáo việc chẩn đoán, lựa chọn giới tính phôi, thai nhi; (b) Quảng cáo, môi giới việc hiến, nhận bộ phận cơ thể người vì mục đích thương mại"; bổ sung tước GPHĐ 03–06 tháng. Luật TMĐT Đ22 k5–7 (yêu cầu giấy xác nhận trước khi livestream hàng phải xác nhận; dừng, gỡ ngay livestream hàng cấm quảng cáo như thuốc kê đơn; **lưu dữ liệu hình ảnh, âm thanh livestream ít nhất 01 năm**), Đ24.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: bộ lọc nội dung chặn từ khóa giới tính thai, "sinh con trai/gái", môi giới tạng trên mọi bài, quảng cáo của PK sản, BV; nền tảng có livestream: lưu bản ghi ≥ 1 năm, chặn livestream thuốc kê đơn.

### E. Ngôn ngữ, bộ mã và khả năng tiếp cận

#### CHUYENKHOA-R34 — Tiếng Việt là ngôn ngữ KCB; chỉ định điều trị và đơn thuốc ghi bằng tiếng Việt
- **Căn cứ**: Luật KCB **Đ21 k1**: "Ngôn ngữ sử dụng trong khám bệnh, chữa bệnh là tiếng Việt", trừ k2 (người hành nghề nước ngoài được dùng ngôn ngữ khác với người bệnh cùng ngôn ngữ mẹ đẻ hoặc cùng ngôn ngữ đã đăng ký, người bệnh nước ngoài, KCB nhân đạo theo đợt, chuyển giao kỹ thuật). **Đ21 k3 b**: "Việc ghi thông tin về khám bệnh, chữa bệnh được thực hiện bằng ngôn ngữ đã đăng ký của người hành nghề nước ngoài đồng thời phải được dịch sang tiếng Việt." NĐ 96/2023 **Đ35 k3** (gốc-OCR): "Việc chỉ định điều trị, kê đơn thuốc phải ghi bằng tiếng Việt. Trường hợp người hành nghề là người nước ngoài thì việc chỉ định điều trị, kê đơn thuốc phải ghi bằng ngôn ngữ mà người hành nghề đăng ký sử dụng khi khám bệnh, chữa bệnh và phải được dịch sang tiếng Việt, có chữ ký của người phiên dịch trên đơn thuốc." TT 32 Đ52 k2 c (không viết tắt trên tài liệu cấp cho người bệnh, xem EMR-R04).
- **Áp dụng cho**: mọi cơ sở KCB · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: mọi trường văn bản pháp định (chỉ định, đơn thuốc, HSBA, giấy tờ) có bản tiếng Việt là bản chính; bản song ngữ là phụ; với người hành nghề nước ngoài: lưu song song bản gốc theo ngôn ngữ đã đăng ký và bản dịch tiếng Việt, ghi người dịch, và **đơn thuốc phải có chữ ký người phiên dịch** (thêm vai ký thứ hai trên đơn); master thuốc, dịch vụ, chẩn đoán dùng tên tiếng Việt theo danh mục BYT.
- **Ghi chú / bẫy**: Luật KCB Đ121 k4: quy định ngôn ngữ trong cấp phép và hành nghề với người nước ngoài theo Luật 40/2009 "được áp dụng đến hết ngày 31 tháng 12 năm 2031"; Đ120 k4: điều kiện năng lực tiếng Việt từ 01/01/2032. Quan hệ giữa Đ21 (luật mới), NĐ 96 Đ35 và quy định cũ trong giai đoạn chuyển tiếp: chưa xác minh (mục 7). Phương án an toàn: đáp ứng cả hai, nghĩa là luôn có bản tiếng Việt và người phiên dịch (suy luận).

#### CHUYENKHOA-R35 — Ghi nhận nhu cầu ngôn ngữ và người phiên dịch cho người bệnh nước ngoài, dân tộc thiểu số, khuyết tật ngôn ngữ
- **Căn cứ**: Luật KCB Đ21 k3 a (KCB cho người bệnh nước ngoài bởi người hành nghề nước ngoài, và KCB nhân đạo, chuyển giao kỹ thuật "phải có người phiên dịch"), k4. NĐ 96 Đ35 k1, k2 (tiêu chuẩn người phiên dịch; trường hợp nhân đạo, chuyển giao: người phiên dịch phải có GPHN), **Đ36 k1**: người nước ngoài, đồng bào dân tộc thiểu số không sử dụng được tiếng Việt, người khuyết tật về ngôn ngữ "phải thực hiện việc đăng ký khám bệnh, chữa bệnh và yêu cầu về ngôn ngữ" với cơ sở để cơ sở bố trí người hành nghề hoặc người phiên dịch; không bố trí được thì người bệnh tự bố trí và tự chịu trách nhiệm nội dung phiên dịch; k2 a (cấp cứu: được dùng nhân viên biết ngôn ngữ, nhân viên không chịu trách nhiệm kết quả phiên dịch), k2 b, k3 (theo Luật KCB Đ15).
- **Áp dụng cho**: mọi cơ sở KCB, đặc biệt BV, PK quốc tế · **Mức**: BẮT BUỘC (nghĩa vụ cơ sở); phần mềm hỗ trợ là NÊN nhưng thiếu thì khó chứng minh tuân thủ.
- **Phần mềm phải**: trường `preferred_language`, `needs_interpreter`, `interpreter_source` (cơ sở bố trí / người bệnh tự bố trí / nhân viên hỗ trợ cấp cứu), tên, GPHN (nếu là trường hợp nhân đạo, chuyển giao) của người phiên dịch gắn với lượt khám; mẫu xác nhận người bệnh tự bố trí phiên dịch; app đặt lịch cho chọn ngôn ngữ ngay khi đăng ký (thực hiện Đ36 k1 "đăng ký… yêu cầu về ngôn ngữ"). Định danh người nước ngoài: SKDT-R12.

#### CHUYENKHOA-R36 — Ngôn ngữ đăng ký của người hành nghề nước ngoài
- **Căn cứ**: Luật KCB Đ37 k5 (nội dung đăng ký hành nghề có ngôn ngữ người hành nghề nước ngoài sử dụng); NĐ 96 Đ28 (nội dung đăng ký, điểm e theo OCR).
- **Mức**: BẮT BUỘC (khi cơ sở có người hành nghề nước ngoài).
- **Phần mềm phải**: hồ sơ nhân sự có trường ngôn ngữ đã đăng ký; chặn người hành nghề nước ngoài khám bằng ngôn ngữ khác ngôn ngữ đã đăng ký mà không có phiên dịch (cảnh báo) và tự đòi bản dịch tiếng Việt (R34).

#### CHUYENKHOA-R37 — Bộ mã ký tự: Unicode TCVN 6909:2001, UTF-8
- **Căn cứ**: QĐ 72/2002/QĐ-TTg Đ1 (gốc): từ 01/01/2003 "thống nhất dùng bộ mã các ký tự chữ Việt theo tiêu chuẩn TCVN 6909:2001… trong trao đổi thông tin điện tử giữa các tổ chức của Đảng và Nhà nước". TT 39/2017/TT-BTTTT PL (đọc ảnh): mục 2.7 "Trình diễn bộ kí tự: UTF-8" **bắt buộc áp dụng**; mục 3.14 "Bộ ký tự và mã hóa cho tiếng Việt: TCVN 6909:2001" **bắt buộc áp dụng**. CV 365 mục III.1.3 c: phần mềm HSBA điện tử đáp ứng TT 39/2017 (xem EMR, MA-LT).
- **Áp dụng cho**: BV công, hệ thống đầu tư hoặc thuê bằng NSNN, EMR theo CV 365; vendor · **Mức**: BẮT BUỘC? (TT 39 dựa trên Luật CNTT đã hết HL; CV 365 không phải VBQPPL); NÊN với cơ sở tư.
- **Phần mềm phải**: lưu, truyền, xuất (XML BHYT, API, PDF) bằng UTF-8; không dùng bảng mã TCVN3/VNI; chuẩn hóa chuỗi tiếng Việt về một dạng Unicode (khuyến nghị NFC) trước khi lưu và so khớp để tránh trùng hồ sơ do dấu tổ hợp khác dạng dựng sẵn (suy luận kỹ thuật); font PDF nhúng đủ ký tự tiếng Việt.

#### CHUYENKHOA-R38 — Khả năng tiếp cận cho người khuyết tật trên website, cổng, app
- **Căn cứ**: TT 26/2020/TT-BTTTT (đọc ảnh): Đ2 k2 (CQNN gồm "các đơn vị sự nghiệp sử dụng ngân sách nhà nước để thiết kế và xây dựng Trang thông tin điện tử/Cổng thông tin điện tử/Cổng Dịch vụ công"), Đ2 k1 (doanh nghiệp sản xuất phần mềm, nội dung số), k4 (tổ chức cung cấp dịch vụ công); **Đ5 k1**: trang, cổng của cơ quan, tổ chức tại Đ2 k2, k3 áp dụng tiêu chuẩn tại Phụ lục; Đ5 k2: khuyến khích tổ chức khác; Đ6 k2: chậm nhất 12 tháng từ 01/01/2021 phải nâng cấp. PL mục 3: **WCAG 1.0 "Bắt buộc đối với các cơ quan, tổ chức tại khoản 2 và khoản 3, Điều 2"**; ISO/IEC 40500:2012 (WCAG 2.0), WCAG 2.1, ATAG: khuyến nghị; mục 1–2 (TCVN 9249:2012, ISO/IEC 29138-1, ISO/IEC 24786…): khuyến nghị. TT 39/2017 mục 3.1: WCAG 2.0 khuyến nghị. Luật Người khuyết tật Đ4 k1 d (quyền tiếp cận CNTT), Đ43 k1 (Nhà nước khuyến khích phát triển CNTT dành cho NKT).
- **Áp dụng cho**: BV công dùng NSNN làm website, cổng, cổng đặt khám (BẮT BUỘC?); BV tư, PK, app thương mại (NÊN).
- **Mức**: BẮT BUỘC? (WCAG 1.0 với đơn vị sự nghiệp dùng NSNN; hiệu lực TT 26/2020 sau khi Luật CNTT hết HL chưa xác minh); NÊN (WCAG 2.1 AA cho mọi app y tế).
- **Phần mềm phải**: đạt tối thiểu WCAG 1.0 (pháp định cho BV công), nhắm WCAG 2.1 mức AA (thực hành tốt): văn bản thay thế cho ảnh, tương phản, điều khiển bằng bàn phím, nhãn form, không chỉ dùng màu để báo trạng thái; app di động hỗ trợ trình đọc màn hình (VoiceOver, TalkBack), cỡ chữ động; quy trình đặt khám không bắt buộc CAPTCHA hình ảnh duy nhất (suy luận).
- **Ghi chú / bẫy**: Luật NKT không đặt nghĩa vụ trực tiếp cho tư nhân về website; dự án sửa 6 luật (có Luật NKT) đang trình QH tháng 10/2026, cần theo dõi.

#### CHUYENKHOA-R39 — Ưu tiên khám trong xếp hàng, đặt lịch
- **Căn cứ**: Luật KCB **Đ3 k2**: "Ưu tiên khám bệnh, chữa bệnh đối với trường hợp người bệnh trong tình trạng cấp cứu, trẻ em dưới 06 tuổi, phụ nữ có thai, người khuyết tật đặc biệt nặng, người khuyết tật nặng, người từ đủ 75 tuổi trở lên, người có công với cách mạng phù hợp với đặc thù của cơ sở khám bệnh, chữa bệnh."
- **Áp dụng cho**: mọi cơ sở KCB · **Mức**: BẮT BUỘC (nguyên tắc; cách thực hiện "phù hợp với đặc thù" do cơ sở quyết định).
- **Phần mềm phải**: hệ thống lấy số, hàng đợi có cờ ưu tiên theo đúng 7 nhóm; tự gợi ý ưu tiên từ tuổi (dưới 06, từ đủ 75), thai kỳ, mức độ khuyết tật (bảng XML12 có `DANG_KHUYETTAT`, `MUC_DO_KHUYETTAT` theo TT 01/2019/TT-BLĐTBXH); ghi lý do ưu tiên để audit.

---

## 3. Pattern thiết kế

**P1. Chẩn đoán đa hệ mã có phiên bản** (R01, R02, R03)
- Bảng `code_system(id, name CHECK IN ('ICD10-TT06','YHCT-7603','YHCT-2552-PL1','YHCT-2552-PL2','HUYET-2552','KT-TT23-PL01','KT-TT23-PL02',…), source_doc, version, valid_from, valid_to)`; `code(code_system_id, code, display_vi, parent_code, status, inactive_from)`; `code_map(from_system, from_code, to_system, to_code, map_type CHECK IN ('equivalent','broader'), source_doc, valid_from)` (YHCT 7603 ↔ ICD-10).
- `encounter_diagnosis(encounter_id, system CHECK IN ('YHHD','YHCT'), role CHECK IN ('main','secondary'), code, code_system_version, display_snapshot, timepoint CHECK IN ('referral','opd','discharge'))`; ràng buộc `UNIQUE(encounter_id, system, timepoint) WHERE role='main'`.
- Chẩn đoán YHCT mở rộng: `tcm_diagnosis_detail(encounter_id, bat_cuong[], nguyen_nhan[], tang_phu[], kinh_lac[], the_lam_sang)` lưu mã PL I, PL II QĐ 2552.
- Hàm `xml_ma_benh_yhct(encounter)` sinh chuỗi `chính;kèm…` và tên bảng kê `Tên YHCT [Tên YHHĐ]`.
- Đánh đổi: thêm bảng, đổi lại nạp đợt mã mới (QĐ 1978, đợt 2 của 2552) không phải sửa code.

**P2. Master thuốc YHCT và công thức chế phẩm** (R05, R06, R07)
- `tcm_product(id, kind CHECK IN ('thuoc_duoc_lieu','thuoc_co_truyen','thuoc_ket_hop','duoc_lieu','vi_thuoc','che_pham_tu_bao_che'), name_by_ingredients, brand_name, route_group CHECK IN ('uong','dung_ngoai',…), reg_no, bhyt_list_ref, bhyt_condition JSONB, valid_from, valid_to)`; `tcm_indication(product_id, icd10, yhct_code, source CHECK IN ('to_HDSD','HD_BYT'))`.
- `formula(id, product_id, version, approved_by, approved_at, sent_to_bhxh_at, unit_cost)`; `formula_line(formula_id, ingredient_id, qty, in_bhyt_list BOOL, che_bien_codes[])`.
- `recall(product_id, lot_no NULL, effective_from, scope, doc_ref)` → loại khỏi thanh toán theo ngày dùng.
- Ràng buộc bán ra ngoài: `CHECK (kind <> 'che_pham_tu_bao_che' OR channel = 'internal')`.

**P3. Mẫu HSBA chuyên khoa và thành phần vẽ** (R09, R10, R12)
- `record_template(code '01/BV1'…'29/BV1','01/BV2'…'53/BV2', specialty, allowed_facility_types[], legal_source='TT32', version)`; `facility_template_enable(facility_id, template_code)` kiểm tra với phạm vi chuyên môn.
- Trường kiểu `drawing`: lưu SVG hoặc PNG + `base_diagram_id` + `author_id`, `drawn_at`; đưa vào gói PDF ký.
- Trường mở rộng chuyên khoa đặt trong `extension JSONB`, không đè trường của mẫu.

**P4. Cổng đồng ý (consent gate)** (R11, R14, R15)
- `consent(id, patient_id, encounter_id, type CHECK IN ('01/BV2','40/BV2','41/BV2','45/BV2','46/BV2','48/BV2','49/BV2','marketing_photo','ivf_donor',…), signer_role CHECK IN ('patient','representative'), representative_relation, checklist JSONB, signed_doc_id, signed_at, revoked_at)`.
- Trigger: không chuyển `procedure.status` sang `in_progress` nếu thiếu `consent(type='01/BV2')` hợp lệ, trừ `emergency_override(reason, approver)`.
- Ảnh lâm sàng: `clinical_photo(id, encounter_id, phase CHECK IN ('before','during','after'), storage_ref, retention_class)`; view `marketing_photo` chỉ trả ảnh có `consent(type='marketing_photo')` chưa thu hồi.

**P5. Lưu trữ theo loại hồ sơ chuyên khoa** (R13, R15, R24)
- Mở rộng `retention_policy` của EMR-R22: thêm `PTTM_20Y` (mục 43), `IVF_PERMANENT` (211), `GAMETE_DONATION_PERMANENT` (214), `GENDER_REASSIGN_70Y` (215), `IMMUNIZATION_RECORD` (chưa có dòng, đặt ≥ 10 năm, cờ "cần xác minh").
- Tự nâng lớp khi phát sinh thủ thuật có cờ `is_cosmetic_surgery`.

**P6. Giả danh người cho giao tử, phôi** (R15)
- Schema riêng `ivf_identity` (mã hóa cột, khóa trong KMS, quyền chỉ cho vai "IVF registrar"); bảng nghiệp vụ chỉ chứa `donor_pseudonym`, `ethnicity`, đặc điểm; mọi truy vấn ánh xạ ghi `access_log` có lý do.
- Đánh đổi: khó tra cứu khi có yêu cầu pháp lý; cần quy trình "break-glass" có phê duyệt.

**P7. Đồng bộ tiêm chủng theo sự kiện** (R16, R17, R18, R21)
- `immunization_subject(id, national_id, national_subject_id, … 44 trường QĐ 3891, dedup_key)`, `immunization_event(id, subject_id, vaccine_id, antigen_codes[], dose_no, program, site_id, lot_no, screening_id, given_at, observed_until, aefi_flag)`.
- Outbox: `outbox(aggregate='immunization_event', payload, status, attempt, sent_at, ack_id)`; SLA mục tiêu "thời gian thực" (ví dụ < 5 phút) có cảnh báo; dashboard độ trễ.
- `aefi_report(id, event_id, severity CHECK IN ('thong_thuong','tai_bien_nang'), detected_at, deadline_at = detected_at + 24h, sent_soy_at, sent_cdc_at)`; trigger khóa `vaccine_lot` khi `tai_bien_nang`.
- Bộ lọc loại trừ đối tượng BCA, BQP khỏi outbox.

**P8. Kiểm duyệt nội dung quảng cáo và đánh giá** (R26–R33)
- `promo_content(id, facility_id, type CHECK IN ('service','drug','supplement','device','kol_post'), body, media[], required_fields_ok BOOL, approval_status, approved_by_professional_id, published_at, unpublished_at)`; trước khi publish chạy `lint_rules`: trường bắt buộc NĐ 342 Đ9, từ cấm (Luật QC Đ8 k11; NĐ 163 Đ104 k6), cờ `rx_only`, từ khóa giới tính thai, ảnh nhân viên y tế trong quảng cáo thuốc, dịch vụ ngoài `facility_scope`.
- `ad_record(…đủ trường NĐ 342 Đ19 k2, last_shown_at, retain_until = last_shown_at + 3y)`; `takedown_request(id, authority, received_at, ad_id, removed_at, CHECK (removed_at - received_at <= interval '24 hours'))` (ràng buộc mềm, cảnh báo).
- `review(id, author_account_id, verified_encounter_id NULL, rating, text, status CHECK IN ('visible','held_incident_allegation','removed_illegal'), moderation_reason)`; trang công khai `ranking_criteria`.

**P9. Văn bản hai ngôn ngữ có bản tiếng Việt là bản chính** (R34, R35, R36)
- `clinical_text(id, lang_original, text_original, text_vi, translator_id NULL, translated_at)`; với `practitioner.is_foreign = true` bắt buộc `text_vi` và `translator_id` trước khi ký; đơn thuốc thêm `signature(role='translator')`.
- `encounter_language(encounter_id, preferred_language, interpreter_source, interpreter_name, interpreter_license_no)`.

**P10. Chất lượng dữ liệu tiếng Việt và tiếp cận** (R37, R38, R39)
- Middleware chuẩn hóa Unicode NFC ở tầng nhập; cột so khớp `name_search` bỏ dấu để tìm trùng.
- Pipeline CI chạy kiểm tra accessibility tự động (axe-core hoặc tương đương) trên các luồng đặt khám, xem kết quả; danh sách kiểm tra thủ công với trình đọc màn hình.
- `queue_ticket(priority_reason CHECK IN ('cap_cuu','duoi_6_tuoi','co_thai','nkt_dac_biet_nang','nkt_nang','tu_75_tuoi','nguoi_co_cong'))`.

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| CHUYENKHOA-A01 | R01 | Mở 5 bệnh án YHCT nội trú, ngoại trú, nhi. So trường với 18, 19, 20/BV1 (hai cột chẩn đoán có mã, tứ chẩn, biện chứng, pháp, phương). Tìm mẫu theo QĐ 1941/2019 | Bảng so khớp trường, bản in | Bắt buộc |
| CHUYENKHOA-A02 | R02 | SQL đếm `MA_BENH_YHCT` rỗng trong hồ sơ có khoa YHCT; tra 05 mã PL 02 QĐ 1978 trong dữ liệu sau 01/07/2026; kiểm `U50.351` ánh xạ A97 (không còn A90) | Kết quả truy vấn, file XML mẫu | Bắt buộc |
| CHUYENKHOA-A03 | R02 | Xem tên bệnh trên bảng kê 01/KBCB của ca YHCT có dạng `Tên YHCT [Tên YHHĐ]` | Bảng kê in | Bắt buộc |
| CHUYENKHOA-A04 | R03 | Hỏi vendor có nạp QĐ 2552 (4 PL) chưa; chẩn đoán bát cương, tạng phủ là text tự do hay mã; thử chỉ định kỹ thuật có dấu * (mã 3810426–3820489) | Ảnh màn hình danh mục, kết quả thử | Nên (Bắt buộc?) |
| CHUYENKHOA-A05 | R04 | Thử chỉ định một kỹ thuật YHCT chỉ có ở PL 02 TT 23 trước 01/01/2028 | Bị chặn hay không | Bắt buộc |
| CHUYENKHOA-A06 | R05 | Xem master thuốc YHCT: tên theo thành phần hay tên thương mại; đường dùng; điều kiện thanh toán có ngày hiệu lực; danh mục TT 05/2015 còn trong hệ thống | Xuất danh mục, cấu hình | Bắt buộc |
| CHUYENKHOA-A07 | R06 | Tạo đơn bán ra ngoài cho một chế phẩm tự bào chế; xem công thức có cờ ngoài danh mục BHYT, số phê duyệt chi phí, ngày gửi BHXH; trường `MA_PP_CHEBIEN` trong XML2 | Kết quả thử, hồ sơ công thức | Bắt buộc |
| CHUYENKHOA-A08 | R07, R08 | Kê thuốc YHCT cho chẩn đoán ngoài chỉ định; dùng tài khoản y sĩ, lương y chỉ định kết hợp | Cảnh báo, chặn | Bắt buộc (BHYT) / Nên (CDS) |
| CHUYENKHOA-A09 | R09, R10 | Liệt kê loại bệnh án PK chuyên khoa đang dùng; mẫu RHM có trường hình vẽ không; trường chuyên khoa thêm có đè trường mẫu không | Danh sách mẫu, bản in | Bắt buộc |
| CHUYENKHOA-A10 | R11 | Thử bắt đầu phiếu phẫu thuật, thủ thuật (kể cả tiêm filler) khi chưa có 01/BV2; xem người ký là đại diện có ghi quan hệ | Kết quả thử, mẫu ký | Bắt buộc |
| CHUYENKHOA-A11 | R13 | Xem cấu hình loại hình cơ sở và danh mục dịch vụ thẩm mỹ xâm lấn; SQL phân bố `retention_class` của HSBA có PTTM | Cấu hình, truy vấn | Bắt buộc |
| CHUYENKHOA-A12 | R14 | Tìm ảnh người bệnh trên website, fanpage; đối chiếu bản ghi đồng ý dùng cho truyền thông | Danh sách ảnh, bản ghi đồng ý | Bắt buộc |
| CHUYENKHOA-A13 | R15 | Với BV có IVF: ai đọc được bảng danh tính người cho; log truy cập; `retention_class` vĩnh viễn | Ma trận quyền, log | Bắt buộc |
| CHUYENKHOA-A14 | R16, R17 | Đo độ trễ từ lúc xác nhận mũi tiêm tới ack của Hệ thống quốc gia trên 100 mũi gần nhất; tìm đối tượng trùng (cùng số định danh) | Log outbox, truy vấn trùng | Bắt buộc |
| CHUYENKHOA-A15 | R18 | So schema đối tượng tiêm với 44 trường QĐ 3891; thử gửi thiếu 1 trong 20 trường bắt buộc | Bảng so khớp, kết quả thử | Bắt buộc? |
| CHUYENKHOA-A16 | R19, R20 | Thử xác nhận mũi tiêm khi chưa xong sàng lọc; xem có ghi giờ kết thúc theo dõi 30 phút; người được tiêm nhận sổ hoặc sổ điện tử | Kết quả thử, mẫu sổ | Bắt buộc |
| CHUYENKHOA-A17 | R21 | Diễn tập ghi nhận tai biến nặng: buổi tiêm có bị khóa, lô có bị chặn, báo cáo Sở Y tế và CDC có trong 24 giờ | Biên bản diễn tập, log | Bắt buộc |
| CHUYENKHOA-A18 | R22 | Lấy báo cáo tháng gần nhất: ngày gửi so với "trước ngày 03 tháng sau" | Báo cáo, thời điểm gửi | Bắt buộc |
| CHUYENKHOA-A19 | R23, R24 | Bảng giá: vắc xin TCMR có bị tính tiền; buổi tiêm mở tại điểm chưa công bố đủ điều kiện | Cấu hình giá, danh sách điểm | Bắt buộc |
| CHUYENKHOA-A20 | R26, R27 | Duyệt 20 bài quảng cáo, trang dịch vụ: đủ 5 trường NĐ 342 Đ9; dịch vụ nào ngoài phạm vi chuyên môn trong GPHĐ | Ảnh chụp, bảng đối chiếu GPHĐ | Bắt buộc |
| CHUYENKHOA-A21 | R28, R29 | Kiểm tra nhãn "Quảng cáo" trên vị trí trả phí, nút tắt popup, luồng báo vi phạm; xem log yêu cầu gỡ và thời gian gỡ; truy vấn `ad_record` 3 năm | Ảnh chụp, log | Bắt buộc |
| CHUYENKHOA-A22 | R30, R31 | Thử tạo banner cho thuốc kê đơn; xem quảng cáo thuốc có câu "Đọc kỹ hướng dẫn sử dụng trước khi dùng" và số xác nhận; danh mục thuốc có lẫn thực phẩm bảo vệ sức khỏe | Kết quả thử, ảnh chụp | Bắt buộc |
| CHUYENKHOA-A23 | R32 | Đọc trang tiêu chí xếp hạng; thống kê review bị ẩn và lý do; thử đăng review quy kết sự cố y khoa; bài KOL có nhãn tài trợ | Ảnh chụp, log kiểm duyệt | Bắt buộc |
| CHUYENKHOA-A24 | R33 | Tìm từ khóa "giới tính thai", "sinh con trai" trong nội dung đã đăng; nền tảng có livestream: bản ghi cũ 11 tháng còn không | Kết quả tìm, file lưu | Bắt buộc |
| CHUYENKHOA-A25 | R34, R36 | Với người hành nghề nước ngoài: đơn thuốc có bản tiếng Việt và chữ ký người phiên dịch; hồ sơ nhân sự có ngôn ngữ đăng ký | Bản in đơn, hồ sơ | Bắt buộc |
| CHUYENKHOA-A26 | R35 | Lượt khám người bệnh nước ngoài, dân tộc thiểu số: có ghi nhu cầu ngôn ngữ và người phiên dịch | Bản ghi lượt khám | Bắt buộc (cơ sở) / Nên (phần mềm) |
| CHUYENKHOA-A27 | R37 | Kiểm encoding DB, API, XML (UTF-8); tìm bản ghi tên trùng do khác dạng Unicode (so sánh sau chuẩn hóa NFC) | Kết quả truy vấn | Bắt buộc? / Nên |
| CHUYENKHOA-A28 | R38 | Chạy công cụ kiểm tra tự động trên trang đặt khám; thử với VoiceOver, TalkBack; ghi mức WCAG đạt | Báo cáo kiểm tra | Bắt buộc? (BV công) / Nên |
| CHUYENKHOA-A29 | R39 | Lấy số cho người 75 tuổi, trẻ 5 tuổi, phụ nữ có thai: có cờ ưu tiên và lý do | Ảnh chụp hàng đợi | Bắt buộc |

---

## 5. Dòng thời gian & đối tượng

| Ngày | Trạng thái | Sự kiện | Ai phải làm | Căn cứ |
|---|---|---|---|---|
| 01/01/2024 | Đã qua | Mẫu HSBA TT 32 (gồm 18–20/BV1 YHCT, 27–29/BV1 PHCN) thay QĐ 1941/2019, QĐ 3730/2021 | Mọi cơ sở KCB, vendor | TT 32 Đ53 |
| 01/07/2025 | Đã qua | TT 33/2025: PTTM 20 năm, IVF và hiến giao tử vĩnh viễn | Mọi cơ sở | TT 33 Đ2 |
| 12/08/2025 | Đã qua | QĐ 2552 mã dùng chung thuật ngữ YHCT đợt 1 | Cơ sở có YHCT, vendor | QĐ 2552 Đ4 |
| 01/09/2025 | Đã qua | TT 27/2025 HL; TT 05/2015 Đ4–6 và TT 27/2020 hết HL | Cơ sở BHYT | TT 27 Đ20 |
| 18/12/2025 | Đã qua | QĐ 3891 danh mục 44 trường tiêm chủng | Cơ sở tiêm | QĐ 3891 |
| 01/01/2026 | Đã qua | Luật 75/2025 sửa Luật Quảng cáo (gỡ 24 giờ, KOL) | Mọi bên quảng cáo trên mạng | Luật 75 |
| 15/02/2026 | Đã qua | NĐ 342/2025 HL; TT 03/2026 bỏ thủ tục xác nhận nội dung quảng cáo dịch vụ KCB | Cơ sở KCB, nền tảng | NĐ 342; TT 03/2026 |
| 15/05/2026 | Đã qua | NĐ 87/2026 (phạt quảng cáo) và NĐ 90/2026 (phạt y tế) HL | Tất cả | NĐ 87; NĐ 90 Đ115 |
| 01/07/2026 | Đã qua | Luật Phòng bệnh, NĐ 165, TT 13/2026, TT 15/2026, Luật TMĐT, NĐ 248, TT 06/2026 HL; QĐ 1978 (mã YHCT) áp dụng; Luật PCBTN, NĐ 104 (trừ Đ9–11), TT 34/2018, TT 54/2015 hết HL | Cơ sở tiêm, cơ sở BHYT, nền tảng | các văn bản nêu |
| 15/07/2026 | Đã qua | QĐ 2149 sửa mốc QTKT YHCT | Cơ sở có YHCT | QĐ 2149 |
| khoảng 30/08/2026 | Đã qua | Hết 60 ngày chuyển tiếp gửi lại dữ liệu chuẩn hóa mã YHCT (suy luận cách đếm) | Cơ sở BHYT | QĐ 1978 Đ2 |
| 31/12/2026 | Sắp tới | Hạn HSBA điện tử với PK, cơ sở không phải BV (gồm PK chuyên khoa có điều trị theo đợt) | PK | TT 13/2025 Đ4 k2 b (EMR-R01) |
| 01/01/2027 | Sắp tới | Xác thực danh tính người bán, người livestream trên nền tảng (theo lượt phụ) | Nền tảng TMĐT | NĐ 248/2026 |
| 30/06/2027 | Sắp tới | Hết HL Đ9–11 NĐ 104/2016 (điều kiện kinh doanh dịch vụ tiêm, công bố) | Cơ sở tiêm | NĐ 165 Đ94 k5 |
| 01/07/2027 | Sắp tới | NĐ 165 Đ49 (điều kiện cơ sở tiêm chủng mới) có HL | Cơ sở tiêm | NĐ 165 Đ94 k2 |
| 31/12/2027 / 01/01/2028 | Sắp tới | TT 23 PL 01 hết; PL 02 và kỹ thuật YHCT chỉ có ở PL 02 bắt đầu | Mọi cơ sở, vendor | TT 25/2026; QĐ 2149 |
| 31/12/2031 / 01/01/2032 | Xa | Hết áp dụng quy định ngôn ngữ cũ với người nước ngoài; bắt đầu điều kiện năng lực tiếng Việt | Người hành nghề nước ngoài, cơ sở | Luật KCB Đ121 k4, Đ120 k4 |
| Chưa định | Theo dõi | TT danh mục thuốc YHCT BHYT mới (kích hoạt Đ9–11 TT 27); chuẩn API Hệ thống tiêm chủng; QĐ 2552 đợt 2; Luật sửa 6 luật (có Luật NKT) | BYT, Cục Phòng bệnh, QH | — |

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuỗi thay thế**

| Cũ | → | Mới | Từ ngày | Ghi chú |
|---|---|---|---|---|
| QĐ 1941/QĐ-BYT (2019) mẫu bệnh án YHCT | → | TT 32/2023 mẫu 18, 19, 20/BV1 + PL XXIX mục 54, 55 | 01/01/2024 | TT 32 Đ53 k2 h |
| QĐ 3730/QĐ-BYT (2021) mẫu PHCN | → | TT 32/2023 mẫu 27, 28, 29/BV1 | 01/01/2024 | TT 32 Đ53 k2 i |
| QĐ 6061/QĐ-BYT (2017, bản 5) | → | QĐ 7603/QĐ-BYT (2018, bản 6) PL 07.1 mã bệnh YHCT | 15/01/2019 | xem BHYT-DATA |
| QĐ 7603 PL 07.1 (một phần) | → | QĐ 1978/QĐ-BYT (30 mã sửa/bổ sung; 05 mã không dùng) | 01/07/2026 | Phần khác giữ nguyên |
| TT 05/2015 Đ4–6, TT 27/2020 | → | TT 27/2025 | 01/09/2025 | Danh mục TT 05/2015 còn dùng tới TT danh mục mới |
| QĐ 486/QĐ-BYT (2026) Đ3 | → | QĐ 2149/QĐ-BYT | 15/07/2026 | Kỹ thuật PL 02: từ 01/01/2028 |
| Luật PCBTN 03/2007 | → | Luật Phòng bệnh 114/2025 | 01/07/2026 | Luật 114 Đ45 k2 |
| NĐ 104/2016, NĐ 13/2024 | → | NĐ 165/2026 | 01/07/2026 | Đ9–11 NĐ 104 giữ tới 30/06/2027 |
| TT 34/2018, TT 24/2018, TT 05/2020, TT 52/2025 | → | TT 13/2026 | 01/07/2026 | TT 13 Đ27 k2 |
| TT 54/2015 (báo cáo BTN) | → | TT 15/2026 | 01/07/2026 | TT 15 Đ65 k2 (giải quyết MT-31) |
| NĐ 181/2013, NĐ 70/2021 | → | NĐ 342/2025 | 15/02/2026 | Đ3 NĐ 181 đã hết HL trước đó do NĐ 163 |
| TT 09/2015/TT-BYT (xác nhận nội dung QC) | → | Bãi bỏ phần lớn bởi TT 03/2026 | 15/02/2026 | Còn phần thực phẩm, sữa trẻ em |
| NĐ 38/2021 (sửa bởi NĐ 129/2021, NĐ 128/2022) | → | NĐ 87/2026 | 15/05/2026 | Phạt quảng cáo |
| NĐ 117/2020 | → | NĐ 90/2026 | 15/05/2026 | Phạt y tế (gồm tiêm chủng Đ9) |
| NĐ 54/2017, NĐ 88/2023; TT 07/2018 | → | NĐ 163/2025; TT 31/2025 | 01/07/2025 | Dược, thông tin thuốc |
| NĐ 52/2013, NĐ 85/2021 | → | Luật TMĐT 122/2025 + NĐ 248/2026 | 01/07/2026 | — |
| TT 28/2009/TT-BTTTT | → | TT 26/2020/TT-BTTTT | 01/01/2021 | Tiếp cận cho NKT |
| TT 22/2013/TT-BTTTT | → | TT 39/2017/TT-BTTTT | 01/07/2018 | Danh mục tiêu chuẩn CQNN |

**Bẫy trích dẫn**
1. Hành vi cấm quảng cáo KCB là **Luật KCB Đ7 k20** (và k17, k21), không phải "Điều 12".
2. **NĐ 90/2026 không phạt quảng cáo thuốc, quảng cáo dịch vụ KCB**; dùng NĐ 87/2026 (Đ49, Đ69, Đ75…). NĐ 90 chỉ phạt các hành vi y tế liên quan (Đ38 k5 n, k7 h; Đ59; Đ67).
3. "Cập nhật dữ liệu tiêm chủng trong 24 giờ" **không có căn cứ**. Mốc 24 giờ chỉ dành cho báo cáo tai biến nặng (TT 13 Đ15 k5 a) và mũi viêm gan B sơ sinh (Đ26 k1). Cập nhật đối tượng: "kịp thời" (Đ10); hệ thống riêng: "thời gian thực" (Đ25 k8).
4. TT 34/2018 và NĐ 104/2016 đã hết HL; tài liệu, phần mềm còn trích là lỗi thời. QĐ 3421/2017 và QĐ 3891/2025 dựa trên căn cứ đã hết HL: trích kèm cảnh báo.
5. PL IV QĐ 2552 có tiêu đề "thực hiện đến ngày 30/06/2026"; mốc của TT 23 PL 01 đã lùi tới 31/12/2027 (TT 25/2026). Không suy ra PL IV hết hiệu lực.
6. QĐ 1978/2026 **không** thay toàn bộ danh mục mã bệnh YHCT; chỉ sửa 30 dòng và liệt kê 05 mã không dùng.
7. TT 27/2025 là thông tư nguyên tắc; danh mục thuốc YHCT BHYT hiện vẫn theo TT 05/2015 (VBHN 13/VBHN-BYT) cho tới khi có TT danh mục mới.
8. "HSBA thẩm mỹ 20 năm chỉ áp cho bệnh viện" là sai: TT 33 quy định theo loại hồ sơ. Ngược lại "mọi hồ sơ thẩm mỹ 20 năm" cũng không chính xác: mục 43 chỉ nêu phẫu thuật thẩm mỹ.
9. TT 39/2017 bắt buộc **WCAG** là sai: WCAG 2.0 chỉ "khuyến nghị" trong TT 39. Mức bắt buộc duy nhất tìm thấy là **WCAG 1.0** trong TT 26/2020, chỉ với CQNN và đơn vị sự nghiệp dùng NSNN làm website, cổng.
10. Luật KCB Đ121 k4 giữ quy định ngôn ngữ của Luật 2009 với người nước ngoài tới hết 31/12/2031; đừng trích Đ21 như thể là quy định duy nhất trong giai đoạn này.

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Bản PL 07.1 QĐ 7603 gốc** (toàn bộ danh mục mã bệnh YHCT và cặp ICD-10) chưa đọc; mới có phần sửa của QĐ 1978. Cần tải bản BYT hoặc BHXH. Số lượng mã YHCT (thứ cấp nêu 4.144) chưa xác minh.
2. **Tính bắt buộc của QĐ 2552/2025**: không hạn, không chế tài, không trường XML. Hỏi Cục QL YDCT: có lộ trình bắt buộc dùng mã thể lâm sàng, bát cương trong HSBA điện tử và liên thông Sổ SKĐT không; khi nào có đợt 2.
3. **TT danh mục thuốc YHCT BHYT mới** (kích hoạt Đ9–11 TT 27/2025): chỉ thấy tin dự thảo (thứ cấp). TT 26/2026/TT-BYT (danh mục dược liệu, thuốc cổ truyền rủi ro trung bình) chỉ biết qua tiêu đề trên vanban, chưa đánh giá tác động phần mềm.
4. **QĐ 486/QĐ-BYT (13/02/2026)** về quy trình kỹ thuật YHCT chưa đọc nội dung (chỉ đọc QĐ 2149 sửa Đ3).
5. **Bảng chỉ tiêu QĐ 4750/3176** cho `MA_BENH_YHCT`, `MA_PP_CHEBIEN`: người viết chỉ đối chiếu bản QĐ 130 năm 2023; cần đối chiếu bản 3176 (BHYT-DATA).
6. **Chuẩn API Hệ thống quản lý thông tin tiêm chủng quốc gia** cho phần mềm riêng (TT 13 Đ15 k7, Đ25 k8): chưa có văn bản. Hỏi Cục Phòng bệnh hoặc VNCDC. Đồng thời hỏi hiệu lực QĐ 3421/2017 và QĐ 3891/2025 sau 01/07/2026, và có thay QĐ 3421 không.
7. **Thời hạn lưu hồ sơ tiêm chủng cá nhân** (sổ, phiếu sàng lọc, phản ứng sau tiêm): TT 33 không có dòng riêng. Hỏi Văn phòng BYT theo hướng dẫn cuối TT 33.
8. **Giấy xác nhận tiêm chủng điện tử trong nước** và mẫu sổ theo dõi tiêm chủng cá nhân mới: chưa thấy văn bản. TT 13/2026 chưa thấy trên datafiles; bản đang dùng do BVĐK Bạc Liêu đăng lại.
9. NĐ 90/2026 Đ9 k3 c bị OCR hỏng chữ; lượt phụ đọc qua ảnh là "không thực hiện đúng quy định về an toàn tiêm chủng, quản lý đối tượng…". Hành vi "không cập nhật dữ liệu lên Hệ thống" không có điểm riêng; xếp vào k3 c, k2 b hay k1 d là suy luận. **Cần luật sư** khi tư vấn mức phạt.
10. **Sàn đặt khám có phải "người kinh doanh dịch vụ quảng cáo trên mạng"** (NĐ 342 Đ19) khi bán vị trí nổi bật, và có thuộc Luật TMĐT khi không có thanh toán: suy luận, **cần luật sư** hoặc hỏi Bộ VHTTDL, Bộ Công Thương. TT 12/2026/TT-BVHTTDL (chi tiết Luật Quảng cáo) chỉ có nguồn thứ cấp.
11. **Ngôn ngữ trong giai đoạn chuyển tiếp** (Luật KCB Đ21 so với Đ121 k4 và Luật 2009): cần luật sư hoặc hỏi Cục QLKCB. Văn bản sửa NĐ 96/2023 (VBHN 10/VBHN-BYT 2026 theo thứ cấp là về phân cấp thủ tục) chưa đối chiếu với Đ35, Đ36, Đ40.
12. **TT 26/2020/TT-BTTTT, TT 39/2017/TT-BTTTT, QĐ 72/2002/QĐ-TTg** sau khi Luật CNTT hết HL (01/07/2026) và BTTTT sáp nhập BKHCN: mst.gov.vn còn ghi "còn hiệu lực" nhưng chưa thấy văn bản xác nhận hay thay thế theo Luật CĐS. Hỏi Bộ KH&CN.
13. **Hỗ trợ sinh sản**: NĐ 98/2016 (sửa NĐ 10/2015) chưa đọc; tác động của Luật Dân số 2025 (HL 01/07/2026) lên quy định IVF, mang thai hộ chưa xác minh. Dữ liệu di truyền, sinh sản như loại dữ liệu nhạy cảm đặc thù: giao cụm DLCN.
14. **Nha khoa, mắt**: không tìm thấy quy định phần mềm riêng (sơ đồ răng, đơn kính, chuẩn ảnh nha khoa). Đơn kính của cơ sở kính thuốc (NĐ 96 Đ57) chưa khảo sát.
15. Các điều Luật Quảng cáo, Luật Dược, NĐ 163, Luật TMĐT, Luật BVQLNTD, NĐ 87 (trừ Đ75), NĐ 248 ở mục D chủ yếu do lượt phụ đọc gốc; người viết đã đối chiếu lại Đ23 k7 Luật 75, NĐ 342 Đ9 và Đ19, NĐ 87 Đ75, TT 03/2026 Đ2. Các mức phạt khác nên đối chiếu lại trước khi đưa vào skill.
