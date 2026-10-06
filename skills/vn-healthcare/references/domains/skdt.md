# SKDT — Sổ sức khỏe điện tử, VNeID và định danh người bệnh

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám (kể cả PK không ký hợp đồng BHYT), cơ sở tổ chức KSK định kỳ/sàng lọc, vendor HIS/app y tế · Research gốc: `research/deep/SKDT.md`

Phạm vi: liên thông Sổ SKĐT VNeID từ lượt KCB, dữ liệu KSK định kỳ/sàng lọc (QĐ 1551), mã định danh y tế, căn cước, định danh và xác thực điện tử, người bệnh không giấy tờ/trẻ em/người nước ngoài, hai hệ mã cơ sở. Ngoài phạm vi: xuất trình thẻ BHYT bằng căn cước/VNeID → BHYT-GD-R01..R05; chuẩn XML 130/4750/3176 → BHYT-DATA; MPI trong HSBA → EMR-R05; căn cứ xử lý, quyền chủ thể → DLCN; giấy chứng sinh, báo tử, giấy nghỉ BHXH, KSK lái xe → GIAYTO. Tài liệu nghiên cứu, không phải ý kiến pháp lý.

## Tóm tắt nhanh

- Từ **01/01/2026** cơ sở KCB phải liên thông Sổ SKĐT VNeID cho **mọi** người bệnh, mọi loại hình, cả lượt viện phí (QĐ 31 Đ5). Căn cứ cấp VBQPPL là NĐ 102/2025 Đ10 k5 b, Đ23 k2: audit nên trích cả hai.
- Kênh liên thông lượt KCB là XML ký số lên **Cổng tiếp nhận dữ liệu giám định BHYT** (QĐ 2733 PL01). Cơ sở **không** kết nối trực tiếp VNeID; BHXH hiển thị lên VNeID trong 24 giờ sau khi nhận.
- KSK định kỳ/sàng lọc: gửi về CSDL sức khỏe cá nhân của BYT **trong 24 giờ** sau khi kết thúc đợt khám, ký số, theo 17 mẫu PL01 QĐ 1551. Hạn đồng bộ dữ liệu tồn đã qua (15/07/2026).
- Mã định danh y tế của cá nhân = số định danh cá nhân 12 số (NĐ 102 Đ6). Người nước ngoài chỉ có mã này khi **đã có tài khoản định danh điện tử**.
- Bẫy nặng nhất: vendor HIS/app tư nhân tự kết nối CSDL dân cư hoặc hệ thống định danh. NĐ 69 Đ18 k4 buộc tổ chức khác đi qua **tổ chức cung cấp dịch vụ xác thực** được BCA cấp phép, và cấm chia sẻ lại kết quả xác thực (Đ19 k4).
- Hai hệ mã cơ sở: mã 5 ký tự (QĐ 384/2019, XML BHXH) và mã định danh **13 chữ số** chuẩn GLN (QĐ 1551, cấp qua `app.qlhanhnghekcb.gov.vn`). Không trộn.
- Mốc gần nhất: 15/10/2026 hết "chiến dịch 100 ngày" Sổ SKĐT (thứ cấp); 31/12/2026 mục tiêu toàn dân được khám và lập Sổ SKĐT (CT 17, chỉ tiêu điều hành).
- MPI phải chịu được đổi số định danh (NĐ 70 Đ11 k7), trẻ sơ sinh chưa có số, người vô danh. Ràng buộc `UNIQUE(so_dinh_danh)` cứng trên bảng người bệnh là sai thiết kế.

## Mục lục

| ID | Tiêu đề |
|---|---|
| SKDT-R01 | Liên thông Sổ SKĐT VNeID cho mọi người bệnh, mọi loại hình |
| SKDT-R02 | Kênh XML ký số lên Cổng giám định BHYT; bộ bảng cho lượt không BHYT |
| SKDT-R03 | Nội dung tối thiểu Sổ SKĐT; tóm tắt đợt điều trị |
| SKDT-R04 | Tiếp nhận bằng căn cước, số định danh, số thẻ BHYT, trên thẻ hoặc VNeID |
| SKDT-R05 | Mã định danh y tế = số định danh cá nhân; khóa MPI |
| SKDT-R06 | Chấp nhận dữ liệu VNeID thay giấy |
| SKDT-R07 | Khai thác thông tin căn cước đúng luật (QR, số cũ, chip) |
| SKDT-R08 | Xác thực qua CSDL dân cư/hệ thống định danh: trực tiếp hay qua trung gian |
| SKDT-R09 | Lưu nguồn định danh và nguồn xác thực theo lượt |
| SKDT-R10 | Người bệnh vô danh, không giấy tờ |
| SKDT-R11 | Trẻ em chưa có số định danh; người giám hộ |
| SKDT-R12 | Người nước ngoài; người gốc Việt chưa xác định quốc tịch |
| SKDT-R13 | Số định danh bị hủy, xác lập lại: MPI giữ lịch sử |
| SKDT-R14 | Khử trùng hồ sơ, đối soát theo mã định danh |
| SKDT-R15 | Dữ liệu KSK theo 17 mẫu, gửi trong 24 giờ, ký số |
| SKDT-R16 | Tài khoản liên thông, mã 13 chữ số, tài khoản định danh tổ chức |
| SKDT-R17 | API Trục dữ liệu BYT (PL02 QĐ 1551) |
| SKDT-R18 | Hai hệ mã cơ sở: 5 ký tự và 13 ký tự |
| SKDT-R19 | Phạm vi truy cập, chia sẻ, lọc dữ liệu nhạy cảm |
| SKDT-R20 | Báo cáo 6 tháng về liên thông Sổ SKĐT |
| SKDT-R21 | Quy chế, quy trình Sổ SKĐT tại cơ sở |
| SKDT-R22 | Người đại diện hợp pháp; địa giới không còn cấp huyện |
| SKDT-R23 | Lồng ghép KSK với KCB, tránh khám và thanh toán trùng |
| SKDT-R24 | Chuẩn bị cho Luật Định danh và xác thực điện tử |

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 102/2025/NĐ-CP (13/05/2025) | Quản lý dữ liệu y tế | 01/07/2025 | Còn hiệu lực | gốc (Đ6, Đ10 k5, Đ23 đối chiếu bản Công báo có text) | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-102-2025-nd-cp-44865.htm) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/102-ndcp.signed.pdf) |
| 1332/QĐ-BYT (21/05/2024) | Mẫu Sổ SKĐT tích hợp VNeID (thí điểm) | Từ ngày ký | Còn hiệu lực; nội dung chuẩn mà QĐ 2733, 31, 1551 dẫn | gốc-OCR | [PDF (BVĐK Bạc Liêu đăng lại)](https://bvdkbaclieu.gov.vn/upload/1000079/20240622/382_Quyet_dinh-1332-QD-BYT_beaeb9e1ff.pdf) |
| 2733/QĐ-BYT (17/09/2024) | Hướng dẫn thí điểm Sổ SKĐT VNeID; PL02 ánh xạ trường sang XML 130/4750 | Từ ngày ký | Còn hiệu lực; QĐ 31 dùng làm hướng dẫn kỹ thuật | gốc-OCR | [PDF (BVĐK Bạc Liêu đăng lại)](https://bvdkbaclieu.gov.vn/upload/1000079/20241031/444_Quyet_dinh-2733-QD-BYT_8fd263b901.pdf) |
| 31/QĐ-BYT (06/01/2026) | Công bố dữ liệu Sổ SKĐT VNeID thay sổ giấy trong TTHC | Từ ngày ký; Đ5 mốc 01/01/2026 | Còn hiệu lực | gốc | [PDF (BVĐK Bạc Liêu đăng lại)](https://bvdkbaclieu.gov.vn/upload/1000079/20260305/691_Quyet-dinh-31-QD-BYT_704c0ca597.pdf) |
| 1551/QĐ-BYT (31/05/2026) | Liên thông dữ liệu KSK, tạo lập Sổ SKĐT (PL01 17 mẫu; PL02 API; PL03 API BHXH) | Từ ngày ký | Còn hiệu lực | gốc | [PDF (SYT Lai Châu)](https://soyte.laichau.gov.vn/upload/1001027/20260602/2026_05_31_QD_ban_hanh_HD_ket_noi_lien_thong_du_lieu_KSK_Final_signed_2be3f377e1.pdf) |
| 4395/BYT-KCB (13/07/2023) | Liên thông Bảng 1, Bảng 8 cho người bệnh không dùng thẻ BHYT | — | Chưa rõ còn áp dụng nguyên trạng (QĐ 130 đã sửa nhiều lần) | thứ cấp | [luatvietnam (thứ cấp)](https://luatvietnam.vn/y-te/cong-van-4395-byt-kcb-2023-lien-thong-du-lieu-theo-quyet-dinh-130-qd-byt-259277-d6.html) |
| 26/2023/QH15 | Luật Căn cước | 01/07/2024 | Còn hiệu lực | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/01/luat26.pdf) |
| 70/2024/NĐ-CP (25/06/2024) | Hướng dẫn Luật Căn cước | 01/07/2024 | Còn hiệu lực | gốc-OCR (Đ1–14) | [VB 210497](https://vanban.chinhphu.vn/?pageid=27160&docid=210497) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/6/70-nd.signed.pdf) |
| 69/2024/NĐ-CP (25/06/2024) | Định danh và xác thực điện tử | 01/07/2024 | Còn hiệu lực; thay NĐ 59/2022 | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/6/69-cp.signed.pdf) |
| 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ2 k10, Đ72, Đ73 | 01/01/2024 | Còn hiệu lực | gốc | [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 826/QĐ-TTg (11/05/2026) | Chương trình Đề án 06 giai đoạn 2026–2030 | Từ ngày ký | Còn hiệu lực; tiếp nối QĐ 06/QĐ-TTg | gốc-OCR (bảng mục tiêu đã đối chiếu ảnh) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/826-ttg.signed.pdf) |
| 940/QĐ-TTg (26/05/2026) | Đề án phát triển ứng dụng VNeID 2026–2030 | Từ ngày ký | Còn hiệu lực (bối cảnh) | gốc-OCR | [VB 218266](https://vanban.chinhphu.vn/?pageid=27160&docid=218266) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/940-ttg.signed.pdf) |
| 17/CT-TTg (06/05/2026) | KSK định kỳ, khám sàng lọc miễn phí | Từ ngày ký | Còn hiệu lực | thứ cấp | [baochinhphu (báo, bối cảnh)](https://baochinhphu.vn/tu-nam-2026-to-chuc-kham-suc-khoe-dinh-ky-mien-phi-cho-nguoi-dan-102260506175509173.htm) |
| 1129/TTg-KGVX (16/09/2026) | Triển khai CT 17 | Từ ngày ký | Còn hiệu lực | gốc-OCR | [VB 219523](https://vanban.chinhphu.vn/?pageid=27160&docid=219523) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/1129_ttg-kgvx_16092026-signed.signed.pdf) |
| 384/QĐ-BYT (01/02/2019) | Nguyên tắc cấp mã cơ sở KCB 5 ký tự | — | Còn hiệu lực (QĐ 2733 dẫn) | chưa xác minh (chỉ thấy dẫn chiếu) | link chưa kiểm tra được |
| 831/QĐ-BYT (2017) | Mẫu hồ sơ quản lý sức khỏe cá nhân tuyến cơ sở | — | Theo CSDL thứ cấp: còn hiệu lực | chưa xác minh | link chưa kiểm tra được |
| Dự thảo Luật Định danh và xác thực điện tử | — | QĐ 940 giao trình QH trong năm 2026 | Dự thảo | thứ cấp | [luatvietnam (thứ cấp, bối cảnh)](https://luatvietnam.vn/tu-phap/du-thao-luat-dinh-danh-va-xac-thuc-dien-tu-2026-436278-d10.html) |

Tham chiếu không đào lại ở đây: TT 13/2025 Đ1 k3 và CV 365 PL III.1.1 a (EMR-R05); NĐ 188/2025 Đ37, Đ38, TT 01/2025 (BHYT-GD); NQ 66.7/2025/NQ-CP Đ7, NĐ 278/2025 (căn cứ QĐ 31, xem HTTT-BC); QĐ 1272/QĐ-BYT 2026 (kế hoạch KSK, chưa đọc); TCVN 12344:2019 (nhãn định danh người bệnh, tự nguyện).

## 2. Yêu cầu

### A. Liên thông Sổ SKĐT từ lượt KCB

### SKDT-R01 — Liên thông Sổ SKĐT VNeID cho mọi người bệnh, mọi loại hình KCB
- **Căn cứ**: NĐ 102 Đ10 k5 b: cơ sở y tế hoạt động hợp pháp "có trách nhiệm kết nối, chia sẻ, liên thông dữ liệu y tế liên quan với Sổ sức khỏe điện tử tích hợp trên ứng dụng định danh quốc gia"; Đ23 k2 (đồng bộ với CSDL quốc gia về y tế, CSDL BYT, CSDL địa phương và Sổ SKĐT). QĐ 31 Đ5: cơ sở KCB thực hiện liên thông dữ liệu Sổ SKĐT VNeID "của tất cả các đối tượng người bệnh" theo QĐ 2733, kể từ 01/01/2026. QĐ 2733 Đ2 (gốc-OCR, diễn giải): áp dụng cho mọi cơ sở KCB công và tư có giấy phép, mọi loại hình (khám ngoại trú, điều trị ngoại trú, nội trú, ban ngày, lĩnh thuốc theo hẹn, KCB từ xa); Đ4 k5 đ: gửi lên Cổng giám định sau khi người bệnh kết thúc đợt KCB.
- **Áp dụng**: BV công, BV tư, PK (cả PK không ký hợp đồng BHYT) · **Hiệu lực/hạn**: NĐ 102 từ 01/07/2025; QĐ 31 từ 01/01/2026 (đã qua)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: khi đóng lượt (kết thúc khám, ra viện, kết thúc điều trị ngoại trú/ban ngày, lĩnh thuốc theo hẹn, phiên KCB từ xa) tự sinh gói dữ liệu Sổ SKĐT vào hàng đợi gửi; áp cho cả lượt viện phí, dịch vụ; lưu trạng thái gửi theo lượt (`chua_gui | da_gui | loi | gui_lai`) và mã phản hồi; báo cáo được tỷ lệ đã liên thông theo loại hình và BHYT/không BHYT (phục vụ R20).
- **Bẫy**: QĐ 31 ký 06/01/2026 nhưng Đ5 lấy mốc 01/01/2026. QĐ 2733 tự gọi là "thí điểm", QĐ 31 mở rộng ra mọi người bệnh: không có căn cứ để loại lượt không BHYT. Nhà thuốc thuộc "cơ sở y tế" của NĐ 102 nhưng dữ liệu bán thuốc đi kênh dược (DUOC), không đi kênh Sổ SKĐT (suy luận).

### SKDT-R02 — Kênh XML ký số lên Cổng giám định BHYT; bộ bảng cho lượt không BHYT
- **Căn cứ**: QĐ 1332 Đ3 (gốc-OCR): chuẩn liên thông Sổ SKĐT theo chuẩn dữ liệu đầu ra phục vụ giám định, thanh toán. QĐ 2733 PL01 Đ1 k2–3, Đ4 k2–3, Đ5 (gốc-OCR, diễn giải): dữ liệu theo QĐ 130/4750; gửi qua Cổng tiếp nhận dữ liệu giám định BHYT; phần mềm phải cấu hình liên thông và ký số bằng chứng thư của cơ sở; 7 bước (đăng ký mã liên thông, tài khoản Cổng, …, ký số và gửi sau khi kết thúc đợt KCB, BHXH trích xuất và hiển thị lên VNeID trong 24 giờ kể từ khi nhận). PL02: ánh xạ trường Sổ SKĐT sang Bảng 1, 2, 3, 4, 8. CV 4395 (thứ cấp): lượt không dùng thẻ BHYT gửi Bảng 1 và Bảng 8; cơ sở chưa ký hợp đồng BHYT đăng ký với BHXH địa phương trước khi gửi.
- **Áp dụng**: BV công, BV tư, PK · **Hiệu lực/hạn**: như R01
- **Mức**: BẮT BUỘC (kênh Cổng BHXH, chuẩn XML, ký số) · BẮT BUỘC? (bộ bảng tối thiểu cho lượt không BHYT: CV 4395 mới đọc qua thứ cấp)
- **Phần mềm phải**: sinh XML từ cùng nguồn với hồ sơ BHYT (BHYT-DATA-R01, R07); lượt không BHYT tối thiểu Bảng 1 và Bảng 8, để trống trường đặc thù BHYT (`MA_THE_BHYT`, mức hưởng); ký số chứng thư cơ sở; lưu bằng chứng gửi.
- **Bẫy**: ghi chú bảng 2023 (BHYT-DATA-R01) chỉ yêu cầu XML8 cho nội trú, ban ngày, lưu TYT/PKĐKKV, nhưng QĐ 2733 PL02 lấy phần tóm tắt điều trị (mục 3.6, trường 41–45) từ Bảng 8. Không gửi XML8 cho lượt ngoại trú thì Sổ SKĐT thiếu tóm tắt. Chưa có văn bản phân xử; nên cho cấu hình "gửi XML8 cho mọi lượt" (suy luận). Chuẩn XML hiện hành là chuỗi 130 → 4750 → 3176 → QĐ 1931/QĐ-BYT năm 2026 sửa QĐ 130 (xem BHYT-DATA); không dừng ở 4750 như PL02.

### SKDT-R03 — Nội dung tối thiểu của Sổ SKĐT; tóm tắt đợt điều trị
- **Căn cứ**: QĐ 31 Đ2 k3 (gốc): 4 nhóm trường: (a) hành chính (họ tên, ngày sinh, giới, dân tộc, quốc tịch, nghề nghiệp, số định danh/CCCD, điện thoại, mã thẻ BHYT, nơi ĐKKCB ban đầu, hạn thẻ, địa chỉ, người đại diện hợp pháp); (b) tiền sử dị ứng, bệnh tật, tiêm chủng; (c) từng đợt KCB (cơ sở, thời gian, hình thức, lý do, tình trạng ra viện, kết quả, chẩn đoán ra viện, nhóm máu, chiều cao, cân nặng, CLS, thuốc, PTTT); (d) tóm tắt HSBA (tiền sử, bệnh sử, diễn biến, CLS có giá trị, phương pháp điều trị, hướng điều trị tiếp, đơn thuốc, lời dặn, lịch tái khám, bác sĩ điều trị). QĐ 1332 Phụ lục B: 46 trường, có cột hiển thị. QĐ 31 Đ3: người bệnh hoặc người đại diện tải bản ghi từng đợt KCB dạng PDF qua VNeID. QĐ 2733 Đ4 k5 d (diễn giải): bác sĩ thực hiện tóm tắt HSBA, quá trình điều trị để cung cấp cho Sổ SKĐT.
- **Áp dụng**: BV công, BV tư, PK · **Hiệu lực/hạn**: như R01
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mẫu "Tóm tắt đợt điều trị" bắt buộc khi đóng lượt với 4 ô (tiền sử và bệnh sử; CLS có giá trị; phương pháp điều trị; hướng điều trị tiếp và lịch tái khám) cùng bác sĩ điều trị; chặn đóng lượt khi trống (ngoại lệ cấu hình cho lượt khám đơn giản); ICD-10 nhiều mã phân cách ";", mã đầu là bệnh chính (QĐ 1332 chú thích 1, 7); nhóm máu, chiều cao, cân nặng là chỉ số chính.
- **Bẫy**: bản PDF trên VNeID do hệ thống quốc gia dựng từ dữ liệu cơ sở gửi, có giá trị như bản giấy (QĐ 31 Đ1 k1): câu chữ tóm tắt cẩu thả hiện thẳng cho người bệnh và cơ quan TTHC. Dữ liệu HIV và nhóm nhạy cảm phải lọc trước khi gửi (R19, DLCN-R32). Bộ trường tóm tắt của TT 38 cho HTTT quản lý KCB xem HTTT-BC-R04: nên dùng một mô hình tóm tắt cho cả hai đích.

### SKDT-R04 — Tiếp nhận bằng căn cước, số định danh hoặc số thẻ BHYT, trên thẻ hoặc VNeID
- **Căn cứ**: QĐ 2733 Đ4 k5 b, PL01 Đ2, Đ5 bước 4 (gốc-OCR, diễn giải): tiếp nhận KCB bằng thẻ căn cước, số định danh cá nhân hoặc số thẻ BHYT cho mọi người bệnh; người không có thẻ BHYT dùng số căn cước/số định danh (trên thẻ nhựa hoặc VNeID) làm định danh để liên thông. Luật Căn cước Đ20 k3: thẻ căn cước hoặc số định danh dùng để kiểm tra thông tin trong CSDL dân cư và CSDL khác.
- **Áp dụng**: BV công, BV tư, PK · **Hiệu lực/hạn**: 17/09/2024; bao trùm mọi người bệnh từ 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: một ô tìm người bệnh nhận số định danh 12 số, số thẻ BHYT hoặc dữ liệu quét QR căn cước; người bệnh viện phí vẫn thu số định danh. Phần BHYT (VNeID mức 2, VssID, trẻ dưới 6 tuổi): xem BHYT-GD-R01, R03, R05.
- **Bẫy**: QĐ 826 đặt chỉ tiêu "dùng thẻ căn cước thay thẻ BHYT" 50% năm 2026, 80% năm 2030 (đã đối chiếu ảnh): đó là chỉ tiêu quản lý, không phải hạn chót của cơ sở. Nghĩa vụ chấp nhận căn cước thay thẻ BHYT ở NĐ 188 Đ37 (BHYT-GD-R01).

### SKDT-R05 — Mã định danh y tế của cá nhân = số định danh cá nhân; khóa MPI
- **Căn cứ**: NĐ 102 Đ6: "Sử dụng số định danh cá nhân của công dân Việt Nam và người nước ngoài đã được cấp tài khoản định danh điện tử theo quy định pháp luật về căn cước làm mã định danh y tế của cá nhân." Đ14 k4 a: là trường của CSDL quốc gia về y tế. Luật Căn cước Đ12 k1–2: số định danh công dân là dãy 12 chữ số, không lặp. NĐ 69 Đ5 k2: người nước ngoài có số định danh duy nhất do hệ thống định danh xác lập.
- **Áp dụng**: mọi cơ sở y tế · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trường `so_dinh_danh` riêng (không gộp với hộ chiếu, CMND 9 số), kiểm tra 12 chữ số cho công dân VN; duy nhất có điều kiện (chỉ bản ghi đang hiệu lực, xem R13); giữ `MA_BN` nội bộ song song; mọi bản tin (XML, KSK, đơn thuốc) lấy số định danh từ MPI, không nhập tự do ở từng phân hệ. Dùng chung cho HTTT-BC-R16.
- **Bẫy**: Đ6 chỉ tính người nước ngoài đã có tài khoản định danh; khách ngắn ngày không có mã định danh y tế (R12). Văn bản đã đọc không quy định thuật toán chữ số kiểm tra: đừng tự chế ngoài độ dài và kiểu số (suy luận).

### SKDT-R06 — Chấp nhận dữ liệu VNeID và Sổ SKĐT thay giấy
- **Căn cứ**: QĐ 31 Đ1 k1: dữ liệu Sổ SKĐT đã liên thông, hiển thị trên VNeID "có giá trị pháp lý tương đương bản giấy"; Đ1 k2: cơ sở KCB không yêu cầu cung cấp bản giấy nếu đã có đầy đủ thông tin trên VNeID. QĐ 2733 PL01 Đ6 (gốc-OCR, diễn giải): thông tin cá nhân, thẻ BHYT, lịch sử KCB, phiếu hẹn, giấy chuyển tuyến trên VNeID có giá trị như bản giấy. NĐ 102 Đ10 k5 c; NĐ 69 Đ9 k6; Luật Căn cước Đ22 k3, Đ33 k1.
- **Áp dụng**: BV công, BV tư, PK · **Hiệu lực/hạn**: 06/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không đặt trường bắt buộc "ảnh/scan sổ khám, giấy ra viện, giấy chuyển tuyến" khi người bệnh trình VNeID; có lựa chọn ghi "đã đối chiếu trên VNeID" (người xem, thời điểm, loại giấy tờ); nhập lại thông tin thì ghi nguồn "VNeID do người bệnh xuất trình".
- **Bẫy**: phần mềm cơ sở **không** kéo được Sổ SKĐT từ VNeID; văn bản chỉ mô tả người bệnh mở app cho bác sĩ xem. Hướng dẫn kết nối của cơ quan quản lý CSDL Sổ SKĐT (QĐ 31 Đ4 k2) chưa tìm thấy (mục 7).

### SKDT-R07 — Khai thác thông tin căn cước đúng luật: QR, số cũ, chip
- **Căn cứ**: Luật Căn cước Đ20 k3: khi đã xuất trình thẻ căn cước thì không được yêu cầu xuất trình giấy tờ hoặc cung cấp thông tin đã in, tích hợp vào thẻ; Đ33 k2: thông tin thẻ/chip khác căn cước điện tử thì dùng căn cước điện tử; Đ22 k5: thông tin mã hóa trong chip chỉ khai thác bằng thiết bị chuyên dụng, tổ chức ngoài nhà nước cần công dân đồng ý; Đ32 k2 (thiết bị theo quy định BCA). NĐ 70 Đ12 k1 (gốc-OCR, diễn giải): số CMND 9 số và số định danh đã hủy nằm trong QR thẻ căn cước; tổ chức quét QR để dùng, không được đòi công dân xác nhận số cũ.
- **Áp dụng**: BV công, BV tư, PK, app y tế · **Hiệu lực/hạn**: 01/07/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: quét QR căn cước để điền hồ sơ, lưu số CMND cũ/số định danh cũ làm định danh phụ để ghép hồ sơ; không bắt nộp "giấy xác nhận số CMND"; đọc chip thì có bước ghi đồng ý (tổ chức tư) và dùng thiết bị đáp ứng quy định BCA; thông tin thẻ lệch VNeID thì lấy theo VNeID và ghi vết.
- **Bẫy**: quy trình "photo CCCD hai mặt" ở quầy vừa thừa vừa tạo kho ảnh căn cước, là dữ liệu nhạy cảm theo NĐ 356 Đ4 k1 i (DLCN). Thông tư BCA về thiết bị chuyên dụng chưa đọc.

### SKDT-R08 — Xác thực qua CSDL dân cư/hệ thống định danh: ai kết nối trực tiếp, ai qua trung gian
- **Căn cứ** (NĐ 69, NĐ 70 gốc-OCR, diễn giải): NĐ 69 Đ18 k1: cơ quan nhà nước, tổ chức chính trị - xã hội, tổ chức cung cấp dịch vụ công được kết nối trực tiếp với hệ thống định danh và xác thực nếu HTTT đạt an toàn cấp độ 3 trở lên; k2: thống nhất bằng văn bản với C06; k3: thẩm định 30 ngày (07 ngày làm việc nếu đã kết nối CSDL dân cư); **k4: tổ chức khác kết nối thông qua tổ chức cung cấp dịch vụ xác thực điện tử**. Đ19 k3: phải có đồng ý của chủ thể qua VNeID, SMS số chính chủ hoặc hình thức khác; **k4: không được chia sẻ kết quả xác thực cho tổ chức khác; kết quả không làm yếu tố xác thực trong giao dịch khác**. Đ22–23: dịch vụ xác thực là ngành nghề có điều kiện, chỉ đơn vị sự nghiệp công lập hoặc doanh nghiệp thuộc CAND được cấp phép. Đ20: 4 mức xác thực. NĐ 70 Đ7 k2, k4; Đ8 k2, k4, k5; Luật Căn cước Đ10 k8: tổ chức khác khai thác CSDL dân cư khi cơ quan quản lý căn cước và công dân đồng ý.
- **Áp dụng**: BV công, BV tư, PK, vendor HIS/app · **Hiệu lực/hạn**: 01/07/2024
- **Mức**: BẮT BUỘC (cấm kết nối trực tiếp trái điều kiện; cấm chia sẻ lại kết quả) · BẮT BUỘC? (BV công có là "tổ chức cung cấp dịch vụ công" để kết nối trực tiếp hay không: chưa có giải thích)
- **Phần mềm phải**: vendor HIS/app tư nhân không tự kết nối CSDL dân cư hoặc hệ thống định danh; chỉ tích hợp qua tổ chức cung cấp dịch vụ xác thực được BCA cấp phép hoặc giải pháp trên app VNeID; luồng qua trung gian có bước người bệnh đồng ý và lưu bằng chứng; không chuyển kết quả xác thực cho bên thứ ba (bảo hiểm tư, đối tác), không dùng lại làm "đăng nhập" cho giao dịch khác; BV công kết nối trực tiếp thì phải có hồ sơ cấp độ 3 (xem ANM; NĐ 85/2016 đã hết hiệu lực từ 01/07/2026) và văn bản thống nhất với C06.
- **Bẫy**: "tích hợp xác thực VNeID/CSDL dân cư" của vendor nhỏ: hỏi đi qua trung gian nào, có văn bản/hợp đồng không. Tra thẻ BHYT trên Cổng BHXH (BHYT-GD-R02) là kênh khác, không phải xác thực danh tính theo NĐ 69. Ngưỡng cấp độ 3 ở đây do NĐ 69 đặt riêng cho kết nối định danh, không phải quy tắc "≥10.000 người bệnh" (C19, ANM-R02).

### SKDT-R09 — Lưu nguồn định danh và nguồn xác thực theo lượt
- **Căn cứ**: QĐ 2733 PL01 Đ5 bước 4; NĐ 69 Đ19 k4; Luật Căn cước Đ33 k2; BHYT-GD-R02 (lưu phản hồi tra cứu thẻ).
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: —
- **Mức**: NÊN (không văn bản buộc lưu "nguồn xác thực", nhưng là bằng chứng cho R04, R06, R07, R08)
- **Phần mềm phải**: mỗi lượt lưu `phuong_thuc_dinh_danh` (QR_CCCD | CHIP_CCCD | VNEID_APP | DICH_VU_XAC_THUC | TRA_CUU_BHXH | NHAP_TAY | CHUA_XAC_DINH), người thực hiện, thời điểm, mã giao dịch/mã phản hồi; không lưu ảnh căn cước nếu không cần.
- **Bẫy**: NĐ 69 Đ17 k2 và Đ28 k4 ("lưu 05 năm") là nghĩa vụ của hệ thống định danh quốc gia, không phải của HIS. Thời hạn log của cơ sở: xem ANM-R11 (C22: không có quy định riêng cho log truy cập HSBA; khuyến nghị lưu bằng thời hạn HSBA, tối thiểu 5 năm, NÊN, suy luận).

### B. Trường hợp đặc biệt về định danh

### SKDT-R10 — Người bệnh vô danh, không giấy tờ
- **Căn cứ**: Luật KCB Đ2 k10 (người bệnh không có thân nhân: cấp cứu không giấy tờ, không thân nhân, không thông tin liên lạc; không làm chủ nhận thức; trẻ dưới 06 tháng bị bỏ rơi), Đ72 k1 (kiểm kê, lập biên bản, lưu giữ tài sản), k2 (sau **48 giờ** không xác định được thân nhân thì thông báo UBND cấp xã; chuyển trẻ bị bỏ rơi vào cơ sở trợ giúp xã hội), Đ73 (tử vong không giấy tờ: thông báo UBND xã trong **24 giờ**; lấy và lưu mẫu thi thể).
- **Áp dụng**: BV công, BV tư, PK có cấp cứu · **Hiệu lực/hạn**: 01/01/2024
- **Mức**: BẮT BUỘC (quy trình Đ72, Đ73) · NÊN (cách đánh mã tạm)
- **Phần mềm phải**: tạo hồ sơ "chưa xác định danh tính" bằng mã tạm có quy tắc (ví dụ `VD-<mã cơ sở>-<yyyymmdd>-<seq>`), giới và tuổi ước lượng, đặc điểm nhận dạng; đồng hồ 48 giờ nhắc thông báo UBND xã; biên bản tài sản gắn hồ sơ; xác định được danh tính thì gộp về hồ sơ có số định danh (mã tạm thành alias, ghi người gộp, lý do); chỉ gửi Sổ SKĐT khi có định danh hợp lệ hoặc gửi lại sau khi gộp (suy luận).
- **Bẫy**: đừng để ô "số định danh bắt buộc" chặn mở hồ sơ cấp cứu.

### SKDT-R11 — Trẻ em chưa có số định danh, trẻ dưới 14 tuổi, người giám hộ
- **Căn cứ**: NĐ 70 Đ11 k2–3 (gốc-OCR): số định danh xác lập khi đăng ký khai sinh; trước đó trẻ chưa có số. Luật Căn cước Đ19 k3 (dưới 14 tuổi cấp căn cước theo nhu cầu). NĐ 69 Đ7 k1, Đ14 k2 (dưới 6 tuổi chỉ tài khoản mức 1; dưới 14 tuổi dùng tài khoản cần đồng ý của người đại diện qua VNeID). QĐ 2733 PL01 Đ7 k3: người giám hộ, người đại diện quản lý Sổ SKĐT của trẻ, người già, người khuyết tật khi họ không tự quản lý được. QĐ 1332 phần B trường 12–15 (người giám hộ/chăm sóc/đại diện); QĐ 2733 PL02 mục 1.3: các trường này chưa có trường XML tương ứng. QĐ 1551 PL01 có `NGUOI_GIAM_HO`, `SO_CCCD_NGH`; PL03: không có giấy tờ thì dùng mã tài khoản định danh điện tử. Trẻ dưới 6 tuổi KCB BHYT: BHYT-GD-R01, R05.
- **Áp dụng**: BV/PK sản, nhi; mọi cơ sở khám trẻ; KSK học đường · **Hiệu lực/hạn**: 01/07/2024; 31/05/2026 (QĐ 1551)
- **Mức**: BẮT BUỘC (thu thông tin người giám hộ/đại diện; dùng số định danh khi đã có) · NÊN (cách liên kết sơ sinh với mẹ)
- **Phần mềm phải**: hồ sơ sơ sinh tạo ngay khi sinh, liên kết `me_id` và số giấy chứng sinh (GIAYTO-R08), chưa có số định danh; cập nhật số sau khai sinh (nhập có đối chiếu hoặc lấy từ mã thẻ BHYT mới) và ghi vết; bảng người đại diện (họ tên, quan hệ, số định danh, điện thoại, căn cứ); kiểm tra tuổi để biết khi nào cần đồng ý của người đại diện (DLCN-R08).
- **Bẫy**: không bịa "số định danh tạm" 12 chữ số cho trẻ; mã tạm phải khác hẳn định dạng 12 số để không lọt vào `SO_CCCD` (suy luận).

### SKDT-R12 — Người nước ngoài và người gốc Việt chưa xác định quốc tịch
- **Căn cứ**: NĐ 102 Đ6, Đ10 k5 c (chỉ người nước ngoài có tài khoản định danh). NĐ 69 Đ5 k1 (danh tính điện tử người nước ngoài gồm số định danh, hộ chiếu…), Đ7 k2 (từ đủ 6 tuổi có thẻ thường trú/tạm trú được cấp tài khoản). QĐ 2733 PL02 (gốc-OCR): `SO_CCCD` ghi căn cước, CMND hoặc hộ chiếu; không có thì mã tài khoản định danh; quốc tịch `MA_QUOCTICH` theo PL 2 TT 07/2016/TT-BCA. Luật Căn cước Đ30 k1, k2 c: người gốc Việt chưa xác định quốc tịch sống liên tục từ 06 tháng tại một xã được cấp giấy chứng nhận căn cước và xác lập số định danh.
- **Áp dụng**: BV công, BV tư, PK (nhất là cơ sở nhận khách quốc tế) · **Hiệu lực/hạn**: 01/07/2024–01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: loại giấy tờ là danh mục (`CAN_CUOC | SO_DINH_DANH_NN | HO_CHIEU | GIAY_CN_CAN_CUOC | TK_DINH_DANH | KHONG_CO`) kèm số và quốc gia cấp; quốc tịch theo danh mục mã; người nước ngoài không có tài khoản định danh thì lưu hộ chiếu, không suy ra mã định danh y tế; giấy chứng nhận căn cước coi như có số định danh.
- **Bẫy**: `SO_CCCD` trong XML là trường đa năng, không có trường loại giấy tờ; phía nhận không phân biệt được, MPI nội bộ phải lưu loại (suy luận). Hiệu lực TT 07/2016/TT-BCA và mã địa giới sau sắp xếp 2025: chưa xác minh.

### SKDT-R13 — Số định danh bị hủy, xác lập lại: MPI giữ lịch sử
- **Căn cứ**: NĐ 70 Đ11 k7, k8, k11 (gốc-OCR, diễn giải): hủy và xác lập lại số khi xác định lại giới tính, cải chính năm sinh, sai sót đăng ký khai sinh, dùng giấy tờ giả, giấy khai sinh bị thu hồi; số đã hủy được lưu và không cấp cho người khác. Đ12 k1: số đã hủy nằm trong QR căn cước.
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: 01/07/2024
- **Mức**: NÊN (văn bản buộc BCA; hệ quả với phần mềm là suy luận, nhưng thiếu thì MPI vỡ)
- **Phần mềm phải**: bảng định danh dạng lịch sử; tìm được theo số cũ; người bệnh trình căn cước số mới thì đề xuất ghép với hồ sơ số cũ (đọc từ QR); không xóa số cũ.
- **Bẫy**: `UNIQUE(so_dinh_danh)` cứng trên bảng người bệnh không chịu được đổi số; đặt ràng buộc ở bảng định danh, chỉ trên bản ghi đang hiệu lực.

### SKDT-R14 — Khử trùng hồ sơ, đối soát theo mã định danh
- **Căn cứ**: QĐ 1551 mục 3 e: dữ liệu "đúng, đủ, sạch, sống" và được ký số. CV 1129 mục 1 b, mục 4 (gốc-OCR, diễn giải): đối soát theo mã định danh cá nhân để hạn chế thống kê trùng, tránh một người bị khám, thanh toán trùng. Luật Căn cước Đ11 k4 (dữ liệu chuyên ngành lệch CSDL dân cư thì phối hợp điều chỉnh). NĐ 102 Đ24 k1. EMR-R05 (mỗi người bệnh một mã định danh đơn nhất).
- **Áp dụng**: mọi cơ sở; đơn vị KSK · **Hiệu lực/hạn**: —
- **Mức**: BẮT BUỘC? (có căn cứ về chất lượng dữ liệu, chưa có tiêu chí kiểm chứng)
- **Phần mềm phải**: cảnh báo trùng khi tạo mới (cùng số định danh; hoặc cùng họ tên chuẩn hóa, ngày sinh, giới, SĐT); hàng đợi rà soát trùng; gộp/tách có log và hoàn tác được; báo cáo số hồ sơ thiếu số định danh.

### C. Dữ liệu KSK định kỳ và sàng lọc (QĐ 1551)

Domain này là chủ của nghĩa vụ liên thông KSK theo QĐ 1551; GIAYTO-R19 dẫn chiếu về đây. Mẫu giấy KSK (TT 32/2023, TT 25/2026) và KSK lái xe: GIAYTO-R18, R20.

### SKDT-R15 — Dữ liệu KSK theo 17 mẫu, gửi trong 24 giờ, ký số
- **Căn cứ**: QĐ 1551 HD mục 3 b: trường thông tin tuân thủ kiểu và định dạng PL01; mục 3 c: chưa có phần mềm thì nhập trên Cổng dữ liệu sức khỏe `https://csdlksk.vn`; mục 3 d: dữ liệu khám trước ngày hướng dẫn rà soát, đồng bộ **trước 15/7/2026**; mục 4 a: liên thông về CSDL sức khỏe cá nhân của BYT "trong vòng 24 giờ sau khi kết thúc đợt khám", thủ công hoặc tự động theo PL02, "phải ký số trước khi đồng bộ". PL01: 17 mẫu (giấy KSK 6 đến dưới 18 tuổi; từ 18 tuổi; sổ KSK lái xe, nhân viên đường sắt, thuyền viên; trẻ theo 7 nhóm tháng tuổi và 2 đến dưới 6 tuổi; học sinh mầm non, lớp 1–5, 6–9, 10–12). Mỗi mẫu có `CKS_NGUOI_KET_LUAN`, `CKS_BENH_VIEN`, nhiều mẫu có `CKS_NGUOI_KHAM` từng chuyên khoa; trường hành chính theo QĐ 3176; `MA_LK` (mã đợt duy nhất), `DOI_TUONG` (14 mã), `NGUON_KINH_PHI` (NSTW, NSĐP, Quỹ BHYT, người sử dụng lao động, xã hội hóa, khác), `PHAN_LOAI_SK`, `KET_LUAN_BENH` (ICD-10 nhiều mã ";"). Mục 4 b: khám bệnh thông thường do BHXH chia sẻ sang BYT qua Nền tảng điều phối dữ liệu của TTDLQG (PL03), cơ sở không đẩy lần hai.
- **Áp dụng**: mọi cơ sở KCB tổ chức KSK định kỳ hoặc khám sàng lọc, công và tư · **Hiệu lực/hạn**: 31/05/2026; dữ liệu tồn 15/07/2026 (đã qua); thường xuyên 24 giờ
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi mẫu một schema có phiên bản, đúng tên chỉ tiêu, kiểu, độ dài; chữ ký số từng bác sĩ chuyên khoa, người kết luận và cơ sở; xác định thời điểm "kết thúc đợt khám" để chạy đồng hồ 24 giờ, cảnh báo quá hạn; chế độ đồng bộ lô cho dữ liệu tồn; lưu `DOI_TUONG` và `NGUON_KINH_PHI` (CV 1129 yêu cầu phân định nguồn kinh phí, tránh thanh toán trùng).
- **Bẫy**: (1) "đợt khám" chưa được định nghĩa là cả chiến dịch hay từng người; thận trọng tính theo từng phiếu đã kết luận (suy luận). (2) Mẫu sổ KSK lái xe của QĐ 1551 trùng phạm vi luồng KSK lái xe ↔ CSDL giao thông (GIAYTO-R20): có thể phải gửi hai nơi. (3) PL01 không có cột "bắt buộc"; danh sách trường bắt buộc chưa rõ. (4) QĐ 1551 chỉ nói KSK định kỳ và sàng lọc; KSK đi học, đi làm, theo yêu cầu có phải gửi không: chưa xác minh. (5) PL01 ban hành trước mẫu KSK mới của TT 25/2026 (01/07/2026): có thể lệch trường.

### SKDT-R16 — Tài khoản liên thông, mã định danh cơ sở 13 chữ số, tài khoản định danh tổ chức
- **Căn cứ**: QĐ 1551 HD mục 2 a: mỗi cơ sở 01 tài khoản liên thông dữ liệu và 01 tài khoản quản trị trên Cổng dữ liệu sức khỏe; mục 2 b: đăng ký trên Hệ thống quản lý quốc gia về hành nghề và hoạt động KCB (`https://app.qlhanhnghekcb.gov.vn/`), Sở Y tế hoặc BYT phê duyệt, hệ thống cấp "mã định danh 13 chữ số" cho cơ sở; cơ sở có trách nhiệm đăng ký "tài khoản định danh tổ chức" theo hướng dẫn BCA. NĐ 69 Đ6, Đ7 k3 (tài khoản định danh tổ chức), Đ40 k4 (tài khoản tổ chức do Cổng DVC cấp chỉ dùng đến 30/06/2025).
- **Áp dụng**: mọi cơ sở KCB có KSK; vendor quản lý cấu hình · **Hiệu lực/hạn**: 31/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấu hình theo cơ sở (đa tenant): mã 13 chữ số, tài khoản liên thông lưu trong kho bí mật (không hard-code), chứng thư số tổ chức; tách tài khoản quản trị (web) khỏi tài khoản liên thông (máy); hỗ trợ xoay mật khẩu.
- **Bẫy**: chuỗi PK nhiều điểm (mỗi điểm một giấy phép) cần một tài khoản cho mỗi cơ sở, không dùng chung (suy luận từ "mỗi cơ sở").

### SKDT-R17 — API Trục dữ liệu BYT (PL02 QĐ 1551)
- **Căn cứ**: QĐ 1551 PL02 (gốc): RESTful, HTTPS, JSON UTF-8, OAuth2 + Bearer. Môi trường: Cổng `https://csdlksk.vn` (sandbox `https://sandbox-csdlksk.vn`); "Trục dữ liệu Bộ Y tế": admin `https://admin.emrhub.vn`, API `https://api.emrhub.vn` (sandbox `https://admin-sandbox.emrhub.vn`, `https://api-sandbox.emrhub.vn`). `POST /api/auth/login` (tài khoản "Agent Account") trả `token`, `refresh_token`, `duration` (giây), `role` (`facility` | `department`). `POST /api/platform/data-sync/push`, header `Authorization: Bearer …`, `service-type: 100`; body `header{version, sender_id (13 số), receiver_id (ví dụ TDLBYT), txn_type = sync_checkup, msg_id = sender_id + YYMMDD + UUIDv4 bỏ gạch, msg_type = 101, data_type ∈ xml/base64 | json/base64 | png/base64 | jpg/base64 | pdf/base64, send_datetime (Unix ms 13 số)}`, `data` (Base64), `signature` (SHA256RSA trên header + data). Phản hồi: HTTP 200/400/401/403/404/500/504; `res_code` ∈ `CM_SUCCESS | CM_INVALID_REQUEST | PS_SIGNATURE_INVALID`; `msg_type 102`, `ref_msg_id`, `data.data_state`, `message_check_ca`, `message_notify`, chữ ký bên nhận. Ví dụ XML có `CKS_BENH_VIEN` là phần tử XMLDSig.
- **Áp dụng**: cơ sở chọn đồng bộ tự động; vendor phần mềm KSK · **Hiệu lực/hạn**: 31/05/2026
- **Mức**: BẮT BUỘC (khi dùng kênh tự động)
- **Phần mềm phải**: client cấp và làm mới token theo `duration`; `msg_id` đúng mẫu làm khóa idempotent; ký XMLDSig nội dung phiếu và SHA256RSA cho gói tin; lưu nguyên request, response, chữ ký phản hồi; `PS_SIGNATURE_INVALID` là lỗi cấu hình chứng thư, không thử lại mù; `CM_INVALID_REQUEST` thì sửa dữ liệu; 5xx thử lại có backoff; chạy sandbox trước production; allowlist tên miền đúng như PL02.
- **Bẫy**: ba địa chỉ có ba vai trò, không thay thế nhau: `app.qlhanhnghekcb.gov.vn` đăng ký và lấy mã 13 số; `csdlksk.vn` nhập tay/quản trị; `api.emrhub.vn` API đẩy dữ liệu. `emrhub.vn` không phải `.gov.vn` nhưng có trong bản gốc PL02 với tên "Trục dữ liệu Bộ Y tế": kiểm tra TLS, không lấy endpoint từ bài báo hay email lạ. Bảng thuộc tính PL02 đánh số trùng (1.5, 1.6): đặt tên trường theo bảng, không theo số thứ tự. Cột "bắt buộc" của `signature` để trống nhưng thân văn bản buộc ký số: coi là bắt buộc.

### SKDT-R18 — Hai hệ mã cơ sở: 5 ký tự và 13 ký tự (GLN)
- **Căn cứ**: QĐ 2733 PL01 Đ3: mã cơ sở theo QĐ 384/QĐ-BYT/2019 làm định danh cơ sở khi liên thông Sổ SKĐT; Đ4 k4 b: Sở Y tế cấp mã cho cơ sở chưa có. QĐ 1551 PL01: `MA_CSKCB` (5 ký tự) và `MA_GTIN_CSKCB` (theo chuẩn GLN, 13 ký tự); PL02 `sender_id` = mã 13 số.
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: —
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục cơ sở lưu cả hai mã, kiểm tra độ dài 5 và 13; XML BHXH/Sổ SKĐT dùng mã 5; bản tin KSK dùng cả hai, `sender_id` dùng mã 13. Mã 5 cũng nằm trong mã số giấy chứng sinh (GIAYTO-R08).
- **Bẫy**: thống nhất với BHYT-DATA-R24. Mã 13 số khác "số định danh của tổ chức" trong hệ thống định danh điện tử (NĐ 69 Đ6 k2). Chưa thấy văn bản riêng quy định cấu trúc GLN cho cơ sở KCB.

### D. Bảo mật, quản trị, báo cáo

### SKDT-R19 — Phạm vi truy cập, chia sẻ, lọc dữ liệu nhạy cảm
- **Căn cứ**: QĐ 2733 PL01 Đ7 (gốc-OCR, diễn giải): Sổ SKĐT có chế độ bảo mật như thông tin khác trên VNeID; bác sĩ, nhân viên y tế được truy cập trong quá trình KCB cho người bệnh; BYT là bên kiểm soát dữ liệu Sổ SKĐT, chia sẻ phải được BYT đồng ý. QĐ 31 Đ2 k2 a (tuân thủ Luật KCB Đ69 và Luật BVDLCN 2025). NĐ 102 Đ9 k2 b, Đ10 k2 c, Đ23 k3. Liên quan DLCN-R01, R32, R33.
- **Áp dụng**: BV công, BV tư, PK, vendor · **Hiệu lực/hạn**: 17/09/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dữ liệu người bệnh xuất trình từ VNeID chỉ dùng cho lượt hiện tại, có log ai xem; vendor không gom dữ liệu Sổ SKĐT của khách hàng vào kho chung; bộ lọc trước khi gửi cho dữ liệu hạn chế (đơn ARV, xét nghiệm HIV theo DLCN-R32) và quy tắc cấu hình; TLS, ký số.
- **Bẫy**: sau khi BHXH/BYT hiển thị lên VNeID, dữ liệu không còn do cơ sở kiểm soát; phần cơ sở chịu trách nhiệm là tính đúng của dữ liệu gửi và việc lọc trước khi gửi.

### SKDT-R20 — Báo cáo 6 tháng về liên thông Sổ SKĐT
- **Căn cứ**: QĐ 2733 PL01 Đ8 (gốc-OCR, đã đối chiếu ảnh): báo cáo 6 tháng một lần trên trang báo cáo trực tuyến của Cục QLKCB (`cdc.kcb.vn`): 6 loại hình (khám ngoại trú, điều trị ngoại trú, lĩnh thuốc theo hẹn, nội trú, ban ngày, KCB từ xa) × có/không BHYT × số lượt/đã liên thông; kèm khó khăn, kiến nghị. CV 1129 mục 1 g: UBND tỉnh báo cáo hằng tháng về BYT số người đã khám theo nhóm, nguồn kinh phí, mức cập nhật dữ liệu.
- **Áp dụng**: BV công, BV tư, PK; đơn vị KSK theo phân công của tỉnh · **Hiệu lực/hạn**: 17/09/2024; 16/09/2026
- **Mức**: BẮT BUỘC? (QĐ 2733 là hướng dẫn thí điểm; QĐ 31 dẫn chiếu nhưng không nhắc lại Đ8)
- **Phần mềm phải**: báo cáo dựng sẵn đúng ma trận Đ8 từ trạng thái gửi của R01; báo cáo KSK theo `DOI_TUONG` × `NGUON_KINH_PHI` × trạng thái đồng bộ.

### SKDT-R21 — Quy chế và quy trình Sổ SKĐT tại cơ sở
- **Căn cứ**: QĐ 2733 Đ4 k5 a, PL01 Đ4 k4–5 (gốc-OCR, diễn giải): lập kế hoạch, phân công cán bộ chuyên môn và CNTT, giám sát chất lượng dữ liệu; bảo đảm ANM khi kết nối; quy chế và quy trình được thủ trưởng phê duyệt.
- **Áp dụng**: BV công, BV tư, PK · **Hiệu lực/hạn**: 17/09/2024
- **Mức**: BẮT BUỘC? (văn bản thí điểm; nghĩa vụ tổ chức hơn là phần mềm)
- **Phần mềm phải**: vendor cung cấp mẫu quy trình, tài liệu cấu hình; màn hình giám sát chất lượng dữ liệu (lượt thiếu tóm tắt, thiếu số định danh, lỗi gửi).

### SKDT-R22 — Người đại diện hợp pháp; địa giới không còn cấp huyện
- **Căn cứ**: QĐ 31 Đ2 k3 a (thông tin người đại diện hợp pháp, nếu có). QĐ 1332 phần B trường 9 (nơi quản lý hồ sơ sức khỏe), mục 1.2 (địa chỉ cư trú làm căn cứ chuyển dữ liệu về hồ sơ sức khỏe địa phương), mục 1.3. Luật KCB Đ8 (người đại diện, qua DLCN-R08). QĐ 1551 dùng `MATINH_CU_TRU` 3 ký tự, `MAXA_CU_TRU` 5 ký tự, không có cấp huyện.
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: như R01
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: địa chỉ cư trú có mã tỉnh, mã xã chuẩn hiện hành; danh mục địa giới có hiệu lực theo thời gian để dữ liệu cũ vẫn hợp lệ; người đại diện có số định danh.
- **Bẫy**: QĐ 2733 PL02 (2024) còn `MAHUYEN_CU_TRU` theo QĐ 124/2004/QĐ-TTg; đừng copy cấu trúc địa chỉ 2024.

### E. Định hướng

### SKDT-R23 — Lồng ghép KSK với KCB, tránh khám và thanh toán trùng
- **Căn cứ**: CV 1129 mục 1 b, 1 d, 2 c, 3 b (gốc-OCR, diễn giải): lồng ghép KSK định kỳ, sàng lọc, học đường, người lao động với KCB BHYT; kế thừa kết quả khám còn giá trị lâm sàng; kết nối dữ liệu KSK với KCB BHYT, xét nghiệm, CĐHA; BHXH đối soát để ngăn thanh toán trùng. CT 17 (thứ cấp): mục tiêu từ 2026 người dân được khám ít nhất mỗi năm 01 lần và lập Sổ SKĐT.
- **Áp dụng**: cơ sở tham gia KSK · **Hiệu lực/hạn**: 16/09/2026
- **Mức**: NÊN (chỉ đạo điều hành, chưa có hướng dẫn kỹ thuật)
- **Phần mềm phải**: khi mở phiếu KSK hiển thị CLS còn hiệu lực của người đó; đánh dấu chỉ tiêu "kế thừa" kèm nguồn; chặn hai phiếu KSK cùng người, cùng năm, khác nhóm đối tượng.

### SKDT-R24 — Chuẩn bị cho Luật Định danh và xác thực điện tử, VNeID mini app
- **Căn cứ**: QĐ 940 mục VII.1 b, c (gốc-OCR, diễn giải): BCA trình QH Luật Định danh và xác thực điện tử trong năm 2026; VNeID thành siêu ứng dụng có nền tảng Mini App cho bên thứ ba. Dự thảo luật (thứ cấp): 3 mức xác thực, Open API, lưu nhật ký xác thực ≥ 5 năm.
- **Áp dụng**: vendor app, HIS · **Hiệu lực/hạn**: dự thảo
- **Mức**: NÊN
- **Phần mềm phải**: lớp adapter "nhà cung cấp định danh" để thay cơ chế xác thực khi luật mới có hiệu lực; không gắn logic nghiệp vụ vào một nhà cung cấp.

## 3. Pattern thiết kế

### SKDT-P01 — MPI hướng định danh, có lịch sử và alias
- **Giải quyết**: R05, R10, R11, R12, R13, R14
- **Cách làm**: tách "người bệnh" khỏi "định danh"; một người bệnh có nhiều định danh theo thời gian; khóa liên thông là số định danh đang hiệu lực. Tiếp đón tìm theo bất kỳ định danh nào → không có thì tạo mới với trạng thái phù hợp → bổ sung số định danh thì kiểm tra trùng và đề xuất gộp.
- **Gợi ý dữ liệu**: `patient(id, ma_bn UNIQUE, trang_thai_dinh_danh ENUM('DA_XAC_DINH','TAM','VO_DANH','SO_SINH_CHUA_KS'), ho_ten, ngay_sinh, gioi_tinh, quoc_tich, merged_into)`; `patient_identifier(patient_id, loai ENUM('SDDCN','CMND9','SDDCN_DA_HUY','SDD_NN','HO_CHIEU','GCN_CAN_CUOC','TK_DINH_DANH','MA_THE_BHYT','GIAY_CHUNG_SINH','MA_TAM'), gia_tri, quoc_gia_cap, hieu_luc_tu, hieu_luc_den, nguon)` với `UNIQUE(loai, gia_tri) WHERE hieu_luc_den IS NULL AND loai IN ('SDDCN','SDD_NN')`, CHECK `SDDCN ~ '^[0-9]{12}$'`, `MA_TAM !~ '^[0-9]{12}$'`; `patient_link(patient_id, related_id, quan_he ENUM('ME','CHA','GIAM_HO','DAI_DIEN','NGUOI_CHAM_SOC'), so_dinh_danh_lien_quan, dien_thoai, can_cu, hieu_luc_tu, hieu_luc_den)`; `patient_merge_log(from_id, to_id, ly_do, bang_chung, user_id, ts, undo_of)`; chỉ mục tìm trùng mờ `(unaccent(lower(ho_ten)), ngay_sinh, gioi_tinh)`.
- **Đánh đổi**: phức tạp hơn một cột `cccd`, đổi lại xử lý đổi số, sơ sinh, vô danh, người nước ngoài không phải sửa schema.

### SKDT-P02 — Bản ghi nguồn định danh và xác thực theo lượt
- **Giải quyết**: R04, R06, R07, R08, R09
- **Cách làm**: mỗi lần định danh/xác thực tạo một dòng append-only; kết quả xác thực không tái dùng cho phiên đăng nhập khác (NĐ 69 Đ19 k4).
- **Gợi ý dữ liệu**: `encounter_identity_check(encounter_id, phuong_thuc, dinh_danh_ap_dung, ket_qua, ma_giao_dich, nha_cung_cap_xac_thuc, dong_y_id, nguoi_thuc_hien, ts)`; không lưu ảnh căn cước, QR chỉ lưu trường cần thiết và số cũ.
- **Đánh đổi**: thêm thao tác ghi, bù lại có bằng chứng khi kiểm tra hoặc tranh chấp danh tính.

### SKDT-P03 — Cổng adapter xác thực danh tính
- **Giải quyết**: R08, R24
- **Cách làm**: interface `IdentityVerifier.verify(subject, method)`; triển khai `QrCccdParser` (offline), `ChipReader` (thiết bị chuyên dụng, cần đồng ý), `ThirdPartyAuthProvider` (tổ chức được BCA cấp phép, có bước đồng ý), `DirectNdaIntegration` (chỉ bật khi có văn bản với C06 và hồ sơ cấp độ 3). Cờ theo cơ sở, mặc định tắt kênh trực tiếp.
- **Gợi ý dữ liệu**: `identity_provider_config(facility_id, provider, enabled, legal_basis_ref, valid_from)`.
- **Đánh đổi**: thêm lớp trừu tượng; tránh khóa vào một nhà cung cấp.

### SKDT-P04 — Outbox Sổ SKĐT hai đích
- **Giải quyết**: R01, R02, R15, R17, R20
- **Cách làm**: sự kiện "đóng lượt KCB" hoặc "kết luận phiếu KSK" ghi `outbound_message` trong cùng transaction. Đích `BHXH_GDBHYT`: XML (Bảng 1 + 8 cho lượt không BHYT; đủ bảng cho BHYT), ký, gửi Cổng giám định. Đích `BYT_TRUC_DL`: phiếu KSK theo PL01, XMLDSig, đóng gói PL02, ký SHA256RSA. Lỗi chữ ký thì dừng thử lại, báo quản trị. Cùng hạ tầng với GIAYTO-P03 và HTTT-BC-P01.
- **Gợi ý dữ liệu**: `outbound_message(dich, loai, encounter_id|ksk_id, msg_id UNIQUE, payload_hash, payload_ref, trang_thai, so_lan_thu, han_chot_at, gui_luc, res_code, res_body_ref, chu_ky_phan_hoi)`; chỉ mục `(trang_thai, han_chot_at)`; `han_chot_at` = kết thúc + 24h cho KSK.
- **Đánh đổi**: cần job nền và lưu payload; bù lại idempotent, kiểm chứng và báo cáo được.

### SKDT-P05 — Schema phiếu KSK có phiên bản theo mẫu
- **Giải quyết**: R15
- **Cách làm**: kiểm tra dữ liệu bằng JSON Schema sinh từ PL01 (kiểu, độ dài); mẫu mới thêm phiên bản, không sửa phiên bản cũ.
- **Gợi ý dữ liệu**: `ksk_form_template(code, phien_ban, hieu_luc_tu, json_schema)`; `ksk_record(patient_id, template_code, phien_ban, doi_tuong, nguon_kinh_phi, dot_kham_id, ket_luan_luc, data JSONB, trang_thai_ky)`; `ksk_signature(record_id, phan, signer, cert_serial, ts, sig_ref)`.
- **Đánh đổi**: JSONB linh hoạt khi BYT đổi mẫu; thống kê cần view hoặc cột sinh.

### SKDT-P06 — Bộ lọc dữ liệu nhạy cảm trước khi gửi
- **Giải quyết**: R03, R19
- **Cách làm**: rule engine áp lên payload trước khi ký, loại hoặc che chỉ định và kết quả gắn nhãn hạn chế (HIV theo DLCN-R32; danh sách khác cấu hình được).
- **Gợi ý dữ liệu**: `filter_rule(id, nhan, field_path, hanh_dong, can_cu)`; `filter_log(message_id, rule_id, field_path)`.
- **Đánh đổi**: Sổ SKĐT có thể thiếu dữ liệu; cần chính sách được cơ sở phê duyệt (R21).

### SKDT-P07 — Danh mục cơ sở và địa giới có hiệu lực theo thời gian
- **Giải quyết**: R18, R22
- **Cách làm**: bản tin cũ dựng lại theo mã đúng thời điểm.
- **Gợi ý dữ liệu**: `facility(ma_bhxh CHAR(5), ma_gln CHAR(13), ten, hieu_luc_tu, hieu_luc_den)`; `dia_gioi(ma, cap, ten, hieu_luc_tu, hieu_luc_den, thay_the_boi)`.
- **Đánh đổi**: truy vấn phải luôn kèm ngày hiệu lực.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| SKDT-A01 | R01 | Lấy 20 lượt đã đóng trong tháng (10 BHYT, 10 viện phí; đủ ngoại trú, nội trú, lĩnh thuốc hẹn, từ xa nếu có): lượt nào có bản tin gửi Cổng? | Truy vấn lượt JOIN log gửi; mã phản hồi | BẮT BUỘC |
| SKDT-A02 | R02 | Mở XML của một lượt viện phí: có Bảng 1, Bảng 8, ký số (`CHUKYDONVI`), `MA_THE_BHYT` để trống? | File XML; kết quả kiểm chữ ký | BẮT BUỘC |
| SKDT-A03 | R02 | Lượt ngoại trú có gửi XML8 không? Không gửi thì Sổ SKĐT thiếu tóm tắt | Cấu hình gửi bảng; mẫu XML | BẮT BUỘC? |
| SKDT-A04 | R03 | Đóng lượt bỏ trống tóm tắt: có chặn/cảnh báo? Đọc 10 tóm tắt: đủ 4 ý, có bác sĩ điều trị? | Ảnh màn hình; mẫu dữ liệu | BẮT BUỘC |
| SKDT-A05 | R04, R05 | Tiếp đón thử: chỉ số định danh 12 số; chỉ QR căn cước; VNeID; chỉ số thẻ BHYT. Ca nào bị chặn? Có kiểm 12 chữ số? | Ảnh màn hình; schema cột | BẮT BUỘC |
| SKDT-A06 | R05, R14 | `SELECT so_dinh_danh, COUNT(*) … HAVING COUNT(*)>1`; tỷ lệ hồ sơ có số định danh 12 tháng | Kết quả truy vấn | BẮT BUỘC |
| SKDT-A07 | R06, R07 | Form tiếp đón có trường bắt buộc ảnh/scan căn cước, sổ khám, giấy ra viện? Quầy có photo căn cước? | Cấu hình; quan sát | BẮT BUỘC |
| SKDT-A08 | R07, R13 | Quét QR căn cước của người có CMND cũ: có lưu số cũ và tìm ra hồ sơ cũ? | Ảnh màn hình; bảng định danh | NÊN |
| SKDT-A09 | R08 | Hỏi vendor về "xác thực VNeID/CSDL dân cư": trực tiếp hay qua tổ chức nào? Có văn bản C06/hợp đồng? Có bước đồng ý? Kết quả có chuyển bên thứ ba? | Hợp đồng, sơ đồ luồng, log | BẮT BUỘC |
| SKDT-A10 | R08 | Nếu kết nối trực tiếp: có quyết định phê duyệt cấp độ 3 trở lên? | Hồ sơ cấp độ (ANM) | BẮT BUỘC |
| SKDT-A11 | R09 | Mỗi lượt có ghi phương thức định danh/xác thực, người thực hiện, thời điểm? | Bảng log | NÊN |
| SKDT-A12 | R10 | Mở hồ sơ cấp cứu vô danh không cần số định danh? Có cảnh báo 48 giờ, biên bản tài sản? Gộp có log và hoàn tác? | Ảnh màn hình; merge log | BẮT BUỘC |
| SKDT-A13 | R11 | Hồ sơ sơ sinh có liên kết mẹ, số giấy chứng sinh, cập nhật số định danh sau khai sinh? Mã tạm có thể trùng định dạng 12 số? | Ảnh màn hình; ràng buộc CHECK | BẮT BUỘC |
| SKDT-A14 | R12 | Khách nước ngoài chỉ có hộ chiếu: lưu loại giấy tờ, quốc gia cấp, mã quốc tịch? XML ghi gì vào `SO_CCCD`? | Ảnh màn hình; XML | BẮT BUỘC |
| SKDT-A15 | R15 | Đợt KSK gần nhất: thời gian từ kết luận đến gửi thành công; phiếu nào quá 24 giờ? Dữ liệu trước 31/05/2026 đã đồng bộ trước 15/07/2026? | Log outbox; báo cáo trên csdlksk.vn | BẮT BUỘC |
| SKDT-A16 | R15 | So schema phiếu KSK với PL01 QĐ 1551: tên chỉ tiêu, kiểu, độ dài; đủ chữ ký số từng phần? | Bảng so sánh; payload | BẮT BUỘC |
| SKDT-A17 | R16, R18 | Cấu hình cơ sở có mã 13 số, mã 5 ký tự, tài khoản liên thông riêng, tài khoản định danh tổ chức? Mật khẩu lưu ở đâu? | Ảnh cấu hình; kho bí mật | BẮT BUỘC |
| SKDT-A18 | R17 | Log gọi API: endpoint đúng `api.emrhub.vn` hoặc sandbox; `msg_id` đúng mẫu; có `signature`; xử lý `PS_SIGNATURE_INVALID` | Log request/response | BẮT BUỘC |
| SKDT-A19 | R19 | Gửi thử lượt có xét nghiệm HIV dương tính/đơn ARV: payload có chứa không? Vendor có bản sao dữ liệu Sổ SKĐT ngoài hệ thống khách hàng? | Payload; hợp đồng xử lý dữ liệu | BẮT BUỘC |
| SKDT-A20 | R20 | Xuất được bảng báo cáo 6 tháng theo QĐ 2733 PL01 Đ8? Đã nộp trên cdc.kcb.vn? | Báo cáo; xác nhận nộp | BẮT BUỘC? |
| SKDT-A21 | R21 | Có quy chế, quy trình Sổ SKĐT được thủ trưởng phê duyệt? | Văn bản | BẮT BUỘC? |
| SKDT-A22 | R22 | Danh mục địa giới dùng mã tỉnh 3, mã xã 5 hiện hành? Còn bắt buộc cấp huyện? | Danh mục; form | BẮT BUỘC |
| SKDT-A23 | R23 | Phiếu KSK có hiện CLS còn hiệu lực, chặn phiếu trùng trong năm? | Ảnh màn hình | NÊN |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 21/05/2024 | QĐ 1332: mẫu Sổ SKĐT VNeID | BYT; cơ sở KCB | Đã qua |
| 01/07/2024 | Luật Căn cước, NĐ 69, NĐ 70 có hiệu lực | Mọi tổ chức | Đã qua |
| 17/09/2024 | QĐ 2733: liên thông Sổ SKĐT qua Cổng giám định; báo cáo 6 tháng | Cơ sở KCB công, tư | Đã qua |
| 30/06/2025 | Hết dùng tài khoản tổ chức do Cổng DVC cấp; phải có tài khoản định danh tổ chức | Tổ chức, kể cả cơ sở KCB | Đã qua |
| 01/07/2025 | NĐ 102: mã định danh y tế = số định danh; nghĩa vụ kết nối Sổ SKĐT | Mọi cơ sở y tế | Đã qua |
| 01/01/2026 | Liên thông Sổ SKĐT VNeID cho mọi người bệnh (QĐ 31 Đ5) | Cơ sở KCB | Đã qua |
| 06/01/2026 | QĐ 31: Sổ SKĐT thay sổ giấy trong TTHC | Cơ sở KCB, cơ quan TTHC | Đã qua |
| 06/05/2026 | CT 17: KSK định kỳ/sàng lọc miễn phí từ 2026 (thứ cấp) | UBND tỉnh, cơ sở KCB | Đã qua |
| 11/05/2026 | QĐ 826: chỉ tiêu căn cước thay thẻ BHYT 50% (2026) | BYT, BCA (gián tiếp BV) | Đã qua |
| 31/05/2026 | QĐ 1551: liên thông KSK 24 giờ; tài khoản, mã 13 số | Cơ sở có KSK | Đã qua |
| 15/07/2026 | Hạn đồng bộ dữ liệu KSK đã khám trước 31/05/2026 | Cơ sở có KSK | Đã qua |
| 16/09/2026 | CV 1129: lồng ghép, đối soát theo mã định danh; tỉnh báo cáo hằng tháng | UBND tỉnh, BYT, BHXH, BCA | Đã qua |
| 15/10/2026 | Hết "chiến dịch 100 ngày" Sổ SKĐT (thứ cấp, gắn với CT 07/CT-BYT, chưa đọc gốc) | Cơ sở KCB | Sắp tới |
| Cuối 2026 | Trình Luật Định danh và xác thực điện tử (QĐ 940) | BCA; vendor theo dõi | Sắp tới |
| 31/12/2026 | Mục tiêu toàn dân được khám và lập Sổ SKĐT (CT 17, thứ cấp) | Địa phương, cơ sở KCB | Sắp tới |
| 2030 | 100% người dân có HSSK điện tử liên thông; căn cước thay thẻ BHYT 80% (QĐ 826) | BYT, BCA | Sắp tới |
| Thường xuyên | Gửi Sổ SKĐT sau mỗi lượt (BHXH hiển thị ≤ 24 giờ sau nhận); KSK ≤ 24 giờ sau đợt khám; báo cáo 6 tháng | Cơ sở KCB | — |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**
- NĐ 59/2022/NĐ-CP → NĐ 69/2024 (Đ40 k2, 01/07/2024); tài khoản và giấy xác nhận cấp theo NĐ 59 còn giá trị đến hết hạn (Đ40 k5).
- QĐ 34/2021/QĐ-TTg (định danh, xác thực trên CSDL dân cư): NĐ 69 Đ40 không nêu tên; tình trạng chưa xác minh.
- QĐ 06/QĐ-TTg (Đề án 06, 2022–2025) → tiếp nối bởi QĐ 826/QĐ-TTg (2026–2030). QĐ 1332, 2733 còn lấy QĐ 06 làm căn cứ; trích mục tiêu hiện hành thì dùng QĐ 826.
- QĐ 1332 (mẫu) → QĐ 2733 (hướng dẫn thí điểm) → QĐ 31 (nghĩa vụ cho mọi người bệnh) → QĐ 1551 (dữ liệu KSK, Trục dữ liệu BYT): **cộng dồn**, không văn bản nào thay văn bản nào.
- Chuẩn XML: QĐ 130 → 4750 → 3176 → QĐ 1931/QĐ-BYT năm 2026 sửa QĐ 130 (không nhầm với QĐ 1931 năm 2016; xem BHYT-DATA §6). QĐ 2733 PL02 ánh xạ theo 130/4750; QĐ 1551 PL01 dẫn 3176 cho trường hành chính.

**Bẫy trích dẫn**
1. "QĐ 31 buộc từ 01/01/2026" đúng câu chữ, nhưng căn cứ cấp VBQPPL là NĐ 102 Đ10 k5 b và Đ23 k2; QĐ 31, 2733, 1551 là quyết định hành chính/hướng dẫn.
2. QĐ 31 và QĐ 1551 lấy NĐ 42/2025 làm căn cứ thẩm quyền BYT; NĐ 42 đã được NĐ 313/2026 thay (theo inventory). Hai QĐ không vì thế mà mất hiệu lực.
3. Không trích NĐ 69 Đ17 k2, Đ28 k4 ("lưu 05 năm") làm thời hạn log của HIS.
4. "Xác thực" trong NĐ 69 (danh tính) khác "xác thực dữ liệu" trong NĐ 188 Đ69 k9 (ký số hồ sơ chi phí, BHYT-GD-R18).
5. Mã 13 số (QĐ 1551, GLN) ≠ mã 5 ký tự (QĐ 384/2019) ≠ số định danh tổ chức (NĐ 69 Đ6 k2).
6. `emrhub.vn` là endpoint chính thức theo bản gốc QĐ 1551 PL02; đừng lấy endpoint không có trong văn bản.
7. "Người nước ngoài dùng số định danh làm mã định danh y tế" chỉ đúng khi đã có tài khoản định danh điện tử (thường là người có thẻ thường trú/tạm trú).
8. Số hiệu QĐ 940 trên bản OCR bị đọc thành "3420"; ảnh bản gốc là 940/QĐ-TTg ngày 26/5/2026.
9. QĐ 2733 PL02 còn mã huyện (QĐ 124/2004/QĐ-TTg); QĐ 1551 đã bỏ cấp huyện.
10. Câu chữ QĐ 1332, QĐ 2733, NĐ 69, NĐ 70, QĐ 826, QĐ 940, CV 1129 lấy từ OCR: file này chỉ diễn giải, không trích nguyên văn (số và ngày đã đối chiếu).
11. Văn bản nói về cấp độ an toàn HTTT: NĐ 85/2016 đã hết hiệu lực từ 01/07/2026 (C07); dẫn theo khung pháp luật hiện hành ở ANM.

**Mâu thuẫn đã phân xử**
- Một hay nhiều điểm tích hợp: **nhiều điểm**. (a) Lượt KCB, mọi người bệnh: XML lên Cổng giám định BHYT; BHXH hiển thị VNeID ≤ 24 giờ và chia sẻ sang CSDL sức khỏe cá nhân của BYT qua Nền tảng điều phối của TTDLQG (QĐ 1551 mục 4 b, PL03). (b) KSK định kỳ/sàng lọc: cơ sở đẩy lên CSDL sức khỏe cá nhân của BYT qua `csdlksk.vn` hoặc `api.emrhub.vn`. (c) Đơn thuốc: kênh DUOC. (d) Giấy chứng sinh, báo tử: Cổng DVC quốc gia (GIAYTO-R08, R10). Cơ sở không kết nối trực tiếp VNeID.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. Hướng dẫn kết nối của cơ quan quản lý CSDL Sổ SKĐT VNeID (QĐ 31 Đ4 k2): chưa thấy. Cơ sở có kênh nào để **đọc** Sổ SKĐT (có đồng ý) hay chỉ xem app người bệnh xuất trình?
2. CV 4395/BYT-KCB: cần bản gốc để xác nhận bộ bảng tối thiểu cho lượt không BHYT, nghĩa vụ đăng ký với BHXH tỉnh của cơ sở không ký hợp đồng, còn áp dụng sau 3176 và QĐ 1931 năm 2026 không. Hỏi BHXH VN hoặc Cục QLKCB.
3. XML8 cho lượt ngoại trú (R02): ghi chú bảng 2023 và QĐ 2733 PL02 vênh nhau.
4. BV công có là "tổ chức cung cấp dịch vụ công" (NĐ 69 Đ18 k1; Luật Căn cước Đ32 k1) để kết nối trực tiếp? Hỏi luật sư hoặc C06.
5. Danh sách tổ chức được BCA cấp phép dịch vụ xác thực (NĐ 69 Đ22 k3) và thông tư BCA về thiết bị đọc chip: chưa đọc.
6. Trường bắt buộc trong bản tin KSK; định nghĩa "kết thúc đợt khám". Hỏi Trung tâm Thông tin y tế quốc gia.
7. KSK lái xe: gửi song song Trục dữ liệu BYT (QĐ 1551 mẫu 3) và CSDL giao thông (TT 36/2024)? (GIAYTO-R20.)
8. Chế tài khi không liên thông Sổ SKĐT hoặc dữ liệu KSK: chưa thấy điều khoản riêng; chế tài dữ liệu BHYT xem BHYT-GD-R30.
9. CT 17/CT-TTg: chưa có bản gốc (chỉ bài trên cổng Chính phủ và cổng địa phương). CT 07/CT-BYT ("chiến dịch 100 ngày" theo inventory; HTTT-BC mô tả CT 07 là chỉ thị xử lý điểm nghẽn CĐS) và NQ 221/NQ-CP: chỉ có nguồn thứ cấp, nội dung hai mô tả chưa đối chiếu được với nhau.
10. QĐ 831/QĐ-BYT (2017) và quan hệ với CSDL sức khỏe cá nhân (QĐ 1551 mục 1 a): chưa đọc bản gốc.
11. NQ 66.7/2025/NQ-CP Đ7 và NĐ 278/2025 (căn cứ QĐ 31): có thể đặt thêm nghĩa vụ chia sẻ cho BV công nếu được coi là cơ quan thuộc hệ thống chính trị (xem HTTT-BC-R20).
12. TT 07/2016/TT-BCA (mã quốc tịch, đơn vị hành chính) còn hiệu lực không; danh mục mã tỉnh, xã sau sắp xếp 2025 dùng trong XML.
13. Luật Định danh và xác thực điện tử: chưa thông qua tại 2026-10-06; theo dõi kỳ họp QH tháng 10/2026.
