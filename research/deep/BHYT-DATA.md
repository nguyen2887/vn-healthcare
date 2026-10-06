# BHYT-DATA — Chuẩn dữ liệu đầu ra XML BHYT & bộ mã danh mục dùng chung

> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: nửa "chuẩn dữ liệu & danh mục mã" của cụm K2 (inventory mục 5). Gồm: bộ bảng XML theo QĐ 130/QĐ-BYT và các bản sửa (4750, 3176, 1931/2026), bảng check-in, định dạng trường, thời hạn gửi theo TT 48/2017, ký số file XML; bộ mã danh mục dùng chung (QĐ 7603 → 3276/2025; QĐ 2010/2025; QĐ 1804/2026), danh mục sử dụng tại cơ sở (TT 12/2026 Đ7–8, Phụ lục II), bảng kê 01/KBCB (QĐ 697/2026), quy tắc ICD-10 (TT 06/2026) ở góc dữ liệu đầu ra. Phần giám định, quyết toán, NĐ 188 Đ66–72 chi tiết, dự thảo thay TT 48 thuộc cụm `BHYT-GD`; ở đây chỉ nhắc khi cần để giải thích chuẩn dữ liệu.
>
> **Quy ước mức xác minh**: `gốc` = đọc toàn văn có lớp text; `gốc-ảnh` = bản scan, đã đọc trực tiếp ảnh trang (giữ dấu), số và câu chữ tin được; `gốc-OCR` = OCR tesseract `eng`, mất dấu; `thứ cấp` = báo, CSDL luật tư nhân; `chưa XM` = chưa mở được. Chỗ ghi **(suy luận)** là ý kiến của người nghiên cứu, không phải câu chữ văn bản. Đây là tài liệu định hướng kỹ thuật, **không phải ý kiến pháp lý**.

---

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| QD-130-2023-BYT | 130/QĐ-BYT, 18/01/2023 | Quy định chuẩn và định dạng dữ liệu đầu ra phục vụ quản lý, giám định, thanh toán chi phí KCB và giải quyết các chế độ liên quan | Ký; kiểm thử từ 31/03/2023; chính thức 01/09/2023 (Đ4 k3–4 gốc; **mốc sau đó bị 4750 dời**) | Còn HL, đã sửa bởi 4750, 3176, 1931/2026. Thay QĐ 4210/QĐ-BYT (2017) | BV công, BV tư, PK có HĐ KCB BHYT; vendor HIS | gốc-OCR (thân QĐ, số và ngày rõ) + gốc (file XLSX 13 bảng chỉ tiêu bản 2023) | [PDF QĐ, SYT Quảng Ninh](http://soytequangninh.gov.vn/upload/1002610/20230131/130Q__signed_7a47686ff6.pdf) · [XLSX bảng chỉ tiêu](http://soytequangninh.gov.vn/upload/1002610/20230131/20230118_Chuan_du_lieu_dau_ra_FINAL_a675b931cf.xlsx) · [trang tin SYT QN](http://soytequangninh.gov.vn/menu-second/iso-9001-2008/cong-khai-tai-chinh2/cac-du-toan-va-quyet-toan-tai-chinh/trien-khai-quyet-dinh-so-130-qd-byt-ngay-18-01-2023-cua-bo-y.html) |
| QD-4750-2023-BYT | 4750/QĐ-BYT, 29/12/2023 | Sửa đổi, bổ sung QĐ 130 (thay toàn bộ Bảng chỉ tiêu; định nghĩa lại check-in) | Ký; kiểm thử từ 01/04/2024; chính thức 01/07/2024; QĐ 4210 hết HL 01/07/2024 (Đ2 k3–5, Đ3) | Còn HL (đã sửa bởi 3176) | như trên | gốc-ảnh (Đ1–Đ4 và một phần phụ lục; file 14 trang chỉ chứa phần đầu phụ lục) | [PDF, BVĐK Bạc Liêu](http://bvdkbaclieu.gov.vn/upload/1000079/20240107/252QUY_1_c1005feda7.pdf) |
| QD-3176-2024-BYT | 3176/QĐ-BYT, 29/10/2024 | Sửa đổi, bổ sung **tạm thời** các Bảng chỉ tiêu của QĐ 4750 | Ký; triển khai đồng bộ 01/01/2025 (Đ3) | Còn HL; là bản "đang chạy" trên Cổng (BHXH gọi endpoint `...QD3176`) | như trên | thứ cấp (thân QĐ, caselaw); phụ lục: chưa đọc bản gốc, chỉ có danh sách thẻ XML qua tài liệu BHXH | [caselaw, thứ cấp](https://caselaw.vn/van-ban-phap-luat/508520-quyet-dinh-so-3176-qd-byt-ngay-29-10-2024-cua-bo-truong-bo-y-te-sua-doi-quyet-dinh-4750-qd-byt-sua-doi-quyet-dinh-130-qd-byt-quy-dinh-chuan-va-dinh-dang-du-lieu-dau-ra-phuc-vu-viec-quan-ly-giam-dinh-thanh-toan-chi-phi-kham-benh-chua-benh-va-giai-quyet-cac-che-do-lien-quan) |
| QD-1931-2026-BYT | 1931/QĐ-BYT, **29/06/2026** (≠ QĐ 1931/QĐ-BYT năm 2016 về tẩy sán lá gan) | Sửa đổi, bổ sung chuẩn dữ liệu đầu ra: `MUC_HUONG` tối đa 04 ký tự; quy tắc ghi `SO_DANG_KY` cho thuốc hiếm UBND tỉnh cấp phép nhập khẩu | 01/07/2026 | Còn HL (theo nguồn thứ cấp) | như trên | **thứ cấp (1 nguồn báo)**; chưa tìm được bản gốc | [suckhoetreem, thứ cấp](https://suckhoetreem.vn/cuoc-song-so/cap-nhat-chuan-du-lieu-phuc-vu-giam-dinh-kham-chua-benh-va-thanh-toan-bhyt-tu-01-7-2026-131048.html) |
| CV-BHXH-LT3176 | Công văn …/BHXH-CNTT (số, ngày để trống trên bản đăng), Phụ lục 01 "Hướng dẫn liên thông dữ liệu theo QĐ 3176" (tên file ghi "ký số 07012026") | Đăng ký chứng thư số, API gửi check-in và hồ sơ XML, cấu trúc XML0–XML15, chữ ký `CHUKYDONVI` SHA256 | 2026 (chưa rõ ngày) | Hướng dẫn kỹ thuật của BHXH, không phải QPPL | cơ sở KCB BHYT, vendor | gốc (PDF có text) nhưng **số hiệu CV chưa xác minh**; đăng lại trên site UBND xã | [PDF, khanhcuong.quangngai.gov.vn](https://khanhcuong.quangngai.gov.vn/upload/2007018/20260128/PL01_li%C3%AAn%20th%C3%B4ng%20d%E1%BB%AF%20li%E1%BB%87u_3176_k%C3%BD%20s%E1%BB%91_07012026%20(1).pdf) |
| TT-48-2017-BYT | 48/2017/TT-BYT, 28/12/2017 | Trích chuyển dữ liệu điện tử trong quản lý và thanh toán chi phí KCB BHYT | 01/03/2018 (Đ14) | Còn HL (vẫn là căn cứ của QĐ 3276/2025 và QĐ 1804/2026). Có dự thảo thay, dự kiến 01/01/2027 | cơ sở KCB BHYT | gốc-ảnh (Đ2–Đ8), gốc-OCR (Đ9–Đ15) | [PDF ký số BYT, SYT Hà Tĩnh](https://soyte.hatinh.gov.vn/upload/1000030/20171027/4e5899d541ea00e83dd2fce1579631cdtt-2017-48-1_1.pdf) |
| QD-7603-2018-BYT | 7603/QĐ-BYT, **25/12/2018** | Bộ mã danh mục dùng chung áp dụng trong quản lý KCB và thanh toán BHYT (phiên bản số 6), 11 danh mục; thay QĐ 6061/QĐ-BYT (bản 5) | Phần mềm hoàn thiện từ 15/01/2019 | Còn HL **một phần**: PL01–04 bị QĐ 2010 bãi bỏ; PL11 còn dùng tạm cho chỉ số CLS chưa có trong QĐ 1227 | cơ sở KCB BHYT | gốc (ngày và tình trạng qua QĐ 2010 gốc và TT 12 gốc); thân QĐ chưa đọc | [tin BHXH VN](https://baohiemxahoi.gov.vn/gioithieu/Pages/gioi-thieu-chung.aspx?CateID=0&ItemID=11950) |
| QD-824-2023-BYT | 824/QĐ-BYT, 15/02/2023 | Bổ sung 6 danh mục mã dùng chung | — | Còn HL **một phần**: PL1 (loại hình KCB) bãi bỏ từ 01/08/2026 (QĐ 1804); PL2 (đối tượng KCB) bãi bỏ bởi QĐ 2010; PL5 (xăng dầu) bãi bỏ bởi QĐ 3276. PL3, PL4, PL6 (theo thứ cấp: PP chế biến vị thuốc YHCT, thuốc bổ sung TT 20/2022, đối tượng GĐYK) chưa thấy bị bãi bỏ | cơ sở KCB BHYT | gốc (các lệnh bãi bỏ trong QĐ 2010, 3276, 1804); nội dung PL3, 4, 6: thứ cấp, chưa mở | — |
| QD-2010-2025-BYT | 2010/QĐ-BYT, 19/06/2025 | Ban hành tạm thời 6 danh mục mã dùng chung: PL1 DVKT, PL2 khám bệnh, PL3 tiền giường, PL4 ngày giường ban ngày (hóa-xạ trị, PHCN, YHCT), PL5 đối tượng KCB, PL6 mã khoa | Ký; cập nhật phần mềm chậm nhất 01/08/2025 (Đ5) | Còn HL **một phần**: PL5 bãi bỏ bởi QĐ 3276 (17/10/2025); PL6 bãi bỏ từ 01/08/2026 (QĐ 1804) | cơ sở KCB BHYT | gốc (PDF 1.068 trang có text) | [PDF, BVĐK Bạc Liêu](https://bvdkbaclieu.gov.vn/upload/1000079/20250715/583_Quyet_dinh-2010-QD-BYT_256a10e6ec.pdf) |
| QD-3276-2025-BYT | 3276/QĐ-BYT, 17/10/2025 | Danh mục mã đối tượng đến KCB (`MA_DOITUONG_KCB`, 27 dòng, kèm cột `MUC_HUONG`) và mã nhiên liệu (`MA_XANG_DAU`) | Ký; cho phép gửi lại hồ sơ từ 01/07/2025; chuyển tiếp đến 31/12/2025 | Còn HL | cơ sở KCB BHYT | gốc | [PDF xdcs.cdnchinhphu.vn](https://xdcs.cdnchinhphu.vn/446259493575335936/2025/10/27/3276-1761531834581496757967.pdf) |
| QD-1804-2026-BYT | 1804/QĐ-BYT, 19/06/2026 | Danh mục mã loại hình KCB (`MA_LOAI_KCB`, 16 mã) và mã khoa (`MA_KHOA`, 61 dòng) | Ký; thực hiện chậm nhất 01/08/2026 | Còn HL | cơ sở KCB BHYT | gốc | [PDF đính kèm tin BHXH](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26715/QD%201804%20BYT.pdf) · [tin BHXH](https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=26715&CateID=169) |
| QD-1227-2025-BYT (**mới**) | 1227/QĐ-BYT, 11/04/2025 | Danh mục mã dùng chung đối với kỹ thuật, thuật ngữ chỉ số cận lâm sàng (Đợt 1) | Ký | Còn HL; QĐ 2010 Đ3 bắt dùng mã chỉ số này cho XML4 | mọi cơ sở KCB (theo tin báo); XML4 cho cơ sở BHYT | gốc (dẫn chiếu trong QĐ 2010 Đ3); nội dung chưa đọc | — |
| QD-697-2026-BYT | 697/QĐ-BYT, 19/03/2026 | Mẫu bảng kê chi phí KCB + Phụ lục hướng dẫn kỹ thuật ghi bảng kê; thay QĐ 6556/QĐ-BYT (30/10/2018) | Ký; phần mềm nâng cấp chậm nhất 01/07/2026 (Đ4 k1) | Còn HL | **mọi** cơ sở KCB (bảng kê dùng cho mọi người bệnh; phần hướng dẫn BHYT áp cho người có thẻ) | gốc | [PDF QĐ (file trên BHXH tên "QĐ 967.pdf")](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26339/Q%C4%90%20967.pdf) · [PDF Phụ lục hướng dẫn](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26339/PL%20huong%20dan.pdf) |
| TT-12-2026-BTC | 12/2026/TT-BTC, 10/02/2026 | Giám định chi phí KCB BHYT, biểu mẫu thanh toán, quyết toán (phần liên quan: Đ5 k1, Đ7, Đ8, Đ9 k1, Phụ lục II Mẫu 01–06/DM) | (xem cụm BHYT-GD) | Còn HL | cơ sở KCB BHYT | gốc-ảnh (Đ5–Đ9, Phụ lục II trang 31–32) | [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-btc.pdf) |
| TT-06-2026-BYT | 06/2026/TT-BYT, 02/04/2026 | Mã hóa bệnh tật, nguyên nhân tử vong theo ICD-10 | 01/07/2026; Đ5 k2, k3 từ 01/06/2026 | Còn HL | mọi cơ sở KCB | gốc | [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf) |
| ND-188-2025 | 188/2025/NĐ-CP, 01/07/2025 | Hướng dẫn Luật BHYT (phần liên quan: Đ68 k1, k5; Đ69 k1, k8 d, k9; Đ70) | 15/08/2025 (một số điều 01/07/2025) | Còn HL | cơ sở KCB BHYT | gốc-ảnh (tr. 68–71) | [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/188-ndcp.signed.pdf) |
| DT-TT48 | Dự thảo TT ứng dụng CNTT, CĐS, chia sẻ dữ liệu trong BHYT (thay TT 48/2017) | Phạm vi theo báo: bộ mã dùng chung, chuẩn và định dạng dữ liệu, ký số dữ liệu chi phí; gửi trong 03 giờ; 15 ngày đối chiếu | Lấy ý kiến đến 07/10/2026; dự kiến 01/01/2027 | Dự thảo | cơ sở KCB BHYT | thứ cấp | [vtv, thứ cấp](https://vtv.vn/de-xuat-co-so-y-te-phai-gui-du-lieu-bhyt-trong-vong-3-gio-sau-kham-cham-nhieu-lan-co-the-bi-xu-phat-100261001082022915.htm) |

Văn bản tham chiếu nhỏ được dẫn trong các bản gốc trên (chưa đọc riêng, chỉ ghi để truy vết): QĐ 4905/QĐ-BYT 21/10/2019 và QĐ 5937/QĐ-BYT 30/12/2021 (sửa 7603; PL1 và PL5 của 5937 bị QĐ 2010 bãi bỏ; PL6 của 5937 là mã nhóm thầu, còn được XML2 dẫn); QĐ 5086/QĐ-BYT 04/11/2021 (nguyên tắc mã hóa vật tư y tế, XML3 dẫn); QĐ 4469/QĐ-BYT 28/10/2020 (ICD-10 cũ, XML1 bản 2023 dẫn); QĐ 34/2020/QĐ-TTg (mã nghề nghiệp); TT 07/2016/TT-BCA và QĐ 124/2004/QĐ-TTg (mã đơn vị hành chính); TT 25/2025/TT-BYT (bệnh dài ngày, QĐ 1804 dẫn); TT 23/2024/TT-BYT (danh mục kỹ thuật, là gốc của mã DVKT trong QĐ 2010).

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### BHYT-DATA-R01 — Sinh đủ bộ bảng XML hiện hành
- **Căn cứ**: QĐ 130 Đ1 (13 bảng: check-in, Bảng 1–12; UTF-8, XML), thay bảng bởi QĐ 4750 Đ1, sửa tạm thời bởi QĐ 3176 Đ1; TT 12/2026 Đ5 k1 a (Bảng kê chi tiết đề nghị thanh toán "được lập theo chuẩn" QĐ 130 sửa bởi 4750 và 3176). Bộ bảng đang được Cổng nhận (CV-BHXH-LT3176 mục 2.4, 3.4, 3.5): **XML0** check-in; **XML1** tổng hợp; **XML2** thuốc; **XML3** DVKT và VTYT; **XML4** CLS; **XML5** diễn biến lâm sàng; **XML6** HSBA HIV/AIDS; **XML7** giấy ra viện; **XML8** tóm tắt HSBA; **XML9** giấy chứng sinh; **XML10** giấy nghỉ dưỡng thai; **XML11** giấy nghỉ việc hưởng BHXH; **XML13** giấy chuyển tuyến; **XML14** giấy hẹn khám lại; **XML15** điều trị bệnh lao. **XML12** (giám định y khoa) không đi qua HIS: cơ sở GĐYK nhập trực tiếp trên Cổng (QĐ 130 Đ3 k3).
- **Áp dụng cho**: cơ sở KCB có HĐ KCB BHYT (BV công, BV tư, PK) và vendor HIS · **Hiệu lực**: bộ 4750 từ 01/07/2024; bộ 3176 từ 01/01/2025; sửa 1931 từ 01/07/2026.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh được từng bảng trên từ dữ liệu lâm sàng và viện phí; chỉ đính kèm bảng liên quan theo loại lượt KCB (QĐ 130 Đ3 k2 "tùy vào đối tượng và mục đích"; ghi chú bảng 2023: XML4 chỉ khi có CLS; XML5 chỉ khi MA_LOAI_KCB thuộc nhóm điều trị; XML8 chỉ khi nội trú, nội trú ban ngày, lưu TYT/PKĐKKV); đóng gói vào khung `GIAMDINHHS/THONGTINHOSO/DANHSACHHOSO/HOSO/FILEHOSO{LOAIHOSO, NOIDUNGFILE}` với `NOIDUNGFILE` là nội dung bảng mã hóa base64; mỗi lần gửi `fileHSBase64` là **một hồ sơ KCB**.
- **Ghi chú / bẫy**: (1) Thẻ XML thực tế lấy theo tài liệu BHXH, không theo tên bảng tiếng Việt (vd `TONG_HOP`, `CHITIEU_CHITIET_THUOC/DSACH_CHI_TIET_THUOC/CHI_TIET_THUOC`). (2) Tên trường là `MA_DOITUONG_KCB` (không có gạch giữa DOI và TUONG); inventory ghi `MA_DOI_TUONG_KCB` là sai. (3) So với bảng 2023, bản 3176 thêm vào XML1 `NHOM_MAU`; XML2 `NGAY_TH_YL`; XML0 `NGAY_VAO_NOI_TRU`, `LY_DO_VNT`, `MA_LY_DO_VNT`, `MA_THUOC`, `TEN_THUOC`, `MA_VAT_TU`, `TEN_VAT_TU`; XML6 thêm 16 trường hành chính và lao/ARV; các bảng 7, 9, 10, 11 thêm `DU_PHONG` (so sánh thẻ XML tài liệu BHXH với XLSX 2023, kích thước từng trường bản 3176 **chưa đối chiếu được**). (4) XML6 ngoài Cổng BHXH còn phải gửi Cổng HMED `dieutri.arv.vn` (ghi chú Bảng 6 bản 2023, chưa rõ còn hiệu lực sau 3176).

### BHYT-DATA-R02 — Định dạng chung của file
- **Căn cứ**: TT 48/2017 Đ4 k3 a, b (XML, UTF-8; mỗi file một hoặc nhiều hồ sơ, mỗi hồ sơ một đợt KCB, kể cả người bệnh có từ hai thẻ BHYT trong đợt); QĐ 130 Đ1 đoạn cuối.
- **Áp dụng cho**: như R01 · **Hiệu lực**: từ 01/03/2018, đang áp dụng.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: xuất UTF-8 (khai báo `encoding="utf-8"`), escape ký tự đặc biệt; một hồ sơ = một đợt KCB, gom mọi thẻ BHYT của đợt vào cùng hồ sơ.
- **Ghi chú / bẫy**: TT 48 cho phép một file nhiều hồ sơ, nhưng API hiện tại của BHXH yêu cầu "mỗi file XML là một hồ sơ KCB" (CV-BHXH-LT3176 mục 3.2). Thiết kế theo API, giữ khả năng đóng lô cho phương thức khác.

### BHYT-DATA-R03 — Bảng check-in (XML0) gửi khi phát sinh chi phí đầu tiên
- **Căn cứ**: QĐ 130 Đ3 k1 được sửa bởi QĐ 4750 Đ2 k2: (a) gửi "ngay sau khi có phát sinh chi phí khám bệnh, chữa bệnh đầu tiên của người bệnh"; (b) nếu được chỉ định nội trú, nội trú ban ngày hoặc ngoại trú: gửi ngay sau khi phát sinh chi phí của dịch vụ đầu tiên tại khoa điều trị đó; (c) **không cần** gửi khi cấp cứu (`MA_DOITUONG_KCB = 2`) hoặc cơ sở chỉ nhận người bệnh/mẫu bệnh phẩm để làm CLS. QĐ 130 Đ2 k1 sửa bởi 4750 Đ2 k1: check-in chỉ để thông báo trạng thái, **không** dùng làm căn cứ giám định, thanh toán.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: 01/07/2024.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bắt sự kiện "dòng chi phí đầu tiên của lượt" (thường là tiền khám) và sự kiện "chi phí đầu tiên tại khoa điều trị" để gửi XML0 (endpoint `api/qd130/checkInKcbQd3176`, `loaiHoSo = 0`); điền `MA_DICH_VU/TEN_DICH_VU` hoặc `MA_THUOC/TEN_THUOC` hoặc `MA_VAT_TU/TEN_VAT_TU` của chi phí đầu tiên, `NGAY_YL`; có luật miễn gửi theo mã đối tượng 2 và theo loại cơ sở chỉ làm CLS; lưu `maGiaoDich`.
- **Ghi chú / bẫy**: căn cứ miễn trong 4750 dẫn NĐ 146/2018 Đ15 k6 và TT 30/2020 Đ9, nay đã bị NĐ 188/2025 và TT 01/2025 thay; mã cấp cứu vẫn là "2" trong QĐ 3276 nên logic không đổi, nhưng căn cứ pháp lý của trường hợp "cơ sở chỉ làm CLS" cần xác minh lại (mục 7).

### BHYT-DATA-R04 — Tra cứu thẻ BHYT khi tiếp đón và lấy thông tin hành chính từ Cổng
- **Căn cứ**: QĐ 4750, bảng check-in, diễn giải `MA_THE_BHYT` (khi tiếp đón phải tra cứu trên Cổng; cấp cứu thì tra trước khi ra viện; thẻ QN, HC, LS, XK, CY, CA tra hạn sử dụng; chưa có thẻ thì dùng chức năng tra thẻ tạm trẻ em/người hiến tạng); TT 48 Đ13 k2; QĐ 697 Phụ lục, Phần Một mục III (thông tin hành chính lấy từ Cổng hoặc thẻ giấy với QN, CA, CY; nếu tra ra từ 02 mã thẻ thì dùng mã có hạn phù hợp thời điểm đến KCB).
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: gọi API tra cứu thẻ khi tiếp đón, lưu nguyên phản hồi (thời điểm tra, mã thẻ, hạn thẻ, mức hưởng, thời điểm đủ 5 năm liên tục, tiền cùng chi trả lũy kế); cho phép cập nhật khi BHXH đã cập nhật thông tin hành chính trong đợt; chọn mã thẻ theo thời điểm đến khám khi có nhiều thẻ.
- **Ghi chú / bẫy**: dữ liệu tra cứu là đầu vào của bảng kê (mục 16, 17, 18 mẫu 697) và của `MUC_HUONG`; phải lưu "ảnh chụp" phản hồi để chứng minh khi BHXH đối chiếu.

### BHYT-DATA-R05 — Thời hạn gửi dữ liệu
- **Căn cứ**: TT 48/2017 Đ6 k1 (gửi lên Cổng "ngay sau khi kết thúc lần khám bệnh hoặc kết thúc đợt điều trị ngoại trú hoặc kết thúc đợt điều trị nội trú", trừ Đ8); Đ6 k3 (dữ liệu phục vụ quản lý không phải xác thực); Đ7 k1 (trong 07 ngày làm việc kể từ ngày kết thúc KCB: hiệu chỉnh, xác thực, gửi dữ liệu đề nghị giám định, thanh toán; chi phí phát sinh cuối tháng, quý, năm gửi trước ngày 05 tháng kế tiếp); Đ8 (được gửi chậm khi sự cố bất khả kháng, mất điện, mất mạng; phải thông báo ngay cho bên kia); Đ13 k7 (kết thúc vào ngày nghỉ, lễ, tết thì trích chuyển vào ngày làm việc kế tiếp); Đ13 k8 (được gửi dữ liệu đề nghị thanh toán cùng lúc với dữ liệu quản lý nếu làm được). TT 12/2026 Đ9 k1 dẫn lại thời hạn Đ7, Đ8 TT 48 cho Bảng kê chi tiết.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: đang áp dụng; dự thảo thay TT 48 đề xuất **≤ 03 giờ** từ 01/01/2027 (chưa ban hành).
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tự động gửi khi đóng lượt KCB; bộ đếm hạn theo lịch làm việc (bảng ngày nghỉ, lễ cấu hình được); cảnh báo hồ sơ sắp quá 07 ngày làm việc và hồ sơ cuối tháng chưa gửi trước ngày 05; ghi nhật ký sự cố mất kết nối (thời điểm, nguyên nhân, thông báo) làm bằng chứng cho Đ8.
- **Ghi chú / bẫy**: TT 48 không định nghĩa "ngay sau" bằng giờ; nếu DT-TT48 được ban hành với ngưỡng 03 giờ thì mọi kiến trúc gửi theo lô cuối ngày sẽ vi phạm. Nên thiết kế từ giờ theo hàng đợi gần thời gian thực (xem P4).

### BHYT-DATA-R06 — Hiệu chỉnh, gửi lại, thay thế hồ sơ
- **Căn cứ**: TT 48 Đ7 k1 a (hiệu chỉnh trước khi gửi đề nghị thanh toán), Đ13 k9 (được hiệu chỉnh dữ liệu đã gửi khi phát hiện sai lệch, phải nêu rõ lý do và thống nhất với BHXH); QĐ 130, Bảng 1, `NGAY_TTOAN` (người bệnh ra viện chưa thanh toán thì để trống, khi hoàn tất thanh toán phải bổ sung và gửi lại); QĐ 3276 Đ2 (gửi lại hồ sơ thay thế theo mã đối tượng mới cho dữ liệu từ 01/07/2025); QĐ 3176 Đ2 k1 đ (cửa sổ thay thế hồ sơ 01/07/2024–31/12/2024); TT 12 Đ9 k3 (trong 02 ngày làm việc kể từ khi nhận phản hồi lỗi cấu trúc/sai lệch, gửi bảng kê, bảng tổng hợp hoặc báo cáo quyết toán điều chỉnh kèm văn bản).
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cho phép tái sinh XML của một `MA_LK` đã gửi với lý do bắt buộc, giữ mọi phiên bản đã gửi; bổ sung `NGAY_TTOAN` và gửi lại tự động khi thanh toán xong; đọc phản hồi lỗi theo từng trường của từng bảng (TT 48 Đ7 k3 c) và mở việc xử lý có hạn 02 ngày làm việc.
- **Ghi chú / bẫy**: tái sinh hồ sơ cũ phải dùng **đúng phiên bản chuẩn và danh mục của thời điểm KCB**, trừ khi văn bản cho phép hoặc yêu cầu áp mã mới (như QĐ 3276). Đây là lý do cần P1, P2.

### BHYT-DATA-R07 — Ký số file XML và đăng ký chứng thư số trên Cổng
- **Căn cứ**: pháp lý: TT 12/2026 Đ9 k1 câu cuối (hồ sơ đề nghị thanh toán "được ký số xác thực theo quy định tại điểm c khoản 2 Điều 35 và khoản 9 Điều 69" NĐ 188); NĐ 188 Đ69 k9 ("Việc triển khai xác thực dữ liệu điện tử chi phí khám bệnh, chữa bệnh bảo hiểm y tế thực hiện chậm nhất từ ngày 01 tháng 01 năm 2026."); TT 48 Đ7 k1 b (xác thực trước khi gửi bởi người được giao hoặc ủy quyền), Đ13 k4 (báo cáo khi thay đổi người được ủy quyền xác thực). Kỹ thuật: CV-BHXH-LT3176 mục I (đăng ký chứng thư số tại Quản trị hệ thống → Danh mục chứng thư số trên `gdbhyt.baohiemxahoi.gov.vn`, tài khoản quyền AD), mục 2.4, 3.4 (thẻ `<CHUKYDONVI>` ở cuối file, giải thuật ký SHA256, chi tiết theo tệp XSD đăng ở mục Trợ giúp/Tài liệu của Cổng).
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: chậm nhất 01/01/2026.
- **Mức**: BẮT BUỘC (nghĩa vụ ký); chi tiết kỹ thuật theo hướng dẫn BHXH (BẮT BUỘC? vì số hiệu CV chưa xác minh)
- **Phần mềm phải**: ký số file XML0 và file hồ sơ trước khi gửi bằng chứng thư số của cơ sở đã đăng ký trên Cổng; kiểm tra hạn và trạng thái chứng thư trước khi ký; ghi nhật ký ai/khi nào/chứng thư nào ký hồ sơ nào.
- **Ghi chú / bẫy**: (1) Tài liệu BHXH mục 3.4 chép lại câu của mục 2.4 ("nội dung ký là từ thẻ mở `<CHI_TIEU_TRANG_THAI_KCB>`…") cho file `GIAMDINHHS`, rõ ràng là lỗi sao chép: phạm vi ký thực tế phải lấy từ XSD trên Cổng. (2) Định dạng chữ ký (XMLDSig enveloped hay khác) tài liệu không nói rõ (suy luận: XMLDSig, cần kiểm bằng XSD). (3) Ý nghĩa "xác thực dữ liệu" ở NĐ 188 Đ69 k9 là ký số hồ sơ hay xác thực người bệnh thuộc câu hỏi của cụm BHYT-GD; tài liệu BHXH cho thấy ít nhất là ký số file.

### BHYT-DATA-R08 — Quy tắc định dạng trường
- **Căn cứ**: Bảng chỉ tiêu QĐ 130 (bản 2023) và các bản sửa 4750, 3176: thời điểm dạng `yyyymmddHHMM` 12 ký tự (`NGAY_VAO`, `NGAY_RA`, `NGAY_YL`, `NGAY_TTOAN`, `NGAY_SINH`); ngày dạng `yyyymmdd` 8 ký tự (`GT_THE_TU`, `GT_THE_DEN`); `NGAY_SINH` thiếu giờ phút ghi `0000`, thiếu ngày tháng ghi `0000`, trẻ ≤ 28 ngày tuổi ghi đủ giờ phút; số thập phân dùng dấu chấm "."; nhiều giá trị trong một trường phân cách bằng ";" (`MA_BENH_KT`, `MA_KHOA`, `MA_GIUONG`, `MA_BAC_SI`); `SO_DANG_KY` không có khoảng trắng. QĐ 4750 (bảng check-in): `MA_LOAI_KCB` **đổi kiểu dữ liệu thành chuỗi**; `MA_DOITUONG_KCB` đổi thành chuỗi, kích thước tối đa **4 ký tự**; thêm `NGAY_VAO_NOI_TRU` 12 ký tự. QĐ 697 Phụ lục III.1 (dẫn 3176): `GIOI_TINH` Nam 1, Nữ 2, Chưa xác định 3.
- **Áp dụng cho**: như R01 · **Hiệu lực**: theo phiên bản chuẩn.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kiểm tra kiểu, độ dài tối đa, mẫu định dạng của từng trường theo phiên bản chuẩn đang áp dụng **trước khi gửi**; lưu mã dưới dạng chuỗi (giữ số 0 đầu như "01", "1.11").
- **Ghi chú / bẫy**: bảng 2023 để `MA_LOAI_KCB` là "Số" và `MA_DOITUONG_KCB` ở check-in là "Số, 1"; ai còn đọc XLSX 2023 sẽ làm rơi số 0 và cắt mã "1.11". Kích thước từng trường của bản 3176 chưa đọc được gốc; khi triển khai lấy XSD từ Cổng làm chuẩn kiểm.

### BHYT-DATA-R09 — Khóa liên kết và đánh số
- **Căn cứ**: QĐ 130 các bảng: `MA_LK` chuỗi ≤ 100, "mã đợt điều trị duy nhất", liên kết XML1 với các bảng còn lại (PRIMARY KEY); `STT` tăng từ 1 trong một lần gửi; `MA_BN` theo quy định cơ sở; `MA_HSBA` ≤ 100.
- **Áp dụng cho**: như R01 · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấp `MA_LK` duy nhất, bất biến cho mỗi đợt KCB (không tái sử dụng khi gửi lại); mọi dòng XML2–XML15 mang đúng `MA_LK` của XML1; QĐ 697 Phụ lục II.3–4 yêu cầu "Số khám bệnh" trên bảng kê = `MA_LK`, "Mã số người bệnh" = `MA_BN`.
- **Ghi chú / bẫy**: `MA_LK` dùng làm khóa ở cả bảng kê giấy và XML, nên không được đổi khi chỉnh sửa hồ sơ.

### BHYT-DATA-R10 — Quy tắc tính tiền trong XML
- **Căn cứ**: QĐ 130 Bảng 2: `DON_GIA` làm tròn 3 chữ số thập phân; `THANH_TIEN_BV = SO_LUONG * DON_GIA` làm tròn 2 chữ số thập phân; Bảng 1: `T_TONGCHI_BV` = tổng `THANH_TIEN_BV` của XML2 và XML3. TT 12 Đ5 k2 (khớp đúng giữa Bảng kê chi tiết, Bảng tổng hợp, Báo cáo quyết toán và HSBA).
- **Áp dụng cho**: như R01 · **Hiệu lực**: đang áp dụng (công thức bản 3176 chưa đối chiếu gốc).
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tính bằng kiểu thập phân chính xác (không dùng float nhị phân), đúng thứ tự làm tròn; kiểm tra tổng XML1 = tổng chi tiết trước khi gửi.
- **Ghi chú / bẫy**: tiền VND trong bảng kê là đồng (697 Phần IV.1) nhưng XML cho phép thập phân ở đơn giá thuốc; đừng ép kiểu integer cho đơn giá.

### BHYT-DATA-R11 — Trường MUC_HUONG 4 ký tự và cách tính mức hưởng
- **Căn cứ**: QĐ 1931/QĐ-BYT ngày 29/06/2026 (thứ cấp): tăng kích thước tối đa `MUC_HUONG` lên 04 ký tự từ 01/07/2026. QĐ 3276 PL1 cột `MUC_HUONG` theo từng mã đối tượng (mã 1.13, 1.14, 1.18: từ 01/07/2026 hưởng 50% chi phí theo phạm vi quyền lợi, mức hưởng; mã 3.1: 40% nội trú, 0% ngoại trú). QĐ 697 Phụ lục IV.2 (mức hưởng ghi "sau khi nhân (x) mức hưởng theo nhóm đối tượng với mức hưởng theo quy định của Luật BHYT", theo PL1 QĐ 3276). Bảng 2023: `MUC_HUONG` "Số, 3", trái tuyến ghi mức đã nhân (ví dụ 32).
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC? (nghĩa vụ rõ theo thứ cấp; bản gốc 1931 chưa đọc)
- **Phần mềm phải**: lưu và xuất `MUC_HUONG` 4 ký tự ở XML2, XML3; tính mức hưởng từ (mức theo thẻ) × (tỷ lệ theo mã đối tượng, theo ngày); tách chi phí theo từng mức hưởng khi một đợt có hai mức (697 Phần IV.2).
- **Ghi chú / bẫy**: (suy luận) 4 ký tự cần cho giá trị có phần thập phân, ví dụ 95 × 50% = 47.5. Cần xác nhận với bản gốc 1931 xem có cho phép dấu thập phân hay không.

### BHYT-DATA-R12 — SO_DANG_KY cho thuốc hiếm nhập khẩu do UBND tỉnh cấp phép
- **Căn cứ**: QĐ 1931/2026 (thứ cấp): bổ sung quy tắc ghi `SO_DANG_KY` cho thuốc hiếm được UBND cấp tỉnh cấp phép nhập khẩu. Bảng 2023: ghi số đăng ký lưu hành, không có khoảng trắng; dược liệu nhập khẩu ghi số C/O; dược liệu GACP ghi số giấy chứng nhận GACP.
- **Áp dụng cho**: cơ sở KCB BHYT dùng thuốc loại này · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC? (chưa có câu chữ gốc của quy tắc mã)
- **Phần mềm phải**: danh mục thuốc có trường "loại căn cứ lưu hành" (SĐK, C/O, GACP, giấy phép nhập khẩu tỉnh…) và sinh `SO_DANG_KY` theo quy tắc tương ứng.
- **Ghi chú / bẫy**: quy tắc mã cụ thể **chưa xác minh**; không tự chế định dạng.

### BHYT-DATA-R13 — Chỉ dùng bộ mã danh mục dùng chung do BYT ban hành
- **Căn cứ**: NĐ 188 Đ68 k1 (BYT xây dựng, ban hành các bộ mã danh mục dùng chung, tiêu chuẩn, định dạng dữ liệu); TT 48 Đ4 k2 (dữ liệu đầu vào và đầu ra phải đúng Bộ mã danh mục dùng chung), Đ13 k1 (cơ sở phải sử dụng Bộ mã, Chuẩn và định dạng dữ liệu đầu ra, Xác thực điện tử); TT 12/2026 Đ7 k1 a (danh mục mã hóa theo QĐ 7603 sửa bởi 4905/2019, 5937/2021, 824/2023, 2010/2025, 3276/2025). QĐ 1804 bổ sung thêm sau TT 12.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: có kho danh mục dùng chung nạp từ nguồn chính thức, mỗi mã có nguồn (số QĐ, phụ lục), ngày hiệu lực, ngày bãi bỏ; ánh xạ danh mục nội bộ sang mã dùng chung; chặn gửi hồ sơ có mã không tồn tại tại thời điểm áp dụng.
- **Ghi chú / bẫy**: chuỗi văn bản danh mục bị **bãi bỏ theo từng phụ lục**, không theo cả quyết định (mục 6). Danh sách trong TT 12 Đ7 chưa có QĐ 1804 vì ban hành sau.

### BHYT-DATA-R14 — Mã loại hình KCB theo QĐ 1804 (16 mã)
- **Căn cứ**: QĐ 1804/2026 Đ1 k1, Phụ lục 01; Đ2 (thực hiện chậm nhất 01/08/2026; bãi bỏ PL1 QĐ 824 từ 01/08/2026). Mã: 01 Khám bệnh; 02 Điều trị ngoại trú (bệnh không thuộc PL I TT 25/2025); 03 Điều trị nội trú (dưới 4 giờ dùng 09); 04 Điều trị ban ngày (không dùng cho nội trú dưới 4 giờ); 05 Ngoại trú bệnh dài ngày có khám và lĩnh thuốc (nếu có DVKT thì dùng 08, không dùng 05); 06 Lưu tại PKĐK, PKĐKKV, nhà hộ sinh, trạm y tế; 07 Nhận thuốc theo hẹn (không phải đi KCB); 08 Ngoại trú bệnh dài ngày có khám, DVKT và/hoặc thuốc; 09 Nội trú dưới 04 giờ; 10 Khác; 11 KCB lưu động (ngoài địa điểm trong giấy phép, trừ tại nhà); 12 KCB tại nhà; 13 Y học gia đình; 14 KCB từ xa; 15 Khám sức khỏe định kỳ; 16 Khám sàng lọc (15, 16: với BHYT chỉ dùng khi có quy định cho Quỹ thanh toán).
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: chậm nhất 01/08/2026.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dùng đúng 16 mã; kiểm tra chéo: thời gian nội trú < 4 giờ thì buộc 09; mã 05 không đi kèm DVKT; mã 11 không dùng cho KCB tại nhà; mã 12, 13, 14 cần quy trình KCB tương ứng.
- **Ghi chú / bẫy**: mã 12, 14 xuất hiện trong khi quy định thanh toán BHYT cho KCB tại nhà và từ xa còn là dự thảo (DT-BHYT-TUXA, inventory). Có mã không có nghĩa là Quỹ trả.

### BHYT-DATA-R15 — Mã khoa theo QĐ 1804 Phụ lục 02
- **Căn cứ**: QĐ 1804 Phụ lục 02 (61 dòng: K01–K60 và K99 "Khoa điều trị bệnh truyền nhiễm nhóm A", cùng mã con K16.1–K16.3, K22.1, K59.1–K59.2) và Ghi chú: liên chuyên khoa ghi `Kxxyyzz…`; khoa tách sâu ghi `KXY.Z`; đơn nguyên ghi mã khoa + ".D" + 2 số của khoa tương ứng (ví dụ K02.D35); tên khoa không trùng thì chọn 01 mã phù hợp nhất; K32 nếu không có thì dùng K33; "Khoa" hiểu là Khoa/Trung tâm/Viện/Đơn nguyên. TT 12 Phụ lục II Mẫu 01/DM chỉ tiêu `MA_KHOA` (chuỗi 50) dùng cùng quy tắc (ví dụ "K0809", "K02.D35"). QĐ 2010 PL6 bị bãi bỏ từ 01/08/2026.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: chậm nhất 01/08/2026.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục khoa nội bộ ánh xạ sang mã QĐ 1804 theo cú pháp trên (regex kiểm được); `MA_KHOA` XML1 ghi lần lượt các khoa người bệnh đã điều trị, phân cách ";".
- **Ghi chú / bẫy**: inventory ghi "60 mã khoa K01–K60"; bản gốc có thêm K99 và các mã con. Ghi chú QĐ 1804 viết "02 ký tự là số thứ tự tên khoa theo quy chế bệnh viện", nhưng K51–K60 không theo quy chế cũ, nên lấy danh mục làm chuẩn.

### BHYT-DATA-R16 — Mã đối tượng đến KCB và mã nhiên liệu theo QĐ 3276
- **Căn cứ**: QĐ 3276/2025 Đ1, PL1 (27 dòng mã: 1.1–1.7, 1.11–1.18, 2, 3.1, 3.2, 3.3, 3.6, 7, 7.2, 7.3, 7.4, 8 "Thu hồi đề nghị thanh toán", 9 "Người bệnh không KCB BHYT", 10; mỗi mã kèm căn cứ và `MUC_HUONG`). Ghi chú PL1: mã được **xác định sau khi kết thúc** khám hoặc điều trị; nếu áp được nhiều mã thì chọn theo thứ tự từ trên xuống. PL2: `MA_XANG_DAU` theo loại nhiên liệu và vùng (R954V1…, XEDIEN). Đ2: bãi bỏ PL5 QĐ 824 (xăng dầu) và PL5 QĐ 2010 (đối tượng); cho phép trích xuất lại, gửi hồ sơ thay thế cho dữ liệu từ 01/07/2025; chuyển tiếp đến 31/12/2025.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: 17/10/2025 (hiệu lực ngược cho dữ liệu từ 01/07/2025 nếu gửi thay thế).
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tính `MA_DOITUONG_KCB` khi đóng lượt (không chốt ở quầy tiếp đón), theo thứ tự ưu tiên bảng; cấp cứu = "2"; dùng mã "8" khi thu hồi đề nghị thanh toán; cập nhật tỷ lệ hưởng theo ngày (01/07/2026 với 1.13, 1.14, 1.18).
- **Ghi chú / bẫy**: STT trong PL1 nhảy từ 21 sang 23 (không có dòng 22) ngay trong bản gốc; đừng dùng STT làm khóa. Xác định mã ở check-in (XML0) là tạm, mã cuối nằm ở XML1.

### BHYT-DATA-R17 — Mã DVKT, khám, giường, chỉ số CLS
- **Căn cứ**: QĐ 2010/2025 Đ1, PL1 (mã DVKT dùng chung `MA_DICH_VU`, dạng `CC.KKKK.GGGG`, một số mã có hậu tố `_GT`, ánh xạ với TT 23/2024 và tên giá theo TT 43, 50, 21 và TT 22/2023), PL2 (mã khám), PL3 (mã tiền giường), PL4 (ngày giường ban ngày); Đ2 (bãi bỏ PL01–04 QĐ 7603; PL1, PL5 QĐ 5937; PL2 QĐ 824); Đ3 (XML4: dùng tên, mã chỉ số CLS cột mã dùng chung của QĐ 1227/2025; chỉ số chưa có thì tạm dùng PL11 QĐ 7603); Đ5 (cập nhật phần mềm chậm nhất 01/08/2025). Bảng 3 bản 2023: vận chuyển ghi `VC.XXXXX`; CLS chuyển nơi khác ghi `XX.YYYY.ZZZZ.K.WWWWW`; mã giường 4 ký tự H/T/C/K + số.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: 01/08/2025, đang áp dụng.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: ánh xạ dịch vụ nội bộ sang mã DVKT dùng chung, giữ cả mã kỹ thuật TT 23 và STT giá; ánh xạ chỉ số xét nghiệm/CĐHA sang mã QĐ 1227, có cờ "đang dùng tạm PL11 7603".
- **Ghi chú / bẫy**: (suy luận) cấu trúc `CC.KKKK.GGGG` ứng với chương TT 23 + số kỹ thuật + STT giá, rút ra từ các cột của PL1, chưa thấy văn bản định nghĩa. QĐ 2010 tự gọi là "tạm thời", nên dự kiến sẽ còn bản thay.

### BHYT-DATA-R18 — Mã thuốc, vật tư/thiết bị y tế, máu, thầu
- **Căn cứ**: Bảng 2 bản 2023: `MA_THUOC` = mã hoạt chất theo bộ mã DMDC (thuốc tự bào chế ghi các mã thành phần nối "+"; oxy "40.17"; NO "40.573"; máu có hậu tố ".KT", ".NAT"); `TT_THAU` = số QĐ trúng thầu; mã gói; mã nhóm thầu theo PL6 QĐ 5937; năm, phân cách ";" (hai nhà thầu thì thêm `Gi.YY`). Bảng 3 bản 2023: `MA_VAT_TU` chi tiết tới kích thước, **được cấp tự động trên Cổng** theo nguyên tắc QĐ 5086/2021; chỉ ghi VTYT ngoài cơ cấu giá DVKT. QĐ 697 Phụ lục IV.8: máu, chế phẩm máu theo PL9 QĐ 7603.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục thuốc lưu mã hoạt chất DMDC, SĐK, thông tin thầu đúng cú pháp; danh mục VTYT/TBYT lưu mã do Cổng cấp; không tự sinh mã VTYT.
- **Ghi chú / bẫy**: QĐ 697 và TT 24/2025 dùng thuật ngữ "thiết bị y tế" trong khi XML vẫn là `MA_VAT_TU`/VTYT. Danh mục mã thuốc có được cập nhật theo danh mục thuốc BHYT mới (TT 37/2024, TT 27/2025) hay không: **chưa xác minh**.

### BHYT-DATA-R19 — Danh mục sử dụng tại cơ sở (Mẫu 01–06/DM) và cập nhật có ngày hiệu lực
- **Căn cứ**: TT 12/2026 Đ7 k1 b (chuẩn và định dạng theo Phụ lục II), k2 (sau khi ký hợp đồng lần đầu, lập danh mục, **ký số** gửi qua Cổng, khớp hồ sơ ký hợp đồng), k3 (thời điểm áp dụng danh mục từ ngày hợp đồng có hiệu lực; thuốc, TBYT không sớm hơn hiệu lực hợp đồng mua sắm), k5 (phát hiện sai lệch thì điều chỉnh hoặc hủy trong 05 ngày làm việc); Đ8 (đề nghị cập nhật qua Cổng kèm văn bản; BHXH xử lý trong 05 ngày làm việc; thuốc, TBYT mua để cấp cứu áp dụng theo ngày hóa đơn; cơ sở gửi lại trong 15 ngày nếu bị từ chối). Phụ lục II: Mẫu 01/DM bộ phận chuyên môn (`MA_KHOA`, `BAN_KHAM`, `GIUONG_PD`, `GIUONG_TK`, `GIUONG_HSTC`, `GIUONG_HSCC`, `TU_NGAY`, `DEN_NGAY`, `MA_CSKCB`); 02/DM nhân lực; 03/DM thuốc, máu; 04/DM TBYT; 05/DM dịch vụ KCB; 06/DM TBYT để thực hiện DVKT. Ghi chú Mẫu 01/DM: thay đổi thông tin thì gửi **02 dòng**: dòng 1 thông tin cũ với `DEN_NGAY` là ngày ngừng áp dụng; dòng 2 thông tin mới với `TU_NGAY` là ngày bắt đầu, `DEN_NGAY` để trống. `TU_NGAY`, `DEN_NGAY` dạng `yyyymmdd`.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: theo TT 12 (inventory ghi danh mục từ 01/04/2026; điều hiệu lực chưa đọc lại).
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: quản lý danh mục nội bộ dạng có thời hạn hiệu lực (valid-time), sinh file Mẫu 01–06/DM, ký số, gửi Cổng, theo dõi trạng thái chấp nhận/từ chối; chỉ cho phép dùng mục danh mục trong hồ sơ nếu ngày y lệnh nằm trong [`TU_NGAY`, `DEN_NGAY`] đã được Cổng chấp nhận.
- **Ghi chú / bẫy**: chính TT 12 đã chuẩn hóa mô hình "đóng dòng cũ, mở dòng mới", nên **không được update-in-place** danh mục đã gửi.

### BHYT-DATA-R20 — ICD-10 theo TT 06/2026 trong dữ liệu đầu ra
- **Căn cứ**: TT 06/2026 Đ3 (danh mục mã bệnh tại Phụ lục); Đ4 k1 (cột 1–23 là thông tin mã), k2 (cột 24: không được dùng là bệnh chính; 25: không khuyến khích dùng là bệnh chính; 26: không dùng vì có mã 4 hoặc 5 ký tự cụ thể hơn; 27: chỉ dùng mã hóa nguyên nhân tử vong; 28: chỉ có hoặc chủ yếu ở nữ; 29: chỉ có hoặc chủ yếu ở nam), k3 (định nghĩa bệnh chính, kèm theo, biến chứng, di chứng); Đ5 k3 (mã Q87.11 thành Q87.1 từ 01/06/2026); Đ6 k1 (văn bản cũ khác thì áp TT này; mã cũ bị hủy thì chọn mã phù hợp nhất), **k2** (vào viện trước 01/07/2026 và kết thúc lượt trong hoặc sau ngày đó thì dùng mã theo TT này), k3 (mã cũ trong HSBA đã lưu vẫn có giá trị pháp lý); Đ7 k3 a (BHXH cập nhật danh mục trên Cổng), k5 b (cơ sở cập nhật danh mục vào phần mềm). Bảng 1 bản 2023: `MA_BENH_CHINH` chỉ 01 mã (chuỗi ≤ 7); `MA_BENH_KT` tối đa 12 mã, phân cách ";"; `MA_BENH_YHCT` ghi kèm mã YHCT tương ứng ICD-10.
- **Áp dụng cho**: mọi cơ sở KCB (XML: cơ sở BHYT) · **Hiệu lực**: 01/07/2026 (một phần 01/06/2026).
- **Mức**: BẮT BUỘC (nạp danh mục, dùng đúng mã, quy tắc chuyển tiếp); kiểm tra tự động theo cột 24–29: NÊN (văn bản đặt nguyên tắc, không bắt phần mềm phải chặn)
- **Phần mềm phải**: nạp đủ 29 cột; khi chốt hồ sơ chọn bộ mã theo **thời điểm kết thúc lượt KCB** (`NGAY_RA`); chặn cứng mã cột 24, 26, 27 ở `MA_BENH_CHINH`; cảnh báo cột 25; cảnh báo cột 28, 29 khi lệch `GIOI_TINH`; không viết đè mã đã lưu trong HSBA cũ.
- **Ghi chú / bẫy**: bảng 2023 vẫn dẫn QĐ 4469/2020; theo TT 06 Đ6 k1 thì từ 01/07/2026 phải theo TT 06. Đây là trường hợp duy nhất trong cụm có **quy tắc chọn phiên bản theo ngày kết thúc lượt** được ghi rõ.

### BHYT-DATA-R21 — Bảng kê chi phí 01/KBCB theo QĐ 697
- **Căn cứ**: QĐ 697/2026 Đ2 k1 (mỗi lượt lập 01 bảng kê lưu hồ sơ, 01 bảng kê giao người bệnh), k2 (đã triển khai bệnh án điện tử thì lập bảng kê điện tử, cung cấp qua phương tiện điện tử, không phải lập giấy; "Bảng kê điện tử có ký số đầy đủ theo quy định thì có giá trị tương đương bản giấy"; bảng kê giấy ký tay của người bệnh được scan và ký số xác thực của cơ sở thì có giá trị như bản điện tử), k3 (chỉ kê mục có phát sinh, giữ nguyên STT mã mục); Đ3 (thay QĐ 6556/2018); Đ4 k1 (nâng cấp phần mềm chậm nhất 01/07/2026), k2 (trước đó dùng mẫu 6556), k3 (văn bản dẫn trong Phụ lục bị thay thì theo văn bản mới). Phụ lục: tiêu đề ghi ô loại 01/02/03/04; ánh xạ `MA_LK`, `MA_BN`, `DIA_CHI`, `GIOI_TINH`, `MA_LOAI_RV`, mã đối tượng (3276); Phần IV: tách chi phí theo từng thẻ, từng mức hưởng; quy tắc tỷ lệ thanh toán khám (100/30/10/0%), giường (100/50/33%), gói TBYT với trần 45 tháng lương cơ sở.
- **Áp dụng cho**: mọi cơ sở KCB lập bảng kê (BV công, BV tư, PK); phần BHYT cho người có thẻ · **Hiệu lực**: chậm nhất 01/07/2026.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: in và xuất bảng kê đúng mẫu 697; bảng kê điện tử ký số (cơ sở, người lập, người bệnh theo mẫu); cho phép scan bản ký tay và ký số xác thực cơ sở; sinh bảng kê **từ cùng một ảnh chụp dữ liệu** với XML (xem P8).
- **Ghi chú / bẫy**: (1) Trên trang BHXH, file quyết định có tên "QĐ 967.pdf" nhưng nội dung là QĐ 697. (2) Phụ lục 697 dẫn mã khoa theo PL6 QĐ 2010, đã bị QĐ 1804 bãi bỏ từ 01/08/2026; theo Đ4 k3 thì dùng mã QĐ 1804. (3) Phụ lục 697 ghi ngày QĐ 7603 là "15/12/2018", trong khi QĐ 2010 và TT 12 ghi 25/12/2018: lỗi trong Phụ lục.

### BHYT-DATA-R22 — Phương thức kết nối và lưu bằng chứng gửi
- **Căn cứ**: TT 48 Đ5 (chọn 1 trong 4 phương thức: web service, đồng bộ từ phần mềm máy trạm, nhập trực tiếp, FTP; phải cho cùng kết quả dữ liệu đầu ra); Đ6 k2, Đ7 k2–3 (Cổng phản hồi tiếp nhận, kết quả giám định trong 07 ngày làm việc, lỗi theo từng trường của từng bảng XML). TT 12 Đ9 k2 (Cổng phản hồi tự động: chậm nhất 06 giờ nếu gửi sai thời hạn; 24 giờ nếu sai cấu trúc, định dạng, ghi rõ lỗi từng trường; 48 giờ nếu Bảng tổng hợp lệch Bảng kê chi tiết). CV-BHXH-LT3176 mục II: REST JSON, `api/token/take` (mật khẩu MD5 viết hoa), `api/qd130/checkInKcbQd3176`, `api/qd130/guiHoSoXmlQD3176`; phản hồi `maKetQua`, `maGiaoDich` ("lưu lại để đối chiếu"), `thoiGianTiepNhan`, `thongDiep`; tra cứu kết quả trên Cổng tối đa 60 ngày.
- **Áp dụng cho**: cơ sở KCB BHYT, vendor · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC (phản hồi lỗi, chọn phương thức); lưu `maGiaoDich`: NÊN (hướng dẫn BHXH, không phải QPPL)
- **Phần mềm phải**: lưu bền mọi phản hồi gắn với `MA_LK` và phiên bản file đã gửi; tự kéo kết quả, lỗi về và gán việc xử lý.
- **Ghi chú / bẫy**: Cổng chỉ cho tra cứu 60 ngày, nên **HIS phải tự lưu** biên nhận lâu dài. Mật khẩu băm MD5 do BHXH quy định là yếu (suy luận); không lưu mật khẩu rõ trong cấu hình, giữ trong kho bí mật.

### BHYT-DATA-R23 — Chuyển đổi phiên bản chuẩn theo mốc của Bộ
- **Căn cứ**: QĐ 130 Đ4 k3–5, Đ5 (kiểm thử song song với 4210 từ 31/03/2023; chính thức 01/09/2023); QĐ 4750 Đ2 k3 (kiểm thử từ 01/04/2024, song song với bảng 4210), k4 (chính thức 01/07/2024), k5 và Đ3 (4210 chấm dứt và hết hiệu lực 01/07/2024; nội dung không sửa giữ theo 130); QĐ 3176 Đ3 (đồng bộ từ 01/01/2025; phần không sửa giữ theo 4750 và 130), Đ2 k1 b (BHXH phải thông báo trước thay đổi trên Cổng), đ (cửa sổ thay thế hồ sơ 01/07–31/12/2024); QĐ 130 Đ5 đoạn cuối (văn bản dẫn chiếu bị thay thì theo văn bản mới).
- **Áp dụng cho**: cơ sở KCB BHYT, vendor · **Hiệu lực**: theo từng QĐ.
- **Mức**: BẮT BUỘC (áp đúng mốc); chạy song song nhiều phiên bản: NÊN
- **Phần mềm phải**: chạy được **hai phiên bản chuẩn song song** trong giai đoạn kiểm thử; chuyển phiên bản theo cấu hình ngày, không sửa code; giữ khả năng tái sinh hồ sơ cũ theo phiên bản cũ.
- **Ghi chú / bẫy**: mỗi QĐ sửa là **bản vá chồng lên** bản trước ("nội dung còn lại giữ nguyên"), nên bản hợp nhất phải tự dựng. Mốc của QĐ 130 (01/09/2023) đã bị 4750 dời: không trích QĐ 130 đơn lẻ.

### BHYT-DATA-R24 — Mã cơ sở KCB và thay đổi tổ chức
- **Căn cứ**: Bảng 1 bản 2023: `MA_CSKCB` chuỗi 5 "do cơ quan có thẩm quyền cấp"; `MA_DKBD` 5 ký tự. NĐ 188 Đ69 k8 d (cơ sở sắp xếp, sáp nhập, đổi tên được tiếp tục dùng mã cơ sở cũ đến khi được cấp mã mới), nhưng Đ70 k3: **khoản 8 Đ69 chỉ có hiệu lực 01/07/2025–31/12/2025**.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: k8 hết hiệu lực 31/12/2025.
- **Mức**: NÊN (quản lý mã cơ sở có hiệu lực theo thời gian); dùng đúng mã được cấp: BẮT BUỘC
- **Phần mềm phải**: lưu mã cơ sở như dữ liệu có thời hạn (mã cũ, mã mới, ngày chuyển), áp vào hồ sơ theo ngày KCB; cập nhật `MA_NOI_DI`, `MA_NOI_DEN`, `MA_DKBD` của các cơ sở khác theo danh mục BHXH.
- **Ghi chú / bẫy**: mã cơ sở 5 ký tự của BHXH khác "mã định danh cơ sở 13 chữ số" trong luồng Sổ SKĐT/KSK (QĐ 1551/2026, cụm K4). Không trộn hai mã.

### BHYT-DATA-R25 — Bảo mật dữ liệu trong trích chuyển
- **Căn cứ**: TT 48 Đ3 k2 (minh bạch, an toàn, bảo mật, theo pháp luật giao dịch điện tử), Đ9 (bảo mật, toàn vẹn, quyền riêng tư; dùng dữ liệu trong phạm vi chức năng), Đ13 k3 (cơ sở chịu trách nhiệm tính chính xác và bảo mật dữ liệu người bệnh); NĐ 188 Đ68 k5 c.
- **Áp dụng cho**: cơ sở KCB BHYT, vendor · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: TLS khi gửi; phân quyền tài khoản Cổng; nhật ký truy cập và gửi; không lưu XML ở nơi công khai. (Chi tiết an ninh, DLCN thuộc cụm K8, K9.)
- **Ghi chú / bẫy**: XML6 (HIV) chứa dữ liệu nhạy cảm, cần phân quyền chặt hơn (suy luận, liên quan khoảng trống #10 của inventory).

### BHYT-DATA-R26 — Chứng từ BHXH trong bộ XML (XML7–XML11, XML13, XML14)
- **Căn cứ**: QĐ 130 Đ2 k4 (Bảng 7–11 dùng để tạo lập chứng từ giải quyết chế độ BHXH theo TT 56/2017 và TT 18/2022); QĐ 4750 bổ sung Bảng 13 (giấy chuyển tuyến) và 14 (giấy hẹn khám lại). TT 06/2026 Đ5 k2: phiếu hẹn khám lại và phiếu chuyển cơ sở KCB bản điện tử dùng **ký số xác thực của cơ sở** thay đóng dấu từ 01/06/2026.
- **Áp dụng cho**: cơ sở KCB cấp các chứng từ này · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC? (TT 56/2017 có thể đã được TT 25/2025 thay, chưa đọc; nghĩa vụ gửi XML chứng từ với người bệnh không dùng BHYT chưa rõ)
- **Phần mềm phải**: sinh XML7, 9, 10, 11, 13, 14 khi phát hành chứng từ tương ứng; một trẻ một bản khi sinh đôi trở lên (ghi chú Bảng 7, 9 bản 2023); ký số cơ sở trên bản điện tử phiếu hẹn, phiếu chuyển.
- **Ghi chú / bẫy**: phần chứng từ BHXH, giấy chứng sinh, nghỉ việc giao thoa với cụm K4 (giấy tờ điện tử liên thông).

---

## 3. Pattern thiết kế

### P1. Sổ đăng ký phiên bản chuẩn XML (Spec Registry) — giải quyết R01, R08, R09, R11, R23
- **Mô tả**: mô hình hóa mỗi văn bản sửa chuẩn là một **lớp vá** lên lớp trước, đúng như cách Bộ ban hành (4750 có cột "Đính chính hoặc sửa đổi, bổ sung" cạnh diễn giải QĐ 130; 3176 "sửa đổi, bổ sung tạm thời"; "nội dung còn lại giữ nguyên"). Bản hiệu lực của một ngày = hợp nhất các lớp có `mandatory_from ≤ ngày`.
- **Dữ liệu gợi ý**:
  - `spec_release(id, decision_no, decision_date, kind[base|amend], parent_id, test_from, mandatory_from, sunset_at, source_url, verification_level)`; ràng buộc: `decision_no` kèm năm (tránh nhầm 1931/2016 với 1931/2026).
  - `spec_field(release_id, xml_table['XML0'..'XML15'], xml_path, field_name, data_type[string|number|datetime12|date8], max_len, required_rule, format_regex, change_type[add|modify|retype|remove], note, source_ref)`; khóa duy nhất `(release_id, xml_table, field_name)`.
  - View `effective_spec(as_of_date)` hợp nhất theo `parent_id`.
- **Luồng**: sinh XSD và bộ kiểm tra từ `effective_spec`; đối chiếu XSD tự sinh với XSD BHXH đăng trên Cổng (nguồn sự thật kỹ thuật) trong CI.
- **Đánh đổi**: tốn công nhập liệu thủ công từ PDF/XLSX; đổi lại, thêm 1931 chỉ là một bản ghi `modify MUC_HUONG max_len 3→4`.

### P2. Kho danh mục dùng chung có thời gian hiệu lực theo phụ lục — giải quyết R13–R18, R20
- **Mô tả**: quản lý mã ở mức **phụ lục của văn bản**, vì việc bãi bỏ diễn ra theo phụ lục (1804 bỏ PL1 của 824 và PL6 của 2010; 3276 bỏ PL5 của 824 và PL5 của 2010; 2010 bỏ PL01–04 của 7603).
- **Dữ liệu gợi ý**:
  - `code_source(id, decision_no, decision_date, appendix, code_system, effective_from, mandatory_from, abolished_by_source_id, abolished_from)`.
  - `code_value(code_system, code, display, attrs jsonb, source_id, valid_from, valid_to, recorded_at, superseded_by)`; chỉ mục `(code_system, code, valid_from)`; ràng buộc không chồng lấn khoảng hiệu lực cho cùng `(code_system, code)` (exclusion constraint trên `daterange`).
  - ICD-10: `attrs` chứa 29 cột, có cờ `col24_not_primary`, `col25_discouraged_primary`, `col26_has_more_specific`, `col27_death_cause_only`, `col28_female`, `col29_male`.
- **Hàm tra cứu**: `resolve(code_system, code, as_of)`; chính sách chọn `as_of` cấu hình được theo hệ mã: ICD theo ngày kết thúc lượt (TT 06 Đ6 k2); danh mục cơ sở theo ngày y lệnh trong `[TU_NGAY, DEN_NGAY]`; các QĐ không nói rõ khóa ngày (1804, 2010) thì mặc định ngày kết thúc lượt và đánh dấu "chưa xác minh" (mục 7).
- **Đánh đổi**: hai trục thời gian (hiệu lực pháp lý và thời điểm nạp) làm truy vấn phức tạp hơn, nhưng là cách duy nhất để tái sinh hồ sơ cũ đúng mã cũ và chứng minh "đã dùng mã nào, theo văn bản nào".

### P3. Danh mục sử dụng tại cơ sở kiểu "đóng dòng cũ, mở dòng mới" — giải quyết R19
- **Mô tả**: làm theo đúng Ghi chú Mẫu 01/DM TT 12: thay đổi = gửi 2 dòng. Mọi mục danh mục nội bộ (khoa, nhân lực, thuốc, TBYT, DVKT) là bản ghi có `tu_ngay`/`den_ngay`, trạng thái đồng bộ với Cổng.
- **Dữ liệu gợi ý**: `facility_catalog_item(id, form['01/DM'..'06/DM'], local_code, dmdc_code, payload jsonb, tu_ngay, den_ngay, contract_ref, purchase_contract_effective, sync_status[draft|signed|sent|accepted|rejected], portal_msg, signed_by, signed_at)`; ràng buộc `tu_ngay ≥ purchase_contract_effective` cho thuốc, TBYT (TT 12 Đ7 k3).
- **Luồng**: sửa → sinh 2 dòng → ký số → gửi → chờ chấp nhận (BHXH có 05 ngày làm việc) → chỉ khi `accepted` mới cho dùng trong hồ sơ; bị từ chối → bộ đếm 15 ngày gửi lại.
- **Đánh đổi**: người dùng không "sửa" được tại chỗ; cần UI giải thích.

### P4. Đường ống hồ sơ hướng sự kiện, có đồng hồ hạn chót — giải quyết R03, R05, R06, R22
- **Mô tả**: outbox pattern trong HIS.
  - Sự kiện `first_cost_posted(lượt)` và `first_cost_in_ward(lượt, khoa)` → job check-in (trừ khi `MA_DOITUONG_KCB = 2` hoặc cơ sở chỉ làm CLS).
  - `encounter_closed` → chốt ảnh chụp hồ sơ (P5) → kiểm tra (P6) → ký (P7) → gửi → lưu biên nhận.
  - `payment_completed` → bổ sung `NGAY_TTOAN` → gửi lại.
  - `portal_error(maGiaoDich, lỗi theo trường)` → việc xử lý có hạn 02 ngày làm việc (TT 12 Đ9 k3).
- **Dữ liệu gợi ý**: `claim_submission(id, ma_lk, kind[checkin|claim|replace], snapshot_id, spec_release_id, payload_hash, signed_cert_serial, sent_at, ma_giao_dich, thoi_gian_tiep_nhan, ma_ket_qua, thong_diep, deadline_at, status)`; `work_calendar(date, is_working_day, note)`; job tính `deadline_at` theo quy tắc TT 48 (ngày làm việc kế tiếp; 07 ngày làm việc; trước ngày 05 tháng sau) và có sẵn cấu hình 03 giờ cho dự thảo.
- **Đánh đổi**: gửi gần thời gian thực làm tăng số lần gửi lại khi dữ liệu còn thay đổi; nhưng nếu DT-TT48 ban hành thì gửi theo lô sẽ không còn hợp lệ.

### P5. Ảnh chụp hồ sơ bất biến và tái sinh có lý do — giải quyết R06, R09, R10, R21
- **Mô tả**: khi đóng lượt, đóng băng mọi dữ liệu nguồn thành `claim_snapshot` (JSON chuẩn hóa) kèm phiên bản chuẩn (P1) và phiên bản từng danh mục (P2) đã dùng. XML, bảng kê, báo cáo đều sinh từ snapshot.
- **Dữ liệu gợi ý**: `claim_snapshot(id, ma_lk, version_no, created_at, reason, spec_release_id, code_versions jsonb, data jsonb, sha256)`; duy nhất `(ma_lk, version_no)`; không cho UPDATE/DELETE.
- **Đánh đổi**: tốn lưu trữ; đổi lại có truy vết đầy đủ khi BHXH xuất toán hoặc thanh tra hỏi "lúc gửi dữ liệu là gì".

### P6. Kiểm tra nhiều tầng trước khi gửi — giải quyết R08, R10, R14–R17, R20
- **Tầng 1** cấu trúc: XSD (độ dài, kiểu, thẻ bắt buộc).
- **Tầng 2** định dạng: regex `^\d{12}$` cho thời điểm, `^\d{8}$` cho ngày; danh sách ";"; mã khoa theo cú pháp QĐ 1804 (ví dụ `^K\d{2}((\d{2})*|\.\d+|\.D\d{2})$`, cần chỉnh theo dữ liệu thật).
- **Tầng 3** liên bảng: mọi `MA_LK` con tồn tại ở XML1; `T_TONGCHI_BV = Σ THANH_TIEN_BV(XML2, XML3)`; `THANH_TIEN_BV = round(SO_LUONG × DON_GIA, 2)`.
- **Tầng 4** danh mục theo ngày: mã có hiệu lực tại `as_of` (P2), mục danh mục cơ sở đã `accepted` (P3).
- **Tầng 5** nghiệp vụ: `MA_LOAI_KCB` so với thời gian nằm viện (< 4 giờ → 09); 05 không có DVKT; ICD cột 24–29; `GIOI_TINH` với cột 28, 29; `MA_BENH_KT` ≤ 12 mã.
- **Đầu ra**: lỗi gắn theo `bảng/trường` giống cách Cổng trả lỗi (TT 48 Đ7 k3 c), để người dùng sửa một chỗ.
- **Đánh đổi**: luật tầng 5 phải bật/tắt theo ngày hiệu lực; viết như dữ liệu cấu hình, không hard-code.

### P7. Dịch vụ ký số tập trung — giải quyết R07, R19, R21, R26
- **Mô tả**: một dịch vụ ký riêng (HSM hoặc token ký từ xa) nhận file đã chuẩn hóa, ký theo phạm vi nút do XSD BHXH quy định, thuật toán băm SHA256, đặt vào `<CHUKYDONVI>`; dùng chung cho XML0, hồ sơ XML, danh mục Mẫu /DM, bảng kê điện tử, phiếu hẹn, phiếu chuyển.
- **Dữ liệu gợi ý**: `signing_cert(serial, subject, issuer, valid_from, valid_to, registered_on_portal_at, status)`; `signature_log(doc_type, doc_id, cert_serial, digest, signed_at, actor)`; cảnh báo chứng thư sắp hết hạn trước 30 ngày (suy luận, ngưỡng tự chọn).
- **Đánh đổi**: tập trung tạo điểm lỗi đơn; cần hàng đợi và cơ chế thử lại.

### P8. Một nguồn cho XML và bảng kê — giải quyết R21, R10, R09
- **Mô tả**: bảng kê 697 là **phép chiếu** từ cùng `claim_snapshot`: "Số khám bệnh" = `MA_LK`, "Mã số người bệnh" = `MA_BN`, giới tính 1/2/3, tình trạng ra viện = `MA_LOAI_RV`, mã đối tượng = `MA_DOITUONG_KCB`; nhóm theo mã mục 1–12, bỏ mục không phát sinh nhưng giữ STT; tách khối theo thẻ và mức hưởng.
- **Đánh đổi**: buộc thống nhất mô hình chi phí giữa viện phí và BHYT; nhưng TT 12 Đ5 k2 yêu cầu khớp đúng nên không có lựa chọn khác.

### P9. Theo dõi thay đổi quy định và cờ theo ngày — giải quyết R23, R11, R14, R15
- **Mô tả**: mỗi văn bản mới (QĐ chuẩn, QĐ danh mục, TT) thành một "change ticket" có `effective_from`, `mandatory_from`, phần bị bãi bỏ, mức xác minh nguồn; cờ tính năng bật theo ngày; bộ hồ sơ mẫu (fixtures) cho từng phiên bản để chạy hồi quy.
- **Đánh đổi**: cần người theo dõi BYT/BHXH định kỳ; bù lại tránh được kiểu sự cố "QĐ ký ngày 29/6, áp dụng 01/7".

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| BHYT-DATA-A01 | R01 | Xuất hồ sơ mẫu cho 5 loại lượt (khám, ngoại trú, nội trú, nội trú < 4 giờ, sinh con); xem có đủ XML1–5, 7–9, 13–15 theo tình huống; XML12 không có trong gói | File XML mẫu, ảnh màn hình cấu hình bảng | Bắt buộc |
| BHYT-DATA-A02 | R02 | Mở file: khai báo UTF-8, tiếng Việt có dấu đúng; mỗi file một hồ sơ; đợt có 2 thẻ nằm chung hồ sơ | File mẫu, hexdump BOM/encoding | Bắt buộc |
| BHYT-DATA-A03 | R03 | Tạo lượt mới, ghi tiền khám: kiểm log có gửi XML0 ngay; chuyển nội trú: có XML0 lần 2 khi phát sinh chi phí tại khoa; tạo ca cấp cứu: không gửi XML0 | Log gửi kèm thời điểm, `maGiaoDich` | Bắt buộc |
| BHYT-DATA-A04 | R04 | Tiếp đón: phần mềm gọi API tra thẻ, lưu phản hồi; thử thẻ hết hạn, thẻ QN/CA | Bảng lưu phản hồi tra cứu; log API | Bắt buộc |
| BHYT-DATA-A05 | R05 | Truy vấn DB: phân bố (thời điểm gửi − `NGAY_RA`); đếm hồ sơ > 07 ngày làm việc; hồ sơ cuối tháng gửi sau ngày 05; có lịch ngày nghỉ không | Kết quả truy vấn, báo cáo trễ hạn, biên bản sự cố (Đ8) | Bắt buộc |
| BHYT-DATA-A06 | R06 | Sửa một hồ sơ đã gửi: phần mềm có bắt nhập lý do, giữ bản cũ, giữ nguyên `MA_LK`; hồ sơ chưa thanh toán gửi `NGAY_TTOAN` trống rồi tự gửi lại | Lịch sử phiên bản hồ sơ, log gửi lại | Bắt buộc |
| BHYT-DATA-A07 | R07 | Kiểm file đã gửi có `<CHUKYDONVI>` hợp lệ, SHA256, chứng thư còn hạn và đã đăng ký trên Cổng; ai được quyền ký | File ký, thông tin chứng thư, ảnh màn hình Danh mục chứng thư số trên Cổng | Bắt buộc |
| BHYT-DATA-A08 | R08 | Kiểm XSD/regex nội bộ: `MA_LOAI_KCB` có giữ "01"; `MA_DOITUONG_KCB` nhận "1.11"; ngày giờ 12 ký tự; dấu "." thập phân | Kết quả chạy bộ kiểm với file mẫu | Bắt buộc |
| BHYT-DATA-A09 | R09 | Truy vấn trùng `MA_LK` giữa các đợt; dòng XML con mồ côi | Kết quả truy vấn | Bắt buộc |
| BHYT-DATA-A10 | R10 | Lấy 50 hồ sơ ngẫu nhiên, tính lại tổng và làm tròn; kiểm kiểu dữ liệu cột tiền trong DB (decimal hay float) | Bảng đối chiếu, schema DB | Bắt buộc |
| BHYT-DATA-A11 | R11 | Kiểm cột `MUC_HUONG` chứa được 4 ký tự; hồ sơ sau 01/07/2026 với mã 1.13/1.14/1.18 ra đúng mức | File mẫu, schema | Bắt buộc? |
| BHYT-DATA-A12 | R12 | Danh mục thuốc có phân loại căn cứ lưu hành; thử thuốc hiếm nhập khẩu theo giấy phép tỉnh | Ảnh màn hình danh mục, file XML2 | Bắt buộc? |
| BHYT-DATA-A13 | R13 | Liệt kê nguồn từng danh mục trong phần mềm (số QĐ, phụ lục, ngày nạp); có danh mục nào còn theo phụ lục đã bãi bỏ (PL1 824, PL5 824, PL5 2010, PL6 2010, PL01–04 7603) | Bảng metadata danh mục | Bắt buộc |
| BHYT-DATA-A14 | R14 | Danh mục loại hình có đủ 16 mã; thử ca nội trú 3 giờ → 09; ca 05 có DVKT bị chặn | Danh mục, kết quả thử | Bắt buộc |
| BHYT-DATA-A15 | R15 | So danh mục khoa nội bộ với PL02 QĐ 1804 (gồm K99, mã con, `.D`); hồ sơ sau 01/08/2026 không còn mã khoa theo PL6 QĐ 2010 không có trong QĐ 1804 | Bảng ánh xạ, truy vấn | Bắt buộc |
| BHYT-DATA-A16 | R16 | `MA_DOITUONG_KCB` được tính khi đóng lượt; thứ tự ưu tiên đúng; có mã 8 cho thu hồi | Cấu hình luật, hồ sơ mẫu | Bắt buộc |
| BHYT-DATA-A17 | R17 | Tỷ lệ dịch vụ nội bộ đã ánh xạ sang mã DVKT QĐ 2010; tỷ lệ chỉ số XN đã ánh xạ QĐ 1227; danh sách chỉ số còn dùng PL11 7603 | Báo cáo ánh xạ | Bắt buộc |
| BHYT-DATA-A18 | R18 | Mẫu XML2 với thuốc tự bào chế, oxy, máu .KT/.NAT; `TT_THAU` đúng cú pháp; mã VTYT lấy từ Cổng | File mẫu, danh mục | Bắt buộc |
| BHYT-DATA-A19 | R19 | Lịch sử danh mục: thay đổi được lưu thành 2 dòng `TU_NGAY`/`DEN_NGAY`, có ký số và trạng thái chấp nhận của Cổng; hồ sơ không dùng mục chưa được chấp nhận | Bảng danh mục có lịch sử, file Mẫu /DM đã gửi | Bắt buộc |
| BHYT-DATA-A20 | R20 | Danh mục ICD đủ 29 cột theo TT 06; thử mã cột 24, 27 làm bệnh chính bị chặn; mã cột 28 với nam bị cảnh báo; ca vào 30/06/2026 ra 02/07/2026 dùng mã mới; Q87.1 thay Q87.11 | Danh mục, kết quả thử | Bắt buộc (nạp, chuyển tiếp) / Nên (chặn tự động) |
| BHYT-DATA-A21 | R21 | In bảng kê: đúng mẫu 697, bỏ mục không phát sinh nhưng giữ STT, 2 bản; bảng kê điện tử có chữ ký số; số liệu khớp XML cùng `MA_LK` | Bảng kê mẫu, file ký, đối chiếu với XML | Bắt buộc |
| BHYT-DATA-A22 | R22 | Phương thức kết nối đang dùng; nơi lưu `maGiaoDich`, phản hồi lỗi; có lấy được biên nhận cũ hơn 60 ngày từ HIS không | Cấu hình, truy vấn bảng biên nhận | Bắt buộc / Nên |
| BHYT-DATA-A23 | R23 | Phần mềm chạy được hai phiên bản chuẩn song song; chuyển phiên bản bằng cấu hình ngày; tái sinh hồ sơ năm 2024 theo chuẩn cũ | Tài liệu kiến trúc, demo | Nên |
| BHYT-DATA-A24 | R24 | Mã cơ sở lưu có thời hạn; hồ sơ trước, sau thời điểm đổi mã dùng đúng mã | Bảng mã cơ sở, hồ sơ mẫu | Nên |
| BHYT-DATA-A25 | R25 | Kết nối Cổng qua TLS; mật khẩu tài khoản Cổng không nằm rõ trong cấu hình; quyền truy cập XML6 | Cấu hình, kết quả quét bí mật | Bắt buộc |
| BHYT-DATA-A26 | R26 | Phát hành phiếu hẹn, phiếu chuyển điện tử: có ký số cơ sở (từ 01/06/2026) và sinh XML13/XML14 | File phiếu, XML | Bắt buộc? |

---

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái (so với 05/10/2026) | Sự kiện | Ai phải làm | Văn bản |
|---|---|---|---|---|
| 01/03/2018 | đã qua | TT 48 có hiệu lực: XML, UTF-8, 4 phương thức, thời hạn gửi | cơ sở KCB BHYT | TT-48-2017 |
| 15/01/2019 | đã qua | Áp dụng bộ mã dùng chung phiên bản 6 | cơ sở KCB BHYT, BHXH | QD-7603-2018 |
| 31/03/2023 → 01/09/2023 | đã qua | Kiểm thử rồi chính thức chuẩn 130 (mốc sau đó bị 4750 dời) | cơ sở KCB BHYT | QD-130-2023 |
| 01/04/2024 | đã qua | Bắt đầu kiểm thử bảng 4750, song song bảng 4210 | cơ sở KCB BHYT | QD-4750-2023 |
| 01/07/2024 | đã qua | Chính thức bảng 4750; QĐ 4210 hết hiệu lực; check-in bắt buộc | cơ sở KCB BHYT | QD-4750-2023 |
| 01/07–31/12/2024 | đã qua | Cửa sổ thay thế hồ sơ chuyển đổi chuẩn | cơ sở KCB BHYT | QD-3176-2024 Đ2 k1 đ |
| 01/01/2025 | đã qua | Áp dụng đồng bộ bảng 3176 | cơ sở KCB BHYT | QD-3176-2024 |
| 11/04/2025 | đã qua | Mã chỉ số CLS dùng chung đợt 1 | mọi cơ sở KCB; XML4 | QD-1227-2025 |
| 01/08/2025 | đã qua | Cập nhật phần mềm theo 6 danh mục QĐ 2010 | cơ sở KCB BHYT | QD-2010-2025 |
| 17/10/2025 (hiệu lực ngược 01/07/2025) → 31/12/2025 | đã qua | Mã đối tượng, mã nhiên liệu mới; cửa sổ gửi lại hồ sơ | cơ sở KCB BHYT | QD-3276-2025 |
| 01/01/2026 | đã qua | Chậm nhất triển khai xác thực dữ liệu điện tử chi phí KCB BHYT | cơ sở KCB BHYT | ND-188-2025 Đ69 k9 |
| 01/04/2026 | đã qua (theo inventory) | Biểu mẫu và danh mục TT 12 (Mẫu 01–06/DM) | cơ sở KCB BHYT | TT-12-2026-BTC |
| 01/06/2026 | đã qua | Phiếu hẹn, phiếu chuyển điện tử ký số cơ sở; Q87.11 → Q87.1 | mọi cơ sở KCB | TT-06-2026 Đ5 k2, k3 |
| 01/07/2026 | đã qua | ICD-10 theo TT 06; bảng kê mẫu 697; `MUC_HUONG` 4 ký tự và `SO_DANG_KY` thuốc hiếm (1931); mức hưởng 50% cho mã đối tượng 1.13, 1.14, 1.18 | mọi cơ sở KCB (ICD, bảng kê); cơ sở BHYT (XML) | TT-06-2026, QD-697-2026, QD-1931-2026, QD-3276-2025 |
| 01/08/2026 | đã qua | Mã loại hình KCB (16 mã) và mã khoa mới; PL1 QĐ 824 và PL6 QĐ 2010 hết hiệu lực | cơ sở KCB BHYT | QD-1804-2026 |
| 07/10/2026 | sắp tới | Hết hạn lấy ý kiến dự thảo thay TT 48 | vendor, cơ sở góp ý | DT-TT48 |
| 01/01/2027 | sắp tới (dự kiến) | Dự thảo thay TT 48 có hiệu lực: gửi ≤ 03 giờ, 15 ngày đối chiếu, chế tài; có thể kèm bộ mã, chuẩn dữ liệu, ký số mới | cơ sở KCB BHYT, vendor | DT-TT48 |
| chưa định | sắp tới | QĐ 2010 và QĐ 3176 đều tự ghi "tạm thời", nên khả năng có bản thay | vendor theo dõi | — |

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuẩn XML**
- QĐ 4210/QĐ-BYT (20/09/2017) → QĐ 130/QĐ-BYT (18/01/2023) → sửa bởi QĐ 4750 (29/12/2023, chính thức 01/07/2024) → sửa tạm thời bởi QĐ 3176 (29/10/2024, đồng bộ 01/01/2025) → sửa bởi QĐ 1931 (29/06/2026, áp dụng 01/07/2026).
- Bẫy 1: trích "QĐ 130" đơn lẻ là sai; bảng chỉ tiêu 2023 đã bị 4750 thay toàn bộ, và mốc 01/09/2023 của QĐ 130 bị 4750 dời sang 01/07/2024.
- Bẫy 2: **QĐ 1931/QĐ-BYT** trùng số với QĐ năm 2016 về tẩy sán lá gan nhỏ. Luôn ghi "ngày 29/6/2026".
- Bẫy 3: XLSX bảng chỉ tiêu 2023 còn lưu nhiều nơi; trong đó `MA_LOAI_KCB` và `MA_DOITUONG_KCB` (check-in) là kiểu "Số". 4750 đã đổi sang chuỗi, `MA_DOITUONG_KCB` tối đa 4 ký tự.
- Bẫy 4: tài liệu BHXH hướng dẫn liên thông 3176 chép nhầm phạm vi ký từ XML0 sang file hồ sơ; dùng XSD trên Cổng.

**Bộ mã danh mục dùng chung** (bãi bỏ **theo phụ lục**, không theo cả quyết định)
- QĐ 6061/QĐ-BYT (29/12/2017, bản 5) → QĐ 7603 (25/12/2018, bản 6), sửa bởi 4905 (21/10/2019), 5937 (30/12/2021), 824 (15/02/2023), 2010 (19/06/2025), 3276 (17/10/2025), 1804 (19/06/2026).
- QĐ 2010 Đ2 bãi bỏ: PL01–04 QĐ 7603 (DVKT tương đương, khám, giường, ngày giường ban ngày theo hạng BV); PL1 (ngày giường ban ngày PHCN) và PL5 (mã khoa) QĐ 5937; PL2 (mã đối tượng) QĐ 824.
- QĐ 3276 Đ2 bãi bỏ: PL5 QĐ 824 (xăng dầu); PL5 QĐ 2010 (mã đối tượng).
- QĐ 1804 Đ2 bãi bỏ từ 01/08/2026: PL1 QĐ 824 (loại hình KCB); PL6 QĐ 2010 (mã khoa).
- Chuỗi mã khoa: PL5 QĐ 5937 → PL6 QĐ 2010 → PL02 QĐ 1804. Chuỗi mã đối tượng: PL2 QĐ 824 → PL5 QĐ 2010 → PL1 QĐ 3276. Chuỗi mã loại hình: PL1 QĐ 824 → PL01 QĐ 1804. Chuỗi xăng dầu: PL5 QĐ 824 → PL2 QĐ 3276.
- Bẫy 5: TT 12/2026 Đ7 liệt kê chuỗi đến 3276 nhưng chưa có 1804 (ban hành sau). Đừng coi danh sách trong TT 12 là đầy đủ.
- Bẫy 6: Phụ lục QĐ 697 ghi QĐ 7603 ngày "15/12/2018"; đúng là 25/12/2018 (QĐ 2010, TT 12 bản gốc).
- Bẫy 7: Bảng XML1 bản 2023 dẫn mã khoa theo PL5 QĐ 5937 và ICD theo QĐ 4469/2020; cả hai đã bị thay (QĐ 1804; TT 06/2026).

**Bảng kê**
- QĐ 6556/QĐ-BYT (30/10/2018) → QĐ 697/QĐ-BYT (19/03/2026); phần mềm nâng cấp chậm nhất 01/07/2026.
- Bẫy 8: file trên trang BHXH tên "QĐ 967.pdf". Nội dung là QĐ 697.
- Bẫy 9: Phụ lục 697 dẫn PL6 QĐ 2010 cho mã khoa; từ 01/08/2026 dùng QĐ 1804 (697 Đ4 k3).

**Thời hạn và căn cứ**
- TT 48/2017 còn hiệu lực (QĐ 1804 ngày 19/06/2026 vẫn lấy làm căn cứ); dự thảo thay dự kiến 01/01/2027.
- Bẫy 10: NĐ 188 **Đ69 là "Điều khoản chuyển tiếp"** (không phải điều về CNTT); điều về trách nhiệm CNTT là Đ68. Đ69 k8 (cho dùng mã cơ sở cũ sau sáp nhập) chỉ có hiệu lực 01/07/2025–31/12/2025 (Đ70 k3).
- Bẫy 11: QĐ 4750, 2010 viện dẫn NĐ 146/2018, NĐ 75/2023, NĐ 02/2025, TT 30/2020 đã hết hiệu lực hoặc bị thay; nội dung kỹ thuật vẫn dùng, nhưng khi trích căn cứ pháp lý phải đổi sang NĐ 188/2025, TT 01/2025.

**Mâu thuẫn trong inventory đã xử lý**
- MT-07: xác nhận bằng bản gốc QĐ 1804 Đ2 (chỉ bãi bỏ phụ lục). Bổ sung: QĐ 3276 cũng bãi bỏ PL5 QĐ 824 và PL5 QĐ 2010, inventory chưa ghi.
- MT-08: chuỗi 130 → 4750 → 3176 → 1931 đúng về cấu trúc; riêng QĐ 1931/2026 **vẫn chỉ có nguồn thứ cấp** (suckhoetreem và kết quả tìm kiếm). Có căn cứ gián tiếp: QĐ 3276 (gốc) đặt mức hưởng 50% cho một số mã từ 01/07/2026, khớp với lý do mở rộng `MUC_HUONG` (suy luận).
- Câu hỏi mở K2 số 2: QĐ 1804 có 16 mã loại hình (khớp) và **61 dòng mã khoa** (K01–K60 cộng K99), thêm các mã con; inventory ghi "60 mã".
- MT-33: QĐ 3276 PL1 có 27 dòng, STT nhảy từ 21 lên 23 ngay trong bản gốc.
- Ngày QĐ 7603: 25/12/2018 (gốc qua QĐ 2010, TT 12).
- TT 48: hiệu lực 01/03/2018 (Đ14, gốc-OCR); thời hạn Đ6–Đ8, Đ13 k7 đọc từ bản gốc.
- (Cho cụm BHYT-GD) TT 12 Đ9 k1 bản gốc: Bảng tổng hợp gửi trong 15 ngày đầu mỗi tháng, Báo cáo quyết toán quý trước trong 15 ngày đầu mỗi quý (dẫn Luật BHYT Đ32 k2 a); hồ sơ ký số theo NĐ 188 Đ35 k2 c và Đ69 k9; Đ9 k2: Cổng phản hồi trong 06/24/48 giờ.

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **QĐ 1931/QĐ-BYT ngày 29/06/2026**: chưa có bản gốc. Cần: số và ngày chính xác, bảng nào bị sửa (XML2, XML3 hay cả XML0), `MUC_HUONG` có cho dấu thập phân không, quy tắc mã `SO_DANG_KY` cho thuốc hiếm nhập khẩu theo giấy phép UBND tỉnh. Nguồn nên thử: trang BHXH VN, moh.gov.vn, kcb.vn, cổng Sở Y tế.
2. **Phụ lục QĐ 3176 bản gốc**: chưa đọc. Kích thước, kiểu, diễn giải từng trường (đặc biệt `MA_BENH_KT` tối đa bao nhiêu mã, `MA_KHOA`, `MA_LOAI_RV`, `KET_QUA_DTRI`, công thức tiền) mới chỉ có theo bản 2023 và phần đầu bản 4750. Việc triển khai nên lấy **XSD trên Cổng** làm chuẩn kỹ thuật.
3. **Số hiệu công văn BHXH** kèm "Phụ lục 01 Hướng dẫn liên thông dữ liệu theo QĐ 3176" (bản đăng để trống số và ngày); hỏi BHXH VN hoặc BHXH tỉnh.
4. **Khóa ngày chọn phiên bản danh mục** khi QĐ không nói rõ (QĐ 1804 "thực hiện chậm nhất từ 01/08/2026"; QĐ 2010 "chậm nhất 01/08/2025"): theo ngày vào, ngày ra, ngày y lệnh hay ngày gửi? Lượt KCB vắt qua 01/08/2026 ghi mã khoa nào? Chỉ TT 06 Đ6 k2 có quy tắc rõ (theo kết thúc lượt). Cần hỏi Vụ BHYT hoặc BHXH.
5. **Miễn check-in cho cơ sở chỉ làm CLS**: căn cứ gốc (TT 30/2020 Đ9) đã bị thay một phần bởi TT 01/2025; trường hợp miễn này còn hiệu lực không.
6. **Mã đơn vị hành chính** (`MATINH_CU_TRU`, `MAHUYEN_CU_TRU`, `MAXA_CU_TRU`): bảng 2023 dẫn TT 07/2016/TT-BCA và QĐ 124/2004/QĐ-TTg; sau khi bỏ cấp huyện từ 01/07/2025, BHXH hướng dẫn điền `MAHUYEN_CU_TRU` thế nào: **chưa tìm thấy văn bản**.
7. **QĐ 824/2023 PL3, PL4, PL6** và **QĐ 1227/2025**: nội dung chưa mở bản gốc; danh mục mã thuốc có cập nhật theo TT 37/2024, TT 27/2025 không.
8. **Ý nghĩa "xác thực dữ liệu điện tử"** ở NĐ 188 Đ69 k9 và "tiêu chuẩn kết nối … đã được xác thực" ở Đ68 k5 b: có thủ tục xác thực phần mềm HIS trước khi kết nối không (khoảng trống #14). Thuộc cụm BHYT-GD; về dữ liệu, tài liệu BHXH chỉ yêu cầu đăng ký chứng thư số.
9. **XML7–XML11 với người bệnh không có BHYT**: có bắt buộc gửi lên Cổng giám định không, và TT 56/2017 đã bị TT 25/2025 thay đến đâu (liên quan cụm K4).
10. **Dự thảo thay TT 48**: toàn văn chưa đọc. Cần xem dự thảo có đổi chuẩn XML, bộ mã, phương thức ký số ("thí điểm ký số XML" theo báo) hay chỉ đổi thời hạn; nếu có, mọi pattern P1, P4, P7 phải có lớp phiên bản mới từ 01/01/2027.
11. Định dạng chữ ký trong `<CHUKYDONVI>` (XMLDSig enveloped, canonicalization nào): suy luận, cần đối chiếu XSD trên Cổng.
