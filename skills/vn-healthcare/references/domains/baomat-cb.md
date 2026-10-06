# BAOMAT-CB — Bảo mật chuyên biệt: dữ liệu có luật riêng, nhật ký truy cập HSBA, sinh trắc và chữ ký của người bệnh

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám, phòng xét nghiệm, cơ sở điều trị methadone, cơ sở IVF, ngân hàng mô, BV ghép tạng, vendor HIS/EMR/LIS/RIS/app · Research gốc: `research/deep/BAOMAT-CB.md`

Phạm vi: (1) dữ liệu có luật riêng về bảo mật hoặc chia sẻ: HIV/AIDS, điều trị thay thế (methadone) và xét nghiệm ma túy, tâm thần và bắt buộc chữa bệnh, hỗ trợ sinh sản và mang thai hộ, giới tính thai nhi, hiến ghép mô tạng, xác định lại giới tính, di truyền, bạo lực gia đình, trẻ em; (2) thời hạn lưu nhật ký truy cập HSBA; (3) sinh trắc, chữ ký của người bệnh; (4) rà soát docid còn sót. Domain này là **chủ** của các yêu cầu trên; DLCN-R31–R33, ANM-R11, EMR-R06/R22, SKDT-R19 chỉ dẫn chiếu sang đây cho phần chuyên biệt.

## Tóm tắt nhanh

- **HIV dương tính chỉ được thông báo cho danh sách đóng** của Luật HIV Đ30 (bản sửa bởi Luật 71/2020, 7 khoản). Thông báo sai đối tượng: 5–10 triệu; tiết lộ việc một người nhiễm HIV: 10–15 triệu; công khai tên, ảnh: 15–20 triệu (NĐ 90/2026, mức cá nhân, tổ chức ×2). Kết quả phải thông báo trong **72 giờ làm việc** (TT 04/2023 Đ3).
- **Giới tính thai nhi**: từ 01/07/2026 Luật Dân số Đ6 k3 cấm thông báo, tiết lộ (trừ danh mục BYT, chưa ban hành). Phần mềm siêu âm, NIPT phải che giới tính thai ở mọi kênh xuất.
- **IVF, mang thai hộ**: NĐ 207/2025 thay NĐ 10/2015 từ 01/10/2025; vô danh người hiến–người nhận, mỗi mẫu hiến chỉ cho một phụ nữ/một cặp, mã hóa và chia sẻ CSDL dùng chung (phạt 10–20 triệu nếu không mã hóa/không chia sẻ).
- **Hồ sơ ghép tạng lưu 30 năm** (Luật 75/2006 Đ38 k4), không phải 20 năm như TT 33/2025 mục 43. Thông tin người hiến, người được ghép phải mã hóa, chỉ cung cấp theo yêu cầu người đứng đầu cơ sở y tế (mục đích chữa bệnh) hoặc cơ quan tố tụng.
- **Methadone**: NĐ 141/2024 thay NĐ 90/2016 từ 15/12/2024; thông tin chỉ đi UBND xã qua Mẫu 11, 12, 14, 15, 16.
- **Nhật ký truy cập HSBA**: không có văn bản y tế riêng. Bắt buộc có log và lưu theo khung ANM (ANM-R11, khuyến nghị 12 tháng); **NÊN** lưu log truy cập từng HSBA bằng thời hạn HSBA đó, tối thiểu 05 năm (suy luận).
- **QCVN 16, 17:2026/BCA** (giọng nói, mống mắt; HL 15/04/2027) chỉ phục vụ CSDL căn cước, không áp cho ký xác nhận trên HSBA. Luật 20/2026/QH16 không sửa Đ22–23 Luật GDĐT.
- **Mốc tuổi khác nhau theo hành vi**: 7 (đồng ý của trẻ về đời tư), 12 (methadone cần đồng ý đại diện tới dưới 18), 15 (tự nguyện XN HIV), 18 (thông báo HIV cho cha mẹ sau trẻ). Không dùng một mốc "trẻ em" chung.

## Mục lục

**A. Khung chung**: R01 danh mục nhạy cảm, cờ mức bản ghi
**B. HIV**: R02 danh sách đóng được thông báo · R03 tiếp cận thông tin bằng văn bản · R04 Phiếu kết quả, 72 giờ làm việc · R05 luồng nội bộ, chuyển khoa · R06 người chưa thành niên · R07 HIV-INFO · R08 XN giấu tên
**C. Ma túy**: R09 methadone, Mẫu 11–16 · R10 XN ma túy, xác định nghiện
**D. Tâm thần**: R11 bắt buộc chữa bệnh; không có quy chế bảo mật riêng
**E. Sinh sản, giới tính thai**: R12 IVF, mang thai hộ · R13 giới tính thai nhi
**F. Ghép tạng**: R14 mã hóa, vô danh, hai kênh cung cấp · R15 lưu 30 năm
**G. Giới tính, di truyền**: R16 xác định lại giới tính · R17 dữ liệu di truyền
**H. BLGĐ, trẻ em**: R18 bạo lực gia đình · R19 trẻ em
**I. Cơ chế xuyên suốt**: R20 phá kính · R21 bộ lọc xuất theo đích
**J. Nhật ký**: R22 thời hạn lưu nhật ký truy cập HSBA
**K. Sinh trắc, chữ ký**: R23 QCVN sinh trắc BCA không áp · R24 xác thực VNeID khi ký · R25 lưu sinh trắc · R26 chữ ký số người bệnh, Luật 20/2026
**L. Rà soát docid**: R27 lực lượng thường trực ANM · R28 phân nhóm TBYT là phần mềm

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 64/2006/QH11 | Luật HIV: Đ4 k1 d, Đ8 k5, Đ25, Đ27, Đ28, Đ30 | 01/01/2007 | Còn HL; sửa bởi Luật 71/2020 | gốc | [VB 29395](https://vanban.chinhphu.vn/?pageid=27160&docid=29395) |
| 71/2020/QH14 | Sửa Luật HIV: Đ27 k2–3 (tuổi 15), Đ29, Đ30 mới | 01/07/2021 | Còn HL | gốc-OCR, đối chiếu ảnh trang | [VB 202612](https://vanban.chinhphu.vn/?pageid=27160&docid=202612) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2021/02/71.signed.pdf) |
| 04/2023/TT-BYT | Thông báo kết quả XN HIV dương tính, tiếp cận thông tin người nhiễm | 01/05/2023 | Còn HL; thay TT 02/2020 | gốc (đọc ảnh trang); không có trên vanban.chinhphu.vn | [Trang tulieuvankien](https://tulieuvankien.dangcongsan.vn/he-thong-van-ban/van-ban-quy-pham-phap-luat/thong-tu-so-042023tt-byt-ngay-28022023-cua-bo-y-te-ve-quy-dinh-hinh-thuc-quy-trinh-thong-bao-ket-qua-xet-nghiem-hiv-duong-9524) · [PDF](https://tulieuvankien.dangcongsan.vn/upload/3000006/20251024/5e25c5488424a8af36c535133a60fe9a04-BYT.pdf) |
| 07/2023/TT-BYT | Giám sát dịch tễ HIV/AIDS, hệ thống HIV-INFO | 01/06/2023 | Còn HL | gốc-OCR (Đ1–11) | [VB 207732](https://vanban.chinhphu.vn/?pageid=27160&docid=207732) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/4/07-byt.pdf) (khoảng 30 MB, vượt giới hạn tải của script kiểm link; đã mở tay 06/10/2026: PDF 29 trang) |
| 141/2024/NĐ-CP | Chi tiết Luật HIV: điều trị thay thế (Chương III), XN HIV | 15/12/2024 | Còn HL; thay NĐ 108/2007, NĐ 75/2016, NĐ 90/2016 | gốc | [VB 211553](https://vanban.chinhphu.vn/?pageid=27160&docid=211553) · [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-141-2024-nd-cp-43066.htm) |
| 10/2025/TT-BYT | Bãi bỏ VBQPPL về HIV (TTLT 03/2010, TT 04/2019, một phần TT 06/2012, TT 01/2015) | 09/05/2025 | Còn HL | gốc | [VB 213682](https://vanban.chinhphu.vn/?pageid=27160&docid=213682) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/10-byt.pdf) |
| 73/2021/QH14 | Luật Phòng, chống ma túy: Đ22, Đ26, Đ27 | 01/01/2022 | Còn HL | gốc | [VB 204940](https://vanban.chinhphu.vn/?pageid=27160&docid=204940) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2022/01/73luat.pdf) |
| 15/2023/QH15 (VBHN 26) | Luật KCB: Đ7 k10, k19; Đ10 k2; Đ13; Đ34 k1 d; Đ45 k5; Đ69; Đ82 | 01/01/2024; Đ34 k1 d từ 01/07/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 96/2023/NĐ-CP | Đ91–93 bắt buộc chữa bệnh | 01/01/2024 | Còn HL | gốc-OCR | [VB 209491](https://vanban.chinhphu.vn/?pageid=27160&docid=209491) |
| 114/2025/QH15 | Luật Phòng bệnh: Đ17 k1 c, Đ31–33 | 01/07/2026 | Còn HL | gốc | [VB 216498](https://vanban.chinhphu.vn/?pageid=27160&docid=216498) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat114-2025.pdf) |
| 207/2025/NĐ-CP | Hỗ trợ sinh sản, mang thai hộ: Đ3, Đ4, Đ8, Đ10, Đ12, Đ15–17 | 01/10/2025 | Còn HL; thay NĐ 10/2015, NĐ 98/2016; bãi bỏ NĐ 96 Đ40 k9 | gốc-OCR (đối chiếu lại Đ3, Đ8, Đ10, Đ15–17) | [VB 214619](https://vanban.chinhphu.vn/?pageid=27160&docid=214619) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/207-cp.signed.pdf) |
| 113/2025/QH15 | Luật Dân số: Đ6 k3, Đ15 k2, Đ21, Đ29 k4 | 01/07/2026 | Còn HL; Pháp lệnh Dân số hết HL | gốc | [VB 216497](https://vanban.chinhphu.vn/?pageid=27160&docid=216497) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat113-2025.pdf) |
| 75/2006/QH11 | Luật Hiến, lấy, ghép mô, bộ phận cơ thể: Đ4 k4, Đ11 k9, Đ36, Đ38 | 01/07/2007 | Còn HL; dự thảo sửa đổi đang thẩm tra | gốc | [VB 29735](https://vanban.chinhphu.vn/?pageid=27160&docid=29735) |
| Dự án Luật Hiến, lấy, ghép mô (sửa đổi) | 7 chương 39 điều | — | Thẩm tra 04/10/2026 | thứ cấp | [suckhoedoisong 04/10/2026 (báo, bối cảnh)](https://suckhoedoisong.vn/hoan-thien-khung-phap-ly-ve-hien-ghep-mo-tang-tang-bao-ve-nguoi-hien-169261004160641867.htm) |
| 13/2022/QH15 | Luật Phòng, chống bạo lực gia đình: Đ3, Đ9, Đ29, Đ34, Đ35, Đ37 | 01/07/2023 | Còn HL | gốc | [VB 207711](https://vanban.chinhphu.vn/?pageid=27160&docid=207711) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/4/luat13.pdf) |
| 102/2016/QH13 | Luật Trẻ em: Đ6 k11, Đ21, Đ51, Đ54 k2, Đ58 | 01/06/2017 | Còn HL; trong dự án sửa 6 luật (trình 10/2026) | gốc-OCR | [VB 184566](https://vanban.chinhphu.vn/?pageid=27160&docid=184566) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2016/05/102.signed.pdf) |
| 90/2026/NĐ-CP | Xử phạt y tế: Đ4, Đ18, Đ19, Đ38 k3 c, k5 a, Đ42 k3–4, Đ44, Đ45, Đ97–99 | 15/05/2026 | Còn HL; thay NĐ 117/2020 | gốc-OCR (đối chiếu lại mọi điều dẫn) | [VB 217386](https://vanban.chinhphu.vn/?pageid=27160&docid=217386) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| 356/2025/NĐ-CP | Đ4 k1 (danh mục DLCN nhạy cảm), k2 (phân quyền giới hạn) | 01/01/2026 | Còn HL | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/17/356signed-1768638052103952849513.pdf) |
| 169/2026/TT-BCA | QCVN 16:2026/BCA sinh trắc giọng nói (chỉ cho CSDL căn cước) | 15/04/2027 | Sắp HL | gốc-OCR | [VB 219782](https://vanban.chinhphu.vn/?pageid=27160&docid=219782) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/10/169-bca.signed.pdf) |
| 170/2026/TT-BCA | QCVN 17:2026/BCA sinh trắc mống mắt (chỉ cho CSDL căn cước) | 15/04/2027 | Sắp HL | gốc-OCR, đối chiếu ảnh trang 1 | [VB 219783](https://vanban.chinhphu.vn/?pageid=27160&docid=219783) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/10/170-bca.signed.pdf) |
| 117/2026/TT-BCA | Bảo vệ dữ liệu CSDL dân cư; 6 trường hợp khai thác sinh trắc | 01/07/2026 | Còn HL | thứ cấp (không thấy trên vanban) | [luatvietnam (thứ cấp)](https://luatvietnam.vn/tin-van-ban-moi/chi-duoc-phep-khai-thac-du-lieu-sinh-trac-hoc-cua-cong-dan-trong-6-truong-hop-tu-01-7-2026-186-110735-article.html) |
| 69/2024/NĐ-CP | Định danh, xác thực điện tử: Đ17 k2, Đ18, Đ19, Đ20, Đ33 | 01/07/2024 | Còn HL | gốc-OCR | [VB 210491](https://vanban.chinhphu.vn/?pageid=27160&docid=210491) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/6/69-cp.signed.pdf) |
| 26/2023/QH15 | Luật Căn cước: Đ15 k3, Đ16 k1 d | 01/07/2024 | Còn HL; sửa bởi Luật 118/2025/QH15 (chưa đọc) | gốc | [VB 209628](https://vanban.chinhphu.vn/?pageid=27160&docid=209628) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/01/luat26.pdf) |
| 23/2025/NĐ-CP; VBHN 17/2026/VBHN-NĐ-BKHCN (07/09/2026) | Chữ ký điện tử, dịch vụ tin cậy: Đ36 k2; hợp nhất với NĐ 15/2026 | 10/04/2025; NĐ 15/2026: 14/01/2026 | Còn HL | gốc-OCR | [VB 212829](https://vanban.chinhphu.vn/?pageid=27160&docid=212829) · [PDF NĐ 23](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/02/23-cp.signed.pdf) · [VB 219408 (VBHN)](https://vanban.chinhphu.vn/?pageid=27160&docid=219408) · [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/17-vbhn-bkhcn.signed.pdf) |
| 20/2026/QH16 (24/08/2026) | Sửa Luật Tần số, Viễn thông, GDĐT, Chuyển giao công nghệ | 01/03/2027 (một số khoản 01/10/2026) | Sắp HL | gốc-OCR (đã đọc phần sửa GDĐT) | [VB 219488](https://vanban.chinhphu.vn/?pageid=27160&docid=219488) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/20-qh16.signed.pdf) |
| 165/2025/NĐ-CP | Đ17 k10: nhật ký xử lý dữ liệu cốt lõi, quan trọng ≥06 tháng | 01/07/2025 | Còn HL | gốc-OCR | [VB 214331](https://vanban.chinhphu.vn/?pageid=27160&docid=214331) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/165nd.signed.pdf) |
| Dự án Luật Định danh và xác thực điện tử | — | — | Thẩm tra 30/09/2026; trình Kỳ họp 2 (khai mạc dự kiến 17/10/2026) | thứ cấp | [lsvn 30/09/2026 (báo, bối cảnh)](https://lsvn.vn/uy-ban-quoc-phong-an-ninh-va-doi-ngoai-cua-quoc-hoi-tham-tra-chinh-thuc-du-an-luat-dinh-danh-va-xac-thuc-dien-tu-a180100.html) · [VB 218055 (NQ 125/NQ-CP)](https://vanban.chinhphu.vn/?pageid=27160&docid=218055) |
| 329/2026/NĐ-CP | Lực lượng bảo vệ an ninh mạng: Đ6 | 19/08/2026 | Còn HL | gốc-OCR | [VB 219235](https://vanban.chinhphu.vn/?pageid=27160&docid=219235) |
| 57/2025/TT-BYT | Phân nhóm TBYT theo tiêu chuẩn kỹ thuật (đấu thầu) | 15/02/2026; phân nhóm từ 01/01/2027 | Còn HL | gốc | [VB 216452](https://vanban.chinhphu.vn/?pageid=27160&docid=216452) |
| 47/2025/TT-BYT | Bãi bỏ 43 VBQPPL, có QĐ 2824/2004 và TT 22/2024/TT-BYT | 15/02/2026 | Còn HL | gốc | [VB 216427](https://vanban.chinhphu.vn/?pageid=27160&docid=216427) |

**Rà soát docid vanban.chinhphu.vn còn sót** (đã mở cả 10): [219235](https://vanban.chinhphu.vn/?pageid=27160&docid=219235) NĐ 329/2026 → R27 · [216452](https://vanban.chinhphu.vn/?pageid=27160&docid=216452) TT 57/2025 → R28 · [219586](https://vanban.chinhphu.vn/?pageid=27160&docid=219586) QĐ 1830/QĐ-TTg (kết nối VNeID với ASEAN; ngoại vi) · [219479](https://vanban.chinhphu.vn/?pageid=27160&docid=219479) QĐ 1772/QĐ-TTg (danh mục văn bản chi tiết luật kỳ họp bất thường; ngoại vi) · [219489](https://vanban.chinhphu.vn/?pageid=27160&docid=219489) Luật 21/2026/QH16 (nông nghiệp, môi trường; loại) · [218842](https://vanban.chinhphu.vn/?pageid=27160&docid=218842) QĐ 1250/QĐ-TTg (kế hoạch phát triển YHCT; chưa đọc nội dung) · [216991](https://vanban.chinhphu.vn/?pageid=27160&docid=216991) TT 03/2026/TT-BYT (bãi bỏ phần lớn TT 09/2015; xem CHUYENKHOA-R26) · [216427](https://vanban.chinhphu.vn/?pageid=27160&docid=216427) TT 47/2025/TT-BYT · [213682](https://vanban.chinhphu.vn/?pageid=27160&docid=213682) TT 10/2025/TT-BYT · [216632](https://vanban.chinhphu.vn/?pageid=27160&docid=216632) NĐ 13/2026/NĐ-CP (sửa NĐ 62/2024 về thống kê; chưa đọc).

## 2. Yêu cầu

Quy ước: yêu cầu đã có ở domain khác chỉ ghi phần bổ sung, kèm ID gốc. Mọi mức phạt NĐ 90/2026 là của cá nhân; tổ chức gấp 02 lần (NĐ 90 Đ4 k5).

### A. Khung chung

### BAOMAT-CB-R01 — Danh mục "nhạy cảm chuyên biệt" và cờ ở mức bản ghi
- **Căn cứ**: NĐ 356/2025 Đ4 k1: DLCN nhạy cảm gồm c (đời sống riêng tư, bí mật cá nhân, gia đình), d (sức khỏe), đ (sinh trắc, di truyền), e (đời sống tình dục), m (dữ liệu khác pháp luật quy định cần giữ bí mật); Đ4 k2 (phân quyền giới hạn truy cập, quy trình, biện pháp bảo mật). Các luật riêng ở mục B–H là "pháp luật quy định cần giữ bí mật" theo k1 m (suy luận ghép).
- **Áp dụng**: mọi hệ thống · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục tối thiểu `HIV`, `OST`, `DRUG_TEST`, `PSY`, `ART_DONOR`, `SURROGACY`, `FETAL_SEX`, `TRANSPLANT_DONOR_RECIPIENT`, `GENDER_REASSIGN`, `GENETIC`, `DV`, `CHILD_ABUSE`; gắn cờ ở mức bản ghi (chỉ định, kết quả, chẩn đoán, đơn, phiếu, tệp đính kèm), không chỉ mức người bệnh; gắn tự động theo mã (ICD-10, dịch vụ, thuốc, chỉ số XN), gắn tay có ghi vết; mỗi loại có chính sách xem, in, xuất, gửi riêng.
- **Bẫy**: DLCN-R32 ghi hai nhóm sinh sản, di truyền là NÊN; domain này nâng IVF, mang thai hộ, ghép tạng, giới tính thai, xác định lại giới tính lên BẮT BUỘC vì đã có căn cứ riêng. Tâm thần vẫn NÊN ở phần cờ riêng (R11).

### B. HIV/AIDS

### BAOMAT-CB-R02 — Kết quả HIV dương tính chỉ thông báo cho danh sách đóng
- **Căn cứ**: Luật 64/2006 Đ30 (thay bởi Luật 71/2020 Đ1 k10) k1 (người đứng đầu cơ sở XN khẳng định chịu trách nhiệm thông báo), k2 (chỉ thông báo cho: a người được XN; b vợ/chồng, cha mẹ, người giám hộ, đại diện của người dưới 18 tuổi hoặc hạn chế năng lực; c người được giao tư vấn, thông báo; d người đứng đầu, người được giao giám sát dịch tễ HIV; đ người đứng đầu, điều dưỡng trưởng khoa có người nhiễm điều trị và nhân viên y tế được giao trực tiếp điều trị, chăm sóc; e y tế tại cơ sở giáo dục bắt buộc, trường giáo dưỡng, cơ sở cai nghiện, bảo trợ xã hội, trại giam, tạm giam, tạm giữ; g cơ quan tố tụng khi XN bắt buộc theo Đ28 k1), k6 (những người này giữ bí mật). Đ8 k5 (cấm công khai, tiết lộ khi chưa được đồng ý, trừ Đ30). NĐ 90/2026 Đ19 k3 đ (thông báo sai đối tượng, tiết lộ bí mật kết quả: 5–10 triệu); Đ18 k3 c (tiết lộ việc một người nhiễm HIV: 10–15 triệu); Đ18 k4 (công khai tên, địa chỉ, hình ảnh: 15–20 triệu); Đ18 k5 c (buộc xin lỗi, cải chính).
- **Áp dụng**: cơ sở XN HIV, BV, PK, LIS · **Hiệu lực/hạn**: 01/07/2021
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kết quả HIV có phản ứng/dương tính mặc định ẩn với mọi vai trò, chỉ hiện cho người được ánh xạ vào một điểm của k2 (bảng ánh xạ vai trò → điểm a–g, có người cấp quyền, căn cứ); "được giao trực tiếp điều trị" là phân công có thời hạn theo lượt (care team), không phải cả khoa; không hiện ở danh sách chờ, bảng theo dõi khoa, màn hình công cộng, phiếu tóm tắt, SMS, thông báo đẩy; chặn in, xuất khi người thao tác không thuộc danh sách; log riêng mọi lần xem (R22).
- **Bẫy**: bản Đ30 năm 2006 chỉ 3 khoản, danh sách khác; nhiều tài liệu HIS cũ còn trích bản này.

### BAOMAT-CB-R03 — Tiếp cận thông tin người nhiễm HIV: ai, phạm vi, thủ tục văn bản
- **Căn cứ**: Luật HIV Đ30 k3 (người được tiếp cận: a giám sát dịch tễ; b BHXH khi giám định, thanh toán BHYT; c người đứng đầu, người được giao của cơ sở y tế khi trực tiếp thanh toán, quản lý thông tin KCB của người nhiễm; d người được người nhiễm đồng ý), k4 (phạm vi: k3 b, c chỉ với người nhiễm KCB tại cơ sở nơi làm việc hoặc được phân công giám định), k5 (nội dung). TT 04/2023 Đ11 (3 hình thức: đọc trực tiếp trên HSBA, phiếu, hệ thống quản lý thông tin; nhận văn bản; hình thức khác), Đ12 (người đề nghị phải có văn bản đề nghị; k3 d phải có đồng ý bằng văn bản của người nhiễm; cơ quan quản lý thông tin có văn bản đồng ý). NĐ 90 Đ19 k2 g (tiếp cận sai hình thức, quy trình: 3–5 triệu).
- **Áp dụng**: BV, PK (thu ngân, KHTH, quản lý dữ liệu); vendor tích hợp BHXH · **Hiệu lực/hạn**: 01/05/2023
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: thu ngân, kế toán, giám định nội bộ chỉ thấy phần cần cho thanh toán (mã dịch vụ, thuốc, chi phí), che chẩn đoán, kết quả, diễn biến; luồng "đề nghị tiếp cận thông tin người nhiễm HIV" lưu văn bản đề nghị, điểm k3, phạm vi, nội dung, hình thức, thời hạn, văn bản đồng ý của cơ sở, đồng ý của người nhiễm (k3 d); quyền mở sau khi duyệt và tự hết hạn; XML BHYT sang BHXH là luồng được phép theo k3 b (R21).
- **Bẫy**: k3 c không phải căn cứ cho mọi admin hệ thống xem dữ liệu HIV. Vendor hỗ trợ từ xa không thuộc danh sách nào; dùng dữ liệu che hoặc phá kính có duyệt (R20, suy luận).

### BAOMAT-CB-R04 — Phiếu kết quả XN HIV dương tính; hạn 72 giờ làm việc
- **Căn cứ**: TT 04/2023 Đ2 k1 (thu thông tin theo mẫu Phiếu, đối chiếu giấy tờ), k2 b (Phiếu tối thiểu 03 bản: cơ sở chỉ định, cơ sở XN khẳng định, người được XN), k3 a (quy trình chuyển Phiếu giữa các khoa bảo đảm bí mật), k3 b (gửi ra ngoài: phong bì dán kín, niêm phong), k3 c (được chuyển Phiếu qua hệ thống thông tin bệnh viện hoặc hệ thống thông tin HIV/AIDS); Đ3 (thông báo chậm nhất 72 giờ làm việc từ khi người chịu trách nhiệm nhận Phiếu; ngoại lệ: không đến nhận, chưa đủ sức khỏe); Đ4 (hình thức theo đối tượng). NĐ 90 Đ19 k1 e (1–3 triệu), k2 b (sai thời gian: 3–5 triệu), k2 c (sai hình thức, quy trình: 3–5 triệu).
- **Áp dụng**: cơ sở XN sàng lọc, khẳng định HIV; LIS · **Hiệu lực/hạn**: 01/05/2023
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh Phiếu đúng mẫu Phụ lục TT 04 (mẫu chưa trích) với 3 bản đánh số; chuyển Phiếu điện tử chỉ tới người có vai trò thuộc Đ30 k2, ghi nhận đã nhận; đồng hồ 72 giờ làm việc theo lịch ngày làm việc, cảnh báo quá hạn, lý do ngoại lệ; ghi hình thức đã thông báo cho từng đối tượng.
- **Bẫy**: "72 giờ làm việc" khác "72 giờ" của sự cố DLCN (DLCN-R17). Cách tính giờ làm việc chưa có hướng dẫn (suy luận: 9 ngày làm việc × 8 giờ).

### BAOMAT-CB-R05 — Luồng nội bộ: khoa điều trị, chuyển khoa, chuyển cơ sở
- **Căn cứ**: TT 04/2023 Đ5 (khám: bộ phận XN lưu 01 Phiếu, chuyển 01 Phiếu cho bác sĩ khám; nhập viện thì Phiếu đi kèm HSBA; chuyển cơ sở điều trị HIV thì chuyển Phiếu), Đ6 (nội trú: người được giao thông báo cho nhân viên trực tiếp chăm sóc hoặc nhân viên trực tiếp khám, làm kỹ thuật ở khoa, phòng khác; chuyển khoa, chuyển cơ sở thì Phiếu đi kèm), Đ7, Đ8 (cơ sở quản lý như trại giam, cai nghiện).
- **Áp dụng**: BV, PK có nội trú, ngoại trú; HIS/EMR · **Hiệu lực/hạn**: 01/05/2023
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chuyển khoa thì quyền xem HIV đi theo care team khoa nhận, khoa cũ mất quyền sau bàn giao (giữ quyền đọc phần mình đã ghi, có log); chỉ định kỹ thuật ở khoa khác cho phép "thông báo có chủ đích" tới người làm kỹ thuật mà không mở toàn bộ hồ sơ; giấy chuyển viện, tóm tắt có Phiếu HIV đính kèm tách riêng.
- **Bẫy**: Đ6 là căn cứ cảnh báo phòng hộ ở phòng mổ, thủ thuật, nhưng chỉ cho người trực tiếp làm (suy luận).

### BAOMAT-CB-R06 — Người chưa thành niên, người hạn chế năng lực
- **Căn cứ**: Luật HIV Đ27 k2–3 (sửa bởi Luật 71/2020): từ đủ 15 tuổi có năng lực hành vi được tự nguyện yêu cầu XN; dưới 15 tuổi, mất hoặc hạn chế năng lực chỉ XN khi có đồng ý bằng văn bản của cha mẹ, người giám hộ, đại diện. TT 04/2023 Đ5 k5: dưới 15 tuổi và nhóm hạn chế năng lực thì thông báo đồng thời cho người đó và người đại diện; từ 15 đến dưới 18 thì thông báo, tư vấn cho người được XN trước, rồi mới cho cha mẹ. NĐ 90 Đ19 k3 e (XN cho người dưới 15 tuổi… chưa có đồng ý bằng văn bản, trừ cấp cứu: 5–10 triệu).
- **Áp dụng**: cơ sở XN, BV nhi, sản, PK · **Hiệu lực/hạn**: 01/07/2021; 01/05/2023
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chỉ định XN HIV cho người dưới 15 tuổi (tính theo ngày sinh tại thời điểm chỉ định) hoặc có cờ hạn chế năng lực phải đính kèm đồng ý của người đại diện, trừ cấp cứu có lý do; tác vụ thông báo cho người 15–<18 gồm hai bước tuần tự.
- **Bẫy**: bản 2006 dùng mốc 16 tuổi; hệ thống viết trước 2021 có thể còn mốc 16.

### BAOMAT-CB-R07 — Chia sẻ bắt buộc qua HIV-INFO cho giám sát dịch tễ
- **Căn cứ**: TT 07/2023 Đ5 k1 a (cơ sở XN sàng lọc chuyển thông tin người có kết quả phản ứng tới cơ sở XN khẳng định qua HIV-INFO hoặc văn bản Phụ lục 1), k2 a (cơ sở khẳng định cập nhật kết quả lên HIV-INFO), k4; Đ6 k1 (thông báo dương tính cho cơ quan giám sát các cấp và Cục Phòng, chống HIV/AIDS qua HIV-INFO); Đ9 k1 (cơ sở điều trị thông báo thông tin điều trị theo Phụ lục 2). Luật HIV Đ30 k2 d, k3 a. NĐ 90 Đ18 k3 c loại trừ việc phản hồi thông tin trong giám sát dịch tễ.
- **Áp dụng**: cơ sở XN sàng lọc, khẳng định, cơ sở điều trị ARV · **Hiệu lực/hạn**: 01/06/2023
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: xuất dữ liệu theo Phụ lục 1, 2 TT 07 (trường chưa trích chi tiết) hoặc in mẫu văn bản thay thế; ghi `disclosure_log` (đích, thời điểm, người gửi, tóm tắt, căn cứ "TT 07/2023 Đ5/Đ6/Đ9"); các luồng này miễn bộ lọc HIV của R21 nhưng chỉ đi đúng đích.
- **Bẫy**: TT 07 và NĐ 141 còn dùng "cấp huyện"; đích nhận thực tế sau khi bỏ cấp huyện chưa xác minh. Đặc tả API HIV-INFO không thấy công bố.

### BAOMAT-CB-R08 — Xét nghiệm giấu tên trong giám sát trọng điểm
- **Căn cứ**: Luật HIV Đ25 k2 (giám sát trọng điểm phải dùng phương pháp XN HIV giấu tên), k3 (giữ bí mật, chỉ dùng cho giám sát dịch tễ, nghiên cứu). TT 07/2023 Đ12–17.
- **Áp dụng**: cơ sở XN tham gia giám sát trọng điểm · **Hiệu lực/hạn**: 01/01/2007
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chế độ mẫu giấu tên trong LIS: chỉ mã mẫu và biến dịch tễ, không lưu họ tên, định danh, số điện thoại; không cho liên kết với hồ sơ người bệnh; không đẩy sang HIS, Sổ SKĐT, XML BHYT.

### C. Điều trị thay thế và xét nghiệm ma túy

### BAOMAT-CB-R09 — Methadone: đồng ý, thông báo tới UBND xã, tóm tắt khi chuyển
- **Căn cứ**: NĐ 141/2024 Đ27 k1 (tự nguyện); Đ29 k1–2 (từ đủ 12 đến dưới 18 tuổi cần đồng ý bằng văn bản của người đại diện); Đ30 (hồ sơ: đơn Mẫu 09; quyết định UBND xã Mẫu 10 hoặc phiếu xác định tình trạng nghiện); Đ31 k2 b–c, k3 (Thông báo tiếp nhận Mẫu 11 / không tiếp nhận Mẫu 12 gửi UBND xã nơi cư trú; 03 bản); Đ34 (Bản tóm tắt bệnh án Mẫu 14 khi chuyển tiếp điều trị); Đ35 k3 a (danh sách cấp thuốc nhiều ngày gửi UBND xã); Đ36 k2 (căn cứ chấm dứt: bỏ thuốc từ 30 ngày; dương tính chất dạng thuốc phiện ≥02 lần trong 12 tháng sau đạt liều duy trì…), k3 a (chấm dứt: Mẫu 15), k4 a (hoàn thành: Mẫu 16); Đ26 k3; Đ54 k2 (thuốc thay thế quản lý như thuốc gây nghiện).
- **Áp dụng**: cơ sở điều trị thay thế, cơ sở cấp phát, BV có người bệnh nội trú đang uống methadone · **Hiệu lực/hạn**: 15/12/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dữ liệu điều trị thay thế gắn cờ `OST`, mặc định chỉ đội điều trị thay thế thấy; Mẫu 11, 12, 14, 15, 16 sinh từ dữ liệu, ghi `disclosure_log` (đích UBND xã, căn cứ); không gửi thông tin ra UBND xã ngoài các mẫu này; người 12–<18 bắt buộc đồng ý của đại diện trước khi kích hoạt; cảnh báo các mốc dẫn tới chấm dứt, không tự chấm dứt.
- **Bẫy**: Mẫu 15 dẫn tới việc UBND xã lập hồ sơ đưa vào cai nghiện bắt buộc (Đ36 k3 b); gửi nhầm có hậu quả nặng → duyệt hai người (suy luận). NĐ 90/2016 (methadone) hết HL từ 15/12/2024.

### BAOMAT-CB-R10 — Xét nghiệm ma túy, xác định tình trạng nghiện
- **Căn cứ**: Luật PCMT 2021 Đ22 k1–2 (các trường hợp XN ma túy trong cơ thể; kết quả dương tính gửi ngay Chủ tịch UBND xã nơi cư trú, trừ người đang cai nghiện bắt buộc); Đ27 k4 (cơ sở y tế xác định tình trạng nghiện gửi ngay kết quả cho cơ quan đề nghị và người được xác định), k6 (NĐ 109/2021, chưa đọc). Luật PCMT không có điều khoản bí mật riêng → áp chung Luật KCB Đ10 k2, Đ45 k5, NĐ 90 Đ38 k3 c (làm lộ thông tin, HSBA: 1–3 triệu), NĐ 356 Đ4 k1 d.
- **Áp dụng**: cơ sở xác định tình trạng nghiện, phòng XN ma túy, cơ sở cai nghiện có KCB · **Hiệu lực/hạn**: 01/01/2022
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phân biệt XN ma túy theo Đ22 k1 (có cơ quan đề nghị, có nghĩa vụ báo) với XN thường quy lâm sàng (ngộ độc, KSK lái xe), vì nghĩa vụ gửi UBND xã chỉ áp loại đầu (suy luận); lưu cơ quan đề nghị, số văn bản; gửi kết quả có ghi vết; cờ `DRUG_TEST`.
- **Bẫy**: khi phòng XN chỉ làm theo đề nghị, ai gửi kết quả cho UBND xã chưa rõ (mục 7).

### D. Sức khỏe tâm thần

### BAOMAT-CB-R11 — Tâm thần: bắt buộc chữa bệnh có thủ tục riêng; không có quy chế bảo mật riêng
- **Căn cứ**: Luật KCB Đ82 k1 b (bắt buộc chữa bệnh: trầm cảm có ý tưởng, hành vi tự sát; bệnh tâm thần ở trạng thái kích động có khả năng gây nguy hại), Đ13 k1–2, Đ7 k19. NĐ 96/2023 Đ91 k1 b, k2; Đ93 k1–2 (cơ sở tổ chức điều trị bắt buộc hoặc chuyển cơ sở tâm thần, đồng thời thông báo thân nhân; không xác định được hoặc thân nhân từ chối thì lập hồ sơ đề nghị cơ quan bảo trợ xã hội). NĐ 90 Đ38 k5 a (ngăn cản người thuộc diện bắt buộc chữa bệnh: 5–10 triệu). Luật Phòng bệnh Đ33 k1 b. TT 33/2025 mục 40: HSBA tâm thần 20 năm (EMR-R22). Báo cáo RLTT: HTTT-BC-R29.
- **Áp dụng**: BV tâm thần, khoa tâm thần, PK tâm thần, app tư vấn tâm lý · **Hiệu lực/hạn**: 01/01/2024
- **Mức**: BẮT BUỘC (ghi nhận quyết định bắt buộc chữa bệnh, thông báo thân nhân, lưu 20 năm) / NÊN (cờ `PSY` và phân quyền hẹp hơn HSBA thường)
- **Phần mềm phải**: bản ghi quyết định bắt buộc chữa bệnh có căn cứ (Đ82 k1 a/b/c), người quyết định (NĐ 96 Đ93 không nêu chức danh; áp tương tự Đ92 k3 a theo quy chế nội bộ, suy luận), thời điểm, ghi nhận đã thông báo thân nhân hoặc lý do; khóa chức năng ký từ chối điều trị/ra viện trái chỉ định khi quyết định còn hiệu lực; (NÊN) ghi chép tâm lý trị liệu để ở ngăn riêng, không vào tóm tắt Sổ SKĐT, không hiện cho khoa khác.
- **Bẫy**: không có văn bản cấm tiết lộ chẩn đoán tâm thần riêng như HIV; đừng tuyên bố "luật bắt buộc che hồ sơ tâm thần". Luật KCB Đ10 k2, NĐ 90 Đ38 k3 c vẫn áp như mọi HSBA.

### E. Hỗ trợ sinh sản, mang thai hộ, giới tính thai nhi

### BAOMAT-CB-R12 — IVF, mang thai hộ: vô danh, mã hóa, chia sẻ CSDL dùng chung
- **Căn cứ**: NĐ 207/2025 (diễn giải, gốc-OCR) Đ3 k1 (chỉ hiến tại một cơ sở được phép lưu giữ), k2 (mẫu hiến chỉ dùng cho một phụ nữ hoặc một cặp vợ chồng), k3 (vô danh giữa người hiến và người nhận), k5 (vợ chồng nhờ mang thai hộ, người mang thai hộ, trẻ sinh ra được bảo đảm đời sống riêng tư, bí mật cá nhân, gia đình); Đ4 k2 (người hiến không bệnh di truyền, tâm thần, không nhiễm HIV); Đ8 k2 (không đóng phí lưu giữ thì sau 06 tháng cơ sở được hủy); Đ17 k1 b (BYT xây dựng CSDL dùng chung về hỗ trợ sinh sản và quy định chia sẻ). NĐ 90/2026 Đ42 k3 (10–20 triệu): a (cơ sở lưu giữ không bảo mật thông tin người hiến, người nhận), d (không mã hóa thông tin hiến, lưu giữ; không chia sẻ CSDL dùng chung), v (cơ sở IVF, mang thai hộ, lưu giữ không mã hóa hoặc không chia sẻ); Đ42 k4 a, d (cho hiến ở hơn một cơ sở; dùng mẫu hiến cho từ hai phụ nữ/cặp trở lên: 20–30 triệu). Phạm vi cơ sở được làm IVF và thời hạn lưu: xem CHUYENKHOA-R15.
- **Áp dụng**: cơ sở IVF, ngân hàng mô lưu giao tử/phôi, phần mềm labo IVF · **Hiệu lực/hạn**: 01/10/2025 (NĐ 207); 15/05/2026 (NĐ 90)
- **Mức**: BẮT BUỘC (vô danh, bảo mật, mã hóa) / BẮT BUỘC? (chia sẻ CSDL dùng chung: chưa thấy văn bản kỹ thuật)
- **Phần mềm phải**: người hiến định danh bằng mã hiến; bảng nối mã ↔ danh tính ở kho tách riêng, khóa riêng, chỉ vai trò quản lý ngân hàng mẫu truy cập; hồ sơ người nhận, bệnh án IVF, giấy chứng sinh chỉ chứa mã hiến; `UNIQUE(donation_id)` trên bảng phân bổ (phân bổ lại khi hủy có ghi vết); cờ `SURROGACY`; cổng xuất dữ liệu đã mã hóa sang CSDL dùng chung khi BYT công bố đặc tả; lịch hủy mẫu khi quá 06 tháng không đóng phí, có biên bản.
- **Bẫy**: NĐ 10/2015, NĐ 98/2016 hết HL từ 01/10/2025. "Mã hóa" trong NĐ 90 Đ42 không được định nghĩa (mã định danh hay mã hóa mật mã); nên làm cả hai (suy luận).

### BAOMAT-CB-R13 — Giới tính thai nhi: cấm thông báo, tiết lộ qua siêu âm, xét nghiệm
- **Căn cứ**: Luật Dân số 2025 Đ6 k3 nghiêm cấm "Lựa chọn giới tính thai nhi dưới mọi hình thức; thông báo, tiết lộ giới tính thai nhi, trừ trường hợp do Bộ trưởng Bộ Y tế quy định để phục vụ chẩn đoán và điều trị các bệnh liên quan đến giới tính"; Đ15 k2. Luật KCB Đ34 k1 d (do Luật Dân số Đ29 k4 bổ sung từ 01/07/2026: đình chỉ hành nghề). NĐ 90/2026 Đ98 k2 (bắt mạch, siêu âm, xét nghiệm để chẩn đoán và tiết lộ giới tính thai: 7–15 triệu; k3 tước giấy phép, chứng chỉ 01–03 tháng); Đ97 (tuyên truyền, tư vấn, đưa lên mạng, nền tảng phương pháp chọn giới tính: 5–20 triệu theo hành vi); Đ99 k3 (chỉ định thuốc, chế phẩm để chọn giới tính: 20–25 triệu). Quảng cáo chẩn đoán, chọn giới tính: xem CHUYENKHOA-R33.
- **Áp dụng**: PK, BV có siêu âm sản; RIS/PACS; LIS làm NIPT, karyotype trước sinh; app thai kỳ · **Hiệu lực/hạn**: 01/07/2026; 15/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mẫu kết quả siêu âm thai không có trường giới tính thai; nếu máy tự điền thì lọc khi đẩy sang RIS, HIS, app, Sổ SKĐT; LIS che nhiễm sắc thể giới tính (X/Y) trên phiếu và mọi kênh xuất, trừ chỉ định có mã bệnh liên quan giới tính thuộc danh mục BYT (chưa ban hành) và khi đó chỉ trả cho bác sĩ chỉ định; app, chatbot không dự đoán/tư vấn giới tính thai; log mọi lần mở kết quả có X/Y.
- **Bẫy**: NĐ 90 vẫn dẫn Pháp lệnh Dân số làm căn cứ; từ 01/07/2026 hành vi cấm nằm ở Luật Dân số, chế tài NĐ 90 Đ98 vẫn áp (suy luận).

### F. Hiến, ghép mô tạng

### BAOMAT-CB-R14 — Người hiến, người được ghép: mã hóa, vô danh khi công bố, hai kênh cung cấp
- **Căn cứ**: Luật 75/2006 Đ4 k4 (giữ bí mật thông tin người hiến, người được ghép, trừ thỏa thuận khác hoặc luật khác), Đ11 k9 (cấm tiết lộ trái pháp luật), Đ36 k2 d, Đ38 k1: "Mọi thông tin về người hiến, người được ghép bộ phận cơ thể người phải được mã hóa thông tin và bảo mật"; k2 (công bố phải vô danh, trừ cùng dòng máu trực hệ hoặc họ trong phạm vi ba đời); k3 (chỉ cung cấp vì mục đích chữa bệnh theo yêu cầu người đứng đầu cơ sở y tế hoặc theo yêu cầu cơ quan tiến hành tố tụng). NĐ 90/2026 Đ44 k5 a (tiết lộ thông tin, bí mật người hiến, người được ghép: 30–40 triệu), Đ44 k1 d (không báo cáo danh sách người đăng ký hiến: 1–2 triệu).
- **Áp dụng**: BV ghép tạng, ngân hàng mô, cơ sở tiếp nhận đăng ký hiến · **Hiệu lực/hạn**: 01/07/2007
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hồ sơ người hiến và người nhận liên kết qua mã ca ghép, không hiện danh tính bên kia (trừ cờ cùng huyết thống theo Đ38 k2 kèm văn bản thỏa thuận); báo cáo, bài trình bày ca ghép xuất vô danh; luồng cung cấp thông tin chỉ có hai căn cứ (người đứng đầu cơ sở y tế vì chữa bệnh; cơ quan tố tụng) kèm văn bản; mã hóa cột danh tính với khóa riêng.
- **Bẫy**: dự thảo luật sửa đổi (thẩm tra 10/2026) có nội dung CĐS, phân quyền, kết nối CSDL quốc gia (thứ cấp); theo dõi.

### BAOMAT-CB-R15 — Lưu hồ sơ người hiến và người được ghép 30 năm
- **Căn cứ**: Luật 75/2006 Đ38 k4: "Hồ sơ về người hiến và người được ghép phải được lưu giữ, bảo quản trong ba mươi năm". TT 33/2025 PL mục 43: HSBA đợt ghép mô, tạng 20 năm (EMR-R22). Luật có hiệu lực cao hơn thông tư.
- **Áp dụng**: BV ghép tạng, ngân hàng mô · **Hiệu lực/hạn**: 01/07/2007
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: loại lưu trữ "ghép tạng" 30 năm cho hồ sơ người hiến và người được ghép, kể cả HSBA đợt ghép (nguyên tắc lấy thời hạn dài nhất, EMR-R22); nhật ký truy cập các hồ sơ này lưu cùng thời hạn (R22).
- **Bẫy**: mâu thuẫn TT 33 (20 năm) và Luật 75 (30 năm); áp 30 năm (suy luận theo thứ bậc văn bản). Áp cho EMR-R22, CHUYENKHOA-R13.

### G. Xác định lại giới tính, di truyền

### BAOMAT-CB-R16 — Thông tin xác định lại giới tính
- **Căn cứ**: NĐ 90/2026 Đ45 k1 a (tiết lộ thông tin về việc xác định lại giới tính của người khác: 2–5 triệu), k1 b (phân biệt đối xử). Văn bản gốc quy định nghĩa vụ chưa đọc.
- **Áp dụng**: BV có phẫu thuật xác định lại giới tính, BV nhi (dị tật giới tính)
- **Mức**: BẮT BUỘC? (có chế tài, chưa đọc văn bản gốc của nghĩa vụ)
- **Phần mềm phải**: cờ `GENDER_REASSIGN`; khi giấy tờ đổi giới tính, hồ sơ hiện tại dùng giới tính mới, lịch sử giới tính cũ chỉ người có quyền thấy, không in trên phiếu thường quy (suy luận). Thời hạn lưu 70 năm (TT 33 mục 215): CHUYENKHOA-P05.

### BAOMAT-CB-R17 — Dữ liệu di truyền và xét nghiệm gen
- **Căn cứ**: NĐ 356 Đ4 k1 đ. NĐ 102/2025 Đ9 k2 b, c (tiếp cận thông tin di truyền khi người đó đồng ý; bí mật gia đình cần đồng ý các thành viên): xem DLCN-R33. Luật Dân số Đ6 k6, Đ21. Không tìm thấy văn bản riêng về xét nghiệm gen, ngân hàng gen.
- **Áp dụng**: phòng XN di truyền, LIS, công ty XN gen trực tiếp người tiêu dùng
- **Mức**: BẮT BUỘC (phân quyền, đồng ý theo NĐ 356, NĐ 102)
- **Phần mềm phải**: cờ `GENETIC` cho giải trình tự, panel gen, karyotype; dữ liệu thô (FASTQ, VCF) lưu tách khỏi HIS, mã hóa, truy cập theo yêu cầu; không dùng cho nghiên cứu khi chưa có căn cứ (DLCN Nhóm H); kết hợp R13 cho XN trước sinh.

### H. Bạo lực gia đình và trẻ em

### BAOMAT-CB-R18 — Người bị bạo lực gia đình
- **Căn cứ**: Luật 13/2022 Đ29 k1 a (cơ sở KCB tiếp nhận, sàng lọc, phân loại, chăm sóc, điều trị), k1 b (cung cấp thông tin tình trạng tổn hại sức khỏe theo đề nghị của người đó hoặc cơ quan, người có thẩm quyền), k2 (nhân viên y tế phát hiện dấu hiệu phải báo ngay người đứng đầu cơ sở); Đ9 k1 c (giữ bí mật nơi tạm lánh, đời sống riêng tư); Đ34 k2 (bảo vệ thông tin người báo tin); Đ35 k2 b; Đ37 k2 (cơ sở công lập có thể bố trí nơi tạm lánh không quá 01 ngày); Đ3 k1 h.
- **Áp dụng**: BV, PK (cấp cứu, sản, nhi) · **Hiệu lực/hạn**: 01/07/2023
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trường sàng lọc "nghi BLGĐ"; khi đánh dấu tạo tác vụ báo người đứng đầu (hoặc người được ủy quyền) hạn "ngay"; cờ `DV`: người đi kèm, kể cả người đại diện hợp pháp, không thấy địa chỉ tạm lánh, số liên hệ an toàn, ghi chú xã hội; app gia đình không hiện lượt khám có cờ này (suy luận từ Đ9 k1 c); mẫu cung cấp thông tin tổn hại sức khỏe lưu văn bản đề nghị; thông tin nhân viên báo tin không xuất ra ngoài.
- **Bẫy**: người đại diện hợp pháp theo Luật KCB Đ8 có thể là người gây bạo lực; logic "đại diện được xem toàn bộ" cần ngoại lệ khi có cờ `DV` (suy luận; cần luật sư).

### BAOMAT-CB-R19 — Trẻ em: đồng ý của trẻ từ đủ 7 tuổi; thông báo xâm hại; bảo mật trên mạng
- **Căn cứ**: Luật Trẻ em (diễn giải, gốc-OCR) Đ6 k11 (cấm công bố, tiết lộ đời sống riêng tư, bí mật cá nhân của trẻ khi không có đồng ý của trẻ từ đủ 07 tuổi và của cha mẹ, người giám hộ), Đ21, Đ51 k1 (trách nhiệm thông báo, tố giác hành vi xâm hại trẻ em tới cơ quan có thẩm quyền; k3 tổng đài quốc gia), Đ54 k2 (dịch vụ trên mạng bảo đảm bí mật đời sống riêng tư của trẻ), Đ58 k1 đ. DLCN-R08 (đồng ý kép theo Luật BVDLCN).
- **Áp dụng**: BV nhi, PK, app có người dùng là trẻ em · **Hiệu lực/hạn**: 01/06/2017
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dùng hình ảnh, ca bệnh trẻ em cho truyền thông, đào tạo, đăng mạng phải có đồng ý của trẻ (≥7 tuổi) và của cha mẹ/người giám hộ; cờ `CHILD_ABUSE` tạo tác vụ thông báo cơ quan có thẩm quyền (hoặc tổng đài 111), ghi vết; ẩn thông tin trẻ bị xâm hại với người đi kèm là nghi phạm (suy luận); app có người dùng dưới 16/18 mặc định riêng tư cao.
- **Bẫy**: Luật Trẻ em nằm trong dự án sửa 6 luật trình Kỳ họp 2 (10/2026); mốc 7 tuổi có thể đổi. Dùng bảng mốc tuổi theo hành vi (P09).

### I. Cơ chế xuyên suốt

### BAOMAT-CB-R20 — Phá kính có lý do, duyệt sau, trong phạm vi luật cho phép
- **Căn cứ**: NĐ 356 Đ4 k2; Luật HIV Đ30 k2–4; TT 04/2023 Đ12; NĐ 90 Đ19 k2 g; Luật KCB Đ69 k3. Không văn bản nào dùng khái niệm "phá kính"; đây là cơ chế hiện thực (suy luận).
- **Áp dụng**: HIS/EMR/LIS
- **Mức**: BẮT BUỘC? (bắt buộc có phân quyền, quy trình; cơ chế phá kính cụ thể là thiết kế)
- **Phần mềm phải**: người ngoài danh sách chỉ mở dữ liệu có cờ nhạy cảm qua phá kính: chọn lý do trong danh mục, diễn giải, thời hạn ngắn (ví dụ 4 giờ), cảnh báo tức thời cho người phụ trách bảo mật/DPO; duyệt sau trong ≤3 ngày làm việc (khuyến nghị); **không cho phá kính** với danh tính người hiến giao tử/phôi (R12), danh tính người hiến tạng với người nhận (R14), mẫu XN giấu tên (R08); báo cáo định kỳ số lần phá kính.
- **Bẫy**: phá kính không biến người truy cập thành "người được thông báo" theo Đ30 k2; truy cập HIV ngoài danh sách vẫn có rủi ro bị coi là tiếp cận sai quy trình.

### BAOMAT-CB-R21 — Bộ lọc xuất ra ngoài theo loại nhạy cảm và theo đích
- **Căn cứ**: các căn cứ R02–R19; SKDT-R19; DLCN-R32; Luật HIV Đ30 k3 b; Luật 75 Đ38 k2; NĐ 207 Đ3 k3.
- **Áp dụng**: mọi luồng xuất: Sổ SKĐT/VNeID, app người bệnh, cổng tra cứu, SMS/Zalo, XML BHYT, HTTT quản lý KCB, báo cáo thống kê, nghiên cứu, tóm tắt, giấy ra viện, chuyển viện
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: ma trận `category × destination → {gửi, che, không gửi, cần đồng ý}`, tối thiểu:

  | Loại | XML BHYT | Sổ SKĐT / app | Người đi kèm, đại diện | Thống kê | Cơ quan luật chỉ định |
  |---|---|---|---|---|---|
  | HIV | Gửi (Đ30 k3 b) | Không gửi mặc định; chỉ khi người bệnh đồng ý (suy luận) | Chỉ theo Đ30 k2 b | Tổng hợp, không định danh | HIV-INFO (R07); tố tụng (Đ30 k2 g) |
  | Methadone | Theo thực tế thanh toán (chưa xác minh) | Không gửi mặc định | Không | Theo NĐ 141 Đ26 k3 | UBND xã qua Mẫu 11–16 (R09) |
  | Giới tính thai | Không | Không | Không | Không | Không (trừ danh mục BYT) |
  | Người hiến tạng/giao tử | Không định danh | Không | Không | Vô danh | Trung tâm điều phối; CSDL hỗ trợ sinh sản; tố tụng |
  | BLGĐ | Dữ liệu thanh toán | Không gửi ghi chú xã hội | Không | Tổng hợp | Theo đề nghị có thẩm quyền (Đ29 k1 b) |

- **Bẫy**: ma trận là mức tối thiểu đề xuất; dòng Sổ SKĐT là suy luận vì QĐ 31, QĐ 2733 không nêu ngoại lệ cho HIV. Lọc không được làm thiếu dữ liệu bắt buộc (ví dụ XML BHYT cần chẩn đoán để thanh toán ARV).

### J. Nhật ký truy cập HSBA

### BAOMAT-CB-R22 — Thời hạn lưu nhật ký truy cập HSBA
- **Căn cứ**: không văn bản y tế nào nêu riêng "nhật ký truy cập HSBA". CV 365 (thứ cấp) yêu cầu ghi vết giao dịch, thao tác, đăng nhập nhưng không nêu thời hạn; TT 13/2025, TT 33/2025 không có quy định. Khung ANM (chủ: **ANM-R11**) có các mức tùy đối tượng: NĐ 330 Đ34 k1 c (≥90 ngày thông tin đăng nhập tài khoản số), NĐ 333 Đ16 k6, Đ20 k3 (≥12 tháng với DN cung cấp dịch vụ trên mạng), TCVN 14423:2026 (cấp 2: ≥01 tháng; cấp 3: ≥03 tháng; cấp 4: ≥06 tháng; cấp 5: ≥12 tháng), QĐ 326/QĐ-BYT (ứng dụng ≥03 tháng, máy chủ ≥06 tháng); NĐ 165/2025 Đ17 k10 (nhật ký xử lý dữ liệu cốt lõi, quan trọng ≥06 tháng). NĐ 69/2024 Đ17 k2 (lịch sử truy cập tài khoản định danh điện tử ≥05 năm) chỉ áp cho hệ thống ĐD&XT quốc gia. NĐ 356 Đ8 k1 (nhật ký toàn bộ hoạt động xử lý DLCN) chỉ cho tài chính, ngân hàng. Dự án Luật ĐD&XTĐT (bản lấy ý kiến nêu ≥5 năm cho nhật ký xác thực) chưa thông qua.
- **Áp dụng**: HIS, EMR, LIS, RIS/PACS
- **Mức**: BẮT BUỘC (có nhật ký đọc/ghi theo EMR-R12; lưu ≥ mức khung ANM áp cho hệ thống, ANM-R11 khuyến nghị 12 tháng) / NÊN (lưu nhật ký truy cập của từng HSBA bằng thời hạn lưu HSBA đó, tối thiểu 05 năm; suy luận)
- **Lý do đề xuất mức NÊN** (suy luận): (1) nhật ký là bằng chứng duy nhất trả lời "ai đã xem HSBA của tôi" khi khiếu nại có thể phát sinh nhiều năm sau; (2) TT 33 Đ1 k2 b: hồ sơ chưa có quy định thì áp thời hạn nhóm tương đương, nhóm gần nhất là chính HSBA; (3) 05 năm khớp NĐ 69 Đ17 k2 và dự thảo Luật ĐD&XTĐT (không áp trực tiếp); (4) thời hiệu xử phạt ANM/DLCN 01 năm chỉ là sàn.
- **Phần mềm phải**: tách nhật ký an ninh hệ thống (đăng nhập, IP, cổng; theo ANM-R11, nóng 90 ngày, lưu ≥12 tháng) và nhật ký truy cập hồ sơ (patient_id, encounter_id, tài liệu, hành động, lý do, cờ nhạy cảm, phá kính); `retain_until = max(retention của HSBA liên quan, created_at + 5 năm)`, tự kéo dài khi HSBA đổi loại lưu trữ (ví dụ tử vong, ghép tạng 30 năm); chỉ-ghi-thêm, chuyển kho lạnh sau 12 tháng, vẫn truy vấn được theo người bệnh; báo cáo "ai đã xem hồ sơ của tôi" dạng tổng hợp theo vai trò, khoa (suy luận từ quyền chủ thể dữ liệu); không xóa nhật ký trước hạn kể cả khi người bệnh yêu cầu xóa dữ liệu.
- **Bẫy**: đừng trích "Luật ĐD&XTĐT yêu cầu lưu log 5 năm" như căn cứ đã có hiệu lực; đừng trích NĐ 69 Đ17 k2 như nghĩa vụ của bệnh viện.

### K. Sinh trắc và chữ ký của người bệnh

### BAOMAT-CB-R23 — QCVN sinh trắc của Bộ Công an không áp cho việc ký xác nhận trên HSBA
- **Căn cứ**: TT 169/2026/TT-BCA (QCVN 16:2026/BCA, giọng nói) và TT 170/2026/TT-BCA (QCVN 17:2026/BCA, mống mắt), ký 01/10/2026, HL 15/04/2027; mục 1.1–1.2 (diễn giải): phạm vi, đối tượng là thiết bị, phần mềm, dữ liệu sinh trắc phục vụ Cơ sở dữ liệu căn cước. TT 13/2025 Đ3 cho người bệnh xác nhận bằng kỹ thuật sinh trắc nhưng không dẫn QCVN nào (EMR-R06, R09).
- **Áp dụng**: vendor EMR, app ký tại giường
- **Mức**: NÊN (tham khảo yêu cầu kỹ thuật khi chọn thiết bị; không bắt buộc)
- **Phần mềm phải**: không cần chứng nhận hợp quy QCVN 16/17 cho thiết bị đọc vân tay, khuôn mặt dùng ký phiếu nội bộ; nhãn "đạt QCVN 17:2026/BCA" của thiết bị không làm tăng giá trị pháp lý của chữ ký người bệnh.
- **Bẫy**: số QCVN (16, 17:2026/BCA) khác số thông tư (169, 170/2026/TT-BCA); trang 1 TT 170 có số viết tay, OCR có thể đọc nhầm.

### BAOMAT-CB-R24 — Xác thực VNeID/sinh trắc khi người bệnh ký
- **Căn cứ**: NĐ 69/2024 Đ18 k1 (CQNN, tổ chức cung cấp dịch vụ công kết nối hệ thống ĐD&XT khi HTTT đạt tối thiểu cấp độ 3), k4 (tổ chức khác kết nối qua tổ chức cung cấp dịch vụ xác thực); Đ19 k3 (phải được chủ thể đồng ý qua VNeID, SMS số chính chủ hoặc hình thức khác), k4 (không chia sẻ kết quả xác thực; kết quả xác thực không dùng làm yếu tố xác thực cho giao dịch khác); Đ20 k1 (mức 3: ≥2 yếu tố có sinh trắc; mức 4: sinh trắc + sở hữu + biết), k2; Đ22 k1; Đ33 k2. TT 117/2026/TT-BCA (thứ cấp): khai thác sinh trắc trong CSDL dân cư chỉ trong 6 trường hợp, ưu tiên trả kết quả khớp/không khớp.
- **Áp dụng**: BV công (có thể kết nối trực tiếp nếu đạt cấp độ 3, suy luận), BV tư, PK (qua dịch vụ xác thực), vendor app
- **Mức**: BẮT BUỘC (khi chọn dùng xác thực qua hệ thống ĐD&XT)
- **Phần mềm phải**: mỗi lần xác nhận phiếu tạo một giao dịch xác thực riêng gắn hash nội dung phiếu (không tái dùng kết quả xác thực lúc đăng ký khám); lưu mức độ đạt được, mã giao dịch, thời điểm, nhà cung cấp; không lưu ảnh khuôn mặt/vân tay thô nếu đã có kết quả so khớp (R25); màn hình ký hiện nội dung đồng ý xác thực.

### BAOMAT-CB-R25 — Lưu dữ liệu sinh trắc của người bệnh
- **Căn cứ**: NĐ 356 Đ4 k1 đ, k2; Luật Căn cước Đ15 k3; NĐ 23/2025 Đ36 k2 a, d; DLCN-R17/R18 (sự cố liên quan sinh trắc).
- **Áp dụng**: EMR ký bằng sinh trắc, app eKYC
- **Mức**: BẮT BUỘC (phân quyền, bảo mật như DLCN nhạy cảm) / NÊN (không lưu mẫu thô, chỉ lưu template băm hoặc kết quả so khớp)
- **Phần mềm phải**: mẫu sinh trắc (nếu phải lưu làm bằng chứng) mã hóa, khóa riêng, tách khỏi HSBA, liên kết bằng ID bằng chứng; thời hạn lưu bằng thời hạn của phiếu được ký; không dùng cho mục đích khác (chấm công, nhận diện ở sảnh) khi chưa có căn cứ.

### BAOMAT-CB-R26 — Chữ ký số người bệnh qua CA; tác động của Luật 20/2026/QH16
- **Căn cứ**: NĐ 23/2025 Đ36 k2 (CA phát hành chứng thư bằng phương thức điện tử phải đối chiếu sinh trắc với giấy tờ, định danh và xác thực, chống mạo danh, lưu dữ liệu nhận biết); hợp nhất trong VBHN 17/2026/VBHN-NĐ-BKHCN với NĐ 15/2026. Luật 20/2026/QH16 Đ3 chỉ sửa Đ28 k4 Luật GDĐT và thay "Bộ TT&TT" bằng "Bộ KH&CN" tại Đ25 k2–3, Đ26 k4, Đ28 k3, Đ47 k2 d, Đ48 k2, Đ50 k2–3; không sửa Đ22, Đ23.
- **Áp dụng**: vendor EMR, app ký từ xa
- **Mức**: NÊN
- **Phần mềm phải**: eKYC sinh trắc khi người bệnh ký số từ xa do CA làm; HIS/EMR không tự thu sinh trắc để "định danh" thay CA; vẫn kiểm tra trạng thái chứng thư theo EMR-R07.
- **Bẫy**: "Luật 20/2026 có thể thay đổi Đ22–23 GDĐT" là sai; TT 13/2025 Đ3 k3 vẫn dẫn được Đ22 k4.

### L. Bổ sung từ rà soát docid

### BAOMAT-CB-R27 — Lực lượng thường trực bảo vệ ANM cho HTTT y tế
- **Căn cứ**: NĐ 329/2026 Đ6 k1 (lực lượng thường trực gồm bộ phận bảo vệ ANM cho HTTT, CSDL của cơ quan, tổ chức, doanh nghiệp), k2 (bố trí theo quy mô, rủi ro; hình thức: đơn vị chuyên trách, nhân sự chuyên trách, hoặc thuê doanh nghiệp ANM), k4 (nhiệm vụ gồm kiểm soát truy cập, phân quyền, báo cáo sự cố, kiểm tra tuân thủ, BVDLCN, diễn tập), k5, k6 (khuyến khích DN xử lý lượng lớn DLCN). Liên kết ANM-R21.
- **Áp dụng**: chủ quản HTTT y tế, SaaS xử lý lượng lớn DLCN · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC? (k1 bao gồm doanh nghiệp, nhưng k2 để chủ quản tự cân nhắc; k6 là khuyến khích)
- **Phần mềm phải**: vai trò "ANM thường trực" tách khỏi quản trị nghiệp vụ, xem được nhật ký an ninh và nhật ký truy cập dữ liệu nhạy cảm nhưng không xem nội dung lâm sàng; báo cáo phân quyền, truy cập.

### BAOMAT-CB-R28 — Phần mềm là thiết bị y tế bán qua đấu thầu công: hồ sơ phân nhóm từ 01/01/2027
- **Căn cứ**: TT 57/2025/TT-BYT Đ2 (tiêu chuẩn kỹ thuật, hình thức chứng minh), Đ4 (6 nhóm theo tiêu chuẩn và lưu hành tại nước tham chiếu), Đ6 k2 (phân nhóm từ 01/01/2027), Đ8 k3. Xem CLS-R23, R24.
- **Áp dụng**: vendor phần mềm là TBYT dự thầu tại cơ sở công
- **Mức**: BẮT BUỘC? (với gói thầu áp NĐ 214/2025 Đ146 k2 d; phạm vi với phần mềm chưa có hướng dẫn riêng)
- **Phần mềm phải**: (không phải chức năng) hồ sơ sản phẩm liệt kê tiêu chuẩn áp dụng (ví dụ IEC 62304, ISO 14971), chứng nhận, giấy phép lưu hành nước ngoài nếu có.

## 3. Pattern thiết kế

### BAOMAT-CB-P01 — Phân loại nhạy cảm ở mức bản ghi bằng luật mã
- **Giải quyết**: R01, R02, R09, R11–R19
- **Cách làm**: bộ quy tắc trung tâm gán cờ khi tạo hoặc đổi mã bản ghi; bỏ cờ tay phải có lý do và người duyệt.
- **Gợi ý dữ liệu**: `sensitivity_category(code PK, legal_basis, default_policy_id, breakglass_allowed)`; `sensitivity_rule(category_code, code_system, code_pattern, active_from, active_to, version)`; `record_sensitivity(record_type, record_id, category_code, source, rule_id, set_by, set_at, reason)`, chỉ mục `(record_type, record_id)`, `(category_code, patient_id)`.
- **Đánh đổi**: danh mục mã (ICD B20–B24, Z21; mã XN HIV, NIPT; ARV, methadone) phải theo QĐ danh mục BYT (MA-LT); gắn sai làm lộ hoặc cản trở điều trị.

### BAOMAT-CB-P02 — Sổ "người được biết theo luật" (statutory need-to-know)
- **Giải quyết**: R02, R03, R05, R09, R14
- **Cách làm**: quyền xem dữ liệu nhạy cảm gắn với căn cứ pháp lý cụ thể và phạm vi, không gắn vai trò tĩnh; care team tự sinh grant theo lượt điều trị, hết hạn khi kết thúc hoặc chuyển khoa.
- **Gợi ý dữ liệu**: `access_grant(patient_id, category_code, grantee_user_id | grantee_org_id, legal_basis IN ('HIV_30_2_a',…,'HIV_30_3_d','TRANSPLANT_38_3_HEAD','TRANSPLANT_38_3_COURT','DV_29_1_b',…), scope JSON, granted_by, request_doc_uri, consent_doc_uri, valid_from, valid_to, revoked_at)`; ràng buộc `HIV_30_3_d ⇒ consent_doc_uri NOT NULL`; `HIV_30_3_% ⇒ request_doc_uri NOT NULL`.
- **Đánh đổi**: phức tạp hơn RBAC; cần màn hình quản trị cho KHTH/DPO.

### BAOMAT-CB-P03 — Phá kính có phân loại
- **Giải quyết**: R20
- **Cách làm**: chính sách theo `breakglass_allowed` (FALSE cho danh tính người hiến giao tử, tạng, mẫu giấu tên); cảnh báo realtime cho DPO/ANM thường trực (R27); báo cáo tuần sự kiện chưa duyệt.
- **Gợi ý dữ liệu**: `breakglass_event(user_id, patient_id, category_code, reason_code, reason_text, started_at, expires_at, reviewed_by, reviewed_at, review_result)`.
- **Đánh đổi**: cân bằng an toàn cấp cứu với lạm dụng; đừng để phá kính thành đường tắt mặc định.

### BAOMAT-CB-P04 — Nhật ký truy cập hồ sơ có thời hạn theo HSBA
- **Giải quyết**: R22, R15, R02
- **Cách làm**: phân vùng theo tháng, chỉ-ghi-thêm, chuỗi băm theo ngày; job đêm tính lại `retain_until` khi `retention_class` của HSBA đổi; tách khỏi `security_log` (ANM P3).
- **Gợi ý dữ liệu**: `record_access_log(ts_utc, user_id, role, org_unit, patient_id, encounter_id, record_type, record_id, action, sensitivity_codes[], via IN ('normal','grant','breakglass'), grant_id, breakglass_id, client_ip, device_id, retain_until)`; chỉ mục `(patient_id, ts_utc)`.
- **Đánh đổi**: dung lượng lớn khi giữ 10–30 năm; nén, kho lạnh sau 12 tháng.

### BAOMAT-CB-P05 — Hồ sơ chính sách xuất theo đích (egress profiles)
- **Giải quyết**: R21, R07, R09, R13
- **Cách làm**: mọi bộ sinh dữ liệu xuất (XML, FHIR, PDF) gọi chung hàm `filter(payload, destination)`; kiểm thử hồi quy với bộ dữ liệu mẫu đủ các cờ.
- **Gợi ý dữ liệu**: `egress_policy(category_code, destination IN ('BHYT_XML','SKDT','PATIENT_APP','SMS','REPORT','HTTT_KCB','HIV_INFO','UBND_XA','RESEARCH','PRINT_SUMMARY','REFERRAL'), action IN ('send','mask','drop','consent_required'), legal_basis)`; `disclosure_log(ts, destination, patient_id, categories, legal_basis, payload_hash, sent_by)` (DLCN P04).
- **Đánh đổi**: lọc mù làm thiếu dữ liệu bắt buộc; phải để `send` có căn cứ khi luật cho phép.

### BAOMAT-CB-P06 — Hộp thông báo bắt buộc có đồng hồ
- **Giải quyết**: R04, R07, R09, R10, R18, R19
- **Cách làm**: mỗi nghĩa vụ thông báo là một tác vụ có hạn, bằng chứng gửi, người duyệt; lịch ngày làm việc cho "72 giờ làm việc"; duyệt hai người cho Mẫu 15.
- **Gợi ý dữ liệu**: `mandatory_notice(type IN ('HIV_POS_RESULT','HIV_INFO_REPORT','OST_FORM_11',…,'OST_FORM_16','DRUG_TEST_POS','DV_HEAD_REPORT','CHILD_ABUSE_REPORT'), patient_id, recipient, due_at, due_rule, status, sent_at, evidence_uri, approved_by)`.
- **Đánh đổi**: HIV-INFO, UBND xã chưa có API; cho nhập "đã gửi" thủ công kèm bằng chứng.

### BAOMAT-CB-P07 — Kho danh tính tách biệt cho người hiến
- **Giải quyết**: R12, R14, R08
- **Cách làm**: bảng nghiệp vụ chỉ có token; tra ngược chỉ qua thủ tục có căn cứ (Luật 75 Đ38 k3) và ghi vết; mẫu XN giấu tên không có khóa ngoại tới bệnh nhân ở mức schema.
- **Gợi ý dữ liệu**: `donor_identity(donor_token PK, encrypted_identity, key_id)` ở schema/DB riêng, khóa trong KMS; `UNIQUE(donation_id) WHERE status = 'allocated'`; `anon_sample(anon_sample_id, …)` không có `patient_id`.
- **Đánh đổi**: khó truy vết khi cần thu hồi mẫu; cần quy trình tra ngược khẩn cấp có người đứng đầu ký.

### BAOMAT-CB-P08 — Che giới tính thai ở nguồn
- **Giải quyết**: R13
- **Cách làm**: middleware từ máy siêu âm/LIS loại trường `fetal_sex`, analyte X/Y, kết luận giới tính trong NIPT, QF-PCR, karyotype trước khi lưu vào kho dùng chung; bản gốc ở vùng hạn chế chỉ cho bác sĩ chỉ định có mã bệnh liên quan giới tính (khi BYT ban hành danh mục).
- **Gợi ý dữ liệu**: `blocked_field(source_system, field_code, legal_basis)`; `restricted_result(result_id, reason, allowed_role)`.
- **Đánh đổi**: màn hình máy siêu âm vẫn có thể hiển thị; phần mềm chỉ kiểm soát lưu và xuất.

### BAOMAT-CB-P09 — Bảng mốc tuổi theo hành vi
- **Giải quyết**: R06, R09, R19 (nối DLCN P09)
- **Cách làm**: hàm `consent_requirement(dob, action, at)` đọc bảng có hiệu lực theo thời gian.
- **Gợi ý dữ liệu**: `age_rule(action IN ('HIV_TEST_SELF_CONSENT','HIV_RESULT_PARENT_AFTER_CHILD','OST_ENROLL_REP_CONSENT','CHILD_PRIVATE_INFO_CONSENT','DLCN_CHILD_CONSENT'), min_age, max_age, requires IN ('self','rep','both','self_then_rep'), legal_basis, valid_from, valid_to)`.
- **Đánh đổi**: phải cập nhật khi luật sửa (dự án sửa Luật Trẻ em).

### BAOMAT-CB-P10 — Ký xác nhận bằng xác thực bên ngoài thay vì giữ sinh trắc
- **Giải quyết**: R23–R26
- **Cách làm**: thứ tự ưu tiên (suy luận): (1) xác thực VNeID qua dịch vụ xác thực (mức 3/4) gắn hash phiếu; (2) chữ ký số cá nhân qua CA; (3) OTP SMS số chính chủ; (4) chữ ký tay trên bảng ký + ảnh khi không có cách khác.
- **Gợi ý dữ liệu**: `patient_attestation(document_id, document_hash, method IN ('VNEID_AUTH','CA_SIGNATURE','OTP','HANDWRITTEN_PAD','BIOMETRIC_LOCAL'), assurance_level, provider, provider_txn_id, signer_person_id, representative_relation, ts, evidence_uri, biometric_template_ref NULL)`.
- **Đánh đổi**: phụ thuộc dịch vụ ngoài (mạng, chi phí); vẫn cần dự phòng giấy.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| BAOMAT-CB-A01 | R01 | Danh mục loại nhạy cảm, cơ chế gắn cờ; tạo chỉ định XN HIV, đơn methadone, siêu âm thai, xem cờ tự gắn | Cấu hình, bảng rule | BẮT BUỘC |
| BAOMAT-CB-A02 | R02 | Đăng nhập điều dưỡng khoa khác, thu ngân, admin; tìm người có kết quả HIV dương tính | Ảnh: kết quả bị ẩn; log | BẮT BUỘC |
| BAOMAT-CB-A03 | R02 | In danh sách khoa, phiếu tóm tắt, SMS trả kết quả cho người HIV dương tính | Bản in, SMS không chứa HIV | BẮT BUỘC |
| BAOMAT-CB-A04 | R03 | Luồng đề nghị tiếp cận thông tin; bảng quyền có văn bản đề nghị, đồng ý | Bản ghi grant | BẮT BUỘC |
| BAOMAT-CB-A05 | R04 | Kết quả khẳng định giả lập: Phiếu 03 bản, đồng hồ 72 giờ làm việc, ngoại lệ | Phiếu, cảnh báo | BẮT BUỘC |
| BAOMAT-CB-A06 | R05 | Chuyển khoa người bệnh HIV; quyền khoa cũ/mới; chỉ định CĐHA khoa khác | Log quyền | BẮT BUỘC |
| BAOMAT-CB-A07 | R06 | Chỉ định XN HIV cho người 14 tuổi không có đồng ý; trả kết quả người 16 tuổi | Bị chặn; thứ tự tác vụ | BẮT BUỘC |
| BAOMAT-CB-A08 | R07 | Xuất Phụ lục 1, 2 TT 07 hoặc tích hợp HIV-INFO; `disclosure_log` | File, log | BẮT BUỘC |
| BAOMAT-CB-A09 | R08 | Mẫu giám sát trọng điểm: schema không có khóa ngoại tới bệnh nhân | DDL | BẮT BUỘC |
| BAOMAT-CB-A10 | R09 | Sinh Mẫu 11, 12, 14, 15, 16; đăng ký người 15 tuổi không có đồng ý đại diện | Mẫu in; bị chặn | BẮT BUỘC |
| BAOMAT-CB-A11 | R10 | Phân biệt XN ma túy theo đề nghị với thường quy; trường cơ quan đề nghị | Ảnh, log gửi | BẮT BUỘC |
| BAOMAT-CB-A12 | R11 | Tạo quyết định bắt buộc chữa bệnh; thử ký ra viện trái chỉ định | Bị chặn; ghi nhận thông báo thân nhân | BẮT BUỘC |
| BAOMAT-CB-A13 | R11 | Ghi chép tâm lý trị liệu có bị đẩy sang Sổ SKĐT | Payload | NÊN |
| BAOMAT-CB-A14 | R12 | Hồ sơ người nhận IVF có cột danh tính người hiến; phân bổ một mẫu hiến cho hai người nhận | Truy vấn; lỗi ràng buộc | BẮT BUỘC |
| BAOMAT-CB-A15 | R13 | Kết quả siêu âm có trường giới tính từ máy; bản trên RIS, app, Sổ SKĐT; phiếu NIPT | PDF không có giới tính thai | BẮT BUỘC |
| BAOMAT-CB-A16 | R14 | Bệnh án người nhận tạng có danh tính người hiến; báo cáo ca ghép | Ảnh, báo cáo vô danh | BẮT BUỘC |
| BAOMAT-CB-A17 | R15 | Cấu hình thời hạn loại "ghép tạng" | = 30 năm | BẮT BUỘC |
| BAOMAT-CB-A18 | R18 | Đánh dấu nghi BLGĐ: tác vụ báo người đứng đầu; tài khoản người đại diện trên app | Tác vụ; app không hiện ghi chú | BẮT BUỘC |
| BAOMAT-CB-A19 | R19 | Quy trình dùng ảnh, ca bệnh trẻ em; cờ nghi xâm hại | Mẫu đồng ý 2 chữ ký; tác vụ | BẮT BUỘC |
| BAOMAT-CB-A20 | R20 | Phá kính hồ sơ HIV; thử phá kính xem danh tính người hiến giao tử | Cảnh báo DPO; bị từ chối | BẮT BUỘC? |
| BAOMAT-CB-A21 | R21 | Sinh XML BHYT, gói Sổ SKĐT, payload app cho bộ người bệnh mẫu đủ cờ; so ma trận | Payload; `egress_policy` | BẮT BUỘC |
| BAOMAT-CB-A22 | R22 | Log truy cập cũ nhất còn giữ; cấu hình retention; thử xóa log | Ngày log; lỗi khi xóa | BẮT BUỘC / NÊN |
| BAOMAT-CB-A23 | R22 | Chạy báo cáo "ai đã xem hồ sơ người bệnh X" | Báo cáo | BẮT BUỘC |
| BAOMAT-CB-A24 | R24 | Ký phiếu bằng VNeID: mỗi phiếu có mã giao dịch riêng, mức độ, nhà cung cấp | `patient_attestation` | BẮT BUỘC |
| BAOMAT-CB-A25 | R25 | Nơi lưu ảnh khuôn mặt, vân tay người bệnh; mã hóa, phân quyền | Cấu hình, khóa | BẮT BUỘC |
| BAOMAT-CB-A26 | R26 | Quy chế ký số còn dẫn "Luật 20/2026 sửa Đ22–23" hay NĐ 130/2018 | Văn bản quy chế | NÊN |
| BAOMAT-CB-A27 | R27 | Vai trò ANM thường trực tách quản trị nghiệp vụ; báo cáo phân quyền | Ma trận vai trò | BẮT BUỘC? |
| BAOMAT-CB-A28 | R28 | Hồ sơ sản phẩm có tiêu chuẩn áp dụng, giấy phép lưu hành nước tham chiếu | Hồ sơ | BẮT BUỘC? |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới |
|---|---|---|---|
| 01/07/2021 | Luật 71/2020: Đ30 HIV mới; tuổi tự nguyện XN HIV 15 | Cơ sở XN, BV, PK | Đã qua |
| 01/05/2023 | TT 04/2023; TT 02/2020 hết HL | Cơ sở XN, BV, PK | Đã qua |
| 01/06/2023 | TT 07/2023 (HIV-INFO) | Cơ sở XN, điều trị HIV | Đã qua |
| 01/07/2023 | Luật PCBLGĐ 2022 | BV, PK | Đã qua |
| 15/12/2024 | NĐ 141/2024; NĐ 90/2016, NĐ 108/2007, NĐ 75/2016 hết HL | Cơ sở điều trị thay thế, XN HIV | Đã qua |
| 09/05/2025 | TT 10/2025 bãi bỏ văn bản HIV cũ | — | Đã qua |
| 01/10/2025 | NĐ 207/2025; NĐ 10/2015, NĐ 98/2016 hết HL | Cơ sở IVF, mang thai hộ | Đã qua |
| 01/01/2026 | NĐ 356/2025 (danh mục nhạy cảm) | Tất cả | Đã qua |
| 14/01/2026 | NĐ 15/2026 sửa NĐ 23/2025 | CA | Đã qua |
| 15/02/2026 | TT 47/2025 (bãi bỏ QĐ 2824/2004, TT 22/2024), TT 57/2025, TT 03/2026 HL | Vendor HIS, BV | Đã qua |
| 15/05/2026 | NĐ 90/2026 (HIV, IVF, ghép tạng, giới tính thai) | Tất cả | Đã qua |
| 01/07/2026 | Luật Dân số (Đ6 k3; Luật KCB Đ34 k1 d); Luật Phòng bệnh; TT 117/2026/TT-BCA (thứ cấp) | BV, PK sản, CĐHA, LIS | Đã qua |
| 19/08/2026 | NĐ 329/2026 lực lượng bảo vệ ANM | Chủ quản HTTT | Đã qua |
| 04/10/2026 | Thẩm tra dự án Luật Hiến, lấy, ghép mô (sửa đổi) | Theo dõi | Đã qua |
| 17/10/2026 (dự kiến) | Khai mạc Kỳ họp 2: dự án Luật ĐD&XTĐT; dự án sửa 6 luật (có Luật Trẻ em) | Theo dõi | Sắp tới |
| 01/01/2027 | Phân nhóm TBYT theo TT 57/2025 trong đấu thầu | Vendor SaMD, cơ sở công | Sắp tới |
| 01/03/2027 | Luật 20/2026/QH16 HL (không đụng Đ22–23 GDĐT) | — | Sắp tới |
| 10/04/2027 | Hạn rà soát phần mềm ký số theo NĐ 23 Đ47 k6 (EMR-R07) | Vendor ký số | Sắp tới |
| 15/04/2027 | QCVN 16, 17:2026/BCA HL (chỉ cho CSDL căn cước) | Không áp cho EMR | Sắp tới |
| Chưa có ngày | BYT ban hành danh mục ngoại lệ giới tính thai; CSDL dùng chung hỗ trợ sinh sản và quy định chia sẻ | BYT; sau đó cơ sở IVF, PK sản | Treo |

## 6. Bẫy trích dẫn và chuỗi thay thế

| Cũ | Mới | Từ ngày | Ghi chú |
|---|---|---|---|
| Luật HIV Đ30 bản 2006 (3 khoản); Đ27 k2 "đủ 16 tuổi" | Luật 71/2020 Đ1 k10 (Đ30 mới, 7 khoản); "đủ 15 tuổi" | 01/07/2021 | — |
| TT 02/2020/TT-BYT | TT 04/2023/TT-BYT | 01/05/2023 | — |
| NĐ 108/2007, NĐ 75/2016, NĐ 90/2016 (methadone) | NĐ 141/2024 | 15/12/2024 | Cũng bãi bỏ Đ16 k1–2 NĐ 155/2018, một phần Đ13 NĐ 63/2021 |
| TTLT 03/2010, TT 04/2019, một phần TT 06/2012, TT 01/2015 | Bãi bỏ bởi TT 10/2025 | 09/05/2025 | — |
| NĐ 10/2015 + NĐ 98/2016; Đ19 k2 NĐ 155/2018; NĐ 96 Đ40 k9 | NĐ 207/2025 | 01/10/2025 | NĐ 207 Đ15 k2 |
| Pháp lệnh Dân số 2003 | Luật Dân số 113/2025 | 01/07/2026 | — |
| NĐ 117/2020 | NĐ 90/2026 | 15/05/2026 | — |
| TT 09/2015/TT-BYT, TT 20/2024 | Phần lớn bãi bỏ bởi TT 03/2026 | 15/02/2026 | Còn phần thực phẩm |
| TT 22/2024/TT-BYT; QĐ 2824/2004/QĐ-BYT | Bãi bỏ bởi TT 47/2025 | 15/02/2026 | Văn bản thay TT 22/2024 chưa xác minh |
| NĐ 23/2025 | VBHN 17/2026/VBHN-NĐ-BKHCN (với NĐ 15/2026) | 07/09/2026 | — |
| Luật Căn cước 26/2023 | Sửa bởi Luật 118/2025/QH15 | — | Chưa đọc |

**Bẫy trích dẫn**
1. Trích Luật HIV Đ30 phải dùng bản sau Luật 71/2020 (có k3 về BHXH và cơ sở y tế thanh toán).
2. NĐ 141/2024 khác NĐ 141/2013. Hai NĐ số 90: **NĐ 90/2016** (methadone, hết HL) và **NĐ 90/2026** (xử phạt y tế). Hai NĐ số 165: 165/2025 (Luật Dữ liệu) và 165/2026 (Luật Phòng bệnh).
3. QCVN 16/17:2026/**BCA** là số quy chuẩn; thông tư ban hành là 169/170/2026/**TT-BCA**.
4. TT 04/2023/TT-BYT không có trên vanban.chinhphu.vn; bản gốc lấy từ tulieuvankien.dangcongsan.vn.
5. TT 07/2023, NĐ 141/2024 còn nhắc "cấp huyện", NĐ 96 Đ93 còn nhắc "LĐTBXH": đặc tả dùng tên cơ quan hiện hành, trích nguyên văn thì giữ.
6. NĐ 90/2026 dẫn Pháp lệnh Dân số và Luật PCBTN 2007 làm căn cứ dù hai văn bản này hết HL từ 01/07/2026; hành vi cấm hiện nằm ở Luật Dân số, Luật Phòng bệnh.
7. "Mã hóa" trong Luật 75 Đ38 và NĐ 90 Đ42 không được định nghĩa.
8. TT 117/2026/TT-BCA chỉ có nguồn thứ cấp; đừng trích như gốc.
9. Hành vi cấm của Luật KCB 2023 nằm ở **Đ7**, không phải Đ6: tẩy xóa HSBA là **Đ7 k10**; bắt buộc chữa bệnh sai đối tượng là Đ7 k19.
10. Hồ sơ ghép tạng: 30 năm (Luật 75), không phải 20 năm (TT 33 mục 43).
11. Thời hạn log: đừng trộn con số ANM (90 ngày/3/6/12 tháng tùy đối tượng) với log truy cập HSBA (không có quy định riêng; NÊN bằng thời hạn HSBA, tối thiểu 05 năm).

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. **HIV trên Sổ SKĐT/VNeID**: gửi chẩn đoán, thuốc ARV lên Sổ SKĐT có vi phạm Luật HIV Đ8 k5 không. Hỏi Cục Phòng bệnh và Cục Quản lý KCB.
2. **Mẫu Phiếu kết quả XN HIV dương tính** (Phụ lục TT 04/2023) và trường Phụ lục 1, 2 TT 07/2023 chưa trích chi tiết; đặc tả API HIV-INFO không thấy công bố.
3. **Đích "cấp huyện"** trong HIV-INFO, NĐ 141 sau khi bỏ cấp huyện: chưa có hướng dẫn.
4. **Danh mục ngoại lệ thông báo giới tính thai** (Luật Dân số Đ6 k3): chưa ban hành; đến khi có, chặn tuyệt đối việc trả giới tính thai cho thai phụ.
5. **CSDL dùng chung hỗ trợ sinh sản** (NĐ 207 Đ17 k1 b): chưa thấy văn bản thành lập, đặc tả; NĐ 90 Đ42 k3 d, v đã phạt việc không chia sẻ. Hỏi BYT (Cục Bà mẹ trẻ em hoặc đơn vị kế nhiệm).
6. **NĐ 90/2026 Đ42 k3 q** (theo research là "không thực hiện nguyên tắc vô danh") bị OCR hỏng chữ ở cả hai lượt; các điểm k3 a–p, r–v đã đọc được.
7. **XN ma túy theo Luật PCMT Đ22**: phòng XN BV làm theo đề nghị của công an thì ai gửi kết quả cho Chủ tịch UBND xã; NĐ 109/2021 chưa đọc.
8. **BLGĐ**: nghĩa vụ báo người đứng đầu (Đ29 k2) có kéo theo báo công an/UBND xã không; ngoại lệ với quyền người đại diện khi người đại diện là người gây bạo lực: **cần luật sư**.
9. **BV công có phải "tổ chức cung cấp dịch vụ công"** để kết nối trực tiếp hệ thống ĐD&XT (NĐ 69 Đ18 k1, Đ19 k2): hỏi C06 Bộ Công an.
10. **Luật 118/2025/QH15** sửa Luật Căn cước chưa đọc; **TT 117/2026/TT-BCA** cần bản gốc.
11. **Xác định lại giới tính**: văn bản gốc của nghĩa vụ giữ bí mật (R16) chưa đọc.
12. **Văn bản thay TT 22/2024/TT-BYT** (thanh toán trực tiếp BHYT) sau khi bị TT 47/2025 bãi bỏ: chuyển BHYT-GD kiểm.
13. **QĐ 1250/QĐ-TTg (YHCT)** và **NĐ 13/2026/NĐ-CP (thống kê)**: chỉ gốc-meta.
14. **Thời hạn lưu nhật ký truy cập HSBA** (R22): mức NÊN là suy luận; hỏi BYT (Cục Quản lý KCB hoặc Trung tâm Thông tin y tế quốc gia) hoặc theo dõi Luật ĐD&XTĐT tại Kỳ họp 2.
15. **Dự thảo Luật Hiến, lấy, ghép mô (sửa đổi)**: nội dung CSDL, phân quyền mới chỉ qua báo; khi thông qua có thể thay R14, R15.
