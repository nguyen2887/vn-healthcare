# BHYT-DATA — Chuẩn dữ liệu đầu ra XML BHYT và bộ mã danh mục dùng chung

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám có hợp đồng KCB BHYT; vendor HIS/CIS · Research gốc: `research/deep/BHYT-DATA.md`

Không phải ý kiến pháp lý. Phạm vi: bộ bảng XML (QĐ 130 → 4750 → 3176 → 1931/2026), định dạng trường, ký số file XML, bộ mã dùng chung (QĐ 7603 và các QĐ sửa theo phụ lục), danh mục sử dụng tại cơ sở (TT 12/2026 Mẫu 01–06/DM), bảng kê 01/KBCB (QĐ 697/2026). Quy trình giám định, thời hạn, quyết toán, xử phạt → **BHYT-GD**. Quy tắc mã hóa ICD-10 → **MA-LT**. Giấy tờ BHXH → **GIAYTO**.

## Tóm tắt nhanh

- Bộ đang chạy trên Cổng là **QĐ 130 sửa bởi 4750 và 3176**, cộng QĐ 1931/QĐ-BYT **ngày 29/06/2026** (từ 01/07/2026: `MUC_HUONG` 4 ký tự, quy tắc `SO_DANG_KY` thuốc hiếm). Mỗi QĐ là bản vá chồng lên bản trước; không trích "QĐ 130" đơn lẻ.
- Danh mục dùng chung bị **bãi bỏ theo phụ lục**, không theo cả quyết định: QĐ 1804/2026 chỉ bỏ PL1 QĐ 824 và PL6 QĐ 2010 (từ 01/08/2026); QĐ 3276/2025 bỏ PL5 QĐ 824 và PL5 QĐ 2010.
- Mốc vừa qua phải đã xong: 01/07/2026 (ICD-10 TT 06/2026, bảng kê QĐ 697, `MUC_HUONG` 4 ký tự); 01/08/2026 (16 mã loại hình KCB, 61 dòng mã khoa QĐ 1804).
- Sắp tới: **07/10/2026** hết góp ý dự thảo thay TT 48/2017; dự kiến **01/01/2027** gửi dữ liệu ≤ 03 giờ (dự thảo, chưa ban hành). Kiến trúc gửi lô cuối ngày sẽ không đạt.
- Ký số file XML (`<CHUKYDONVI>`, SHA256, chứng thư đã đăng ký trên Cổng) bắt buộc chậm nhất từ 01/01/2026.
- Bẫy kiểu dữ liệu: `MA_LOAI_KCB` và `MA_DOITUONG_KCB` là **chuỗi** (giữ "01", "1.11"); XLSX 2023 còn ghi "Số". Tên trường đúng là `MA_DOITUONG_KCB`.
- ICD-10 cột 26 bị cấm ở **mọi vị trí**, cột 27 chỉ dùng cho nguyên nhân tử vong — không chỉ chặn ở bệnh chính.
- Danh mục cơ sở thay đổi theo kiểu "đóng dòng cũ, mở dòng mới" (TT 12 Mẫu 01/DM); không update-in-place.

## Mục lục

| ID | Tiêu đề |
|---|---|
| BHYT-DATA-R01 | Sinh đủ bộ bảng XML hiện hành |
| BHYT-DATA-R02 | Định dạng chung của file |
| BHYT-DATA-R03 | Bảng check-in XML0 |
| BHYT-DATA-R04 | Lưu kết quả tra cứu thẻ làm đầu vào dữ liệu |
| BHYT-DATA-R05 | Thời hạn gửi dữ liệu (tóm tắt; chủ ở BHYT-GD) |
| BHYT-DATA-R06 | Hiệu chỉnh, gửi lại, thay thế hồ sơ |
| BHYT-DATA-R07 | Ký số file XML, đăng ký chứng thư trên Cổng |
| BHYT-DATA-R08 | Quy tắc định dạng trường |
| BHYT-DATA-R09 | Khóa liên kết `MA_LK` và đánh số |
| BHYT-DATA-R10 | Quy tắc tính tiền |
| BHYT-DATA-R11 | `MUC_HUONG` 4 ký tự và mức hưởng |
| BHYT-DATA-R12 | `SO_DANG_KY` thuốc hiếm nhập khẩu theo giấy phép tỉnh |
| BHYT-DATA-R13 | Chỉ dùng bộ mã dùng chung BYT |
| BHYT-DATA-R14 | Mã loại hình KCB (QĐ 1804, 16 mã) |
| BHYT-DATA-R15 | Mã khoa (QĐ 1804 PL02) |
| BHYT-DATA-R16 | Mã đối tượng KCB, mã nhiên liệu (QĐ 3276) |
| BHYT-DATA-R17 | Mã DVKT, khám, giường, chỉ số CLS |
| BHYT-DATA-R18 | Mã thuốc, VTYT/TBYT, máu, thầu |
| BHYT-DATA-R19 | Danh mục sử dụng tại cơ sở (Mẫu 01–06/DM) |
| BHYT-DATA-R20 | ICD-10 TT 06/2026 trong dữ liệu đầu ra |
| BHYT-DATA-R21 | Bảng kê 01/KBCB theo QĐ 697 |
| BHYT-DATA-R22 | Phương thức kết nối và lưu biên nhận |
| BHYT-DATA-R23 | Chuyển đổi phiên bản chuẩn theo mốc |
| BHYT-DATA-R24 | Mã cơ sở KCB và thay đổi tổ chức |
| BHYT-DATA-R25 | Bảo mật dữ liệu trích chuyển |
| BHYT-DATA-R26 | Chứng từ BHXH trong bộ XML |

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 130/QĐ-BYT (18/01/2023) | Chuẩn và định dạng dữ liệu đầu ra; 13 bảng; thay QĐ 4210/2017 | Mốc chính thức 01/09/2023 đã bị QĐ 4750 dời | Còn HL, đã sửa bởi 4750, 3176, 1931/2026 | gốc-OCR (không dấu; số, ngày rõ) | [PDF QĐ, SYT Quảng Ninh](http://soytequangninh.gov.vn/upload/1002610/20230131/130Q__signed_7a47686ff6.pdf) · [trang tin kèm XLSX bảng chỉ tiêu 2023](http://soytequangninh.gov.vn/menu-second/iso-9001-2008/cong-khai-tai-chinh2/cac-du-toan-va-quyet-toan-tai-chinh/trien-khai-quyet-dinh-so-130-qd-byt-ngay-18-01-2023-cua-bo-y.html) |
| 4750/QĐ-BYT (29/12/2023) | Thay toàn bộ bảng chỉ tiêu; định nghĩa lại check-in | Kiểm thử 01/04/2024; chính thức 01/07/2024; QĐ 4210 hết HL 01/07/2024 | Còn HL | gốc-ảnh (Đ1–Đ4, một phần phụ lục) | [PDF, BVĐK Bạc Liêu](http://bvdkbaclieu.gov.vn/upload/1000079/20240107/252QUY_1_c1005feda7.pdf) |
| 3176/QĐ-BYT (29/10/2024) | Sửa **tạm thời** bảng chỉ tiêu 4750 | Đồng bộ 01/01/2025 | Còn HL; Cổng gọi endpoint `...QD3176` | thứ cấp (thân QĐ); phụ lục chưa đọc gốc | [caselaw, thứ cấp](https://caselaw.vn/van-ban-phap-luat/508520-quyet-dinh-so-3176-qd-byt-ngay-29-10-2024-cua-bo-truong-bo-y-te-sua-doi-quyet-dinh-4750-qd-byt-sua-doi-quyet-dinh-130-qd-byt-quy-dinh-chuan-va-dinh-dang-du-lieu-dau-ra-phuc-vu-viec-quan-ly-giam-dinh-thanh-toan-chi-phi-kham-benh-chua-benh-va-giai-quyet-cac-che-do-lien-quan) |
| 1931/QĐ-BYT **ngày 29/06/2026** (≠ QĐ 1931/QĐ-BYT năm 2016) | Sửa chuẩn: `MUC_HUONG` ≤ 4 ký tự; `SO_DANG_KY` thuốc hiếm UBND tỉnh cấp phép nhập | 01/07/2026 | Còn HL (theo nguồn duy nhất) | thứ cấp, 1 nguồn báo | [suckhoetreem (báo, bối cảnh)](https://suckhoetreem.vn/cuoc-song-so/cap-nhat-chuan-du-lieu-phuc-vu-giam-dinh-kham-chua-benh-va-thanh-toan-bhyt-tu-01-7-2026-131048.html) |
| CV …/BHXH-CNTT + "Phụ lục 01 Hướng dẫn liên thông dữ liệu theo QĐ 3176" (tên file ghi ký số 07012026) | Đăng ký chứng thư, API check-in và gửi XML, cấu trúc XML0–XML15, `CHUKYDONVI` SHA256 | 2026 | Hướng dẫn kỹ thuật BHXH, không phải QPPL; số hiệu CV chưa xác minh | gốc (PDF có text, đăng lại) | [PDF, UBND xã Khánh Cường](https://khanhcuong.quangngai.gov.vn/upload/2007018/20260128/PL01_li%C3%AAn%20th%C3%B4ng%20d%E1%BB%AF%20li%E1%BB%87u_3176_k%C3%BD%20s%E1%BB%91_07012026%20(1).pdf) |
| 48/2017/TT-BYT (28/12/2017) | Trích chuyển dữ liệu điện tử KCB BHYT | 01/03/2018 | Còn HL; có dự thảo thay dự kiến 01/01/2027 | gốc-ảnh (Đ2–Đ8), gốc-OCR (Đ9–Đ15) | [PDF ký số BYT, SYT Hà Tĩnh](https://soyte.hatinh.gov.vn/upload/1000030/20171027/4e5899d541ea00e83dd2fce1579631cdtt-2017-48-1_1.pdf) |
| 7603/QĐ-BYT (**25/12/2018**) | Bộ mã danh mục dùng chung phiên bản 6 (11 danh mục); thay QĐ 6061 | 15/01/2019 | Còn HL một phần: PL01–04 bị QĐ 2010 bỏ; PL11 dùng tạm cho chỉ số CLS chưa có trong QĐ 1227 | gốc (qua QĐ 2010, TT 12) | link chưa kiểm tra được (trang tin BHXH VN từ chối truy cập khi kiểm tra 2026-10-06) |
| 824/QĐ-BYT (15/02/2023) | Bổ sung 6 danh mục | — | Còn HL một phần: PL1 bỏ từ 01/08/2026 (QĐ 1804); PL2 bỏ (QĐ 2010); PL5 bỏ (QĐ 3276); PL3, 4, 6 chưa thấy bị bỏ | gốc (qua lệnh bãi bỏ); nội dung PL3, 4, 6 chưa mở | link chưa kiểm tra được |
| 2010/QĐ-BYT (19/06/2025) | Tạm thời 6 danh mục: DVKT, khám, giường, ngày giường ban ngày, đối tượng, mã khoa | Cập nhật chậm nhất 01/08/2025 | Còn HL một phần: PL5 bỏ (QĐ 3276); PL6 bỏ từ 01/08/2026 (QĐ 1804) | gốc | [PDF, BVĐK Bạc Liêu](https://bvdkbaclieu.gov.vn/upload/1000079/20250715/583_Quyet_dinh-2010-QD-BYT_256a10e6ec.pdf) |
| 3276/QĐ-BYT (17/10/2025) | Mã đối tượng đến KCB (27 dòng, kèm `MUC_HUONG`), mã nhiên liệu | Ký; gửi lại hồ sơ từ 01/07/2025; chuyển tiếp đến 31/12/2025 | Còn HL | gốc | [PDF](https://xdcs.cdnchinhphu.vn/446259493575335936/2025/10/27/3276-1761531834581496757967.pdf) |
| 1804/QĐ-BYT (19/06/2026) | Mã loại hình KCB (16), mã khoa (61 dòng) | Chậm nhất 01/08/2026 | Còn HL | gốc | [PDF đính kèm tin BHXH](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26715/QD%201804%20BYT.pdf) |
| 1227/QĐ-BYT (11/04/2025) | Mã kỹ thuật, thuật ngữ chỉ số CLS (đợt 1) | Ký | Còn HL; QĐ 2010 Đ3 buộc dùng cho XML4 | gốc (dẫn chiếu); nội dung chưa đọc | link chưa kiểm tra được |
| 697/QĐ-BYT (19/03/2026) | Mẫu bảng kê chi phí KCB + phụ lục hướng dẫn; thay QĐ 6556/2018 | Nâng cấp phần mềm chậm nhất 01/07/2026 | Còn HL | gốc | [PDF QĐ (file tên "QĐ 967.pdf")](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26339/Q%C4%90%20967.pdf) · [PDF phụ lục](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26339/PL%20huong%20dan.pdf) |
| 12/2026/TT-BTC (10/02/2026) | Giám định, biểu mẫu thanh toán (phần dữ liệu: Đ5 k1, Đ7, Đ8, Đ9 k1, PL II Mẫu 01–06/DM) | Xem BHYT-GD | Còn HL | gốc-ảnh | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-btc.pdf) |
| 06/2026/TT-BYT (02/04/2026) | Mã hóa bệnh tật, nguyên nhân tử vong ICD-10 | 01/07/2026; Đ5 k2, k3 từ 01/06/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf) |
| 188/2025/NĐ-CP | Hướng dẫn Luật BHYT (Đ68 k1, k5; Đ69 k8 d, k9; Đ70) | 15/08/2025 (một số điều 01/07/2025) | Còn HL | gốc-ảnh | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/188-ndcp.signed.pdf) |
| Dự thảo TT thay TT 48/2017 | Bộ mã, chuẩn dữ liệu, ký số; gửi ≤ 03 giờ; 15 ngày đối chiếu | Góp ý đến 07/10/2026; dự kiến 01/01/2027 | **Dự thảo** | thứ cấp | [vtv (báo, bối cảnh)](https://vtv.vn/de-xuat-co-so-y-te-phai-gui-du-lieu-bhyt-trong-vong-3-gio-sau-kham-cham-nhieu-lan-co-the-bi-xu-phat-100261001082022915.htm) |

Văn bản phụ được dẫn trong bản gốc (chưa đọc riêng): QĐ 4905/2019, QĐ 5937/2021 (PL6 mã nhóm thầu còn được XML2 dẫn), QĐ 5086/2021 (nguyên tắc mã VTYT), QĐ 4469/2020 (ICD cũ), QĐ 34/2020/QĐ-TTg (nghề nghiệp), TT 07/2016/TT-BCA và QĐ 124/2004/QĐ-TTg (đơn vị hành chính), TT 23/2024 (danh mục kỹ thuật, gốc mã DVKT).

## 2. Yêu cầu

### BHYT-DATA-R01 — Sinh đủ bộ bảng XML hiện hành
- **Căn cứ**: QĐ 130 Đ1 (13 bảng, UTF-8, XML), thay bảng bởi QĐ 4750 Đ1, sửa tạm thời bởi QĐ 3176 Đ1; TT 12/2026 Đ5 k1 a (Bảng kê chi tiết đề nghị thanh toán lập theo chuẩn 130 sửa bởi 4750, 3176). Bộ Cổng nhận (hướng dẫn BHXH mục 2.4, 3.4, 3.5): XML0 check-in; XML1 tổng hợp; XML2 thuốc; XML3 DVKT và VTYT; XML4 CLS; XML5 diễn biến lâm sàng; XML6 HSBA HIV/AIDS; XML7 giấy ra viện; XML8 tóm tắt HSBA; XML9 giấy chứng sinh; XML10 nghỉ dưỡng thai; XML11 nghỉ việc hưởng BHXH; XML13 giấy chuyển tuyến; XML14 giấy hẹn khám lại; XML15 điều trị lao. XML12 (giám định y khoa) nhập trực tiếp trên Cổng, không qua HIS (QĐ 130 Đ3 k3).
- **Áp dụng**: cơ sở KCB BHYT, vendor HIS · **Hiệu lực/hạn**: 4750 từ 01/07/2024; 3176 từ 01/01/2025; 1931 từ 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh từng bảng từ dữ liệu lâm sàng và viện phí; chỉ đính kèm bảng liên quan theo loại lượt (XML4 khi có CLS; XML5 khi `MA_LOAI_KCB` thuộc nhóm điều trị; XML8 khi nội trú, nội trú ban ngày, lưu TYT/PKĐKKV); đóng gói `GIAMDINHHS/THONGTINHOSO/DANHSACHHOSO/HOSO/FILEHOSO{LOAIHOSO, NOIDUNGFILE}` với `NOIDUNGFILE` base64; mỗi lần gửi `fileHSBase64` là một hồ sơ KCB.
- **Bẫy**: tên thẻ thực tế lấy theo tài liệu BHXH (ví dụ `TONG_HOP`, `CHITIEU_CHITIET_THUOC/DSACH_CHI_TIET_THUOC/CHI_TIET_THUOC`), không theo tên tiếng Việt. Bản 3176 thêm vào XML1 `NHOM_MAU`; XML2 `NGAY_TH_YL`; XML0 `NGAY_VAO_NOI_TRU`, `LY_DO_VNT`, `MA_LY_DO_VNT`, `MA_THUOC`, `TEN_THUOC`, `MA_VAT_TU`, `TEN_VAT_TU`; XML6 thêm 16 trường; XML7, 9, 10, 11 thêm `DU_PHONG` (kích thước từng trường 3176 chưa đối chiếu gốc). XML6 còn phải gửi Cổng HMED `dieutri.arv.vn` theo ghi chú bản 2023 (chưa rõ còn áp dụng).

### BHYT-DATA-R02 — Định dạng chung của file
- **Căn cứ**: TT 48/2017 Đ4 k3 a, b (XML, UTF-8; mỗi hồ sơ một đợt KCB, kể cả người có từ hai thẻ trong đợt); QĐ 130 Đ1.
- **Áp dụng**: như R01 · **Hiệu lực/hạn**: 01/03/2018
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: xuất UTF-8 có khai báo `encoding="utf-8"`, escape ký tự đặc biệt; gom mọi thẻ BHYT của đợt vào cùng hồ sơ.
- **Bẫy**: TT 48 cho một file nhiều hồ sơ, nhưng API BHXH hiện tại yêu cầu mỗi file một hồ sơ (hướng dẫn mục 3.2). Thiết kế theo API, giữ khả năng đóng lô.

### BHYT-DATA-R03 — Bảng check-in XML0
- **Căn cứ**: QĐ 130 Đ3 k1 sửa bởi QĐ 4750 Đ2 k2: gửi ngay sau khi phát sinh chi phí KCB đầu tiên; khi chỉ định nội trú, ban ngày, ngoại trú thì gửi ngay sau chi phí đầu tiên tại khoa điều trị đó; không cần gửi khi cấp cứu (`MA_DOITUONG_KCB = 2`) hoặc cơ sở chỉ nhận người bệnh/mẫu để làm CLS. QĐ 130 Đ2 k1 sửa bởi 4750 Đ2 k1: check-in chỉ thông báo trạng thái, không là căn cứ giám định, thanh toán.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/07/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bắt sự kiện "chi phí đầu tiên của lượt" và "chi phí đầu tiên tại khoa điều trị" để gửi XML0 (`api/qd130/checkInKcbQd3176`, `loaiHoSo = 0`); điền dịch vụ/thuốc/vật tư đầu tiên và `NGAY_YL`; luật miễn theo mã đối tượng 2 và loại cơ sở chỉ làm CLS; lưu `maGiaoDich`.
- **Bẫy**: căn cứ miễn trong 4750 dẫn NĐ 146/2018 và TT 30/2020, nay bị NĐ 188/2025 và TT 01/2025 thay; mã cấp cứu vẫn là "2" (QĐ 3276), nhưng căn cứ của trường hợp "chỉ làm CLS" cần xác minh lại.

### BHYT-DATA-R04 — Lưu kết quả tra cứu thẻ làm đầu vào dữ liệu
- **Căn cứ**: QĐ 4750 diễn giải `MA_THE_BHYT` (tra cứu trên Cổng khi tiếp đón; cấp cứu tra trước khi ra viện; thẻ QN, HC, LS, XK, CY, CA tra hạn; chưa có thẻ dùng chức năng thẻ tạm trẻ em/người hiến tạng); TT 48 Đ13 k2; QĐ 697 PL Phần Một mục III (thông tin hành chính lấy từ Cổng; tra ra từ 02 mã thẻ thì dùng mã có hạn phù hợp thời điểm đến KCB).
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu nguyên phản hồi tra cứu (thời điểm, mã thẻ, hạn thẻ, mức hưởng, thời điểm đủ 5 năm liên tục, cùng chi trả lũy kế); cập nhật khi BHXH sửa thông tin hành chính trong đợt; chọn mã thẻ theo thời điểm đến khám.
- **Bẫy**: luồng nghiệp vụ tra cứu (3 thời điểm, Cổng lỗi, xuất trình muộn) do **BHYT-GD-R01–R03** làm chủ; ở đây chỉ phần dữ liệu cấp cho bảng kê (mục 16–18 mẫu 697) và `MUC_HUONG`.

### BHYT-DATA-R05 — Thời hạn gửi dữ liệu
- **Căn cứ**: TT 48 Đ6 k1 (gửi "ngay sau khi kết thúc lần khám bệnh hoặc kết thúc đợt điều trị ngoại trú hoặc kết thúc đợt điều trị nội trú"), Đ7 k1 (07 ngày làm việc hiệu chỉnh, xác thực, gửi đề nghị thanh toán; phát sinh cuối tháng, quý, năm gửi trước ngày 05 tháng kế tiếp), Đ8 (gửi chậm khi sự cố), Đ13 k7, k8. TT 12 Đ9 k1 dẫn lại.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: hiện hành; dự thảo ≤ 03 giờ từ 01/01/2027 (chưa ban hành)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tự gửi khi đóng lượt; bộ đếm hạn theo lịch làm việc; ghi sự cố mất kết nối làm bằng chứng. Chi tiết: **xem BHYT-GD-R19, R20, R21, R34**.
- **Bẫy**: TT 48 không định nghĩa "ngay sau" bằng giờ; thiết kế hàng đợi gần thời gian thực ngay từ giờ (P04).

### BHYT-DATA-R06 — Hiệu chỉnh, gửi lại, thay thế hồ sơ
- **Căn cứ**: TT 48 Đ7 k1 a, Đ13 k9 (hiệu chỉnh dữ liệu đã gửi phải nêu lý do, thống nhất với BHXH); QĐ 130 Bảng 1 `NGAY_TTOAN` (ra viện chưa thanh toán để trống, thanh toán xong bổ sung và gửi lại); QĐ 3276 Đ2 (gửi lại theo mã đối tượng mới cho dữ liệu từ 01/07/2025); QĐ 3176 Đ2 k1 đ (cửa sổ thay thế 01/07–31/12/2024); TT 12 Đ9 k3 (02 ngày làm việc gửi bản điều chỉnh sau phản hồi lỗi).
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tái sinh XML của một `MA_LK` đã gửi với lý do bắt buộc, giữ mọi phiên bản đã gửi; tự bổ sung `NGAY_TTOAN` và gửi lại; đọc lỗi theo từng trường từng bảng (TT 48 Đ7 k3 c) và mở việc có hạn 02 ngày làm việc (BHYT-GD-R22).
- **Bẫy**: tái sinh hồ sơ cũ dùng **đúng phiên bản chuẩn và danh mục tại thời điểm KCB**, trừ khi văn bản yêu cầu áp mã mới (như QĐ 3276). Đây là lý do cần P01, P02.

### BHYT-DATA-R07 — Ký số file XML, đăng ký chứng thư trên Cổng
- **Căn cứ**: TT 12/2026 Đ9 k1 (hồ sơ đề nghị thanh toán "được ký số xác thực theo quy định tại điểm c khoản 2 Điều 35 và khoản 9 Điều 69" NĐ 188); NĐ 188 Đ69 k9 ("Việc triển khai xác thực dữ liệu điện tử chi phí khám bệnh, chữa bệnh bảo hiểm y tế thực hiện chậm nhất từ ngày 01 tháng 01 năm 2026."); TT 48 Đ7 k1 b, Đ13 k4. Kỹ thuật (hướng dẫn BHXH mục I, 2.4, 3.4): đăng ký chứng thư tại Quản trị hệ thống → Danh mục chứng thư số trên `gdbhyt.baohiemxahoi.gov.vn` (tài khoản quyền AD); thẻ `<CHUKYDONVI>` cuối file, SHA256, chi tiết theo XSD ở mục Trợ giúp/Tài liệu của Cổng.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: chậm nhất 01/01/2026
- **Mức**: BẮT BUỘC (nghĩa vụ ký) · BẮT BUỘC? (chi tiết kỹ thuật theo hướng dẫn BHXH chưa rõ số hiệu)
- **Phần mềm phải**: ký XML0 và file hồ sơ bằng chứng thư cơ sở đã đăng ký; kiểm hạn, trạng thái chứng thư trước khi ký; ghi ai, khi nào, chứng thư nào ký hồ sơ nào.
- **Bẫy**: tài liệu BHXH mục 3.4 chép nhầm câu phạm vi ký của mục 2.4 (thẻ `<CHI_TIEU_TRANG_THAI_KCB>`) cho file `GIAMDINHHS`: phạm vi ký thực tế lấy từ XSD. Định dạng chữ ký (XMLDSig enveloped?) chưa rõ (suy luận). "Xác thực dữ liệu" là ký số hồ sơ chi phí, không phải xác thực sinh trắc người bệnh (xem BHYT-GD-R18).

### BHYT-DATA-R08 — Quy tắc định dạng trường
- **Căn cứ**: bảng chỉ tiêu QĐ 130 (2023) và các bản sửa: thời điểm `yyyymmddHHMM` 12 ký tự (`NGAY_VAO`, `NGAY_RA`, `NGAY_YL`, `NGAY_TTOAN`, `NGAY_SINH`); ngày `yyyymmdd` 8 ký tự (`GT_THE_TU`, `GT_THE_DEN`); `NGAY_SINH` thiếu giờ phút ghi `0000`, thiếu ngày tháng ghi `0000`, trẻ ≤ 28 ngày ghi đủ giờ phút; thập phân dùng "."; nhiều giá trị phân cách ";" (`MA_BENH_KT`, `MA_KHOA`, `MA_GIUONG`, `MA_BAC_SI`); `SO_DANG_KY` không khoảng trắng. QĐ 4750 (check-in): `MA_LOAI_KCB` đổi sang chuỗi; `MA_DOITUONG_KCB` chuỗi tối đa 4 ký tự; thêm `NGAY_VAO_NOI_TRU` 12 ký tự. QĐ 697 PL III.1: `GIOI_TINH` Nam 1, Nữ 2, Chưa xác định 3.
- **Áp dụng**: như R01 · **Hiệu lực/hạn**: theo phiên bản chuẩn
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kiểm kiểu, độ dài, mẫu định dạng từng trường theo phiên bản đang áp dụng trước khi gửi; lưu mã dạng chuỗi (giữ "01", "1.11").
- **Bẫy**: XLSX 2023 để `MA_LOAI_KCB` "Số" và `MA_DOITUONG_KCB` "Số, 1" — đọc theo đó sẽ rơi số 0, cắt "1.11". Lấy XSD trên Cổng làm chuẩn kiểm.

### BHYT-DATA-R09 — Khóa liên kết `MA_LK` và đánh số
- **Căn cứ**: QĐ 130: `MA_LK` chuỗi ≤ 100, mã đợt điều trị duy nhất, liên kết XML1 với các bảng; `STT` tăng từ 1 trong một lần gửi; `MA_HSBA` ≤ 100. QĐ 697 PL II.3–4: "Số khám bệnh" = `MA_LK`, "Mã số người bệnh" = `MA_BN`.
- **Áp dụng**: như R01 · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấp `MA_LK` duy nhất, bất biến mỗi đợt, không đổi khi gửi lại; mọi dòng XML2–XML15 mang đúng `MA_LK` của XML1.

### BHYT-DATA-R10 — Quy tắc tính tiền
- **Căn cứ**: QĐ 130 Bảng 2: `DON_GIA` làm tròn 3 chữ số thập phân; `THANH_TIEN_BV = SO_LUONG * DON_GIA` làm tròn 2 chữ số; Bảng 1: `T_TONGCHI_BV` = tổng `THANH_TIEN_BV` của XML2 và XML3. TT 12 Đ5 k2 (khớp giữa Bảng kê chi tiết, Bảng tổng hợp, Báo cáo quyết toán, HSBA).
- **Áp dụng**: như R01 · **Hiệu lực/hạn**: hiện hành (công thức bản 3176 chưa đối chiếu gốc)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dùng kiểu thập phân chính xác (không float nhị phân), đúng thứ tự làm tròn; kiểm tổng XML1 = tổng chi tiết trước khi gửi.
- **Bẫy**: bảng kê tính bằng đồng (697 Phần IV.1) nhưng đơn giá XML có thập phân; không ép integer cho đơn giá.

### BHYT-DATA-R11 — `MUC_HUONG` 4 ký tự và mức hưởng
- **Căn cứ**: QĐ 1931/QĐ-BYT ngày 29/06/2026 (thứ cấp): `MUC_HUONG` tối đa 04 ký tự từ 01/07/2026. QĐ 3276 PL1 cột `MUC_HUONG` theo mã đối tượng (1.13, 1.14, 1.18: từ 01/07/2026 hưởng 50%; 3.1: 40% nội trú, 0% ngoại trú). QĐ 697 PL IV.2 (mức hưởng sau khi nhân mức theo nhóm đối tượng với mức theo Luật BHYT). Bảng 2023: `MUC_HUONG` "Số, 3".
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC? (bản gốc 1931 chưa đọc)
- **Phần mềm phải**: lưu và xuất `MUC_HUONG` 4 ký tự ở XML2, XML3; tính mức hưởng = mức theo thẻ × tỷ lệ theo mã đối tượng, theo ngày; tách chi phí theo từng mức hưởng khi một đợt có hai mức. Quy tắc tỷ lệ hưởng theo cấp CMKT: xem BHYT-GD-R10.
- **Bẫy**: 4 ký tự có thể để chứa giá trị thập phân (95 × 50% = 47.5) (suy luận); xác nhận với bản gốc 1931.

### BHYT-DATA-R12 — `SO_DANG_KY` thuốc hiếm nhập khẩu theo giấy phép tỉnh
- **Căn cứ**: QĐ 1931/2026 (thứ cấp): bổ sung quy tắc ghi `SO_DANG_KY` cho thuốc hiếm UBND cấp tỉnh cấp phép nhập. Bảng 2023: số đăng ký lưu hành, không khoảng trắng; dược liệu nhập khẩu ghi số C/O; dược liệu GACP ghi số giấy chứng nhận GACP.
- **Áp dụng**: cơ sở dùng thuốc loại này · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: danh mục thuốc có trường "loại căn cứ lưu hành" (SĐK, C/O, GACP, giấy phép nhập khẩu tỉnh…) và sinh `SO_DANG_KY` theo quy tắc tương ứng.
- **Bẫy**: quy tắc mã cụ thể chưa xác minh; không tự chế định dạng.

### BHYT-DATA-R13 — Chỉ dùng bộ mã dùng chung BYT
- **Căn cứ**: NĐ 188 Đ68 k1; TT 48 Đ4 k2, Đ13 k1; TT 12/2026 Đ7 k1 a (QĐ 7603 sửa bởi 4905/2019, 5937/2021, 824/2023, 2010/2025, 3276/2025); QĐ 1804/2026 ban hành sau TT 12.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kho danh mục nạp từ nguồn chính thức, mỗi mã có nguồn (số QĐ, phụ lục), ngày hiệu lực, ngày bãi bỏ; ánh xạ danh mục nội bộ; chặn gửi hồ sơ có mã không tồn tại tại thời điểm áp dụng.
- **Bẫy**: bãi bỏ theo phụ lục (mục 6). Danh sách trong TT 12 Đ7 chưa có QĐ 1804.

### BHYT-DATA-R14 — Mã loại hình KCB (QĐ 1804, 16 mã)
- **Căn cứ**: QĐ 1804/2026 Đ1 k1, PL01; Đ2 (chậm nhất 01/08/2026; bỏ PL1 QĐ 824). Mã: 01 Khám bệnh; 02 Điều trị ngoại trú (bệnh không thuộc PL I TT 25/2025); 03 Nội trú (dưới 4 giờ dùng 09); 04 Điều trị ban ngày; 05 Ngoại trú bệnh dài ngày có khám và lĩnh thuốc (có DVKT thì dùng 08); 06 Lưu tại PKĐK, PKĐKKV, nhà hộ sinh, trạm y tế; 07 Nhận thuốc theo hẹn; 08 Ngoại trú bệnh dài ngày có khám, DVKT và/hoặc thuốc; 09 Nội trú dưới 04 giờ; 10 Khác; 11 KCB lưu động (trừ tại nhà); 12 KCB tại nhà; 13 Y học gia đình; 14 KCB từ xa; 15 Khám sức khỏe định kỳ; 16 Khám sàng lọc (15, 16 với BHYT chỉ dùng khi có quy định cho Quỹ thanh toán).
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/08/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dùng đúng 16 mã; kiểm chéo: nội trú < 4 giờ → 09; mã 05 không kèm DVKT; mã 11 không dùng cho KCB tại nhà.
- **Bẫy**: mã 12, 14 tồn tại trong khi quy định thanh toán BHYT cho KCB tại nhà, từ xa còn là dự thảo — có mã không có nghĩa là Quỹ trả (xem TELE).

### BHYT-DATA-R15 — Mã khoa (QĐ 1804 PL02)
- **Căn cứ**: QĐ 1804 PL02: 61 dòng (K01–K60 và K99 "Khoa điều trị bệnh truyền nhiễm nhóm A") cùng mã con K16.1–K16.3, K22.1, K59.1–K59.2. Ghi chú: liên chuyên khoa ghi `Kxxyyzz…`; khoa tách sâu `KXY.Z`; đơn nguyên = mã khoa + ".D" + 2 số (ví dụ K02.D35); tên không trùng thì chọn 01 mã phù hợp nhất; không có K32 thì dùng K33; "Khoa" gồm Khoa/Trung tâm/Viện/Đơn nguyên. TT 12 PL II Mẫu 01/DM `MA_KHOA` chuỗi 50 (ví dụ "K0809", "K02.D35"). QĐ 2010 PL6 bị bỏ từ 01/08/2026.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/08/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục khoa nội bộ ánh xạ sang mã QĐ 1804 theo cú pháp trên (kiểm bằng regex); `MA_KHOA` XML1 ghi lần lượt các khoa đã điều trị, phân cách ";".
- **Bẫy**: không phải "60 mã K01–K60"; có thêm K99 và mã con. K51–K60 không theo quy chế cũ: lấy danh mục làm chuẩn.

### BHYT-DATA-R16 — Mã đối tượng KCB, mã nhiên liệu (QĐ 3276)
- **Căn cứ**: QĐ 3276/2025 Đ1, PL1 (27 dòng: 1.1–1.7, 1.11–1.18, 2, 3.1, 3.2, 3.3, 3.6, 7, 7.2, 7.3, 7.4, 8 "Thu hồi đề nghị thanh toán", 9 "Người bệnh không KCB BHYT", 10; mỗi mã kèm căn cứ và `MUC_HUONG`); ghi chú PL1: mã xác định **sau khi kết thúc** khám/điều trị, nhiều mã thì chọn theo thứ tự từ trên xuống. PL2 `MA_XANG_DAU` (R954V1…, XEDIEN). Đ2: bỏ PL5 QĐ 824 và PL5 QĐ 2010; gửi thay thế cho dữ liệu từ 01/07/2025; chuyển tiếp đến 31/12/2025.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 17/10/2025 (hồi tố cho dữ liệu từ 01/07/2025 nếu gửi thay thế)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tính `MA_DOITUONG_KCB` khi đóng lượt theo thứ tự ưu tiên; cấp cứu = "2"; mã "8" cho thu hồi; cập nhật tỷ lệ hưởng theo ngày (01/07/2026 với 1.13, 1.14, 1.18).
- **Bẫy**: STT trong PL1 nhảy từ 21 sang 23 ngay trong bản gốc — đừng dùng STT làm khóa. Mã ở XML0 là tạm, mã cuối ở XML1.

### BHYT-DATA-R17 — Mã DVKT, khám, giường, chỉ số CLS
- **Căn cứ**: QĐ 2010/2025 Đ1, PL1 (mã DVKT `MA_DICH_VU` dạng `CC.KKKK.GGGG`, một số hậu tố `_GT`, ánh xạ TT 23/2024 và tên giá), PL2 (khám), PL3 (tiền giường), PL4 (ngày giường ban ngày); Đ2 (bỏ PL01–04 QĐ 7603; PL1, PL5 QĐ 5937; PL2 QĐ 824); Đ3 (XML4 dùng mã chỉ số CLS của QĐ 1227/2025; chưa có thì tạm PL11 QĐ 7603); Đ5 (cập nhật chậm nhất 01/08/2025). Bảng 3 (2023): vận chuyển `VC.XXXXX`; CLS chuyển nơi khác `XX.YYYY.ZZZZ.K.WWWWW`; mã giường 4 ký tự H/T/C/K + số.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: ánh xạ dịch vụ nội bộ sang mã DVKT, giữ cả mã kỹ thuật TT 23 và STT giá; ánh xạ chỉ số xét nghiệm/CĐHA sang QĐ 1227, có cờ "đang dùng tạm PL11 7603".
- **Bẫy**: cấu trúc `CC.KKKK.GGGG` = chương TT 23 + số kỹ thuật + STT giá là suy luận từ cột PL1. QĐ 2010 tự gọi là "tạm thời". Danh mục kỹ thuật nền: xem MA-LT.

### BHYT-DATA-R18 — Mã thuốc, VTYT/TBYT, máu, thầu
- **Căn cứ**: Bảng 2 (2023): `MA_THUOC` = mã hoạt chất DMDC (thuốc tự bào chế nối mã thành phần bằng "+"; oxy "40.17"; NO "40.573"; máu hậu tố ".KT", ".NAT"); `TT_THAU` = số QĐ trúng thầu; mã gói; mã nhóm thầu theo PL6 QĐ 5937; năm, phân cách ";" (hai nhà thầu thêm `Gi.YY`). Bảng 3: `MA_VAT_TU` chi tiết tới kích thước, **do Cổng cấp tự động** theo QĐ 5086/2021; chỉ ghi VTYT ngoài cơ cấu giá DVKT. QĐ 697 PL IV.8: máu theo PL9 QĐ 7603.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục thuốc lưu mã hoạt chất DMDC, SĐK, thông tin thầu đúng cú pháp; VTYT/TBYT lưu mã do Cổng cấp; không tự sinh mã VTYT.
- **Bẫy**: QĐ 697 dùng "thiết bị y tế", XML vẫn `MA_VAT_TU`. Danh mục mã thuốc có cập nhật theo danh mục thuốc BHYT mới (TT 37/2024, TT 27/2025) không: chưa xác minh (xem DUOC).

### BHYT-DATA-R19 — Danh mục sử dụng tại cơ sở (Mẫu 01–06/DM)
- **Căn cứ**: TT 12/2026 Đ7 k1 b (định dạng theo PL II), k2 (sau ký hợp đồng lần đầu lập danh mục, **ký số**, gửi Cổng), k3 (áp dụng từ ngày hợp đồng có hiệu lực; thuốc, TBYT không sớm hơn hiệu lực hợp đồng mua sắm), k5 (sai lệch thì điều chỉnh/hủy trong 05 ngày làm việc); Đ8 (cập nhật qua Cổng; BHXH xử lý 05 ngày làm việc; thuốc, TBYT mua cấp cứu áp dụng theo ngày hóa đơn; bị từ chối gửi lại trong 15 ngày). PL II: 01/DM bộ phận chuyên môn (`MA_KHOA`, `BAN_KHAM`, `GIUONG_PD`, `GIUONG_TK`, `GIUONG_HSTC`, `GIUONG_HSCC`, `TU_NGAY`, `DEN_NGAY`, `MA_CSKCB`); 02/DM nhân lực; 03/DM thuốc, máu; 04/DM TBYT; 05/DM dịch vụ KCB; 06/DM TBYT thực hiện DVKT. Ghi chú 01/DM: thay đổi gửi **02 dòng** (dòng cũ có `DEN_NGAY` là ngày ngừng; dòng mới có `TU_NGAY`, `DEN_NGAY` trống); `TU_NGAY`, `DEN_NGAY` dạng `yyyymmdd`.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/04/2026 (TT 12 Đ17 k1)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục nội bộ có thời gian hiệu lực; sinh file Mẫu 01–06/DM, ký số, gửi, theo dõi chấp nhận/từ chối; chỉ dùng mục trong hồ sơ khi ngày y lệnh nằm trong [`TU_NGAY`, `DEN_NGAY`] đã được Cổng chấp nhận.
- **Bẫy**: không update-in-place danh mục đã gửi. Luồng duyệt và hạn: xem BHYT-GD-R28.

### BHYT-DATA-R20 — ICD-10 TT 06/2026 trong dữ liệu đầu ra
- **Căn cứ**: TT 06/2026 Đ3; Đ4 k1, k2 (cột 24 không dùng làm bệnh chính; 25 không khuyến khích làm bệnh chính; 26 không được sử dụng vì có mã 4 hoặc 5 ký tự cụ thể hơn; 27 chỉ dùng mã hóa nguyên nhân tử vong; 28 nữ; 29 nam), k3; Đ5 k3 (Q87.11 → Q87.1 từ 01/06/2026); Đ6 k1, **k2** (vào viện trước 01/07/2026, kết thúc trong hoặc sau ngày đó thì dùng mã TT 06), k3 (mã cũ trong HSBA đã lưu vẫn có giá trị); Đ7 k3 a, k5 b. Bảng 1 (2023): `MA_BENH_CHINH` 01 mã (≤ 7); `MA_BENH_KT` tối đa 12 mã, ";"; `MA_BENH_YHCT` kèm mã YHCT tương ứng.
- **Áp dụng**: mọi cơ sở KCB (XML: cơ sở BHYT) · **Hiệu lực/hạn**: 01/07/2026 (một phần 01/06/2026)
- **Mức**: BẮT BUỘC (nạp danh mục, dùng đúng mã, quy tắc chuyển tiếp) · NÊN (phần mềm tự chặn/cảnh báo)
- **Phần mềm phải**: nạp đủ 29 cột; chọn bộ mã theo thời điểm kết thúc lượt (`NGAY_RA`); áp quy tắc cột theo **MA-LT-R02**: cột 24 chặn ở `MA_BENH_CHINH`; cột 26 chặn ở **mọi vị trí** (`MA_BENH_CHINH`, `MA_BENH_KT`, nguyên nhân tử vong); cột 27 chỉ cho ở trường nguyên nhân tử vong, chặn ở `MA_BENH_CHINH` và `MA_BENH_KT`; cột 25 cảnh báo khi làm bệnh chính; cột 28, 29 cảnh báo khi lệch `GIOI_TINH`; không ghi đè mã đã lưu trong HSBA cũ.
- **Bẫy**: bảng 2023 vẫn dẫn QĐ 4469/2020; từ 01/07/2026 theo TT 06. Đây là trường hợp duy nhất có quy tắc chọn phiên bản theo ngày kết thúc lượt được ghi rõ. Cổng BHXH có chặn cột 26, 27 ở `MA_BENH_KT` không: chưa xác minh.

### BHYT-DATA-R21 — Bảng kê 01/KBCB theo QĐ 697
- **Căn cứ**: QĐ 697/2026 Đ2 k1 (mỗi lượt 01 bảng kê lưu, 01 giao người bệnh), k2 (đã triển khai bệnh án điện tử thì lập bảng kê điện tử, không phải lập giấy; "Bảng kê điện tử có ký số đầy đủ theo quy định thì có giá trị tương đương bản giấy"; bản giấy ký tay được scan và ký số xác thực cơ sở có giá trị như bản điện tử), k3 (chỉ kê mục phát sinh, giữ STT mã mục); Đ3 (thay QĐ 6556/2018); Đ4 k1 (nâng cấp phần mềm chậm nhất 01/07/2026), k3 (văn bản dẫn trong PL bị thay thì theo văn bản mới). PL: ô loại 01/02/03/04; ánh xạ `MA_LK`, `MA_BN`, `DIA_CHI`, `GIOI_TINH`, `MA_LOAI_RV`, mã đối tượng; Phần IV: tách chi phí theo thẻ và mức hưởng; tỷ lệ thanh toán khám (100/30/10/0%), giường (100/50/33%), gói TBYT trần 45 tháng lương cơ sở.
- **Áp dụng**: mọi cơ sở KCB lập bảng kê (phần BHYT cho người có thẻ) · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: in và xuất đúng mẫu 697; bảng kê điện tử ký số; cho scan bản ký tay rồi ký số cơ sở; sinh bảng kê **từ cùng ảnh chụp dữ liệu** với XML (P08).
- **Bẫy**: file trên trang BHXH tên "QĐ 967.pdf" nhưng nội dung là QĐ 697. PL 697 dẫn mã khoa PL6 QĐ 2010 (bỏ từ 01/08/2026) → dùng QĐ 1804. PL 697 ghi QĐ 7603 ngày "15/12/2018" — sai, đúng là 25/12/2018.

### BHYT-DATA-R22 — Phương thức kết nối và lưu biên nhận
- **Căn cứ**: TT 48 Đ5 (1 trong 4 phương thức: web service, đồng bộ máy trạm, nhập trực tiếp, FTP; kết quả đầu ra như nhau), Đ6 k2, Đ7 k2–3. TT 12 Đ9 k2 (phản hồi tự động 06/24/48 giờ; chủ ở BHYT-GD-R22). Hướng dẫn BHXH mục II: REST JSON, `api/token/take` (mật khẩu MD5 viết hoa), `api/qd130/checkInKcbQd3176`, `api/qd130/guiHoSoXmlQD3176`; phản hồi `maKetQua`, `maGiaoDich` ("lưu lại để đối chiếu"), `thoiGianTiepNhan`, `thongDiep`; tra cứu kết quả trên Cổng tối đa 60 ngày.
- **Áp dụng**: cơ sở KCB BHYT, vendor · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC (phương thức, xử lý phản hồi) · NÊN (lưu `maGiaoDich` — hướng dẫn BHXH)
- **Phần mềm phải**: lưu bền mọi phản hồi gắn `MA_LK` và phiên bản file đã gửi; tự kéo kết quả, lỗi và gán việc.
- **Bẫy**: Cổng chỉ tra 60 ngày → HIS phải tự lưu biên nhận lâu dài. MD5 là yêu cầu của BHXH, không phải thực hành tốt; giữ mật khẩu trong kho bí mật (BHYT-GD-R16).

### BHYT-DATA-R23 — Chuyển đổi phiên bản chuẩn theo mốc
- **Căn cứ**: QĐ 130 Đ4 k3–5, Đ5; QĐ 4750 Đ2 k3–5, Đ3 (kiểm thử song song từ 01/04/2024; chính thức và 4210 hết HL 01/07/2024; phần không sửa giữ theo 130); QĐ 3176 Đ3 (đồng bộ 01/01/2025), Đ2 k1 b (BHXH thông báo trước thay đổi trên Cổng), đ; QĐ 130 Đ5 (văn bản dẫn chiếu bị thay thì theo văn bản mới).
- **Áp dụng**: cơ sở KCB BHYT, vendor · **Hiệu lực/hạn**: theo từng QĐ
- **Mức**: BẮT BUỘC (áp đúng mốc) · NÊN (chạy song song nhiều phiên bản)
- **Phần mềm phải**: chạy hai phiên bản chuẩn song song trong giai đoạn kiểm thử; chuyển phiên bản bằng cấu hình ngày, không sửa code; tái sinh hồ sơ cũ theo phiên bản cũ.
- **Bẫy**: mỗi QĐ là bản vá ("nội dung còn lại giữ nguyên"), bản hợp nhất phải tự dựng.

### BHYT-DATA-R24 — Mã cơ sở KCB và thay đổi tổ chức
- **Căn cứ**: Bảng 1 (2023): `MA_CSKCB` chuỗi 5 do cơ quan có thẩm quyền cấp; `MA_DKBD` 5 ký tự. NĐ 188 Đ69 k8 d (cơ sở sáp nhập, đổi tên dùng mã cũ đến khi có mã mới) — nhưng Đ70 k3: k8 chỉ có hiệu lực 01/07/2025–31/12/2025.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: k8 hết hiệu lực 31/12/2025
- **Mức**: NÊN (quản lý mã cơ sở có thời hạn) · BẮT BUỘC (dùng đúng mã được cấp)
- **Phần mềm phải**: lưu mã cơ sở dạng có thời hạn (mã cũ, mã mới, ngày chuyển), áp theo ngày KCB; cập nhật `MA_NOI_DI`, `MA_NOI_DEN`, `MA_DKBD` theo danh mục BHXH.
- **Bẫy**: mã cơ sở 5 ký tự của BHXH khác mã định danh cơ sở 13 chữ số trong luồng Sổ SKĐT/KSK (QĐ 1551/2026; xem SKDT).

### BHYT-DATA-R25 — Bảo mật dữ liệu trích chuyển
- **Căn cứ**: TT 48 Đ3 k2, Đ9, Đ13 k3; NĐ 188 Đ68 k5 c.
- **Áp dụng**: cơ sở KCB BHYT, vendor · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: TLS khi gửi; phân quyền tài khoản Cổng; nhật ký truy cập và gửi; không để XML ở nơi công khai. Hồ sơ bí mật nhà nước: xem BHYT-GD-R31; an ninh, DLCN: ANM, DLCN.
- **Bẫy**: XML6 (HIV) là dữ liệu có luật bảo mật riêng, cần phân quyền chặt hơn (xem BAOMAT-CB).

### BHYT-DATA-R26 — Chứng từ BHXH trong bộ XML
- **Căn cứ**: QĐ 130 Đ2 k4 (Bảng 7–11 tạo chứng từ giải quyết chế độ BHXH; bản gốc dẫn TT 56/2017 và TT 18/2022 — **nay cả hai đã bị TT 25/2025 thay** từ 01/07/2025, xem GIAYTO); QĐ 4750 bổ sung Bảng 13 (giấy chuyển tuyến), 14 (giấy hẹn khám lại). TT 06/2026 Đ5 k2: phiếu hẹn, phiếu chuyển bản điện tử dùng ký số xác thực của cơ sở thay đóng dấu từ 01/06/2026.
- **Áp dụng**: cơ sở cấp các chứng từ này · **Hiệu lực/hạn**: hiện hành; ký số cơ sở từ 01/06/2026
- **Mức**: BẮT BUỘC? (nghĩa vụ gửi XML chứng từ với người bệnh không dùng BHYT chưa rõ)
- **Phần mềm phải**: sinh XML7, 9, 10, 11, 13, 14 khi phát hành chứng từ; sinh đôi trở lên mỗi trẻ một bản (ghi chú Bảng 7, 9); ký số cơ sở trên phiếu hẹn, phiếu chuyển điện tử. Mẫu giấy tờ: GIAYTO; luồng phiếu hẹn/chuyển: BHYT-GD-R11, R12.

**Tổng**: 26 yêu cầu. BẮT BUỘC 22 (R01–R10, R13–R23, R25); BẮT BUỘC? 3 (R11, R12, R26); NÊN 1 (R24, phần dùng đúng mã là BẮT BUỘC). Phần con: R07 kỹ thuật BẮT BUỘC?; R20 chặn tự động, R22 lưu `maGiaoDich`, R23 chạy song song là NÊN.

## 3. Pattern thiết kế

### BHYT-DATA-P01 — Sổ đăng ký phiên bản chuẩn XML
- **Giải quyết**: R01, R08, R09, R11, R23
- **Cách làm**: mỗi QĐ sửa chuẩn là một lớp vá lên lớp trước; bản hiệu lực tại một ngày = hợp nhất các lớp có `mandatory_from ≤ ngày`; sinh XSD và bộ kiểm tra từ bản hợp nhất; đối chiếu với XSD của BHXH trong CI.
- **Gợi ý dữ liệu**: `spec_release(id, decision_no, decision_date, kind[base|amend], parent_id, test_from, mandatory_from, sunset_at, source_url, verification_level)` (số QĐ luôn kèm năm); `spec_field(release_id, xml_table, xml_path, field_name, data_type[string|number|datetime12|date8], max_len, required_rule, format_regex, change_type[add|modify|retype|remove], source_ref)`, khóa `(release_id, xml_table, field_name)`; view `effective_spec(as_of_date)`.
- **Đánh đổi**: nhập liệu thủ công từ PDF/XLSX; đổi lại thêm QĐ 1931 chỉ là một bản ghi `modify MUC_HUONG max_len 3→4`.

### BHYT-DATA-P02 — Kho mã dùng chung có hiệu lực theo phụ lục
- **Giải quyết**: R13–R18, R20
- **Cách làm**: quản lý nguồn ở mức phụ lục của văn bản; hàm `resolve(code_system, code, as_of)` với chính sách chọn `as_of` theo hệ mã: ICD theo ngày kết thúc lượt (TT 06 Đ6 k2); danh mục cơ sở theo ngày y lệnh; QĐ 1804, 2010 không nói rõ khóa ngày → mặc định ngày kết thúc lượt, đánh dấu chưa xác minh.
- **Gợi ý dữ liệu**: `code_source(id, decision_no, decision_date, appendix, code_system, effective_from, mandatory_from, abolished_by_source_id, abolished_from)`; `code_value(code_system, code, display, attrs jsonb, source_id, valid_from, valid_to, recorded_at, superseded_by)`, index `(code_system, code, valid_from)`, exclusion constraint chống chồng `daterange`; ICD `attrs` có cờ cột 24–29.
- **Đánh đổi**: hai trục thời gian làm truy vấn phức tạp, nhưng là cách duy nhất tái sinh hồ sơ cũ đúng mã cũ và chứng minh đã dùng mã theo văn bản nào.

### BHYT-DATA-P03 — Danh mục cơ sở "đóng dòng cũ, mở dòng mới"
- **Giải quyết**: R19
- **Cách làm**: sửa → sinh 2 dòng → ký số → gửi → chờ chấp nhận (05 ngày làm việc) → chỉ `accepted` mới dùng trong hồ sơ; bị từ chối → đếm 15 ngày gửi lại.
- **Gợi ý dữ liệu**: `facility_catalog_item(id, form['01/DM'..'06/DM'], local_code, dmdc_code, payload jsonb, tu_ngay, den_ngay, contract_ref, purchase_contract_effective, sync_status[draft|signed|sent|accepted|rejected], portal_msg, signed_by, signed_at)`; ràng buộc `tu_ngay ≥ purchase_contract_effective` cho thuốc, TBYT.
- **Đánh đổi**: người dùng không sửa tại chỗ được; cần UI giải thích.

### BHYT-DATA-P04 — Đường ống hồ sơ hướng sự kiện, có đồng hồ hạn
- **Giải quyết**: R03, R05, R06, R22
- **Cách làm**: outbox: `first_cost_posted`, `first_cost_in_ward` → check-in (trừ mã 2, cơ sở chỉ CLS); `encounter_closed` → snapshot (P05) → kiểm tra (P06) → ký (P07) → gửi → lưu biên nhận; `payment_completed` → bổ sung `NGAY_TTOAN`, gửi lại; `portal_error` → việc có hạn 02 ngày làm việc.
- **Gợi ý dữ liệu**: `claim_submission(id, ma_lk, kind[checkin|claim|replace], snapshot_id, spec_release_id, payload_hash, signed_cert_serial, sent_at, ma_giao_dich, thoi_gian_tiep_nhan, ma_ket_qua, thong_diep, deadline_at, status)`; `work_calendar(date, is_working_day, note)`; cấu hình sẵn chế độ 03 giờ của dự thảo.
- **Đánh đổi**: gửi sớm làm tăng số lần gửi lại khi dữ liệu còn đổi; nhưng gửi lô sẽ không hợp lệ nếu dự thảo ban hành.

### BHYT-DATA-P05 — Ảnh chụp hồ sơ bất biến, tái sinh có lý do
- **Giải quyết**: R06, R09, R10, R21
- **Cách làm**: đóng lượt thì đóng băng dữ liệu nguồn thành snapshot kèm phiên bản chuẩn và phiên bản danh mục đã dùng; XML, bảng kê, báo cáo đều sinh từ snapshot.
- **Gợi ý dữ liệu**: `claim_snapshot(id, ma_lk, version_no, created_at, reason, spec_release_id, code_versions jsonb, data jsonb, sha256)`, duy nhất `(ma_lk, version_no)`, cấm UPDATE/DELETE.
- **Đánh đổi**: tốn lưu trữ; đổi lại trả lời được "lúc gửi dữ liệu là gì" khi xuất toán hoặc thanh tra.

### BHYT-DATA-P06 — Kiểm tra nhiều tầng trước khi gửi
- **Giải quyết**: R08, R10, R14–R17, R20
- **Cách làm**: tầng 1 XSD; tầng 2 regex (`^\d{12}$`, `^\d{8}$`, danh sách ";", mã khoa ví dụ `^K\d{2}((\d{2})*|\.\d+|\.D\d{2})$` cần chỉnh theo dữ liệu thật); tầng 3 liên bảng (`MA_LK` con có ở XML1, tổng tiền, làm tròn); tầng 4 mã có hiệu lực tại `as_of` và danh mục cơ sở `accepted`; tầng 5 nghiệp vụ (< 4 giờ → 09; 05 không DVKT; ICD cột 24–29; `MA_BENH_KT` ≤ 12 mã). Lỗi gắn theo `bảng/trường` như Cổng trả.
- **Gợi ý dữ liệu**: `validation_rule(id, layer, code, effective_from, effective_to, severity, expr)`.
- **Đánh đổi**: luật tầng 5 phải bật/tắt theo ngày hiệu lực; viết dạng cấu hình, không hard-code. Bộ tự giám định theo TT 12 Đ10: xem BHYT-GD-P05.

### BHYT-DATA-P07 — Dịch vụ ký số tập trung
- **Giải quyết**: R07, R19, R21, R26
- **Cách làm**: dịch vụ riêng (HSM hoặc ký từ xa) ký theo phạm vi nút XSD BHXH, SHA256, đặt `<CHUKYDONVI>`; dùng chung cho XML0, hồ sơ XML, Mẫu /DM, bảng kê, phiếu hẹn, phiếu chuyển.
- **Gợi ý dữ liệu**: `signing_cert(serial, subject, issuer, valid_from, valid_to, registered_on_portal_at, status)`; `signature_log(doc_type, doc_id, cert_serial, digest, signed_at, actor)`; cảnh báo chứng thư sắp hết hạn trước 30 ngày (ngưỡng tự chọn).
- **Đánh đổi**: điểm lỗi đơn; cần hàng đợi và thử lại.

### BHYT-DATA-P08 — Một nguồn cho XML và bảng kê
- **Giải quyết**: R21, R10, R09
- **Cách làm**: bảng kê 697 là phép chiếu từ cùng snapshot: "Số khám bệnh" = `MA_LK`, "Mã số người bệnh" = `MA_BN`, giới tính 1/2/3, tình trạng ra viện = `MA_LOAI_RV`, mã đối tượng = `MA_DOITUONG_KCB`; nhóm theo mục 1–12, bỏ mục không phát sinh nhưng giữ STT; tách khối theo thẻ và mức hưởng.
- **Gợi ý dữ liệu**: `billing_statement(id, snapshot_id, form_version, signed_document_id)`.
- **Đánh đổi**: buộc thống nhất mô hình chi phí viện phí và BHYT; TT 12 Đ5 k2 không cho lựa chọn khác.

### BHYT-DATA-P09 — Theo dõi thay đổi quy định, cờ theo ngày
- **Giải quyết**: R23, R11, R14, R15
- **Cách làm**: mỗi văn bản mới là một change ticket có `effective_from`, `mandatory_from`, phần bị bãi bỏ, mức xác minh; cờ tính năng bật theo ngày; bộ hồ sơ mẫu cho từng phiên bản để chạy hồi quy.
- **Gợi ý dữ liệu**: `reg_change(id, decision_no, decision_date, scope, effective_from, mandatory_from, abolishes jsonb, verification_level, status)`.
- **Đánh đổi**: cần người theo dõi BYT/BHXH định kỳ; tránh sự cố kiểu "ký 29/6, áp dụng 01/7".

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| BHYT-DATA-A01 | R01 | Xuất hồ sơ mẫu cho 5 loại lượt (khám, ngoại trú, nội trú, nội trú < 4 giờ, sinh con); đủ bảng theo tình huống; không có XML12 | File XML mẫu, cấu hình bảng | BẮT BUỘC |
| BHYT-DATA-A02 | R02 | Khai báo UTF-8, tiếng Việt đúng; mỗi file một hồ sơ; đợt có 2 thẻ chung hồ sơ | File mẫu, hexdump | BẮT BUỘC |
| BHYT-DATA-A03 | R03 | Ghi tiền khám → có XML0 ngay; chuyển nội trú → XML0 lần 2; ca cấp cứu → không gửi | Log gửi, `maGiaoDich` | BẮT BUỘC |
| BHYT-DATA-A04 | R04 | Tiếp đón: phản hồi tra thẻ được lưu nguyên; thử thẻ hết hạn, QN/CA | Bảng phản hồi, log API | BẮT BUỘC |
| BHYT-DATA-A05 | R05 | Phân bố (thời điểm gửi − `NGAY_RA`); hồ sơ > 07 ngày làm việc; cuối tháng gửi sau ngày 05; có lịch nghỉ | Truy vấn, biên bản sự cố | BẮT BUỘC |
| BHYT-DATA-A06 | R06 | Sửa hồ sơ đã gửi: bắt lý do, giữ bản cũ, giữ `MA_LK`; hồ sơ chưa thanh toán tự gửi lại khi có `NGAY_TTOAN` | Lịch sử phiên bản, log | BẮT BUỘC |
| BHYT-DATA-A07 | R07 | File đã gửi có `<CHUKYDONVI>` hợp lệ, SHA256, chứng thư còn hạn và đã đăng ký; ai được ký | File ký, ảnh Danh mục chứng thư trên Cổng | BẮT BUỘC |
| BHYT-DATA-A08 | R08 | Bộ kiểm giữ "01", nhận "1.11", ngày giờ 12 ký tự, dấu "." | Kết quả chạy bộ kiểm | BẮT BUỘC |
| BHYT-DATA-A09 | R09 | Truy vấn `MA_LK` trùng giữa các đợt; dòng XML con mồ côi | Kết quả truy vấn | BẮT BUỘC |
| BHYT-DATA-A10 | R10 | 50 hồ sơ ngẫu nhiên: tính lại tổng, làm tròn; kiểu cột tiền trong DB (decimal hay float) | Bảng đối chiếu, schema | BẮT BUỘC |
| BHYT-DATA-A11 | R11 | `MUC_HUONG` chứa 4 ký tự; hồ sơ sau 01/07/2026 mã 1.13/1.14/1.18 ra đúng mức | File mẫu, schema | BẮT BUỘC? |
| BHYT-DATA-A12 | R12 | Danh mục thuốc có loại căn cứ lưu hành; thử thuốc hiếm nhập theo giấy phép tỉnh | Ảnh danh mục, XML2 | BẮT BUỘC? |
| BHYT-DATA-A13 | R13 | Nguồn từng danh mục (QĐ, phụ lục, ngày nạp); còn dùng phụ lục đã bỏ (PL1, PL5 QĐ 824; PL5, PL6 QĐ 2010; PL01–04 QĐ 7603) không | Metadata danh mục | BẮT BUỘC |
| BHYT-DATA-A14 | R14 | Đủ 16 mã; nội trú 3 giờ → 09; mã 05 có DVKT bị chặn | Danh mục, kết quả thử | BẮT BUỘC |
| BHYT-DATA-A15 | R15 | So danh mục khoa với PL02 QĐ 1804 (K99, mã con, `.D`); hồ sơ sau 01/08/2026 không còn mã chỉ có trong PL6 QĐ 2010 | Bảng ánh xạ, truy vấn | BẮT BUỘC |
| BHYT-DATA-A16 | R16 | `MA_DOITUONG_KCB` tính khi đóng lượt, đúng thứ tự ưu tiên; có mã 8 | Cấu hình, hồ sơ mẫu | BẮT BUỘC |
| BHYT-DATA-A17 | R17 | Tỷ lệ dịch vụ đã ánh xạ mã DVKT QĐ 2010; chỉ số XN ánh xạ QĐ 1227; danh sách còn dùng PL11 7603 | Báo cáo ánh xạ | BẮT BUỘC |
| BHYT-DATA-A18 | R18 | XML2 với thuốc tự bào chế, oxy, máu .KT/.NAT; `TT_THAU` đúng cú pháp; mã VTYT lấy từ Cổng | File mẫu | BẮT BUỘC |
| BHYT-DATA-A19 | R19 | Thay đổi danh mục lưu thành 2 dòng, có ký số và trạng thái Cổng; hồ sơ không dùng mục chưa chấp nhận | Lịch sử danh mục, file /DM | BẮT BUỘC |
| BHYT-DATA-A20 | R20 | Đủ 29 cột; cột 24 làm bệnh chính bị chặn; cột 26 ở `MA_BENH_KT` bị chặn; cột 27 chỉ nhận ở nguyên nhân tử vong; cột 28 với nam bị cảnh báo; ca vào 30/06/2026 ra 02/07/2026 dùng mã mới; Q87.1 thay Q87.11 | Danh mục, kết quả thử | BẮT BUỘC (nạp, chuyển tiếp) / NÊN (chặn tự động) |
| BHYT-DATA-A21 | R21 | Bảng kê đúng mẫu 697, bỏ mục không phát sinh nhưng giữ STT; bản điện tử ký số; khớp XML cùng `MA_LK` | Bảng kê, file ký, đối chiếu | BẮT BUỘC |
| BHYT-DATA-A22 | R22 | Phương thức kết nối; nơi lưu `maGiaoDich`, phản hồi; lấy được biên nhận > 60 ngày từ HIS | Cấu hình, truy vấn | BẮT BUỘC / NÊN |
| BHYT-DATA-A23 | R23 | Chạy hai phiên bản song song; chuyển bằng cấu hình ngày; tái sinh hồ sơ 2024 theo chuẩn cũ | Tài liệu kiến trúc, demo | NÊN |
| BHYT-DATA-A24 | R24 | Mã cơ sở lưu có thời hạn; hồ sơ trước/sau đổi mã đúng mã | Bảng mã, hồ sơ mẫu | NÊN |
| BHYT-DATA-A25 | R25 | TLS; mật khẩu Cổng không nằm rõ trong cấu hình; quyền truy cập XML6 | Cấu hình, kết quả quét bí mật | BẮT BUỘC |
| BHYT-DATA-A26 | R26 | Phiếu hẹn, phiếu chuyển điện tử có ký số cơ sở (từ 01/06/2026) và sinh XML13/14; XML11 theo mẫu TT 25/2025 | File phiếu, XML | BẮT BUỘC? |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới |
|---|---|---|---|
| 01/03/2018 | TT 48 có HL: XML, UTF-8, 4 phương thức, thời hạn gửi | Cơ sở KCB BHYT | Đã qua |
| 15/01/2019 | Bộ mã dùng chung phiên bản 6 (QĐ 7603) | Cơ sở, BHXH | Đã qua |
| 01/04/2024 | Kiểm thử bảng 4750 song song 4210 | Cơ sở, vendor | Đã qua |
| 01/07/2024 | Chính thức 4750; QĐ 4210 hết HL; check-in bắt buộc | Cơ sở, vendor | Đã qua |
| 01/07–31/12/2024 | Cửa sổ thay thế hồ sơ (QĐ 3176 Đ2 k1 đ) | Cơ sở | Đã qua |
| 01/01/2025 | Đồng bộ bảng 3176 | Cơ sở, vendor | Đã qua |
| 01/07/2025 | TT 25/2025 thay TT 56/2017, TT 18/2022 (chứng từ XML7–11) | Cơ sở | Đã qua |
| 01/08/2025 | Cập nhật phần mềm theo 6 danh mục QĐ 2010 | Cơ sở, vendor | Đã qua |
| 17/10/2025 (hồi tố 01/07/2025) → 31/12/2025 | Mã đối tượng, mã nhiên liệu QĐ 3276; cửa sổ gửi lại | Cơ sở | Đã qua |
| 01/01/2026 | Chậm nhất ký số (xác thực) dữ liệu chi phí KCB BHYT (NĐ 188 Đ69 k9) | Cơ sở, vendor | Đã qua |
| 01/04/2026 | Mẫu 01–06/DM theo TT 12 | Cơ sở | Đã qua |
| 01/06/2026 | Phiếu hẹn, phiếu chuyển điện tử ký số cơ sở; Q87.11 → Q87.1 | Mọi cơ sở KCB | Đã qua |
| 01/07/2026 | ICD-10 TT 06; bảng kê 697; `MUC_HUONG` 4 ký tự và `SO_DANG_KY` thuốc hiếm (QĐ 1931/2026); mức hưởng 50% cho mã 1.13, 1.14, 1.18 | Mọi cơ sở (ICD, bảng kê); cơ sở BHYT (XML) | Đã qua |
| 01/08/2026 | 16 mã loại hình, mã khoa QĐ 1804; PL1 QĐ 824 và PL6 QĐ 2010 hết HL | Cơ sở, vendor | Đã qua |
| 07/10/2026 | Hết góp ý dự thảo thay TT 48 | Vendor, cơ sở góp ý | Sắp tới (ngày mai) |
| 01/01/2027 (dự kiến) | Dự thảo thay TT 48 có HL: ≤ 03 giờ, 15 ngày đối chiếu, có thể kèm chuẩn và ký số mới | Cơ sở, vendor | Sắp tới |
| chưa định | QĐ 2010, QĐ 3176 tự ghi "tạm thời" → có thể có bản thay | Vendor theo dõi | — |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuẩn XML**: QĐ 4210/2017 → QĐ 130 (18/01/2023) → sửa bởi QĐ 4750 (29/12/2023, chính thức 01/07/2024) → sửa tạm thời bởi QĐ 3176 (29/10/2024, đồng bộ 01/01/2025) → sửa bởi QĐ 1931 (29/06/2026, áp dụng 01/07/2026).
1. Trích "QĐ 130" đơn lẻ là sai: bảng 2023 đã bị 4750 thay toàn bộ, mốc 01/09/2023 bị dời sang 01/07/2024.
2. **QĐ 1931/QĐ-BYT** trùng số với QĐ năm 2016 (tẩy sán lá gan). Luôn ghi "QĐ 1931/QĐ-BYT ngày 29/06/2026 sửa QĐ 130".
3. XLSX 2023 còn ghi `MA_LOAI_KCB`, `MA_DOITUONG_KCB` (check-in) kiểu "Số"; 4750 đã đổi sang chuỗi.
4. Hướng dẫn BHXH chép nhầm phạm vi ký từ XML0 sang file hồ sơ; dùng XSD trên Cổng.

**Bộ mã dùng chung** (bãi bỏ theo phụ lục): QĐ 6061 (bản 5) → QĐ 7603 (25/12/2018, bản 6), sửa bởi 4905/2019, 5937/2021, 824/2023, 2010/2025, 3276/2025, 1804/2026.
- QĐ 2010 Đ2 bỏ: PL01–04 QĐ 7603; PL1, PL5 QĐ 5937; PL2 QĐ 824.
- QĐ 3276 Đ2 bỏ: PL5 QĐ 824 (xăng dầu); PL5 QĐ 2010 (đối tượng).
- QĐ 1804 Đ2 bỏ từ 01/08/2026: **chỉ** PL1 QĐ 824 (loại hình) và PL6 QĐ 2010 (mã khoa). Không thay cả QĐ 824 hay QĐ 2010.
- Chuỗi mã khoa: PL5 QĐ 5937 → PL6 QĐ 2010 → PL02 QĐ 1804. Mã đối tượng: PL2 QĐ 824 → PL5 QĐ 2010 → PL1 QĐ 3276. Loại hình: PL1 QĐ 824 → PL01 QĐ 1804. Xăng dầu: PL5 QĐ 824 → PL2 QĐ 3276.
5. TT 12/2026 Đ7 liệt kê chuỗi đến 3276, chưa có 1804 — không phải danh sách đầy đủ.
6. PL QĐ 697 ghi QĐ 7603 ngày "15/12/2018"; đúng là 25/12/2018.
7. XML1 bản 2023 dẫn mã khoa PL5 QĐ 5937 và ICD QĐ 4469/2020 — cả hai đã bị thay (QĐ 1804; TT 06/2026).

**Bảng kê**: QĐ 6556/2018 → QĐ 697/2026 (phần mềm chậm nhất 01/07/2026).
8. File trên trang BHXH tên "QĐ 967.pdf", nội dung là QĐ 697.
9. PL 697 dẫn PL6 QĐ 2010 cho mã khoa; từ 01/08/2026 dùng QĐ 1804 (697 Đ4 k3).

**ICD-10**: QĐ 4469/2020 → TT 06/2026 (01/07/2026).
10. Cột 24–29 không chỉ áp cho bệnh chính: cột 26 cấm mọi vị trí, cột 27 chỉ cho nguyên nhân tử vong (MA-LT-R02).

**Căn cứ**
11. TT 48/2017 còn HL (QĐ 1804 vẫn lấy làm căn cứ); chỉ có dự thảo thay.
12. NĐ 188 **Đ69 là điều khoản chuyển tiếp**; điều trách nhiệm CNTT là Đ68. Đ69 k8 chỉ hiệu lực 01/07/2025–31/12/2025 (Đ70 k3).
13. QĐ 4750, 2010 viện dẫn NĐ 146/2018, NĐ 75/2023, NĐ 02/2025, TT 30/2020 đã hết HL; nội dung kỹ thuật vẫn dùng, căn cứ pháp lý đổi sang NĐ 188/2025, TT 01/2025.
14. QĐ 130 Đ2 k4 dẫn TT 56/2017, TT 18/2022 cho chứng từ BHXH; cả hai đã bị TT 25/2025 thay toàn bộ.
15. Tên trường là `MA_DOITUONG_KCB`, không phải `MA_DOI_TUONG_KCB`.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. **QĐ 1931/QĐ-BYT ngày 29/06/2026**: chưa có bản gốc (chỉ 1 nguồn báo). Cần: bảng nào bị sửa, `MUC_HUONG` có cho dấu thập phân không, quy tắc `SO_DANG_KY` thuốc hiếm.
2. **Phụ lục QĐ 3176 bản gốc**: chưa đọc; kích thước, diễn giải từng trường mới có theo bản 2023 và phần đầu 4750. Triển khai lấy XSD trên Cổng làm chuẩn.
3. Số hiệu công văn BHXH kèm "Phụ lục 01 hướng dẫn liên thông theo QĐ 3176" (bản đăng để trống) — hỏi BHXH VN.
4. Khóa ngày chọn phiên bản danh mục khi QĐ không nói rõ (QĐ 1804, QĐ 2010): theo ngày vào, ra, y lệnh hay gửi? Lượt vắt qua 01/08/2026 ghi mã khoa nào? — hỏi Vụ BHYT hoặc BHXH.
5. Miễn check-in cho cơ sở chỉ làm CLS: căn cứ gốc TT 30/2020 Đ9 đã bị TT 01/2025 thay một phần; còn hiệu lực không.
6. Mã đơn vị hành chính (`MATINH_CU_TRU`, `MAHUYEN_CU_TRU`, `MAXA_CU_TRU`) sau khi bỏ cấp huyện từ 01/07/2025: chưa tìm thấy hướng dẫn BHXH.
7. QĐ 824/2023 PL3, PL4, PL6 và QĐ 1227/2025: chưa mở bản gốc; danh mục mã thuốc có cập nhật theo TT 37/2024, TT 27/2025 không.
8. Cổng BHXH có chặn ICD cột 26, 27 ở `MA_BENH_KT` không — hỏi Trung tâm Giám định BHYT.
9. XML7–XML11 với người bệnh không có BHYT: có bắt buộc gửi Cổng không (xem GIAYTO).
10. Toàn văn dự thảo thay TT 48: có đổi chuẩn XML, bộ mã, phương thức ký số không; nếu có, P01, P04, P07 cần lớp phiên bản mới từ 01/01/2027.
11. Định dạng chữ ký trong `<CHUKYDONVI>` (XMLDSig enveloped, canonicalization): suy luận, cần XSD trên Cổng (cần tài khoản).
