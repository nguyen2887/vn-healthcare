# EMR — Hồ sơ bệnh án điện tử: chức năng EMR, ký số, lưu trữ

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám và cơ sở khác có điều trị nội trú/ban ngày/ngoại trú; vendor EMR/HIS/CIS · Research gốc: `research/deep/EMR.md`

Không phải ý kiến pháp lý. Chỗ ghi "(suy luận)" là diễn giải của người nghiên cứu. Phạm vi giao sang domain khác: cấp độ an toàn HTTT → ANM; dữ liệu cá nhân → DLCN; kê đơn → DUOC; ICD và danh mục → MA-LT; VNeID, Sổ SKĐT → SKDT; giấy ra viện, tóm tắt, báo tử → GIAYTO; dữ liệu có luật bảo mật riêng → BAOMAT-CB.

## Tóm tắt nhanh

- **Hạn pháp lý** (TT 13/2025 Đ4 k2): bệnh viện xong HSBA điện tử chậm nhất **30/09/2025** (đã qua); cơ sở KCB khác có điều trị nội trú, ban ngày, ngoại trú hoàn thành chậm nhất **31/12/2026**.
- Mốc "BV bỏ bệnh án giấy **01/01/2027**" chỉ là **mục tiêu kế hoạch** (QĐ 586/QĐ-BYT, CT 04/CT-BYT; QĐ 965 đặt 2030), không phải hạn luật định và không có chế tài riêng.
- TT 13 chỉ có 6 điều. Mọi yêu cầu chức năng (phân quyền, ghi vết, sao lưu, XML/JSON, cloud tại VN, bàn giao dữ liệu) nằm ở **CV 365/TTYQG-GPQLCL** — hướng dẫn kỹ thuật, không phải VBQPPL, nhưng TT 13 Đ6 k3 a buộc làm theo.
- Chế tài tổ chức (NĐ 90/2026, mức tổ chức gấp đôi cá nhân): không có quy chế HSBA điện tử hoặc không đáp ứng yêu cầu CNTT: **6–10 triệu**; tẩy xóa, sửa HSBA làm sai lệch: **10–20 triệu**.
- Hạn sắp tới: **~23/10/2026** rà soát hệ thống chuyển đổi giấy ↔ điện tử (NĐ 137 Đ23); **15/11/2026** TT 41/2017/TT-BTTTT bị bãi bỏ (quy chế ký số BV công phải đổi căn cứ); **10/04/2027** phần mềm ký số phải nâng cấp theo NĐ 23/2025 Đ17.
- Thời hạn lưu: HSBA thường 10 năm, tử vong 30 năm, tâm thần/TNLĐ/TNGT 20 năm; hồ sơ người hiến và người được ghép **30 năm** (Luật 75/2006 thắng TT 33/2025). Tính từ **năm** kết thúc công việc.
- Bẫy: ảnh chữ ký dán vào PDF không phải chữ ký số; mẫu tóm tắt HSBA hiện hành là **Mẫu 03 TT 25/2025**, không phải CV-01 TT 32; điều cấm tẩy xóa HSBA là Luật KCB **Đ7 k10**.

## Mục lục

| ID | Tiêu đề |
|---|---|
| EMR-R01 | Nghĩa vụ và lộ trình triển khai HSBA điện tử |
| EMR-R02 | Phòng khám chỉ khám và kê đơn |
| EMR-R03 | Nội dung HSBA đủ trường theo mẫu BYT |
| EMR-R04 | Người ghi, thời điểm ghi, viết tắt |
| EMR-R05 | Định danh người bệnh theo số định danh cá nhân |
| EMR-R06 | Ký và xác nhận điện tử của NVYT, người bệnh, người đại diện |
| EMR-R07 | Phần mềm ký số và kiểm tra chữ ký theo NĐ 23/2025 |
| EMR-R08 | Ký số của tổ chức; căn cứ sau 15/11/2026 |
| EMR-R09 | Xác nhận của người bệnh bằng sinh trắc hoặc OTP |
| EMR-R10 | Toàn vẹn, hiệu chỉnh có vết |
| EMR-R11 | Phân quyền, xác thực, bảo mật truy cập |
| EMR-R12 | Nhật ký ghi vết mọi giao dịch |
| EMR-R13 | In theo mẫu; bản giấy chuyển đổi từ HSBA điện tử |
| EMR-R14 | Quyền người bệnh: đọc, sao chụp, nhận tóm tắt |
| EMR-R15 | Khai thác HSBA của bên thứ ba theo trạng thái hồ sơ |
| EMR-R16 | Số hóa bệnh án giấy cũ |
| EMR-R17 | Chuyển tiếp người bệnh đang dùng bệnh án giấy |
| EMR-R18 | Kết xuất XML/JSON theo phụ lục CV 365 |
| EMR-R19 | Dùng danh mục dùng chung BYT |
| EMR-R20 | Kiến trúc; dữ liệu HSBA lưu độc lập |
| EMR-R21 | Sao lưu, phục hồi, mã hóa |
| EMR-R22 | Thời hạn lưu trữ HSBA |
| EMR-R23 | Lưu thông điệp dữ liệu kèm metadata |
| EMR-R24 | Hủy HSBA hết hạn |
| EMR-R25 | Quy chế HSBA điện tử của cơ sở |
| EMR-R26 | Hạ tầng tại VN; sở hữu và bàn giao dữ liệu |
| EMR-R27 | ATTT, IPv6, chuẩn kỹ thuật theo CV 365 |
| EMR-R28 | Đơn thuốc trong HSBA |

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 13/2025/TT-BYT (06/06/2025) | Hướng dẫn triển khai HSBA điện tử (Đ1–Đ6) | 21/07/2025 | Còn HL; làm hết HL TT 46/2018 từ 06/06/2025 | gốc-OCR (có dấu); Đ4 k2 đã đối chiếu bản có dấu thứ cấp | [PDF sao y, SYT Quảng Ninh](https://soytequangninh.gov.vn/upload/1002610/20250610/THONG_TU_HSBA_DIEN_TU_21_7_2025TT_13_2025__TT-BYT_ngay_6_6_2025_f5604afb8f.pdf) |
| 365/TTYQG-GPQLCL (06/06/2025) | Hướng dẫn kỹ thuật phần mềm HSBA điện tử + PL "Mô tả dữ liệu trao đổi HSBA điện tử" | Từ khi ban hành | Hướng dẫn kỹ thuật, không phải VBQPPL | gốc (PDF ký số, có text) | [PDF, UBND Sơn Tịnh đăng lại](https://sontinh.quangngai.gov.vn/upload/2006782/20260423/H%C6%AF%E1%BB%9ANG%20D%E1%BA%AAN%20K%E1%BB%B8%20THU%E1%BA%ACT%20TRI%E1%BB%82N%20KHAI.pdf) |
| 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ2 k17, Đ7 k10, Đ8, Đ10 k2, Đ12, Đ62, Đ69, Đ76, Đ120 | 01/01/2024 | Còn HL | gốc | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 32/2023/TT-BYT | Chi tiết Luật KCB; Chương X (Đ51–52) HSBA; PL XXVIII (bệnh án), PL XXIX (giấy, phiếu) | 01/01/2024 | Còn HL; TT 25/2026 không sửa Chương X; Mẫu 52/BV2, 53/BV2 PL XXIX hết HL từ 01/07/2025 (TT 25/2025 Đ29 k2) | gốc | [PDF ký số, BV Bệnh Nhiệt đới](https://bvbnd.vn/wp-content/uploads/2024/01/32-thongtuhuongdanluatkbcb31122023_91202410.pdf) · [PL XXVIII, BV Bắc Hà](https://benhvienbacha.vn/wp-content/uploads/2024/01/28.-Phu-luc-XVIII.-Mau-benh-an.pdf) |
| 25/2025/TT-BYT | Mẫu giấy tờ (Mẫu 03 tóm tắt HSBA, Mẫu 04 giấy đề nghị, Mẫu 05 giấy báo tử…) | 01/07/2025 | Còn HL | gốc-OCR (xem GIAYTO) | xem GIAYTO |
| 25/2026/TT-BYT | Sửa TT 32/2023 (chỉ phần KSK) | 15/08/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/25-byt.signed.pdf) |
| 33/2025/TT-BYT | Thời hạn lưu trữ hồ sơ, tài liệu ngành y tế; thay TT 53/2017 | 01/07/2025 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [Phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| 75/2006/QH11 | Luật hiến, lấy, ghép mô (Đ38 k4: lưu 30 năm) | 01/07/2007 | Còn HL | gốc (xem BAOMAT-CB) | xem BAOMAT-CB |
| 26/2025/TT-BYT | Đơn thuốc, kê đơn ngoại trú | 01/07/2025 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf) |
| 20/2023/QH15 | Luật Giao dịch điện tử: Đ8–13, Đ22–23 | 01/07/2024 | Còn HL; Luật 20/2026/QH16 sửa từ 01/03/2027, không sửa Đ22–23 (xem BAOMAT-CB-R26) | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/8/luat20-2023-qh15..pdf) |
| 23/2025/NĐ-CP | Chữ ký điện tử và dịch vụ tin cậy; thay NĐ 130/2018 | 10/04/2025 | Còn HL | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/02/23-cp.signed.pdf) |
| 59/2026/TT-BKHCN (25/09/2026) | Bãi bỏ TT 41/2017/TT-BTTTT (và TT 37/2009, 08/2011) | 15/11/2026 | Sắp HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/59-bkhcn.signed.pdf) |
| 137/2024/NĐ-CP | GDĐT của CQNN: Đ4–5 chuyển đổi giấy ↔ điện tử, Đ23 chuyển tiếp | Từ ngày ký (23/10/2024 theo inventory) | Còn HL | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/10/137-cp.signed.pdf) · [VB 211481](https://vanban.chinhphu.vn/?pageid=27160&docid=211481) |
| 90/2026/NĐ-CP | Xử phạt VPHC y tế: Đ4, Đ38–40, Đ85–86; thay NĐ 117/2020 | 15/05/2026 | Còn HL | gốc-OCR (chỉ diễn giải) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| 33/2024/QH15 | Luật Lưu trữ: Đ3, Đ15, Đ16, Đ32–37, Đ53 | 01/07/2025 | Còn HL; bắt buộc với tài liệu khu vực công, tổ chức tư tự quyết (Đ3 k5) | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/9/33-2024-qh15.pdf) |
| 113/2025/NĐ-CP | Chi tiết Luật Lưu trữ (kho lưu trữ số, hủy, dịch vụ lưu trữ) | 21/07/2025 | Còn HL; với EMR chỉ tham chiếu | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/6/113-cp.signed.pdf) · [VB 213822](https://vanban.chinhphu.vn/?pageid=27160&docid=213822) |
| 586/QĐ-BYT (09/03/2026) | Kế hoạch triển khai HSBA điện tử năm 2026 | Từ khi ký | Văn bản kế hoạch | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-586-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-427964-d1.html) · [SYT Đồng Nai, thứ cấp](https://syt.dongnai.gov.vn/vi/news/chuyen-doi-so/dong-nai-day-nhanh-tien-do-trien-khai-ho-so-benh-an-dien-tu-tai-cac-co-so-y-te-42075.html) |
| 965/QĐ-BYT (10/04/2026) | Kế hoạch HSBA điện tử 2026–2030 | Từ khi ký | Văn bản kế hoạch | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-965-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-431556-d1.html) |
| 04/CT-BYT (07/04/2026) | Đẩy mạnh triển khai HSBA điện tử | Từ khi ký | Chỉ thị | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/chi-thi-04-ct-byt-2026-day-manh-trien-khai-ho-so-benh-an-dien-tu-tai-co-so-kham-chua-benh-431124-d1.html) |
| 54/2017/TT-BYT | Tiêu chí ứng dụng CNTT tại cơ sở KCB | 27/02/2018 | Còn HL một phần: Mục VIII PL I và tiêu chí EMR hết HL từ 06/06/2025 (TT 13 Đ4 k3 b) | gốc-OCR (qua TT 13) | — |
| (thực tiễn) | Cổng benhandientu.moh.gov.vn: danh sách cơ sở công bố (1.273 cơ sở, kiểm tra ngày 2026-10-05) | — | Mục "Văn bản pháp lý có hiệu lực" còn liệt kê thông tư HSBA điện tử cũ đã hết HL (mục 6, bẫy 11) | đã mở | [benhandientu.moh.gov.vn](https://benhandientu.moh.gov.vn/) · [Ví dụ QĐ công bố TTYT Mỹ Tú](https://benhandientu.moh.gov.vn/storage/uploads/2025/10/quyet-dinh-162-ttyt-my-tu-su-dung-emr-thay-benh-an-giay-1759413339.pdf) |

**Chế tài NĐ 90/2026** (gốc-OCR, diễn giải). Mức Chương II là mức cá nhân; tổ chức gấp 2 (Đ4 k5).

| Hành vi | Điều | Cá nhân | Tổ chức |
|---|---|---|---|
| Không ban hành quy chế lập, cập nhật, quản lý, lưu trữ, sử dụng, ATTT với HSBA điện tử | Đ39 k2 c | 3–5 tr | 6–10 tr |
| Không đáp ứng yêu cầu CNTT triển khai HSBA điện tử | Đ39 k2 d | 3–5 tr | 6–10 tr |
| Không lập HSBA hoặc không ghi đủ các mục theo mẫu | Đ40 k1 a | 1–3 tr | 2–6 tr |
| Không lưu trữ hồ sơ, bệnh án theo quy định | Đ40 k1 b | 1–3 tr | 2–6 tr |
| Làm lộ tình trạng bệnh, thông tin người bệnh, HSBA | Đ38 k3 c | 1–3 tr | 2–6 tr |
| Tẩy xóa, sửa HSBA làm sai lệch thông tin KCB | Đ38 k5 e | 5–10 tr | 10–20 tr |
| Lập HSBA khống để chiếm đoạt hoặc gây thiệt hại quỹ BHYT | Đ85, Đ86 | theo giá trị vi phạm | ×2 |

## 2. Yêu cầu

### EMR-R01 — Nghĩa vụ và lộ trình triển khai HSBA điện tử
- **Căn cứ**: TT 13/2025 Đ4 k2 a: bệnh viện "triển khai hồ sơ bệnh án điện tử chậm nhất vào ngày 30 tháng 9 năm 2025". Đ4 k2 b: cơ sở KCB khác có người bệnh điều trị nội trú, ban ngày và ngoại trú hoàn thành chậm nhất 31/12/2026. Đ6 k3 a: triển khai theo TT 13 và hướng dẫn của cơ quan có thẩm quyền (tức CV 365). Luật KCB Đ69 k1: HSBA giấy và điện tử có giá trị pháp lý như nhau.
- **Áp dụng**: BV công và tư (hạn đã qua); PK, TTYT không phải BV, trạm y tế có điều trị · **Hiệu lực/hạn**: 30/09/2025; 31/12/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lập HSBA điện tử thay hoàn toàn bản giấy cho mọi loại bệnh án cơ sở dùng; đáp ứng R03–R28 để cơ sở tự đánh giá "đạt".
- **Bẫy**: TT 13 không định nghĩa "triển khai/hoàn thành" và không có thủ tục công nhận thay TT 46/2018 (suy luận). Thực tiễn: hội đồng thẩm định nội bộ tự đánh giá theo TT 13 + CV 365, Giám đốc ra QĐ sử dụng HSBA điện tử thay giấy, công bố trên benhandientu.moh.gov.vn. "nội trú, ban ngày **và** ngoại trú" nên đọc là có bất kỳ loại nào (suy luận).

### EMR-R02 — Phòng khám chỉ khám và kê đơn
- **Căn cứ**: Luật KCB Đ69 k1 (người bệnh điều trị nội trú, ban ngày, ngoại trú phải được lập HSBA); Đ76 (điều trị ngoại trú áp dụng cho các trường hợp không phải nội trú — định nghĩa phần dư); TT 26/2025 Đ5 k1 a (lượt khám kê đơn mà "người bệnh không có hồ sơ bệnh án ngoại trú") và b (có HSBA ngoại trú); Mẫu 15/BV1 gắn HSBA ngoại trú với "đợt điều trị".
- **Áp dụng**: PK đa khoa, chuyên khoa, bác sĩ gia đình, YHCT tư nhân · **Hiệu lực/hạn**: 31/12/2026 nếu thuộc phạm vi
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: (1) mở được HSBA ngoại trú điện tử theo mẫu 15/BV1, 16/BV1, 19/BV1 và mẫu ngoại trú PHCN, có số ngoại trú và ngày bắt đầu/kết thúc đợt; (2) lượt không mở HSBA vẫn lưu phiếu khám có người ghi, thời gian, chữ ký (R04, R06), đơn thuốc điện tử và giữ đủ thời hạn (R22); (3) cấu hình bắt buộc mở HSBA ngoại trú cho tình huống chắc chắn cần (ung thư dùng thuốc gây nghiện TT 26 Đ8 k1; điều trị nhiều buổi PHCN, YHCT, thủ thuật theo đợt).
- **Bẫy**: không có câu miễn trừ cho phòng khám. Đọc chặt Đ76 + Đ69 k1 thì mọi lượt chữa bệnh không nội trú cần HSBA; đọc theo hệ thống (TT 26 Đ5 k1 a) thì lượt chỉ kê đơn không có HSBA (suy luận, hai cách đọc). Khi audit coi là **trong phạm vi** từ 31/12/2026 cho đến khi có văn bản trả lời của BYT/Sở Y tế. Kê đơn điện tử vẫn bắt buộc (xem R28).

### EMR-R03 — Nội dung HSBA đủ trường theo mẫu BYT
- **Căn cứ**: TT 13 Đ1 k2 (đủ thông tin theo Chương X TT 32/2023); TT 32 Đ51 (mẫu PL XXVIII, XXIX), Đ52 k1 b (bệnh án điện tử phải đủ nội dung các trường); Luật KCB Đ2 k17; CV 365 PL III.1.1 a.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: theo R01
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mẫu nhập và hiển thị cho từng loại bệnh án, phiếu cơ sở dùng (PL XXVIII: 29 mẫu bệnh án), đủ mọi trường; bản in/PDF đúng bố cục (R13); ràng buộc trường bắt buộc khi đóng HSBA.
- **Bẫy**: mẫu QĐ 4069/2001, QĐ 1941/2019 (YHCT), QĐ 3730/2021 (PHCN) đã hết HL (TT 32 Đ53 k2). Tóm tắt HSBA dùng **Mẫu 03 PL II TT 25/2025** (kèm giấy đề nghị Mẫu 04), không còn CV-01/Mẫu 52/BV2 TT 32; giấy báo tử dùng Mẫu 05 TT 25/2025, không còn mẫu PL I TT 24/2020 (xem GIAYTO-R10, R15). TT 25/2026 không sửa mẫu HSBA.

### EMR-R04 — Người ghi, thời điểm ghi, viết tắt
- **Căn cứ**: TT 32 Đ52 k2 a (chính xác, trung thực, đầy đủ), k2 c (không viết tắt trong tài liệu cấp cho người bệnh: tóm tắt HSBA, tài liệu bàn giao, giấy chuyển tuyến, giấy hẹn; viết tắt khác theo danh sách cơ sở ban hành), k2 d ("Thông tin trong hồ sơ bệnh án cần thể hiện rõ thời gian và người ghi chép.").
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi mục ghi chép lưu `author_user_id`, chức danh, `recorded_at` do server cấp, thời điểm lâm sàng nếu khác; có danh mục viết tắt; bản xuất cho người bệnh tự bung viết tắt hoặc cảnh báo.
- **Bẫy**: tài khoản dùng chung hoặc "ghi hộ" không lưu người ghi thật là vi phạm trực tiếp.

### EMR-R05 — Định danh người bệnh theo số định danh cá nhân
- **Căn cứ**: TT 13 Đ1 k3 (kết nối HSBA với số định danh cá nhân của công dân và người nước ngoài có tài khoản định danh điện tử); CV 365 PL III.1.1 a (mỗi người bệnh một mã định danh đơn nhất theo số định danh cá nhân); TT 26 Đ6 k2.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 21/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: master patient index lấy số định danh cá nhân làm khóa liên thông; mã tạm cho sơ sinh, người nước ngoài không có tài khoản, người vô danh cấp cứu; gộp hồ sơ (merge) có ghi vết khi có số thật; chặn tạo trùng.
- **Bẫy**: kết nối VNeID, Sổ SKĐT xem SKDT.

### EMR-R06 — Ký và xác nhận điện tử của NVYT, người bệnh, người đại diện
- **Căn cứ**: TT 13 Đ3: ký hoặc xác nhận theo một trong ba hình thức: chữ ký điện tử hợp pháp; kỹ thuật sinh trắc học; hình thức xác nhận điện tử khác theo Luật GDĐT Đ22 k4. Luật GDĐT Đ22 k1–3 (các loại chữ ký), Đ23 k2 (chỉ chữ ký điện tử chuyên dùng bảo đảm an toàn hoặc chữ ký số mới tương đương chữ ký tay). CV 365 mục V (phần mềm cho phép ký, xác nhận; cơ sở ban hành quy định quản lý chữ ký).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 21/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: ít nhất một phương thức ký hợp lệ cho mỗi vai trò; mỗi lần ký lưu người ký, vai trò, phương thức, phiên bản tài liệu được ký, thời điểm, bằng chứng (chứng thư, log OTP, mẫu sinh trắc đã băm…); có các phiếu cần chữ ký người bệnh (cam kết, đồng ý phẫu thuật/thủ thuật, từ chối điều trị, ra viện trái chỉ định); hiển thị trạng thái đã ký/chưa ký từng phiếu.
- **Bẫy**: ảnh chữ ký dán vào PDF không phải chữ ký số, không gắn duy nhất với nội dung. Với giấy tờ luật đòi "bằng văn bản" có chữ ký người bệnh (đồng ý phẫu thuật; thiếu thì bị phạt NĐ 90 Đ40 k5 a), OTP có giá trị chứng cứ thấp hơn chữ ký số vì Đ23 k2 không coi là tương đương chữ ký tay (suy luận). Sinh trắc và CA cho người bệnh: xem BAOMAT-CB-R23–R26.

### EMR-R07 — Phần mềm ký số và kiểm tra chữ ký theo NĐ 23/2025
- **Căn cứ**: NĐ 23/2025 Đ15 (người ký kiểm tra trạng thái chứng thư của mình và của tổ chức phát hành trước khi ký), Đ16 (người nhận kiểm tra trạng thái chứng thư tại thời điểm ký), Đ17 k2–3 (chức năng bắt buộc của phần mềm ký và phần mềm kiểm tra: xác thực chủ thể, kiểm tra hiệu lực chứng thư và kết nối Cổng kết nối dịch vụ chứng thực chữ ký số công cộng, lưu và hủy thông tin kèm thông điệp ký, thêm/bớt chứng thư CA, thông báo kết quả), Đ47 k6–7 (phần mềm có tích hợp ký số phải rà soát, nâng cấp trong 02 năm kể từ ngày NĐ có hiệu lực; chủ quản HTTT chịu trách nhiệm).
- **Áp dụng**: vendor, chủ quản EMR có dùng chữ ký số · **Hiệu lực/hạn**: **10/04/2027** (10/04/2025 + 02 năm, suy luận cách tính)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kiểm OCSP/CRL ở cả hai tầng (chứng thư thuê bao và CA) trước khi ký và khi xác minh; lưu kết quả kiểm tra kèm chữ ký (dạng LTV); báo kết quả rõ ràng; quản lý danh sách CA tin cậy.
- **Bẫy**: ký số từ xa được thừa nhận (NĐ 23 Đ37 k4). Yêu cầu kỹ thuật chi tiết do Bộ trưởng (BTTTT, nay BKHCN) quy định (Đ17 k4): văn bản hiện hành chưa xác minh.

### EMR-R08 — Ký số của tổ chức; căn cứ sau 15/11/2026
- **Căn cứ**: Luật GDĐT Đ23 k3 (văn bản cần tổ chức xác nhận phải có chữ ký số hoặc chữ ký chuyên dùng bảo đảm an toàn của tổ chức đó); NĐ 23 Đ13 (chứng thư cho người có thẩm quyền ghi chức danh), Đ14 (ký thay, thừa lệnh theo chức danh), Đ9; TT 59/2026/TT-BKHCN Đ1 k3 (bãi bỏ TT 41/2017/TT-BTTTT từ 15/11/2026); TT 06/2026/TT-BYT Đ5 k2 (phiếu hẹn, phiếu chuyển bản điện tử dùng ký số của cơ sở thay đóng dấu từ 01/06/2026; xem BHYT-GD-R11, R12).
- **Áp dụng**: BV công (đang dẫn TT 41/2017); mọi cơ sở cấp giấy tờ ra ngoài · **Hiệu lực/hạn**: 15/11/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hỗ trợ chứng thư tổ chức (HSM hoặc ký số từ xa) cho giấy ra viện, chuyển tuyến, tóm tắt HSBA, phiếu hẹn; chữ ký cá nhân kèm chức danh khi ký thay/thừa lệnh; cấu hình thẩm quyền ký theo chức danh.
- **Bẫy**: sau 15/11/2026 quy chế ký số BV công không được dẫn TT 41/2017 mà dẫn Luật GDĐT 2023 + NĐ 23/2025. Nhiều quy chế mẫu còn dẫn NĐ 130/2018 (hết HL 10/04/2025, NĐ 23 Đ46 k2).

### EMR-R09 — Xác nhận của người bệnh bằng sinh trắc hoặc OTP
- **Căn cứ**: TT 13 Đ3 k2, k3; Luật GDĐT Đ22 k4 (hình thức xác nhận khác theo pháp luật liên quan; TT 13 là "quy định khác" cho HSBA, suy luận), Đ11 k2 (giá trị chứng cứ dựa trên độ tin cậy của cách khởi tạo, lưu, bảo toàn, xác định người khởi tạo).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 21/07/2025
- **Mức**: BẮT BUỘC? (được phép là chắc chắn; mức bằng chứng tối thiểu không có văn bản)
- **Phần mềm phải**: lưu gói bằng chứng: hash nội dung, kênh OTP (số điện thoại đã xác minh), mã giao dịch, thời điểm, thiết bị/IP, mẫu hoặc kết quả so khớp sinh trắc, danh tính và quan hệ người đại diện (Luật KCB Đ8); khóa nội dung sau xác nhận.
- **Bẫy**: dữ liệu sinh trắc là dữ liệu cá nhân nhạy cảm (DLCN; BAOMAT-CB-R25).

### EMR-R10 — Toàn vẹn, hiệu chỉnh có vết
- **Căn cứ**: Luật KCB **Đ7 k10** cấm "Tẩy xóa, sửa chữa hồ sơ bệnh án nhằm làm sai lệch thông tin… lập hồ sơ bệnh án giả" (gốc VBHN); NĐ 90 Đ38 k5 e. Luật GDĐT Đ10 k1 (toàn vẹn từ khi khởi tạo), Đ22 k3 d (thay đổi sau khi ký số đều phát hiện được). CV 365 PL III.1.1 c (phân quyền xem, nhập mới, chỉnh sửa, hủy, khôi phục). TT 32 Đ52 k2 d.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không sửa đè hay xóa vật lý nội dung lâm sàng; mỗi sửa đổi tạo phiên bản mới, giữ bản cũ, lưu lý do, người sửa, thời điểm; nội dung đã ký số thì không sửa, phải tạo bản bổ sung/đính chính rồi ký lại; "hủy" là đánh dấu có lý do, vẫn xem được; "khôi phục" có phân quyền và ghi vết.
- **Bẫy**: không văn bản nào dùng chữ "khóa hồ sơ". Ranh giới pháp lý duy nhất là Luật KCB Đ69 k3 (đang điều trị) và k4 (đã hoàn thành, chuyển lưu trữ); khóa sau khi chuyển lưu trữ là cách hiện thực (suy luận; P01). Thời hạn hoàn thiện HSBA sau ra viện: không thấy trong văn bản đã đọc.

### EMR-R11 — Phân quyền, xác thực, bảo mật truy cập
- **Căn cứ**: Luật KCB Đ10 k2 (giữ bí mật thông tin trong HSBA); NĐ 90 Đ38 k3 c; CV 365 PL III.1.1 g (xác thực, cấp quyền theo vai trò công việc, giới hạn khoảng thời gian truy cập, ngăn truy cập trái phép).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC (bảo mật HSBA) · BẮT BUỘC? (RBAC chi tiết và khung giờ — nguồn là công văn)
- **Phần mềm phải**: RBAC theo vai trò (bác sĩ, điều dưỡng, KTV, học viên, KHTH, lưu trữ, BHXH…); phạm vi theo khoa và quan hệ điều trị; khung giờ truy cập theo tài khoản/vai trò; khóa phiên, khóa tài khoản khi sai nhiều lần; không tài khoản chung.
- **Bẫy**: cấp độ HTTT và MFA xem ANM; phá kính xem BAOMAT-CB-R20; mượn tài khoản HIS bị phạt (BHYT-GD-R17).

### EMR-R12 — Nhật ký ghi vết mọi giao dịch
- **Căn cứ**: CV 365 PL III.1.1 đ (giám sát hành động người dùng, ghi vết tất cả giao dịch, tương tác), III.1.2 b (quản lý nhật ký người dùng); Luật GDĐT Đ13 k1 c.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: log cả **xem**, không chỉ ghi/sửa; mỗi bản ghi có người, vai trò, hành động, đối tượng (mã người bệnh, HSBA, phiếu, phiên bản), thời điểm server, nguồn IP/thiết bị, kết quả; append-only, chống giả mạo, tách quyền quản trị log; tra được "ai đã xem HSBA của người bệnh X".
- **Bẫy**: TT 33 không có dòng thời hạn cho nhật ký. Thời hạn hợp nhất: nhật ký truy cập HSBA lưu bằng thời hạn HSBA liên quan, tối thiểu 05 năm (NÊN, suy luận — chủ là BAOMAT-CB-R22); nhật ký an ninh hệ thống theo ANM-R11.

### EMR-R13 — In theo mẫu; bản giấy chuyển đổi từ HSBA điện tử
- **Căn cứ**: CV 365 PL III.1.1 a (xem tối thiểu dạng .pdf), e (hiển thị và in theo mẫu BYT); Luật GDĐT Đ12 k2 (bản giấy chuyển đổi phải toàn vẹn, có thông tin hệ thống và chủ quản để tra cứu, ký hiệu riêng xác nhận đã chuyển đổi, thông tin người chuyển đổi); NĐ 137 Đ5 k1–3 (tên hệ thống, chủ quản, mã hoặc đường dẫn tra cứu, ký hiệu riêng bằng chữ, thời gian, người chuyển đổi; có thể thêm QR).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC (Luật GDĐT Đ12) · BẮT BUỘC? (chi tiết NĐ 137 với cơ sở tư)
- **Phần mềm phải**: xuất PDF đúng mẫu; mọi bản in có footer "Bản giấy chuyển đổi từ HSBA điện tử", tên hệ thống, cơ sở chủ quản, mã tra cứu/QR, thời điểm, người in; log mỗi lần in.

### EMR-R14 — Quyền người bệnh: đọc, sao chụp, nhận tóm tắt
- **Căn cứ**: Luật KCB Đ12 k1; Đ69 k4 d (người bệnh, người đại diện theo Đ8 k2 c, d được đọc, xem, sao chụp, ghi chép và nhận bản tóm tắt khi có yêu cầu bằng văn bản); Đ69 k4 đ (người đại diện theo Đ8 k2 a, d chỉ nhận bản tóm tắt khi có yêu cầu bằng văn bản). TT 25/2025 Đ8 (tóm tắt theo Mẫu 03, giấy đề nghị Mẫu 04, trả giấy hẹn; xem GIAYTO-R15).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2024; mẫu từ 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tiếp nhận yêu cầu bằng văn bản (giấy/điện tử), xác minh người yêu cầu, loại đại diện theo Đ8 k2, phạm vi (toàn bộ hay chỉ tóm tắt); xuất bản sao/PDF có ký hiệu chuyển đổi (R13) và tóm tắt Mẫu 03 có ký số cơ sở; ghi vết việc cung cấp.
- **Bẫy**: "điểm d khoản 2 Điều 8" xuất hiện ở cả k4 d và k4 đ theo VBHN — trích đúng nguyên văn, cần luật sư đọc lại. Quyền chủ thể dữ liệu theo Luật BVDLCN chồng lên quyền này: xem DLCN.

### EMR-R15 — Khai thác HSBA của bên thứ ba theo trạng thái hồ sơ
- **Căn cứ**: Luật KCB Đ69 k3 (đang điều trị: a người học, người hành nghề, người trực tiếp điều trị được đọc, chỉ sao chép khi cơ sở đồng ý; b người hành nghề cơ sở khác đọc, sao chép khi cơ sở đồng ý); Đ69 k4 a–c (đã lưu trữ: cơ quan quản lý, điều tra, viện kiểm sát, tòa án, thanh tra, giám định pháp y, luật sư; người học và người hành nghề mượn tại chỗ khi cơ sở đồng ý; BHXH, cơ quan bồi thường nhà nước mượn tại chỗ, ghi chép, đề nghị bản sao khi cơ sở đồng ý); Đ69 k5 (đúng mục đích).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chính sách truy cập phụ thuộc trạng thái HSBA và loại người truy cập; quyền sao chép (xuất, tải, in) tách khỏi quyền đọc và cần phê duyệt; cấp quyền tạm cho người ngoài (thanh tra, giám định BHXH) có mục đích, tự hết hạn, có log.

### EMR-R16 — Số hóa bệnh án giấy cũ
- **Căn cứ**: TT 13 Đ5 k2 (HSBA giấy lập trước 21/07/2025: Thủ trưởng quyết định chuyển đổi theo NĐ 137/2024); Luật GDĐT Đ12 k1; NĐ 137 Đ4 k1 a, k2 (ký hiệu riêng, thời gian, người chuyển đổi; hệ thống chuyển đổi toàn vẹn, lưu trữ, ATTT, ký số nếu cần), Đ23 (hệ thống chuyển đổi phải rà soát đáp ứng Đ4 k2, Đ5 k3 trong 24 tháng từ ngày NĐ có hiệu lực); Luật Lưu trữ Đ34 (bản số hóa có giá trị khi toàn vẹn, có dấu hiệu nhận biết đã số hóa, được xác thực).
- **Áp dụng**: cơ sở chọn số hóa; chủ quản hệ thống chuyển đổi · **Hiệu lực/hạn**: **~23/10/2026** (23/10/2024 + 24 tháng, suy luận cách tính)
- **Mức**: BẮT BUỘC (khi cơ sở chọn số hóa)
- **Phần mềm phải**: module scan gắn ký hiệu "Bản điện tử chuyển đổi từ văn bản giấy", thời điểm, đơn vị và người chuyển đổi, ký số của cơ sở; lưu metadata, liên kết người bệnh và đợt điều trị; ghi nhận giữ hay hủy bản giấy theo quyết định Thủ trưởng.

### EMR-R17 — Chuyển tiếp người bệnh đang dùng bệnh án giấy
- **Căn cứ**: TT 13 Đ5 k1 (vào viện trước 21/07/2025, ra viện hoặc kết thúc đợt ngoại trú sau ngày đó thì tiếp tục dùng HSBA giấy đến khi kết thúc, trừ khi chuyển được sang điện tử).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 21/07/2025 (gần hết tác dụng thực tế)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trường hình thức HSBA `paper | electronic | hybrid` để báo cáo và lưu trữ không sót.

### EMR-R18 — Kết xuất XML/JSON theo phụ lục CV 365
- **Căn cứ**: CV 365 PL III.1.1 d (kết xuất XML hoặc JSON theo Phụ lục "Mô tả dữ liệu trao đổi HSBA điện tử"), mục IV (khi có yêu cầu). Phụ lục: phần tử gốc `HoSoBenhAn`, 11 nhóm: `ThongTinBenhNhan`, `ThongTinVaoVien`, `ThongTinDieuTri`, `YLenhThuocVatTu`, `PhieuChiDinh`, `KetQuaChanDoanHinhAnh`, `KetQuaXetNghiem`, `GiayChuyenVien`, `HoSoCapCuu`, `PhieuThuThuat`, `PhieuPhauThuat`; mỗi chỉ tiêu có kiểu và độ dài tối đa (ví dụ `cccd_so` Số, 15); có ví dụ JSON, XML.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: xuất từng HSBA thành JSON và XML đúng tên trường, kiểu, độ dài; kiểm hợp lệ trước khi gửi; có API hoặc nút xuất theo yêu cầu.
- **Bẫy**: schema không có trường chữ ký số, chỉ `chuky_hoten`; muốn chuyển kèm bằng chứng ký phải gửi thêm PDF đã ký (suy luận). Trường địa chỉ còn cấp huyện (`quanhuyen_ma`), lệch mô hình 2 cấp hành chính từ 07/2025 (xem MA-LT). Chuẩn dữ liệu XML BHYT là bộ khác: xem BHYT-DATA.

### EMR-R19 — Dùng danh mục dùng chung BYT
- **Căn cứ**: CV 365 PL III.1.1 h.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: ICD, DVKT, thuốc và vật tư (`mathuocvattu_byt`), nghề nghiệp, dân tộc… theo danh mục BYT; map mã nội bộ sang mã BYT. Chi tiết: MA-LT, BHYT-DATA-R13.

### EMR-R20 — Kiến trúc; dữ liệu HSBA lưu độc lập
- **Căn cứ**: CV 365 PL III.1.1 b (tạo lập bằng đồng bộ từ hệ thống khác hoặc nhập trực tiếp), i (phân hệ HIS hoặc EMR độc lập), k (dữ liệu HSBA "được lưu trữ độc lập không phụ thuộc vào các hệ thống khác").
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: kho HSBA (tài liệu đã ký + dữ liệu cấu trúc) vẫn đọc và xuất được khi HIS, LIS, PACS ngừng hoặc bị thay; không chỉ lưu link sang hệ thống khác.

### EMR-R21 — Sao lưu, phục hồi, mã hóa
- **Căn cứ**: TT 13 Đ2 k1 (hạ tầng tối thiểu có giải pháp lưu trữ, gồm lưu trữ dự phòng), Đ2 k4 (sẵn sàng phục hồi và truy xuất để đối chiếu, thanh tra, nghiên cứu); CV 365 PL III.1.2 a (chống truy cập trái phép CSDL, cơ chế sao lưu và khôi phục, toàn vẹn, khả năng mã hóa dữ liệu lưu), b (mã hóa khi truyền); CV 365 III.2 c (01 bản sao lưu tại cơ sở; khuyến nghị thêm 01 bản tại đơn vị cung cấp dịch vụ lưu trữ).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 21/07/2025
- **Mức**: BẮT BUỘC (TT 13 Đ2) · NÊN (bản sao lưu thứ hai ở nơi khác)
- **Phần mềm phải**: lịch sao lưu tự động, kiểm toàn vẹn bản sao lưu, quy trình khôi phục đã diễn tập; mã hóa at-rest và TLS; báo cáo sao lưu.
- **Bẫy**: vi phạm Đ2 bị phạt theo NĐ 90 Đ39 k2 d. Yêu cầu sao lưu theo luật ANM: xem ANM.

### EMR-R22 — Thời hạn lưu trữ HSBA
- **Căn cứ**: TT 33/2025 Phụ lục, Nhóm 01 "Tài liệu về khám bệnh, chữa bệnh" (gốc):

  | Mục | Loại hồ sơ | Thời hạn |
  |---|---|---|
  | 38 | Hồ sơ giải quyết sự cố y khoa | Vĩnh viễn |
  | 39 | HSBA tử vong | 30 năm |
  | 40 | HSBA tâm thần, tai nạn lao động, tai nạn giao thông | 20 năm |
  | 43 | HSBA điều trị đợt ghép mô, tạng, phẫu thuật thẩm mỹ | 20 năm (TT 33) — **riêng hồ sơ người hiến và người được ghép: 30 năm** theo Luật 75/2006 Đ38 k4, áp 30 năm (xem BAOMAT-CB-R15) |
  | 44 | HSBA nội trú, ngoại trú | 10 năm |
  | 47 | Sổ, sách phục vụ công tác KCB | 05 năm |
  | 48 | Giấy khám sức khỏe | 02 năm |
  | 49 | Sổ sức khỏe điện tử | 10 năm sau khi người dân qua đời |

  TT 33 Đ1 k2 a (áp cả tài liệu điện tử), k2 b (hồ sơ chưa quy định thì áp nhóm tương đương, không thấp hơn), Đ2 k3 (thời hạn xác định trước 01/07/2025 giữ nguyên). Luật Lưu trữ Đ15 k3 (tính từ năm kết thúc công việc), k4 (hồ sơ gồm tài liệu khác thời hạn thì lấy thời hạn dài nhất). Luật KCB Đ69 k2; NĐ 90 Đ40 k1 b.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: gán loại lưu trữ cho mỗi HSBA; tự nâng loại khi có sự kiện (tử vong → 30 năm; ghép tạng → 30 năm); `retention_until` = 31/12 năm kết thúc đợt điều trị + N năm (suy luận cách áp); không cho hủy trước hạn.
- **Bẫy**: mâu thuẫn TT 33 (20 năm) với Luật 75/2006 (30 năm) cho hồ sơ ghép tạng: luật cao hơn thông tư. Phụ lục TT 33 không có dòng cho đơn thuốc ngoại trú độc lập, phim/ảnh DICOM, kết quả xét nghiệm rời, audit log → tự xếp nhóm tương đương; thận trọng: tài liệu thuộc HSBA lưu theo HSBA (suy luận).

### EMR-R23 — Lưu thông điệp dữ liệu kèm metadata
- **Căn cứ**: Luật GDĐT Đ13 k1 (truy cập được; lưu ở khuôn dạng khởi tạo hoặc thể hiện chính xác; xác định được nguồn gốc, người gửi, người nhận, thời gian), k3 (giá trị như lưu văn bản giấy); Luật Lưu trữ Đ33 k2 (xác thực, toàn vẹn, lưu đồng thời với dữ liệu chủ), Đ36 k2 b, c (xác thực lâu dài, chuyển đổi theo công nghệ).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC (Luật GDĐT; phần Luật Lưu trữ với BV công) · BẮT BUỘC? (phần Luật Lưu trữ với BV, PK tư — Đ3 k5)
- **Phần mềm phải**: lưu bản "đóng băng" định dạng ổn định (khuyến nghị PDF/A kèm dữ liệu cấu trúc); metadata mỗi tài liệu: loại, mã HSBA, người lập, người ký, thời điểm, hash, định dạng, thời hạn lưu; kế hoạch chuyển đổi định dạng và gia hạn chữ ký (re-timestamp) cho thời hạn 10–30 năm.

### EMR-R24 — Hủy HSBA hết hạn
- **Căn cứ**: Luật Lưu trữ Đ16 k1–3 (hủy tài liệu hết hạn; hủy toàn bộ, không khôi phục được; người đứng đầu quyết định), Đ36 k4 (chỉ hủy khi không còn liên kết với tài liệu có thời hạn dài hơn; hủy đồng thời dữ liệu chủ và bản giấy đã số hóa); NĐ 113 Đ20 (tham chiếu: thông báo đến hạn, đánh giá lại, xác nhận lệnh hủy, danh mục, lịch sử hủy).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC (khu vực công) · BẮT BUỘC? (tư) · NÊN (quy trình theo NĐ 113 Đ20)
- **Phần mềm phải**: hủy theo lô: danh mục dự kiến → phê duyệt người đứng đầu → hủy bản chính, bản sao lưu, metadata, bản scan → biên bản và danh mục đã hủy; giữ log của việc hủy; chặn hủy hồ sơ đang bị giữ (khiếu nại, tố tụng, sự cố y khoa).

### EMR-R25 — Quy chế HSBA điện tử của cơ sở
- **Căn cứ**: TT 13 Đ6 k3 b (cơ sở ban hành quy chế lập, cập nhật, quản lý, lưu trữ, sử dụng, ATTT với HSBA điện tử, gồm nội dung Đ3); NĐ 90 Đ39 k2 c; CV 365 mục V k2.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 21/07/2025
- **Mức**: BẮT BUỘC (cơ sở ban hành) · NÊN (phần mềm hỗ trợ, vendor cung cấp mẫu quy chế)
- **Phần mềm phải**: cấu hình được theo quy chế: ai ký phiếu nào, thẩm quyền, thời hạn hoàn thiện HSBA nội bộ, danh mục viết tắt, quy trình sửa và khôi phục.

### EMR-R26 — Hạ tầng tại VN; sở hữu và bàn giao dữ liệu
- **Căn cứ**: CV 365 III.2 a (hạ tầng của cơ sở hoặc cloud đặt tại Việt Nam), III.2 đ (DC theo quy định BKHCN, khuyến nghị Tier 3, ISO 27001; dữ liệu hình thành khi thuê thuộc sở hữu cơ sở; hết hợp đồng thì bàn giao toàn bộ dữ liệu kèm đặc tả chi tiết, hỗ trợ chuyển, hủy an toàn trên thiết bị nhà cung cấp; có cam kết bảo mật), III.4 c (thuê phần mềm phải cam kết bàn giao toàn bộ CSDL).
- **Áp dụng**: cơ sở thuê, vendor SaaS · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: xuất toàn bộ dữ liệu (dump + đặc tả schema + tài liệu đã ký + log); quy trình xóa an toàn có biên bản; cấu hình vùng dữ liệu chỉ ở VN, kể cả bản sao lưu.
- **Bẫy**: lưu trữ dữ liệu trong nước theo luật ANM: xem ANM. SaaS EMR có bị coi là "kinh doanh dịch vụ lưu trữ" (Luật Lưu trữ Đ53, NĐ 113 Đ37) không: chưa xác minh.

### EMR-R27 — ATTT, IPv6, chuẩn kỹ thuật theo CV 365
- **Căn cứ**: CV 365 III.1.2 b (ATTT trước khi đưa vào dùng theo QĐ 742/QĐ-BTTTT; vá phần mềm nền), III.1.3 c (TT 39/2017/TT-BTTTT), III.4 a, b (tối thiểu cấp độ 2 theo NĐ 85/2016 và TT 12/2022), III.5 (IPv6), III.6 (BVDLCN theo NĐ 13/2023).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC? (văn bản dẫn chiếu đã hoặc đang bị thay)
- **Phần mềm phải**: báo cáo kiểm thử ATTT trước go-live; chạy được trên IPv6; chuẩn trao đổi XML, JSON, UTF-8.
- **Bẫy**: NĐ 85/2016 và TT 12/2022 **hết HL từ 01/07/2026** cùng luật gốc (Luật 87/2025 sửa Đ57 k2 Luật 64); cấp độ HTTT nay theo NĐ 331/2026, NĐ 85 chỉ còn dùng cho thẩm định chuyển tiếp mà NĐ 331 Đ39 k1 cho phép (xem ANM). HIS/EMR nội bộ thường cấp 2; cấp 3 gắn với dịch vụ trực tuyến ≥10.000 người dùng (suy luận, ANM-R02). NĐ 13/2023 → Luật 91/2025 + NĐ 356/2025 (xem DLCN).

### EMR-R28 — Đơn thuốc trong HSBA
- **Căn cứ**: TT 26/2025 Đ5 k1 b (có HSBA ngoại trú thì chỉ định vào HSBA), Đ9 k1 (đơn "H" 3 bản, 1 bản lưu HSBA), Đ10 (đơn điện tử lập, ký số, lưu điện tử có giá trị như đơn giấy), Đ13 k3 (BV trước 01/10/2025; cơ sở khác trước 01/01/2026).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/10/2025; 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: đơn thuốc trong EMR là tài liệu đã ký số, liên kết y lệnh, lưu cùng thời hạn HSBA. Chi tiết kê đơn: DUOC.

**Tổng**: 28 yêu cầu. BẮT BUỘC 19 (R01, R03–R08, R10, R13–R17, R21–R25, R28) + phần bảo mật R11; BẮT BUỘC? 9 (R02, R09, R11 phần chi tiết, R12, R18, R19, R20, R26, R27); NÊN ở phần con R21, R24, R25.

## 3. Pattern thiết kế

### EMR-P01 — Máy trạng thái HSBA gắn chính sách truy cập
- **Giải quyết**: R10, R15, R17, R22, R24
- **Cách làm**: `DRAFT → ACTIVE` (đang điều trị, Đ69 k3) `→ CLOSED` (ra viện, chờ hoàn thiện, ký đủ) `→ ARCHIVED` (chuyển lưu trữ, Đ69 k4, bất biến, bắt đầu tính hạn) `→ DESTROYED` (chỉ còn metadata hủy).
- **Gợi ý dữ liệu**: `medical_record(id, patient_id, record_type, form_version, medium ENUM('electronic','paper','hybrid'), status, opened_at, closed_at, archived_at, retention_class_id, retention_until DATE, legal_hold BOOL)`; trigger chặn UPDATE nội dung khi `status IN ('ARCHIVED','DESTROYED')`; index `(patient_id, status)`, `(retention_until) WHERE status='ARCHIVED'`.
- **Đánh đổi**: kết quả về muộn (giải phẫu bệnh) sau lưu trữ phải đi luồng "phụ lục bổ sung" có ký, không mở lại hồ sơ.

### EMR-P02 — Ghi chép append-only kèm đính chính
- **Giải quyết**: R04, R10
- **Cách làm**: không DELETE; UPDATE chỉ đổi `status` sang `superseded`/`cancelled` kèm lý do; UI hiện bản mới nhất, có "lịch sử phiên bản".
- **Gợi ý dữ liệu**: `clinical_entry(id, record_id, entry_type, payload JSONB, author_id, author_role, recorded_at DEFAULT now(), clinical_time, supersedes_id, amend_reason, status ENUM('active','superseded','cancelled'))`.
- **Đánh đổi**: tốn dung lượng, query phức tạp; đổi lại chứng minh được không tẩy xóa.

### EMR-P03 — Phong bì chữ ký
- **Giải quyết**: R06, R07, R08, R09
- **Cách làm**: render tài liệu (PDF/A hoặc JSON chuẩn hóa) → SHA-256 → ký; nội dung đã ký bất biến, sửa thì `version+1` và ký lại.
- **Gợi ý dữ liệu**: `signed_document(id, record_id, doc_type, version, content_hash, storage_uri, created_at)`; `signature(id, signed_document_id, signer_type ENUM('staff','patient','representative','organization'), signer_ref, signer_title, method ENUM('pki_token','pki_remote','hsm_org','biometric','otp','other'), cert_serial, issuer, cert_status_at_sign JSONB, tsa_token, evidence_uri, signed_at)`; `UNIQUE(signed_document_id, signer_ref, role)`.
- **Đánh đổi**: ký từ xa tiện nhưng phụ thuộc mạng và CA; HSM nội bộ nhanh nhưng cơ sở tự quản lý khóa.

### EMR-P04 — Audit log chống giả mạo
- **Giải quyết**: R12, R10
- **Cách làm**: bảng hoặc DB riêng chỉ INSERT; chuỗi hash, neo định kỳ bằng ký số hoặc dấu thời gian; quyền quản trị log tách khỏi quản trị ứng dụng.
- **Gợi ý dữ liệu**: `audit_event(seq BIGSERIAL, ts, actor_id, actor_role, action ENUM('view','create','update','cancel','restore','print','export','sign','share','destroy'), object_type, object_id, patient_id, purpose, ip, device, result, prev_hash, hash, retain_until)`; index `(patient_id, ts)`; `retain_until = max(retention HSBA liên quan, created_at + 5 năm)` (BAOMAT-CB-R22).
- **Đánh đổi**: khối lượng lớn vì log `view`; phân vùng theo tháng, chuyển kho lạnh, vẫn truy vấn được.

### EMR-P05 — Truy cập theo vai trò, quan hệ điều trị, thời gian; cấp quyền tạm
- **Giải quyết**: R11, R15
- **Cách làm**: RBAC → ABAC (`care_team`, khoa, trạng thái HSBA) → khung giờ (`access_window`); phá kính có lý do và hậu kiểm (BAOMAT-CB-R20); quyền đọc tách quyền sao chép.
- **Gợi ý dữ liệu**: `access_grant(grantee, scope, purpose, approved_by, valid_from, valid_to, can_copy BOOL)`.
- **Đánh đổi**: cấu hình ABAC tốn công ban đầu; bù lại đáp ứng Đ69 k3 a (đọc ≠ sao chép).

### EMR-P06 — Quy trình yêu cầu của người bệnh
- **Giải quyết**: R14
- **Cách làm**: phạm vi do luật định: người bệnh, đại diện theo Đ8 k2 c, d → `full`; đại diện theo Đ8 k2 a, d → `summary`. Đầu ra: PDF có ký hiệu chuyển đổi (P07) + tóm tắt Mẫu 03 TT 25/2025 ký số cơ sở.
- **Gợi ý dữ liệu**: `patient_request(id, patient_id, requester_id, requester_relation, written_request_uri, scope ENUM('full','summary'), status, appointment_at, fulfilled_at, delivered_doc_id)`.
- **Đánh đổi**: luật lặp "điểm d" ở hai điểm, cần chốt cách áp với luật sư trước khi cứng hóa.

### EMR-P07 — Dấu chuyển đổi giấy ↔ điện tử
- **Giải quyết**: R13, R16
- **Cách làm**: dịch vụ sinh footer, watermark, QR; bản scan nhập vào gắn ký hiệu và chữ ký tổ chức.
- **Gợi ý dữ liệu**: `conversion_stamp(direction, system_name, owner_name, lookup_code, converted_by, converted_at)`; `scan_batch(id, source_record_id, page_count, operator, converted_at, org_signature_id)`.
- **Đánh đổi**: QR cần cổng xác minh công khai, phải chống dò mã (rate limit, mã ngẫu nhiên đủ dài).

### EMR-P08 — Động cơ thời hạn lưu trữ
- **Giải quyết**: R22, R24
- **Cách làm**: tính lại hạn khi có sự kiện (tử vong, ghép tạng, sự cố y khoa); cờ `legal_hold` chặn hủy; job hằng năm lập danh mục dự kiến hủy chờ duyệt; hủy cả backup (backup xóa chọn lọc hoặc crypto-shredding: mã hóa từng hồ sơ bằng khóa riêng rồi hủy khóa).
- **Gợi ý dữ liệu**: `retention_class(code, legal_basis, years, permanent BOOL)` — ví dụ `('GHEP_TANG', 'Luật 75/2006 Đ38 k4', 30, false)`, `('THUONG', 'TT 33/2025 PL mục 44', 10, false)`.
- **Đánh đổi**: crypto-shredding giải bài toán xóa trong backup nhưng tăng độ phức tạp quản lý khóa.

### EMR-P09 — Lớp xuất liên thông theo CV 365
- **Giải quyết**: R18, R05, R19
- **Cách làm**: mapper mô hình nội bộ → `HoSoBenhAn` (JSON/XML), validate bằng schema tự dựng từ bảng phụ lục; đính kèm PDF đã ký; bản đồ mã BYT có phiên bản.
- **Gợi ý dữ liệu**: `export_job(record_id, format, schema_version, payload_hash, attachments, created_at)`.
- **Đánh đổi**: schema tự dựng có thể lệch khi TTYQG cập nhật phụ lục; cần theo dõi.

### EMR-P10 — Sao lưu và kế hoạch rời nhà cung cấp
- **Giải quyết**: R21, R26
- **Cách làm**: 3-2-1: bản tại cơ sở (bắt buộc theo CV 365) + bản ở nơi khác (khuyến nghị) + bản offline/immutable; diễn tập khôi phục định kỳ có biên bản; hợp đồng SaaS có điều khoản bàn giao (dump, đặc tả schema, tài liệu đã ký, log) và biên bản hủy.
- **Gợi ý dữ liệu**: `backup_run(id, scope, started_at, finished_at, location, checksum, verified_at)`; `restore_drill(id, run_id, rto_measured, result, minutes_uri)`.
- **Đánh đổi**: chi phí lưu trữ tăng; cần đảm bảo mọi bản đều đặt tại VN.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| EMR-A01 | R01 | Xem QĐ triển khai/công bố HSBA điện tử và tên trên benhandientu.moh.gov.vn; so ngày go-live với 30/09/2025 (BV) hoặc 31/12/2026 | QĐ công bố, biên bản tự đánh giá TT 13 + CV 365, ảnh cổng | BẮT BUỘC |
| EMR-A02 | R02 | PK: liệt kê loại lượt khám; có mở HSBA ngoại trú điện tử (15/16/19/BV1, PHCN) không; lượt chỉ kê đơn có phiếu khám ký và đơn điện tử không | Danh sách loại bệnh án, mẫu in | BẮT BUỘC? |
| EMR-A03 | R03 | Chọn ngẫu nhiên 10 HSBA mỗi loại, so từng trường với PL XXVIII/XXIX TT 32; tìm mẫu cũ QĐ 4069; tóm tắt HSBA có theo Mẫu 03 TT 25/2025 không | Bảng so khớp, ảnh màn hình | BẮT BUỘC |
| EMR-A04 | R04 | `SELECT count(*) FROM clinical_entry WHERE author_id IS NULL OR recorded_at IS NULL`; tìm tài khoản dùng chung; in tóm tắt, chuyển tuyến để tìm viết tắt | Kết quả truy vấn, danh sách tài khoản, bản in | BẮT BUỘC |
| EMR-A05 | R05 | Tỷ lệ người bệnh có số định danh; số hồ sơ trùng; có quy trình gộp và log không | Truy vấn, log merge | BẮT BUỘC |
| EMR-A06 | R06, R09 | Mở phiếu đồng ý phẫu thuật: người bệnh ký bằng gì, có gói bằng chứng không; chữ ký NVYT là chữ ký số hay ảnh | PDF đã ký (kiểm bằng công cụ xác minh), bản ghi OTP | BẮT BUỘC |
| EMR-A07 | R07 | Ký thử bằng chứng thư thu hồi/hết hạn: có bị chặn không; có lưu kết quả OCSP/CRL không; kế hoạch nâng cấp trước 10/04/2027 | Video/ảnh thử, tài liệu nâng cấp | BẮT BUỘC |
| EMR-A08 | R08 | Quy chế ký số BV công còn dẫn TT 41/2017 hoặc NĐ 130/2018 không; giấy ra viện, chuyển tuyến có chữ ký tổ chức hoặc người có thẩm quyền kèm chức danh không | Quy chế, file đã ký | BẮT BUỘC |
| EMR-A09 | R10 | Sửa một mục đã lưu: bản cũ còn, có lý do; sửa nội dung đã ký có bị chặn; tài khoản DB ứng dụng có quyền DELETE/UPDATE trực tiếp bảng lâm sàng không | Ảnh lịch sử phiên bản, cấu hình quyền DB | BẮT BUỘC |
| EMR-A10 | R11 | Điều dưỡng khoa A xem được HSBA khoa B không; có khung giờ truy cập; có khóa tài khoản | Ma trận phân quyền, ảnh cấu hình | BẮT BUỘC? |
| EMR-A11 | R12 | Xem một HSBA rồi tra log: có bản ghi `view` không; admin có xóa/sửa được log không; log có `retain_until` ≥ 5 năm | Trích log, kết quả thử xóa | BẮT BUỘC? |
| EMR-A12 | R13 | In một phiếu: footer có ký hiệu chuyển đổi, tên hệ thống, chủ quản, mã tra cứu/QR, thời gian, người in; PDF đúng mẫu | Bản in, file PDF | BẮT BUỘC |
| EMR-A13 | R14 | Diễn tập yêu cầu: có yêu cầu bằng văn bản (Mẫu 04); đại diện theo Đ8 k2 a bị giới hạn chỉ nhận tóm tắt; có giấy hẹn | Hồ sơ yêu cầu, tóm tắt Mẫu 03 | BẮT BUỘC |
| EMR-A14 | R15 | Học viên xem được nhưng không xuất/in khi chưa duyệt; cấp quyền tạm cho thanh tra/BHXH có hạn và log | Ảnh thử, bảng `access_grant` | BẮT BUỘC |
| EMR-A15 | R16 | 5 bản scan bệnh án cũ: có ký hiệu, thời gian, người chuyển đổi, chữ ký số cơ sở; có QĐ Thủ trưởng; đã rà soát theo NĐ 137 Đ23 chưa | File scan, QĐ, biên bản rà soát | BẮT BUỘC |
| EMR-A16 | R17 | Có trường hình thức HSBA (giấy/điện tử/lai); báo cáo HSBA giấy tồn | Truy vấn | BẮT BUỘC |
| EMR-A17 | R18 | Xuất 1 HSBA ra JSON và XML, validate theo 11 nhóm phụ lục CV 365 | File xuất, kết quả validate | BẮT BUỘC? |
| EMR-A18 | R19 | Lấy mẫu mã ICD, DVKT, thuốc: có theo danh mục BYT | Bảng mapping | BẮT BUỘC? |
| EMR-A19 | R20 | Ngắt HIS/PACS: kho EMR còn xem, xuất được HSBA đã ký không | Kết quả thử | BẮT BUỘC? |
| EMR-A20 | R21 | Lịch và báo cáo sao lưu 3 tháng; biên bản diễn tập khôi phục; cấu hình mã hóa at-rest và TLS | Báo cáo, biên bản | BẮT BUỘC |
| EMR-A21 | R22 | Phân bố `retention_class`; tử vong 30 năm; tâm thần/TNLĐ/TNGT 20 năm; hồ sơ ghép tạng 30 năm; cách tính `retention_until`; đơn thuốc, ảnh CĐHA, log gán hạn nào | Truy vấn, chính sách lưu trữ | BẮT BUỘC |
| EMR-A22 | R23 | 1 tài liệu đã lưu trữ có metadata đủ; hash khớp; định dạng ổn định (PDF/A) | Bản ghi metadata, kết quả kiểm hash | BẮT BUỘC |
| EMR-A23 | R24 | Thử hủy hồ sơ chưa hết hạn hoặc đang `legal_hold`: bị chặn; hủy có xóa backup và bản scan; có biên bản, danh mục | Quy trình, biên bản | BẮT BUỘC |
| EMR-A24 | R25 | Có quy chế HSBA điện tử gồm phần ký và xác nhận (TT 13 Đ3); cấu hình phần mềm khớp quy chế | Quy chế, đối chiếu cấu hình | BẮT BUỘC |
| EMR-A25 | R26 | Hợp đồng SaaS: dữ liệu thuộc cơ sở; điều khoản bàn giao kèm đặc tả và hủy an toàn; DC và backup tại VN; NDA | Hợp đồng, chứng chỉ DC | BẮT BUỘC? |
| EMR-A26 | R27 | Báo cáo kiểm thử ATTT trước go-live; hồ sơ cấp độ HTTT (xem ANM); chạy IPv6 | Báo cáo, hồ sơ | BẮT BUỘC? |
| EMR-A27 | R28 | Đơn thuốc trong HSBA có ký số, liên kết y lệnh; đơn "H" có bản lưu HSBA | File đơn đã ký | BẮT BUỘC |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới |
|---|---|---|---|
| 01/01/2024 | Luật KCB 2023, TT 32/2023 có HL; mẫu HSBA mới thay QĐ 4069/2001 | Mọi cơ sở, vendor | Đã qua |
| 10/04/2025 | NĐ 23/2025 có HL; NĐ 130/2018 hết HL | Người ký số, vendor | Đã qua |
| 06/06/2025 | TT 13 ban hành; **TT 46/2018** và Mục VIII PL I TT 54/2017 (tiêu chí EMR) hết HL ngay ngày ban hành (TT 13 Đ4 k3); CV 365 ban hành | — | Đã qua |
| 01/07/2025 | TT 33/2025, Luật Lưu trữ 2024, TT 26/2025, TT 25/2025 (mẫu tóm tắt, báo tử mới) có HL | Mọi cơ sở | Đã qua |
| 21/07/2025 | TT 13 có HL (mốc chuyển tiếp HSBA giấy Đ5); NĐ 113/2025 có HL | Mọi cơ sở | Đã qua |
| 30/09/2025 | **Hạn BV hoàn thành HSBA điện tử** (TT 13 Đ4 k2 a) | BV công, tư | Đã qua |
| 01/01/2026 | Hạn chót (chậm nhất trước ngày này) để cơ sở không phải BV kê đơn điện tử (TT 26 Đ13 k3 b) | PK, TTYT | Đã qua |
| 15/05/2026 | NĐ 90/2026 có HL (Đ39 k2 c, d) | Mọi cơ sở | Đã qua |
| 01/07/2026 | NĐ 85/2016, TT 12/2022 hết HL (CV 365 còn dẫn) | Chủ quản HTTT | Đã qua |
| 15/08/2026 | TT 25/2026 có HL (không sửa Chương X TT 32) | — | Đã qua |
| ~23/10/2026 | Hết 24 tháng rà soát hệ thống chuyển đổi giấy ↔ điện tử (NĐ 137 Đ23; cách tính suy luận) | Chủ quản hệ thống số hóa/in chuyển đổi | Sắp tới |
| 15/11/2026 | TT 41/2017/TT-BTTTT bị bãi bỏ (TT 59/2026) | BV công: sửa quy chế ký số | Sắp tới |
| 31/12/2026 | **Hạn cơ sở KCB khác có điều trị hoàn thành HSBA điện tử** (TT 13 Đ4 k2 b) | PK, TTYT, cơ sở tư; vendor CIS | Sắp tới |
| 01/01/2027 | BV không dùng HSBA giấy — **chỉ là mục tiêu kế hoạch** QĐ 586, CT 04 (thứ cấp), không có trong TT 13, không có chế tài riêng. Cùng ngày: Luật KCB Đ120 k5 a (hạ tầng CNTT là điều kiện cấp GPHĐ mới) | BV; cơ sở xin GPHĐ mới | Sắp tới |
| 01/03/2027 | Luật 20/2026/QH16 sửa Luật GDĐT có HL; không đổi Đ22–23 (BAOMAT-CB-R26) | Tất cả | Sắp tới |
| 10/04/2027 | Hạn nâng cấp phần mềm ký số theo NĐ 23 Đ17 (Đ47 k6; cách tính suy luận) | Vendor, chủ quản EMR | Sắp tới |
| 01/01/2029 | Cơ sở có GPHĐ trước 2027 phải đáp ứng hạ tầng CNTT (Luật KCB Đ120 k5 b) | Mọi cơ sở | Xa |
| 2030 | 100% cơ sở không dùng bệnh án giấy (QĐ 965, kế hoạch; thứ cấp) | Mọi cơ sở | Xa |

QĐ 586 (kế hoạch năm 2026) và QĐ 965 (kế hoạch 2026–2030) là quyết định phê duyệt kế hoạch, không phải VBQPPL, không tự tạo chế tài với cơ sở tư; không thấy nguồn nói QĐ 965 thay QĐ 586 (suy luận: song song). Nghĩa vụ có chế tài là TT 13 Đ4 k2 + NĐ 90 Đ39 k2 c, d.

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**
- TT 46/2018/TT-BYT → TT 13/2025: hết HL **06/06/2025** (ngày ban hành TT 13), không phải 21/07/2025.
- TT 54/2017 Mục VIII PL I và tiêu chí EMR → bãi bỏ 06/06/2025; phần còn lại vẫn HL, chưa có thông tư thay.
- Thủ tục công nhận HSBA điện tử theo TT 46 → không có thủ tục thay; thực tiễn tự thẩm định, QĐ công bố.
- TT 53/2017 (thời hạn bảo quản) → TT 33/2025 (01/07/2025).
- QĐ 4069/2001, QĐ 1941/2019, QĐ 3730/2021 → TT 32/2023 PL XXVIII–XXIX.
- Tóm tắt HSBA: PL 4 TT 18/2022 → CV-01/Mẫu 52/BV2 TT 32/2023 → **Mẫu 03 (+ đề nghị Mẫu 04) PL II TT 25/2025** (01/07/2025).
- Giấy báo tử: mẫu PL I TT 24/2020 → **Mẫu 05 PL II TT 25/2025** (01/07/2025); phần phiếu chẩn đoán nguyên nhân tử vong của TT 24/2020 còn HL (xem GIAYTO).
- NĐ 130/2018, NĐ 48/2024 → NĐ 23/2025 (10/04/2025).
- TT 41/2017/TT-BTTTT → bãi bỏ 15/11/2026 (TT 59/2026), không có thông tư thay; dùng Luật GDĐT 2023 + NĐ 23/2025.
- NĐ 117/2020 → NĐ 90/2026 (15/05/2026).
- Luật Lưu trữ 2011 → Luật Lưu trữ 2024 (01/07/2025).
- NĐ 13/2023 → Luật 91/2025 + NĐ 356/2025 (DLCN).
- NĐ 85/2016, TT 12/2022 → hết HL từ 01/07/2026 cùng luật gốc (Luật 64/2025 Đ57 k2 sửa bởi Luật 87/2025). Không viết "NĐ 331 thay NĐ 85": NĐ 331/2026 không có điều bãi bỏ, nó là khung cấp độ mới (ANM-R05, C07).

**Bẫy trích dẫn**
1. TT 13 rất ngắn; yêu cầu chức năng nằm ở CV 365 (công văn hướng dẫn). Ghi "CV 365 PL mục III.x", đừng gán cho TT 13.
2. Điều cấm tẩy xóa HSBA là **Luật KCB Đ7 k10**, không phải Đ6 k10.
3. TT 26/2025 Đ11 dẫn TT 53/2017 (đã hết HL) cho việc lưu đơn; áp TT 33 theo TT 26 Đ14; TT 33 không có dòng "đơn thuốc" nên áp nhóm tương đương.
4. TT 33 không có dòng cho phim/ảnh CĐHA, xét nghiệm rời, audit log. Đừng viết "TT 33 quy định lưu log X năm".
5. Thời hạn lưu tính "kể từ năm kết thúc công việc" (Luật Lưu trữ Đ15 k3), không từ ngày ra viện.
6. Hồ sơ ghép tạng: TT 33 mục 43 ghi 20 năm, Luật 75/2006 Đ38 k4 ghi 30 năm → áp 30 năm.
7. "Chữ ký điện tử" ≠ "chữ ký số"; ảnh chữ ký không đủ (Luật GDĐT Đ23 k2).
8. TT 13 Đ4 k2 b viết "nội trú, ban ngày **và** ngoại trú"; có trang chép thành "hoặc".
9. CV 365 vẫn dẫn NĐ 85/2016, TT 12/2022, NĐ 13/2023 (đã hết HL/bị thay), QĐ 742/QĐ-BTTTT, TT 39/2017/TT-BTTTT (trạng thái chưa xác minh).
10. Quy chế mẫu của cơ sở (ví dụ QĐ 162/QĐ-TTYT Mỹ Tú) còn dẫn NĐ 130/2018 và ghi sai "Luật GDĐT 20/2025/QH15". Đừng chép căn cứ từ quy chế mẫu.
11. Cổng benhandientu.moh.gov.vn vẫn liệt kê TT 46/2018 là "có hiệu lực" — không dùng để xác định hiệu lực.
12. Mốc 01/01/2027 "BV dừng bệnh án giấy" là kế hoạch, không phải hạn luật định.
13. Mức phạt NĐ 90 Chương II là mức cá nhân; cơ sở KCB là tổ chức nên ×2 (Đ39 k2 c, d là 6–10 triệu).
14. Schema CV 365 không có trường chữ ký số; địa chỉ còn cấp huyện.
15. NĐ 90/2026 và TT 25/2025 chỉ có bản OCR: chỉ diễn giải, không trích nguyên văn.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. Bản gốc QĐ 586/QĐ-BYT, QĐ 965/QĐ-BYT, CT 04/CT-BYT chưa tìm được trên nguồn nhà nước (link moh.gov.vn trả 404); bài NHIC/TTYQG 18/08/2026 dẫn QĐ 965: link chưa kiểm tra được (lỗi chứng chỉ).
2. Phòng khám chỉ khám và kê đơn (R02): hỏi Cục K2ĐT hoặc Cục QLKCB — lượt chỉ kê đơn (TT 26 Đ5 k1 a) có phải "điều trị ngoại trú" theo Luật KCB Đ76 và TT 13 Đ4 k2 b không; có bị phạt NĐ 90 Đ39 k2 d sau 31/12/2026 không.
3. Tiêu chí "hoàn thành" HSBA điện tử và quy trình công bố: không có trong VBQPPL; nội dung "Hồ sơ thẩm định đủ điều kiện công bố mẫu" trên cổng chưa đọc được.
4. Thời hạn lưu đơn thuốc độc lập, tài liệu thuốc gây nghiện/hướng thần/tiền chất (TT 26 Đ11 k2 dẫn TT 20/2017), ảnh DICOM (CLS), audit log: TT 33 không quy định; cần BYT hướng dẫn hoặc cơ sở tự quyết theo TT 33 Đ1 k2 b.
5. Thời hạn TT 53/2017 cho HSBA lập trước 01/07/2025 (TT 33 Đ2 k3 giữ thời hạn cũ): chưa đọc TT 53.
6. Luật Lưu trữ với cơ sở tư: Đ3 k5 cho tự quyết, nhưng Luật KCB Đ69 k2 buộc lưu theo pháp luật lưu trữ — phần nào bắt buộc với BV, PK tư (luật sư).
7. SaaS EMR có thuộc "kinh doanh dịch vụ lưu trữ" (Luật Lưu trữ Đ53, NĐ 113 Đ37) không (luật sư).
8. Luật 20/2026/QH16 (sửa Luật GDĐT, HL 01/03/2027): theo BAOMAT-CB-R26 không sửa Đ22–23; còn cần đọc phần sửa khác xem có ảnh hưởng TT 13 Đ3 k3 không.
9. Văn bản kỹ thuật cho phần mềm ký số theo NĐ 23 Đ17 k4; trạng thái TT 39/2017/TT-BTTTT, QĐ 742/QĐ-BTTTT.
10. Giá trị chứng cứ của OTP/sinh trắc cho giấy tờ luật đòi "bằng văn bản" (đồng ý phẫu thuật, từ chối điều trị) — luật sư (Luật GDĐT Đ11, Đ23).
11. Thời hạn hoàn thiện HSBA sau ra viện và quy tắc "khóa": không thấy trong Luật KCB, TT 32, TT 13, CV 365; kiểm thêm NĐ 96/2023 và quy chế chuyên môn BYT.
12. Ngày HL NĐ 137/2024 (để tính hạn Đ23): đang lấy 23/10/2024 theo inventory; nên đối chiếu ngày ký trên bản gốc.
13. Luật KCB Đ69 k4 d và đ cùng dẫn "điểm d khoản 2 Điều 8": có phải lỗi kỹ thuật lập pháp không, áp dụng thế nào (luật sư đọc bản gốc 2023).
