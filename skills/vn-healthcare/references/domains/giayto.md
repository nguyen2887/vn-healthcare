# GIAYTO — Giấy tờ y tế điện tử liên thông

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám, nhà hộ sinh, trạm y tế có giường lưu, cơ sở KSK/khám lái xe, vendor HIS/EMR/phần mềm phòng khám · Research gốc: `research/deep/GIAYTO.md`

Phạm vi: giấy chứng sinh, giấy báo tử, phiếu chẩn đoán nguyên nhân tử vong, giấy chứng nhận nghỉ việc hưởng BHXH, giấy ra viện, tóm tắt HSBA và các giấy thai sản, chứng nhận thương tích, phiếu chuyển, phiếu hẹn khám lại, giấy KSK, KSK lái xe: mẫu, trường bắt buộc, người ký, hạn gửi, nơi nhận, cấp lại. Ngoài phạm vi: Sổ SKĐT/VNeID, mã định danh, liên thông KSK theo QĐ 1551 (→ SKDT); bảng XML7–XML14 (→ BHYT-DATA-R26); quy tắc phiếu chuyển, phiếu hẹn trong luồng BHYT (→ BHYT-GD-R11, R12); chữ ký số chung (→ EMR-R06–R08); thời hạn lưu trữ (→ EMR-R22). Tài liệu nghiên cứu, không phải ý kiến pháp lý.

## Tóm tắt nhanh

- Giấy chứng sinh và giấy báo tử phải liên thông dữ liệu có ký số **chậm nhất 04 giờ làm việc sau khi cấp bản giấy** (NĐ 63/2024 Đ25 k1). Từ **01/09/2026** đích là **Cổng DVC quốc gia** (NĐ 301/2026); Phần mềm DVC liên thông chỉ chạy đến **01/01/2027** rồi chuyển sang Hệ thống điều phối của Cổng DVC: endpoint phải là cấu hình.
- Chứng từ BHXH (giấy ra viện, tóm tắt HSBA, giấy nghỉ việc, giấy chứng sinh, giấy chuyển viện, giấy báo tử, nghỉ dưỡng thai) gửi lên Cổng tiếp nhận dữ liệu giám định BHYT ngay khi người bệnh xuất viện, có ký số (QĐ 69/2025 Đ5 k4).
- Mẫu hiện hành từ 01/07/2025 là **13 mẫu PL II TT 25/2025** (thay toàn bộ TT 56/2017, TT 18/2022; C16). Giấy báo tử = **Mẫu 05**, không còn mẫu PL I TT 24/2020 (C02). Tóm tắt HSBA = **Mẫu 03** (+ giấy đề nghị Mẫu 04), không còn mẫu TT 32/2023 (C01).
- Giấy chứng sinh theo **TT 22/2025** (từ 01/10/2025), mã số 18 ký tự `XXXXX.GCS.ZZZZZ.YY`, cấp lại giữ nguyên mã số.
- "Ký số cơ sở thay đóng dấu từ 01/06/2026" (TT 06/2026 Đ5 k2) **chỉ** áp cho phiếu hẹn khám lại và phiếu chuyển cơ sở KCB bản điện tử. Không suy rộng cho giấy khác.
- Giấy nghỉ việc hưởng BHXH (Mẫu 07) chỉ cho ngoại trú, tối đa 30 ngày/lần (50 ngày với một số ca sảy/phá thai từ 13 tuần; 180 ngày với lao), ngày bắt đầu nghỉ trùng ngày khám.
- Giấy KSK: 4 mẫu mới theo TT 25/2026 từ 01/07/2026; trả KSK đơn lẻ trong 24 giờ; giá trị 12 tháng. Liên thông KSK định kỳ/sàng lọc trong 24 giờ: xem SKDT-R15.
- Mốc sắp tới: 01/01/2027 đổi endpoint Cổng DVC; 01/03/2027 Luật Hộ tịch 2026 có hiệu lực (UBND xã chủ động khai sinh, khai tử từ dữ liệu cơ sở KCB).

## Mục lục

| ID | Tiêu đề |
|---|---|
| GIAYTO-R01 | Đúng mẫu hiện hành theo ngày sự kiện; giữ mẫu cũ cho giấy đã cấp |
| GIAYTO-R02 | Trường tối thiểu bắt buộc; được thêm trường; không tẩy xóa |
| GIAYTO-R03 | Bản điện tử ký số hiển thị VNeID tương đương bản giấy |
| GIAYTO-R04 | Ma trận người ký; ký số tổ chức thay dấu |
| GIAYTO-R05 | Giấy hẹn trả giấy và cấp đúng hẹn |
| GIAYTO-R06 | Sai sót, cấp lại, thay thế |
| GIAYTO-R07 | Trách nhiệm tính chính xác và chứng từ điện tử |
| GIAYTO-R08 | Giấy chứng sinh và liên thông trong 04 giờ làm việc |
| GIAYTO-R09 | Khai sinh, khai tử chủ động theo Luật Hộ tịch 2026 |
| GIAYTO-R10 | Giấy báo tử Mẫu 05 và liên thông trong 04 giờ làm việc |
| GIAYTO-R11 | Phiếu chẩn đoán nguyên nhân tử vong |
| GIAYTO-R12 | Giấy chứng nhận nghỉ việc hưởng BHXH (Mẫu 07) |
| GIAYTO-R13 | Gửi chứng từ điện tử lên Cổng giám định BHYT khi xuất viện |
| GIAYTO-R14 | Giấy ra viện (Mẫu 02) |
| GIAYTO-R15 | Tóm tắt HSBA, xác nhận nội trú, giấy thai sản |
| GIAYTO-R16 | Giấy chứng nhận thương tích (Mẫu 01) |
| GIAYTO-R17 | Phiếu hẹn khám lại, phiếu chuyển: hai chữ ký số từ 01/06/2026 |
| GIAYTO-R18 | Giấy KSK: mẫu, người kết luận, 24 giờ, 12 tháng |
| GIAYTO-R19 | Liên thông KSK định kỳ/sàng lọc (xem SKDT-R15–R17) |
| GIAYTO-R20 | Giấy KSK lái xe và kết nối CSDL giao thông |
| GIAYTO-R21 | Chế tài liên quan giấy tờ |
| GIAYTO-R22 | Định danh người được cấp giấy |
| GIAYTO-R23 | Đối soát với nơi nhận, theo dõi đa hạn chót |

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 25/2025/TT-BYT (30/06/2025) | Chi tiết Luật BHXH, ATVSLĐ về y tế; 13 mẫu PL II (01 thương tích, 02 ra viện, 03 tóm tắt HSBA, 04 đề nghị, 05 báo tử, 06 xác nhận nội trú, 07 nghỉ việc BHXH, 08 chăm sóc khi bất khả kháng, 09 vô sinh, 10 mẹ không đủ sức khỏe chăm con, 11 nghỉ dưỡng thai, 12–13 giám định y khoa) | 01/07/2025 | Còn hiệu lực. Đ29 k2 làm hết hiệu lực TT 56/2017, TT 18/2022, TT 46/2016, Mẫu 52/BV2 và 53/BV2 PL XXIX TT 32/2023, mẫu giấy báo tử PL I TT 24/2020 | gốc-OCR (scan; Mẫu 01, 02, 07 đối chiếu ảnh trang) | [PDF scan](http://datafile.chinhsachquandoi.gov.vn/ecm/source_files/2025/07/12/thong-tu-so-25-2025-071910-120725-67.pdf) · [trang văn bản](http://chinhsachquandoi.gov.vn/chi-tiet-van-ban.htm?loai=vbqppl&id=200273) |
| 22/2025/TT-BYT (28/06/2025) | Cấp và sử dụng giấy chứng sinh (Mẫu 01; Mẫu 02 mang thai hộ) | 01/10/2025 | Còn hiệu lực; thay TT 17/2012, TT 34/2015, TT 27/2019 | gốc (bản đăng lại để trống số, ngày; số và ngày theo nguồn thứ cấp nhà nước) | [PDF (BVĐK Bạc Liêu)](https://bvdkbaclieu.gov.vn/upload/1000079/20250715/593_Thong_tu-22-2025-TT-BYT_5874ca4c81.pdf) |
| 1898/QĐ-BYT (09/06/2025) | Chuẩn định dạng dữ liệu điện tử giấy chứng sinh | Từ ngày ký | Còn hiệu lực (chưa thấy bị thay) | thứ cấp (chưa có bản gốc, chưa có PL I) | [PBGDPL Cần Thơ (thứ cấp)](https://pbgdpl.cantho.gov.vn/quy-dinh-chi-tiet-ve-chuan-va-dinh-dang-du-lieu-dien-tu-giay-chung-sinh-duoc-bo-y-te-quy-dinh-tai-quyet-dinh-1898qd-byt-nam-2025) |
| 63/2024/NĐ-CP (10/06/2024) | Liên thông 02 nhóm TTHC (khai sinh…; khai tử…) | Từ ngày ký | Còn hiệu lực; sửa bởi NĐ 301/2026 | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/6/63-cp.signed.pdf) · [VB 210359](https://vanban.chinhphu.vn/?pageid=27160&docid=210359) |
| 301/2026/NĐ-CP (30/07/2026) | Sửa NĐ 63: liên thông với Cổng DVC quốc gia; căn cước trẻ dưới 6 tuổi; tờ khai mới | 01/09/2026; một số nội dung 01/01/2027, 01/03/2027 | Còn hiệu lực | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/301_2026_nd-cp_30072026_3-signed.signed.pdf) · [VB 219043](https://vanban.chinhphu.vn/?pageid=27160&docid=219043) |
| 03/2026/QH16 (23/04/2026) | Luật Hộ tịch (thay Luật 60/2014/QH13) | 01/03/2027; khai sinh, khai tử chủ động toàn quốc chậm nhất 01/01/2031 | Sắp có hiệu lực | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-03-2026-qh16-469530/64878.htm) · [PDF Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/5/27/469530-1779268193_v1_1779843006_signed.pdf) |
| 69/QĐ-TTg (10/01/2025) | Liên thông dữ liệu KCB, dân cư, hộ tịch cho ốm đau, thai sản | Từ ngày ký; BHXH tiếp nhận từ 01/07/2025 | Còn hiệu lực (còn dẫn NĐ 13/2023, NĐ 166/2016) | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/69-ttg.signed.pdf) · [VB 212391](https://vanban.chinhphu.vn/?pageid=27160&docid=212391) |
| 01/2025/TT-BYT | Hướng dẫn Luật BHYT: Đ11 phiếu hẹn (PL V), Đ12 phiếu chuyển (PL VI) | 01/01/2025 | Còn hiệu lực; sửa bởi TT 06/2026 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/01-byt.pdf) |
| 06/2026/TT-BYT (02/04/2026) | ICD-10; Đ5 k2 ký số cơ sở thay dấu trên phiếu hẹn, phiếu chuyển điện tử | 01/07/2026; Đ5 k2, k3 từ 01/06/2026 | Còn hiệu lực | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf) |
| 32/2023/TT-BYT | Chương VI KSK (Đ30–38), PL XXIV | 01/01/2024 | Còn hiệu lực; Đ34, Đ36, PL XXIV sửa bởi TT 25/2026 | gốc | [PDF ký số (BV Bệnh Nhiệt đới)](https://bvbnd.vn/wp-content/uploads/2024/01/32-thongtuhuongdanluatkbcb31122023_91202410.pdf) |
| 25/2026/TT-BYT (30/06/2026) | Sửa TT 32 Đ34, Đ36; Mẫu KSK 01–04 mới | 15/08/2026; Đ2, Đ3 từ 01/07/2026 | Còn hiệu lực | gốc (thân văn bản; phụ lục mẫu chưa có) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/25-byt.signed.pdf) |
| 1551/QĐ-BYT (31/05/2026) | Liên thông dữ liệu KSK định kỳ, sàng lọc (chi tiết ở SKDT) | Từ ngày ký | Còn hiệu lực | gốc | [PDF (SYT Lai Châu)](https://soyte.laichau.gov.vn/upload/1001027/20260602/2026_05_31_QD_ban_hanh_HD_ket_noi_lien_thong_du_lieu_KSK_Final_signed_2be3f377e1.pdf) |
| 36/2024/TT-BYT (16/11/2024) | Tiêu chuẩn sức khỏe, KSK người lái xe | 01/01/2025 | Còn hiệu lực; thay TTLT 24/2015 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/36-byt.pdf) |
| 7586/BYT-KCB (30/12/2022) | Liên thông giấy KSK lái xe trong 4 giờ | 01/01/2023 | Chưa rõ còn áp dụng nguyên trạng sau TT 36/2024 | thứ cấp | [CĐS Bình Phước (thứ cấp)](https://cds.binhphuoc.gov.vn/Tin-tuc/bo-y-te-yeu-cau-lien-thong-du-lieu-giay-kham-suc-khoe-lai-xe-241.html) |
| 24/2020/TT-BYT (28/12/2020) | Phiếu chẩn đoán nguyên nhân tử vong, thống kê tử vong | — | Còn hiệu lực **trừ** mẫu giấy báo tử PL I (hết hiệu lực 01/07/2025) | chưa xác minh (chỉ qua TT 25/2025) | link chưa kiểm tra được |
| 1996/QĐ-BYT (18/06/2025) | Hướng dẫn ghi phiếu CĐNNTV (thay QĐ 1921/QĐ-BYT theo thứ cấp) | Từ ngày ký | Còn hiệu lực | thứ cấp (tài liệu tập huấn Cục QLKCB 2026) | [Tài liệu tập huấn, kcb.vn](https://kcb.vn/upload/2005611/20260303/Tai_lieu_tap_huan_ghi_nhan_Phieu_CDNNTV_5c9bd.pdf) |
| 41/2024/QH15 | Luật BHXH: Đ47 hồ sơ ốm đau, Đ61 hồ sơ thai sản | 01/07/2025 | Còn hiệu lực | thứ cấp | link chưa kiểm tra được |
| 33/2025/TT-BYT | Thời hạn lưu trữ hồ sơ ngành y tế; PL mục 48 giấy KSK 02 năm (chi tiết ở EMR-R22) | 01/07/2025 | Còn hiệu lực; thay TT 53/2017 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [Phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| 90/2026/NĐ-CP | Xử phạt VPHC y tế (Đ46, Đ95 k4) | 15/05/2026 | Còn hiệu lực | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |

Dẫn chiếu: QĐ 130/4750/3176 và QĐ 1931/QĐ-BYT năm 2026 sửa QĐ 130, bảng XML7 (ra viện), XML8 (tóm tắt), XML9 (chứng sinh), XML10 (dưỡng thai), XML11 (nghỉ việc), XML13 (chuyển tuyến), XML14 (hẹn khám) → BHYT-DATA-R01, R26; NĐ 164/2025 → BHYT-GD; Luật GDĐT 2023 Đ23 k3, NĐ 23/2025 → EMR-R07, R08.

## 2. Yêu cầu

**Bảng tra nhanh theo loại giấy**

| Giấy | Mẫu hiện hành | Ai ký (theo mẫu) | Gửi đi đâu | Hạn gửi | Cấp lại |
|---|---|---|---|---|---|
| Giấy chứng sinh | TT 22/2025 Mẫu 01, 02 | Thân nhân; người đỡ đẻ; đại diện cơ sở + dấu | Cổng DVC quốc gia; Cổng giám định BHYT (XML9) | 04 giờ làm việc sau cấp bản giấy; BHXH khi xuất viện | 03 ngày làm việc, giữ mã số cũ |
| Giấy báo tử | TT 25/2025 Mẫu 05 | Người thân; người ghi giấy; Thủ trưởng + dấu | Cổng DVC quốc gia; Cổng giám định BHYT | 04 giờ làm việc | Đóng dấu "Cấp lại"; sửa + dấu treo |
| Phiếu CĐNNTV | TT 24/2020 + QĐ 1996/2025 | Thủ trưởng/người chịu trách nhiệm chuyên môn | Hệ thống báo cáo BYT (`cdc.kcb.vn`, theo tập huấn) | chưa xác minh | — |
| Nghỉ việc hưởng BHXH | TT 25/2025 Mẫu 07 (ngoại trú) | Người hành nghề; đại diện đơn vị + dấu | Cổng giám định BHYT (XML11) | Khi phát hành | "CẤP LẠI", ngày ký = ngày phát hành |
| Giấy ra viện | TT 25/2025 Mẫu 02 | Người hành nghề; đại diện đơn vị + dấu | Cổng giám định BHYT (XML7) | Khi xuất viện | như trên |
| Tóm tắt HSBA | TT 25/2025 Mẫu 03 (+ đề nghị Mẫu 04) | Đại diện đơn vị + dấu | Cổng giám định BHYT (XML8) | Khi xuất viện / theo hẹn | như trên |
| Dưỡng thai, nội trú, vô sinh, mẹ không đủ sức khỏe | TT 25/2025 Mẫu 11, 06, 09, 10 | theo mẫu | Cổng giám định BHYT (XML10 cho dưỡng thai) | Khi xuất viện / theo hẹn | như trên |
| Chứng nhận thương tích | TT 25/2025 Mẫu 01 | Người hành nghề; đại diện đơn vị + dấu | Không thấy kênh điện tử bắt buộc | Theo giấy hẹn | như trên |
| Phiếu chuyển | TT 01/2025 PL VI | Bác sĩ; bản điện tử từ 01/06/2026 thêm ký số cơ sở | Cổng giám định (XML13); VNeID | Giá trị 10 ngày làm việc / 01 năm | BHYT-GD-R11 |
| Phiếu hẹn khám lại | TT 01/2025 PL V | Bác sĩ (ký số); từ 01/06/2026 ký số cơ sở | Cổng giám định (XML14); VNeID | Dùng 01 lần | BHYT-GD-R12 |
| Giấy/sổ KSK | TT 32 PL XXIV (Mẫu 01–04 theo TT 25/2026) | Người kết luận + dấu | CSDL sức khỏe cá nhân BYT (định kỳ/sàng lọc) | 24 giờ (SKDT-R15); trả giấy KSK đơn lẻ 24 giờ | chưa có quy định riêng |
| Giấy KSK lái xe | TT 36/2024 PL II | Người kết luận + dấu | CSDL trật tự an toàn giao thông; BYT (CV 7586) | 4 giờ (CV 7586, thứ cấp) | chưa có quy định riêng |

### A. Khung chung

### GIAYTO-R01 — Đúng mẫu hiện hành theo ngày sự kiện; giữ mẫu cũ cho giấy đã cấp
- **Căn cứ**: TT 25/2025 Đ5, Đ7–Đ15 (mỗi giấy theo mẫu PL II), Đ29 k2 (danh sách văn bản, mẫu hết hiệu lực), Đ30 k1 (giấy nghỉ việc, ra viện, dưỡng thai, mẹ không đủ sức khỏe cấp trước 01/07/2025 vẫn có giá trị). TT 22/2025 Đ3 k1, k3; Đ6 k1 (trẻ sinh trước 01/10/2025 dùng mẫu cũ), Đ6 k2 (cấp lại cho trẻ sinh trước 01/10/2025 dùng mẫu mới). TT 25/2026 Đ2 k4, k5, Đ5 (hồ sơ KSK khám xong trước hiệu lực theo mẫu cũ; đã nhận nhưng chưa khám theo mẫu mới).
- **Áp dụng**: mọi cơ sở KCB, vendor · **Hiệu lực/hạn**: 01/07/2025, 01/10/2025, 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu mỗi loại giấy với `mau_id`, `phien_ban`, `hieu_luc_tu/den`; chọn mẫu theo **ngày sự kiện** (ngày sinh cho giấy chứng sinh lần đầu, ngày tiếp nhận hồ sơ KSK), không theo ngày in; giấy đã phát hành giữ nguyên mẫu, không render lại bằng mẫu mới.
- **Bẫy**: tài liệu tập huấn Cục QLKCB 2026 vẫn hướng dẫn cấp giấy báo tử theo TT 24/2020: sai mẫu (đúng là Mẫu 05 TT 25/2025). "Giấy chuyển viện" trong QĐ 69 = phiếu chuyển PL VI TT 01/2025 = XML13 "giấy chuyển tuyến".

### GIAYTO-R02 — Trường tối thiểu bắt buộc; được thêm trường; không tẩy xóa
- **Căn cứ**: TT 25/2025 Đ3 k2 (gốc-OCR, diễn giải): thông tin trong các mẫu là thông tin cơ bản, bắt buộc phải có; người đứng đầu cơ sở được bổ sung thông tin phục vụ hoạt động của cơ sở. Đ3 k1: giấy cấp phải phù hợp phạm vi chuyên môn được phê duyệt và tình trạng người bệnh. Hướng dẫn Mẫu 07: ghi đầy đủ, rõ ràng, không tẩy xóa, bằng tiếng Việt, 2 liên như nhau. TT 22/2025 Đ7 k1: dữ liệu điện tử giấy chứng sinh phải đủ các trường theo mẫu. TT 32/2023 Đ52 k2 c (không viết tắt, xem EMR-R04).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kiểm tra đủ trường của mẫu trước khi cho ký; cho thêm trường tùy biến nhưng không ẩn/xóa trường của mẫu; ký xong thì khóa nội dung (sửa qua R06); chặn phát hành khi người ký không có phạm vi chuyên môn phù hợp (ví dụ khoa không có chức năng sản cấp giấy chứng sinh; suy luận từ Đ3 k1).

### GIAYTO-R03 — Bản điện tử ký số hiển thị VNeID tương đương bản giấy
- **Căn cứ**: TT 25/2025 Đ3 k2 câu cuối (gốc-OCR, diễn giải): thông tin trong mẫu đã hiển thị trên VNeID và ký số đầy đủ có giá trị như bản giấy. TT 01/2025 ghi chú PL V, VI: tương tự cho phiếu hẹn, phiếu chuyển. TT 22/2025 Đ7 k1: trường thông tin giấy chứng sinh được xác thực điện tử hợp pháp. QĐ 69/2025 Đ4 k2: dữ liệu chia sẻ được ký số.
- **Áp dụng**: cơ sở phát hành giấy trong phạm vi TT 25/2025, TT 22/2025, TT 01/2025 · **Hiệu lực/hạn**: 01/01/2025 (TT 01), 01/07/2025 (TT 25), 01/10/2025 (TT 22)
- **Mức**: BẮT BUỘC? (luật cho phép bản điện tử thay giấy, không buộc mọi cơ sở phát hành bản điện tử; riêng dữ liệu liên thông ở R08, R10, R13 phải ký số)
- **Phần mềm phải**: phát hành bản có cấu trúc (XML/JSON) và bản trình bày (PDF) cùng nội dung, ký đủ mọi vị trí ký của mẫu (R04); lưu bằng chứng ký (chứng thư, thời điểm, kết quả kiểm tra hiệu lực, EMR-R07).
- **Bẫy**: "ký số đầy đủ" nghĩa là đủ mọi vị trí ký (người hành nghề và đại diện đơn vị), không chỉ chữ ký tổ chức (suy luận). Kênh đưa giấy lên VNeID: SKDT.

### GIAYTO-R04 — Ma trận người ký; ký số tổ chức thay dấu
- **Căn cứ** (vị trí ký theo mẫu):
  - Chứng nhận thương tích, giấy ra viện (TT 25/2025 Mẫu 01, 02, đối chiếu ảnh): đại diện đơn vị (ký, ghi rõ họ tên, đóng dấu) và người hành nghề KB, CB (ký, ghi rõ họ tên). Đại diện đơn vị là người đứng đầu hoặc người được phân công.
  - Tóm tắt HSBA (Mẫu 03, diễn giải): đại diện đơn vị ký, đóng dấu.
  - Giấy báo tử (Mẫu 05, diễn giải): người thân thích; người ghi giấy (ghi chức danh); Thủ trưởng, người chịu trách nhiệm chuyên môn hoặc người được ủy quyền ký, đóng dấu.
  - Nghỉ việc hưởng BHXH (Mẫu 07, đối chiếu ảnh): đại diện đơn vị và người hành nghề; người đứng đầu đồng thời là người khám thì chỉ ký và đóng dấu ở phần đại diện đơn vị.
  - Giấy chứng sinh (TT 22/2025 PL I mục 19–21): thân nhân của trẻ; người đỡ đẻ (ghi chức danh); đại diện cơ sở (ghi chức danh, đóng dấu).
  - Phiếu hẹn (TT 01/2025 Đ11 k2): bản giấy đóng dấu treo + chữ ký bác sĩ; bản điện tử chữ ký số bác sĩ điều trị. TT 06/2026 Đ5 k2: dòng đóng dấu trên Mẫu PL V và PL VI được "thay thế bằng ký số xác thực của cơ sở khám bệnh, chữa bệnh đối với bản điện tử", từ 01/06/2026.
  - Giấy/sổ KSK (TT 32/2023 Đ37 k4): người kết luận ký, ghi rõ họ tên, đóng dấu cơ sở; QĐ 1551 PL01 có `CKS_NGUOI_KET_LUAN`, `CKS_BENH_VIEN`.
  - Nguyên tắc chung: Luật GDĐT 2023 Đ23 k3 (văn bản cần tổ chức xác nhận thì dùng chữ ký số tổ chức), EMR-R08.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng; ký số cơ sở trên phiếu hẹn, phiếu chuyển điện tử từ 01/06/2026 (đã qua)
- **Mức**: BẮT BUỘC (vị trí ký theo mẫu) · BẮT BUỘC? (ký số tổ chức thay dấu ở giấy ngoài phiếu hẹn/phiếu chuyển: chỉ có căn cứ chung Luật GDĐT)
- **Phần mềm phải**: cấu hình theo mẫu danh sách vị trí ký (`vai_tro`, `loai_chu_ky` cá nhân | tổ chức, `bat_buoc`); chặn "đã phát hành" khi còn vị trí bắt buộc chưa ký; hỗ trợ "một người ký hai vai" của Mẫu 07; chứng thư cá nhân của người ký thay có chức danh (NĐ 23 Đ13, EMR-R08); chữ ký người thân có thể là chữ ký tay số hóa hoặc xác nhận điện tử (EMR-R06, R09).
- **Bẫy**: không suy rộng mốc 01/06/2026 cho giấy ra viện, nghỉ việc, chứng sinh, KSK. Căn cứ nằm trong một thông tư về ICD-10 nên dễ bị bỏ sót.

### GIAYTO-R05 — Giấy hẹn trả giấy và cấp đúng hẹn
- **Căn cứ**: TT 25/2025 Đ5 k2, Đ8 k2 b, Đ9 k2 b, Đ10 k2, Đ11 k3 b, Đ13 k2, Đ14 k2, Đ15 k2 (diễn giải): cơ sở trả người đề nghị giấy hẹn ghi rõ thời gian cấp và cấp đúng hẹn; Đ28 k5: người lao động đã KCB nhưng chưa được cấp giấy thì cơ sở cấp theo văn bản đề nghị. TT 22/2025 Đ3 k2 b (sinh ngoài cơ sở: 05 ngày làm việc từ khi nhận tờ khai), Đ3 k3 b (mang thai hộ sinh tại cơ sở khác: 03 ngày làm việc), Đ4 k3 b (cấp lại: 03 ngày làm việc).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025; 01/10/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: yêu cầu cấp giấy (kể cả cấp muộn theo Đ28 k5) thành phiếu có `ngay_hen_tra`; in/gửi điện tử giấy hẹn; cảnh báo quá hạn; báo cáo tỷ lệ trả đúng hẹn; tính hạn theo ngày làm việc có lịch nghỉ.
- **Bẫy**: TT 25/2025 không ấn định số ngày tối đa của giấy hẹn, chỉ buộc ghi rõ và giữ đúng. Quyền yêu cầu tóm tắt HSBA: Luật KCB Đ69 k4 d, đ (EMR-R14).

### GIAYTO-R06 — Sai sót, cấp lại, thay thế
- **Căn cứ**: TT 25/2025 Đ28 k4 a (diễn giải): cấp lại khi mất, hỏng, người ký không đúng thẩm quyền, đóng dấu sai; giấy cấp lại đóng dấu "Cấp lại"; Đ28 k4 b: sai thông tin thì bổ sung, sửa rồi đóng dấu treo. Hướng dẫn Mẫu 07 (đối chiếu ảnh): ngày ký giấy cấp lại là ngày phát hành. TT 22/2025 Đ4: cấp lại giấy chứng sinh khi nhầm, thiếu thông tin, mất, rách; hồ sơ gồm tờ khai PL III, giấy cũ (trừ khi mất), giấy tờ chứng minh; mã số giấy cấp lại **giữ nguyên mã số cũ**. NĐ 301/2026 Đ6 k5, Đ10: sai sót trong giấy khai sinh/trích lục khai tử điện tử do cơ quan hộ tịch sửa.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC (cấp lại, sửa sai) · BẮT BUỘC? (cách xử lý tương đương với dữ liệu điện tử đã liên thông: văn bản không quy định)
- **Phần mềm phải**: không sửa tại chỗ giấy đã phát hành; tạo phiên bản thay thế liên kết `thay_the_cho`, `ly_do` (mat_hong | sai_tham_quyen | sai_dau | sai_thong_tin | thieu_thong_tin), cờ `cap_lai` hiện trên bản in và dữ liệu; giữ mã số với giấy chứng sinh; gửi lại dữ liệu thay thế lên đúng kênh và lưu biên nhận; bản cũ chuyển `bi_thay_the`, không xóa.
- **Bẫy**: cơ chế thu hồi dữ liệu đã gửi lên Cổng DVC/Cổng giám định không có trong văn bản đã đọc; dữ liệu BHYT có quy tắc gửi lại riêng (BHYT-DATA-R06); giấy chứng sinh/báo tử đã dùng để khai sinh/khai tử thì sửa phải phối hợp cơ quan hộ tịch (suy luận).

### GIAYTO-R07 — Trách nhiệm tính chính xác và chứng từ điện tử
- **Căn cứ**: TT 25/2025 Đ28 k2, k3 (diễn giải): xây dựng quy trình cấp, giám sát người ghi giấy, chịu trách nhiệm tính chính xác; cập nhật dữ liệu KCB vào CSDL để liên thông với BHXH, tạo lập chứng từ điện tử. QĐ 69/2025 Đ5 k4 (diễn giải): cơ sở KCB, HĐ GĐYK tạo lập chứng từ điện tử, chịu trách nhiệm tính hợp pháp, chính xác, lưu trữ và bảo đảm toàn vẹn.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu bất biến bản đã ký và mọi lần gửi (payload, chữ ký, thời điểm, phản hồi); nhật ký tạo, ký, sửa (EMR-R12); quy trình cấp giấy cấu hình theo quy chế cơ sở.
- **Bẫy**: TT 25/2025 và QĐ 69 dẫn NĐ 166/2016, NĐ 13/2023; đọc theo văn bản thay thế (NĐ 164/2025 cho giao dịch BHXH; Luật 91/2025, NĐ 356/2025 cho DLCN). TT 25/2025 Đ31 cho phép áp văn bản thay thế.

### B. Giấy chứng sinh

### GIAYTO-R08 — Giấy chứng sinh và liên thông có ký số trong 04 giờ làm việc
- **Căn cứ**: TT 22/2025 Đ2 (mọi cơ sở KCB có giấy phép), Đ3 k1 (sinh tại cơ sở: cấp trước khi trẻ ra khỏi cơ sở), k2 (sinh ngoài cơ sở có người đỡ đẻ: tờ khai trong 30 ngày, cấp trong 05 ngày làm việc, không xác minh được thì không cấp), k4 (trẻ sinh sống rồi tử vong trước khi ra viện: cấp giấy chứng sinh **rồi** giấy báo tử), k5 (02 bản; sinh đôi trở lên mỗi trẻ 01 giấy, mã số khác nhau), Đ7 k1 (liên thông dữ liệu điện tử giấy chứng sinh với Phần mềm DVC liên thông theo NĐ 63, đủ trường, xác thực điện tử hợp pháp). NĐ 63/2024 Đ25 k1 (gốc-OCR, diễn giải): người đứng đầu cơ sở chịu trách nhiệm liên thông dữ liệu giấy chứng sinh, giấy báo tử có ký số chậm nhất 04 giờ làm việc sau khi cấp bản giấy; k2: bảo đảm hạ tầng. NĐ 301/2026 Đ4 (sửa Đ5 k2 NĐ 63): liên thông với Cổng DVC quốc gia. QĐ 1898/2025: chuẩn định dạng (thứ cấp). QĐ 69 Đ2 k1, Đ5 k4: giấy chứng sinh cũng gửi Cổng giám định BHYT.
- **Áp dụng**: BV công, BV tư, PK, nhà hộ sinh có đỡ đẻ; vendor · **Hiệu lực/hạn**: NĐ 63 từ 10/06/2024 (tiếp nhận hồ sơ liên thông từ 01/07/2024); TT 22 từ 01/10/2025; Cổng DVC quốc gia từ 01/09/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: (1) mã số **18 ký tự** `XXXXX.GCS.ZZZZZ.YY` (XXXXX số thứ tự tăng trong năm tại cơ sở; ZZZZZ mã cơ sở 5 số theo QĐ 384/2019; YY hai số cuối năm cấp), duy nhất, trùng giữa phần mềm và bản giấy (TT 22 PL I mục 4); (2) đủ trường Mẫu 01: họ tên mẹ in hoa có dấu, ngày sinh, dân tộc, số định danh hoặc hộ chiếu (không có thì CMND/giấy khai sinh kèm loại, ngày, nơi cấp), nơi cư trú, mã số BHXH/thẻ BHYT (không có thì **10 chữ số 0**), giờ phút ngày sinh con, nơi sinh, số con trong lần sinh, giới tính (nam/nữ/không xác định), cân nặng gam (không cân thì "Không cân"), tên dự định, ghi chú (phẫu thuật, dưới 32 tuần, dị tật); Mẫu 02 thêm thông tin bên nhờ và bên mang thai hộ; (3) ký số theo R04 rồi đẩy dữ liệu, đồng hồ 04 giờ làm việc từ lúc cấp bản giấy; (4) lưu biên nhận; (5) đồng thời đẩy XML9 lên Cổng giám định BHYT (R13).
- **Bẫy**: hai kênh song song (Cổng DVC quốc gia cho hộ tịch, cư trú, BHYT trẻ em, căn cước; Cổng giám định BHYT cho thai sản). NĐ 301 Đ15 k14 đổi "Phần mềm DVC liên thông" thành "Cổng DVC quốc gia" ở một số điều; Đ18 k3: Phần mềm DVC liên thông chỉ chạy đến 01/01/2027, sau đó tích hợp vào Hệ thống điều phối giải quyết TTHC của Cổng DVC → endpoint là cấu hình. NĐ 301 không sửa Đ25 NĐ 63 nên hạn 04 giờ làm việc vẫn giữ (suy luận). QĐ 1898 ban hành trước khi TT 22/2025 có hiệu lực: có bao phủ Mẫu 02 mang thai hộ không, chưa xác minh.

### GIAYTO-R09 — Khai sinh, khai tử chủ động theo Luật Hộ tịch 2026
- **Căn cứ**: Luật Hộ tịch 03/2026/QH16 Đ15 k2 (UBND xã, theo lựa chọn của người yêu cầu, chủ động đăng ký khai sinh khi dữ liệu của cơ sở KCB được kết nối, chia sẻ tự động tới hệ thống hộ tịch điện tử; trẻ sinh tại cơ sở KCB và người yêu cầu đã cung cấp đủ nội dung), Đ20 k2 (tương tự cho khai tử, chết tại cơ sở KCB), Đ29 k1 (hiệu lực 01/03/2027; theo lộ trình, toàn quốc chậm nhất 01/01/2031). NĐ 301 Đ18 k2: từ 01/03/2027 UBND xã thực hiện Đ15 k2; "Trích lục khai tử" đổi thành "Giấy chứng tử".
- **Áp dụng**: cơ sở KCB có sinh, tử; vendor · **Hiệu lực/hạn**: 01/03/2027 (sắp tới); toàn quốc chậm nhất 01/01/2031
- **Mức**: BẮT BUỘC? (luật buộc UBND xã; nghĩa vụ kỹ thuật của cơ sở chờ nghị định hướng dẫn, Đ29 k4 b)
- **Phần mềm phải** (chuẩn bị): dữ liệu giấy chứng sinh/báo tử đủ để cơ quan hộ tịch dùng trực tiếp (số định danh của mẹ/người chết, nơi cư trú, thời gian, nơi sinh/chết, nguyên nhân chết theo Đ20 k4 b); kênh gửi thêm được đích mới (hệ thống hộ tịch) không đổi mô hình dữ liệu.
- **Bẫy**: Luật Hộ tịch 60/2014 hết hiệu lực 01/03/2027; tài liệu dẫn "Luật Hộ tịch 2014" sẽ sai căn cứ.

### C. Giấy báo tử

### GIAYTO-R10 — Giấy báo tử Mẫu 05 TT 25/2025 và liên thông trong 04 giờ làm việc
- **Căn cứ**: TT 25/2025 Đ9 k1 (diễn giải): Mẫu 05; cấp sau khi người bệnh tử vong tại cơ sở hoặc trong quá trình chuyển cơ sở; thẩm quyền: cơ sở nơi KCB. Hướng dẫn Mẫu 05 (gốc-OCR, diễn giải): cấp cho người thân để đi khai tử; mọi ca tử vong tại cơ sở, kể cả trên đường đi cấp cứu; chết trên đường đến cơ sở thì cơ sở nơi được chuyển **đến** cấp; chết trên đường chuyển giữa hai cơ sở thì cơ sở **chuyển đi** cấp; có ô tích "tử vong khi đang trên đường đi cấp cứu". Trường: cơ sở, họ tên in hoa có dấu, ngày sinh, giới, dân tộc, quốc tịch, nơi thường trú/tạm trú, số định danh (nếu có), giấy tờ tùy thân, giờ phút ngày vào, giờ phút ngày tử vong (số và chữ; không rõ thì bỏ trống), nguyên nhân tử vong (chưa xác định thì ghi "không rõ"), cấp lần đầu/số quyển. TT 22/2025 Đ3 k4. NĐ 63 Đ10 k1 b, Đ11, Đ25 k1; NĐ 301 Đ8 (liên thông với Cổng DVC quốc gia). TT 25/2025 Đ6 k1 a; QĐ 69 Đ2 k1.
- **Áp dụng**: BV công, BV tư, PK có lưu bệnh, cấp cứu ngoại viện · **Hiệu lực/hạn**: Mẫu 05 từ 01/07/2025; Cổng DVC quốc gia từ 01/09/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sự kiện tử vong trong EMR mở luồng bắt buộc: giấy báo tử Mẫu 05 có số, mã số; ký số Thủ trưởng/người được ủy quyền và người ghi giấy; đẩy dữ liệu có ký số lên Cổng DVC quốc gia trong 04 giờ làm việc, lưu biên nhận; xử lý ca chết trên đường cấp cứu, trên đường chuyển viện; liên kết giấy chứng sinh nếu là sơ sinh.
- **Bẫy**: mẫu giấy báo tử PL I TT 24/2020 hết hiệu lực từ 01/07/2025, nhưng phần còn lại của TT 24/2020 (phiếu CĐNNTV, thống kê tử vong) vẫn hiệu lực (C02 cần đọc theo nghĩa này). Tài liệu tập huấn Cục QLKCB 2026 yêu cầu ghi mã số giấy báo tử "theo hướng dẫn Đề án 06": định dạng mã chưa xác minh (có thể tương tự mã giấy chứng sinh, suy luận).

### GIAYTO-R11 — Phiếu chẩn đoán nguyên nhân tử vong
- **Căn cứ**: TT 24/2020 (phần phiếu CĐNNTV còn hiệu lực, chưa đọc gốc); QĐ 1996/QĐ-BYT 2025 (thứ cấp). Tài liệu tập huấn Cục QLKCB 2026: phiếu không giao người nhà, không lưu cùng HSBA tử vong, lưu tại cơ sở để báo cáo; báo cáo điện tử trên hệ thống BYT (`cdc.kcb.vn`); bác sĩ điều trị cuối cùng lập chuỗi sự kiện và mã ICD-10; thủ trưởng hoặc người chịu trách nhiệm chuyên môn ký; không dùng nội dung phiếu để kiểm điểm nhân viên.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC? (nghĩa vụ ở TT 24/2020 chưa đọc gốc; kênh `cdc.kcb.vn` chỉ thấy trong tập huấn)
- **Phần mềm phải**: tách phiếu CĐNNTV khỏi HSBA và khỏi bản in cho người nhà; quyền xem hẹp; chuỗi nguyên nhân theo ICD-10 TT 06/2026 (mã chỉ dùng cho nguyên nhân tử vong, cột 27; cột 26 cấm ở mọi vị trí, BHYT-DATA-R20, C04); xuất dữ liệu cho hệ thống báo cáo BYT. Dữ liệu tử vong cho HTTT quản lý KCB: HTTT-BC-R05.

### D. Giấy tờ hưởng BHXH

### GIAYTO-R12 — Giấy chứng nhận nghỉ việc hưởng BHXH (Mẫu 07, chỉ ngoại trú)
- **Căn cứ**: TT 25/2025 Đ10 (Mẫu 07; cấp theo giấy hẹn; thẩm quyền cơ sở nơi KCB). Hướng dẫn Mẫu 07 (gốc-OCR, đối chiếu ảnh, diễn giải): góc trái ghi tên cơ sở và số khám bệnh (theo bộ phận nếu nhiều bộ phận); ô Mẫu, Số, Số …/KCB, Số seri; họ tên in hoa, ngày sinh (chỉ có năm thì ghi năm); mã số BHXH (khi BHXH thông báo dùng thay số thẻ) hoặc số thẻ BHYT; số CCCD/định danh/hộ chiếu, ngày cấp; giới; đơn vị làm việc (con ốm thì ghi đơn vị của cha hoặc mẹ); chẩn đoán có mã ICD-10 và tên bệnh (bệnh dài ngày theo PL I TT 25/2025; có thai ghi tuổi thai); phương pháp điều trị; số ngày nghỉ tối đa 30 ngày/lần (sảy, phá thai, thai chết, thai ngoài tử cung từ 13 tuần: tối đa 50 ngày; lao theo chương trình quốc gia: tối đa 180 ngày); ngày bắt đầu nghỉ trùng ngày đến khám; trẻ dưới 07 tuổi ghi thông tin cha, mẹ; ngày cấp trùng ngày khám (đợt nhiều ngày thì ngày cuối); mã bệnh khớp PL I mà tên không khớp thì theo mã. Luật BHXH 2024 Đ47 (thứ cấp). QĐ 69 Đ2 k1, Đ5 k4; XML11.
- **Áp dụng**: BV, PK, TYT có khám ngoại trú · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chặn phát hành cho lượt nội trú; chặn `so_ngay_nghi` > 30 trừ khi có cờ lý do 50 hoặc 180 ngày; mặc định `tu_ngay` và `ngay_cap` = ngày khám (hoặc ngày cuối đợt); bắt buộc ICD-10 + tên bệnh, kiểm tra theo danh mục bệnh dài ngày PL I; bắt buộc cha, mẹ khi tuổi < 7; `so_kcb` + `so_seri` duy nhất; ký theo R04; gửi XML11 (R13).
- **Bẫy**: nội dung giấy nghỉ việc ở **Đ10** và Mẫu 07; Đ29 chỉ là điều hiệu lực. Giấy ra viện cũng tối đa 30 ngày nghỉ (OCR từng đọc nhầm "36"; ảnh trang là 30). Giấy cấp trước 01/07/2025 theo mẫu TT 56/2017, TT 18/2022 vẫn có giá trị (Đ30 k1).

### GIAYTO-R13 — Gửi chứng từ điện tử lên Cổng giám định BHYT khi xuất viện
- **Căn cứ**: QĐ 69/2025 (gốc-OCR, diễn giải): Đ2 k1 dữ liệu chia sẻ gồm giấy ra viện, giấy nghỉ việc hưởng BHXH, giấy chứng sinh, giấy chuyển viện, tóm tắt HSBA, giấy báo tử, biên bản GĐYK, giấy nghỉ dưỡng thai; Đ4 k2 ký số; Đ5 k4 cơ sở KCB, HĐ GĐYK tạo lập chứng từ điện tử và gửi lên Cổng tiếp nhận dữ liệu Hệ thống thông tin giám định BHYT ngay khi người bệnh xuất viện, lưu trữ, bảo đảm toàn vẹn; Đ6 k3 a BHXH tiếp nhận, giải quyết ốm đau, thai sản từ 01/07/2025. TT 25/2025 Đ28 k3. Chuẩn bảng: BHYT-DATA-R26.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC (cơ sở KCB BHYT) · BẮT BUỘC? (người bệnh không dùng BHYT, cơ sở không có hợp đồng BHYT)
- **Phần mềm phải**: khi chốt ra viện/kết thúc lượt, tự sinh và đẩy các chứng từ đã phát hành của lượt (XML7, 8, 9, 10, 11, 13) đã ký số; giấy nghỉ việc ngoại trú đẩy khi phát hành; lưu mã giao dịch, thời điểm tiếp nhận, lỗi; hàng đợi gửi lại.
- **Bẫy**: QĐ 69 không có số giờ cụ thể. Văn bản không giới hạn ở người có BHYT (người lao động KCB dịch vụ vẫn hưởng ốm đau); Cổng nhận hồ sơ không có thẻ BHYT thế nào: chưa xác minh (trùng câu hỏi mở 9 của BHYT-DATA).

### GIAYTO-R14 — Giấy ra viện (Mẫu 02 TT 25/2025)
- **Căn cứ**: TT 25/2025 Đ7: cấp sau khi người hành nghề quyết định cho ra viện hoặc chuyển cơ sở. Trường (đối chiếu ảnh): cơ quan chủ quản, cơ sở, số, MS, số hồ sơ/BA, họ tên, ngày sinh (tuổi), giới, dân tộc, nghề nghiệp, số CCCD/định danh/hộ chiếu, ngày cấp, mã số BHXH/thẻ BHYT (nếu có), địa chỉ, giờ phút ngày vào, ra viện, chẩn đoán, phương pháp điều trị, ghi chú. Hướng dẫn: chẩn đoán có ICD-10; thai ghi tuổi thai và cách đình chỉ thai; ghi chú số ngày nghỉ ngoại trú sau ra viện (tối đa 30; 50; 180 với lao), "để dưỡng thai"; người mất năng lực hoặc trẻ dưới 16 tuổi ghi cha, mẹ hoặc người giám hộ; giấy để giải quyết BHXH một lần ghi tên bệnh theo Luật BHXH Đ70 k1 c. TT 01/2025 Đ11 k1: lịch hẹn có thể ghi trong giấy ra viện (khi đó là phiếu hẹn, R17). QĐ 69 Đ2 k1; XML7.
- **Áp dụng**: BV, cơ sở có nội trú/ban ngày · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấp giấy ra viện gắn với quyết định ra viện/chuyển viện; kiểm tra số ngày nghỉ tối đa; bắt buộc người giám hộ khi tuổi < 16; lịch hẹn trong giấy ra viện áp quy tắc dùng 01 lần; gửi XML7 (R13).

### GIAYTO-R15 — Tóm tắt HSBA, xác nhận điều trị nội trú, giấy thai sản
- **Căn cứ**: TT 25/2025 (gốc-OCR, diễn giải; Mẫu 03–13 chưa đối chiếu bản có dấu): Đ8 (tóm tắt HSBA Mẫu 03; người đề nghị nộp Mẫu 04; cơ sở trả giấy hẹn), Đ2 k2 (bản trích sao HSBA theo Luật ATVSLĐ Đ57 k2 chính là bản tóm tắt theo Luật KCB Đ69 k1), Đ9 k2 (xác nhận nội trú Mẫu 06), Đ11 (chăm sóc khi bất khả kháng Mẫu 08), Đ12–Đ15 (vô sinh Mẫu 09, mẹ không đủ sức khỏe Mẫu 10, dưỡng thai Mẫu 11). Mẫu 03 có số căn cước/hộ chiếu/định danh, chẩn đoán vào và ra viện kèm ICD, tóm tắt bệnh lý và diễn biến, tình trạng ra viện, hướng điều trị tiếp; trạm y tế có giường lưu được cấp tóm tắt. QĐ 69 Đ2 k1; XML8, XML10.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hỗ trợ các mẫu PL II ứng với loại hình cơ sở; phát hành tóm tắt HSBA từ dữ liệu EMR, khóa phiên bản theo HSBA đã đóng; nhận giấy đề nghị Mẫu 04 (giấy hoặc điện tử), ghi người đề nghị và tư cách (EMR-R14); gửi XML8, XML10 (R13).

### GIAYTO-R16 — Giấy chứng nhận thương tích (Mẫu 01 TT 25/2025)
- **Căn cứ**: TT 25/2025 Đ1 k2 d, Đ5 (Mẫu 01; giấy hẹn ghi rõ thời gian cấp; thẩm quyền cơ sở nơi KCB). Trường (đối chiếu ảnh): như giấy ra viện cộng nơi làm việc, nơi cấp giấy tờ, lý do vào viện và **tình trạng thương tích/tổn thương lúc vào và lúc ra viện**; ký: đại diện đơn vị (đóng dấu), người hành nghề. TT 32/2023 Đ30 k2 c: khám để cấp giấy chứng thương không thuộc chế độ KSK.
- **Áp dụng**: BV, cơ sở cấp cứu, điều trị chấn thương · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lấy dữ liệu từ HSBA (mô tả tổn thương lúc vào và lúc ra phải có trong bệnh án); quản lý giấy hẹn (R05); bản in có số, MS; cấp lại theo R06.
- **Bẫy**: không có trong danh mục QĐ 69 Đ2 k1, không có bảng XML riêng; không thấy nghĩa vụ liên thông điện tử.

### E. Phiếu chuyển và phiếu hẹn

### GIAYTO-R17 — Phiếu hẹn khám lại, phiếu chuyển: hai chữ ký số từ 01/06/2026
- **Căn cứ**: TT 01/2025 Đ11 k1–k3, k5 (phiếu hẹn PL V hoặc ghi trong đơn thuốc, giấy ra viện; giấy hoặc điện tử; mỗi phiếu dùng 01 lần; chỉ hẹn một lần sau một đợt điều trị), Đ12 k1–k2 (phiếu chuyển PL VI, giá trị 10 ngày làm việc từ ngày ký; bệnh PL III: 01 năm). TT 06/2026 Đ5 k2 (từ 01/06/2026, bản điện tử thay dấu bằng ký số xác thực của cơ sở).
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/01/2025; ký số cơ sở 01/06/2026 (đã qua)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: quy tắc hạn dùng, dùng 01 lần, chặn hẹn lần 2: xem BHYT-GD-R11, R12; XML13, XML14: BHYT-DATA-R26. Bổ sung: phiếu điện tử phát hành từ 01/06/2026 phải có **hai** chữ ký số (bác sĩ + cơ sở); phiếu phát hành 01/01/2025–31/05/2026 chỉ có chữ ký bác sĩ vẫn hợp lệ (suy luận: không hồi tố); giấy ra viện, đơn thuốc có lịch hẹn cũng quản lý như phiếu hẹn (trạng thái đã dùng).

### F. Khám sức khỏe

### GIAYTO-R18 — Giấy KSK: mẫu, người kết luận, trả trong 24 giờ, giá trị 12 tháng
- **Căn cứ**: TT 32/2023 Đ30 (đối tượng KSK; loại trừ khám ngoại trú/nội trú, giám định, chứng thương, bệnh nghề nghiệp, đối tượng BQP/BCA, ngành nghề đặc thù), Đ31 k3 (giấy KSK nước ngoài: khi có điều ước, hạn không quá 6 tháng), Đ34 mới (TT 25/2026: Mẫu 01 dưới 6 tuổi, 02 từ 6 đến dưới 18, 03 từ 18 trở lên, 04 KSK tâm thần; người mất/hạn chế năng lực hành vi thêm văn bản đồng ý của thân nhân), Đ36 mới (khám đủ nội dung mẫu; bác sĩ có CCHN/GPHN được người phụ trách chuyên môn phân công bằng văn bản; KSK định kỳ chỉ làm CLS khi có chỉ định; KSK theo yêu cầu thiếu chuyên khoa thì không phân loại), Đ35 k2 (đối chiếu ảnh, đóng dấu giáp lai ảnh), Đ37 k3, k4 (người kết luận phân loại; ký, ghi rõ họ tên, đóng dấu), Đ38 (01 bản cấp, 01 bản lưu; KSK đơn lẻ trả **trong 24 giờ** từ khi kết thúc khám trừ khi phải khám bổ sung; giấy KSK có giá trị **12 tháng** từ ngày ký kết luận; Đ38 dẫn lưu trữ theo TT 53/2017, nay là TT 33/2025). TT 33/2025 PL mục 48 (gốc, đã đối chiếu phụ lục): giấy khám sức khỏe phục vụ người lao động đi học, đi làm và các hoạt động khác lưu **02 năm**. TT 25/2026 Đ5 (chuyển tiếp), Đ6 k2.
- **Áp dụng**: BV, PK đã công bố KSK · **Hiệu lực/hạn**: Đ34, Đ36, mẫu mới từ 01/07/2026 (đã qua)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chọn mẫu theo tuổi và mục đích; bắt buộc ảnh (chụp không quá 6 tháng) hoặc ảnh số; danh sách bác sĩ được phân công KSK (có văn bản, CCHN/GPHN còn hiệu lực), chặn người ngoài danh sách ký kết luận; chặn phân loại khi KSK theo yêu cầu thiếu chuyên khoa; đồng hồ 24 giờ cho KSK đơn lẻ; tính và in `het_han` 12 tháng; lưu bản lưu tối thiểu 02 năm (TT 33/2025 mục 48), retention cấu hình được (EMR-R22).
- **Bẫy**: phụ lục Mẫu 01–04 mới của TT 25/2026 chưa lấy được (PDF chỉ có thân văn bản). TT 25/2026 không sửa Đ37 k4 ("đóng dấu") và Đ38; ký số cơ sở thay dấu chỉ dựa nguyên tắc chung (R04). Phần KSK của TT 32 là Chương VI (Đ30–38), không phải Chương X. TT 25/2025 (BHXH) và TT 25/2026 (KSK) cùng số 25: ghi đủ năm.

### GIAYTO-R19 — Liên thông dữ liệu KSK định kỳ, khám sàng lọc
- **Căn cứ**: QĐ 1551/QĐ-BYT 2026 HD mục 2–4, PL01–PL03. Domain chủ: **SKDT-R15** (17 mẫu, 24 giờ, ký số), **SKDT-R16** (tài khoản, mã 13 chữ số, tài khoản định danh tổ chức), **SKDT-R17** (API Trục dữ liệu BYT), **SKDT-R18** (mã 5 và mã 13).
- **Áp dụng**: mọi cơ sở KCB tổ chức KSK định kỳ hoặc sàng lọc; vendor KSK · **Hiệu lực/hạn**: 31/05/2026; dữ liệu tồn 15/07/2026 (đã qua)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: như SKDT-R15–R17. Bổ sung từ góc giấy tờ: phiếu KSK chỉ được coi là "kết thúc" (mốc 24 giờ) khi đã đủ chữ ký người kết luận và cơ sở (R04, R18); adapter ánh xạ giấy KSK nội bộ sang mẫu PL01 theo nhóm tuổi và đối tượng nghề.
- **Bẫy**: QĐ 1551 chỉ nêu KSK định kỳ và sàng lọc; giấy KSK đi học, đi làm, theo yêu cầu có phải liên thông không: chưa xác minh. Đặc tả PL01 (31/05/2026) ban hành trước mẫu KSK mới của TT 25/2026 (01/07/2026): có thể lệch trường.

### GIAYTO-R20 — Giấy KSK lái xe và kết nối CSDL trật tự an toàn giao thông
- **Căn cứ**: TT 36/2024 Đ1 (không áp dụng người điều khiển xe gắn máy), Đ2 (tiêu chuẩn PL I), Đ3 (quy trình theo TT 32 Đ35; KSK định kỳ lái xe ô tô hành nghề có xét nghiệm ma túy, nồng độ cồn), Đ4, Đ5 (cấu trúc dữ liệu kết quả KSK lái xe: hành chính theo Đề án 06; cơ sở, ngày khám; kết quả xét nghiệm ma túy; kết luận), Đ9 (mẫu cũ TTLT 24/2015 dùng tiếp đến hạn ghi trên giấy; sổ in sẵn đến 30/06/2025), **Đ10 k3 b** (cơ sở KCB kết nối, chia sẻ dữ liệu KSK với CSDL về trật tự, an toàn giao thông đường bộ và CSDL khác). PL II: giấy giá trị 12 tháng; người có CCCD gắn chip hoặc số định danh đã kết nối CSDL dân cư thì bỏ trống một số mục hành chính. CV 7586/BYT-KCB 2022 (thứ cấp): trong 4 giờ sau khi cấp giấy KSK lái xe đủ điều kiện, liên thông về BYT qua Cổng giám định BHYT (API) hoặc `dulieu.kcb.vn`; không có dữ liệu trên hệ thống thì coi như không đủ điều kiện. QĐ 1551 PL01 mẫu 3 (sổ KSK định kỳ lái xe, `HANG_LAI_XE`).
- **Áp dụng**: BV, PK đã công bố khám lái xe · **Hiệu lực/hạn**: 01/01/2025
- **Mức**: BẮT BUỘC (kết nối, chia sẻ theo Đ10 k3 b) · BẮT BUỘC? (hạn 4 giờ và kênh cụ thể, chỉ có ở công văn 2022 đọc qua thứ cấp)
- **Phần mềm phải**: mẫu PL II, hạng GPLX đề nghị (cấp mới/đổi/lại); kết quả ma túy bắt buộc cho nhóm tương ứng; ký số người kết luận và cơ sở; gửi theo cấu trúc Đ5 trong 4 giờ (cấu hình được), lưu biên nhận; sổ KSK định kỳ lái xe đồng thời đẩy theo QĐ 1551 (24 giờ).
- **Bẫy**: sau Luật TTATGTĐB 2024, CSDL trật tự an toàn giao thông do ngành công an quản lý (suy luận); kênh kỹ thuật hiện hành chưa xác minh bản gốc.

### G. Chế tài

### GIAYTO-R21 — Chế tài liên quan giấy tờ
- **Căn cứ** (NĐ 90/2026, gốc-OCR, diễn giải; mức cá nhân, tổ chức gấp đôi theo BHYT-GD mục D): Đ46 k1 (3–5 triệu: cấp giấy KSK khi không khám đủ nội dung; phân loại sức khỏe sai tình trạng), k2 (5–10 triệu: không bảo đảm điều kiện của cơ sở KSK; đình chỉ KSK 01–03 tháng), k3 (10–20 triệu: KSK khi chưa công bố; tước GPHĐ 01–03 tháng). Đ95 k4 (1–3 triệu): a) không đăng ký với BHXH mẫu dấu, mẫu chữ ký của người hành nghề được phép ký giấy chứng nhận và người được ủy quyền ký, đóng dấu của cơ sở; b) không kết nối, liên thông dữ liệu, tạo lập chứng từ điện tử về KCB theo quy định giao dịch điện tử BHYT.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 15/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh sách người được ký giấy chứng nhận (mẫu chữ ký, chứng thư) khớp danh sách đã đăng ký với BHXH, chặn người chưa đăng ký ký giấy nghỉ việc, giấy ra viện; với chữ ký số, đăng ký chứng thư trên Cổng giám định (BHYT-DATA-R07); chặn phát hành giấy KSK khi chưa đủ kết quả chuyên khoa của mẫu (trừ KSK theo yêu cầu không phân loại); báo cáo tuân thủ từng loại giấy (phát hành, gửi đúng hạn, quá hạn, lỗi).
- **Bẫy**: Đ95 k4 a (đã đối chiếu ảnh trang) còn dùng tên cũ "giấy chứng nhận không đủ sức khỏe" (NĐ 146/2018), nay đọc là giấy chứng nhận nghỉ việc hưởng BHXH (suy luận). Không tìm thấy (qua OCR) điều riêng phạt chậm liên thông giấy chứng sinh, giấy báo tử.

### H. Định danh và đối soát

### GIAYTO-R22 — Định danh người được cấp giấy
- **Căn cứ**: TT 22/2025 PL I mục 7 (mẹ người nước ngoài: dân tộc ghi "Người nước ngoài" và quốc tịch), mục 8 (số định danh; không có thì hộ chiếu; không có nữa thì CMND hoặc giấy khai sinh kèm loại, ngày, nơi cấp), mục 9 (người nước ngoài không cư trú ở VN sinh ở vùng biên), mục 10 (không có mã BHXH/thẻ BHYT: 10 chữ số 0). TT 25/2025 Mẫu 05 (số định danh "nếu có", giấy tờ thay thế), Mẫu 01, 02, 03, 07 (số CCCD/CMND/định danh/hộ chiếu); hướng dẫn Mẫu 02, 07 (mã số BHXH thay số thẻ khi BHXH có thông báo). TT 36/2024 PL II. QĐ 1551 PL01 (`SO_CCCD`, `SO_CCCD_NGH`). NĐ 63 Đ25 k3. Mô hình định danh chung: SKDT-R05, R11, R12.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trường định danh có `loai_giay_to` (DDCN | HO_CHIEU | CMND | GIAY_KHAI_SINH | KHAC), số, ngày, nơi cấp, quốc tịch, lấy từ MPI (SKDT-P01); giấy chứng sinh định danh **người mẹ**; trẻ dưới 7 tuổi (giấy nghỉ việc) và dưới 16 tuổi (giấy ra viện) bắt buộc cha, mẹ hoặc người giám hộ; người vô danh tử vong: phát hành giấy báo tử với "không rõ" và bổ sung sau qua R06 (suy luận).
- **Bẫy**: mã số BHXH thay số thẻ BHYT chỉ khi BHXH có thông báo chính thức: cần cờ cấu hình chuyển đổi.

### GIAYTO-R23 — Đối soát với nơi nhận, theo dõi đa hạn chót
- **Căn cứ**: không có điều luật riêng; suy ra từ hạn ở R08, R10, R13, R19, R20 và trách nhiệm lưu, bảo đảm toàn vẹn chứng từ (QĐ 69 Đ5 k4; TT 25/2025 Đ28 k3).
- **Áp dụng**: vendor, cơ sở KCB · **Hiệu lực/hạn**: —
- **Mức**: NÊN
- **Phần mềm phải**: bảng điều khiển theo kênh (Cổng DVC quốc gia, Cổng giám định BHYT, Trục dữ liệu BYT, báo cáo tử vong, CSDL lái xe): phát hành, đã gửi, đã nhận, lỗi, quá hạn; đối soát cuối ngày giữa sổ giấy tờ và biên nhận; cảnh báo trước hạn (ví dụ còn 1 giờ làm việc cho giấy chứng sinh).

## 3. Pattern thiết kế

### GIAYTO-P01 — Sổ giấy tờ điện tử hợp nhất
- **Giải quyết**: R01, R02, R03, R06, R07, R22
- **Cách làm**: mọi giấy tờ là bản ghi `document` bất biến sau khi ký, có loại, mẫu, phiên bản, số, mã số, liên kết lượt KCB; PDF chỉ là phép chiếu từ dữ liệu có cấu trúc; chọn `template_id` theo `event_at`, không theo `now()`.
- **Gợi ý dữ liệu**: `doc_type(code, ten, can_cu, kenh_lien_thong[])` (`GCS`, `GBT`, `GNV_BHXH`, `GRV`, `TTHSBA`, `GCN_TT`, `PHIEU_HEN`, `PHIEU_CHUYEN`, `KSK`, `KSK_LAIXE`, `PHIEU_CDNNTV`); `doc_template(doc_type, mau_so, van_ban, hieu_luc_tu, hieu_luc_den, schema_json, sign_slots_json)`; `document(doc_type, template_id, so, ma_so, so_seri, encounter_id, patient_id, subject_snapshot_json, payload_json, payload_sha256, status, cap_lai, thay_the_cho_id, ly_do_thay_the, issued_at, issued_by, event_at)`; `UNIQUE(doc_type, ma_so) WHERE thay_the_cho_id IS NULL` (GCS cấp lại được trùng `ma_so` khi `cap_lai` và trỏ về bản cùng mã); `status IN ('DRAFT','PENDING_SIGN','ISSUED','SUPERSEDED','VOID')`; trigger chặn UPDATE `payload_json` khi khác DRAFT.
- **Đánh đổi**: một bảng chung dễ đối soát, audit; schema từng mẫu khác nhau nên dùng `payload_json` + JSON Schema theo mẫu, tách cột cho trường cần truy vấn (ngày nghỉ, ICD, số định danh).

### GIAYTO-P02 — Bộ ký theo vị trí (signature slots)
- **Giải quyết**: R03, R04, R17, R18, R21
- **Cách làm**: mỗi mẫu khai báo slot (`vai_tro`: NGUOI_HANH_NGHE, DAI_DIEN_DON_VI, TO_CHUC, NGUOI_DO_DE, THAN_NHAN, NGUOI_GHI_GIAY, NGUOI_KET_LUAN; `loai`: CA_NHAN | TO_CHUC | XAC_NHAN_DIEN_TU | TAY_SO_HOA; `bat_buoc`; `hieu_luc_tu`, ví dụ slot TO_CHUC của PHIEU_HEN/PHIEU_CHUYEN bắt buộc từ 2026-06-01). `PENDING_SIGN` → đủ slot bắt buộc → `ISSUED` → kích hoạt outbox (P03). Một người lấp hai slot khi mẫu cho phép (Mẫu 07).
- **Gợi ý dữ liệu**: `doc_signature(document_id, slot, signer_user_id, signer_role_title, cert_serial, cert_issuer, signed_at, sig_format, sig_value, ocsp_response, ok)`; `authorized_signer(user_id, doc_type, slot, bhxh_registered_at, valid_from, valid_to)` cho R21.
- **Đánh đổi**: cần HSM hoặc ký số từ xa cho chữ ký tổ chức (EMR-R08); chữ ký người thân thường là chữ ký tay → slot TAY_SO_HOA lưu bản quét.

### GIAYTO-P03 — Outbox đa kênh có đồng hồ hạn chót và biên nhận
- **Giải quyết**: R08, R10, R13, R19, R20, R23
- **Cách làm**: khi `document` sang `ISSUED`, sinh một dòng dispatch cho **mỗi** kênh bắt buộc của loại giấy (giấy chứng sinh → Cổng DVC quốc gia + Cổng giám định BHYT); mỗi kênh một adapter. Bản thay thế sinh dispatch mới `REPLACE`, tham chiếu giao dịch cũ nếu kênh hỗ trợ. Dùng chung hạ tầng với SKDT-P04, HTTT-BC-P01.
- **Gợi ý dữ liệu**: `doc_dispatch(document_id, channel (DVCQG|BHXH_GD|TRUC_BYT_KSK|CDC_KCB|CSDL_GT), payload_variant, signed_blob, sha256, deadline_at, attempt, status (QUEUED|SENT|ACK|REJECTED|RETRY|DEAD), remote_txn_id, remote_code, remote_msg, sent_at, ack_at)`; chỉ mục `(status, deadline_at)`; `deadline_at`: +04 giờ làm việc (GCS, GBT, theo lịch làm việc cơ sở), khi xuất viện (BHXH), +24 giờ sau đợt khám (KSK), +4 giờ (KSK lái xe, cấu hình).
- **Đánh đổi**: endpoint đổi từ 01/01/2027 → URL, chứng thư, mã dịch vụ là cấu hình.

### GIAYTO-P04 — Mã số giấy tờ có cấu trúc
- **Giải quyết**: R08, R10, R12
- **Cách làm**: bộ sinh số theo `(doc_type, ma_co_so, nam)`, không tái sử dụng khi hủy nháp; cấp lại không gọi sequence.
- **Gợi ý dữ liệu**: GCS `lpad(seq,5,'0') || '.GCS.' || ma_cskcb_5 || '.' || to_char(nam,'YY')`, sequence reset theo năm; giấy nghỉ việc `so_kcb` theo sổ khám từng bộ phận + `so_seri`; bảng cơ sở lưu song song `ma_cskcb_5` và `ma_dinh_danh_13` (SKDT-R18).
- **Đánh đổi**: sequence theo năm cần khóa hoặc bảng đếm để tránh trùng khi nhiều máy chủ; 5 chữ số giới hạn 99.999 giấy/năm/cơ sở (suy luận: đủ cho hầu hết cơ sở).

### GIAYTO-P05 — Quy tắc nghiệp vụ dạng bảng cho giấy BHXH
- **Giải quyết**: R12, R14, R15
- **Cách làm**: giới hạn 30/50/180 ngày, cha mẹ khi < 7 tuổi, giám hộ khi < 16, ngày bắt đầu = ngày khám, Mẫu 07 chỉ ngoại trú, ICD theo danh mục bệnh dài ngày đặt trong bảng quy tắc có ngày hiệu lực.
- **Gợi ý dữ liệu**: `rule(doc_type, field, expr, message, hieu_luc_tu, hieu_luc_den, can_cu)`.
- **Đánh đổi**: linh hoạt nhưng cần kiểm thử hồi quy khi đổi quy tắc.

### GIAYTO-P06 — Sự kiện lâm sàng → giấy tờ bắt buộc
- **Giải quyết**: R08, R10, R11, R14, R17
- **Cách làm**: `BIRTH_LIVE` → GCS (trước khi trẻ rời cơ sở); `DEATH` → GBT + phiếu CĐNNTV (tách quyền) + liên kết GCS nếu sơ sinh; `DISCHARGE` → giấy ra viện, tóm tắt nếu cần, gửi BHXH; `TRANSFER_OUT` → phiếu chuyển + giấy ra viện; `OUTPATIENT_SICK_LEAVE` → Mẫu 07. Không cho khóa HSBA khi còn giấy bắt buộc chưa phát hành.
- **Gợi ý dữ liệu**: `doc_task(encounter_id, event, doc_type, due_at, document_id, status)`.
- **Đánh đổi**: chặn đóng hồ sơ gây ùn ở khoa; cảnh báo mềm trước, chặn cứng ở bước khóa HSBA.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| GIAYTO-A01 | R01 | Danh mục mẫu: giấy báo tử còn PL I TT 24/2020? Tóm tắt HSBA còn mẫu TT 32/TT 18? Giấy nghỉ việc còn TT 56/TT 18? Giấy chứng sinh còn TT 17/2012, 27/2019? Mẫu KSK theo TT 25/2026 cho hồ sơ từ 01/07/2026? | Mẫu in, cấu hình mẫu, ngày áp dụng | BẮT BUỘC |
| GIAYTO-A02 | R02 | In thử từng giấy, đối chiếu đủ trường; bỏ trống trường bắt buộc có bị chặn; tìm chữ viết tắt | Bản in, thông báo lỗi | BẮT BUỘC |
| GIAYTO-A03 | R03, R04 | Lấy 1 file điện tử mỗi loại, kiểm chữ ký bằng công cụ độc lập: đủ chữ ký cá nhân và tổ chức theo mẫu? Chứng thư còn hiệu lực lúc ký? | File đã ký, báo cáo kiểm chữ ký | BẮT BUỘC? |
| GIAYTO-A04 | R04, R17 | Phiếu hẹn, phiếu chuyển điện tử sau 01/06/2026 có chữ ký số cơ sở? Mẫu điện tử còn chữ "đóng dấu"? | File phiếu, kết quả kiểm | BẮT BUỘC |
| GIAYTO-A05 | R05 | Yêu cầu cấp tóm tắt HSBA, giấy nghỉ việc muộn: có giấy hẹn ghi thời gian? Tỷ lệ trả đúng hẹn | Giấy hẹn, truy vấn | BẮT BUỘC |
| GIAYTO-A06 | R06 | Sửa giấy đã phát hành: sửa tại chỗ được không? Cấp lại có "Cấp lại", giữ bản cũ, gửi lại dữ liệu? GCS cấp lại giữ mã số? | Lịch sử phiên bản, log gửi | BẮT BUỘC |
| GIAYTO-A07 | R08 | Mỗi GCS: `ack_at - issued_at` theo giờ làm việc; số quá 04 giờ làm việc 3 tháng gần nhất; mã khớp `^[0-9]{5}\.GCS\.[0-9]{5}\.[0-9]{2}$` và duy nhất | Kết quả truy vấn, biên nhận Cổng | BẮT BUỘC |
| GIAYTO-A08 | R08, R22 | Sinh đôi: 2 giấy, 2 mã? Mẹ không có BHXH/BHYT: "0000000000"? Mẹ người nước ngoài: dân tộc "Người nước ngoài" + quốc tịch? | Hồ sơ thử | BẮT BUỘC |
| GIAYTO-A09 | R08, R10 | Endpoint còn hard-code "Phần mềm DVC liên thông"? Có kế hoạch chuyển sang Hệ thống điều phối Cổng DVC từ 01/01/2027? | Tài liệu cấu hình, kế hoạch | BẮT BUỘC |
| GIAYTO-A10 | R10 | Ca tử vong thử: Mẫu 05; ca chết trên đường cấp cứu có ô tích; dữ liệu gửi trong 04 giờ làm việc | Giấy báo tử, log gửi | BẮT BUỘC |
| GIAYTO-A11 | R11 | Phiếu CĐNNTV có bị in kèm giấy báo tử, lưu chung HSBA, hiện cho người nhà? Có xuất cho hệ thống BYT? | Phân quyền, bản in, file xuất | BẮT BUỘC? |
| GIAYTO-A12 | R12 | Thử Mẫu 07 cho nội trú (phải chặn); 31 ngày nghỉ (chặn trừ lý do 50/180); trẻ 5 tuổi thiếu cha mẹ (chặn); ngày bắt đầu khác ngày khám (cảnh báo) | Thông báo lỗi | BẮT BUỘC |
| GIAYTO-A13 | R13 | Tỷ lệ lượt ra viện có XML7/XML8/XML11 đã gửi; thời gian từ ra viện đến gửi; người không BHYT có được gửi? | Truy vấn, log Cổng | BẮT BUỘC |
| GIAYTO-A14 | R14, R15 | Giấy ra viện có ICD-10, tuổi thai, số ngày nghỉ ≤ 30 (hoặc 50/180), giám hộ khi < 16? Tóm tắt theo Mẫu 03 và nhận đề nghị Mẫu 04? | Bản in, cấu hình | BẮT BUỘC |
| GIAYTO-A15 | R16 | Chứng nhận thương tích có tình trạng thương tích lúc vào/ra viện? Có giấy hẹn? | Bản in | BẮT BUỘC |
| GIAYTO-A16 | R18 | Danh sách bác sĩ được phân công KSK bằng văn bản? Người ngoài danh sách ký được không? KSK đơn lẻ trả trong 24 giờ? Giấy ghi hạn 12 tháng? KSK theo yêu cầu thiếu chuyên khoa bị chặn phân loại? | Văn bản phân công, log, bản in | BẮT BUỘC |
| GIAYTO-A17 | R19 | Chạy SKDT-A15–A18 (tài khoản, mã 13 số, 24 giờ, `PS_SIGNATURE_INVALID`, dữ liệu tồn) | Như SKDT | BẮT BUỘC |
| GIAYTO-A18 | R20 | Giấy KSK lái xe theo TT 36/2024; có kết quả ma túy; dữ liệu gửi trong 4 giờ | Bản in, log | BẮT BUỘC |
| GIAYTO-A19 | R21 | Danh sách người ký giấy chứng nhận khớp danh sách đã đăng ký với BHXH? Người chưa đăng ký ký được Mẫu 07? | Danh sách BHXH, cấu hình người ký | BẮT BUỘC |
| GIAYTO-A20 | R22 | Người nước ngoài chỉ có hộ chiếu; người vô danh tử vong: phát hành được giấy và bổ sung sau? | Hồ sơ thử | BẮT BUỘC |
| GIAYTO-A21 | R23 | Có bảng điều khiển hạn chót theo kênh, đối soát cuối ngày? | Ảnh màn hình, báo cáo | NÊN |
| GIAYTO-A22 | R09 | Kế hoạch đáp ứng Luật Hộ tịch 2026 (chia sẻ tự động với hệ thống hộ tịch từ 01/03/2027)? | Lộ trình sản phẩm | NÊN |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 01/01/2023 | Liên thông giấy KSK lái xe trong 4 giờ (CV 7586, thứ cấp) | Cơ sở khám lái xe | Đã qua |
| 10/06/2024; 01/07/2024 | NĐ 63: GCS/GBT liên thông có ký số trong 04 giờ làm việc; tiếp nhận hồ sơ liên thông từ 01/07/2024 | Cơ sở có sinh/tử; vendor | Đã qua |
| 01/01/2025 | Phiếu hẹn, phiếu chuyển giấy hoặc điện tử (TT 01/2025); KSK lái xe (TT 36/2024) | Cơ sở KCB BHYT; cơ sở khám lái xe | Đã qua |
| 30/06/2025 | Hết dùng sổ KSK định kỳ lái xe mẫu cũ in sẵn (TT 36 Đ9 k3) | Cơ sở khám lái xe | Đã qua |
| 01/07/2025 | TT 25/2025: 13 mẫu mới; TT 56/2017, TT 18/2022 hết hiệu lực; BHXH tiếp nhận dữ liệu ốm đau, thai sản (QĐ 69) | Mọi cơ sở KCB | Đã qua |
| 01/10/2025 | TT 22/2025 giấy chứng sinh; TT 17/2012, 34/2015, 27/2019 hết hiệu lực | Cơ sở có đỡ đẻ | Đã qua |
| 31/12/2025 | Hết dùng mẫu giấy hẹn, giấy chuyển cũ (TT 01/2025 Đ15, xem BHYT-GD) | Cơ sở KCB BHYT | Đã qua |
| 15/05/2026 | NĐ 90/2026 (Đ46, Đ95 k4) | Mọi cơ sở | Đã qua |
| 31/05/2026 | QĐ 1551: liên thông KSK 24 giờ (SKDT-R15) | Cơ sở có KSK | Đã qua |
| 01/06/2026 | Phiếu hẹn, phiếu chuyển điện tử: ký số cơ sở thay đóng dấu | Cơ sở KCB BHYT, vendor | Đã qua |
| 01/07/2026 | TT 25/2026 Đ2: hồ sơ, nội dung KSK theo 4 mẫu mới | Cơ sở có KSK | Đã qua |
| 15/07/2026 | Đồng bộ xong dữ liệu KSK tồn đọng | Cơ sở có KSK | Đã qua |
| 01/09/2026 | NĐ 301: GCS/GBT liên thông với Cổng DVC quốc gia | Cơ sở KCB; vendor | Đã qua |
| 01/01/2027 | Phần mềm DVC liên thông ngừng; chuyển sang Hệ thống điều phối của Cổng DVC (đổi endpoint) | Vendor | Sắp tới |
| 01/03/2027 | Luật Hộ tịch 2026 có hiệu lực; "Trích lục khai tử" → "Giấy chứng tử" | Cơ sở KCB (dữ liệu), vendor | Sắp tới |
| 10/04/2027 | Hạn rà soát, nâng cấp phần mềm ký số theo NĐ 23/2025 (suy luận cách tính, xem EMR-R07) | Vendor | Sắp tới |
| 30/06/2030 | Tổng kết liên thông dữ liệu ốm đau, thai sản (QĐ 69 Đ6 k3 b) | BHXH | Sắp tới |
| 01/01/2031 | Khai sinh, khai tử chủ động thống nhất toàn quốc | Cơ sở KCB, chính quyền | Sắp tới |
| Thường xuyên | GCS, GBT: 04 giờ làm việc; chứng từ BHXH: khi xuất viện; KSK định kỳ/sàng lọc: 24 giờ; KSK lái xe: 4 giờ; trả giấy KSK đơn lẻ: 24 giờ | Cơ sở KCB | — |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**
- Giấy chứng sinh: TT 17/2012 → sửa bởi TT 34/2015, TT 27/2019 → **TT 22/2025** (01/10/2025). Mẫu PL 5 TT 56/2017 chỉ còn cho trẻ sinh trước 01/10/2025.
- Giấy tờ hưởng BHXH: TT 56/2017 → sửa bởi TT 18/2022 → **TT 25/2025** (01/07/2025), thay toàn bộ (C16). Danh mục bệnh dài ngày: TT 46/2016 → PL I TT 25/2025.
- Giấy báo tử: PL I TT 24/2020 → **Mẫu 05 TT 25/2025**. Phần phiếu CĐNNTV của TT 24/2020 còn hiệu lực; hướng dẫn ghi phiếu QĐ 1921 → QĐ 1996/2025 (thứ cấp).
- Tóm tắt HSBA: PL 4 TT 18/2022 → Mẫu 52/BV2 TT 32/2023 → **Mẫu 03 (+ Mẫu 04) TT 25/2025** (C01: EMR từng dẫn "CV-01 TT 32/2023").
- KSK: TT 14/2013 → TT 32/2023 Chương VI → Đ34, Đ36, PL XXIV sửa bởi **TT 25/2026** (01/07/2026).
- KSK lái xe: TTLT 24/2015/TTLT-BYT-BGTVT → **TT 36/2024** (01/01/2025).
- Liên thông khai sinh/khai tử: NĐ 63/2024 → sửa bởi **NĐ 301/2026** (01/09/2026); Luật Hộ tịch 60/2014 → **Luật 03/2026/QH16** (01/03/2027); Phần mềm DVC liên thông → Hệ thống điều phối của Cổng DVC quốc gia (01/01/2027).
- Phiếu hẹn, phiếu chuyển: "đóng dấu" → ký số xác thực của cơ sở cho bản điện tử (TT 06/2026 Đ5 k2, 01/06/2026).
- Chuẩn XML: QĐ 130 → 4750 → 3176 → QĐ 1931/QĐ-BYT năm 2026 sửa QĐ 130 (C23).
- Thời hạn lưu trữ hồ sơ: TT 53/2017 → **TT 33/2025** (01/07/2025).

**Bẫy trích dẫn**
1. "Ký số tổ chức thay con dấu từ 01/06/2026" chỉ đúng cho phiếu hẹn và phiếu chuyển bản điện tử.
2. Giấy nghỉ việc BHXH: nội dung ở TT 25/2025 **Đ10** + Mẫu 07, không phải Đ29.
3. Tài liệu tập huấn Cục QLKCB 2026 vẫn dẫn TT 24/2020 cho mẫu giấy báo tử: mẫu đó hết hiệu lực.
4. TT 25/2025 (BHXH) ≠ TT 25/2026 (sửa TT 32, KSK).
5. TT 32/2023 về KSK là Chương VI (Đ30–38), không phải Chương X (HSBA).
6. Đọc NĐ 63/2024 riêng sẽ thấy "Phần mềm dịch vụ công liên thông"; sau NĐ 301 nhiều chỗ đã là "Cổng Dịch vụ công quốc gia".
7. `MA_CSKCB` 5 ký tự (trong mã giấy chứng sinh) ≠ mã định danh 13 số/`MA_GTIN_CSKCB` (QĐ 1551). Xem SKDT-R18, BHYT-DATA-R24.
8. "Giấy chuyển viện" (QĐ 69) = phiếu chuyển cơ sở KCB (TT 01/2025 PL VI) = XML13 "giấy chuyển tuyến": ba tên cho một giấy.
9. NĐ 90/2026 Đ95 k4 a dùng tên cũ "giấy chứng nhận không đủ sức khỏe".
10. QĐ 69/2025, TT 25/2025 dẫn NĐ 13/2023, NĐ 166/2016: đọc theo văn bản thay thế.
11. TT 22/2025 bản đăng lại phổ biến để trống số và ngày; trích dẫn chính thức nên dùng bản Công báo.
12. TT 32/2023 Đ38 (và research gốc) ghi hồ sơ KSK "lưu theo TT 53/2017": TT 53/2017 đã hết hiệu lực từ 01/07/2025. Dẫn đúng là **TT 33/2025 PL mục 48**: giấy khám sức khỏe (đi học, đi làm, hoạt động khác) **02 năm** (đã đối chiếu phụ lục gốc).
13. TT 25/2025 chỉ có bản scan OCR không dấu: Mẫu 03–13 và thân văn bản trong file này chỉ diễn giải (C21); Mẫu 01, 02, 07 và Đ95 k4 NĐ 90 đã đối chiếu ảnh trang.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. QĐ 1898/QĐ-BYT 2025 bản gốc và PL I (schema giấy chứng sinh: XML hay JSON, vị trí chữ ký số); có bao phủ Mẫu 02 mang thai hộ không.
2. Mã số và đặc tả dữ liệu giấy báo tử điện tử (văn bản "hướng dẫn Đề án 06" mà tài liệu tập huấn nhắc).
3. Đặc tả tích hợp Cổng DVC quốc gia/Phần mềm DVC liên thông cho cơ sở KCB (API, chứng thư, mã dịch vụ) và lộ trình chuyển từ 01/01/2027: hỏi Văn phòng Chính phủ/BCA/BYT.
4. Phụ lục Mẫu 01–04 PL XXIV mới (TT 25/2026): chưa có; cần đối chiếu với PL01 QĐ 1551.
5. KSK đi học, đi làm, theo yêu cầu có phải liên thông lên CSDL sức khỏe cá nhân của BYT: hỏi Cục QLKCB.
6. CV 7586/2022 (4 giờ, Cổng giám định hoặc `dulieu.kcb.vn`) còn áp dụng sau TT 36/2024 và sau khi CSDL giao thông chuyển cho ngành công an không.
7. Chứng từ BHXH cho người bệnh không có BHYT hoặc cơ sở không ký hợp đồng BHYT: Cổng giám định có nhận, bằng định danh gì.
8. Cơ chế hủy/thay thế dữ liệu điện tử đã liên thông (GCS, GBT đã dùng để khai sinh/khai tử; giấy nghỉ việc đã được chi trả): hỏi BHXH VN, Bộ Tư pháp.
9. Ký số tổ chức thay dấu cho giấy ngoài phiếu hẹn/phiếu chuyển: BHXH, cơ quan hộ tịch, cơ quan nhận KSK có bắt buộc chấp nhận khi mẫu ghi "đóng dấu"? Hỏi luật sư.
10. Đăng ký mẫu dấu, mẫu chữ ký với BHXH (NĐ 90 Đ95 k4 a) khi ký số: đăng ký chứng thư trên Cổng giám định có thay được không. Hỏi BHXH.
11. TT 24/2020 bản gốc: phần còn hiệu lực (phiếu CĐNNTV, thống kê, thời hạn báo cáo); kênh `cdc.kcb.vn` chỉ thấy trong tài liệu tập huấn.
12. Nghị định hướng dẫn Luật Hộ tịch 2026 (Đ29 k4 b): chưa ban hành tại 2026-10-06.
13. TT 25/2025 bản có lớp text/bản Công báo: cần để trích nguyên văn Mẫu 03–13.
14. Luật BHXH 2024 Đ47, Đ61 bản gốc: mới đọc qua thứ cấp.
