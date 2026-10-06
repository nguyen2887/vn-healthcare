# DUOC — Kê đơn điện tử, dược và nhà thuốc (cụm K3)
> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: kê đơn thuốc ngoại trú (hóa dược, sinh phẩm, cổ truyền, dược liệu), đơn thuốc điện tử và mã đơn, ký số, liên thông Hệ thống đơn thuốc quốc gia (donthuocquocgia.vn), thuốc phải kiểm soát đặc biệt (gây nghiện "N", hướng thần/tiền chất "H", phóng xạ, thuốc độc), lưu trữ đơn, phần mềm nhà thuốc GPP (bán theo đơn, xuất nhập tồn, truy xuất lô/hạn), liên thông Hệ thống cơ sở dữ liệu về dược (csdlduoc.com.vn), bán thuốc qua thương mại điện tử, cấp phát thuốc tại cơ sở KCB.
>
> Phương pháp: đọc bản gốc có lớp text (datafiles.chinhphu.vn) cho TT 26/2025, TT 55/2025, TT 33/2025 (+ phụ lục), Luật 44/2024, QĐ 2656/QĐ-BYT, VBHN 11/VBHN-BYT (TT 02/2018 hợp nhất đến TT 11/2025), TT 27/2024, TT 31/2025, VBHN Luật KCB. Bản scan (NĐ 163/2025, NĐ 90/2026, QĐ 425/QĐ-BYT) được OCR bằng tesseract `eng` nên **mất dấu**: ghi "gốc-OCR", câu chữ trích dẫn trong file này là phục dựng dấu, số/điều/khoản tin được. Văn bản chỉ đọc qua luatvietnam/báo ghi "thứ cấp". Không dùng hethongphapluat. Đây là tài liệu nghiên cứu, **không phải ý kiến pháp lý**.

---

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| TT-26-2025-BYT | 26/2025/TT-BYT (30/06/2025) | Đơn thuốc và kê đơn thuốc hóa dược, sinh phẩm trong điều trị ngoại trú tại cơ sở KCB | 01/07/2025; e-Rx: BV trước 01/10/2025, cơ sở khác trước 01/01/2026 (Đ13 k3) | Còn HL; thay TT 52/2017, 18/2018, 04/2022, 27/2021 (Đ13 k2) | BV công, BV tư, PK, nhà thuốc, vendor HIS/PK/nhà thuốc | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf) |
| TT-55-2025-BYT | 55/2025/TT-BYT (31/12/2025) | Kê đơn thuốc cổ truyền, thuốc dược liệu và kê đơn kết hợp với thuốc hóa dược | 01/03/2026 | Còn HL; thay TT 44/2018 (Đ12 k2); mẫu đơn thang cũ đã in dùng đến 30/06/2026 (Đ14) | Cơ sở KCB có YHCT (nội trú, ban ngày, ngoại trú), nhà thuốc, vendor | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/55-byt.pdf) |
| TT-33-2025-BYT | 33/2025/TT-BYT (01/07/2025) | Thời hạn lưu trữ hồ sơ, tài liệu ngành y tế | 01/07/2025 | Còn HL; thay TT 53/2017 | Mọi cơ sở (giấy + điện tử, Đ1 k2a) | gốc | [PDF thân](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [PDF phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| L-DUOC-SD-2024 | 44/2024/QH15 (21/11/2024) | Luật sửa đổi, bổ sung một số điều của Luật Dược | 01/07/2025 (một số điểm 01/01/2025, Đ3 k2) | Còn HL | Nhà thuốc, chuỗi, TMĐT, vendor | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat44.pdf) |
| L-DUOC-2016 | 105/2016/QH13 | Luật Dược (gốc) | — | Còn HL, sửa bởi 28/2018/QH14 và 44/2024/QH15 | Tất cả | gốc-meta (qua căn cứ của TT 55, QĐ 2656) | — |
| L-KCB-2023 | 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB, Đ62–63 (kê đơn, sử dụng thuốc) | 01/01/2024 | Còn HL | Cơ sở KCB | gốc (VBHN) | [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| ND-163-2025 | 163/2025/NĐ-CP (29/06/2025) | Quy định chi tiết Luật Dược (Đ30–36 thuốc KSĐB; Đ41–42 TMĐT; Đ124 lộ trình báo cáo) | 01/07/2025 (Đ129 k1) | Còn HL; thay NĐ 54/2017, NĐ 88/2023 (Đ129 k2) | Nhà thuốc, cơ sở KCB dùng thuốc KSĐB, bán buôn | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/163nd.signed.pdf) |
| TT-02-2018-BYT (VBHN) | 02/2018/TT-BYT, hợp nhất tại 11/VBHN-BYT (2025) | Thực hành tốt cơ sở bán lẻ thuốc (GPP), đã sửa bởi 12/2020, 29/2020, 11/2025 | 08/03/2018; phần sửa bởi TT 11/2025 từ 01/07/2025; liên thông CSDL dược từ **01/01/2026** | Còn HL; điểm đ k1 Đ5 bị bãi bỏ (QĐ 2656) | Nhà thuốc (PL I-1a), quầy thuốc (I-1b), tủ thuốc trạm y tế xã (I-1c), vendor | gốc (VBHN) | [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/11-vbhn-byt.pdf) |
| TT-11-2025-BYT | 11/2025/TT-BYT (16/05/2025) | Sửa TT 02/2018 (GPP), TT 03/2018 (GDP), TT 36/2018 (GSP) | 01/07/2025; Đ5 k2: liên thông dữ liệu với hệ thống thông tin về dược từ 01/01/2026 | Còn HL | Nhà thuốc, quầy, bán buôn | gốc (qua VBHN 11/VBHN-BYT, chú thích 60–74) | (qua VBHN ở trên) |
| QD-2656-2026-BYT | 2656/QĐ-BYT (19/08/2026) | Bãi bỏ điểm đ k1 Đ5 TT 02/2018 | Kể từ ngày ký (Đ2) = 19/08/2026 | Còn HL | Nhà thuốc (thủ tục hồ sơ) | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/2656-byt.signed.pdf) |
| TT-31-2025-BYT | 31/2025/TT-BYT (01/07/2025) | Chi tiết Luật Dược và NĐ 163 (Đ10 + PL III: Danh mục thuốc hạn chế bán lẻ) | 01/07/2025 | Còn HL; thay TT 07/2018 (Đ25 k2) | Nhà thuốc, vendor | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/31-byt.pdf) |
| TT-20-2017-BYT | 20/2017/TT-BYT, sửa bởi 27/2024/TT-BYT | Thuốc và nguyên liệu làm thuốc phải kiểm soát đặc biệt (báo cáo, giao nhận, biên bản nhận lại) | TT 27/2024 HL 30/01/2025 (thứ cấp) | Còn HL (TT 26 Đ11 k2, Đ12 k7b vẫn dẫn chiếu; văn bản gốc hướng dẫn NĐ 54 đã hết HL nên cần xác minh) | Cơ sở KCB, nhà thuốc | TT 27/2024: gốc; TT 20/2017: chưa đọc | [VB 211680](https://vanban.chinhphu.vn/?pageid=27160&docid=211680) · [PDF TT 27/2024](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/27-byt.pdf) |
| TT-32-2026-BYT (mới) | 32/2026/TT-BYT (29/07/2026) | Đăng ký lưu hành thuốc, nguyên liệu làm thuốc (Đ15 tiêu chí OTC; PL V cấu trúc số đăng ký 12 chữ số) | **01/10/2026** (Đ52 k1) | Còn HL; thay TT 12/2025 (Đ52 k2a) | Vendor (master data thuốc), nhà thuốc | gốc (bản PDF do BV Ung Bướu đăng, chưa đối chiếu datafiles) | [PDF](https://benhvienungbuou.vn/wp-content/uploads/2026/08/Thong-tu-32.2026.TT-BYT-ngay-29.07.2026-quy-dinh-viec-dang-ky-luu-hanh-thuoc-nguyen-lieu-lam-thuoc-do-Bo-truong-Bo-Y-te-ban-hanh.pdf) |
| TT-12-2025-BYT (mới) | 12/2025/TT-BYT (16/05/2025) | Đăng ký lưu hành thuốc (cũ) | 01/07/2025 → hết HL 01/10/2026 | Thay bởi TT-32-2026-BYT | — | gốc-meta | [VB 213708](https://vanban.chinhphu.vn/?pageid=27160&docid=213708) |
| ND-90-2026 | 90/2026/NĐ-CP (30/03/2026) | Xử phạt VPHC lĩnh vực y tế (Đ38, Đ41 kê đơn/cấp phát; Đ59 bán lẻ thuốc; Đ85–86 kê khống BHYT) | 15/05/2026 | Còn HL; thay NĐ 117/2020 | Cơ sở KCB, nhà thuốc | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| QD-425-2025-BYT | 425/QĐ-BYT (05/02/2025) | Quy chế quản lý, vận hành, sử dụng, bảo đảm an toàn, an ninh mạng của Hệ thống thông tin quốc gia về quản lý kê đơn thuốc và bán thuốc theo đơn | Kể từ ngày ký | Còn HL (căn cứ của nó đã bị thay: TT 27/2021, TT 04/2022, TT 46/2018, NĐ 13/2023, NĐ 85/2016) | Cơ sở KCB, nhà thuốc, đơn vị phát triển hệ thống | gốc-OCR (bản sao do BVĐK Bạc Liêu đăng) | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20250404/529_Quyet_dinh-425-QD-BYT_60abac9cf6.pdf) |
| QD-808-BYT | 808/QĐ-BYT, ngày **01/04/2022** (không phải 2023, xem §6) | Tài liệu hướng dẫn kết nối với Hệ thống thông tin quốc gia về quản lý kê đơn thuốc và bán thuốc theo đơn | Kể từ ngày ký | Còn HL (là chuẩn kết nối mà QĐ 425 Đ9 k2, Đ19 k1 dẫn chiếu) | Vendor HIS/PK | thứ cấp (luatvietnam) + được QĐ 228/QĐ-QLD dẫn chiếu | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-808-qd-byt-bo-y-te-218990-d1.html) |
| QD-228-2023-QLD (mới) | 228/QĐ-QLD (03/04/2023) | Chuẩn kết nối giữa Hệ thống CSDL Dược quốc gia và Hệ thống đơn thuốc quốc gia (API lấy đơn, API cập nhật số lượng bán) | Kể từ ngày ký | Còn HL (quan hệ với QĐ 232/2026 chưa rõ); thay Bảng 3 QĐ 540/QĐ-QLD (2018) và mục 2–4, 5.2 QĐ 777/QĐ-QLD (2018) | Vendor phần mềm nhà thuốc | gốc (bản ký số, sao trên syt.hue.gov.vn) | [PDF](https://syt.hue.gov.vn/review/?id=MTM1NjcyfFRUVERU0&fileName=228_1%281%29.pdf) |
| QD-318-2021-QLD (mới) | 318/QĐ-QLD (04/06/2021) | Chuẩn kết nối dữ liệu phần mềm kết nối liên thông cơ sở phân phối thuốc | Kể từ ngày ký | Chưa rõ sau QĐ 232/2026 | Vendor phần mềm bán buôn | gốc | [PDF](https://dav.gov.vn/upload_images/files/318_Q%C4%90_QLD_signed.pdf) |
| QD-1867-BYT | 1867/QĐ-BYT (24/06/2026) | Kế hoạch triển khai Hệ thống cơ sở dữ liệu về dược | Kể từ ngày ký | Còn HL | XNK, bán buôn, bán lẻ, chuỗi nhà thuốc | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-1867-qd-byt-2026-trien-khai-he-thong-co-so-du-lieu-ve-duoc-438578-d1.html) |
| QD-232-TTYQG | 232/QĐ-TTYQG (17/07/2026) | Tài liệu kỹ thuật đặc tả API (PL 1, v1.1) và hướng dẫn sử dụng Hệ thống cơ sở dữ liệu về dược | chưa xác minh | Còn HL | Vendor phần mềm nhà thuốc/kho/ERP dược | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-232-qd-ttyqg-2026-ban-hanh-tai-lieu-ky-thuat-api-va-huong-dan-su-dung-he-thong-co-so-du-lieu-duoc-441421-d1.html) |
| CV-934-2026-TTYQG | 934/TTYQG-DA (12/08/2026) | Triển khai Hệ thống CSDL về dược (dữ liệu từ 01/01/2026; 2 phương thức API/nhập tay; xác thực VNeID) | — | Đang áp dụng | Bán buôn, bán lẻ | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/tin-van-ban-moi/co-so-ban-buon-ban-le-thuoc-phai-lien-thong-du-lieu-tu-01-01-2026-len-he-thong-co-so-du-lieu-ve-duoc-186-111475-article.html) · [VNeID, thứ cấp](https://luatvietnam.vn/tin-van-ban-moi/nha-thuoc-thuc-hien-xac-thuc-tai-khoan-qua-vneid-khi-dang-nhap-he-thong-co-so-du-lieu-ve-duoc-186-111551-article.html) |
| CV-3656-2026-QLD | 3656/QLD-KD (28/09/2026) | Đăng ký tài khoản Hệ thống CSDL về dược trước 04/10/2026 | — | Đang áp dụng | Theo tóm tắt: cơ sở SX, XNK, kinh doanh dịch vụ bảo quản…; Sở Y tế phê duyệt tài khoản bán buôn/bán lẻ | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/tin-van-ban-moi/co-so-kinh-doanh-duoc-khan-truong-dang-ky-tai-khoan-tren-he-thong-co-so-du-lieu-ve-duoc-truoc-04-10-2026-186-112993-article.html) |
| TT-23-2011-BYT | 23/2011/TT-BYT | Hướng dẫn sử dụng thuốc trong cơ sở y tế có giường bệnh | — | Còn HL (TT 55 Đ3 k6 vẫn dẫn chiếu, 12/2025) | BV (kho, cấp phát nội trú) | chưa XM (chưa đọc) | — |

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### A. Kê đơn (HIS, EMR, phần mềm phòng khám)

**DUOC-R01. Chỉ người có thẩm quyền mới được kê đơn**
- **Căn cứ**: TT 26/2025 Đ2 (bác sỹ, y sỹ có CCHN hoặc GPHN); TT 55/2025 Đ4 (ma trận chức danh kê thuốc thang / cổ truyền / dược liệu; lương y chỉ kê thuốc nam dạng thang), Đ6 (kê kết hợp hóa dược; điểm b k1: một số chức danh chỉ được kê kết hợp khi "người chịu trách nhiệm chuyên môn của cơ sở cho phép bằng văn bản"), Đ15 k3 g.
- **Áp dụng cho**: BV công, BV tư, PK · **Hiệu lực**: 01/07/2025 (hóa dược), 01/03/2026 (YHCT)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu chức danh, số CCHN/GPHN, phạm vi hành nghề của từng người kê; chặn ký/phát hành đơn nếu chức danh không có quyền với loại thuốc trong đơn (ví dụ y sĩ YHCT kê thuốc hóa dược ngoài trường hợp cấp cứu, TT 55 Đ6 k3 b); lưu số/ngày văn bản cho phép kê kết hợp.
- **Ghi chú / bẫy**: thẩm quyền với YHCT phụ thuộc chức danh *và* loại thuốc (thang / cổ truyền / dược liệu / hóa dược), không chỉ "bác sĩ hay y sĩ".

**DUOC-R02. Mã liên thông duy nhất của cơ sở và của người kê đơn**
- **Căn cứ**: TT 26 Đ12 k1 c, k5 d (Cục QLKCB và Sở Y tế cấp mã định danh cơ sở và mã người hành nghề qua Hệ thống đơn thuốc QG); QĐ 425 Đ3 k2–3 (mã liên thông người kê đơn tạo theo QĐ 3176/QĐ-BYT 29/10/2024; mã cơ sở theo QĐ 384/QĐ-BYT 01/02/2019), Đ9 k1 b ("là mã duy nhất"), Đ9 k4, Đ20 k3 a ("Mỗi cơ sở và mỗi người kê đơn chỉ sử dụng một mã liên thông duy nhất").
- **Áp dụng cho**: mọi cơ sở KCB kê đơn · **Hiệu lực**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: có trường mã liên thông cơ sở và mã liên thông người kê đơn (một mã cho mỗi người, dùng chung khi người đó làm ở nhiều cơ sở); gắn vào mọi đơn gửi đi; có quy trình cập nhật khi nhân sự thay đổi (QĐ 425 Đ9 k4 c).
- **Ghi chú / bẫy**: QĐ 425 Đ8 k1 đ: đơn vị phát triển phần mềm **không được cấp tài khoản** trên Hệ thống đơn thuốc QG; vendor không được giữ hộ tài khoản quản trị của cơ sở.

**DUOC-R03. Mẫu đơn và các trường thông tin bắt buộc**
- **Căn cứ**: TT 26 Đ3 (PL I đơn thường, PL II đơn "N", PL III đơn "H"), Đ6 k1–4 (số định danh cá nhân/CCCD/căn cước/hộ chiếu nếu có; nơi cư trú; trẻ dưới 72 tháng: số tháng tuổi, cân nặng, họ tên người đưa trẻ), chú thích PL I (chú thích 3: công dân VN đã cung cấp số định danh cá nhân thì không cần khai giới tính, ngày sinh, địa chỉ thường trú; chú thích 6: mã số BHYT; chú thích 7: lời dặn gồm lịch tái khám, "thời hạn tốt nhất của việc mua thuốc"). PL II, III thêm "số định danh … của người nhận thuốc". Đ4 k2: khám nhiều chuyên khoa trong một lần được kê 01 đơn. TT 55 PL I (đơn thuốc thang: bảng vị thuốc, khối lượng, số thang, cách sắc, cách uống), PL II (đơn cổ truyền, dược liệu), Đ8 k2–4.
- **Áp dụng cho**: cơ sở KCB · **Hiệu lực**: 01/07/2025; 01/03/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: có đủ trường theo mẫu; validate: trẻ < 72 tháng thì bắt buộc tháng tuổi + cân nặng + người đưa trẻ; cho phép bỏ trống giới tính/ngày sinh/địa chỉ khi đã có số định danh cá nhân; bản in khớp bố cục mẫu PL; đơn N, H có ô thông tin người nhận thuốc.
- **Ghi chú / bẫy**: Luật KCB Đ63 k2: "không kê đơn thực phẩm chức năng trong đơn thuốc", phần mềm phải chặn sản phẩm không phải thuốc khỏi đơn (NĐ 90 Đ41 k2 b phạt "kê vào đơn thuốc các sản phẩm không được kê đơn").

**DUOC-R04. Mã đơn thuốc đúng định dạng 14 ký tự**
- **Căn cứ**: TT 26 PL I chú thích 1 (dùng chung cho PL II, III): "Mã đơn thuốc: có chiều dài 14 ký tự (bao gồm chữ số và chữ cái) được tạo ra tự động theo cấu trúc … xxxxxyyyyyyy-z." 5 ký tự x = mã cơ sở KCB; 7 ký tự y = "giá trị ngẫu nhiên là số từ 0-9 hoặc chữ cái từ a-z, bảo đảm tính duy nhất của đơn thuốc tại một cơ sở"; z = loại đơn: **N** (gây nghiện), **H** (hướng thần, tiền chất), **C** (đơn khác); dấu "-" ngăn giữa 12 ký tự đầu và z. TT 55 PL I chú thích 1: z = **T** (đơn thuốc thang).
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 01/07/2025 (YHCT: 01/03/2026)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh mã tự động; độ dài 14 tính **cả dấu gạch ngang** (5+7+1+1); phần y sinh ngẫu nhiên (không dùng số tăng dần), ký tự [0-9a-z]; ràng buộc duy nhất (mã cơ sở, phần y); z suy ra từ nội dung đơn (có thuốc gây nghiện → N; có hướng thần/tiền chất → H; thang → T; còn lại → C); mã bất biến sau khi phát hành.
- **Ghi chú / bẫy**: TT 55 PL II (đơn cổ truyền, dược liệu) chép nguyên chú thích "T: Đơn thuốc thang", không định nghĩa ký tự riêng cho đơn cổ truyền/dược liệu (xem §6, §7). Bộ ký tự của 5 ký tự mã cơ sở do QĐ 384/QĐ-BYT quy định, chưa đọc.

**DUOC-R05. Quy tắc ghi thuốc trong đơn**
- **Căn cứ**: TT 26 Đ6 k5 (một hoạt chất: ghi tên chung quốc tế INN, hoặc INN + (tên thương mại); nhiều hoạt chất hoặc sinh phẩm: tên thương mại), k6 (tên, nồng độ/hàm lượng, số lượng/thể tích, liều mỗi lần, số lần/ngày, đường dùng, thời điểm dùng, số ngày dùng; "Nếu đơn thuốc có thuốc độc phải ghi thuốc độc trước khi ghi các thuốc khác"), k7 (số lượng < 10 ghi số 0 phía trước; thuốc gây nghiện ghi số rồi ghi bằng chữ). Luật KCB Đ63 k2. TT 55 Đ8 k1 (tên thuốc bằng tiếng Việt), k5 (thuốc thang: tên theo Dược điển hoặc tên thường dùng, không viết tắt; vị < 10 g ghi số 0 phía trước; vị chế từ dược liệu độc theo TT 13/2024 ghi khối lượng bằng số và bằng chữ; trùng lặp vị vượt liều thì ghi số, chữ và "tôi kê liều này", "bao gồm việc kê đơn thuốc điện tử"), k6 (thứ tự kê).
- **Áp dụng cho**: cơ sở KCB · **Hiệu lực**: như R03
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục thuốc có trường INN, tên thương mại, số hoạt chất, cờ thuốc độc, cờ gây nghiện, cờ dược liệu độc; tự sinh tên hiển thị đúng quy tắc; tự sắp thuốc độc lên đầu; render số lượng 2 chữ số ("05"); với thuốc N tự thêm số bằng chữ ("05 (năm)"); bắt buộc nhập đủ liều, đường dùng, thời điểm, số ngày; YHCT có cơ chế xác nhận "tôi kê liều này" khi vượt liều.
- **Ghi chú / bẫy**: NĐ 90/2026 Đ38 k5 đ (gốc-OCR) phạt chỉ định điều trị, kê đơn bằng ngôn ngữ không phải tiếng Việt khi chưa đăng ký ngôn ngữ. Giao diện đa ngôn ngữ không được in đơn bằng ngôn ngữ khác.

**DUOC-R06. Giới hạn số ngày dùng thuốc**
- **Căn cứ**: TT 26 Đ6 k8 a (tối đa 30 ngày/thuốc), k8 b + PL VII (252 bệnh/nhóm bệnh theo mã ICD-10: tối đa 90 ngày); Đ7 k2 (gây nghiện, bệnh cấp tính: ≤ 7 ngày); Đ8 k1 (ung thư: mỗi lần ≤ 30 ngày, ghi 3 đợt liên tiếp, mỗi đợt ≤ 10 ngày, ghi ngày bắt đầu/kết thúc); Đ9 k2–3 (hướng thần/tiền chất: cấp tính ≤ 10 ngày, dài ngày ≤ 30 ngày). TT 55 Đ8 k7 a (thuốc thang ≤ 30 ngày; chứa vị từ dược liệu độc ≤ 05 ngày; bệnh cấp tính ≤ 05 ngày; cổ truyền/dược liệu ≤ 90 ngày), k7 b (thang nội trú kê tối thiểu 2 lần/10 ngày).
- **Áp dụng cho**: cơ sở KCB · **Mức**: BẮT BUỘC
- **Phần mềm phải**: rule engine theo (loại thuốc × chẩn đoán ICD-10 × cấp tính/mạn tính); bảng PL VII nạp làm master data có phiên bản; chặn hoặc cảnh báo cứng khi vượt; đơn N ung thư có 3 đợt với ngày.
- **Ghi chú / bẫy**: PL VII ghi "Z69.64", "Z69.65" cho thay khớp háng/gối, không khớp mã ICD-10 WHO thông dụng (suy luận: có thể là lỗi in của Z96.6x). Nạp đúng nguyên văn rồi ánh xạ thêm, không tự sửa.

**DUOC-R07. Đơn "N" và "H" là đơn riêng, nhiều bản**
- **Căn cứ**: TT 26 Đ7 k1 (đơn "N" dùng tại cơ sở KCB **có giường bệnh**, làm 03 bản: lưu cơ sở KCB, lưu HSBA, bản có dấu treo lưu tại cơ sở cấp/bán; cơ sở tự cấp thì không cần dấu); Đ9 k1 (đơn "H" 03 bản tương tự); PL II chú thích 10 (mua/lĩnh đợt 2, 3 trước 01–03 ngày), chú thích 11 (cơ sở cấp/bán yêu cầu người nhận xuất trình căn cước).
- **Áp dụng cho**: cơ sở KCB, nhà thuốc · **Mức**: BẮT BUỘC
- **Phần mềm phải**: tách đơn theo loại (thuốc N không lẫn vào đơn C); chặn tạo đơn N ở cơ sở không có giường bệnh (cấu hình loại hình cơ sở); in đủ 03 bản có nhãn bản; lưu trạng thái đã đóng dấu/đã giao bản cho người bệnh.
- **Ghi chú / bẫy**: TT 26 Đ10 cho đơn điện tử giá trị như đơn giấy, nhưng Đ7, Đ9 vẫn yêu cầu bản có dấu lưu tại nơi bán. Chưa có hướng dẫn bỏ bản giấy cho N/H (xem §7). Suy luận: vẫn phải in.

**DUOC-R08. Hồ sơ kèm theo đơn thuốc gây nghiện**
- **Căn cứ**: TT 26 Đ7 k3 + PL IV (cam kết sử dụng thuốc gây nghiện, 02 bản), Đ7 k4 (danh sách chữ ký mẫu người kê đơn thuốc gây nghiện), Đ8 k1 (ung thư: lập HSBA ngoại trú), Đ8 k2 (người bệnh ung thư nằm tại nhà: bác sỹ cơ sở có giường nội trú kê; xác nhận của trạm trưởng trạm y tế theo PL V, giá trị cho một lần kê; tóm tắt bệnh án theo PL XXIX TT 32/2023).
- **Áp dụng cho**: cơ sở KCB · **Mức**: BẮT BUỘC
- **Phần mềm phải**: workflow kê đơn N yêu cầu đính kèm hoặc ghi nhận cam kết (scan hoặc ký điện tử), mỗi xác nhận PL V chỉ dùng cho một đơn; quản lý danh sách chữ ký mẫu người kê N; bắt buộc có HSBA ngoại trú khi chẩn đoán ung thư.

**DUOC-R09. Sửa đơn là kê đơn mới thay thế, đơn đã gửi bất biến**
- **Căn cứ**: TT 26 Đ6 k9 ("người kê đơn thực hiện kê đơn thuốc mới thay thế đơn thuốc cũ"); QĐ 425 Đ9 k3 c (gốc-OCR): đơn đã gửi lên hệ thống không được thay đổi, cập nhật lại; đơn cũ vẫn được lưu nhưng không cung cấp cho người bệnh để cấp phát hay mua bán. TT 55 Đ9 k1 (BV: gửi đơn/phiếu lĩnh đã điều chỉnh tới khoa dược; PK dùng giấy: ký tên, ghi ngày cạnh chỗ sửa, lưu đơn trước và sau).
- **Áp dụng cho**: cơ sở KCB · **Mức**: BẮT BUỘC
- **Phần mềm phải**: không có thao tác UPDATE nội dung đơn đã phát hành; "sửa" = tạo đơn mới (mã mới) có liên kết `replaces`, đơn cũ chuyển trạng thái "đã thay thế"; thông báo người bệnh (TT 55 Đ15 k4 d).

**DUOC-R10. Đơn phải khớp chỉ định trong HSBA**
- **Căn cứ**: TT 26 Đ5 k1 b (có HSBA ngoại trú: chỉ định ghi vào HSBA, đơn phải phù hợp), k2 a (ra viện cần dùng 01–07 ngày: ghi HSBA nội trú và kê đơn phù hợp), k2 b (trên 07 ngày: kê đơn ngoại trú, lập HSBA ngoại trú hoặc chuyển viện); TT 55 Đ8 k7 c.
- **Áp dụng cho**: BV, PK có HSBA · **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh đơn từ y lệnh trong HSBA (một nguồn dữ liệu), không cho hai bản lệch nhau; kiểm tra nhất quán khi ký.

**DUOC-R11. Kê đơn bằng hình thức điện tử và ký số**
- **Căn cứ**: TT 26 Đ10 ("được lập, hiển thị, ký số, chia sẻ, lưu trữ bằng phương thức điện tử … có giá trị pháp lý như đơn thuốc giấy"); Đ13 k3 (BV trước 01/10/2025; cơ sở khác trước 01/01/2026); QĐ 425 Đ11 (gốc-OCR): hai hình thức: (1) chữ ký số của người chịu trách nhiệm chuyên môn trên mỗi đơn + người kê ký chữ ký điện tử; (2) người kê dùng chữ ký số cá nhân trên mỗi đơn. TT 55 Đ10 k1–2.
- **Áp dụng cho**: BV (đã quá hạn 01/10/2025), PK và cơ sở khác (đã quá hạn 01/01/2026) · **Mức**: BẮT BUỘC
- **Phần mềm phải**: hỗ trợ ít nhất một trong hai mô hình ký của QĐ 425 Đ11; chữ ký số gắn với bản đơn chuẩn hóa (canonical) đã gửi; lưu chứng thư, dấu thời gian, kết quả xác thực.
- **Ghi chú / bẫy**: QĐ 425 Đ11 k1 còn dẫn TT 46/2018 (đã bị TT 13/2025 thay). Hình thức chữ ký số và dịch vụ tin cậy thuộc cụm K1/NĐ 23/2025. TT 55 Đ10 k2 đoạn 2 cho phòng khám tư "ghi trong máy tính 01 lần, sau đó in ra và người hành nghề ký tên" là cơ chế lai cho đơn YHCT.

**DUOC-R12. Gửi đơn lên Hệ thống đơn thuốc quốc gia đúng thời điểm**
- **Căn cứ**: TT 26 Đ12 k6 d: gửi đơn điện tử "ngay sau khi kết thúc quy trình khám bệnh, chữa bệnh" với các trường hợp ở Đ5 (ngoại trú và ra viện); TT 55 Đ15 k3 d (YHCT ngoại trú); QĐ 425 Đ9 k3 a (gốc-OCR): ngoại trú ngay sau khi kết thúc khám, **nội trú trước khi ra viện**; đơn gửi gồm đơn BHYT, đơn ngoại trú dịch vụ và "bảng tổng hợp thuốc sử dụng của người bệnh điều trị nội trú"; Đ10 (loại đơn phải gửi); Đ20 k3 b.
- **Áp dụng cho**: mọi cơ sở KCB · **Mức**: BẮT BUỘC (ngoại trú); BẮT BUỘC? (bảng tổng hợp thuốc nội trú: QĐ 425 Đ10 k2 dẫn TT 27/2021 đã hết HL)
- **Phần mềm phải**: tự động gửi khi đóng lượt khám hoặc ký đơn (không phụ thuộc thao tác tay); hàng đợi gửi lại khi lỗi; lưu mã phản hồi, thời điểm gửi, thời điểm nhận; báo cáo đơn chưa gửi hoặc gửi lỗi; chặn xuất viện nếu chưa gửi (cấu hình).
- **Ghi chú / bẫy**: "ngay sau" không có số phút cụ thể. Gửi gom cuối ngày có rủi ro bị coi là vi phạm (suy luận). Không tìm thấy trong bản OCR NĐ 90/2026 điều khoản phạt riêng cho việc không gửi đơn điện tử (xem §7).

**DUOC-R13. Kết nối theo chuẩn của Bộ Y tế**
- **Căn cứ**: QĐ 425 Đ9 k2 (phần mềm cơ sở KCB kết nối theo QĐ 808/QĐ-BYT), Đ19 k1; TT 26 Đ12 k3 a (Cục KHCN&ĐT chủ trì ban hành đặc tả cấu trúc dữ liệu và hướng dẫn kết nối cho cơ sở KCB và cơ sở bán lẻ); Đ12 k6 c ("Bảo đảm hạ tầng công nghệ thông tin đáp ứng tiêu chí kỹ thuật theo quy định của Bộ trưởng Bộ Y tế").
- **Áp dụng cho**: vendor HIS/PK · **Mức**: BẮT BUỘC? (QĐ 808 mới đọc qua thứ cấp; chưa thấy đặc tả mới theo TT 26 Đ12 k3 a)
- **Phần mềm phải**: tách adapter kết nối để thay phiên bản đặc tả không phải sửa lõi; lưu `spec_version` cho mỗi lần gửi.

**DUOC-R14. Gửi đơn hoặc mã đơn cho người bệnh qua phương tiện điện tử**
- **Căn cứ**: TT 26 Đ12 k6 đ; TT 55 Đ15 k3 đ.
- **Áp dụng cho**: cơ sở KCB · **Mức**: BẮT BUỘC (kênh cụ thể "theo hướng dẫn của Bộ Y tế", chưa thấy hướng dẫn)
- **Phần mềm phải**: giao mã đơn (QR/mã vạch trên bản in, SMS, app, Sổ SKĐT/VNeID nếu có) và lưu bằng chứng đã gửi; không đưa dữ liệu nhạy cảm vào tin nhắn rõ (NÊN).

**DUOC-R15. Lưu trữ đơn và bảo đảm trích xuất**
- **Căn cứ**: TT 26 Đ11 k1 (cơ sở KCB, pha chế, cấp thuốc, bán lẻ lưu toàn bộ đơn và tài liệu ở Đ7 k3, Đ8 k2, Đ12 k6 b, Đ12 k7 b "theo quy định … tại Thông tư số 53/2017/TT-BYT"); Đ11 k2 (hết hạn lưu tài liệu về thuốc gây nghiện, hướng thần, tiền chất thì lập Hội đồng hủy tài liệu theo TT 20/2017); Đ12 k6 e (lưu trữ và "bảo đảm việc trích xuất dữ liệu khi cần thiết"); Đ14 (văn bản viện dẫn bị thay thì áp dụng văn bản mới); TT 55 Đ10 k2 (đơn điện tử lưu trong CSDL của cơ sở, "bảo đảm liên thông với cơ sở dữ liệu quốc gia về y tế và sổ sức khoẻ điện tử"), Đ10 k3, Đ11 k2 (thời hạn lưu "theo quy định tại điểm a khoản 2 Điều 1 Thông tư số 33/2025/TT-BYT"); TT 33/2025 Đ1 k2 a (thời hạn trong Phụ lục áp dụng cho tài liệu giấy và điện tử), k2 b (loại chưa quy định thì áp dụng thời hạn tương đương nhóm tương ứng, "không được thấp hơn").
- **Áp dụng cho**: cơ sở KCB, nhà thuốc · **Mức**: BẮT BUỘC (phải lưu và trích xuất được); BẮT BUỘC? (con số thời hạn, xem §6)
- **Phần mềm phải**: lưu bất biến đơn đã ký (gồm cả đơn bị thay thế), cam kết PL IV, xác nhận PL V, biên bản PL VI; chính sách retention cấu hình theo loại tài liệu, mặc định **≥ 10 năm** (khuyến nghị, suy luận theo dòng 44 PL TT 33 "Hồ sơ bệnh án nội trú, ngoại trú: 10 năm"); xuất theo yêu cầu (lọc theo người bệnh, người kê, thời gian, loại N/H/C/T); hủy chỉ qua quy trình có biên bản Hội đồng.
- **Ghi chú / bẫy**: Phụ lục TT 33 (đã đọc đủ 210+ dòng) **không có dòng riêng cho đơn thuốc** hay "hồ sơ cấp phát thuốc". Dòng gần nhất: 44 (HSBA nội trú, ngoại trú: 10 năm), 47 (sổ, sách phục vụ công tác KCB: 05 năm). Xem §6.

**DUOC-R16. Thời hạn hiệu lực của đơn**
- **Căn cứ**: TT 26 Đ12 k9 b (người bệnh lĩnh thuốc "trong thời hạn tối đa 05 ngày, kể từ ngày kê đơn"); TT 55 Đ11 k1 (đơn "có giá trị mua, lĩnh thuốc trong thời hạn tối đa là 05 (năm) ngày"), Đ15 k5 b (ra viện dùng tiếp 01–07 ngày: lĩnh trong 02 ngày); PL II TT 26 chú thích 10 (đơn N theo đợt); GPP PL I-1a III.2 đ ("không bán đơn thuốc hết hạn").
- **Áp dụng cho**: cơ sở KCB (hiển thị), nhà thuốc (chặn) · **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu `valid_until` cho đơn (ngày kê + 5 ngày; trường hợp ra viện YHCT + 2 ngày; đơn N theo đợt); in trên đơn; phía nhà thuốc chặn bán khi hết hạn.

**DUOC-R17. Thuốc YHCT: quy tắc riêng**
- **Căn cứ**: TT 55 Đ3 k5 (phần hóa dược trong đơn kết hợp ngoại trú theo TT 26), Đ7 k2 (mẫu PL I, PL II), Đ8, Đ9 k2 (thuốc chưa dùng phải có xác nhận trưởng khoa gửi khoa dược trong 24 giờ), Đ9 k4 (hủy thuốc thang đã sắc: Hội đồng ≥ 03 người), Đ12 k3 (e-Rx YHCT "theo lộ trình của Chính phủ và Bộ Y tế"), Đ15 k3 d–e.
- **Áp dụng cho**: cơ sở có YHCT · **Mức**: BẮT BUỘC (nội dung đơn); BẮT BUỘC? (mốc bắt buộc e-Rx YHCT chưa có ngày, nhưng Đ15 k3 d đã yêu cầu gửi đơn điện tử ngoại trú)
- **Phần mềm phải**: hỗ trợ đơn kết hợp (thang + cổ truyền + dược liệu + hóa dược) thành các đơn theo mẫu tương ứng; mã đơn z = T cho đơn thang; danh mục vị thuốc có cờ dược liệu độc (TT 13/2024).

**DUOC-R18. Nhận lại thuốc gây nghiện, hướng thần, tiền chất**
- **Căn cứ**: TT 26 Đ12 k6 b (cơ sở KCB nhận lại thuốc không dùng hết hoặc người bệnh tử vong, lập biên bản theo PL VI, 02 bản, thuốc biệt trữ và tiêu hủy), Đ12 k7 b (cơ sở bán lẻ, xử lý theo TT 27/2024); TT 20/2017 Đ7 k2 d bổ sung bởi TT 27/2024 Đ1 k4 (cơ sở bán lẻ lập biên bản nhận lại 02 bản theo PL XX); TT 55 Đ9 k3, Đ15 k3 b.
- **Áp dụng cho**: cơ sở KCB, nhà thuốc · **Mức**: BẮT BUỘC
- **Phần mềm phải**: phiếu nhận lại thuốc gắn với đơn gốc và lô; tạo bút toán nhập vào kho biệt trữ (không bán lại); in biên bản đúng mẫu; theo dõi đến khi hủy.

**DUOC-R19. Báo cáo thuốc phải kiểm soát đặc biệt**
- **Căn cứ**: TT 20/2017 Đ8 k1 a sửa bởi TT 27/2024 Đ1 k5: trước 15/01 hằng năm, cơ sở KCB lập báo cáo xuất, nhập, tồn kho, sử dụng thuốc gây nghiện, hướng thần, tiền chất, **thuốc phóng xạ**, thuốc dạng phối hợp có chứa tiền chất theo PL X, gửi Sở Y tế. NĐ 163 Đ35 k2 a (gốc-OCR): cơ sở bán buôn, bán lẻ, chuỗi nhà thuốc báo cáo 06 tháng và năm trước 15/7 và 15/01 theo Mẫu 06 PL II gửi UBND cấp tỉnh; Đ35 k2 b: cơ sở bán lẻ, chuỗi báo cáo năm về thuốc phóng xạ; Đ35 k4: nhầm lẫn, thất thoát báo cáo trong **48 giờ** kể từ khi phát hiện (Mẫu 07); Đ35 k5: không báo cáo thì bị ngừng tiếp nhận hồ sơ mua thuốc.
- **Áp dụng cho**: cơ sở KCB, nhà thuốc · **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh báo cáo theo mẫu từ sổ cái kho (không nhập tay số liệu), theo kỳ 6 tháng/năm; quy trình báo cáo sự cố thất thoát có đồng hồ 48 giờ.

**DUOC-R20. Cấp phát thuốc tại cơ sở KCB phải đối chiếu đơn**
- **Căn cứ**: Luật KCB Đ63 k3 (kiểm tra đơn, phiếu lĩnh; đối chiếu tên thuốc, nồng độ, hàm lượng, hạn dùng, số lượng; đối chiếu họ tên người bệnh; nội trú ghi thời gian cấp phát); NĐ 90 Đ41 k1 (gốc-OCR, phạt 1–2 triệu đồng cho từng hành vi không kiểm tra, không đối chiếu, không ghi thời gian cấp phát), Đ41 k3 (cấp phát thuốc hết hạn, không rõ nguồn gốc: 20–30 triệu).
- **Áp dụng cho**: BV, PK có quầy cấp phát · **Mức**: BẮT BUỘC
- **Phần mềm phải**: màn hình cấp phát quét mã đơn và mã thuốc/lô; chặn lô hết hạn hoặc bị thu hồi; ghi người cấp, thời gian cấp; nội trú ghi thời điểm cấp từng liều (eMAR, NÊN).

**DUOC-R21. Bảo mật dữ liệu đơn thuốc**
- **Căn cứ**: QĐ 425 Đ9 k5 (gốc-OCR: đơn thuốc cho người bệnh HIV/AIDS phải được mã hóa thông tin người bệnh để không hiển thị khi tra cứu), Đ17 ("Thông tin định danh cá nhân của người bệnh phải được mã hóa và áp dụng cơ chế phân quyền"), Đ8 k2, Đ12 k2 (xuất dữ liệu phải ẩn danh), Đ16 k3 (mật khẩu tài khoản quản trị ≥ 8 ký tự gồm chữ hoa, chữ thường, số, ký tự đặc biệt, đổi tối thiểu 06 tháng/lần); Đ20 k4 c (nhà thuốc bảo mật thông tin người bệnh); GPP PL I-1a III.4 a (giữ bí mật thông tin người bệnh).
- **Áp dụng cho**: cơ sở KCB, nhà thuốc, vendor · **Mức**: BẮT BUỘC? (các điều trên điều chỉnh trực tiếp Hệ thống QG; với phần mềm cơ sở thì có căn cứ chung về bảo mật nhưng không có câu chữ "mã hóa" riêng)
- **Phần mềm phải**: đánh dấu đơn HIV/AIDS để gửi theo cơ chế ẩn danh nếu đặc tả hỗ trợ; mã hóa trường định danh khi lưu; xuất báo cáo ẩn danh; chính sách mật khẩu tối thiểu như QĐ 425 Đ16 k3 cho tài khoản quản trị (NÊN mở rộng cho mọi tài khoản).

### B. Nhà thuốc, quầy thuốc (phần mềm bán lẻ)

**DUOC-R22. Chỉ bán thuốc kê đơn khi có đơn; thuốc gây nghiện chỉ theo đơn "N"**
- **Căn cứ**: TT 26 Đ12 k7 c (thuốc ngoài Danh mục thuốc không kê đơn chỉ bán khi có đơn), Đ12 k7 d; TT 55 Đ15 k6 c–d (thuốc chứa dược liệu độc); Luật 44/2024 Đ1 k1 (định nghĩa thuốc không kê đơn tại khoản 27 Điều 2); TT 32/2026 Đ15 + PL V (chữ số thứ 5 của số đăng ký: 0 = không kê đơn, 1 = kê đơn); NĐ 90 Đ59 k4 g (gốc-OCR: bán thuốc kê đơn khi không có đơn: 10–20 triệu đồng với cá nhân, tổ chức gấp 02 lần theo Đ4 k5).
- **Áp dụng cho**: nhà thuốc, quầy thuốc · **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi mã hàng có cờ kê đơn/không kê đơn và cờ kiểm soát đặc biệt; giao dịch có thuốc kê đơn bắt buộc gắn mã đơn điện tử hoặc thông tin đơn giấy (người kê, cơ sở); thuốc gây nghiện chỉ khi đơn loại N.

**DUOC-R23. Bán theo đơn điện tử, báo cáo đơn đã bán**
- **Căn cứ**: GPP PL I-1a III.2 đ (bổ sung bởi TT 11/2025 Đ1 k8): "Khi bán thuốc kê đơn theo đơn thuốc điện tử, cơ sở phải cập nhật mã đơn thuốc điện tử vào hệ thống bằng dữ liệu đơn thuốc điện tử của Bộ Y tế, đảm bảo liên thông tới hệ thống của Bộ Y tế; bán thuốc đúng theo đơn, số lượng thuốc bán không nhiều hơn số lượng tại đơn thuốc, không bán đơn thuốc hết hạn"; QĐ 425 Đ9 k3 b (gốc-OCR: cơ sở bán lẻ cập nhật trực tiếp báo cáo đơn đã bán, kể cả thuốc thay thế, ngay sau khi hoàn thiện nghiệp vụ bán), Đ12 k1 đ, Đ20 k4 a–b; QĐ 228/QĐ-QLD PL mục I (API `GET /api/v1/thong-tin-donthuoc/{ma_don_thuoc}`), mục II (API `POST /api/v1/cap-nhat-don-thuoc` với `ma_thuoc_da_ke_don`, `ma_thuoc`, `biet_duoc`, `ten_thuoc`, `don_vi_tinh`, `so_luong`, `cach_dung`, mã định danh cơ sở cung ứng…), Đ2 (đơn vị cung cấp phần mềm phải nâng cấp phần mềm để "đón đơn thuốc điện tử").
- **Áp dụng cho**: nhà thuốc (PL I-1a); quầy thuốc (PL I-1b không có điểm tương đương III.2 đ) · **Mức**: BẮT BUỘC (nhà thuốc); BẮT BUỘC? (quầy thuốc, qua TT 26 Đ12 k7 a và QĐ 425 Đ20 k4)
- **Phần mềm phải**: tra đơn bằng mã; tính số lượng còn được bán = kê − đã bán (cộng dồn qua nhiều lần/nhiều nhà thuốc nếu API trả về); chặn vượt số lượng; chặn đơn hết hạn hoặc đơn đã bị thay thế; gửi báo cáo bán ngay sau thanh toán qua hàng đợi có retry.

**DUOC-R24. Thay thế thuốc trong đơn**
- **Căn cứ**: GPP PL I-1a III.2 c: người có Bằng dược sỹ được thay thuốc đã kê bằng thuốc khác cùng hoạt chất, đường dùng, liều lượng khi người mua đồng ý; QĐ 425 Đ9 k3 b (báo cáo kể cả thuốc thay thế).
- **Áp dụng cho**: nhà thuốc · **Mức**: BẮT BUỘC
- **Phần mềm phải**: chỉ cho tài khoản có trình độ dược sỹ thực hiện thay thế; kiểm tra cùng hoạt chất/đường dùng/hàm lượng; ghi nhận đồng ý của người mua; báo cáo đúng `ma_thuoc_da_ke_don` → `ma_thuoc` thực bán.

**DUOC-R25. Quản lý mua bán bằng phần mềm: xuất nhập tồn, lô, hạn, nguồn gốc**
- **Căn cứ**: GPP PL I-1a II.4 b (sổ sách hoặc máy tính quản lý nhập, xuất, tồn, số lô, hạn dùng, nguồn gốc; thông tin thuốc gồm số GPLH/GPNK, số lô, hạn dùng, nhà sản xuất, nhà nhập khẩu, điều kiện bảo quản; người mua, ngày, số lượng với thuốc gây nghiện, hướng thần, tiền chất, dạng phối hợp; thuốc kê đơn thêm người kê và cơ sở hành nghề); II.4 c sửa bởi TT 11/2025 Đ1 k7: "Cơ sở phải có thiết bị công nghệ thông tin kết nối internet và thực hiện quản lý hoạt động mua, bán thuốc bằng phần mềm ứng dụng; bảo đảm kiểm soát xuất xứ, giá cả, nguồn gốc thuốc mua vào, bán ra; đảm bảo truy xuất được nguồn gốc thuốc; đảm bảo trích xuất đầy đủ dữ liệu …"; PL II-2a tiêu chí 5.3.2 (*) là **điểm không chấp nhận** (mắc là không đạt GPP, Đ7 k3 c); NĐ 90 Đ59 k1 c, k2 d, k3 g.
- **Áp dụng cho**: nhà thuốc, quầy thuốc (PL I-1b II.4 c tương tự); tủ thuốc trạm y tế xã (PL I-1c 3 c: kết nối mạng từ 01/01/2021) · **Mức**: BẮT BUỘC
- **Phần mềm phải**: sổ cái kho theo lô/hạn; truy vết một lô từ nhà cung cấp tới từng người mua; xuất toàn bộ dữ liệu theo yêu cầu cơ quan quản lý (CSV/Excel); niêm yết giá và chặn bán cao hơn giá niêm yết (GPP III.2 a; Luật 44 sửa Đ6 k5 i).
- **Ghi chú / bẫy**: Mức phạt theo NĐ 90 Đ59 (gốc-OCR, cá nhân; tổ chức gấp 02): không mở sổ hoặc không dùng máy tính quản lý XNT, lô, hạn: 1–3 triệu (k1 c); không có phần mềm, không truy xuất, không trích xuất hoặc "không liên thông và cập nhật đầy đủ dữ liệu với hệ thống thông tin về dược theo hướng dẫn của Bộ Y tế": 3–5 triệu (k2 d); không có thiết bị, không ứng dụng CNTT, không kết nối mạng: 5–10 triệu (k3 g).

**DUOC-R26. Liên thông Hệ thống cơ sở dữ liệu về dược**
- **Căn cứ**: GPP PL I-1a, I-1b II.4 c (như R25); TT 11/2025 Đ5 k2: quy định liên thông và cập nhật dữ liệu với hệ thống thông tin về dược "thực hiện từ ngày 01 tháng 01 năm 2026"; Luật 44/2024 Đ1 k36 (sửa k2 Đ74: Bộ trưởng quy định "việc liên thông dữ liệu với hệ thống thông tin về dược trong cơ sở dữ liệu quốc gia về y tế"); QĐ 1867/QĐ-BYT (thứ cấp); QĐ 232/QĐ-TTYQG PL 1 API v1.1 (thứ cấp: OAuth 2.0 + Bearer, HTTPS/TLS 1.3; nhóm API danh mục, nhập, xuất, kiểm kho; đồng bộ "theo thời gian thực"); CV 934/TTYQG-DA (thứ cấp: dữ liệu phải liên thông "bao gồm cả dữ liệu từ ngày 01/01/2026 đến thời điểm thực hiện"; 2 phương thức: API qua phần mềm hoặc nhập trực tiếp; định danh, xác thực qua VNeID khi đăng nhập); CV 3656/QLD-KD (thứ cấp: đăng ký tài khoản trên https://csdlduoc.com.vn trước 04/10/2026).
- **Áp dụng cho**: nhà thuốc, quầy thuốc, bán buôn, chuỗi, vendor · **Hiệu lực**: 01/01/2026 (dữ liệu tính từ mốc này) · **Mức**: BẮT BUỘC (nghĩa vụ liên thông); BẮT BUỘC? (chi tiết API, thời gian thực)
- **Phần mềm phải**: map mọi bút toán kho sang loại giao dịch của QĐ 232 (nhập: từ NCC, trả lại, tồn đầu, chuyển kho…; xuất: bán buôn, bán lẻ, chuyển kho, trả lại, thu hồi, hủy…; kiểm kho); outbox đồng bộ gần thời gian thực; chức năng **backfill** dữ liệu từ 01/01/2026; lưu `sync_status` cho từng bút toán; quản lý token theo tài khoản cơ sở (không dùng chung tài khoản giữa các nhà thuốc).
- **Ghi chú / bẫy**: Hệ thống mới (csdlduoc.com.vn, TTYQG vận hành) khác Hệ thống đơn thuốc QG (donthuocquocgia.vn, Cục QLKCB). Chuẩn kết nối cũ của Cục QLD (QĐ 540, 777/2018; 318/2021; 228/2023) có còn dùng song song hay không: chưa rõ. Nguồn duy nhất của nhận định "phần mềm nhà thuốc phải liên thông với hệ thống thuế" (MT-32) **không có trong TT 11/2025/VBHN GPP** (đã tìm, không có từ "thuế").

**DUOC-R27. Lưu hồ sơ, đơn thuốc tại nhà thuốc**
- **Căn cứ**: GPP PL I-1a II.4 d ("Hồ sơ hoặc sổ sách phải được lưu trữ ít nhất 1 năm kể từ khi hết hạn dùng của thuốc"); III.2 c ("Sau khi bán thuốc gây nghiện, thuốc hướng thần, thuốc tiền chất người bán lẻ phải vào sổ, lưu đơn thuốc bản chính"); PL II-2a 5.3.2 ("lưu đơn thuốc của bệnh nhân (bản giấy hoặc điện tử)"); QĐ 425 Đ20 k4 b (lưu đơn tại thời điểm bán trên phần mềm); TT 26 Đ11 k1 (cơ sở bán lẻ lưu toàn bộ đơn); NĐ 90 Đ59 k1 e (không lưu giữ chứng từ, tài liệu liên quan đến lô thuốc trong thời gian phải lưu: 1–3 triệu).
- **Áp dụng cho**: nhà thuốc, quầy thuốc · **Mức**: BẮT BUỘC
- **Phần mềm phải**: snapshot nội dung đơn tại thời điểm bán (không chỉ lưu mã); retention tính theo hạn dùng của lô cuối cùng liên quan + ≥ 1 năm (tối thiểu); cờ "đã lưu bản chính" cho đơn N/H.

**DUOC-R28. Thuốc hạn chế bán lẻ**
- **Căn cứ**: TT 31/2025 Đ10 + PL III (22 hoạt chất trị sốt rét, lao, HIV; mục 23 "thuốc … quản lý đặc biệt trong đó có yêu cầu hạn chế bán lẻ"; ghi chú: chỉ áp dụng khi chỉ định trên đơn đúng cột "Hạn chế bán lẻ đối với các chỉ định được ghi trên đơn thuốc"); Đ10 k3 (Sở Y tế có thể cho phép bán một số thuốc); NĐ 90 Đ59 k4 d.
- **Áp dụng cho**: nhà thuốc · **Mức**: BẮT BUỘC
- **Phần mềm phải**: cờ hạn chế bán lẻ theo hoạt chất + chỉ định; chặn bán khi chỉ định trên đơn trùng danh mục, trừ khi cấu hình văn bản cho phép của Sở Y tế (số, ngày, phạm vi).

**DUOC-R29. Bán thuốc qua thương mại điện tử**
- **Căn cứ**: Luật Dược Đ6 k17–19 (bổ sung bởi Luật 44 Đ1 k3 d: cấm bán lẻ TMĐT thuốc kê đơn trừ cách ly y tế dịch nhóm A, thuốc kiểm soát đặc biệt, thuốc hạn chế bán lẻ; cấm kinh doanh qua phương tiện không phải sàn, app, website TMĐT có chức năng đặt hàng); Đ42 k4 (bổ sung bởi Luật 44 Đ1 k18 c: bảo mật thông tin người mua, đăng tải GCN, CCHN, thông tin thuốc, thông báo trước cho cơ quan, tư vấn trực tuyến); NĐ 163 Đ41 (gốc-OCR: thông tin bắt buộc đăng tải; thông tin thuốc trên chuyên mục riêng), Đ42 k2 (bao bì giao hàng ghi tên, địa chỉ, SĐT khách và SĐT người tư vấn); GPP PL I-1a III.2 d (tư vấn trực tuyến bằng âm thanh, video, tin nhắn; phần mềm bán hàng ghi nhận liên lạc người mua, tóm tắt tư vấn; "lưu bằng chứng … ít nhất 24 tháng"); NĐ 90 Đ59 k3 m, k4 i–l.
- **Áp dụng cho**: nhà thuốc/chuỗi bán online, nền tảng · **Mức**: BẮT BUỘC
- **Phần mềm phải**: chặn đưa vào giỏ hàng online các mã có cờ kê đơn, KSĐB, hạn chế bán lẻ (công tắc riêng cho tình huống dịch nhóm A); bắt buộc hoàn tất phiên tư vấn trước khi chốt đơn; lưu bản ghi tư vấn ≥ 24 tháng; in nhãn giao hàng đủ trường.

**DUOC-R30. Theo dõi thuốc kiểm soát đặc biệt bằng sổ hoặc phần mềm**
- **Căn cứ**: NĐ 163 Đ31 k8 b (gốc-OCR: cơ sở bán lẻ thuốc gây nghiện, hướng thần, tiền chất có "hệ thống quản lý, theo dõi bằng hồ sơ sổ sách theo quy định của Bộ trưởng"), k9 (dạng phối hợp: "theo dõi bằng hệ thống phần mềm hoặc hồ sơ, sổ sách"), k10 (bán lẻ thuốc phóng xạ: khu vực riêng, hồ sơ sổ sách), k13 (thuốc độc, thuốc cấm dùng trong một số ngành: phần mềm hoặc hồ sơ, sổ sách toàn bộ xuất, nhập, tồn); GPP II.4 đ (dẫn Đ43 NĐ 54/2017, nay áp NĐ 163 theo Đ15a TT 02).
- **Áp dụng cho**: nhà thuốc kinh doanh KSĐB · **Mức**: BẮT BUỘC
- **Phần mềm phải**: sổ theo dõi KSĐB riêng theo từng hoạt chất/lô, in được dạng sổ; khóa sửa xóa; đối chiếu tồn thực tế.

### C. Dữ liệu chủ (master data) thuốc

**DUOC-R31. Phân loại thuốc theo số đăng ký**
- **Căn cứ**: TT 32/2026 Đ12 k4 (mỗi hồ sơ một số đăng ký theo PL V; "nhằm mục đích tra cứu, tổng hợp và thống kê dữ liệu"), PL V: 12 chữ số = mã nước sản xuất (3, theo GS1 prefix) + nhóm thuốc (1: 1 hóa dược, 2 dược liệu, 3 vắc xin, 4 sinh phẩm, 5 nguyên liệu) + phân loại kê đơn (1: 0 không kê đơn, 1 kê đơn) + phân loại KSĐB (1: 0 không, 1 gây nghiện, 2 hướng thần, 3 tiền chất, 4 độc, 5 cấm dùng cho các bộ ngành, 6 phóng xạ) + số thứ tự (4) + năm cấp (2); Đ52 k4 (thuốc cấp trước 01/01/2023: ghi số đăng ký theo cấu trúc mới chậm nhất 12 tháng sau gia hạn), k5 (thuốc đã phân loại kê đơn/không kê đơn không phải phân loại lại).
- **Áp dụng cho**: vendor, nhà thuốc, khoa dược · **Hiệu lực**: 01/10/2026 · **Mức**: NÊN (dùng để tự gắn cờ); dữ liệu gốc vẫn phải đối chiếu công bố của Cục QLD
- **Phần mềm phải**: parse SĐK 12 số để đề xuất cờ kê đơn/KSĐB, nhưng ưu tiên dữ liệu công bố; hỗ trợ đồng thời số đăng ký kiểu cũ.
- **Ghi chú / bẫy**: ghi chú (1) PL V: các giá trị "có thể phát sinh" nên không hard-code enum đóng.

**DUOC-R32. Kiểm soát thuốc theo danh mục đặc biệt khi kê**
- **Căn cứ**: TT 26 Đ3, Đ6 k6–7, Đ7–9; TT 55 Đ8 k5 đ (dược liệu độc); NĐ 163 Đ29 (danh mục nguyên liệu phóng xạ) — gốc-OCR.
- **Áp dụng cho**: cơ sở KCB · **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục thuốc nội bộ có các cờ: gây nghiện, hướng thần, tiền chất, phối hợp chứa GN/HT/TC, độc, phóng xạ, dược liệu độc, hạn chế bán lẻ, OTC; mỗi cờ điều khiển loại đơn, giới hạn ngày, quy tắc ghi số lượng và kênh bán.
- **Ghi chú / bẫy**: TT 26 **không có điều riêng về kê đơn thuốc phóng xạ**; thuốc phóng xạ chủ yếu xuất hiện ở NĐ 163 (Đ31 k10, Đ35) và TT 20/2017 sửa bởi TT 27/2024 (báo cáo, cung cấp tại cơ sở KCB).

### D. Thực hành tốt (không phải luật)

**DUOC-R33. Nhật ký truy vết toàn bộ vòng đời đơn**
- **Căn cứ**: không có điều luật trực tiếp cho phần mềm cơ sở; QĐ 425 Đ9 k1 a chỉ áp với tài khoản quản trị trên Hệ thống QG ("phải được ghi nhật ký trên hệ thống để có thể theo dõi, giám sát và truy cứu trách nhiệm").
- **Mức**: NÊN
- **Phần mềm phải**: log bất biến cho tạo, ký, gửi, thay thế, hủy, xem đơn (ai, khi nào, từ đâu); giữ log bằng thời hạn lưu đơn.

**DUOC-R34. Cảnh báo tương tác, dị ứng, liều theo cân nặng**
- **Căn cứ**: TT 26 Đ4 k1 (kê đơn phù hợp tờ HDSD, hướng dẫn chẩn đoán điều trị, Dược thư); NĐ 90 Đ41 k2 c (phạt kê không phù hợp tờ HDSD, HDCĐĐT, Dược thư: 10–20 triệu).
- **Mức**: NÊN (công cụ hỗ trợ; nghĩa vụ phù hợp tài liệu là của người kê)
- **Phần mềm phải**: CDSS cảnh báo liều tối đa, tương tác, chống chỉ định; trẻ < 72 tháng dùng cân nặng bắt buộc để tính liều.

---

**Tổng hợp mức** (tính theo mức chính của mỗi mục; R12, R15, R17, R23, R26 có phần phụ BẮT BUỘC? ghi trong mục): **BẮT BUỘC 29** (R01–R12, R14–R20, R22–R30, R32) · **BẮT BUỘC? 2** (R13, R21) · **NÊN 3** (R31, R33, R34). Tổng 34 mục.

---

## 3. Pattern thiết kế

**P1. Đơn thuốc bất biến có chuỗi thay thế** (R09, R11, R12, R15)
- Bảng `prescription(id, rx_code UNIQUE, facility_code, prescriber_id, patient_id, encounter_id, type CHECK IN ('C','N','H','T'), status CHECK IN ('draft','signed','sent','superseded','cancelled'), replaces_id FK NULL, issued_at, valid_until, payload_canonical JSONB, payload_hash, signature_blob, signed_at, sent_at, national_ack_id)`; `prescription_item(...)`.
- Sau `signed`: trigger/policy chặn UPDATE các cột nội dung; sửa = INSERT bản mới với `replaces_id`, bản cũ chuyển `superseded`.
- Đánh đổi: tăng số bản ghi; đổi lại có bằng chứng pháp lý và khớp QĐ 425 Đ9 k3 c.

**P2. Bộ sinh mã đơn** (R04)
- `rx_code = facility5 + random7([0-9a-z], CSPRNG) + '-' + type`; ràng buộc `UNIQUE(facility_code, substring(rx_code,6,7))`; retry khi trùng; regex kiểm tra `^[0-9A-Za-z]{5}[0-9a-z]{7}-[NHCT]$` (bộ ký tự 5 ký tự đầu cần xác nhận theo QĐ 384).
- Không dùng sequence (vi phạm "giá trị ngẫu nhiên" và lộ lưu lượng).

**P3. Rule engine kê đơn theo dữ liệu chủ có phiên bản** (R05, R06, R07, R16, R17, R32)
- Bảng `drug_master(… inn, brand, ingredient_count, rx_flag, control_class, is_poison, is_radioactive, herbal_toxic, restricted_retail, reg_no, reg_no_parsed …, valid_from, valid_to)`; `long_term_icd10(code, source='TT26-PLVII', version)`.
- Hàm `max_days(drug, icd10, acute)` trả 7/10/30/90 (+ quy tắc YHCT); validate khi ký. Lưu `ruleset_version` vào đơn để audit.

**P4. Outbox gửi Hệ thống đơn thuốc QG** (R12, R13, R14)
- Bảng `outbox(id, aggregate='prescription', aggregate_id, endpoint, spec_version, payload, attempt, next_retry_at, status, last_error, created_at)`; worker gửi ngay sau commit, backoff có trần; dashboard "đơn chưa gửi > N phút".
- Event `encounter.closed` hoặc `discharge.requested` kích hoạt gửi; xuất viện chờ ack (cấu hình).
- Đánh đổi: thêm hạ tầng hàng đợi; đổi lại không mất đơn khi mạng hoặc hệ thống QG lỗi.

**P5. Workflow thuốc kiểm soát đặc biệt** (R07, R08, R18, R19, R30)
- Bảng `narcotic_commitment(patient_id, form='PL-IV', signed_at, file_ref)`, `commune_confirmation(id, prescription_id UNIQUE, form='PL-V')` (một xác nhận cho một đơn), `sample_signature(prescriber_id, image_ref, valid_from)`, `controlled_return(id, rx_id, lot_id, qty, form='PL-VI'|'PL-XX', quarantine_location)`.
- In 3 bản có watermark "Bản lưu cơ sở KCB / Bản lưu HSBA / Bản giao nơi bán".

**P6. Bán lẻ theo đơn điện tử** (R16, R22, R23, R24, R27)
- Bảng `erx_snapshot(rx_code PK, fetched_at, payload JSONB, valid_until, status)` lấy qua API QĐ 228; `dispense(id, rx_code FK, pharmacist_id, substituted BOOL, consent_ref)`, `dispense_line(prescribed_drug_code, dispensed_drug_code, lot_id, qty)`; ràng buộc tổng `qty` theo `prescribed_drug_code` ≤ số lượng kê.
- Outbox gửi `cap-nhat-don-thuoc` ngay sau thanh toán.

**P7. Sổ cái kho theo lô, đồng bộ CSDL dược** (R25, R26, R30, R19)
- Bảng `stock_movement(id, ts, facility_id, drug_id, lot_no, expiry_date, qty_signed, movement_type, counterparty_id, source_doc, price, gtin)`, append-only; tồn = SUM. `movement_type` ánh xạ 1-1 sang loại giao dịch QĐ 232; `national_sync(movement_id, status, sent_at, remote_id)`.
- Job backfill từ 01/01/2026; báo cáo KSĐB (Mẫu 06 NĐ 163, PL X TT 27/2024) sinh từ sổ cái.
- Đánh đổi: append-only khó "sửa nhầm"; dùng bút toán đảo có lý do.

**P8. Lưu trữ và hủy có kiểm soát** (R15, R27)
- Bảng `retention_policy(doc_type, min_years, anchor CHECK IN ('issued_at','lot_expiry','last_encounter'))`; `legal_hold`; `destruction_batch(id, council_decision_ref, members, minutes_file, executed_at)`.
- File ký số và PDF đơn lưu trên kho WORM/khóa đối tượng; xóa chỉ qua `destruction_batch`.

**P9. Kênh giao mã đơn cho người bệnh** (R14, R21)
- Bản in có QR chứa `rx_code`; SMS/app chỉ gửi mã và link tra cứu, không gửi chẩn đoán; lưu `delivery_log(rx_code, channel, sent_at, status)`.

**P10. Nhật ký tư vấn TMĐT** (R29)
- Bảng `online_consult(order_id, buyer_contact, channel, summary, media_ref, pharmacist_id, created_at)`; retention 24 tháng; order không chuyển sang "confirmed" nếu thiếu consult.

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| DUOC-A01 | R01 | Đăng nhập tài khoản điều dưỡng/dược sĩ thử tạo và ký đơn; với YHCT thử y sĩ YHCT kê hóa dược | Ảnh màn hình bị chặn; cấu hình quyền | Bắt buộc |
| DUOC-A02 | R02 | Truy vấn bảng nhân sự: mỗi người kê có đúng 1 mã liên thông; mở 10 đơn đã gửi xem có mã | Kết quả SQL; payload gửi | Bắt buộc |
| DUOC-A03 | R03 | Tạo đơn cho trẻ 3 tuổi bỏ trống cân nặng; in đơn so với PL I/II/III TT 26 | Thông báo lỗi; bản in | Bắt buộc |
| DUOC-A04 | R04 | `SELECT rx_code FROM … WHERE rx_code !~ '^.{5}[0-9a-z]{7}-[NHCT]$' OR length(rx_code)<>14`; kiểm tra phần y có tăng dần không | Kết quả truy vấn; mẫu 100 mã | Bắt buộc |
| DUOC-A05 | R05 | Kê 1 thuốc độc + 2 thuốc thường, số lượng 5, 1 thuốc gây nghiện; xem bản in | Bản in: thuốc độc đứng đầu, "05", số bằng chữ cho N | Bắt buộc |
| DUOC-A06 | R03, R05 | Thử thêm thực phẩm chức năng vào đơn | Bị chặn | Bắt buộc |
| DUOC-A07 | R06 | Kê 60 ngày với ICD ngoài PL VII; kê N cấp tính 10 ngày; kê H cấp tính 15 ngày | Bị chặn/cảnh báo cứng | Bắt buộc |
| DUOC-A08 | R07 | Ở cơ sở không giường bệnh thử tạo đơn N; tạo đơn lẫn thuốc N và C | Bị chặn hoặc tự tách đơn | Bắt buộc |
| DUOC-A09 | R08 | Tạo đơn N không có cam kết PL IV; dùng một xác nhận PL V cho 2 đơn | Bị chặn | Bắt buộc |
| DUOC-A10 | R09 | Sửa đơn đã gửi; kiểm tra DB có UPDATE nội dung không (xem audit/trigger) | Đơn mới mã mới + liên kết; đơn cũ "superseded" | Bắt buộc |
| DUOC-A11 | R10 | So sánh y lệnh HSBA với đơn cùng lượt trên 20 hồ sơ | Bảng đối chiếu | Bắt buộc |
| DUOC-A12 | R11 | Mở file đơn đã ký, xác thực chữ ký, kiểm tra chứng thư thuộc người kê hoặc người chịu trách nhiệm chuyên môn | Kết quả verify | Bắt buộc |
| DUOC-A13 | R12 | `SELECT percentile(sent_at - encounter_closed_at)`; đếm đơn chưa gửi; kiểm tra luồng ra viện | Thống kê độ trễ; danh sách lỗi | Bắt buộc |
| DUOC-A14 | R13 | Đọc tài liệu tích hợp của vendor: phiên bản đặc tả (QĐ 808 hoặc mới hơn) | Tài liệu, log | Bắt buộc? |
| DUOC-A15 | R14 | Hỏi quy trình giao mã đơn; xem log gửi SMS/app | delivery_log | Bắt buộc |
| DUOC-A16 | R15 | Xem cấu hình retention; thử xóa đơn cũ bằng UI và API; xuất đơn theo người bệnh/khoảng thời gian | Cấu hình; kết quả xóa bị chặn; file xuất | Bắt buộc |
| DUOC-A17 | R16 | Nhà thuốc: quét đơn kê 6 ngày trước | Bị chặn | Bắt buộc |
| DUOC-A18 | R17 | Tạo đơn thuốc thang có vị < 10 g, vị chế từ dược liệu độc, vượt liều | Bản in "08 g", số + chữ, "tôi kê liều này"; mã đuôi T | Bắt buộc |
| DUOC-A19 | R18 | Tạo phiếu nhận lại thuốc N; kiểm tra tồn có cộng vào kho bán không | Biên bản PL VI/PL XX; kho biệt trữ | Bắt buộc |
| DUOC-A20 | R19 | Sinh báo cáo KSĐB kỳ gần nhất, đối chiếu với sổ cái | Báo cáo + truy vấn đối chiếu | Bắt buộc |
| DUOC-A21 | R20 | Cấp phát lô hết hạn hoặc lô bị thu hồi | Bị chặn; log người cấp, thời gian | Bắt buộc |
| DUOC-A22 | R21 | Kiểm tra mã hóa trường CCCD/BHYT ở DB; đơn HIV có cờ ẩn danh; chính sách mật khẩu | Schema, cấu hình | Bắt buộc? |
| DUOC-A23 | R22 | Bán thuốc kê đơn không có mã đơn; bán thuốc N với đơn C | Bị chặn | Bắt buộc |
| DUOC-A24 | R23 | Bán vượt số lượng; bán đơn đã bị thay thế; xem log gọi API cập nhật bán | Bị chặn; log API | Bắt buộc |
| DUOC-A25 | R24 | Nhân viên không phải dược sỹ thử thay thuốc | Bị chặn; bản ghi đồng ý | Bắt buộc |
| DUOC-A26 | R25 | Chọn 1 lô, truy từ hóa đơn nhập tới từng giao dịch bán; xuất toàn bộ dữ liệu XNT | Báo cáo truy vết; file xuất | Bắt buộc |
| DUOC-A27 | R26 | Kiểm tra tài khoản csdlduoc của cơ sở; tỷ lệ bút toán đã đồng bộ từ 01/01/2026; có backfill | Ảnh tài khoản; thống kê sync | Bắt buộc |
| DUOC-A28 | R27 | Kiểm tra đơn N/H đã bán có ảnh/bản chính; retention ≥ 1 năm sau hạn dùng | Mẫu hồ sơ; cấu hình | Bắt buộc |
| DUOC-A29 | R28 | Bán Isoniazid với chỉ định "điều trị lao" trên đơn | Bị chặn (trừ khi có văn bản Sở Y tế) | Bắt buộc |
| DUOC-A30 | R29 | Thêm thuốc kê đơn vào giỏ online; chốt đơn online không có tư vấn; tìm bản ghi tư vấn 20 tháng trước | Bị chặn; bản ghi tư vấn | Bắt buộc |
| DUOC-A31 | R30 | In sổ KSĐB; thử xóa một dòng | Sổ in; bị chặn | Bắt buộc |
| DUOC-A32 | R31, R32 | Kiểm tra master thuốc: tỷ lệ mã có cờ kê đơn/KSĐB; parse SĐK 12 số | Thống kê master data | Nên / Bắt buộc |
| DUOC-A33 | R33 | Xem log vòng đời 5 đơn | Log | Nên |
| DUOC-A34 | R34 | Kê liều vượt tối đa theo cân nặng | Cảnh báo | Nên |

---

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái (so với 05/10/2026) | Nội dung | Ai phải làm | Căn cứ |
|---|---|---|---|---|
| 01/04/2022 | Đã qua | QĐ 808/QĐ-BYT hướng dẫn kết nối Hệ thống đơn thuốc QG | Vendor HIS/PK | QD-808 (thứ cấp) |
| 03/04/2023 | Đã qua | Chuẩn kết nối nhà thuốc ↔ đơn thuốc QG (API lấy đơn, cập nhật bán) | Vendor nhà thuốc | QĐ 228/QĐ-QLD |
| 30/01/2025 | Đã qua | TT 27/2024 sửa TT 20/2017 có HL (báo cáo KSĐB trước 15/01) | Cơ sở KCB, nhà thuốc | TT 27/2024 (ngày HL: thứ cấp) |
| 05/02/2025 | Đã qua | Quy chế Hệ thống đơn thuốc QG | Cơ sở KCB, nhà thuốc | QĐ 425 |
| 01/07/2025 | Đã qua | TT 26 HL (mẫu đơn mới, mã đơn); NĐ 163, TT 31 HL; TT 11/2025 (GPP sửa: phần mềm, TMĐT, e-Rx tại nhà thuốc); Luật 44 HL | Tất cả | TT 26 Đ13 k1; NĐ 163 Đ129; TT 11 Đ5 k1 |
| trước 01/10/2025 | Đã qua (hạn chót) | Bệnh viện kê đơn điện tử | BV công, BV tư | TT 26 Đ13 k3 a |
| trước 01/01/2026 | Đã qua (hạn chót) | Cơ sở KCB khác (PK…) kê đơn điện tử | PK, cơ sở khác | TT 26 Đ13 k3 b |
| 01/01/2026 | Đã qua | Nhà thuốc, quầy thuốc, bán buôn liên thông dữ liệu với hệ thống thông tin về dược; dữ liệu tính từ mốc này | Nhà thuốc, quầy, bán buôn | TT 11/2025 Đ5 k2; CV 934 (thứ cấp) |
| 15/01 hằng năm | Định kỳ | Báo cáo năm XNT thuốc KSĐB (cơ sở KCB gửi Sở Y tế; nhà thuốc gửi UBND tỉnh) | Cơ sở KCB, nhà thuốc | TT 27/2024 Đ1 k5; NĐ 163 Đ35 k2 |
| 15/7 hằng năm | Định kỳ | Báo cáo 6 tháng KSĐB | Nhà thuốc, bán buôn, chuỗi | NĐ 163 Đ35 k2 a |
| 01/03/2026 | Đã qua | TT 55 (YHCT) HL; e-Rx YHCT theo lộ trình chưa định ngày | Cơ sở YHCT | TT 55 Đ12 |
| 15/05/2026 | Đã qua | NĐ 90 (xử phạt) HL | Tất cả | NĐ 90 |
| 24/06/2026 | Đã qua | Kế hoạch triển khai Hệ thống CSDL về dược | XNK, bán buôn, bán lẻ, chuỗi | QĐ 1867 (thứ cấp) |
| 30/06/2026 | Đã qua | Hết thời gian dùng mẫu đơn thuốc thang in theo TT 44/2018 | Cơ sở YHCT | TT 55 Đ14 |
| 17/07/2026 | Đã qua | Đặc tả API Hệ thống CSDL về dược v1.1 | Vendor | QĐ 232 (thứ cấp) |
| 12/08/2026 | Đã qua | Hướng dẫn kết nối, xác thực VNeID, dữ liệu hồi tố từ 01/01/2026 | Bán buôn, bán lẻ | CV 934 (thứ cấp) |
| 19/08/2026 | Đã qua | Bãi bỏ điểm đ k1 Đ5 TT 02/2018 (bản tự kiểm tra GPP trong hồ sơ) | Nhà thuốc (thủ tục) | QĐ 2656 |
| 01/10/2026 | Đã qua (4 ngày) | TT 32/2026 HL: cấu trúc số đăng ký 12 chữ số, tiêu chí OTC; TT 12/2025 hết HL | Vendor master data, nhà thuốc | TT 32/2026 Đ52 |
| 04/10/2026 | Đã qua (hôm qua) | Hạn đăng ký tài khoản Hệ thống CSDL về dược | Theo CV 3656 (thứ cấp) | CV 3656 |
| 01/07/2027 | Sắp tới | BYT triển khai hệ thống phần mềm quản lý trực tuyến XNK thuốc; đổi nơi tiếp nhận báo cáo XNK | Cơ sở SX, XNK | NĐ 163 Đ124, Đ130 k3 (gốc-OCR) |
| Thường xuyên | — | Gửi đơn ngay sau khám (ngoại trú), trước ra viện (nội trú); nhà thuốc báo cáo đơn đã bán ngay sau bán; báo cáo nhầm lẫn/thất thoát KSĐB trong 48 giờ | Cơ sở KCB, nhà thuốc | TT 26 Đ12 k6 d; QĐ 425 Đ9 k3; NĐ 163 Đ35 k4 |

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuỗi thay thế**
| Cũ | → | Mới | Từ ngày | Ghi chú |
|---|---|---|---|---|
| TT 52/2017, 18/2018, 04/2022, 27/2021 (BYT) | → | TT 26/2025 | 01/07/2025 | TT 26 Đ13 k2 |
| TT 44/2018 (YHCT) | → | TT 55/2025 | 01/03/2026 | Mẫu cũ đã in dùng đến 30/06/2026 |
| TT 53/2017 (thời hạn bảo quản) | → | TT 33/2025 | 01/07/2025 | TT 26 Đ11 vẫn dẫn TT 53 |
| NĐ 54/2017, NĐ 88/2023 | → | NĐ 163/2025 | 01/07/2025 | GPP II.4 đ vẫn dẫn "Điều 43 NĐ 54" → áp NĐ 163 (Đ15a TT 02) |
| TT 07/2018 (kinh doanh dược) | → | TT 31/2025 | 01/07/2025 | TT 31 Đ25 k2 |
| TT 12/2025 (đăng ký thuốc) | → | TT 32/2026 | 01/10/2026 | TT 32 Đ52 k2 a |
| NĐ 117/2020 | → | NĐ 90/2026 | 15/05/2026 | |
| QĐ 540/QĐ-QLD (Bảng 3), QĐ 777/QĐ-QLD (mục 2–4, 5.2) (2018) | → | QĐ 228/QĐ-QLD | 03/04/2023 | Chuẩn kết nối nhà thuốc |
| QĐ 330/QĐ-QLD (2019) | → | QĐ 318/QĐ-QLD | 04/06/2021 | Chuẩn kết nối cơ sở phân phối |
| Điểm đ k1 Đ5 TT 02/2018 | → bãi bỏ | QĐ 2656/QĐ-BYT | 19/08/2026 | Nội dung bị bãi bỏ: "Bản tự kiểm tra Thực hành tốt cơ sở bán lẻ thuốc theo Danh mục kiểm tra" trong tài liệu kỹ thuật của hồ sơ. **Không** liên quan yêu cầu phần mềm; căn cứ là Kết luận kiểm tra 5614/KL-BTP |

**Bẫy trích dẫn**
1. **Thời hạn lưu đơn thuốc (câu hỏi mở 7 / MT-34)**: TT 26 Đ11 k1 dẫn TT 53/2017 đã hết HL; theo Đ14 TT 26 phải áp TT 33/2025. TT 55 Đ11 k2 dẫn "điểm a khoản 2 Điều 1 TT 33", nhưng điểm này chỉ nói Phụ lục áp dụng cho tài liệu giấy, vật mang tin và điện tử, **không nêu số năm**. Phụ lục TT 33 không có dòng "đơn thuốc". Theo TT 33 Đ1 k2 b, loại chưa quy định thì cơ sở tự xác định thời hạn tương đương nhóm tương ứng, không thấp hơn mức của Phụ lục. **Kết luận làm việc (suy luận, cần xác nhận với BYT)**: (a) đơn gắn với HSBA (Đ5 k1 b, k2 a TT 26; bản đơn "N" lưu trong HSBA theo Đ7 k1) theo dòng 44: **10 năm** (hoặc theo dòng 39–43 nếu HSBA tử vong 30 năm, tâm thần 20 năm…); (b) đơn ngoại trú không có HSBA: tối thiểu dòng 47 "sổ, sách phục vụ công tác KCB" **05 năm**, khuyến nghị 10 năm để thống nhất; (c) nhà thuốc: GPP II.4 d **≥ 1 năm kể từ khi thuốc hết hạn dùng** (quy định riêng, còn HL); bằng chứng tư vấn TMĐT ≥ 24 tháng. Phần mềm nên để retention cấu hình được, mặc định ≥ 10 năm cho cơ sở KCB.
2. **Ngày của QĐ 808/QĐ-BYT**: luatvietnam ghi 01/04/2022; QĐ 228/QĐ-QLD (ký 03/04/2023) dẫn "Quyết định số 808/QĐ-BYT ngày 01/04/2022"; QĐ 425/QĐ-BYT Đ9 k2 lại ghi "ngày 01/4/2023" (gốc-OCR). Hai nguồn độc lập cho 2022, nên khả năng cao QĐ 425 ghi nhầm năm. Inventory (QD-808-2023-BYT) đang dùng năm sai, nên đổi ID thành QD-808-2022-BYT.
3. **QĐ 425 dẫn chiếu văn bản đã hết hiệu lực**: TT 27/2021, TT 04/2022 (→ TT 26/2025), TT 46/2018 (→ TT 13/2025), NĐ 13/2023 (→ NĐ 356/2025), NĐ 85/2016 (→ NĐ 331/2026, xem cụm K9), TT 05/2016 (Đ3 k1). Khi trích QĐ 425 phải ghi rõ văn bản thay thế.
4. **"14 ký tự" đã gồm dấu "-"**: 5 + 7 + 1 + 1 = 14. Nhiều tài liệu vendor hiểu nhầm thành 14 ký tự + dấu gạch.
5. **Ký tự loại đơn trong TT 55**: PL I (đơn thang) z = T. PL II (đơn cổ truyền, dược liệu) chép lại đúng chú thích "T: Đơn thuốc thang", không có ký tự riêng. Không tự chế ký tự mới; xem §7.
6. **Phạm vi TT 26 là ngoại trú** (kể cả đơn ra viện, Đ5 k2). Kê thuốc nội trú theo TT 23/2011 (TT 55 Đ3 k6). Nghĩa vụ gửi "bảng tổng hợp thuốc nội trú" chỉ có trong QĐ 425 Đ9 k3 a, Đ10 k2 (dẫn TT 27/2021 đã hết HL).
7. **Phòng khám không giường bệnh không dùng mẫu đơn "N"** (TT 26 Đ7 k1: đơn N dùng "tại cơ sở khám bệnh, chữa bệnh có giường bệnh"). Kê giảm đau gây nghiện cho người bệnh ung thư tại nhà cũng phải do bác sỹ cơ sở có giường nội trú (Đ8 k2 a).
8. **MT-32 đã phân xử**: nghĩa vụ liên thông của nhà thuốc nằm ở **văn bản QPPL** là TT 02/2018 PL I-1a/1b II.4 c sửa bởi TT 11/2025 Đ1 k7, với mốc 01/01/2026 tại TT 11/2025 Đ5 k2, và có căn cứ luật ở Luật Dược Đ74 k2 (sửa bởi Luật 44). NĐ 163 không chứa nghĩa vụ này (chỉ có Đ31 về sổ/phần mềm KSĐB). Các công văn 934, 3656 và QĐ 1867, 232 chỉ là hướng dẫn triển khai. Phần "liên thông với hệ thống thuế" **không có** trong TT 11/2025.
9. **NĐ 90 Đ59 k2 điểm d** (câu hỏi mở 4): khoản 2 có các điểm a, b, c, d; OCR không dấu nên "d" và "đ" có thể lẫn, cần đối chiếu bản có dấu. Nội dung phục dựng từ OCR (gốc-OCR, cần đối chiếu bản có dấu): "Không có thiết bị công nghệ thông tin kết nối internet và thực hiện quản lý hoạt động mua, bán thuốc bằng phần mềm ứng dụng hoặc không bảo đảm kiểm soát xuất xứ, giá cả, nguồn gốc thuốc mua vào, bán ra hoặc không đảm bảo truy xuất được nguồn gốc thuốc hoặc không bảo đảm trích xuất đầy đủ dữ liệu các thông tin trên khi cơ quan quản lý yêu cầu hoặc không liên thông và cập nhật đầy đủ dữ liệu với hệ thống thông tin về dược theo hướng dẫn của Bộ Y tế" — phạt 3–5 triệu (cá nhân; tổ chức gấp 02 lần theo Đ4 k5). Câu chữ gần như sao nguyên GPP II.4 c.
10. **CV 3656/QLD-KD**: inventory ghi chung "đăng ký trước 04/10/2026". Theo tóm tắt luatvietnam, đối tượng chính là cơ sở SX, XNK, dịch vụ bảo quản, kinh doanh nguyên liệu; bán buôn/bán lẻ do Sở Y tế phê duyệt tài khoản. Cần bản gốc để chốt nhà thuốc có cùng hạn này không.
11. **ID "QD-232-TTYQG" và "QD-1867-BYT"**: ngày ban hành lần lượt 17/07/2026 và 24/06/2026 (thứ cấp), bổ sung vào inventory.
12. **TT 32/2026 thay TT 12/2025 từ 01/10/2026**: tài liệu nói "TT 12/2025 quy định số đăng ký/OTC" đã lỗi thời. Thông tin thứ cấp "TT 12/2025 thay TT 07/2017 (danh mục thuốc không kê đơn)" chưa xác minh.
13. **Phụ lục VII TT 26 có mã "Z69.64", "Z69.65"** cho thay khớp háng, gối, khác mã ICD-10 thông dụng (suy luận: lỗi in). Nạp nguyên văn và ghi chú.

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Thời hạn lưu đơn thuốc tại cơ sở KCB**: không có con số trực tiếp (xem §6 bẫy 1). Hỏi Văn phòng Bộ Y tế (đơn vị soạn TT 33) hoặc Cục QLKCB. Đồng thời tìm nội dung TT 53/2017 cũ (chưa mở được bản gốc) để biết thời hạn đã "xác định trước" theo TT 33 Đ2 k3.
2. **Đặc tả kết nối Hệ thống đơn thuốc QG hiện hành**: QĐ 808/2022 mới đọc qua thứ cấp; chưa thấy văn bản của Cục KHCN&ĐT theo TT 26 Đ12 k3 a. Chưa thấy "tiêu chí kỹ thuật hạ tầng CNTT" theo TT 26 Đ12 k6 c.
3. **Quan hệ giữa các chuẩn của Cục QLD (540, 777/2018; 318/2021; 228/2023) và QĐ 232/QĐ-TTYQG (2026)**: còn song song hay đã bị thay. Hệ thống "Cổng dược quốc gia" cũ và csdlduoc.com.vn có hợp nhất không. Cần bản gốc QĐ 1867, QĐ 232, CV 934, CV 3656 (hiện chỉ thứ cấp).
4. **Mốc bắt buộc e-Rx YHCT**: TT 55 Đ12 k3 "theo lộ trình của Chính phủ và Bộ Y tế", chưa thấy văn bản lộ trình; trong khi Đ15 k3 d đã yêu cầu gửi đơn điện tử ngoại trú. Ký tự loại đơn cho đơn cổ truyền/dược liệu (PL II) chưa rõ. Hỏi Cục Quản lý Y, Dược cổ truyền.
5. **Đơn "N"/"H" điện tử có thay được bản giấy có dấu không** (TT 26 Đ7 k1, Đ9 k1 vs Đ10). Sổ theo dõi thuốc gây nghiện, hướng thần, tiền chất tại nhà thuốc có được thay hoàn toàn bằng phần mềm không (NĐ 163 Đ31 k8 b nói "hồ sơ sổ sách theo quy định của Bộ trưởng"; GPP 5.3.1 chấp nhận "máy tính"). Câu hỏi mở 6 của inventory chỉ giải quyết một phần.
6. **TT 20/2017 (gốc)**: chưa đọc bản gốc; chưa rõ thời hạn lưu giữ chứng từ thuốc KSĐB và thủ tục Hội đồng hủy tài liệu mà TT 26 Đ11 k2 dẫn chiếu. Tình trạng hiệu lực của TT 20 sau khi NĐ 54 hết hiệu lực cũng cần xác nhận (vẫn được TT 26, TT 55 dẫn chiếu).
7. **Chế tài khi không gửi đơn điện tử**: không tìm thấy điều riêng trong bản OCR không dấu của NĐ 90/2026 (đã tìm "đơn thuốc điện tử", "Hệ thống đơn thuốc"). Cần đọc bản có dấu hoặc hỏi luật sư; có thể rơi vào điều khoản chung về chuyên môn hoặc Đ39 k2 d ("không đáp ứng yêu cầu về CNTT triển khai HSBA điện tử").
8. **Quầy thuốc và e-Rx**: PL I-1b GPP không có điểm tương ứng III.2 đ của nhà thuốc. Nghĩa vụ báo cáo đơn đã bán của quầy thuốc chỉ suy ra từ TT 26 Đ12 k7 và QĐ 425 Đ20 k4.
9. **Kho thuốc tại cơ sở KCB** (TT 22/2011, TT 23/2011): chưa đọc; chưa xác định có yêu cầu phần mềm cụ thể. Cơ sở KCB có thuộc đối tượng liên thông Hệ thống CSDL về dược không: theo tóm tắt QĐ 1867 thì không (chỉ XNK, bán buôn, bán lẻ, chuỗi), cần bản gốc.
10. **Ngày hiệu lực TT 27/2024** (30/01/2025) và **danh mục thuốc không kê đơn hiện hành** (TT 07/2017 hay cơ chế công bố theo TT 12/2025 → TT 32/2026): mới có nguồn thứ cấp.
11. **QĐ 3176/QĐ-BYT (29/10/2024) và QĐ 384/QĐ-BYT (01/02/2019)**: quy tắc tạo mã người kê đơn và mã cơ sở (bộ ký tự 5 ký tự đầu của mã đơn), mới thấy qua dẫn chiếu trong QĐ 425 (gốc-OCR).
12. **Bản có dấu của NĐ 163/2025, NĐ 90/2026, QĐ 425/QĐ-BYT**: mọi câu chữ trích trong file này từ ba văn bản đó là phục dựng từ OCR không dấu. Trước khi đưa vào skill như trích dẫn nguyên văn phải OCR lại bằng `tesseract -l vie` hoặc lấy bản Word trên Công báo.
