# SKDT — Sổ sức khỏe điện tử, VNeID và định danh người bệnh
> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: nửa "Sổ SKĐT / VNeID / định danh" của cụm K4 trong inventory. Gồm: nghĩa vụ liên thông Sổ SKĐT VNeID (QĐ 1332, QĐ 2733, QĐ 31), dữ liệu khám sức khỏe định kỳ và sàng lọc (QĐ 1551, CT 17), mã định danh y tế (NĐ 102), số định danh cá nhân và căn cước (Luật Căn cước, NĐ 70), định danh và xác thực điện tử (NĐ 69), người bệnh không giấy tờ, trẻ em, người nước ngoài, mã cơ sở KCB 5 ký tự và 13 chữ số, chương trình Đề án 06 giai đoạn 2026–2030. **Ngoài phạm vi**, dẫn chiếu sang cụm khác: xuất trình thẻ BHYT bằng căn cước/VNeID → **BHYT-GD-R01..R05**; chuẩn XML 130/4750/3176 → **BHYT-DATA**; MPI trong EMR → **EMR-R05**; căn cứ xử lý và quyền chủ thể → **DLCN**; giấy chứng sinh, giấy báo tử, giấy nghỉ hưởng BHXH, KSK lái xe ↔ CSDL giao thông → nửa "giấy tờ điện tử liên thông" của K4 (cụm khác).
>
> Nguồn gốc đã đọc trong pha này: QĐ 31/QĐ-BYT (PDF có lớp text), QĐ 1551/QĐ-BYT (PDF có lớp text, 224 trang), QĐ 1332/QĐ-BYT và QĐ 2733/QĐ-BYT (PDF scan, OCR tesseract `vie`), NĐ 102/2025, NĐ 69/2024, NĐ 70/2024 (Đ1–14), QĐ 826/QĐ-TTg, QĐ 940/QĐ-TTg, CV 1129/TTg-KGVX (PDF scan datafiles, OCR `vie`), Luật Căn cước 26/2023 (Công báo, có lớp text), VBHN 26/VBHN-VPQH Luật KCB (có lớp text). "gốc-OCR" nghĩa là số và ngày tin được, câu chữ có thể lệch dấu. Đây là tài liệu nghiên cứu, **không phải ý kiến pháp lý**.

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| ND-102-2025 | 102/2025/NĐ-CP (13/05/2025) | Quy định quản lý dữ liệu y tế | 01/07/2025 (Đ25) | Còn HL | Mọi cơ sở y tế (BV công, BV tư, PK; nhà thuốc ở mức "cơ sở y tế") | gốc-OCR | [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/102-ndcp.signed.pdf) |
| QD-1332-2024-BYT | 1332/QĐ-BYT (21/05/2024) | Ban hành "Sổ sức khỏe điện tử" phục vụ tích hợp trên VNeID (thí điểm) | Từ ngày ký (Đ5) | Còn HL; là nội dung chuẩn mà QĐ 2733, QĐ 31, QĐ 1551 dẫn chiếu | BV công, BV tư, PK (Đ2: "tất cả các cơ sở KCB công lập và tư nhân") | gốc-OCR (nâng từ "thứ cấp") | [PDF, BVĐK Bạc Liêu đăng](https://bvdkbaclieu.gov.vn/upload/1000079/20240622/382_Quyet_dinh-1332-QD-BYT_beaeb9e1ff.pdf) |
| QD-2733-2024-BYT | 2733/QĐ-BYT (17/09/2024) | Hướng dẫn thí điểm thực hiện Sổ SKĐT phục vụ tích hợp trên VNeID (PL01 hướng dẫn; PL02 ánh xạ trường sang XML 130/4750) | Từ ngày ký (Đ5) | Còn HL; QĐ 31 Đ5 dẫn chiếu làm hướng dẫn kỹ thuật | BV công, BV tư, PK; mọi loại hình ngoại trú, nội trú, ban ngày, lĩnh thuốc theo hẹn, KCB từ xa (Đ2) | gốc-OCR (bản sao y của BYT; nâng từ "chỉ dẫn chiếu") | [PDF, BVĐK Bạc Liêu đăng](https://bvdkbaclieu.gov.vn/upload/1000079/20241031/444_Quyet_dinh-2733-QD-BYT_8fd263b901.pdf) |
| QD-31-2026-BYT | 31/QĐ-BYT (06/01/2026) | Công bố dữ liệu, hướng dẫn khai thác dữ liệu Sổ SKĐT VNeID thay sổ giấy trong TTHC | Từ ngày ký (Đ6); Đ5 nêu mốc 01/01/2026 | Còn HL | Cơ sở KCB (Đ1 k2, Đ5); cơ quan giải quyết TTHC (Đ4) | gốc | [PDF, BVĐK Bạc Liêu đăng](https://bvdkbaclieu.gov.vn/upload/1000079/20260305/691_Quyet-dinh-31-QD-BYT_704c0ca597.pdf) |
| QD-1551-2026-BYT | 1551/QĐ-BYT (31/05/2026) | Hướng dẫn thu thập, cập nhật, kết nối liên thông dữ liệu khám sức khỏe và tạo lập, cập nhật Sổ SKĐT trên VNeID (PL01: 17 mẫu đặc tả; PL02: API; PL03: API nhận dữ liệu BHXH) | Từ ngày ký (Đ2) | Còn HL | Cơ sở KCB tổ chức KSK định kỳ, khám sàng lọc (công và tư); vendor phần mềm KSK | gốc | [PDF, SYT Lai Châu](https://soyte.laichau.gov.vn/upload/1001027/20260602/2026_05_31_QD_ban_hanh_HD_ket_noi_lien_thong_du_lieu_KSK_Final_signed_2be3f377e1.pdf) |
| CV-4395-2023-BYT (**mới với cụm**) | 4395/BYT-KCB (13/07/2023) | Áp dụng liên thông dữ liệu theo QĐ 130 (Bảng 1 và Bảng 8) với người bệnh không dùng thẻ BHYT, phục vụ Đề án 06 | — | Chưa rõ còn áp dụng nguyên trạng không (QĐ 130 đã sửa bởi 4750, 3176) | BV công, BV tư, PK, kể cả cơ sở chưa ký HĐ BHYT (theo tóm tắt) | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/cong-van-4395-byt-kcb-2023-lien-thong-du-lieu-theo-quyet-dinh-130-qd-byt-259277-d6.html) |
| L-CANCUOC-2023 | 26/2023/QH15 (27/11/2023) | Luật Căn cước | 01/07/2024 | Còn HL | Mọi tổ chức khai thác thông tin căn cước | gốc (Công báo, có text; nâng từ gốc-meta) | [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/01/luat26.pdf) |
| ND-70-2024 | 70/2024/NĐ-CP (25/06/2024) | Hướng dẫn Luật Căn cước | 01/07/2024 | Còn HL | Như trên | gốc-OCR (Đ1–14) | [VB 210497](https://vanban.chinhphu.vn/?pageid=27160&docid=210497) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/6/70-nd.signed.pdf) |
| ND-69-2024 | 69/2024/NĐ-CP (25/06/2024) | Định danh và xác thực điện tử | 01/07/2024 (Đ40 k1) | Còn HL; thay NĐ 59/2022 (Đ40 k2) | Cơ sở KCB, vendor tích hợp VNeID, app y tế | gốc-OCR (toàn văn) | [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/6/69-cp.signed.pdf) |
| L-KCB-2023 (VBHN) | 26/VBHN-VPQH | Luật KCB hợp nhất: Đ2 k10 (người bệnh không có thân nhân), Đ72, Đ73 | 01/01/2024 | Còn HL | BV công, BV tư, PK | gốc | [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| QD-826-2026-TTg | 826/QĐ-TTg (11/05/2026) | Chương trình Đề án 06 giai đoạn 2026–2030, tầm nhìn 2035 | Ký | Còn HL; tiếp nối QĐ 06/QĐ-TTg (2022–2025) | Chủ yếu cơ quan nhà nước; gián tiếp cơ sở KCB | gốc-OCR (bảng mục tiêu đã đối chiếu ảnh) | [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/826-ttg.signed.pdf) |
| QD-940-2026-TTg | 940/QĐ-TTg (26/05/2026) | Đề án phát triển ứng dụng VNeID 2026–2030, tầm nhìn 2045 | Ký | Còn HL | Bối cảnh (VNeID mini app, luật ĐD&XTĐT) | gốc-OCR (nâng từ gốc-meta) | [VB 218266](https://vanban.chinhphu.vn/?pageid=27160&docid=218266) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/940-ttg.signed.pdf) |
| CT-17-2026-TTg | 17/CT-TTg (06/05/2026) | Tổ chức KSK định kỳ, khám sàng lọc miễn phí cho người dân | Ký | Còn HL | Cơ sở KCB công và ngoài công lập tham gia KSK | thứ cấp (bài đăng trên xaydungchinhsach.chinhphu.vn) | [xaydungchinhsach](https://xaydungchinhsach.chinhphu.vn/chi-thi-so-17-ct-ttg-to-chuc-kham-suc-khoe-dinh-ky-kham-sang-loc-mien-phi-cho-nguoi-dan-119260507075549614.htm) |
| CV-1129-2026-TTg (**mới với cụm**, inventory gộp vào CT 17) | 1129/TTg-KGVX (16/09/2026) | Triển khai CT 17 về KSK cho người dân | Ký | Còn HL | UBND tỉnh, BYT, BTC (BHXH), BCA | gốc-OCR | [VB 219523](https://vanban.chinhphu.vn/?pageid=27160&docid=219523) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/1129_ttg-kgvx_16092026-signed.signed.pdf) |
| QD-384-2019-BYT | 384/QĐ-BYT (01/02/2019) | Nguyên tắc cấp mã cơ sở KCB (mã 5 ký tự) | — | Còn HL (QĐ 2733 PL01 Đ3 dẫn chiếu) | Mọi cơ sở KCB | gốc (chỉ dẫn chiếu trong QĐ 2733) | — chưa mở bản gốc |
| QD-831-2017-BYT (**mới với cụm**) | 831/QĐ-BYT (2017) | Mẫu hồ sơ quản lý sức khỏe cá nhân phục vụ chăm sóc sức khỏe ban đầu | — | Theo CSDL thứ cấp: còn HL | Trạm y tế xã, PK bác sĩ gia đình | chưa XM (chỉ thấy kết quả tìm kiếm) | — chưa kiểm tra được |
| DT-LUAT-DDXT | Dự thảo Luật Định danh và xác thực điện tử | — | QĐ 940 mục VII.1 b giao BCA trình QH "trong năm 2026" | Dự thảo | Tất cả | thứ cấp (nội dung); gốc-OCR (việc giao trình) | [luatvietnam (dự thảo), thứ cấp](https://luatvietnam.vn/tu-phap/du-thao-luat-dinh-danh-va-xac-thuc-dien-tu-2026-436278-d10.html) — chưa mở trong pha này |

Văn bản tham chiếu, không đào lại trong cụm này: TT 13/2025/TT-BYT Đ1 k3 và CV 365 PL III.1.1 a (đã có ở EMR-R05); NĐ 188/2025 Đ37, Đ38, TT 01/2025, QĐ 2555/2025 (BHYT-GD); NQ 66.7/2025/NQ-CP Đ7, NĐ 278/2025 (QĐ 31 lấy làm căn cứ, chưa đọc); QĐ 1272/QĐ-BYT 06/05/2026 (kế hoạch KSK, căn cứ của QĐ 1551, chưa đọc); TCVN 12344:2019 (ghi nhãn định danh người bệnh, tự nguyện, thứ cấp).

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### A. Liên thông Sổ SKĐT VNeID từ lượt KCB

#### SKDT-R01 — Liên thông dữ liệu Sổ SKĐT VNeID cho **mọi** người bệnh, mọi loại hình KCB
- **Căn cứ**:
  - NĐ 102 Đ10 k5 b: cơ sở y tế hoạt động hợp pháp tại Việt Nam "có trách nhiệm kết nối, chia sẻ, liên thông dữ liệu y tế liên quan với Sổ sức khỏe điện tử tích hợp trên ứng dụng định danh quốc gia". Đ23 k2: kết nối, chia sẻ, đồng bộ dữ liệu với CSDL quốc gia về y tế, CSDL BYT, CSDL y tế địa phương và Sổ SKĐT trên ứng dụng định danh quốc gia.
  - QĐ 31 Đ5: "Cơ sở khám chữa bệnh có trách nhiệm thực hiện liên thông dữ liệu Sổ sức khoẻ điện tử VNeID của tất cả các đối tượng người bệnh (theo hướng dẫn tại Quyết định số 2733/QĐ-BYT…) kể từ ngày 01/01/2026".
  - QĐ 2733 Đ2 (gốc-OCR): áp dụng cho mọi cơ sở KCB công lập và tư nhân có giấy phép, mọi loại hình (khám ngoại trú, điều trị ngoại trú, nội trú, ban ngày, kê đơn lĩnh thuốc theo hẹn, KCB từ xa). Đ4 k5 đ: liên thông lên Cổng tiếp nhận dữ liệu giám định BHYT "sau khi người bệnh kết thúc đợt khám bệnh, chữa bệnh".
- **Áp dụng cho**: BV công, BV tư, PK (cả PK không ký hợp đồng BHYT) · **Hiệu lực / hạn chót**: NĐ 102 từ 01/07/2025; QĐ 31 Đ5 từ 01/01/2026 (đã qua)
- **Mức**: BẮT BUỘC (nghĩa vụ kết nối nằm ở NĐ 102, là VBQPPL; chi tiết kỹ thuật ở QĐ 2733, QĐ 31)
- **Phần mềm phải**: (1) khi đóng một lượt KCB (kết thúc khám, ra viện, kết thúc điều trị ngoại trú/ban ngày, lĩnh thuốc theo hẹn, phiên KCB từ xa) tự sinh gói dữ liệu Sổ SKĐT và đưa vào hàng đợi gửi; (2) áp dụng cho cả lượt viện phí, dịch vụ, không chỉ lượt BHYT; (3) lưu trạng thái gửi theo từng lượt (`chua_gui | da_gui | loi | gui_lai`) và mã phản hồi; (4) báo cáo được tỷ lệ lượt đã liên thông theo loại hình và theo BHYT/không BHYT (phục vụ SKDT-R20).
- **Ghi chú / bẫy**: QĐ 31 ký ngày 06/01/2026 nhưng Đ5 lấy mốc 01/01/2026. QĐ 2733 tự gọi là "thí điểm" và Đ3 gắn lộ trình với QĐ 4750 cho cơ sở có KCB BHYT; QĐ 31 Đ5 mở rộng ra "tất cả các đối tượng người bệnh". Không có căn cứ để vendor tự loại lượt không BHYT. Nhà thuốc nằm trong khái niệm "cơ sở y tế" của NĐ 102 nhưng dữ liệu bán thuốc đi theo kênh dược (cụm DUOC), không theo kênh Sổ SKĐT (suy luận).

#### SKDT-R02 — Kênh và chuẩn dữ liệu cho lượt KCB: XML đầu ra lên Cổng giám định BHYT, ký số
- **Căn cứ**:
  - QĐ 1332 Đ3 (gốc-OCR): chuẩn và định dạng liên thông Sổ SKĐT thực hiện theo chuẩn dữ liệu đầu ra phục vụ quản lý, giám định, thanh toán chi phí KCB.
  - QĐ 2733 PL01 Đ1 k2–3: dữ liệu theo QĐ 130 và QĐ 4750; dùng Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định BHYT của BHXH VN để liên thông. PL01 Đ4 k2–3: phần mềm phải ghi nhận được thông tin Sổ SKĐT và được cấu hình liên thông theo QĐ 130/4750; có chữ ký số, chứng thư số của cơ sở để ký trước khi gửi. PL01 Đ5: 7 bước, gồm Bước 1 đăng ký mã liên thông, Bước 2 tài khoản Cổng, Bước 6 ký số và gửi sau khi người bệnh kết thúc đợt KCB, Bước 7 BHXH trích xuất dữ liệu theo QĐ 1332 và hiển thị lên VNeID "trong vòng 24 giờ kể từ khi nhận được dữ liệu".
  - QĐ 2733 PL02: bảng ánh xạ từng trường Sổ SKĐT sang bảng và trường XML (Bảng 1 tổng hợp, Bảng 2 thuốc, Bảng 3 DVKT, Bảng 4 CLS, Bảng 8 tóm tắt HSBA).
  - CV 4395/BYT-KCB (thứ cấp): người bệnh không dùng thẻ BHYT gửi **Bảng 1 và Bảng 8** theo QĐ 130; cơ sở chưa ký hợp đồng BHYT đăng ký với BHXH địa phương trước khi gửi.
- **Áp dụng cho**: BV công, BV tư, PK · **Hiệu lực**: như R01
- **Mức**: BẮT BUỘC (kênh Cổng BHXH, chuẩn XML, ký số) · BẮT BUỘC? (bộ bảng tối thiểu cho lượt không BHYT, vì CV 4395 mới đọc qua bản thứ cấp và QĐ 130 đã được sửa)
- **Phần mềm phải**: sinh XML từ cùng nguồn dữ liệu với hồ sơ BHYT (xem BHYT-DATA-R01, R07); với lượt không BHYT tối thiểu sinh Bảng 1 và Bảng 8, để trống trường đặc thù BHYT (`MA_THE_BHYT`, mức hưởng…); ký số bằng chứng thư của cơ sở; gửi qua Cổng tiếp nhận dữ liệu giám định BHYT; lưu bằng chứng gửi.
- **Ghi chú / bẫy**: Theo BHYT-DATA-R01, ghi chú bảng 2023 chỉ yêu cầu XML8 cho nội trú, nội trú ban ngày, lưu TYT/PKĐKKV. Nhưng QĐ 2733 PL02 lấy phần "tóm tắt quá trình điều trị" (mục 3.6, trường 41–45) từ **Bảng 8**. Nếu không gửi Bảng 8 cho lượt ngoại trú, Sổ SKĐT của người bệnh sẽ thiếu tóm tắt. Đây là xung đột giữa hai văn bản. Chưa có văn bản nào phân xử. Khuyến nghị cho phép cấu hình "gửi XML8 cho mọi lượt" (suy luận).

#### SKDT-R03 — Nội dung tối thiểu của Sổ SKĐT, chất lượng phần tóm tắt và bản PDF cho người bệnh
- **Căn cứ**: QĐ 31 Đ2 k3 (gốc): 4 nhóm trường được chia sẻ: (a) hành chính (họ tên, ngày sinh, giới tính, dân tộc, quốc tịch, nghề nghiệp; số định danh cá nhân hoặc số CCCD, điện thoại; mã thẻ BHYT, nơi ĐKKCB ban đầu, hạn thẻ; địa chỉ chi tiết; họ tên, quan hệ, số định danh, điện thoại của người đại diện hợp pháp); (b) tiền sử dị ứng, bệnh tật, tiêm chủng; (c) từng đợt KCB: cơ sở, thời gian, hình thức, lý do, tình trạng ra viện, kết quả điều trị, chẩn đoán ra viện, nhóm máu, chiều cao, cân nặng, kết quả CLS, thuốc, PTTT; (d) tóm tắt HSBA: tiền sử, bệnh sử, diễn biến; kết quả CLS có giá trị; phương pháp điều trị; hướng điều trị tiếp, đơn thuốc, lời dặn, lịch tái khám; bác sĩ điều trị. QĐ 1332 Phụ lục phần B: 46 trường, có cột "hiển thị". QĐ 2733 Đ4 k5 d: cơ sở đào tạo bác sĩ "thực hiện tóm tắt hồ sơ bệnh án, tóm tắt quá trình điều trị để cung cấp thông tin cho Sổ sức khỏe điện tử VNeID". QĐ 31 Đ3: người bệnh hoặc người đại diện hợp pháp được tải bản ghi chi tiết từng đợt KCB dưới dạng **PDF** qua VNeID.
- **Áp dụng cho**: BV công, BV tư, PK · **Hiệu lực**: như R01
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: có màn hình hoặc mẫu "Tóm tắt đợt điều trị" bắt buộc khi đóng lượt, gồm 4 ô tóm tắt (tiền sử và bệnh sử, CLS có giá trị, phương pháp điều trị, hướng điều trị tiếp và lịch tái khám) cùng bác sĩ điều trị và điện thoại liên hệ nếu có; chặn đóng lượt khi trống (có ngoại lệ cấu hình được cho lượt khám đơn giản); chẩn đoán ICD-10 với mã đầu tiên là bệnh chính, phân cách bằng ";" (QĐ 1332 chú thích 1, 7); nhóm máu, chiều cao, cân nặng là chỉ số theo dõi chính (QĐ 1332 III.3, đánh dấu *).
- **Ghi chú / bẫy**: Bản PDF trên VNeID do hệ thống quốc gia sinh ra từ dữ liệu cơ sở gửi, nên câu chữ tóm tắt cẩu thả sẽ hiện thẳng cho người bệnh và cơ quan TTHC (QĐ 31 Đ1 k1: có giá trị pháp lý tương đương bản giấy). Dữ liệu HIV và các nhóm nhạy cảm khác phải lọc trước khi gửi (xem SKDT-R19, DLCN-R32).

#### SKDT-R04 — Tiếp nhận bằng căn cước, số định danh cá nhân hoặc số thẻ BHYT, trên thẻ hoặc trên VNeID, cho mọi người bệnh
- **Căn cứ**: QĐ 2733 Đ4 k5 b (gốc-OCR): cơ sở "thực hiện tiếp nhận khám, chữa bệnh bằng một trong các số định danh sau: Thẻ Căn cước, Số định danh cá nhân, Số thẻ BHYT cho tất cả đối tượng người bệnh". PL01 Đ2: người bệnh không có thẻ BHYT dùng số thẻ căn cước hoặc số định danh cá nhân (trên thẻ cứng hoặc trên VNeID) làm số định danh người bệnh để liên thông Sổ SKĐT. PL01 Đ5 bước 4: tiếp nhận "trên thẻ nhựa hoặc trên VNeID". Luật Căn cước Đ20 k3: thẻ căn cước hoặc số định danh cá nhân dùng để kiểm tra thông tin trong CSDL quốc gia về dân cư và các CSDL khác.
- **Áp dụng cho**: BV công, BV tư, PK · **Hiệu lực**: từ 17/09/2024 (QĐ 2733); bao trùm mọi người bệnh từ 01/01/2026 (QĐ 31 Đ5)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: màn hình tiếp đón có một ô tìm người bệnh nhận được số định danh 12 số, số thẻ BHYT hoặc dữ liệu quét QR căn cước; với người bệnh viện phí vẫn thu số định danh (không chỉ họ tên, ngày sinh). Phần BHYT (xuất trình bằng VNeID mức 2, VssID, thẻ giấy, trẻ dưới 6 tuổi) xem **BHYT-GD-R01, R03, R05**, không lặp ở đây.
- **Ghi chú / bẫy**: QĐ 826 (bảng mục tiêu, dòng 5) đặt chỉ tiêu "tỷ lệ bệnh viện, trường học triển khai thanh toán không dùng tiền mặt; sử dụng thẻ căn cước thay thế thẻ BHYT": **50% năm 2026, 80% năm 2030** (đã đối chiếu ảnh bản gốc). Đó là chỉ tiêu quản lý, không phải hạn chót của cơ sở. Nghĩa vụ chấp nhận căn cước thay thẻ BHYT nằm ở NĐ 188 Đ37 (BHYT-GD-R01).

#### SKDT-R05 — Mã định danh y tế của cá nhân = số định danh cá nhân; khóa liên thông của MPI
- **Căn cứ**: NĐ 102 Đ6: "Sử dụng số định danh cá nhân của công dân Việt Nam và người nước ngoài đã được cấp tài khoản định danh điện tử theo quy định pháp luật về căn cước làm mã định danh y tế của cá nhân." Đ14 k4 a: "mã định danh y tế của cá nhân" là một trường của CSDL quốc gia về y tế. Luật Căn cước Đ12 k1–2: số định danh cá nhân của công dân VN là dãy **12 chữ số** do CSDL quốc gia về dân cư xác lập, không lặp lại ở người khác. NĐ 69 Đ5 k2: số định danh của người nước ngoài là dãy số tự nhiên duy nhất do hệ thống định danh xác lập. MPI trong HSBA: EMR-R05 (TT 13 Đ1 k3, CV 365 PL III.1.1 a).
- **Áp dụng cho**: mọi cơ sở y tế · **Hiệu lực**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trường `so_dinh_danh` riêng (không gộp với số hộ chiếu, CMND 9 số), kiểm tra 12 chữ số cho công dân VN; ràng buộc duy nhất có điều kiện (`UNIQUE WHERE so_dinh_danh IS NOT NULL AND trang_thai='hieu_luc'`); giữ mã người bệnh nội bộ (`MA_BN`) song song; mọi bản tin liên thông (XML, KSK, đơn thuốc) lấy số định danh từ MPI, không cho nhập tự do ở từng phân hệ.
- **Ghi chú / bẫy**: Câu chữ Đ6 chỉ tính người nước ngoài **đã có tài khoản định danh điện tử**. Khách du lịch ngắn ngày không có tài khoản nên không có mã định danh y tế (xem R12). Không có quy định về thuật toán chữ số kiểm tra của số định danh trong các văn bản đã đọc. Đừng tự chế thuật toán kiểm tra ngoài độ dài và kiểu số (suy luận).

#### SKDT-R06 — Chấp nhận dữ liệu VNeID và Sổ SKĐT thay giấy; không đòi bản giấy trùng thông tin
- **Căn cứ**: QĐ 31 Đ1 k1: dữ liệu Sổ SKĐT VNeID đã liên thông và hiển thị trên VNeID "có giá trị pháp lý tương đương bản giấy". Đ1 k2: cơ sở KCB "không yêu cầu cá nhân, tổ chức cung cấp bản giấy nếu đã có đầy đủ thông tin trên VNeID". QĐ 2733 PL01 Đ6 bước 3 (gốc-OCR): thông tin cá nhân, số định danh, thẻ BHYT, lịch sử KCB, phiếu hẹn, giấy chuyển tuyến trên VNeID có giá trị như bản giấy. NĐ 102 Đ10 k5 c: cơ sở y tế, công dân, người nước ngoài có tài khoản định danh được dùng Sổ SKĐT để thay giấy tờ trong phòng bệnh, KCB. NĐ 69 Đ9 k6, Luật Căn cước Đ22 k3 và Đ33 k1: thông tin tích hợp trên căn cước hoặc tài khoản định danh có giá trị tương đương xuất trình giấy tờ.
- **Áp dụng cho**: BV công, BV tư, PK · **Hiệu lực**: 06/01/2026 (QĐ 31)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không đặt trường bắt buộc "ảnh hoặc scan sổ khám, giấy ra viện, giấy chuyển tuyến" khi người bệnh trình VNeID; có lựa chọn ghi nhận "đã đối chiếu trên VNeID" (người xem, thời điểm, loại giấy tờ) thay cho file đính kèm; bác sĩ xem được lịch sử KCB do người bệnh xuất trình mà không phải nhập lại thủ công (nhập lại khi cần thì ghi rõ nguồn là "VNeID do người bệnh xuất trình").
- **Ghi chú / bẫy**: Phần mềm của cơ sở **không** kéo được Sổ SKĐT trực tiếp từ VNeID. Các văn bản đã đọc chỉ mô tả cách người bệnh tự mở app cho bác sĩ xem (QĐ 2733 PL01 Đ6). Hướng dẫn kết nối của "cơ quan quản lý CSDL Sổ SKĐT VNeID" (QĐ 31 Đ4 k2) chưa tìm thấy (mục 7).

#### SKDT-R07 — Khai thác thông tin căn cước đúng luật: QR, số cũ, ưu tiên căn cước điện tử
- **Căn cứ**: Luật Căn cước Đ20 k3 (đoạn 2): khi đã xuất trình thẻ căn cước thì cơ quan, tổ chức, cá nhân "không được yêu cầu người được cấp thẻ xuất trình giấy tờ hoặc cung cấp thông tin đã được in, tích hợp vào thẻ căn cước". Đ33 k2: nếu thông tin trên thẻ hoặc trong chip khác với căn cước điện tử thì dùng thông tin trong căn cước điện tử. NĐ 70 Đ12 k1: số CMND 9 số và số định danh đã hủy được mã hóa trong mã QR trên thẻ căn cước; tổ chức quét QR để dùng và "không được yêu cầu công dân phải cung cấp xác nhận số chứng minh nhân dân 09 số, số định danh cá nhân đã hủy". Luật Căn cước Đ22 k5: khai thác thông tin tích hợp **được mã hóa trong chip** phải dùng thiết bị chuyên dụng; tổ chức không phải cơ quan nhà nước chỉ được khai thác khi công dân đồng ý (điểm d).
- **Áp dụng cho**: BV công, BV tư, PK, app y tế · **Hiệu lực**: 01/07/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hỗ trợ quét QR căn cước để điền hồ sơ và lưu cả số CMND cũ, số định danh cũ (nếu có) làm định danh phụ để ghép hồ sơ cũ; không bắt người bệnh nộp "giấy xác nhận số CMND"; nếu đọc chip bằng đầu đọc thì có bước ghi nhận đồng ý của người bệnh (tổ chức tư nhân) và dùng thiết bị đáp ứng quy định kỹ thuật của BCA (Luật Căn cước Đ32 k2); khi thông tin thẻ lệch với VNeID thì lấy theo VNeID và ghi vết.
- **Ghi chú / bẫy**: Luật cấm đòi giấy tờ trùng thông tin trên thẻ. Vì vậy quy trình "photo CCCD hai mặt" ở quầy tiếp đón vừa thừa, vừa tạo thêm kho ảnh căn cước. Ảnh thẻ căn cước là dữ liệu nhạy cảm theo NĐ 356 Đ4 k1 i (DLCN, ghi chú mục R01). Tiêu chuẩn kỹ thuật cụ thể của "thiết bị chuyên dụng" (thông tư BCA) chưa đọc.

#### SKDT-R08 — Xác thực người bệnh qua CSDL dân cư hoặc hệ thống định danh: ai được kết nối trực tiếp, ai phải qua bên trung gian
- **Căn cứ**:
  - NĐ 69 Đ18 k1: cơ quan nhà nước, tổ chức chính trị, chính trị - xã hội, **tổ chức cung cấp dịch vụ công** được kết nối HTTT của mình với hệ thống định danh và xác thực điện tử, với điều kiện HTTT đạt **an toàn cấp độ 3** trở lên. k2: phải thống nhất bằng văn bản với cơ quan quản lý định danh (C06), nêu rõ phạm vi và mục đích. k3: thẩm định trong 30 ngày, hoặc 07 ngày làm việc nếu đã kết nối CSDL dân cư. **k4: tổ chức khác kết nối "thông qua tổ chức cung cấp dịch vụ xác thực điện tử"**.
  - NĐ 69 Đ19 k3: tổ chức, cá nhân không thuộc k2 yêu cầu xác thực qua dịch vụ của tổ chức cung cấp dịch vụ xác thực, và phải được chủ thể đồng ý qua VNeID, SMS số chính chủ hoặc hình thức khác. **k4: không được cung cấp, chia sẻ kết quả xác thực cho tổ chức khác; kết quả xác thực không có giá trị làm yếu tố xác thực trong giao dịch khác.**
  - NĐ 69 Đ22–23: dịch vụ xác thực điện tử là ngành nghề kinh doanh có điều kiện, chỉ **đơn vị sự nghiệp công lập hoặc doanh nghiệp trong Công an nhân dân** được cấp phép. NĐ 69 Đ20: 4 mức xác thực (mức 3 có 1 yếu tố sinh trắc; mức 4 gồm sinh trắc, vật sở hữu và yếu tố biết).
  - NĐ 70 Đ7 k2: HTTT của cơ quan nhà nước kết nối CSDL dân cư phải đạt chuẩn kỹ thuật và an toàn tối thiểu cấp độ 3; Đ7 k4: C06 từ chối hoặc ngừng kết nối khi vi phạm BVDLCN. NĐ 70 Đ8 k2, k4, k5 và Luật Căn cước Đ10 k8: tổ chức khác khai thác thông tin CSDL dân cư khi **được cơ quan quản lý căn cước và chính công dân đồng ý**.
  - NĐ 69 Đ21 k2: xác thực tài khoản tại nơi giao dịch dùng giải pháp xác thực cung cấp trên ứng dụng định danh quốc gia.
- **Áp dụng cho**: BV công, BV tư, PK, vendor HIS/app · **Hiệu lực**: 01/07/2024
- **Mức**: BẮT BUỘC (cấm kết nối trực tiếp trái điều kiện; cấm chia sẻ lại kết quả xác thực) · BẮT BUỘC? (bệnh viện công có được coi là "tổ chức cung cấp dịch vụ công" để kết nối trực tiếp hay không: chưa có văn bản giải thích)
- **Phần mềm phải**: (1) vendor HIS hoặc app tư nhân **không** tự kết nối CSDL dân cư hoặc hệ thống định danh. Chỉ tích hợp qua tổ chức cung cấp dịch vụ xác thực được BCA cấp phép, hoặc qua giải pháp trên app VNeID; (2) với luồng xác thực qua dịch vụ trung gian phải có bước người bệnh xác nhận đồng ý (trên VNeID hoặc SMS) và lưu bằng chứng; (3) không chuyển kết quả xác thực cho bên thứ ba (bảo hiểm tư, đối tác) và không dùng lại kết quả đó làm "đăng nhập" cho giao dịch khác; (4) nếu bệnh viện công kết nối trực tiếp thì HTTT phải có hồ sơ cấp độ 3 (cụm ANM) và văn bản thống nhất với C06.
- **Ghi chú / bẫy**: Câu quảng cáo "tích hợp xác thực VNeID/CSDL dân cư" của vendor nhỏ cần kiểm tra họ đi qua đơn vị trung gian nào và có văn bản hay hợp đồng không. Tra thẻ BHYT trên Cổng BHXH (BHYT-GD-R02) là kênh khác, không phải xác thực danh tính theo NĐ 69.

#### SKDT-R09 — Lưu nguồn định danh và nguồn xác thực của từng lượt (provenance)
- **Căn cứ**: QĐ 2733 PL01 Đ5 bước 4 (tiếp nhận bằng số thẻ BHYT, căn cước, số định danh, trên thẻ nhựa hoặc VNeID); NĐ 69 Đ19 k4 (kết quả xác thực không làm yếu tố xác thực giao dịch khác); Luật Căn cước Đ33 k2 (căn cước điện tử được ưu tiên khi lệch); BHYT-GD-R02 (lưu phản hồi tra cứu thẻ).
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: —
- **Mức**: NÊN (không văn bản nào buộc lưu "nguồn xác thực", nhưng cần làm bằng chứng cho R04, R06, R07, R08)
- **Phần mềm phải**: với mỗi lượt lưu `phuong_thuc_dinh_danh` (QR_CCCD | CHIP_CCCD | VNEID_APP | DICH_VU_XAC_THUC | TRA_CUU_BHXH | NHAP_TAY | CHUA_XAC_DINH), mức tin cậy, người thực hiện, thời điểm, mã giao dịch hoặc mã phản hồi (không lưu ảnh căn cước nếu không cần).
- **Ghi chú / bẫy**: NĐ 69 Đ17 k2 (lịch sử truy cập lưu ≥05 năm) và Đ28 k4 (lịch sử dùng căn cước điện tử lưu 05 năm) là nghĩa vụ của **hệ thống định danh quốc gia**, không phải của HIS. Đừng trích hai điều này làm căn cứ thời hạn lưu log của bệnh viện. Thời hạn log của bệnh viện xem ANM-R11.

### B. Các trường hợp đặc biệt về định danh

#### SKDT-R10 — Người bệnh không có giấy tờ, không xác định được danh tính (vô danh)
- **Căn cứ**: Luật KCB Đ2 k10: "người bệnh không có thân nhân" gồm người cấp cứu không có giấy tờ tùy thân, không có thân nhân đi cùng, không có thông tin liên lạc; người không làm chủ được nhận thức và không có giấy tờ; người đã xác định danh tính nhưng không có thân nhân; trẻ dưới 06 tháng bị bỏ rơi. Đ72 k1: kiểm kê, lập biên bản, lưu giữ tài sản. k2: sau **48 giờ** vẫn không xác định được thân nhân thì thông báo UBND cấp xã để tìm thân nhân trên phương tiện thông tin đại chúng; lập hồ sơ chuyển trẻ bị bỏ rơi vào cơ sở trợ giúp xã hội. Đ73 k1 b, k2 a–b: tử vong không có giấy tờ thì thông báo UBND xã trong **24 giờ**; lấy và lưu mẫu thi thể để xác định nhân thân.
- **Áp dụng cho**: BV công, BV tư, PK có cấp cứu · **Hiệu lực**: 01/01/2024
- **Mức**: BẮT BUỘC (quy trình Đ72, Đ73) · NÊN (cách đánh mã tạm)
- **Phần mềm phải**: tạo hồ sơ "chưa xác định danh tính" bằng mã tạm có quy tắc (ví dụ `VD-<mã cơ sở>-<yyyymmdd>-<seq>`), giới tính và tuổi ước lượng, đặc điểm nhận dạng, ảnh nếu quy chế cho phép; đồng hồ 48 giờ cảnh báo nghĩa vụ thông báo UBND xã; biên bản kiểm kê tài sản gắn với hồ sơ; khi xác định được danh tính thì **gộp** về hồ sơ có số định danh (giữ mã tạm làm alias, ghi vết người gộp, lý do); chỉ gửi dữ liệu Sổ SKĐT khi đã có định danh hợp lệ hoặc gửi lại sau khi gộp (suy luận: Sổ SKĐT gắn với số định danh hoặc mã thẻ BHYT nên bản tin không có định danh sẽ không vào được sổ của ai).
- **Ghi chú / bẫy**: Người bệnh vô danh vẫn phải được cấp cứu. Đừng để ô "số định danh bắt buộc" chặn việc mở hồ sơ cấp cứu.

#### SKDT-R11 — Trẻ em chưa có số định danh, trẻ dưới 14 tuổi và vai trò người giám hộ
- **Căn cứ**:
  - NĐ 70 Đ11 k2–3 (gốc-OCR): số định danh của công dân được **xác lập khi đăng ký khai sinh**. CSDL hộ tịch chuyển thông tin cho CSDL dân cư, hệ thống tự kiểm tra, xác lập và chuyển ngay số định danh cho cơ quan hộ tịch. Trước khi đăng ký khai sinh, trẻ chưa có số.
  - Luật Căn cước Đ19 k3: dưới 14 tuổi được cấp thẻ căn cước theo nhu cầu. NĐ 69 Đ7 k1: dưới 6 tuổi có thẻ căn cước thì chỉ được tài khoản mức 1; từ đủ 6 đến dưới 14 tuổi được mức 1 hoặc 2 khi có nhu cầu. Đ14 k2: người dưới 14 tuổi dùng tài khoản phải có đồng ý của người đại diện, giám hộ qua VNeID; người đại diện dùng tài khoản đó thay mặt trẻ.
  - QĐ 2733 PL01 Đ7 k3: người giám hộ, người nuôi dưỡng chính, người đại diện hợp pháp được quản lý Sổ SKĐT VNeID của trẻ em, người già, người khuyết tật và người thuộc Luật KCB Đ15 k1 b khi họ không tự quản lý được. QĐ 1332 phần B trường 12–15 (người giám hộ, người chăm sóc chính, người đại diện: họ tên, quan hệ, số định danh, điện thoại). QĐ 2733 PL02 mục 1.3 ghi chú các trường này cần "phối hợp với C06 để thống nhất phương án xử lý": chưa có trường XML tương ứng.
  - QĐ 1551 PL01 các mẫu cho trẻ và học sinh: có `NGUOI_GIAM_HO` và `SO_CCCD_NGH`; PL03: không có CCCD, CMND, hộ chiếu thì dùng "mã tài khoản định danh điện tử".
  - Trẻ dưới 6 tuổi đi KCB BHYT bằng giấy chứng sinh hoặc mã thẻ tạm: BHYT-GD-R01, R05.
- **Áp dụng cho**: BV/PK sản, nhi; mọi cơ sở khám trẻ em; đơn vị KSK học đường · **Hiệu lực**: 01/07/2024 (NĐ 69, 70); 31/05/2026 (QĐ 1551)
- **Mức**: BẮT BUỘC (thu thông tin người giám hộ/đại diện; dùng số định danh khi đã có) · NÊN (cách liên kết sơ sinh với mẹ)
- **Phần mềm phải**: hồ sơ sơ sinh tạo ngay khi sinh, liên kết `me_id` và số giấy chứng sinh, tạm chưa có số định danh; khi gia đình đăng ký khai sinh xong thì cập nhật số định danh (nhập tay có đối chiếu, hoặc lấy từ mã thẻ BHYT mới) và ghi vết; bảng `nguoi_dai_dien` (họ tên, quan hệ, số định danh, điện thoại, căn cứ đại diện) gắn với người bệnh; kiểm tra tuổi để biết khi nào cần đồng ý của người đại diện (liên kết DLCN-R08).
- **Ghi chú / bẫy**: Không bịa "số định danh tạm" có 12 chữ số cho trẻ. Mã tạm phải khác hẳn định dạng 12 số để không lọt vào trường `SO_CCCD` khi gửi (suy luận).

#### SKDT-R12 — Người nước ngoài và người gốc Việt chưa xác định quốc tịch
- **Căn cứ**: NĐ 102 Đ6 (người nước ngoài **đã được cấp tài khoản định danh điện tử** dùng số định danh làm mã định danh y tế). NĐ 69 Đ5 k1 (danh tính điện tử người nước ngoài gồm số định danh, họ tên, ngày sinh, giới tính, quốc tịch, số và nơi cấp hộ chiếu, ảnh mặt, vân tay), Đ7 k2 (người nước ngoài từ đủ 6 tuổi có thẻ thường trú hoặc tạm trú được cấp tài khoản mức 1, mức 2 khi có nhu cầu). NĐ 102 Đ10 k5 c (người nước ngoài có tài khoản định danh được dùng Sổ SKĐT). QĐ 2733 PL02, trường "Số định danh cá nhân/Số thẻ Căn cước" → `SO_CCCD`: ghi số căn cước, CMND hoặc **hộ chiếu**; không có thì dùng **mã tài khoản định danh điện tử**. Quốc tịch → `MA_QUOCTICH` theo Phụ lục 2 TT 07/2016/TT-BCA (gốc-OCR). Luật Căn cước Đ30 k1, k2 c: người gốc Việt Nam chưa xác định được quốc tịch, sống liên tục từ 06 tháng tại một xã, được cấp **giấy chứng nhận căn cước** và được **xác lập số định danh cá nhân**.
- **Áp dụng cho**: BV công, BV tư, PK (nhất là cơ sở nhận khách quốc tế) · **Hiệu lực**: 01/07/2024–01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: loại giấy tờ định danh là danh mục (`CAN_CUOC | SO_DINH_DANH_NN | HO_CHIEU | GIAY_CN_CAN_CUOC | TK_DINH_DANH | KHONG_CO`) kèm số và quốc gia cấp; trường quốc tịch theo danh mục mã; người nước ngoài không có tài khoản định danh thì lưu hộ chiếu, không suy ra "mã định danh y tế"; giấy chứng nhận căn cước được coi như có số định danh cá nhân.
- **Ghi chú / bẫy**: Trường `SO_CCCD` trong XML là trường "đa năng" (căn cước, CMND, hộ chiếu, mã tài khoản định danh). Không có trường riêng cho loại giấy tờ nên phía nhận không phân biệt được. MPI nội bộ phải lưu loại giấy tờ. Không suy ra được từ XML (suy luận). TT 07/2016/TT-BCA còn hiệu lực hay không, và mã đơn vị hành chính sau sắp xếp năm 2025: chưa xác minh trong cụm này.

#### SKDT-R13 — Số định danh có thể bị hủy và xác lập lại: MPI phải giữ lịch sử
- **Căn cứ**: NĐ 70 Đ11 k7 (gốc-OCR): hủy, xác lập lại số định danh khi xác định lại giới tính, cải chính năm sinh; sai sót nơi đăng ký khai sinh, năm sinh, giới tính; dùng giấy tờ giả; giấy khai sinh bị thu hồi. k8: trường hợp a, b theo nhu cầu công dân. k11: số đã hủy được lưu và "không được sử dụng để cấp cho người khác". Đ12 k1: số đã hủy nằm trong QR căn cước.
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: 01/07/2024
- **Mức**: NÊN (văn bản buộc BCA; hệ quả với phần mềm là suy luận, nhưng thiếu thì MPI vỡ)
- **Phần mềm phải**: bảng định danh dạng lịch sử (`patient_identifier(patient_id, loai, gia_tri, hieu_luc_tu, hieu_luc_den, trang_thai, nguon)`); tìm kiếm theo cả số cũ; khi người bệnh trình căn cước có số mới thì tự đề xuất ghép với hồ sơ mang số cũ (đọc từ QR); không xóa số cũ.
- **Ghi chú / bẫy**: Ràng buộc `UNIQUE(so_dinh_danh)` cứng trên bảng người bệnh sẽ không chịu được chuyện đổi số. Nên đặt ràng buộc ở bảng định danh, chỉ trên các bản ghi đang hiệu lực.

#### SKDT-R14 — Khử trùng hồ sơ, đối soát theo mã định danh, dữ liệu "đúng, đủ, sạch, sống"
- **Căn cứ**: QĐ 1551 mục 3 e: dữ liệu đồng bộ phải "đúng, đủ, sạch, sống" và được ký số. CV 1129 mục 4 (gốc-OCR): BCA hỗ trợ "đối soát theo mã định danh cá nhân để xác định chính xác người đã được khám, hạn chế thống kê trùng"; mục 1 b: tránh một người bị xếp vào nhiều nhóm và bị khám, thanh toán trùng. Luật Căn cước Đ11 k4: thông tin trong CSDL chuyên ngành không thống nhất với CSDL dân cư thì phối hợp kiểm tra và điều chỉnh. NĐ 102 Đ24 k1: tổ chức, cá nhân thông báo kịp thời khi dữ liệu phản ánh mình có sai sót. EMR-R05 (CV 365: mỗi người bệnh một mã định danh đơn nhất).
- **Áp dụng cho**: mọi cơ sở; đơn vị KSK · **Hiệu lực**: —
- **Mức**: BẮT BUỘC? (có căn cứ về chất lượng dữ liệu và chống trùng, nhưng chưa có tiêu chí kiểm chứng)
- **Phần mềm phải**: thuật toán cảnh báo trùng khi tạo mới (cùng số định danh; hoặc cùng họ tên chuẩn hóa, ngày sinh, giới tính, SĐT); hàng đợi rà soát trùng cho người quản trị; gộp hoặc tách có log và có thể hoàn tác; báo cáo số hồ sơ không có số định danh.

### C. Dữ liệu khám sức khỏe định kỳ và sàng lọc (QĐ 1551)

#### SKDT-R15 — Thu thập dữ liệu KSK theo 17 mẫu đặc tả và gửi trong 24 giờ, có ký số
- **Căn cứ**: QĐ 1551 HD mục 3 b: cơ sở có phần mềm KSK nhập dữ liệu vào phần mềm, trường thông tin "tuân thủ kiểu và định dạng dữ liệu quy định tại Phụ lục 01". Mục 3 c: chưa có phần mềm thì dùng Cổng dữ liệu sức khỏe `https://csdlksk.vn`. Mục 3 d: dữ liệu khám trước ngày hướng dẫn phải rà soát và đồng bộ **trước 15/7/2026**. Mục 4 a: "Trong vòng **24 giờ** sau khi kết thúc đợt khám cho người dân" liên thông về CSDL sức khỏe cá nhân của BYT (thủ công trên csdlksk.vn hoặc tự động theo PL02); "phải ký số trước khi đồng bộ". PL01: 17 mẫu (giấy KSK 6 đến dưới 18 tuổi; từ 18 tuổi; sổ KSK lái xe; nhân viên đường sắt; thuyền viên; trẻ 0 đến dưới 2 tháng, 2–3, 4–6, 7–9, 10–12, 13–18, 19 đến dưới 24 tháng, 2 đến dưới 6 tuổi; học sinh 3 tháng đến dưới 6 tuổi; lớp 1–5; lớp 6–9; lớp 10–12). Mỗi mẫu có `CKS_NGUOI_KET_LUAN`, `CKS_BENH_VIEN` và nhiều mẫu có `CKS_NGUOI_KHAM` cho từng chuyên khoa. Trường hành chính "ghi theo hướng dẫn tại QĐ 3176/QĐ-BYT". Có `DOI_TUONG` (14 mã: người cao tuổi, khuyết tật, hộ nghèo, …, người lao động, khác) và `NGUON_KINH_PHI` (NSTW, NSĐP, Quỹ BHYT, người sử dụng lao động, xã hội hóa, khác).
- **Áp dụng cho**: mọi cơ sở KCB tổ chức KSK định kỳ hoặc khám sàng lọc, công và tư (CT 17 lồng ghép cơ sở ngoài công lập đủ điều kiện) · **Hiệu lực / hạn chót**: 31/05/2026; dữ liệu cũ: 15/07/2026 (đã qua); thường xuyên: 24 giờ
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mô hình phiếu KSK theo 17 mẫu (mỗi mẫu một schema có phiên bản), đúng tên chỉ tiêu, kiểu, độ dài; mã ICD-10 nhiều mã phân cách ";"; chữ ký số của từng bác sĩ khám chuyên khoa, người kết luận và cơ sở; xác định "kết thúc đợt khám" (đóng đợt hoặc đóng phiếu) để chạy đồng hồ 24 giờ; cảnh báo quá hạn; chế độ đồng bộ lô cho dữ liệu tồn; lưu `DOI_TUONG` và `NGUON_KINH_PHI` vì CV 1129 yêu cầu phân định nguồn kinh phí, tránh thanh toán trùng.
- **Ghi chú / bẫy**: (1) "24 giờ sau khi kết thúc **đợt** khám" chưa định nghĩa đợt là cả chiến dịch hay từng người. Thận trọng thì tính theo từng phiếu đã kết luận (suy luận). (2) Mẫu KSK lái xe trong QĐ 1551 trùng phạm vi với luồng KSK lái xe ↔ CSDL giao thông (TT 36/2024, nửa còn lại của K4). Có thể phải gửi hai nơi; chưa xác minh. (3) Phụ lục 01 **không có cột "bắt buộc"**. Chỉ PL03 (bản tin BHXH) nói trường không bắt buộc để NULL. Danh sách trường bắt buộc của bản tin cơ sở gửi chưa rõ (mục 7).

#### SKDT-R16 — Đăng ký tài khoản liên thông, mã định danh cơ sở 13 chữ số và tài khoản định danh tổ chức
- **Căn cứ**: QĐ 1551 HD mục 2 a: mỗi cơ sở được cấp **01 tài khoản liên thông dữ liệu** và **01 tài khoản quản trị** trên Cổng dữ liệu sức khỏe. Mục 2 b: đăng ký trên Hệ thống quản lý quốc gia về hành nghề và hoạt động KCB `https://app.qlhanhnghekcb.gov.vn/`; Sở Y tế hoặc BYT phê duyệt; hệ thống gửi thông tin đăng nhập qua email "đồng thời cấp **mã định danh 13 chữ số** cho cơ sở khám bệnh, chữa bệnh"; cơ sở "có trách nhiệm đăng ký **tài khoản định danh tổ chức** theo hướng dẫn của Bộ Công an". NĐ 69 Đ7 k3: cơ quan, tổ chức thành lập hoặc đăng ký hoạt động tại VN được cấp tài khoản định danh điện tử không phân mức. Đ6: danh tính điện tử tổ chức gồm số định danh tổ chức, tên, mã số thuế, người đại diện… NĐ 69 Đ40 k4: tài khoản tổ chức do Cổng DVC hoặc hệ thống TTHC cấp chỉ dùng đến 30/06/2025.
- **Áp dụng cho**: mọi cơ sở KCB có KSK; vendor quản lý cấu hình · **Hiệu lực**: 31/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấu hình theo cơ sở (đa tenant): mã 13 chữ số, tài khoản liên thông (username/password lưu trong kho bí mật, không hard-code), chứng thư số tổ chức; tách tài khoản quản trị (dùng trên web) khỏi tài khoản liên thông (dùng cho máy); hỗ trợ xoay mật khẩu.
- **Ghi chú / bẫy**: QĐ 1551 chỉ cấp **một** tài khoản liên thông cho mỗi cơ sở. Chuỗi phòng khám nhiều điểm (mỗi điểm một giấy phép) cần một tài khoản cho mỗi cơ sở, không dùng chung (suy luận từ "mỗi cơ sở").

#### SKDT-R17 — API Trục dữ liệu BYT (PL02 QĐ 1551): xác thực, đóng gói, ký, xử lý phản hồi
- **Căn cứ**: QĐ 1551 PL02 (gốc):
  - Mục 1: RESTful API, HTTPS, JSON (UTF-8), xác thực OAuth2 và Bearer Token.
  - Mục 2.1, môi trường: Cổng dữ liệu sức khỏe BYT `https://csdlksk.vn` (sandbox `https://sandbox-csdlksk.vn`); **"Trục dữ liệu Bộ Y tế"**: admin `https://admin.emrhub.vn`, API `https://api.emrhub.vn` (sandbox `https://admin-sandbox.emrhub.vn`, `https://api-sandbox.emrhub.vn`).
  - Mục 3–4: `POST /api/auth/login` (username, password của "Agent Account") trả `token`, `refresh_token`, `duration` (giây), `role` (`facility` hoặc `department`). `POST /api/platform/data-sync/push` với header `Authorization: Bearer …`, `service-type: 100`. Body gồm: `header.version`, `sender_id` (13 số mã định danh cơ sở), `receiver_id` (ví dụ `TDLBYT`), `txn_type = sync_checkup`, `msg_id` = sender_id + YYMMDD + UUIDv4 bỏ gạch, `msg_type = 101`, `data_type` (`xml/base64` | `json/base64` | `png/base64` | `jpg/base64` | `pdf/base64`), `send_datetime` (Unix ms 13 số); `data` là file đã mã hóa Base64; `signature` là chữ ký checksum **SHA256RSA** trên header và data.
  - Phản hồi: HTTP 200/400/401/403/404/500/504; `res_code` `CM_SUCCESS` | `CM_INVALID_REQUEST` | `PS_SIGNATURE_INVALID`; `msg_type 102`; `ref_msg_id`; `data.data_state`, `message_check_ca`, `message_notify`; có `signature` của bên nhận. Mục 5: ví dụ JSON và XML cho 13 mẫu. Ví dụ XML có `CKS_BENH_VIEN` là phần tử XMLDSig.
- **Áp dụng cho**: cơ sở chọn đồng bộ tự động; vendor phần mềm KSK · **Hiệu lực**: 31/05/2026
- **Mức**: BẮT BUỘC (khi dùng kênh tự động)
- **Phần mềm phải**: client cấp và làm mới token; sinh `msg_id` đúng mẫu và dùng làm khóa idempotent; ký XMLDSig nội dung phiếu và ký SHA256RSA cho gói tin; lưu nguyên request, response và chữ ký phản hồi; phân loại lỗi (`PS_SIGNATURE_INVALID` là lỗi cấu hình chứng thư, không thử lại mù quáng; 5xx thì thử lại có backoff); chạy thử trên sandbox trước khi bật production; danh sách cho phép (allowlist) tên miền đúng như PL02.
- **Ghi chú / bẫy**: **MT-29 đã giải quyết**: emrhub.vn **chính là "Trục dữ liệu Bộ Y tế"** theo bản gốc PL02. Ba địa chỉ không thay thế nhau mà mỗi cái một vai trò: `app.qlhanhnghekcb.gov.vn` để đăng ký và lấy mã 13 số; `csdlksk.vn` là cổng web nhập tay hoặc quản trị; `api.emrhub.vn` là API đẩy dữ liệu. Tên miền emrhub.vn không phải gov.vn, nên khi triển khai phải kiểm tra chứng chỉ TLS và đối chiếu với văn bản. Không lấy endpoint từ bài báo hay email lạ (chống giả mạo). Bảng thuộc tính trong PL02 đánh số trùng (1.5, 1.6 lặp lại). Đặt tên trường theo bảng, đừng theo số thứ tự.

#### SKDT-R18 — Hai hệ mã cơ sở: mã 5 ký tự (BHXH, QĐ 384/2019) và mã 13 ký tự (GLN, QĐ 1551)
- **Căn cứ**: QĐ 2733 PL01 Đ3: dùng mã cơ sở theo QĐ 384/QĐ-BYT ngày 01/02/2019 làm số định danh cơ sở khi liên thông Sổ SKĐT. QĐ 2733 Đ4 k4 b: Sở Y tế cấp mã cho cơ sở chưa có mã. QĐ 1551 PL01, trường `MA_CSKCB` (5 ký tự) và `MA_GTIN_CSKCB` ("theo chuẩn GLN", **13 ký tự**); PL02 `sender_id` = 13 số mã định danh cơ sở.
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: —
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục cơ sở lưu cả hai mã, kiểm tra độ dài (5 và 13); bản tin BHXH và Sổ SKĐT qua XML dùng mã 5 ký tự; bản tin KSK dùng cả hai, `sender_id` dùng mã 13.
- **Ghi chú / bẫy**: Thống nhất với BHYT-DATA-R24: không trộn hai mã. Inventory có câu "mã định danh cơ sở KCB 13 số": căn cứ duy nhất tìm được là QĐ 1551. Chưa thấy văn bản riêng quy định cấu trúc mã GLN cho cơ sở KCB.

### D. Bảo mật, quản trị, báo cáo

#### SKDT-R19 — Phạm vi truy cập và chia sẻ dữ liệu Sổ SKĐT
- **Căn cứ**: QĐ 2733 PL01 Đ7 k1: thông tin trên Sổ SKĐT VNeID có chế độ bảo mật như thông tin khác trên VNeID. k2: bác sĩ điều trị, nhân viên y tế **trong quá trình KCB** cho người bệnh được truy cập, sử dụng. k4: BYT là "Bên kiểm soát" dữ liệu Sổ SKĐT VNeID; chia sẻ dữ liệu sức khỏe trên Sổ SKĐT "phải được sự đồng ý của Bộ Y tế". QĐ 31 Đ2 k2 a: khai thác phải tuân thủ Luật KCB Đ69 và Luật BVDLCN 2025. NĐ 102 Đ9 k2 b (tiếp cận thông tin sức khỏe khi người đó đồng ý), Đ10 k2 c (tổ chức khác khai thác DLCN y tế khi đơn vị quản lý dữ liệu và chủ thể cùng đồng ý), Đ23 k3 (bảo đảm ATTT khi kết nối). Liên quan: DLCN-R33, DLCN-R32 (HIV), DLCN-R01.
- **Áp dụng cho**: BV công, BV tư, PK, vendor · **Hiệu lực**: 17/09/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dữ liệu người bệnh xuất trình từ VNeID chỉ dùng cho lượt KCB hiện tại, có log ai xem; vendor không gom dữ liệu Sổ SKĐT của khách hàng vào kho dùng chung hay phân tích riêng; bộ lọc trước khi gửi cho dữ liệu cần hạn chế (đơn ARV, xét nghiệm HIV, theo DLCN-R32) và quy tắc theo cấu hình; kênh truyền TLS, ký số.
- **Ghi chú / bẫy**: Dữ liệu cơ sở gửi lên **không** còn do cơ sở kiểm soát sau khi BHXH hoặc BYT hiển thị trên VNeID (BYT là bên kiểm soát). Phần cơ sở chịu trách nhiệm là tính đúng của dữ liệu gửi và việc lọc trước khi gửi.

#### SKDT-R20 — Báo cáo định kỳ 6 tháng về liên thông Sổ SKĐT
- **Căn cứ**: QĐ 2733 PL01 Đ8 (gốc-OCR, đã đối chiếu ảnh): cơ sở KCB báo cáo **6 tháng 1 lần** trên trang báo cáo trực tuyến của Cục QLKCB (`cdc.kcb.vn`): bảng theo 6 loại hình (khám ngoại trú, điều trị ngoại trú, lĩnh thuốc theo hẹn, nội trú, ban ngày, KCB từ xa) × {có BHYT, không BHYT} × {số lượt, đã liên thông}; kèm khó khăn và kiến nghị. CV 1129 mục 1 g: UBND tỉnh báo cáo **hằng tháng** về BYT số người đã khám theo nhóm, nguồn kinh phí, mức độ cập nhật dữ liệu.
- **Áp dụng cho**: BV công, BV tư, PK (QĐ 2733); đơn vị KSK theo phân công của tỉnh (CV 1129) · **Hiệu lực**: 17/09/2024; 16/09/2026
- **Mức**: BẮT BUỘC? (QĐ 2733 là hướng dẫn "thí điểm"; QĐ 31 dẫn chiếu nhưng không nhắc lại Đ8)
- **Phần mềm phải**: báo cáo dựng sẵn đúng ma trận Đ8 lấy từ trạng thái gửi của R01; báo cáo KSK theo `DOI_TUONG` × `NGUON_KINH_PHI` × trạng thái đồng bộ.

#### SKDT-R21 — Quy chế và quy trình Sổ SKĐT tại cơ sở; người phụ trách
- **Căn cứ**: QĐ 2733 Đ4 k5 a: lập kế hoạch, phân công cán bộ chuyên môn xây dựng quy trình ghi nhận, phân công cán bộ CNTT xây dựng quy trình liên thông, giám sát chất lượng dữ liệu. PL01 Đ4 k4–5: bảo đảm ANM và bảo mật khi kết nối; có quy chế sử dụng và quy trình triển khai Sổ SKĐT VNeID được thủ trưởng cơ sở phê duyệt.
- **Áp dụng cho**: BV công, BV tư, PK · **Hiệu lực**: 17/09/2024
- **Mức**: BẮT BUỘC? (văn bản thí điểm, nghĩa vụ tổ chức hơn là phần mềm)
- **Phần mềm phải**: vendor cung cấp mẫu quy trình và tài liệu cấu hình; phần mềm có màn hình giám sát chất lượng dữ liệu (lượt thiếu tóm tắt, thiếu số định danh, lỗi gửi).

#### SKDT-R22 — Ghi đủ thông tin người đại diện hợp pháp và nơi quản lý hồ sơ
- **Căn cứ**: QĐ 31 Đ2 k3 a (họ tên, quan hệ, số định danh cá nhân, điện thoại người đại diện hợp pháp, nếu có). QĐ 1332 phần B trường 9 và chú thích 3 ("Nơi quản lý hồ sơ sức khoẻ của người bệnh"), mục 1.2 chú thích 4 (địa chỉ cư trú làm căn cứ chuyển dữ liệu về hệ thống hồ sơ sức khỏe của địa phương), mục 1.3 chú thích 5 (người đại diện được phép quản lý sổ khi chủ thể không tự quản lý được). Luật KCB Đ8 (người đại diện), dẫn qua DLCN-R08.
- **Áp dụng cho**: mọi cơ sở · **Hiệu lực**: như R01
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: địa chỉ cư trú có mã tỉnh, mã xã chuẩn (QĐ 1551 dùng `MATINH_CU_TRU` 3 ký tự, `MAXA_CU_TRU` 5 ký tự, không còn cấp huyện); thông tin người đại diện có số định danh.
- **Ghi chú / bẫy**: QĐ 2733 PL02 (2024) còn dùng `MAHUYEN_CU_TRU` theo QĐ 124/2004/QĐ-TTg. QĐ 1551 (2026) đã bỏ cấp huyện. Danh mục địa giới phải có hiệu lực theo thời gian để dữ liệu cũ vẫn hợp lệ.

### E. Định hướng sắp tới

#### SKDT-R23 — Lồng ghép KSK với KCB, tái sử dụng kết quả CLS, tránh khám và thanh toán trùng
- **Căn cứ**: CV 1129 mục 1 b (lồng ghép KSK định kỳ, sàng lọc, học đường, bệnh nghề nghiệp, người lao động, KCB BHYT; "sử dụng và kế thừa kết quả khám còn giá trị lâm sàng"); mục 1 d (kết nối dữ liệu KSK với dữ liệu KCB BHYT, xét nghiệm, CĐHA); mục 2 c (BYT chuẩn hóa dữ liệu, quy trình); mục 3 b (BHXH đồng bộ dữ liệu KCB BHYT lên VNeID, đối soát để ngăn thanh toán trùng). CT 17 (thứ cấp): mục tiêu đến hết năm 2026 toàn dân được khám và lập Sổ SKĐT.
- **Áp dụng cho**: cơ sở tham gia KSK · **Hiệu lực**: 16/09/2026
- **Mức**: NÊN (chỉ đạo điều hành, chưa có hướng dẫn kỹ thuật)
- **Phần mềm phải**: khi mở phiếu KSK, hiển thị CLS còn hiệu lực của chính người đó tại cơ sở (và từ nguồn liên thông khi có); đánh dấu chỉ tiêu "kế thừa" kèm nguồn; tránh tạo hai phiếu KSK cho cùng người, cùng năm, khác nhóm đối tượng.

#### SKDT-R24 — Chuẩn bị cho Luật Định danh và xác thực điện tử và VNeID mini app
- **Căn cứ**: QĐ 940 mục VII.1 b (gốc-OCR): BCA tham mưu trình QH ban hành Luật Định danh và xác thực điện tử "trong năm 2026"; mục c "Lớp ứng dụng": VNeID thành siêu ứng dụng có nền tảng cho bên thứ ba làm Mini App. Dự thảo luật (thứ cấp, inventory): 3 mức xác thực, Open API, lưu nhật ký xác thực ≥5 năm.
- **Áp dụng cho**: vendor app, HIS · **Hiệu lực**: dự thảo
- **Mức**: NÊN
- **Phần mềm phải**: tách lớp "nhà cung cấp định danh" (adapter) để thay được cơ chế xác thực khi luật mới có hiệu lực; không gắn chặt logic nghiệp vụ vào một nhà cung cấp xác thực.

## 3. Pattern thiết kế

### P1. MPI hướng định danh, có lịch sử và alias — giải quyết R05, R10, R11, R12, R13, R14
- **Mô tả**: tách "người bệnh" khỏi "định danh". Một người bệnh có nhiều định danh theo thời gian. Khóa liên thông là số định danh cá nhân đang hiệu lực.
- **Dữ liệu**:
  - `patient(id PK, ma_bn UNIQUE, trang_thai_dinh_danh ENUM('DA_XAC_DINH','TAM','VO_DANH','SO_SINH_CHUA_KS'), ho_ten, ngay_sinh, gioi_tinh, quoc_tich, merged_into NULL FK)`
  - `patient_identifier(id, patient_id FK, loai ENUM('SDDCN','CMND9','SDDCN_DA_HUY','SDD_NN','HO_CHIEU','GCN_CAN_CUOC','TK_DINH_DANH','MA_THE_BHYT','GIAY_CHUNG_SINH','MA_TAM'), gia_tri, quoc_gia_cap, hieu_luc_tu, hieu_luc_den, nguon, created_by, created_at)`. Ràng buộc duy nhất có điều kiện: `UNIQUE(loai, gia_tri) WHERE hieu_luc_den IS NULL AND loai IN ('SDDCN','SDD_NN')`. CHECK: `loai='SDDCN' → gia_tri ~ '^[0-9]{12}$'`; `loai='MA_TAM' → gia_tri !~ '^[0-9]{12}$'`.
  - `patient_link(id, patient_id, related_id, quan_he ENUM('ME','CHA','GIAM_HO','DAI_DIEN','NGUOI_CHAM_SOC'), so_dinh_danh_nguoi_lien_quan, dien_thoai, can_cu, hieu_luc_tu, hieu_luc_den)`: nguồn cho trường người đại diện (R11, R22) và cho liên kết sơ sinh với mẹ.
  - `patient_merge_log(id, from_id, to_id, ly_do, bang_chung, user_id, ts, undo_of)`.
  - Chỉ mục: `patient_identifier(gia_tri)`; chỉ mục khóa tìm trùng mờ `(unaccent(lower(ho_ten)), ngay_sinh, gioi_tinh)`.
- **Luồng**: tiếp đón tìm theo bất kỳ định danh nào → nếu không có thì tạo mới với trạng thái phù hợp → khi bổ sung số định danh, kiểm tra trùng và đề xuất gộp.
- **Đánh đổi**: phức tạp hơn một cột `cccd` trên bảng người bệnh. Đổi lại xử lý được đổi số, trẻ sơ sinh, người vô danh, người nước ngoài mà không phải sửa schema.

### P2. Bản ghi nguồn định danh và xác thực theo lượt (identity provenance) — giải quyết R04, R06, R07, R08, R09
- **Dữ liệu**: `encounter_identity_check(id, encounter_id, phuong_thuc ENUM('QR_CCCD','CHIP_CCCD','VNEID_APP','DV_XAC_THUC','TRA_CUU_BHXH','NHAP_TAY'), dinh_danh_ap_dung, ket_qua, ma_giao_dich, nha_cung_cap_xac_thuc NULL, dong_y_id NULL, nguoi_thuc_hien, ts)`, append-only. **Không** lưu ảnh căn cước. Nếu quét QR thì chỉ lưu các trường cần thiết và số cũ.
- **Luồng**: mỗi lần định danh hoặc xác thực tạo một dòng. Kết quả xác thực không được tái dùng cho phiên đăng nhập khác (NĐ 69 Đ19 k4).
- **Đánh đổi**: thêm thao tác ghi, bù lại có bằng chứng khi kiểm tra hoặc khi có tranh chấp về danh tính.

### P3. Cổng adapter xác thực danh tính — giải quyết R08, R24
- **Mô tả**: interface `IdentityVerifier { verify(subject, method) -> Result }`. Các triển khai: `QrCccdParser` (offline), `ChipReader` (thiết bị chuyên dụng, cần đồng ý), `ThirdPartyAuthProvider` (tổ chức cung cấp dịch vụ xác thực được BCA cấp phép; có bước đồng ý qua VNeID/SMS), `DirectNdaIntegration` (chỉ bật khi có văn bản thống nhất với C06 và hồ sơ cấp độ 3). Cờ cấu hình theo cơ sở, mặc định tắt kênh trực tiếp.
- **Đánh đổi**: thêm lớp trừu tượng; tránh bị khóa vào một nhà cung cấp và dễ đáp ứng luật mới.

### P4. Hộp thư gửi đi (outbox) cho Sổ SKĐT, hai đích — giải quyết R01, R02, R15, R17, R20
- **Mô tả**: mỗi sự kiện "đóng lượt KCB" hoặc "kết luận phiếu KSK" ghi một dòng vào `outbound_message` trong cùng transaction. Worker gửi theo đích:
  - Đích `BHXH_GDBHYT`: XML 130/4750/3176 (Bảng 1 + 8 cho lượt không BHYT; đủ bảng cho BHYT), ký XML, gửi Cổng giám định. BHXH chuyển lên VNeID và BYT.
  - Đích `BYT_TRUC_DL`: phiếu KSK JSON/XML theo PL01 QĐ 1551, ký XMLDSig, đóng gói theo PL02 và ký SHA256RSA.
- **Dữ liệu**: `outbound_message(id, dich, loai, encounter_id|ksk_id, msg_id UNIQUE, payload_hash, payload_ref, trang_thai, so_lan_thu, han_chot_at, gui_luc, res_code, res_body_ref, chu_ky_phan_hoi)`. Chỉ mục `(trang_thai, han_chot_at)`.
- **Luồng**: `han_chot_at` = thời điểm kết thúc + 24h cho KSK. Cảnh báo trước hạn. Lỗi chữ ký thì dừng thử lại, báo quản trị.
- **Đánh đổi**: cần job nền và lưu payload. Bù lại idempotent, kiểm chứng được và báo cáo được (R20).

### P5. Schema phiếu KSK có phiên bản theo mẫu — giải quyết R15
- **Mô tả**: `ksk_form_template(code, ten, phien_ban, hieu_luc_tu, json_schema)` cho 17 mẫu; `ksk_record(id, patient_id, template_code, phien_ban, doi_tuong, nguon_kinh_phi, dot_kham_id, ket_luan_luc, data JSONB, trang_thai_ky)`; `ksk_signature(record_id, phan ('KHAM_MAT','TMH',…,'KET_LUAN','CO_SO'), signer, cert_serial, ts, sig_ref)`. Kiểm tra dữ liệu bằng JSON Schema sinh từ PL01 (kiểu, độ dài).
- **Đánh đổi**: JSONB linh hoạt khi BYT đổi mẫu. Truy vấn thống kê cần view hoặc cột sinh.

### P6. Bộ lọc dữ liệu nhạy cảm trước khi gửi — giải quyết R03, R19
- **Mô tả**: rule engine áp lên payload trước khi ký: loại bỏ hoặc che chỉ định và kết quả thuộc nhãn "restricted" (HIV theo DLCN-R32; danh sách khác cấu hình được). Ghi `filter_log(message_id, rule_id, field_path)`.
- **Đánh đổi**: có thể làm thiếu dữ liệu trên Sổ SKĐT. Cần chính sách do cơ sở phê duyệt (R21).

### P7. Danh mục cơ sở và địa giới có hiệu lực theo thời gian — giải quyết R18, R22
- **Dữ liệu**: `facility(id, ma_bhxh CHAR(5), ma_gln CHAR(13), ten, hieu_luc_tu, hieu_luc_den)`; `dia_gioi(ma, cap, ten, hieu_luc_tu, hieu_luc_den, thay_the_boi)`. Bản tin cũ được dựng lại theo mã đúng thời điểm.

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| SKDT-A01 | R01 | Lấy ngẫu nhiên 20 lượt đã đóng trong tháng (10 BHYT, 10 viện phí, đủ ngoại trú, nội trú, lĩnh thuốc hẹn, từ xa nếu có): lượt nào có bản tin gửi Cổng? | Truy vấn `encounter` JOIN log gửi; mã phản hồi Cổng | Bắt buộc |
| SKDT-A02 | R02 | Mở bản tin XML của một lượt viện phí: có Bảng 1 và Bảng 8 không? có ký số (`CHUKYDONVI`) không? `MA_THE_BHYT` có để trống đúng không? | File XML đã gửi; kết quả kiểm tra chữ ký | Bắt buộc |
| SKDT-A03 | R02 | Lượt ngoại trú có gửi XML8 (tóm tắt) không? Nếu không, Sổ SKĐT của người bệnh thiếu tóm tắt | Cấu hình gửi bảng; mẫu XML | Bắt buộc? |
| SKDT-A04 | R03 | Đóng một lượt mà bỏ trống tóm tắt: hệ thống có chặn hoặc cảnh báo không? Đọc 10 tóm tắt bất kỳ: có đủ 4 ý, có bác sĩ điều trị không? | Ảnh màn hình; mẫu dữ liệu | Bắt buộc |
| SKDT-A05 | R04, R05 | Tiếp đón thử: (a) chỉ đọc số định danh 12 số; (b) chỉ quét QR căn cước; (c) mở VNeID; (d) chỉ số thẻ BHYT. Ca nào bị chặn? Có kiểm tra 12 chữ số không? | Ảnh màn hình; schema cột số định danh | Bắt buộc |
| SKDT-A06 | R05, R14 | `SELECT so_dinh_danh, COUNT(*) FROM patient GROUP BY 1 HAVING COUNT(*)>1`; tỷ lệ hồ sơ có số định danh trong 12 tháng | Kết quả truy vấn | Bắt buộc |
| SKDT-A07 | R06, R07 | Cấu hình form tiếp đón: có trường bắt buộc ảnh hoặc scan căn cước, sổ khám, giấy ra viện không? Quy trình quầy có photo căn cước không? | Cấu hình; quan sát quy trình | Bắt buộc |
| SKDT-A08 | R07, R13 | Quét QR căn cước của người có CMND cũ: hệ thống có lưu số cũ và tìm ra hồ sơ cũ không? | Ảnh màn hình; bảng định danh | Nên |
| SKDT-A09 | R08 | Hỏi vendor về tích hợp "xác thực VNeID / CSDL dân cư": kết nối trực tiếp hay qua tổ chức cung cấp dịch vụ xác thực nào? Có văn bản thống nhất với C06 hoặc hợp đồng dịch vụ không? Có bước người bệnh đồng ý không? Kết quả xác thực có bị chuyển cho bên thứ ba không? | Hợp đồng, văn bản, sơ đồ luồng, log | Bắt buộc |
| SKDT-A10 | R08 | Nếu kết nối trực tiếp: HTTT có quyết định phê duyệt cấp độ 3 trở lên không? | Hồ sơ cấp độ (xem ANM-A*) | Bắt buộc |
| SKDT-A11 | R09 | Mỗi lượt có ghi phương thức định danh hoặc xác thực, người thực hiện, thời điểm không? | Bảng log; mẫu bản ghi | Nên |
| SKDT-A12 | R10 | Mở hồ sơ cấp cứu vô danh: tạo được không cần số định danh? Có cảnh báo 48 giờ, biên bản tài sản? Gộp hồ sơ có log và hoàn tác được không? | Ảnh màn hình; `merge_log` | Bắt buộc |
| SKDT-A13 | R11 | Tạo hồ sơ sơ sinh: có liên kết mẹ, số giấy chứng sinh, cập nhật số định danh sau khai sinh không? Mã tạm có thể bị nhầm thành 12 số không? | Ảnh màn hình; ràng buộc CHECK | Bắt buộc |
| SKDT-A14 | R12 | Tạo hồ sơ khách nước ngoài chỉ có hộ chiếu: lưu loại giấy tờ, quốc gia cấp, mã quốc tịch không? XML ghi gì vào `SO_CCCD`? | Ảnh màn hình; XML | Bắt buộc |
| SKDT-A15 | R15 | Với đợt KSK gần nhất: thời gian từ kết luận đến lúc gửi thành công. Có phiếu nào quá 24 giờ? Dữ liệu KSK trước 31/05/2026 đã đồng bộ chưa (hạn 15/07/2026)? | Log outbox; báo cáo trên csdlksk.vn | Bắt buộc |
| SKDT-A16 | R15 | So schema phiếu KSK với PL01 QĐ 1551 (mẫu tương ứng): tên chỉ tiêu, kiểu, độ dài; có đủ chữ ký số từng phần không? | Bảng so sánh; payload mẫu | Bắt buộc |
| SKDT-A17 | R16, R18 | Cấu hình cơ sở: có mã 13 chữ số, mã 5 ký tự, tài khoản liên thông riêng, tài khoản định danh tổ chức trên VNeID không? Mật khẩu lưu ở đâu? | Ảnh cấu hình; kho bí mật | Bắt buộc |
| SKDT-A18 | R17 | Xem log gọi API: endpoint đúng `api.emrhub.vn` hoặc sandbox; `msg_id` đúng mẫu; có `signature`; xử lý `PS_SIGNATURE_INVALID` thế nào | Log request/response | Bắt buộc |
| SKDT-A19 | R19 | Gửi thử lượt có xét nghiệm HIV dương tính hoặc đơn ARV: payload gửi đi có chứa không? Vendor có bản sao dữ liệu Sổ SKĐT ngoài hệ thống của khách hàng không? | Payload; hợp đồng xử lý dữ liệu | Bắt buộc |
| SKDT-A20 | R20 | Có xuất được bảng báo cáo 6 tháng theo QĐ 2733 PL01 Đ8 không? Cơ sở đã nộp trên cdc.kcb.vn chưa? | Báo cáo; ảnh xác nhận nộp | Bắt buộc? |
| SKDT-A21 | R21 | Có quy chế và quy trình Sổ SKĐT được thủ trưởng phê duyệt không? | Văn bản | Bắt buộc? |
| SKDT-A22 | R22 | Danh mục địa giới: dùng mã tỉnh 3 ký tự, mã xã 5 ký tự hiện hành? Có còn bắt buộc cấp huyện không? | Danh mục; form | Bắt buộc |
| SKDT-A23 | R23 | Phiếu KSK có hiện CLS còn hiệu lực, chặn phiếu trùng trong năm không? | Ảnh màn hình | Nên |

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái (so với 05/10/2026) | Nội dung | Ai phải làm | Nguồn |
|---|---|---|---|---|
| 21/05/2024 | Đã qua | Ban hành mẫu Sổ SKĐT VNeID (thí điểm) | BYT; cơ sở KCB | QĐ 1332 |
| 01/07/2024 | Đã qua | Luật Căn cước, NĐ 69, NĐ 70 có hiệu lực; tài khoản cá nhân do Cổng DVC cấp hết dùng 30/06/2024 | Mọi tổ chức | Luật 26/2023 Đ45; NĐ 69 Đ40 |
| 17/09/2024 | Đã qua | Hướng dẫn liên thông Sổ SKĐT qua Cổng giám định BHYT; báo cáo 6 tháng | Cơ sở KCB công, tư | QĐ 2733 |
| 30/06/2025 | Đã qua | Hết dùng tài khoản tổ chức do Cổng DVC/hệ thống TTHC cấp, phải có tài khoản định danh tổ chức | Tổ chức (kể cả cơ sở KCB) | NĐ 69 Đ40 k4 |
| 01/07/2025 | Đã qua | NĐ 102 có hiệu lực: mã định danh y tế = số định danh; nghĩa vụ kết nối Sổ SKĐT | Mọi cơ sở y tế | NĐ 102 Đ6, Đ10, Đ23, Đ25 |
| 01/01/2026 | Đã qua | Liên thông Sổ SKĐT VNeID cho **tất cả** người bệnh | Cơ sở KCB | QĐ 31 Đ5 |
| 06/01/2026 | Đã qua | Ký QĐ 31: dữ liệu Sổ SKĐT VNeID thay sổ giấy trong TTHC | Cơ sở KCB, cơ quan TTHC | QĐ 31 |
| 06/05/2026 | Đã qua | CT 17: KSK định kỳ hoặc sàng lọc miễn phí từ 2026; KSK học sinh, sinh viên hoàn thành tháng 6/2026 (thứ cấp) | UBND tỉnh, cơ sở KCB công và ngoài công lập | CT 17 |
| 11/05/2026 | Đã qua | Chương trình Đề án 06 2026–2030: chỉ tiêu căn cước thay thẻ BHYT 50% (2026) / 80% (2030); 100% người dân có HSSK điện tử liên thông (2030) | BYT, BCA (gián tiếp: BV) | QĐ 826 |
| 31/05/2026 | Đã qua | Hướng dẫn liên thông dữ liệu KSK; đăng ký tài khoản, mã 13 số | Cơ sở có KSK | QĐ 1551 |
| 15/07/2026 | Đã qua | Hạn đồng bộ dữ liệu KSK đã khám trước ngày ban hành hướng dẫn | Cơ sở có KSK | QĐ 1551 mục 3 d |
| 16/09/2026 | Đã qua | CV 1129: đẩy nhanh, lồng ghép, đối soát theo mã định danh; báo cáo hằng tháng | UBND tỉnh, BYT, BHXH, BCA | CV 1129 |
| 15/10/2026 | Sắp tới | Hết "chiến dịch 100 ngày" Sổ SKĐT (thứ cấp, theo inventory) | Cơ sở KCB | CT 07/CT-BYT (chưa đọc gốc) |
| 10/2026 – cuối 2026 | Sắp tới | Trình Luật Định danh và xác thực điện tử (QĐ 940: trong năm 2026); hoàn thiện Sổ SKĐT trên VNeID (NQ 221, thứ cấp) | BCA; vendor theo dõi | QĐ 940; inventory |
| 31/12/2026 | Sắp tới | Mục tiêu toàn dân được khám và lập Sổ SKĐT (CT 17 thứ cấp; NQ 282) | Địa phương, cơ sở KCB | CT 17; NQ 282 |
| 2030 | Xa | 100% người dân có HSSK điện tử liên thông; căn cước thay thẻ BHYT 80% bệnh viện, trường học | BYT, BCA | QĐ 826 |
| Thường xuyên | — | Gửi dữ liệu Sổ SKĐT sau mỗi lượt KCB (BHXH hiển thị ≤24 giờ sau khi nhận); gửi dữ liệu KSK ≤24 giờ sau đợt khám; báo cáo 6 tháng | Cơ sở KCB | QĐ 2733; QĐ 1551 |

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuỗi**
- NĐ 59/2022/NĐ-CP → **NĐ 69/2024** (Đ40 k2, từ 01/07/2024). Tài khoản định danh và giấy xác nhận dịch vụ xác thực cấp theo NĐ 59 còn giá trị đến hết hạn (Đ40 k5).
- QĐ 34/2021/QĐ-TTg (định danh, xác thực trên CSDL dân cư): NĐ 69 Đ40 không nêu tên văn bản này trong danh sách hết hiệu lực. Tình trạng vẫn **chưa xác minh** (giữ như inventory MT, mục 3).
- QĐ 06/QĐ-TTg (Đề án 06, 2022–2025) → tiếp nối bởi **QĐ 826/QĐ-TTg** (2026–2030). QĐ 1332 và QĐ 2733 còn lấy QĐ 06 làm căn cứ. Văn bản vẫn có giá trị, nhưng khi trích mục tiêu hiện hành thì dùng QĐ 826.
- QĐ 1332 (mẫu, 2024) → QĐ 2733 (hướng dẫn thí điểm, 2024) → **QĐ 31** (2026, biến thành nghĩa vụ cho mọi người bệnh, giữ QĐ 2733 làm hướng dẫn kỹ thuật) → **QĐ 1551** (2026, bổ sung dữ liệu KSK và kênh Trục dữ liệu BYT). Không văn bản nào thay văn bản nào. Chúng **cộng dồn**.
- Chuẩn XML: QĐ 130 → 4750 → 3176 → 1931 (xem BHYT-DATA §6). QĐ 2733 PL02 ánh xạ theo **130/4750**. QĐ 1551 PL01 dẫn chiếu **3176** cho trường hành chính. Khi triển khai phải dùng phiên bản XML hiện hành, không dừng ở 4750.

**Bẫy trích dẫn**
1. "QĐ 31 buộc từ 01/01/2026" là đúng về câu chữ (Đ5), nhưng **căn cứ pháp lý cấp VBQPPL** của nghĩa vụ kết nối là **NĐ 102 Đ10 k5 b và Đ23 k2**. QĐ 31, QĐ 2733, QĐ 1551 là quyết định hành chính hoặc hướng dẫn. Audit nên trích cả hai.
2. QĐ 31 và QĐ 1551 lấy **NĐ 42/2025** làm căn cứ thẩm quyền BYT. Theo inventory, NĐ 42 đã bị **NĐ 313/2026** thay. Văn bản không vì thế mà mất hiệu lực.
3. **Không** trích NĐ 69 Đ17 k2 hoặc Đ28 k4 ("lưu 05 năm") làm thời hạn lưu log của HIS. Đó là nghĩa vụ của hệ thống định danh quốc gia.
4. **"Xác thực" trong NĐ 69 khác "xác thực dữ liệu" trong NĐ 188 Đ69 k9.** Cái sau là ký số hồ sơ chi phí (BHYT-GD-R18), không phải xác thực danh tính người bệnh.
5. **Mã cơ sở**: "mã định danh 13 chữ số" (QĐ 1551, chuẩn GLN, cấp qua app.qlhanhnghekcb.gov.vn) khác mã 5 ký tự (QĐ 384/2019, dùng trong XML BHXH và QĐ 2733). Cũng khác "số định danh của tổ chức" trong hệ thống định danh điện tử (NĐ 69 Đ6 k2).
6. **emrhub.vn** xuất hiện trong bản gốc QĐ 1551 PL02 với tên "Trục dữ liệu Bộ Y tế". Đây là endpoint chính thức theo văn bản, không phải trang lạ. Ngược lại, đừng lấy endpoint nào không có trong văn bản.
7. Câu "người nước ngoài dùng số định danh làm mã định danh y tế" chỉ đúng với người **đã được cấp tài khoản định danh điện tử** (NĐ 102 Đ6), tức người có thẻ thường trú hoặc tạm trú (NĐ 69 Đ7 k2).
8. Số hiệu QĐ 940 trên bản OCR bị đọc nhầm thành "3420". Đối chiếu ảnh bản gốc cho thấy đúng là **940/QĐ-TTg ngày 26/5/2026**.
9. QĐ 2733 PL02 tham chiếu mã huyện (QĐ 124/2004/QĐ-TTg). QĐ 1551 đã bỏ cấp huyện. Tránh copy cấu trúc địa chỉ 2024.
10. Inventory ghi QĐ 1332 ở mức "thứ cấp" và QĐ 2733 là "nội dung chưa đọc". Pha này đã đọc bản gốc (OCR) của cả hai, nâng lên **gốc-OCR**.

**Mâu thuẫn đã phân xử**
- **MT-29 (kênh QĐ 1551)**: giải quyết theo bản gốc PL02. Ba địa chỉ có ba vai trò khác nhau (R17).
- **MT-30 (một hay nhiều điểm tích hợp)**: **nhiều điểm**. (a) Dữ liệu từng lượt KCB, mọi người bệnh: XML lên **Cổng giám định BHYT của BHXH** (QĐ 2733 PL01 Đ1 k3, Đ5). BHXH hiển thị lên VNeID trong 24 giờ, đồng thời chia sẻ sang CSDL sức khỏe cá nhân của BYT qua **Nền tảng chia sẻ, điều phối dữ liệu của TTDLQG** (QĐ 1551 mục 4 b, PL03, AgentNode, TT 08/2025/TT-BCA). (b) Dữ liệu KSK định kỳ và sàng lọc: lên **CSDL sức khỏe cá nhân của BYT** qua `csdlksk.vn` hoặc API `api.emrhub.vn` (QĐ 1551 mục 4 a). BYT chia sẻ sang CSDL dân cư để hiện trên VNeID (mục 5). (c) Đơn thuốc: kênh riêng (cụm DUOC). Cơ sở KCB **không** kết nối trực tiếp với VNeID.
- **Câu hỏi mở K4-7 (người nước ngoài, trẻ chưa có số, người vô danh)**: đã trả lời tại R10–R12.

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Hướng dẫn kết nối của "cơ quan quản lý CSDL Sổ SKĐT VNeID"** (QĐ 31 Đ4 k2): chưa tìm thấy văn bản. Câu hỏi còn treo: cơ sở KCB có được kênh nào để **đọc** Sổ SKĐT của người bệnh (có đồng ý) không, hay chỉ xem trên app người bệnh xuất trình?
2. **CV 4395/BYT-KCB (2023)**: mới đọc qua luatvietnam. Cần bản gốc để xác nhận (a) bộ bảng tối thiểu cho lượt không BHYT, (b) nghĩa vụ đăng ký với BHXH tỉnh của cơ sở không ký hợp đồng BHYT, (c) còn áp dụng sau 3176 và 1931 hay không. Nên hỏi BHXH VN hoặc Cục QLKCB.
3. **XML8 cho lượt ngoại trú** (R02, ghi chú): ghi chú bảng 2023 và QĐ 2733 PL02 vênh nhau. Cần BHXH hoặc BYT xác nhận.
4. **Bệnh viện công có phải "tổ chức cung cấp dịch vụ công"** theo NĐ 69 Đ18 k1 và Luật Căn cước Đ32 k1 để kết nối trực tiếp với hệ thống định danh hay không. Bệnh viện tư chắc chắn phải qua tổ chức cung cấp dịch vụ xác thực. Cần luật sư hoặc hỏi C06.
5. **Danh sách tổ chức được BCA cấp phép cung cấp dịch vụ xác thực điện tử** (niêm yết trên trang định danh điện tử theo NĐ 69 Đ22 k3) và thông tư BCA về "thiết bị chuyên dụng" đọc chip căn cước: chưa đọc.
6. **Trường bắt buộc trong bản tin KSK** cơ sở gửi (PL01 QĐ 1551 không có cột bắt buộc); định nghĩa "kết thúc đợt khám" để tính 24 giờ. Hỏi TT Thông tin y tế QG (đơn vị đồng đề xuất QĐ 1551).
7. **KSK lái xe**: có phải gửi song song cho Trục dữ liệu BYT (QĐ 1551 mẫu 3) và CSDL giao thông (TT 36/2024) không? Thuộc nửa còn lại của K4.
8. **Chế tài** khi không liên thông Sổ SKĐT hoặc dữ liệu KSK: chưa tìm thấy điều khoản xử phạt riêng. Chế tài cho dữ liệu BHYT xem BHYT-GD-R30. Cần rà nghị định xử phạt lĩnh vực y tế hiện hành.
9. **CT 17/CT-TTg**: chưa có bản gốc (chỉ bài đăng trên xaydungchinhsach). Vanban.chinhphu.vn mới xác nhận CV 1129. **CT 07/CT-BYT** (chiến dịch 100 ngày) và **NQ 221/NQ-CP** (hoàn thiện Sổ SKĐT tháng 10/2026): vẫn chỉ có nguồn thứ cấp.
10. **QĐ 831/QĐ-BYT (2017)** về hồ sơ quản lý sức khỏe cá nhân tại tuyến cơ sở và quan hệ của nó với CSDL sức khỏe cá nhân (QĐ 1551 mục 1 a) và Sổ SKĐT: chưa đọc bản gốc, chưa biết còn được dùng làm chuẩn cho phần mềm trạm y tế hay không.
11. **NQ 66.7/2025/NQ-CP Đ7** và **NĐ 278/2025** (căn cứ của QĐ 31) chưa đọc. Có thể đặt thêm nghĩa vụ kết nối, chia sẻ bắt buộc với bệnh viện công nếu bệnh viện công được coi là "cơ quan thuộc hệ thống chính trị". Thuộc cụm K5.
12. **TT 07/2016/TT-BCA** (mã quốc tịch, mã đơn vị hành chính) còn hiệu lực không, và danh mục mã tỉnh, xã sau sắp xếp 2025 dùng trong XML: chưa xác minh trong cụm này.
13. **Dự thảo Luật Định danh và xác thực điện tử**: chưa có văn bản thông qua tại thời điểm 05/10/2026. Theo dõi kỳ họp QH tháng 10/2026.
14. Câu chữ của QĐ 1332, QĐ 2733, NĐ 69, NĐ 70, NĐ 102, QĐ 826, QĐ 940, CV 1129 lấy từ **OCR**. Số và ngày đã đối chiếu (QĐ 826 bảng mục tiêu, QĐ 940 số hiệu, QĐ 2733 Đ8 đã xem ảnh). Trước khi trích nguyên văn trong hồ sơ pháp lý nên đối chiếu lại bản gốc.
