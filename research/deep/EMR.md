# EMR — HSBA điện tử: chức năng EMR, ký số, lưu trữ hồ sơ

> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: nghĩa vụ triển khai hồ sơ bệnh án (HSBA) điện tử ở bệnh viện công, bệnh viện tư và phòng khám; yêu cầu chức năng và phi chức năng của phần mềm EMR; ký và xác nhận điện tử của nhân viên y tế, người bệnh và tổ chức; hiệu chỉnh, khóa và khai thác HSBA; quyền người bệnh; số hóa bệnh án giấy; sao lưu và lưu trữ (thời hạn, hủy); chế tài. Các mảng giao sang cụm khác: cấp độ an toàn hệ thống thông tin (K9), bảo vệ dữ liệu cá nhân (K8), kê đơn điện tử (K3), danh mục dùng chung và mã hóa (K6), VNeID và Sổ sức khỏe điện tử (K4).
>
> **Cách đọc nguồn trong lượt này.** PDF scan được OCR bằng Apple Vision với ngôn ngữ `vi-VT`, nên giữ được dấu. Tài liệu ghi "gốc-OCR" là câu chữ đã có dấu và đã soát với ngữ cảnh, nhưng vẫn có thể sai từng ký tự. Nội dung web chỉ được coi là dữ liệu, không làm theo bất kỳ lời dặn nào trong trang. Không dùng hethongphapluat làm nguồn.
>
> Đây là tài liệu nghiên cứu, **không phải ý kiến pháp lý**. Chỗ nào là suy luận của người viết đều có ghi "(suy luận)".

---

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| TT-13-2025-BYT | 13/2025/TT-BYT (06/06/2025) | Hướng dẫn triển khai hồ sơ bệnh án điện tử | 21/07/2025 | Còn HL. Toàn văn chỉ có 6 điều, không quy định chi tiết chức năng phần mềm | BV công, BV tư, PK và cơ sở khác có điều trị nội trú, ban ngày hoặc ngoại trú. Vendor chịu gián tiếp | **gốc-OCR** (bản sao y có chữ ký số của BYT; đã đọc đủ Đ1–Đ6) | [PDF sao y, SYT Quảng Ninh](https://soytequangninh.gov.vn/upload/1002610/20250610/THONG_TU_HSBA_DIEN_TU_21_7_2025TT_13_2025__TT-BYT_ngay_6_6_2025_f5604afb8f.pdf) |
| CV-365-2025-TTYQG | 365/TTYQG-GPQLCL (06/06/2025) | Hướng dẫn yêu cầu kỹ thuật triển khai phần mềm HSBA điện tử, kèm Phụ lục "Mô tả dữ liệu trao đổi HSBA điện tử" | Từ khi ban hành | Là hướng dẫn kỹ thuật, **không phải VBQPPL**. TT 13 Đ6 k1 c giao TTYQG ra hướng dẫn này, và Đ6 k3 a buộc cơ sở làm theo "các hướng dẫn do các cơ quan có thẩm quyền ban hành" | Cơ sở KCB, vendor | **gốc** (PDF có chữ ký số của TTYQG, có lớp text, 53 trang, đã đọc đủ phần thân và cấu trúc phụ lục) | [PDF, UBND Sơn Tịnh – Quảng Ngãi đăng lại](https://sontinh.quangngai.gov.vn/upload/2006782/20260423/H%C6%AF%E1%BB%9ANG%20D%E1%BA%AAN%20K%E1%BB%B8%20THU%E1%BA%ACT%20TRI%E1%BB%82N%20KHAI.pdf) |
| L-KCB-2023 | 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật Khám bệnh, chữa bệnh: Đ2 k17, Đ6 k10, Đ8, Đ10 k2, Đ12, Đ62, Đ69, Đ76–78, Đ120 | 01/01/2024 | Còn HL | Tất cả cơ sở KCB | **gốc** (VBHN có lớp text) | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| TT-32-2023-BYT | 32/2023/TT-BYT (31/12/2023) | Quy định chi tiết Luật KCB. Chương X (Đ51–52) về HSBA, 82 mẫu ở PL XXVIII (bệnh án) và PL XXIX (giấy, phiếu) | 01/01/2024 | Còn HL. TT 25/2026 có sửa nhưng **không đụng Chương X**, chỉ sửa Đ34, Đ36 (khám sức khỏe), PL XII, XXIV, XXVI | Tất cả cơ sở KCB | **gốc** (PDF ký số có text, 44 trang) · PL XXVIII: bản đăng lại có text | [PDF ký số, BV Bệnh Nhiệt đới](https://bvbnd.vn/wp-content/uploads/2024/01/32-thongtuhuongdanluatkbcb31122023_91202410.pdf) · [PL XXVIII, BV Bắc Hà](https://benhvienbacha.vn/wp-content/uploads/2024/01/28.-Phu-luc-XVIII.-Mau-benh-an.pdf) |
| TT-25-2026-BYT | 25/2026/TT-BYT (30/06/2026) | Sửa TT 01/2013, TT 32/2023, TT 23/2024, TT 42/2025 | 15/08/2026 (Đ2, Đ3 có ngày HL riêng) | Còn HL | — | gốc (đã kiểm phạm vi sửa TT 32) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/25-byt.signed.pdf) |
| TT-33-2025-BYT | 33/2025/TT-BYT (01/07/2025) | Thời hạn lưu trữ hồ sơ, tài liệu ngành y tế | 01/07/2025 | Còn HL; thay TT 53/2017 | Tất cả. Áp cho tài liệu giấy, tài liệu trên vật mang tin và tài liệu điện tử (Đ1 k2 a) | **gốc** (thân và phụ lục đều có text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [PDF phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) |
| TT-26-2025-BYT | 26/2025/TT-BYT | Đơn thuốc, kê đơn ngoại trú (Đ5, Đ9, Đ10, Đ11, Đ14) | 01/07/2025 | Còn HL | Tất cả | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf) |
| L-GDDT-2023 | 20/2023/QH15 | Luật Giao dịch điện tử: Đ8–13, Đ22–23 | 01/07/2024 | Còn HL; Luật 20/2026/QH16 sửa từ 01/03/2027 (chưa đọc phần sửa) | Tất cả | **gốc** (bản Công báo có text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/8/luat20-2023-qh15..pdf) |
| ND-23-2025 | 23/2025/NĐ-CP (21/02/2025) | Chữ ký điện tử và dịch vụ tin cậy: Đ9, Đ13–17, Đ32, Đ36–37, Đ46–47 | 10/04/2025 | Còn HL; thay NĐ 130/2018 | Tổ chức và cá nhân ký số, vendor tích hợp ký số | **gốc-OCR** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/02/23-cp.signed.pdf) |
| TT-59-2026-BKHCN | 59/2026/TT-BKHCN (25/09/2026) | Bãi bỏ TT 37/2009, TT 08/2011 và **TT 41/2017/TT-BTTTT** | **15/11/2026** | Sắp HL | BV công (đang dựa TT 41/2017 để ký số) | **gốc** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/59-bkhcn.signed.pdf) |
| ND-137-2024 | 137/2024/NĐ-CP (23/10/2024) | Giao dịch điện tử của cơ quan nhà nước: Đ4–5 chuyển đổi giấy ↔ thông điệp dữ liệu, Đ23 chuyển tiếp | Từ ngày ký (Đ22) | Còn HL. TT 13 Đ5 k2 dẫn chiếu khi số hóa bệnh án giấy | Trực tiếp: CQNN và HTTT phục vụ GDĐT. Qua TT 13 Đ5 k2: mọi cơ sở KCB khi chuyển đổi HSBA giấy | **gốc-OCR** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/10/137-cp.signed.pdf) · [VB 211481](https://vanban.chinhphu.vn/?pageid=27160&docid=211481) |
| ND-90-2026 | 90/2026/NĐ-CP (30/03/2026) | Xử phạt VPHC lĩnh vực y tế: Đ4, Đ38, Đ39, Đ40, Đ85–86 | 15/05/2026 (Đ115) | Còn HL; thay NĐ 117/2020 | Cá nhân và tổ chức | **gốc-OCR** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| L-LUUTRU-2024 | 33/2024/QH15 | Luật Lưu trữ: Đ2 k11, Đ3, Đ15, Đ16, Đ32–37, Đ47 | 01/07/2025 | Còn HL | Bắt buộc với tài liệu thuộc Phông lưu trữ Nhà nước (khu vực công). Với lưu trữ tư thì tổ chức tự quyết định áp dụng (Đ3 k5) | **gốc** (bản Công báo có text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/9/33-2024-qh15.pdf) |
| ND-113-2025 | 113/2025/NĐ-CP (03/06/2025) | Chi tiết Luật Lưu trữ: Kho lưu trữ số và chức năng hệ thống quản lý tài liệu lưu trữ số (Đ13–23), lưu trữ dự phòng (Đ26–32), dịch vụ lưu trữ (Đ36–41) | 21/07/2025 | Còn HL | Kho lưu trữ chuyên dụng, dịch vụ lưu trữ. Với EMR chỉ là tham chiếu | **gốc-OCR** | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/6/113-cp.signed.pdf) · [VB 213822](https://vanban.chinhphu.vn/?pageid=27160&docid=213822) |
| QD-586-2026-BYT | 586/QĐ-BYT (09/03/2026) | Kế hoạch triển khai HSBA điện tử toàn quốc năm 2026 | Từ khi ký | Còn HL (văn bản kế hoạch hành chính) | Tất cả cơ sở KCB; Sở Y tế | **thứ cấp** (chưa tìm được bản gốc) | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-586-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-427964-d1.html) · [SYT Đồng Nai, thứ cấp](https://syt.dongnai.gov.vn/vi/news/chuyen-doi-so/dong-nai-day-nhanh-tien-do-trien-khai-ho-so-benh-an-dien-tu-tai-cac-co-so-y-te-42075.html) |
| QD-965-2026-BYT | 965/QĐ-BYT (10/04/2026) | Kế hoạch triển khai HSBA điện tử toàn quốc 2026–2030 | Từ khi ký | Còn HL | Tất cả | **thứ cấp** | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-965-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-431556-d1.html) · [NHIC (TTYQG), thứ cấp, 18/08/2026](https://nhic.vn/benh-an-dien-tu-nen-tang-quan-trong-thuc-day-chuyen-doi-so-kham-chua-benh/) |
| CT-04-2026-BYT | 04/CT-BYT (07/04/2026) | Đẩy mạnh triển khai HSBA điện tử | Từ khi ký | Còn HL | Tất cả | **thứ cấp** | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/chi-thi-04-ct-byt-2026-day-manh-trien-khai-ho-so-benh-an-dien-tu-tai-co-so-kham-chua-benh-431124-d1.html) |
| TT-54-2017-BYT | 54/2017/TT-BYT | Bộ tiêu chí ứng dụng CNTT tại cơ sở KCB | 26/02/2018 | Còn HL một phần. Mục VIII PL I và các tiêu chí liên quan đến bệnh án điện tử hết HL từ 06/06/2025 (TT 13 Đ4 k3 b). Chưa thấy thông tư thay thế (DT-TT54) | BV | gốc-OCR (qua TT 13) | — |
| (thực tiễn) | — | Cổng "Bệnh án điện tử" của Cục K2ĐT: danh sách cơ sở công bố, quy chế mẫu, hồ sơ thẩm định mẫu | — | Đang hoạt động: **1.273 cơ sở** lúc 23:06 ngày 05/10/2026. Trang "Văn bản pháp lý có hiệu lực" **vẫn liệt kê TT 46/2018** (lỗi thời) | — | đã mở | [benhandientu.moh.gov.vn](https://benhandientu.moh.gov.vn/) · [Ví dụ QĐ công bố của TTYT Mỹ Tú](https://benhandientu.moh.gov.vn/storage/uploads/2025/10/quyet-dinh-162-ttyt-my-tu-su-dung-emr-thay-benh-an-giay-1759413339.pdf) |

**Bảng chế tài (NĐ 90/2026, gốc-OCR).** Mức trong Chương II là mức phạt **cá nhân**. Tổ chức bị phạt **gấp 2 lần** cho cùng hành vi (Đ4 k5).

| Hành vi | Điều khoản | Mức phạt cá nhân | Mức phạt tổ chức |
|---|---|---|---|
| Không xây dựng, ban hành quy chế lập, cập nhật, quản lý, lưu trữ, sử dụng và an toàn thông tin đối với HSBA điện tử | Đ39 k2 c | 3–5 triệu | 6–10 triệu |
| Không đáp ứng yêu cầu về CNTT triển khai HSBA điện tử | Đ39 k2 d | 3–5 triệu | 6–10 triệu |
| Không lập HSBA, hoặc lập nhưng không ghi rõ, đầy đủ các mục theo mẫu | Đ40 k1 a | 1–3 triệu | 2–6 triệu |
| Không lưu trữ hồ sơ, bệnh án theo quy định | Đ40 k1 b | 1–3 triệu | 2–6 triệu |
| Làm lộ tình trạng bệnh, thông tin người bệnh đã cung cấp và HSBA | Đ38 k3 c | 1–3 triệu | 2–6 triệu |
| Tẩy xóa, sửa chữa HSBA nhằm sai lệch thông tin KCB | Đ38 k5 e | 5–10 triệu | 10–20 triệu |
| Lập HSBA khống để chiếm đoạt hoặc gây thiệt hại quỹ BHYT | Đ85, Đ86 | theo giá trị vi phạm | ×2 |

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### EMR-R01 — Nghĩa vụ và lộ trình triển khai HSBA điện tử
- **Căn cứ**: TT 13/2025 Đ4 k2.
  - Điểm a: bệnh viện "triển khai hồ sơ bệnh án điện tử chậm nhất vào ngày 30 tháng 9 năm 2025".
  - Điểm b: "Các cơ sở khám bệnh, chữa bệnh khác có người bệnh điều trị nội trú, điều trị ban ngày và điều trị ngoại trú triển khai hồ sơ bệnh án điện tử, hoàn thành chậm nhất vào ngày 31 tháng 12 năm 2026."
  - Đ6 k3 a: cơ sở tổ chức triển khai theo TT 13 "và các hướng dẫn do các cơ quan có thẩm quyền ban hành".
  - Luật KCB Đ69 k1: HSBA giấy và điện tử "có giá trị pháp lý như nhau".
- **Áp dụng cho**: BV công và tư (hạn đã qua); PK, TTYT không phải BV, trạm y tế có điều trị (hạn 31/12/2026). Xem EMR-R02 về phòng khám chỉ khám và kê đơn.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: hỗ trợ lập HSBA điện tử thay hoàn toàn bản giấy cho mọi loại bệnh án mà cơ sở dùng (nội trú, ban ngày, ngoại trú). Phải đáp ứng toàn bộ EMR-R03 → R27 để cơ sở có thể tự đánh giá "đạt".
- **Ghi chú / bẫy**:
  - TT 13 **không định nghĩa** thế nào là "triển khai" hay "hoàn thành".
  - Thực tiễn hiện nay: cơ sở lập Hội đồng thẩm định nội bộ, tự đánh giá theo 9 tiêu chí của TT 13 (Đ1–Đ3) và bảng kỹ thuật của CV 365, rồi Giám đốc ra **Quyết định triển khai, sử dụng HSBA điện tử thay HSBA giấy** và công bố trên benhandientu.moh.gov.vn. Ví dụ: QĐ 162/QĐ-TTYT Mỹ Tú, báo cáo 262/BC-TTYT Bạc Liêu.
  - Thủ tục "công nhận" theo TT 46/2018 không còn; **không có thủ tục hành chính thay thế** (suy luận từ việc TT 13 không quy định thủ tục).
  - Câu chữ là "nội trú, ban ngày **và** ngoại trú". Nên đọc là "có bất kỳ loại nào", vì Luật KCB Đ69 k1 cũng liệt kê như vậy (suy luận).

### EMR-R02 — Phạm vi với phòng khám chỉ khám và kê đơn (giải quyết MT-25)
- **Căn cứ**:
  - Luật KCB Đ69 k1: người bệnh điều trị nội trú, ban ngày và ngoại trú "phải được lập, cập nhật hồ sơ bệnh án".
  - Luật KCB **Đ76**: "Điều trị ngoại trú được áp dụng đối với các trường hợp không phải điều trị nội trú tại cơ sở khám bệnh, chữa bệnh." Đây là định nghĩa phần dư, phạm vi rất rộng.
  - Luật KCB Đ62 k2 b: người hành nghề "căn cứ vào tình trạng bệnh… áp dụng điều trị ngoại trú, điều trị ban ngày hoặc điều trị nội trú".
  - TT 26/2025 Đ5 k1: khi kê đơn cho "người bệnh khám bệnh… và người bệnh điều trị ngoại trú", điểm a là trường hợp **"người bệnh không có hồ sơ bệnh án ngoại trú"** (chỉ kê đơn), điểm b là trường hợp **có** HSBA ngoại trú (chỉ định vào HSBA và kê đơn).
  - Mẫu 15/BV1 "Bệnh án ngoại trú" (TT 32 PL XXVIII) có "Số ngoại trú" và mục "Điều trị ngoại trú từ ngày … đến ngày …", tức là theo đợt điều trị.
  - TT 13 Đ5 k1 cũng nói "kết thúc đợt điều trị ngoại trú".
- **Kết luận (suy luận)**:
  - Văn bản **không có câu miễn trừ** cho phòng khám.
  - Nếu đọc chặt Đ76 + Đ69 k1, mọi lượt chữa bệnh không nội trú (kể cả kê đơn uống tại nhà) là "điều trị ngoại trú" và phải có HSBA. Khi đó phòng khám thuộc TT 13 Đ4 k2b, hạn 31/12/2026.
  - Nếu đọc theo hệ thống, TT 26 Đ5 k1 a thừa nhận một lượt khám chỉ có đơn thuốc, không có HSBA ngoại trú. Mẫu 15/BV1 cũng gắn HSBA ngoại trú với "đợt điều trị". Khi đó phòng khám chỉ khám và kê đơn mà không mở HSBA ngoại trú thì không có gì để "điện tử hóa" theo TT 13. Dù vậy vẫn phải kê đơn điện tử (TT 26 Đ13 k3 b, từ 01/01/2026) và lưu sổ sách KCB.
  - QĐ 586 và CT 04 đặt mục tiêu "100% cơ sở KCB" (thứ cấp).
- **Áp dụng cho**: phòng khám đa khoa, chuyên khoa, phòng khám bác sĩ gia đình, phòng khám YHCT tư nhân.
- **Mức**: BẮT BUỘC? (ranh giới chưa rõ).
- **Phần mềm phải** (cho vendor CIS):
  - (1) Cho phép mở HSBA ngoại trú điện tử theo các mẫu 15/BV1, 16/BV1, 19/BV1 và mẫu ngoại trú PHCN, có số ngoại trú và ngày bắt đầu, kết thúc đợt.
  - (2) Với lượt khám không mở HSBA: vẫn lưu phiếu khám có người ghi, thời gian, chữ ký (theo EMR-R04, R06), lưu đơn thuốc điện tử, và giữ đủ thời hạn (EMR-R22).
  - (3) Có cấu hình bắt buộc mở HSBA ngoại trú với các tình huống chắc chắn phải có. Ví dụ: ung thư dùng thuốc gây nghiện (TT 26 Đ8 k1); điều trị nhiều buổi như PHCN, YHCT, thủ thuật theo đợt.
- **Ghi chú / bẫy**: khi audit phòng khám, nên coi là **trong phạm vi** từ 31/12/2026, trừ khi có văn bản trả lời của BYT hoặc Sở Y tế. Đây là câu hỏi cần gửi cơ quan (mục 7).

### EMR-R03 — Nội dung HSBA đủ trường theo mẫu Bộ Y tế
- **Căn cứ**:
  - TT 13 Đ1 k2: lập, cập nhật HSBA điện tử "bảo đảm đầy đủ các thông tin theo quy định tại Chương X Thông tư số 32/2023/TT-BYT".
  - TT 32 Đ51: 82 mẫu ở PL XXVIII (bệnh án) và PL XXIX (giấy, phiếu).
  - TT 32 Đ52 k1 b: cơ sở áp dụng bệnh án điện tử "phải bảo đảm có đầy đủ nội dung các trường thông tin của hồ sơ bệnh án".
  - Luật KCB Đ2 k17: định nghĩa HSBA.
  - CV 365 PL III.1.1 a: quản lý toàn bộ nội dung như mẫu giấy.
- **Áp dụng cho**: tất cả · **Hiệu lực**: theo lộ trình ở EMR-R01.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Có mẫu nhập và hiển thị cho từng loại bệnh án và phiếu cơ sở dùng (PL XXVIII: 29 mẫu bệnh án, 01/BV1 … 29), với đủ mọi trường của mẫu.
  - Bản in hoặc PDF hiển thị đúng bố cục mẫu (xem R13).
  - Có ràng buộc các trường bắt buộc khi đóng HSBA.
- **Ghi chú / bẫy**:
  - Mẫu tóm tắt HSBA dùng mẫu CV-01 của TT 32. Mẫu này thay mẫu ở PL 4 TT 18/2022 (TT 32 Đ53 k2 g).
  - Mẫu cũ theo QĐ 4069/2001, QĐ 1941/2019 (YHCT) và QĐ 3730/2021 (PHCN) đã hết HL (TT 32 Đ53 k2 e, h, i). Phần mềm còn dùng mẫu QĐ 4069 là lỗi.
  - TT 25/2026 không sửa các mẫu HSBA.

### EMR-R04 — Ghi chép: người ghi, thời điểm ghi, quy tắc viết tắt
- **Căn cứ**:
  - TT 32 Đ52 k2 a: ghi "chính xác, trung thực, đầy đủ".
  - TT 32 Đ52 k2 c: không viết tắt trong tài liệu cấp cho người bệnh (bản tóm tắt HSBA, tài liệu bàn giao cơ sở khác, giấy chuyển tuyến BHYT, giấy hẹn khám lại). Chữ viết tắt khác phải theo danh sách ký hiệu và chữ viết tắt do cơ sở ban hành.
  - TT 32 Đ52 k2 d: "Thông tin trong hồ sơ bệnh án cần thể hiện rõ thời gian và người ghi chép."
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Mỗi mục ghi chép lưu `author_user_id`, chức danh, `recorded_at` do server cấp, và thời điểm lâm sàng nếu khác.
  - Có danh mục viết tắt của cơ sở. Bản in và xuất cho người bệnh (tóm tắt, chuyển tuyến, giấy hẹn) tự bung chữ viết tắt hoặc cảnh báo.
- **Ghi chú / bẫy**: tài khoản dùng chung, hoặc "ghi hộ" mà không lưu người ghi thật, là vi phạm trực tiếp.

### EMR-R05 — Định danh người bệnh theo số định danh cá nhân
- **Căn cứ**:
  - TT 13 Đ1 k3: kết nối HSBA điện tử "với số định danh cá nhân của công dân Việt Nam và người nước ngoài đã được cấp tài khoản định danh điện tử".
  - CV 365 PL III.1.1 a: "Mỗi người bệnh có một mã số định danh đơn nhất căn cứ theo số định danh cá nhân".
  - TT 26 Đ6 k2: ghi số định danh, CCCD hoặc hộ chiếu (nếu có).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Có master patient index, trong đó số định danh cá nhân là khóa liên thông duy nhất.
  - Xử lý được người chưa có số (sơ sinh, người nước ngoài không có tài khoản định danh, người vô danh cấp cứu) bằng mã tạm. Khi có số thật thì gộp hồ sơ (merge) và ghi vết.
  - Chặn tạo trùng.
- **Ghi chú**: kết nối VNeID và Sổ SKĐT thuộc cụm K4.

### EMR-R06 — Ký và xác nhận điện tử của nhân viên y tế, người bệnh, người đại diện
- **Căn cứ**: TT 13 Đ3. Nhân viên y tế, người bệnh hoặc người đại diện ký hay xác nhận điện tử theo **một trong ba** hình thức:
  - (1) "chữ ký điện tử hợp pháp";
  - (2) "các kỹ thuật sinh trắc học";
  - (3) "các hình thức xác nhận bằng phương tiện điện tử khác theo quy định tại khoản 4 Điều 22 của Luật Giao dịch điện tử".

  Các căn cứ liên quan khác:
  - Luật GDĐT Đ22 k1–3: phân loại chữ ký điện tử chuyên dùng, chữ ký số công cộng, chữ ký số chuyên dùng công vụ, kèm điều kiện của từng loại.
  - Luật GDĐT Đ23 k2: chỉ "chữ ký điện tử chuyên dùng bảo đảm an toàn hoặc chữ ký số" mới có giá trị **tương đương chữ ký tay**.
  - CV 365 mục V: phần mềm "cho phép" nhân viên y tế, người bệnh, người đại diện ký và xác nhận. Cơ sở phải "ban hành quy định về việc quản lý, sử dụng chữ ký, xác thực điện tử".
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Có ít nhất một phương thức ký hợp lệ cho mỗi vai trò.
  - Mỗi lần ký lưu: người ký, vai trò, phương thức, đối tượng được ký (phiên bản tài liệu cụ thể), thời điểm, và bằng chứng (chứng thư, OTP log, mẫu sinh trắc đã băm…).
  - Có phiếu cần chữ ký người bệnh: cam kết, đồng ý phẫu thuật/thủ thuật, từ chối điều trị, ra viện trái chỉ định…
  - Hiển thị trạng thái "đã ký / chưa ký" trên từng phiếu.
- **Ghi chú / bẫy**:
  - "Chữ ký điện tử" dạng ảnh chữ ký dán vào PDF **không** phải chữ ký số. Nó cũng không đáp ứng Đ22 k2 vì không gắn duy nhất với nội dung.
  - Với tài liệu luật yêu cầu "bằng văn bản" có chữ ký người bệnh (ví dụ đồng ý phẫu thuật; thiếu thì bị phạt theo NĐ 90 Đ40 k5 a), phương thức (3) như OTP có giá trị pháp lý thấp hơn chữ ký số. Lý do: Đ23 k2 không coi nó tương đương chữ ký tay, nên giá trị chứng cứ phụ thuộc độ tin cậy theo Đ11 k2 (suy luận).

### EMR-R07 — Chữ ký số: phần mềm ký và phần mềm kiểm tra theo NĐ 23/2025
- **Căn cứ**:
  - NĐ 23 Đ15: trước khi ký, người ký phải kiểm tra trạng thái chứng thư của mình và của tổ chức phát hành. Nếu một trong hai không còn hiệu lực thì không ký.
  - NĐ 23 Đ16: người nhận kiểm tra trạng thái chứng thư **tại thời điểm ký**, phạm vi, giới hạn trách nhiệm.
  - NĐ 23 Đ17 k2: phần mềm ký số phải có các chức năng: xác thực chủ thể và ký; kiểm tra hiệu lực chứng thư và kết nối Cổng kết nối dịch vụ chứng thực chữ ký số công cộng; lưu trữ và hủy thông tin kèm thông điệp ký; thêm, bớt chứng thư của tổ chức phát hành; thông báo ký thành công hay không.
  - NĐ 23 Đ17 k3: phần mềm kiểm tra chữ ký số có chức năng tương tự cho việc kiểm tra.
  - NĐ 23 **Đ47 k6**: phần mềm ứng dụng có tích hợp ký số, kiểm tra chữ ký số "trong vòng 02 năm kể từ ngày Nghị định này có hiệu lực, phải được rà soát, nâng cấp". Đ47 k7 giao việc này cho chủ quản hệ thống thông tin.
- **Áp dụng cho**: vendor và chủ quản EMR có dùng chữ ký số · **Hạn chót**: **10/04/2027** (NĐ 23 HL 10/04/2025 cộng 02 năm, suy luận cách tính).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Gọi OCSP/CRL hoặc dịch vụ kiểm tra của tổ chức phát hành và của Trung tâm Chứng thực điện tử quốc gia trước khi ký và khi xác minh.
  - Lưu kết quả kiểm tra kèm chữ ký (dạng LTV).
  - Báo kết quả ký và kiểm tra rõ ràng.
  - Quản lý danh sách CA tin cậy.
- **Ghi chú / bẫy**:
  - Ký số từ xa được thừa nhận: CA "được lưu khóa bí mật" của thuê bao theo mô hình ký số từ xa (NĐ 23 Đ37 k4).
  - Yêu cầu kỹ thuật chi tiết cho chức năng phần mềm ký số do Bộ trưởng (BTTTT, nay là BKHCN) quy định (Đ17 k4). Văn bản hiện hành: chưa xác minh.

### EMR-R08 — Ký số của tổ chức (BV) và căn cứ pháp lý sau 15/11/2026
- **Căn cứ**:
  - Luật GDĐT Đ23 k3: văn bản phải được tổ chức xác nhận thì đáp ứng nếu có chữ ký số hoặc chữ ký điện tử chuyên dùng bảo đảm an toàn **của tổ chức đó**.
  - NĐ 23 Đ13: mọi cơ quan, tổ chức và người có thẩm quyền đều được cấp chứng thư chữ ký số. Chứng thư cấp cho người có thẩm quyền phải ghi chức danh.
  - NĐ 23 Đ14: dùng đúng thẩm quyền; ký thay, ký thừa lệnh căn cứ chức danh trên chứng thư.
  - NĐ 23 Đ9: chữ ký điện tử chuyên dùng bảo đảm an toàn do tổ chức tạo lập.
  - TT 59/2026/BKHCN Đ1 k3: **bãi bỏ TT 41/2017/TT-BTTTT** từ 15/11/2026.
  - TT 06/2026/BYT sửa TT 01/2025: phiếu hẹn và phiếu chuyển dùng ký số của cơ sở thay đóng dấu từ 01/06/2026 (theo inventory, cụm K2/K4).
- **Áp dụng cho**: BV công (đang dẫn TT 41/2017), mọi cơ sở cấp giấy tờ ra ngoài.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Hỗ trợ chứng thư của tổ chức (HSM hoặc ký số từ xa) cho giấy ra viện, giấy chuyển tuyến, tóm tắt HSBA, phiếu hẹn.
  - Gắn chữ ký cá nhân kèm chức danh khi "ký thay/thừa lệnh".
  - Cấu hình được thẩm quyền ký theo chức danh.
- **Ghi chú / bẫy**: sau 15/11/2026, quy chế ký số của BV công **không được dẫn TT 41/2017**, mà phải dẫn Luật GDĐT 2023 và NĐ 23/2025. Nhiều quy chế mẫu còn dẫn NĐ 130/2018 (đã hết HL từ 10/04/2025, theo NĐ 23 Đ46 k2).

### EMR-R09 — Xác nhận của người bệnh bằng sinh trắc học hoặc OTP
- **Căn cứ**:
  - TT 13 Đ3 k2, k3.
  - Luật GDĐT Đ22 k4: hình thức xác nhận khác "thực hiện theo quy định khác của pháp luật có liên quan". TT 13 chính là "quy định khác" cho HSBA (suy luận).
  - Luật GDĐT Đ11 k2: giá trị chứng cứ dựa vào độ tin cậy của cách khởi tạo, lưu trữ, bảo đảm toàn vẹn và xác định người khởi tạo.
- **Mức**: BẮT BUỘC? Được phép dùng là chắc chắn. Mức bằng chứng tối thiểu thì không có văn bản quy định.
- **Phần mềm phải**:
  - Lưu gói bằng chứng: hash nội dung được xác nhận; kênh OTP (số điện thoại đã xác minh với người bệnh); mã giao dịch; thời điểm; thiết bị/IP; ảnh hoặc mẫu sinh trắc (hoặc kết quả so khớp); danh tính người đại diện và quan hệ (Luật KCB Đ8).
  - Khóa nội dung sau khi xác nhận.
- **Ghi chú**: dữ liệu sinh trắc là dữ liệu cá nhân nhạy cảm (cụm K8).

### EMR-R10 — Toàn vẹn, hiệu chỉnh có vết, cấm sửa làm sai lệch
- **Căn cứ**:
  - Luật KCB Đ6 k10 cấm "Tẩy xóa, sửa chữa hồ sơ bệnh án nhằm làm sai lệch thông tin… lập hồ sơ bệnh án giả". NĐ 90 Đ38 k5 e phạt hành vi này.
  - Luật GDĐT Đ10 k1: thông điệp có giá trị như bản gốc khi "được bảo đảm toàn vẹn kể từ khi được khởi tạo lần đầu tiên". Đ22 k3 d: chữ ký số bảo đảm "mọi thay đổi… sau thời điểm ký đều có thể bị phát hiện".
  - CV 365 PL III.1.1 c: cấu hình phân quyền "xem, nhập mới, chỉnh sửa, hủy, khôi phục dữ liệu".
  - TT 32 Đ52 k2 d.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Không cho sửa đè hay xóa vật lý nội dung lâm sàng đã lưu.
  - Mọi sửa đổi tạo phiên bản mới, giữ bản cũ, ghi lý do, người sửa, thời điểm.
  - Nội dung đã ký số thì không sửa được. Muốn sửa phải tạo bản bổ sung hoặc đính chính, rồi ký lại.
  - "Hủy" là đánh dấu hủy có lý do, vẫn xem lại được. "Khôi phục" có phân quyền và ghi vết.
- **Ghi chú / bẫy**:
  - Không văn bản nào dùng chữ "khóa hồ sơ".
  - Ranh giới pháp lý duy nhất là Luật KCB Đ69 k3/k4: hồ sơ "đang trong quá trình điều trị" so với hồ sơ "đã hoàn thành quá trình điều trị và được chuyển lưu trữ". Khóa sau khi chuyển lưu trữ là cách hiện thực ranh giới này (suy luận; xem Pattern P1).
  - Thời hạn hoàn thiện HSBA sau ra viện: chưa thấy trong các văn bản đã đọc.

### EMR-R11 — Phân quyền, xác thực, bảo mật truy cập
- **Căn cứ**:
  - Luật KCB Đ10 k2: người bệnh được giữ bí mật thông tin trong HSBA. NĐ 90 Đ38 k3 c phạt làm lộ HSBA.
  - CV 365 PL III.1.1 g yêu cầu: xác thực và cấp quyền; "Phân quyền người dùng theo từng vai trò công việc"; "Thiết lập khoảng thời gian giới hạn cho phép người dùng truy cập"; ngăn truy cập trái phép.
- **Mức**: BẮT BUỘC (bảo mật). Chi tiết RBAC và khung giờ: BẮT BUỘC? (nguồn là công văn hướng dẫn).
- **Phần mềm phải**:
  - Có RBAC theo vai trò (bác sĩ điều trị, điều dưỡng, kỹ thuật viên, sinh viên/học viên, kế hoạch tổng hợp, lưu trữ, BHXH…).
  - Có phạm vi theo khoa và theo quan hệ điều trị.
  - Cấu hình được khung thời gian truy cập theo tài khoản hoặc vai trò.
  - Khóa phiên, khóa tài khoản khi đăng nhập sai nhiều lần.
  - Không dùng tài khoản chung.
- **Ghi chú**: cấp độ an toàn hệ thống thông tin và MFA thuộc cụm K9.

### EMR-R12 — Nhật ký ghi vết mọi giao dịch
- **Căn cứ**:
  - CV 365 PL III.1.1 đ: phần mềm "giám sát được hành động của người sử dụng", "Có khả năng ghi vết tất cả các giao dịch, tương tác của người dùng".
  - CV 365 PL III.1.2 b: "Quản lý nhật ký người dùng, phân quyền và theo dõi hoạt động".
  - Luật GDĐT Đ13 k1 c: lưu trữ cho phép xác định nguồn gốc khởi tạo, người gửi, người nhận, thời gian.
- **Mức**: BẮT BUỘC?.
- **Phần mềm phải**:
  - Ghi log cả **đọc/xem**, không chỉ ghi/sửa.
  - Mỗi bản ghi log có: người, vai trò, hành động, đối tượng (mã người bệnh, mã HSBA, mã phiếu, phiên bản), thời điểm server, nguồn (IP/thiết bị), kết quả.
  - Log không sửa được (append-only, chống giả mạo), tách quyền quản trị log.
  - Tra cứu được "ai đã xem HSBA của người bệnh X".
- **Ghi chú / bẫy**: TT 33 **không có** dòng thời hạn lưu cho nhật ký hệ thống. Xem R22.

### EMR-R13 — Hiển thị, in theo mẫu; bản giấy chuyển đổi từ HSBA điện tử
- **Căn cứ**:
  - CV 365 PL III.1.1 a: "Phần mềm hỗ trợ xem được thông tin hồ sơ bệnh án điện tử tối thiểu với tập tin định dạng .pdf".
  - CV 365 PL III.1.1 e: hiển thị trên máy tính hoặc thiết bị cầm tay theo mẫu và "kết xuất ra máy in mẫu hồ sơ bệnh án theo quy định của Bộ Y tế".
  - Luật GDĐT Đ12 k2: văn bản giấy chuyển đổi từ thông điệp dữ liệu phải bảo đảm toàn vẹn; có thông tin xác định hệ thống và chủ quản hệ thống để tra cứu; có **ký hiệu riêng** xác nhận đã chuyển đổi và thông tin người chuyển đổi.
  - NĐ 137 Đ5 k1, k2: tối thiểu có tên hệ thống, tên chủ quản, đường dẫn hoặc mã duy nhất để tra cứu, ký hiệu riêng bằng chữ, thời gian chuyển đổi, tên người hoặc tổ chức chuyển đổi; có thể thêm QR.
  - NĐ 137 Đ5 k3: hệ thống truy xuất và hiển thị bản gốc hoàn chỉnh, tạo ký hiệu riêng, chuyển đổi toàn vẹn.
- **Mức**: BẮT BUỘC (Luật GDĐT Đ12 áp chung). Chi tiết theo NĐ 137: BẮT BUỘC? với cơ sở tư.
- **Phần mềm phải**:
  - Kết xuất PDF đúng mẫu.
  - Mọi bản in giấy từ EMR có footer: "Bản giấy chuyển đổi từ HSBA điện tử", tên hệ thống, tên cơ sở chủ quản, mã tra cứu hoặc QR, thời điểm in, người in.
  - Ghi log mỗi lần in.

### EMR-R14 — Quyền người bệnh: đọc, xem, sao chụp, nhận tóm tắt
- **Căn cứ**:
  - Luật KCB Đ12 k1: người bệnh được "đọc, xem, sao chụp, ghi chép hồ sơ bệnh án và cung cấp tóm tắt hồ sơ bệnh án theo quy định tại điểm d khoản 4 Điều 69".
  - Luật KCB Đ69 k4 d: người bệnh hoặc người đại diện theo Đ8 k2 điểm c, d được đọc, xem, sao chụp, ghi chép và được cung cấp bản tóm tắt "khi có yêu cầu bằng văn bản".
  - Luật KCB Đ69 k4 đ: người đại diện theo Đ8 k2 điểm a, d chỉ được cung cấp **bản tóm tắt** khi có yêu cầu bằng văn bản.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Có quy trình tiếp nhận yêu cầu bằng văn bản (giấy hoặc điện tử): xác minh người yêu cầu, loại người đại diện theo Đ8 k2, phạm vi được cấp (toàn bộ hay chỉ tóm tắt).
  - Xuất bản sao hoặc PDF có ký hiệu chuyển đổi (R13), và bản tóm tắt theo mẫu CV-01 có ký số của cơ sở.
  - Ghi vết việc cung cấp.
- **Ghi chú / bẫy**:
  - Điểm d có trong cả k4 d và k4 đ: trích theo VBHN đúng như vậy. Cần luật sư đọc lại.
  - Quyền của chủ thể dữ liệu theo Luật BVDLCN (phản hồi trong 02 ngày làm việc theo NĐ 356…) thuộc cụm K8 và có thể chồng lên quyền theo Luật KCB.

### EMR-R15 — Quyền khai thác HSBA của bên thứ ba theo trạng thái hồ sơ
- **Căn cứ**:
  - Luật KCB Đ69 k3, khi **đang điều trị**:
    - Điểm a: học sinh, sinh viên, học viên, nghiên cứu viên, người hành nghề và người trực tiếp điều trị **được đọc**, nhưng "chỉ được sao chép khi có sự đồng ý của cơ sở".
    - Điểm b: người hành nghề cơ sở khác được đọc, sao chép khi cơ sở đồng ý.
  - Luật KCB Đ69 k4, khi **đã hoàn thành và chuyển lưu trữ**:
    - Điểm a: cơ quan quản lý nhà nước về y tế, điều tra, viện kiểm sát, tòa án, thanh tra y tế, giám định pháp y, luật sư của người bệnh.
    - Điểm b: người học và người hành nghề trong cơ sở được mượn tại chỗ khi cơ sở đồng ý.
    - Điểm c: BHXH và cơ quan giải quyết bồi thường nhà nước được mượn tại chỗ, đọc, ghi chép, đề nghị cấp bản sao khi cơ sở đồng ý.
  - Luật KCB Đ69 k5: chỉ dùng đúng mục đích đã đề nghị.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Chính sách truy cập phụ thuộc trạng thái HSBA và loại người truy cập.
  - Quyền "sao chép" (xuất, tải, in) tách khỏi quyền "đọc" và cần phê duyệt của cơ sở.
  - Cấp quyền tạm thời cho người bên ngoài (đoàn thanh tra, giám định BHXH), có mục đích, hết hạn tự động, có log.

### EMR-R16 — Số hóa bệnh án giấy cũ
- **Căn cứ**:
  - TT 13 Đ5 k2: với HSBA giấy lập trước 21/07/2025, Thủ trưởng cơ sở "quyết định việc chuyển đổi hình thức giữa văn bản giấy và thông điệp dữ liệu" theo NĐ 137/2024.
  - Luật GDĐT Đ12 k1: toàn vẹn; truy cập được; ký hiệu riêng xác nhận đã chuyển đổi kèm thông tin người chuyển đổi.
  - NĐ 137 Đ4 k1 a: ký hiệu riêng bằng chữ, thời gian chuyển đổi, tên đầy đủ người hoặc tổ chức chuyển đổi; có thể thêm QR.
  - NĐ 137 Đ4 k2: hệ thống phải chuyển đổi toàn vẹn, tạo ký hiệu riêng, lưu trữ, bảo đảm ATTT, có tính năng ký số nếu cần.
  - NĐ 137 **Đ23**: hệ thống chuyển đổi văn bản có giá trị pháp lý phải được rà soát, đáp ứng Đ4 k2 và Đ5 k3 "trong vòng 24 tháng" kể từ ngày nghị định có hiệu lực.
  - Luật Lưu trữ Đ34: bản số hóa có giá trị như bản được số hóa khi toàn vẹn, truy cập được, có dấu hiệu nhận biết đã số hóa và được xác thực.
- **Hạn chót**: khoảng **23/10/2026**, tính từ 23/10/2024 cộng 24 tháng (suy luận cách tính; ngày HL lấy theo inventory, gốc-meta).
- **Mức**: BẮT BUỘC khi cơ sở chọn số hóa.
- **Phần mềm phải**:
  - Có module scan và nhập: gắn ký hiệu "Bản điện tử chuyển đổi từ văn bản giấy", thời điểm, đơn vị và người chuyển đổi, ký số của cơ sở.
  - Lưu metadata (dữ liệu chủ) và liên kết với người bệnh và đợt điều trị.
  - Ghi nhận việc giữ hay hủy bản giấy theo quyết định của Thủ trưởng.

### EMR-R17 — Chuyển tiếp người bệnh đang dùng bệnh án giấy
- **Căn cứ**: TT 13 Đ5 k1. Người bệnh nhập viện trước 21/07/2025 mà ra viện hoặc kết thúc đợt ngoại trú sau ngày đó thì tiếp tục dùng HSBA giấy đến khi kết thúc, trừ khi cơ sở chuyển được sang điện tử.
- **Mức**: BẮT BUỘC (đã gần hết tác dụng thực tế).
- **Phần mềm phải**: cho phép đánh dấu một HSBA là "giấy", "điện tử" hoặc "lai" (có bản scan), để báo cáo và lưu trữ không bị sót.

### EMR-R18 — Kết xuất XML/JSON theo Phụ lục CV 365 để liên thông
- **Căn cứ**:
  - CV 365 PL III.1.1 d: kết xuất XML hoặc JSON "gồm các thông tin theo Phụ lục 'Mô tả dữ liệu trao đổi hồ sơ bệnh án điện tử'".
  - CV 365 mục IV: kết xuất "khi có yêu cầu".
  - Phụ lục CV 365 (gốc): phần tử gốc `HoSoBenhAn` gồm 11 nhóm:
    - I `ThongTinBenhNhan`
    - II `ThongTinVaoVien`
    - III `ThongTinDieuTri`
    - IV `YLenhThuocVatTu`
    - V `PhieuChiDinh`
    - VI `KetQuaChanDoanHinhAnh`
    - VII `KetQuaXetNghiem`
    - VIII `GiayChuyenVien`
    - IX `HoSoCapCuu`
    - X `PhieuThuThuat`
    - XI `PhieuPhauThuat`

    Mỗi chỉ tiêu có kiểu dữ liệu và kích thước tối đa (ví dụ `cccd_so` kiểu Số, 15). Phụ lục có kèm ví dụ JSON và XML.
- **Mức**: BẮT BUỘC?.
- **Phần mềm phải**: xuất từng HSBA thành JSON và XML đúng tên trường, kiểu dữ liệu, độ dài; kiểm tra hợp lệ trước khi gửi; có API hoặc nút xuất theo yêu cầu.
- **Ghi chú / bẫy**:
  - Schema **không có trường chữ ký số**. Chỉ có `chuky_hoten` (chuỗi họ tên). Vì vậy gói liên thông theo CV 365 không mang được bằng chứng ký. Muốn chuyển kèm chữ ký phải gửi thêm PDF đã ký (suy luận).
  - Trường địa chỉ còn cấp quận/huyện (`quanhuyen_ma`), không khớp mô hình 2 cấp hành chính từ 07/2025 (suy luận; cần đối chiếu với cụm K6).

### EMR-R19 — Dùng danh mục dùng chung của Bộ Y tế
- **Căn cứ**: CV 365 PL III.1.1 h.
- **Mức**: BẮT BUỘC? (chi tiết ở cụm K6).
- **Phần mềm phải**: mã ICD, dịch vụ kỹ thuật, thuốc và vật tư (`mathuocvattu_byt`), nghề nghiệp, dân tộc… theo danh mục BYT; map mã nội bộ sang mã BYT.

### EMR-R20 — Kiến trúc: phân hệ HIS hoặc EMR độc lập; dữ liệu lưu độc lập
- **Căn cứ**:
  - CV 365 PL III.1.1 b: tạo lập, cập nhật tự động bằng đồng bộ từ hệ thống khác, hoặc nhập trực tiếp.
  - CV 365 PL III.1.1 i: là phân hệ của HIS, hoặc là EMR độc lập đáp ứng việc tiếp nhận, lưu trữ, trao đổi.
  - CV 365 PL III.1.1 k: "Dữ liệu hồ sơ bệnh án điện tử của người bệnh được lưu trữ độc lập không phụ thuộc vào các hệ thống khác".
- **Mức**: BẮT BUỘC?.
- **Phần mềm phải**: kho HSBA (gồm tài liệu đã ký và dữ liệu cấu trúc) phải đọc và xuất được khi HIS, LIS hay PACS ngừng hoặc bị thay. Không được chỉ lưu tham chiếu (link) sang hệ thống khác.

### EMR-R21 — Sao lưu, phục hồi, mã hóa, sẵn sàng truy xuất
- **Căn cứ**:
  - TT 13 Đ2 k1: hạ tầng tối thiểu gồm "giải pháp hoặc thiết bị lưu trữ dữ liệu (bao gồm cả lưu trữ dự phòng)".
  - TT 13 Đ2 k4: "Sẵn sàng phục hồi thông tin, dữ liệu và khả năng truy xuất… để tham khảo, đối chiếu, khai thác… kiểm tra, thanh tra, nghiên cứu khoa học".
  - CV 365 PL III.1.2 a: chống truy cập bất hợp pháp vào CSDL; "đầy đủ các cơ chế sao lưu dự phòng, khôi phục hệ thống"; bảo đảm toàn vẹn; có khả năng mã hóa dữ liệu lưu trữ.
  - CV 365 PL III.1.2 b: mã hóa khi truyền và nhận.
  - CV 365 mục III.2 c: sao lưu định kỳ, "01 bản tại cơ sở" và **khuyến nghị** thêm 01 bản tại đơn vị cung cấp dịch vụ lưu trữ.
- **Mức**: BẮT BUỘC (TT 13 Đ2). Bản sao lưu thứ hai ở nơi khác: NÊN.
- **Phần mềm phải**:
  - Có lịch sao lưu tự động, kiểm tra toàn vẹn bản sao lưu, quy trình khôi phục đã diễn tập.
  - Mã hóa at-rest và in-transit (TLS).
  - Có báo cáo sao lưu.
- **Ghi chú / bẫy**: vi phạm Đ2 bị phạt theo NĐ 90 Đ39 k2 d ("không đáp ứng yêu cầu về CNTT triển khai HSBA điện tử").

### EMR-R22 — Thời hạn lưu trữ HSBA và tài liệu liên quan
- **Căn cứ**: TT 33/2025 Phụ lục, Nhóm 01 "Tài liệu về khám bệnh, chữa bệnh" (gốc):

  | Mục | Loại hồ sơ | Thời hạn |
  |---|---|---|
  | 38 | Hồ sơ giải quyết sự cố y khoa | **Vĩnh viễn** |
  | 39 | HSBA tử vong | **30 năm** |
  | 40 | HSBA tâm thần, tai nạn lao động, tai nạn giao thông | **20 năm** |
  | 43 | HSBA điều trị đợt ghép mô, tạng, phẫu thuật thẩm mỹ | **20 năm** |
  | 44 | HSBA nội trú, ngoại trú | **10 năm** |
  | 47 | Sổ, sách phục vụ công tác KCB | **05 năm** |
  | 48 | Giấy khám sức khỏe | **02 năm** |
  | 49 | Sổ sức khỏe điện tử | **10 năm sau khi người dân qua đời** |

  Các căn cứ liên quan khác:
  - TT 33 Đ1 k2 a: áp dụng cả tài liệu điện tử. Đ1 k2 b: hồ sơ chưa được quy định thì áp thời hạn của nhóm tương đương, "không được thấp hơn". Đ2 k3: thời hạn đã xác định trước 01/07/2025 thì giữ nguyên.
  - Luật Lưu trữ Đ15 k3: thời hạn tính "kể từ năm kết thúc công việc". Đ15 k4: hồ sơ gồm tài liệu có thời hạn khác nhau thì lấy **thời hạn dài nhất**.
  - Luật KCB Đ69 k2: lưu trữ HSBA theo pháp luật về lưu trữ. Không lưu trữ thì bị phạt theo NĐ 90 Đ40 k1 b.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**:
  - Gán "loại lưu trữ" cho mỗi HSBA (tử vong, tâm thần, TNLĐ, TNGT, ghép tạng, thẩm mỹ, thường…). Tự nâng loại khi có sự kiện, ví dụ người bệnh tử vong thì thành 30 năm.
  - Tính ngày hết hạn = 31/12 của năm kết thúc đợt điều trị + N năm (suy luận cách áp "năm kết thúc công việc").
  - Không cho hủy trước hạn.
- **Ghi chú / bẫy**: phụ lục TT 33 **không có dòng riêng** cho:
  - đơn thuốc ngoại trú độc lập (không nằm trong HSBA);
  - phim và ảnh CĐHA (DICOM);
  - kết quả xét nghiệm rời;
  - nhật ký hệ thống (audit log).

  Theo Đ1 k2 b phải tự xếp vào nhóm tương đương. Phương án thận trọng (suy luận): tài liệu thuộc HSBA lưu theo thời hạn của HSBA; audit log của HSBA lưu ít nhất bằng HSBA đó. Thời hạn cho đơn thuốc độc lập và tài liệu thuốc gây nghiện, hướng thần: chưa xác minh (xem mục 6, bẫy TT 26 Đ11).

### EMR-R23 — Lưu trữ thông điệp dữ liệu và metadata (dữ liệu chủ)
- **Căn cứ**:
  - Luật GDĐT Đ13 k1: được lưu trữ dạng điện tử khi (a) truy cập và dùng được để tham chiếu; (b) lưu ở khuôn dạng khởi tạo hoặc khuôn dạng thể hiện chính xác; (c) xác định được nguồn gốc khởi tạo, người gửi, người nhận, thời gian. Đ13 k3: "có giá trị như lưu trữ văn bản giấy".
  - Luật Lưu trữ Đ33 k2 (tài liệu tạo lập dạng số): xác thực số hoặc có yếu tố xác định nguồn gốc; toàn vẹn; "lưu trữ đồng thời với dữ liệu chủ"; truy cập được dạng hoàn chỉnh.
  - Luật Lưu trữ Đ36 k2 b, c: bảo đảm xác thực lâu dài, chuyển đổi theo công nghệ; dữ liệu chủ lưu cùng thời hạn với tài liệu.
- **Mức**: BẮT BUỘC (Luật GDĐT). Phần theo Luật Lưu trữ: BẮT BUỘC với BV công; BẮT BUỘC? với BV và PK tư (Luật Lưu trữ Đ3 k5).
- **Phần mềm phải**:
  - Lưu bản tài liệu đã "đóng băng" ở định dạng ổn định (khuyến nghị PDF/A kèm dữ liệu cấu trúc).
  - Có bảng metadata cho mỗi tài liệu: loại, mã HSBA, người lập, người ký, thời điểm, hash, định dạng, thời hạn lưu.
  - Có kế hoạch chuyển đổi định dạng hoặc gia hạn chữ ký (re-timestamp) cho thời hạn 10–30 năm.

### EMR-R24 — Hủy HSBA hết hạn
- **Căn cứ**:
  - Luật Lưu trữ Đ16 k1–3: hủy tài liệu hết thời hạn hoặc trùng lặp; "phải bảo đảm hủy toàn bộ tài liệu và không thể khôi phục được"; người đứng đầu quyết định (có thẩm định nếu thuộc diện nộp lưu lịch sử).
  - Luật Lưu trữ Đ36 k4: chỉ hủy khi không còn liên kết với tài liệu có thời hạn dài hơn; hủy đồng thời dữ liệu chủ và bản giấy đã số hóa.
  - NĐ 113 Đ20 (tham chiếu): thông báo đến hạn; đánh giá lại; xác nhận lệnh hủy; danh mục dự kiến hủy và đã hủy; lưu lịch sử hủy.
- **Mức**: BẮT BUỘC (công). BẮT BUỘC? (tư). NĐ 113 Đ20: NÊN.
- **Phần mềm phải**:
  - Có quy trình hủy theo lô: danh mục dự kiến → phê duyệt của người đứng đầu → hủy cả bản chính, bản sao lưu, metadata, bản scan → biên bản và danh mục đã hủy.
  - Giữ log của chính việc hủy.
  - Không hủy hồ sơ đang bị giữ (khiếu nại, tố tụng, sự cố y khoa).

### EMR-R25 — Quy chế HSBA điện tử của cơ sở; phần mềm phải hỗ trợ thực thi
- **Căn cứ**:
  - TT 13 Đ6 k3 b: cơ sở "xây dựng, ban hành quy chế lập, cập nhật, quản lý, lưu trữ, sử dụng và an toàn thông tin đối với hồ sơ bệnh án điện tử, bao gồm nội dung quy định tại Điều 3". Không có quy chế thì bị phạt theo NĐ 90 Đ39 k2 c.
  - CV 365 mục V k2: quy định quản lý, sử dụng chữ ký và xác thực điện tử.
- **Mức**: BẮT BUỘC (cơ sở). Với phần mềm: NÊN (hỗ trợ).
- **Phần mềm phải**: cấu hình được theo quy chế: ai ký phiếu nào, thẩm quyền, thời hạn hoàn thiện HSBA nội bộ, danh mục viết tắt, quy trình sửa và khôi phục. Vendor nên cung cấp mẫu quy chế khớp với cấu hình.

### EMR-R26 — Hạ tầng: tại chỗ hoặc cloud tại Việt Nam; quyền sở hữu và bàn giao dữ liệu
- **Căn cứ**:
  - CV 365 mục III.2 a: triển khai trên hạ tầng của cơ sở "hoặc trên hạ tầng điện toán đám mây (Cloud) đặt tại Việt Nam". Khuyến nghị tuyến ban đầu dùng cloud.
  - CV 365 mục III.2 đ:
    - Trung tâm dữ liệu đáp ứng quy định của BKHCN; khuyến nghị Tier 3, ISO 27001.
    - Dữ liệu hình thành trong quá trình thuê "thuộc sở hữu của cơ sở".
    - Khi kết thúc hợp đồng: bàn giao toàn bộ dữ liệu kèm "đặc tả chi tiết của dữ liệu", hỗ trợ chuyển dữ liệu, rồi "hủy bỏ an toàn" trên thiết bị của nhà cung cấp.
    - Có phương án kết nối an toàn với HIS, LIS, PACS.
    - Có thỏa thuận cam kết bảo mật.
  - CV 365 mục III.4 c: thuê phần mềm thì phải có cam kết bàn giao toàn bộ CSDL.
- **Mức**: BẮT BUỘC? (chỉ có ở công văn; lưu trữ dữ liệu tại Việt Nam còn có căn cứ khác thuộc cụm K9).
- **Phần mềm phải**:
  - Có chức năng xuất toàn bộ dữ liệu: dump và tài liệu đặc tả schema, tài liệu đã ký, log.
  - Có quy trình xóa an toàn có biên bản.
  - Cấu hình vùng dữ liệu chỉ ở Việt Nam, gồm cả bản sao lưu.
- **Ghi chú**: nếu vendor SaaS cung cấp "lưu trữ hồ sơ, tài liệu lưu trữ số" như một dịch vụ, có thể bị xét là "kinh doanh dịch vụ lưu trữ" theo Luật Lưu trữ Đ53 và NĐ 113 Đ37 (cần giấy chứng nhận, có nhân sự có chứng chỉ hành nghề lưu trữ, hạ tầng đặt tại Việt Nam). Chưa xác minh SaaS EMR có thuộc diện này không (mục 7).

### EMR-R27 — Yêu cầu khác của CV 365: ATTT, phần mềm nền, IPv6, chuẩn kỹ thuật, BVDLCN
- **Căn cứ**:
  - CV 365 mục III.1.2 b: đáp ứng ATTT "trước khi đưa vào sử dụng" theo QĐ 742/QĐ-BTTTT (22/4/2022); phần mềm nền được vá thường xuyên.
  - CV 365 mục III.1.3 c: đáp ứng TT 39/2017/TT-BTTTT (danh mục tiêu chuẩn kỹ thuật). Đây là cách CV 365 hiện thực hóa TT 13 Đ2 k3.
  - CV 365 mục III.4 a, b: tối thiểu **cấp độ 2** theo NĐ 85/2016 và TT 12/2022.
  - CV 365 mục III.5: sẵn sàng IPv6.
  - CV 365 mục III.6: bảo vệ dữ liệu cá nhân theo NĐ 13/2023.
- **Mức**: BẮT BUỘC? (các văn bản dẫn chiếu đã hoặc đang bị thay; xem mục 6).
- **Phần mềm phải**:
  - Có báo cáo kiểm thử ATTT trước khi go-live.
  - Chạy được trên IPv6.
  - Tuân thủ chuẩn trao đổi (XML, JSON, UTF-8…).
- **Ghi chú**: cấp độ hệ thống thông tin nay theo NĐ 331/2026 (cụm K9). Bảo vệ dữ liệu cá nhân nay theo Luật 91/2025 và NĐ 356/2025 (cụm K8).

### EMR-R28 — Đơn thuốc trong HSBA và kê đơn điện tử
- **Căn cứ**:
  - TT 26/2025 Đ5 k1 b: có HSBA ngoại trú thì chỉ định vào HSBA và kê đơn phù hợp.
  - TT 26 Đ9 k1: đơn "H" 3 bản, 1 bản lưu trong HSBA.
  - TT 26 Đ10: đơn điện tử được "lập, hiển thị, ký số, chia sẻ, lưu trữ bằng phương thức điện tử", có giá trị như đơn giấy.
  - TT 26 Đ13 k3: BV kê đơn điện tử trước 01/10/2025; cơ sở khác trước 01/01/2026.
- **Mức**: BẮT BUỘC (chi tiết ở cụm K3).
- **Phần mềm phải**: đơn thuốc trong EMR là tài liệu đã ký số, liên kết với y lệnh trong HSBA và lưu cùng thời hạn với HSBA.

**Tổng: 28 yêu cầu.** BẮT BUỘC 19 (R01, R03, R04, R05, R06, R07, R08, R10, R13, R14, R15, R16, R17, R21, R22, R23, R24, R25, R28). BẮT BUỘC? 9 (R02, R09, R11 phần chi tiết, R12, R18, R19, R20, R26, R27). Một số yêu cầu có phần con ở mức NÊN: bản sao lưu thứ hai (R21), quy trình hủy theo NĐ 113 (R24), mẫu quy chế (R25).

---

## 3. Pattern thiết kế

**P1. Máy trạng thái HSBA gắn với chính sách truy cập** (R10, R15, R17, R22, R24)
- Trạng thái: `DRAFT → ACTIVE` (đang điều trị, Đ69 k3) `→ CLOSED` (ra viện hoặc kết thúc đợt; chờ hoàn thiện, ký đủ) `→ ARCHIVED` (đã chuyển lưu trữ, Đ69 k4; nội dung bất biến; bắt đầu tính thời hạn lưu) `→ DESTROYED` (chỉ còn metadata của việc hủy).
- Dữ liệu:
  - `medical_record(id, patient_id, record_type /*01/BV1…29*/, form_version, medium ENUM('electronic','paper','hybrid'), status, opened_at, closed_at, archived_at, retention_class_id, retention_until DATE, legal_hold BOOL)`.
  - Ràng buộc: trigger chặn UPDATE nội dung khi `status IN ('ARCHIVED','DESTROYED')`.
  - Chỉ mục: `(patient_id, status)`, `(retention_until) WHERE status='ARCHIVED'`.
- Đánh đổi: hồ sơ cần bổ sung sau khi đã lưu trữ (ví dụ kết quả giải phẫu bệnh về muộn) phải có luồng "phụ lục bổ sung" có ký, không mở lại hồ sơ.

**P2. Ghi chép append-only kèm đính chính** (R04, R10)
- Dữ liệu: `clinical_entry(id, record_id, entry_type, payload JSONB, author_id, author_role, recorded_at DEFAULT now(), clinical_time, supersedes_id NULL, amend_reason, status ENUM('active','superseded','cancelled'))`.
- Không cho DELETE; UPDATE chỉ được đổi `status` sang `superseded` hoặc `cancelled`, kèm lý do và log.
- Giao diện mặc định hiện bản mới nhất, có nút "lịch sử phiên bản".
- Đánh đổi: tốn dung lượng, query phức tạp hơn. Bù lại chứng minh được không "tẩy xóa".

**P3. Phong bì chữ ký (signature envelope)** (R06, R07, R08, R09)
- Khi ký: render tài liệu (PDF/A hoặc JSON chuẩn hóa) → hash SHA-256 → ký.
- Dữ liệu:
  - `signed_document(id, record_id, doc_type, version, content_hash, storage_uri, created_at)`.
  - `signature(id, signed_document_id, signer_type ENUM('staff','patient','representative','organization'), signer_ref, signer_title, method ENUM('pki_token','pki_remote','hsm_org','biometric','otp','other'), cert_serial, issuer, cert_status_at_sign JSONB /*kết quả OCSP/CRL ở cả 2 tầng theo NĐ 23 Đ15–16*/, tsa_token, evidence_uri, signed_at)`.
  - Ràng buộc: `UNIQUE(signed_document_id, signer_ref, role)`.
- Nội dung đã có chữ ký thì bất biến. Muốn sửa phải tạo `version+1` và ký lại.
- Đánh đổi:
  - Ký từ xa (CA giữ khóa, NĐ 23 Đ37 k4) thuận tiện nhưng phụ thuộc mạng và CA.
  - Ký bằng HSM nội bộ cho chữ ký tổ chức nhanh hơn, nhưng cơ sở phải tự quản lý khóa.

**P4. Audit log chống giả mạo** (R12, R10)
- Bảng log riêng (hoặc DB riêng) chỉ cho INSERT: `audit_event(seq BIGSERIAL, ts, actor_id, actor_role, action ENUM('view','create','update','cancel','restore','print','export','sign','share','destroy'), object_type, object_id, patient_id, purpose, ip, device, result, prev_hash, hash)`.
- Chuỗi hash, neo định kỳ bằng ký số hoặc dấu thời gian.
- Quyền quản trị log tách khỏi quản trị ứng dụng.
- Chỉ mục: `(patient_id, ts)` để trả lời "ai đã xem hồ sơ của tôi".
- Đánh đổi: khối lượng lớn vì có log `view`. Cần phân vùng theo tháng và đưa lên cold storage, nhưng vẫn giữ ít nhất bằng thời hạn HSBA (suy luận).

**P5. Truy cập theo vai trò, quan hệ điều trị và thời gian; cấp quyền tạm** (R11, R15)
- Kiểm tra theo thứ tự: RBAC → ABAC (`care_team` của người bệnh, khoa, trạng thái HSBA) → khung giờ (`access_window` theo người dùng hoặc vai trò, CV 365 g).
- "Break-glass" cho cấp cứu: bắt buộc nhập lý do và báo hậu kiểm.
- Người bên ngoài (thanh tra, BHXH, luật sư): `access_grant(grantee, scope, purpose, approved_by, valid_from, valid_to, can_copy BOOL)`.
- Quyền đọc và quyền sao chép tách riêng (Đ69 k3 a).

**P6. Quy trình yêu cầu của người bệnh** (R14)
- `patient_request(id, patient_id, requester_id, requester_relation ENUM(theo Đ8 k2 a–đ), written_request_uri, scope ENUM('full','summary'), status, fulfilled_at, delivered_doc_id)`.
- Luật định `scope`: người bệnh và đại diện theo Đ8 k2 c, d được `full`; đại diện theo Đ8 k2 a, d chỉ `summary`.
- Đầu ra: PDF có ký hiệu chuyển đổi (P7) và bản tóm tắt CV-01 có ký số của cơ sở.

**P7. Dấu chuyển đổi giấy ↔ điện tử** (R13, R16)
- Dịch vụ `conversion_stamp(direction, system_name, owner_name, lookup_code, converted_by, converted_at)` sinh footer, watermark và QR.
- Bản scan nhập vào: lưu `scan_batch(id, source_record_id, page_count, operator, converted_at, org_signature_id)`.
- Đánh đổi: QR chứa mã tra cứu cần cổng xác minh công khai. Cổng này phải chống dò mã (rate limit, mã ngẫu nhiên đủ dài).

**P8. Động cơ thời hạn lưu trữ** (R22, R24)
- Bảng tham chiếu `retention_class(code, legal_basis 'TT33/2025 PL mục 44', years, permanent BOOL)`.
- Ngày hết hạn được tính lại khi có sự kiện (tử vong, sự cố y khoa → vĩnh viễn với hồ sơ sự cố). Cờ `legal_hold` chặn hủy.
- Job hằng năm lập "danh mục dự kiến hủy" và chờ phê duyệt. Khi hủy thì xóa cả bản sao lưu (cần thiết kế backup cho phép xóa có chọn lọc, hoặc mã hóa từng hồ sơ bằng khóa riêng rồi hủy khóa — crypto-shredding).
- Đánh đổi: crypto-shredding giải được bài toán xóa trong backup, nhưng tăng độ phức tạp quản lý khóa.

**P9. Lớp xuất liên thông theo CV 365** (R18, R05, R19)
- Mapper từ mô hình nội bộ sang `HoSoBenhAn` (JSON/XML), kiểm tra hợp lệ bằng schema tự dựng từ bảng phụ lục (tên trường, kiểu, độ dài).
- Đính kèm PDF đã ký vì schema không có chữ ký.
- Bản đồ mã danh mục BYT có kiểm tra phiên bản.

**P10. Sao lưu và kế hoạch rời nhà cung cấp** (R21, R26)
- 3-2-1: bản tại cơ sở (bắt buộc theo CV 365) + bản ở nơi khác hoặc nhà cung cấp lưu trữ (khuyến nghị) + bản offline hoặc immutable.
- Diễn tập khôi phục định kỳ và lưu biên bản.
- Hợp đồng SaaS có điều khoản bàn giao (dump, đặc tả schema, tài liệu đã ký, log) và biên bản hủy dữ liệu.

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| EMR-A01 | R01 | Xem Quyết định triển khai/công bố HSBA điện tử của cơ sở và việc có tên trên benhandientu.moh.gov.vn. Đối chiếu ngày go-live với hạn 30/09/2025 (BV) hoặc 31/12/2026 | QĐ công bố, biên bản tự đánh giá TT 13 và CV 365, ảnh chụp cổng | Bắt buộc |
| EMR-A02 | R02 | Với phòng khám: liệt kê loại lượt khám. Có mở HSBA ngoại trú điện tử không (mẫu 15/16/19/BV1, ngoại trú PHCN)? Lượt chỉ kê đơn có phiếu khám ký và đơn điện tử không? | Danh sách loại bệnh án đang dùng, mẫu in | Bắt buộc? |
| EMR-A03 | R03 | Chọn ngẫu nhiên 10 HSBA mỗi loại, so từng trường với mẫu PL XXVIII/XXIX TT 32. Tìm mẫu cũ theo QĐ 4069/2001 | Bảng so khớp trường, ảnh màn hình | Bắt buộc |
| EMR-A04 | R04 | SQL: `SELECT count(*) FROM clinical_entry WHERE author_id IS NULL OR recorded_at IS NULL`. Kiểm tra có tài khoản dùng chung không. In tóm tắt HSBA hoặc giấy chuyển tuyến để tìm chữ viết tắt | Kết quả truy vấn, danh sách tài khoản, bản in | Bắt buộc |
| EMR-A05 | R05 | Tỷ lệ người bệnh có số định danh cá nhân; số hồ sơ trùng (cùng số định danh, nhiều mã); có quy trình gộp hồ sơ và log không | Truy vấn thống kê, log merge | Bắt buộc |
| EMR-A06 | R06, R09 | Mở phiếu cam kết hoặc đồng ý phẫu thuật: người bệnh ký bằng phương thức gì? Có gói bằng chứng (hash, OTP log, sinh trắc) không? Chữ ký nhân viên y tế là chữ ký số hay ảnh chữ ký? | File PDF đã ký (kiểm bằng Adobe hoặc công cụ kiểm tra), bản ghi bằng chứng OTP | Bắt buộc |
| EMR-A07 | R07 | Ký thử bằng chứng thư đã thu hồi hoặc hết hạn: phần mềm có chặn không? Có lưu kết quả OCSP/CRL không? Có kế hoạch nâng cấp theo NĐ 23 Đ17 trước 10/04/2027 không? | Video hoặc ảnh thử nghiệm, tài liệu nâng cấp | Bắt buộc |
| EMR-A08 | R08 | Quy chế ký số của BV công: còn dẫn TT 41/2017 hoặc NĐ 130/2018 không (sau 15/11/2026 là sai căn cứ)? Giấy ra viện, chuyển tuyến có chữ ký số của tổ chức hoặc người có thẩm quyền kèm chức danh không? | Quy chế, file đã ký | Bắt buộc |
| EMR-A09 | R10 | Sửa một mục đã lưu: bản cũ còn không? Có lý do không? Sửa nội dung đã ký: có bị chặn không? Kiểm tra DB có quyền DELETE hoặc UPDATE trực tiếp trên bảng lâm sàng không | Ảnh lịch sử phiên bản, cấu hình quyền DB | Bắt buộc |
| EMR-A10 | R11 | Đăng nhập bằng vai trò điều dưỡng khoa A: xem được HSBA khoa B không? Có cấu hình khung giờ truy cập không? Có chính sách khóa tài khoản không? | Ma trận phân quyền, ảnh cấu hình | Bắt buộc? |
| EMR-A11 | R12 | Xem một HSBA rồi tra log: có bản ghi `view` không? Admin có xóa hoặc sửa được log không? | Trích log, thử xóa | Bắt buộc? |
| EMR-A12 | R13 | In một phiếu: footer có ký hiệu "chuyển đổi từ thông điệp dữ liệu", tên hệ thống, chủ quản, mã tra cứu hoặc QR, thời gian, người in không? Xuất PDF đúng mẫu không? | Bản in, file PDF | Bắt buộc |
| EMR-A13 | R14 | Diễn tập yêu cầu của người bệnh: có phiếu yêu cầu bằng văn bản không? Người đại diện theo Đ8 k2 a có bị giới hạn chỉ nhận tóm tắt không? Thời gian đáp ứng? | Hồ sơ yêu cầu mẫu, bản tóm tắt CV-01 | Bắt buộc |
| EMR-A14 | R15 | Sinh viên hoặc học viên: xem được nhưng không xuất hay in nếu chưa được phê duyệt? Có cơ chế cấp quyền tạm cho thanh tra hoặc BHXH, có hạn và có log không? | Ảnh thử nghiệm, bảng `access_grant` | Bắt buộc |
| EMR-A15 | R16 | Lấy 5 bản scan bệnh án cũ: có ký hiệu chuyển đổi, thời gian, người chuyển đổi, chữ ký số của cơ sở không? Có QĐ của Thủ trưởng về chuyển đổi không? Hệ thống đã rà soát theo NĐ 137 Đ23 (hạn khoảng 23/10/2026) chưa? | File scan, QĐ, biên bản rà soát | Bắt buộc |
| EMR-A16 | R17 | Có trường hình thức HSBA (giấy, điện tử, lai) không? Báo cáo HSBA giấy còn tồn | Truy vấn | Bắt buộc |
| EMR-A17 | R18 | Xuất 1 HSBA ra JSON và XML. Kiểm tra theo bảng phụ lục CV 365 (11 nhóm, tên trường, kiểu, độ dài) | File xuất, kết quả validate | Bắt buộc? |
| EMR-A18 | R19 | Lấy mẫu mã ICD, mã dịch vụ, mã thuốc: có theo danh mục BYT không? | Bảng mapping | Bắt buộc? |
| EMR-A19 | R20 | Tắt hoặc ngắt HIS hay PACS: kho EMR có còn xem và xuất được HSBA đã ký không? | Kết quả thử nghiệm | Bắt buộc? |
| EMR-A20 | R21 | Xem lịch và báo cáo sao lưu 3 tháng gần nhất; biên bản diễn tập khôi phục; cấu hình mã hóa at-rest và TLS | Báo cáo, biên bản | Bắt buộc |
| EMR-A21 | R22 | SQL: phân bố `retention_class`. HSBA tử vong có 30 năm không? Tâm thần, TNLĐ, TNGT có 20 năm không? Cách tính `retention_until`. Đơn thuốc, ảnh CĐHA, log được gán thời hạn nào? | Truy vấn, tài liệu chính sách lưu trữ | Bắt buộc |
| EMR-A22 | R23 | Lấy 1 tài liệu đã lưu trữ: có metadata (người lập, người ký, hash, định dạng, thời hạn) không? Hash có khớp không? Định dạng có ổn định lâu dài (PDF/A) không? | Bản ghi metadata, kết quả kiểm hash | Bắt buộc |
| EMR-A23 | R24 | Có quy trình hủy không? Thử hủy hồ sơ chưa hết hạn hoặc đang `legal_hold`: có bị chặn không? Hủy có xóa cả backup và bản scan không? Có biên bản và danh mục hủy không? | Quy trình, biên bản | Bắt buộc |
| EMR-A24 | R25 | Có quy chế HSBA điện tử (gồm phần ký và xác nhận theo TT 13 Đ3) không? Cấu hình phần mềm có khớp quy chế không? | Quy chế đã ban hành, đối chiếu cấu hình | Bắt buộc |
| EMR-A25 | R26 | Hợp đồng thuê hoặc SaaS: dữ liệu thuộc cơ sở; có điều khoản bàn giao kèm đặc tả và hủy an toàn; DC và backup đặt tại Việt Nam; có NDA | Hợp đồng, chứng chỉ DC | Bắt buộc? |
| EMR-A26 | R27 | Báo cáo kiểm thử ATTT trước go-live; hồ sơ cấp độ hệ thống thông tin (xem K9); khả năng chạy IPv6 | Báo cáo, hồ sơ | Bắt buộc? |
| EMR-A27 | R28 | Đơn thuốc trong HSBA có ký số không? Có liên kết y lệnh không? Đơn "H" có bản lưu trong HSBA không? | File đơn đã ký | Bắt buộc |

---

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái | Sự kiện | Ai phải làm | Nguồn |
|---|---|---|---|---|
| 01/01/2024 | Đã qua | Luật KCB 2023 và TT 32/2023 có HL. Mẫu HSBA mới thay QĐ 4069/2001 | Mọi cơ sở, vendor | gốc |
| 10/04/2025 | Đã qua | NĐ 23/2025 có HL; NĐ 130/2018 hết HL | Người ký số, vendor | gốc-OCR |
| 06/06/2025 | Đã qua | TT 13 ban hành; **TT 46/2018 và Mục VIII PL I cùng tiêu chí EMR của TT 54/2017 hết HL từ ngày này** (TT 13 Đ4 k3); CV 365 ban hành | — | gốc-OCR, gốc |
| 01/07/2025 | Đã qua | TT 33/2025 thay TT 53/2017; Luật Lưu trữ 2024 có HL; TT 26/2025 có HL | Mọi cơ sở | gốc |
| 21/07/2025 | Đã qua | TT 13 có HL (mốc chuyển tiếp HSBA giấy ở Đ5); NĐ 113/2025 có HL | Mọi cơ sở | gốc-OCR |
| 30/09/2025 | Đã qua | **BV hoàn thành HSBA điện tử** (TT 13 Đ4 k2 a) | BV công và tư | gốc-OCR |
| 01/01/2026 | Đã qua | Cơ sở không phải BV phải kê đơn điện tử (TT 26 Đ13 k3 b) | PK, TTYT | gốc |
| 15/05/2026 | Đã qua | NĐ 90/2026 (chế tài HSBA điện tử Đ39 k2 c, d) có HL | Mọi cơ sở | gốc-OCR |
| 15/08/2026 | Đã qua | TT 25/2026 có HL (không sửa Chương X TT 32) | — | gốc |
| **~23/10/2026** | Sắp tới | Hết 24 tháng rà soát hệ thống chuyển đổi giấy ↔ điện tử theo NĐ 137 Đ4 k2, Đ5 k3 (NĐ 137 Đ23) | Chủ quản hệ thống có số hóa hoặc in chuyển đổi HSBA | gốc-OCR (cách tính là suy luận) |
| **15/11/2026** | Sắp tới | TT 41/2017/TT-BTTTT bị bãi bỏ (TT 59/2026 BKHCN) | BV công: sửa quy chế ký số sang Luật GDĐT và NĐ 23 | gốc |
| **31/12/2026** | Sắp tới | **Cơ sở KCB khác có điều trị nội trú, ban ngày, ngoại trú hoàn thành HSBA điện tử** (TT 13 Đ4 k2 b). Mục tiêu 100% cơ sở theo QĐ 586 và CT 04 | PK, TTYT, cơ sở tư; vendor CIS | gốc-OCR / thứ cấp |
| **01/01/2027** | Sắp tới | **BV công và tư không dùng HSBA giấy**: chỉ là **mục tiêu kế hoạch** của QĐ 586, nhắc lại ở CT 04 (thứ cấp). Không có trong TT 13. Không có chế tài riêng cho việc "còn dùng giấy". Cùng ngày: Luật KCB Đ120 k5 a (hạ tầng CNTT kết nối HTTT quản lý KCB là điều kiện cấp GPHĐ mới) | BV; cơ sở xin GPHĐ mới | thứ cấp / gốc |
| 01/03/2027 | Sắp tới | Luật 20/2026/QH16 (sửa Luật GDĐT) có HL. **Chưa đọc phần sửa**, có thể ảnh hưởng Đ22–23 | Tất cả | gốc-meta (inventory) |
| **10/04/2027** | Sắp tới | Hết 02 năm để phần mềm tích hợp ký số và kiểm tra chữ ký nâng cấp theo NĐ 23 Đ17 (Đ47 k6, k7) | Vendor, chủ quản EMR | gốc-OCR (cách tính là suy luận) |
| 01/01/2029 | Xa | Cơ sở có GPHĐ trước 2027 phải đáp ứng hạ tầng CNTT (Luật KCB Đ120 k5 b) | Mọi cơ sở | gốc |
| 2030 | Xa | 100% cơ sở KCB triển khai HSBA điện tử, không dùng bệnh án giấy (QĐ 965) | Mọi cơ sở | thứ cấp (NHIC, luatvietnam) |

**Quan hệ QĐ 586, QĐ 965 và mốc 01/01/2027 (giải quyết MT-23)**:
- (1) Cả hai QĐ đều là **quyết định phê duyệt kế hoạch** của Bộ trưởng BYT, không phải VBQPPL. Chúng chỉ đạo Sở Y tế và đơn vị trực thuộc, không tự tạo chế tài với cơ sở tư (suy luận về bản chất văn bản).
- (2) QĐ 586 (09/03/2026) là kế hoạch **năm 2026**: 100% cơ sở hoàn thành trước 31/12/2026, BV dừng giấy từ 01/01/2027. QĐ 965 (10/04/2026) là kế hoạch **2026–2030**: 100% cơ sở không dùng giấy vào 2030. Không thấy nguồn nào nói QĐ 965 thay hay bãi bỏ QĐ 586. Hai văn bản là ngắn hạn và trung hạn song song (suy luận).
- (3) Nghĩa vụ **có chế tài** là TT 13 Đ4 k2 (triển khai và hoàn thành) cộng NĐ 90 Đ39 k2 c, d (không có quy chế; không đáp ứng yêu cầu CNTT). NĐ 90 không có hành vi "còn dùng HSBA giấy". Luật KCB Đ69 k1 vẫn cho giấy và điện tử giá trị như nhau.
- (4) Thực tế quản lý: dù không có chế tài trực tiếp, BV công sẽ bị Sở Y tế và BYT kiểm tra theo QĐ 586 và CT 04. Bài của TTYQG ngày 18/08/2026 dẫn QĐ 965 (mốc 2030) và CT 04, không nhắc 01/01/2027.

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuỗi thay thế**
- TT 46/2018/TT-BYT (HSBA điện tử) → TT 13/2025. **Hết HL từ 06/06/2025** (ngày ban hành TT 13), không phải 21/07/2025. Câu chữ Đ4 k3: "hết hiệu lực kể từ ngày Thông tư này được ban hành" (gốc-OCR có dấu).
- TT 54/2017 Mục VIII PL I và các tiêu chí EMR → bãi bỏ cùng ngày. Phần còn lại vẫn HL; chưa thấy thông tư thay thế.
- Thủ tục "công nhận/công bố" HSBA điện tử theo TT 46 → không có thủ tục thay. Thực tiễn: tự thẩm định nội bộ, QĐ công bố, đăng cổng benhandientu.
- TT 53/2017 (thời hạn bảo quản) → TT 33/2025 (01/07/2025).
- QĐ 4069/2001, QĐ 1941/2019, QĐ 3730/2021 (mẫu HSBA) → TT 32/2023 PL XXVIII–XXIX. Mẫu tóm tắt PL 4 TT 18/2022 → CV-01 TT 32.
- NĐ 130/2018 và NĐ 48/2024 (chữ ký số) → NĐ 23/2025 (10/04/2025).
- TT 41/2017/TT-BTTTT (chữ ký số trong CQNN) → bãi bỏ từ 15/11/2026 (TT 59/2026 BKHCN). Không có thông tư thay; dùng Luật GDĐT 2023 và NĐ 23/2025.
- NĐ 117/2020 (xử phạt y tế) → NĐ 90/2026 (15/05/2026).
- Luật Lưu trữ 2011 → Luật Lưu trữ 2024 (01/07/2025).
- NĐ 13/2023 (CV 365 mục III.6) → Luật 91/2025 và NĐ 356/2025 (01/01/2026), thuộc cụm K8.
- NĐ 85/2016 và TT 12/2022 (CV 365 mục III.4) → NĐ 331/2026, thuộc cụm K9 (theo inventory, NĐ 331 không có điều bãi bỏ NĐ 85).

**Bẫy trích dẫn**
1. **TT 13 rất ngắn.** Mọi yêu cầu chức năng (phân quyền, ghi vết, sao lưu, XML/JSON, cloud tại Việt Nam, bàn giao dữ liệu) nằm ở **CV 365**. Đây là công văn hướng dẫn kỹ thuật, không phải VBQPPL. Khi trích, ghi "CV 365 PL mục III.x", đừng gán cho TT 13.
2. **TT 26/2025 Đ11** dẫn TT 53/2017 cho việc lưu đơn, nhưng TT 53 đã hết HL cùng ngày TT 26 có HL. Áp TT 33 theo TT 26 Đ14. Phụ lục TT 33 **không có dòng "đơn thuốc"** nên phải áp nhóm tương đương (TT 33 Đ1 k2 b).
3. **TT 33 không có dòng** cho phim/ảnh CĐHA, kết quả xét nghiệm rời và audit log. Đừng trích "TT 33 quy định lưu log X năm".
4. **Thời hạn tính theo năm** "kể từ năm kết thúc công việc" (Luật Lưu trữ Đ15 k3), không tính từ ngày ra viện.
5. **"Chữ ký điện tử" ≠ "chữ ký số."** Chỉ chữ ký số và chữ ký điện tử chuyên dùng bảo đảm an toàn mới tương đương chữ ký tay (Luật GDĐT Đ23 k2). Ảnh chữ ký dán vào phiếu không đủ.
6. **TT 13 Đ4 k2 b** viết "nội trú, ban ngày **và** ngoại trú". Có trang tóm tắt chép thành "hoặc". Nghĩa thực tế: có bất kỳ loại nào (suy luận).
7. **CV 365 vẫn dẫn** NĐ 85/2016, TT 12/2022, NĐ 13/2023, QĐ 742/QĐ-BTTTT, TT 39/2017/TT-BTTTT. Ba văn bản đầu đã bị thay. Trạng thái hai văn bản cuối: chưa xác minh (đều dựa trên Luật CNTT 2006).
8. **Quy chế mẫu của cơ sở** (ví dụ QĐ 162/QĐ-TTYT Mỹ Tú, 29/9/2025) còn dẫn NĐ 130/2018 đã hết HL và ghi sai số hiệu "Luật Giao dịch điện tử 20/2025/QH15". Đừng sao chép căn cứ từ quy chế mẫu.
9. **Cổng benhandientu.moh.gov.vn** mục "Văn bản pháp lý có hiệu lực" vẫn liệt kê TT 46/2018 (kiểm tra 05/10/2026). Không dùng cổng này để xác định hiệu lực.
10. **Mốc 01/01/2027 "BV dừng bệnh án giấy"** đến từ kế hoạch QĐ 586 và CT 04 (thứ cấp), **không có trong TT 13**. Đừng gọi là "hạn chót luật định".
11. **Luật KCB Đ69 k4 d và đ** cùng dẫn "điểm d khoản 2 Điều 8". Trích đúng nguyên văn VBHN, đừng tự sửa.
12. **Schema CV 365 không có trường chữ ký số** (chỉ `chuky_hoten`). Trường địa chỉ còn cấp quận/huyện.
13. **Mức phạt NĐ 90** trong Chương II là mức cho cá nhân; tổ chức gấp đôi (Đ4 k5). Cơ sở KCB thường là tổ chức, nên Đ39 k2 c, d là **6–10 triệu**, không phải 3–5 triệu.

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Bản gốc QĐ 586/QĐ-BYT, QĐ 965/QĐ-BYT, CT 04/CT-BYT** chưa tìm được trên nguồn nhà nước. Các link moh.gov.vn trong kết quả tìm kiếm đều trả 404. Nội dung về mốc 31/12/2026, 01/01/2027, 2030 và người ký chỉ ở mức thứ cấp (luatvietnam, SYT Đồng Nai, NHIC). Cần bản gốc để xác nhận câu chữ và chủ thể của mốc 01/01/2027.
2. **Phòng khám chỉ khám và kê đơn (MT-25)**: cần **hỏi Cục KHCN&ĐT (K2ĐT) hoặc Cục QLKCB**. Câu hỏi: lượt khám ngoại trú chỉ kê đơn, không mở HSBA ngoại trú (TT 26 Đ5 k1 a), có thuộc "điều trị ngoại trú" theo Luật KCB Đ76 và TT 13 Đ4 k2 b không? Phòng khám như vậy có bị phạt theo NĐ 90 Đ39 k2 d sau 31/12/2026 không?
3. **Tiêu chí "hoàn thành" HSBA điện tử** và quy trình công bố: không có trong VBQPPL. Cổng benhandientu có "Hồ sơ thẩm định đủ điều kiện công bố mẫu", nhưng chưa đọc được nội dung (trang chỉ có danh mục).
4. **Thời hạn lưu** đơn thuốc ngoại trú độc lập, tài liệu thuốc gây nghiện, hướng thần, tiền chất (TT 26 Đ11 k2 dẫn TT 20/2017, hiện trạng chưa kiểm); phim và ảnh DICOM (cụm K7); audit log. TT 33 không quy định. Cần BYT (Văn phòng Bộ, cơ quan chủ trì TT 33) hướng dẫn, hoặc cơ sở tự quyết theo Đ1 k2 b và Luật Lưu trữ Đ15 k6.
5. **Thời hạn TT 53/2017** cho HSBA lập trước 01/07/2025 (TT 33 Đ2 k3 giữ thời hạn cũ): chưa đọc TT 53 nên chưa liệt kê được.
6. **Luật Lưu trữ với cơ sở tư nhân**: Đ3 k5 cho tổ chức tư tự quyết áp dụng. Nhưng Luật KCB Đ69 k2 buộc HSBA lưu "theo quy định của pháp luật về lưu trữ". Cần luật sư xác định phần nào (thời hạn, thủ tục hủy, yêu cầu tài liệu số) bắt buộc với BV và PK tư.
7. **SaaS EMR có phải "kinh doanh dịch vụ lưu trữ"** theo Luật Lưu trữ Đ53 và NĐ 113 Đ37 (cần giấy chứng nhận, nhân sự có chứng chỉ hành nghề lưu trữ) không? Cần luật sư.
8. **Luật 20/2026/QH16** (sửa Luật GDĐT, HL 01/03/2027): chưa đọc. Có thể thay đổi Đ22–23 (phân loại chữ ký, hình thức xác nhận khác), ảnh hưởng TT 13 Đ3 k3.
9. **Văn bản kỹ thuật** cho phần mềm ký số theo NĐ 23 Đ17 k4 (sau khi BTTTT sáp nhập vào BKHCN) và trạng thái TT 39/2017/TT-BTTTT, QĐ 742/QĐ-BTTTT: chưa xác minh.
10. **Giá trị pháp lý của xác nhận bằng OTP hoặc sinh trắc** của người bệnh cho các văn bản luật yêu cầu "bằng văn bản" (đồng ý phẫu thuật, cam kết từ chối điều trị): cần luật sư đánh giá rủi ro chứng cứ (Luật GDĐT Đ11, Đ23). Xử lý dữ liệu sinh trắc theo Luật BVDLCN thuộc cụm K8.
11. **Thời hạn hoàn thiện HSBA** sau ra viện, quy tắc "khóa" HSBA: không thấy trong Luật KCB, TT 32, TT 13 và CV 365. Kiểm tra thêm NĐ 96/2023 và các quy chế chuyên môn của BYT.
12. **Ngày HL của NĐ 137/2024** dùng để tính hạn 24 tháng ở Đ23: lấy 23/10/2024 theo inventory (gốc-meta, "từ ngày ký"). Nên đối chiếu ngày ký trên bản gốc.
13. **Luật KCB Đ69 k4 d và đ** cùng dẫn "điểm d khoản 2 Điều 8": cần luật sư đọc bản gốc 2023 để biết có lỗi kỹ thuật lập pháp không và nên áp dụng thế nào.
