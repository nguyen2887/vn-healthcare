# TELE — KCB từ xa, app sức khỏe, thương mại điện tử và AI

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám làm KCB từ xa/hỗ trợ từ xa; nền tảng kết nối bác sĩ, app sức khỏe, nhà thuốc online (phần TMĐT); vendor và BV/PK có tính năng AI · Research gốc: `research/deep/TELE-AI.md`

Phạm vi: KCB từ xa và hỗ trợ KCB từ xa (Luật KCB Đ80, NĐ 96/2023 Đ87–88, TT 30/2023); BHYT cho KCB từ xa (NĐ 96 Đ87 k8–10, dự thảo TT BHYT dự kiến 01/01/2027); kê đơn sau phiên từ xa; nghĩa vụ TMĐT của app/website (Luật TMĐT 122/2025, NĐ 248/2026); Luật AI 134/2025, NĐ 142/2026, QĐ 33/2026/QĐ-TTg, TT 05/2026/TT-BKHCN.
Không lặp: cấp độ ATTT, lưu dữ liệu tại VN, xác thực → ANM-R02, R19, R20. Đồng ý, xuyên biên giới, GCN dịch vụ xử lý DLCN, AI trên dữ liệu BN → DLCN-R03, R15, R22, R24, R25, R26, R29. Đơn điện tử, đơn N/H, bán thuốc TMĐT → DUOC-R07–R08, R11–R14, R29. Định danh, ký, lưu HSBA → EMR-R05, R06, R09, R22. Sổ SKĐT → SKDT-R01. Mã loại hình 14 → BHYT-DATA-R14. Phần mềm/AI là thiết bị y tế → CLS-R23–R27. Không phải ý kiến pháp lý.

## Tóm tắt nhanh

- **Văn bản đúng là TT 30/2023/TT-BYT** (danh mục 50 bệnh/tình trạng được chữa bệnh từ xa) + **NĐ 96/2023 Đ87–88**. Không có "TT 30/2025 về KCB từ xa" (TELE-R04).
- Chỉ **cơ sở KCB có GPHĐ đã công bố đủ điều kiện** mới được KCB từ xa; app công nghệ không phải cơ sở KCB không tự cung cấp. Mỗi phiên phải gắn cơ sở chịu trách nhiệm, bác sĩ đúng giờ/phạm vi đã đăng ký (TELE-R02, R03).
- **BHYT hiện chỉ trả khi người bệnh đến một cơ sở** để được cơ sở khác KCB từ xa; không trả thí điểm; khám trực tiếp từ nhà qua app là thỏa thuận. Dự thảo TT BHYT (dự kiến 01/01/2027) giữ nguyên mô hình (TELE-R10).
- TMĐT: NĐ 52/2013 và NĐ 85/2021 hết HL 01/07/2026 (NĐ 248 thay); nền tảng kinh doanh trực tiếp nay **thông báo UBND tỉnh**, không còn Bộ Công Thương. **Hạn 30/06/2027** làm lại hồ sơ cho nền tảng đã xác nhận theo NĐ 52; **01/01/2027** sàn trung gian phải xác thực danh tính người bán (TELE-R14, R17, R18).
- AI: Danh mục rủi ro cao (QĐ 33/2026) mục y tế **chỉ có 2 dòng rô-bốt**; CDSS, AI đọc ảnh, chatbot không có tên. Chatbot hướng người bệnh nhiều khả năng **rủi ro trung bình → thông báo Bộ KH&CN trước khi dùng** (TELE-R22, R23).
- Hạn tuân thủ AI: **01/09/2027** cho AI y tế đã chạy trước 01/03/2026; **01/03/2027** cho AI rủi ro cao đưa vào hoạt động 15/08/2026–15/02/2027 (sớm hơn hệ thống cũ); AI trung bình/thấp go-live sau 01/03/2026 áp ngay (TELE-R25).
- Sự cố AI nghiêm trọng: báo sơ bộ **72 giờ / 05 ngày làm việc**, chính thức **15 ngày** (TELE-R29).

## Mục lục

| ID | Tiêu đề | ID | Tiêu đề |
|---|---|---|---|
| TELE-R01 | Phân biệt 4 mô hình dịch vụ từ xa | TELE-R18 | Chuyển tiếp NĐ 52 → hạn 30/06/2027 |
| TELE-R02 | Chỉ cơ sở KCB đã công bố mới được cung cấp | TELE-R19 | App sức khỏe: ma trận nghĩa vụ |
| TELE-R03 | Người hành nghề đúng phạm vi, giờ, cơ sở | TELE-R20 | Quảng bá dịch vụ y tế |
| TELE-R04 | Chữa bệnh từ xa trong 50 bệnh TT 30/2023; thí điểm có hạn mức | TELE-R21 | Kiểm kê và tự phân loại AI |
| TELE-R05 | Trách nhiệm chuyên môn và HSBA phiên từ xa | TELE-R22 | Phạm vi rủi ro cao trong y tế (QĐ 33) |
| TELE-R06 | Kê đơn sau phiên từ xa | TELE-R23 | Rủi ro trung bình: thông báo trước khi dùng |
| TELE-R07 | Hồ sơ minh chứng hạ tầng | TELE-R24 | Minh bạch, đánh dấu, gắn nhãn |
| TELE-R08 | Hợp đồng giữa các cơ sở | TELE-R25 | Hạn tuân thủ AI |
| TELE-R09 | Định giá, thu tiền theo mô hình | TELE-R26 | Con người giám sát AI |
| TELE-R10 | BHYT cho KCB từ xa | TELE-R27 | Nghĩa vụ AI rủi ro cao (rô-bốt) |
| TELE-R11 | Hỗ trợ và hội chẩn từ xa | TELE-R28 | Bên triển khai: phân loại lại, hợp đồng |
| TELE-R12 | Ghi âm/ghi hình phiên | TELE-R29 | Báo cáo sự cố AI |
| TELE-R13 | Định danh BN, xác thực bác sĩ | TELE-R30 | Dữ liệu huấn luyện hợp pháp |
| TELE-R14 | Loại nền tảng TMĐT, thông báo/đăng ký | TELE-R31 | Cấm AI thao túng |
| TELE-R15 | Nội dung công khai, chính sách, đồng ý | TELE-R32 | Khung đạo đức AI |
| TELE-R16 | Lưu dữ liệu giao dịch TMĐT | TELE-R33 | Đánh giá tác động AI ở cơ quan nhà nước |
| TELE-R17 | Nền tảng trung gian | | |
| TELE-P01…P09 | Pattern: cổng kiểm tra phiên, danh mục ICD + thí điểm, engine giá, e-Rx theo mode, tách TMĐT/y khoa, sổ AI, human-in-the-loop, nhãn AI, sự cố hợp nhất | | |
| TELE-A01…A35 | Checklist audit | | |

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ2 k19, Đ7, Đ36–38, Đ62–64, Đ80 | 01/01/2024 | Còn HL; Luật 112/2025, 113/2025 không sửa Đ80 | gốc | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 96/2023/NĐ-CP | Chi tiết Luật KCB: Đ39, **Đ87 (KCB từ xa), Đ88 (hỗ trợ)**, Đ147 | 01/01/2024 (đăng tải lên HTTT quản lý KCB từ 01/01/2027) | Còn HL; Đ87–88 chưa bị sửa (NQ 21/2026 không đụng) | gốc-OCR (Đ87 đối chiếu ảnh) | [VB 209491](https://vanban.chinhphu.vn/?pageid=27160&docid=209491) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/01/96-nd.signed.pdf) |
| 30/2023/TT-BYT (30/12/2023) | Danh mục 50 bệnh, tình trạng bệnh được KCB từ xa (chuyên khoa, ICD-10) | 01/01/2024 | Còn HL; không bãi bỏ văn bản nào | gốc-OCR | [PDF (BVĐK Bạc Liêu)](https://bvdkbaclieu.gov.vn/upload/1000079/20240107/261_Thong_tu_302023TT-BYT_cua_Bo_Y_te_quy_dinh_danh_muc_benh__tinh_trang_benh_duoc_kham_benh__chua_benh_tu_xa_84bb708446.pdf) |
| 49/2017/TT-BYT (28/12/2017) | Hoạt động y tế từ xa (tư vấn, hội chẩn, CĐHA/GPB từ xa) | 15/02/2018 | **Chưa rõ**: không thấy văn bản bãi bỏ; căn cứ chỉ NĐ 75/2017 | thứ cấp | [luatvietnam](https://luatvietnam.vn/y-te/thong-tu-49-2017-tt-byt-bo-y-te-158562-d1.html) |
| 53/2014/TT-BYT | Điều kiện hoạt động y tế trên môi trường mạng | 01/03/2015 (thứ cấp) | Chưa rõ; có thể hết HL 01/07/2026 cùng Luật CNTT (suy luận) | chưa xác minh | link chưa kiểm tra được |
| Dự thảo TT thanh toán BHYT KCB y học gia đình, tại nhà, từ xa (Vụ BHYT) | Đ4 (từ xa), Đ5 (hỗ trợ), Đ6 k1 HL dự kiến 01/01/2027; PL3 kế thừa TT 30/2023 | — | **Dự thảo**; bản 04/08/2026; vòng ý kiến mới CV 7409/BYT-BH 01/10/2026 (bản này chưa đọc) | gốc (bản dự thảo) | [Toàn văn dự thảo](https://xaydungchinhsach.chinhphu.vn/toan-van-du-thao-thong-tu-quy-dinh-thanh-toan-bao-hiem-y-te-doi-voi-kham-chua-benh-y-hoc-gia-dinh-tai-nha-tu-xa-119260804164624105.htm) · [SYT Đồng Nai](https://syt.dongnai.gov.vn/vi/news/thong-bao/xin-y-kien-gop-y-du-thao-thong-tu-quy-dinh-thanh-toan-bao-hiem-y-te-doi-voi-kham-benh-chua-benh-y-hoc-gia-dinh-tai-nha-tu-xa-44038.html) |
| 26/2025/TT-BYT | Đơn thuốc ngoại trú: Đ6 k2, Đ7–9 (N, H), Đ10 (đơn điện tử) | 01/07/2025 | Còn HL; không có điều riêng cho kê đơn từ xa | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf) |
| 90/2026/NĐ-CP | Xử phạt VPHC y tế: Đ4, Đ38 k4, Đ39 k6, Đ59 | 15/05/2026 | Còn HL; không có hành vi riêng về KCB từ xa | gốc-OCR (chỉ diễn giải) | [VB 217386](https://vanban.chinhphu.vn/?pageid=27160&docid=217386) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| 122/2025/QH15 | Luật TMĐT: Đ3, Đ5 k5, Đ11–17, Đ41 | 01/07/2026 | Còn HL | gốc-OCR | [VB 216503](https://vanban.chinhphu.vn/?pageid=27160&docid=216503) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat122.2025.qh15.pdf) |
| 248/2026/NĐ-CP (30/06/2026) | Chi tiết Luật TMĐT: Đ4–16, Đ23–30, Đ52 (bãi bỏ NĐ 52/2013, NĐ 85/2021), Đ53 (chuyển tiếp) | 01/07/2026; xác thực danh tính người bán từ 01/01/2027 | Còn HL | gốc-OCR | [VB 218747](https://vanban.chinhphu.vn/?pageid=27160&docid=218747) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/248-ndcp.signed.pdf) |
| 52/2013/NĐ-CP; 85/2021/NĐ-CP | TMĐT (cũ) | — | **Hết HL 01/07/2026** (NĐ 248 Đ52 k3); xác nhận cũ dùng đến 30/06/2027 (Đ53) | gốc-OCR (qua NĐ 248) | — |
| 134/2025/QH15 | Luật Trí tuệ nhân tạo | 01/03/2026 (Đ34), trừ Đ35 | Còn HL | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-134-2025-qh15-468694.htm) · [PDF](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/26/l134signed-176941401701024378539.pdf) |
| 142/2026/NĐ-CP (30/04/2026) | Chi tiết Luật AI: phân loại, hồ sơ, thông báo, đánh giá sự phù hợp, minh bạch, sự cố, đánh giá tác động | 01/05/2026 | Còn HL | gốc-OCR | [VB 218029](https://vanban.chinhphu.vn/?pageid=27160&docid=218029) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/142-2026-ndcp.signed.pdf) |
| 33/2026/QĐ-TTg (30/06/2026) | Danh mục hệ thống AI rủi ro cao (mục III y tế: 2 dòng rô-bốt) | 15/08/2026 | Còn HL | gốc-OCR (đối chiếu ảnh trang PL) | [VB 218658](https://vanban.chinhphu.vn/?pageid=27160&docid=218658) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/33-qdttg.signed.pdf) |
| 05/2026/TT-BKHCN | Khung đạo đức AI quốc gia (PL II phiếu tự đánh giá) | 10/03/2026 | Còn HL; bắt buộc với AI phục vụ QLNN/dịch vụ công, tổ chức khác khuyến khích | gốc | [VB 217165](https://vanban.chinhphu.vn/?pageid=27160&docid=217165) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/05-bkhcn.pdf) |
| 21/2026/NQ-CP (29/04/2026) | Cắt giảm điều kiện kinh doanh, TTHC lĩnh vực y tế | 29/04/2026 | Còn HL; không sửa NĐ 96 Đ87–88 | gốc-OCR | [VB 217977](https://vanban.chinhphu.vn/?pageid=27160&docid=217977) |
| 32/2023/TT-BYT | Đ53 k2: danh sách văn bản hết HL (không có TT 49/2017) | 01/01/2024 | Còn HL; TT 25/2026 sửa nhưng không đụng KCB từ xa | gốc | [PDF](https://bvbnd.vn/wp-content/uploads/2024/01/32-thongtuhuongdanluatkbcb31122023_91202410.pdf) · [TT 25/2026](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/25-byt.signed.pdf) |

## 2. Yêu cầu

### A. KCB từ xa

### TELE-R01 — Phân biệt 4 mô hình dịch vụ từ xa, gắn đúng cho từng lượt
- **Căn cứ**: Luật KCB Đ2 k19: KCB từ xa là KCB không trực tiếp tiếp xúc giữa người hành nghề và người bệnh, thực hiện qua thiết bị, CNTT; Đ80 k1 (người hành nghề ↔ người bệnh), k2 (hỗ trợ giữa các cơ sở); Đ64 k3 b (hội chẩn từ xa). NĐ 96 Đ87 k9 (người bệnh đến một cơ sở tiếp nhận để được cơ sở khác KCB từ xa), k10 (không qua cơ sở khác), Đ88 (hỗ trợ).
- **Áp dụng**: mọi cơ sở KCB, vendor nền tảng · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC (mỗi mô hình có điều kiện, trách nhiệm, thanh toán khác nhau).
- **Phần mềm phải**: trường `remote_mode` ∈ {`DIRECT_TO_PATIENT` (Đ87 k10), `VIA_RECEIVING_FACILITY` (Đ87 k9), `INTER_FACILITY_SUPPORT` (Đ88), `TELECONSULT_MDT` (Luật Đ64)}; giá, BHYT, chữ ký, người chịu trách nhiệm suy ra từ trường này (R09–R11).
- **Bẫy**: "tư vấn sức khỏe" qua chat/video có đánh giá tình trạng sức khỏe vẫn có thể là KCB từ xa theo Đ2 k19 (suy luận). TT 49/2017 tách "tư vấn y tế từ xa" nhưng hiệu lực chưa rõ.

### TELE-R02 — Chỉ cơ sở KCB có giấy phép, đã công bố đủ điều kiện KCB từ xa, mới được cung cấp
- **Căn cứ**: NĐ 96 Đ87 k1: điều kiện gồm (a) do người hành nghề của cơ sở KCB thuộc hình thức tổ chức tại Đ39 thực hiện; (b) phạm vi chuyên môn phù hợp; (c) đủ người hành nghề; (d) hạ tầng, thiết bị, phần mềm bảo đảm truyền tải, hiển thị, xử lý, lưu trữ dữ liệu an toàn, bảo mật. Đ87 k2 (hồ sơ công bố gồm danh mục dịch vụ KCB từ xa, tài liệu minh chứng điểm d); k3 (nộp BYT hoặc cơ quan y tế tỉnh; trong 10 ngày đăng tải; quá 10 ngày không có văn bản thì được bắt đầu — k3 d; thay đổi thì công bố lại — k3 đ). Luật KCB Đ7 k15 a, c. NĐ 90 Đ39 k6 a, b (gốc-OCR, diễn giải: 40–50 triệu với cá nhân; tổ chức ×2).
- **Áp dụng**: BV, PK, cơ sở CLS; doanh nghiệp vận hành app kết nối bác sĩ · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (1) bảng `facility_tele_registration` (cơ quan tiếp nhận, ngày phiếu, ngày được bắt đầu = min(ngày đăng tải, phiếu + 10 ngày), danh mục dịch vụ đã công bố); (2) chỉ mở bán/đặt lịch dịch vụ trong danh mục đã công bố; (3) thêm dịch vụ từ xa mới, đổi người hành nghề/hạ tầng → cờ "phải công bố lại", khóa dịch vụ mới; (4) nền tảng đa cơ sở: mỗi phiên gắn `facility_id` của cơ sở chịu trách nhiệm chuyên môn.
- **Bẫy**: bác sĩ có giấy phép tư vấn qua app của công ty công nghệ (không phải cơ sở KCB) là sai mô hình: điều kiện Đ87 k1 a gắn với cơ sở. NĐ 90 không có hành vi riêng "KCB từ xa khi chưa công bố"; khả năng áp Đ39 k6 b (suy luận). Đăng tải lên HTTT quản lý KCB bắt đầu 01/01/2027 (NĐ 96 Đ147 k2).

### TELE-R03 — Người hành nghề: đúng phạm vi, đã đăng ký hành nghề tại cơ sở, không trùng giờ
- **Căn cứ**: Luật KCB Đ80 k1 a (theo phạm vi hành nghề); Đ7 k4, k5 (cấm ngoài phạm vi; cấm hành nghề ngoài thời gian, địa điểm đã đăng ký); Đ36 k1 (nhiều cơ sở nhưng không trùng thời gian); Đ37; Đ38 k1 b. NĐ 90 Đ38 k4 a, đ; Đ39 k2 a, k4 a.
- **Áp dụng**: cơ sở KCB, nền tảng · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: lịch trực từ xa chỉ trong khung giờ đã đăng ký tại cơ sở; kiểm chồng giờ giữa các cơ sở trên cùng nền tảng; chặn dịch vụ/chuyên khoa ngoài phạm vi hành nghề; lưu số giấy phép hành nghề trên mỗi phiên.
- **Bẫy**: "khám online ngoài giờ" từ nhà bác sĩ là rủi ro nếu khung giờ chưa đăng ký (suy luận). Danh sách công khai trên HTTT quản lý KCB: HTTT-BC-R06.

### TELE-R04 — Chữa bệnh từ xa chỉ với 50 bệnh/tình trạng của TT 30/2023; ngoài danh mục phải được duyệt thí điểm, giới hạn số ca
- **Căn cứ**: Luật KCB Đ80 k1 a: "việc chữa bệnh từ xa phải theo danh mục bệnh, tình trạng bệnh do Bộ trưởng Bộ Y tế ban hành". TT 30/2023 Đ1 + PL (gốc-OCR): 50 dòng, mỗi dòng có chuyên khoa và mã ICD-10, ví dụ E66; J00, J31.1; K12.0, K14.1, K06.9; M25.5, M53.1, M54.5, M05.0, M17, M47, M81; Z09; Z08; I10; I83, I87.2, I74.3; E10.9–E14.9; E78; E00–E07; N18.1; J45; J44; F28.8; F41.2; L01, L02, L66; B86, B35, B36.0; B01, B02; L20, L23, L28.2, L50; G20; F00, F01; G43; G44.2; H81; B24; Z76.0 + A15–A19; A97.0; cúm; U07.1; K29; K59; K21; B16, B18.1; H10; H16; H35.5; Z50.1. NĐ 96 Đ87 k4–k7 (ngoài danh mục: hồ sơ thí điểm, thẩm định 30 ngày, văn bản cho phép ghi rõ số ca, báo cáo sau thí điểm).
- **Áp dụng**: cơ sở KCB, vendor · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (1) `tele_allowed_icd` nạp từ TT 30/2023, có phiên bản, so khớp theo tiền tố/dải mã; (2) đóng phiên có chẩn đoán/chỉ định điều trị: chẩn đoán chính phải thuộc danh mục hoặc một `pilot_approval` còn hạn (số văn bản, ICD, hạn mức ca, bộ đếm); (3) không thỏa thì chỉ đóng phiên dạng "khám/tư vấn, hẹn khám trực tiếp", không kê đơn điều trị (cách làm là suy luận).
- **Bẫy**: (1) Luật chỉ ràng buộc danh mục cho **chữa bệnh** từ xa; ranh giới thực tế: có kê đơn/chỉ định điều trị thì coi là chữa bệnh (suy luận, mục 7). (2) OCR TT 30 mất/sai một số mã: I10 và Z76.0 lấy theo PL3 dự thảo TT BHYT (có lớp chữ); mã cúm PL3 ghi "J19; J10; J10.1" ("J19" nhiều khả năng lỗi đánh máy, chưa xác minh); dòng 15 dự thảo khác chữ TT 30. Nạp danh mục phải đối chiếu bản gốc. (3) PL đánh số 1–50; báo hay ghi "46 bệnh".

### TELE-R05 — Trách nhiệm chuyên môn và HSBA phiên từ xa
- **Căn cứ**: Luật KCB Đ80 k1 b: "Người hành nghề phải chịu trách nhiệm về kết quả chẩn đoán bệnh, chỉ định phương pháp chữa bệnh và kê đơn thuốc của mình". Đ62 k2 a; Đ63 k1 b; Đ69; Đ7 k10. Hồ sơ, ký, lưu: EMR-R03–R06, R10, R22.
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: phiên từ xa sinh một lượt KCB đầy đủ (định danh BN, lý do, thăm khám qua video/ảnh/thiết bị, chẩn đoán ICD-10, chỉ định, đơn), người hành nghề, thời điểm bắt đầu/kết thúc, kênh (video/thoại/chat), thiết bị đo từ xa; ký số (EMR-R06); đẩy Sổ SKĐT (SKDT-R01).
- **Bẫy**: chưa có mẫu HSBA riêng cho KCB từ xa; dự thảo TT BHYT Đ8 k2 giao Cục QLKCB ban hành mẫu — theo dõi.

### TELE-R06 — Kê đơn sau phiên từ xa
- **Căn cứ**: Luật KCB Đ80 k1 b, Đ63 k2. TT 26/2025 Đ6 k2 (số định danh nếu có), Đ7 k1 (đơn "N" dùng tại cơ sở có giường bệnh), Đ7 k3 (cam kết sử dụng thuốc gây nghiện), Đ8 k2 (ung thư tại nhà: xác nhận của Trạm trưởng TYT xã cho từng lần kê), Đ9 (đơn "H"), Đ10 (đơn điện tử ký số). Cấm bán lẻ thuốc kê đơn qua TMĐT: DUOC-R29.
- **Áp dụng**: cơ sở KCB, nền tảng có chức năng giao thuốc · **Hiệu lực/hạn**: TT 26 từ 01/07/2025.
- **Mức**:
  - BẮT BUỘC — đơn điện tử, liên thông (DUOC-R11–R14); không bán lẻ thuốc kê đơn qua app.
  - BẮT BUỘC? — chặn đơn N/H trong phiên từ xa (không có điều cấm trực tiếp, nhưng cam kết, xác nhận TYT khó đáp ứng từ xa).
- **Phần mềm phải**: (1) đơn từ xa đi chung pipeline đơn điện tử, gửi Hệ thống đơn thuốc quốc gia; (2) mặc định chặn thuốc gây nghiện, hướng thần, tiền chất ở `DIRECT_TO_PATIENT`, chỉ mở khi có cam kết và xác nhận TYT đính kèm; (3) "giao thuốc tận nhà" không thành bán lẻ thuốc kê đơn qua app; cơ sở tự cấp phát thì tách khỏi luồng TMĐT, có căn cứ riêng (suy luận).
- **Bẫy**: Z08 (chăm sóc giảm nhẹ sau ung thư) có trong TT 30 nhưng đơn N tại nhà vẫn cần xác nhận TYT mỗi lần. Nhân viên mang thuốc tới nhà (dự thảo TT BHYT Đ3 k7 a) là KCB tại nhà, không phải từ xa.

### TELE-R07 — Hạ tầng, an toàn, lưu trữ: có tài liệu minh chứng nộp kèm hồ sơ công bố
- **Căn cứ**: NĐ 96 Đ87 k1 d (hạ tầng, thiết bị, phần mềm; truyền tải, xử lý, lưu trữ an toàn, bảo mật; bảo đảm thời gian lưu trữ, dự phòng dữ liệu theo pháp luật), k2 đ. Mức an ninh: ANM-R02, ANM-R19; DLCN-R15 (video/cloud nước ngoài).
- **Áp dụng**: vendor nền tảng, cơ sở KCB · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC (có tài liệu minh chứng); thông số cụ thể theo ANM, DLCN.
- **Phần mềm phải**: vendor cấp "bộ hồ sơ minh chứng Đ87 k1 d": sơ đồ kiến trúc, nơi đặt dữ liệu, mã hóa khi truyền (video, chat, file) và khi lưu, sao lưu/dự phòng, thời hạn lưu theo loại dữ liệu (HSBA theo EMR-R22), kết quả phân loại cấp độ (ANM-R02), nhà cung cấp phụ (video, SMS, cloud).
- **Bẫy**: NĐ 96 không nêu băng thông, độ phân giải. Các con số 4 Mbps, HD, lưu 10 năm nằm ở TT 49/2017 (hiệu lực chưa rõ) → chỉ là thực hành tốt (R12).

### TELE-R08 — Hợp đồng giữa cơ sở KCB từ xa và cơ sở tiếp nhận / được hỗ trợ
- **Căn cứ**: NĐ 96 Đ87 k11 (nội dung tối thiểu: trách nhiệm, quyền lợi; hạ tầng, thiết bị, phần mềm, ATTT; lưu trữ, dự phòng dữ liệu; chi phí dịch vụ; mức thỏa thuận chi phí giữa các cơ sở); Đ88 k1 b. Luật KCB Đ80 k2 b.
- **Áp dụng**: mạng lưới BV tuyến trên – tuyến dưới, chuỗi PK, nền tảng kết nối cơ sở · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: lưu `tele_contract` (hai bên, hiệu lực, dịch vụ, đơn giá, điều khoản dữ liệu); chặn phiên `VIA_RECEIVING_FACILITY`/`INTER_FACILITY_SUPPORT` khi không có hợp đồng hiệu lực; đối soát chi phí theo kỳ.

### TELE-R09 — Định giá và thu tiền theo mô hình
- **Căn cứ**: NĐ 96 Đ87 k8 (a: giá khám theo giá phê duyệt tại cơ sở KCB từ xa; b: ngày giường, DVKT theo giá tại cơ sở tiếp nhận; c: thuốc, TBYT, máu theo chi phí hợp lý), k9 (cơ sở tiếp nhận thu của người bệnh rồi thanh toán cho cơ sở từ xa theo hợp đồng), k10 (không qua cơ sở khác: thỏa thuận hai bên); Đ88 k4 (hỗ trợ: giá theo cơ sở được hỗ trợ, trả phí hỗ trợ theo hợp đồng).
- **Áp dụng**: cơ sở KCB, module viện phí · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: engine giá chọn bảng giá theo (`remote_mode`, cấu phần); sinh bút toán phải trả cho cơ sở từ xa; `DIRECT_TO_PATIENT` hiển thị giá thỏa thuận trước khi người bệnh xác nhận (R15).

### TELE-R10 — BHYT cho KCB từ xa: chỉ qua cơ sở tiếp nhận; không trả thí điểm; dự thảo 2027 giữ mô hình
- **Căn cứ**: NĐ 96 Đ87 k9: Quỹ BHYT thanh toán khi người bệnh đến một cơ sở để được cơ sở khác KCB từ xa; "Quỹ bảo hiểm y tế không thanh toán chi phí trong trường hợp thí điểm chữa bệnh từ xa"; k10: không qua cơ sở khác → thỏa thuận (suy luận: ngoài BHYT). Dự thảo TT BHYT (bản 04/08/2026): Đ4 k1 (Quỹ chỉ trả khi người bệnh đến một cơ sở), k2 (cả hai cơ sở có hợp đồng KCB BHYT), k3 (người bệnh được thông tin; chỉ thực hiện DVKT sau khi người bệnh đồng ý), k4 (danh mục = PL3 kế thừa TT 30/2023), k6 d (chi phí CNTT kết cấu vào giá DVKT từ xa); Đ5; Đ6 k1 (HL 01/01/2027); Đ8 k5 b (cơ sở cập nhật phần mềm gửi mã, chi phí). Mã loại hình 14: BHYT-DATA-R14.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: NĐ 96 từ 01/01/2024; dự thảo dự kiến 01/01/2027.
- **Mức**:
  - BẮT BUỘC — theo NĐ 96.
  - BẮT BUỘC? — phần dự thảo (chưa ban hành).
- **Phần mềm phải**: (1) không đẩy hồ sơ BHYT cho lượt `DIRECT_TO_PATIENT` và lượt thí điểm; (2) lượt `VIA_RECEIVING_FACILITY`: XML do cơ sở tiếp nhận lập (suy luận từ k9), mã loại hình 14; (3) chuẩn bị bước "đồng ý của người bệnh trước DVKT" có bằng chứng; mã dịch vụ từ xa có cấu phần CNTT khi BYT ban hành giá.
- **Bẫy**: tin báo nói dự thảo "yêu cầu video, HSBA điện tử, ký số" — bản 04/08/2026 không có câu nào như vậy; bản 01/10/2026 chưa đọc. Có mã 14 không có nghĩa Quỹ trả mọi lượt từ xa.

### TELE-R11 — Hỗ trợ KCB từ xa và hội chẩn từ xa
- **Căn cứ**: Luật KCB Đ80 k2 a (người hành nghề tại cơ sở được hỗ trợ chịu trách nhiệm kết quả KCB của mình); Đ64 k1: "Kết quả hội chẩn phải được thể hiện bằng văn bản và được lưu trữ trong hồ sơ bệnh án"; k4. NĐ 96 Đ88 k2 (người bệnh được thông tin về dịch vụ hỗ trợ), k3 (cơ sở hỗ trợ báo cáo hằng năm cho cơ quan quản lý).
- **Áp dụng**: BV tuyến trên, BV vệ tinh, cơ sở được hỗ trợ · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: biên bản hội chẩn/hỗ trợ từ xa có cấu trúc trong HSBA của cơ sở được hỗ trợ (người tham gia hai đầu, kết luận, ký số); ghi đã thông tin người bệnh; báo cáo năm (số ca theo cơ sở, dịch vụ, chi phí).
- **Bẫy**: quyết định cuối thuộc người hành nghề tại chỗ; ý kiến tuyến trên không tự động thành y lệnh.

### TELE-R12 — Ghi âm/ghi hình phiên từ xa
- **Căn cứ**: Luật KCB Đ80, NĐ 96 Đ87–88 không yêu cầu ghi hình phiên. TT 49/2017 (thứ cấp, hiệu lực chưa rõ) có yêu cầu hệ thống ghi dữ liệu lưu tối thiểu 10 năm (Đ4 k3), ít nhất một điểm hội chẩn có hệ thống ghi (Đ7 k2). Ghi âm/hình là xử lý DLCN nhạy cảm: DLCN-R03, DLCN-R29.
- **Áp dụng**: cơ sở KCB, vendor · **Hiệu lực/hạn**: —.
- **Mức**:
  - NÊN — ghi hội chẩn từ xa; ghi phiên khi có đồng ý.
  - BẮT BUỘC — nếu đã ghi thì tuân thủ DLCN, lưu đúng thời hạn.
- **Phần mềm phải**: cấu hình ghi theo loại phiên; thông báo, lấy đồng ý trước khi ghi; bản ghi gắn lượt KCB, mã hóa, phân quyền như HSBA, thời hạn theo EMR-R22; log truy cập.

### TELE-R13 — Định danh người bệnh và xác thực bác sĩ
- **Căn cứ**: không có điều riêng cho KCB từ xa. Áp dụng chung: TT 26/2025 Đ6 k2; EMR-R05, EMR-R09; SKDT-R04 (VNeID); ANM-R20; ANM-R10, DLCN-R24 (MFA nhân viên); DUOC-R11 (ký số đơn).
- **Áp dụng**: mọi nền tảng · **Hiệu lực/hạn**: đang áp dụng.
- **Mức**:
  - BẮT BUỘC — định danh trên đơn, ký số đơn.
  - NÊN — eKYC qua VNeID/căn cước trước phiên đầu; đối chiếu khuôn mặt đầu phiên.
- **Phần mềm phải**: tài khoản BN xác thực SĐT VN hoặc VNeID, phiên đầu đối chiếu số định danh; bác sĩ đăng nhập MFA, ký đơn bằng chữ ký số cá nhân; trước phiên hiển thị họ tên, chức danh, số giấy phép hành nghề, cơ sở chịu trách nhiệm; trẻ em/người mất năng lực ghi người đại diện (DLCN-R08).

### B. App, website, nền tảng TMĐT

### TELE-R14 — Xác định loại nền tảng TMĐT: kinh doanh trực tiếp (thông báo UBND tỉnh) hay trung gian (đăng ký Bộ Công Thương)
- **Căn cứ** (gốc-OCR, diễn giải): Luật TMĐT Đ3 k3 (kinh doanh trực tiếp), k4 (trung gian), k8 (chức năng đặt hàng = giao kết hợp đồng điện tử); Đ14 k1 (trực tiếp có đặt hàng: thông báo trước khi vận hành), k2 (trung gian: pháp nhân, đăng ký trước khi vận hành); Đ5 k5 (KCB, dược là ngành nghề có điều kiện). NĐ 248 Đ23–24 (thông báo, UBND tỉnh xác nhận — Đ24 k5; sửa đổi trong 20 ngày làm việc khi đổi tên miền/app, người phụ trách, nội dung công khai), Đ25–30 (đăng ký với Bộ Công Thương).
- **Áp dụng**: PK/BV tư bán gói khám, đặt lịch có trả phí; nhà thuốc online; app kết nối nhiều PK/bác sĩ · **Hiệu lực/hạn**: 01/07/2026.
- **Mức**:
  - BẮT BUỘC — tư nhân.
  - BẮT BUỘC? — app của BV công thu viện phí (có phải "hoạt động thương mại" không, mục 7).
- **Phần mềm phải**: cấu hình nền tảng có loại nền tảng, có/không chức năng đặt hàng, số và ngày xác nhận; footer/"Giới thiệu" hiển thị thông tin xác nhận; release checklist khi đổi tên miền/tên app (20 ngày làm việc).
- **Bẫy**: cơ quan xác nhận đã đổi (NĐ 52/2013: Bộ Công Thương; nay kinh doanh trực tiếp: UBND tỉnh). App chỉ đặt lịch không thu tiền, không giao kết hợp đồng có thể không có chức năng đặt hàng (suy luận). Nhà thuốc online còn phải thông báo cơ quan quản lý dược (DUOC-R29).

### TELE-R15 — Nội dung công khai; chính sách dịch vụ, chấm dứt, hoàn tiền; tiếng Việt; đồng ý trước khi mở tài khoản
- **Căn cứ** (gốc-OCR, diễn giải): Luật TMĐT Đ11 k1 (thông tin chủ quản; chính sách bảo mật; quyền, nghĩa vụ; khiếu nại), k2 (dễ thấy, tiếng Việt), k3 (giá, chi phí, điều kiện, thanh toán; dịch vụ: phương thức cung cấp, chấm dứt, hoàn tiền), k4 (đồng ý trước khi mở tài khoản); Đ12 (rà soát trước khi đặt, xem lại sau đặt); Đ16 k1 b (công khai giấy tờ chứng minh điều kiện kinh doanh — GPHĐ, GCN đủ điều kiện kinh doanh dược). NĐ 248 Đ4–7, Đ15 (phương thức cung cấp dịch vụ, đặt trước dùng sau), Đ16 (chấm dứt, hoàn tiền).
- **Áp dụng**: như R14 · **Hiệu lực/hạn**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: trang "Điều kiện giao dịch" có phiên bản; checkbox đồng ý khi mở tài khoản, lưu phiên bản + thời điểm; màn xác nhận trước thanh toán hiển thị dịch vụ, bác sĩ/cơ sở, thời lượng, thiết bị cần, giá, chính sách hủy/hoàn tiền khi mất kết nối; mục "Giấy phép" hiển thị GPHĐ, công bố KCB từ xa (R02).

### TELE-R16 — Lưu dữ liệu giao dịch: ≥ 1 năm (tin đăng), ≥ 3 năm (hợp đồng)
- **Căn cứ** (gốc-OCR, diễn giải): Luật TMĐT Đ16 k1 d (≥ 1 năm từ khi đăng thông tin), k2 b (≥ 3 năm từ khi giao kết hợp đồng; DNNVV khởi nghiệp, siêu nhỏ, hộ kinh doanh: ≥ 1 năm trong 5 năm đầu — k2 c); Đ17 k1 e, k2 i, k2 đ (trung gian; người bán tải dữ liệu hợp đồng trong 3 năm sau khi bị khóa).
- **Áp dụng**: như R14 · **Hiệu lực/hạn**: 01/07/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: `order/contract` không xóa cứng trước hạn; snapshot dịch vụ + giá tại thời điểm đặt; công cụ export cho người bán.
- **Bẫy**: hạn TMĐT (3 năm) ngắn hơn hạn HSBA; dữ liệu y khoa theo EMR-R22. Chính sách "xóa đơn hàng sau 3 năm" không được kéo theo xóa HSBA.

### TELE-R17 — Nền tảng trung gian: xác thực người bán, kiểm duyệt trước khi hiển thị, đánh giá, khiếu nại
- **Căn cứ** (gốc-OCR, diễn giải): Luật TMĐT Đ17 k1 c (xác thực điện tử danh tính người bán trước khi cho bán), k1 đ (kiểm duyệt nội dung trước khi hiển thị), k2 g (báo trước 5 ngày trước khi hạn chế tài khoản), k2 h (cho người mua đánh giá, hiển thị đầy đủ), k3–k4 (nền tảng lớn: khiếu nại trực tuyến, có giám sát của con người). NĐ 248 Đ52 k2 (xác thực danh tính người bán từ 01/01/2027).
- **Áp dụng**: app kết nối nhiều PK/bác sĩ/nhà thuốc · **Hiệu lực/hạn**: 01/07/2026; xác thực danh tính **01/01/2027**.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: onboarding người bán bằng định danh điện tử tổ chức; kiểm GPHĐ, công bố KCB từ xa, danh sách người hành nghề trước khi duyệt; hàng đợi kiểm duyệt nội dung quảng bá (Luật KCB Đ7 k20); đánh giá bác sĩ có cơ chế ẩn đánh giá vi phạm nhưng không ẩn đánh giá xấu hợp lệ.
- **Bẫy**: Luật KCB Đ7 k21 cấm đăng thông tin quy kết trách nhiệm người hành nghề khi chưa có kết luận — xung đột với nghĩa vụ hiển thị đánh giá (suy luận, mục 7).

### TELE-R18 — Chuyển tiếp: nền tảng đã xác nhận theo NĐ 52/2013 phải làm lại trước 30/06/2027
- **Căn cứ**: Luật TMĐT Đ41 k1 (website, app đã xác nhận trước 01/07/2026 hoạt động theo nội dung đã xác nhận đến hết 30/06/2027); NĐ 248 Đ53 (trong thời gian này làm thủ tục sửa đổi, bổ sung theo NĐ 248). NĐ 52/2013, NĐ 85/2021 bị NĐ 248 bãi bỏ từ 01/07/2026.
- **Áp dụng**: PK, nhà thuốc, nền tảng đã có xác nhận theo NĐ 52 · **Hiệu lực/hạn**: **30/06/2027**.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (quy trình) rà nội dung công khai theo NĐ 248 Đ4–16, cập nhật chính sách, nộp sửa đổi/bổ sung, lưu số xác nhận mới.

### TELE-R19 — App sức khỏe thu dữ liệu trực tiếp từ người dân: tổ hợp nghĩa vụ
- **Căn cứ**: DLCN-R24 (Luật 91/2025 Đ26 k3: app y tế tuân thủ đầy đủ BVDLCN); DLCN-R22 (NĐ 356 Đ21 k4: GCN dịch vụ xử lý DLCN của BCA); ANM-R02 (cấp độ: KCB từ xa và bán thuốc online là cấp 3 — suy luận; ngưỡng "≥ 10.000 người" chỉ đúng cho dịch vụ trực tuyến, HIS nội bộ là cấp 2); ANM-R20; R14–R17 nếu bán dịch vụ; CLS-R23 nếu app tự kết luận y khoa; R21–R25 nếu dùng AI; R02 nếu có bác sĩ tư vấn.
- **Áp dụng**: app theo dõi sức khỏe, đặt lịch, tư vấn, wearable, PHR · **Hiệu lực/hạn**: theo từng nhánh.
- **Mức**: BẮT BUỘC (theo từng nhánh ở domain gốc).
- **Phần mềm phải**: "ma trận phân loại app" trước khi phát hành: có bác sĩ tư vấn? (→ KCB từ xa) · thu tiền, giao kết hợp đồng? (→ TMĐT) · thuật toán kết luận y khoa? (→ TBYT, AI) · chatbot? (→ AI trung bình) · loại dịch vụ và số chủ thể dữ liệu sức khỏe (→ cấp độ ANM) · vendor xử lý thay cơ sở KCB? (→ GCN dịch vụ xử lý DLCN). Mỗi nhánh dẫn tới checklist domain tương ứng.
- **Bẫy**: không có "giấy phép app y tế" riêng; nghĩa vụ phát sinh theo chức năng. App "tư vấn miễn phí" vẫn chịu Luật 91 và NĐ 356.

### TELE-R20 — Quảng bá dịch vụ y tế không vượt phạm vi, không gian dối
- **Căn cứ**: Luật KCB Đ7 k17 (cấm lợi dụng hình ảnh người hành nghề khuyến khích phương pháp chưa được công nhận), k20 (cấm quảng cáo vượt phạm vi, gian dối). Luật TMĐT Đ17 k1 đ. Luật Quảng cáo: chưa đọc.
- **Áp dụng**: cơ sở KCB, nền tảng · **Hiệu lực/hạn**: 01/01/2024.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: dịch vụ quảng bá chỉ chọn từ danh mục được phép (GPHĐ/công bố từ xa); kiểm duyệt từ khóa ("chữa khỏi", "cam kết 100%"); ảnh/video bác sĩ do AI tạo phải gắn nhãn (R24).

### C. Trí tuệ nhân tạo

### TELE-R21 — Kiểm kê mọi hệ thống AI và tự phân loại rủi ro trước khi đưa vào sử dụng
- **Căn cứ**: Luật AI Đ3 k2 (định nghĩa hệ thống AI), k4 (nhà cung cấp: đưa AI vào sử dụng dưới tên mình, dù tự phát triển hay của bên thứ ba), k5 (bên triển khai); Đ9 k1 (cao, trung bình, thấp); Đ10 k1: "Nhà cung cấp tự phân loại hệ thống trí tuệ nhân tạo trước khi đưa vào sử dụng" (trung bình/cao có hồ sơ phân loại); k2 (bên triển khai kế thừa; tích hợp làm rủi ro cao hơn thì phân loại lại). NĐ 142 (gốc-OCR, diễn giải): Đ6 k2 (phân loại áp cho hệ thống, không cho mô hình đứng riêng); Đ11 (phân loại lại khi thay đổi đáng kể, sự cố nghiêm trọng, Danh mục sửa; mức cao hơn thì thông báo trong 15 ngày làm việc; sửa lỗi thông thường không phải phân loại lại); Đ12 (nội dung hồ sơ; lưu suốt thời gian hệ thống hoạt động; được dùng DPIA thay/tích hợp).
- **Áp dụng**: vendor có tính năng AI; BV/PK tự xây hoặc gắn tên mình lên AI (nhà cung cấp); BV/PK dùng AI của vendor (bên triển khai) · **Hiệu lực/hạn**: 01/03/2026 (hệ thống mới); hệ thống đã chạy: R25.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: `ai_system_registry`: tên, phiên bản, vai trò, mô hình nền và bên cung cấp, mục đích, người dùng, người bị ảnh hưởng, dữ liệu đầu vào, mức rủi ro + lý do + căn cứ, ngày go-live, mã định danh do Cổng cấp, liên kết DPIA; trigger phân loại lại khi đổi mô hình, mục đích, đối tượng (TELE-P06).
- **Bẫy**: BV dùng LLM thương mại qua API rồi gắn tên BV lên chatbot → BV là nhà cung cấp, không chỉ bên triển khai.

### TELE-R22 — Rủi ro cao trong y tế theo QĐ 33/2026: chỉ AI tích hợp rô-bốt phẫu thuật/điều trị tự động
- **Căn cứ**: QĐ 33/2026 PL mục III "Lĩnh vực y tế" (gốc-OCR, đã đối chiếu ảnh trang, diễn giải), đúng 2 dòng: (1) AI hỗ trợ phẫu thuật/rô-bốt phẫu thuật — chỉ khi tích hợp vào rô-bốt tham gia trực tiếp can thiệp hoặc dẫn hướng thao tác, hoặc rô-bốt tự động hoàn toàn thay hành vi con người; đánh giá sự phù hợp theo Luật AI Đ13 k2 b (tự đánh giá hoặc thuê). (2) Rô-bốt dùng AI điều khiển tự động — chỉ khi trực tiếp thực thi tác động điều trị theo y lệnh lên người bệnh và không cần xác nhận của nhân viên y tế cho mỗi bước thay đổi thông số; theo Đ13 k2 a (bắt buộc chứng nhận bởi tổ chức). NĐ 142 Đ6 k3 a; Đ8 k2 (tiêu chí loại trừ: chỉ xử lý dữ liệu; có giám sát thực chất của con người trước khi quyết định có hiệu lực; chỉ dùng nội bộ; chỉ khuyến nghị tham khảo).
- **Áp dụng**: vendor/nhà phân phối rô-bốt phẫu thuật có AI, BV dùng · **Hiệu lực/hạn**: 15/08/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: tài liệu phân loại CDSS, AI đọc ảnh, chatbot ghi rõ "không thuộc QĐ 33/2026" và lý do; AI điều khiển thiết bị điều trị (bơm tiêm, máy thở, xạ trị tự chỉnh tham số…) bắt buộc xác nhận của nhân viên y tế cho mỗi bước thay đổi thông số để nằm ngoài dòng 2 (suy luận; "rô-bốt" chưa được định nghĩa).
- **Bẫy**: không thuộc rủi ro cao theo Luật AI không có nghĩa không phải TBYT (CLS-R23–R25). Danh mục có thể sửa; NĐ 142 Đ11 k5 cho tối đa 12 tháng hoàn thiện khi bị xếp lại, trong thời gian đó phải có giám sát của con người và nhật ký can thiệp.

### TELE-R23 — Rủi ro trung bình: chatbot/trợ lý ảo hướng người bệnh → hồ sơ phân loại, thông báo Bộ KH&CN trước khi dùng
- **Căn cứ**: Luật AI Đ9 k1 b (trung bình: có khả năng gây nhầm lẫn, tác động, thao túng do người dùng không nhận biết đang tương tác với AI hoặc nội dung do AI tạo); Đ10 k3 (trung bình, cao: thông báo kết quả phân loại cho Bộ KH&CN qua Cổng một cửa trước khi đưa vào sử dụng); Đ15 k1. NĐ 142 (gốc-OCR, diễn giải): Đ9 k1, k3 (không xếp trung bình: công cụ văn phòng người dùng biết rõ là AI; không tương tác, không cung cấp trực tiếp ra công chúng; chỉ xử lý dữ liệu trong hệ thống kỹ thuật); Đ14 (thông báo điện tử, qua Cổng hoặc API; Cổng cấp mã định danh hệ thống); Đ46 k1 (Cổng chưa vận hành thì qua kênh Bộ KH&CN công bố).
- **Áp dụng**: chatbot hỏi đáp sức khỏe, symptom checker, trợ lý đặt lịch giọng nói, tổng đài AI, avatar bác sĩ ảo · **Hiệu lực/hạn**: 01/03/2026 (Luật), 01/05/2026 (NĐ 142).
- **Mức**: BẮT BUỘC? (chatbot hướng người bệnh nhiều khả năng trung bình; CDSS, AI scribe, AI đọc ảnh chỉ cho nhân viên nhiều khả năng thấp theo Đ9 k3) (suy luận; chưa có hướng dẫn riêng cho y tế).
- **Phần mềm phải**: hồ sơ phân loại theo NĐ 142 Đ12; bản ghi đã thông báo (ngày, kênh, mã định danh); khóa go-live khi chưa có mã/biên nhận; sẵn xuất dữ liệu kê khai qua API Cổng khi có đặc tả.
- **Bẫy**: "hiển thị rõ đây là AI" không tự loại khỏi nhóm trung bình — tiêu chí là khả năng gây nhầm lẫn (suy luận). Xếp thấp thì không phải thông báo nhưng vẫn phải giải trình khi có dấu hiệu vi phạm (Luật Đ15 k2).

### TELE-R24 — Minh bạch: báo đang tương tác với AI; đánh dấu máy đọc nội dung AI tạo; gắn nhãn mô phỏng người thật
- **Căn cứ**: Luật AI Đ11 k1 (người dùng nhận biết khi tương tác với AI), k2 (âm thanh, hình ảnh, video do AI tạo đánh dấu ở định dạng máy đọc), k3, k4 (mô phỏng ngoại hình, giọng nói người thật phải gắn nhãn), k5; Đ7 k5 (cấm che giấu, tẩy xóa nhãn). NĐ 142 (gốc-OCR, diễn giải): Đ16 k2 b (thông tin mục đích, phạm vi, hạn chế), Đ17 (đánh dấu qua metadata, chữ ký số…; văn bản không bắt buộc đánh dấu máy đọc), Đ18 k3, k4 (miễn nhãn: chỉnh sửa kỹ thuật, sửa chính tả, tóm tắt, dịch không sai nội dung; nội dung chỉ dùng nội bộ).
- **Áp dụng**: mọi AI hướng người bệnh; AI sinh ảnh/giọng · **Hiệu lực/hạn**: 01/03/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: thông báo đầu phiên chatbot ("Bạn đang trò chuyện với trợ lý AI, không phải bác sĩ"), nhắc lại khi chuyển người thật ↔ AI; trang "Giới hạn của trợ lý AI"; metadata/watermark (vd C2PA, XMP) cho ảnh, audio, video AI tạo; nhãn trên video bác sĩ ảo; log `ai_disclosed_at` (TELE-P08).
- **Bẫy**: tóm tắt HSBA do AI soạn dùng nội bộ không phải gắn nhãn, nhưng vẫn cần người hành nghề duyệt (R26).

### TELE-R25 — Hạn tuân thủ cho AI y tế
- **Căn cứ**: Luật AI Đ34, Đ35 k1 a (hệ thống đã hoạt động trước khi Luật có HL: 18 tháng cho y tế, giáo dục, tài chính → 01/09/2027), k1 b (12 tháng lĩnh vực khác → 01/03/2027), k2. QĐ 33 Đ4 k1 a (AI thuộc Danh mục đã hoạt động trước 15/08/2026, lĩnh vực y tế: hoàn thành trước 01/09/2027), k3 (đưa vào hoạt động trong 6 tháng kể từ 15/08/2026: hoàn thành trước 01/03/2027, không phân biệt lĩnh vực).
- **Áp dụng**: vendor, BV/PK · **Hiệu lực/hạn**: **01/03/2027**, **01/09/2027**.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: sổ AI có `go_live_date` và hạn tính tự động: (a) go-live < 01/03/2026 → 01/09/2027; (b) rủi ro cao, 01/03/2026 ≤ go-live < 15/08/2026 → 01/09/2027; (c) rủi ro cao, 15/08/2026 ≤ go-live < 15/02/2027 → 01/03/2027; (d) trung bình/thấp go-live ≥ 01/03/2026 → áp ngay; (e) rủi ro cao go-live sau (c) → đánh giá sự phù hợp xong trước go-live (Luật Đ13 k1, k3).
- **Bẫy**: Luật ghi "18 tháng", ngày 01/09/2027 là kết quả tính. Rô-bốt AI mới lắp 10/2026 có hạn 01/03/2027, sớm hơn hệ thống cũ. Mốc cuối 15/02/2027 là suy luận về cách đếm.

### TELE-R26 — Con người giám sát; AI không thay trách nhiệm người hành nghề
- **Căn cứ**: Luật AI Đ4 k2 (AI không thay thế thẩm quyền, trách nhiệm của con người; duy trì kiểm soát, khả năng can thiệp), Đ6 k2 a (y tế), Đ7 k4 (cấm vô hiệu hóa cơ chế giám sát của con người). QĐ 33 Đ1 k2. Luật KCB Đ62 k2 a, Đ80 k1 b. DLCN-R25 (quyết định tự động phải cho yêu cầu đánh giá lại bởi con người).
- **Áp dụng**: mọi AI lâm sàng và AI hướng người bệnh · **Hiệu lực/hạn**: 01/03/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (1) đầu ra AI ở trạng thái "đề xuất", chỉ thành dữ liệu lâm sàng khi người hành nghề chấp nhận/sửa và ký; (2) log phiên bản mô hình, đầu vào, đầu ra, người duyệt, quyết định, thời điểm; (3) không có cấu hình "tự động chấp nhận" cho chỉ định điều trị/đơn; tắt AI theo khoa/người dùng có log; (4) chatbot không đưa chẩn đoán xác định, không kê đơn; luôn có lối chuyển người hành nghề; quy tắc khẩn cấp (gợi ý gọi 115) (TELE-P07).
- **Bẫy**: thiết kế này đồng thời giúp ở ngoài Danh mục (NĐ 142 Đ8 k2) và giảm rủi ro thành TBYT mức cao (CLS-R27).

### TELE-R27 — AI rủi ro cao (rô-bốt): đánh giá sự phù hợp, quản lý rủi ro, hồ sơ kỹ thuật, nhật ký, đại diện tại VN
- **Căn cứ**: Luật AI Đ13 k1 (đánh giá sự phù hợp trước khi dùng và khi thay đổi đáng kể), k2 a, b, k3 (kết quả là điều kiện đưa vào sử dụng); Đ14 k1 (quản lý rủi ro; quản trị dữ liệu; hồ sơ kỹ thuật, nhật ký hoạt động; giám sát của con người; không buộc lộ mã nguồn), k2 (bên triển khai), k6 (nhà cung cấp nước ngoài: đầu mối tại VN; nếu thuộc diện chứng nhận bắt buộc: hiện diện thương mại hoặc đại diện ủy quyền). NĐ 142 Đ13 (đánh giá lại khi đổi chức năng, kiến trúc, mô hình, nguồn dữ liệu; dùng kết quả theo luật chuyên ngành; công khai trên Cổng trước khi dùng), Đ15.
- **Áp dụng**: vendor rô-bốt phẫu thuật, BV dùng · **Hiệu lực/hạn**: 15/08/2026; hạn chuyển tiếp R25.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (vendor) hồ sơ kỹ thuật, thẻ mô hình/thẻ hệ thống, nhật ký vận hành đủ để hậu kiểm; (BV) sổ thiết bị ghi số lưu hành TBYT (CLS-R25) và kết quả đánh giá sự phù hợp AI; nhật ký mỗi ca: người vận hành, lần can thiệp/ghi đè.
- **Bẫy**: rô-bốt phẫu thuật gần như chắc là TBYT loại cao → hai hồ sơ (NĐ 98 và Luật AI); NĐ 142 Đ5 k6–7, Đ13 k3 cho dùng lại kết quả đánh giá theo luật chuyên ngành.

### TELE-R28 — Bên triển khai: dùng đúng mục đích, phân loại lại khi tùy biến, thỏa thuận trách nhiệm với nhà cung cấp
- **Căn cứ**: Luật AI Đ10 k2; Đ29 k2 (AI rủi ro cao dùng đúng vẫn gây thiệt hại → bên triển khai bồi thường, đòi nhà cung cấp hoàn trả nếu có thỏa thuận), k4; Đ14 k5 (khuyến khích bảo hiểm trách nhiệm). NĐ 142 Đ6 k4, Đ11 k2–3, Đ16 k6.
- **Áp dụng**: BV, PK, chuỗi · **Hiệu lực/hạn**: 01/03/2026.
- **Mức**:
  - BẮT BUỘC — phân loại lại khi tùy biến làm tăng rủi ro.
  - NÊN — điều khoản hoàn trả, bảo hiểm trách nhiệm.
- **Phần mềm phải**: thay đổi cấu hình AI (prompt hệ thống, ngưỡng, nguồn dữ liệu, đối tượng) có bước "có làm tăng rủi ro không"; hợp đồng mua/thuê AI có mục đích, giới hạn, nghĩa vụ thông tin minh bạch/giải trình, phối hợp sự cố, hoàn trả bồi thường.

### TELE-R29 — Sự cố nghiêm trọng do AI: báo sơ bộ 72 giờ / 05 ngày làm việc, chính thức 15 ngày
- **Căn cứ**: Luật AI Đ3 k8, Đ12 k2, k4 (qua Cổng một cửa). NĐ 142 Đ19 (gốc-OCR, diễn giải): k1 (hậu quả: tính mạng, sức khỏe, tài sản, quyền con người, gián đoạn dịch vụ thiết yếu); k2 a (bên triển khai báo nhà cung cấp); k3 (báo sơ bộ Mẫu AI01a/AI01b: 72 giờ với sự cố khẩn cấp, 05 ngày làm việc với sự cố khác, tính từ khi có đủ thông tin ban đầu; không coi là thừa nhận lỗi; không liên lạc được nhà cung cấp thì bên triển khai tự báo); k4 (lưu nhật ký; báo cáo chính thức trong 15 ngày từ báo cáo sơ bộ); k5 (trùng nghĩa vụ theo luật ANM, BVDLCN, chuyên ngành thì theo luật đó).
- **Áp dụng**: vendor AI, BV/PK dùng AI · **Hiệu lực/hạn**: 01/05/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: nút "Báo sự cố AI" trong UI lâm sàng gắn bản ghi suy luận (input hash, output, phiên bản mô hình); workflow phân loại và đồng hồ 72h/05 ngày làm việc/15 ngày; liên kết quy trình sự cố y khoa (HTTT-BC-R32–R35) và sự cố ANM (ANM-R16) (TELE-P09).
- **Bẫy**: sự cố y khoa có yếu tố AI có thể phải báo song song theo TT 43/2018 và NĐ 142; cách phối hợp chưa có hướng dẫn (mục 7).

### TELE-R30 — Dữ liệu phát triển, huấn luyện, kiểm thử AI phải hợp pháp
- **Căn cứ**: Luật AI Đ7 k3 (cấm xử lý dữ liệu cho AI trái luật dữ liệu, BVDLCN, SHTT, an ninh mạng); Đ14 k1 b. Chi tiết: DLCN-R25, R26 (khử nhận dạng, cấm tái nhận dạng), DLCN-R15 (gửi dữ liệu ra nước ngoài, kể cả gọi API LLM đặt ở nước ngoài).
- **Áp dụng**: vendor AI, BV có dự án AI · **Hiệu lực/hạn**: 01/03/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: pipeline dữ liệu huấn luyện có cổng kiểm soát (căn cứ xử lý, khử nhận dạng, phê duyệt); chặn gửi dữ liệu định danh BN tới API AI bên ngoài khi chưa có căn cứ/đánh giá chuyển dữ liệu; log dữ liệu nào vào tập huấn luyện nào.

### TELE-R31 — Không dùng AI thao túng, lợi dụng nhóm dễ bị tổn thương
- **Căn cứ**: Luật AI Đ7 k2 b (giả mạo, mô phỏng người thật để lừa dối, thao túng gây tổn hại nghiêm trọng), k2 c (lợi dụng điểm yếu của trẻ em, người cao tuổi, người khuyết tật…). TT 05/2026 Đ3 k2 b.
- **Áp dụng**: app sức khỏe có AI cá nhân hóa, upsell gói khám, chatbot bán hàng · **Hiệu lực/hạn**: 01/03/2026.
- **Mức**:
  - BẮT BUỘC — hành vi bị cấm.
  - NÊN — cơ chế phòng ngừa.
- **Phần mềm phải**: không dùng avatar/giọng bác sĩ thật do AI tạo khi bác sĩ chưa đồng ý; quy tắc nội dung chatbot: không gây sợ hãi để bán dịch vụ; đánh giá thiên lệch khi gợi ý dịch vụ cho người cao tuổi.

### TELE-R32 — Khung đạo đức AI: bắt buộc với AI phục vụ dịch vụ công, khuyến khích với tư nhân
- **Căn cứ**: Luật AI Đ26 k4, Đ27 k1 (AI trong QLNN, dịch vụ công phải tuân thủ Khung đạo đức). TT 05/2026 Đ1 k2 (áp cho AI phục vụ QLNN hoặc dịch vụ công), k3 (tổ chức khác khuyến khích), Đ3 (nguyên tắc), PL I mục 2 e (quy tắc đạo đức AI nội bộ), PL II (phiếu tự đánh giá), Đ5 k1 (rà soát 3 năm/lần).
- **Áp dụng**: BV công (nếu được coi là cung cấp dịch vụ công — mục 7); BV/PK tư, vendor · **Hiệu lực/hạn**: 10/03/2026.
- **Mức**:
  - BẮT BUỘC? — BV công.
  - NÊN — tư nhân.
- **Phần mềm phải**: phiếu tự đánh giá PL II cho từng hệ thống trong sổ AI; quy tắc đạo đức AI nội bộ; kênh phản ánh về AI trong app.

### TELE-R33 — Đánh giá tác động khi cơ quan nhà nước dùng AI rủi ro cao hoặc làm căn cứ quyết định hành chính
- **Căn cứ**: Luật AI Đ27 k2–k4 (người ra quyết định chịu trách nhiệm; lập và công khai báo cáo đánh giá tác động). NĐ 142 Đ20 (gốc-OCR, diễn giải): k1 (cơ quan nhà nước đánh giá khi hệ thống rủi ro cao hoặc kết quả là căn cứ trực tiếp ban hành quyết định hành chính), k3 (Mẫu AI02), k4 (phê duyệt trước khi dùng), k5 (công khai), k7 (tình huống: căn cứ quyết định QLNN/dịch vụ công; chấm điểm, xếp hạng; phân bổ nguồn lực; sàng lọc, giám sát).
- **Áp dụng**: Sở Y tế, BHXH (giám định tự động), BV công nếu bị coi là cơ quan nhà nước/dịch vụ công · **Hiệu lực/hạn**: 01/05/2026.
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: vendor bán cho khối nhà nước chuẩn bị dữ liệu đầu vào cho Mẫu AI02 (mô tả, rủi ro, cơ chế can thiệp) cho mỗi hệ thống.
- **Bẫy**: AI chấm điểm/ưu tiên hồ sơ (vd phát hiện gian lận BHYT tự động) rơi đúng k7 (suy luận).

**Tổng hợp mức** (theo mức cao nhất của mục): BẮT BUỘC 30 (R01–R22, R24–R31; trong đó R06, R10, R12, R13, R14, R28, R31 có phần BẮT BUỘC? hoặc NÊN tách riêng); BẮT BUỘC? 3 (R23, R32, R33); NÊN 0 làm mức cao nhất.

## 3. Pattern thiết kế

### TELE-P01 — Encounter từ xa có `remote_mode` và cổng kiểm tra pháp lý trước khi mở phiên
- **Giải quyết**: R01–R04, R08, R13
- **Cách làm**: trước "Bắt đầu phiên" kiểm theo thứ tự: (1) cơ sở có đăng ký từ xa hiệu lực, dịch vụ trong danh mục đã công bố; (2) bác sĩ đăng ký hành nghề tại cơ sở, giờ hiện tại thuộc giờ đăng ký, không chồng lịch; (3) mode cần hợp đồng → hợp đồng hiệu lực; (4) BN đã định danh.
- **Gợi ý dữ liệu**: `facility_tele_registration(facility_id, authority, receipt_no, receipt_date, published_date, effective_from, services jsonb, status)`; `practitioner_registration(practitioner_id, facility_id, license_no, scope_codes[], weekday, start_time, end_time, valid_from, valid_to)` + `EXCLUDE USING gist` trên `tstzrange` theo `practitioner_id`; `tele_contract(provider_facility_id, receiving_facility_id, type ENUM('KCB_TU_XA','HO_TRO'), services, price_terms jsonb, data_terms, valid_from, valid_to)`; `encounter.remote_mode`, `receiving_facility_id`, `contract_id`.
- **Đánh đổi**: chặn cứng có thể vướng cấp cứu → override có lý do, log, cảnh báo quản lý chuyên môn.

### TELE-P02 — Danh mục ICD được phép từ xa + thí điểm có hạn mức
- **Giải quyết**: R04, R10
- **Cách làm**: trigger tăng `cases_used` khi đóng lượt có chẩn đoán thuộc thí điểm, chặn khi đạt quota; `bhyt_eligible = false` cho lượt thí điểm.
- **Gợi ý dữ liệu**: `tele_allowed_icd(code_prefix, source ENUM('TT30_2023','DT_BHYT_PL3'), valid_from, valid_to)`; `pilot_approval(facility_id, doc_no, doc_date, icd_prefixes[], case_quota, cases_used, valid_to)`.
- **Đánh đổi**: so khớp tiền tố phải xử lý dải (A15–A19) → lưu dạng dải chuẩn hóa.

### TELE-P03 — Engine giá theo mô hình
- **Giải quyết**: R09, R10
- **Cách làm**: `price(encounter_item) → (price_source_facility, payer, amount)`: công khám theo bảng giá cơ sở từ xa; DVKT, giường theo cơ sở tiếp nhận; `DIRECT_TO_PATIENT` lấy `agreed_price` đã hiển thị khi đặt.
- **Gợi ý dữ liệu**: `interfacility_payable(contract_id, encounter_id, amount)`.
- **Đánh đổi**: hai cơ sở hai HIS khác nhau → cần API đối soát; tối thiểu xuất CSV theo kỳ.

### TELE-P04 — Đơn thuốc từ xa đi chung pipeline e-Rx, chính sách thuốc theo mode
- **Giải quyết**: R06
- **Cách làm**: mặc định BLOCK N/H/tiền chất ở `DIRECT_TO_PATIENT`; khi mở bắt đính kèm (cam kết, xác nhận TYT theo phụ lục TT 26); nút "Mua thuốc" chỉ hiện thuốc không kê đơn; thuốc kê đơn hiển thị mã đơn điện tử để mua tại nhà thuốc (DUOC-R14).
- **Gợi ý dữ liệu**: `drug_policy(drug_class ∈ {N,H,TIEN_CHAT,KE_DON,KHONG_KE_DON}, remote_mode, action ∈ {BLOCK, REQUIRE_ATTACHMENT, ALLOW})`.
- **Đánh đổi**: chặn mặc định có thể gây phiền cho chăm sóc giảm nhẹ tại nhà; cần quy trình mở có kiểm soát.

### TELE-P05 — Tách lớp TMĐT khỏi lớp y khoa
- **Giải quyết**: R14–R18
- **Cách làm**: `commerce_order` (giá, chính sách, đồng ý, lưu ≥ 3 năm, snapshot `terms_version`) liên kết 1–1 với `encounter` (HSBA, lưu theo EMR-R22); chính sách xóa/ẩn danh hai lớp độc lập.
- **Gợi ý dữ liệu**: `platform_compliance(platform_type, has_order_function, notice_or_registration_no, confirmed_by ENUM('UBND_TINH','BCT'), confirmed_date, legacy_nd52_no, legacy_deadline DATE DEFAULT '2027-06-30')`.
- **Đánh đổi**: thêm một lớp dữ liệu; đổi lại không để retention TMĐT kéo theo xóa HSBA.

### TELE-P06 — Sổ đăng ký AI và cổng go-live
- **Giải quyết**: R21–R25, R28
- **Cách làm**: CI/CD không bật tính năng `uses_ai` ở production nếu `risk_level` NULL, hoặc MEDIUM/HIGH mà `notified_at` NULL, hoặc HIGH mà `conformity_result_url` NULL.
- **Gợi ý dữ liệu**: `ai_system_registry(name, version, role ENUM('PROVIDER','DEPLOYER'), upstream_model, upstream_provider, intended_purpose, users ENUM('CLINICIAN','PATIENT','ADMIN'), affected_persons, input_data_types, risk_level ENUM('HIGH','MEDIUM','LOW'), risk_basis, qd33_row, go_live_date, compliance_deadline GENERATED, portal_id, notified_at, conformity_method, conformity_result_url, dpia_ref, ethics_self_assessment_ref, status)`.
- **Đánh đổi**: gánh nặng cho tính năng AI nhỏ → gom theo "hệ thống" (NĐ 142 Đ6 k2), không theo từng prompt.

### TELE-P07 — Human-in-the-loop có vết
- **Giải quyết**: R26, R27, R29
- **Cách làm**: dữ liệu lâm sàng chỉ nhận output AI qua review đã ký; thiết bị điều trị: mỗi thay đổi thông số cần review riêng.
- **Gợi ý dữ liệu**: `ai_inference(system_id, model_version, encounter_id, input_ref, output jsonb, created_at)`; `ai_review(inference_id, reviewer_id, decision ENUM('ACCEPT','EDIT','REJECT'), edited_output, signed_at)`.
- **Đánh đổi**: thêm click cho bác sĩ → chấp nhận theo lô ký một lần nhưng log từng mục.

### TELE-P08 — Nhãn AI và đánh dấu nội dung
- **Giải quyết**: R24
- **Cách làm**: middleware gắn `ai_generated=true` + nhà cung cấp + thời điểm vào metadata ảnh/audio/video sinh ra; component UI chuẩn "AI" cho mọi bong bóng chat; log `ai_disclosed_at` đầu phiên.
- **Gợi ý dữ liệu**: cột `ai_disclosed_at` trên phiên chat; metadata file theo C2PA/XMP.
- **Đánh đổi**: một số kênh (SMS, tổng đài) khó gắn metadata → dùng câu thông báo bằng lời.

### TELE-P09 — Workflow sự cố hợp nhất
- **Giải quyết**: R29 (và ANM-R16, HTTT-BC-R32–R35)
- **Cách làm**: một `incident` có nhiều nghĩa vụ báo cáo, deadline tính từ `confirmed_at` theo từng chế độ (AI: 72h/05 ngày làm việc → 15 ngày).
- **Gợi ý dữ liệu**: `incident_obligation(incident_id, regime ∈ {AI_ND142, ANM_ND331, DLCN, SU_CO_Y_KHOA}, deadline, submitted_at, ref)`.
- **Đánh đổi**: cần người điều phối pháp chế xác định chế độ nào áp dụng cho từng sự cố.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| TELE-A01 | R01 | 20 lượt từ xa gần nhất có trường phân biệt 4 mô hình | Truy vấn `encounter` theo mode | BẮT BUỘC |
| TELE-A02 | R02 | Có số phiếu công bố KCB từ xa, danh mục dịch vụ; thử mở bán dịch vụ ngoài danh mục | Ảnh màn hình; kết quả chặn; công bố trên cổng Sở Y tế | BẮT BUỘC |
| TELE-A03 | R02 | Nền tảng: mỗi phiên gắn `facility_id` có GPHĐ; có bác sĩ "tự do" không gắn cơ sở? | Truy vấn phiên thiếu facility | BẮT BUỘC |
| TELE-A04 | R03 | Đặt lịch ngoài giờ đăng ký; tạo hai lịch chồng giờ ở hai cơ sở | Kết quả chặn/cảnh báo; danh sách đăng ký hành nghề | BẮT BUỘC |
| TELE-A05 | R04 | Đóng phiên với chẩn đoán ngoài TT 30 (vd I21) và kê đơn điều trị; bảng ICD đủ 50 dòng, mã đúng | Kết quả chặn; bảng ICD | BẮT BUỘC |
| TELE-A06 | R04 | Thí điểm: văn bản cho phép, quota, bộ đếm ca | Văn bản; truy vấn đếm ca | BẮT BUỘC |
| TELE-A07 | R05 | HSBA lượt từ xa: ICD, người hành nghề, thời điểm, kênh, chữ ký số; đã lên Sổ SKĐT | HSBA xuất; log gửi Cổng | BẮT BUỘC |
| TELE-A08 | R06 | Phiên trực tiếp BN thử kê thuốc gây nghiện/hướng thần; đơn từ xa có mã đơn, đã gửi đơn thuốc quốc gia | Kết quả chặn; mã đơn; phản hồi hệ thống | BẮT BUỘC? / BẮT BUỘC |
| TELE-A09 | R06 | App có cho thêm thuốc kê đơn vào giỏ/giao tận nhà sau phiên? | Thử thao tác | BẮT BUỘC |
| TELE-A10 | R07 | Bộ hồ sơ minh chứng hạ tầng (nơi đặt dữ liệu, mã hóa, sao lưu, bên thứ ba) | Tài liệu vendor; phân loại cấp độ | BẮT BUỘC |
| TELE-A11 | R08 | Lượt qua cơ sở tiếp nhận/hỗ trợ có hợp đồng hiệu lực đủ 5 nhóm nội dung Đ87 k11 | Hợp đồng; truy vấn lượt không có contract | BẮT BUỘC |
| TELE-A12 | R09 | Lượt qua cơ sở tiếp nhận: công khám, DVKT lấy giá cơ sở nào; có bút toán phải trả | Phiếu thanh toán; sổ đối soát | BẮT BUỘC |
| TELE-A13 | R10 | Có hồ sơ BHYT gửi cho lượt trực tiếp BN hoặc thí điểm? Mã loại hình 14 dùng thế nào? | Truy vấn XML đã gửi | BẮT BUỘC |
| TELE-A14 | R11 | Hội chẩn/hỗ trợ: biên bản trong HSBA cơ sở được hỗ trợ; ghi đã thông tin BN; báo cáo năm | Biên bản; báo cáo | BẮT BUỘC |
| TELE-A15 | R12 | Nếu ghi hình: thông báo, đồng ý trước; nơi lưu, thời hạn, phân quyền | Màn hình đồng ý; cấu hình; log truy cập | BẮT BUỘC (nếu ghi) / NÊN |
| TELE-A16 | R13 | Tài khoản BN xác thực bằng gì; bác sĩ MFA; BN thấy tên, số giấy phép, cơ sở trước phiên | Màn hình; cấu hình IdP | NÊN / BẮT BUỘC |
| TELE-A17 | R14, R18 | Loại nền tảng; số, ngày xác nhận; xác nhận cũ theo NĐ 52 có kế hoạch làm lại trước 30/06/2027 | Tra hệ thống quản lý TMĐT; văn bản xác nhận | BẮT BUỘC |
| TELE-A18 | R15 | Điều kiện giao dịch tiếng Việt đủ nội dung Đ11; checkbox đồng ý lưu phiên bản; công khai GPHĐ | Ảnh màn hình; bảng consent | BẮT BUỘC |
| TELE-A19 | R16 | Chính sách lưu/xóa đơn hàng; đơn 30 tháng trước còn truy cập được | Truy vấn; cấu hình retention | BẮT BUỘC |
| TELE-A20 | R17 | Sàn trung gian: xác thực danh tính người bán, kiểm GPHĐ, duyệt trước khi hiển thị, đánh giá đầy đủ | Quy trình; log duyệt | BẮT BUỘC |
| TELE-A21 | R19 | Có ma trận phân loại app và kết luận từng nhánh | Tài liệu | BẮT BUỘC |
| TELE-A22 | R20 | Nội dung quảng bá: dịch vụ ngoài phạm vi? từ ngữ cam kết khỏi bệnh? | Ảnh chụp; đối chiếu GPHĐ | BẮT BUỘC |
| TELE-A23 | R21 | Sổ AI liệt kê mọi tính năng AI (kể cả gọi API LLM), vai trò, mức rủi ro, lý do | Sổ AI; grep code lời gọi API AI | BẮT BUỘC |
| TELE-A24 | R22 | Mỗi AI có kết luận thuộc/không thuộc QĐ 33 kèm dòng đối chiếu; AI điều khiển thiết bị điều trị có xác nhận từng bước | Hồ sơ phân loại; thử UI | BẮT BUỘC |
| TELE-A25 | R23 | Chatbot hướng BN: hồ sơ phân loại, biên nhận/mã định danh thông báo trước go-live | Biên nhận; ngày go-live | BẮT BUỘC? |
| TELE-A26 | R24 | Chatbot báo là AI ngay đầu phiên; file AI tạo có metadata; avatar bác sĩ ảo có nhãn | Ảnh màn hình; đọc metadata (exiftool) | BẮT BUỘC |
| TELE-A27 | R25 | Sổ AI có go-live và hạn tuân thủ đúng quy tắc | Sổ AI | BẮT BUỘC |
| TELE-A28 | R26 | Tìm cấu hình "tự động chấp nhận"; log review; chatbot có kê đơn/chẩn đoán xác định? | Cấu hình; truy vấn log; thử hội thoại | BẮT BUỘC |
| TELE-A29 | R27 | (Rô-bốt AI) chứng nhận/đánh giá sự phù hợp công khai trên Cổng; số lưu hành TBYT; đại diện tại VN | Văn bản chứng nhận; sổ thiết bị | BẮT BUỘC |
| TELE-A30 | R28 | Hợp đồng AI có mục đích, giới hạn, nghĩa vụ thông tin, sự cố, hoàn trả; thay đổi cấu hình có bước đánh giá rủi ro | Hợp đồng; change log | BẮT BUỘC / NÊN |
| TELE-A31 | R29 | Quy trình, mẫu AI01a/b, đồng hồ 72h/05 ngày làm việc/15 ngày; diễn tập | Quy trình; biên bản diễn tập | BẮT BUỘC |
| TELE-A32 | R30 | Dữ liệu BN có gửi tới API AI nước ngoài; tập huấn luyện có căn cứ/khử nhận dạng | Sơ đồ luồng dữ liệu; log export | BẮT BUỘC |
| TELE-A33 | R31 | Rà kịch bản chatbot bán hàng, cá nhân hóa cho người cao tuổi | Kịch bản; mẫu hội thoại | BẮT BUỘC / NÊN |
| TELE-A34 | R32 | BV công: phiếu tự đánh giá PL II TT 05/2026 cho từng AI; quy tắc đạo đức nội bộ | Phiếu; văn bản | BẮT BUỘC? / NÊN |
| TELE-A35 | R33 | Cơ quan nhà nước/BHXH dùng AI chấm điểm, sàng lọc: báo cáo Mẫu AI02 đã duyệt, công khai | Báo cáo | BẮT BUỘC? |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 01/01/2024 | Luật KCB Đ80, NĐ 96 Đ87–88, TT 30/2023 có HL | Cơ sở KCB làm từ xa | Đã qua |
| 01/03/2026 | Luật AI có HL (trừ Đ35): AI mới tự phân loại; trung bình/cao thông báo trước khi dùng | Vendor AI, BV/PK | Đã qua |
| 10/03/2026 | Khung đạo đức AI (TT 05/2026) | AI phục vụ dịch vụ công | Đã qua |
| 01/05/2026 | NĐ 142 có HL | Như trên | Đã qua |
| 15/05/2026 | NĐ 90/2026 có HL | Cơ sở KCB, người hành nghề | Đã qua |
| 01/07/2026 | Luật TMĐT + NĐ 248 có HL; NĐ 52/2013, NĐ 85/2021 hết HL | Nền tảng bán dịch vụ y tế, nhà thuốc online | Đã qua |
| 15/08/2026 | QĐ 33/2026 Danh mục AI rủi ro cao có HL | Vendor/BV rô-bốt AI | Đã qua |
| 07/10/2026 | Hạn góp ý dự thảo TT BHYT (qua SYT Đồng Nai) | Cơ sở KCB BHYT (tùy chọn) | Sắp tới |
| **01/01/2027** | Dự thảo TT BHYT KCB từ xa dự kiến HL; sàn trung gian xác thực danh tính người bán; HTTT quản lý KCB đăng tải thông tin theo NĐ 96 | Cơ sở KCB BHYT; sàn trung gian; cơ sở KCB | Sắp tới |
| 15/02/2027 | Hết 6 tháng kể từ 15/08/2026 (cách đếm là suy luận) | Vendor/BV rô-bốt AI mới | Sắp tới |
| **01/03/2027** | Hạn AI rủi ro cao đưa vào hoạt động 15/08/2026–15/02/2027; hạn AI lĩnh vực khác đã chạy trước 01/03/2026 | BV có rô-bốt AI mới; vendor đa lĩnh vực | Sắp tới |
| **30/06/2027** | Hết chuyển tiếp nền tảng TMĐT đã xác nhận theo NĐ 52 | PK, nhà thuốc, nền tảng cũ | Sắp tới |
| **01/09/2027** | AI y tế đã chạy trước 01/03/2026 tuân thủ Luật AI; AI y tế thuộc Danh mục chạy trước 15/08/2026 hoàn thành nghĩa vụ | Vendor AI y tế, BV/PK | Sắp tới |
| Thường xuyên | Công bố lại khi đổi thông tin KCB từ xa; phân loại lại AI (15 ngày làm việc nếu mức cao hơn); sự cố AI 72h/05 ngày làm việc/15 ngày; sửa đổi TMĐT trong 20 ngày làm việc; báo cáo năm hỗ trợ từ xa | Như trên | — |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**

| Cũ | Mới | Từ ngày | Ghi chú |
|---|---|---|---|
| NĐ 52/2013/NĐ-CP + NĐ 85/2021/NĐ-CP (TMĐT) | Luật 122/2025/QH15 + NĐ 248/2026/NĐ-CP | 01/07/2026 | NĐ 248 Đ52 k3 bãi bỏ; xác nhận cũ dùng đến 30/06/2027 (Đ53) |
| TT 49/2017/TT-BYT (y tế từ xa) | ? (nội dung trùng nay theo NĐ 96) | — | Không thấy văn bản bãi bỏ (đã kiểm TT 30/2023, TT 32/2023 Đ53 k2, TT 25/2026); phần kỹ thuật chưa có văn bản thay |
| TT 53/2014/TT-BYT | ? (Luật CNTT 2006 → Luật CĐS 148/2025 từ 01/07/2026) | — | Chưa xác minh căn cứ, tình trạng |
| Luật 71/2025 Chương IV (AI) và các điều liên quan | Luật AI 134/2025 | 01/03/2026 | Luật 134 Đ33 bãi bỏ |

**Bẫy trích dẫn**

1. **"TT 30/2025 về KCB từ xa"** không tồn tại. Văn bản đúng: TT 30/2023/TT-BYT (danh mục 50 bệnh/tình trạng, mã ICD) + NĐ 96/2023 Đ87–88; dự thảo TT BHYT (PL3) chỉ kế thừa TT 30/2023.
2. **"KCB từ xa phải ghi hình/ký số theo dự thảo BHYT"**: bản toàn văn 04/08/2026 không có. Đừng trích tin báo.
3. **"BHYT đã chi trả khám online"**: Quỹ chỉ trả khi người bệnh đến một cơ sở để được cơ sở khác KCB từ xa; không trả thí điểm; khám từ nhà qua app là thỏa thuận.
4. **"Chỉ được khám từ xa 50 bệnh"**: Luật Đ80 k1 a gắn danh mục với **chữa bệnh** từ xa; với "khám" chưa rõ. Ngược lại, đừng viết "khám từ xa không bị giới hạn" như kết luận.
5. **"AI y tế là AI rủi ro cao"**: sai với Danh mục hiện hành (chỉ 2 dòng rô-bốt). Luật Đ6 k2 a giao văn bản chuyên ngành; BYT chưa ban hành.
6. **"Hạn 01/09/2027 cho mọi AI y tế"**: chỉ cho hệ thống chạy trước 01/03/2026 hoặc rủi ro cao chạy trước 15/08/2026; rủi ro cao chạy 15/08/2026–15/02/2027 có hạn 01/03/2027; trung bình/thấp go-live sau 01/03/2026 không có chuyển tiếp.
7. **"Đ35 Luật AI hiệu lực 01/09/2027"**: Đ35 là điều chuyển tiếp ghi "18 tháng"; ngày là kết quả tính.
8. **Mức phạt AI "2 tỷ đồng/2% doanh thu"**: là con số của dự thảo Luật, không có trong Luật 134 (Đ29 k5 giao Chính phủ). Chưa thấy NĐ xử phạt VPHC lĩnh vực AI.
9. **"Thông báo website TMĐT lên online.gov.vn"**: nay nền tảng kinh doanh trực tiếp do UBND tỉnh xác nhận (NĐ 248 Đ24 k5); chỉ nền tảng trung gian/MXH/tích hợp đăng ký với Bộ Công Thương.
10. **NĐ 90/2026 không có hành vi "KCB từ xa chưa công bố"**: chỉ suy luận áp Đ39 k6 b.
11. **TT 05/2026 "bắt buộc mọi tổ chức"**: sai; chỉ AI phục vụ QLNN/dịch vụ công.
12. **QĐ 33 hai dòng cùng tên** nhưng phương thức đánh giá khác nhau (dòng 1: Đ13 k2 b tự đánh giá được; dòng 2: Đ13 k2 a phải chứng nhận). Đọc qua OCR dễ nhầm.
13. **"≥ 10.000 người bệnh = cấp độ 3"** chỉ đúng cho dịch vụ trực tuyến; HIS nội bộ là cấp 2; KCB từ xa/bán thuốc online cấp 3 (suy luận, xem ANM-R02).
14. NĐ 96 Đ87–88 **chưa bị sửa**: NQ 21/2026/NQ-CP không đụng; VBHN 10/VBHN-BYT 2026 là hợp nhất thông tư về phân cấp TTHC, không phải VBHN NĐ 96 (thứ cấp).

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. TT 49/2017 và TT 53/2014 còn hiệu lực không (hỏi Vụ Pháp chế BYT).
2. Danh mục TT 30/2023 ràng buộc "khám" từ xa hay chỉ "chữa bệnh" từ xa (Luật Đ80 k1 a). Hỏi Cục QLKCB.
3. App chỉ tư vấn sức khỏe chung có phải KCB từ xa; doanh nghiệp công nghệ có được vận hành qua hợp đồng với cơ sở KCB không (NĐ 96 Đ87 k1 a). Cần BYT hoặc luật sư.
4. Bản dự thảo TT BHYT 01/10/2026 (CV 7409/BYT-BH): chưa đọc; có thể khác bản 04/08/2026.
5. Mã ICD TT 30/2023: cần bản Công báo có lớp chữ để nạp chính xác (mã cúm "J19" nghi lỗi đánh máy).
6. Chatbot hướng BN là trung bình hay thấp khi đã công bố rõ là AI; AI nội bộ (CDSS, scribe, đọc ảnh) có chắc "thấp". Có thể đề nghị Bộ KH&CN hướng dẫn phân loại (Luật Đ10 k4, NĐ 142 Đ10 k4).
7. Cổng một cửa về AI: đã vận hành chính thức chưa, địa chỉ, đặc tả API kê khai.
8. NĐ xử phạt VPHC lĩnh vực AI (Luật Đ29 k5): chưa thấy ban hành đến 06/10/2026.
9. Văn bản BYT về AI trong KCB (NĐ 142 Đ43 k1; Luật Đ6 k4): chưa có; TTYQG lấy ý kiến "Bộ tiêu chí tham chiếu đánh giá sản phẩm, giải pháp AI trong y tế" (06/2026), chưa đọc bản gốc.
10. BV công có là "cơ quan nhà nước"/"cung cấp dịch vụ công" theo Luật AI Đ27, NĐ 142 Đ20, TT 05/2026 Đ1 k2.
11. App BV công thu viện phí, bán gói khám có phải nền tảng TMĐT phải thông báo (Luật TMĐT Đ3 k1).
12. Xung đột Luật KCB Đ7 k21 với Luật TMĐT Đ17 k2 h (đánh giá bác sĩ). Cần luật sư.
13. Báo cáo sự cố y khoa có yếu tố AI: phối hợp TT 43/2018 với NĐ 142 Đ19 k5.
14. Cơ sở KCB tự cấp phát thuốc kê đơn tại nhà sau KCB từ xa có bị coi là bán lẻ thuốc kê đơn qua TMĐT. Hỏi Cục Quản lý Dược.
15. QĐ 804/QĐ-TTg (bộ dữ liệu phục vụ phát triển AI): chưa đọc.
16. CV 7946/BYT-KCB (12/12/2023) hướng dẫn KCB từ xa ở y tế cơ sở: chỉ thấy qua báo, chưa có bản gốc.
