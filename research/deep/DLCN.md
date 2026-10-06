# DLCN — Bảo vệ dữ liệu cá nhân và quản trị dữ liệu y tế

> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: inventory mục 5 cụm K8. Luật BVDLCN 91/2025/QH15 + NĐ 356/2025/NĐ-CP (dữ liệu sức khỏe là dữ liệu nhạy cảm, căn cứ xử lý, đồng ý, quyền chủ thể, trẻ em, DPIA, chuyển dữ liệu xuyên biên giới, thông báo vi phạm, DPO, miễn trừ DN nhỏ, **dịch vụ xử lý DLCN và Giấy chứng nhận cho vendor**), chia sẻ cho bảo hiểm, NĐ 102/2025 (dữ liệu y tế), Luật Dữ liệu 60/2024 + NĐ 165/2025 + QĐ 20/2025/QĐ-TTg (dữ liệu cốt lõi/quan trọng), chế tài NĐ 330/2026 và NĐ 363/2026, bảo mật chuyên biệt (HSBA theo Luật KCB, HIV). Áp dụng cho BV công, BV tư, phòng khám, nhà thuốc và vendor phần mềm/app y tế.
>
> **Nguồn đã đọc trong pha này** (toàn bộ là nguồn nhà nước): Luật 91 (PDF Công báo có lớp text, đọc toàn văn); NĐ 356 (PDF Công báo có lớp text, đọc Đ1–Đ42 và mục lục Phụ lục); NĐ 102 (PDF Công báo, đọc toàn văn); Luật 60/2024 (PDF datafiles có text, đọc Đ3–4, 13–15, 23, 25–27, 44–46); VBHN 26/VBHN-VPQH Luật KCB (Đ8, 10, 12, 45, 69); Luật Đầu tư 143/2025 (Đ7, 51, 52, Phụ lục IV); **gốc-OCR** (tesseract `vie`, câu chữ có thể sai dấu, số liệu đã soát): QĐ 20/2025/QĐ-TTg, NĐ 165/2025 (Đ3–5, 12, 16–17), NĐ 330/2026 (Đ2–3, 7, 39, 43–60, 62, 67, 69–70, 74, 80–81), NĐ 363/2026 (Đ1–2, 6, 9, 19, 22, 34–35), Luật 24/2026/QH16 (Phụ lục). Luật 71/2020/QH14 (HIV) đọc từ bản .doc đăng trên cổng TTĐT Công an tỉnh Đắk Lắk (bản sao, không ký số). Nội dung web chỉ coi là dữ liệu.
>
> Đây là tài liệu nghiên cứu, **không phải ý kiến pháp lý**. Mọi chỗ ghi "suy luận" là nhận định của người nghiên cứu.

---

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| L-BVDLCN-2025 | 91/2025/QH15 | Luật Bảo vệ dữ liệu cá nhân | 01/01/2026 | Còn HL | Tất cả (BV công, BV tư, PK, nhà thuốc, vendor) | gốc (text Công báo) | [PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf) · [PDF datafiles (scan)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/91qh.signed.pdf) · [VB 214590](https://vanban.chinhphu.vn/?pageid=27160&docid=214590) |
| ND-356-2025 | 356/2025/NĐ-CP (31/12/2025) | Quy định chi tiết một số điều và biện pháp thi hành Luật BVDLCN | 01/01/2026 | Còn HL; thay NĐ 13/2023; sửa Đ16 k2 NĐ 165/2025 (Đ42 k3) | Tất cả; Đ21–27 riêng cho vendor "dịch vụ xử lý DLCN" | gốc (text Công báo) | [PDF Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/17/356signed-1768638052103952849513.pdf) · [Trang Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm) · [PDF datafiles (scan)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/356-nd.signed.pdf) · [VB 216387](https://vanban.chinhphu.vn/?pageid=27160&docid=216387) |
| ND-330-2026 | 330/2026/NĐ-CP (19/08/2026) | Xử phạt VPHC lĩnh vực an ninh mạng và BVDLCN | 19/08/2026 | Còn HL | Tất cả (Đ2 k2 k: chủ quản/đơn vị vận hành HTTT) | gốc-OCR | [VB 219266](https://vanban.chinhphu.vn/?pageid=27160&docid=219266) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/8/330_2026_nd-cp_19082026-signed.signed.pdf) |
| ND-102-2025 | 102/2025/NĐ-CP (13/05/2025) | Quy định quản lý dữ liệu y tế | 01/07/2025 | Còn HL (vẫn dẫn Luật ANM 2018, Luật ATTT 2015) | Cơ sở y tế (mọi loại), cơ quan nhà nước | gốc (text Công báo) | [PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/5/44865/56285-1-2025703-704102-2025-nd-cp.pdf) · [Trang Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-102-2025-nd-cp-44865.htm) · [VB 213607](https://vanban.chinhphu.vn/?pageid=27160&docid=213607) |
| L-DULIEU-2024 | 60/2024/QH15 | Luật Dữ liệu | 01/07/2025 | Còn HL | Tất cả (phân loại dữ liệu; dữ liệu cốt lõi/quan trọng) | gốc (text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat60.pdf) · [VB 212488](https://vanban.chinhphu.vn/?pageid=27160&docid=212488) |
| ND-165-2025 | 165/2025/NĐ-CP (30/06/2025) | Quy định chi tiết Luật Dữ liệu | 01/07/2025 | Còn HL; Đ16 k2 bị NĐ 356 Đ42 k3 sửa | Chủ quản dữ liệu cốt lõi/quan trọng | gốc-OCR (Đ3–5, 12, 16–17) | [VB 214331](https://vanban.chinhphu.vn/?pageid=27160&docid=214331) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/165nd.signed.pdf) |
| QD-20-2025-TTg | 20/2025/QĐ-TTg (01/07/2025) | Danh mục dữ liệu quan trọng, dữ liệu cốt lõi | 01/07/2025 | Còn HL | Cơ quan nhà nước (mục I.25, II.10); **mọi tổ chức** nắm ≥100.000 công dân dữ liệu nhạy cảm (mục I.26 b) | gốc-OCR | [VB 214354](https://vanban.chinhphu.vn/?pageid=27160&docid=214354) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/20qd.signed.pdf) |
| ND-363-2026 | 363/2026/NĐ-CP (19/09/2026) | Xử phạt VPHC trong lĩnh vực dữ liệu | **11/11/2026** | Sắp HL | Tất cả kể cả ĐVSN công lập (Đ2 k2 d) | gốc-OCR | [VB 219598](https://vanban.chinhphu.vn/?pageid=27160&docid=219598) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/363_2026_nd-cp_19092026-signed.signed.pdf) |
| L-DAUTU-2025 *(mới với cụm)* | 143/2025/QH15 (11/12/2025) | Luật Đầu tư — Phụ lục IV STT 198 "Dịch vụ xử lý dữ liệu cá nhân" | Luật 01/03/2026; **Phụ lục IV 01/07/2026** (Đ51 k2) | Còn HL; Phụ lục IV sẽ bị Luật 24/2026 thay từ 01/03/2027 | Vendor | gốc (text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat143-2025.pdf) · [VB 216524](https://vanban.chinhphu.vn/?pageid=27160&docid=216524) |
| L-DAUTU-SD-2026 *(mới)* | 24/2026/QH16 (24/08/2026) | Luật sửa đổi Luật Đầu tư — Phụ lục IV mới, STT 136 "Dịch vụ xử lý dữ liệu cá nhân" (vẫn giữ) | 01/03/2027 | Sắp HL | Vendor | gốc-OCR (phụ lục) | [VB 219356](https://vanban.chinhphu.vn/?pageid=27160&docid=219356) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/luatso24-suadoiluatdautu.signed.pdf) |
| L-KCB-2023 (tham chiếu) | VBHN 26/VBHN-VPQH | Luật KCB hợp nhất — Đ10 k2, Đ12, Đ45 k5, Đ69 (bí mật & khai thác HSBA) | 01/01/2024 | Còn HL | BV, PK | gốc (text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| L-HIV-SD-2020 *(mới)* | 71/2020/QH14 (16/11/2020) sửa Luật 64/2006/QH11 | Phòng, chống HIV/AIDS — Đ30 thông báo kết quả dương tính và tiếp cận thông tin người nhiễm HIV | 01/07/2021 | Còn HL (chưa kiểm VBHN mới hơn) | BV, PK, LIS | bản sao trên cổng .gov.vn (không ký số) | [Trang CA Đắk Lắk](https://congan.daklak.gov.vn/laws/detail/Luat-sua-doi-bo-sung-mot-so-dieu-cua-Luat-Phong-chong-nhiem-vi-rut-gay-ra-hoi-chung-suy-giam-mien-dich-mac-phai-o-nguoi-HIV-AIDS-2020-SO-71-2020-QH14-324/) (lỗi chứng chỉ SSL, mở được bằng curl -k) |
| ND-13-2023 | 13/2023/NĐ-CP | BVDLCN (cũ) | 01/07/2023 → hết HL 01/01/2026 (NĐ 356 Đ42 k2) | Hết HL | Chỉ để chuyển tiếp (Luật 91 Đ39) | gốc (qua NĐ 356) | — |
| QD-2623-2025-TTg | 2623/QĐ-TTg (29/11/2025) | Kế hoạch triển khai thi hành Luật BVDLCN | ký | Còn HL | Bối cảnh (cơ quan nhà nước) | gốc-meta | [VB 216065](https://vanban.chinhphu.vn/?pageid=27160&docid=216065) |
| ND-169-2025 / ND-347-2026 | 169/2025/NĐ-CP; sửa bởi 347/2026/NĐ-CP | Sản phẩm, dịch vụ về dữ liệu | 01/07/2025; 347: 15/09/2026 | Còn HL | Ngoại vi (vendor bán dịch vụ dữ liệu) | gốc-meta | [VB 214306](https://vanban.chinhphu.vn/?pageid=27160&docid=214306) · [VB 219411](https://vanban.chinhphu.vn/?pageid=27160&docid=219411) |
| ND-314-2026 | 314/2026/NĐ-CP (08/08/2026) | Hoạt động của sàn dữ liệu | 25/09/2026 | Còn HL | Ngoại vi (NĐ 356 Đ7 k5: phải khử nhận dạng trước khi giao dịch trên sàn) | gốc-meta | [VB 219180](https://vanban.chinhphu.vn/?pageid=27160&docid=219180) |

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### Nhóm A. Phân loại và căn cứ xử lý

#### DLCN-R01 — Dữ liệu sức khỏe là DLCN nhạy cảm: phân quyền giới hạn truy cập
- **Căn cứ**: NĐ 356 Đ4 k1 điểm d ("Tình trạng sức khỏe"), điểm đ (sinh trắc học, đặc điểm di truyền), điểm e (đời sống tình dục), điểm i (tên đăng nhập/mật khẩu tài khoản định danh điện tử; ảnh thẻ căn cước), điểm k (tài khoản ngân hàng, lịch sử giao dịch, thông tin bảo hiểm của khách hàng tại tổ chức tín dụng/bảo hiểm); Đ4 k2: "phải thiết lập quy định phân quyền giới hạn truy cập, quy trình xử lý và các biện pháp bảo mật". Luật 91 Đ2 k3 (định nghĩa). Chế tài: NĐ 330 Đ62 k1 b (app y tế, nền tảng chăm sóc sức khỏe trực tuyến thu thập dữ liệu nhạy cảm mà không phân quyền giới hạn: 50–70 triệu); khắc phục Đ62 k4 a.
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: (1) gắn nhãn độ nhạy (cơ bản/nhạy cảm) cho từng trường hoặc nhóm dữ liệu; mọi dữ liệu lâm sàng, kết quả CLS, chẩn đoán, đơn thuốc, ảnh, sinh trắc mặc định "nhạy cảm"; (2) RBAC/ABAC với nguyên tắc tối thiểu: chỉ người được phân công điều trị/xử lý mới xem; (3) có văn bản quy trình xử lý dữ liệu nhạy cảm và ma trận phân quyền xuất được ra file để nộp kèm DPIA.
- **Ghi chú / bẫy**: Số điện thoại, CCCD, ảnh chân dung là dữ liệu **cơ bản** (NĐ 356 Đ3 k6, k7), nhưng **ảnh thẻ căn cước** là nhạy cảm (Đ4 k1 i). App lưu ảnh chụp CCCD/thẻ BHYT có ảnh để xác thực bệnh nhân là đang giữ dữ liệu nhạy cảm.

#### DLCN-R02 — Căn cứ xử lý: đồng ý là mặc định, ngoại lệ theo Luật 91 Đ19 k1
- **Căn cứ**: Luật 91 Đ26 k1 a: với thông tin sức khỏe "phải có sự đồng ý của chủ thể dữ liệu cá nhân trong quá trình thu thập, xử lý dữ liệu cá nhân, trừ trường hợp quy định tại khoản 1 Điều 19"; Đ11 k1 (đồng ý trước khi thu thập). Đ19 k1: a) bảo vệ tính mạng, sức khỏe trong trường hợp cấp bách (bên xử lý **có trách nhiệm chứng minh**); b) tình trạng khẩn cấp, an ninh; c) phục vụ hoạt động của cơ quan nhà nước theo luật; d) thực hiện thỏa thuận của chủ thể với tổ chức theo quy định của pháp luật; đ) trường hợp khác theo quy định của pháp luật. Đ19 k2: xử lý không cần đồng ý vẫn phải có quy trình, biện pháp bảo vệ, đánh giá rủi ro, kiểm tra định kỳ, cơ chế tiếp nhận phản ánh. Luật 91 Đ5 k2: luật ban hành trước 01/01/2026 có quy định cụ thể về BVDLCN không trái nguyên tắc thì áp dụng luật đó (Luật KCB 2023, Luật HIV, Luật BHYT). NĐ 330 Đ47 (không chứng minh được căn cứ miễn đồng ý: 30–50 triệu; không có quy trình: 10–20 triệu).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC (phải có căn cứ cho từng mục đích và chứng minh được) · BẮT BUỘC? (việc xếp hoạt động KCB cốt lõi như lập HSBA, gửi XML BHYT, liên thông Sổ SKĐT vào Đ19 k1 đ/d thay vì đồng ý — **suy luận**, chưa có hướng dẫn)
- **Phần mềm phải**: duy trì **sổ đăng ký hoạt động xử lý** (processing register): mỗi mục đích có `legal_basis` ∈ {consent, emergency_19_1_a, state_19_1_c, contract_19_1_d, law_19_1_dd} + `legal_reference` (vd "Luật KCB Đ69 k1", "NĐ 102 Đ10 k5 b"); với ca cấp cứu nhập chưa có đồng ý phải ghi cờ `emergency_basis` + lý do + người xác nhận, và nhắc thu đồng ý khi người bệnh/đại diện có khả năng.
- **Ghi chú / bẫy**: Đừng dựa hoàn toàn vào "luật định" cho mọi việc: mục đích ngoài KCB (nghiên cứu, CRM, marketing, đào tạo AI, chia sẻ cho đối tác) **luôn** cần đồng ý riêng. Thực hành an toàn (suy luận): thu đồng ý ở bước đăng ký khám cho cả mục đích KCB, đồng thời ghi căn cứ luật định làm căn cứ dự phòng.

#### DLCN-R03 — Hình thức đồng ý, lưu bằng chứng, cấm mặc định đồng ý
- **Căn cứ**: Luật 91 Đ9 k2 (tự nguyện, biết rõ loại dữ liệu, mục đích, bên kiểm soát, quyền/nghĩa vụ), k3 (rõ ràng, cụ thể, in/sao chép được, kể cả điện tử), k4 (đồng ý **từng mục đích**; không kèm điều kiện bắt buộc; hiệu lực tới khi thay đổi; im lặng không phải đồng ý). NĐ 356 Đ6 k1 (phương thức: văn bản; cuộc gọi ghi âm; cú pháp SMS; email/web/app có thiết lập kỹ thuật; phương thức khác in được — **phải kiểm chứng được** chủ thể, thời điểm, nội dung), k2 (**phải lưu trữ** sự đồng ý; tranh chấp thì bên kiểm soát chịu trách nhiệm chứng minh), k3 (không thiết lập mặc định đồng ý, không chỉ dẫn gây hiểu lầm), k4 (khi xin đồng ý xử lý dữ liệu nhạy cảm phải **thông báo rằng đó là dữ liệu nhạy cảm**). NĐ 330 Đ43 k1 (30–50 triệu, gồm điểm g: không lưu nhật ký đồng ý; điểm h: không thông báo dữ liệu nhạy cảm đang được xử lý), k2 (50–70 triệu: tiếp tục xử lý sau khi bị yêu cầu ngừng; coi im lặng là đồng ý).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/01/2026; đồng ý thu theo NĐ 13/2023 vẫn giữ giá trị (Luật 91 Đ39 k1)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: (1) màn hình/biểu mẫu đồng ý tách từng mục đích, checkbox **không tick sẵn**, nút đồng ý và không đồng ý cân bằng; (2) câu thông báo "dữ liệu sức khỏe là dữ liệu cá nhân nhạy cảm"; (3) lưu bản ghi đồng ý bất biến: chủ thể (mã BN + định danh), người ký thay (nếu có) và quan hệ, phiên bản văn bản thông báo (hash nội dung), mục đích, kênh (giấy scan/ký số/OTP/app), thời điểm, IP/thiết bị, người tiếp nhận; (4) xuất được bằng chứng ra PDF; (5) KCB không bị từ chối vì người bệnh không đồng ý mục đích phụ (Đ9 k4 b; NĐ 330 Đ43 k1 b).
- **Ghi chú / bẫy**: "Đồng ý chung chung trong phiếu nhập viện" không đáp ứng yêu cầu từng mục đích. Bản ghi đồng ý cũ theo NĐ 13 cần được migrate kèm metadata gốc.

### Nhóm B. Quyền của chủ thể dữ liệu

#### DLCN-R04 — Quy trình, biểu mẫu và kênh tiếp nhận yêu cầu thực hiện quyền
- **Căn cứ**: Luật 91 Đ4 k1 (quyền: biết; đồng ý/rút lại; xem, chỉnh sửa; yêu cầu cung cấp, xóa, hạn chế, phản đối; khiếu nại; yêu cầu biện pháp bảo vệ), k4, k5. NĐ 356 Đ5 k1: phải xây dựng "quy trình, thủ tục, biểu mẫu rõ ràng", phân trách nhiệm các bộ phận, bảo đảm chủ thể được biết thủ tục. NĐ 330 Đ44 k1 (10–20 triệu).
- **Áp dụng cho**: bên kiểm soát (BV, PK, nhà thuốc; vendor app B2C) · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: module "Yêu cầu chủ thể dữ liệu" (DSR) gồm biểu mẫu web/app/quầy, xác minh danh tính người yêu cầu, phân loại loại yêu cầu, đồng hồ SLA, nhật ký xử lý, mẫu thư phản hồi; trang công khai mô tả thủ tục.

#### DLCN-R05 — Thời hạn phản hồi và thực hiện (SLA pháp định)
- **Căn cứ**: NĐ 356 Đ5:
  - k2 rút lại đồng ý / hạn chế / phản đối: phản hồi **02 ngày làm việc**, thực hiện **15 ngày**; nếu phải yêu cầu bên xử lý/bên thứ ba ngừng: **20 ngày**; gia hạn tối đa 1 lần ≤ **15 ngày**;
  - k3 xem / chỉnh sửa / cung cấp: phản hồi 02 ngày làm việc, thực hiện **10 ngày**; qua bên xử lý/bên thứ ba: **15 ngày**; gia hạn 1 lần ≤ **10 ngày**;
  - k4 xóa: phản hồi 02 ngày làm việc, thực hiện **20 ngày**; qua bên xử lý/bên thứ ba: **30 ngày**; gia hạn 1 lần ≤ **20 ngày**;
  - k5 yêu cầu áp dụng biện pháp bảo vệ: phản hồi 02 ngày làm việc, thực hiện **15 ngày**; gia hạn ≤ 15 ngày.
  - Mọi gia hạn phải thông báo lý do và tự chứng minh là cần thiết.
  - Chế tài: NĐ 330 Đ44 k1 d (quá 02 ngày làm việc), k3 (30–40 triệu khi quá hạn thực hiện), k2 (bên xử lý/bên thứ ba không thực hiện đúng hạn bên kiểm soát đặt: 20–30 triệu).
- **Áp dụng cho**: bên kiểm soát; vendor là bên xử lý phải hỗ trợ trong hạn bên kiểm soát đặt · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tính hạn theo **ngày làm việc** cho mốc phản hồi và theo ngày (chưa rõ ngày làm việc hay ngày lịch, xem mục 7) cho mốc thực hiện; cảnh báo trước hạn; ghi lý do gia hạn; API cho bên kiểm soát gửi lệnh "ngừng/xóa/sửa" tới vendor và nhận xác nhận hoàn thành.
- **Ghi chú / bẫy**: Discovery F (J4) ghi đúng mốc xem/sửa, nhưng bỏ sót mốc 20/30 ngày cho xóa và mốc 20 ngày cho bên thứ ba khi rút đồng ý.

#### DLCN-R06 — Quyền xem, sao chép hồ sơ bệnh án: áp dụng song song Luật KCB
- **Căn cứ**: Luật KCB (VBHN 26) Đ12 k1 (người bệnh được đọc, xem, sao chụp, ghi chép HSBA và nhận tóm tắt theo Đ69 k4 d); Đ69 k4 d (người bệnh/đại diện theo Đ8 k2 c, d: được đọc, xem, sao chụp khi **có yêu cầu bằng văn bản**), Đ69 k4 đ (đại diện theo Đ8 k2 a, d: chỉ được tóm tắt). Luật 91 Đ15 k2 a (cung cấp cho chủ thể, trừ khi gây tổn hại tới tính mạng, sức khỏe người khác). Luật 91 Đ5 k2 (luật cũ có quy định cụ thể thì áp dụng). NĐ 330 Đ49 k1 (từ chối cung cấp cho chính chủ thể: 10–20 triệu).
- **Áp dụng cho**: BV, PK · **Hiệu lực**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cổng/quầy cung cấp bản sao HSBA điện tử hoặc tóm tắt cho người bệnh có kiểm tra tư cách người yêu cầu theo loại đại diện (Đ8 k2 a–đ), lưu yêu cầu bằng văn bản (điện tử), ghi vết lần cung cấp.
- **Ghi chú / bẫy**: Phạm vi cho đại diện khác nhau theo loại đại diện; app bệnh nhân cho người nhà xem toàn bộ bệnh án là có thể vượt Đ69 k4 đ.

#### DLCN-R07 — Xóa, hủy: được từ chối khi luật buộc lưu, phải báo lý do; xóa an toàn
- **Căn cứ**: Luật 91 Đ14 k1 (các trường hợp xóa: chủ thể yêu cầu, hết mục đích, hết hạn lưu trữ…), k2 (không xóa theo yêu cầu khi thuộc Đ19), k3 (xóa bằng biện pháp an toàn, chống khôi phục), k4 (cấm cố ý khôi phục), k5 (không xóa được vì lý do chính đáng phải thông báo); Đ3 k3 (lưu trữ trong thời gian phù hợp mục đích, trừ khi luật khác quy định). Luật KCB Đ69 k2 (HSBA lưu giữ theo pháp luật về lưu trữ). NĐ 330 Đ51 (10–60 triệu), Đ39 k1 c (lưu vượt thời gian cần thiết: 20–40 triệu).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: (1) bảng chính sách lưu trữ (retention schedule) theo loại dữ liệu, có trường căn cứ luật; (2) với HSBA đang trong thời hạn lưu: từ chối yêu cầu xóa, gửi thông báo lý do, có thể **hạn chế xử lý** (khóa khỏi mục đích phụ); (3) dữ liệu ngoài HSBA (tài khoản app, marketing, log phụ) xóa được thật; (4) quy trình hủy dữ liệu an toàn (crypto-shredding hoặc ghi đè) kể cả bản sao lưu, có biên bản.
- **Ghi chú / bẫy**: Thời hạn lưu HSBA thuộc cụm K1 (TT 13/2025, TT 33/2025). Xóa "mềm" (cờ `deleted`) không đáp ứng yêu cầu "xóa, hủy" khi đã đến hạn hủy.

#### DLCN-R08 — Trẻ em, người mất/hạn chế năng lực hành vi
- **Căn cứ**: Luật 91 Đ24 k2: người đại diện theo pháp luật thay mặt thực hiện quyền (trừ Đ19 k1); xử lý dữ liệu trẻ em **nhằm công bố, tiết lộ** thông tin đời sống riêng tư, bí mật cá nhân của trẻ **từ đủ 07 tuổi** phải có đồng ý của **cả trẻ và người đại diện**; k3: ngừng xử lý khi người đã đồng ý rút lại hoặc theo yêu cầu cơ quan có thẩm quyền. NĐ 330 Đ60 k1 a (**không thực hiện quy trình xác minh tuổi** trước khi xử lý dữ liệu trẻ em: 30–50 triệu), k1 b (trẻ dưới 7 tuổi không có đồng ý đại diện), k1 c (trẻ từ đủ 7 tuổi xử lý mà **không có đồng thời** đồng ý của trẻ và đại diện), k2 (50–100 triệu), k3 (không xóa dữ liệu trẻ em khi phải xóa: 100–200 triệu). Luật KCB Đ8 (người đại diện của người bệnh; cha mẹ của con chưa thành niên).
- **Áp dụng cho**: tất cả, đặc biệt BV/PK nhi, sản, app mẹ và bé · **Hiệu lực**: 01/01/2026 (phạt từ 19/08/2026)
- **Mức**: BẮT BUỘC (đại diện đồng ý; xác minh tuổi) · BẮT BUỘC? (đồng ý kép cho mọi xử lý dữ liệu trẻ ≥7 tuổi — NĐ 330 Đ60 k1 c rộng hơn Luật 91 Đ24 k2)
- **Phần mềm phải**: tính tuổi từ ngày sinh tại thời điểm xin đồng ý; dưới 7: đồng ý của đại diện; từ đủ 7 tới dưới 18: thu **hai** chữ ký/xác nhận (trẻ + đại diện) cho mục đích ngoài KCB cấp cứu; lưu quan hệ đại diện và giấy tờ chứng minh; tự động nhắc khi trẻ tròn 7 tuổi và 18 tuổi để thu đồng ý lại.
- **Ghi chú / bẫy**: Xem mục 7 về độ vênh Luật/NĐ. Trẻ em ở đây là dưới 16 tuổi theo Luật Trẻ em (suy luận, chưa đọc lại trong pha này), nhưng người bệnh chưa thành niên dưới 18 do cha mẹ đại diện theo Luật KCB Đ8.

### Nhóm C. Chia sẻ, chuyển giao, bên xử lý

#### DLCN-R09 — Cấm cung cấp dữ liệu cho bảo hiểm sức khỏe/nhân thọ và cơ sở CSSK khác nếu không có yêu cầu bằng văn bản của chủ thể
- **Căn cứ**: Luật 91 Đ26 k2: tổ chức hoạt động trong lĩnh vực sức khỏe "không cung cấp dữ liệu cá nhân cho bên thứ ba là tổ chức cung cấp dịch vụ chăm sóc sức khỏe hoặc dịch vụ bảo hiểm sức khỏe, bảo hiểm nhân thọ, trừ trường hợp có yêu cầu bằng văn bản của chủ thể dữ liệu cá nhân hoặc trường hợp quy định tại khoản 1 Điều 19". NĐ 330 Đ62 k2: **70–100 triệu** khi cung cấp, chia sẻ dữ liệu bệnh nhân cho tổ chức CSSK khác hoặc DN bảo hiểm sức khỏe, nhân thọ "khi chưa nhận được yêu cầu bằng văn bản"; bổ sung đình chỉ hoạt động xử lý 3–6 tháng (Đ62 k3); buộc bên thứ ba xóa (Đ62 k4 b).
- **Áp dụng cho**: BV, PK, nhà thuốc, app y tế · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: (1) chặn mọi luồng xuất/API sang đối tác có `partner_type` ∈ {bảo hiểm thương mại, cơ sở CSSK khác} nếu không có bản ghi **yêu cầu bằng văn bản** (điện tử, kiểm chứng được) của chính người bệnh, gắn phạm vi (đợt điều trị, loại tài liệu) và thời hạn; (2) luồng **bảo lãnh viện phí** phải khởi tạo từ yêu cầu của người bệnh (ký trên giấy/ký điện tử/OTP), không gửi tự động; (3) nhật ký từng lần cung cấp.
- **Ghi chú / bẫy**: BHYT xã hội do BHXH (cơ quan nhà nước) không phải "dịch vụ bảo hiểm sức khỏe" thương mại; luồng XML BHYT dựa trên Luật BHYT/NĐ 188 và Đ19 k1 c (suy luận). Cụm từ "tổ chức cung cấp dịch vụ chăm sóc sức khỏe" rộng: chuyển tuyến, gửi mẫu cho phòng xét nghiệm ngoài, hội chẩn từ xa cần xác định căn cứ (Đ19 k1 a cấp cứu; Đ19 k1 đ khi luật chuyên ngành quy định chuyển tuyến) hoặc lấy yêu cầu bằng văn bản — xem mục 7. NĐ 330 Đ62 k2 không chép phần ngoại lệ Đ19 nhưng Luật có hiệu lực cao hơn.

#### DLCN-R10 — Thỏa thuận chuyển giao; mã hóa khi chuyển dữ liệu nhạy cảm; kiểm soát chia sẻ nội bộ
- **Căn cứ**: Luật 91 Đ17 k1 (các trường hợp chuyển giao), Đ15 k2 b (cung cấp cho bên khác khi có đồng ý). NĐ 356 Đ7 k1 (thỏa thuận chuyển giao phải nêu: mục đích; đối tượng, loại dữ liệu; thời hạn xử lý và yêu cầu xóa; cơ sở pháp lý; trách nhiệm bảo vệ; trách nhiệm thực hiện quyền chủ thể; phối hợp khi vi phạm), k2 (dữ liệu nhạy cảm: bảo mật vật lý thiết bị lưu trữ/truyền tải, **mã hóa, ẩn danh** và biện pháp khác), k4 (chia sẻ giữa các bộ phận trong cùng tổ chức: quy trình kiểm soát, chống nhân sự chia sẻ trái phép ra ngoài), k6 (cung cấp theo từng yêu cầu của chủ thể không phải chuyển giao). NĐ 330 Đ52 (20–80 triệu; Đ52 k3: chuyển dữ liệu nhạy cảm không mã hóa 50–80 triệu), Đ49 k2–3 (cung cấp không đồng ý; gấp đôi nếu nhạy cảm).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mọi kênh xuất dữ liệu (API, HL7/FHIR, file XML, email, USB, in) đi qua lớp kiểm soát có: đối tác đã có thỏa thuận (mã hợp đồng), căn cứ pháp lý, mã hóa TLS/mã hóa file, tối thiểu hóa trường; chức năng xuất hàng loạt (export Excel) bị giới hạn theo vai trò và ghi vết; cảnh báo DLP khi xuất bất thường.

#### DLCN-R11 — Hợp đồng xử lý dữ liệu với vendor (DPA) và trả/xóa dữ liệu khi chấm dứt
- **Căn cứ**: Luật 91 Đ37 k1 a, đ (bên kiểm soát nêu rõ trách nhiệm trong hợp đồng, chọn bên xử lý phù hợp), k2 a (bên xử lý **chỉ được tiếp nhận dữ liệu sau khi có thỏa thuận, hợp đồng**), k2 b (xử lý đúng hợp đồng). Luật 91 Đ23 k1 câu 2 (bên xử lý phát hiện vi phạm phải báo kịp thời cho bên kiểm soát). NĐ 330 Đ51 k2 c (bên xử lý không xóa hoặc trả lại toàn bộ dữ liệu sau khi kết thúc hợp đồng: 30–50 triệu), Đ46 k1 b (bên xử lý tự ý chỉnh sửa khi chưa được bên kiểm soát đồng ý bằng văn bản), Đ54 k1 a.
- **Áp dụng cho**: BV/PK thuê phần mềm; vendor · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải** (phía vendor): chức năng **xuất toàn bộ dữ liệu của khách hàng** theo định dạng chuẩn và **xóa có biên bản** khi hết hợp đồng; tách dữ liệu theo tenant; nhân sự vendor truy cập dữ liệu khách hàng chỉ qua phiên hỗ trợ có phê duyệt, ghi vết.

#### DLCN-R12 — Điện toán đám mây: hợp đồng và mã hóa khi lưu/truyền
- **Căn cứ**: NĐ 356 Đ12 k2 (hợp đồng với nhà cung cấp cloud: chấp hành luật VN; thông tin DPO; luồng xử lý và vai trò; biện pháp bảo mật trong hợp đồng; thông báo ngay thay đổi; thời hạn xử lý, xóa; quyền chủ thể; phân cấp truy cập), k3 (nhà cung cấp cloud: đánh giá tuân thủ **01 năm/lần**, ràng buộc nhà thầu phụ), k4: "Dữ liệu cá nhân trên điện toán đám mây phải được mã hoá ở trạng thái nghỉ và truyền, kèm theo phân quyền truy cập nghiêm ngặt." Luật 91 Đ30 k3. NĐ 330 Đ69 k2 b (không mã hóa at-rest/in-transit: 50–70 triệu), k1 (20–50 triệu).
- **Áp dụng cho**: mọi hệ thống chạy trên cloud (kể cả private cloud thuê) · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mã hóa DB, object storage, backup (KMS, quản lý khóa tách biệt); TLS cho mọi kết nối kể cả nội bộ; IAM tối thiểu; hồ sơ đánh giá tuân thủ hằng năm (nếu là nhà cung cấp cloud/SaaS).

### Nhóm D. Hồ sơ đánh giá tác động, chuyển dữ liệu ra nước ngoài

#### DLCN-R13 — Hồ sơ đánh giá tác động xử lý DLCN (DPIA): lập, nộp trong 60 ngày
- **Căn cứ**: Luật 91 Đ21 k1 (bên kiểm soát, bên kiểm soát và xử lý lập, lưu và gửi 01 bản chính cho cơ quan chuyên trách **trong 60 ngày kể từ ngày đầu tiên xử lý**), k2 (lập 01 lần, cập nhật theo Đ22), k3 (bên xử lý lập và lưu theo thỏa thuận), k6 (**cơ quan nhà nước có thẩm quyền** được miễn). NĐ 356 Đ19 k1 (kể cả **bên xử lý** lập và lưu giữ từ khi bắt đầu xử lý), k2 (thành phần: Báo cáo theo **Mẫu số 10**; bản sao hợp đồng/thỏa thuận xử lý; chính sách, quy trình, biểu mẫu), k3 (nội dung báo cáo: các bên và liên lạc; DPO; mục đích, loại dữ liệu, **sơ đồ luồng dữ liệu**; việc xin đồng ý, chính sách lưu/xóa; phương án an toàn, **sơ đồ thiết kế hệ thống**, tiêu chuẩn áp dụng; kết quả đánh giá tuân thủ; đánh giá rủi ro và biện pháp giảm thiểu), k4 (luôn sẵn sàng; nộp kèm **Mẫu 02a/02b** trong 60 ngày, trực tuyến/trực tiếp/bưu chính), k5 (cơ quan trả kết quả đạt/không đạt trong 15 ngày), k6 (hoàn thiện trong 30 ngày nếu được yêu cầu). Nơi nhận theo NĐ 330 Đ55 k1 b: Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (Bộ Công an). NĐ 330 Đ55 k1 (20–30 triệu), k2 (làm giả, sai lệch hồ sơ: 50–100 triệu), k3 b (**buộc dừng xử lý** cho tới khi nộp xong).
- **Áp dụng cho**: BV tư, PK, nhà thuốc, vendor (cả vai bên xử lý); BV công: BẮT BUỘC? (xem ghi chú) · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh tự động phần kỹ thuật của DPIA: danh mục trường dữ liệu và độ nhạy (R01), sổ đăng ký hoạt động xử lý (R02), sơ đồ luồng dữ liệu (tích hợp, đối tác, vùng lưu trữ), ma trận phân quyền, biện pháp mã hóa/sao lưu/ghi vết, danh sách bên xử lý phụ. Có trường `dpia_submitted_at`, `dpia_result`, `next_review_at`.
- **Ghi chú / bẫy**: (1) BV công lập là ĐVSN, không phải "cơ quan nhà nước có thẩm quyền" — **suy luận**: không được miễn theo Đ21 k6; cần hỏi cơ quan chuyên trách. (2) Hồ sơ đã được tiếp nhận theo NĐ 13/2023 trước 01/01/2026 được dùng tiếp (Luật 91 Đ39 k2). (3) Với hoạt động xử lý đã chạy trước 01/01/2026 mà chưa có hồ sơ: luật không nêu mốc riêng; **suy luận** tính từ 01/01/2026 (hạn khoảng 02/03/2026) — đã quá hạn.

#### DLCN-R14 — Cập nhật DPIA/TIA: định kỳ 06 tháng khi có thay đổi; 10 ngày với thay đổi lớn
- **Căn cứ**: Luật 91 Đ22 k1–3 (cập nhật định kỳ 06 tháng khi có thay đổi hoặc ngay trong các trường hợp k2; trên Cổng thông tin quốc gia về BVDLCN hoặc tại cơ quan chuyên trách). NĐ 356 Đ20 k1 (cập nhật định kỳ 06 tháng kể từ lần đầu nộp khi: phát sinh mục đích mới; phát sinh/thay đổi bên kiểm soát, bên xử lý, bên thứ ba), k2 (**trong 10 ngày** khi: tổ chức lại, chấm dứt, giải thể, phá sản; thay đổi tổ chức/cá nhân cung cấp dịch vụ BVDLCN; phát sinh/thay đổi ngành nghề liên quan đến xử lý DLCN), k3 (Mẫu 03a/03b). NĐ 330 Đ55 k1 d, đ.
- **Áp dụng cho**: như R13 · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trình theo dõi thay đổi (change log) tự gợi ý khi thêm đối tác tích hợp mới, thêm mục đích mới, đổi nhà cung cấp cloud/vendor → tạo việc "cập nhật DPIA" với hạn 10 ngày hoặc gộp vào kỳ 6 tháng.

#### DLCN-R15 — Chuyển dữ liệu xuyên biên giới (TIA) — kể cả lưu trên cloud nước ngoài
- **Căn cứ**: Luật 91 Đ20 k1 (các trường hợp: chuyển dữ liệu đang lưu tại VN ra hệ thống đặt ngoài lãnh thổ; chuyển cho tổ chức nước ngoài; dùng nền tảng ở nước ngoài để xử lý dữ liệu thu thập tại VN), k2 (lập hồ sơ, gửi bản chính **trong 60 ngày** từ ngày đầu tiên chuyển), k3, k4 (kiểm tra ≤1 lần/năm), k5 (lệnh ngừng chuyển), k6 (miễn: cơ quan nhà nước; dữ liệu người lao động trên cloud; chủ thể tự chuyển; trường hợp Chính phủ quy định). NĐ 356 Đ17 k1 a (lưu trên "dịch vụ điện toán đám mây của nhà cung cấp dịch vụ ở nước ngoài" là chuyển xuyên biên giới), k3 c (miễn trong tình huống khẩn cấp để bảo vệ tính mạng, sức khỏe), Đ18 k2–7 (hồ sơ: Mẫu 09, hợp đồng chuyển giao, chính sách; nội dung báo cáo gồm đánh giá mức bảo vệ của bên nhận; nộp kèm Mẫu 01a/01b trong 60 ngày; kết quả trong 15 ngày; hoàn thiện 30 ngày). Luật 91 Đ8 k4: phạt tối đa **5% doanh thu năm trước** với tổ chức. NĐ 330 Đ56 k1 (30–50 triệu), k2 (50–100 triệu), k3 (**1–5% doanh thu tại VN** nếu dẫn tới lộ, mất dữ liệu ≥10.000 công dân), k4 (200 triệu–3 tỷ nếu không có doanh thu), k5 b (đình chỉ chuyển 6–12 tháng).
- **Áp dụng cho**: mọi bên dùng cloud/SaaS/AI API đặt ở nước ngoài (vd máy chủ Singapore, API LLM nước ngoài), vendor có đội hỗ trợ ở nước ngoài truy cập dữ liệu · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấu hình rõ vùng lưu trữ (data residency) cho từng kho dữ liệu, kể cả backup, log, CDN, công cụ giám sát, email/SMS gateway, dịch vụ AI; sổ đăng ký luồng ra nước ngoài (bên nhận, quốc gia, loại dữ liệu, ngày bắt đầu, `tia_submitted_at`); chặn mặc định gửi PHI tới endpoint nước ngoài chưa đăng ký.
- **Ghi chú / bẫy**: Luật BVDLCN **không cấm** lưu ngoài VN, chỉ buộc TIA. Yêu cầu "EMR trên cloud đặt tại VN" của CV 365 và nghĩa vụ lưu trữ trong nước theo luật an ninh mạng thuộc cụm K1/K9 — phải đáp ứng đồng thời.

#### DLCN-R16 — Dữ liệu cốt lõi/quan trọng theo Luật Dữ liệu (bệnh viện, nền tảng lớn)
- **Căn cứ**: Luật 60/2024 Đ3 k6–7 (định nghĩa, gồm tác động tới "sức khỏe và an toàn cộng đồng"), Đ13 k2 (**chủ sở hữu/chủ quản không phải cơ quan nhà nước cũng phải phân loại** dữ liệu cốt lõi/quan trọng/khác), Đ23 k2, Đ25 k3–4, Đ27 k3. QĐ 20/2025/QĐ-TTg Phụ lục mục I (cốt lõi) điểm 25 (dữ liệu y tế **do cơ quan nhà nước** thu thập, quản lý chưa công khai: a) số mắc/chết bệnh truyền nhiễm mới chưa rõ tác nhân; b) thử nghiệm, sản xuất, dự trữ thuốc, TBYT phạm vi quốc gia; c) tác nhân gây bệnh mới; d) chứng chỉ hành nghề; đ) thông tin lưu hành dược, TBYT) và điểm **26 b: "Dữ liệu công dân nhạy cảm của 100.000 công dân Việt Nam trở lên"** (thuộc nhóm "dữ liệu về tổ chức, công dân chưa công khai", không giới hạn chủ thể là cơ quan nhà nước — gốc-OCR); mục II.1 (mọi dữ liệu cốt lõi cũng là quan trọng), II.10 (dữ liệu quỹ BHXH, BHYT do cơ quan nhà nước quản lý). NĐ 165 Đ17 k10 (chủ quản dữ liệu cốt lõi/quan trọng ghi nhật ký xử lý, **lưu ít nhất 06 tháng**), k11 (đánh giá rủi ro hằng năm). **NĐ 356 Đ42 k3** sửa NĐ 165 Đ16 k2: bảo vệ dữ liệu cốt lõi/quan trọng là DLCN thực hiện theo pháp luật BVDLCN; chuyển xuyên biên giới thì làm hồ sơ DPIA/TIA theo BVDLCN, **không** làm đánh giá rủi ro/tác động theo NĐ 165. NĐ 363 (từ 11/11/2026): Đ9 (không phân loại dữ liệu: 30–50 triệu, mức tổ chức), Đ19 k3 b (chuyển dữ liệu cốt lõi khi chưa có chấp thuận: 60–80 triệu, nhân 2 với tổ chức theo Đ6 k2), Đ22 k1 b (không ghi nhật ký ≥06 tháng với dữ liệu quan trọng/cốt lõi).
- **Áp dụng cho**: BV/nền tảng/vendor SaaS nắm dữ liệu nhạy cảm của ≥100.000 công dân; cơ quan, ĐVSN y tế công · **Hiệu lực**: 01/07/2025; chế tài NĐ 363 từ 11/11/2026
- **Mức**: BẮT BUỘC (phân loại dữ liệu theo Luật 60 Đ13 k2) · BẮT BUỘC? (nghĩa vụ riêng cho dữ liệu cốt lõi khi dữ liệu đó là DLCN, sau NĐ 356 Đ42 k3)
- **Phần mềm phải**: đếm số chủ thể duy nhất có dữ liệu nhạy cảm (cộng dồn) và cảnh báo khi vượt 100.000; ghi nhãn phân loại cốt lõi/quan trọng/khác; nhật ký xử lý lưu ≥ 6 tháng (khuyến nghị dài hơn, xem R24).
- **Ghi chú / bẫy**: Câu hỏi mở inventory "mục 25 là quan trọng hay cốt lõi" → **cốt lõi** (mục I), đồng thời là quan trọng (II.1). Nhưng mục 25 chỉ áp với dữ liệu do cơ quan nhà nước quản lý; với BV tư điểm đáng chú ý là I.26 b.

### Nhóm E. Sự cố và thông báo vi phạm

#### DLCN-R17 — Thông báo vi phạm cho cơ quan chuyên trách trong 72 giờ; biên bản; nội dung tối thiểu
- **Căn cứ**: Luật 91 Đ23 k1 (bên kiểm soát, bên kiểm soát và xử lý, bên thứ ba phát hiện vi phạm có thể gây tổn hại tới… tính mạng, sức khỏe, danh dự, nhân phẩm, tài sản của chủ thể: thông báo cho cơ quan chuyên trách "**chậm nhất là 72 giờ** kể từ khi phát hiện"; bên xử lý báo kịp thời cho bên kiểm soát), k2 (**lập biên bản xác nhận**), k3 (các trường hợp khác cũng phải thông báo: xử lý sai mục đích, không bảo đảm quyền chủ thể…). NĐ 356 Đ28 k1 (nội dung: thời gian, địa điểm, hành vi, tổ chức, cá nhân, loại và số lượng dữ liệu; liên lạc DPO; hậu quả; biện pháp), k2 (gửi cơ quan chuyên trách hoặc qua Cổng thông tin quốc gia về BVDLCN theo **Mẫu số 08**). NĐ 330 Đ54 k3 (chậm hơn 72 giờ: 40–60 triệu), k1 (không lập biên bản, che giấu: 10–20 triệu), k2 (không thông báo: 20–40 triệu), k4 (không ngăn chặn/khắc phục: 60–80 triệu).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: quy trình sự cố có đồng hồ 72 giờ từ `detected_at`; biểu mẫu sự cố theo trường Mẫu 08; khả năng truy vấn nhanh "dữ liệu của ai, loại gì, bao nhiêu bản ghi bị ảnh hưởng" từ log truy cập; với vendor: kênh báo sự cố tự động cho từng khách hàng (bên kiểm soát) trong hợp đồng.
- **Ghi chú / bẫy**: Mốc 72 giờ nằm ở **Luật 91 Đ23**, không phải NĐ 356 Đ29 (Đ29 là thông báo cho chủ thể với dữ liệu vị trí/sinh trắc). Sự cố an ninh mạng còn có nghĩa vụ báo cáo riêng theo NĐ 331/2026 (cụm K9).

#### DLCN-R18 — Sinh trắc học (và vị trí): thông báo chủ thể trong 72 giờ, lưu hồ sơ sự cố ≥5 năm
- **Căn cứ**: Luật 91 Đ31 k4 a (bảo mật vật lý thiết bị lưu/truyền dữ liệu sinh trắc, hạn chế truy cập, hệ thống theo dõi phát hiện xâm phạm), k3 b (app di động phải thông báo dùng vị trí, có tùy chọn). NĐ 356 Đ29 k1 a (thông báo chủ thể bị ảnh hưởng **≤ 72 giờ**), k1 c (lưu hồ sơ vi phạm **tối thiểu 5 năm** từ ngày khắc phục xong), k2 (nội dung tối thiểu), k3 (không thông báo hết được thì công bố trên web/app). NĐ 330 Đ70 k1 (50–70 triệu, gồm điểm đ: không thông báo cơ quan chuyên trách **và** chủ thể trong 72 giờ), k2 b (dùng sinh trắc vượt mục đích ban đầu chưa có đồng ý: 70–150 triệu).
- **Áp dụng cho**: hệ thống chấm công/định danh khuôn mặt, vân tay, xác thực BN bằng khuôn mặt, ảnh mống mắt, dữ liệu gen; app có định vị · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu template sinh trắc tách biệt, mã hóa, không dùng cho mục đích khác; nếu có sự cố: gửi thông báo cho BN qua SMS/app theo mẫu nội dung Đ29 k2; lưu hồ sơ sự cố ≥ 5 năm.

#### DLCN-R19 — Thông báo sự cố dữ liệu cho chủ thể khi gây thiệt hại (Luật Dữ liệu)
- **Căn cứ**: Luật 60/2024 Đ25 k3 (chủ quản dữ liệu không phải cơ quan nhà nước tự đánh giá rủi ro, khắc phục và "thông báo cho chủ thể dữ liệu"); NĐ 363 Đ22 k1 c (không thông báo sự cố dữ liệu cho tổ chức, cá nhân liên quan khi sự cố gây thiệt hại), k2 c (không có kế hoạch ứng phó khẩn cấp sự cố dữ liệu).
- **Áp dụng cho**: tất cả · **Hiệu lực**: Luật từ 01/07/2025; chế tài từ 11/11/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chức năng gửi thông báo hàng loạt cho BN bị ảnh hưởng; có kế hoạch ứng phó sự cố dữ liệu bằng văn bản và lịch diễn tập.

### Nhóm F. Tổ chức, nhân sự, miễn trừ

#### DLCN-R20 — Chỉ định nhân sự/bộ phận bảo vệ DLCN (DPO) hoặc thuê dịch vụ
- **Căn cứ**: Luật 91 Đ33 k2 (cơ quan, tổ chức **có trách nhiệm** chỉ định bộ phận, nhân sự đủ điều kiện hoặc thuê dịch vụ). NĐ 356 Đ13 k1 (chỉ định bằng **văn bản chính thức**), k2 (nhân sự: cao đẳng trở lên; ≥02 năm kinh nghiệm pháp chế/CNTT/an ninh mạng/an ninh dữ liệu/quản trị rủi ro/tuân thủ/nhân sự; đã được đào tạo BVDLCN), k5 (thỏa thuận bảo mật), k6 (đào tạo); Đ14 (nhiệm vụ: chính sách, quyền chủ thể, đánh giá định kỳ, lập DPIA/TIA, báo cáo vi phạm, đào tạo, kế hoạch ứng cứu); Đ15 (cá nhân cung cấp dịch vụ: ≥03 năm kinh nghiệm), Đ16 (tổ chức cung cấp dịch vụ: ≥03 nhân sự đủ điều kiện; công khai thông tin cho chủ thể). NĐ 330 Đ57 (cảnh cáo hoặc 10–30 triệu).
- **Áp dụng cho**: tất cả tổ chức (không có miễn trừ khi xử lý dữ liệu nhạy cảm — R21) · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấu hình thông tin liên hệ DPO hiển thị trong chính sách quyền riêng tư, biểu mẫu đồng ý, thông báo sự cố; vai trò "DPO" có quyền xem nhật ký truy cập, hàng đợi DSR, sổ đăng ký xử lý.

#### DLCN-R21 — Phòng khám nhỏ, nhà thuốc, startup y tế **không** được miễn DPIA/DPO
- **Căn cứ**: Luật 91 Đ38 k2 (DN nhỏ, khởi nghiệp được chọn không làm Đ21, Đ22, Đ33 k2 trong 05 năm, **trừ** DN "kinh doanh dịch vụ xử lý dữ liệu cá nhân, trực tiếp xử lý dữ liệu cá nhân nhạy cảm hoặc xử lý dữ liệu cá nhân của số lượng lớn chủ thể"), k3 (hộ kinh doanh, DN siêu nhỏ không phải làm, với cùng ngoại lệ). NĐ 356 Đ41 k1–2 (ngưỡng "số lượng lớn" = **từ 100 nghìn chủ thể** tính cộng dồn).
- **Áp dụng cho**: PK, nhà thuốc, startup app y tế, vendor · **Hiệu lực**: 01/01/2026 (miễn trừ cho DN thường kết thúc 01/01/2031)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không có tính năng riêng; checklist triển khai cho khách hàng nhỏ phải mặc định bật bộ DPIA/DPO.
- **Ghi chú / bẫy**: Ngưỡng 100.000 ở Đ41 chỉ là một trong ba ngoại lệ; cơ sở y tế đã thuộc ngoại lệ "trực tiếp xử lý dữ liệu nhạy cảm" ngay từ chủ thể đầu tiên. Hộ kinh doanh (nhiều nhà thuốc) bị phạt theo mức cá nhân = 1/2 tổ chức (NĐ 330 Đ2 k3, Đ7 k1).

### Nhóm G. Vendor phần mềm/SaaS/app y tế

#### DLCN-R22 — Vendor SaaS/app y tế thuộc diện "dịch vụ xử lý DLCN": phải có Giấy chứng nhận đủ điều kiện của Bộ Công an
- **Căn cứ**:
  - Luật 91 Đ33 k3 (Chính phủ quy định điều kiện "dịch vụ xử lý dữ liệu cá nhân"), Đ38 k2–3 (gọi tên "kinh doanh dịch vụ xử lý dữ liệu cá nhân").
  - NĐ 356 **Đ21** (danh mục dịch vụ): k1 "Dịch vụ cung cấp và vận hành hệ thống, phần mềm tự động để thay mặt bên kiểm soát, bên kiểm soát và xử lý tiến hành xử lý dữ liệu cá nhân"; **k4 "Dịch vụ thu thập, xử lý dữ liệu cá nhân qua trang web, ứng dụng, phần mềm chăm sóc sức khỏe, theo dõi sức khỏe, dịch vụ y tế"**; k3 (thu thập trực tuyến qua web, app); k6 (phân tích, khai thác); k7 (mã hóa khi truyền và lưu); k8 (xử lý tự động dựa trên dữ liệu lớn, AI, chuỗi khối); k9 (nền tảng cung cấp dữ liệu vị trí).
  - NĐ 356 **Đ22** (điều kiện): tổ chức thành lập theo pháp luật VN; người đứng đầu phụ trách chuyên môn xử lý DLCN là **công dân VN thường trú tại VN**; đội ngũ quản lý đáp ứng chuyên môn; **≥03 nhân sự** đạt Đ13 k2; hạ tầng phù hợp; có kết quả **đạt** với hồ sơ DPIA (và TIA nếu có chuyển ra nước ngoài).
  - NĐ 356 **Đ24** (Bộ Công an cấp, giao cơ quan chuyên trách), **Đ25** (hồ sơ: đơn Mẫu 04; bản sao GCN ĐKDN; văn bản chỉ định bộ phận BVDLCN hoặc hợp đồng dịch vụ BVDLCN; **đề án** gồm sự cần thiết, lĩnh vực, phương án kinh doanh, quy mô, khung quản trị rủi ro, kế hoạch đánh giá tuân thủ, tiêu chuẩn áp dụng, phương án định danh và xác thực điện tử, trách nhiệm, nhân sự; bằng cấp nhân sự; nộp trực tuyến/trực tiếp/bưu chính; đánh giá hồ sơ 10 ngày; bổ sung 15 ngày; **quyết định cấp trong 30 ngày** từ hồ sơ hợp lệ; Mẫu 05; bản giấy và điện tử), **Đ26** (cấp lại, cấp đổi 05 ngày làm việc), **Đ27** (thu hồi: không đảm bảo điều kiện; không kinh doanh ≥12 tháng; giải thể; không khắc phục vi phạm; tự đề nghị; nộp lại trong 05 ngày làm việc; công bố trên Cổng).
  - **Luật Đầu tư 143/2025/QH15 Phụ lục IV STT 198 "Dịch vụ xử lý dữ liệu cá nhân"** — ngành nghề đầu tư kinh doanh có điều kiện, Phụ lục có hiệu lực **01/07/2026** (Đ51 k2); **Luật 24/2026/QH16** thay Phụ lục IV từ 01/03/2027, vẫn giữ ngành này ở **STT 136**.
  - Chế tài: NĐ 330 Đ59 k3 a (kinh doanh khi chưa có Giấy chứng nhận: **50–80 triệu**), k4 (tiếp tục sau khi bị thu hồi: 80–100 triệu), k5 (buộc xóa dữ liệu xử lý trái phép, nộp lại khoản thu).
- **Áp dụng cho**: vendor HIS/EMR/LIS/RIS-PACS dạng **SaaS/hosted do vendor vận hành**; nền tảng khám từ xa, đặt lịch, app theo dõi sức khỏe, app nhà thuốc; dịch vụ AI chẩn đoán xử lý dữ liệu thay cơ sở KCB. **Không** áp cho cơ sở KCB tự vận hành hệ thống của mình (không "kinh doanh dịch vụ" cho người khác) — suy luận.
- **Hiệu lực / hạn chót**: NĐ 356 từ 01/01/2026, **không có điều khoản chuyển tiếp** cho Giấy chứng nhận (Đ42 chỉ quy định hiệu lực và bãi bỏ NĐ 13; Luật 91 Đ39 chỉ chuyển tiếp đồng ý và hồ sơ đánh giá tác động). Luật Đầu tư 143 Đ52 k15 chỉ chuyển tiếp cho ngành bị **bãi bỏ**, không cho ngành mới.
- **Mức**: BẮT BUỘC (SaaS/app do vendor vận hành, khớp nguyên văn Đ21 k1, k4) · BẮT BUỘC? (vendor bán license cài đặt tại chỗ nhưng có truy cập từ xa để bảo trì, hỗ trợ, đồng bộ dữ liệu)
- **Phần mềm phải**: vendor phải có hồ sơ chứng minh điều kiện (tài liệu hạ tầng, khung quản trị rủi ro, kết quả DPIA đạt); hiển thị số Giấy chứng nhận trong hợp đồng/điều khoản dịch vụ; khách hàng (BV/PK) kiểm tra khi chọn bên xử lý (Luật 91 Đ37 k1 đ).
- **Ghi chú / bẫy**: (1) NĐ 356 Đ27 k1 a dẫn chiếu "khoản 1, khoản 2 Điều 26" — có vẻ là lỗi dẫn chiếu (Đ26 là cấp lại/cấp đổi; điều kiện nằm ở Đ22). (2) Tên giấy dùng lẫn "đủ điều kiện kinh doanh" (Đ25–27) và "đủ điều kiện cung cấp" (Đ24) — cùng một giấy. (3) Chưa thấy văn bản xếp ngành này vào danh mục "cấp phép trước" hay "hậu kiểm" theo Luật Đầu tư 143 Đ7 k1 đoạn 2 — xem mục 7. (4) Vendor là pháp nhân nước ngoài không đáp ứng Đ22 k1 → phải qua pháp nhân VN.

#### DLCN-R23 — Nghĩa vụ của tổ chức đã được cấp Giấy chứng nhận
- **Căn cứ**: NĐ 356 Đ23: tuân thủ nghĩa vụ bên kiểm soát và xử lý/bên xử lý; **khung quản trị rủi ro**; **đánh giá hiện trạng tuân thủ và mức độ tín nhiệm 01 năm/lần**; áp dụng tiêu chuẩn an ninh dữ liệu, BVDLCN, an ninh mạng; quy định trách nhiệm và quyền hạn; ngăn truy cập trái phép; khi là bên xử lý, **yêu cầu bên kiểm soát xin đồng ý** của chủ thể trước khi cung cấp dịch vụ và bảo đảm chủ thể biết tên tổ chức cung cấp dịch vụ (k7); **xác thực danh tính tổ chức** theo pháp luật định danh điện tử (k8). NĐ 330 Đ59 k1–2 (20–50 triệu).
- **Áp dụng cho**: vendor đã có giấy · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: màn hình đồng ý do vendor cung cấp cho khách hàng phải nêu tên vendor như bên xử lý; báo cáo đánh giá tuân thủ hằng năm; tài khoản định danh điện tử tổ chức (VNeID tổ chức) — suy luận về cách thực hiện k8.

#### DLCN-R24 — Ứng dụng y tế "tuân thủ đầy đủ"; xử lý dữ liệu lớn: xác thực đa yếu tố, giám sát truy cập
- **Căn cứ**: Luật 91 Đ26 k3 (tổ chức, cá nhân phát triển ứng dụng về y tế phải tuân thủ đầy đủ quy định BVDLCN), Đ30 k3 (hệ thống dùng dữ liệu lớn, AI, cloud: xác thực, định danh phù hợp, phân quyền truy cập). NĐ 356 Đ9 k1 (dữ liệu lớn: quy mô lớn, liên tục, tích hợp nhiều nguồn, có khả năng phân tích hành vi, dự đoán, phân loại người dùng), k3 b (**xác thực mạnh, tối thiểu đa yếu tố**, phù hợp độ nhạy cảm; phân quyền), k3 c (mã hóa, ẩn danh khi chuyển giao, cung cấp), k3 d (**giám sát liên tục** truy cập, phát hiện bất thường), k3 đ (đánh giá an ninh định kỳ). NĐ 330 Đ66 (chưa đọc chi tiết mức phạt).
- **Áp dụng cho**: app y tế (mọi quy mô) cho phần Đ26 k3; nền tảng HIS/EMR tập trung đa cơ sở, kho dữ liệu y tế, nền tảng phân tích cho phần Đ9 · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC (Đ26 k3, Đ30 k3) · BẮT BUỘC? (Đ9: ranh giới "dữ liệu lớn" chưa định lượng)
- **Phần mềm phải**: MFA cho tài khoản nhân viên truy cập dữ liệu BN (ít nhất cho truy cập từ xa, quản trị, xuất dữ liệu); nhật ký truy cập ở mức bản ghi BN (ai, khi nào, xem/sửa/xuất gì) và cảnh báo hành vi bất thường (xem hồ sơ không thuộc ca điều trị, truy cập hàng loạt, ngoài giờ).

#### DLCN-R25 — AI và xử lý tự động (CDSS, chẩn đoán hình ảnh AI, chatbot)
- **Căn cứ**: Luật 91 Đ30 k4 (xử lý DLCN bằng AI phải phân loại theo mức rủi ro). NĐ 356 Đ10 k2 (kết quả suy luận AI xác định được người cụ thể là DLCN), k3 (thông báo cho chủ thể về **xử lý tự động**, giải thích nguyên tắc thuật toán và ảnh hưởng, **cho lựa chọn không tham gia**), k5 đ (đánh giá tuân thủ 01 năm/lần), k6 (quyền chỉnh sửa, ẩn danh, xóa hồ sơ nhận dạng). NĐ 330 Đ67 k1 (20–50 triệu), k2 (50–70 triệu: không giải thích, không cho từ chối, không phân loại rủi ro…), k3 b (quyết định tự động ảnh hưởng quyền lợi mà không có giám sát hoặc không cho yêu cầu **đánh giá lại bởi con người**: 70–100 triệu).
- **Áp dụng cho**: vendor và cơ sở dùng AI trên dữ liệu BN · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hồ sơ phân loại rủi ro cho từng mô hình; thông báo trong biểu mẫu đồng ý/chính sách về xử lý tự động; cờ opt-out theo BN và mô hình; kết quả AI luôn có người hành nghề xác nhận (human-in-the-loop) và lưu vết; dùng dữ liệu BN để huấn luyện mô hình là mục đích riêng cần đồng ý riêng hoặc khử nhận dạng (R26).

### Nhóm H. Mục đích phụ, khử nhận dạng, quảng cáo, mua bán

#### DLCN-R26 — Khử nhận dạng cho nghiên cứu, thống kê, huấn luyện; cấm tái nhận dạng
- **Căn cứ**: Luật 91 Đ2 k1 câu 3 ("Dữ liệu cá nhân sau khi khử nhận dạng không còn là dữ liệu cá nhân"), Đ2 k11 (định nghĩa), Đ14 k6 (kiểm soát quá trình khử nhận dạng; **không được tái nhận dạng** trừ khi luật quy định). NĐ 356 Đ7 k5 (khử nhận dạng trước khi giao dịch trên sàn dữ liệu). Luật KCB Đ69 k3–4 (khai thác HSBA cho nghiên cứu cần đồng ý của cơ sở KCB, giữ bí mật, đúng mục đích). NĐ 330 Đ51 k1 d–đ, k2 d, k3 b (tái nhận dạng: 50–60 triệu).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC (cấm tái nhận dạng; kiểm soát quá trình) · NÊN (dùng khử nhận dạng thay cho xin đồng ý khi làm phân tích, đào tạo AI, báo cáo)
- **Phần mềm phải**: pipeline khử nhận dạng có cấu hình (loại bỏ định danh trực tiếp, tổng quát hóa ngày sinh/địa chỉ, kiểm tra k-anonymity), bảng ánh xạ khóa giả danh lưu tách biệt với quyền truy cập riêng; ghi vết mọi lần xuất bộ dữ liệu nghiên cứu.
- **Ghi chú / bẫy**: Mã hóa/giả danh **không** phải khử nhận dạng: dữ liệu mã hóa vẫn là DLCN (Luật 91 Đ12 k1).

#### DLCN-R27 — Không mua bán dữ liệu cá nhân; chuyển giao có thu phí phải đúng điều kiện
- **Căn cứ**: Luật 91 Đ7 k6 (cấm mua, bán DLCN trừ khi luật quy định), Đ17 k2 (chuyển giao hợp lệ có/không thu phí không bị coi là mua bán), Đ8 k3 (phạt tối đa 10 lần khoản thu). NĐ 356 Đ7 k3 (chuyển giao có thu phí: cơ chế đồng ý **theo từng lần chuyển giao**, giới hạn loại dữ liệu, không hình thành kho dữ liệu cho mục đích khác…). NĐ 330 Đ53 (2–10 lần khoản thu; không có khoản thu: 70 triệu–3 tỷ theo số chủ thể, dữ liệu nhạy cảm ngưỡng thấp hơn).
- **Áp dụng cho**: tất cả, đặc biệt app/nền tảng có mô hình doanh thu từ dữ liệu, giới thiệu BN, "bán lead" · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không có tính năng bán/cho thuê danh sách BN; nếu có mô hình hợp tác có phí (vd chuyển hồ sơ cho đối tác theo yêu cầu BN) thì đồng ý theo từng lần chuyển, ghi rõ bên nhận và mục đích.

#### DLCN-R28 — Tin nhắn chăm sóc, quảng cáo, nhắc lịch mang tính tiếp thị
- **Căn cứ**: Luật 91 Đ28 k3 (xử lý dữ liệu khách hàng để quảng cáo phải được đồng ý, biết rõ nội dung, phương thức, tần suất; có cách từ chối), k5 (quyền yêu cầu ngừng nhận), k8 (quảng cáo theo hành vi: chỉ thu thập qua theo dõi web/app khi có đồng ý). Chế tài NĐ 330 Đ63 (chưa đọc chi tiết mức phạt trong pha này).
- **Áp dụng cho**: PK, BV tư, nhà thuốc, app có CRM/SMS/Zalo marketing · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tách loại tin "nghiệp vụ KCB" (kết quả, lịch tái khám) và "tiếp thị" (khuyến mãi, gói khám); tin tiếp thị chỉ gửi khi có đồng ý mục đích quảng cáo; mỗi tin có cách hủy đăng ký; không gắn pixel/SDK theo dõi quảng cáo vào trang có dữ liệu sức khỏe khi chưa có đồng ý.

#### DLCN-R29 — Camera giám sát, ghi âm tại cơ sở
- **Căn cứ**: Luật 91 Đ32 k1 a (ghi hình nơi công cộng không cần đồng ý để bảo vệ an ninh, quyền lợi hợp pháp), k2 (**phải thông báo** để người bị ghi hình biết), k3 (đúng mục đích), k4 (lưu trong thời gian cần thiết rồi xóa).
- **Áp dụng cho**: BV, PK, nhà thuốc · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: (nếu VMS tích hợp) chính sách tự xóa theo thời hạn cấu hình; phân quyền xem lại; ghi vết trích xuất. Không đặt camera ở buồng khám/thủ thuật khi không có căn cứ (suy luận).

#### DLCN-R30 — Nguyên tắc giới hạn mục đích, chính xác, thời hạn lưu
- **Căn cứ**: Luật 91 Đ3 k2–3. NĐ 330 Đ39 k1 a (xử lý vượt phạm vi, mục đích: 20–40 triệu), b (không bảo đảm chính xác), c (lưu vượt thời gian cần thiết).
- **Áp dụng cho**: tất cả · **Hiệu lực**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi trường dữ liệu thu thập phải gắn ít nhất một mục đích trong sổ đăng ký xử lý; không thu trường thừa (vd nghề nghiệp, tôn giáo) nếu biểu mẫu chuyên môn không yêu cầu; job định kỳ rà dữ liệu quá hạn lưu.

### Nhóm I. Bảo mật chuyên ngành y tế

#### DLCN-R31 — Bí mật hồ sơ bệnh án và quyền khai thác HSBA
- **Căn cứ**: Luật KCB Đ10 k2 (người bệnh được giữ bí mật thông tin HSBA và đời tư, trừ khi đồng ý chia sẻ hoặc Đ69 k3, k4), Đ45 k5 (người hành nghề giữ bí mật), Đ69 k2 (HSBA lưu giữ, giữ bí mật; HSBA thuộc bí mật nhà nước theo luật bảo vệ BMNN), k3 (HSBA **đang điều trị**: người trực tiếp điều trị, học viên, nghiên cứu viên được đọc, chỉ sao chép khi cơ sở đồng ý; người hành nghề cơ sở khác đọc, sao chép khi cơ sở đồng ý), k4 a (cơ quan quản lý y tế, điều tra, viện kiểm sát, tòa án, thanh tra y tế, giám định pháp y/pháp y tâm thần, **luật sư của người bệnh** được tiếp cận để thực hiện nhiệm vụ), k4 b, c (học viên, BHXH, cơ quan bồi thường nhà nước: mượn tại chỗ khi cơ sở đồng ý), k5 (người khai thác giữ bí mật, đúng mục đích đã đề nghị).
- **Áp dụng cho**: BV, PK · **Hiệu lực**: 01/01/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phân quyền HSBA theo trạng thái (đang điều trị / đã lưu trữ) và theo vai trò khai thác ở Đ69 k3–4; luồng "đề nghị khai thác HSBA" có phê duyệt của cơ sở, mục đích, thời hạn; chế độ chỉ đọc (không cho sao chép/in/tải) với học viên khi chưa được duyệt; ghi vết.

#### DLCN-R32 — Thông tin người nhiễm HIV: danh sách người được biết và phạm vi tiếp cận đóng
- **Căn cứ**: Luật 64/2006/QH11 sửa bởi Luật 71/2020/QH14, **Đ30** k1 (người đứng đầu cơ sở xét nghiệm thực hiện thông báo kết quả dương tính), k2 (kết quả dương tính **chỉ** thông báo cho: người được xét nghiệm; vợ/chồng; cha mẹ/giám hộ/đại diện của người dưới 18 tuổi, mất/hạn chế năng lực; người tư vấn trực tiếp; người làm giám sát dịch tễ HIV; trưởng khoa, điều dưỡng trưởng, nhân viên y tế trực tiếp điều trị; y tế tại cơ sở giam giữ, cai nghiện, bảo trợ; một số cơ quan), k3 (người được **tiếp cận thông tin** người nhiễm: giám sát dịch tễ; BHXH khi giám định, thanh toán BHYT; người của cơ sở y tế trực tiếp thanh toán, quản lý thông tin KCB; người được chính người nhiễm đồng ý), k4 (phạm vi: theo địa bàn được giao; theo cơ sở nơi làm việc/được phân công giám định), k5 (nội dung: thông tin cá nhân, dịch tễ, tình trạng điều trị), k6 (giữ bí mật), k7 (Bộ trưởng BYT quy định hình thức, quy trình — văn bản hướng dẫn chưa xác minh trong pha này).
- **Áp dụng cho**: BV, PK, phòng xét nghiệm, LIS, phần mềm quản lý điều trị ARV · **Hiệu lực**: 01/07/2021
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: gắn nhãn "HIV-restricted" cho chỉ định, kết quả xét nghiệm HIV, chẩn đoán ICD B20–B24/Z21 (danh sách mã cụ thể là suy luận), thuốc ARV; ẩn khỏi màn hình chung, báo cáo khoa, bản in tóm tắt, kết quả trả qua app/Sổ SKĐT trừ người trong danh sách Đ30 k2–3; truy cập ngoài danh sách cần "phá kính" có lý do và cảnh báo DPO.
- **Ghi chú / bẫy**: Kiểm tra lại tương thích với nghĩa vụ liên thông Sổ SKĐT và XML BHYT (cụm K2, K4) — luật HIV cho phép BHXH tiếp cận (k3 b) nhưng không nói gì về hiển thị trên VNeID.

#### DLCN-R33 — Dữ liệu y tế theo NĐ 102: tiếp cận có điều kiện, khai thác bởi tổ chức khác
- **Căn cứ**: NĐ 102 Đ6 (số định danh cá nhân là **mã định danh y tế** của cá nhân), Đ9 k1 (xử lý theo Luật Dữ liệu Đ22–26), Đ9 k2 b (thông tin bí mật đời tư, tình trạng sức khỏe, di truyền, đời sống tình dục… "được tiếp cận trong trường hợp được người đó đồng ý"), k2 c (bí mật gia đình: cần đồng ý của các thành viên gia đình), k2 d (người đứng đầu cơ quan nhà nước được quyết định cung cấp không cần đồng ý vì lợi ích công cộng, sức khỏe cộng đồng), Đ10 k2 c (tổ chức, cá nhân khác khai thác DLCN y tế khi **được đồng ý của đơn vị quản lý dữ liệu và của chủ thể**), Đ10 k5 b và Đ23 k2 (cơ sở y tế kết nối, chia sẻ với Sổ SKĐT trên VNeID và CSDL quốc gia về y tế), Đ23 k3 (bảo đảm ATTT, ANM khi kết nối).
- **Áp dụng cho**: mọi cơ sở y tế; bên thứ ba khai thác dữ liệu (công ty nghiên cứu, insurtech) · **Hiệu lực**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dùng số định danh cá nhân làm khóa định danh BN (giữ mã nội bộ song song); với yêu cầu khai thác của tổ chức ngoài, quy trình cần hai lớp chấp thuận (cơ sở + BN); thông tin di truyền liên quan cả gia đình (vd xét nghiệm gen gia đình) cần cơ chế đồng ý của các thành viên — suy luận áp Đ9 k2 c.

### Tóm tắt số lượng
33 yêu cầu, đếm theo mức chính: **BẮT BUỘC 32** (R01–R15, R17–R33), **BẮT BUỘC? 1** (R16 phần nghĩa vụ riêng cho dữ liệu cốt lõi), **NÊN 0** mục riêng. Phần phạm vi còn treo nằm trong 6 yêu cầu bắt buộc: R02 (xếp xử lý KCB vào Đ19), R08 (đồng ý kép mọi xử lý trẻ ≥7 tuổi), R13 (BV công có được miễn DPIA), R22 (vendor on-premise), R24 (ngưỡng "dữ liệu lớn" → MFA), và R26 có phần NÊN (dùng khử nhận dạng thay xin đồng ý).

---

## 3. Pattern thiết kế

### P01 — Sổ đăng ký hoạt động xử lý + nhãn độ nhạy cảm ở mức trường (giải R01, R02, R13, R16, R30)
- **Mô tả**: metadata trung tâm mô tả "dữ liệu gì, vì mục đích gì, căn cứ nào, lưu bao lâu, ai nhận". Là nguồn sinh DPIA, chính sách quyền riêng tư và kiểm tra luồng xuất.
- **Mô hình dữ liệu**:
  - `data_element(id, entity, field, sensitivity ENUM('basic','sensitive','hiv_restricted','biometric','genetic'), core_data_candidate BOOL)`
  - `processing_activity(id, name, purpose, legal_basis ENUM('consent','emergency_19_1a','state_19_1c','contract_19_1d','law_19_1dd'), legal_reference TEXT NOT NULL, retention_rule_id, controller_org_id, created_at, retired_at)`
  - `processing_activity_element(activity_id, element_id)`; `recipient(id, type ENUM('internal','processor','third_party','insurer_commercial','healthcare_provider','state'), country_code, contract_ref)`
  - Ràng buộc: không cho tạo `processing_activity` có `legal_basis='consent'` mà thiếu `consent_template_id`.
- **Đánh đổi**: tốn công khai báo ban đầu; bù lại DPIA và audit gần như tự động.

### P02 — Kho bằng chứng đồng ý bất biến, theo mục đích (R03, R08, R09, R25, R28)
- `consent_template(id, version, purpose_code, text_hash, is_sensitive_notice BOOL, locale, effective_from)`
- `consent_record(id, subject_id, template_id, decision ENUM('granted','denied'), actor_type ENUM('self','legal_rep','child_and_rep'), actor_ids[], rep_relation, channel ENUM('paper_scan','e_sign','otp_sms','app','recorded_call'), evidence_uri, captured_by, captured_at, ip, device)` — **append-only** (không UPDATE/DELETE; rút lại = bản ghi mới `withdrawn`).
- `consent_withdrawal(id, consent_record_id, requested_at, responded_at, effective_at)`
- View `effective_consent(subject_id, purpose_code)` dùng cho mọi kiểm tra trước khi xử lý.
- Chỉ mục: `(subject_id, purpose_code, captured_at DESC)`.
- **Đánh đổi**: cần chữ ký điện tử/OTP; chi phí lưu bằng chứng (scan) nhưng là bắt buộc chịu trách nhiệm chứng minh (NĐ 356 Đ6 k2).

### P03 — Hàng đợi yêu cầu chủ thể (DSR) có SLA pháp định (R04–R07)
- `dsr_request(id, subject_id, requester_id, requester_role, type ENUM('withdraw','restrict','object','access','rectify','copy_record','erase','protect'), received_at, verified_at, ack_due_at, ack_sent_at, due_at, extended_until, extension_reason, involves_third_party BOOL, status, outcome, refusal_reason)`
- Quy tắc tính hạn (cấu hình được): `ack_due_at = received_at + 2 ngày làm việc`; `due_at` theo bảng: withdraw/restrict/object 15 (20 nếu có bên thứ ba), access/rectify/copy 10 (15), erase 20 (30), protect 15; gia hạn tối đa 1 lần 15/10/20/15.
- Fan-out: `dsr_task(processor_id, action, sent_at, confirmed_at)` gửi lệnh tới vendor/bên thứ ba qua API, có xác nhận.
- **Đánh đổi**: cần lịch ngày làm việc VN (nghỉ lễ thay đổi theo năm).

### P04 — Cổng chia sẻ ra ngoài có "người gác" pháp lý (R09, R10, R11, R15, R27, R32, R33)
- Mọi tích hợp ra ngoài đi qua một egress service. Trước khi gửi: kiểm `recipient.type`; nếu `insurer_commercial` hoặc `healthcare_provider` mà không thuộc căn cứ cấp cứu/luật định → bắt buộc có `written_request(subject_id, recipient_id, scope, signed_at, evidence_uri, expires_at)` còn hiệu lực; nếu `country_code != 'VN'` → bắt buộc có `transfer_impact_assessment` đã nộp; lọc trường theo `data_element.sensitivity` (HIV-restricted bị loại trừ trừ khi người nhận nằm trong danh sách Đ30).
- Log: `disclosure_log(id, subject_id, recipient_id, activity_id, legal_basis, payload_hash, fields[], sent_at, actor)`.
- **Đánh đổi**: thêm độ trễ và điểm lỗi; bù lại một chỗ duy nhất để audit.

### P05 — Nhật ký truy cập ở mức hồ sơ BN + phát hiện bất thường + "phá kính" (R01, R16, R24, R31, R32)
- `access_log(id, ts, user_id, role, patient_id, encounter_id, resource_type, action ENUM('view','edit','print','export','share'), reason_code, break_glass BOOL, client_ip, session_id)` — ghi vào kho append-only (WORM hoặc bảng có hash-chain), lưu **≥ 6 tháng** (NĐ 165 Đ17 k10 cho dữ liệu cốt lõi/quan trọng); khuyến nghị lâu hơn vì thời hiệu xử phạt 01 năm (NĐ 330 Đ3 k1) và hồ sơ sự cố sinh trắc lưu ≥5 năm (NĐ 356 Đ29 k1 c).
- Quy tắc cảnh báo: xem BN ngoài danh sách được phân công; > N hồ sơ/giờ; xuất hàng loạt; tự xem hồ sơ của người thân cùng họ/địa chỉ.
- "Phá kính": cho phép truy cập khẩn cấp có lý do bắt buộc, gửi cảnh báo DPO, rà soát sau.
- **Đánh đổi**: dung lượng log lớn; cần phân vùng theo tháng.

### P06 — Mã hóa và nơi lưu trữ (R12, R15, R18)
- Mã hóa at-rest (TDE/disk + mã hóa cột cho trường HIV, gen, sinh trắc với khóa riêng), TLS 1.2+ mọi kết nối, backup mã hóa; quản lý khóa ở KMS/HSM; tách khóa theo tenant (SaaS).
- Bảng `storage_location(system, component, provider, region, country_code, contains_personal BOOL)` — kiểm tra CI: nếu có thành phần ngoài VN mà không có TIA → fail.
- **Đánh đổi**: mã hóa cột làm khó tìm kiếm; cân nhắc tokenization.

### P07 — Bộ sinh DPIA/TIA từ cấu hình (R13, R14, R15)
- Sinh bản nháp Mẫu 10/Mẫu 09 từ P01, P04, P06 (luồng dữ liệu, bên nhận, biện pháp); `dpia_dossier(id, type ENUM('dpia','tia'), version, submitted_at, receipt_no, result, result_at, next_periodic_update_due)`; trigger thay đổi → việc cập nhật 10 ngày hoặc kỳ 6 tháng.
- **Đánh đổi**: phần đánh giá rủi ro vẫn cần con người viết.

### P08 — Quy trình sự cố có đồng hồ 72 giờ (R17, R18, R19)
- `incident(id, detected_at, reported_internal_at, controller_notified_at, authority_due_at = detected_at + 72h, authority_notified_at, subject_notice_required BOOL, subjects_notified_at, record_retained_until = remediated_at + 5y, affected_count, data_types[], minutes_uri)`.
- Truy vấn dựng sẵn trên `access_log` và `disclosure_log` để ước lượng phạm vi.
- **Đánh đổi**: phải tích hợp với quy trình báo cáo sự cố ANM (K9) để tránh làm hai lần.

### P09 — Đối tượng đặc biệt: trẻ em và người đại diện (R08, R06)
- `legal_representative(subject_id, rep_person_id, rep_type ENUM('8_2_a','8_2_b','8_2_c','8_2_d','8_2_dd'), evidence_uri, valid_from, valid_to)` theo Luật KCB Đ8 k2; hàm `consent_requirement(subject_dob, purpose, at)` trả về `rep_only` (<7), `child_and_rep` (7–<18 cho mục đích ngoài KCB), `self`.
- Lịch nhắc thu đồng ý lại khi tròn 7 và 18 tuổi.

### P10 — Cách ly dữ liệu cực nhạy (R32, R18)
- Lớp "restricted compartment": dữ liệu HIV, gen, sức khỏe tâm thần, sinh sản (hai nhóm sau là NÊN, chưa có căn cứ riêng được xác minh) lưu với nhãn và khóa riêng; truy vấn danh sách/báo cáo dùng view đã che; API Sổ SKĐT/app BN dùng bộ lọc riêng.
- **Đánh đổi**: phức tạp hóa báo cáo; cần danh mục mã ICD/XN/thuốc được cập nhật.

### P11 — Gói tuân thủ dành cho vendor (R11, R22, R23)
- Đa tenant cách ly; công cụ export toàn bộ dữ liệu khách hàng; quy trình xóa có biên bản khi chấm dứt; phiên hỗ trợ từ xa "just-in-time" có phê duyệt của khách hàng; trang "Trust" công bố số Giấy chứng nhận, DPO, danh sách bên xử lý phụ và vùng lưu trữ; báo cáo đánh giá tuân thủ hằng năm.

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| DLCN-A01 | R01 | Lấy danh sách vai trò; đăng nhập bằng tài khoản điều dưỡng khoa A, thử mở hồ sơ BN khoa B; thử export danh sách BN | Ma trận phân quyền; ảnh chụp bị chặn/không bị chặn; văn bản quy trình xử lý dữ liệu nhạy cảm | Bắt buộc |
| DLCN-A02 | R02, R30 | Yêu cầu sổ đăng ký hoạt động xử lý; đối chiếu với các module thực tế (CRM, app, nghiên cứu, AI) | Sổ đăng ký có cột căn cứ pháp lý; các mục đích không có căn cứ | Bắt buộc |
| DLCN-A03 | R03 | Đăng ký BN mới trên UI: xem checkbox có tick sẵn không, có tách mục đích, có câu "dữ liệu nhạy cảm" không; truy vấn DB bảng đồng ý: có thời điểm, phiên bản văn bản, kênh, người thu | Ảnh màn hình; 5 bản ghi đồng ý mẫu; thử xuất bằng chứng | Bắt buộc |
| DLCN-A04 | R03 | Từ chối mục đích phụ (marketing/nghiên cứu) và kiểm tra vẫn đăng ký khám được | Ảnh màn hình | Bắt buộc |
| DLCN-A05 | R04, R05 | Gửi thử yêu cầu xem dữ liệu và rút đồng ý qua kênh công bố; đo thời gian phản hồi; xem hệ thống có tính hạn 2 ngày làm việc/10/15/20/30 ngày | Log DSR, thời điểm phản hồi; quy trình văn bản | Bắt buộc |
| DLCN-A06 | R05, R11 | Rút đồng ý marketing → kiểm tra 15 ngày sau hệ thống SMS/CRM bên thứ ba còn gửi không | Log gửi tin; xác nhận từ bên xử lý | Bắt buộc |
| DLCN-A07 | R06, R31 | Yêu cầu sao HSBA với tư cách BN và với tư cách đại diện loại "8_2_a"; xem phạm vi được cấp | Biểu mẫu yêu cầu bằng văn bản; log cung cấp | Bắt buộc |
| DLCN-A08 | R07 | Gửi yêu cầu xóa tài khoản app; kiểm tra DB, backup, log phụ; với HSBA kiểm tra có thư từ chối nêu lý do | Bảng chính sách lưu trữ; biên bản hủy; thư phản hồi | Bắt buộc |
| DLCN-A09 | R08 | Tạo hồ sơ BN 5 tuổi và 10 tuổi; kiểm tra luồng đồng ý đòi người đại diện / cả hai; hệ thống có xác minh tuổi | Ảnh màn hình; bản ghi đồng ý có `actor_type` | Bắt buộc |
| DLCN-A10 | R09 | Liệt kê các tích hợp với công ty bảo hiểm (bảo lãnh viện phí, TPA) và phòng khám/BV đối tác; với mỗi lần gửi, truy ngược yêu cầu bằng văn bản của BN | Danh sách endpoint; 10 hồ sơ bảo lãnh mẫu với yêu cầu ký của BN | Bắt buộc |
| DLCN-A11 | R10 | Rà các kênh xuất: API, file XML, email, Excel, USB; kiểm tra mã hóa khi truyền dữ liệu nhạy cảm và thỏa thuận chuyển giao | Danh sách kênh; cấu hình TLS; thỏa thuận có đủ 7 nội dung NĐ 356 Đ7 k1 | Bắt buộc |
| DLCN-A12 | R11 | Đọc hợp đồng với vendor phần mềm, cloud, SMS, lab ngoài: có điều khoản xử lý DLCN, xóa/trả dữ liệu khi chấm dứt, báo sự cố | Bản hợp đồng/phụ lục DPA | Bắt buộc |
| DLCN-A13 | R12 | Kiểm tra cấu hình mã hóa DB, storage, backup; kiểm tra kết nối nội bộ có TLS | Ảnh cấu hình KMS/TDE; kết quả quét TLS | Bắt buộc |
| DLCN-A14 | R13, R14 | Yêu cầu bản DPIA đã nộp, biên nhận, kết quả đánh giá; so nội dung với hệ thống thực tế; kiểm tra lần cập nhật gần nhất so với thay đổi (thêm đối tác, cloud mới) | Hồ sơ Mẫu 10 + 02a/02b; biên nhận; nhật ký thay đổi | Bắt buộc |
| DLCN-A15 | R15 | Liệt kê mọi thành phần lưu/ xử lý dữ liệu ngoài VN (cloud region, backup, log SaaS, email, AI API, đội hỗ trợ nước ngoài) | Sơ đồ hạ tầng; hồ sơ TIA Mẫu 09 + 01a/01b; biên nhận | Bắt buộc |
| DLCN-A16 | R16 | Đếm số BN duy nhất có dữ liệu sức khỏe (SQL `COUNT(DISTINCT patient_id)`); nếu ≥100.000 kiểm tra kết quả phân loại dữ liệu cốt lõi và log xử lý ≥6 tháng | Kết quả truy vấn; văn bản phân loại dữ liệu | Bắt buộc? |
| DLCN-A17 | R17 | Yêu cầu quy trình sự cố; diễn tập giả lập lộ dữ liệu: đo thời gian từ phát hiện tới bản thông báo theo Mẫu 08; kiểm tra khả năng xác định BN bị ảnh hưởng từ log | Quy trình; biên bản diễn tập; biên bản sự cố thật (nếu có) | Bắt buộc |
| DLCN-A18 | R18 | Nếu có sinh trắc: kiểm tra nơi lưu template, mã hóa, phân quyền; quy trình thông báo BN trong 72 giờ; lưu hồ sơ sự cố 5 năm | Cấu hình; quy trình | Bắt buộc |
| DLCN-A19 | R20, R21 | Xem quyết định chỉ định DPO/bộ phận; hồ sơ năng lực (bằng cấp, 2 năm kinh nghiệm, chứng nhận đào tạo); thỏa thuận bảo mật | Quyết định; CV; chứng chỉ | Bắt buộc |
| DLCN-A20 | R22 | Với vendor SaaS/app: yêu cầu Giấy chứng nhận đủ điều kiện kinh doanh dịch vụ xử lý DLCN (số, ngày cấp, phạm vi dịch vụ theo Đ21); nếu chưa có: biên nhận hồ sơ đang xin | Bản sao giấy hoặc biên nhận | Bắt buộc (SaaS) / Bắt buộc? (on-prem) |
| DLCN-A21 | R23 | Vendor đã có giấy: báo cáo đánh giá tuân thủ năm gần nhất, khung quản trị rủi ro; màn hình đồng ý có nêu tên vendor | Báo cáo; ảnh màn hình | Bắt buộc |
| DLCN-A22 | R24 | Kiểm tra MFA cho tài khoản nhân viên (ít nhất admin, truy cập từ xa, export); có giám sát truy cập bất thường | Cấu hình IdP; mẫu cảnh báo | Bắt buộc? |
| DLCN-A23 | R25 | Liệt kê tính năng AI/xử lý tự động; kiểm tra thông báo cho BN, cơ chế opt-out, xác nhận của bác sĩ, hồ sơ phân loại rủi ro | Tài liệu mô hình; ảnh UI | Bắt buộc |
| DLCN-A24 | R26 | Kiểm tra bộ dữ liệu nghiên cứu/đào tạo AI đã xuất: có định danh trực tiếp không; bảng ánh xạ khóa giả danh tách quyền | Mẫu dữ liệu xuất; quy trình khử nhận dạng | Bắt buộc / Nên |
| DLCN-A25 | R27 | Rà hợp đồng doanh thu với đối tác (giới thiệu BN, quảng cáo, data partnership) | Hợp đồng; luồng dữ liệu | Bắt buộc |
| DLCN-A26 | R28 | Kiểm tra CRM: tin tiếp thị chỉ gửi cho người có đồng ý quảng cáo; mỗi tin có cách hủy; trang web/app có pixel quảng cáo trên trang có dữ liệu sức khỏe không | Danh sách chiến dịch; cấu hình tag manager | Bắt buộc |
| DLCN-A27 | R29 | Đi thực địa: biển thông báo camera; xem chính sách tự xóa của VMS | Ảnh; cấu hình | Bắt buộc |
| DLCN-A28 | R31 | Tài khoản sinh viên/học viên: thử in, tải, sao chép HSBA đang điều trị | Ảnh màn hình; log | Bắt buộc |
| DLCN-A29 | R32 | Tài khoản nhân viên không điều trị BN HIV: thử tìm kết quả XN HIV, mã B20–B24, đơn ARV; xem bản in tóm tắt, app BN, dữ liệu gửi Sổ SKĐT | Ảnh màn hình; log truy cập | Bắt buộc |
| DLCN-A30 | R33 | Kiểm tra trường số định danh cá nhân là mã định danh y tế; quy trình cung cấp dữ liệu cho tổ chức ngoài có 2 lớp chấp thuận | Schema; quy trình | Bắt buộc |
| DLCN-A31 | R01, R24 | Kiểm tra log truy cập ở mức hồ sơ BN tồn tại, không sửa được, thời gian lưu | Truy vấn log 6 tháng trước; cấu hình WORM | Nên (Bắt buộc? với dữ liệu cốt lõi) |

---

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái (so với 2026-10-05) | Sự kiện | Ai phải làm |
|---|---|---|---|
| 01/07/2021 | Đã qua | Luật 71/2020/QH14 (HIV) có hiệu lực — Đ30 mới | BV, PK, phòng XN |
| 01/01/2024 | Đã qua | Luật KCB 15/2023 có hiệu lực (Đ10, 69) | BV, PK |
| 01/07/2025 | Đã qua | Luật Dữ liệu, NĐ 165, QĐ 20/2025/QĐ-TTg, NĐ 102 có hiệu lực; mốc tính lũy kế dữ liệu cốt lõi/quan trọng chuyển ra nước ngoài (NĐ 165 Đ12 k10) | Tất cả; cơ sở y tế phải kết nối Sổ SKĐT (NĐ 102 Đ23) |
| 01/01/2026 | Đã qua | Luật 91 + NĐ 356 có hiệu lực; NĐ 13/2023 hết hiệu lực; bắt đầu nghĩa vụ DPIA/TIA, DPO, SLA quyền chủ thể; Giấy chứng nhận dịch vụ xử lý DLCN (không có chuyển tiếp) | Tất cả; vendor SaaS/app |
| ~02/03/2026 | Đã qua (suy luận) | 60 ngày từ 01/01/2026: hạn nộp DPIA/TIA cho hoạt động đang chạy, nếu tính từ ngày luật có hiệu lực | Bên kiểm soát, vendor |
| 01/03/2026 | Đã qua | Luật Đầu tư 143/2025 có hiệu lực (trừ Phụ lục IV) | — |
| 01/07/2026 | Đã qua | Phụ lục IV Luật Đầu tư 143 có hiệu lực: "Dịch vụ xử lý dữ liệu cá nhân" (STT 198) là ngành nghề kinh doanh có điều kiện | Vendor |
| 19/08/2026 | Đã qua | NĐ 330/2026 có hiệu lực: chế tài BVDLCN (tối đa 3 tỷ; 5% doanh thu với chuyển xuyên biên giới; 10 lần khoản thu với mua bán) | Tất cả |
| 25/09/2026 | Đã qua | NĐ 314/2026 (sàn dữ liệu) có hiệu lực | Ngoại vi |
| **11/11/2026** | **Sắp tới** | NĐ 363/2026 có hiệu lực: chế tài lĩnh vực dữ liệu (phân loại dữ liệu, dữ liệu cốt lõi/quan trọng, log ≥6 tháng, chuyển xuyên biên giới dữ liệu cốt lõi) | BV/nền tảng lớn; ĐVSN y tế công; vendor |
| 01/03/2027 | Sắp tới | Luật 24/2026/QH16 có hiệu lực; Phụ lục IV mới, "Dịch vụ xử lý DLCN" ở STT 136 (vẫn có điều kiện) | Vendor |
| 01/01/2031 | Tương lai | Hết 05 năm tùy chọn cho DN nhỏ/khởi nghiệp (Luật 91 Đ38 k2) — **không áp** cho bên xử lý dữ liệu nhạy cảm | — |
| Thường xuyên | — | Phản hồi yêu cầu chủ thể 02 ngày làm việc; thực hiện 10/15/20/30 ngày; thông báo vi phạm ≤72 giờ; cập nhật DPIA/TIA 06 tháng khi có thay đổi hoặc 10 ngày với thay đổi lớn; nộp DPIA/TIA ≤60 ngày khi bắt đầu xử lý/chuyển mới; đánh giá tuân thủ 01 năm/lần (vendor có giấy, nhà cung cấp cloud, hệ thống AI); log dữ liệu cốt lõi ≥6 tháng; lưu hồ sơ sự cố sinh trắc/vị trí ≥5 năm | Như trên |

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuỗi thay thế**
- NĐ 13/2023/NĐ-CP → Luật 91/2025/QH15 + NĐ 356/2025/NĐ-CP (từ 01/01/2026; NĐ 356 Đ42 k2). Đồng ý và hồ sơ đánh giá tác động đã nộp theo NĐ 13 vẫn dùng được (Luật 91 Đ39 k1–2).
- NĐ 165/2025 Đ16 k2 (bản gốc: dữ liệu cốt lõi/quan trọng là DLCN thì đánh giá theo Luật Dữ liệu, **không** phải đánh giá theo pháp luật BVDLCN) → **bị đảo ngược** bởi NĐ 356 Đ42 k3 (làm hồ sơ theo BVDLCN, không làm đánh giá theo NĐ 165). Mọi tài liệu trích NĐ 165 Đ16 k2 nguyên bản là lỗi thời.
- Luật Đầu tư 2020 Phụ lục IV → Luật Đầu tư 143/2025 Phụ lục IV (01/07/2026, STT 198) → Luật 24/2026/QH16 Phụ lục IV (01/03/2027, STT 136).
- Văn bản còn dẫn NĐ 13/2023: TT 38/2024/TT-BYT, QĐ 69/2025/QĐ-TTg (theo inventory mục 3) → đọc thành Luật 91 + NĐ 356.
- NĐ 102/2025 căn cứ Luật ANM 2018 và Luật ATTT mạng 2015 — hai luật đã bị Luật ANM 116/2025/QH15 thay từ 01/07/2026 (theo discovery J9; thuộc cụm K9).

**Phân xử MT-15 (đã giải quyết bằng bản gốc)**
- DPIA: **nộp trong 60 ngày** kể từ ngày đầu tiên xử lý (Luật 91 Đ21 k1; NĐ 356 Đ19 k4) **và** cập nhật **định kỳ 06 tháng** khi có thay đổi (Luật 91 Đ22 k1; NĐ 356 Đ20 k1), **10 ngày** với tổ chức lại/đổi dịch vụ BVDLCN/đổi ngành nghề (NĐ 356 Đ20 k2). Hai bản khảo sát đều đúng một nửa.
- Số điều đúng của NĐ 356: Đ13 điều kiện nhân sự BVDLCN; Đ14 nhiệm vụ; Đ17 chuyển xuyên biên giới; Đ18 hồ sơ TIA; Đ19 hồ sơ DPIA; Đ20 cập nhật; Đ21 danh mục dịch vụ xử lý DLCN; Đ22 điều kiện; Đ23 trách nhiệm; Đ24–27 cấp/cấp lại/thu hồi Giấy chứng nhận; Đ28 nội dung thông báo vi phạm; Đ29 thông báo vi phạm với dữ liệu vị trí/sinh trắc; Đ41 ngưỡng 100.000 cho miễn trừ DN nhỏ.
- **72 giờ** báo cơ quan chuyên trách nằm ở Luật 91 Đ23 k1, không phải NĐ 356 Đ29. NĐ 356 Đ29 là 72 giờ báo **chủ thể** khi lộ dữ liệu vị trí/sinh trắc; NĐ 356 Đ8 k3 là 72 giờ cho lĩnh vực tài chính, ngân hàng.

**Bẫy khác**
- NĐ 330 Đ7 k1: mức phạt Mục 6 (BVDLCN) là mức **tổ chức**, cá nhân bằng 1/2; ngược với phần an ninh mạng (Mục 1–5) mức là cá nhân, tổ chức gấp 2. NĐ 363 Đ6 k2: mức là cá nhân, tổ chức gấp 2, **trừ** Đ8 k1 b, Đ9, Đ10, Đ13 k2, Đ16 k4 là mức tổ chức.
- NĐ 330 Đ62 k2 không chép ngoại lệ Đ19 k1 của Luật 91 Đ26 k2 — áp dụng theo Luật.
- NĐ 330 Đ60 k1 c đòi đồng ý kép cho mọi xử lý dữ liệu trẻ từ đủ 7 tuổi; Luật 91 Đ24 k2 chỉ đòi đồng ý kép khi xử lý **nhằm công bố, tiết lộ** đời sống riêng tư.
- NĐ 356 Đ27 k1 a dẫn chiếu "khoản 1, khoản 2 Điều 26" — có vẻ lỗi (điều kiện ở Đ22).
- QĐ 20/2025: mục 25 (y tế) thuộc **Mục I — dữ liệu cốt lõi** và chỉ áp với dữ liệu do cơ quan nhà nước thu thập, quản lý chưa công khai; còn mục **I.26 b** (dữ liệu nhạy cảm của ≥100.000 công dân) mới là điểm chạm BV tư/vendor. Đây là gốc-OCR, cần đối chiếu bản text.
- Nơi nhận hồ sơ DPIA: NĐ 330 Đ55 k1 b ghi rõ Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (Bộ Công an); Luật/NĐ 356 chỉ ghi "cơ quan chuyên trách".
- Thanh tra Bộ Y tế không có tên trong thẩm quyền xử phạt BVDLCN của NĐ 330 Đ74 (chỉ thanh tra BQP, BCA, NHNN được liệt kê) — chưa đọc hết Đ72–78.
- Dữ liệu mã hóa vẫn là DLCN (Luật 91 Đ12 k1); chỉ dữ liệu đã khử nhận dạng mới ra khỏi phạm vi (Đ2 k1).
- Discovery F trích "NĐ 356 Đ4 k1 điểm d, đ" đúng; trích "J5 … Đ29 thông báo vi phạm 72 giờ" là sai điều (xem trên).
- Không dùng hethongphapluat làm nguồn cho NĐ 102 (MT-21); bản Công báo đã đọc khớp các điều F trích (Đ6, 9, 10, 14, 23).

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Vendor on-premise**: vendor bán bản quyền cài tại cơ sở nhưng có truy cập từ xa để bảo trì, đồng bộ, sao lưu hộ — có phải "dịch vụ cung cấp và vận hành hệ thống… thay mặt bên kiểm soát" (NĐ 356 Đ21 k1) không? Hỏi Cục A05.
2. **Không có chuyển tiếp cho Giấy chứng nhận**: vendor đang hoạt động trước 01/01/2026 bị coi là vi phạm từ ngày nào? Chính phủ đã xếp ngành STT 198 vào danh mục "cấp phép trước" hay "hậu kiểm" theo Luật Đầu tư 143 Đ7 k1 chưa? Chưa tìm thấy văn bản. Chưa kiểm Phụ lục IV Luật Đầu tư 2020 (trước 01/07/2026) có ngành này không.
3. **Căn cứ cho xử lý KCB cốt lõi**: lập HSBA, gửi dữ liệu BHYT, liên thông Sổ SKĐT, báo cáo bệnh truyền nhiễm — xếp vào Luật 91 Đ19 k1 đ (luật định) / d (thỏa thuận) được không, hay vẫn phải đồng ý theo Đ26 k1 a? Chưa có hướng dẫn của BCA/BYT.
4. **Đ26 k2 và luồng lâm sàng**: chuyển tuyến, hội chẩn, gửi mẫu tới phòng xét nghiệm ngoài, chia sẻ cho bác sĩ gia đình — có bị coi là cung cấp cho "tổ chức cung cấp dịch vụ chăm sóc sức khỏe" cần yêu cầu bằng văn bản không? Phòng XN ngoài là bên xử lý (hợp đồng) hay bên thứ ba?
5. **"Yêu cầu bằng văn bản"** cho bảo lãnh viện phí có chấp nhận dạng điện tử (OTP, ký trên app) không — Luật 91 Đ10 k2 cho phép điện tử với rút đồng ý, Đ26 k2 không nói rõ.
6. **Trẻ em**: Luật 91 Đ24 k2 hay NĐ 330 Đ60 k1 c (đồng ý kép cho mọi xử lý trẻ ≥7 tuổi)? Thực tế triển khai đồng ý của trẻ 7 tuổi trong KCB?
7. **BV công lập** có được miễn DPIA như "cơ quan nhà nước có thẩm quyền" (Luật 91 Đ21 k6, Đ20 k6 a) không — suy luận là không.
8. **Bên xử lý có phải nộp DPIA** cho cơ quan chuyên trách không: Luật 91 Đ21 k3 nói "lập và lưu trữ theo thỏa thuận", NĐ 356 Đ19 k1, k4 và NĐ 330 Đ55 k1 b có thể hiểu là phải nộp.
9. **Mốc 60 ngày cho hoạt động xử lý có từ trước 01/01/2026** (không có hồ sơ theo NĐ 13): tính từ đâu?
10. **Ngày lịch hay ngày làm việc** cho mốc thực hiện 10/15/20/30 ngày (NĐ 356 Đ5 chỉ ghi "ngày"; mốc phản hồi ghi rõ "ngày làm việc").
11. **Dữ liệu cốt lõi ≥100.000 công dân** (QĐ 20 mục I.26 b, gốc-OCR): sau NĐ 356 Đ42 k3, chủ quản là BV tư/vendor còn phải làm nghĩa vụ riêng của Luật Dữ liệu (log ≥6 tháng, đánh giá rủi ro hằng năm, chấp thuận trước khi chuyển dữ liệu cốt lõi ra nước ngoài theo NĐ 165 Đ12 k5 và NĐ 363 Đ19 k3 b) không? Cần đối chiếu bản text QĐ 20.
12. **Dữ liệu nhạy cảm chuyên biệt khác**: sức khỏe tâm thần (Luật KCB có bắt buộc chữa bệnh Đ82 nhưng chưa thấy quy định bảo mật riêng), hỗ trợ sinh sản/IVF (bí mật người cho tinh trùng, noãn, phôi — văn bản hướng dẫn hiện hành chưa xác minh), di truyền/gen, ma túy/cai nghiện, hiến ghép mô tạng — **chưa xác minh** trong pha này. Văn bản BYT hướng dẫn Luật HIV Đ30 k7 (hình thức, quy trình thông báo) và VBHN mới nhất của Luật HIV chưa kiểm.
13. **Thời hạn lưu log truy cập HSBA**: ngoài NĐ 165 Đ17 k10 (≥6 tháng, chỉ cho dữ liệu cốt lõi/quan trọng) chưa thấy quy định riêng trong cụm này (khoảng trống #19 của inventory còn mở).
14. **Chưa đọc chi tiết** NĐ 330 Đ63 (quảng cáo), Đ66 (dữ liệu lớn), Đ72–79 (thẩm quyền đầy đủ); NĐ 356 nội dung chi tiết các Mẫu 01–10; NĐ 363 Đ8, 10–18, 20–21, 23–33; QĐ 2623/QĐ-TTg (chỉ gốc-meta); NĐ 169/347, NĐ 314 (gốc-meta).
15. **Cổng thông tin quốc gia về BVDLCN**: địa chỉ và thủ tục nộp trực tuyến chưa kiểm tra được.
16. **Luật 71/2020/QH14** đọc từ bản .doc đăng trên cổng TTĐT Công an tỉnh Đắk Lắk (bản sao) — cần đối chiếu Công báo hoặc VBHN.
