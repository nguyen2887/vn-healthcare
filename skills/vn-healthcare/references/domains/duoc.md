# DUOC — Kê đơn điện tử, dược và nhà thuốc

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám (kê đơn, cấp phát), nhà thuốc, quầy thuốc, chuỗi nhà thuốc, bán thuốc qua TMĐT, vendor HIS/PK/phần mềm nhà thuốc · Research gốc: `research/deep/DUOC.md`

Phạm vi: kê đơn ngoại trú (hóa dược, sinh phẩm, YHCT), mã đơn, ký số, gửi Hệ thống đơn thuốc quốc gia (`donthuocquocgia.vn`, Cục QLKCB), thuốc phải kiểm soát đặc biệt (N, H, phóng xạ, độc), lưu đơn, phần mềm nhà thuốc GPP, liên thông Hệ thống cơ sở dữ liệu về dược (`csdlduoc.com.vn`, TTYQG vận hành), TMĐT thuốc, cấp phát tại cơ sở KCB. Tài liệu nghiên cứu, không phải ý kiến pháp lý.

## Tóm tắt nhanh

- Kê đơn điện tử đã là nghĩa vụ: BV hạn trước 01/10/2025, cơ sở KCB khác trước 01/01/2026 (TT 26/2025 Đ13 k3). Đơn phải gửi lên Hệ thống đơn thuốc QG ngay sau khi kết thúc khám (ngoại trú), trước khi ra viện (nội trú) — DUOC-R11, R12.
- Mã đơn 14 ký tự **đã gồm dấu "-"**: 5 ký tự mã cơ sở + 7 ký tự ngẫu nhiên [0-9a-z] + "-" + loại đơn N/H/C (T cho thuốc thang YHCT). Không dùng số tăng dần — DUOC-R04.
- Đơn đã gửi là bất biến: sửa = kê đơn mới thay thế, đơn cũ vẫn lưu nhưng không dùng để cấp/bán (QĐ 425 Đ9 k3 c) — DUOC-R09.
- Nhà thuốc, quầy thuốc phải quản lý mua bán bằng phần mềm và liên thông Hệ thống CSDL về dược với dữ liệu tính **từ 01/01/2026** (phải backfill). Không liên thông, không truy xuất: phạt 3–5 triệu (cá nhân), tổ chức gấp đôi (NĐ 90/2026 Đ59 k2 d, Đ4 k5) — DUOC-R25, R26.
- Bán thuốc kê đơn không có đơn: 10–20 triệu (cá nhân), tổ chức gấp đôi (NĐ 90/2026 Đ59 k4 g) — DUOC-R22.
- Mốc mới nhất: TT 32/2026 có hiệu lực 01/10/2026 (số đăng ký 12 chữ số mã hóa cờ kê đơn và KSĐB); hạn đăng ký tài khoản CSDL dược 04/10/2026 (thứ cấp) đã qua. Mốc gần tới: báo cáo năm thuốc KSĐB **trước 15/01/2027**.
- Bẫy dễ sai nhất: (1) không có con số pháp định cho thời hạn lưu đơn thuốc tại cơ sở KCB — mặc định ≥ 10 năm là suy luận; (2) phòng khám **không giường bệnh** không được dùng mẫu đơn "N"; (3) NĐ 90/2026 Đ41 chỉ áp cho cơ sở có điều trị nội trú và thời gian lưu theo dõi ngoại trú.

## Mục lục

- A. Kê đơn: R01 thẩm quyền kê · R02 mã liên thông · R03 mẫu đơn, trường bắt buộc · R04 mã đơn 14 ký tự · R05 quy tắc ghi thuốc · R06 giới hạn số ngày · R07 đơn N, H riêng, 03 bản · R08 hồ sơ kèm đơn N · R09 đơn bất biến, sửa = đơn mới · R10 khớp HSBA · R11 kê đơn điện tử và ký số · R12 gửi đơn đúng thời điểm · R13 chuẩn kết nối · R14 giao mã đơn cho người bệnh · R15 lưu và trích xuất đơn · R16 thời hạn hiệu lực đơn · R17 quy tắc riêng YHCT · R18 nhận lại thuốc KSĐB · R19 báo cáo thuốc KSĐB · R20 cấp phát đối chiếu đơn · R21 bảo mật dữ liệu đơn
- B. Nhà thuốc: R22 bán thuốc kê đơn phải có đơn · R23 bán theo đơn điện tử, báo cáo đã bán · R24 thay thế thuốc · R25 quản lý bằng phần mềm (XNT, lô, hạn) · R26 liên thông CSDL dược · R27 lưu hồ sơ, đơn tại nhà thuốc · R28 thuốc hạn chế bán lẻ · R29 bán thuốc TMĐT · R30 sổ theo dõi thuốc KSĐB
- C. Dữ liệu chủ: R31 phân loại theo số đăng ký · R32 cờ danh mục đặc biệt
- D. Thực hành tốt: R33 nhật ký vòng đời đơn · R34 cảnh báo liều, tương tác
- Pattern: P01–P10 · Audit: A01–A34

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| TT 26/2025/TT-BYT | Đơn thuốc, kê đơn hóa dược, sinh phẩm ngoại trú | 01/07/2025; e-Rx BV trước 01/10/2025, cơ sở khác trước 01/01/2026 (Đ13 k3) | Còn HL; thay TT 52/2017, 18/2018, 04/2022, 27/2021 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf) |
| TT 55/2025/TT-BYT | Kê đơn thuốc cổ truyền, dược liệu, kê kết hợp | 01/03/2026 | Còn HL; thay TT 44/2018; mẫu đơn thang cũ dùng đến 30/06/2026 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/55-byt.pdf) |
| TT 33/2025/TT-BYT | Thời hạn lưu trữ hồ sơ ngành y tế | 01/07/2025 | Còn HL; thay TT 53/2017 | gốc | [PDF thân](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [PDF phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| Luật 44/2024/QH15 | Sửa đổi Luật Dược 105/2016 | 01/07/2025 (một số điểm 01/01/2025) | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat44.pdf) |
| Luật 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB — Đ62–63 kê đơn, sử dụng thuốc | 01/01/2024 | Còn HL | gốc | [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| NĐ 163/2025/NĐ-CP | Chi tiết Luật Dược (Đ31–36 thuốc KSĐB; Đ41–42 TMĐT; Đ124 lộ trình) | 01/07/2025 | Còn HL; thay NĐ 54/2017, NĐ 88/2023 | gốc (Đ31, Đ35, Đ41, Đ42 đối chiếu bản Công báo có dấu); gốc-OCR phần còn lại | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/163nd.signed.pdf) |
| TT 02/2018/TT-BYT (VBHN 11/VBHN-BYT) | GPP, đã sửa bởi TT 12/2020, 29/2020, 11/2025 | 08/03/2018; phần sửa bởi TT 11/2025 từ 01/07/2025 | Còn HL; điểm đ k1 Đ5 bị bãi bỏ (QĐ 2656) | gốc | [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/11-vbhn-byt.pdf) |
| TT 11/2025/TT-BYT | Sửa GPP, GDP, GSP; Đ5 k2 liên thông dữ liệu từ 01/01/2026 | 01/07/2025 | Còn HL | gốc (qua VBHN 11) | (qua VBHN ở trên) |
| QĐ 2656/QĐ-BYT (19/08/2026) | Bãi bỏ điểm đ k1 Đ5 TT 02/2018 (bản tự kiểm tra GPP) | 19/08/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/2656-byt.signed.pdf) |
| TT 31/2025/TT-BYT | Chi tiết Luật Dược, NĐ 163 (Đ10 + PL III thuốc hạn chế bán lẻ) | 01/07/2025 | Còn HL; thay TT 07/2018 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/31-byt.pdf) |
| TT 20/2017/TT-BYT sửa bởi TT 27/2024/TT-BYT | Thuốc KSĐB: báo cáo, giao nhận, biên bản nhận lại | TT 27/2024: 30/01/2025 (thứ cấp) | Còn HL (vẫn được TT 26 dẫn; tình trạng TT 20 sau khi NĐ 54 hết HL cần xác nhận) | TT 27/2024: gốc; TT 20/2017: chưa xác minh | [VB 211680](https://vanban.chinhphu.vn/?pageid=27160&docid=211680) · [PDF TT 27/2024](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/27-byt.pdf) |
| TT 32/2026/TT-BYT (29/07/2026) | Đăng ký lưu hành thuốc (Đ15 tiêu chí OTC; PL V số đăng ký 12 chữ số) | **01/10/2026** | Còn HL; thay TT 12/2025 | gốc (bản do BV Ung Bướu đăng lại) | [PDF](https://benhvienungbuou.vn/wp-content/uploads/2026/08/Thong-tu-32.2026.TT-BYT-ngay-29.07.2026-quy-dinh-viec-dang-ky-luu-hanh-thuoc-nguyen-lieu-lam-thuoc-do-Bo-truong-Bo-Y-te-ban-hanh.pdf) |
| TT 12/2025/TT-BYT | Đăng ký lưu hành thuốc (cũ) | 01/07/2025 → hết HL 01/10/2026 | Bị TT 32/2026 thay | gốc-meta | [VB 213708](https://vanban.chinhphu.vn/?pageid=27160&docid=213708) |
| NĐ 90/2026/NĐ-CP | Xử phạt VPHC lĩnh vực y tế (Đ38, Đ41, Đ59, Đ85–86) | 15/05/2026 | Còn HL; thay NĐ 117/2020 | gốc-OCR có dấu (OCR tiếng Việt bản ký số; Đ4, Đ38 k5, Đ41, Đ59 đã đối chiếu ảnh) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| QĐ 425/QĐ-BYT (05/02/2025) | Quy chế Hệ thống thông tin quốc gia về quản lý kê đơn thuốc và bán thuốc theo đơn | Từ ngày ký | Còn HL; nhiều căn cứ đã bị thay (xem §6) | gốc-OCR có dấu (OCR tiếng Việt bản sao BVĐK Bạc Liêu đăng) | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20250404/529_Quyet_dinh-425-QD-BYT_60abac9cf6.pdf) |
| QĐ 808/QĐ-BYT (01/04/2022) | Hướng dẫn kết nối Hệ thống đơn thuốc QG | Từ ngày ký | Còn HL (chuẩn kết nối QĐ 425 Đ9 k2 dẫn) | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-808-qd-byt-bo-y-te-218990-d1.html) |
| QĐ 228/QĐ-QLD (03/04/2023) | Chuẩn kết nối CSDL Dược QG ↔ Hệ thống đơn thuốc QG (API lấy đơn, API cập nhật bán) | Từ ngày ký | Còn HL; quan hệ với QĐ 232/2026 chưa rõ | gốc (đã đọc bản ký số); link bản ký số chưa kiểm tra được | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-228-qd-qld-cuc-quan-ly-duoc-248169-d1.html) |
| QĐ 318/QĐ-QLD (04/06/2021) | Chuẩn kết nối phần mềm cơ sở phân phối thuốc | Từ ngày ký | Chưa rõ sau QĐ 232/2026 | gốc | [PDF](https://dav.gov.vn/upload_images/files/318_Q%C4%90_QLD_signed.pdf) |
| QĐ 1867/QĐ-BYT (24/06/2026) | Kế hoạch triển khai Hệ thống CSDL về dược | Từ ngày ký | Còn HL | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-1867-qd-byt-2026-trien-khai-he-thong-co-so-du-lieu-ve-duoc-438578-d1.html) |
| QĐ 232/QĐ-TTYQG (17/07/2026) | Đặc tả API v1.1 và hướng dẫn Hệ thống CSDL về dược | chưa xác minh | Còn HL | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-232-qd-ttyqg-2026-ban-hanh-tai-lieu-ky-thuat-api-va-huong-dan-su-dung-he-thong-co-so-du-lieu-duoc-441421-d1.html) |
| CV 934/TTYQG-DA (12/08/2026) | Triển khai CSDL dược: dữ liệu từ 01/01/2026; API hoặc nhập tay; xác thực VNeID | — | Đang áp dụng | thứ cấp | [luatvietnam, thứ cấp, nguồn duy nhất](https://luatvietnam.vn/tin-van-ban-moi/co-so-ban-buon-ban-le-thuoc-phai-lien-thong-du-lieu-tu-01-01-2026-len-he-thong-co-so-du-lieu-ve-duoc-186-111475-article.html) · [VNeID, thứ cấp](https://luatvietnam.vn/tin-van-ban-moi/nha-thuoc-thuc-hien-xac-thuc-tai-khoan-qua-vneid-khi-dang-nhap-he-thong-co-so-du-lieu-ve-duoc-186-111551-article.html) |
| CV 3656/QLD-KD (28/09/2026) | Đăng ký tài khoản CSDL dược trước 04/10/2026 | — | Đang áp dụng | thứ cấp | [luatvietnam, thứ cấp, nguồn duy nhất](https://luatvietnam.vn/tin-van-ban-moi/co-so-kinh-doanh-duoc-khan-truong-dang-ky-tai-khoan-tren-he-thong-co-so-du-lieu-ve-duoc-truoc-04-10-2026-186-112993-article.html) |
| TT 23/2011/TT-BYT | Sử dụng thuốc trong cơ sở có giường bệnh | — | Còn HL (TT 55 Đ3 k6 vẫn dẫn) | chưa xác minh | — |

## 2. Yêu cầu

### A. Kê đơn (HIS, EMR, phần mềm phòng khám)

### DUOC-R01 — Chỉ người có thẩm quyền mới được kê đơn
- **Căn cứ**: TT 26 Đ2 (bác sỹ, y sỹ có CCHN/GPHN); TT 55 Đ4 (ma trận chức danh × loại thuốc thang/cổ truyền/dược liệu; lương y chỉ kê thuốc nam dạng thang), Đ6 k1 b (một số chức danh chỉ kê kết hợp hóa dược khi người chịu trách nhiệm chuyên môn cho phép bằng văn bản), Đ6 k3 b, Đ15 k3 g.
- **Áp dụng**: BV, PK · **Hiệu lực/hạn**: 01/07/2025 (hóa dược); 01/03/2026 (YHCT)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu chức danh, số CCHN/GPHN, phạm vi hành nghề; chặn ký/phát hành đơn khi chức danh không có quyền với loại thuốc trong đơn; lưu số, ngày văn bản cho phép kê kết hợp.
- **Bẫy**: thẩm quyền YHCT phụ thuộc cả chức danh và loại thuốc, không chỉ "bác sĩ hay y sĩ".

### DUOC-R02 — Mã liên thông duy nhất của cơ sở và người kê đơn
- **Căn cứ**: TT 26 Đ12 k1 c, k5 d; QĐ 425 Đ3 k2–3 (mã người kê theo QĐ 3176/QĐ-BYT 29/10/2024; mã cơ sở theo QĐ 384/QĐ-BYT 01/02/2019), Đ9 k1 b, Đ9 k4, Đ20 k3 a: "Mỗi cơ sở và mỗi người kê đơn chỉ sử dụng một mã liên thông duy nhất".
- **Áp dụng**: mọi cơ sở KCB kê đơn · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trường mã liên thông cơ sở và người kê (một mã/người, dùng chung khi làm nhiều nơi); gắn vào mọi đơn gửi; quy trình cập nhật khi đổi nhân sự (QĐ 425 Đ9 k4 c).
- **Bẫy**: QĐ 425 Đ8 k1 đ — đơn vị phát triển, triển khai phần mềm **không được cấp tài khoản** trên Hệ thống đơn thuốc QG; vendor không giữ hộ tài khoản quản trị của cơ sở.

### DUOC-R03 — Mẫu đơn và trường thông tin bắt buộc
- **Căn cứ**: TT 26 Đ3 (PL I đơn thường, PL II đơn "N", PL III đơn "H"), Đ6 k1–4 (số định danh cá nhân/căn cước/hộ chiếu nếu có; nơi cư trú; trẻ dưới 72 tháng: số tháng tuổi, cân nặng, họ tên người đưa trẻ); chú thích PL I (đã có số định danh cá nhân thì không cần khai giới tính, ngày sinh, địa chỉ; mã thẻ BHYT; lời dặn gồm lịch tái khám); PL II, III thêm định danh người nhận thuốc; Đ4 k2 (khám nhiều chuyên khoa một lần: 01 đơn). TT 55 PL I (đơn thang: vị thuốc, khối lượng, số thang, cách sắc, cách uống), PL II, Đ8 k2–4. Luật KCB Đ63 k2: không kê thực phẩm chức năng trong đơn thuốc.
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025; YHCT 01/03/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: đủ trường theo mẫu; trẻ < 72 tháng bắt buộc tháng tuổi + cân nặng + người đưa trẻ; cho bỏ trống giới tính/ngày sinh/địa chỉ khi có số định danh cá nhân; bản in khớp bố cục PL; đơn N, H có ô người nhận thuốc; chặn sản phẩm không phải thuốc khỏi đơn.
- **Bẫy**: NĐ 90/2026 Đ41 k2 b phạt 10–20 triệu (cá nhân) hành vi kê vào đơn các sản phẩm không được kê đơn — nhưng Đ41 chỉ áp cho cơ sở có điều trị nội trú và thời gian lưu theo dõi ngoại trú (tiêu đề điều).

### DUOC-R04 — Mã đơn thuốc 14 ký tự
- **Căn cứ**: TT 26 PL I chú thích 1 (dùng chung PL II, III): "Mã đơn thuốc: có chiều dài 14 ký tự (bao gồm chữ số và chữ cái) được tạo ra tự động theo cấu trúc … xxxxxyyyyyyy-z." x (5) = mã cơ sở KCB; y (7) = giá trị ngẫu nhiên [0-9a-z] bảo đảm duy nhất tại một cơ sở; z = N (gây nghiện), H (hướng thần, tiền chất), C (đơn khác). TT 55 PL I chú thích 1: z = T (đơn thuốc thang).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025; YHCT 01/03/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh mã tự động; độ dài 14 tính cả "-" (5+7+1+1); phần y ngẫu nhiên (CSPRNG), không tăng dần; ràng buộc duy nhất (mã cơ sở, y); z suy ra từ nội dung đơn; mã bất biến sau phát hành.
- **Bẫy**: TT 55 PL II (đơn cổ truyền, dược liệu) chép lại chú thích "T: Đơn thuốc thang", không có ký tự riêng — không tự chế ký tự (§7). Bộ ký tự 5 ký tự đầu theo QĐ 384, chưa đọc.

### DUOC-R05 — Quy tắc ghi thuốc trong đơn
- **Căn cứ**: TT 26 Đ6 k5 (một hoạt chất: INN, hoặc INN + (tên thương mại); nhiều hoạt chất hoặc sinh phẩm: tên thương mại), k6 (tên, nồng độ/hàm lượng, số lượng, liều mỗi lần, số lần/ngày, đường dùng, thời điểm, số ngày; "Nếu đơn thuốc có thuốc độc phải ghi thuốc độc trước khi ghi các thuốc khác"), k7 (số lượng < 10 ghi số 0 phía trước; thuốc gây nghiện ghi số rồi ghi bằng chữ). TT 55 Đ8 k1 (tên tiếng Việt), k5 (thuốc thang: tên theo Dược điển, không viết tắt; vị < 10 g thêm số 0; vị từ dược liệu độc theo TT 13/2024 ghi số và chữ; trùng vị vượt liều ghi số, chữ và "tôi kê liều này", kể cả đơn điện tử), k6.
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: như R03
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục thuốc có INN, tên thương mại, số hoạt chất, cờ độc, cờ gây nghiện, cờ dược liệu độc; tự sinh tên hiển thị; tự đưa thuốc độc lên đầu; render "05"; thuốc N thêm số bằng chữ; bắt buộc nhập liều, đường dùng, thời điểm, số ngày; YHCT có xác nhận "tôi kê liều này".
- **Bẫy**: NĐ 90/2026 Đ38 k5 đ phạt 5–10 triệu (cá nhân) hành vi chỉ định điều trị, kê đơn bằng ngôn ngữ khác tiếng Việt khi ngôn ngữ đó chưa được đăng ký sử dụng. Giao diện đa ngôn ngữ không được in đơn bằng ngôn ngữ khác.

### DUOC-R06 — Giới hạn số ngày dùng thuốc
- **Căn cứ**: TT 26 Đ6 k8 a (≤ 30 ngày), k8 b + PL VII (252 bệnh/nhóm bệnh theo ICD-10: ≤ 90 ngày); Đ7 k2 (gây nghiện, cấp tính ≤ 7 ngày); Đ8 k1 (ung thư: mỗi lần ≤ 30 ngày, 3 đợt, mỗi đợt ≤ 10 ngày, ghi ngày bắt đầu/kết thúc); Đ9 k2–3 (hướng thần/tiền chất: cấp tính ≤ 10 ngày, dài ngày ≤ 30 ngày). TT 55 Đ8 k7 a (thang ≤ 30 ngày; có vị từ dược liệu độc ≤ 05 ngày; cấp tính ≤ 05 ngày; cổ truyền/dược liệu ≤ 90 ngày), k7 b.
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: như R03
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: rule engine (loại thuốc × ICD-10 × cấp/mạn); PL VII là master data có phiên bản; chặn/cảnh báo cứng khi vượt; đơn N ung thư có 3 đợt với ngày.
- **Bẫy**: PL VII ghi "Z69.64", "Z69.65" cho thay khớp háng/gối, khác mã ICD-10 thông dụng (suy luận: lỗi in của Z96.6x). Nạp nguyên văn rồi ánh xạ thêm, không tự sửa.

### DUOC-R07 — Đơn "N" và "H" là đơn riêng, 03 bản
- **Căn cứ**: TT 26 Đ7 k1 (đơn "N" dùng tại cơ sở KCB **có giường bệnh**, 03 bản: lưu cơ sở KCB, lưu HSBA, bản có dấu lưu tại nơi cấp/bán; cơ sở tự cấp thì không cần dấu); Đ9 k1 (đơn "H" 03 bản tương tự); PL II chú thích 10 (lĩnh đợt 2, 3 trước 01–03 ngày), 11 (người nhận xuất trình căn cước).
- **Áp dụng**: cơ sở KCB, nhà thuốc · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tách đơn theo loại; chặn tạo đơn N ở cơ sở không có giường (cấu hình loại hình); in đủ 03 bản có nhãn bản; lưu trạng thái đóng dấu/giao bản.
- **Bẫy**: TT 26 Đ10 cho đơn điện tử giá trị như giấy, nhưng Đ7, Đ9 vẫn yêu cầu bản có dấu lưu tại nơi bán. Chưa có hướng dẫn bỏ bản giấy cho N/H — suy luận: vẫn phải in.

### DUOC-R08 — Hồ sơ kèm đơn thuốc gây nghiện
- **Căn cứ**: TT 26 Đ7 k3 + PL IV (cam kết sử dụng thuốc gây nghiện, 02 bản), Đ7 k4 (danh sách chữ ký mẫu người kê N), Đ8 k1 (ung thư: lập HSBA ngoại trú), Đ8 k2 (người bệnh ung thư tại nhà: bác sỹ cơ sở có giường nội trú kê; xác nhận trạm y tế theo PL V, dùng cho một lần kê; kèm tóm tắt bệnh án).
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kê đơn N phải đính kèm/ghi nhận cam kết PL IV; mỗi xác nhận PL V dùng cho đúng một đơn; quản lý chữ ký mẫu; bắt buộc HSBA ngoại trú khi chẩn đoán ung thư.
- **Bẫy**: TT 26 Đ8 k2 dẫn "tóm tắt bệnh án theo PL XXIX TT 32/2023"; mẫu tóm tắt HSBA hiện hành là **Mẫu 03 PL II TT 25/2025** (C01; xem GIAYTO).

### DUOC-R09 — Đơn đã gửi bất biến; sửa đơn là kê đơn mới thay thế
- **Căn cứ**: TT 26 Đ6 k9 ("người kê đơn thực hiện kê đơn thuốc mới thay thế đơn thuốc cũ"); QĐ 425 Đ9 k3 c: "Đơn thuốc đã kê và gửi về Hệ thống không được thay đổi và cập nhật lại." Đơn cũ vẫn lưu trên hệ thống nhưng không cung cấp cho người bệnh để cấp phát, mua bán. TT 55 Đ9 k1.
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không UPDATE nội dung đơn đã phát hành; "sửa" = đơn mới (mã mới) liên kết `replaces`, đơn cũ chuyển "superseded"; thông báo người bệnh (TT 55 Đ15 k4 d).

### DUOC-R10 — Đơn phải khớp chỉ định trong HSBA
- **Căn cứ**: TT 26 Đ5 k1 b (có HSBA ngoại trú: chỉ định ghi HSBA, đơn phải phù hợp), k2 a (ra viện dùng tiếp 01–07 ngày: ghi HSBA nội trú và kê đơn phù hợp), k2 b (trên 07 ngày: kê đơn ngoại trú, lập HSBA ngoại trú hoặc chuyển viện); TT 55 Đ8 k7 c.
- **Áp dụng**: BV, PK có HSBA · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh đơn từ y lệnh trong HSBA (một nguồn dữ liệu); kiểm tra nhất quán khi ký.

### DUOC-R11 — Kê đơn điện tử và ký số
- **Căn cứ**: TT 26 Đ10 (đơn "được lập, hiển thị, ký số, chia sẻ, lưu trữ bằng phương thức điện tử … có giá trị pháp lý như đơn thuốc giấy"); Đ13 k3 (BV trước 01/10/2025; cơ sở khác trước 01/01/2026); QĐ 425 Đ11: hình thức 1 — chữ ký số của người chịu trách nhiệm chuyên môn kỹ thuật trên mỗi đơn, người kê dùng chữ ký điện tử; hình thức 2 — người kê dùng chữ ký số cá nhân trên mỗi đơn. TT 55 Đ10 k1–2.
- **Áp dụng**: BV (đã quá hạn 01/10/2025), PK và cơ sở khác (đã quá hạn 01/01/2026) · **Hiệu lực/hạn**: đã qua
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hỗ trợ ít nhất một mô hình ký của QĐ 425 Đ11; chữ ký gắn với bản đơn chuẩn hóa đã gửi; lưu chứng thư, dấu thời gian, kết quả xác thực.
- **Bẫy**: QĐ 425 Đ11 k1 dẫn TT 46/2018 về HSBA điện tử — văn bản này hết HL ngày 06/06/2025, thay bằng TT 13/2025 (C10). Hình thức chữ ký số, dịch vụ tin cậy: xem EMR (NĐ 23/2025). TT 55 Đ10 k2 đoạn 2 cho phòng khám tư YHCT cơ chế lai "ghi trong máy tính 01 lần, sau đó in ra và người hành nghề ký tên".

### DUOC-R12 — Gửi đơn lên Hệ thống đơn thuốc QG đúng thời điểm
- **Căn cứ**: TT 26 Đ12 k6 d (gửi đơn điện tử "ngay sau khi kết thúc quy trình khám bệnh, chữa bệnh" với các trường hợp ở Đ5); TT 55 Đ15 k3 d; QĐ 425 Đ9 k3 a (ngoại trú ngay sau khi kết thúc khám; nội trú trước khi ra viện; đơn gửi gồm đơn BHYT, đơn ngoại trú dịch vụ và bảng tổng hợp thuốc nội trú), Đ10, Đ20 k3 b.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC (đơn ngoại trú, đơn ra viện) · BẮT BUỘC? (bảng tổng hợp thuốc nội trú: QĐ 425 Đ9 k3 a, Đ10 k2 dẫn TT 27/2021 đã hết HL)
- **Phần mềm phải**: tự động gửi khi đóng lượt khám/ký đơn; hàng đợi gửi lại khi lỗi; lưu mã phản hồi, thời điểm gửi, nhận; báo cáo đơn chưa gửi/lỗi; tùy chọn chặn xuất viện khi chưa gửi.
- **Bẫy**: "ngay sau" không có số phút; gửi gom cuối ngày có rủi ro bị coi là vi phạm (suy luận). Chưa thấy điều phạt riêng cho việc không gửi đơn điện tử trong NĐ 90/2026 (§7).

### DUOC-R13 — Kết nối theo chuẩn của Bộ Y tế
- **Căn cứ**: QĐ 425 Đ9 k2 (phần mềm cơ sở KCB kết nối theo QĐ 808/QĐ-BYT), Đ19 k1; TT 26 Đ12 k3 a (Cục KHCN&ĐT ban hành đặc tả, hướng dẫn kết nối), k6 c (hạ tầng CNTT đáp ứng tiêu chí kỹ thuật theo quy định của Bộ trưởng).
- **Áp dụng**: vendor HIS/PK · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC? (QĐ 808 mới đọc qua thứ cấp; chưa thấy đặc tả mới theo TT 26 Đ12 k3 a)
- **Phần mềm phải**: adapter kết nối tách riêng để thay phiên bản đặc tả không sửa lõi; lưu `spec_version` mỗi lần gửi.

### DUOC-R14 — Gửi đơn hoặc mã đơn cho người bệnh qua phương tiện điện tử
- **Căn cứ**: TT 26 Đ12 k6 đ; TT 55 Đ15 k3 đ (kênh cụ thể "theo hướng dẫn của Bộ Y tế", chưa thấy hướng dẫn).
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: giao mã đơn (QR trên bản in, SMS, app, Sổ SKĐT nếu có) và lưu bằng chứng đã gửi; không đưa chẩn đoán vào tin nhắn rõ (NÊN).

### DUOC-R15 — Lưu trữ đơn và bảo đảm trích xuất
- **Căn cứ**: TT 26 Đ11 k1 (cơ sở KCB, pha chế, cấp thuốc, bán lẻ lưu toàn bộ đơn và tài liệu ở Đ7 k3, Đ8 k2, Đ12 k6 b, Đ12 k7 b, dẫn TT 53/2017), Đ11 k2 (hết hạn lưu tài liệu N/H/tiền chất thì Hội đồng hủy theo TT 20/2017), Đ12 k6 e (lưu và "bảo đảm việc trích xuất dữ liệu khi cần thiết"), Đ14 (văn bản viện dẫn bị thay thì áp văn bản mới → TT 33/2025); TT 55 Đ10 k2, k3, Đ11 k2; TT 33/2025 Đ1 k2 a (thời hạn ở Phụ lục áp cho giấy và điện tử), k2 b (loại chưa quy định: tương đương nhóm tương ứng, "không được thấp hơn").
- **Áp dụng**: cơ sở KCB, nhà thuốc · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC (lưu và trích xuất được) · BẮT BUỘC? (con số thời hạn, xem §6 bẫy 1)
- **Phần mềm phải**: lưu bất biến đơn đã ký (kể cả đơn bị thay thế), cam kết PL IV, xác nhận PL V, biên bản PL VI; retention cấu hình theo loại tài liệu, mặc định ≥ 10 năm cho cơ sở KCB (suy luận theo dòng 44 Phụ lục TT 33 "Hồ sơ bệnh án nội trú, ngoại trú: 10 năm"); xuất theo người bệnh, người kê, thời gian, loại N/H/C/T; hủy chỉ qua quy trình có biên bản Hội đồng.
- **Bẫy**: Phụ lục TT 33 không có dòng riêng cho đơn thuốc. Thời hạn lưu HSBA chi tiết: xem EMR-R22.

### DUOC-R16 — Thời hạn hiệu lực của đơn
- **Căn cứ**: TT 26 Đ12 k9 b (lĩnh thuốc trong tối đa 05 ngày kể từ ngày kê); TT 55 Đ11 k1 (05 ngày), Đ15 k5 b (ra viện dùng tiếp 01–07 ngày: lĩnh trong 02 ngày); TT 26 PL II chú thích 10 (đơn N theo đợt); GPP PL I-1a III.2 đ ("không bán đơn thuốc hết hạn").
- **Áp dụng**: cơ sở KCB (hiển thị), nhà thuốc (chặn) · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu `valid_until` (ngày kê + 5; YHCT ra viện + 2; đơn N theo đợt); in trên đơn; nhà thuốc chặn bán khi hết hạn.

### DUOC-R17 — Thuốc YHCT: quy tắc riêng
- **Căn cứ**: TT 55 Đ3 k5 (phần hóa dược trong đơn kết hợp ngoại trú theo TT 26), Đ7 k2, Đ8, Đ9 k2 (thuốc chưa dùng: xác nhận trưởng khoa gửi khoa dược trong 24 giờ), Đ9 k4 (hủy thuốc thang đã sắc: Hội đồng ≥ 03 người), Đ12 k3 (e-Rx YHCT "theo lộ trình của Chính phủ và Bộ Y tế"), Đ15 k3 d–e.
- **Áp dụng**: cơ sở có YHCT · **Hiệu lực/hạn**: 01/03/2026
- **Mức**: BẮT BUỘC (nội dung đơn) · BẮT BUỘC? (mốc e-Rx YHCT chưa có ngày, dù Đ15 k3 d đã yêu cầu gửi đơn điện tử ngoại trú)
- **Phần mềm phải**: tách đơn kết hợp thành các đơn theo mẫu tương ứng; z = T cho đơn thang; danh mục vị thuốc có cờ dược liệu độc (TT 13/2024).

### DUOC-R18 — Nhận lại thuốc gây nghiện, hướng thần, tiền chất
- **Căn cứ**: TT 26 Đ12 k6 b (cơ sở KCB nhận lại thuốc không dùng hết hoặc người bệnh tử vong: biên bản PL VI, 02 bản, biệt trữ và hủy), Đ12 k7 b (bán lẻ theo TT 27/2024); TT 20/2017 Đ7 k2 d bổ sung bởi TT 27/2024 Đ1 k4 (bán lẻ: biên bản nhận lại 02 bản theo PL XX); TT 55 Đ9 k3, Đ15 k3 b.
- **Áp dụng**: cơ sở KCB, nhà thuốc · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phiếu nhận lại gắn đơn gốc và lô; bút toán nhập kho biệt trữ (không bán lại); in biên bản đúng mẫu; theo dõi đến khi hủy.

### DUOC-R19 — Báo cáo thuốc phải kiểm soát đặc biệt
- **Căn cứ**: TT 20/2017 Đ8 k1 a sửa bởi TT 27/2024 Đ1 k5 (cơ sở KCB, trước 15/01 hằng năm: báo cáo XNT, sử dụng thuốc gây nghiện, hướng thần, tiền chất, phóng xạ, dạng phối hợp chứa tiền chất theo PL X, gửi Sở Y tế). NĐ 163 Đ35 k2 a (bán buôn, bán lẻ, chuỗi: báo cáo 06 tháng và năm trước 15/7 và 15/01 theo Mẫu 06, gửi UBND cấp tỉnh nơi đặt trụ sở chính), k2 b (bán lẻ, chuỗi: báo cáo năm về thuốc phóng xạ), k4 (nhầm lẫn, thất thoát: báo cáo UBND cấp tỉnh "trong thời hạn 48 giờ kể từ khi phát hiện" theo Mẫu 07), k5 (không báo cáo: ngừng tiếp nhận hồ sơ đề nghị mua thuốc đến khi báo cáo đủ).
- **Áp dụng**: cơ sở KCB, nhà thuốc · **Hiệu lực/hạn**: định kỳ 15/01, 15/7
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh báo cáo theo mẫu từ sổ cái kho (không nhập tay), kỳ 6 tháng/năm; quy trình sự cố thất thoát có đồng hồ 48 giờ.

### DUOC-R20 — Cấp phát thuốc tại cơ sở KCB phải đối chiếu đơn
- **Căn cứ**: Luật KCB Đ63 k3 (kiểm tra đơn, phiếu lĩnh; đối chiếu tên thuốc, nồng độ, hàm lượng, hạn dùng, số lượng, họ tên người bệnh; nội trú ghi thời gian cấp phát); NĐ 90/2026 Đ41 k1 b, c, d, đ (không kiểm tra, không đối chiếu, không ghi đầy đủ thời gian cấp phát: 1–2 triệu, cá nhân), Đ41 k3 (cấp phát, bán thuốc hết hạn, bảo quản sai, đã thu hồi, không rõ nguồn gốc: 20–30 triệu, cá nhân).
- **Áp dụng**: BV, PK có quầy cấp phát · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: màn hình cấp phát quét mã đơn và mã thuốc/lô; chặn lô hết hạn hoặc bị thu hồi; ghi người cấp, thời gian cấp; nội trú ghi thời điểm cấp từng liều (eMAR, NÊN).
- **Bẫy**: Đ41 NĐ 90 áp cho cơ sở có điều trị nội trú và thời gian lưu theo dõi ngoại trú; mức trong NĐ 90 là mức cá nhân, tổ chức gấp đôi (Đ4 k5).

### DUOC-R21 — Bảo mật dữ liệu đơn thuốc
- **Căn cứ**: QĐ 425 Đ9 k5 (đơn thuốc cho người bệnh HIV/AIDS phải được mã hóa thông tin người bệnh để không hiển thị khi tra cứu), Đ17 ("Thông tin định danh cá nhân của người bệnh phải được mã hóa và áp dụng cơ chế phân quyền"), Đ8 k2 (xuất dữ liệu phải mã hóa dữ liệu định danh, không còn định danh cá nhân), Đ16 k3 (mật khẩu quản trị tài khoản ≥ 8 ký tự gồm hoa, thường, số, ký tự đặc biệt; đổi tối thiểu 06 tháng/lần), Đ20 k4; GPP PL I-1a III.4 a.
- **Áp dụng**: cơ sở KCB, nhà thuốc, vendor · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC? (các điều trên điều chỉnh trực tiếp Hệ thống QG; phần mềm cơ sở chịu căn cứ chung về bảo mật, xem DLCN-R01, DLCN-R12)
- **Phần mềm phải**: cờ đơn HIV/AIDS để gửi theo cơ chế ẩn danh nếu đặc tả hỗ trợ (bảo mật HIV chi tiết: DLCN-R32, BAOMAT-CB-R02); mã hóa trường định danh khi lưu; xuất báo cáo ẩn danh; chính sách mật khẩu tối thiểu như QĐ 425 Đ16 k3 (mức kỹ thuật cao hơn: ANM-R10).

### B. Nhà thuốc, quầy thuốc (phần mềm bán lẻ)

### DUOC-R22 — Chỉ bán thuốc kê đơn khi có đơn; thuốc gây nghiện chỉ theo đơn "N"
- **Căn cứ**: TT 26 Đ12 k7 c, d; TT 55 Đ15 k6 c–d; Luật 44/2024 Đ1 k1 (định nghĩa thuốc không kê đơn); TT 32/2026 Đ15 + PL V (chữ số thứ 5 của số đăng ký: 0 không kê đơn, 1 kê đơn); NĐ 90/2026 Đ59 k4 g ("Bán thuốc kê đơn khi không có đơn thuốc": 10–20 triệu, cá nhân; tổ chức gấp đôi theo Đ4 k5).
- **Áp dụng**: nhà thuốc, quầy thuốc · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi mã hàng có cờ kê đơn/không kê đơn và cờ KSĐB; giao dịch có thuốc kê đơn bắt buộc gắn mã đơn điện tử hoặc thông tin đơn giấy; thuốc N chỉ khi đơn loại N.

### DUOC-R23 — Bán theo đơn điện tử, báo cáo đơn đã bán
- **Căn cứ**: GPP PL I-1a III.2 đ (bổ sung bởi TT 11/2025 Đ1 k8): "Khi bán thuốc kê đơn theo đơn thuốc điện tử, cơ sở phải cập nhật mã đơn thuốc điện tử vào hệ thống bằng dữ liệu đơn thuốc điện tử của Bộ Y tế, đảm bảo liên thông tới hệ thống của Bộ Y tế; bán thuốc đúng theo đơn, số lượng thuốc bán không nhiều hơn số lượng tại đơn thuốc, không bán đơn thuốc hết hạn". QĐ 425 Đ9 k3 b (bán lẻ cập nhật báo cáo đơn đã bán, kể cả thuốc thay thế, ngay sau khi hoàn thiện nghiệp vụ cấp, bán), Đ20 k4 a. QĐ 228/QĐ-QLD: API `GET /api/v1/thong-tin-donthuoc/{ma_don_thuoc}`, API `POST /api/v1/cap-nhat-don-thuoc` (trường `ma_thuoc_da_ke_don`, `ma_thuoc`, `biet_duoc`, `ten_thuoc`, `don_vi_tinh`, `so_luong`, `cach_dung`…), Đ2 (vendor phải nâng cấp phần mềm để nhận đơn điện tử).
- **Áp dụng**: nhà thuốc (PL I-1a); quầy thuốc (PL I-1b không có điểm tương đương) · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC (nhà thuốc) · BẮT BUỘC? (quầy thuốc, suy ra từ TT 26 Đ12 k7 a và QĐ 425 Đ20 k4)
- **Phần mềm phải**: tra đơn bằng mã; số còn được bán = kê − đã bán (cộng dồn qua nhiều lần/nhiều nhà thuốc nếu API trả về); chặn vượt số lượng, đơn hết hạn, đơn đã bị thay thế; gửi báo cáo bán ngay sau thanh toán qua hàng đợi có retry.

### DUOC-R24 — Thay thế thuốc trong đơn
- **Căn cứ**: GPP PL I-1a III.2 c (người có Bằng dược sỹ được thay thuốc đã kê bằng thuốc khác cùng hoạt chất, đường dùng, liều lượng khi người mua đồng ý); QĐ 425 Đ9 k3 b.
- **Áp dụng**: nhà thuốc · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chỉ tài khoản dược sỹ được thay thế; kiểm tra cùng hoạt chất/đường dùng/hàm lượng; ghi đồng ý của người mua; báo cáo đúng `ma_thuoc_da_ke_don` → `ma_thuoc` thực bán.

### DUOC-R25 — Quản lý mua bán bằng phần mềm: xuất nhập tồn, lô, hạn, nguồn gốc
- **Căn cứ**: GPP PL I-1a II.4 b (sổ hoặc máy tính quản lý nhập, xuất, tồn, số lô, hạn dùng, nguồn gốc; người mua, ngày, số lượng với thuốc N/H/tiền chất/dạng phối hợp; thuốc kê đơn thêm người kê và cơ sở); II.4 c sửa bởi TT 11/2025 Đ1 k7 ("Cơ sở phải có thiết bị công nghệ thông tin kết nối internet và thực hiện quản lý hoạt động mua, bán thuốc bằng phần mềm ứng dụng; bảo đảm kiểm soát xuất xứ, giá cả, nguồn gốc thuốc mua vào, bán ra; đảm bảo truy xuất được nguồn gốc thuốc; đảm bảo trích xuất đầy đủ dữ liệu …"); PL II-2a tiêu chí 5.3.2 (*) là điểm không chấp nhận. NĐ 90/2026 Đ59: k1 c (không mở sổ hoặc không dùng máy tính quản lý XNT, lô, hạn, nguồn gốc: 1–3 triệu), k2 d (không quản lý bằng phần mềm, không truy xuất, không trích xuất dữ liệu, hoặc "không liên thông và cập nhật đầy đủ dữ liệu với hệ thống thông tin về dược theo hướng dẫn của Bộ Y tế": 3–5 triệu), k3 g (không có thiết bị, không triển khai CNTT, không kết nối mạng, không kiểm soát xuất xứ, giá, nguồn gốc, trừ bán lẻ dược liệu: 5–10 triệu). Mức cá nhân, tổ chức gấp đôi.
- **Áp dụng**: nhà thuốc, quầy thuốc (PL I-1b II.4 c tương tự); tủ thuốc trạm y tế xã (PL I-1c 3 c) · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sổ cái kho theo lô/hạn; truy vết một lô từ nhà cung cấp tới từng người mua; xuất toàn bộ dữ liệu theo yêu cầu cơ quan quản lý; niêm yết giá và chặn bán cao hơn giá niêm yết (GPP III.2 a; Luật 44 sửa Đ6 k5 i).

### DUOC-R26 — Liên thông Hệ thống cơ sở dữ liệu về dược
- **Căn cứ**: GPP PL I-1a, I-1b II.4 c (như R25); TT 11/2025 Đ5 k2 (liên thông, cập nhật dữ liệu với hệ thống thông tin về dược "thực hiện từ ngày 01 tháng 01 năm 2026"); Luật 44/2024 Đ1 k36 (sửa Đ74 k2 Luật Dược: Bộ trưởng quy định liên thông dữ liệu với hệ thống thông tin về dược); NĐ 90/2026 Đ59 k2 d (chế tài). Hướng dẫn triển khai (thứ cấp): QĐ 1867/QĐ-BYT; QĐ 232/QĐ-TTYQG PL 1 API v1.1 (OAuth 2.0 + Bearer, HTTPS/TLS 1.3; nhóm API danh mục, nhập, xuất, kiểm kho; đồng bộ "theo thời gian thực"); CV 934/TTYQG-DA (dữ liệu phải gồm cả giai đoạn từ 01/01/2026; API hoặc nhập tay; xác thực VNeID khi đăng nhập); CV 3656/QLD-KD (đăng ký tài khoản trước 04/10/2026).
- **Áp dụng**: nhà thuốc, quầy thuốc, bán buôn, chuỗi, vendor · **Hiệu lực/hạn**: 01/01/2026 (dữ liệu tính từ mốc này)
- **Mức**: BẮT BUỘC (nghĩa vụ liên thông) · BẮT BUỘC? (chi tiết API, yêu cầu thời gian thực — nguồn thứ cấp)
- **Phần mềm phải**: map mọi bút toán kho sang loại giao dịch của QĐ 232 (nhập từ NCC, trả lại, tồn đầu, chuyển kho; xuất bán buôn, bán lẻ, chuyển kho, trả lại, thu hồi, hủy; kiểm kho); outbox đồng bộ gần thời gian thực; chức năng **backfill** từ 01/01/2026; `sync_status` từng bút toán; token theo tài khoản từng cơ sở (không dùng chung giữa các nhà thuốc).
- **Bẫy**: Hệ thống CSDL về dược (`csdlduoc.com.vn`, TTYQG) khác Hệ thống đơn thuốc QG (`donthuocquocgia.vn`, Cục QLKCB). Không có nghĩa vụ "liên thông với hệ thống thuế" trong TT 11/2025 hay VBHN GPP (đã tìm). NĐ 163 không chứa nghĩa vụ liên thông này (chỉ Đ31 về sổ/phần mềm KSĐB).

### DUOC-R27 — Lưu hồ sơ, đơn thuốc tại nhà thuốc
- **Căn cứ**: GPP PL I-1a II.4 d ("Hồ sơ hoặc sổ sách phải được lưu trữ ít nhất 1 năm kể từ khi hết hạn dùng của thuốc"); III.2 c (sau khi bán thuốc N, H, tiền chất phải vào sổ, lưu đơn thuốc bản chính); PL II-2a 5.3.2 (lưu đơn bản giấy hoặc điện tử); QĐ 425 Đ20 k4 b (lưu đơn tại thời điểm bán trên phần mềm); TT 26 Đ11 k1; NĐ 90/2026 Đ59 k1 e (không lưu giữ chứng từ, tài liệu liên quan đến lô thuốc trong thời gian phải lưu: 1–3 triệu, cá nhân).
- **Áp dụng**: nhà thuốc, quầy thuốc · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: snapshot nội dung đơn tại thời điểm bán (không chỉ lưu mã); retention = hạn dùng của lô cuối liên quan + ≥ 1 năm; cờ "đã lưu bản chính" cho đơn N/H.

### DUOC-R28 — Thuốc hạn chế bán lẻ
- **Căn cứ**: TT 31/2025 Đ10 + PL III (22 hoạt chất trị sốt rét, lao, HIV; mục 23 thuốc quản lý đặc biệt có yêu cầu hạn chế bán lẻ; chỉ áp khi chỉ định trên đơn trùng cột "Hạn chế bán lẻ đối với các chỉ định được ghi trên đơn thuốc"), Đ10 k3 (Sở Y tế có thể cho phép bán); NĐ 90/2026 Đ59 k4 d (mua, bán thuốc hạn chế bán lẻ khi chưa được phép: 10–20 triệu, cá nhân).
- **Áp dụng**: nhà thuốc · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cờ hạn chế bán lẻ theo hoạt chất + chỉ định; chặn bán khi chỉ định trên đơn trùng danh mục, trừ khi có văn bản cho phép của Sở Y tế (số, ngày, phạm vi).

### DUOC-R29 — Bán thuốc qua thương mại điện tử
- **Căn cứ**: Luật Dược Đ6 (bổ sung bởi Luật 44 Đ1 k3 d: cấm bán lẻ TMĐT thuốc kê đơn trừ cách ly y tế dịch nhóm A, thuốc KSĐB, thuốc hạn chế bán lẻ; cấm kinh doanh qua phương tiện không phải sàn, app, website TMĐT có chức năng đặt hàng), Đ42 k4 (bổ sung bởi Luật 44 Đ1 k18 c); NĐ 163 Đ41 k1–2 (đăng tải Giấy chứng nhận đủ điều kiện kinh doanh dược, CCHN người phụ trách chuyên môn, thông tin thuốc; thông tin thuốc "phải đăng tải trên chuyên mục riêng và không được lẫn thông tin của sản phẩm khác không phải là thuốc"), Đ42 k2 (bao bì giao hàng bán lẻ ghi tên, địa chỉ, số điện thoại khách và số điện thoại người tư vấn); GPP PL I-1a III.2 d (tư vấn trực tuyến; phần mềm ghi nhận liên lạc người mua, tóm tắt tư vấn; lưu bằng chứng ít nhất 24 tháng); NĐ 90/2026 Đ59 k3 m (không tư vấn trực tuyến, không đăng tải đủ thông tin: 5–10 triệu), k4 i, k, l (bán qua TMĐT thuốc KSĐB/hạn chế bán lẻ/kê đơn; bán qua kênh không phải sàn/app/website có đặt hàng; không thông báo trước: 10–20 triệu), mức cá nhân.
- **Áp dụng**: nhà thuốc/chuỗi bán online, nền tảng · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chặn đưa vào giỏ online mã có cờ kê đơn, KSĐB, hạn chế bán lẻ (công tắc riêng cho tình huống dịch nhóm A); bắt buộc hoàn tất tư vấn trước khi chốt đơn; lưu bản ghi tư vấn ≥ 24 tháng; nhãn giao hàng đủ trường; chuyên mục thuốc tách khỏi hàng không phải thuốc. Phân loại app và cấp độ ANM: xem TELE, ANM-R02.

### DUOC-R30 — Theo dõi thuốc kiểm soát đặc biệt bằng sổ hoặc phần mềm
- **Căn cứ**: NĐ 163 Đ31 k8 b (bán lẻ thuốc gây nghiện, hướng thần, tiền chất: "Có hệ thống quản lý, theo dõi bằng hồ sơ sổ sách theo quy định của Bộ trưởng Bộ Y tế"), k9 (dạng phối hợp: "theo dõi bằng hệ thống phần mềm hoặc hồ sơ, sổ sách"), k10 b (bán lẻ thuốc phóng xạ: hồ sơ sổ sách), k13 (thuốc độc, thuốc cấm dùng trong một số ngành: phần mềm hoặc hồ sơ, sổ sách toàn bộ xuất, nhập, tồn); GPP II.4 đ (dẫn NĐ 54/2017, nay áp NĐ 163).
- **Áp dụng**: nhà thuốc kinh doanh thuốc KSĐB · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sổ theo dõi KSĐB riêng theo hoạt chất/lô, in được dạng sổ; khóa sửa xóa; đối chiếu tồn thực tế.
- **Bẫy**: với thuốc N/H/tiền chất đơn chất, NĐ 163 Đ31 k8 b chỉ nói "hồ sơ sổ sách" (không nhắc phần mềm như k9, k13) — phần mềm có thay hoàn toàn sổ được không: §7.

### C. Dữ liệu chủ (master data) thuốc

### DUOC-R31 — Phân loại thuốc theo số đăng ký 12 chữ số
- **Căn cứ**: TT 32/2026 Đ12 k4, PL V: mã nước sản xuất (3, theo GS1 prefix) + nhóm thuốc (1: 1 hóa dược, 2 dược liệu, 3 vắc xin, 4 sinh phẩm, 5 nguyên liệu) + kê đơn (1: 0 không, 1 có) + KSĐB (1: 0 không, 1 gây nghiện, 2 hướng thần, 3 tiền chất, 4 độc, 5 cấm dùng cho các bộ ngành, 6 phóng xạ) + số thứ tự (4) + năm cấp (2); Đ52 k4 (thuốc cấp trước 01/01/2023 đổi sang cấu trúc mới chậm nhất 12 tháng sau gia hạn), k5.
- **Áp dụng**: vendor, nhà thuốc, khoa dược · **Hiệu lực/hạn**: 01/10/2026
- **Mức**: NÊN (dùng để đề xuất cờ; dữ liệu gốc vẫn đối chiếu công bố của Cục QLD)
- **Phần mềm phải**: parse SĐK 12 số để gợi ý cờ kê đơn/KSĐB, ưu tiên dữ liệu công bố; hỗ trợ đồng thời số đăng ký kiểu cũ.
- **Bẫy**: PL V ghi chú các giá trị "có thể phát sinh" — không hard-code enum đóng.

### DUOC-R32 — Cờ danh mục đặc biệt khi kê
- **Căn cứ**: TT 26 Đ3, Đ6 k6–7, Đ7–9; TT 55 Đ8 k5 đ; NĐ 163 Đ29 (gốc-OCR).
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục nội bộ có cờ: gây nghiện, hướng thần, tiền chất, phối hợp chứa GN/HT/TC, độc, phóng xạ, dược liệu độc, hạn chế bán lẻ, OTC; mỗi cờ điều khiển loại đơn, giới hạn ngày, cách ghi số lượng, kênh bán.
- **Bẫy**: TT 26 không có điều riêng về kê đơn thuốc phóng xạ; thuốc phóng xạ chủ yếu ở NĐ 163 (Đ31 k10, Đ35) và TT 20/2017 sửa bởi TT 27/2024.

### D. Thực hành tốt

### DUOC-R33 — Nhật ký truy vết vòng đời đơn
- **Căn cứ**: không có điều luật trực tiếp cho phần mềm cơ sở; QĐ 425 Đ9 k1 a chỉ áp cho tài khoản quản trị trên Hệ thống QG (cập nhật phải "được ghi nhật ký trên hệ thống để có thể theo dõi, giám sát và truy cứu trách nhiệm").
- **Áp dụng**: cơ sở KCB, nhà thuốc · **Hiệu lực/hạn**: —
- **Mức**: NÊN
- **Phần mềm phải**: log bất biến cho tạo, ký, gửi, thay thế, hủy, xem đơn (ai, khi nào, từ đâu); giữ log bằng thời hạn lưu đơn (cùng nguyên tắc BAOMAT-CB-R22; khung log an ninh: ANM-R11).

### DUOC-R34 — Cảnh báo liều, tương tác, dị ứng
- **Căn cứ**: TT 26 Đ4 k1 (kê đơn phù hợp tờ HDSD, hướng dẫn chẩn đoán điều trị, Dược thư); NĐ 90/2026 Đ41 k2 c (kê không phù hợp tờ HDSD, HDCĐĐT, Dược thư quốc gia: 10–20 triệu, cá nhân; phạm vi Đ41 như R20).
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: —
- **Mức**: NÊN (nghĩa vụ phù hợp là của người kê; phần mềm là công cụ hỗ trợ)
- **Phần mềm phải**: CDSS cảnh báo liều tối đa, tương tác, chống chỉ định; trẻ < 72 tháng tính liều theo cân nặng bắt buộc. AI/CDSS: xem TELE.

**Tổng hợp mức** (theo mức chính): BẮT BUỘC 29 (R01–R12, R14–R20, R22–R30, R32) · BẮT BUỘC? 2 (R13, R21) · NÊN 3 (R31, R33, R34). R12, R15, R17, R23, R26 có phần phụ BẮT BUỘC?.

## 3. Pattern thiết kế

### DUOC-P01 — Đơn thuốc bất biến có chuỗi thay thế
- **Giải quyết**: R09, R11, R12, R15
- **Cách làm**: sau trạng thái `signed`, chặn UPDATE cột nội dung (trigger/policy); sửa = INSERT bản mới có `replaces_id`, bản cũ chuyển `superseded`.
- **Gợi ý dữ liệu**: `prescription(id, rx_code UNIQUE, facility_code, prescriber_id, patient_id, encounter_id, type CHECK IN ('C','N','H','T'), status CHECK IN ('draft','signed','sent','superseded','cancelled'), replaces_id FK NULL, issued_at, valid_until, payload_canonical JSONB, payload_hash, signature_blob, signed_at, sent_at, national_ack_id, ruleset_version)`; `prescription_item(...)`.
- **Đánh đổi**: nhiều bản ghi hơn; đổi lại có bằng chứng pháp lý, khớp QĐ 425 Đ9 k3 c.

### DUOC-P02 — Bộ sinh mã đơn
- **Giải quyết**: R04
- **Cách làm**: `rx_code = facility5 + random7([0-9a-z], CSPRNG) + '-' + type`; retry khi trùng; không dùng sequence (vi phạm "giá trị ngẫu nhiên", lộ lưu lượng).
- **Gợi ý dữ liệu**: `UNIQUE(facility_code, substring(rx_code,6,7))`; regex `^[0-9A-Za-z]{5}[0-9a-z]{7}-[NHCT]$` (bộ ký tự 5 ký tự đầu cần xác nhận theo QĐ 384).
- **Đánh đổi**: cần retry khi va chạm (xác suất rất thấp).

### DUOC-P03 — Rule engine kê đơn theo dữ liệu chủ có phiên bản
- **Giải quyết**: R05, R06, R07, R16, R17, R32
- **Cách làm**: hàm `max_days(drug, icd10, acute)` trả 7/10/30/90 (+ quy tắc YHCT); validate khi ký; lưu `ruleset_version` vào đơn.
- **Gợi ý dữ liệu**: `drug_master(inn, brand, ingredient_count, rx_flag, control_class, is_poison, is_radioactive, herbal_toxic, restricted_retail, reg_no, reg_no_parsed, valid_from, valid_to)`; `long_term_icd10(code, source='TT26-PLVII', version)`.
- **Đánh đổi**: phải cập nhật master data khi văn bản đổi.

### DUOC-P04 — Outbox gửi Hệ thống đơn thuốc QG
- **Giải quyết**: R12, R13, R14
- **Cách làm**: event `encounter.closed` / `discharge.requested` ghi outbox trong cùng transaction; worker gửi ngay sau commit, backoff có trần; dashboard "đơn chưa gửi > N phút"; xuất viện chờ ack (cấu hình).
- **Gợi ý dữ liệu**: `outbox(id, aggregate, aggregate_id, endpoint, spec_version, payload, attempt, next_retry_at, status, last_error, created_at)`.
- **Đánh đổi**: thêm hạ tầng hàng đợi; đổi lại không mất đơn khi mạng hoặc hệ thống QG lỗi.

### DUOC-P05 — Workflow thuốc kiểm soát đặc biệt
- **Giải quyết**: R07, R08, R18, R19, R30
- **Cách làm**: in 03 bản có watermark "Bản lưu cơ sở KCB / Bản lưu HSBA / Bản giao nơi bán"; một xác nhận PL V cho một đơn.
- **Gợi ý dữ liệu**: `narcotic_commitment(patient_id, form='PL-IV', signed_at, file_ref)`, `commune_confirmation(id, prescription_id UNIQUE, form='PL-V')`, `sample_signature(prescriber_id, image_ref, valid_from)`, `controlled_return(id, rx_id, lot_id, qty, form IN ('PL-VI','PL-XX'), quarantine_location)`.
- **Đánh đổi**: quy trình dài hơn ở quầy.

### DUOC-P06 — Bán lẻ theo đơn điện tử
- **Giải quyết**: R16, R22, R23, R24, R27
- **Cách làm**: lấy đơn qua API QĐ 228, snapshot; ràng buộc tổng `qty` theo `prescribed_drug_code` ≤ số lượng kê; outbox gửi `cap-nhat-don-thuoc` ngay sau thanh toán.
- **Gợi ý dữ liệu**: `erx_snapshot(rx_code PK, fetched_at, payload JSONB, valid_until, status)`; `dispense(id, rx_code FK, pharmacist_id, substituted BOOL, consent_ref)`; `dispense_line(prescribed_drug_code, dispensed_drug_code, lot_id, qty)`.
- **Đánh đổi**: phụ thuộc tính sẵn sàng của API QG; cần chế độ ngoại tuyến có kiểm soát.

### DUOC-P07 — Sổ cái kho theo lô, đồng bộ CSDL dược
- **Giải quyết**: R19, R25, R26, R30
- **Cách làm**: append-only; tồn = SUM; `movement_type` ánh xạ 1-1 sang loại giao dịch QĐ 232; job backfill từ 01/01/2026; báo cáo KSĐB (Mẫu 06 NĐ 163, PL X TT 27/2024) sinh từ sổ cái.
- **Gợi ý dữ liệu**: `stock_movement(id, ts, facility_id, drug_id, lot_no, expiry_date, qty_signed, movement_type, counterparty_id, source_doc, price, gtin)`; `national_sync(movement_id, status, sent_at, remote_id)`.
- **Đánh đổi**: append-only khó "sửa nhầm"; dùng bút toán đảo có lý do.

### DUOC-P08 — Lưu trữ và hủy có kiểm soát
- **Giải quyết**: R15, R27
- **Cách làm**: file ký số và PDF đơn trên kho WORM/khóa đối tượng; xóa chỉ qua lô hủy có quyết định Hội đồng.
- **Gợi ý dữ liệu**: `retention_policy(doc_type, min_years, anchor CHECK IN ('issued_at','lot_expiry','last_encounter'))`; `legal_hold`; `destruction_batch(id, council_decision_ref, members, minutes_file, executed_at)`.
- **Đánh đổi**: chi phí lưu trữ dài hạn.

### DUOC-P09 — Kênh giao mã đơn cho người bệnh
- **Giải quyết**: R14, R21
- **Cách làm**: bản in có QR chứa `rx_code`; SMS/app chỉ gửi mã và link tra cứu, không gửi chẩn đoán.
- **Gợi ý dữ liệu**: `delivery_log(rx_code, channel, sent_at, status)`.
- **Đánh đổi**: chi phí SMS.

### DUOC-P10 — Nhật ký tư vấn TMĐT
- **Giải quyết**: R29
- **Cách làm**: đơn hàng online không chuyển "confirmed" nếu thiếu bản ghi tư vấn.
- **Gợi ý dữ liệu**: `online_consult(order_id, buyer_contact, channel, summary, media_ref, pharmacist_id, created_at)`; retention 24 tháng.
- **Đánh đổi**: tăng thời gian chốt đơn.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| DUOC-A01 | R01 | Đăng nhập điều dưỡng/dược sĩ thử tạo, ký đơn; y sĩ YHCT thử kê hóa dược | Ảnh màn hình bị chặn; cấu hình quyền | BẮT BUỘC |
| DUOC-A02 | R02 | Mỗi người kê có đúng 1 mã liên thông; mở 10 đơn đã gửi xem có mã | Kết quả SQL; payload | BẮT BUỘC |
| DUOC-A03 | R03 | Tạo đơn trẻ 3 tuổi bỏ trống cân nặng; so bản in với PL I/II/III TT 26 | Thông báo lỗi; bản in | BẮT BUỘC |
| DUOC-A04 | R04 | `SELECT rx_code … WHERE rx_code !~ '^.{5}[0-9a-z]{7}-[NHCT]$' OR length(rx_code)<>14`; kiểm phần y có tăng dần | Kết quả truy vấn; mẫu 100 mã | BẮT BUỘC |
| DUOC-A05 | R05 | Kê 1 thuốc độc + 2 thuốc thường, số lượng 5, 1 thuốc N | Bản in: độc đứng đầu, "05", số bằng chữ cho N | BẮT BUỘC |
| DUOC-A06 | R03, R05 | Thêm thực phẩm chức năng vào đơn | Bị chặn | BẮT BUỘC |
| DUOC-A07 | R06 | Kê 60 ngày với ICD ngoài PL VII; N cấp tính 10 ngày; H cấp tính 15 ngày | Bị chặn/cảnh báo cứng | BẮT BUỘC |
| DUOC-A08 | R07 | Cơ sở không giường thử tạo đơn N; đơn lẫn N và C | Bị chặn hoặc tự tách | BẮT BUỘC |
| DUOC-A09 | R08 | Đơn N không có cam kết PL IV; một PL V cho 2 đơn | Bị chặn | BẮT BUỘC |
| DUOC-A10 | R09 | Sửa đơn đã gửi; kiểm DB có UPDATE nội dung không | Đơn mới mã mới + liên kết; đơn cũ "superseded" | BẮT BUỘC |
| DUOC-A11 | R10 | So y lệnh HSBA với đơn cùng lượt trên 20 hồ sơ | Bảng đối chiếu | BẮT BUỘC |
| DUOC-A12 | R11 | Xác thực chữ ký trên file đơn; chứng thư thuộc người kê hoặc người chịu trách nhiệm chuyên môn | Kết quả verify | BẮT BUỘC |
| DUOC-A13 | R12 | Phân vị `sent_at - encounter_closed_at`; đếm đơn chưa gửi; luồng ra viện | Thống kê độ trễ; danh sách lỗi | BẮT BUỘC |
| DUOC-A14 | R13 | Tài liệu tích hợp: phiên bản đặc tả (QĐ 808 hoặc mới hơn) | Tài liệu, log | BẮT BUỘC? |
| DUOC-A15 | R14 | Quy trình giao mã đơn; log gửi SMS/app | delivery_log | BẮT BUỘC |
| DUOC-A16 | R15 | Cấu hình retention; thử xóa đơn cũ qua UI và API; xuất đơn theo người bệnh/khoảng thời gian | Cấu hình; xóa bị chặn; file xuất | BẮT BUỘC |
| DUOC-A17 | R16 | Nhà thuốc quét đơn kê 6 ngày trước | Bị chặn | BẮT BUỘC |
| DUOC-A18 | R17 | Đơn thang có vị < 10 g, vị từ dược liệu độc, vượt liều | "08 g", số + chữ, "tôi kê liều này", mã đuôi T | BẮT BUỘC |
| DUOC-A19 | R18 | Phiếu nhận lại thuốc N; tồn có cộng vào kho bán không | Biên bản PL VI/PL XX; kho biệt trữ | BẮT BUỘC |
| DUOC-A20 | R19 | Sinh báo cáo KSĐB kỳ gần nhất, đối chiếu sổ cái | Báo cáo + truy vấn đối chiếu | BẮT BUỘC |
| DUOC-A21 | R20 | Cấp phát lô hết hạn hoặc bị thu hồi | Bị chặn; log người cấp, thời gian | BẮT BUỘC |
| DUOC-A22 | R21 | Mã hóa trường CCCD/BHYT ở DB; cờ ẩn danh đơn HIV; chính sách mật khẩu | Schema, cấu hình | BẮT BUỘC? |
| DUOC-A23 | R22 | Bán thuốc kê đơn không có mã đơn; bán thuốc N với đơn C | Bị chặn | BẮT BUỘC |
| DUOC-A24 | R23 | Bán vượt số lượng; bán đơn đã bị thay thế; log API cập nhật bán | Bị chặn; log API | BẮT BUỘC |
| DUOC-A25 | R24 | Nhân viên không phải dược sỹ thử thay thuốc | Bị chặn; bản ghi đồng ý | BẮT BUỘC |
| DUOC-A26 | R25 | Truy 1 lô từ hóa đơn nhập tới từng giao dịch bán; xuất toàn bộ XNT | Báo cáo truy vết; file xuất | BẮT BUỘC |
| DUOC-A27 | R26 | Tài khoản CSDL dược của cơ sở; tỷ lệ bút toán đã đồng bộ từ 01/01/2026; có backfill | Ảnh tài khoản; thống kê sync | BẮT BUỘC |
| DUOC-A28 | R27 | Đơn N/H đã bán có bản chính/ảnh; retention ≥ 1 năm sau hạn dùng | Mẫu hồ sơ; cấu hình | BẮT BUỘC |
| DUOC-A29 | R28 | Bán isoniazid với chỉ định "điều trị lao" trên đơn | Bị chặn (trừ văn bản Sở Y tế) | BẮT BUỘC |
| DUOC-A30 | R29 | Thêm thuốc kê đơn vào giỏ online; chốt đơn không có tư vấn; tìm bản ghi tư vấn 20 tháng trước | Bị chặn; bản ghi tư vấn | BẮT BUỘC |
| DUOC-A31 | R30 | In sổ KSĐB; thử xóa một dòng | Sổ in; bị chặn | BẮT BUỘC |
| DUOC-A32 | R31, R32 | Tỷ lệ mã có cờ kê đơn/KSĐB; parse SĐK 12 số | Thống kê master data | NÊN (R31) / BẮT BUỘC (R32) |
| DUOC-A33 | R33 | Log vòng đời 5 đơn | Log | NÊN |
| DUOC-A34 | R34 | Kê liều vượt tối đa theo cân nặng | Cảnh báo | NÊN |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 01/04/2022 | QĐ 808/QĐ-BYT hướng dẫn kết nối Hệ thống đơn thuốc QG | Vendor HIS/PK | Đã qua |
| 03/04/2023 | QĐ 228/QĐ-QLD chuẩn kết nối nhà thuốc ↔ đơn thuốc QG | Vendor nhà thuốc | Đã qua |
| 30/01/2025 | TT 27/2024 sửa TT 20/2017 có HL (thứ cấp) | Cơ sở KCB, nhà thuốc | Đã qua |
| 05/02/2025 | QĐ 425 Quy chế Hệ thống đơn thuốc QG | Cơ sở KCB, nhà thuốc | Đã qua |
| 01/07/2025 | TT 26, NĐ 163, TT 31, TT 11/2025, Luật 44 có HL | Tất cả | Đã qua |
| trước 01/10/2025 | Bệnh viện kê đơn điện tử | BV công, BV tư | Đã qua (hạn chót) |
| trước 01/01/2026 | Cơ sở KCB khác kê đơn điện tử | PK, cơ sở khác | Đã qua (hạn chót) |
| 01/01/2026 | Nhà thuốc, quầy, bán buôn liên thông hệ thống thông tin về dược; dữ liệu tính từ mốc này | Nhà thuốc, quầy, bán buôn | Đã qua |
| 01/03/2026 | TT 55 (YHCT) có HL; e-Rx YHCT theo lộ trình chưa định ngày | Cơ sở YHCT | Đã qua |
| 15/05/2026 | NĐ 90/2026 (xử phạt) có HL | Tất cả | Đã qua |
| 30/06/2026 | Hết dùng mẫu đơn thuốc thang in theo TT 44/2018 | Cơ sở YHCT | Đã qua |
| 17/07/2026 | Đặc tả API CSDL dược v1.1 (QĐ 232, thứ cấp) | Vendor | Đã qua |
| 12/08/2026 | CV 934: kết nối, xác thực VNeID, dữ liệu hồi tố từ 01/01/2026 (thứ cấp) | Bán buôn, bán lẻ | Đã qua |
| 19/08/2026 | QĐ 2656 bãi bỏ điểm đ k1 Đ5 TT 02/2018 | Nhà thuốc (thủ tục) | Đã qua |
| 01/10/2026 | TT 32/2026 có HL (SĐK 12 số, tiêu chí OTC); TT 12/2025 hết HL | Vendor master data, nhà thuốc | Đã qua (5 ngày) |
| 04/10/2026 | Hạn đăng ký tài khoản CSDL dược (CV 3656, thứ cấp; đối tượng chưa chốt) | Xem §7 | Đã qua (2 ngày) |
| trước 15/01/2027 | Báo cáo năm 2026 XNT thuốc KSĐB (cơ sở KCB → Sở Y tế; nhà thuốc, chuỗi → UBND cấp tỉnh) | Cơ sở KCB, nhà thuốc | Sắp tới |
| 01/07/2027 | BYT triển khai phần mềm quản lý trực tuyến XNK thuốc; đổi nơi tiếp nhận báo cáo XNK (gốc-OCR) | Cơ sở SX, XNK | Sắp tới |
| trước 15/07/2027 | Báo cáo 6 tháng đầu năm 2027 thuốc KSĐB | Nhà thuốc, bán buôn, chuỗi | Sắp tới |
| Thường xuyên | Gửi đơn ngay sau khám (ngoại trú), trước ra viện (nội trú); nhà thuốc báo cáo đơn đã bán ngay sau bán; báo cáo nhầm lẫn, thất thoát KSĐB trong 48 giờ | Cơ sở KCB, nhà thuốc | — |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**

| Cũ | Mới | Từ ngày | Ghi chú |
|---|---|---|---|
| TT 52/2017, 18/2018, 04/2022, 27/2021 | TT 26/2025 | 01/07/2025 | TT 26 Đ13 k2 |
| TT 44/2018 (YHCT) | TT 55/2025 | 01/03/2026 | Mẫu cũ đã in dùng đến 30/06/2026 |
| TT 53/2017 (thời hạn bảo quản) | TT 33/2025 | 01/07/2025 | TT 26 Đ11 vẫn dẫn TT 53; áp TT 33 theo TT 26 Đ14 |
| NĐ 54/2017, NĐ 88/2023 | NĐ 163/2025 | 01/07/2025 | GPP II.4 đ vẫn dẫn "Điều 43 NĐ 54" → đọc NĐ 163 |
| TT 07/2018 | TT 31/2025 | 01/07/2025 | TT 31 Đ25 k2 |
| TT 12/2025 (đăng ký thuốc) | TT 32/2026 | 01/10/2026 | TT 32 Đ52 k2 a |
| NĐ 117/2020 | NĐ 90/2026 | 15/05/2026 | |
| QĐ 540/QĐ-QLD (Bảng 3), QĐ 777/QĐ-QLD (mục 2–4, 5.2) | QĐ 228/QĐ-QLD | 03/04/2023 | Chuẩn kết nối nhà thuốc |
| QĐ 330/QĐ-QLD (2019) | QĐ 318/QĐ-QLD | 04/06/2021 | Chuẩn kết nối cơ sở phân phối |
| Điểm đ k1 Đ5 TT 02/2018 | bãi bỏ (QĐ 2656) | 19/08/2026 | Chỉ là bản tự kiểm tra GPP trong hồ sơ; không liên quan yêu cầu phần mềm |

**Bẫy trích dẫn**

1. **Thời hạn lưu đơn thuốc**: TT 26 Đ11 k1 dẫn TT 53/2017 đã hết HL → áp TT 33/2025. TT 55 Đ11 k2 dẫn "điểm a khoản 2 Điều 1 TT 33", nhưng điểm này chỉ nói Phụ lục áp cho giấy và điện tử, không nêu số năm. Phụ lục TT 33 không có dòng "đơn thuốc". Kết luận làm việc (suy luận, cần BYT xác nhận): (a) đơn gắn HSBA theo dòng 44: 10 năm (hoặc theo dòng HSBA đặc thù: tử vong, tâm thần…, xem EMR-R22); (b) đơn ngoại trú không có HSBA: tối thiểu dòng 47 "sổ, sách phục vụ công tác KCB" 05 năm, khuyến nghị 10 năm; (c) nhà thuốc: ≥ 1 năm kể từ khi thuốc hết hạn dùng (GPP II.4 d); bằng chứng tư vấn TMĐT ≥ 24 tháng.
2. **Ngày QĐ 808/QĐ-BYT**: luatvietnam và QĐ 228 ghi 01/04/2022; QĐ 425 Đ9 k2 ghi "ngày 01/4/2023" (đã kiểm lại bằng OCR tiếng Việt). Hai nguồn độc lập cho 2022 → QĐ 425 nhiều khả năng ghi nhầm năm. ID đúng: QD-808-2022-BYT.
3. **QĐ 425 dẫn văn bản đã hết HL**: TT 05/2016 (Đ3 k1), TT 27/2021, TT 04/2022 (→ TT 26/2025), TT 46/2018 (→ TT 13/2025, hết HL 06/06/2025, C10), NĐ 13/2023 (→ Luật 91/2025 + NĐ 356/2025), NĐ 85/2016 (hết HL từ 01/07/2026 cùng Luật ATTT mạng theo Luật 64/2025 Đ57 k2 sửa bởi Luật 87/2025; khung mới NĐ 331/2026, xem ANM-R05, C07). Khi trích QĐ 425 phải ghi văn bản thay thế.
4. **"14 ký tự" đã gồm dấu "-"** (5+7+1+1). Nhiều tài liệu vendor hiểu nhầm thành 14 ký tự + dấu gạch.
5. **Ký tự loại đơn TT 55**: PL II (cổ truyền, dược liệu) không có ký tự riêng; không tự chế.
6. **Phạm vi TT 26 là ngoại trú** (kể cả đơn ra viện, Đ5 k2). Kê thuốc nội trú theo TT 23/2011 (TT 55 Đ3 k6). Nghĩa vụ gửi bảng tổng hợp thuốc nội trú chỉ có ở QĐ 425 Đ9 k3 a, Đ10 k2 (dẫn TT 27/2021 đã hết HL).
7. **Phòng khám không giường bệnh không dùng đơn "N"** (TT 26 Đ7 k1); giảm đau gây nghiện cho người bệnh ung thư tại nhà do bác sỹ cơ sở có giường nội trú kê (Đ8 k2 a).
8. **Nghĩa vụ liên thông của nhà thuốc** nằm ở VBQPPL: GPP PL I-1a/1b II.4 c (sửa bởi TT 11/2025 Đ1 k7) + TT 11/2025 Đ5 k2 (mốc 01/01/2026) + Luật Dược Đ74 k2 (sửa bởi Luật 44). CV 934, CV 3656, QĐ 1867, QĐ 232 chỉ là hướng dẫn triển khai. Không có "liên thông với hệ thống thuế" trong TT 11/2025.
9. **NĐ 90/2026 Đ59 k2 là điểm d** (đã đối chiếu ảnh bản ký số, không phải "đ"). Mức 3–5 triệu là mức cá nhân; tổ chức gấp 02 lần (Đ4 k5: "Đối với cùng một hành vi vi phạm hành chính thì mức phạt tiền đối với tổ chức bằng 02 lần mức phạt tiền đối với cá nhân."). Câu chữ điểm d gần như sao nguyên GPP II.4 c.
10. **NĐ 90/2026 Đ41** có tiêu đề giới hạn ở "cơ sở khám bệnh, chữa bệnh có thực hiện điều trị nội trú và trong thời gian lưu người bệnh ngoại trú để theo dõi". Đừng trích Đ41 làm chế tài chung cho mọi phòng khám ngoại trú.
11. **CV 3656/QLD-KD**: theo tóm tắt thứ cấp, đối tượng chính là cơ sở SX, XNK, dịch vụ bảo quản; tài khoản bán buôn/bán lẻ do Sở Y tế phê duyệt. Đừng viết "mọi nhà thuốc phải đăng ký trước 04/10/2026" khi chưa có bản gốc.
12. **TT 32/2026 thay TT 12/2025 từ 01/10/2026**: tài liệu nói "TT 12/2025 quy định số đăng ký/OTC" đã lỗi thời.
13. **Mẫu tóm tắt bệnh án** TT 26 Đ8 k2 dẫn PL XXIX TT 32/2023 → dùng Mẫu 03 PL II TT 25/2025 (C01, GIAYTO).

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. **Thời hạn lưu đơn thuốc tại cơ sở KCB**: không có con số trực tiếp (§6 bẫy 1). Hỏi Văn phòng BYT hoặc Cục QLKCB; tìm nội dung TT 53/2017 cũ.
2. **Đặc tả kết nối Hệ thống đơn thuốc QG hiện hành**: QĐ 808/2022 chỉ đọc qua thứ cấp; chưa thấy văn bản của Cục KHCN&ĐT theo TT 26 Đ12 k3 a; chưa thấy "tiêu chí kỹ thuật hạ tầng CNTT" theo Đ12 k6 c.
3. **Quan hệ giữa chuẩn Cục QLD (540, 777/2018; 318/2021; 228/2023) và QĐ 232/QĐ-TTYQG (2026)**: song song hay thay thế; cần bản gốc QĐ 1867, QĐ 232, CV 934, CV 3656.
4. **Mốc bắt buộc e-Rx YHCT** (TT 55 Đ12 k3) và ký tự loại đơn cổ truyền/dược liệu: hỏi Cục Quản lý Y, Dược cổ truyền.
5. **Đơn "N"/"H" điện tử có thay được bản giấy có dấu không** (TT 26 Đ7 k1, Đ9 k1 vs Đ10); sổ theo dõi thuốc N/H/tiền chất tại nhà thuốc có thay hoàn toàn bằng phần mềm được không (NĐ 163 Đ31 k8 b chỉ nói "hồ sơ sổ sách").
6. **TT 20/2017 (gốc)**: chưa đọc; thời hạn lưu chứng từ thuốc KSĐB, thủ tục Hội đồng hủy tài liệu; tình trạng HL sau khi NĐ 54 hết HL.
7. **Chế tài khi không gửi đơn điện tử**: chưa thấy điều riêng trong NĐ 90/2026 (đã rà tiêu đề Đ35–Đ73); có thể rơi vào điều khoản chung về chuyên môn hoặc Đ39 k2 d. Chế tài kê đơn sai ở phòng khám ngoại trú không giường (ngoài phạm vi Đ41) cũng chưa xác định — hỏi luật sư.
8. **Quầy thuốc và e-Rx**: PL I-1b GPP không có điểm tương ứng III.2 đ; nghĩa vụ báo cáo đơn đã bán chỉ suy ra từ TT 26 Đ12 k7 và QĐ 425 Đ20 k4.
9. **Kho thuốc tại cơ sở KCB** (TT 22/2011, TT 23/2011): chưa đọc. Cơ sở KCB có thuộc đối tượng liên thông CSDL dược không: theo tóm tắt QĐ 1867 thì không (chỉ XNK, bán buôn, bán lẻ, chuỗi) — cần bản gốc.
10. **Ngày HL TT 27/2024** (30/01/2025) và **danh mục thuốc không kê đơn hiện hành**: mới có nguồn thứ cấp.
11. **QĐ 3176/QĐ-BYT và QĐ 384/QĐ-BYT**: quy tắc mã người kê và mã cơ sở (bộ ký tự 5 ký tự đầu mã đơn), mới thấy qua dẫn chiếu trong QĐ 425.
12. **NĐ 163 Đ124, Đ130 k3** (mốc 01/07/2027 cho XNK) chưa đối chiếu bản có dấu — chỉ diễn giải. Link bản ký số QĐ 228 (cổng SYT Huế) hiện không mở được; đang dẫn trang thứ cấp.
