# CLS — CLS liên thông, LIS, RIS/PACS và phần mềm là thiết bị y tế

> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: nghĩa vụ liên thông và sử dụng lại kết quả cận lâm sàng (CLS) giữa các cơ sở KCB BHYT từ 01/01/2027 (luật, văn bản giao thẩm quyền, hai bản dự thảo thông tư danh mục); mã chỉ số CLS dùng chung (QĐ 1227/2025); quản lý chất lượng xét nghiệm (TT 01/2013 sửa bởi TT 25/2026, tiêu chí mức chất lượng PXN QĐ 2429/2017) và hệ quả với LIS; phiếu trả kết quả, ký duyệt, sửa kết quả, thời gian trả kết quả; RIS/PACS: thời hạn lưu kết quả và ảnh, DICOM, trả kết quả hình ảnh không in phim và giá BHYT; an toàn bức xạ có ràng buộc RIS; **phần mềm là thiết bị y tế (SaMD)** theo NĐ 98/2021 (VBHN đến NĐ 04/2025), TT 05/2022 (sửa bởi TT 24/2026), chế tài NĐ 90/2026. Giao sang cụm khác: gửi XML4 và mã DVKT (BHYT-DATA), chuyển mẫu/người bệnh làm DVCLS theo NĐ 188 Đ44 (BHYT-GD-R13), ký số và lưu trữ HSBA (EMR), bảo mật dữ liệu HIV và dữ liệu nhạy cảm (DLCN), sao lưu và cấp độ HTTT (ANM), AI rủi ro cao (K10), chuẩn HL7/FHIR/DICOM trong khung kiến trúc QĐ 2146 (K6, MT-24).
>
> **Cách đọc nguồn trong lượt này.** PDF scan được OCR bằng Apple Vision (`vi-VT`), nên giữ được dấu; "gốc-OCR" nghĩa là câu chữ có thể sai từng ký tự. Bảng tiêu chí TT 54/2017 được đối chiếu thêm bằng ảnh trang. Nội dung web chỉ được coi là dữ liệu. Không dùng hethongphapluat làm nguồn.
>
> Đây là tài liệu nghiên cứu, **không phải ý kiến pháp lý**. Chỗ nào là suy luận của người viết đều ghi "(suy luận)".

---

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| L-BHYT-SD-2024 | 51/2024/QH15 (27/11/2024) | Luật sửa đổi Luật BHYT: **Đ3 k4** (mốc liên thông CLS), Đ1 k3 b (sửa Đ6 k3: BYT ban hành quy định liên thông CLS) | 01/07/2025; Đ3 k4: "chậm nhất" 01/01/2027 | Còn HL | Cơ sở KCB BHYT (BV công, BV tư, PK có HĐ BHYT) | **gốc** (Công báo, có lớp text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat51.pdf) |
| ND-313-2026 (**mới**) | 313/2026/NĐ-CP (08/08/2026) | Chức năng, nhiệm vụ, quyền hạn, cơ cấu tổ chức của Bộ Y tế: **Đ2 k14 c** (BYT ban hành quy định liên thông và sử dụng kết quả CLS; cấp mã danh mục dùng chung, chuẩn định dạng dữ liệu); Đ2 k12 (thiết bị y tế) | 18/08/2026 (Đ4 k1) | Còn HL; **thay NĐ 42/2025/NĐ-CP** (Đ4 k2) | BYT (văn bản giao thẩm quyền) | **gốc** (PDF ký số, có lớp text) | [PDF, Cục Dân số đăng lại](https://vnpa.moh.gov.vn/wp-content/uploads/2026/08/NGHI-DINH-313_2026_ND-CP_08082026_1-signed.pdf) |
| DT-CLS-LT | Dự thảo TT "danh mục xét nghiệm, dịch vụ CLS và điều kiện sử dụng kết quả CLS liên thông giữa các cơ sở KCB BHYT" | Hai phiên bản: **11/2025** (~1.114 kỹ thuật, 6 phụ lục) và **08/2026** (441 kỹ thuật) | Báo nêu dự kiến 01/07/2026 (đã lỡ); Thứ trưởng nói dự kiến ban hành **tháng 10/2026** (báo 18/09/2026) | **Dự thảo**, chưa thấy ban hành đến 05/10/2026 | Cơ sở KCB BHYT có CLS | **thứ cấp** (chỉ qua báo; chưa tìm được toàn văn dự thảo) | [baochinhphu 18/11/2025](https://baochinhphu.vn/nguyen-tac-su-dung-ket-qua-xet-nghiem-khi-lien-thong-ket-qua-giua-cac-co-so-kham-chua-benh-10225111816281683.htm) · [baodauthau 29/11/2025](https://baodauthau.vn/xay-danh-muc-xet-nghiem-dich-vu-can-lam-sang-lien-thong-bao-hiem-y-te-post189720.html) · [vietnamnet 2025](https://vietnamnet.vn/bo-y-te-de-xuat-lien-thong-hon-1-000-ket-qua-xet-nghiem-chieu-chup-2464690.html) · [dantri 24/08/2026](https://dantri.com.vn/suc-khoe/de-xuat-hon-400-xet-nghiem-chup-chieu-co-the-duoc-dung-lai-khi-chuyen-vien-20260824223459660.htm) · [vietnamplus 2026](https://www.vietnamplus.vn/bo-y-te-de-xuat-441-xet-nghiem-dien-quang-co-the-dung-lai-khi-chuyen-vien-post1132284.vnp) · [suckhoedoisong 25/08/2026](https://suckhoedoisong.vn/bo-y-te-de-xuat-441-xet-nghiem-dien-quang-co-the-dung-lai-khi-chuyen-vien-169260825004553706.htm) · [vietnamnet 2026](https://vietnamnet.vn/bo-y-te-de-xuat-lien-thong-du-lieu-441-xet-nghiem-chup-x-quang-ct-mri-2548513.html) · [thanhnien 18/09/2026](https://thanhnien.vn/lien-thong-xet-nghiem-kiem-soat-chi-dinh-trung-lap-185260918124008537.htm) |
| QD-1227-2025-BYT | 1227/QĐ-BYT (11/04/2025) | Danh mục mã dùng chung đối với kỹ thuật, thuật ngữ chỉ số CLS (Đợt 1): 2.964 chỉ số (HH-TM 1.022; hóa sinh 447; vi sinh 174; GPB 81; điện quang 1.240) | Từ ngày ký (Đ4) | Còn HL; chưa thấy "Đợt 2" cho chỉ số CLS | **Mọi** cơ sở KCB công và tư (Đ2) | **thứ cấp** (thân QĐ đọc qua bản đăng lại; phụ lục chưa đọc) | [clbv.vn, thứ cấp](https://clbv.vn/van-ban/1227qd-byt) · [vietnamplus, thứ cấp](https://www.vietnamplus.vn/bo-y-te-ban-hanh-danh-muc-chi-so-can-lam-sang-phuc-vu-benh-an-dien-tu-post1027210.vnp) |
| TT-01-2013-BYT | 01/2013/TT-BYT (11/01/2013) | Hướng dẫn thực hiện quản lý chất lượng xét nghiệm tại cơ sở KCB (Đ2–Đ10, Phụ lục bộ chỉ số chất lượng) | 15/03/2013 | Còn HL; **Đ5 k5 sửa bởi TT 25/2026 Đ1** | Cơ sở KCB **có phòng xét nghiệm** | **gốc** (Công báo số 69+70/2013, có lớp text) | [Công báo](https://congbao.chinhphu.vn/van-ban/thong-tu-so-01-2013-tt-byt-1583.htm) |
| TT-25-2026-BYT | 25/2026/TT-BYT (30/06/2026) | Đ1: sửa TT 01/2013 Đ5 k5 (ngoại kiểm thành "khuyến khích"); Đ2: sửa TT 32/2023; Đ3: sửa TT 23/2024 | 15/08/2026; **Đ2, Đ3 từ 01/07/2026** (Đ6) | Còn HL | Như trên | **gốc** (PDF ký số) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/25-byt.signed.pdf) |
| QD-2429-2017-BYT (**mới với inventory**) | 2429/QĐ-BYT (12/06/2017) | Tiêu chí đánh giá mức chất lượng phòng xét nghiệm y học: 12 chương, 169 tiêu chí, 6 bậc (chưa xếp mức, mức 1–5) | Từ khi ký | Không phải VBQPPL. Cục KCB vẫn đăng kèm sổ tay hướng dẫn (2021); chưa thấy văn bản thay thế. Là "thước đo mức chất lượng" mà DT-CLS-LT dùng làm điều kiện công nhận kết quả (suy luận từ báo) | PXN của cơ sở KCB tự đánh giá; cơ quan quản lý đánh giá, công bố | **gốc** (PDF trên kcb.vn, có lớp text) | [PDF, kcb.vn](https://kcb.vn/upload/2005611/20210723/3d486c540e73ba776981b50506ad7526Tieu-chi-danh-gia-muc-chat-luong-phong-xet-nghiem_final.pdf) |
| L-KCB-2023 | 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Đ2 k17 (HSBA gồm "kết quả cận lâm sàng"), Đ69, Đ77 k4 (chuyển cơ sở phải hoàn chỉnh HSBA), **Đ113** (TBYT phải được phép lưu hành; hồ sơ theo dõi TBYT) | 01/01/2024 | Còn HL | Tất cả cơ sở KCB | **gốc** | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| TT-32-2023-BYT | 32/2023/TT-BYT | Đ51 (82 mẫu HSBA, PL XXVIII–XXIX), **Đ52 k2** (ghi chép: thời gian, người ghi; cấm viết tắt trong tài liệu bàn giao cho cơ sở khác) | 01/01/2024 | Còn HL (TT 25/2026 không sửa Chương X) | Tất cả cơ sở KCB | **gốc** | [PDF ký số, BV Bệnh Nhiệt đới](https://bvbnd.vn/wp-content/uploads/2024/01/32-thongtuhuongdanluatkbcb31122023_91202410.pdf) |
| TT-33-2025-BYT | 33/2025/TT-BYT (01/07/2025) | Thời hạn lưu trữ hồ sơ ngành y tế: HSBA nội/ngoại trú 10 năm (dòng 44), tâm thần/TNLĐ/TNGT 20 năm (40), tử vong 30 năm (39); Đ1 k2 b nhóm tương đương | 01/07/2025 | Còn HL; thay TT 53/2017 | Tất cả; áp cho cả tài liệu điện tử (Đ1 k2 a) | **gốc** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [PDF phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| TT-54-2017-BYT | 54/2017/TT-BYT (29/12/2017) | Bộ tiêu chí ứng dụng CNTT tại cơ sở KCB: nhóm IV RIS-PACS (tiêu chí 62–79), nhóm V LIS (80–89), PL II (mức 1–7) | 26/02/2018 | Còn HL một phần (Mục VIII PL I và tiêu chí EMR hết HL từ 06/06/2025 theo TT 13/2025). Chưa có thông tư thay thế (DT-TT54) | Cơ sở KCB có GPHĐ (Đ1 k2). Là **khung tự đánh giá mức**, không bắt đạt mức nào | **gốc-OCR** (bản gốc từ CSDL quốc gia về pháp luật; bảng đối chiếu ảnh trang) | [vbpl.vn](https://vbpl.vn/van-ban/chi-tiet/thong-tu-54-2017-tt-byt--128249) · [PDF bản gốc](https://vbpl-bientap-gateway.moj.gov.vn/api/qtdc/public/doc/minio/buckets/vbpl/128249/VanBanGoc_tt-2017-54-1.pdf/download) |
| QD-4868-2015-BYT + CV-5319-2020-BYT | 4868/QĐ-BYT (16/11/2015); 5319/BYT-KH-TC (05/10/2020) | Đề án thí điểm DVKT CĐHA trên PACS (không in phim), hạn thí điểm đến 30/12/2019; CV 5319: cơ sở thí điểm được thanh toán **bằng giá dịch vụ có in phim** | — | Hết thời gian thí điểm; CV 5319 là hướng dẫn chuyển tiếp | 17 BV thí điểm, 3 BV đã thẩm định, BV làm EMR theo TT 46/2018 trước 30/05/2020 | **thứ cấp** (caselaw) | [CV 5319, caselaw](https://caselaw.vn/van-ban-phap-luat/357365-cong-van-so-5319-byt-kh-tc-ngay-05-10-2020-cua-bo-y-te-ve-thuc-hien-thanh-toan-chi-phi-dich-vu-ky-thuat-thuc-hien-bang-he-thong-luu-tru-va-truyen-hinh-anh-pacs) |
| QD-313-2026-BYT + CV đôn đốc giá PACS (**mới**) | 313/QĐ-BYT (29/01/2026); CV đôn đốc do Thứ trưởng Vũ Mạnh Hà ký (báo 03/08/2026; một kết quả tìm kiếm ghi **5586/BYT-BH ngày 28/07/2026**, chưa xác minh) | QĐ 313: giá DVKT CĐHA **sử dụng PACS** (không in phim) tại BV Bạch Mai, 734 dịch vụ, giảm bình quân 5,9%. CV: đề nghị mọi cơ sở xây phương án giá dịch vụ CĐHA dùng PACS theo TT 21/2024/TT-BYT, trình phê duyệt | QĐ 313: từ khi ký | Còn HL | QĐ 313: BV Bạch Mai; CV: mọi cơ sở KCB, Sở Y tế | **thứ cấp** | [suckhoedoisong 03/08/2026](https://suckhoedoisong.vn/bo-y-te-don-doc-khan-truong-phe-duyet-gia-dich-vu-chan-doan-hinh-anh-su-dung-pacs-16926080313455106.htm) · [nhandan](https://nhandan.vn/dua-dich-vu-ky-thuat-chan-doan-hinh-anh-khong-in-phim-vao-chi-tra-bao-hiem-y-te-post942349.html) · [tuoitre 04/02/2026](https://tuoitre.vn/chan-doan-hinh-anh-khong-in-phim-co-the-tiet-kiem-1-500-ti-dong-moi-nam-20260204170824964.htm) |
| TT-59-2025-BKHCN (**mới**) | 59/2025/TT-BKHCN (31/12/2025) | Bảo đảm an toàn bức xạ và ứng phó sự cố: **Đ32** kiểm soát chiếu xạ y tế (tham khảo các lần khám trước; mức liều tham chiếu chẩn đoán ở PL 2 Mục 2) | 01/01/2026 (Đ113 k1) | Còn HL; **thay TTLT 13/2014/TTLT-BKHCN-BYT và TT 13/2018/TT-BKHCN** (Đ113 k2) | Cơ sở có công việc bức xạ trong y tế | **gốc-OCR** (bản sao y của Bộ KH&CN) | [Trang văn bản, mst.gov.vn](https://mst.gov.vn/van-ban-phap-luat/25309.htm) · [PDF](https://mic.mediacdn.vn/document/2026/1/17/59tt-17686411227721232332528.pdf) |
| ND-98-2021 (VBHN) | 98/2021/NĐ-CP, sửa bởi NĐ 07/2023, NĐ 96/2023 (đổi "trang thiết bị y tế" thành "thiết bị y tế"), NĐ 85/2024, NĐ 04/2025 | Quản lý thiết bị y tế: **Đ2 k1** (TBYT gồm "phần mềm (software)"), **Đ3 k8 a** (miễn phân loại/số lưu hành cho "phần mềm sử dụng cho thiết bị y tế"), Đ4–Đ5 (phân loại A–D), Đ8 (ISO 13485), Đ21–Đ23 (số lưu hành, điều kiện lưu hành), Đ63–Đ65 (sử dụng tại cơ sở), Đ76 k5 (CSDT bắt buộc từ 01/01/2024) | 01/01/2022 | Còn HL. **NĐ 04/2025 chỉ sửa Đ76** (chuyển tiếp giấy phép nhập khẩu, số đăng ký IVD). Chưa có Luật TBYT (đang ở giai đoạn đề xuất xây dựng, theo [tờ trình dự thảo Đề án chuỗi cung ứng TBYT, 15/06/2026](https://imda.moh.gov.vn/documents/10182/10030600/Duthaototrinh.15.06.2026/db844d21-f1d8-493e-914e-130b24ab9812)) | Chủ sở hữu, cơ sở sản xuất, nhập khẩu, mua bán TBYT; cơ sở y tế sử dụng | **gốc-OCR** (bản gốc 2021 và VBHN sao y của BYT ngày 26/03/2025) | [PDF gốc 2021](https://datafiles.chinhphu.vn/cpp/files/vbpq/2021/11/98.signed.pdf) · [VBHN, Cục HT&TBYT](https://imda.moh.gov.vn/documents/10182/10030594/VB05_NDQLTBYT/aa35210b-dd78-489e-a843-8545b0b17926) · [Danh mục văn bản, imda.moh.gov.vn](https://imda.moh.gov.vn/van-ban-phap-quy) |
| TT-05-2022-BYT | 05/2022/TT-BYT (01/08/2022) | Chi tiết NĐ 98: Đ2 + **PL I quy tắc phân loại** (16 quy tắc thường + 7 quy tắc IVD, theo ASEAN); Đ5 danh mục phải kiểm định (6 thiết bị phần cứng) | 01/08/2022 | Còn HL; sửa bởi TT 59/2025/TT-BYT rồi **TT 24/2026** (TT 59/2025/TT-BYT hết HL 01/07/2026); VBHN 04/VBHN-BYT (19/01/2026, thứ cấp) | Như NĐ 98 | **gốc-OCR** (lớp text gốc bị lỗi mã, đã OCR lại) | [PDF, Cục HT&TBYT](https://imda.moh.gov.vn/documents/10182/10030594/05TT.signed_compress.pdf/35c913bf-b4cd-4b30-b97f-fe12ee9f5d0e) · [VBHN 04/VBHN-BYT, luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/van-ban-hop-nhat-04-vbhn-byt-2026-quy-dinh-chi-tiet-thi-hanh-nghi-dinh-98-2021-ve-quan-ly-thiet-bi-y-te-424617-d5.html) |
| TT-24-2026-BYT | 24/2026/TT-BYT (30/06/2026) | Đ2: mức độ rủi ro và biện pháp quản lý TBYT "thực hiện theo" NĐ 98 và văn bản hướng dẫn; Đ3: sửa TT 05 Đ8 (lộ trình kiểm định) | 01/07/2026 | Còn HL; thay TT 59/2025/TT-BYT | Như NĐ 98 | **gốc** (PDF ký số, 3 trang) | [VB 218703](https://vanban.chinhphu.vn/?pageid=27160&docid=218703) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/24-byt.signed.pdf) |
| ND-90-2026 | 90/2026/NĐ-CP | Xử phạt VPHC y tế: Đ4 k5 (tổ chức ×2), Đ40 k1 (HSBA), **Đ71, Đ73, Đ79** (TBYT) | 15/05/2026 | Còn HL; thay NĐ 117/2020 | Cá nhân, tổ chức | **gốc-OCR** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |

**Bảng chế tài liên quan (NĐ 90/2026, gốc-OCR).** Mức trong Chương II là mức cho **cá nhân**; tổ chức bị phạt **gấp 2 lần** (Đ4 k5).

| Hành vi | Điều khoản | Mức phạt cá nhân | Mức phạt tổ chức |
|---|---|---|---|
| Lưu hành TBYT khi chưa có số lưu hành / giấy phép nhập khẩu | Đ73 k4 a | 80–100 triệu | 160–200 triệu |
| Không phân loại, không công bố kết quả phân loại TBYT lên Cổng của BYT | Đ71 k1 | 25–50 triệu | 50–100 triệu |
| Không thông báo thay đổi và cập nhật hồ sơ công bố tiêu chuẩn áp dụng (5 ngày làm việc) / hồ sơ đăng ký lưu hành (10 ngày làm việc) | Đ73 k1 d, đ | 20–40 triệu | 40–80 triệu |
| Không có HDSD tiếng Việt; lưu hành mà cơ sở sản xuất chưa công bố đủ điều kiện sản xuất | Đ73 k1 b, g | 20–40 triệu | 40–80 triệu |
| Không công bố lại tiêu chuẩn áp dụng (loại A, B) khi thay đổi chủ sở hữu, loại, chủng loại, mục đích sử dụng, chỉ định | Đ73 k2 a | 40–60 triệu | 80–120 triệu |
| Không lập, duy trì hồ sơ theo dõi và truy xuất nguồn gốc TBYT | Đ73 k2 b, g | 40–60 triệu (theo khung k2, chưa đối chiếu từng điểm) | ×2 |
| **Cơ sở y tế** sử dụng TBYT không có số lưu hành | Đ79 k3 | 10–20 triệu | 20–40 triệu |
| Cơ sở y tế không lập, quản lý, lưu trữ hồ sơ TBYT; vận hành không theo hướng dẫn chủ sở hữu | Đ79 k2 | 3–5 triệu | 6–10 triệu |
| Cơ sở y tế không báo cáo TBYT có lỗi | Đ79 k1 | 0,5–1 triệu | 1–2 triệu |
| Không lập HSBA đầy đủ mục theo mẫu; không lưu trữ hồ sơ, bệnh án | Đ40 k1 a, b | 1–3 triệu | 2–6 triệu |

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### A. Liên thông và sử dụng lại kết quả CLS

### CLS-R01 — Mốc 01/01/2027 liên thông và sử dụng kết quả CLS giữa cơ sở KCB BHYT
- **Căn cứ**:
  - Luật 51/2024 **Đ3 k4**: "Chậm nhất là ngày 01 tháng 01 năm 2027, thực hiện liên thông, sử dụng kết quả cận lâm sàng liên thông giữa các cơ sở khám bệnh, chữa bệnh bảo hiểm y tế phù hợp với yêu cầu chuyên môn theo quy định của Chính phủ."
  - Luật 51/2024 Đ1 k3 b, sửa **Đ6 k3 Luật BHYT**: BYT ban hành quy định về "việc liên thông và sử dụng kết quả cận lâm sàng liên thông giữa các cơ sở khám bệnh, chữa bệnh bảo hiểm y tế phù hợp yêu cầu chuyên môn".
  - NĐ 313/2026 **Đ2 k14 c**: BYT ban hành quy định về liên thông và sử dụng kết quả CLS; "ban hành, cấp mã danh mục dùng chung, các tiêu chuẩn, định dạng dữ liệu, kết nối, liên thông dữ liệu điện tử trong lĩnh vực bảo hiểm y tế".
- **Áp dụng cho**: mọi cơ sở KCB BHYT có làm CLS hoặc nhận người bệnh chuyển đến; vendor HIS/LIS/RIS/PACS · **Hiệu lực / hạn chót**: 01/01/2027 [TỚI].
- **Mức**: **BẮT BUỘC?** Mốc là luật định nhưng văn bản chi tiết (DT-CLS-LT) chưa ban hành đến 05/10/2026. NĐ 188/2025 không có điều nào về nội dung này (BHYT-GD-R14).
- **Phần mềm phải**: trước 01/01/2027, có khả năng (1) xuất kết quả CLS của cơ sở theo gói có cấu trúc (CLS-R02, CLS-R05), (2) nhận và hiển thị kết quả CLS của cơ sở khác kèm nguồn gốc, (3) hỗ trợ bác sĩ quyết định dùng lại hay chỉ định lại (CLS-R03, CLS-R06). Phải có lớp chuyển đổi định dạng (adapter) vì định dạng trao đổi chưa được quy định (suy luận).
- **Ghi chú / bẫy**:
  - **Giải quyết câu hỏi mở 1 (cụm K7)**: "theo quy định của Chính phủ" ở Đ3 k4 **chưa có nghị định riêng**. Thẩm quyền ban hành nội dung chi tiết được giao cho **BYT** qua Luật BHYT Đ6 k3 (sửa bởi Luật 51) và nhắc lại trong NĐ 313/2026 Đ2 k14 c. Công cụ thực tế là **thông tư của BYT** (DT-CLS-LT). Nếu đến 01/01/2027 thông tư chưa có hiệu lực thì nghĩa vụ áp dụng ra sao: **cần luật sư/hỏi BYT** (xem mục 7).
  - Chi tiết nghĩa vụ phía BHYT (XML, thanh toán) xem BHYT-GD-R14; ở đây là yêu cầu về dữ liệu và phần mềm.

### CLS-R02 — Kết quả CLS phải mang đủ thông tin định danh, thời điểm, người thực hiện, người kết luận, cơ sở thực hiện
- **Căn cứ**:
  - TT 32/2023 **Đ52 k2 d**: "Thông tin trong hồ sơ bệnh án cần thể hiện rõ thời gian và người ghi chép." Đ52 k2 c: không dùng chữ viết tắt trong tài liệu bàn giao cho cơ sở KCB khác.
  - Luật KCB Đ2 k17: HSBA gồm "kết quả cận lâm sàng"; Đ77 k4: chuyển cơ sở thì phải hoàn chỉnh HSBA.
  - DT-CLS-LT (bản 08/2026, thứ cấp): cơ sở phải bảo đảm "đầy đủ thông tin nhân dạng bệnh nhân, thời gian lấy mẫu, người thực hiện"; thời hạn giá trị tính **từ thời điểm lấy mẫu** (xét nghiệm) hoặc **thời điểm thực hiện kỹ thuật** (điện quang).
  - DT-CLS-LT (bản 11/2025, thứ cấp qua baodauthau): kết quả CĐHA có giá trị pháp lý khi làm tại cơ sở có phép, đúng phạm vi, **ký bởi người thực hiện và bác sĩ đọc** (giấy) hoặc **xác thực điện tử**.
  - QĐ 2429/2017 tiêu chí **8.21** (nội dung phiếu trả kết quả, xem CLS-R12).
- **Áp dụng cho**: mọi cơ sở KCB (TT 32); liên thông: cơ sở BHYT · **Hiệu lực**: TT 32 từ 01/01/2024; DT-CLS-LT chưa có.
- **Mức**: **BẮT BUỘC** với thời gian và người ghi (TT 32 Đ52); **BẮT BUỘC?** với bộ trường liên thông (dự thảo).
- **Phần mềm phải**: mỗi kết quả CLS lưu tối thiểu: định danh người bệnh (số định danh cá nhân, xem EMR-R05; mã BN nội bộ; mã thẻ BHYT nếu có), mã cơ sở thực hiện, mã DVKT dùng chung và mã chỉ số QĐ 1227 (CLS-R07), **thời điểm lấy mẫu** hoặc **thời điểm thực hiện kỹ thuật** (bắt buộc, có múi giờ), thời điểm nhận mẫu, thời điểm duyệt và phát hành, người thực hiện (KTV), người đọc/kết luận (BS), người duyệt, phương pháp/thiết bị, loại mẫu, trạng thái (sơ bộ/chính thức/đã sửa). Không cho phát hành kết quả khi thiếu các trường này. Bản gửi cho cơ sở khác không dùng viết tắt nội bộ.
- **Ghi chú / bẫy**: nhiều HIS chỉ lưu "ngày chỉ định" và "ngày kết quả"; thiếu **thời điểm lấy mẫu** thì không tính được thời hạn giá trị khi liên thông. XML4 có trường ngày kết quả và mã BS đọc kết quả (BHYT-DATA), nhưng không đủ cho liên thông lâm sàng (suy luận).

### CLS-R03 — Thời hạn giá trị theo từng dịch vụ và cảnh báo chỉ định trùng lặp
- **Căn cứ**: DT-CLS-LT bản 08/2026 (thứ cấp, nhiều báo): danh mục **441** kỹ thuật gồm 367 điện quang (X-quang, CT, MRI), 26 vi sinh – ký sinh trùng (**48 giờ đến 30 ngày, chỉ kết quả dương tính**), 27 huyết học – truyền máu (**24 giờ đến 7 ngày**), 21 hóa sinh (**24 giờ đến 60 ngày**; ví dụ HbA1c 60 ngày; acid uric, cholesterol toàn phần tối đa 168 giờ; urê, bilirubin tối đa 24 giờ). TT 59/2025/TT-BKHCN Đ32 k1 đ: bác sĩ "tham khảo thông tin các lần khám trước để tránh việc kiểm tra bổ sung nếu không cần thiết" (gốc-OCR).
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: khi thông tư ban hành; Đ32 TT 59/2025/TT-BKHCN đã có HL từ 01/01/2026.
- **Mức**: **BẮT BUỘC?** (dự thảo; con số có thể đổi giữa các bản).
- **Phần mềm phải**:
  - Bảng tham số cấu hình được, có phiên bản và ngày hiệu lực: `mã dịch vụ/chỉ số → thời hạn giá trị (giờ) → điều kiện (vd "chỉ dương tính") → căn cứ (số hiệu văn bản)`. Không hard-code.
  - Khi bác sĩ chỉ định CLS: tra kết quả cùng loại còn hạn (của chính cơ sở và nhận từ cơ sở khác) và **cảnh báo trùng lặp**.
  - Với điện quang: hiển thị lịch sử chụp trước đó (đáp ứng cả Đ32 k1 đ TT 59/2025/TT-BKHCN).
- **Ghi chú / bẫy**: bản 11/2025 có 6 phụ lục (gồm di truyền – sinh học phân tử 86, giải phẫu bệnh 14, điện quang 893); bản 08/2026 rút còn 4 nhóm. Đừng nạp cứng danh mục theo bản nháp. Sở Y tế một số tỉnh đề nghị khớp thời hạn với quy định thanh toán BHYT (vietnamnet 2026), nên con số còn có thể đổi.

### CLS-R04 — Công nhận kết quả theo mức chất lượng phòng xét nghiệm
- **Căn cứ**: DT-CLS-LT (thứ cấp): "công nhận kết quả lẫn nhau giữa các phòng xét nghiệm đạt cùng mức chất lượng"; PXN mức thấp công nhận kết quả của PXN mức cao hơn; PXN đạt ISO 15189 liên thông theo phạm vi được công nhận (bản 11/2025); cơ sở phải **công khai** kết quả đánh giá chất lượng xét nghiệm. TT 01/2013 **Đ4 k3**: cơ sở KCB "phải công khai công tác kiểm chuẩn xét nghiệm". QĐ 2429/2017 phần I mục 8: 6 bậc (chưa xếp mức; mức 1: 20–<35% điểm; mức 2: 35–<65%; mức 3: 65–<85%; mức 4: 85–<95%; mức 5: ≥95%), mỗi mức phải đạt các tiêu chí bắt buộc (*, ***). Mục tiêu của QĐ 2429 nêu rõ là căn cứ "liên thông, công nhận kết quả xét nghiệm".
- **Áp dụng cho**: PXN của cơ sở KCB; cơ sở nhận kết quả · **Hiệu lực**: TT 01/2013 Đ4 k3 đang HL; phần công nhận chờ thông tư.
- **Mức**: **BẮT BUỘC** (công khai kiểm chuẩn, TT 01/2013 Đ4 k3); **BẮT BUỘC?** (công nhận theo mức).
- **Phần mềm phải**: có danh mục "năng lực chất lượng" theo cơ sở/PXN/phạm vi: mức chất lượng theo QĐ 2429 (ngày đánh giá, cơ quan đánh giá, hiệu lực), chứng nhận ISO 15189 (danh sách xét nghiệm trong phạm vi, ngày hết hạn). Gắn thông tin này vào kết quả khi gửi đi. Phía nhận: tự so mức chất lượng nguồn với mức của PXN nhận và gợi ý "được công nhận / cần cân nhắc".
- **Ghi chú / bẫy**: CĐHA **chưa có** hệ thống đánh giá mức chất lượng tương đương; BYT nói sẽ xây dựng riêng (vietnamnet 2026). Không suy diễn quy tắc "mức" cho điện quang.

### CLS-R05 — Liên thông kết quả CĐHA gồm cả dữ liệu ảnh, toàn vẹn, định dạng DICOM
- **Căn cứ**:
  - DT-CLS-LT bản 08/2026 (thứ cấp): với CĐHA, dữ liệu liên thông gồm "kết luận" **và** dữ liệu hình ảnh.
  - DT-CLS-LT bản 11/2025 (thứ cấp): dữ liệu ảnh phải nguyên vẹn, rõ, đủ chuỗi ảnh (CT/MRI), "định dạng chuẩn DICOM, kèm phần mềm đọc"; có thể kết nối PACS–PACS; cơ sở chuyển gửi kèm phiếu kết quả và dữ liệu điện tử; thông tin người bệnh trên ảnh khớp HSBA; cấm sửa, cắt xén dữ liệu ảnh.
  - TT 54/2017 PL I tiêu chí **70** (cơ bản): "Hỗ trợ tiêu chuẩn HL7 bản tin, DICOM"; **74** (cơ bản): kết xuất ảnh DICOM ra CD/DVD kèm phần mềm xem hoặc đường dẫn web; **78** (nâng cao): xem ảnh DICOM qua WebView; **79** (nâng cao): hội chẩn đa điểm.
- **Áp dụng cho**: cơ sở có CĐHA, vendor RIS/PACS · **Hiệu lực**: chờ thông tư.
- **Mức**: **BẮT BUỘC?** (dự thảo); hiện tại **NÊN** (TT 54 chỉ là tiêu chí xếp mức).
- **Phần mềm phải**: lưu **ảnh gốc DICOM** (không chỉ JPEG), xuất trọn study (đủ series) kèm báo cáo đã ký; cung cấp kênh nhận/gửi PACS–PACS (DICOM C-STORE/C-MOVE hoặc DICOMweb STOW/WADO — lựa chọn kỹ thuật là suy luận); tính và lưu hash cho study gửi đi; đối chiếu định danh người bệnh trong DICOM header với HSBA trước khi gửi và khi nhận; ghi nhận ảnh nhận được là "ảnh ngoài cơ sở" (không ghi đè, không tính phí lại).
- **Ghi chú / bẫy**: **Giải quyết câu hỏi mở 2 (một phần)**: theo báo, dự thảo liên thông **cả ảnh gốc lẫn kết luận**; DICOM xuất hiện ở bản 11/2025, chưa thấy báo nêu lại ở bản 08/2026. Định dạng trao đổi cho kết quả xét nghiệm (HL7 v2/FHIR/XML) **chưa thấy** trong bất kỳ bản nào. TT 54 tiêu chí 68 mô tả luồng "PACS chuyển DICOM sang JPEG cho RIS, RIS trả JPEG cho HIS để hoàn thiện HSBA": luồng này **không đủ** cho liên thông ảnh theo dự thảo (suy luận).

### CLS-R06 — Bác sĩ quyết định dùng lại hay làm lại; ghi lý do
- **Căn cứ**: DT-CLS-LT (thứ cấp): bác sĩ điều trị quyết định dùng kết quả liên thông hay chỉ định lại và "chịu trách nhiệm"; nếu chỉ định lại thì phải ghi rõ lý do (vietnamnet 2026). Bản 11/2025: cơ sở nhận được chụp lại khi lâm sàng thay đổi rõ, đã quá lâu, chất lượng ảnh kém, hoặc nghi sai lệch thông tin người bệnh. Luật KCB Đ62 k2 a: người hành nghề chỉ định "kịp thời, chính xác và chịu trách nhiệm về quyết định của mình".
- **Áp dụng cho**: cơ sở nhận người bệnh · **Hiệu lực**: chờ thông tư.
- **Mức**: **BẮT BUỘC?**
- **Phần mềm phải**: khi cảnh báo trùng lặp (CLS-R03) mà bác sĩ vẫn chỉ định, bắt chọn lý do theo danh mục (lâm sàng thay đổi; quá thời hạn; chất lượng ảnh/mẫu không đạt; nghi sai lệch định danh; PXN nguồn không đủ mức chất lượng; khác + mô tả) và lưu vào y lệnh. Báo cáo tỷ lệ chỉ định lại có/không lý do.
- **Ghi chú / bẫy**: giám định BHYT có thể dùng lý do này để xét thanh toán dịch vụ lặp (suy luận, chưa có văn bản).

### CLS-R07 — Dùng mã chỉ số CLS dùng chung (QĐ 1227/2025)
- **Căn cứ**: QĐ 1227/QĐ-BYT **Đ1** (ban hành danh mục để "thống nhất thuật ngữ chuyên môn, chuẩn hoá dữ liệu, ứng dụng công nghệ thông tin trong bệnh án điện tử, liên thông kết quả cận lâm sàng, dữ liệu khám chữa bệnh, bảo hiểm y tế"), **Đ2** (áp dụng thống nhất toàn quốc, mọi cơ sở công lập và tư nhân), Đ4 (HL từ ngày ký). QĐ 2010/2025 Đ3: XML4 dùng tên, mã chỉ số theo QĐ 1227; chỉ số chưa có thì tạm dùng PL11 QĐ 7603 (BHYT-DATA-R17). NĐ 313/2026 Đ2 k14 c: BYT cấp mã danh mục dùng chung.
- **Áp dụng cho**: mọi cơ sở KCB; vendor LIS/RIS/HIS · **Hiệu lực**: 11/04/2025 [QUA].
- **Mức**: **BẮT BUỘC** với XML4 (cơ sở BHYT); **BẮT BUỘC?** với dữ liệu nội bộ và EMR (QĐ hành chính, không phải VBQPPL, nhưng Đ2 viết "áp dụng thống nhất").
- **Phần mềm phải**: danh mục chỉ số nội bộ (theo máy, theo PXN) phải ánh xạ 1-n sang mã QĐ 1227, lưu cả mã nội bộ, mã máy (LIS host code) và mã dùng chung; có cờ "chưa có mã 1227, đang dùng PL11 7603"; chặn gửi kết quả liên thông nếu chỉ số chưa ánh xạ (suy luận). Có bảng đơn vị đo theo SI khi có thể (QĐ 2429 tiêu chí 8.21 i).
- **Ghi chú / bẫy**: **Giải quyết khoảng trống 2 (một phần)**: "danh mục chỉ số xét nghiệm chuẩn" hiện là QĐ 1227 (2.964 chỉ số, gồm cả 1.240 chỉ số điện quang). **Không tìm thấy** văn bản bắt dùng LOINC. Cấu trúc cột của phụ lục (có ánh xạ LOINC hay không, có đơn vị chuẩn không) **chưa xác minh** vì chưa đọc được phụ lục gốc.

### CLS-R08 — Kết quả của xét nghiệm gửi đi ngoài cơ sở (DVCLS chuyển)
- **Căn cứ**: NĐ 188/2025 Đ44 (chuyển người bệnh hoặc mẫu bệnh phẩm làm DVCLS; Mẫu số 9) — chi tiết ở **BHYT-GD-R13**. QĐ 2429 tiêu chí **8.21 c**: phiếu kết quả "có nhận dạng các xét nghiệm của PXN chuyển gửi thực hiện".
- **Áp dụng cho**: cơ sở gửi và nhận mẫu · **Hiệu lực**: 01/07/2025.
- **Mức**: **BẮT BUỘC** (NĐ 188 phần thanh toán); **NÊN** (đánh dấu trên phiếu).
- **Phần mềm phải**: LIS nhận kết quả của PXN ngoài (nhập tay hoặc giao diện), gắn cờ "thực hiện tại [mã cơ sở]", giữ mức chất lượng của PXN ngoài (CLS-R04) và in nhận dạng này trên phiếu.

### B. LIS và quản lý chất lượng xét nghiệm

### CLS-R09 — Chương trình nội kiểm có hệ thống ghi chép, lưu trữ, phát hiện sự cố
- **Căn cứ**: TT 01/2013 **Đ5 k4**: "Xây dựng và thực hiện chương trình nội kiểm do lãnh đạo cơ sở khám bệnh, chữa bệnh phê duyệt, có hệ thống ghi chép, lưu trữ, phát hiện sự cố và biện pháp khắc phục, phòng ngừa sự cố." Đ6 k2 a: thiết lập hệ thống quản lý tài liệu, hồ sơ, "khuyến khích ứng dụng công nghệ thông tin". Đ9 k4: nhân viên QLCL thu thập, phân tích dữ liệu, "quản lý và bảo mật thông tin". QĐ 2429 tiêu chí 8.7–8.11 (*), 8.13.
- **Áp dụng cho**: cơ sở KCB có PXN (BV, PK có xét nghiệm) · **Hiệu lực**: từ 15/03/2013.
- **Mức**: **BẮT BUỘC** (nghĩa vụ có hồ sơ nội kiểm). Dùng phần mềm hay sổ giấy: **không bắt buộc**.
- **Phần mềm phải** (nếu LIS đảm nhận): lưu kết quả QC theo máy, theo xét nghiệm, theo lô vật liệu kiểm soát, **ít nhất 2 mức** cho định lượng (QĐ 2429 tiêu chí 8.7), chứng âm/chứng dương cho định tính (8.8); biểu đồ Levey-Jennings và quy tắc Westgard (công cụ là suy luận); ghi nhận sự cố QC, hành động khắc phục, người duyệt; xem xét định kỳ xu hướng (8.13).
- **Ghi chú / bẫy**: **Giải quyết câu hỏi mở 5**: TT 25/2026 Đ1 **chỉ sửa Đ5 k5** (ngoại kiểm), **không** đặt thêm yêu cầu nào với LIS. TT 01/2013 không bắt dùng phần mềm.

### CLS-R10 — Ngoại kiểm: từ bắt buộc thành khuyến khích (từ 15/08/2026)
- **Căn cứ**: TT 01/2013 Đ5 k5 bản gốc: "Tham gia các chương trình ngoại kiểm theo chuyên ngành...". TT 25/2026 **Đ1** sửa thành: "Khuyến khích các cơ sở khám bệnh, chữa bệnh tham gia các chương trình ngoại kiểm..." (HL 15/08/2026 theo Đ6 k1). QĐ 2429 tiêu chí **8.15** (*) vẫn coi tham gia EQA hoặc so sánh liên phòng là tiêu chí bắt buộc để được xếp mức.
- **Áp dụng cho**: cơ sở KCB có PXN · **Hiệu lực**: 15/08/2026 [QUA].
- **Mức**: **NÊN** về mặt pháp lý. Thực tế cần có để được xếp mức chất lượng, và do đó để kết quả được công nhận khi liên thông (CLS-R04; suy luận).
- **Phần mềm phải**: lưu kết quả EQA theo chương trình, đợt, xét nghiệm, đánh giá đạt/không đạt, hành động khắc phục (8.15 c); xuất báo cáo cho đoàn đánh giá.
- **Ghi chú / bẫy**: tài liệu cũ hay viết "ngoại kiểm là bắt buộc theo TT 01/2013". Từ 15/08/2026 câu này **sai**.

### CLS-R11 — Chặn trả kết quả khi nội kiểm không đạt
- **Căn cứ**: QĐ 2429 tiêu chí **8.6** (PXN có quy định "tạm dừng trả kết quả cho khách hàng nếu kết quả nội kiểm không đạt"), **8.11** (*: nội kiểm đồng thời hoặc trước khi chạy mẫu người bệnh), **8.12** (***: QC không đạt thì tìm nguyên nhân, khắc phục, chỉ chạy tiếp sau khi khắc phục). TT 01/2013 Đ2 k5: nội kiểm nhằm bảo đảm kết quả "có đủ độ tin cậy trước khi trả cho khách hàng".
- **Áp dụng cho**: PXN muốn đạt mức chất lượng · **Hiệu lực**: từ 2017.
- **Mức**: **NÊN** (tiêu chí của QĐ hành chính); tiêu chí *** là bắt buộc để đạt **mức 3** trở lên.
- **Phần mềm phải**: trạng thái QC theo (máy, xét nghiệm, ca); khi QC "không đạt" thì khóa duyệt và phát hành kết quả người bệnh của xét nghiệm đó trên máy đó cho đến khi có bản ghi khắc phục được duyệt; cho phép "giữ lại" kết quả đã chạy trong cửa sổ lỗi để chạy lại; log toàn bộ thao tác ghi đè khóa (ai, khi nào, lý do).

### CLS-R12 — Phiếu trả kết quả xét nghiệm có đủ nội dung tối thiểu
- **Căn cứ**: QĐ 2429 tiêu chí **8.21** (3 điểm), phiếu gồm: (a) loại xét nghiệm, phương pháp/kỹ thuật/thiết bị; (b) nhận biết PXN trả kết quả; (c) nhận dạng xét nghiệm chuyển gửi; (d) nhận biết người bệnh và địa chỉ trên **mọi trang**; (e) tên người yêu cầu; (f) ngày (giờ) nhận mẫu; (g) loại mẫu; (h) quy trình đo; (i) đơn vị SI khi có thể; (j) khoảng tham chiếu, giá trị quyết định lâm sàng; (k) diễn giải; (l) ghi chú cảnh báo; (m) **người xem xét và có thẩm quyền ban hành**; (n) **ngày ký duyệt và thời gian ban hành**; (o) số trang/tổng số trang; (p) khoảng trống phiên giải. Tiêu chí 8.20: PXN quy định định dạng phiếu và hình thức trả. TT 32/2023 Đ51 k1 b: mẫu giấy, phiếu y ở PL XXIX.
- **Áp dụng cho**: PXN của cơ sở KCB · **Hiệu lực**: từ 2017.
- **Mức**: **NÊN** (QĐ 2429). Nếu PL XXIX TT 32 có mẫu phiếu kết quả xét nghiệm thì mẫu đó **BẮT BUỘC** theo Đ51: **chưa xác minh** từng mẫu trong PL XXIX.
- **Phần mềm phải**: mẫu in và bản điện tử (PDF/A hoặc tài liệu ký số) chứa đủ (a)–(p); header/footer lặp định danh người bệnh và "trang x/y"; khoảng tham chiếu theo tuổi, giới; cờ H/L và cờ nguy kịch.

### CLS-R13 — Rà soát, ký duyệt, kết quả tạm thời, báo động giá trị nguy kịch
- **Căn cứ**: QĐ 2429 tiêu chí **3.5** (*: người ký duyệt kết quả có đủ năng lực theo quy định), **8.18** (***: quy trình rà soát kết quả trước khi trả, nêu rõ người có thẩm quyền), **8.22** (quy trình trả kết quả: ghi chú chất lượng mẫu không đạt; thông báo kết quả "cảnh báo"/"báo động"; khi trả kết quả tạm thì phải gửi báo cáo cuối cùng; kết quả qua điện thoại hoặc bản điện tử phải đến đúng người có thẩm quyền nhận; báo miệng thì phải gửi văn bản sau và có hồ sơ ghi lại). TT 01/2013 Phụ lục, chỉ số **21** ("Có trả kết quả các trường hợp giá trị vượt ngưỡng nguy kịch") và **24** (trả kết quả chính xác không nhầm lẫn). Ký số người duyệt: EMR-R06, EMR-R07. Kết quả HIV dương tính: chỉ thông báo cho người được phép (DLCN-R32).
- **Áp dụng cho**: PXN · **Hiệu lực**: từ 2013/2017.
- **Mức**: **NÊN** (QĐ 2429), trừ phần ký số HSBA và bảo mật HIV là **BẮT BUỘC** theo cụm EMR, DLCN.
- **Phần mềm phải**: hai bước duyệt (duyệt kỹ thuật, duyệt y khoa) gắn với danh sách người được ủy quyền ký duyệt theo nhóm xét nghiệm; trạng thái "sơ bộ" và "chính thức" tách biệt, kết quả sơ bộ hiển thị rõ nhãn; quy tắc giá trị nguy kịch cấu hình được, sinh cảnh báo có xác nhận đã nhận (người nhận, thời điểm, kênh), leo thang khi quá thời gian; nhật ký báo miệng.

### CLS-R14 — Sửa kết quả sau khi phát hành: giữ bản gốc, đánh dấu, thông báo
- **Căn cứ**: QĐ 2429 tiêu chí **8.23** (kết quả đã sửa được nhận biết rõ, dẫn chiếu ngày và định danh của báo cáo ban đầu; khách hàng biết có sửa; hồ sơ sửa có thời gian, ngày, tên người chịu trách nhiệm), **8.24** ("Kết quả ban đầu được lưu giữ khi thực hiện các sửa đổi"). NĐ 90/2026 Đ38 k5 e: phạt tẩy xóa, sửa chữa HSBA nhằm sai lệch thông tin (EMR-R10).
- **Áp dụng cho**: PXN, khoa CĐHA · **Hiệu lực**: đang HL.
- **Mức**: **BẮT BUỘC** (cấm sửa làm sai lệch HSBA, kết quả CLS là một phần HSBA); **NÊN** (quy trình chi tiết theo QĐ 2429).
- **Phần mềm phải**: kết quả đã phát hành là bất biến; sửa bằng cách tạo phiên bản mới có trạng thái "đã sửa", lý do, người sửa, thời điểm, liên kết phiên bản trước; thông báo tự động cho người chỉ định và, nếu đã gửi liên thông hoặc XML4, đánh dấu cần gửi lại (BHYT-DATA-R06). Áp dụng tương tự cho báo cáo CĐHA (addendum).

### CLS-R15 — Thời gian quay vòng (TAT) đo được theo từng giai đoạn
- **Căn cứ**: TT 01/2013 **Đ5 k6 a**: bộ chỉ số chất lượng xây dựng "theo quy định tại Phụ lục"; Phụ lục mục I.2: chỉ số phải đánh giá cả 3 quy trình trước, trong, sau xét nghiệm; danh mục tham khảo có chỉ số **6** (thời gian lấy mẫu), **17** (thời gian hoàn thành xét nghiệm), **23** (thời gian trả kết quả). QĐ 2429 phần I mục 3 g: định nghĩa "thời gian trả kết quả" tính từ khi PXN nhận hay lấy mẫu đến khi trả kết quả.
- **Áp dụng cho**: PXN · **Hiệu lực**: từ 2013.
- **Mức**: **BẮT BUỘC?** (bắt xây bộ chỉ số; Phụ lục ghi là "danh mục tham khảo").
- **Phần mềm phải**: ghi mốc thời gian chuẩn hóa cho mỗi mẫu: chỉ định, lấy mẫu, nhận mẫu, bắt đầu chạy, có kết quả máy, duyệt kỹ thuật, duyệt y khoa, phát hành, người nhận xem; báo cáo TAT theo xét nghiệm, theo khoa, theo ca; tỷ lệ mẫu bị từ chối và lý do (chỉ số 11).

### CLS-R16 — Quản lý thông tin PXN: phân quyền, toàn vẹn, ghi nhận trục trặc, dự phòng
- **Căn cứ**: QĐ 2429 Chương IX: **9.1** (***: bảo mật thông tin, kết quả), **9.2** (phân định người được truy cập, nhập, thay đổi dữ liệu và kết quả, ban hành kết quả), **9.3** (hệ thống điện tử được bảo vệ khỏi truy cập trái phép), **9.4** (toàn vẹn dữ liệu), **9.5** (lưu hồ sơ trục trặc hệ thống và khắc phục), **9.6** (kế hoạch dự phòng khi hệ thống hỏng hoặc bảo trì). Yêu cầu pháp lý tương ứng ở ANM-R09, ANM-R13, DLCN-R01.
- **Áp dụng cho**: PXN · **Mức**: **NÊN** (QĐ 2429); phần ATTT và DLCN là **BẮT BUỘC** theo cụm ANM, DLCN.
- **Phần mềm phải**: vai trò tách biệt nhập kết quả / sửa kết quả / duyệt / phát hành; log sự cố hệ thống có liên kết tới phiếu khắc phục; chế độ vận hành dự phòng (in phiếu, nhập lại có đối soát) khi LIS hoặc kết nối HIS ngừng.

### CLS-R17 — Kết nối HIS ↔ LIS và LIS ↔ máy xét nghiệm (tiêu chí TT 54)
- **Căn cứ**: TT 54/2017 PL I nhóm V. **Cơ bản**: 80 quản trị hệ thống; 81 danh mục; 82 chỉ định; 83 kết quả; **84** kết nối máy xét nghiệm (ra lệnh và nhận kết quả tự động); 85 báo cáo thống kê. **Nâng cao**: 86 quản lý mẫu; 87 hóa chất; **88** liên thông với HIS (nhận chỉ định, đồng bộ kết quả); 89 cảnh báo vượt ngưỡng. PL II: **mức 3** yêu cầu "LIS đáp ứng mức cơ bản"; **mức 4** yêu cầu "LIS đáp ứng mức đầy đủ".
- **Áp dụng cho**: cơ sở KCB tự xác định mức (TT 54 Đ5) · **Mức**: **NÊN** (khung tự đánh giá; không bắt đạt mức).
- **Phần mềm phải**: driver/middleware cho máy xét nghiệm (ASTM/LIS2-A2, HL7 v2: chọn chuẩn là suy luận), mã vạch mẫu, đồng bộ hai chiều chỉ định–kết quả với HIS.
- **Ghi chú / bẫy**: "tiêu chí 88 liên thông HIS" chỉ là **nâng cao** trong TT 54, nhưng trên thực tế cần cho XML4 và HSBA điện tử (suy luận). Xem CLS-R26 về việc middleware có thể bị coi là phụ kiện hay TBYT.

### C. RIS/PACS: lưu trữ, định dạng, trả kết quả không in phim

### CLS-R18 — Thời hạn lưu kết quả CLS và ảnh CĐHA
- **Căn cứ**: Luật KCB **Đ2 k17** (HSBA gồm kết quả CLS), Đ69 k2 (lưu theo pháp luật lưu trữ). TT 33/2025 PL: HSBA nội trú, ngoại trú **10 năm** (dòng 44); tâm thần, TNLĐ, TNGT **20 năm** (40); ghép mô tạng, phẫu thuật thẩm mỹ **20 năm** (43); tử vong **30 năm** (39); "Sổ, sách phục vụ công tác khám chữa bệnh" **05 năm** (47). TT 33 **Đ1 k2 b**: hồ sơ chưa được quy định thì áp thời hạn "tương đương", không thấp hơn mức trong phụ lục. Phụ lục **không có dòng riêng** cho phim, ảnh CĐHA, dữ liệu DICOM, kết quả xét nghiệm rời (đã kiểm lại toàn văn phụ lục).
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/07/2025.
- **Mức**: **BẮT BUỘC** với kết quả CLS và báo cáo CĐHA nằm trong HSBA (theo thời hạn HSBA, xem EMR-R22). **BẮT BUỘC?** với ảnh gốc DICOM (không có dòng riêng; phải tự xếp nhóm tương đương).
- **Phần mềm phải**: kết quả CLS và báo cáo CĐHA kế thừa "loại lưu trữ" của HSBA chứa nó (tự nâng 10 → 20 → 30 năm khi HSBA đổi loại). Với ảnh DICOM: có chính sách lưu cấu hình được theo loại HSBA, mặc định không ngắn hơn HSBA liên quan (phương án thận trọng, suy luận); PACS lưu phân tầng (nóng/ấm/lạnh) để giữ được ảnh gốc 10–30 năm; cấm xóa trước hạn; legal hold. Với lượt khám ngoại trú không lập HSBA: thời hạn **chưa xác minh** (có thể rơi vào "sổ, sách" 5 năm hoặc hồ sơ tương đương; cần hỏi BYT).
- **Ghi chú / bẫy**: **Giải quyết câu hỏi mở 4**: TT 33/2025 **không quy định** thời hạn riêng cho ảnh DICOM hay phim. Đừng trích "TT 33 quy định lưu ảnh X năm". TT 54 tiêu chí 68 cho thấy ý đồ cũ là đưa **ảnh JPEG chọn lọc** vào HSBA; nếu chỉ giữ JPEG thì không đáp ứng được liên thông ảnh gốc theo dự thảo (CLS-R05).

### CLS-R19 — DICOM: hiện chưa có văn bản quy phạm bắt buộc
- **Căn cứ**: TT 54/2017 Đ2 k11 (định nghĩa DICOM), PL I tiêu chí 70, 74, 76, 78 (DICOM là tiêu chí **cơ bản**/**nâng cao** để xếp mức RIS-PACS), nhóm phi chức năng tiêu chí "áp dụng các tiêu chuẩn trong nước hoặc quốc tế (HL7, HL7 CDA, DICOM, ICD-10...)". DT-CLS-LT bản 11/2025: định dạng chuẩn DICOM (thứ cấp). QĐ 2146/2026 (khung kiến trúc số): có nêu DICOM/DICOMweb hay không đang là MT-24 (cụm K6).
- **Áp dụng cho**: cơ sở có PACS, vendor · **Mức**: **NÊN** (hiện tại); **BẮT BUỘC?** khi thông tư liên thông ban hành với yêu cầu DICOM.
- **Phần mềm phải**: lưu và trao đổi ảnh ở DICOM nguyên bản (không chuyển mất dữ liệu làm bản lưu trữ chính); nén lưu trữ nếu dùng thì dạng không mất dữ liệu hoặc JPEG 2000 theo tiêu chí 77 (nâng cao); có DICOM conformance statement; hỗ trợ worklist và nhận ảnh từ máy chụp (tiêu chí 67).
- **Ghi chú / bẫy**: không tìm thấy VBQPPL nào **bắt buộc** DICOM. Câu "Bộ Y tế bắt buộc DICOM" trong tài liệu chào hàng của vendor là chưa có căn cứ, trừ khi dẫn được thông tư liên thông đã ban hành.

### CLS-R20 — Trả kết quả hình ảnh điện tử không in phim và tính giá BHYT
- **Căn cứ**:
  - QĐ 4868/QĐ-BYT (16/11/2015): đề án thí điểm DVKT CĐHA trên PACS không in phim, hạn đến 30/12/2019. CV 5319/BYT-KH-TC (05/10/2020): cơ sở thí điểm và cơ sở làm EMR theo TT 46/2018 được thanh toán **theo giá dịch vụ có in phim** (thứ cấp).
  - QĐ 313/QĐ-BYT (29/01/2026): giá riêng cho DVKT CĐHA **sử dụng PACS** tại BV Bạch Mai, áp dụng thanh toán BHYT; CV đôn đốc của BYT (báo 03/08/2026): mọi cơ sở xây phương án giá CĐHA dùng PACS theo **TT 21/2024/TT-BYT**, trình cấp có thẩm quyền phê duyệt (thứ cấp).
  - TT 54/2017 PL II **mức 5**: "PACS đáp ứng nâng cao, thay thế tất cả phim"; tiêu chí 74: kết xuất DICOM ra CD/DVD kèm phần mềm xem **hoặc** đường dẫn truy cập ảnh trên web.
- **Áp dụng cho**: cơ sở KCB có CĐHA muốn bỏ in phim · **Hiệu lực**: QĐ 313 từ 29/01/2026; giá các cơ sở khác phụ thuộc quyết định phê duyệt riêng.
- **Mức**: **BẮT BUỘC?** Không có văn bản nào **cấm** trả kết quả ảnh điện tử. Nhưng để **thu theo giá PACS** của BHYT thì cơ sở phải có giá được phê duyệt; tiếp tục thu giá "có in phim" mà không in phim là rủi ro xuất toán (suy luận).
- **Phần mềm phải**: danh mục DVKT có hai biến thể giá (in phim / dùng PACS) với mã và ngày hiệu lực theo quyết định phê duyệt của cơ sở; chọn biến thể theo cách trả kết quả thực tế; kênh trả kết quả ảnh cho người bệnh (cổng/app/đường dẫn có hạn, mã QR, hoặc đĩa DICOM kèm viewer) có xác thực và ghi nhận đã giao; lưu bằng chứng người bệnh đã nhận được ảnh.
- **Ghi chú / bẫy**: **Giải quyết mục "DT-QD586-SP: hướng dẫn giá RIS-PACS không in phim"** (inventory 1.8): trên thực tế cơ chế giá đã chạy qua QĐ 313/2026 và CV đôn đốc 2026, dựa trên TT 21/2024 (thứ cấp). Chưa thấy văn bản quy định **điều kiện kỹ thuật** PACS để được áp giá này (thời gian lưu, cách giao ảnh): **chưa xác minh**; cần đọc QĐ 313 bản gốc.

### CLS-R21 — Giao diện RIS ↔ HIS ↔ PACS (tiêu chí TT 54)
- **Căn cứ**: TT 54/2017 PL I nhóm IV. **Cơ bản** (62–75): quản trị, cấu hình máy chủ và trạm PACS, quản lý chỉ định, danh sách bệnh nhân được chỉ định, interface hai chiều với CT, MRI, X-quang, DSA, siêu âm (67), interface với HIS (68: RIS nhận chỉ định từ HIS và chuyển vào máy theo HL7; liên thông hai chiều báo cáo CĐHA giữa PACS và HIS), quản lý kết quả (69), HL7/DICOM (70), đo lường (71), xử lý ảnh 2D (72), 3D (73), kết xuất DICOM (74), thống kê (75). **Nâng cao** (76–79): biên tập DICOM, nén JPEG2000, WebView, hội chẩn đa điểm. PL II: **mức 4** cần "PACS đáp ứng cơ bản, cho phép các bác sỹ truy cập hình ảnh y khoa từ bên ngoài khoa chẩn đoán hình ảnh".
- **Áp dụng cho**: cơ sở tự xác định mức CNTT · **Mức**: **NÊN**.
- **Phần mềm phải**: Modality Worklist từ chỉ định HIS; trạng thái thực hiện; báo cáo có cấu trúc đồng bộ hai chiều với HIS; viewer cho bác sĩ lâm sàng ngoài khoa CĐHA có phân quyền.

### CLS-R22 — An toàn bức xạ: thông tin phục vụ bác sĩ chỉ định và nhân viên vận hành
- **Căn cứ**: TT 59/2025/TT-BKHCN **Đ32 k1** (gốc-OCR): bác sĩ điều trị chịu trách nhiệm an toàn bức xạ cho người bệnh: (c) tránh chỉ định bức xạ ion hóa cho phụ nữ có thai, nghi có thai hoặc đang cho con bú trừ khi bắt buộc, khi đó phải thông báo cho nhân viên; (đ) tham khảo các lần khám trước để tránh kiểm tra bổ sung không cần thiết; (e) chỉ định mức chiếu xạ tối thiểu "trên cơ sở các mức liều tham chiếu chẩn đoán" ở Mục 2 Phụ lục 2. Đ32 k2 a: chiếu xạ y tế chỉ thực hiện khi có chỉ định của bác sĩ.
- **Áp dụng cho**: cơ sở có X-quang, CT, y học hạt nhân, xạ trị · **Hiệu lực**: 01/01/2026 [QUA].
- **Mức**: **BẮT BUỘC** với cơ sở và người hành nghề; với phần mềm là **NÊN** (văn bản không nhắc phần mềm).
- **Phần mềm phải** (suy luận): khi chỉ định CĐHA dùng bức xạ, hiển thị lịch sử chụp chiếu (gồm ảnh liên thông) và hỏi/ghi tình trạng thai nghén, cho con bú với nữ trong độ tuổi sinh đẻ; chuyển cờ này sang RIS/worklist; RIS lưu thông số liều do máy xuất (vd DICOM RDSR) để cơ sở so với mức liều tham chiếu.
- **Ghi chú / bẫy**: **Giải quyết khoảng trống 3 (phần an toàn bức xạ)**: văn bản hiện hành là TT 59/2025/TT-BKHCN, **không phải** TTLT 13/2014 hay TT 13/2018 (đã hết HL 01/01/2026). Chưa thấy điều khoản bắt **ghi liều của từng người bệnh**; Phụ lục 2 Mục 2 chưa đọc. Xem bẫy trùng số hiệu "TT 59" ở mục 6.

### D. Phần mềm là thiết bị y tế (SaMD)

### CLS-R23 — Xác định phần mềm có phải là TBYT hay không
- **Căn cứ**:
  - NĐ 98/2021 **Đ2 k1**: TBYT là "các loại thiết bị, vật tư cấy ghép, dụng cụ, vật liệu, thuốc thử và chất hiệu chuẩn in vitro, **phần mềm (software)**" đáp ứng **đồng thời**: (a) dùng theo chỉ định của chủ sở hữu cho một hoặc nhiều mục đích: chẩn đoán, ngăn ngừa, theo dõi, điều trị, làm giảm nhẹ bệnh tật...; kiểm tra, thay thế, điều chỉnh hoặc hỗ trợ giải phẫu, quá trình sinh lý; hỗ trợ, duy trì sự sống; kiểm soát thụ thai; khử khuẩn TBYT; "cung cấp thông tin cho việc chẩn đoán, theo dõi, điều trị thông qua biện pháp kiểm tra các mẫu vật có nguồn gốc từ cơ thể con người"; (b) không dùng cơ chế dược lý, miễn dịch, chuyển hóa (hoặc chỉ hỗ trợ).
  - Đ2 k2: TBYT chẩn đoán in vitro gồm cả "hệ thống và các sản phẩm khác tham gia hoặc hỗ trợ quá trình thực hiện xét nghiệm".
  - Đ2 k4: **phụ kiện** là sản phẩm được chủ sở hữu chỉ định dùng cùng một TBYT cụ thể để thiết bị đó dùng đúng mục đích. Đ1 k2 d: NĐ **không áp dụng** với phụ kiện.
  - **Đ3 k8 a**: "Không áp dụng các quy định về phân loại, cấp số lưu hành, công bố đủ điều kiện mua bán của Nghị định này đối với: a) Phần mềm (software) sử dụng cho thiết bị y tế" (có từ bản gốc 2021, không bị sửa).
  - Đ5 k6: việc phân loại do "cơ sở đứng tên công bố tiêu chuẩn áp dụng hoặc đăng ký lưu hành" thực hiện.
- **Áp dụng cho**: vendor phần mềm y tế (chủ sở hữu sản phẩm), cơ sở KCB tự phát triển phần mềm · **Hiệu lực**: 01/01/2022.
- **Mức**: **BẮT BUỘC** (phải tự xác định; sai thì bị phạt theo NĐ 90 Đ73 k4 a hoặc Đ71).
- **Phần mềm phải** (tài liệu kèm sản phẩm): văn bản **mục đích sử dụng (intended use)** cho từng module; bảng đánh giá từng module theo Đ2 k1 (có mục đích y tế không) và Đ3 k8 a (có phải phần mềm "sử dụng cho" một TBYT cụ thể không); kết luận, người chịu trách nhiệm, ngày rà soát.
- **Ghi chú / bẫy**: **Giải quyết câu hỏi mở 3 và khoảng trống 1 (một phần)**. Phân tích (suy luận, cần luật sư xác nhận):
  - **Thường không phải TBYT** (không có mục đích y tế theo Đ2 k1 a): HIS phần hành chính, tiếp đón, viện phí, BHYT/XML, kho dược, nhân sự; EMR ở chức năng lưu và hiển thị hồ sơ; RIS/LIS phần quản lý chỉ định, mẫu, trả kết quả, thống kê; PACS chỉ lưu trữ và truyền ảnh.
  - **Phần mềm "sử dụng cho" TBYT cụ thể** (firmware, phần mềm điều khiển máy CT, phần mềm trạm xử lý đi kèm máy, phần mềm đi kèm máy xét nghiệm): rơi vào Đ3 k8 a (không phân loại, không cấp số lưu hành riêng). Cách hiểu thông dụng là chúng đi theo hồ sơ của máy (suy luận).
  - **Có rủi ro bị coi là TBYT độc lập**: phần mềm tự đưa ra hoặc đề xuất chẩn đoán từ ảnh, tín hiệu, kết quả xét nghiệm (CAD, AI đọc X-quang/CT, AI phân loại tế bào); phần mềm tính liều thuốc, liều xạ trị; phần mềm diễn giải xét nghiệm tự động thay bác sĩ; viewer PACS có chức năng **chẩn đoán** (đo lường, dựng 3D dùng để quyết định điều trị, được chào là "dùng cho chẩn đoán chính"). Các phần mềm này có mục đích "chẩn đoán... điều trị" theo Đ2 k1 a và không "sử dụng cho" một máy cụ thể nào.
  - Middleware LIS chỉ chuyển dữ liệu máy ↔ LIS: nhiều khả năng **không** là TBYT; nếu có chức năng **tự duyệt kết quả** (autoverification) hoặc tính toán chỉ số chẩn đoán thì có thể rơi vào Đ2 k2 ("hỗ trợ quá trình thực hiện xét nghiệm") (suy luận).

### CLS-R24 — Nếu là TBYT độc lập: phân loại, số lưu hành, điều kiện lưu hành
- **Căn cứ**: NĐ 98 **Đ4** (loại A thấp, B trung bình thấp, C trung bình cao, D cao), **Đ5** (phân loại dựa trên quy tắc; nhiều mục đích thì theo mức cao nhất; Đ5 k5: BYT quy định chi tiết phù hợp điều ước ASEAN), **Đ21 k1** (số lưu hành là số công bố tiêu chuẩn áp dụng với loại A, B; số giấy chứng nhận đăng ký lưu hành với loại C, D), **Đ22 k1** (lưu hành phải có số lưu hành; nhãn; **HDSD tiếng Việt**; thông tin bảo hành) và **Đ22 k3** (HDSD và bảo hành có thể ở dạng điện tử, phải có hướng dẫn tra cứu trên nhãn), **Đ23 k1** (sản xuất tại cơ sở đã công bố đủ điều kiện sản xuất nếu sản xuất trong nước; cơ sở có ISO 13485 và đã lưu hành ở bất kỳ nước nào nếu nhập khẩu; phù hợp QCVN hoặc tiêu chuẩn công bố), **Đ8 k1** (cơ sở sản xuất đạt ISO 13485), **Đ76 k5** (bắt buộc hồ sơ CSDT ASEAN từ 01/01/2024). TT 05/2022 **PL I** (quy tắc phân loại, gốc-OCR). TT 24/2026 Đ2: mức độ rủi ro và biện pháp quản lý theo NĐ 98 và văn bản hướng dẫn. Luật KCB Đ94 k2: TBYT rủi ro trung bình cao, cao phải thử nghiệm lâm sàng trước khi đăng ký lưu hành "theo quy định của Chính phủ".
- **Áp dụng cho**: chủ sở hữu và tổ chức đứng tên số lưu hành của phần mềm là TBYT · **Hiệu lực**: 01/01/2022; CSDT từ 01/01/2024.
- **Mức**: **BẮT BUỘC** (nếu kết luận là TBYT ở CLS-R23).
- **Phần mềm phải** (quy trình của vendor): bản kết quả phân loại theo PL I TT 05/2022 công bố trên Cổng của BYT; hồ sơ công bố tiêu chuẩn áp dụng (A, B) hoặc đăng ký lưu hành (C, D) theo CSDT; QMS ISO 13485 cho cơ sở sản xuất (gồm vòng đời phát triển phần mềm); HDSD tiếng Việt (có thể điện tử, có chỉ dẫn tra cứu trong màn hình "Giới thiệu"/nhãn điện tử); thông tin bảo hành; số lưu hành hiển thị trong phần mềm.
- **Ghi chú / bẫy**:
  - **Không có quy tắc phân loại riêng cho phần mềm**: đã OCR toàn bộ PL I TT 05/2022, **không có** chữ "phần mềm". Phần mềm phải được phân loại bằng quy tắc chung. Các quy tắc gần nhất là **Quy tắc 9 k2** (thiết bị chủ động nhằm kiểm soát, theo dõi hoặc ảnh hưởng trực tiếp đến hiệu năng thiết bị điều trị chủ động loại C → C), **Quy tắc 10** (thiết bị chủ động dùng để chẩn đoán: B; C nếu giám sát thông số sống mà thay đổi có thể nguy hiểm, hoặc chẩn đoán khi bệnh nhân nguy kịch; **10 k4**: thiết bị kiểm soát, theo dõi thiết bị X-quang → C), **Quy tắc 12** (thiết bị chủ động khác → A); IVD: quy tắc 1–7 Phần III. Phần mềm có phải "TBYT chủ động" (định nghĩa PL I mục 1: hoạt động bằng biến đổi nguồn năng lượng) hay không thì **chưa rõ** (suy luận).
  - TT 24/2026 **không** thêm quy tắc nào; chỉ dẫn chiếu NĐ 98 và sửa lộ trình kiểm định. Lộ trình kiểm định (30/06/2027, 01/01/2028) chỉ áp cho 6 thiết bị phần cứng ở TT 05 Đ5 (máy thở, máy gây mê kèm thở, dao mổ điện, lồng ấp, máy phá rung tim, máy thận nhân tạo), **không** liên quan phần mềm.
  - Chưa có Luật Thiết bị y tế; tờ trình dự thảo của BYT (15/06/2026) mới nêu kế hoạch xây dựng dự án Luật. Khi có luật, quy tắc cho SaMD có thể thay đổi.

### CLS-R25 — Cơ sở KCB chỉ được dùng TBYT có số lưu hành; quản lý hồ sơ, báo lỗi
- **Căn cứ**: Luật KCB **Đ113 k1** ("Thiết bị y tế sử dụng tại các cơ sở khám bệnh, chữa bệnh phải được phép lưu hành hợp pháp tại Việt Nam"), Đ113 k3 (lập, quản lý, lưu trữ hồ sơ theo dõi TBYT). NĐ 98 Đ63 k3 (hồ sơ TBYT), Đ65 k1 b (quyền yêu cầu tài liệu kỹ thuật), Đ65 k2 a (vận hành theo hướng dẫn chủ sở hữu), Đ65 k2 d (báo cáo TBYT có lỗi). NĐ 90 Đ79 k1–k3.
- **Áp dụng cho**: BV, PK, mọi cơ sở y tế dùng phần mềm là TBYT (vd AI đọc ảnh) · **Hiệu lực**: 01/01/2024 (Luật KCB).
- **Mức**: **BẮT BUỘC**.
- **Phần mềm phải** (HIS/quản lý thiết bị của cơ sở): sổ tài sản TBYT có cả phần mềm là TBYT (tên, phiên bản, số lưu hành, chủ sở hữu, ngày đưa vào dùng); kiểm tra số lưu hành trước khi kích hoạt module AI/CAD của bên thứ ba; kênh ghi nhận và báo cáo lỗi TBYT.
- **Ghi chú / bẫy**: hợp đồng mua/thuê PACS kèm AI phải yêu cầu vendor xuất trình số lưu hành hoặc văn bản lý giải vì sao không phải TBYT. Thiếu cả hai thì cơ sở chịu Đ79 k3 (suy luận về cách vận dụng).

### CLS-R26 — Sau bán hàng: thay đổi phiên bản, truy xuất, cảnh báo
- **Căn cứ**: NĐ 90/2026 Đ73 k1 d, đ (không thông báo thay đổi và cập nhật hồ sơ công bố trong **05 ngày làm việc** hoặc hồ sơ đăng ký lưu hành trong **10 ngày làm việc**), Đ73 k2 a (không công bố lại khi thay đổi chủ sở hữu, loại, chủng loại, **mục đích sử dụng, chỉ định**), Đ73 k2 b, g (truy xuất nguồn gốc, hồ sơ theo dõi), Đ73 k4 c (không xử lý sự cố ảnh hưởng sức khỏe người dùng). NĐ 98 Đ33–Đ37 (hồ sơ sau bán hàng, cảnh báo, sự cố, thu hồi; chưa đọc chi tiết từng khoản).
- **Áp dụng cho**: chủ sở hữu số lưu hành phần mềm là TBYT · **Mức**: **BẮT BUỘC** (nếu là TBYT).
- **Phần mềm phải**: quy trình phát hành có bước "phân loại thay đổi" (thay đổi thông thường / thay đổi phải thông báo / thay đổi mục đích sử dụng phải công bố lại); lưu danh sách cơ sở đang dùng từng phiên bản (truy xuất); cơ chế gửi cảnh báo an toàn và vá lỗi tới từng cơ sở; nhật ký sự cố.

### CLS-R27 — Thiết kế ranh giới để HIS/LIS/PACS không vô tình thành TBYT
- **Căn cứ**: suy ra từ NĐ 98 Đ2 k1 (định nghĩa dựa vào **mục đích sử dụng do chủ sở hữu chỉ định**), Đ5 k2–k3 (nhiều mục đích thì lấy mức cao nhất), Đ73 k2 a NĐ 90 (đổi mục đích sử dụng phải công bố lại). Luật AI 134/2025 và QĐ 33/2026/QĐ-TTg (AI rủi ro cao; mục y tế theo inventory chỉ gồm AI hỗ trợ phẫu thuật, rô-bốt và AI điều khiển máy thực thi điều trị): xem DLCN-R25 và cụm K10.
- **Áp dụng cho**: vendor · **Mức**: **NÊN** (thực hành tốt).
- **Phần mềm phải**: (1) tuyên bố intended use của sản phẩm chính **không** gồm chẩn đoán/điều trị tự động; (2) tách module có chức năng y tế (AI, CAD, tính liều) thành sản phẩm riêng, có hồ sơ TBYT riêng, bật/tắt theo hợp đồng; (3) tài liệu marketing và UI không dùng từ ngữ "chẩn đoán", "phát hiện bệnh" cho module không có số lưu hành; (4) CDSS chỉ hiển thị nguồn tham chiếu và cảnh báo để bác sĩ quyết định, không tự đổi y lệnh; (5) LIS autoverification: cấu hình quy tắc do PXN tự phê duyệt và chịu trách nhiệm, vendor chỉ cung cấp công cụ (cách thiết kế này giảm rủi ro nhưng **không chắc chắn** loại trừ được, suy luận).

---

## 3. Pattern thiết kế

### P1 — Kho kết quả CLS chuẩn hóa có metadata liên thông
- **Giải quyết**: CLS-R02, R07, R08, R12, R18.
- **Mô tả**: mọi kết quả (xét nghiệm, CĐHA, thăm dò chức năng) lưu ở một mô hình chung, tách "báo cáo" và "chỉ số".
- **Mô hình dữ liệu (gợi ý)**:
  - `cls_order(id, patient_id, encounter_id, hsba_id, service_code_internal, service_code_shared /*QĐ 2010*/, ordered_by, ordered_at, reorder_reason_code, reorder_reason_text)`
  - `cls_specimen(id, order_id, specimen_type, collected_at NOT NULL, collected_by, received_at, rejected_reason)` (xét nghiệm)
  - `cls_report(id, order_id, performing_facility_code, performing_lab_id, performed_at NOT NULL /*điện quang: thời điểm thực hiện*/, performed_by, interpreted_by, validated_by, released_at, status ENUM('preliminary','final','amended','cancelled'), version, supersedes_report_id, amendment_reason, signature_id, source ENUM('internal','external_referral','interop_received'), source_facility_code, hash)`
  - `cls_observation(id, report_id, analyte_code_internal, analyte_code_1227, analyte_code_temp_7603, value_num, value_text, unit, unit_si, ref_low, ref_high, flag, critical BOOLEAN, method, instrument_id)`
  - Ràng buộc: không cho `status='final'` khi thiếu `collected_at`/`performed_at`, `validated_by`, `analyte_code_1227` (hoặc cờ tạm 7603); `cls_report` bản final là bất biến (trigger chặn UPDATE nội dung).
  - Chỉ mục: `(patient_id, analyte_code_1227, collected_at DESC)` để tra kết quả còn hạn.
- **Đánh đổi**: tăng chi phí ánh xạ danh mục ban đầu; đổi lại dùng chung được cho XML4, EMR và liên thông.

### P2 — Bảng thời hạn giá trị có phiên bản và bộ kiểm tra trùng lặp
- **Giải quyết**: CLS-R03, R06, R22.
- **Mô tả**: `cls_validity_rule(id, code_type /*service|analyte*/, code, validity_hours, condition /*vd 'positive_only'*/, legal_basis, effective_from, effective_to)`. Khi chỉ định: truy vấn kết quả cùng mã còn trong `validity_hours` tính từ `collected_at`/`performed_at`, gồm kết quả nhận liên thông; nếu có → cảnh báo, bắt nhập `reorder_reason_code` nếu vẫn chỉ định.
- **Đánh đổi**: danh mục dự thảo đổi liên tục, nên chỉ nạp khi thông tư ban hành; trước đó chạy ở chế độ "chỉ cảnh báo, không chặn".

### P3 — Sổ năng lực chất lượng (quality credential registry) và nguồn gốc kết quả
- **Giải quyết**: CLS-R04, R08, R10.
- **Mô tả**: `lab_quality_credential(lab_id, facility_code, scheme ENUM('QD2429','ISO15189'), level, scope_analytes[], assessed_by, assessed_at, valid_to, evidence_doc_id)`. Mỗi `cls_report` gửi đi kèm snapshot credential hiệu lực tại `released_at`. Phía nhận lưu snapshot cùng kết quả.
- **Đánh đổi**: cần quy trình cập nhật thủ công khi có kết quả đánh giá mới; không có API quốc gia để tra (chưa thấy).

### P4 — Gói liên thông kết quả có ký số và lớp adapter định dạng
- **Giải quyết**: CLS-R01, R02, R05, R19.
- **Mô tả**: dựng gói nội bộ chuẩn (báo cáo + chỉ số + metadata + credential + chữ ký số của cơ sở), rồi **adapter** xuất ra định dạng mà thông tư quy định khi ban hành (HL7 v2 ORU, HL7 CDA, FHIR DiagnosticReport/Observation, hoặc XML riêng của BYT: chưa biết). Ảnh: tham chiếu study UID, truyền qua PACS–PACS hoặc DICOMweb; hash SHA-256 của từng instance.
- **API (gợi ý)**: `POST /interop/cls/outbound {patient_id, report_ids[], target_facility}`; `POST /interop/cls/inbound` (nhận, xác minh chữ ký, đối chiếu định danh, lưu `source='interop_received'`).
- **Đánh đổi**: viết adapter trước khi có chuẩn có thể phải làm lại; nhưng tách lõi khỏi định dạng giúp đổi nhanh.

### P5 — Vòng đời mẫu và kết quả xét nghiệm có cổng QC
- **Giải quyết**: CLS-R09, R11, R13, R14, R15.
- **Mô tả**: máy trạng thái `ordered → collected → received → in_analysis → result_available → tech_validated → med_validated → released → (amended)`, mỗi bước ghi `actor`, `timestamp`. Cổng QC: `qc_status(instrument_id, test_code, shift, status, run_at)`; nếu `status='fail'` thì chặn chuyển `tech_validated → released` cho tổ hợp đó cho đến khi có `qc_corrective_action` được duyệt. Giá trị nguy kịch sinh `critical_alert(report_id, notified_to, channel, acknowledged_at)`.
- **Đánh đổi**: khóa phát hành có thể làm chậm cấp cứu; cần quyền ghi đè có lý do và kiểm toán.

### P6 — Phân hệ QC nội kiểm và ngoại kiểm
- **Giải quyết**: CLS-R09, R10.
- **Mô tả**: `qc_material(lot, level, target_mean, target_sd, expiry)`, `qc_result(instrument_id, test_code, material_lot, value, run_at, rule_violations[])`, `eqa_round(program, round, test_code, result, evaluation, corrective_action_id)`. Biểu đồ Levey-Jennings, quy tắc Westgard; báo cáo theo mẫu đánh giá QĐ 2429 Chương VIII.
- **Đánh đổi**: nhiều PXN đã dùng phần mềm QC của hãng máy; khi đó LIS chỉ cần nhận trạng thái QC qua giao diện.

### P7 — Lưu trữ PACS phân tầng, thời hạn kế thừa HSBA
- **Giải quyết**: CLS-R18, R19.
- **Mô tả**: `imaging_study(study_uid, patient_id, hsba_id, retention_class, retain_until, storage_tier, legal_hold, sha256_manifest)`; `retain_until` tính lại khi `hsba.retention_class` đổi (EMR-R22). Tầng nóng (≤ 1–2 năm), lạnh (object storage, nén không mất dữ liệu). Job xóa chỉ chạy khi `now > retain_until AND NOT legal_hold` và có biên bản hủy (EMR-R24).
- **Đánh đổi**: chi phí lưu ảnh gốc 10–30 năm rất lớn; nếu chọn chỉ giữ ảnh chọn lọc thì phải có văn bản chính sách của cơ sở và chấp nhận rủi ro với liên thông ảnh gốc.

### P8 — Trả kết quả hình ảnh không in phim và chọn giá đúng
- **Giải quyết**: CLS-R20, R21.
- **Mô tả**: `service_price_variant(service_code, variant ENUM('film','pacs'), price, approval_decision_no, effective_from)`; khi phát hành kết quả CĐHA, ghi `delivery_mode ENUM('film','portal','qr_link','dicom_media')` và chọn `variant` tương ứng; cổng xem ảnh có xác thực người bệnh (OTP/VNeID), link có hạn, nhật ký truy cập.
- **Đánh đổi**: phải đồng bộ với quyết định giá từng cơ sở; nếu cơ sở chưa có giá PACS được duyệt thì phần mềm phải cảnh báo khi chọn trả không in phim mà vẫn dùng giá "có phim" (rủi ro xuất toán, suy luận).

### P9 — Sổ đăng ký mục đích sử dụng và ranh giới SaMD
- **Giải quyết**: CLS-R23, R24, R25, R27.
- **Mô tả**: `product_module(id, name, intended_use_text, is_medical_device ENUM('no','accessory_or_used_for_device','yes'), assessment_doc_id, risk_class, registration_no, registration_holder, reviewed_at)`; feature flag theo module; UI hiển thị số lưu hành ở màn hình "Giới thiệu" của module là TBYT; build pipeline chặn bật module `is_medical_device='yes'` khi `registration_no` rỗng.
- **Đánh đổi**: tách sản phẩm làm tăng chi phí đóng gói và hợp đồng, nhưng giữ HIS lõi ngoài phạm vi quản lý TBYT.

### P10 — Phát hành phiên bản có phân loại thay đổi (cho module là TBYT)
- **Giải quyết**: CLS-R26.
- **Mô tả**: mỗi release có `change_class ENUM('minor','notify_5wd','notify_10wd','re_declare')` do người phụ trách pháp chế duyệt; hạn thông báo tính theo ngày làm việc; bảng `deployment(facility_code, module_id, version, deployed_at)` để truy xuất và gửi cảnh báo an toàn.
- **Đánh đổi**: chậm phát hành; cần người có năng lực đánh giá thay đổi.

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu (ID R) | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| CLS-A01 | R01 | Hỏi vendor lộ trình đáp ứng liên thông CLS 01/01/2027; kiểm tra có module xuất/nhận kết quả của cơ sở khác không | Tài liệu lộ trình, demo | Bắt buộc? |
| CLS-A02 | R02 | SQL: tỷ lệ kết quả CLS final thiếu `collected_at`/`performed_at`, người thực hiện, người duyệt. In thử phiếu gửi cơ sở khác, tìm chữ viết tắt nội bộ | Kết quả truy vấn, bản in | Bắt buộc |
| CLS-A03 | R03 | Chỉ định lại HbA1c trong 30 ngày, urê trong 12 giờ: có cảnh báo trùng lặp không? Bảng thời hạn có cấu hình được, có ngày hiệu lực không? | Ảnh màn hình, cấu hình | Bắt buộc? |
| CLS-A04 | R04 | Có lưu mức chất lượng PXN (QĐ 2429) và phạm vi ISO 15189 kèm hạn không? Cơ sở có công khai kết quả kiểm chuẩn không (TT 01/2013 Đ4 k3)? | Màn hình danh mục, trang công khai | Bắt buộc / Bắt buộc? |
| CLS-A05 | R05, R19 | Xuất một study CT: có đủ series DICOM gốc, header khớp HSBA, có hash không? PACS lưu DICOM gốc hay chỉ JPEG? | File xuất, DICOM dump, cấu hình lưu trữ | Bắt buộc? |
| CLS-A06 | R06 | Khi bác sĩ vẫn chỉ định dù có kết quả còn hạn: phần mềm có bắt nhập lý do không? Báo cáo tỷ lệ chỉ định lại | Ảnh màn hình, báo cáo | Bắt buộc? |
| CLS-A07 | R07 | Tỷ lệ chỉ số XN/CĐHA đã ánh xạ mã QĐ 1227; danh sách còn dùng PL11 QĐ 7603; XML4 lấy mã từ đâu | Báo cáo ánh xạ, mẫu XML4 | Bắt buộc |
| CLS-A08 | R08 | Kết quả XN gửi ngoài có cờ cơ sở thực hiện trên phiếu và trong dữ liệu không? | Phiếu in, bản ghi DB | Nên |
| CLS-A09 | R09 | Có hồ sơ QC nội kiểm (2 mức cho định lượng), sự cố và khắc phục, người duyệt; truy được theo máy và ngày | Báo cáo QC, Levey-Jennings | Bắt buộc |
| CLS-A10 | R10 | Có lưu kết quả EQA/so sánh liên phòng theo đợt không? Tài liệu nội bộ có còn ghi "ngoại kiểm bắt buộc theo TT 01/2013" không? | Hồ sơ EQA, SOP | Nên |
| CLS-A11 | R11 | Đặt QC "không đạt" cho một xét nghiệm trên một máy: phần mềm có chặn phát hành kết quả người bệnh không? Ghi đè có log lý do không? | Ảnh màn hình, log | Nên |
| CLS-A12 | R12 | So phiếu kết quả XN với 16 mục 8.21 QĐ 2429 (a–p); kiểm tra định danh người bệnh và "trang x/y" trên mọi trang | Bảng so khớp, bản in | Nên |
| CLS-A13 | R13 | Danh sách người được ủy quyền ký duyệt theo nhóm XN; phân biệt sơ bộ/chính thức; thử giá trị nguy kịch: có cảnh báo, có xác nhận đã nhận, có leo thang không | Cấu hình, log cảnh báo | Nên |
| CLS-A14 | R14 | Sửa một kết quả đã phát hành: bản gốc còn không? Có nhãn "đã sửa", lý do, người sửa, thông báo người chỉ định, đánh dấu cần gửi lại XML4 không? | Lịch sử phiên bản, log | Bắt buộc |
| CLS-A15 | R15 | Báo cáo TAT theo từng giai đoạn; mốc lấy mẫu và nhận mẫu có được ghi thật hay mặc định bằng giờ chỉ định | Báo cáo, SQL phân bố | Bắt buộc? |
| CLS-A16 | R16 | Ma trận vai trò nhập/sửa/duyệt/phát hành; log trục trặc hệ thống; quy trình vận hành khi LIS ngừng | Ma trận quyền, SOP dự phòng | Nên |
| CLS-A17 | R17, R21 | Đối chiếu tiêu chí 62–89 TT 54: interface máy XN, HIS ↔ LIS hai chiều, worklist, HL7, viewer ngoài khoa CĐHA | Bảng tự đánh giá TT 54 | Nên |
| CLS-A18 | R18 | SQL: kết quả CLS và study ảnh có `retention_class`/`retain_until` kế thừa HSBA không? Có job xóa ảnh theo thời gian cố định (vd 5 năm) bất kể HSBA không? | Truy vấn, cấu hình PACS | Bắt buộc / Bắt buộc? |
| CLS-A19 | R20 | Cơ sở có quyết định giá CĐHA dùng PACS chưa? Phần mềm có hai biến thể giá, chọn theo cách trả kết quả thực tế không? Có bằng chứng người bệnh nhận ảnh điện tử không? | QĐ giá, cấu hình DVKT, log cổng | Bắt buộc? |
| CLS-A20 | R22 | Chỉ định CT cho nữ 15–49 tuổi: có hỏi/ghi tình trạng thai không, có hiện lịch sử chụp không; RIS có lưu thông số liều do máy xuất không | Ảnh màn hình, mẫu dữ liệu | Nên |
| CLS-A21 | R23, R27 | Yêu cầu vendor cung cấp tài liệu intended use và đánh giá TBYT từng module; rà UI, brochure tìm từ "chẩn đoán", "AI phát hiện" ở module không có số lưu hành | Tài liệu đánh giá, ảnh UI, brochure | Bắt buộc |
| CLS-A22 | R24 | Với module là TBYT: tra số lưu hành trên Cổng TBYT của BYT; có bản kết quả phân loại; HDSD tiếng Việt; thông tin bảo hành | Số lưu hành, bản phân loại, HDSD | Bắt buộc |
| CLS-A23 | R25 | Sổ TBYT của cơ sở có liệt kê phần mềm là TBYT (AI/CAD) kèm số lưu hành, phiên bản không? Có kênh báo lỗi TBYT không? | Sổ tài sản, quy trình báo lỗi | Bắt buộc |
| CLS-A24 | R26 | Xem quy trình phát hành của vendor: có phân loại thay đổi, hạn thông báo 5/10 ngày làm việc, danh sách cơ sở theo phiên bản không | SOP phát hành, release log | Bắt buộc (nếu là TBYT) |

---

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái | Nội dung | Ai phải làm | Nguồn |
|---|---|---|---|---|
| 15/03/2013 | đã qua | TT 01/2013 có HL: kế hoạch QLCL, nội kiểm, bộ chỉ số | Cơ sở có PXN | TT-01-2013 |
| 16/11/2015 → 30/12/2019 | đã qua | Thí điểm PACS không in phim (QĐ 4868) | 17 BV thí điểm | QD-4868-2015 (thứ cấp) |
| 12/06/2017 | đã qua | Tiêu chí mức chất lượng PXN (QĐ 2429) | PXN | QD-2429-2017 |
| 26/02/2018 | đã qua | TT 54/2017 (tiêu chí CNTT, LIS, RIS-PACS) | Cơ sở KCB tự đánh giá | TT-54-2017 |
| 05/10/2020 | đã qua | CV 5319: thanh toán CĐHA dùng PACS theo giá có in phim (cơ sở thí điểm) | Cơ sở thí điểm | CV-5319-2020 (thứ cấp) |
| 01/01/2022 | đã qua | NĐ 98/2021 và TT 05/2022 (phân loại) có HL | Vendor phần mềm là TBYT | ND-98-2021 |
| 01/01/2024 | đã qua | Bắt buộc hồ sơ CSDT khi cấp mới số lưu hành; Luật KCB Đ113 có HL | Chủ sở hữu TBYT; cơ sở KCB | ND-98 Đ76 k5; L-KCB-2023 |
| 11/04/2025 | đã qua | Mã chỉ số CLS dùng chung đợt 1 (QĐ 1227) | Mọi cơ sở KCB, vendor | QD-1227-2025 |
| 01/07/2025 | đã qua | TT 33/2025 thời hạn lưu trữ | Mọi cơ sở | TT-33-2025 |
| 01/01/2026 | đã qua | TT 59/2025/TT-BKHCN an toàn bức xạ (thay TTLT 13/2014) | Cơ sở có công việc bức xạ | TT-59-2025-BKHCN |
| 29/01/2026 | đã qua | Giá CĐHA dùng PACS đầu tiên (BV Bạch Mai) | BV Bạch Mai | QD-313-2026 (thứ cấp) |
| 01/07/2026 | đã qua | TT 24/2026 có HL (thay TT 59/2025/TT-BYT); TT 25/2026 Đ2, Đ3 | Chủ sở hữu TBYT | TT-24-2026, TT-25-2026 |
| 28/07/2026 – 03/08/2026 | đã qua | CV đôn đốc xây giá CĐHA dùng PACS | Mọi cơ sở, Sở Y tế | thứ cấp |
| 15/08/2026 | đã qua | TT 25/2026 Đ1: ngoại kiểm thành "khuyến khích" | Cơ sở có PXN | TT-25-2026 |
| 18/08/2026 | đã qua | NĐ 313/2026 có HL (thay NĐ 42/2025) | BYT | ND-313-2026 |
| 24/08/2026 | đã qua | Dự thảo TT liên thông CLS bản 441 kỹ thuật | — | DT-CLS-LT |
| ~10/2026 | [?] | BYT dự kiến ban hành TT liên thông CLS | BYT | thanhnien 18/09/2026 |
| **01/01/2027** | [TỚI] | **Liên thông, sử dụng kết quả CLS giữa cơ sở KCB BHYT** | Mọi cơ sở KCB BHYT có CLS; vendor HIS/LIS/RIS/PACS | L-BHYT-SD-2024 Đ3 k4 |
| 30/06/2027; 01/01/2028 | [TỚI] | Kiểm định 6 loại TBYT phần cứng (không áp cho phần mềm) | Cơ sở có máy thở, máy gây mê kèm thở, dao mổ điện, lồng ấp, máy phá rung, máy thận nhân tạo | TT-24-2026 Đ3 |
| 01/09/2027 | [TỚI] | AI y tế thuộc danh mục rủi ro cao phải tuân thủ (xem K10) | Vendor AI | QD-33-2026-TTg (inventory) |

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuỗi thay thế**

| Cũ | → | Mới | Từ ngày | Ghi chú |
|---|---|---|---|---|
| NĐ 42/2025/NĐ-CP (chức năng BYT) | → | NĐ 313/2026/NĐ-CP | 18/08/2026 | Văn bản ban hành trước ngày này (QĐ 1227, TT 24, TT 25, TT 33) dẫn căn cứ NĐ 42/2025: vẫn đúng tại thời điểm ký |
| TT 01/2013 Đ5 k5 ("tham gia ngoại kiểm") | → | TT 25/2026 Đ1 ("khuyến khích tham gia") | 15/08/2026 | Sửa một khoản, không thay cả thông tư |
| TTLT 13/2014/TTLT-BKHCN-BYT; TT 13/2018/TT-BKHCN; TT 19/2012/TT-BKHCN | → | TT 59/2025/TT-BKHCN | 01/01/2026 | Căn cứ: Luật Năng lượng nguyên tử 94/2025/QH15, NĐ 332/2025 |
| TT 59/2025/TT-BYT (sửa TT 05/2022) | → | TT 24/2026/TT-BYT | 01/07/2026 | |
| TT 39/2016/TT-BYT (phân loại TTBYT); TT 46/2017/TT-BYT; TT 33/2020/TT-BYT | → | TT 05/2022/TT-BYT | 01/01/2022 (TT 05 Đ7 k4) | |
| NĐ 36/2016/NĐ-CP | → | NĐ 98/2021/NĐ-CP | 01/01/2022 | |
| "Trang thiết bị y tế" | → | "Thiết bị y tế" | 01/01/2024 | Đổi thuật ngữ theo NĐ 96/2023 Đ147 k7 |
| TT 53/2017/TT-BYT (thời hạn bảo quản) | → | TT 33/2025/TT-BYT | 01/07/2025 | |
| Thí điểm PACS (QĐ 4868/2015, CV 5319/2020: giá có in phim) | → | Giá riêng "CĐHA dùng PACS" theo TT 21/2024 (QĐ 313/2026 cho Bạch Mai; các cơ sở khác chờ phê duyệt) | 2026 | Thứ cấp |
| DT-CLS-LT bản 11/2025 (~1.114 kỹ thuật, 6 PL, DICOM) | → | DT-CLS-LT bản 08/2026 (441 kỹ thuật, 4 nhóm) | — | Cả hai đều là dự thảo |

**Bẫy trích dẫn**

1. **Ba văn bản cùng số "59"**: TT 59/2025/**TT-BYT** (sửa TT 05/2022 về TBYT, **hết HL 01/07/2026**); TT 59/2025/**TT-BKHCN** (an toàn bức xạ, **còn HL** từ 01/01/2026); TT 59/2026/TT-BKHCN (bãi bỏ TT 41/2017/TT-BTTTT, cụm EMR). Luôn ghi đủ hậu tố cơ quan.
2. "Luật 51 Đ3 k4 giao Chính phủ quy định" **không có nghị định riêng**; đừng trích NĐ 188/2025 cho nội dung liên thông CLS. Căn cứ thẩm quyền chi tiết là Luật BHYT Đ6 k3 (sửa bởi Luật 51 Đ1 k3 b) và NĐ 313/2026 Đ2 k14 c.
3. **"Ngoại kiểm bắt buộc"**: sai từ 15/08/2026 (TT 25/2026 Đ1). Nhưng QĐ 2429 vẫn để EQA là tiêu chí (*) khi xếp mức.
4. **"TT 33/2025 quy định lưu ảnh DICOM X năm"**: không có dòng nào như vậy. Kết quả CLS theo HSBA; ảnh gốc phải tự xếp "nhóm tương đương".
5. **"BYT bắt buộc DICOM"**: chưa có VBQPPL. TT 54 chỉ là tiêu chí xếp mức; DICOM trong dự thảo liên thông (bản 11/2025) là dự thảo.
6. **Con số 441 / ~1.100 kỹ thuật và các thời hạn giá trị** chỉ đến từ báo về dự thảo. Không nạp làm tham số chính thức.
7. **Hiệu lực dự kiến 01/07/2026** của DT-CLS-LT (MT-26) đã lỡ; thông tư chưa ban hành đến 05/10/2026.
8. **QĐ 1227/2025** có 1.240 chỉ số **điện quang**, không chỉ xét nghiệm. "Đợt 2" thuộc danh mục **thuật ngữ y học lâm sàng** (QĐ 2493/2025) chứ không phải chỉ số CLS: đừng nhầm.
9. **NĐ 98 Đ3 k8 a** miễn cho "phần mềm sử dụng cho thiết bị y tế", **không** miễn cho mọi phần mềm y tế. Phần mềm độc lập có mục đích chẩn đoán vẫn có thể là TBYT theo Đ2 k1.
10. **NĐ 04/2025** chỉ sửa Đ76 (chuyển tiếp nhập khẩu, IVD); đừng trích nó cho phân loại phần mềm. MT-27: danh sách sửa đổi đúng là NĐ 07/2023, NĐ 96/2023 (đổi thuật ngữ), NĐ 85/2024 (giá), NĐ 04/2025 (theo VBHN sao y của BYT 26/03/2025). Số VBHN: inventory ghi "08/VBHN-BYT 2026" (chưa xác minh); bản đang đăng trên Cục HT&TBYT có tên tệp "VB05_NDQLTBYT".
11. **Lộ trình kiểm định 30/06/2027 / 01/01/2028** (TT 24/2026) chỉ cho 6 thiết bị phần cứng ở TT 05 Đ5. Không liên quan phần mềm.
12. Tiêu chí TT 54 về PACS–HIS dùng **JPEG** để "hoàn thiện HSBA" là thiết kế năm 2017; không dùng làm chuẩn lưu trữ cho liên thông ảnh gốc.

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Toàn văn DT-CLS-LT** (cả hai bản): chưa tìm được trên cổng BYT hoặc Cổng Chính phủ. Cần: định dạng trao đổi dữ liệu xét nghiệm; DICOM có còn trong bản 08/2026 không; danh mục và thời hạn từng dịch vụ; ai lưu ảnh và cung cấp ảnh cho cơ sở nhận; trách nhiệm khi kết quả liên thông sai; thanh toán BHYT cho dịch vụ làm lại. **Hỏi BYT (Vụ BHYT, Cục QLKCB).**
2. **Nếu đến 01/01/2027 chưa có thông tư** thì Luật 51 Đ3 k4 áp dụng thế nào (nghĩa vụ trực tiếp hay chờ hướng dẫn). **Cần luật sư.**
3. **Phần mềm độc lập có phải TBYT**: NĐ 98 Đ2 k1 và Đ3 k8 a cùng PL I TT 05/2022 không cho câu trả lời rõ cho PACS viewer có chức năng đo, dựng 3D; CAD/AI đọc ảnh; LIS autoverification; CDSS tính liều. Cần: văn bản trả lời của **Cục Hạ tầng và Thiết bị y tế** hoặc tra số lưu hành của các sản phẩm tương tự trên Cổng TBYT; quan điểm chính thức về việc phần mềm có là "TBYT chủ động" khi áp quy tắc 9–12. **Cần luật sư + hỏi Cục HT&TBYT.**
4. **Phụ lục QĐ 1227/2025**: cấu trúc cột (mã, tên, đơn vị, phương pháp, ánh xạ LOINC/DICOM code?) chưa đọc bản gốc.
5. **QĐ 313/QĐ-BYT (2026) và CV đôn đốc giá PACS**: bản gốc, số hiệu CV (kết quả tìm kiếm ghi 5586/BYT-BH ngày 28/07/2026), điều kiện kỹ thuật PACS để được áp giá (thời gian lưu ảnh, cách giao ảnh cho người bệnh).
6. **TT 32/2023 PL XXIX**: có mẫu phiếu kết quả xét nghiệm, phiếu kết quả CĐHA bắt buộc không, và gồm những trường nào (chưa đọc PL XXIX).
7. **Thời hạn lưu ảnh gốc DICOM và kết quả CLS ngoại trú không lập HSBA**: TT 33/2025 không quy định. **Hỏi BYT (Văn phòng Bộ, đơn vị soạn TT 33).**
8. **TT 59/2025/TT-BKHCN Phụ lục 2 Mục 2** (mức liều tham chiếu chẩn đoán) và có nghĩa vụ ghi nhận liều từng người bệnh không: chưa đọc phụ lục.
9. **NĐ 98 Đ33–Đ37** (hồ sơ sau bán hàng, cảnh báo, sự cố, thu hồi) và **Đ26, Đ30** (thành phần hồ sơ công bố, đăng ký) áp cho phần mềm thế nào: mới đọc tiêu đề.
10. **Trạng thái QĐ 2429/2017** (ghi "áp dụng thí điểm 2017–2018" theo tóm tắt luatvietnam): còn được dùng chính thức làm thước đo xếp mức không, hay đã có bộ tiêu chí mới. Dự thảo liên thông dùng "mức chất lượng" nào thì cần toàn văn dự thảo.
11. **QĐ 2146/2026 (khung kiến trúc số)**: có quy định DICOM/DICOMweb, HL7 FHIR cho trao đổi kết quả CLS không (MT-24, cụm K6).
12. **Số hiệu VBHN của NĐ 98**: inventory ghi 08/VBHN-BYT 2026 (chưa xác minh); bản đã đọc là sao y ngày 26/03/2025 trên trang Cục HT&TBYT.
