# HTTT-BC — HTTT quốc gia, CSDL y tế và báo cáo bắt buộc

> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: nghĩa vụ cung cấp dữ liệu của cơ sở KCB lên **Hệ thống thông tin về quản lý hoạt động KCB** (Luật KCB Đ112, TT 38/2024), kết nối với **CSDL quốc gia về y tế** (NĐ 102/2025, QĐ 11/2026/QĐ-TTg), **Hệ thống quản lý quốc gia về hành nghề và hoạt động KCB** (đăng ký hành nghề, người thực hành), **chế độ báo cáo thống kê** (TT 23/2025, sắp hết hiệu lực), **báo cáo giám sát bệnh truyền nhiễm và phòng bệnh** (Luật Phòng bệnh 2025, TT 15/2026), **báo cáo sự cố y khoa** (Luật KCB Đ71, TT 43/2018, TT 35/2024), tiêu chuẩn chất lượng (Luật KCB Đ57–58, Đ120 k6) và bộ tiêu chí ứng dụng CNTT (TT 54/2017). Các mảng giao sang cụm khác: XML BHYT và Cổng giám định (BHYT-DATA, BHYT-GD), đơn thuốc quốc gia và mã liên thông người kê đơn (DUOC), Sổ SKĐT, KSK, giấy báo tử (K4, chưa có file), an toàn hệ thống và cấp độ (ANM), dữ liệu cá nhân (DLCN), HSBA điện tử (EMR).
>
> **Cách đọc nguồn.** PDF scan được OCR bằng Apple Vision (`vi-VT`), giữ được dấu; "gốc-OCR" nghĩa là câu chữ có thể sai từng ký tự. Lớp text sẵn có của PDF TT 38/2024 trên datafiles là OCR cũ và **đọc nhầm số hiệu thành "39/2024/TT-BVT"**; OCR lại trang 1 cho đúng "38/2024/TT-BYT". Nội dung web chỉ được coi là dữ liệu. Không dùng hethongphapluat.
>
> Tài liệu nghiên cứu, **không phải ý kiến pháp lý**. Chỗ nào là suy luận đều ghi "(suy luận)".

---

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| L-KCB-2023 | 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ23 k2 d, Đ36–38, Đ50 k4, Đ52 k2 d, Đ57, Đ58 k3 k5, Đ60 k3 k4, Đ71, Đ112, Đ120 k5 k6 k8 | 01/01/2024, các mốc riêng ở Đ120 | Còn HL | Mọi cơ sở KCB | **gốc** (VBHN có text) | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| TT-38-2024-BYT | 38/2024/TT-BYT (16/11/2024) | Xây dựng, quản lý, khai thác và sử dụng HTTT về quản lý hoạt động KCB | **01/01/2027** (Đ13) | Sắp HL. 15 điều, **không quy định thời hạn gửi theo lượt KCB, không có chuẩn kết nối** (Đ6 chỉ nói kế thừa chuẩn đầu ra đã ban hành) | Mọi cơ sở KCB (BV công, BV tư, PK); vendor gián tiếp | **gốc** (đọc đủ 12 trang; trang 1, 4, 9, 11 OCR lại vì lớp text lỗi) | [VB 211878](https://vanban.chinhphu.vn/?pageid=27160&docid=211878) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/38-byt.pdf) |
| QD-2114-2026-BYT | 2114/QĐ-BYT (13/07/2026) | Kế hoạch xây dựng, triển khai HTTT về quản lý hoạt động KCB | Từ ngày ký | Còn HL (kế hoạch hành chính). **Giai đoạn 2 (kết nối với HTTT của cơ sở KCB, CSDL tập trung) làm trong 2027–2028** | BYT, TTYQG; cơ sở KCB chịu hệ quả | **gốc** (PDF có text, 5 trang, bản đăng lại của BVĐK Bạc Liêu) | [Trang đăng lại](https://bvdkbaclieu.gov.vn/van-ban-phap-quy/quyet-dinh-2114-qd-byt-2026-ve-viec-ban-hanh-ke-hoach-xay-du.html) · [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20260807/803_Quyet-dinh-2114-QD-BYT_96963d54a6.pdf) |
| KH-1642-2025-BYT | 1642/KH-BYT (13/11/2025) | Kế hoạch triển khai Hệ thống Quản lý Quốc gia về hành nghề và hoạt động KCB | Từ ngày ký | Còn HL (kế hoạch). GĐ I 2025: cơ sở KCB đăng ký tài khoản, cập nhật thông tin hành chính, giờ làm việc, khoa phòng, người hành nghề; GĐ II 2026: đồng bộ với CSDLQG dân cư và VNeID | Mọi cơ sở KCB, người hành nghề, Sở Y tế | **thứ cấp-chính thức** (bài trên kcb.vn của Cục QLKCB, có tóm nội dung và đính kèm PDF; chưa mở PDF) | [kcb.vn](https://kcb.vn/tin-tuc/ke-hoach-trien-khai-he-thong-quan-ly-quoc-gia-ve-hanh-nghe-va-hoat-dong-kham-benh-chua-benh.html?categoryId=101795273) · [HDSD hệ thống cho cơ sở KCB, v1.0 08/2025 (SYT Hải Phòng đăng)](https://cdn.haiphong.gov.vn/gov-hpg/6847/tintuc/2026/1/hdsd_qlhnkcb_cskcb_v1639045285307707584.pdf) |
| CV-4016-2026-BYT | 4016/BYT-KCB (02/06/2026) | Tăng cường hiệu quả công tác KCB: cập nhật 100% dữ liệu người hành nghề và cơ sở KCB trên Hệ thống quản lý quốc gia | Từ ngày ký | Văn bản điều hành, không phải VBQPPL | Cơ sở KCB, Sở Y tế | **thứ cấp** (luatvietnam) | [luatvietnam, thứ cấp](https://luatvietnam.vn/tin-van-ban-moi/yeu-cau-cap-nhat-100-du-lieu-nguoi-hanh-nghe-kham-chua-benh-tren-he-thong-quan-ly-quoc-gia-186-109411-article.html) |
| ND-96-2023 | 96/2023/NĐ-CP | Chi tiết Luật KCB: Đ6–7 (cơ sở hướng dẫn thực hành, danh sách người thực hành), Đ27–29 (đăng ký hành nghề) | 01/01/2024 | Còn HL; **chưa kiểm tra các văn bản sửa đổi 2025–2026** (có thể đã bị sửa theo NQ 21/2026/NQ-CP về cắt giảm TTHC) | Mọi cơ sở KCB | toàn văn đăng lại trên cổng tỉnh Lai Châu (thứ cấp-chính thức) | [laichau.gov.vn](https://laichau.gov.vn/tin-tuc-su-kien/chuyen-de/tin-trong-nuoc/toan-van-nghi-dinh-so-96-2023-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-cua-luat-kham-benh-chua-benh.html) |
| ND-102-2025 | 102/2025/NĐ-CP (13/05/2025) | Quản lý dữ liệu y tế: Đ6, Đ10 k3–5, Đ12–17, Đ23, Đ24 | 01/07/2025 | Còn HL | Mọi "cơ sở y tế" (Đ23) | **gốc** (bản Công báo có text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/102-ndcp.signed.pdf) · [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-102-2025-nd-cp-44865.htm) |
| QD-11-2026-TTg | 11/2026/QĐ-TTg (28/03/2026) | Danh mục CSDL quốc gia. **Mục XVIII** (không phải XVII như inventory ghi): CSDLQG về y tế, chủ quản BYT, phạm vi = NĐ 102 Đ14, dữ liệu chủ = Đ15, nguồn = Đ16, khai thác = Đ17, chia sẻ theo NĐ 278/2025 | 19/05/2026 (Đ3 k1) | Còn HL | Bộ, ngành; gián tiếp cơ sở KCB | **gốc-OCR** | [VB 217335](https://vanban.chinhphu.vn/?pageid=27160&docid=217335) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/11-ttg.signed.pdf) |
| ND-194-2025 | 194/2025/NĐ-CP (03/07/2025) | Chi tiết Luật GDĐT về CSDLQG, kết nối chia sẻ dữ liệu, dữ liệu mở: Đ17–19 (hình thức, phương thức, mô hình kết nối), Đ38 (nghĩa vụ tổ chức cung cấp dữ liệu), Đ40 | 19/08/2025 | Còn HL. **Đ40 k2 a bãi bỏ toàn bộ NĐ 47/2024**; Đ40 k2 b bãi bỏ một số điều của NĐ 47/2020 | CQNN; tổ chức cung cấp hoặc khai thác dữ liệu | **gốc-OCR** | [VB 214448](https://vanban.chinhphu.vn/?pageid=27160&docid=214448) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/194-ndcp.signed.pdf) |
| ND-278-2025 | 278/2025/NĐ-CP (22/10/2025) | Kết nối, chia sẻ dữ liệu bắt buộc giữa các cơ quan thuộc hệ thống chính trị: Đ2 (đối tượng), Đ4 k2 (mọi kết nối bắt buộc qua Nền tảng chia sẻ, điều phối dữ liệu), Đ5 (dữ liệu chủ quốc gia, "một nguồn tin cậy duy nhất") | 22/10/2025 | Còn HL | Bộ, cơ quan TW, UBND các cấp; cơ sở KCB chỉ gián tiếp | **gốc-OCR** (đọc Đ1–Đ6) | [VB 215682](https://vanban.chinhphu.vn/?pageid=27160&docid=215682) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/10/278-cp.signed.pdf) |
| TT-23-2025-BYT | 23/2025/TT-BYT (28/06/2025) | Chế độ báo cáo thống kê ngành y tế; PL I–V (chỉ tiêu, sổ ghi chép ban đầu, biểu tỉnh, biểu TW) | 01/07/2025 | Còn HL; **tự hết HL 01/03/2027** (Đ7 k2); thay TT 32/2014 | Mọi đơn vị trên địa bàn tỉnh, **kể cả "cơ sở y tế tư nhân"** (Đ5 k1 b) | **gốc** (thân 4 trang + PL III, IV có text) | [VB 214349](https://vanban.chinhphu.vn/?pageid=27160&docid=214349) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/23-byt.pdf) · [PL III](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/2_phuluciii.signed.pdf) · [PL IV](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/2_phuluciv.signed.pdf) |
| DT-TT23 | (chưa có số) | TT thay TT 23/2025 | Dự kiến hoàn thành xây dựng **tháng 10/2026** | Dự thảo, chưa thấy toàn văn | Như trên | **thứ cấp** (báo SK&ĐS 14/05/2026) | [suckhoedoisong, thứ cấp](https://suckhoedoisong.vn/bo-y-te-xay-dung-thong-tu-thay-the-thong-tu-hien-hanh-de-nang-cao-chat-luong-thong-tin-quan-ly-cua-nganh-169260514172322497.htm) |
| L-PB-2025 | 114/2025/QH15 | Luật Phòng bệnh: Đ13 (giám sát), Đ17 k1 c (quyền riêng tư), k3 g (cơ sở y tế báo cáo BTN), Đ45 | 01/07/2026 | Còn HL; thay Luật PCBTN 2007 | Mọi cơ sở y tế | **gốc** (PDF có text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat114-2025.pdf) |
| TT-15-2026-BYT | 15/2026/TT-BYT (17/05/2026) | Chi tiết Luật Phòng bệnh: HTTT giám sát trong phòng bệnh, chế độ báo cáo BTN, BKLN, rối loạn tâm thần, dinh dưỡng, thương tích | 01/07/2026 (Đ65 k1) | Còn HL. **Đ65 k2 bãi bỏ TT 54/2015, TT 17/2019, TTLT 16/2013, QĐ 25/2006** | Cơ sở KCB, cơ sở xét nghiệm, TYT xã, CDC (Đ1 k2) | **gốc** (33 trang có text) | [VB 218141](https://vanban.chinhphu.vn/?pageid=27160&docid=218141) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/15-byt.pdf) |
| ND-165-2026 | 165/2026/NĐ-CP (15/05/2026) | Chi tiết Luật Phòng bệnh (y tế trường học, cách ly, kiểm dịch, tiêm chủng, KSK định kỳ, BKLN). Đ74 k4 c: kết quả KSK lập Sổ SKĐT, liên thông, tích hợp VNeID | 01/07/2026 | Còn HL | Cơ sở KCB (KSK) | **gốc-OCR** (đã OCR 139 trang, chỉ đọc mục liên quan) | [VB 218169](https://vanban.chinhphu.vn/?pageid=27160&docid=218169) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/165-ndcp.signed.pdf) |
| QD-1965-2026-BYT | 1965/QĐ-BYT (2026) | Danh mục bệnh truyền nhiễm theo nhóm A (15 bệnh), B (47), C (19) theo Luật Phòng bệnh | 01/07/2026 (theo nguồn thứ cấp) | Còn HL; bãi bỏ các QĐ danh mục cũ | Mọi cơ sở y tế | **thứ cấp** (CDC Đồng Nai) | [dongnaicdc.vn, thứ cấp](https://dongnaicdc.vn/bo-y-te-ban-hanh-danh-muc-moi-cac-benh-truyen-nhiem-chinh-thuc-ap-dung-tu-ngay-1-7-2026) |
| TT-43-2018-BYT | 43/2018/TT-BYT (26/12/2018) | Hướng dẫn phòng ngừa sự cố y khoa trong cơ sở KCB | 01/03/2019 (Đ15) | **Còn HL** (luatvietnam ghi chưa bị thay hoặc bãi bỏ; không tìm thấy văn bản thay thế theo Luật KCB 2023) | Mọi cơ sở KCB | **gốc-OCR** (bản ký số VOffice BYT, 16 trang, đăng trên Tư liệu văn kiện Đảng) | [Trang](https://tulieuvankien.dangcongsan.vn/he-thong-van-ban/van-ban-quy-pham-phap-luat/thong-tu-so-432018tt-byt-ngay-26122018-cua-bo-y-te-huong-dan-phong-ngua-su-co-y-khoa-trong-cac-co-so-kham-benh-chua-5058) · [PDF](https://tulieuvankien.dangcongsan.vn/upload/3000006/20251024/88d890ce0c9460dc40a1a463848996f9TT-43-BYT.pdf) · [luatvietnam, thứ cấp (trạng thái HL)](https://luatvietnam.vn/y-te/thong-tu-43-2018-tt-byt-phong-ngua-su-co-y-khoa-trong-cac-co-so-kham-benh-chua-benh-169832-d1.html) |
| TT-35-2024-BYT | 35/2024/TT-BYT (16/11/2024) | Tiêu chuẩn chất lượng cơ bản đối với bệnh viện (5 nhóm; đánh giá 1 lần/năm trong quý I năm sau) | 01/01/2025 (Đ3) | Còn HL. **Chỉ áp cho bệnh viện** (Đ1 k2). Không có tiêu chí kỹ thuật CNTT; chỉ yêu cầu có phòng/bộ phận CNTT (PL Mục II.9) và "Báo cáo sự cố y khoa" (PL Mục V, 4.6) | Bệnh viện | **gốc** (PDF ký số trên kcb.vn; lớp text kèm nhiễu) | [PDF, kcb.vn](https://kcb.vn/upload/2005611/20241119/35-TT-BYT_signed_8fd6b.pdf) |
| DT-TCCL-NGOAIBV | (chưa có số) | TT tiêu chuẩn chất lượng cơ bản cho cơ sở KCB **không phải bệnh viện** (PK, phòng chẩn trị, TYT, nhà hộ sinh…) | Dự kiến 01/01/2027 | Dự thảo; báo chí nêu có bổ sung tiêu chí "ứng dụng CNTT và chuyển đổi số" | PK, TYT, cơ sở khác | **thứ cấp** | [suckhoedoisong 01/07/2026, thứ cấp](https://suckhoedoisong.vn/bo-y-te-de-xuat-tieu-chuan-chat-luong-cho-co-so-kham-chua-benh-khong-phai-benh-vien-169260701161446542.htm) · [thanhnien 23/09/2026, thứ cấp](https://thanhnien.vn/phong-kham-tram-y-te-se-phai-danh-gia-chat-luong-hang-nam-185260923095957611.htm) |
| TT-54-2017-BYT | 54/2017/TT-BYT (29/12/2017) | Bộ tiêu chí ứng dụng CNTT tại cơ sở KCB (8 nhóm: hạ tầng, phần mềm quản lý, HIS, RIS-PACS, LIS, phi chức năng, ATTT, EMR) và xác định mức ứng dụng | 26/02/2018 | Còn HL một phần: Mục VIII PL I và tiêu chí EMR hết HL từ 06/06/2025 (TT 13/2025 Đ4 k3 b, xem EMR). Chưa thấy TT thay (kế hoạch Q2/2026) | Cơ sở KCB (thực tế: bệnh viện) | **chưa đọc gốc** lượt này; cấu trúc theo nguồn thứ cấp + EMR.md | chưa kiểm tra được |
| ND-90-2026 | 90/2026/NĐ-CP (30/03/2026) | Xử phạt VPHC y tế: Đ7 k2 b (báo cáo giám sát BTN), Đ38 k3 b (thu tiền chưa niêm yết), Đ39 k2 a (không gửi danh sách đăng ký hành nghề thay đổi), Đ39 k2 b → k6 d (không bảo đảm điều kiện hoạt động sau cấp phép) | 15/05/2026 | Còn HL | Cá nhân; tổ chức phạt gấp 2 (Đ4 k5, xem EMR.md) | **gốc-OCR** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| CT-07-2026-BYT | 07/CT-BYT (09/2026) | Xử lý "điểm nghẽn" CĐS y tế: 7 nhóm nhiệm vụ (xử lý nhiệm vụ quá hạn trước 30/11/2026; làm sạch 12 CSDL chuyên ngành; Sổ SKĐT theo KH 1261/KH-BYT; chuyển hệ thống lên TTDL quốc gia…) | Từ khi ký | Còn HL; **chưa tìm được bản gốc** | Đơn vị thuộc BYT; gián tiếp cơ sở KCB | **thứ cấp** | [suckhoedoisong, thứ cấp](https://suckhoedoisong.vn/bo-truong-bo-y-te-yeu-cau-day-manh-xu-ly-dut-diem-cac-diem-nghen-chuyen-doi-so-y-te-169260915171532468.htm) · [daibieunhandan, thứ cấp](https://daibieunhandan.vn/bo-y-te-7-nhom-nhiem-vu-day-manh-va-xu-ly-dut-diem-cac-diem-nghen-ve-chuyen-doi-so-y-te-thuc-day-trien-khai-de-an-06-10430624.html) |
| QD-2682-2026-BYT | 2682/QĐ-BYT (22/08/2026, theo kết quả tìm kiếm) | Danh mục thông tin cơ bản của CSDL về hoạt động KCB | Từ ngày ký | **Chưa XM** (thuvienphapluat trả 403; không tìm được bản gốc) | BYT; là "danh mục nội hàm thông tin" mà QĐ 2114 mục II.1 yêu cầu (suy luận) | chưa XM | chưa kiểm tra được |

**Văn bản inventory đã xử lý tình trạng:** ND-47-2024 → **bị bãi bỏ** bởi NĐ 194/2025 Đ40 k2 a (từ 19/08/2025). TT-54-2015-BYT → **bị bãi bỏ** bởi TT 15/2026 Đ65 k2 b (từ 01/07/2026). NQ-282-2025-CP, QD-3516-2025-BYT: chỉ là bối cảnh chiến lược, không đặt nghĩa vụ trực tiếp cho phần mềm cơ sở, không đọc lại trong lượt này.

**Chế tài liên quan (NĐ 90/2026, gốc-OCR; mức cá nhân, tổ chức gấp 2 theo Đ4 k5):**

| Hành vi | Điều khoản | Mức (cá nhân) |
|---|---|---|
| Không báo cáo hoặc báo cáo không đúng về giám sát bệnh truyền nhiễm | Đ7 k2 b | 1–3 triệu |
| Che giấu, không khai báo, khai báo không kịp thời BTN nhóm A của bản thân hoặc người khác; cố ý khai báo sai về BTN nhóm A | Đ7 k3 a, b | 10–20 triệu |
| Yêu cầu người bệnh thanh toán chi phí chưa niêm yết công khai | Đ38 k3 b | 1–3 triệu |
| Không gửi danh sách đăng ký hành nghề đã thay đổi đến cơ quan có thẩm quyền | Đ39 k2 a | 3–5 triệu |
| Không bảo đảm một trong các điều kiện hoạt động sau khi được cấp GPHĐ: cơ sở khác (trừ PKĐK và BV) / PKĐK / BV < 100 giường / BV 100–500 giường / BV > 500 giường | Đ39 k2 b; k3 b; k4 c; k5 c; k6 d | 3–5 tr / 10–20 tr / 20–30 tr / 30–40 tr / 40–50 tr; kèm tước GPHĐ 02–04 tháng (k7 a) |

Không tìm thấy trong NĐ 90/2026 hành vi riêng về "không cung cấp dữ liệu lên HTTT quản lý KCB" hoặc "không báo cáo sự cố y khoa". Chế tài cho báo cáo thống kê nằm ở nghị định xử phạt lĩnh vực thống kê, **chưa đọc**.

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### A. HTTT về quản lý hoạt động KCB (Luật KCB Đ112, TT 38/2024)

#### HTTT-BC-R01 — Nghĩa vụ cung cấp dữ liệu đầy đủ, chính xác, kịp thời
- **Căn cứ**: Luật KCB Đ112 k3: cơ sở KCB "có trách nhiệm cung cấp đầy đủ, chính xác, kịp thời các thông tin" lên HTTT. TT 38 Đ4 k1: cơ sở KCB có trách nhiệm "chuẩn hóa, thu thập và cung cấp đầy đủ dữ liệu về hoạt động khám bệnh, chữa bệnh tại đơn vị". TT 38 Đ15 (khoản cuối, văn bản đánh số nhầm thành "3") nhắc lại nghĩa vụ này. Luật Đ120 k8: BYT hoàn thành xây dựng và vận hành HTTT trước 01/01/2027.
- **Áp dụng cho**: mọi cơ sở KCB (TT 38 không phân biệt công, tư, BV, PK) · **Hiệu lực**: TT 38 có HL **01/01/2027**.
- **Mức**: BẮT BUỘC (về nghĩa vụ). Cách gửi, định dạng và tần suất thì **chưa được quy định** (xem R17).
- **Phần mềm phải**: có một lớp "xuất dữ liệu quản lý" độc lập với luồng XML BHYT, sinh được toàn bộ nhóm dữ liệu ở R02–R12 cho **mọi người bệnh**, cả BHYT lẫn tự chi trả; lưu nhật ký mỗi lần cung cấp (bộ dữ liệu, kỳ, thời điểm, kết quả).
- **Ghi chú / bẫy**: QĐ 2114/2026 cho thấy HTTT chưa sẵn sàng nhận dữ liệu từ HIS. GĐ 1 (2026) chỉ là nâng cấp Hệ thống quản lý hành nghề, thêm chức năng công bố danh sách đăng ký hành nghề và ký số. **GĐ 2 (2027–2028)** mới "kết nối, liên thông với Hệ thống thông tin của các cơ sở khám bệnh, chữa bệnh". Như vậy từ 01/01/2027 nghĩa vụ đã có hiệu lực pháp lý nhưng kênh tự động có thể chưa có (suy luận). Vendor nên chuẩn bị dữ liệu, không nên hứa "đã kết nối HTTT quản lý KCB".

#### HTTT-BC-R02 — Bộ dữ liệu ra viện của mọi ca (ngoại trú, nội trú, điều trị ngoại trú, điều trị ban ngày)
- **Căn cứ**: TT 38 Đ3 k4 (quản lý thông tin ra viện từng ca, tính tỷ lệ mắc, tử vong, phân bố theo tuổi, giới, nghề nghiệp, dân tộc, địa danh hành chính), Đ5 k7 ("Thông tin người bệnh ra viện đối với tất cả trường hợp ra viện"), Đ8 k1: (a) họ tên, ngày sinh, giới, **dân tộc, nghề nghiệp**, số định danh cá nhân hoặc số thẻ BHYT; (b) nơi thường trú, **nơi ở hiện nay**, số điện thoại; (c) ngày giờ nhập, ra viện, tình trạng ra viện, kết quả điều trị, **cân nặng trẻ em**, **số ngày giường hồi sức cấp cứu hoặc hồi sức tích cực**, nơi chuyển đi, nơi chuyển đến; (d) phẫu thuật, thủ thuật kèm **mã ICD-9 CM** (nếu có), gồm cả BHYT chi trả và tự chi trả; (đ) chẩn đoán xác định khi ra viện gồm bệnh chính, biến chứng, bệnh kèm theo, nguyên nhân theo **ICD-10**; (e) nguyên nhân tử vong chính.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2027.
- **Mức**: BẮT BUỘC (nội dung dữ liệu do TT quy định).
- **Phần mềm phải**: có trường bắt buộc và có cấu trúc cho dân tộc, nghề nghiệp (theo danh mục, không nhập tự do), địa chỉ thường trú tách khỏi nơi ở hiện tại, cân nặng trẻ em, số ngày giường HSCC/HSTC, cơ sở chuyển đi và chuyển đến (theo mã cơ sở); mã hóa PT/TT theo ICD-9-CM, kể cả dịch vụ không BHYT; chẩn đoán ra viện theo ICD-10 có phân vai (chính, biến chứng, kèm theo, nguyên nhân ngoài); chặn đóng hồ sơ ra viện khi thiếu các trường này.
- **Ghi chú / bẫy**: XML BHYT không có dân tộc, nghề nghiệp, nơi ở hiện tại, ICD-9-CM và không có ca tự chi trả (suy luận theo phạm vi QĐ 130/4750, xem BHYT-DATA). Đừng giả định "đã gửi XML là đủ".

#### HTTT-BC-R03 — Thuốc, dịch vụ kỹ thuật, chỉ số lâm sàng và cận lâm sàng của mọi lượt
- **Căn cứ**: TT 38 Đ8 k2 (danh mục thuốc, số lượng, đơn vị tính, "bao gồm cả thuốc được bảo hiểm y tế chi trả và thuốc người bệnh tự chi trả"), Đ8 k3 (kết quả một số chỉ số lâm sàng, CLS có giá trị chẩn đoán, tiên lượng, theo dõi), Đ10 k6 b (số lượng từng DVKT đã thực hiện, BHYT chi trả và tự chi trả).
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2027.
- **Mức**: BẮT BUỘC. Danh sách "một số chỉ số" chưa được ban hành → phần đó là BẮT BUỘC?.
- **Phần mềm phải**: thuốc và DVKT của lượt tự chi trả cũng phải được mã hóa theo danh mục dùng chung (mã thuốc, mã DVKT) như lượt BHYT; kết quả CLS lưu dạng có cấu trúc (mã chỉ số, giá trị, đơn vị), không chỉ là file PDF.
- **Ghi chú / bẫy**: nhiều PK tư chỉ mã hóa phần BHYT; phần dịch vụ "theo yêu cầu" đặt tên tự do. Khi phải gửi lên HTTT, dữ liệu này không dùng được (suy luận).

#### HTTT-BC-R04 — Tóm tắt điều trị phục vụ liên thông Sổ SKĐT
- **Căn cứ**: TT 38 Đ8 k4: với người bệnh nội trú, chuyển viện và đối tượng liên quan, gửi tóm tắt gồm (a) tiền sử (dị ứng, bệnh mạn tính, tiền sử phẫu thuật, sản khoa, **thiết bị cấy ghép**), bệnh sử, tình trạng lúc vào; (b) diễn biến lâm sàng; (c) tình trạng ra viện, kết quả; (d) tóm tắt CLS; (đ) phương pháp điều trị (nội khoa, ngoại khoa, PHCN, YHCT); (e) kế hoạch tiếp theo, **đơn thuốc ngoại trú**, lời dặn, lịch tái khám; (g) liên hệ bác sĩ hoặc cơ sở. NĐ 102 Đ10 k5 b: cơ sở y tế có trách nhiệm kết nối, chia sẻ dữ liệu với Sổ SKĐT trên ứng dụng định danh quốc gia.
- **Áp dụng cho**: mọi cơ sở KCB có nội trú hoặc chuyển viện · **Hiệu lực**: NĐ 102 đã HL 01/07/2025; TT 38 từ 01/01/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: sinh "Giấy ra viện / tóm tắt hồ sơ" có cấu trúc đủ 7 nhóm (a–g), gồm danh sách thiết bị cấy ghép và dị ứng ở dạng mã hóa; dùng lại cùng một bộ dữ liệu cho Sổ SKĐT (K4), HTTT quản lý KCB và phiếu chuyển cơ sở (BHYT-GD-R11).
- **Ghi chú / bẫy**: trùng với dữ liệu HSBA điện tử (EMR-R18, Phụ lục CV 365). Nên định nghĩa một mô hình tóm tắt duy nhất, ánh xạ ra nhiều đích.

#### HTTT-BC-R05 — Tử vong và người bệnh nặng xin về
- **Căn cứ**: TT 38 Đ3 k5 (quản lý nguyên nhân tử vong tại cơ sở, tử vong trên đường đến cơ sở, người bệnh nặng xin về), Đ5 k8 (thông tin giấy báo tử, chuỗi bệnh lý dẫn đến tử vong kèm ICD-10 và khoảng thời gian, theo Phiếu chẩn đoán nguyên nhân tử vong), Đ5 k9 (Phiếu thông tin người bệnh nặng xin về), Đ8 k1 e. TT 23/2025 PL IV Biểu 14/BCT có cột "BN nặng xin về", "tử vong trước viện", "tử vong tại viện", "số trường hợp tử vong được cấp giấy báo tử".
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: Biểu 14 đang áp dụng; TT 38 từ 01/01/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: có trạng thái ra viện phân biệt "tử vong tại viện", "tử vong trước khi đến viện / trên đường", "nặng xin về"; có biểu mẫu phiếu chẩn đoán nguyên nhân tử vong với chuỗi nguyên nhân (Ia→Id, II) mỗi dòng có ICD-10 và khoảng thời gian; liên kết giấy báo tử đã cấp.
- **Ghi chú / bẫy**: mẫu phiếu và giấy báo tử thuộc TT 24/2020/TT-BYT (K4, trạng thái hiệu lực chưa xác minh trong lượt này).

#### HTTT-BC-R06 — Dữ liệu người hành nghề, người thực hành và đăng ký hành nghề
- **Căn cứ**: Luật KCB Đ37 (nội dung đăng ký: họ tên, số GPHN, chức danh, vị trí, địa điểm, thời gian hành nghề, ngôn ngữ của người nước ngoài), Đ38 k1 (cơ sở gửi danh sách khi xin GPHĐ và khi có thay đổi), Đ38 k2 b (cơ quan cấp phép công bố trên HTTT trong 05 ngày làm việc), Đ36 k1 (nhiều cơ sở nhưng "không được trùng thời gian"), Đ23 k2 d (cơ sở hướng dẫn thực hành đăng ký danh sách người thực hành trên HTTT). NĐ 96/2023 Đ27 k12, Đ29 k1 c: người hành nghề nghỉ việc → báo cáo trong **03 ngày làm việc** và tạm dừng dịch vụ thuộc phạm vi của người đó nếu chưa có người thay; bổ sung người hành nghề → gửi danh sách trong **10 ngày**, và người hành nghề "chỉ được hành nghề sau khi hoàn thành thủ tục đăng ký hành nghề". NĐ 96 Đ7 k1 b, k6 b: đăng tải danh sách người thực hành và người đã hoàn thành thực hành trên trang của cơ sở và trên HTTT. TT 38 Đ9 k1–4 (trường dữ liệu: số định danh cá nhân, số GPHN/CCHN, nơi cấp, ngày cấp, văn bằng, phạm vi hành nghề, kỹ thuật được giao ngoài phạm vi, quyết định điều chỉnh, thời hạn GPHN; vị trí công tác, thời gian hành nghề ở cơ sở chính và cơ sở ngoài giờ; điểm cập nhật kiến thức y khoa liên tục; dữ liệu người thực hành). CV 4016/BYT-KCB (thứ cấp): cập nhật 100% dữ liệu người hành nghề và cơ sở trên Hệ thống quản lý quốc gia.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: Luật và NĐ 96 đang áp dụng; Hệ thống quản lý quốc gia (app.qlhanhnghekcb.gov.vn theo HDSD) đang vận hành.
- **Mức**: BẮT BUỘC (đăng ký, thời hạn báo thay đổi); NÊN (đồng bộ tự động, vì hệ thống quốc gia hiện chỉ có giao diện web và import file mẫu theo HDSD v1.0).
- **Phần mềm phải**: có sổ nhân sự hành nghề với đủ trường TT 38 Đ9; lưu **lịch hành nghề đã đăng ký** (khung giờ, địa điểm) và chặn gán người đó làm người chỉ định, kê đơn, thực hiện DVKT ngoài khung giờ hoặc ngoài phạm vi; chặn tài khoản lâm sàng của người **chưa hoàn tất đăng ký hành nghề**; khi nhân sự nghỉ việc tạo việc "báo cáo cơ quan cấp phép trong 03 ngày làm việc" và cảnh báo dịch vụ bị mất người phụ trách; xuất được file theo mẫu import của Hệ thống quản lý quốc gia; quản lý người thực hành (hợp đồng, người hướng dẫn tối đa 05 người cùng lúc theo NĐ 96 Đ7 k2 b, ngày bắt đầu và dự kiến kết thúc).
- **Ghi chú / bẫy**: mã người hành nghề dùng trong XML BHYT (MA_BAC_SI, xem BHYT-GD-R17) và mã liên thông người kê đơn (DUOC-R02) là **ba định danh khác nhau** cho cùng một người (số GPHN/CCHN, mã liên thông đơn thuốc, số định danh cá nhân). Phải lưu cả ba và đối soát. NĐ 90/2026 Đ39 k2 a phạt không gửi danh sách thay đổi; Đ38 k4 a phạt người hành nghề ngoài thời gian, địa điểm đã đăng ký.

#### HTTT-BC-R07 — Dữ liệu cơ sở: giấy phép, giường, thiết bị, kho
- **Căn cứ**: TT 38 Đ10 k1 (tên, mã cơ sở, số GPHĐ, ngày cấp, nơi cấp, phạm vi chuyên môn, người chịu trách nhiệm chuyên môn, địa chỉ, hình thức tổ chức, cấp chuyên môn kỹ thuật, tuyến, hạng, chuyên khoa, cơ quan chủ quản, có phải cơ sở hướng dẫn thực hành hoặc cơ sở BHYT, công lập hay tư nhân, giờ làm việc, năm thành lập); Đ10 k2 (giường kế hoạch, giường đăng ký với BV tư, giường thực tế; giường HSTC, **giường áp lực âm**, bàn mổ, bàn đẻ; danh mục TBYT và hiện trạng; **nhập, xuất, tồn thuốc, hóa chất, sinh phẩm định kỳ 06 tháng, 12 tháng**); Đ10 k3 (khoa, phòng; danh sách người hành nghề). TT 38 Đ3 k8: HTTT cấp mã cơ sở KCB thống nhất toàn quốc.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: lưu danh mục giường theo loại (kế hoạch, thực kê, HSTC, áp lực âm) có ngày hiệu lực; module TBYT có hiện trạng; báo cáo nhập-xuất-tồn thuốc, hóa chất, sinh phẩm theo kỳ 6 và 12 tháng; mã cơ sở là thuộc tính cấu hình, thay đổi được theo ngày hiệu lực (xem BHYT-DATA-R24).
- **Ghi chú / bẫy**: PK nhỏ thường không có module TBYT và hóa chất. TT 38 Đ3 k11 cũng nêu "kiểm kê, khấu hao tài sản và TBYT".

#### HTTT-BC-R08 — Dữ liệu chất lượng: đánh giá chất lượng, xét nghiệm, hài lòng, sự cố y khoa
- **Căn cứ**: TT 38 Đ10 k4 (kết quả đánh giá chất lượng cơ sở; chất lượng phòng xét nghiệm; đo lường hài lòng của người bệnh, người nhà và nhân viên; "Quản lý sự cố y khoa và phòng ngừa sự cố y khoa"), Đ3 k13, k14, k16 (phản hồi của người bệnh), Đ5 k2, k3.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2027.
- **Mức**: BẮT BUỘC? (TT 38 liệt kê nội dung thông tin nhưng chưa có biểu mẫu, chỉ số cụ thể).
- **Phần mềm phải**: giữ dữ liệu khảo sát hài lòng và phản hồi người bệnh có cấu trúc (không chỉ là file Excel rời); module sự cố y khoa xuất được số liệu tổng hợp (xem R33–R36).

#### HTTT-BC-R09 — Hoạt động chuyên môn và tài chính định kỳ 6 và 12 tháng
- **Căn cứ**: TT 38 Đ10 k5 (định kỳ 6 tháng, 12 tháng): (a) hoạt động chuyên môn, tổng số ngày điều trị, ngày điều trị trung bình, nhân lực, dược bệnh viện, mô hình bệnh tật, tử vong, điều dưỡng, PHCN, kiểm soát nhiễm khuẩn, chỉ đạo tuyến; (b) tài chính: chi tiết thu, chi, trích lập quỹ, "thông tin cảnh báo rủi ro tài chính", đề nghị và kết quả quyết toán BHYT. Đ3 k12.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2027.
- **Mức**: BẮT BUỘC (kỳ 6 và 12 tháng là quy định rõ duy nhất về tần suất trong TT 38).
- **Phần mềm phải**: báo cáo kỳ 6 tháng (01/01–30/06) và 12 tháng tính từ dữ liệu giao dịch; ngày điều trị và ngày điều trị trung bình tính theo cùng quy tắc với Biểu 9/BCT để số liệu khớp.
- **Ghi chú / bẫy**: với cơ sở tư, "thu, chi, trích lập các quỹ" là dữ liệu kế toán doanh nghiệp, thường nằm ngoài HIS. TT 38 không giới hạn phạm vi, nhưng tính khả thi với PK tư chưa rõ (suy luận).

#### HTTT-BC-R10 — Năng lực chuyên môn: danh mục kỹ thuật, phác đồ
- **Căn cứ**: TT 38 Đ10 k6 (a) danh mục DVKT được phê duyệt; (b) số lượng từng DVKT đã thực hiện; (c) danh mục hướng dẫn chẩn đoán, phác đồ, quy trình kỹ thuật và chăm sóc áp dụng tại cơ sở; Đ3 k15, k17.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: danh mục DVKT của cơ sở gắn số quyết định phê duyệt và ngày hiệu lực; chặn chỉ định DVKT chưa được phê duyệt (cũng là điều kiện thanh toán BHYT); thống kê số lần thực hiện theo mã DVKT tách BHYT và tự chi trả.

#### HTTT-BC-R11 — Niêm yết giá và công khai thông tin trên HTTT
- **Căn cứ**: Luật KCB Đ60 k3 (công khai giờ làm việc, danh sách người hành nghề và giờ làm việc của từng người tại cơ sở), Đ60 k4 (niêm yết giá dịch vụ KCB, giá dịch vụ chăm sóc, hỗ trợ theo yêu cầu "tại cơ sở và trên Hệ thống thông tin"). TT 38 Đ3 k3 (trang tin công khai: GPHĐ, kết quả đánh giá chất lượng, giờ làm việc, danh sách người hành nghề, giá, khuyến cáo phòng ngừa sự cố y khoa), Đ5 k11, Đ10 k7.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: niêm yết tại cơ sở đang áp dụng; phần "trên HTTT" phụ thuộc chức năng HTTT.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: bảng giá có phiên bản theo ngày hiệu lực, tách giá BHYT, giá tự chi trả, giá theo yêu cầu và giá dịch vụ hỗ trợ chăm sóc; xuất được bảng giá hiện hành ở dạng máy đọc được; chặn thu tiền dịch vụ không có trong bảng giá đang niêm yết.
- **Ghi chú / bẫy**: NĐ 90/2026 Đ38 k3 b phạt việc thu chi phí chưa niêm yết.

#### HTTT-BC-R12 — Hạch toán chi phí theo dịch vụ và theo ca bệnh
- **Căn cứ**: TT 38 Đ10 k8: (a) chi nhân công theo **mã nhân viên**, khoa/phòng, tổng thu nhập năm; (b) khấu hao tài sản, TBYT (mã thiết bị, khoa sử dụng, năm sử dụng, nguyên giá, nguồn); (c) khấu hao nhà (mã tòa nhà, diện tích, chi phí xây dựng, khoa sử dụng); (d) chi thường xuyên; (đ) chi trực tiếp theo đợt điều trị (công khám, ngày giường, thuốc, vật tư, máu, dịch truyền, xét nghiệm, CĐHA, PT/TT, vận chuyển). Đ3 k10.
- **Áp dụng cho**: mọi cơ sở KCB (theo câu chữ) · **Hiệu lực**: 01/01/2027.
- **Mức**: BẮT BUỘC? (TT ghi là "thông tin"; chưa có hướng dẫn phương pháp phân bổ và biểu mẫu).
- **Phần mềm phải**: (NÊN chuẩn bị) mô hình dữ liệu cho phép gắn chi phí gián tiếp vào khoa, phòng và phân bổ về ca bệnh; nhân viên, thiết bị, tòa nhà có mã ổn định.

#### HTTT-BC-R13 — Sửa sai và thông báo thay đổi "ngay"
- **Căn cứ**: TT 38 Đ4 k2: cơ sở "phải thông báo ngay" cho cơ quan quản lý HTTT khi có thay đổi, bổ sung hoặc phát hiện sai sót trong dữ liệu của mình. NĐ 102 Đ24 k1 và NĐ 194 Đ38 k4: thông báo kịp thời khi có thay đổi hoặc sai sót đối với dữ liệu đã cung cấp. TT 15/2026 Đ4 k1 b: phát hiện dữ liệu báo cáo thiếu, sai thì kiểm tra, cập nhật, điều chỉnh.
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: NĐ 102 và TT 15 đang áp dụng; TT 38 từ 01/01/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: mọi bản ghi đã gửi ra ngoài là bất biến; sửa đổi tạo phiên bản mới có lý do và tự động đưa vào hàng đợi "gửi bản điều chỉnh" tới mọi đích đã nhận bản cũ; có báo cáo "bản ghi đã gửi nhưng bị sửa sau khi gửi".

#### HTTT-BC-R14 — Cung cấp dữ liệu trong tình huống khẩn cấp và dịch nhóm A
- **Căn cứ**: TT 38 Đ4 k3 (dịch bệnh, thiên tai, tình trạng khẩn cấp: cung cấp dữ liệu theo yêu cầu; cơ quan yêu cầu phải nêu loại dữ liệu, mục đích, thời hạn sử dụng), Đ5 k4 (báo cáo thu dung, điều trị dịch nhóm A về BYT "ngay khi có yêu cầu"), Đ3 k18.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2027 (TT 38); nghĩa vụ báo cáo BTN đang áp dụng (R27–R28).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: truy vấn ad hoc theo nhóm bệnh (mã ICD-10 hoặc nhóm BTN) xuất được danh sách ca, diễn biến, số giường đang dùng trong vài giờ; lưu văn bản yêu cầu của cơ quan (loại dữ liệu, mục đích, thời hạn) làm căn cứ chia sẻ (liên quan DLCN).

#### HTTT-BC-R15 — Báo cáo tai nạn thương tích và báo cáo trực lễ, tết
- **Căn cứ**: TT 38 Đ5 k5 (báo cáo tai nạn giao thông, tai nạn thương tích "theo mẫu quy định": số ca cấp cứu, tình trạng, nguyên nhân sơ bộ theo ICD-10 dựa trên khai báo hoặc nhân viên y tế xác định), Đ5 k6 (báo cáo thường trực trong nghỉ lễ, tết về trực cấp cứu và điều trị; báo cáo tổng kết sau kỳ nghỉ). TT 15/2026 Đ53 k3: cơ sở KCB báo cáo kết quả giám sát người bị thương tích định kỳ 06 tháng và hằng năm cho CDC tỉnh trong **05 ngày làm việc** sau kỳ.
- **Áp dụng cho**: cơ sở có cấp cứu · **Hiệu lực**: TT 15 đang áp dụng; TT 38 từ 01/01/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: tại tiếp đón cấp cứu có trường nguyên nhân bên ngoài (chương XX ICD-10: V01–Y98), loại tai nạn, nơi xảy ra; báo cáo theo kỳ lễ, tết với khoảng ngày cấu hình được.

#### HTTT-BC-R16 — Dùng mã định danh từ CSDL quốc gia
- **Căn cứ**: TT 38 Đ2 k5 ("Sử dụng mã định danh đối tượng được quản lý đã được cấp bởi các cơ sở dữ liệu quốc gia"). NĐ 102 Đ6: số định danh cá nhân là mã định danh y tế của cá nhân. NĐ 278 Đ5 k1, k2: dữ liệu chủ quốc gia có "một nguồn tin cậy duy nhất" (áp trực tiếp cho cơ quan thuộc hệ thống chính trị).
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: NĐ 102 đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: khóa định danh người bệnh là số định danh cá nhân (12 số); mã cơ sở KCB, mã người hành nghề, mã thuốc, mã TBYT lấy từ nguồn quốc gia, không tự sinh; giữ mã nội bộ chỉ làm khóa kỹ thuật (xem EMR-R05).

#### HTTT-BC-R17 — Chuẩn đầu ra và hướng dẫn kỹ thuật kết nối
- **Căn cứ**: Luật KCB Đ112 k5 a (Bộ trưởng BYT quy định chuẩn định dạng dữ liệu đầu ra). TT 38 Đ6: chuẩn đầu ra "được thiết kế dựa trên các nội dung quy định tại Chương II", "trên nguyên tắc kế thừa các chuẩn đầu ra do Bộ Y tế đã ban hành phục vụ công tác quản lý nhà nước về khám bệnh, chữa bệnh và thanh toán chi phí khám chữa bệnh bảo hiểm y tế". TT 38 Đ3 k1: HTTT nhận dữ liệu qua biểu mẫu, dữ liệu có cấu trúc hoặc API. QĐ 2114 mục IV.2 b: TTYQG "ban hành hướng dẫn kỹ thuật phục vụ việc kết nối, tích hợp và liên thông dữ liệu với Hệ thống".
- **Áp dụng cho**: mọi cơ sở KCB, vendor · **Hiệu lực**: hướng dẫn kỹ thuật **chưa ban hành** tại 05/10/2026.
- **Mức**: BẮT BUỘC? (có nghĩa vụ, chưa có chuẩn).
- **Phần mềm phải**: thiết kế lớp xuất theo kiểu adapter có phiên bản, để khi TTYQG ra chuẩn chỉ cần thêm adapter. Ưu tiên tái dùng các bảng chuẩn đã có: XML BHYT (QĐ 130 và các bản sửa, BHYT-DATA-R01), Phụ lục CV 365 (EMR-R18), dữ liệu KSK (QĐ 1551). Hỗ trợ cả ba phương thức: nhập tay qua cổng, upload file có cấu trúc, gọi API.
- **Ghi chú / bẫy**: (suy luận) Câu "kế thừa các chuẩn đầu ra… thanh toán BHYT" cho thấy bộ XML BHYT có khả năng là xương sống. Cần chuẩn bị phần dữ liệu ngoài XML (R02 dân tộc, nghề nghiệp, ICD-9-CM, ca tự chi trả; R07–R12).

#### HTTT-BC-R18 — Bảo mật, toàn vẹn khi kết nối
- **Căn cứ**: TT 38 Đ12 k2 (bảo đảm "tính bảo mật, toàn vẹn và sẵn sàng của dữ liệu trong suốt quá trình truyền tải và sử dụng"), k3 (ngăn truy cập trái phép, rò rỉ, làm giả), k4 (chia sẻ đúng mục đích). NĐ 102 Đ23 k3 (cơ sở y tế bảo đảm ATTT, ANM cho CSDL và quá trình kết nối). TT 38 Đ7 (HTTT của BYT lập hồ sơ cấp độ).
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: NĐ 102 đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: TLS cho mọi kết nối ra ngoài; ký số hoặc ít nhất băm toàn vẹn gói dữ liệu gửi đi; khóa API và tài khoản cổng lưu trong kho bí mật, không nhúng trong cấu hình; nhật ký gửi không chứa dữ liệu sức khỏe dạng rõ (chi tiết ở ANM-R11, ANM-R12, DLCN-R10).

#### HTTT-BC-R19 — Hạ tầng CNTT kết nối HTTT là điều kiện GPHĐ
- **Căn cứ**: Luật KCB Đ52 k2 d: điều kiện cấp mới GPHĐ gồm cơ sở vật chất, "trong đó hạ tầng công nghệ thông tin phải bảo đảm kết nối với Hệ thống thông tin về quản lý hoạt động khám bệnh, chữa bệnh theo quy định tại khoản 1 Điều 112". Đ120 **k5** a: áp dụng từ **01/01/2027** cho hồ sơ xin GPHĐ nộp từ ngày đó; k5 b: **chậm nhất 01/01/2029** với cơ sở có GPHĐ trước 01/01/2027. Đ121 k13: hồ sơ GPHĐ nộp 2024–2026 không phải đáp ứng điều kiện này. NĐ 90/2026 Đ39 k2 b → k6 d: phạt "không bảo đảm một trong các điều kiện sau khi đã được cấp GPHĐ" theo quy mô.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/01/2027 (mới), 01/01/2029 (cũ).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: có tính năng kết nối HTTT (R01, R17) và **bằng chứng kết nối** xuất được để nộp kèm hồ sơ GPHĐ (cấu hình, nhật ký gửi thành công, xác nhận của hệ thống nhận).
- **Ghi chú / bẫy**: brief giao việc ghi "khoản 6, 6b" cho điều kiện CNTT. Thực ra **khoản 5** là điều kiện CNTT; **khoản 6 b** là tiêu chuẩn chất lượng cho cơ sở không phải BV (R38). Việc áp chế tài Đ39 cho điều kiện CNTT với cơ sở cũ trước 2029 là suy luận, chưa có hướng dẫn. Chưa có văn bản nào định nghĩa "hạ tầng CNTT bảo đảm kết nối" gồm những gì.

### B. CSDL quốc gia về y tế (NĐ 102/2025, QĐ 11/2026)

#### HTTT-BC-R20 — Kết nối, chia sẻ, đồng bộ với CSDLQG về y tế, CSDL của BYT, CSDL địa phương và Sổ SKĐT
- **Căn cứ**: NĐ 102 Đ23: cơ sở y tế (1) tạo lập, thu thập, chuẩn hóa dữ liệu và xây dựng CSDL của đơn vị; (2) "Kết nối, chia sẻ, đồng bộ dữ liệu của đơn vị với Cơ sở dữ liệu quốc gia về y tế, cơ sở dữ liệu của Bộ Y tế, cơ sở dữ liệu về y tế của địa phương và Sổ sức khỏe điện tử tích hợp trên ứng dụng định danh quốc gia"; (3) bảo đảm ATTT. Đ16 k1 d: CSDLQG lấy dữ liệu "từ các cơ sở dữ liệu do các cơ sở y tế quản lý". Đ14 k4: phạm vi gồm thông tin chứng sinh, BHYT, phòng bệnh, KCB, chăm sóc sức khỏe, báo tử. QĐ 11/2026 mục XVIII đưa CSDLQG về y tế vào danh mục, phương thức chia sẻ theo NĐ 278/2025.
- **Áp dụng cho**: mọi "cơ sở y tế" · **Hiệu lực**: 01/07/2025.
- **Mức**: BẮT BUỘC (nghĩa vụ). Đặc tả kỹ thuật CSDLQG chưa công bố (CT 07 yêu cầu hoàn thiện cấu trúc dữ liệu CSDLQG trong 9/2026, thứ cấp) → phần kỹ thuật là BẮT BUỘC?.
- **Phần mềm phải**: dùng chung lớp xuất của R17; giữ được nhật ký đồng bộ theo từng đích; hỗ trợ đồng bộ lại toàn bộ hoặc theo khoảng thời gian.
- **Ghi chú / bẫy**: CSDLQG về y tế (NĐ 102), HTTT quản lý KCB (TT 38), Hệ thống quản lý hành nghề (KH 1642), Cổng tiếp nhận BHYT, Hệ thống đơn thuốc QG, HTTT giám sát phòng bệnh và Sổ SKĐT là **các đích khác nhau**, do các đơn vị khác nhau vận hành. Chưa có văn bản hợp nhất "gửi một lần". Thiết kế phải chấp nhận nhiều đích.

#### HTTT-BC-R21 — Tôn trọng dữ liệu chủ quốc gia
- **Căn cứ**: NĐ 102 Đ15 (dữ liệu chủ: phạm vi hoạt động của cơ sở, chứng chỉ hành nghề, định danh và lưu hành thuốc, TBYT, chứng sinh, dữ liệu KCB, báo tử), Đ10 k3 (dữ liệu chủ trong CSDLQG "có giá trị sử dụng chính thức, tương đương văn bản giấy"). NĐ 278 Đ5.
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: đang áp dụng.
- **Mức**: NÊN với phần mềm cơ sở (không có điều khoản buộc cơ sở tư đồng bộ dữ liệu chủ); BẮT BUỘC với hệ thống của cơ quan nhà nước (NĐ 278 Đ5 k1).
- **Phần mềm phải**: lấy thông tin GPHN, phạm vi hành nghề, số đăng ký thuốc, TBYT từ nguồn quốc gia khi tra cứu được; đánh dấu nguồn và thời điểm đồng bộ; cảnh báo khi dữ liệu nội bộ khác dữ liệu chủ.

### C. Báo cáo thống kê ngành y tế (TT 23/2025, sắp được thay)

#### HTTT-BC-R22 — Sổ ghi chép ban đầu theo mẫu
- **Căn cứ**: TT 23 Đ3 k1 + PL III: A1/CSYT Sổ khám bệnh (TYT, **phòng khám**; 14 cột: họ tên, giới, ngày sinh, giấy tờ tùy thân, số thẻ BHYT, địa chỉ, dân tộc, nghề nghiệp, triệu chứng, chẩn đoán, phương pháp điều trị, y bác sĩ khám, ghi chú); A2.1/A2.2 tiêm chủng; A3 khám thai; A4 sổ đẻ; A5.1 biện pháp tránh thai; A5.2 phá thai (TYT, khoa sản BV, NHS, PK…); A6–A12 cho TYT.
- **Áp dụng cho**: TYT, PK, khoa sản BV và cơ sở có dịch vụ tương ứng · **Hiệu lực**: đến 28/02/2027 (văn bản thay có thể đổi mẫu).
- **Mức**: BẮT BUỘC (đến khi TT 23 hết HL).
- **Phần mềm phải**: in hoặc xuất được sổ theo mẫu từ dữ liệu khám (không bắt nhập hai lần); với PK sản phụ khoa có sổ A3, A4, A5.x.
- **Ghi chú / bẫy**: sổ yêu cầu dân tộc và nghề nghiệp, trùng yêu cầu R02.

#### HTTT-BC-R23 — Báo cáo tháng, năm theo PL IV; thời hạn; kỳ báo cáo
- **Căn cứ**: TT 23 Đ4 (kỳ tháng: 0h00 ngày 01 đến 24h00 ngày cuối tháng; kỳ năm: 01/01–31/12; đột xuất phải có văn bản), Đ5 k1 (đơn vị gửi: đơn vị cấp tỉnh, TW và "các cơ sở y tế tư nhân đặt trụ sở trên địa bàn tỉnh"; đơn vị nhận: đơn vị đầu mối do UBND tỉnh phân công; thời hạn **05 ngày làm việc** sau kỳ), Đ6 k1 (báo cáo đầy đủ, chính xác, đúng hạn, chịu trách nhiệm; kiểm tra, cung cấp lại khi được yêu cầu). PL IV: 14 biểu /BCT; Biểu 9 (cơ sở, giường bệnh, hoạt động KCB), Biểu 11 (mắc, tử vong BTN gây dịch), Biểu 14 (bệnh tật, tử vong tại BV theo ICD-10) kỳ tháng; Biểu 2 kỳ năm.
- **Áp dụng cho**: BV công, BV tư, PK · **Hiệu lực**: đến 28/02/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: bộ sinh báo cáo theo kỳ dương lịch (múi giờ Việt Nam, ranh giới 24h00 ngày cuối), tính từ dữ liệu giao dịch, có lịch hạn nộp; lưu snapshot báo cáo đã nộp (số liệu + truy vấn + phiên bản định nghĩa) để "cung cấp lại" khi được hỏi.
- **Ghi chú / bẫy**: thân TT ghi "05 ngày làm việc", còn bảng danh mục PL IV ghi "05 ngày" (Biểu 2 năm: "15 ngày"). Nên lấy mốc sớm hơn (suy luận). TT 23 Đ5 đánh số nhảy từ k2 sang k4 (không có k3). Biểu 1, 3–8, 10, 12, 13 chủ yếu do TYT hoặc đơn vị đầu mối tổng hợp; với cơ sở KCB, quan trọng nhất là Biểu 9, 11, 14 (suy luận theo nội dung biểu).

#### HTTT-BC-R24 — Biểu 14/BCT: bệnh tật và tử vong theo ICD-10
- **Căn cứ**: TT 23 PL IV Biểu 14/BCT: theo từng bệnh hoặc nhóm bệnh và mã ICD-10. Tại khoa khám bệnh: tổng số, nữ, trẻ em < 15 tuổi, tử vong trước viện. Nội trú: mắc (tổng, nữ), tử vong (tổng, nữ), trẻ em < 15 tuổi và < 5 tuổi (mắc, tử vong), BN nặng xin về, số trường hợp tử vong được cấp giấy báo tử.
- **Áp dụng cho**: BV và cơ sở có nội trú (biểu ghi "Tên cơ sở Y tế/Sở Y tế") · **Hiệu lực**: đến 28/02/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: bảng ánh xạ ICD-10 → dòng của Biểu 14 (danh mục nhóm bệnh trong PL IV), có phiên bản; tính tuổi tại ngày vào viện; phân biệt khám ngoại trú và nội trú.

#### HTTT-BC-R25 — Chuyển sang chế độ báo cáo mới trước 01/03/2027
- **Căn cứ**: TT 23 Đ7 k2 (hết HL từ 01/03/2027). Dự thảo TT thay thế dự kiến xong tháng 10/2026 (thứ cấp, R tham chiếu DT-TT23).
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: 01/03/2027.
- **Mức**: BẮT BUỘC? (chưa có văn bản thay; rủi ro "khoảng trống" nếu văn bản mới ban hành muộn).
- **Phần mềm phải**: định nghĩa biểu, chỉ tiêu, kỳ, hạn nộp ở dạng cấu hình có ngày hiệu lực; chạy song song biểu cũ (kỳ tháng 02/2027 nộp đầu tháng 03/2027) và biểu mới.
- **Ghi chú / bẫy**: báo cáo kỳ tháng 02/2027 có hạn rơi vào sau 01/03/2027, khi TT 23 đã hết HL. Cách xử lý chưa rõ, cần hỏi cơ quan (mục 7).

### D. Giám sát bệnh truyền nhiễm và phòng bệnh (Luật Phòng bệnh 2025, TT 15/2026)

#### HTTT-BC-R26 — Báo cáo trực tuyến qua HTTT giám sát trong phòng bệnh; dự phòng khi hệ thống lỗi
- **Căn cứ**: Luật Phòng bệnh Đ13 k7 (BYT quy định chế độ báo cáo giám sát), Đ17 k3 g (cơ sở y tế "Thông tin, báo cáo đầy đủ, chính xác, kịp thời về bệnh truyền nhiễm và dịch bệnh"). TT 15 Đ3 k2 (cơ sở y tế cập nhật, cung cấp dữ liệu lên HTTT giám sát), Đ4 k2 a (báo cáo **trực tuyến** qua HTTT giám sát), Đ4 k2 b (khi HTTT gặp sự cố hoặc chưa đủ chức năng: báo cáo bằng văn bản điện tử hoặc giấy, sau đó "phải thực hiện cập nhật, bổ sung dữ liệu" vào HTTT khi đã khắc phục), Đ4 k3 và Đ10 k2 a (danh mục, mẫu giám sát, mẫu báo cáo "theo hướng dẫn chuyên môn của Cục Phòng bệnh"), Đ66 k2 (hướng dẫn chuyên môn cũ tiếp tục áp dụng đến khi có hướng dẫn mới). Đ61 k2: Cục QLKCB chỉ đạo cơ sở KCB "liên thông trực tuyến, kết nối thông tin, dữ liệu giữa phần mềm của cơ sở khám bệnh, chữa bệnh với hệ thống, phần mềm giám sát trong phòng bệnh".
- **Áp dụng cho**: cơ sở KCB, cơ sở xét nghiệm (Đ10 k2) · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (báo cáo trực tuyến); BẮT BUỘC? (liên thông tự động giữa HIS và hệ thống giám sát: Đ61 k2 là nhiệm vụ của Cục, chưa có chuẩn).
- **Phần mềm phải**: khi chẩn đoán (hoặc kết quả XN) thuộc danh mục BTN cần giám sát, tạo "phiếu báo cáo ca bệnh" chờ gửi với dữ liệu hành chính, dịch tễ, lâm sàng, mẫu bệnh phẩm (TT 15 Đ7 k1 a–đ); theo dõi trạng thái đã nhập lên HTTT giám sát (thủ công hoặc API); khi gửi qua kênh dự phòng (giấy, email) phải đánh dấu "chưa đồng bộ" và nhắc nhập bổ sung.
- **Ghi chú / bẫy**: hệ thống đang vận hành là "HTQLGS bệnh truyền nhiễm" (eCDS, gs.vadp.gov.vn, xây dựng theo TT 54/2015). TT 15 không gọi tên hệ thống này; việc eCDS có phải là "HTTT giám sát trong phòng bệnh" theo TT 15 hay không thì **chưa xác minh**.

#### HTTT-BC-R27 — Thời hạn: ca nghi ngờ 24 giờ, tử vong do BTN 24 giờ
- **Căn cứ**: TT 15 Đ10 k1: cơ quan, tổ chức, cá nhân phát hiện người nghi ngờ mắc BTN "có trách nhiệm thông báo trong vòng 24 giờ cho Trạm Y tế cấp xã trên địa bàn". Đ10 k2 b: cơ sở KCB báo cáo trường hợp tử vong do hoặc nghi do BTN "trong vòng 24 giờ kể từ khi có trường hợp tử vong". Đ26 k1 d: báo cáo ổ dịch hằng ngày đến khi kết thúc (việc của TYT xã). NĐ 90/2026 Đ7 k2 b: phạt không báo cáo hoặc báo cáo không đúng.
- **Áp dụng cho**: cơ sở KCB, cơ sở xét nghiệm · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: đồng hồ hạn 24 giờ tính từ thời điểm ghi chẩn đoán nghi ngờ hoặc thời điểm tử vong; cảnh báo leo thang (bác sĩ → khoa → phòng KHTH) trước hạn; lưu bằng chứng thời điểm gửi.
- **Ghi chú / bẫy**: Đ10 k1 ghi đích nhận là **TYT xã**, không phải CDC tỉnh. Thời hạn báo cáo **từng ca** theo nhóm bệnh (TT 54/2015 cũ phân 24 giờ và 48 giờ theo bệnh) **không còn nằm trong thông tư**, mà chuyển sang hướng dẫn chuyên môn của Cục Phòng bệnh (chưa tìm thấy). Câu hỏi "24 hay 48 giờ" của inventory chưa thể trả lời dứt khoát; xem mục 7.

#### HTTT-BC-R28 — Giám sát dựa vào sự kiện: chùm ca, gia tăng bất thường, nhân viên y tế mắc
- **Căn cứ**: TT 15 Đ9 k1 a: nguồn thông tin gồm thông báo của cơ sở KCB "về các chùm trường hợp bệnh truyền nhiễm chưa rõ nguyên nhân, sự gia tăng bất thường số lượng người bệnh, nhân viên y tế mắc hoặc nghi ngờ mắc bệnh truyền nhiễm hoặc các sự kiện y tế bất thường khác"; Đ9 k1 b: cơ sở KCB cung cấp cho TYT xã hoặc CDC tỉnh.
- **Áp dụng cho**: cơ sở KCB · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC? (Đ9 mô tả nguồn thông tin, không đặt thời hạn cho cơ sở).
- **Phần mềm phải**: (NÊN) báo cáo theo dõi số ca theo hội chứng hoặc nhóm ICD-10 theo ngày, so với ngưỡng nền; cảnh báo chùm ca ở cùng địa chỉ hoặc đơn vị; cờ "nhân viên y tế" trên hồ sơ người bệnh.

#### HTTT-BC-R29 — Bệnh không lây nhiễm, rối loạn tâm thần: báo cáo trong 05 ngày làm việc; lộ trình lên HTTT đến 2030
- **Căn cứ**: TT 15 Đ32–33 k1 (cơ sở KCB báo cáo kết quả giám sát BKLN về CDC tỉnh trong **05 ngày làm việc** sau kỳ tháng hoặc năm), Đ39–40 k1 (rối loạn tâm thần, như trên), Đ46 k2 a (dinh dưỡng: TYT xã thu từ cơ sở KCB), Đ66 k1 (chậm nhất **01/01/2030** báo cáo BKLN, RLTT, dinh dưỡng, thương tích phải thực hiện trên HTTT giám sát).
- **Áp dụng cho**: cơ sở KCB trên địa bàn tỉnh · **Hiệu lực**: 01/07/2026; lộ trình số hóa đến 01/01/2030.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: báo cáo kỳ tháng và năm về số người mắc BKLN, RLTT được phát hiện, quản lý (theo mẫu của Cục Phòng bệnh khi có); lịch hạn 05 ngày làm việc.

#### HTTT-BC-R30 — Danh mục bệnh truyền nhiễm theo nhóm A, B, C mới
- **Căn cứ**: QĐ 1965/QĐ-BYT năm 2026 (thứ cấp): nhóm A 15 bệnh, B 47, C 19, áp dụng từ 01/07/2026, bãi bỏ các QĐ danh mục trước. NĐ 90 Đ7 k3: mức phạt riêng với nhóm A.
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (dùng danh mục hiện hành); nội dung danh mục chưa đọc bản gốc.
- **Phần mềm phải**: bảng danh mục BTN có phiên bản (mã bệnh, nhóm A/B/C, mã ICD-10 tương ứng, quy tắc báo cáo); cập nhật thay cho danh mục theo Luật PCBTN 2007.

#### HTTT-BC-R31 — Bảo mật thông tin người mắc bệnh truyền nhiễm trong báo cáo
- **Căn cứ**: Luật Phòng bệnh Đ17 k1 c (quyền riêng tư, bảo vệ thông tin cá nhân và tình trạng sức khỏe liên quan đến BTN, trừ trường hợp luật khác quy định). TT 15 Đ3 k3.
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: chỉ người có vai trò "báo cáo dịch tễ" xem được hàng đợi báo cáo BTN; báo cáo tổng hợp không chứa định danh; HIV và các bệnh đặc thù theo DLCN-R32.

### E. Sự cố y khoa (Luật KCB Đ71, TT 43/2018, TT 35/2024)

#### HTTT-BC-R32 — Kênh báo cáo sự cố: tự nguyện và bắt buộc; nội dung tối thiểu; lưu giữ mọi báo cáo
- **Căn cứ**: Luật KCB Đ71 k1 (phòng ngừa dựa trên nhận diện, báo cáo, phân tích nguyên nhân, khuyến cáo; khuyến cáo công khai trên HTTT), k2 (trách nhiệm người đứng đầu và người làm việc tại cơ sở). TT 43 Đ5 k1 a (báo cáo tự nguyện với sự cố mục 1–6 PL I, tức NC0–NC2), k1 b (báo cáo **bắt buộc** với mục 7–9 = NC3, và sự cố nghiêm trọng: làm chết 01 người bệnh và nghi còn nguy cơ, hoặc làm chết ≥ 02 người bệnh cùng tình huống hoặc nguyên nhân), Đ5 k2 a (tự nguyện: văn bản hoặc **báo cáo điện tử**; khẩn thì báo trực tiếp hoặc điện thoại rồi ghi nhận lại), Đ5 k3 a (nội dung tối thiểu: địa điểm, thời điểm, mô tả, đánh giá sơ bộ, tình trạng người bị ảnh hưởng, xử lý ban đầu theo **Mẫu PL III**), Đ5 k3 b ("Tất cả các sự cố y khoa được báo cáo phải được ghi nhận và lưu giữ vào hồ sơ hoặc vào hệ thống báo cáo sự cố y khoa trực tuyến"). TT 35/2024 PL Mục V 4.6: "Báo cáo sự cố y khoa" là một tiêu chuẩn chất lượng cơ bản của bệnh viện.
- **Áp dụng cho**: mọi cơ sở KCB (TT 43 Đ1 k3); với BV, còn là tiêu chuẩn chất lượng cơ bản · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: form báo cáo sự cố điện tử với các trường của PL III (số báo cáo/mã sự cố, ngày báo cáo, hình thức tự nguyện hay bắt buộc, đơn vị báo cáo, đối tượng bị ảnh hưởng: người bệnh, người nhà/khách, nhân viên, TTB/hạ tầng; khoa/vị trí, ngày giờ xảy ra, mô tả, đề xuất ban đầu, xử lý ban đầu, đã thông báo bác sĩ, người nhà, người bệnh, đã ghi vào HSBA: Có/Không/Không ghi nhận); mở từ mọi màn hình (nút "báo sự cố"), cho người không đăng nhập HIS (khách, nhân viên ngoài) gửi qua kênh riêng; không cho xóa báo cáo.
- **Ghi chú / bẫy**: TT 43 Đ1 k2 loại trừ sự cố tiêm chủng, ADR và AE của thử nghiệm lâm sàng. ADR đi kênh Trung tâm DI&ADR (xem DUOC). Phần mềm cần tách loại để không báo nhầm kênh.

#### HTTT-BC-R33 — Thời hạn báo cáo sự cố bắt buộc
- **Căn cứ**: TT 43 Đ5 k2 b (NC3: văn bản hỏa tốc hoặc báo cáo điện tử; sự cố nghiêm trọng: báo trước bằng điện thoại **trong 01 giờ** kể từ khi phát hiện), Đ5 k3 a (người gây ra hoặc phát hiện → trưởng khoa và bộ phận quản lý sự cố → lãnh đạo → lãnh đạo "báo cáo ngay cho cơ quan quản lý"), Đ5 k3 b (sự cố nghiêm trọng phải chia sẻ đến cơ quan quản lý trực tiếp và BYT), Đ9 k1 b, c (SYT, BYT báo nhanh trong 24 giờ). Đ8 k1 a (NC2, NC3: bộ phận quản lý sự cố báo ngay người đứng đầu).
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: khi phân loại NC3 hoặc "nghiêm trọng", tự động gửi cảnh báo (SMS, app) tới lãnh đạo và bộ phận quản lý chất lượng; đồng hồ 01 giờ cho cuộc gọi báo trước, có trường ghi nhận "đã gọi lúc, người nhận"; sinh văn bản báo cáo theo PL III có đủ họ tên người báo cáo (bắt buộc với loại này) để gửi cơ quan quản lý.

#### HTTT-BC-R34 — Phân loại, phân tích nguyên nhân gốc, tổng hợp định kỳ
- **Căn cứ**: TT 43 Đ7 k1 (phân loại theo 3 tiêu chí: mức tổn thương PL I [A–I, NC0–NC3], nhóm sự cố Mục II PL IV, nhóm nguyên nhân Mục IV PL IV), Đ7 k2 (NC3 phân loại tiếp theo danh mục 28 loại sự cố nghiêm trọng PL II), Đ8 k1 a (bộ phận quản lý sự cố báo cáo người đứng đầu **1 tuần 1 lần**), Đ8 k1 c (nhóm chuyên gia đề xuất giải pháp **trong 60 ngày** kể từ khi nhận báo cáo phân tích), Đ6 k1 (tổng hợp gửi cơ quan quản lý **6 tháng một lần**: số báo cáo bắt buộc và tự nguyện, tần suất từng loại, kết quả phân tích nguyên nhân gốc, giải pháp đã đề xuất và triển khai), Đ9 k2 a (phản hồi cho người báo cáo tại giao ban), Đ11 (kế hoạch khắc phục).
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: quy trình trạng thái (tiếp nhận → phân loại 3 trục → phân tích RCA → khuyến cáo → kế hoạch khắc phục → đóng); đồng hồ 60 ngày; báo cáo tuần cho lãnh đạo; báo cáo tổng hợp 6 tháng đúng 4 nội dung Đ6 k1 b; liên kết sự cố với HSBA (đánh dấu hồ sơ liên quan là lưu vĩnh viễn, xem EMR-R22 dòng 38 TT 33/2025).

#### HTTT-BC-R35 — Bảo mật và ẩn danh người báo cáo
- **Căn cứ**: TT 43 Đ3 k3 ("Hồ sơ phòng ngừa sự cố y khoa được quản lý theo quy chế bảo mật thông tin"), Đ12 k3 (giữ bí mật, ẩn danh tính cá nhân hoặc cơ sở báo cáo; phân công bộ phận đầu mối "có quyền tra cứu và công bố thông tin"), Đ3 k1 (không nhằm mục đích khác). NĐ 90/2026 Đ38, điểm h của một khoản xử phạt (gốc-OCR, chưa xác định số khoản): phạt hành vi "đăng tải các thông tin mang tính quy kết về trách nhiệm" của người hành nghề, cơ sở KCB khi xảy ra sự cố y khoa mà chưa có kết luận của cơ quan có thẩm quyền.
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: cho phép báo cáo tự nguyện **ẩn danh** (không lưu user ID vào bản ghi hiển thị; tách khóa liên kết danh tính, chỉ bộ phận đầu mối mở được); phân quyền xem module sự cố chỉ cho bộ phận quản lý chất lượng; nhật ký truy cập riêng; báo cáo tổng hợp gửi ra ngoài không có tên người báo cáo, trừ báo cáo bắt buộc.

### F. Chất lượng và mức ứng dụng CNTT

#### HTTT-BC-R36 — Tự đánh giá chất lượng hằng năm và công khai
- **Căn cứ**: Luật KCB Đ58 k3 (hằng năm cơ sở tự đánh giá theo tiêu chuẩn cơ bản Đ57 k1 a), Đ58 k5 (kết quả công khai tại cơ sở và trên HTTT), Đ120 **k6** (tiêu chuẩn cơ bản áp từ 01/01/2025 với BV; **01/01/2027 với hình thức tổ chức khác**). TT 35/2024 Đ1 k3 (BV: đánh giá 1 lần/năm trong **quý I** năm sau; đạt khi mọi tiêu chuẩn "Có"), Đ2 k4 c (thực hiện đánh giá và báo cáo kết quả). Dự thảo TT cho cơ sở không phải BV (thứ cấp): cùng cơ chế, có bổ sung tiêu chí CNTT và CĐS.
- **Áp dụng cho**: BV (đang áp dụng); PK, TYT, phòng chẩn trị… từ 01/01/2027 **khi có TT** · **Hiệu lực**: như trên.
- **Mức**: BẮT BUỘC (BV); BẮT BUỘC? (cơ sở khác: Luật đã có mốc, chưa có tiêu chuẩn ban hành).
- **Phần mềm phải**: (NÊN) module checklist tự đánh giá với bằng chứng đính kèm theo từng tiêu chuẩn; xuất kết quả để công khai.
- **Ghi chú / bẫy**: TT 35 **không có tiêu chí kỹ thuật CNTT**. Trả lời câu hỏi mở số 6: với BV, tiêu chuẩn cơ bản chỉ đòi có phòng/bộ phận CNTT và có báo cáo sự cố y khoa. Với cơ sở ngoài BV, báo chí nói dự thảo có tiêu chí CNTT nhưng chưa thấy toàn văn.

#### HTTT-BC-R37 — Mức ứng dụng CNTT theo TT 54/2017
- **Căn cứ**: TT 54/2017 (phần còn HL: hạ tầng, phần mềm quản lý, HIS, RIS-PACS, LIS, phi chức năng, ATTT). TT 13/2025 Đ4 k3 b đã bãi bỏ Mục VIII PL I và các tiêu chí EMR (xem EMR.md). TT thay thế chưa ban hành.
- **Áp dụng cho**: cơ sở KCB, thực tế là BV · **Hiệu lực**: đang áp dụng một phần.
- **Mức**: NÊN (TT 54 là bộ tiêu chí đánh giá; lượt này chưa đọc bản gốc nên chưa xác định có nghĩa vụ báo cáo mức ứng dụng định kỳ hay không).
- **Phần mềm phải**: vendor HIS/LIS/PACS nên giữ bảng đối chiếu chức năng ↔ tiêu chí TT 54 để hỗ trợ khách hàng tự đánh giá, và theo dõi DT-TT54.

---

**Tổng số yêu cầu: 37** (R01–R37), xếp theo mức chính của từng mục:

| Mức | Số lượng | Yêu cầu |
|---|---|---|
| BẮT BUỘC | 30 | R01–R07, R09–R11, R13–R16, R18–R20, R22–R24, R26, R27, R29–R36 |
| BẮT BUỘC? | 5 | R08, R12, R17, R25, R28 |
| NÊN | 2 | R21, R37 |

Một số mục BẮT BUỘC có phần phụ ở mức thấp hơn: R03 (danh sách "một số chỉ số" CLS chưa ban hành), R06 (đồng bộ tự động với Hệ thống QL hành nghề là NÊN), R20 (đặc tả kỹ thuật CSDLQG chưa có), R26 (liên thông tự động HIS ↔ hệ thống giám sát), R36 (cơ sở ngoài BV chờ TT).

---

## 3. Pattern thiết kế

### P1. Hộp thư đi pháp định (Regulatory Outbox) nhiều đích
- **Giải quyết**: R01, R13, R17, R20, R23, R26, R27.
- **Mô tả**: mọi sự kiện nghiệp vụ (ra viện, tử vong, chẩn đoán BTN, sự cố NC3, thay đổi nhân sự, thay đổi giá) ghi vào bảng outbox trong **cùng transaction** với dữ liệu gốc. Bộ phát tán đọc outbox, áp **quy tắc định tuyến** (sự kiện X → các đích Y), tạo một "lần gửi" cho mỗi đích. Mỗi đích có adapter riêng: HTTT quản lý KCB, CSDLQG y tế, Hệ thống QL hành nghề, HTTT giám sát phòng bệnh, Cổng BHXH, Hệ thống đơn thuốc QG, Sổ SKĐT, và "kênh thủ công" (in hoặc xuất file).
- **Mô hình dữ liệu**:
  - `reg_event(id, event_type, source_table, source_id, source_version, occurred_at, payload_hash, created_at)`.
  - `reg_destination(code, name, operator, transport[api|file|portal_manual], spec_version, active_from, active_to)`.
  - `reg_route(event_type, destination_code, deadline_rule, active_from, active_to)`, trong đó `deadline_rule` là biểu thức như `+24h`, `+5 working_days after period_end`, `+1h`.
  - `reg_submission(id, event_id, destination_code, spec_version, status[pending|sent|acked|rejected|superseded|manual_pending_backfill], due_at, sent_at, ack_at, ack_ref, error_code, attempt, supersedes_submission_id)`. Unique `(event_id, destination_code, source_version)`.
  - Chỉ mục `(status, due_at)` để quét hạn; `(destination_code, sent_at)` để đối soát.
- **Đánh đổi**: thêm bảng và tiến trình nền, nhưng tách lỗi của từng đích; dễ thêm đích mới khi TTYQG ra chuẩn. Phải chống gửi trùng bằng idempotency key = `event_id + destination + source_version`.

### P2. Đồng hồ hạn pháp định và leo thang
- **Giải quyết**: R06 (03 ngày làm việc, 10 ngày), R23 (05 ngày làm việc), R27 (24 giờ), R29 (05 ngày làm việc), R33 (01 giờ, "ngay"), R34 (60 ngày, tuần, 6 tháng).
- **Mô tả**: một dịch vụ lịch dùng chung tính `due_at` theo lịch làm việc Việt Nam (bảng ngày nghỉ lễ, tết có phiên bản theo năm), múi giờ `Asia/Ho_Chi_Minh`. Cảnh báo ở các mốc 50%, 80%, 100% hạn; quá hạn thì tạo bản ghi "vi phạm hạn" bất biến.
- **Mô hình dữ liệu**: `vn_holiday(date, kind, source_doc)`; `deadline_alert(submission_id, threshold, notified_to, notified_at)`.
- **Đánh đổi**: "ngày" và "ngày làm việc" lẫn lộn giữa thân TT và phụ lục (R23). Lưu cả hai cách tính và cảnh báo theo mốc sớm hơn.

### P3. Kênh dự phòng có nhập bù (manual fallback with backfill)
- **Giải quyết**: R26 (TT 15 Đ4 k2 b), R33, R17 (giai đoạn HTTT chưa có API).
- **Mô tả**: khi adapter lỗi quá N lần hoặc đích tuyên bố bảo trì, người dùng có quyền chuyển lần gửi sang `manual_pending_backfill`, in hoặc xuất file theo mẫu, ghi "đã gửi bằng kênh nào, lúc nào, cho ai". Khi đích hoạt động lại, hệ thống nhắc nhập bù và chỉ đóng khi có `ack_ref` của hệ thống.
- **Mô hình dữ liệu**: `reg_submission.status = manual_pending_backfill`; `manual_delivery(submission_id, channel[paper|email|phone], recipient, delivered_at, evidence_file)`.
- **Đánh đổi**: tăng thao tác cho người dùng, đổi lại có bằng chứng tuân thủ khi hệ thống quốc gia lỗi (đúng tinh thần BHYT-GD-R21).

### P4. Động cơ báo cáo thống kê theo định nghĩa có phiên bản
- **Giải quyết**: R22–R25, R09, R15, R29.
- **Mô tả**: mỗi biểu (Biểu 9, 11, 14/BCT; báo cáo BKLN, RLTT, thương tích; báo cáo 6/12 tháng TT 38) là một **định nghĩa** gồm: chỉ tiêu, truy vấn, bảng ánh xạ (ICD-10 → dòng biểu), kỳ, hạn, ngày hiệu lực. Mỗi lần nộp lưu **snapshot** (số liệu, phiên bản định nghĩa, hash tập dữ liệu nguồn, người duyệt) để cung cấp lại theo TT 23 Đ6 k1 b.
- **Mô hình dữ liệu**: `report_def(code, version, legal_basis, period_type, deadline_rule, valid_from, valid_to)`; `report_row_map(report_code, version, row_code, icd10_from, icd10_to, label)`; `report_run(id, report_code, version, period_start, period_end, generated_at, data_hash, approved_by, submitted_at, submission_id)`; `report_cell(run_id, row_code, col_code, value)`.
- **Đánh đổi**: tốn công dựng định nghĩa, nhưng chuyển chế độ ngày 01/03/2027 chỉ là thêm phiên bản. Ràng buộc `valid_from/valid_to` không chồng lấn trên cùng `code`.

### P5. Sổ nhân sự hành nghề có lịch đăng ký và đối soát định danh
- **Giải quyết**: R06, R16, R21; giao với BHYT-GD-R17, DUOC-R02.
- **Mô tả**: một thực thể người hành nghề với ba định danh (số định danh cá nhân, số GPHN/CCHN, mã liên thông đơn thuốc) và các **đợt đăng ký hành nghề** tại cơ sở (vị trí, phạm vi, khung giờ theo ngày trong tuần, ngày hiệu lực, trạng thái gửi cơ quan cấp phép). Mọi y lệnh và chỉ định kiểm tra người thực hiện có đợt đăng ký hiệu lực bao phủ thời điểm y lệnh.
- **Mô hình dữ liệu**: `practitioner(id, cccd unique, license_no unique, license_issued_at, license_expiry, rx_link_code unique null)`; `practice_registration(id, practitioner_id, facility_code, role, scope_codes[], weekly_slots jsonb, valid_from, valid_to, reported_at, report_ref)`; `practice_change_task(registration_id, kind[leave|add], due_at, done_at)`. Ràng buộc: không cho tạo `practice_registration` có khung giờ chồng với đợt khác của cùng người **trong cùng cơ sở** (khác cơ sở thì chỉ cảnh báo vì cơ sở không thấy dữ liệu nơi khác).
- **Đánh đổi**: chặn cứng theo lịch có thể cản cấp cứu. Cần cơ chế "vượt khung" có lý do (Luật Đ36 k3 có ngoại lệ cấp cứu).

### P6. Bộ phân loại BTN và hàng đợi báo cáo dịch tễ
- **Giải quyết**: R26–R28, R30, R31.
- **Mô tả**: luật kích hoạt theo mã ICD-10, kết quả xét nghiệm (mã chỉ số và kết quả dương tính) và cờ "nghi ngờ". Khi kích hoạt, tạo `ido_case_report` với đồng hồ 24 giờ (tử vong) hoặc theo quy tắc của Cục Phòng bệnh (cấu hình). Bảng điều khiển hội chứng theo ngày để phát hiện chùm ca (R28).
- **Mô hình dữ liệu**: `idd_catalog(disease_code, group[A|B|C], icd10_list[], lab_triggers jsonb, report_rule jsonb, valid_from, source_doc)`; `ido_case_report(id, encounter_id, disease_code, status[suspected|probable|confirmed|death], trigger_at, due_at, submitted_at, submission_id)`.
- **Đánh đổi**: quy tắc báo cáo từng bệnh chưa được công bố lại sau khi TT 54/2015 bị bãi bỏ. Phải để ở dạng cấu hình và ghi nguồn.

### P7. Module sự cố y khoa có ẩn danh và vòng đời RCA
- **Giải quyết**: R32–R35, R08.
- **Mô hình dữ liệu**: `incident(id, code, reported_at, report_type[voluntary|mandatory], reporter_ref null, reporter_vault_key null, affected_type, location, occurred_at, description, initial_action, notified_doctor, notified_family, notified_patient, recorded_in_emr, harm_level[A..I], nc_level[0..3], event_group, cause_group, serious_type[1..28] null, status, encounter_id null)`; `incident_identity_vault(key, user_id)` chỉ bộ phận quản lý chất lượng giải mã được; `incident_rca(incident_id, team, due_at = received_at + 60d, findings, recommendations)`; `incident_escalation(incident_id, phone_call_at, called_to, written_sent_at)`.
- **Ràng buộc**: `nc_level = 3` ⇒ `report_type = mandatory` và `reporter_ref not null`; `serious_type` bắt buộc khi `nc_level = 3`. Không có lệnh DELETE.
- **Đánh đổi**: ẩn danh làm khó điều tra bổ sung. Dùng vault có kiểm soát thay cho xóa danh tính hẳn.

### P8. Nguồn công khai máy đọc được (giá, giờ làm việc, người hành nghề)
- **Giải quyết**: R11, R06, R36.
- **Mô tả**: xuất các bản "hiện hành" (bảng giá có hiệu lực, giờ làm việc, danh sách người hành nghề kèm giờ làm, kết quả tự đánh giá chất lượng) ở JSON/CSV có chữ ký và ngày hiệu lực; dùng cho niêm yết tại cơ sở (màn hình, website) và đẩy lên HTTT khi có chức năng.
- **Đánh đổi**: phải đồng bộ với hệ thống thu tiền. Nguyên tắc là chỉ thu theo phiên bản giá đang công khai.

### P9. Đối soát (reconciliation) giữa các đích
- **Giải quyết**: R01, R13, R20, R23.
- **Mô tả**: job hằng ngày so số lượt ra viện trong HIS với số đã gửi thành công cho từng đích (HTTT KCB, BHXH, Sổ SKĐT), và tổng của báo cáo thống kê với dữ liệu chi tiết đã gửi. Lệch thì tạo phiếu xử lý. Kết quả đối soát là bằng chứng "đầy đủ, kịp thời".
- **Mô hình dữ liệu**: `recon_run(date, destination_code, expected, sent_ok, rejected, missing, report_file)`.
- **Đánh đổi**: cần đích trả ack có mã tham chiếu. Nếu đích không trả ack (cổng nhập tay) thì chỉ đối soát được ở mức "đã xuất".

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| BC-A01 | R01, R17 | Hỏi vendor: phần mềm xuất được dữ liệu cho HTTT quản lý KCB chưa? Kiến trúc xuất là adapter có phiên bản hay code cứng theo XML BHYT? | Tài liệu kiến trúc, danh sách đích hiện có | Bắt buộc |
| BC-A02 | R02 | Mở 10 hồ sơ ra viện ngẫu nhiên (có cả tự chi trả): đủ dân tộc, nghề nghiệp, nơi ở hiện tại, cân nặng trẻ em, ngày giường HSTC, ICD-9-CM cho PT/TT, ICD-10 theo vai? Truy vấn tỷ lệ null từng trường trong 3 tháng | Kết quả truy vấn tỷ lệ thiếu, ảnh chụp màn hình | Bắt buộc |
| BC-A03 | R03 | Truy vấn dịch vụ, thuốc của lượt tự chi trả: tỷ lệ có mã danh mục dùng chung | Kết quả truy vấn | Bắt buộc |
| BC-A04 | R04 | In tóm tắt ra viện của 1 ca nội trú: đủ 7 nhóm (a–g), có thiết bị cấy ghép, đơn thuốc ngoại trú, lịch tái khám | Bản in hoặc JSON | Bắt buộc |
| BC-A05 | R05 | Tạo ca thử "nặng xin về" và "tử vong": hệ thống phân biệt trạng thái? Phiếu nguyên nhân tử vong có chuỗi ICD-10 và khoảng thời gian? | Ảnh màn hình, mẫu phiếu | Bắt buộc |
| BC-A06 | R06 | So danh sách tài khoản có quyền chỉ định, kê đơn với danh sách đăng ký hành nghề đã gửi Sở. Thử gán y lệnh cho người ngoài khung giờ đăng ký. Kiểm tra nhân sự nghỉ việc gần nhất: đã báo trong 03 ngày làm việc chưa? | Danh sách đối chiếu, log chặn, văn bản báo Sở | Bắt buộc |
| BC-A07 | R06, R16 | Bảng người hành nghề có đủ số định danh, số GPHN, mã liên thông đơn thuốc, không trùng? | Truy vấn trùng hoặc null | Bắt buộc |
| BC-A08 | R07 | Danh mục giường phân loại HSTC, áp lực âm; module TBYT có hiện trạng; báo cáo nhập-xuất-tồn 6 tháng chạy được | Báo cáo mẫu | Bắt buộc |
| BC-A09 | R09, R10 | Chạy báo cáo 6 tháng: ngày điều trị trung bình khớp Biểu 9/BCT cùng kỳ? Có DVKT nào được chỉ định nhưng không có trong danh mục được phê duyệt? | Hai báo cáo, truy vấn ngoại lệ | Bắt buộc |
| BC-A10 | R11 | So bảng giá trong hệ thống với bảng niêm yết tại quầy và website; tìm hóa đơn có dịch vụ ngoài bảng giá đang hiệu lực | Ảnh niêm yết, truy vấn ngoại lệ | Bắt buộc |
| BC-A11 | R12 | Hỏi khả năng hạch toán chi phí theo ca bệnh: có mã nhân viên, mã thiết bị, mã tòa nhà ổn định không? | Tài liệu, mẫu dữ liệu | Nên |
| BC-A12 | R13 | Sửa một hồ sơ đã gửi đi: hệ thống có tạo phiên bản mới và đưa vào hàng đợi gửi lại cho mọi đích không? | Log submission trước và sau | Bắt buộc |
| BC-A13 | R14 | Đo thời gian xuất danh sách ca theo một nhóm ICD-10 trong 30 ngày qua | Thời gian chạy, file kết quả | Bắt buộc |
| BC-A14 | R15 | Hồ sơ cấp cứu chấn thương có mã nguyên nhân ngoài V01–Y98 không? Tỷ lệ thiếu | Truy vấn | Bắt buộc |
| BC-A15 | R18 | Kiểm tra cấu hình kết nối ra ngoài: TLS, nơi lưu khóa API, log có chứa dữ liệu sức khỏe dạng rõ không | Cấu hình, mẫu log | Bắt buộc |
| BC-A16 | R19 | Cơ sở xin GPHĐ mới từ 2027 hoặc cơ sở cũ trước 01/01/2029: có bằng chứng kết nối HTTT không? | Hồ sơ GPHĐ, nhật ký gửi | Bắt buộc |
| BC-A17 | R20 | Liệt kê các đích quốc gia mà cơ sở đang gửi dữ liệu và tần suất (BHXH, đơn thuốc QG, Sổ SKĐT, KSK, giám sát BTN, QL hành nghề) | Bảng đích + bằng chứng gửi gần nhất | Bắt buộc |
| BC-A18 | R21 | Thông tin GPHN, số đăng ký thuốc có ghi nguồn và ngày đồng bộ không? | Ảnh màn hình, schema | Nên |
| BC-A19 | R22 | In Sổ khám bệnh A1/CSYT (PK) hoặc sổ A3, A4 (sản) từ hệ thống | Bản in | Bắt buộc |
| BC-A20 | R23, R24 | Chạy Biểu 9, 11, 14/BCT tháng gần nhất; so với bản đã nộp; kiểm tra bảng ánh xạ ICD-10 → dòng biểu; xem ngày nộp so với hạn 05 ngày làm việc | Báo cáo, snapshot đã nộp, biên nhận | Bắt buộc |
| BC-A21 | R25 | Định nghĩa biểu có ngày hiệu lực không? Vendor có kế hoạch cho chế độ mới từ 01/03/2027? | Cấu hình, roadmap | Bắt buộc |
| BC-A22 | R26, R27 | Tạo ca thử chẩn đoán BTN và ca tử vong do BTN: hệ thống có tạo phiếu báo cáo, đồng hồ 24 giờ, cảnh báo? Đối chiếu 3 tháng: ca BTN trong HIS và ca đã nhập HTQLGS/eCDS | Log, bảng đối chiếu | Bắt buộc |
| BC-A23 | R26 | Có ghi nhận các lần báo cáo bằng giấy khi hệ thống giám sát lỗi và đã nhập bù chưa? | Sổ dự phòng, trạng thái nhập bù | Bắt buộc |
| BC-A24 | R28 | Có báo cáo theo dõi hội chứng theo ngày hoặc cảnh báo chùm ca không? | Ảnh màn hình | Nên |
| BC-A25 | R29 | Báo cáo BKLN, RLTT kỳ tháng gửi CDC tỉnh trong 05 ngày làm việc? Báo cáo thương tích 6 tháng? | Biên nhận gửi | Bắt buộc |
| BC-A26 | R30 | Danh mục BTN trong hệ thống đã cập nhật nhóm A/B/C theo QĐ 1965/2026 chưa (ví dụ COVID-19 thuộc nhóm B)? | Bảng danh mục, ngày cập nhật | Bắt buộc |
| BC-A27 | R31 | Ai xem được hàng đợi báo cáo BTN? Báo cáo tổng hợp có lộ định danh? | Ma trận phân quyền | Bắt buộc |
| BC-A28 | R32 | Có form báo sự cố điện tử đủ trường PL III TT 43? Người ngoài HIS báo được không? Thử xóa một báo cáo | Ảnh form, kết quả thử xóa | Bắt buộc |
| BC-A29 | R33 | Lấy các sự cố NC3 trong năm: thời điểm phát hiện, thời điểm gọi báo trước (≤ 01 giờ với sự cố nghiêm trọng), thời điểm báo cơ quan quản lý | Bảng thời gian, văn bản đã gửi | Bắt buộc |
| BC-A30 | R34 | Mỗi sự cố có đủ 3 trục phân loại? RCA hoàn thành trong 60 ngày? Có báo cáo tuần và báo cáo 6 tháng gửi cơ quan quản lý? | Truy vấn, báo cáo đã gửi | Bắt buộc |
| BC-A31 | R35 | Báo cáo tự nguyện có ẩn danh được không? Ai giải mã danh tính được? Có log truy cập module sự cố? | Cấu hình quyền, log | Bắt buộc |
| BC-A32 | R36 | BV: có kết quả tự đánh giá TT 35 quý I và đã công khai? Cơ sở ngoài BV: đã chuẩn bị theo dự thảo? | Biên bản tự đánh giá, link công khai | Bắt buộc (BV) / Nên (khác) |
| BC-A33 | R37 | Có bảng đối chiếu chức năng với TT 54/2017 và mức tự xác định gần nhất? | Bảng đối chiếu | Nên |
| BC-A34 | P1, P9 | Có bảng outbox, submission, đối soát định kỳ? Có tỷ lệ gửi lỗi và tồn đọng theo từng đích? | Schema, dashboard | Nên |

---

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái | Nội dung | Ai phải làm | Nguồn |
|---|---|---|---|---|
| 01/03/2019 | [QUA] | TT 43/2018 (sự cố y khoa) có HL | Mọi cơ sở KCB | TT 43 Đ15 |
| 01/01/2024 | [QUA] | Luật KCB 2023 có HL (đăng ký hành nghề, công khai, niêm yết trên HTTT) | Mọi cơ sở KCB | Đ120 k1 |
| 01/01/2025 | [QUA] | Tiêu chuẩn chất lượng cơ bản cho BV (TT 35/2024) | Bệnh viện | Đ120 k6 a; TT 35 Đ3 |
| 01/07/2025 | [QUA] | NĐ 102/2025 (CSDLQG y tế, nghĩa vụ kết nối của cơ sở y tế) và TT 23/2025 (thống kê) có HL | Mọi cơ sở | NĐ 102 Đ25; TT 23 Đ7 k1 |
| 19/08/2025 | [QUA] | NĐ 194/2025 có HL; NĐ 47/2024 bị bãi bỏ | CQNN | NĐ 194 Đ40 |
| 22/10/2025 | [QUA] | NĐ 278/2025 có HL | CQNN | — |
| 11–12/2025 | [QUA] | KH 1642: cơ sở KCB đăng ký tài khoản, cập nhật dữ liệu trên Hệ thống QL hành nghề (Sở tập huấn trước 30/11/2025) | Mọi cơ sở KCB | KH 1642 (thứ cấp-chính thức) |
| Quý I/2026 | [QUA] | BV tự đánh giá TT 35 cho năm 2025 | BV | TT 35 Đ1 k3 b |
| 15/05/2026 | [QUA] | NĐ 90/2026 xử phạt có HL | Mọi cơ sở | NĐ 90 |
| 19/05/2026 | [QUA] | QĐ 11/2026/QĐ-TTg (danh mục CSDLQG, mục XVIII y tế) có HL | BYT | QĐ 11 Đ3 |
| 02/06/2026 | [QUA] | CV 4016: cập nhật 100% dữ liệu người hành nghề, cơ sở | Mọi cơ sở KCB | thứ cấp |
| 01/07/2026 | [QUA] | Luật Phòng bệnh, NĐ 165/2026, TT 15/2026 có HL; TT 54/2015, TT 17/2019 hết HL; danh mục BTN mới (QĐ 1965) | Cơ sở KCB, cơ sở XN | TT 15 Đ65 |
| 07/2026 | [QUA] | Ban hành danh mục nội hàm thông tin CSDL KCB và hành nghề (QĐ 2114 mục II.1); có thể là QĐ 2682 ngày 22/08/2026 (chưa XM) | BYT | QĐ 2114 |
| 10/2026 | [TỚI] | Dự kiến xong dự thảo TT thay TT 23 | BYT | thứ cấp |
| 30/11/2026 | [TỚI] | Xử lý dứt điểm nhiệm vụ CĐS quá hạn (CT 07) | Đơn vị thuộc BYT | thứ cấp |
| **01/01/2027** | [TỚI] | **TT 38/2024 có HL**; HTTT quản lý KCB phải vận hành (Luật Đ120 k8); **điều kiện hạ tầng CNTT kết nối HTTT cho hồ sơ GPHĐ mới** (Đ120 k5 a); **tiêu chuẩn chất lượng cơ bản cho cơ sở không phải BV** (Đ120 k6 b) nếu TT kịp ban hành; BV tư do Sở Y tế cấp phép (Đ120 k9) | Mọi cơ sở KCB; cơ sở xin GPHĐ mới | Luật KCB, TT 38 Đ13 |
| 2027–2028 | [TỚI] | GĐ 2 HTTT quản lý KCB: CSDL tập trung, kết nối với HTTT của cơ sở KCB, chức năng thống kê, báo cáo | TTYQG, Cục QLKCB; cơ sở KCB kết nối | QĐ 2114 mục II.3.2.2 |
| **01/03/2027** | [TỚI] | **TT 23/2025 hết HL**; chế độ báo cáo thống kê mới (nếu đã ban hành) | Mọi cơ sở | TT 23 Đ7 k2 |
| Quý I/2028 | [TỚI] | Lần tự đánh giá đầu tiên của cơ sở ngoài BV cho năm 2027 (suy luận theo cơ chế TT 35 và dự thảo) | PK, TYT… | suy luận |
| **01/01/2029** | [TỚI] | Cơ sở có GPHĐ trước 2027 phải đáp ứng điều kiện hạ tầng CNTT kết nối HTTT | Mọi cơ sở cũ | Đ120 k5 b |
| 01/01/2030 | [TỚI] | Báo cáo BKLN, RLTT, dinh dưỡng, thương tích phải thực hiện trên HTTT giám sát phòng bệnh | Cơ sở KCB, TYT | TT 15 Đ66 k1 |
| Thường xuyên | — | Ca nghi BTN: báo TYT xã trong 24 giờ; tử vong do BTN: 24 giờ; sự cố nghiêm trọng: gọi trong 01 giờ; NC3: báo ngay; tổng hợp sự cố 6 tháng; báo cáo thống kê tháng: 05 ngày làm việc; BKLN, RLTT: 05 ngày làm việc; nhân sự nghỉ: 03 ngày làm việc; bổ sung nhân sự: 10 ngày; TT 38 Đ10 k5: kỳ 6 và 12 tháng | Mọi cơ sở KCB | TT 15, TT 43, TT 23, NĐ 96, TT 38 |

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

### Chuỗi thay thế (đã xác minh trong lượt này)
- **TT 54/2015/TT-BYT** (báo cáo, khai báo BTN) và **TT 17/2019/TT-BYT** (giám sát, đáp ứng BTN) → **bãi bỏ** bởi **TT 15/2026/TT-BYT** Đ65 k2 a, b, từ 01/07/2026. Cùng bị bãi bỏ: TTLT 16/2013/TTLT-BYT-BNN&PTNT, QĐ 25/2006/QĐ-BYT (biểu mẫu tai nạn thương tích). **Giải quyết MT-31.**
- **Luật PCBTN 03/2007** → **Luật Phòng bệnh 114/2025/QH15** (Đ45 k2), từ 01/07/2026.
- **NĐ 47/2024/NĐ-CP** (danh mục CSDLQG) → **bãi bỏ** bởi **NĐ 194/2025** Đ40 k2 a, từ 19/08/2025; danh mục CSDLQG nay là **QĐ 11/2026/QĐ-TTg**. **Giải quyết** "chưa rõ quan hệ ND-47-2024 ↔ QD-11-2026-TTg" trong inventory.
- **NĐ 47/2020** → còn HL một phần; NĐ 194 Đ40 k2 b bãi bỏ k4 Đ3, k2 Đ12, Đ17–21, điểm a, b k1 Đ53; Đ40 k3 sửa k3 Đ35 (tạo tài khoản kết nối trong 02 ngày làm việc).
- **TT 32/2014/TT-BYT** → **TT 23/2025** (01/07/2025) → **văn bản mới chưa ban hành** (TT 23 tự hết HL 01/03/2027).
- **TT 54/2017** → bãi bỏ một phần bởi TT 13/2025 (xem EMR); phần còn lại chờ DT-TT54.
- **TT 43/2018** → chưa bị thay; vẫn là văn bản hướng dẫn báo cáo sự cố duy nhất tìm được. Luật KCB 2023 Đ71 không giao Bộ trưởng quy định chi tiết (suy luận từ câu chữ Đ71), nên chưa chắc sẽ có TT thay.

### Bẫy trích dẫn
1. **"Đ120 k6 b là điều kiện CNTT"** — sai. Điều kiện hạ tầng CNTT kết nối HTTT là **Đ120 k5 a, b** (dẫn Đ52 k2 d). **K6 b** là tiêu chuẩn chất lượng cơ bản cho cơ sở không phải BV từ 01/01/2027.
2. **Số hiệu TT 38/2024 trong lớp text PDF datafiles bị đọc nhầm thành "39/2024/TT-BVT"**. Công cụ trích tự động sẽ ghi sai. Số đúng là 38/2024/TT-BYT (trang VB 211878 và OCR lại trang 1).
3. **TT 38 không có "thời hạn gửi"** theo lượt KCB. Đừng gán cho TT 38 các mốc "24 giờ" hoặc "ngay sau lượt KCB". Các mốc đó thuộc BHYT (NĐ 188, TT 48, xem BHYT-GD-R19), đơn thuốc (DUOC-R12) hoặc KSK (QĐ 1551). TT 38 chỉ có "ngay" khi sửa sai (Đ4 k2), "ngay khi có yêu cầu" với dịch nhóm A (Đ5 k4), và kỳ 6/12 tháng (Đ10 k2 d, k5).
4. **TT 38 vẫn dẫn NĐ 13/2023 và NĐ 47/2020**. NĐ 13 đã được thay bởi Luật 91/2025 và NĐ 356/2025 (DLCN); NĐ 47/2020 bị NĐ 194 bãi bỏ một phần. TT 38 Đ14 cho phép áp văn bản thay thế.
5. **TT 38 Đ15** đánh số khoản "1, 2, 3, 4, 3": khoản cuối (cơ sở KCB cung cấp dữ liệu) thực chất là khoản 5. Trích dẫn nên ghi "Đ15 (khoản cuối)".
6. **TT 23 Đ5** không có khoản 3 (nhảy từ k2 sang k4). Thân TT ghi "05 ngày làm việc", PL IV ghi "05 ngày".
7. **QĐ 11/2026/QĐ-TTg**: CSDLQG về y tế ở **mục XVIII**, không phải XVII. OCR trang 1 đọc năm ký thành "2020"; đúng là 28/03/2026.
8. **eCDS / HTQLGS** được xây theo TT 54/2015 (đã hết HL). Tài liệu hướng dẫn cũ về "báo cáo trong 24 giờ hoặc 48 giờ tùy bệnh" dẫn TT 54/2015, **không còn là căn cứ** sau 01/07/2026. Căn cứ nay là TT 15/2026 + hướng dẫn chuyên môn Cục Phòng bệnh (TT 15 Đ66 k2 cho phép dùng tiếp hướng dẫn chuyên môn cũ của BYT đến khi có hướng dẫn thay).
9. **NĐ 165**: có hai văn bản cùng số. **NĐ 165/2025/NĐ-CP** hướng dẫn Luật Dữ liệu; **NĐ 165/2026/NĐ-CP** hướng dẫn Luật Phòng bệnh. File `dl/nd165.ocr.txt` của lượt trước là bản 2025.
10. **"Hệ thống thông tin về quản lý hoạt động KCB" (TT 38) ≠ "Hệ thống Quản lý Quốc gia về hành nghề và hoạt động KCB" (KH 1642)**. Theo QĐ 2114, hệ thống thứ hai được nâng cấp thành "phiên bản đầu tiên" của hệ thống thứ nhất trong 2026, nhưng về pháp lý đây vẫn là hai tên gọi khác nhau.
11. **TT 35/2024** chỉ áp cho **bệnh viện** (Đ1 k2). Đừng trích TT 35 làm căn cứ cho phòng khám.
12. **TT 43/2018**: mức "báo cáo bắt buộc" gồm mục 7–9 PL I (NC3: G, H, I). Có nguồn ghi sai là "từ NC2". NC2 (E, F) vẫn thuộc báo cáo **tự nguyện**, dù phải báo người đứng đầu ngay (Đ8 k1 a).

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Hướng dẫn kỹ thuật kết nối HTTT quản lý KCB** (QĐ 2114 mục IV.2 b): chưa ban hành. Cần hỏi TTYQG: định dạng (có dùng lại XML QĐ 130 không), phương thức (API, file), tần suất (theo lượt hay theo kỳ), và cơ sở tư nhỏ có được nhập tay qua cổng không.
2. **Từ 01/01/2027 đến khi HTTT GĐ 2 vận hành (2027–2028)**, cơ sở thực hiện nghĩa vụ TT 38 bằng cách nào? Có bị coi là vi phạm nếu chưa gửi được? Cần hỏi Cục QLKCB.
3. **"Hạ tầng CNTT bảo đảm kết nối"** (Luật Đ52 k2 d) gồm tiêu chí nào để thẩm định hồ sơ GPHĐ từ 01/01/2027? Chưa có hướng dẫn. Thẩm định viên Sở Y tế sẽ đòi bằng chứng gì? Cần hỏi Sở Y tế. Việc áp NĐ 90 Đ39 cho cơ sở cũ trước 01/01/2029 cần ý kiến luật sư.
4. **QĐ 2682/QĐ-BYT (22/08/2026)** "Danh mục thông tin cơ bản của CSDL về hoạt động KCB": chưa đọc được bản gốc (TVPL trả 403). Đây có thể là đặc tả trường dữ liệu quan trọng nhất cho R02–R12.
5. **Thời hạn báo cáo từng ca BTN theo nhóm** sau khi TT 54/2015 hết HL: phụ thuộc "hướng dẫn chuyên môn của Cục Phòng bệnh" (TT 15 Đ4 k3). Chưa tìm thấy văn bản của Cục sau 01/07/2026. Cần hỏi Cục Phòng bệnh hoặc CDC tỉnh. Cũng chưa xác minh eCDS/HTQLGS có phải là "HTTT giám sát trong phòng bệnh" theo TT 15 hay không.
6. **QĐ 1965/QĐ-BYT 2026** (danh mục BTN): mới có nguồn thứ cấp. Cần bản gốc để lập bảng ánh xạ ICD-10.
7. **Văn bản thay TT 23/2025**: chưa ban hành. Rủi ro khoảng trống từ 01/03/2027; báo cáo kỳ tháng 02/2027 (hạn rơi sau 01/03/2027) theo mẫu nào? Cần hỏi Vụ KH-TC.
8. **TT 43/2018 còn HL** chỉ dựa vào luatvietnam (thứ cấp) và việc không tìm thấy văn bản thay. Có văn bản hướng dẫn Luật KCB Đ71 nào trong 2024–2026 (ví dụ trong TT 32/2023 hoặc văn bản riêng) không? Lượt này grep TT 32/2023 không thấy "sự cố y khoa".
9. **Tiêu chuẩn chất lượng cơ bản cho cơ sở ngoài BV**: dự thảo chưa có toàn văn, chưa rõ tiêu chí CNTT cụ thể. Nếu không kịp ban hành trước 01/01/2027 thì Đ120 k6 b áp dụng thế nào?
10. **TT 54/2017**: chưa đọc bản gốc lượt này. Có nghĩa vụ tự đánh giá và báo cáo mức ứng dụng CNTT định kỳ không? DT-TT54 (dự kiến Q2/2026) chưa thấy.
11. **CT 07/CT-BYT**: chưa có bản gốc. Ngày ký chính xác (báo chí đưa tin 15/09/2026) và nội dung "di chuyển hệ thống về TTDL quốc gia" có áp cho bệnh viện trực thuộc Bộ hay không.
12. **NĐ 96/2023**: chưa kiểm tra các văn bản sửa đổi (NĐ, NQ 21/2026/NQ-CP về cắt giảm TTHC lĩnh vực y tế). Thời hạn 03 ngày làm việc và 10 ngày có thể đã thay đổi.
13. **Chế tài thống kê**: nghị định xử phạt VPHC lĩnh vực thống kê hiện hành và mức phạt nộp báo cáo muộn chưa đọc.
14. **TT 38 Đ10 k5 b và k8** (thu chi, trích lập quỹ, hạch toán theo ca, chi nhân công theo mã nhân viên) có áp cho cơ sở tư nhân không, và phạm vi dữ liệu thu nhập cá nhân của nhân viên có cần căn cứ xử lý DLCN riêng không: cần ý kiến luật sư (giao DLCN).
15. **Cổng tiếp nhận dữ liệu y tế của BYT** (TT 48 Đ7, NĐ 188 Đ71): quan hệ với HTTT quản lý KCB và CSDLQG chưa rõ (trùng câu hỏi mở số 5 của BHYT-GD).
