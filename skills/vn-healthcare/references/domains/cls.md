# CLS — Cận lâm sàng liên thông, LIS, RIS/PACS và phần mềm là thiết bị y tế

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám có xét nghiệm/CĐHA (đặc biệt cơ sở KCB BHYT), vendor HIS/LIS/RIS/PACS, vendor phần mềm có chức năng y tế (AI, CAD, tính liều) · Research gốc: `research/deep/CLS.md`

Phạm vi: liên thông và dùng lại kết quả CLS giữa cơ sở KCB BHYT từ 01/01/2027 (luật, văn bản giao thẩm quyền, dự thảo thông tư); quản lý chất lượng xét nghiệm (TT 01/2013 sửa bởi TT 25/2026, QĐ 2429/2017) và hệ quả với LIS; phiếu kết quả, ký duyệt, sửa kết quả, TAT; RIS/PACS: thời hạn lưu, DICOM, trả kết quả không in phim và giá BHYT; an toàn bức xạ; phần mềm là thiết bị y tế (NĐ 98/2021, TT 05/2022 sửa bởi TT 24/2026, chế tài NĐ 90/2026).
Không lặp: mã chỉ số CLS QĐ 1227, chuẩn HL7/FHIR/DICOM trong QĐ 2146 → MA-LT (R16, R20, R21). XML4, mã DVKT → BHYT-DATA. Chuyển mẫu làm DVCLS (NĐ 188 Đ44) → BHYT-GD-R13. Ký số, lưu trữ HSBA → EMR. Dữ liệu HIV, dữ liệu nhạy cảm → DLCN. Sao lưu, cấp độ HTTT → ANM. AI rủi ro cao → TELE-R22, TELE-R27. Không phải ý kiến pháp lý.

## Tóm tắt nhanh

- **Hạn gần nhất: 01/01/2027** — Luật 51/2024 Đ3 k4 buộc liên thông, sử dụng kết quả CLS giữa cơ sở KCB BHYT. Thông tư chi tiết **chưa ban hành** đến 05/10/2026 (hai bản dự thảo 11/2025 và 08/2026; báo nêu dự kiến ban hành 10/2026). Phần mềm phải sẵn adapter vì định dạng trao đổi chưa được quy định (CLS-R01).
- Thiếu **thời điểm lấy mẫu / thời điểm thực hiện kỹ thuật** là lỗi dữ liệu nặng nhất: dự thảo tính thời hạn giá trị từ mốc này; TT 32/2023 Đ52 đã buộc ghi thời gian và người ghi (CLS-R02).
- Thời hạn giá trị (vd hóa sinh 24 giờ–60 ngày) và danh mục 441 kỹ thuật chỉ đến từ báo về dự thảo: làm **bảng cấu hình có phiên bản**, không hard-code (CLS-R03).
- **Ngoại kiểm không còn bắt buộc từ 15/08/2026** (TT 25/2026 Đ1); nội kiểm vẫn bắt buộc (CLS-R09, R10).
- **TT 33/2025 không có dòng riêng cho ảnh DICOM**: kết quả CLS kế thừa thời hạn HSBA (10/20/30 năm); ảnh gốc phải tự xếp nhóm tương đương (CLS-R18).
- **DICOM chưa bắt buộc bằng VBQPPL**; QĐ 2146 chỉ nêu DICOM 3.0 trong lộ trình đến 2030 cho đơn vị trực thuộc BYT (CLS-R19, xem MA-LT-R20).
- **SaMD**: NĐ 98 Đ3 k8 a chỉ miễn cho "phần mềm sử dụng cho" một TBYT, không miễn mọi phần mềm y tế. AI/CAD đọc ảnh, tính liều có rủi ro là TBYT độc lập; cơ sở dùng TBYT không số lưu hành bị phạt (CLS-R23, R25).

## Mục lục

| ID | Tiêu đề |
|---|---|
| CLS-R01 | Mốc 01/01/2027 liên thông kết quả CLS |
| CLS-R02 | Kết quả CLS mang đủ định danh, thời điểm, người thực hiện |
| CLS-R03 | Thời hạn giá trị và cảnh báo chỉ định trùng lặp |
| CLS-R04 | Công nhận kết quả theo mức chất lượng PXN |
| CLS-R05 | Liên thông CĐHA gồm ảnh, toàn vẹn, DICOM |
| CLS-R06 | Bác sĩ quyết định dùng lại hay làm lại, ghi lý do |
| CLS-R07 | Dùng mã chỉ số CLS QĐ 1227 trong LIS/RIS |
| CLS-R08 | Kết quả xét nghiệm gửi ngoài cơ sở |
| CLS-R09 | Nội kiểm có ghi chép, lưu trữ, sự cố |
| CLS-R10 | Ngoại kiểm thành khuyến khích |
| CLS-R11 | Chặn trả kết quả khi nội kiểm không đạt |
| CLS-R12 | Nội dung tối thiểu phiếu kết quả xét nghiệm |
| CLS-R13 | Ký duyệt, kết quả tạm, giá trị nguy kịch |
| CLS-R14 | Sửa kết quả sau phát hành |
| CLS-R15 | TAT theo từng giai đoạn |
| CLS-R16 | Quản lý thông tin PXN |
| CLS-R17 | Kết nối HIS ↔ LIS ↔ máy xét nghiệm (TT 54) |
| CLS-R18 | Thời hạn lưu kết quả CLS và ảnh |
| CLS-R19 | DICOM chưa có VBQPPL bắt buộc |
| CLS-R20 | Trả ảnh không in phim và giá BHYT |
| CLS-R21 | Giao diện RIS ↔ HIS ↔ PACS (TT 54) |
| CLS-R22 | An toàn bức xạ: thông tin cho chỉ định |
| CLS-R23 | Xác định phần mềm có là TBYT |
| CLS-R24 | TBYT độc lập: phân loại, số lưu hành |
| CLS-R25 | Cơ sở chỉ dùng TBYT có số lưu hành |
| CLS-R26 | Sau bán hàng: thay đổi, truy xuất, cảnh báo |
| CLS-R27 | Thiết kế ranh giới để HIS/LIS/PACS không thành TBYT |
| CLS-P01…P10 | Pattern: kho kết quả, bảng thời hạn, sổ năng lực chất lượng, gói liên thông, vòng đời mẫu có cổng QC, QC, PACS phân tầng, giá PACS, sổ intended use, phát hành phân loại thay đổi |
| CLS-A01…A24 | Checklist audit |

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 51/2024/QH15 (27/11/2024) | Luật sửa Luật BHYT: Đ3 k4 (mốc liên thông CLS), Đ1 k3 b (sửa Đ6 k3: BYT ban hành quy định liên thông CLS) | 01/07/2025; Đ3 k4 chậm nhất 01/01/2027 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat51.pdf) |
| 313/2026/NĐ-CP (08/08/2026) | Chức năng, nhiệm vụ BYT: Đ2 k14 c (quy định liên thông CLS, mã danh mục dùng chung, chuẩn dữ liệu) | 18/08/2026 | Còn HL; thay NĐ 42/2025 | gốc | [PDF](https://vnpa.moh.gov.vn/wp-content/uploads/2026/08/NGHI-DINH-313_2026_ND-CP_08082026_1-signed.pdf) |
| Dự thảo TT danh mục và điều kiện sử dụng kết quả CLS liên thông | Bản 11/2025 (~1.114 kỹ thuật, 6 phụ lục) và bản 08/2026 (441 kỹ thuật) | Báo nêu dự kiến 01/07/2026 (đã lỡ), nay dự kiến ban hành 10/2026 | **Dự thảo, chưa ban hành** đến 05/10/2026; chưa tìm được toàn văn | thứ cấp | [baochinhphu 18/11/2025](https://baochinhphu.vn/nguyen-tac-su-dung-ket-qua-xet-nghiem-khi-lien-thong-ket-qua-giua-cac-co-so-kham-chua-benh-10225111816281683.htm) (báo, bối cảnh, bản 11/2025) · [suckhoedoisong 25/08/2026](https://suckhoedoisong.vn/bo-y-te-de-xuat-441-xet-nghiem-dien-quang-co-the-dung-lai-khi-chuyen-vien-169260825004553706.htm) (báo, bối cảnh, bản 08/2026) |
| 1227/QĐ-BYT (11/04/2025) | Mã dùng chung chỉ số CLS Đợt 1 (2.964 chỉ số, gồm 1.240 điện quang) | Từ ngày ký | Còn HL | xem MA-LT | xem MA-LT §1 |
| 01/2013/TT-BYT (11/01/2013) | Quản lý chất lượng xét nghiệm | 15/03/2013 | Còn HL; Đ5 k5 sửa bởi TT 25/2026 Đ1 | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/thong-tu-so-01-2013-tt-byt-1583.htm) |
| 25/2026/TT-BYT (30/06/2026) | Đ1 sửa TT 01/2013 Đ5 k5 (ngoại kiểm "khuyến khích"); Đ2 sửa TT 32/2023; Đ3 sửa TT 23/2024 | 15/08/2026; Đ2, Đ3 từ 01/07/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/25-byt.signed.pdf) |
| 2429/QĐ-BYT (12/06/2017) | Tiêu chí đánh giá mức chất lượng PXN y học (12 chương, 169 tiêu chí, 6 bậc) | Từ khi ký | Không phải VBQPPL; Cục QLKCB vẫn đăng kèm sổ tay (2021); chưa thấy văn bản thay | gốc | [PDF, kcb.vn](https://kcb.vn/upload/2005611/20210723/3d486c540e73ba776981b50506ad7526Tieu-chi-danh-gia-muc-chat-luong-phong-xet-nghiem_final.pdf) |
| 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ2 k17, Đ69, Đ77 k4, Đ113 (TBYT phải được phép lưu hành) | 01/01/2024 | Còn HL | gốc | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 32/2023/TT-BYT | Đ51 (mẫu HSBA, PL XXVIII–XXIX), Đ52 k2 (ghi chép) | 01/01/2024 | Còn HL (TT 25/2026 không sửa Chương X) | gốc | [PDF](https://bvbnd.vn/wp-content/uploads/2024/01/32-thongtuhuongdanluatkbcb31122023_91202410.pdf) |
| 33/2025/TT-BYT (01/07/2025) | Thời hạn lưu trữ hồ sơ ngành y tế | 01/07/2025 | Còn HL; thay TT 53/2017 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [PL](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| 54/2017/TT-BYT (29/12/2017) | Tiêu chí CNTT: nhóm IV RIS-PACS (TC 62–79), nhóm V LIS (80–89), PL II mức 1–7 | **27/02/2018** (Đ6, đã đối chiếu ảnh bản gốc) | Còn HL một phần (tiêu chí EMR hết HL 06/06/2025 theo TT 13/2025); khung tự đánh giá, không bắt đạt mức | gốc-OCR | [vbpl.vn](https://vbpl.vn/van-ban/chi-tiet/thong-tu-54-2017-tt-byt--128249) |
| 4868/QĐ-BYT (16/11/2015); CV 5319/BYT-KH-TC (05/10/2020) | Thí điểm CĐHA trên PACS không in phim (đến 30/12/2019); CV 5319: thanh toán theo giá có in phim | — | Hết thí điểm; CV 5319 là hướng dẫn chuyển tiếp | thứ cấp | [CV 5319, caselaw](https://caselaw.vn/van-ban-phap-luat/357365-cong-van-so-5319-byt-kh-tc-ngay-05-10-2020-cua-bo-y-te-ve-thuc-hien-thanh-toan-chi-phi-dich-vu-ky-thuat-thuc-hien-bang-he-thong-luu-tru-va-truyen-hinh-anh-pacs) |
| 313/QĐ-BYT (29/01/2026) + CV đôn đốc giá PACS (báo 03/08/2026; số hiệu chưa xác minh) | Giá CĐHA dùng PACS tại BV Bạch Mai (734 dịch vụ); CV đề nghị mọi cơ sở xây giá CĐHA dùng PACS theo TT 21/2024 | QĐ 313 từ khi ký | Còn HL | thứ cấp | [suckhoedoisong 03/08/2026](https://suckhoedoisong.vn/bo-y-te-don-doc-khan-truong-phe-duyet-gia-dich-vu-chan-doan-hinh-anh-su-dung-pacs-16926080313455106.htm) (báo, bối cảnh) |
| 59/2025/TT-BKHCN (31/12/2025) | An toàn bức xạ: Đ32 kiểm soát chiếu xạ y tế | 01/01/2026 | Còn HL; thay TTLT 13/2014/TTLT-BKHCN-BYT, TT 13/2018/TT-BKHCN | gốc-OCR | [mst.gov.vn](https://mst.gov.vn/van-ban-phap-luat/25309.htm) · [PDF](https://mic.mediacdn.vn/document/2026/1/17/59tt-17686411227721232332528.pdf) |
| 98/2021/NĐ-CP (sửa bởi NĐ 07/2023, NĐ 96/2023, NĐ 85/2024, NĐ 04/2025) | Quản lý TBYT: Đ2 k1 (TBYT gồm phần mềm), Đ3 k8 a (miễn cho phần mềm sử dụng cho TBYT), Đ4–Đ5, Đ8, Đ21–Đ23, Đ63–Đ65, Đ76 k5 | 01/01/2022 | Còn HL; NĐ 04/2025 chỉ sửa Đ76. Chưa có Luật TBYT (mới ở giai đoạn đề xuất) | gốc (Đ2 k1, Đ3 k8 đối chiếu ảnh) + gốc-OCR | [PDF gốc 2021](https://datafiles.chinhphu.vn/cpp/files/vbpq/2021/11/98.signed.pdf) · [Danh mục VB, Cục HT&TBYT](https://imda.moh.gov.vn/van-ban-phap-quy) · [Tờ trình dự thảo 15/06/2026](https://imda.moh.gov.vn/documents/10182/10030600/Duthaototrinh.15.06.2026/db844d21-f1d8-493e-914e-130b24ab9812) |
| 05/2022/TT-BYT (01/08/2022) | Chi tiết NĐ 98: PL I quy tắc phân loại (16 + 7 IVD, theo ASEAN); Đ5 danh mục kiểm định (6 thiết bị phần cứng) | 01/08/2022 | Còn HL; sửa bởi TT 24/2026 (TT 59/2025/TT-BYT hết HL 01/07/2026) | gốc-OCR | [PDF](https://imda.moh.gov.vn/documents/10182/10030594/05TT.signed_compress.pdf/35c913bf-b4cd-4b30-b97f-fe12ee9f5d0e) · [VBHN 04/VBHN-BYT, luatvietnam](https://luatvietnam.vn/y-te/van-ban-hop-nhat-04-vbhn-byt-2026-quy-dinh-chi-tiet-thi-hanh-nghi-dinh-98-2021-ve-quan-ly-thiet-bi-y-te-424617-d5.html) |
| 24/2026/TT-BYT (30/06/2026) | Đ2 rủi ro, biện pháp quản lý theo NĐ 98; Đ3 sửa lộ trình kiểm định TT 05 Đ8 | 01/07/2026 | Còn HL; thay TT 59/2025/TT-BYT | gốc | [VB 218703](https://vanban.chinhphu.vn/?pageid=27160&docid=218703) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/24-byt.signed.pdf) |
| 90/2026/NĐ-CP | Xử phạt VPHC y tế: Đ4 k5 (tổ chức ×2), Đ40 k1 (HSBA), Đ71, Đ73, Đ79 (TBYT) | 15/05/2026 | Còn HL; thay NĐ 117/2020 | gốc-OCR (chỉ diễn giải) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |

**Chế tài liên quan (NĐ 90/2026, gốc-OCR, diễn giải).** Mức trong Chương II là cho cá nhân; tổ chức ×2 (Đ4 k5).

| Hành vi | Điều khoản | Cá nhân | Tổ chức |
|---|---|---|---|
| Lưu hành TBYT chưa có số lưu hành / giấy phép nhập khẩu | Đ73 k4 a | 80–100 tr | 160–200 tr |
| Không phân loại, không công bố kết quả phân loại lên Cổng BYT | Đ71 k1 | 25–50 tr | 50–100 tr |
| Không thông báo thay đổi, cập nhật hồ sơ công bố (5 ngày làm việc) / đăng ký lưu hành (10 ngày làm việc) | Đ73 k1 d, đ | 20–40 tr | 40–80 tr |
| Không có HDSD tiếng Việt; lưu hành khi cơ sở sản xuất chưa công bố đủ điều kiện | Đ73 k1 b, g | 20–40 tr | 40–80 tr |
| Không công bố lại (A, B) khi đổi chủ sở hữu, chủng loại, mục đích sử dụng, chỉ định | Đ73 k2 a | 40–60 tr | 80–120 tr |
| Không lập, duy trì hồ sơ theo dõi, truy xuất TBYT | Đ73 k2 b, g | 40–60 tr (khung k2, chưa đối chiếu từng điểm) | ×2 |
| Cơ sở y tế dùng TBYT không có số lưu hành | Đ79 k3 | 10–20 tr | 20–40 tr |
| Cơ sở y tế không lập, lưu hồ sơ TBYT; vận hành không theo hướng dẫn | Đ79 k2 | 3–5 tr | 6–10 tr |
| Cơ sở y tế không báo cáo TBYT có lỗi | Đ79 k1 | 0,5–1 tr | 1–2 tr |
| Không lập HSBA đủ mục theo mẫu; không lưu hồ sơ, bệnh án | Đ40 k1 a, b | 1–3 tr | 2–6 tr |

## 2. Yêu cầu

### A. Liên thông và sử dụng lại kết quả CLS

### CLS-R01 — Mốc 01/01/2027 liên thông và sử dụng kết quả CLS giữa cơ sở KCB BHYT
- **Căn cứ**: Luật 51/2024 Đ3 k4: "Chậm nhất là ngày 01 tháng 01 năm 2027, thực hiện liên thông, sử dụng kết quả cận lâm sàng liên thông giữa các cơ sở khám bệnh, chữa bệnh bảo hiểm y tế phù hợp với yêu cầu chuyên môn theo quy định của Chính phủ." Luật 51 Đ1 k3 b sửa Luật BHYT Đ6 k3: BYT ban hành quy định về liên thông và sử dụng kết quả CLS. NĐ 313/2026 Đ2 k14 c: BYT ban hành quy định liên thông CLS; cấp mã danh mục dùng chung, tiêu chuẩn, định dạng dữ liệu, kết nối trong lĩnh vực BHYT.
- **Áp dụng**: cơ sở KCB BHYT có CLS hoặc nhận người bệnh chuyển đến; vendor HIS/LIS/RIS/PACS · **Hiệu lực/hạn**: **01/01/2027**.
- **Mức**: BẮT BUỘC? (mốc luật định, nhưng thông tư chi tiết chưa ban hành; NĐ 188/2025 không có điều nào về nội dung này, xem BHYT-GD-R14).
- **Phần mềm phải**: trước 01/01/2027 có khả năng (1) xuất kết quả CLS của cơ sở theo gói có cấu trúc (R02, R05); (2) nhận, hiển thị kết quả CLS cơ sở khác kèm nguồn gốc; (3) hỗ trợ bác sĩ quyết định dùng lại hay làm lại (R03, R06). Có lớp adapter vì định dạng trao đổi chưa được quy định (suy luận).
- **Bẫy**: "theo quy định của Chính phủ" chưa có nghị định riêng; thẩm quyền chi tiết giao cho BYT (Luật BHYT Đ6 k3 sửa đổi; NĐ 313 Đ2 k14 c), công cụ thực tế là thông tư BYT. Nếu đến 01/01/2027 thông tư chưa có hiệu lực: cần luật sư/hỏi BYT (mục 7). Nghĩa vụ phía XML, thanh toán: BHYT-GD-R14.

### CLS-R02 — Kết quả CLS mang đủ định danh, thời điểm, người thực hiện, người kết luận, cơ sở thực hiện
- **Căn cứ**: TT 32/2023 Đ52 k2 d: "Thông tin trong hồ sơ bệnh án cần thể hiện rõ thời gian và người ghi chép." Đ52 k2 c: không dùng viết tắt trong tài liệu bàn giao cho cơ sở khác. Luật KCB Đ2 k17 (HSBA gồm kết quả CLS), Đ77 k4. Dự thảo bản 08/2026 (báo, bối cảnh): kết quả phải đủ nhân dạng người bệnh, thời gian lấy mẫu, người lấy mẫu, người ký xác nhận; thời hạn giá trị tính từ thời điểm lấy mẫu (xét nghiệm) hoặc thực hiện kỹ thuật (điện quang). Dự thảo bản 11/2025 (báo, bối cảnh): kết quả CĐHA có giá trị pháp lý khi làm tại cơ sở có phép, ký bởi người thực hiện và bác sĩ đọc, hoặc xác thực điện tử. QĐ 2429 tiêu chí 8.21 (CLS-R12).
- **Áp dụng**: mọi cơ sở KCB (TT 32); liên thông: cơ sở BHYT · **Hiệu lực/hạn**: TT 32 từ 01/01/2024; dự thảo chưa có.
- **Mức**:
  - BẮT BUỘC — thời gian và người ghi (TT 32 Đ52).
  - BẮT BUỘC? — bộ trường liên thông (dự thảo).
- **Phần mềm phải**: mỗi kết quả lưu tối thiểu: định danh người bệnh (số định danh cá nhân, xem EMR-R05; mã BN; mã thẻ BHYT nếu có), mã cơ sở thực hiện, mã DVKT dùng chung, mã chỉ số QĐ 1227, **thời điểm lấy mẫu** hoặc **thời điểm thực hiện** (bắt buộc, có múi giờ), thời điểm nhận mẫu, duyệt, phát hành, người thực hiện, người đọc/kết luận, người duyệt, phương pháp/thiết bị, loại mẫu, trạng thái (sơ bộ/chính thức/đã sửa). Không phát hành khi thiếu các trường này. Bản gửi cơ sở khác không dùng viết tắt nội bộ.
- **Bẫy**: nhiều HIS chỉ lưu "ngày chỉ định" và "ngày kết quả" → không tính được thời hạn giá trị. Trường của XML4 không đủ cho liên thông lâm sàng (suy luận).

### CLS-R03 — Thời hạn giá trị theo từng dịch vụ và cảnh báo chỉ định trùng lặp
- **Căn cứ**: dự thảo bản 08/2026 (báo, bối cảnh): 441 kỹ thuật: 367 điện quang (X-quang, CT, MRI), 26 vi sinh – ký sinh trùng (48 giờ–30 ngày, chỉ kết quả dương tính), 27 huyết học – truyền máu (24 giờ–7 ngày), 21 hóa sinh (24 giờ–60 ngày; theo báo: HbA1c 60 ngày, urê, bilirubin tối đa 24 giờ). TT 59/2025/TT-BKHCN Đ32 k1 đ (gốc-OCR, diễn giải): bác sĩ tham khảo các lần khám trước để tránh kiểm tra bổ sung không cần thiết.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: khi thông tư ban hành; Đ32 TT 59/2025/TT-BKHCN đã HL từ 01/01/2026.
- **Mức**: BẮT BUỘC? (dự thảo; con số có thể đổi).
- **Phần mềm phải**: bảng tham số có phiên bản, ngày hiệu lực: `mã dịch vụ/chỉ số → thời hạn (giờ) → điều kiện (vd chỉ dương tính) → căn cứ`; khi chỉ định, tra kết quả cùng loại còn hạn (của cơ sở và nhận liên thông) và cảnh báo trùng lặp; điện quang hiển thị lịch sử chụp.
- **Bẫy**: bản 11/2025 có 6 phụ lục (gồm di truyền – sinh học phân tử, giải phẫu bệnh, điện quang 893), bản 08/2026 còn 4 nhóm; một số Sở Y tế đề nghị khớp thời hạn với quy định thanh toán BHYT (báo) → không nạp cứng.

### CLS-R04 — Công nhận kết quả theo mức chất lượng phòng xét nghiệm
- **Căn cứ**: dự thảo (báo, bối cảnh): công nhận lẫn nhau giữa PXN cùng mức chất lượng; PXN mức thấp công nhận kết quả PXN mức cao hơn; PXN đạt ISO 15189 liên thông theo phạm vi được công nhận (bản 11/2025); cơ sở công khai mức chất lượng. TT 01/2013 Đ4 k3: cơ sở KCB phải công khai công tác kiểm chuẩn xét nghiệm. QĐ 2429 phần I mục 8: 6 bậc (chưa xếp mức; mức 1: 20–<35% điểm; 2: 35–<65%; 3: 65–<85%; 4: 85–<95%; 5: ≥95%), mỗi mức phải đạt tiêu chí bắt buộc (*, ***); mục tiêu nêu rõ là căn cứ liên thông, công nhận kết quả.
- **Áp dụng**: PXN của cơ sở KCB; cơ sở nhận kết quả · **Hiệu lực/hạn**: TT 01/2013 Đ4 k3 đang HL; phần công nhận chờ thông tư.
- **Mức**:
  - BẮT BUỘC — công khai kiểm chuẩn (TT 01/2013 Đ4 k3).
  - BẮT BUỘC? — công nhận theo mức (dự thảo).
- **Phần mềm phải**: danh mục năng lực chất lượng theo cơ sở/PXN/phạm vi: mức QĐ 2429 (ngày, cơ quan đánh giá, hiệu lực), ISO 15189 (phạm vi, hạn); gắn vào kết quả khi gửi; phía nhận so mức nguồn với mức của mình và gợi ý "được công nhận / cần cân nhắc" (CLS-P03).
- **Bẫy**: CĐHA chưa có hệ thống đánh giá mức chất lượng tương đương (BYT nói sẽ xây riêng, theo báo). Không suy diễn "mức" cho điện quang.

### CLS-R05 — Liên thông kết quả CĐHA gồm ảnh, toàn vẹn, định dạng DICOM
- **Căn cứ**: dự thảo bản 08/2026 (báo, bối cảnh): dữ liệu CĐHA liên thông gồm kết luận và hình ảnh. Bản 11/2025 (báo, bối cảnh): ảnh nguyên vẹn, rõ, đủ chuỗi ảnh, định dạng DICOM kèm phần mềm đọc; có thể PACS–PACS; thông tin người bệnh trên ảnh khớp HSBA; cấm sửa, cắt xén ảnh. TT 54/2017 PL I TC 70 (cơ bản: hỗ trợ HL7, DICOM), 74 (cơ bản: xuất DICOM ra CD/DVD kèm viewer hoặc đường dẫn web), 78, 79 (nâng cao).
- **Áp dụng**: cơ sở có CĐHA, vendor RIS/PACS · **Hiệu lực/hạn**: chờ thông tư.
- **Mức**:
  - BẮT BUỘC? — khi thông tư ban hành (dự thảo).
  - NÊN — hiện tại (TT 54 chỉ là tiêu chí xếp mức).
- **Phần mềm phải**: lưu ảnh gốc DICOM (không chỉ JPEG); xuất trọn study kèm báo cáo đã ký; kênh PACS–PACS (C-STORE/C-MOVE hoặc DICOMweb STOW/WADO — lựa chọn kỹ thuật là suy luận); hash cho study gửi đi; đối chiếu định danh trong DICOM header với HSBA khi gửi và nhận; ghi ảnh nhận được là "ảnh ngoài cơ sở" (không ghi đè, không tính phí lại).
- **Bẫy**: DICOM có ở bản 11/2025, chưa thấy báo nêu lại ở bản 08/2026. Định dạng trao đổi kết quả xét nghiệm (HL7 v2/FHIR/XML) chưa thấy ở bản nào. Luồng TT 54 TC 68 "PACS chuyển DICOM sang JPEG cho RIS/HIS" không đủ cho liên thông ảnh gốc (suy luận).

### CLS-R06 — Bác sĩ quyết định dùng lại hay làm lại; ghi lý do
- **Căn cứ**: dự thảo (báo, bối cảnh): người hành nghề quyết định dùng kết quả liên thông hay chỉ định lại và chịu trách nhiệm; chỉ định lại phải ghi rõ lý do. Bản 11/2025: được chụp lại khi lâm sàng thay đổi, đã quá lâu, ảnh kém, nghi sai lệch thông tin người bệnh. Luật KCB Đ62 k2 a: người hành nghề chỉ định kịp thời, chính xác và chịu trách nhiệm.
- **Áp dụng**: cơ sở nhận người bệnh · **Hiệu lực/hạn**: chờ thông tư.
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: khi có cảnh báo trùng lặp (R03) mà vẫn chỉ định, bắt chọn lý do (lâm sàng thay đổi; quá hạn; chất lượng ảnh/mẫu không đạt; nghi sai định danh; PXN nguồn không đủ mức; khác + mô tả) lưu vào y lệnh; báo cáo tỷ lệ chỉ định lại có/không lý do.
- **Bẫy**: giám định BHYT có thể dùng lý do này để xét thanh toán dịch vụ lặp (suy luận).

### CLS-R07 — Dùng mã chỉ số CLS dùng chung (QĐ 1227/2025) trong LIS/RIS
- **Căn cứ**: xem MA-LT-R16 (QĐ 1227 Đ1, Đ2; QĐ 2010/2025 Đ3: XML4 dùng mã QĐ 1227, chỉ số chưa có thì tạm dùng PL11 QĐ 7603). NĐ 313/2026 Đ2 k14 c.
- **Áp dụng**: mọi cơ sở KCB; vendor LIS/RIS/HIS · **Hiệu lực/hạn**: 11/04/2025.
- **Mức**:
  - BẮT BUỘC — XML4 (cơ sở BHYT).
  - BẮT BUỘC? — dữ liệu nội bộ, EMR, liên thông.
- **Phần mềm phải**: chỉ số nội bộ (theo máy, PXN) ánh xạ 1-n sang mã QĐ 1227; lưu mã nội bộ, mã máy (LIS host code), mã dùng chung; cờ "chưa có mã 1227, đang dùng PL11 7603"; chặn gửi liên thông nếu chỉ số chưa ánh xạ (suy luận); đơn vị SI khi có thể (QĐ 2429 TC 8.21 i).
- **Bẫy**: QĐ 1227 gồm cả 1.240 chỉ số điện quang. "Đợt 2" thuộc thuật ngữ lâm sàng (QĐ 2493), không phải chỉ số CLS. Không có văn bản bắt dùng LOINC.

### CLS-R08 — Kết quả xét nghiệm gửi ngoài cơ sở (DVCLS chuyển)
- **Căn cứ**: NĐ 188/2025 Đ44 (chuyển người bệnh/mẫu làm DVCLS, Mẫu số 9) — chi tiết BHYT-GD-R13. QĐ 2429 TC 8.21 c: phiếu kết quả nhận dạng xét nghiệm do PXN chuyển gửi thực hiện.
- **Áp dụng**: cơ sở gửi, nhận mẫu · **Hiệu lực/hạn**: 01/07/2025.
- **Mức**:
  - BẮT BUỘC — phần thanh toán (NĐ 188, xem BHYT-GD-R13).
  - NÊN — đánh dấu trên phiếu (QĐ 2429).
- **Phần mềm phải**: LIS nhận kết quả PXN ngoài (nhập tay hoặc giao diện), gắn cờ "thực hiện tại [mã cơ sở]", giữ mức chất lượng của PXN ngoài (R04), in nhận dạng này trên phiếu.

### B. LIS và quản lý chất lượng xét nghiệm

### CLS-R09 — Nội kiểm có ghi chép, lưu trữ, phát hiện sự cố
- **Căn cứ**: TT 01/2013 Đ5 k4: "Xây dựng và thực hiện chương trình nội kiểm do lãnh đạo cơ sở khám bệnh, chữa bệnh phê duyệt, có hệ thống ghi chép, lưu trữ, phát hiện sự cố và biện pháp khắc phục, phòng ngừa sự cố." Đ6 k2 a (khuyến khích ứng dụng CNTT trong quản lý hồ sơ); Đ9 k4. QĐ 2429 TC 8.7–8.11 (*), 8.13.
- **Áp dụng**: cơ sở có PXN · **Hiệu lực/hạn**: từ 15/03/2013.
- **Mức**: BẮT BUỘC (có hồ sơ nội kiểm). Dùng phần mềm hay sổ giấy: không bắt buộc.
- **Phần mềm phải** (nếu LIS đảm nhận): kết quả QC theo máy, xét nghiệm, lô vật liệu; ít nhất 2 mức cho định lượng (TC 8.7), chứng âm/dương cho định tính (8.8); Levey-Jennings, Westgard (suy luận); sự cố QC, khắc phục, người duyệt; xem xét xu hướng (8.13).
- **Bẫy**: TT 25/2026 Đ1 chỉ sửa Đ5 k5 (ngoại kiểm), không thêm yêu cầu nào với LIS.

### CLS-R10 — Ngoại kiểm: từ bắt buộc thành khuyến khích (từ 15/08/2026)
- **Căn cứ**: TT 01/2013 Đ5 k5 bản gốc buộc tham gia ngoại kiểm; TT 25/2026 Đ1 sửa thành khuyến khích (HL 15/08/2026). QĐ 2429 TC 8.15 (*) vẫn coi EQA/so sánh liên phòng là tiêu chí bắt buộc để xếp mức.
- **Áp dụng**: cơ sở có PXN · **Hiệu lực/hạn**: 15/08/2026.
- **Mức**: NÊN (pháp lý). Thực tế cần để được xếp mức và do đó được công nhận khi liên thông (R04; suy luận).
- **Phần mềm phải**: lưu EQA theo chương trình, đợt, xét nghiệm, đạt/không đạt, khắc phục (8.15 c); xuất báo cáo cho đoàn đánh giá.
- **Bẫy**: câu "ngoại kiểm bắt buộc theo TT 01/2013" sai từ 15/08/2026.

### CLS-R11 — Chặn trả kết quả khi nội kiểm không đạt
- **Căn cứ**: QĐ 2429 TC 8.6 (PXN quy định tạm dừng trả kết quả nếu nội kiểm không đạt), 8.11 (*: nội kiểm đồng thời hoặc trước khi chạy mẫu người bệnh), 8.12 (***: QC không đạt thì khắc phục rồi mới chạy tiếp). TT 01/2013 Đ2 k5: nội kiểm để bảo đảm kết quả đủ tin cậy trước khi trả.
- **Áp dụng**: PXN muốn đạt mức chất lượng · **Hiệu lực/hạn**: từ 2017.
- **Mức**: NÊN (QĐ hành chính); tiêu chí *** bắt buộc để đạt mức 3 trở lên.
- **Phần mềm phải**: trạng thái QC theo (máy, xét nghiệm, ca); QC "không đạt" thì khóa duyệt và phát hành kết quả xét nghiệm đó trên máy đó đến khi có bản ghi khắc phục được duyệt; giữ lại kết quả chạy trong cửa sổ lỗi để chạy lại; log mọi lần ghi đè khóa.

### CLS-R12 — Phiếu trả kết quả xét nghiệm đủ nội dung tối thiểu
- **Căn cứ**: QĐ 2429 TC 8.21: (a) loại xét nghiệm, phương pháp/thiết bị; (b) PXN trả kết quả; (c) xét nghiệm chuyển gửi; (d) nhận biết người bệnh và địa chỉ trên mọi trang; (e) người yêu cầu; (f) ngày giờ nhận mẫu; (g) loại mẫu; (h) quy trình đo; (i) đơn vị SI khi có thể; (j) khoảng tham chiếu, giá trị quyết định lâm sàng; (k) diễn giải; (l) cảnh báo; (m) người xem xét và có thẩm quyền ban hành; (n) ngày ký duyệt, thời gian ban hành; (o) số trang/tổng; (p) khoảng trống phiên giải. TC 8.20. TT 32/2023 Đ51 k1 b: mẫu giấy, phiếu ở PL XXIX.
- **Áp dụng**: PXN · **Hiệu lực/hạn**: từ 2017.
- **Mức**: NÊN (QĐ 2429). Nếu PL XXIX TT 32 có mẫu phiếu kết quả xét nghiệm thì mẫu đó bắt buộc theo Đ51: chưa xác minh.
- **Phần mềm phải**: bản in và bản điện tử (PDF/A hoặc tài liệu ký số) đủ (a)–(p); header/footer lặp định danh và "trang x/y"; khoảng tham chiếu theo tuổi, giới; cờ H/L và cờ nguy kịch.

### CLS-R13 — Rà soát, ký duyệt, kết quả tạm thời, báo động giá trị nguy kịch
- **Căn cứ**: QĐ 2429 TC 3.5 (*: người ký duyệt đủ năng lực), 8.18 (***: quy trình rà soát trước khi trả, nêu người có thẩm quyền), 8.22 (ghi chú mẫu không đạt; thông báo kết quả báo động; kết quả tạm phải có báo cáo cuối; kết quả qua điện thoại/điện tử phải đến đúng người; báo miệng phải gửi văn bản sau và có hồ sơ). TT 01/2013 PL chỉ số 21 (trả kết quả vượt ngưỡng nguy kịch), 24. Ký số: EMR-R06, EMR-R07. Kết quả HIV dương tính: DLCN-R32.
- **Áp dụng**: PXN · **Hiệu lực/hạn**: từ 2013/2017.
- **Mức**: NÊN (QĐ 2429). Phần ký số HSBA và bảo mật HIV bắt buộc theo EMR, DLCN.
- **Phần mềm phải**: hai bước duyệt (kỹ thuật, y khoa) gắn danh sách người được ủy quyền theo nhóm xét nghiệm; tách "sơ bộ" và "chính thức", sơ bộ có nhãn rõ; quy tắc giá trị nguy kịch cấu hình được, cảnh báo có xác nhận đã nhận (người, thời điểm, kênh), leo thang khi quá giờ; nhật ký báo miệng.

### CLS-R14 — Sửa kết quả sau khi phát hành: giữ bản gốc, đánh dấu, thông báo
- **Căn cứ**: QĐ 2429 TC 8.23 (kết quả đã sửa nhận biết rõ, dẫn chiếu báo cáo ban đầu, khách hàng biết có sửa, hồ sơ sửa có thời gian, người chịu trách nhiệm), 8.24 (lưu kết quả ban đầu). NĐ 90/2026 (gốc-OCR, diễn giải) phạt tẩy xóa, sửa HSBA làm sai lệch thông tin (xem EMR-R10).
- **Áp dụng**: PXN, khoa CĐHA · **Hiệu lực/hạn**: đang HL.
- **Mức**:
  - BẮT BUỘC — không sửa làm sai lệch HSBA (kết quả CLS là một phần HSBA).
  - NÊN — quy trình chi tiết theo QĐ 2429.
- **Phần mềm phải**: kết quả đã phát hành bất biến; sửa bằng phiên bản mới trạng thái "đã sửa", lý do, người sửa, thời điểm, liên kết bản trước; tự thông báo người chỉ định; nếu đã gửi liên thông/XML4 thì đánh dấu cần gửi lại (BHYT-DATA-R06). Áp dụng tương tự cho báo cáo CĐHA (addendum).

### CLS-R15 — Thời gian quay vòng (TAT) đo được theo từng giai đoạn
- **Căn cứ**: TT 01/2013 Đ5 k6 a (bộ chỉ số chất lượng theo Phụ lục); PL mục I.2: đánh giá trước, trong, sau xét nghiệm; chỉ số tham khảo 6 (thời gian lấy mẫu), 17 (thời gian hoàn thành), 23 (thời gian trả kết quả), 11 (mẫu bị từ chối). QĐ 2429 phần I mục 3 g: thời gian trả kết quả tính từ khi nhận/lấy mẫu đến khi trả.
- **Áp dụng**: PXN · **Hiệu lực/hạn**: từ 2013.
- **Mức**: BẮT BUỘC? (bắt xây bộ chỉ số; Phụ lục ghi là danh mục tham khảo).
- **Phần mềm phải**: mốc thời gian chuẩn cho mỗi mẫu: chỉ định, lấy mẫu, nhận mẫu, bắt đầu chạy, có kết quả máy, duyệt kỹ thuật, duyệt y khoa, phát hành, người nhận xem; báo cáo TAT theo xét nghiệm, khoa, ca; tỷ lệ mẫu bị từ chối và lý do.

### CLS-R16 — Quản lý thông tin PXN: phân quyền, toàn vẹn, trục trặc, dự phòng
- **Căn cứ**: QĐ 2429 Chương IX: 9.1 (***: bảo mật), 9.2 (phân định người truy cập, nhập, sửa, ban hành), 9.3, 9.4 (toàn vẹn), 9.5 (hồ sơ trục trặc), 9.6 (kế hoạch dự phòng). Yêu cầu pháp lý tương ứng: ANM-R09, ANM-R13, DLCN-R01.
- **Áp dụng**: PXN · **Hiệu lực/hạn**: từ 2017.
- **Mức**: NÊN (QĐ 2429); phần ATTT, DLCN bắt buộc theo ANM, DLCN.
- **Phần mềm phải**: vai trò tách nhập / sửa / duyệt / phát hành; log sự cố hệ thống liên kết phiếu khắc phục; chế độ dự phòng (in phiếu, nhập lại có đối soát) khi LIS hoặc kết nối HIS ngừng.

### CLS-R17 — Kết nối HIS ↔ LIS và LIS ↔ máy xét nghiệm (tiêu chí TT 54)
- **Căn cứ**: TT 54/2017 PL I nhóm V. Cơ bản: 80 quản trị; 81 danh mục; 82 chỉ định; 83 kết quả; 84 kết nối máy xét nghiệm (ra lệnh, nhận kết quả tự động); 85 thống kê. Nâng cao: 86 quản lý mẫu; 87 hóa chất; 88 liên thông HIS; 89 cảnh báo vượt ngưỡng. PL II: mức 3 cần LIS đạt cơ bản; mức 4 cần LIS đạt đầy đủ.
- **Áp dụng**: cơ sở tự xác định mức (TT 54 Đ5) · **Hiệu lực/hạn**: 27/02/2018.
- **Mức**: NÊN (khung tự đánh giá).
- **Phần mềm phải**: driver/middleware máy xét nghiệm (ASTM/LIS2-A2, HL7 v2: chọn chuẩn là suy luận), mã vạch mẫu, đồng bộ hai chiều chỉ định–kết quả với HIS.
- **Bẫy**: TC 88 chỉ là "nâng cao" nhưng thực tế cần cho XML4 và HSBA điện tử (suy luận). Middleware có thể bị coi là TBYT: xem R23, R27.

### C. RIS/PACS: lưu trữ, định dạng, trả kết quả không in phim

### CLS-R18 — Thời hạn lưu kết quả CLS và ảnh CĐHA
- **Căn cứ**: Luật KCB Đ2 k17, Đ69 k2. TT 33/2025 PL: HSBA nội trú, ngoại trú 10 năm (dòng 44); tâm thần, TNLĐ, TNGT 20 năm (40); phẫu thuật thẩm mỹ 20 năm (43); tử vong 30 năm (39); sổ sách phục vụ KCB 5 năm (47). Hồ sơ ghép mô, tạng: TT 33 dòng 43 ghi 20 năm nhưng Luật 75/2006 (hiến, lấy, ghép mô, bộ phận cơ thể) quy định 30 năm → áp **30 năm** (mâu thuẫn giữa hai văn bản, giữ mức cao theo luật). TT 33 Đ1 k2 b: hồ sơ chưa quy định thì áp thời hạn tương đương, không thấp hơn mức trong phụ lục. Phụ lục **không có dòng riêng** cho phim, ảnh, DICOM, kết quả xét nghiệm rời.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025.
- **Mức**:
  - BẮT BUỘC — kết quả CLS và báo cáo CĐHA nằm trong HSBA (theo thời hạn HSBA, xem EMR-R22).
  - BẮT BUỘC? — ảnh gốc DICOM (phải tự xếp nhóm tương đương).
- **Phần mềm phải**: kết quả CLS và báo cáo CĐHA kế thừa loại lưu trữ của HSBA chứa nó (tự nâng 10 → 20 → 30 năm khi HSBA đổi loại); ảnh DICOM: chính sách lưu cấu hình theo loại HSBA, mặc định không ngắn hơn HSBA liên quan (phương án thận trọng, suy luận); lưu phân tầng; cấm xóa trước hạn; legal hold. Lượt ngoại trú không lập HSBA: thời hạn chưa xác minh (có thể "sổ, sách" 5 năm hoặc tương đương; hỏi BYT).
- **Bẫy**: đừng trích "TT 33 quy định lưu ảnh X năm". Nếu chỉ giữ JPEG chọn lọc (ý đồ TT 54 TC 68) thì không đáp ứng liên thông ảnh gốc (R05).

### CLS-R19 — DICOM: chưa có văn bản quy phạm bắt buộc
- **Căn cứ**: TT 54/2017 Đ2 k11 (định nghĩa DICOM), PL I TC 70, 74, 76, 78 (tiêu chí xếp mức RIS-PACS), nhóm phi chức năng TC 109. Dự thảo liên thông bản 11/2025 (báo, bối cảnh): định dạng DICOM. QĐ 2146/2026 nhắc HL7 FHIR R4 / DICOM 3.0 trong lộ trình đến 2030, áp cho đơn vị trực thuộc BYT; không văn bản nào buộc cơ sở KCB nói chung dùng FHIR/DICOM (xem MA-LT-R20).
- **Áp dụng**: cơ sở có PACS, vendor · **Hiệu lực/hạn**: —.
- **Mức**:
  - NÊN — hiện tại.
  - BẮT BUỘC? — khi thông tư liên thông ban hành với yêu cầu DICOM; đơn vị trực thuộc BYT ở mức "tuân thủ khung" QĐ 2146.
- **Phần mềm phải**: lưu và trao đổi ảnh ở DICOM nguyên bản (không lấy bản nén mất dữ liệu làm bản lưu chính); nén lưu trữ dạng không mất dữ liệu hoặc JPEG 2000 (TC 77, nâng cao); có DICOM conformance statement; hỗ trợ worklist, nhận ảnh từ máy (TC 67).
- **Bẫy**: câu "Bộ Y tế bắt buộc DICOM" trong tài liệu chào hàng là chưa có căn cứ, trừ khi dẫn được thông tư liên thông đã ban hành.

### CLS-R20 — Trả kết quả hình ảnh không in phim và giá BHYT
- **Căn cứ**: QĐ 4868/QĐ-BYT 2015 (thí điểm đến 30/12/2019); CV 5319/BYT-KH-TC 2020 (thứ cấp): cơ sở thí điểm và cơ sở làm EMR theo TT 46/2018 được thanh toán theo giá có in phim. QĐ 313/QĐ-BYT 29/01/2026 (thứ cấp): giá riêng CĐHA dùng PACS tại BV Bạch Mai; CV đôn đốc của BYT (báo, bối cảnh, 03/08/2026): mọi cơ sở xây phương án giá CĐHA dùng PACS theo TT 21/2024/TT-BYT, trình phê duyệt. TT 54 PL II mức 5: PACS nâng cao, thay thế tất cả phim; TC 74.
- **Áp dụng**: cơ sở có CĐHA muốn bỏ in phim · **Hiệu lực/hạn**: QĐ 313 từ 29/01/2026; cơ sở khác theo quyết định giá riêng.
- **Mức**: BẮT BUỘC? Không văn bản nào cấm trả ảnh điện tử, nhưng thu theo giá PACS phải có giá được duyệt; thu giá "có in phim" mà không in phim là rủi ro xuất toán (suy luận).
- **Phần mềm phải**: DVKT có hai biến thể giá (in phim / PACS) có mã, ngày hiệu lực theo quyết định của cơ sở; chọn theo cách trả thực tế; kênh trả ảnh cho người bệnh (cổng/app/link có hạn, QR, đĩa DICOM kèm viewer) có xác thực và ghi nhận đã giao (CLS-P08).
- **Bẫy**: TT 46/2018 đã hết hiệu lực từ 06/06/2025; CV 5319 chỉ còn giá trị lịch sử. Chưa thấy văn bản quy định điều kiện kỹ thuật PACS để được áp giá (thời gian lưu, cách giao ảnh): chưa xác minh.

### CLS-R21 — Giao diện RIS ↔ HIS ↔ PACS (tiêu chí TT 54)
- **Căn cứ**: TT 54/2017 PL I nhóm IV. Cơ bản (62–75): quản trị, cấu hình PACS, quản lý chỉ định, danh sách bệnh nhân, giao diện hai chiều với CT, MRI, X-quang, DSA, siêu âm (67), giao diện HIS (68: RIS nhận chỉ định từ HIS và chuyển vào máy theo HL7; liên thông hai chiều báo cáo), quản lý kết quả (69), HL7/DICOM (70), đo lường (71), xử lý ảnh 2D/3D (72, 73), xuất DICOM (74), thống kê (75). Nâng cao (76–79). PL II mức 4: PACS cơ bản, bác sĩ truy cập ảnh từ ngoài khoa CĐHA. Chuẩn HL7/DICOM nói chung: MA-LT-R21.
- **Áp dụng**: cơ sở tự xác định mức CNTT · **Hiệu lực/hạn**: 27/02/2018.
- **Mức**: NÊN.
- **Phần mềm phải**: Modality Worklist từ chỉ định HIS; trạng thái thực hiện; báo cáo có cấu trúc đồng bộ hai chiều với HIS; viewer cho bác sĩ ngoài khoa CĐHA có phân quyền.

### CLS-R22 — An toàn bức xạ: thông tin phục vụ bác sĩ chỉ định và nhân viên vận hành
- **Căn cứ**: TT 59/2025/TT-BKHCN Đ32 k1 (gốc-OCR, diễn giải): bác sĩ điều trị chịu trách nhiệm an toàn bức xạ cho người bệnh: (c) tránh chỉ định bức xạ ion hóa cho phụ nữ có thai, nghi có thai, đang cho con bú trừ khi bắt buộc, khi đó thông báo cho nhân viên; (đ) tham khảo các lần khám trước; (e) chỉ định mức chiếu xạ tối thiểu dựa trên mức liều tham chiếu chẩn đoán (PL 2 Mục 2). Đ32 k2 a: chiếu xạ y tế chỉ khi có chỉ định của bác sĩ.
- **Áp dụng**: cơ sở có X-quang, CT, y học hạt nhân, xạ trị · **Hiệu lực/hạn**: 01/01/2026.
- **Mức**:
  - BẮT BUỘC — với cơ sở và người hành nghề.
  - NÊN — hỗ trợ trong phần mềm (văn bản không nhắc phần mềm).
- **Phần mềm phải** (suy luận): khi chỉ định CĐHA dùng bức xạ, hiện lịch sử chụp (gồm ảnh liên thông), hỏi/ghi tình trạng thai, cho con bú với nữ tuổi sinh đẻ; chuyển cờ sang RIS/worklist; RIS lưu thông số liều do máy xuất (vd DICOM RDSR) để so với mức liều tham chiếu.
- **Bẫy**: văn bản hiện hành là TT 59/2025/TT-BKHCN, không phải TTLT 13/2014 hay TT 13/2018 (hết HL 01/01/2026). Chưa thấy điều khoản bắt ghi liều từng người bệnh; PL 2 Mục 2 chưa đọc. Trùng số "TT 59": xem mục 6.

### D. Phần mềm là thiết bị y tế (SaMD)

### CLS-R23 — Xác định phần mềm có phải là TBYT hay không
- **Căn cứ**: NĐ 98/2021 Đ2 k1 (bản gốc, đã đối chiếu ảnh): "Trang thiết bị y tế là các loại thiết bị, vật tư cấy ghép, dụng cụ, vật liệu, thuốc thử và chất hiệu chuẩn in vitro, phần mềm (software) đáp ứng đồng thời các yêu cầu sau đây:" (a) dùng theo chỉ định của chủ sở hữu cho mục đích chẩn đoán, ngăn ngừa, theo dõi, điều trị, làm giảm nhẹ bệnh tật…, hoặc cung cấp thông tin cho chẩn đoán, theo dõi, điều trị qua kiểm tra mẫu vật từ cơ thể người; (b) không dùng cơ chế dược lý, miễn dịch, chuyển hóa. Thuật ngữ "trang thiết bị y tế" đã đổi thành "thiết bị y tế" (NĐ 96/2023). Đ2 k2: IVD gồm cả hệ thống, sản phẩm hỗ trợ quá trình xét nghiệm. Đ2 k4 (phụ kiện), Đ1 k2 d (NĐ không áp dụng với phụ kiện). Đ3 k8 a: "Không áp dụng các quy định về phân loại, cấp số lưu hành, công bố đủ điều kiện mua bán của Nghị định này đối với: a) Phần mềm (software) sử dụng cho trang thiết bị y tế;" Đ5 k6: cơ sở đứng tên công bố/đăng ký thực hiện phân loại.
- **Áp dụng**: vendor phần mềm y tế (chủ sở hữu sản phẩm), cơ sở KCB tự phát triển phần mềm · **Hiệu lực/hạn**: 01/01/2022.
- **Mức**: BẮT BUỘC (phải tự xác định; sai thì bị phạt theo NĐ 90 Đ73 k4 a hoặc Đ71).
- **Phần mềm phải** (tài liệu kèm sản phẩm): văn bản intended use cho từng module; bảng đánh giá từng module theo Đ2 k1 (có mục đích y tế?) và Đ3 k8 a (có phải phần mềm "sử dụng cho" một TBYT cụ thể?); kết luận, người chịu trách nhiệm, ngày rà soát.
- **Bẫy** (suy luận, cần luật sư xác nhận):
  - Thường không phải TBYT: HIS hành chính, tiếp đón, viện phí, BHYT/XML, kho dược, nhân sự; EMR lưu và hiển thị; RIS/LIS quản lý chỉ định, mẫu, trả kết quả, thống kê; PACS chỉ lưu trữ và truyền ảnh.
  - Phần mềm sử dụng cho một TBYT cụ thể (firmware, phần mềm điều khiển máy, trạm xử lý đi kèm máy): thuộc Đ3 k8 a; cách hiểu thông dụng là đi theo hồ sơ của máy.
  - Rủi ro là TBYT độc lập: phần mềm đưa ra/đề xuất chẩn đoán từ ảnh, tín hiệu, kết quả xét nghiệm (CAD, AI đọc X-quang/CT, AI phân loại tế bào); tính liều thuốc, liều xạ; diễn giải xét nghiệm tự động thay bác sĩ; viewer PACS chào bán "dùng cho chẩn đoán chính" có đo lường, dựng 3D để quyết định điều trị.
  - Middleware LIS chỉ chuyển dữ liệu: nhiều khả năng không là TBYT; có autoverification hoặc tính chỉ số chẩn đoán thì có thể rơi vào Đ2 k2.

### CLS-R24 — Nếu là TBYT độc lập: phân loại, số lưu hành, điều kiện lưu hành
- **Căn cứ**: NĐ 98 Đ4 (loại A, B, C, D), Đ5 (phân loại theo quy tắc; nhiều mục đích lấy mức cao nhất), Đ21 k1 (số lưu hành: số công bố tiêu chuẩn với A, B; số đăng ký lưu hành với C, D), Đ22 k1, k3 (nhãn; HDSD tiếng Việt; bảo hành; có thể dạng điện tử với hướng dẫn tra cứu trên nhãn), Đ23 k1, Đ8 k1 (ISO 13485), Đ76 k5 (hồ sơ CSDT ASEAN từ 01/01/2024). TT 05/2022 PL I (quy tắc phân loại, gốc-OCR). TT 24/2026 Đ2. Luật KCB Đ94 k2: TBYT rủi ro trung bình cao, cao phải thử nghiệm lâm sàng trước khi đăng ký lưu hành theo quy định của Chính phủ.
- **Áp dụng**: chủ sở hữu, tổ chức đứng tên số lưu hành của phần mềm là TBYT · **Hiệu lực/hạn**: 01/01/2022; CSDT từ 01/01/2024.
- **Mức**: BẮT BUỘC (nếu kết luận là TBYT ở R23).
- **Phần mềm phải** (quy trình vendor): kết quả phân loại theo PL I TT 05 công bố trên Cổng BYT; hồ sơ công bố (A, B) hoặc đăng ký lưu hành (C, D) theo CSDT; QMS ISO 13485 gồm vòng đời phát triển phần mềm; HDSD tiếng Việt (có thể điện tử, chỉ dẫn tra cứu ở màn hình "Giới thiệu"/nhãn điện tử); thông tin bảo hành; số lưu hành hiển thị trong phần mềm.
- **Bẫy**:
  - PL I TT 05/2022 **không có** chữ "phần mềm"; phải phân loại bằng quy tắc chung. Gần nhất: Quy tắc 9 k2 (kiểm soát/ảnh hưởng thiết bị điều trị chủ động loại C → C), Quy tắc 10 (thiết bị chủ động chẩn đoán: B; C nếu giám sát thông số sống nguy hiểm hoặc chẩn đoán khi nguy kịch; 10 k4: kiểm soát thiết bị X-quang → C), Quy tắc 12 (thiết bị chủ động khác → A); IVD: quy tắc 1–7. Phần mềm có là "TBYT chủ động" (hoạt động bằng biến đổi năng lượng) hay không: chưa rõ (suy luận).
  - TT 24/2026 không thêm quy tắc; lộ trình kiểm định (30/06/2027, 01/01/2028) chỉ cho 6 thiết bị phần cứng (máy thở, máy gây mê kèm thở, dao mổ điện, lồng ấp, máy phá rung, máy thận nhân tạo).
  - Chưa có Luật TBYT; khi có luật, quy tắc SaMD có thể đổi.

### CLS-R25 — Cơ sở KCB chỉ dùng TBYT có số lưu hành; quản lý hồ sơ, báo lỗi
- **Căn cứ**: Luật KCB Đ113 k1: "Thiết bị y tế sử dụng tại các cơ sở khám bệnh, chữa bệnh phải được phép lưu hành hợp pháp tại Việt Nam". Đ113 k3 (hồ sơ theo dõi TBYT). NĐ 98 Đ63 k3, Đ65 k1 b, Đ65 k2 a (vận hành theo hướng dẫn), Đ65 k2 d (báo cáo TBYT có lỗi). NĐ 90 Đ79 k1–k3.
- **Áp dụng**: BV, PK, mọi cơ sở y tế dùng phần mềm là TBYT (vd AI đọc ảnh) · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải** (HIS/quản lý thiết bị): sổ TBYT có cả phần mềm là TBYT (tên, phiên bản, số lưu hành, chủ sở hữu, ngày dùng); kiểm số lưu hành trước khi kích hoạt module AI/CAD bên thứ ba; kênh ghi nhận, báo cáo lỗi TBYT.
- **Bẫy**: hợp đồng PACS kèm AI phải yêu cầu số lưu hành hoặc văn bản lý giải vì sao không phải TBYT; thiếu cả hai thì cơ sở chịu Đ79 k3 (suy luận).

### CLS-R26 — Sau bán hàng: thay đổi phiên bản, truy xuất, cảnh báo
- **Căn cứ**: NĐ 90/2026 (gốc-OCR, diễn giải) Đ73 k1 d, đ (thông báo thay đổi trong 5 ngày làm việc với hồ sơ công bố, 10 ngày làm việc với hồ sơ đăng ký), Đ73 k2 a (công bố lại khi đổi mục đích sử dụng, chỉ định), Đ73 k2 b, g (truy xuất, hồ sơ theo dõi), Đ73 k4 c (không xử lý sự cố). NĐ 98 Đ33–Đ37 (sau bán hàng, cảnh báo, sự cố, thu hồi; chưa đọc chi tiết).
- **Áp dụng**: chủ sở hữu số lưu hành phần mềm là TBYT · **Hiệu lực/hạn**: đang HL.
- **Mức**: BẮT BUỘC (nếu là TBYT).
- **Phần mềm phải**: quy trình phát hành có bước phân loại thay đổi (thông thường / phải thông báo / đổi mục đích phải công bố lại); danh sách cơ sở đang dùng từng phiên bản; cơ chế gửi cảnh báo an toàn, vá lỗi tới từng cơ sở; nhật ký sự cố (CLS-P10).

### CLS-R27 — Thiết kế ranh giới để HIS/LIS/PACS không vô tình thành TBYT
- **Căn cứ**: suy ra từ NĐ 98 Đ2 k1 (định nghĩa dựa vào mục đích do chủ sở hữu chỉ định), Đ5 (nhiều mục đích lấy mức cao nhất), NĐ 90 Đ73 k2 a. AI rủi ro cao (Luật AI 134/2025, QĐ 33/2026/QĐ-TTg): xem DLCN-R25 và TELE-R21–R27.
- **Áp dụng**: vendor · **Hiệu lực/hạn**: —.
- **Mức**: NÊN (thực hành tốt).
- **Phần mềm phải**: (1) intended use của sản phẩm chính không gồm chẩn đoán/điều trị tự động; (2) tách module có chức năng y tế (AI, CAD, tính liều) thành sản phẩm riêng có hồ sơ TBYT, bật/tắt theo hợp đồng; (3) marketing và UI không dùng "chẩn đoán", "phát hiện bệnh" cho module không có số lưu hành; (4) CDSS chỉ hiển thị tham chiếu, cảnh báo, không tự đổi y lệnh; (5) LIS autoverification: quy tắc do PXN phê duyệt và chịu trách nhiệm, vendor chỉ cung cấp công cụ (giảm rủi ro nhưng không chắc loại trừ, suy luận).

**Tổng hợp mức** (theo mức cao nhất của mục): BẮT BUỘC 12 (R02, R04, R07, R08, R09, R14, R18, R22, R23, R24, R25, R26; R24, R26 có điều kiện "nếu là TBYT"); BẮT BUỘC? 7 (R01, R03, R05, R06, R15, R19, R20); NÊN 8 (R10, R11, R12, R13, R16, R17, R21, R27).

## 3. Pattern thiết kế

### CLS-P01 — Kho kết quả CLS chuẩn hóa có metadata liên thông
- **Giải quyết**: R02, R07, R08, R12, R18
- **Cách làm**: mọi kết quả (xét nghiệm, CĐHA, thăm dò chức năng) một mô hình chung, tách báo cáo và chỉ số; bản final bất biến (trigger chặn UPDATE nội dung).
- **Gợi ý dữ liệu**: `cls_order(patient_id, encounter_id, hsba_id, service_code_internal, service_code_shared, ordered_by, ordered_at, reorder_reason_code, reorder_reason_text)`; `cls_specimen(order_id, specimen_type, collected_at NOT NULL, collected_by, received_at, rejected_reason)`; `cls_report(order_id, performing_facility_code, performing_lab_id, performed_at NOT NULL, performed_by, interpreted_by, validated_by, released_at, status ENUM('preliminary','final','amended','cancelled'), version, supersedes_report_id, amendment_reason, signature_id, source ENUM('internal','external_referral','interop_received'), source_facility_code, hash)`; `cls_observation(report_id, analyte_code_internal, analyte_code_1227, analyte_code_temp_7603, value_num, value_text, unit, unit_si, ref_low, ref_high, flag, critical, method, instrument_id)`. Ràng buộc: không cho `final` khi thiếu `collected_at`/`performed_at`, `validated_by`, mã 1227 (hoặc cờ tạm 7603). Chỉ mục `(patient_id, analyte_code_1227, collected_at DESC)`.
- **Đánh đổi**: tốn công ánh xạ danh mục ban đầu; đổi lại dùng chung cho XML4, EMR, liên thông.

### CLS-P02 — Bảng thời hạn giá trị có phiên bản và bộ kiểm tra trùng lặp
- **Giải quyết**: R03, R06, R22
- **Cách làm**: khi chỉ định, tìm kết quả cùng mã còn trong `validity_hours` tính từ `collected_at`/`performed_at` (gồm kết quả nhận liên thông); có thì cảnh báo, bắt `reorder_reason_code` nếu vẫn chỉ định.
- **Gợi ý dữ liệu**: `cls_validity_rule(code_type, code, validity_hours, condition, legal_basis, effective_from, effective_to)`.
- **Đánh đổi**: danh mục dự thảo đổi liên tục → trước khi thông tư ban hành chạy chế độ "chỉ cảnh báo, không chặn".

### CLS-P03 — Sổ năng lực chất lượng và nguồn gốc kết quả
- **Giải quyết**: R04, R08, R10
- **Cách làm**: mỗi `cls_report` gửi đi kèm snapshot credential hiệu lực tại `released_at`; phía nhận lưu snapshot cùng kết quả.
- **Gợi ý dữ liệu**: `lab_quality_credential(lab_id, facility_code, scheme ENUM('QD2429','ISO15189'), level, scope_analytes[], assessed_by, assessed_at, valid_to, evidence_doc_id)`.
- **Đánh đổi**: cập nhật thủ công; chưa thấy API quốc gia để tra.

### CLS-P04 — Gói liên thông kết quả có ký số và lớp adapter định dạng
- **Giải quyết**: R01, R02, R05, R19
- **Cách làm**: dựng gói nội bộ (báo cáo + chỉ số + metadata + credential + chữ ký số cơ sở), rồi adapter xuất ra định dạng thông tư quy định khi ban hành (HL7 v2 ORU, CDA, FHIR DiagnosticReport/Observation hoặc XML riêng của BYT: chưa biết). Ảnh: tham chiếu study UID, truyền PACS–PACS hoặc DICOMweb; SHA-256 từng instance. API gợi ý: `POST /interop/cls/outbound`, `POST /interop/cls/inbound` (xác minh chữ ký, đối chiếu định danh, lưu `source='interop_received'`).
- **Gợi ý dữ liệu**: dùng chung `interface_message` của MA-LT-P06.
- **Đánh đổi**: adapter viết trước chuẩn có thể phải làm lại; tách lõi khỏi định dạng giúp đổi nhanh.

### CLS-P05 — Vòng đời mẫu và kết quả có cổng QC
- **Giải quyết**: R09, R11, R13, R14, R15
- **Cách làm**: máy trạng thái `ordered → collected → received → in_analysis → result_available → tech_validated → med_validated → released → (amended)`, mỗi bước ghi actor, timestamp; QC `fail` chặn `tech_validated → released` cho tổ hợp đó đến khi có khắc phục được duyệt.
- **Gợi ý dữ liệu**: `qc_status(instrument_id, test_code, shift, status, run_at)`; `qc_corrective_action`; `critical_alert(report_id, notified_to, channel, acknowledged_at)`.
- **Đánh đổi**: khóa có thể làm chậm cấp cứu → quyền ghi đè có lý do và kiểm toán.

### CLS-P06 — Phân hệ QC nội kiểm và ngoại kiểm
- **Giải quyết**: R09, R10
- **Cách làm**: Levey-Jennings, Westgard; báo cáo theo mẫu đánh giá QĐ 2429 Chương VIII.
- **Gợi ý dữ liệu**: `qc_material(lot, level, target_mean, target_sd, expiry)`, `qc_result(instrument_id, test_code, material_lot, value, run_at, rule_violations[])`, `eqa_round(program, round, test_code, result, evaluation, corrective_action_id)`.
- **Đánh đổi**: nhiều PXN dùng phần mềm QC của hãng máy; khi đó LIS chỉ cần nhận trạng thái QC qua giao diện.

### CLS-P07 — Lưu trữ PACS phân tầng, thời hạn kế thừa HSBA
- **Giải quyết**: R18, R19
- **Cách làm**: `retain_until` tính lại khi loại lưu trữ của HSBA đổi (EMR-R22); tầng nóng (1–2 năm), tầng lạnh (object storage, nén không mất dữ liệu); job xóa chỉ chạy khi `now > retain_until AND NOT legal_hold` và có biên bản hủy (EMR-R24).
- **Gợi ý dữ liệu**: `imaging_study(study_uid, patient_id, hsba_id, retention_class, retain_until, storage_tier, legal_hold, sha256_manifest)`.
- **Đánh đổi**: lưu ảnh gốc 10–30 năm rất tốn; nếu chỉ giữ ảnh chọn lọc phải có chính sách văn bản và chấp nhận rủi ro với liên thông ảnh gốc.

### CLS-P08 — Trả ảnh không in phim và chọn giá đúng
- **Giải quyết**: R20, R21
- **Cách làm**: khi phát hành kết quả CĐHA ghi `delivery_mode ENUM('film','portal','qr_link','dicom_media')` và chọn biến thể giá tương ứng; cổng xem ảnh có xác thực (OTP/VNeID), link có hạn, nhật ký truy cập.
- **Gợi ý dữ liệu**: `service_price_variant(service_code, variant ENUM('film','pacs'), price, approval_decision_no, effective_from)`.
- **Đánh đổi**: phải đồng bộ quyết định giá từng cơ sở; chưa có giá PACS được duyệt thì cảnh báo khi trả không in phim mà vẫn dùng giá có phim.

### CLS-P09 — Sổ đăng ký mục đích sử dụng và ranh giới SaMD
- **Giải quyết**: R23, R24, R25, R27
- **Cách làm**: feature flag theo module; UI hiện số lưu hành ở màn hình "Giới thiệu" của module là TBYT; build pipeline chặn bật module là TBYT khi `registration_no` rỗng.
- **Gợi ý dữ liệu**: `product_module(name, intended_use_text, is_medical_device ENUM('no','accessory_or_used_for_device','yes'), assessment_doc_id, risk_class, registration_no, registration_holder, reviewed_at)`.
- **Đánh đổi**: tách sản phẩm tăng chi phí đóng gói, hợp đồng; đổi lại giữ HIS lõi ngoài phạm vi quản lý TBYT.

### CLS-P10 — Phát hành phiên bản có phân loại thay đổi (module là TBYT)
- **Giải quyết**: R26
- **Cách làm**: mỗi release có lớp thay đổi do người phụ trách pháp chế duyệt; hạn thông báo tính theo ngày làm việc; truy xuất cơ sở theo phiên bản để gửi cảnh báo an toàn.
- **Gợi ý dữ liệu**: `release(change_class ENUM('minor','notify_5wd','notify_10wd','re_declare'), approved_by)`; `deployment(facility_code, module_id, version, deployed_at)`.
- **Đánh đổi**: chậm phát hành; cần người đủ năng lực đánh giá thay đổi.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| CLS-A01 | R01 | Hỏi lộ trình đáp ứng liên thông 01/01/2027; có module xuất/nhận kết quả cơ sở khác | Tài liệu lộ trình, demo | BẮT BUỘC? |
| CLS-A02 | R02 | SQL tỷ lệ kết quả final thiếu `collected_at`/`performed_at`, người thực hiện, người duyệt; in phiếu gửi cơ sở khác tìm viết tắt nội bộ | Truy vấn, bản in | BẮT BUỘC |
| CLS-A03 | R03 | Chỉ định lại HbA1c trong 30 ngày, urê trong 12 giờ: có cảnh báo trùng? Bảng thời hạn cấu hình được, có ngày hiệu lực? | Ảnh màn hình, cấu hình | BẮT BUỘC? |
| CLS-A04 | R04 | Lưu mức chất lượng PXN (QĐ 2429), phạm vi ISO 15189 kèm hạn? Cơ sở công khai kiểm chuẩn (TT 01/2013 Đ4 k3)? | Màn hình danh mục, trang công khai | BẮT BUỘC / BẮT BUỘC? |
| CLS-A05 | R05, R19 | Xuất một study CT: đủ series DICOM gốc, header khớp HSBA, có hash? PACS lưu DICOM gốc hay chỉ JPEG? | File xuất, DICOM dump, cấu hình | BẮT BUỘC? |
| CLS-A06 | R06 | Vẫn chỉ định dù có kết quả còn hạn: có bắt nhập lý do? Báo cáo tỷ lệ chỉ định lại | Ảnh màn hình, báo cáo | BẮT BUỘC? |
| CLS-A07 | R07 | Tỷ lệ chỉ số XN/CĐHA đã map mã QĐ 1227; danh sách còn dùng PL11 QĐ 7603; XML4 lấy mã từ đâu | Báo cáo ánh xạ, mẫu XML4 | BẮT BUỘC |
| CLS-A08 | R08 | Kết quả XN gửi ngoài có cờ cơ sở thực hiện trên phiếu và trong dữ liệu | Phiếu in, bản ghi | NÊN |
| CLS-A09 | R09 | Hồ sơ QC nội kiểm (2 mức định lượng), sự cố, khắc phục, người duyệt; truy theo máy và ngày | Báo cáo QC, Levey-Jennings | BẮT BUỘC |
| CLS-A10 | R10 | Lưu EQA/so sánh liên phòng theo đợt; tài liệu nội bộ còn ghi "ngoại kiểm bắt buộc"? | Hồ sơ EQA, SOP | NÊN |
| CLS-A11 | R11 | Đặt QC "không đạt" cho một xét nghiệm trên một máy: có chặn phát hành? Ghi đè có log lý do? | Ảnh màn hình, log | NÊN |
| CLS-A12 | R12 | So phiếu kết quả với 16 mục TC 8.21 (a–p); định danh và "trang x/y" trên mọi trang | Bảng so khớp, bản in | NÊN |
| CLS-A13 | R13 | Danh sách người ký duyệt theo nhóm XN; tách sơ bộ/chính thức; thử giá trị nguy kịch: cảnh báo, xác nhận, leo thang | Cấu hình, log cảnh báo | NÊN |
| CLS-A14 | R14 | Sửa kết quả đã phát hành: bản gốc còn? Nhãn "đã sửa", lý do, người sửa, thông báo, đánh dấu gửi lại XML4? | Lịch sử phiên bản, log | BẮT BUỘC |
| CLS-A15 | R15 | Báo cáo TAT từng giai đoạn; mốc lấy mẫu, nhận mẫu ghi thật hay mặc định bằng giờ chỉ định | Báo cáo, phân bố SQL | BẮT BUỘC? |
| CLS-A16 | R16 | Ma trận vai trò nhập/sửa/duyệt/phát hành; log trục trặc; quy trình khi LIS ngừng | Ma trận quyền, SOP dự phòng | NÊN |
| CLS-A17 | R17, R21 | Đối chiếu TC 62–89 TT 54: interface máy XN, HIS ↔ LIS hai chiều, worklist, HL7, viewer ngoài khoa | Bảng tự đánh giá TT 54 | NÊN |
| CLS-A18 | R18 | Kết quả CLS và study có `retention_class`/`retain_until` kế thừa HSBA? Có job xóa ảnh theo thời gian cố định bất kể HSBA? | Truy vấn, cấu hình PACS | BẮT BUỘC / BẮT BUỘC? |
| CLS-A19 | R20 | Có quyết định giá CĐHA dùng PACS? Hai biến thể giá, chọn theo cách trả thực tế? Bằng chứng người bệnh nhận ảnh? | QĐ giá, cấu hình DVKT, log cổng | BẮT BUỘC? |
| CLS-A20 | R22 | Chỉ định CT cho nữ 15–49 tuổi: hỏi/ghi tình trạng thai, hiện lịch sử chụp; RIS lưu thông số liều | Ảnh màn hình, mẫu dữ liệu | NÊN |
| CLS-A21 | R23, R27 | Tài liệu intended use và đánh giá TBYT từng module; rà UI, brochure tìm "chẩn đoán", "AI phát hiện" ở module không số lưu hành | Tài liệu đánh giá, ảnh UI, brochure | BẮT BUỘC |
| CLS-A22 | R24 | Module là TBYT: tra số lưu hành trên Cổng TBYT; bản phân loại; HDSD tiếng Việt; bảo hành | Số lưu hành, bản phân loại, HDSD | BẮT BUỘC |
| CLS-A23 | R25 | Sổ TBYT của cơ sở liệt kê phần mềm là TBYT (AI/CAD) kèm số lưu hành, phiên bản; kênh báo lỗi TBYT | Sổ tài sản, quy trình báo lỗi | BẮT BUỘC |
| CLS-A24 | R26 | Quy trình phát hành: phân loại thay đổi, hạn thông báo 5/10 ngày làm việc, danh sách cơ sở theo phiên bản | SOP phát hành, release log | BẮT BUỘC (nếu là TBYT) |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 27/02/2018 | TT 54/2017 (tiêu chí LIS, RIS-PACS) | Cơ sở tự đánh giá | Đã qua |
| 01/01/2022 | NĐ 98/2021 có HL; TT 05/2022 từ 01/08/2022 | Vendor phần mềm là TBYT | Đã qua |
| 01/01/2024 | Hồ sơ CSDT bắt buộc; Luật KCB Đ113 có HL | Chủ sở hữu TBYT; cơ sở KCB | Đã qua |
| 01/07/2025 | TT 33/2025 thời hạn lưu trữ | Mọi cơ sở | Đã qua |
| 01/01/2026 | TT 59/2025/TT-BKHCN an toàn bức xạ | Cơ sở có công việc bức xạ | Đã qua |
| 29/01/2026 | Giá CĐHA dùng PACS đầu tiên (BV Bạch Mai, QĐ 313) | BV Bạch Mai | Đã qua |
| 01/07/2026 | TT 24/2026 có HL (thay TT 59/2025/TT-BYT) | Chủ sở hữu TBYT | Đã qua |
| 15/08/2026 | Ngoại kiểm thành "khuyến khích" (TT 25/2026 Đ1) | Cơ sở có PXN | Đã qua |
| 18/08/2026 | NĐ 313/2026 có HL (thay NĐ 42/2025) | BYT | Đã qua |
| ~10/2026 | BYT dự kiến ban hành thông tư liên thông CLS (báo) | BYT | Sắp tới (chưa chắc) |
| **01/01/2027** | **Liên thông, sử dụng kết quả CLS giữa cơ sở KCB BHYT** | Cơ sở KCB BHYT có CLS; vendor HIS/LIS/RIS/PACS | Sắp tới (còn ~3 tháng) |
| 30/06/2027; 01/01/2028 | Kiểm định 6 loại TBYT phần cứng (không áp phần mềm) | Cơ sở có các máy đó | Sắp tới |
| 01/09/2027 | AI y tế đã chạy trước 01/03/2026 phải tuân thủ Luật AI (xem TELE-R25) | Vendor AI | Sắp tới |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**

| Cũ | Mới | Từ ngày | Ghi chú |
|---|---|---|---|
| NĐ 42/2025/NĐ-CP (chức năng BYT) | NĐ 313/2026/NĐ-CP | 18/08/2026 | Văn bản ký trước ngày này dẫn NĐ 42/2025 vẫn đúng tại thời điểm ký |
| TT 01/2013 Đ5 k5 (tham gia ngoại kiểm) | TT 25/2026 Đ1 (khuyến khích) | 15/08/2026 | Sửa một khoản |
| TTLT 13/2014/TTLT-BKHCN-BYT; TT 13/2018/TT-BKHCN; TT 19/2012/TT-BKHCN | TT 59/2025/TT-BKHCN | 01/01/2026 | Căn cứ Luật Năng lượng nguyên tử 94/2025/QH15 |
| TT 59/2025/TT-BYT (sửa TT 05/2022) | TT 24/2026/TT-BYT | 01/07/2026 | |
| "Trang thiết bị y tế" | "Thiết bị y tế" | 01/01/2024 | NĐ 96/2023 Đ147 k7 |
| Thí điểm PACS (QĐ 4868/2015; CV 5319/2020 giá có in phim) | Giá riêng "CĐHA dùng PACS" theo TT 21/2024 (QĐ 313/2026; cơ sở khác chờ duyệt) | 2026 | Thứ cấp |
| Dự thảo bản 11/2025 (~1.114 kỹ thuật, 6 PL, DICOM) | Dự thảo bản 08/2026 (441 kỹ thuật, 4 nhóm) | — | Cả hai là dự thảo |

**Bẫy trích dẫn**

1. Ba văn bản số "59": TT 59/2025/**TT-BYT** (sửa TT 05/2022, hết HL 01/07/2026); TT 59/2025/**TT-BKHCN** (an toàn bức xạ, còn HL); TT 59/2026/TT-BKHCN (bãi bỏ TT 41/2017/TT-BTTTT, xem EMR). Luôn ghi đủ hậu tố.
2. "Luật 51 Đ3 k4 giao Chính phủ quy định" chưa có nghị định riêng; đừng trích NĐ 188/2025 cho liên thông CLS.
3. "Ngoại kiểm bắt buộc" sai từ 15/08/2026; nhưng QĐ 2429 vẫn để EQA là tiêu chí (*) khi xếp mức.
4. "TT 33/2025 quy định lưu ảnh DICOM X năm": không có dòng nào như vậy.
5. "BYT bắt buộc DICOM": chưa có VBQPPL. QĐ 2146 chỉ nêu DICOM 3.0 trong lộ trình cho đơn vị trực thuộc BYT; DICOM trong dự thảo liên thông là dự thảo.
6. Con số 441 / ~1.100 kỹ thuật và các thời hạn giá trị chỉ đến từ báo về dự thảo; không nạp làm tham số chính thức. Hiệu lực dự kiến 01/07/2026 đã lỡ.
7. QĐ 1227 có 1.240 chỉ số điện quang, không chỉ xét nghiệm.
8. NĐ 98 Đ3 k8 a chỉ miễn "phần mềm sử dụng cho" TBYT, không miễn mọi phần mềm y tế.
9. NĐ 04/2025 chỉ sửa Đ76 (chuyển tiếp nhập khẩu, IVD); đừng trích cho phân loại phần mềm. Số VBHN của NĐ 98 chưa thống nhất (bản Cục HT&TBYT sao y 26/03/2025; inventory ghi 08/VBHN-BYT 2026, chưa xác minh).
10. Lộ trình kiểm định 30/06/2027, 01/01/2028 (TT 24/2026) chỉ cho 6 thiết bị phần cứng.
11. Tiêu chí TT 54 dùng JPEG để "hoàn thiện HSBA" là thiết kế 2017, không dùng làm chuẩn lưu cho liên thông ảnh gốc.
12. TT 54/2017 có hiệu lực **27/02/2018** (Đ6 bản gốc), không phải 26/02/2018.
13. Thời hạn lưu hồ sơ ghép tạng: TT 33/2025 ghi 20 năm nhưng Luật 75/2006 ghi 30 năm → áp 30 năm.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. Toàn văn dự thảo thông tư liên thông CLS (cả hai bản): định dạng trao đổi xét nghiệm; DICOM còn trong bản 08/2026 không; danh mục, thời hạn từng dịch vụ; ai lưu và cung cấp ảnh; trách nhiệm khi kết quả liên thông sai; thanh toán BHYT dịch vụ làm lại. Hỏi BYT (Vụ BHYT, Cục QLKCB).
2. Nếu đến 01/01/2027 chưa có thông tư, Luật 51 Đ3 k4 áp dụng thế nào (nghĩa vụ trực tiếp hay chờ hướng dẫn): cần luật sư.
3. Phần mềm độc lập có phải TBYT (PACS viewer đo, dựng 3D; CAD/AI đọc ảnh; LIS autoverification; CDSS tính liều); phần mềm có là "TBYT chủ động" khi áp quy tắc 9–12: cần luật sư + hỏi Cục Hạ tầng và Thiết bị y tế.
4. Phụ lục QĐ 1227: cấu trúc cột các phụ lục ngoài huyết học (xem MA-LT §7).
5. QĐ 313/QĐ-BYT 2026 và CV đôn đốc giá PACS: bản gốc, số hiệu CV (một kết quả tìm kiếm ghi 5586/BYT-BH ngày 28/07/2026), điều kiện kỹ thuật PACS để áp giá.
6. TT 32/2023 PL XXIX: có mẫu phiếu kết quả xét nghiệm/CĐHA bắt buộc không.
7. Thời hạn lưu ảnh gốc DICOM và kết quả CLS ngoại trú không lập HSBA: hỏi BYT (đơn vị soạn TT 33).
8. TT 59/2025/TT-BKHCN PL 2 Mục 2 (mức liều tham chiếu) và nghĩa vụ ghi liều từng người bệnh: chưa đọc.
9. NĐ 98 Đ33–Đ37 (sau bán hàng) và Đ26, Đ30 (hồ sơ công bố, đăng ký) áp cho phần mềm: mới đọc tiêu đề.
10. QĐ 2429/2017 (tóm tắt luatvietnam ghi "áp dụng thí điểm 2017–2018"): còn là thước đo chính thức hay đã có bộ tiêu chí mới.
11. Số hiệu VBHN hiện hành của NĐ 98.
