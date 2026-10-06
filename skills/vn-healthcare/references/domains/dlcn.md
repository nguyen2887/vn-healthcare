# DLCN — Bảo vệ dữ liệu cá nhân và quản trị dữ liệu y tế

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám, nhà thuốc, vendor phần mềm/SaaS/app y tế · Research gốc: `research/deep/DLCN.md`

Phạm vi: Luật BVDLCN 91/2025/QH15 + NĐ 356/2025/NĐ-CP (dữ liệu sức khỏe nhạy cảm, căn cứ xử lý, đồng ý, quyền chủ thể, trẻ em, DPIA/TIA, thông báo vi phạm, DPO, miễn trừ DN nhỏ, dịch vụ xử lý DLCN và Giấy chứng nhận cho vendor); chia sẻ cho bảo hiểm; NĐ 102/2025 (dữ liệu y tế); Luật Dữ liệu 60/2024 + NĐ 165/2025 + QĐ 20/2025/QĐ-TTg; chế tài NĐ 330/2026, NĐ 363/2026; bí mật HSBA (Luật KCB), HIV. Tài liệu nghiên cứu, không phải ý kiến pháp lý.

## Tóm tắt nhanh

- Dữ liệu sức khỏe là DLCN **nhạy cảm** (NĐ 356 Đ4 k1 d): bắt buộc phân quyền giới hạn truy cập; app y tế, nền tảng CSSK trực tuyến không phân quyền bị phạt 50–70 triệu (NĐ 330 Đ62 k1 b) — DLCN-R01.
- Đồng ý phải theo **từng mục đích**, không tick sẵn, thông báo rõ là dữ liệu nhạy cảm, lưu bằng chứng kiểm chứng được; im lặng không phải đồng ý — DLCN-R02, R03.
- Cấm cung cấp dữ liệu người bệnh cho **bảo hiểm sức khỏe/nhân thọ hoặc cơ sở CSSK khác** khi chưa có yêu cầu bằng văn bản của người bệnh (trừ Luật 91 Đ19 k1): 70–100 triệu + đình chỉ 3–6 tháng — DLCN-R09.
- DPIA nộp Cục A05 (Bộ Công an) **trong 60 ngày** từ ngày đầu xử lý; cập nhật 06 tháng khi có thay đổi, 10 ngày khi thay đổi lớn. Phòng khám nhỏ, nhà thuốc, startup y tế **không** được miễn — DLCN-R13, R14, R21.
- **Vendor SaaS/app y tế phải có Giấy chứng nhận đủ điều kiện kinh doanh dịch vụ xử lý DLCN của Bộ Công an** (NĐ 356 Đ21 k1, k4; Đ22–27). Không có điều chuyển tiếp; kinh doanh khi chưa có giấy: 50–80 triệu (NĐ 330 Đ59 k3 a). Phần còn treo: vendor bán bản cài tại chỗ có truy cập từ xa — DLCN-R22.
- Vi phạm DLCN: báo cơ quan chuyên trách **chậm nhất 72 giờ** từ khi phát hiện (Luật 91 Đ23, không phải NĐ 356 Đ29) — DLCN-R17.
- Mốc sắp tới: **11/11/2026** NĐ 363/2026 (chế tài lĩnh vực dữ liệu) có hiệu lực; 01/03/2027 Luật 24/2026/QH16 (Phụ lục IV mới, dịch vụ xử lý DLCN ở STT 136).
- Bẫy: mức phạt Mục BVDLCN của NĐ 330 là **mức tổ chức** (cá nhân bằng 1/2), ngược với mục an ninh mạng; mã hóa/giả danh **không** phải khử nhận dạng.

## Mục lục

- A. Phân loại, căn cứ: R01 dữ liệu sức khỏe nhạy cảm, phân quyền · R02 căn cứ xử lý · R03 hình thức đồng ý, bằng chứng
- B. Quyền chủ thể: R04 quy trình, kênh tiếp nhận · R05 SLA pháp định · R06 xem, sao HSBA · R07 xóa, hủy · R08 trẻ em, người mất năng lực
- C. Chia sẻ: R09 cấm cung cấp cho bảo hiểm, cơ sở CSSK khác · R10 thỏa thuận chuyển giao, mã hóa · R11 hợp đồng với vendor (DPA) · R12 điện toán đám mây
- D. Hồ sơ đánh giá: R13 DPIA 60 ngày · R14 cập nhật DPIA/TIA · R15 chuyển xuyên biên giới · R16 dữ liệu cốt lõi/quan trọng
- E. Sự cố: R17 thông báo 72 giờ · R18 sinh trắc, vị trí · R19 thông báo sự cố dữ liệu (Luật Dữ liệu)
- F. Tổ chức: R20 DPO · R21 không miễn trừ cho PK nhỏ, nhà thuốc
- G. Vendor: R22 Giấy chứng nhận dịch vụ xử lý DLCN · R23 nghĩa vụ khi đã có giấy · R24 app y tế, dữ liệu lớn, MFA · R25 AI, xử lý tự động
- H. Mục đích phụ: R26 khử nhận dạng · R27 không mua bán DLCN · R28 tiếp thị · R29 camera · R30 giới hạn mục đích, thời hạn lưu
- I. Bảo mật chuyên ngành: R31 bí mật HSBA · R32 HIV · R33 dữ liệu y tế NĐ 102
- Pattern: P01–P11 · Audit: A01–A31

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| Luật 91/2025/QH15 | Luật Bảo vệ dữ liệu cá nhân | 01/01/2026 | Còn HL | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf) · [VB 214590](https://vanban.chinhphu.vn/?pageid=27160&docid=214590) |
| NĐ 356/2025/NĐ-CP (31/12/2025) | Chi tiết Luật BVDLCN | 01/01/2026 | Còn HL; thay NĐ 13/2023; sửa Đ16 k2 NĐ 165/2025 (Đ42 k3) | gốc | [Trang Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm) · [PDF Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/17/356signed-1768638052103952849513.pdf) · [VB 216387](https://vanban.chinhphu.vn/?pageid=27160&docid=216387) |
| NĐ 330/2026/NĐ-CP (19/08/2026) | Xử phạt VPHC an ninh mạng và BVDLCN | 19/08/2026 | Còn HL | gốc (văn bản Công báo; đã đối chiếu Đ3, Đ59, Đ60, Đ62, Đ63, Đ66) | [Trang Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-330-2026-nd-cp-470339.htm) · [VB 219266](https://vanban.chinhphu.vn/?pageid=27160&docid=219266) |
| NĐ 102/2025/NĐ-CP (13/05/2025) | Quản lý dữ liệu y tế | 01/07/2025 | Còn HL (căn cứ Luật ANM 2018, Luật ATTT mạng 2015 đã bị Luật 116/2025 thay từ 01/07/2026) | gốc | [Trang Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-102-2025-nd-cp-44865.htm) · [VB 213607](https://vanban.chinhphu.vn/?pageid=27160&docid=213607) |
| Luật 60/2024/QH15 | Luật Dữ liệu | 01/07/2025 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat60.pdf) · [VB 212488](https://vanban.chinhphu.vn/?pageid=27160&docid=212488) |
| NĐ 165/2025/NĐ-CP (30/06/2025) | Chi tiết Luật Dữ liệu | 01/07/2025 | Còn HL; Đ16 k2 bị NĐ 356 Đ42 k3 sửa | gốc-OCR có dấu (Đ3–5, 12, 16–17) | [VB 214331](https://vanban.chinhphu.vn/?pageid=27160&docid=214331) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/165nd.signed.pdf) |
| QĐ 20/2025/QĐ-TTg (01/07/2025) | Danh mục dữ liệu quan trọng, cốt lõi | 01/07/2025 | Còn HL | gốc-OCR có dấu | [VB 214354](https://vanban.chinhphu.vn/?pageid=27160&docid=214354) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/20qd.signed.pdf) |
| NĐ 363/2026/NĐ-CP (19/09/2026) | Xử phạt VPHC lĩnh vực dữ liệu | **11/11/2026** | Sắp HL | gốc-OCR có dấu | [VB 219598](https://vanban.chinhphu.vn/?pageid=27160&docid=219598) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/363_2026_nd-cp_19092026-signed.signed.pdf) |
| Luật 143/2025/QH15 (11/12/2025) | Luật Đầu tư — Phụ lục IV STT 198 "Dịch vụ xử lý dữ liệu cá nhân" | Luật 01/03/2026; Phụ lục IV 01/07/2026 (Đ51 k2) | Còn HL; Phụ lục IV bị Luật 24/2026 thay từ 01/03/2027 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat143-2025.pdf) · [VB 216524](https://vanban.chinhphu.vn/?pageid=27160&docid=216524) |
| Luật 24/2026/QH16 (24/08/2026) | Sửa Luật Đầu tư — Phụ lục IV mới, STT 136 "Dịch vụ xử lý dữ liệu cá nhân" | 01/03/2027 | Sắp HL | gốc-OCR có dấu (phụ lục) | [VB 219356](https://vanban.chinhphu.vn/?pageid=27160&docid=219356) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/luatso24-suadoiluatdautu.signed.pdf) |
| Luật KCB (VBHN 26/VBHN-VPQH) | Đ8, Đ10 k2, Đ12, Đ45 k5, Đ69 (bí mật, khai thác HSBA) | 01/01/2024 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| Luật 71/2020/QH14 sửa Luật 64/2006/QH11 | Phòng, chống HIV/AIDS — Đ30 | 01/07/2021 | Còn HL (chưa kiểm VBHN mới hơn) | bản sao trên cổng .gov.vn | [Trang CA Đắk Lắk](https://congan.daklak.gov.vn/laws/detail/Luat-sua-doi-bo-sung-mot-so-dieu-cua-Luat-Phong-chong-nhiem-vi-rut-gay-ra-hoi-chung-suy-giam-mien-dich-mac-phai-o-nguoi-HIV-AIDS-2020-SO-71-2020-QH14-324/) |
| NĐ 13/2023/NĐ-CP | BVDLCN (cũ) | 01/07/2023 → hết HL 01/01/2026 | Hết HL (NĐ 356 Đ42 k2) | gốc (qua NĐ 356) | — |
| QĐ 2623/QĐ-TTg (29/11/2025) | Kế hoạch thi hành Luật BVDLCN | Ký | Còn HL; bối cảnh | gốc-meta | [VB 216065](https://vanban.chinhphu.vn/?pageid=27160&docid=216065) |
| NĐ 169/2025, sửa bởi NĐ 347/2026 | Sản phẩm, dịch vụ về dữ liệu | 01/07/2025; 347: 15/09/2026 | Còn HL; ngoại vi | gốc-meta | [VB 214306](https://vanban.chinhphu.vn/?pageid=27160&docid=214306) · [VB 219411](https://vanban.chinhphu.vn/?pageid=27160&docid=219411) |
| NĐ 314/2026/NĐ-CP (08/08/2026) | Sàn dữ liệu | 25/09/2026 | Còn HL; ngoại vi | gốc-meta | [VB 219180](https://vanban.chinhphu.vn/?pageid=27160&docid=219180) |

## 2. Yêu cầu

### A. Phân loại và căn cứ xử lý

### DLCN-R01 — Dữ liệu sức khỏe là DLCN nhạy cảm: phân quyền giới hạn truy cập
- **Căn cứ**: Luật 91 Đ2 k3; NĐ 356 Đ4 k1 d ("Tình trạng sức khỏe"), đ (sinh trắc, di truyền), e (đời sống tình dục), i (tên đăng nhập/mật khẩu tài khoản định danh điện tử; ảnh thẻ căn cước), k; Đ4 k2 (phải có quy định phân quyền giới hạn truy cập, quy trình xử lý, biện pháp bảo mật). NĐ 330 Đ62 k1 b ("Trong quá trình phát triển, vận hành các ứng dụng y tế, nền tảng chăm sóc sức khỏe trực tuyến, tiến hành thu thập dữ liệu cá nhân nhạy cảm nhưng không thiết lập quy định phân quyền giới hạn truy cập và các biện pháp bảo mật theo quy định": 50–70 triệu), Đ62 k4 a.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: gắn nhãn độ nhạy cho từng trường/nhóm dữ liệu (lâm sàng, CLS, chẩn đoán, đơn thuốc, ảnh, sinh trắc mặc định "nhạy cảm"); RBAC/ABAC tối thiểu quyền, chỉ người được phân công điều trị/xử lý mới xem; ma trận phân quyền và quy trình xử lý dữ liệu nhạy cảm xuất được ra file để nộp kèm DPIA. Mức kỹ thuật tài khoản (45 ngày, rà soát 6 tháng): xem ANM-R09.
- **Bẫy**: số điện thoại, CCCD, ảnh chân dung là dữ liệu cơ bản (NĐ 356 Đ3 k6, k7), nhưng ảnh thẻ căn cước là nhạy cảm (Đ4 k1 i) — app lưu ảnh chụp CCCD để xác thực bệnh nhân đang giữ dữ liệu nhạy cảm.

### DLCN-R02 — Căn cứ xử lý: đồng ý là mặc định, ngoại lệ theo Luật 91 Đ19 k1
- **Căn cứ**: Luật 91 Đ26 k1 a (thông tin sức khỏe phải có đồng ý của chủ thể trong quá trình thu thập, xử lý, trừ trường hợp Đ19 k1); Đ11 k1; Đ19 k1 (a: bảo vệ tính mạng, sức khỏe trường hợp cấp bách — bên xử lý phải chứng minh; b: khẩn cấp, an ninh; c: hoạt động của cơ quan nhà nước theo luật; d: thực hiện thỏa thuận của chủ thể; đ: trường hợp khác theo luật); Đ19 k2 (không cần đồng ý vẫn phải có quy trình, biện pháp, đánh giá rủi ro); Đ5 k2 (luật ban hành trước 01/01/2026 có quy định cụ thể không trái nguyên tắc thì áp dụng: Luật KCB, Luật HIV, Luật BHYT). NĐ 330 Đ47 (không chứng minh được căn cứ miễn đồng ý: 30–50 triệu; không có quy trình: 10–20 triệu).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC (có căn cứ cho từng mục đích, chứng minh được) · BẮT BUỘC? (xếp hoạt động KCB cốt lõi như lập HSBA, gửi XML BHYT, liên thông Sổ SKĐT vào Đ19 k1 đ/d thay cho đồng ý — suy luận, chưa có hướng dẫn)
- **Phần mềm phải**: sổ đăng ký hoạt động xử lý: mỗi mục đích có `legal_basis` ∈ {consent, emergency_19_1_a, state_19_1_c, contract_19_1_d, law_19_1_dd} + `legal_reference`; ca cấp cứu chưa có đồng ý ghi cờ căn cứ khẩn cấp + lý do + người xác nhận và nhắc thu đồng ý khi người bệnh/đại diện có khả năng.
- **Bẫy**: mục đích ngoài KCB (nghiên cứu, CRM, marketing, huấn luyện AI, chia sẻ đối tác) luôn cần đồng ý riêng. Thực hành an toàn (suy luận): thu đồng ý ở bước đăng ký khám cho cả mục đích KCB, đồng thời ghi căn cứ luật định làm căn cứ dự phòng.

### DLCN-R03 — Hình thức đồng ý, lưu bằng chứng, cấm mặc định đồng ý
- **Căn cứ**: Luật 91 Đ9 k2–4 (tự nguyện, rõ ràng, in/sao chép được kể cả điện tử; đồng ý từng mục đích; không kèm điều kiện bắt buộc; im lặng không phải đồng ý). NĐ 356 Đ6 k1 (văn bản, cuộc gọi ghi âm, SMS cú pháp, email/web/app có thiết lập kỹ thuật — phải kiểm chứng được chủ thể, thời điểm, nội dung), k2 (phải lưu trữ; tranh chấp thì bên kiểm soát chứng minh), k3 (không thiết lập mặc định đồng ý), k4 (khi xin đồng ý xử lý dữ liệu nhạy cảm phải thông báo đó là dữ liệu nhạy cảm). NĐ 330 Đ43 k1 (30–50 triệu, gồm g: không lưu nhật ký đồng ý; h: không thông báo dữ liệu nhạy cảm), k2 (50–70 triệu: tiếp tục xử lý sau khi bị yêu cầu ngừng; coi im lặng là đồng ý).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2026; đồng ý thu theo NĐ 13/2023 vẫn có giá trị (Luật 91 Đ39 k1)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: biểu mẫu tách từng mục đích, checkbox không tick sẵn, nút đồng ý/không đồng ý cân bằng; câu thông báo dữ liệu sức khỏe là DLCN nhạy cảm; bản ghi đồng ý bất biến (chủ thể, người ký thay và quan hệ, hash phiên bản văn bản, mục đích, kênh, thời điểm, IP/thiết bị, người tiếp nhận); xuất bằng chứng ra PDF; từ chối mục đích phụ không làm mất quyền KCB (Đ9 k4 b; NĐ 330 Đ43 k1 b).
- **Bẫy**: "đồng ý chung chung trong phiếu nhập viện" không đáp ứng yêu cầu từng mục đích. Bản ghi đồng ý cũ theo NĐ 13 phải migrate kèm metadata gốc.

### B. Quyền của chủ thể dữ liệu

### DLCN-R04 — Quy trình, biểu mẫu và kênh tiếp nhận yêu cầu thực hiện quyền
- **Căn cứ**: Luật 91 Đ4 k1, k4, k5 (biết; đồng ý/rút lại; xem, chỉnh sửa; cung cấp, xóa, hạn chế, phản đối; khiếu nại). NĐ 356 Đ5 k1 (quy trình, thủ tục, biểu mẫu rõ ràng; phân trách nhiệm; chủ thể được biết thủ tục). NĐ 330 Đ44 k1 (10–20 triệu).
- **Áp dụng**: bên kiểm soát (BV, PK, nhà thuốc; vendor app B2C) · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: module yêu cầu chủ thể dữ liệu (DSR): biểu mẫu web/app/quầy, xác minh danh tính người yêu cầu, phân loại, đồng hồ SLA, nhật ký xử lý, mẫu thư phản hồi; trang công khai mô tả thủ tục.

### DLCN-R05 — Thời hạn phản hồi và thực hiện (SLA pháp định)
- **Căn cứ**: NĐ 356 Đ5 — mọi loại yêu cầu: phản hồi **02 ngày làm việc**. Thực hiện: k2 rút đồng ý/hạn chế/phản đối 15 ngày (qua bên xử lý/bên thứ ba 20 ngày; gia hạn 1 lần ≤ 15 ngày); k3 xem/chỉnh sửa/cung cấp 10 ngày (15; gia hạn ≤ 10); k4 xóa 20 ngày (30; gia hạn ≤ 20); k5 biện pháp bảo vệ 15 ngày (gia hạn ≤ 15). Gia hạn phải báo lý do. NĐ 330 Đ44 k1 d (quá 02 ngày làm việc), k2 (bên xử lý/bên thứ ba không đúng hạn bên kiểm soát đặt: 20–30 triệu), k3 (quá hạn thực hiện: 30–40 triệu).
- **Áp dụng**: bên kiểm soát; vendor (bên xử lý) hỗ trợ trong hạn bên kiểm soát đặt · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tính hạn phản hồi theo ngày làm việc; hạn thực hiện cấu hình được (ngày lịch hay ngày làm việc chưa rõ, §7); cảnh báo trước hạn; ghi lý do gia hạn; API để bên kiểm soát gửi lệnh ngừng/xóa/sửa tới vendor và nhận xác nhận.
- **Bẫy**: nhiều tài liệu chỉ nêu mốc xem/sửa, bỏ sót mốc 20/30 ngày cho xóa và 20 ngày khi rút đồng ý có bên thứ ba.

### DLCN-R06 — Quyền xem, sao chép HSBA: áp dụng song song Luật KCB
- **Căn cứ**: Luật KCB Đ12 k1; Đ69 k4 d (người bệnh/đại diện theo Đ8 k2 c, d: đọc, xem, sao chụp khi có yêu cầu bằng văn bản), Đ69 k4 đ (đại diện theo Đ8 k2 a, d: chỉ được tóm tắt). Luật 91 Đ15 k2 a; Đ5 k2. NĐ 330 Đ49 k1 (từ chối cung cấp cho chính chủ thể: 10–20 triệu).
- **Áp dụng**: BV, PK · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cổng/quầy cung cấp bản sao HSBA điện tử hoặc tóm tắt có kiểm tra tư cách theo loại đại diện (Đ8 k2 a–đ); lưu yêu cầu bằng văn bản (điện tử); ghi vết lần cung cấp. Mẫu tóm tắt: Mẫu 03 TT 25/2025 (xem GIAYTO, EMR-R14).
- **Bẫy**: app cho người nhà xem toàn bộ bệnh án có thể vượt Đ69 k4 đ.

### DLCN-R07 — Xóa, hủy: được từ chối khi luật buộc lưu; xóa an toàn
- **Căn cứ**: Luật 91 Đ14 k1–5 (các trường hợp xóa; không xóa khi thuộc Đ19; xóa bằng biện pháp chống khôi phục; cấm cố ý khôi phục; không xóa được phải thông báo), Đ3 k3. Luật KCB Đ69 k2. NĐ 330 Đ51 (10–60 triệu), Đ39 k1 c (lưu vượt thời gian cần thiết: 20–40 triệu).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bảng chính sách lưu trữ theo loại dữ liệu có trường căn cứ; HSBA trong hạn lưu: từ chối xóa, gửi lý do, có thể hạn chế xử lý (khóa khỏi mục đích phụ); dữ liệu ngoài HSBA (tài khoản app, marketing, log phụ) xóa được thật; hủy an toàn (crypto-shredding hoặc ghi đè) kể cả bản sao lưu, có biên bản.
- **Bẫy**: thời hạn lưu HSBA: xem EMR-R22. Xóa mềm (cờ `deleted`) không đáp ứng "xóa, hủy" khi đã đến hạn hủy.

### DLCN-R08 — Trẻ em, người mất/hạn chế năng lực hành vi
- **Căn cứ**: Luật 91 Đ24 k2 (đại diện theo pháp luật thực hiện quyền; xử lý dữ liệu trẻ em **nhằm công bố, tiết lộ** đời sống riêng tư của trẻ từ đủ 07 tuổi phải có đồng ý của cả trẻ và đại diện), k3. NĐ 330 Đ60 k1 a ("Không thực hiện quy trình xác minh tuổi của trẻ em trước khi xử lý dữ liệu cá nhân của trẻ em": 30–50 triệu), k1 b (dưới 07 tuổi không có đồng ý của đại diện), k1 c (từ đủ 07 tuổi không có **đồng thời** đồng ý của trẻ và đại diện, trừ Luật 91 Đ19 k1), k2 (50–100 triệu), k3 (không xóa dữ liệu trẻ em khi phải xóa: 100–200 triệu). Luật KCB Đ8.
- **Áp dụng**: tất cả, nhất là nhi, sản, app mẹ và bé · **Hiệu lực/hạn**: 01/01/2026; phạt từ 19/08/2026
- **Mức**: BẮT BUỘC (đồng ý của đại diện; xác minh tuổi) · BẮT BUỘC? (đồng ý kép cho mọi xử lý dữ liệu trẻ ≥ 07 tuổi — NĐ 330 Đ60 k1 c rộng hơn Luật 91 Đ24 k2)
- **Phần mềm phải**: tính tuổi tại thời điểm xin đồng ý; < 7: đại diện; 7–< 18: hai xác nhận (trẻ + đại diện) cho mục đích ngoài KCB cấp cứu; lưu quan hệ đại diện và giấy tờ; nhắc thu đồng ý lại khi tròn 7 và 18 tuổi. Bổ sung về bảo mật trẻ em: BAOMAT-CB-R19.
- **Bẫy**: "trẻ em" theo Luật Trẻ em là dưới 16 tuổi (suy luận, chưa đọc lại), nhưng người bệnh chưa thành niên dưới 18 do cha mẹ đại diện theo Luật KCB Đ8.

### C. Chia sẻ, chuyển giao, bên xử lý

### DLCN-R09 — Cấm cung cấp dữ liệu cho bảo hiểm sức khỏe/nhân thọ và cơ sở CSSK khác nếu không có yêu cầu bằng văn bản
- **Căn cứ**: Luật 91 Đ26 k2: tổ chức hoạt động trong lĩnh vực sức khỏe "không cung cấp dữ liệu cá nhân cho bên thứ ba là tổ chức cung cấp dịch vụ chăm sóc sức khỏe hoặc dịch vụ bảo hiểm sức khỏe, bảo hiểm nhân thọ, trừ trường hợp có yêu cầu bằng văn bản của chủ thể dữ liệu cá nhân hoặc trường hợp quy định tại khoản 1 Điều 19". NĐ 330 Đ62 k2 (cung cấp, chia sẻ dữ liệu bệnh nhân cho tổ chức CSSK khác hoặc DN bảo hiểm sức khỏe, nhân thọ khi chưa nhận được yêu cầu bằng văn bản: 70–100 triệu), k3 (đình chỉ hoạt động xử lý liên quan 03–06 tháng), k4 b (buộc bên thứ ba hủy, xóa).
- **Áp dụng**: BV, PK, nhà thuốc, app y tế · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chặn mọi luồng xuất/API sang đối tác loại bảo hiểm thương mại hoặc cơ sở CSSK khác nếu không có bản ghi yêu cầu bằng văn bản (điện tử, kiểm chứng được) của chính người bệnh, gắn phạm vi và thời hạn; luồng bảo lãnh viện phí khởi tạo từ yêu cầu của người bệnh, không gửi tự động; nhật ký từng lần cung cấp.
- **Bẫy**: BHYT xã hội (BHXH) không phải bảo hiểm sức khỏe thương mại; luồng XML BHYT dựa trên Luật BHYT và Đ19 k1 c (suy luận). "Tổ chức cung cấp dịch vụ CSSK" rộng: chuyển tuyến, gửi mẫu cho phòng xét nghiệm ngoài, hội chẩn từ xa cần xác định căn cứ hoặc lấy yêu cầu bằng văn bản (§7). NĐ 330 Đ62 k2 không chép ngoại lệ Đ19 nhưng Luật có hiệu lực cao hơn.

### DLCN-R10 — Thỏa thuận chuyển giao; mã hóa khi chuyển dữ liệu nhạy cảm; kiểm soát chia sẻ nội bộ
- **Căn cứ**: Luật 91 Đ17 k1, Đ15 k2 b. NĐ 356 Đ7 k1 (thỏa thuận chuyển giao gồm: mục đích; loại dữ liệu; thời hạn xử lý và xóa; cơ sở pháp lý; trách nhiệm bảo vệ; thực hiện quyền chủ thể; phối hợp khi vi phạm), k2 (dữ liệu nhạy cảm: bảo mật vật lý, mã hóa, ẩn danh), k4 (chia sẻ nội bộ phải có quy trình kiểm soát), k6. NĐ 330 Đ52 (20–80 triệu; k3: chuyển dữ liệu nhạy cảm không mã hóa 50–80 triệu), Đ49 k2–3.
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mọi kênh xuất (API, HL7/FHIR, XML, email, USB, in) qua lớp kiểm soát: đối tác có thỏa thuận, căn cứ pháp lý, mã hóa TLS/file, tối thiểu hóa trường; export hàng loạt giới hạn theo vai trò, ghi vết; cảnh báo DLP. Bộ lọc theo loại dữ liệu nhạy cảm chuyên biệt: BAOMAT-CB-R21.

### DLCN-R11 — Hợp đồng xử lý dữ liệu với vendor (DPA), trả/xóa khi chấm dứt
- **Căn cứ**: Luật 91 Đ37 k1 a, đ; k2 a (bên xử lý chỉ tiếp nhận dữ liệu sau khi có thỏa thuận, hợp đồng), k2 b; Đ23 k1 câu 2 (bên xử lý báo bên kiểm soát khi phát hiện vi phạm). NĐ 330 Đ51 k2 c (bên xử lý không xóa/trả toàn bộ dữ liệu sau hợp đồng: 30–50 triệu), Đ46 k1 b, Đ54 k1 a.
- **Áp dụng**: BV/PK thuê phần mềm; vendor · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải** (vendor): xuất toàn bộ dữ liệu khách hàng theo định dạng chuẩn và xóa có biên bản khi hết hợp đồng; tách dữ liệu theo tenant; nhân sự vendor truy cập dữ liệu khách hàng chỉ qua phiên hỗ trợ có phê duyệt, ghi vết. Nội dung hợp đồng về ANM: ANM-R22.

### DLCN-R12 — Điện toán đám mây: hợp đồng và mã hóa khi lưu, khi truyền
- **Căn cứ**: NĐ 356 Đ12 k2 (hợp đồng với nhà cung cấp cloud: chấp hành luật VN, DPO, luồng xử lý, biện pháp bảo mật, thông báo thay đổi, thời hạn xóa, quyền chủ thể, phân cấp truy cập), k3 (nhà cung cấp cloud đánh giá tuân thủ 01 năm/lần, ràng buộc nhà thầu phụ), k4 ("Dữ liệu cá nhân trên điện toán đám mây phải được mã hoá ở trạng thái nghỉ và truyền, kèm theo phân quyền truy cập nghiêm ngặt."). Luật 91 Đ30 k3. NĐ 330 Đ69 k1 (20–50 triệu), k2 b (cung cấp hoặc sử dụng cloud không mã hóa khi lưu, khi truyền: 50–70 triệu).
- **Áp dụng**: mọi hệ thống chạy cloud (kể cả private cloud thuê) · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mã hóa DB, object storage, backup (KMS, khóa tách biệt); TLS mọi kết nối kể cả nội bộ; IAM tối thiểu; hồ sơ đánh giá tuân thủ hằng năm nếu là nhà cung cấp cloud/SaaS. Tách lô-gic theo cấp độ ANM: ANM-R18.

### D. Hồ sơ đánh giá tác động, chuyển dữ liệu ra nước ngoài

### DLCN-R13 — Hồ sơ đánh giá tác động xử lý DLCN (DPIA): lập, nộp trong 60 ngày
- **Căn cứ**: Luật 91 Đ21 k1 (bên kiểm soát lập, lưu, gửi 01 bản chính cho cơ quan chuyên trách trong 60 ngày kể từ ngày đầu tiên xử lý), k2, k3 (bên xử lý lập và lưu theo thỏa thuận), k6 (cơ quan nhà nước có thẩm quyền được miễn). NĐ 356 Đ19 k1 (kể cả bên xử lý lập, lưu từ khi bắt đầu xử lý), k2 (Báo cáo Mẫu 10; bản sao hợp đồng; chính sách, quy trình), k3 (nội dung gồm sơ đồ luồng dữ liệu, sơ đồ thiết kế hệ thống, tiêu chuẩn áp dụng, đánh giá rủi ro), k4 (nộp kèm Mẫu 02a/02b trong 60 ngày), k5 (kết quả đạt/không đạt trong 15 ngày), k6 (hoàn thiện trong 30 ngày). Nơi nhận theo NĐ 330 Đ55 k1 b: Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (Bộ Công an). NĐ 330 Đ55 k1 (20–30 triệu), k2 (làm giả, sai lệch: 50–100 triệu), k3 b (buộc dừng xử lý đến khi nộp xong).
- **Áp dụng**: BV tư, PK, nhà thuốc, vendor (cả vai bên xử lý) · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC · BẮT BUỘC? (BV công lập: có được miễn như cơ quan nhà nước không — suy luận là không)
- **Phần mềm phải**: sinh phần kỹ thuật của DPIA: danh mục trường và độ nhạy (R01), sổ đăng ký xử lý (R02), sơ đồ luồng dữ liệu (tích hợp, đối tác, vùng lưu), ma trận phân quyền, biện pháp mã hóa/sao lưu/ghi vết, danh sách bên xử lý phụ; trường `dpia_submitted_at`, `dpia_result`, `next_review_at`.
- **Bẫy**: hồ sơ đã được tiếp nhận theo NĐ 13 trước 01/01/2026 dùng tiếp (Luật 91 Đ39 k2). Hoạt động chạy từ trước 01/01/2026 chưa có hồ sơ: suy luận tính 60 ngày từ 01/01/2026 (khoảng 02/03/2026) — đã quá hạn.

### DLCN-R14 — Cập nhật DPIA/TIA: định kỳ 06 tháng khi có thay đổi; 10 ngày với thay đổi lớn
- **Căn cứ**: Luật 91 Đ22 k1–3. NĐ 356 Đ20 k1 (cập nhật định kỳ 06 tháng kể từ lần đầu nộp khi phát sinh mục đích mới; phát sinh/thay đổi bên kiểm soát, bên xử lý, bên thứ ba), k2 (trong 10 ngày khi tổ chức lại, chấm dứt, giải thể, phá sản; thay đổi bên cung cấp dịch vụ BVDLCN; phát sinh/thay đổi ngành nghề liên quan), k3 (Mẫu 03a/03b). NĐ 330 Đ55 k1 d, đ.
- **Áp dụng**: như R13 · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: change log tự tạo việc "cập nhật DPIA" khi thêm đối tác tích hợp, thêm mục đích, đổi nhà cung cấp cloud/vendor (hạn 10 ngày hoặc gộp kỳ 6 tháng).

### DLCN-R15 — Chuyển dữ liệu xuyên biên giới (TIA), kể cả cloud nước ngoài
- **Căn cứ**: Luật 91 Đ20 k1 (chuyển dữ liệu ra hệ thống ngoài lãnh thổ; chuyển cho tổ chức nước ngoài; dùng nền tảng ở nước ngoài xử lý dữ liệu thu thập tại VN), k2 (hồ sơ, gửi bản chính trong 60 ngày từ ngày đầu chuyển), k4, k5, k6 (miễn: cơ quan nhà nước; dữ liệu người lao động trên cloud; chủ thể tự chuyển). NĐ 356 Đ17 k1 a (lưu trên cloud của nhà cung cấp ở nước ngoài là chuyển xuyên biên giới), k3 c (miễn khi khẩn cấp bảo vệ tính mạng, sức khỏe), Đ18 k2–7 (Mẫu 09, nộp kèm Mẫu 01a/01b trong 60 ngày). Luật 91 Đ8 k4 (phạt tối đa 5% doanh thu năm trước với tổ chức). NĐ 330 Đ56 k1 (30–50 triệu), k2 (50–100 triệu), k3 (1–5% doanh thu tại VN nếu dẫn tới lộ, mất dữ liệu ≥ 10.000 công dân), k4 (200 triệu–3 tỷ nếu không có doanh thu), k5 b (đình chỉ chuyển 6–12 tháng).
- **Áp dụng**: mọi bên dùng cloud/SaaS/AI API ở nước ngoài, vendor có đội hỗ trợ nước ngoài truy cập dữ liệu · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấu hình vùng lưu cho từng kho (kể cả backup, log, CDN, giám sát, email/SMS gateway, AI); sổ đăng ký luồng ra nước ngoài (bên nhận, quốc gia, loại dữ liệu, ngày bắt đầu, `tia_submitted_at`); chặn mặc định gửi PHI tới endpoint nước ngoài chưa đăng ký.
- **Bẫy**: Luật BVDLCN không cấm lưu ngoài VN, chỉ buộc TIA. Nghĩa vụ lưu dữ liệu tại VN (Luật 116 Đ25 k3, NĐ 333 Đ19) và yêu cầu "cloud đặt tại Việt Nam" cho HSBA điện tử (CV 365): xem ANM-R19 — phải đáp ứng đồng thời.

### DLCN-R16 — Dữ liệu cốt lõi/quan trọng theo Luật Dữ liệu
- **Căn cứ**: Luật 60/2024 Đ3 k6–7, Đ13 k2 (chủ quản không phải cơ quan nhà nước cũng phải phân loại dữ liệu cốt lõi/quan trọng/khác), Đ23 k2, Đ25 k3–4, Đ27 k3. QĐ 20/2025 Phụ lục mục I.25 (dữ liệu y tế do **cơ quan nhà nước** thu thập, quản lý chưa công khai: bệnh truyền nhiễm mới, thuốc/TBYT phạm vi quốc gia, tác nhân gây bệnh mới, CCHN, lưu hành dược/TBYT) và **I.26 b** (dữ liệu công dân nhạy cảm của ≥ 100.000 công dân Việt Nam — không giới hạn chủ thể là cơ quan nhà nước, gốc-OCR); II.1, II.10. NĐ 165 Đ17 k10 (ghi nhật ký xử lý, lưu ít nhất 06 tháng), k11 (đánh giá rủi ro hằng năm). NĐ 356 Đ42 k3 (sửa NĐ 165 Đ16 k2: dữ liệu cốt lõi/quan trọng là DLCN thì bảo vệ theo pháp luật BVDLCN; chuyển xuyên biên giới làm DPIA/TIA, không làm đánh giá theo NĐ 165). NĐ 363 (từ 11/11/2026) Đ9 (không phân loại dữ liệu: 30–50 triệu, mức tổ chức), Đ19 k3 b (chuyển dữ liệu cốt lõi khi chưa chấp thuận), Đ22 k1 b (không ghi nhật ký ≥ 06 tháng).
- **Áp dụng**: BV/nền tảng/vendor SaaS nắm dữ liệu nhạy cảm ≥ 100.000 công dân; cơ quan, ĐVSN y tế công · **Hiệu lực/hạn**: 01/07/2025; chế tài NĐ 363 từ 11/11/2026
- **Mức**: BẮT BUỘC? (nghĩa vụ riêng cho dữ liệu cốt lõi khi dữ liệu đó là DLCN, sau NĐ 356 Đ42 k3) · BẮT BUỘC (phân loại dữ liệu theo Luật 60 Đ13 k2)
- **Phần mềm phải**: đếm số chủ thể duy nhất có dữ liệu nhạy cảm (cộng dồn), cảnh báo khi vượt 100.000; nhãn cốt lõi/quan trọng/khác; nhật ký xử lý ≥ 06 tháng (khuyến nghị dài hơn, xem P05).
- **Bẫy**: mục I.25 là dữ liệu cốt lõi (đồng thời quan trọng theo II.1) nhưng chỉ áp với dữ liệu do cơ quan nhà nước quản lý; điểm chạm BV tư/vendor là I.26 b.

### E. Sự cố và thông báo vi phạm

### DLCN-R17 — Thông báo vi phạm cho cơ quan chuyên trách trong 72 giờ
- **Căn cứ**: Luật 91 Đ23 k1 (phát hiện vi phạm có thể gây tổn hại: thông báo cơ quan chuyên trách chậm nhất 72 giờ kể từ khi phát hiện; bên xử lý báo kịp thời cho bên kiểm soát), k2 (lập biên bản xác nhận), k3. NĐ 356 Đ28 k1 (nội dung tối thiểu), k2 (gửi cơ quan chuyên trách hoặc qua Cổng thông tin quốc gia về BVDLCN theo Mẫu 08). NĐ 330 Đ54 k1 (không lập biên bản, che giấu: 10–20 triệu), k2 (không thông báo: 20–40 triệu), k3 (chậm hơn 72 giờ: 40–60 triệu), k4 (không ngăn chặn, khắc phục: 60–80 triệu).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: quy trình sự cố có đồng hồ 72 giờ từ `detected_at`; biểu mẫu theo trường Mẫu 08; truy vấn nhanh "dữ liệu của ai, loại gì, bao nhiêu bản ghi" từ log; vendor có kênh báo sự cố tự động cho từng khách hàng.
- **Bẫy**: sự cố an ninh mạng có nghĩa vụ báo cáo riêng (24h/72h/ngay) theo NĐ 331/2026: xem ANM-R16. Hai luồng độc lập, cùng đầu mối Bộ Công an.

### DLCN-R18 — Sinh trắc học và vị trí: thông báo chủ thể trong 72 giờ, lưu hồ sơ sự cố ≥ 05 năm
- **Căn cứ**: Luật 91 Đ31 k4 a, k3 b. NĐ 356 Đ29 k1 a (thông báo chủ thể bị ảnh hưởng ≤ 72 giờ), k1 c (lưu hồ sơ vi phạm tối thiểu 05 năm từ ngày khắc phục xong), k2, k3. NĐ 330 Đ70 k1 (50–70 triệu, gồm không thông báo trong 72 giờ), k2 b (dùng sinh trắc vượt mục đích chưa có đồng ý: 70–150 triệu).
- **Áp dụng**: chấm công/định danh khuôn mặt, vân tay, xác thực người bệnh bằng khuôn mặt, dữ liệu gen; app có định vị · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: template sinh trắc lưu tách biệt, mã hóa, không dùng cho mục đích khác; thông báo người bệnh qua SMS/app theo nội dung Đ29 k2 khi có sự cố; lưu hồ sơ sự cố ≥ 05 năm. Sinh trắc của người bệnh khi ký HSBA: BAOMAT-CB-R23–R25.

### DLCN-R19 — Thông báo sự cố dữ liệu cho chủ thể (Luật Dữ liệu)
- **Căn cứ**: Luật 60/2024 Đ25 k3 (chủ quản không phải cơ quan nhà nước tự đánh giá rủi ro, khắc phục và thông báo cho chủ thể dữ liệu); NĐ 363 Đ22 k1 c (không thông báo sự cố gây thiệt hại), k2 c (không có kế hoạch ứng phó khẩn cấp sự cố dữ liệu).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: Luật từ 01/07/2025; chế tài từ 11/11/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: gửi thông báo hàng loạt cho người bệnh bị ảnh hưởng; kế hoạch ứng phó sự cố dữ liệu bằng văn bản và lịch diễn tập.

### F. Tổ chức, nhân sự, miễn trừ

### DLCN-R20 — Chỉ định nhân sự/bộ phận bảo vệ DLCN (DPO) hoặc thuê dịch vụ
- **Căn cứ**: Luật 91 Đ33 k2. NĐ 356 Đ13 k1 (chỉ định bằng văn bản chính thức), k2 (cao đẳng trở lên; ≥ 02 năm kinh nghiệm pháp chế/CNTT/an ninh mạng/an ninh dữ liệu/quản trị rủi ro/tuân thủ/nhân sự; đã đào tạo BVDLCN), k5, k6; Đ14 (nhiệm vụ); Đ15 (cá nhân cung cấp dịch vụ: ≥ 03 năm kinh nghiệm), Đ16 (tổ chức cung cấp dịch vụ: ≥ 03 nhân sự đủ điều kiện). NĐ 330 Đ57 (cảnh cáo hoặc 10–30 triệu).
- **Áp dụng**: tất cả tổ chức (không miễn khi xử lý dữ liệu nhạy cảm — R21) · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấu hình liên hệ DPO hiển thị ở chính sách quyền riêng tư, biểu mẫu đồng ý, thông báo sự cố; vai trò "DPO" xem nhật ký truy cập, hàng đợi DSR, sổ đăng ký xử lý.

### DLCN-R21 — Phòng khám nhỏ, nhà thuốc, startup y tế không được miễn DPIA/DPO
- **Căn cứ**: Luật 91 Đ38 k2 (DN nhỏ, khởi nghiệp được chọn không làm Đ21, Đ22, Đ33 k2 trong 05 năm, **trừ** DN kinh doanh dịch vụ xử lý DLCN, trực tiếp xử lý DLCN nhạy cảm hoặc xử lý DLCN của số lượng lớn chủ thể), k3 (hộ kinh doanh, DN siêu nhỏ: cùng ngoại lệ). NĐ 356 Đ41 k1–2 (số lượng lớn = từ 100.000 chủ thể cộng dồn).
- **Áp dụng**: PK, nhà thuốc, startup app y tế, vendor · **Hiệu lực/hạn**: 01/01/2026 (miễn trừ cho DN thường kết thúc 01/01/2031)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: checklist triển khai cho khách hàng nhỏ mặc định bật bộ DPIA/DPO.
- **Bẫy**: ngưỡng 100.000 chỉ là một trong ba ngoại lệ; cơ sở y tế đã thuộc ngoại lệ "trực tiếp xử lý dữ liệu nhạy cảm" từ chủ thể đầu tiên. Hộ kinh doanh (nhiều nhà thuốc) bị phạt theo mức cá nhân = 1/2 mức tổ chức (NĐ 330 Đ2 k3, Đ7 k1).

### G. Vendor phần mềm/SaaS/app y tế

### DLCN-R22 — Vendor SaaS/app y tế phải có Giấy chứng nhận đủ điều kiện kinh doanh dịch vụ xử lý DLCN
- **Căn cứ**:
  - Luật 91 Đ33 k3, Đ38 k2–3 (gọi tên "kinh doanh dịch vụ xử lý dữ liệu cá nhân").
  - NĐ 356 Đ21 (danh mục dịch vụ): k1 "Dịch vụ cung cấp và vận hành hệ thống, phần mềm tự động để thay mặt bên kiểm soát, bên kiểm soát và xử lý tiến hành xử lý dữ liệu cá nhân"; k4 "Dịch vụ thu thập, xử lý dữ liệu cá nhân qua trang web, ứng dụng, phần mềm chăm sóc sức khỏe, theo dõi sức khỏe, dịch vụ y tế"; k3, k6, k7, k8 (AI, dữ liệu lớn), k9.
  - NĐ 356 Đ22 (điều kiện): pháp nhân VN; người phụ trách chuyên môn là công dân VN thường trú tại VN; ≥ 03 nhân sự đạt Đ13 k2; hạ tầng phù hợp; có kết quả **đạt** với hồ sơ DPIA (và TIA nếu có).
  - NĐ 356 Đ24 (Bộ Công an cấp), Đ25 (hồ sơ: đơn Mẫu 04, GCN ĐKDN, văn bản chỉ định bộ phận BVDLCN, đề án gồm khung quản trị rủi ro, kế hoạch đánh giá tuân thủ, phương án định danh và xác thực điện tử; quyết định cấp trong 30 ngày từ hồ sơ hợp lệ; Mẫu 05), Đ26 (cấp lại, cấp đổi 05 ngày làm việc), Đ27 (thu hồi).
  - Luật Đầu tư 143/2025 Phụ lục IV STT 198 "Dịch vụ xử lý dữ liệu cá nhân" là ngành nghề kinh doanh có điều kiện từ 01/07/2026 (Đ51 k2); Luật 24/2026/QH16 thay Phụ lục IV từ 01/03/2027, giữ ngành này ở STT 136.
  - NĐ 330 Đ59 k3 a ("Thực hiện hoạt động kinh doanh dịch vụ xử lý dữ liệu cá nhân khi chưa được cấp Giấy chứng nhận đủ điều kiện kinh doanh dịch vụ xử lý dữ liệu cá nhân": 50–80 triệu), k3 b–c (nhân sự không đủ điều kiện, dưới 03 nhân sự), k4 (tiếp tục sau khi bị thu hồi: 80–100 triệu), k5 b–c (buộc xóa dữ liệu xử lý trái phép, nộp lại khoản thu).
- **Áp dụng**: vendor HIS/EMR/LIS/RIS-PACS dạng SaaS/hosted do vendor vận hành; nền tảng khám từ xa, đặt lịch, app theo dõi sức khỏe, app nhà thuốc; dịch vụ AI xử lý dữ liệu thay cơ sở KCB. Không áp cho cơ sở KCB tự vận hành hệ thống của mình (suy luận).
- **Hiệu lực/hạn**: NĐ 356 từ 01/01/2026, **không có điều khoản chuyển tiếp** cho Giấy chứng nhận (NĐ 356 Đ42 chỉ quy định hiệu lực và bãi bỏ NĐ 13; Luật 91 Đ39 chỉ chuyển tiếp đồng ý và hồ sơ đánh giá tác động; Luật Đầu tư 143 Đ52 k15 chỉ chuyển tiếp cho ngành bị bãi bỏ).
- **Mức**: BẮT BUỘC (SaaS/app do vendor vận hành — khớp nguyên văn Đ21 k1, k4) · BẮT BUỘC? (vendor bán license cài tại chỗ nhưng có truy cập từ xa để bảo trì, hỗ trợ, đồng bộ hoặc sao lưu hộ — **còn treo**, §7)
- **Phần mềm phải**: vendor giữ hồ sơ chứng minh điều kiện (hạ tầng, khung quản trị rủi ro, kết quả DPIA đạt); ghi số Giấy chứng nhận trong hợp đồng/điều khoản dịch vụ; khách hàng kiểm tra khi chọn bên xử lý (Luật 91 Đ37 k1 đ).
- **Bẫy**: (1) NĐ 356 Đ27 k1 a dẫn "khoản 1, khoản 2 Điều 26" — có vẻ lỗi dẫn chiếu (điều kiện ở Đ22). (2) Tên giấy dùng lẫn "đủ điều kiện kinh doanh" (Đ25–27) và "đủ điều kiện cung cấp" (Đ24) — cùng một giấy. (3) Chưa thấy văn bản xếp ngành này vào "cấp phép trước" hay "hậu kiểm" theo Luật Đầu tư 143 Đ7 k1. (4) Pháp nhân nước ngoài không đáp ứng Đ22 → phải qua pháp nhân VN.

### DLCN-R23 — Nghĩa vụ của tổ chức đã được cấp Giấy chứng nhận
- **Căn cứ**: NĐ 356 Đ23 (khung quản trị rủi ro; đánh giá hiện trạng tuân thủ và mức độ tín nhiệm 01 năm/lần; tiêu chuẩn an ninh dữ liệu, BVDLCN, ANM; ngăn truy cập trái phép; khi là bên xử lý: yêu cầu bên kiểm soát xin đồng ý của chủ thể trước khi cung cấp dịch vụ, chủ thể biết tên tổ chức cung cấp dịch vụ (k7); xác thực danh tính tổ chức theo pháp luật định danh điện tử (k8)). NĐ 330 Đ59 k1 (20–30 triệu: thiếu khung quản trị rủi ro, quy định trách nhiệm, tiêu chuẩn, xác thực danh tính tổ chức), k2 (30–50 triệu: không yêu cầu xin đồng ý, không đánh giá tuân thủ 01 năm/lần…).
- **Áp dụng**: vendor đã có giấy · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: màn hình đồng ý do vendor cung cấp nêu tên vendor là bên xử lý; báo cáo đánh giá tuân thủ hằng năm; tài khoản định danh điện tử tổ chức (cách thực hiện k8 là suy luận).

### DLCN-R24 — Ứng dụng y tế tuân thủ đầy đủ; dữ liệu lớn: xác thực đa yếu tố, giám sát truy cập
- **Căn cứ**: Luật 91 Đ26 k3 (tổ chức, cá nhân phát triển ứng dụng y tế phải tuân thủ đầy đủ BVDLCN), Đ30 k3. NĐ 356 Đ9 k1 (dữ liệu lớn), k3 b (xác thực mạnh, tối thiểu đa yếu tố; phân quyền), k3 c, k3 d (giám sát liên tục truy cập, phát hiện bất thường), k3 đ. NĐ 330 Đ66 k2 b ("Không sử dụng phương thức xác thực mạnh (tối thiểu xác thực đa yếu tố) hoặc không phân quyền truy cập…": 30–50 triệu), Đ66 k1 (20–30 triệu: thiếu chính sách lưu/xóa, thỏa thuận với bên thứ ba, đào tạo).
- **Áp dụng**: app y tế mọi quy mô (Đ26 k3); HIS/EMR tập trung đa cơ sở, kho dữ liệu y tế, nền tảng phân tích (Đ9) · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC (Đ26 k3, Đ30 k3) · BẮT BUỘC? (Đ9: ranh giới "dữ liệu lớn" chưa định lượng)
- **Phần mềm phải**: MFA cho tài khoản nhân viên truy cập dữ liệu người bệnh (ít nhất truy cập từ xa, quản trị, xuất dữ liệu); nhật ký truy cập mức hồ sơ (ai, khi nào, xem/sửa/xuất gì); cảnh báo bất thường (hồ sơ không thuộc ca điều trị, truy cập hàng loạt, ngoài giờ). Mức kỹ thuật MFA và mật khẩu: ANM-R10.

### DLCN-R25 — AI và xử lý tự động (CDSS, chẩn đoán hình ảnh AI, chatbot)
- **Căn cứ**: Luật 91 Đ30 k4 (xử lý DLCN bằng AI phải phân loại theo mức rủi ro). NĐ 356 Đ10 k2 (kết quả suy luận AI xác định được người cụ thể là DLCN), k3 (thông báo về xử lý tự động, giải thích nguyên tắc thuật toán và ảnh hưởng, cho lựa chọn không tham gia), k5 đ (đánh giá tuân thủ 01 năm/lần), k6. NĐ 330 Đ67 k1 (20–50 triệu), k2 (50–70 triệu), k3 b (quyết định tự động ảnh hưởng quyền lợi không có giám sát hoặc không cho yêu cầu đánh giá lại bởi con người: 70–100 triệu).
- **Áp dụng**: vendor và cơ sở dùng AI trên dữ liệu người bệnh · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hồ sơ phân loại rủi ro từng mô hình; thông báo xử lý tự động trong biểu mẫu đồng ý/chính sách; cờ opt-out theo người bệnh và mô hình; kết quả AI có người hành nghề xác nhận và lưu vết; huấn luyện mô hình bằng dữ liệu người bệnh là mục đích riêng (đồng ý riêng hoặc khử nhận dạng — R26). Yêu cầu AI/TBYT khác: TELE.

### H. Mục đích phụ, khử nhận dạng, quảng cáo, mua bán

### DLCN-R26 — Khử nhận dạng cho nghiên cứu, thống kê, huấn luyện; cấm tái nhận dạng
- **Căn cứ**: Luật 91 Đ2 k1 ("Dữ liệu cá nhân sau khi khử nhận dạng không còn là dữ liệu cá nhân"), Đ2 k11, Đ14 k6 (kiểm soát quá trình khử nhận dạng; không tái nhận dạng trừ khi luật quy định), Đ12 k1 (dữ liệu mã hóa vẫn là DLCN). NĐ 356 Đ7 k5. Luật KCB Đ69 k3–4. NĐ 330 Đ51 k3 b (tái nhận dạng: 50–60 triệu).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC (cấm tái nhận dạng; kiểm soát quá trình) · NÊN (dùng khử nhận dạng thay cho xin đồng ý khi phân tích, huấn luyện AI, báo cáo)
- **Phần mềm phải**: pipeline khử nhận dạng cấu hình được (bỏ định danh trực tiếp, tổng quát hóa ngày sinh/địa chỉ, kiểm k-anonymity); bảng ánh xạ khóa giả danh lưu tách biệt, quyền riêng; ghi vết mọi lần xuất bộ dữ liệu nghiên cứu.
- **Bẫy**: mã hóa hoặc giả danh không phải khử nhận dạng.

### DLCN-R27 — Không mua bán DLCN; chuyển giao có thu phí phải đúng điều kiện
- **Căn cứ**: Luật 91 Đ7 k6, Đ17 k2, Đ8 k3 (phạt tối đa 10 lần khoản thu). NĐ 356 Đ7 k3 (chuyển giao có thu phí: đồng ý theo từng lần, giới hạn loại dữ liệu, không hình thành kho dữ liệu cho mục đích khác). NĐ 330 Đ53 (2–10 lần khoản thu; không có khoản thu: 70 triệu–3 tỷ theo số chủ thể, ngưỡng thấp hơn với dữ liệu nhạy cảm).
- **Áp dụng**: tất cả, nhất là app/nền tảng có doanh thu từ dữ liệu, "bán lead" · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không có tính năng bán/cho thuê danh sách người bệnh; hợp tác có phí thì đồng ý theo từng lần chuyển, ghi bên nhận và mục đích.

### DLCN-R28 — Tin nhắn chăm sóc, quảng cáo, tiếp thị
- **Căn cứ**: Luật 91 Đ28 k3 (quảng cáo phải được đồng ý, rõ nội dung, phương thức, tần suất; có cách từ chối), k5, k8 (quảng cáo theo hành vi chỉ khi có đồng ý). NĐ 330 Đ63 k1 (dùng dữ liệu cơ bản quảng cáo không đồng ý; không có cơ chế từ chối; mặc định đồng ý cho mạng quảng cáo: 30–50 triệu), k2 a (dùng dữ liệu nhạy cảm để phân phối quảng cáo không có đồng ý: 50–70 triệu), k2 c (theo dõi web/app để quảng cáo theo hành vi không có đồng ý: 50–70 triệu).
- **Áp dụng**: PK, BV tư, nhà thuốc, app có CRM/SMS/Zalo marketing · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tách tin nghiệp vụ KCB (kết quả, tái khám) và tin tiếp thị; tin tiếp thị chỉ gửi khi có đồng ý mục đích quảng cáo; mỗi tin có cách hủy; không gắn pixel/SDK quảng cáo vào trang có dữ liệu sức khỏe khi chưa có đồng ý.

### DLCN-R29 — Camera giám sát, ghi âm tại cơ sở
- **Căn cứ**: Luật 91 Đ32 k1 a (ghi hình nơi công cộng không cần đồng ý để bảo vệ an ninh, quyền lợi hợp pháp), k2 (phải thông báo cho người bị ghi hình), k3, k4 (lưu trong thời gian cần thiết rồi xóa).
- **Áp dụng**: BV, PK, nhà thuốc · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: (nếu VMS tích hợp) tự xóa theo thời hạn cấu hình; phân quyền xem lại; ghi vết trích xuất. Không đặt camera ở buồng khám/thủ thuật khi không có căn cứ (suy luận). Ghi hình phiên KCB từ xa: TELE.

### DLCN-R30 — Giới hạn mục đích, chính xác, thời hạn lưu
- **Căn cứ**: Luật 91 Đ3 k2–3. NĐ 330 Đ39 k1 a (vượt phạm vi, mục đích: 20–40 triệu), b (không bảo đảm chính xác), c (lưu vượt thời gian cần thiết).
- **Áp dụng**: tất cả · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi trường thu thập gắn ít nhất một mục đích trong sổ đăng ký xử lý; không thu trường thừa (nghề nghiệp, tôn giáo) khi biểu mẫu chuyên môn không yêu cầu; job định kỳ rà dữ liệu quá hạn lưu.

### I. Bảo mật chuyên ngành y tế

### DLCN-R31 — Bí mật HSBA và quyền khai thác HSBA
- **Căn cứ**: Luật KCB Đ10 k2, Đ45 k5, Đ69 k2 (HSBA được lưu giữ, giữ bí mật), k3 (HSBA đang điều trị: người trực tiếp điều trị, học viên, nghiên cứu viên được đọc, chỉ sao chép khi cơ sở đồng ý; người hành nghề cơ sở khác đọc, sao chép khi cơ sở đồng ý), k4 a (cơ quan quản lý y tế, điều tra, viện kiểm sát, tòa án, thanh tra y tế, giám định, luật sư của người bệnh), k4 b, c (học viên, BHXH, cơ quan bồi thường nhà nước: mượn tại chỗ khi cơ sở đồng ý), k5.
- **Áp dụng**: BV, PK · **Hiệu lực/hạn**: 01/01/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phân quyền HSBA theo trạng thái (đang điều trị/đã lưu trữ) và vai trò khai thác Đ69 k3–4; luồng "đề nghị khai thác HSBA" có phê duyệt, mục đích, thời hạn; chế độ chỉ đọc (không sao chép/in/tải) cho học viên khi chưa được duyệt; ghi vết. Nhật ký truy cập HSBA và thời hạn lưu: BAOMAT-CB-R22.

### DLCN-R32 — Thông tin người nhiễm HIV: danh sách người được biết đóng
- **Căn cứ**: Luật 64/2006/QH11 sửa bởi Luật 71/2020/QH14 Đ30 k1 (người đứng đầu cơ sở xét nghiệm thông báo kết quả dương tính), k2 (chỉ thông báo cho: người được xét nghiệm; vợ/chồng; cha mẹ/giám hộ/đại diện của người dưới 18 tuổi, mất/hạn chế năng lực; người tư vấn trực tiếp; người giám sát dịch tễ HIV; trưởng khoa, điều dưỡng trưởng, nhân viên y tế trực tiếp điều trị; y tế tại cơ sở giam giữ, cai nghiện, bảo trợ; một số cơ quan), k3 (người được tiếp cận: giám sát dịch tễ; BHXH khi giám định, thanh toán BHYT; người của cơ sở y tế trực tiếp thanh toán, quản lý thông tin KCB; người được chính người nhiễm đồng ý), k4–k6, k7 (Bộ trưởng BYT quy định hình thức, quy trình).
- **Áp dụng**: BV, PK, phòng xét nghiệm, LIS, phần mềm điều trị ARV · **Hiệu lực/hạn**: 01/07/2021
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: nhãn "HIV-restricted" cho chỉ định, kết quả XN HIV, chẩn đoán ICD B20–B24/Z21 (danh sách mã cụ thể là suy luận), thuốc ARV; ẩn khỏi màn hình chung, báo cáo khoa, bản in tóm tắt, kết quả trả qua app/Sổ SKĐT trừ người trong danh sách Đ30 k2–3; truy cập ngoài danh sách cần "phá kính" có lý do và cảnh báo DPO. Phần bổ sung (phiếu kết quả, hạn 72 giờ làm việc, HIV-INFO, người chưa thành niên): BAOMAT-CB-R02–R08.
- **Bẫy**: kiểm tương thích với liên thông Sổ SKĐT và XML BHYT — luật HIV cho BHXH tiếp cận (k3) nhưng không nói về hiển thị trên VNeID.

### DLCN-R33 — Dữ liệu y tế theo NĐ 102: tiếp cận có điều kiện
- **Căn cứ**: NĐ 102 Đ6 (số định danh cá nhân là mã định danh y tế), Đ9 k1, Đ9 k2 b (bí mật đời tư, tình trạng sức khỏe, di truyền… được tiếp cận khi người đó đồng ý), k2 c (bí mật gia đình: đồng ý của các thành viên), k2 d, Đ10 k2 c (tổ chức, cá nhân khác khai thác DLCN y tế khi được đồng ý của đơn vị quản lý dữ liệu **và** của chủ thể), Đ10 k5 b và Đ23 k2 (kết nối, chia sẻ với Sổ SKĐT trên VNeID và CSDL quốc gia về y tế), Đ23 k3.
- **Áp dụng**: mọi cơ sở y tế; bên thứ ba khai thác dữ liệu (công ty nghiên cứu, insurtech) · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dùng số định danh cá nhân làm khóa định danh người bệnh (giữ mã nội bộ song song); yêu cầu khai thác của tổ chức ngoài phải qua hai lớp chấp thuận (cơ sở + người bệnh); xét nghiệm gen gia đình cần cơ chế đồng ý của các thành viên (suy luận áp Đ9 k2 c). Liên thông Sổ SKĐT: xem SKDT.

**Tổng hợp mức** (theo mức chính): BẮT BUỘC 32 (R01–R15, R17–R33) · BẮT BUỘC? 1 (R16) · NÊN 0. Phần còn treo nằm trong: R02 (xếp xử lý KCB vào Đ19), R08 (đồng ý kép mọi xử lý trẻ ≥ 7 tuổi), R13 (BV công), R22 (vendor on-premise), R24 (ngưỡng dữ liệu lớn); R26 có phần NÊN.

## 3. Pattern thiết kế

### DLCN-P01 — Sổ đăng ký hoạt động xử lý + nhãn độ nhạy mức trường
- **Giải quyết**: R01, R02, R13, R16, R30
- **Cách làm**: metadata trung tâm "dữ liệu gì, mục đích gì, căn cứ nào, lưu bao lâu, ai nhận"; nguồn sinh DPIA, chính sách quyền riêng tư và kiểm tra luồng xuất.
- **Gợi ý dữ liệu**: `data_element(id, entity, field, sensitivity ENUM('basic','sensitive','hiv_restricted','biometric','genetic'), core_data_candidate BOOL)`; `processing_activity(id, purpose, legal_basis, legal_reference NOT NULL, retention_rule_id, controller_org_id, retired_at)`; `processing_activity_element(activity_id, element_id)`; `recipient(id, type ENUM('internal','processor','third_party','insurer_commercial','healthcare_provider','state'), country_code, contract_ref)`. Ràng buộc: `legal_basis='consent'` thì bắt buộc `consent_template_id`.
- **Đánh đổi**: tốn công khai báo ban đầu; bù lại DPIA và audit gần như tự động.

### DLCN-P02 — Kho bằng chứng đồng ý bất biến theo mục đích
- **Giải quyết**: R03, R08, R09, R25, R28
- **Cách làm**: append-only; rút lại = bản ghi mới; view `effective_consent(subject_id, purpose_code)` dùng cho mọi kiểm tra trước khi xử lý.
- **Gợi ý dữ liệu**: `consent_template(id, version, purpose_code, text_hash, is_sensitive_notice, locale, effective_from)`; `consent_record(id, subject_id, template_id, decision, actor_type ENUM('self','legal_rep','child_and_rep'), actor_ids[], rep_relation, channel, evidence_uri, captured_by, captured_at, ip, device)`; chỉ mục `(subject_id, purpose_code, captured_at DESC)`.
- **Đánh đổi**: cần ký điện tử/OTP và chi phí lưu bằng chứng; bắt buộc vì bên kiểm soát chịu trách nhiệm chứng minh (NĐ 356 Đ6 k2).

### DLCN-P03 — Hàng đợi yêu cầu chủ thể (DSR) có SLA pháp định
- **Giải quyết**: R04–R07
- **Cách làm**: `ack_due_at = received_at + 2 ngày làm việc`; `due_at` theo bảng: withdraw/restrict/object 15 (20 nếu có bên thứ ba), access/rectify/copy 10 (15), erase 20 (30), protect 15; gia hạn 1 lần 15/10/20/15. Fan-out lệnh tới vendor/bên thứ ba qua API có xác nhận.
- **Gợi ý dữ liệu**: `dsr_request(id, subject_id, requester_id, requester_role, type, received_at, verified_at, ack_due_at, ack_sent_at, due_at, extended_until, extension_reason, involves_third_party, status, outcome, refusal_reason)`; `dsr_task(processor_id, action, sent_at, confirmed_at)`.
- **Đánh đổi**: cần lịch ngày làm việc VN cập nhật hằng năm.

### DLCN-P04 — Cổng chia sẻ ra ngoài có "người gác" pháp lý
- **Giải quyết**: R09, R10, R11, R15, R27, R32, R33
- **Cách làm**: mọi tích hợp ra ngoài qua một egress service: kiểm `recipient.type`; bảo hiểm thương mại hoặc cơ sở CSSK khác mà không thuộc căn cứ cấp cứu/luật định → bắt buộc yêu cầu bằng văn bản còn hiệu lực; `country_code != 'VN'` → bắt buộc TIA đã nộp; lọc trường theo độ nhạy (HIV-restricted bị loại trừ trừ người nhận trong danh sách Đ30).
- **Gợi ý dữ liệu**: `written_request(subject_id, recipient_id, scope, signed_at, evidence_uri, expires_at)`; `disclosure_log(id, subject_id, recipient_id, activity_id, legal_basis, payload_hash, fields[], sent_at, actor)`.
- **Đánh đổi**: thêm độ trễ và điểm lỗi; bù lại một chỗ duy nhất để audit.

### DLCN-P05 — Nhật ký truy cập mức hồ sơ + phát hiện bất thường + phá kính
- **Giải quyết**: R01, R16, R24, R31, R32
- **Cách làm**: kho append-only (WORM hoặc hash-chain); cảnh báo khi xem người bệnh ngoài danh sách phân công, > N hồ sơ/giờ, xuất hàng loạt, xem hồ sơ người thân; phá kính có lý do, cảnh báo DPO, rà soát sau. Thời hạn lưu (C22): khung ANM có nhiều mức (90 ngày, 3, 6, 12 tháng tùy đối tượng — ANM-R11); NĐ 165 Đ17 k10 ≥ 06 tháng cho dữ liệu cốt lõi/quan trọng; với log truy cập HSBA không có quy định riêng → **NÊN (suy luận)** lưu bằng thời hạn lưu HSBA liên quan, tối thiểu 05 năm (BAOMAT-CB-R22). Thời hiệu xử phạt 01 năm (NĐ 330 Đ3 k1) là sàn.
- **Gợi ý dữ liệu**: `access_log(id, ts, user_id, role, patient_id, encounter_id, resource_type, action ENUM('view','edit','print','export','share'), reason_code, break_glass BOOL, client_ip, session_id, retain_until)`; phân vùng theo tháng.
- **Đánh đổi**: dung lượng log lớn; nén, chuyển kho lạnh sau 12 tháng.

### DLCN-P06 — Mã hóa và nơi lưu trữ
- **Giải quyết**: R12, R15, R18
- **Cách làm**: mã hóa at-rest (TDE/disk + mã hóa cột cho HIV, gen, sinh trắc với khóa riêng), TLS 1.2+ mọi kết nối, backup mã hóa; KMS/HSM; khóa theo tenant; kiểm tra CI: có thành phần ngoài VN mà không có TIA → fail.
- **Gợi ý dữ liệu**: `storage_location(system, component, provider, region, country_code, contains_personal BOOL)`.
- **Đánh đổi**: mã hóa cột làm khó tìm kiếm; cân nhắc tokenization/blind index.

### DLCN-P07 — Bộ sinh DPIA/TIA từ cấu hình
- **Giải quyết**: R13, R14, R15
- **Cách làm**: sinh nháp Mẫu 10/Mẫu 09 từ P01, P04, P06; trigger thay đổi → việc cập nhật 10 ngày hoặc kỳ 6 tháng.
- **Gợi ý dữ liệu**: `dpia_dossier(id, type ENUM('dpia','tia'), version, submitted_at, receipt_no, result, result_at, next_periodic_update_due)`.
- **Đánh đổi**: phần đánh giá rủi ro vẫn cần người viết.

### DLCN-P08 — Quy trình sự cố có đồng hồ 72 giờ
- **Giải quyết**: R17, R18, R19
- **Cách làm**: truy vấn dựng sẵn trên `access_log`, `disclosure_log` để ước lượng phạm vi; gộp với sổ sự cố ANM (ANM-P07) để không làm hai lần.
- **Gợi ý dữ liệu**: `incident(id, detected_at, controller_notified_at, authority_due_at = detected_at + 72h, authority_notified_at, subject_notice_required, subjects_notified_at, record_retained_until = remediated_at + 5y, affected_count, data_types[], minutes_uri)`.
- **Đánh đổi**: hai luồng báo cáo (DLCN, ANM) khác mẫu, khác nơi nhận chi tiết.

### DLCN-P09 — Trẻ em và người đại diện
- **Giải quyết**: R06, R08
- **Cách làm**: hàm `consent_requirement(subject_dob, purpose, at)` trả `rep_only` (< 7), `child_and_rep` (7–< 18, mục đích ngoài KCB), `self`; lịch nhắc khi tròn 7 và 18 tuổi.
- **Gợi ý dữ liệu**: `legal_representative(subject_id, rep_person_id, rep_type ENUM('8_2_a','8_2_b','8_2_c','8_2_d','8_2_dd'), evidence_uri, valid_from, valid_to)`.
- **Đánh đổi**: thêm bước ở quầy tiếp đón nhi.

### DLCN-P10 — Cách ly dữ liệu cực nhạy
- **Giải quyết**: R18, R32
- **Cách làm**: "restricted compartment" cho HIV, gen, sức khỏe tâm thần, sinh sản (hai nhóm sau là NÊN; căn cứ riêng xem BAOMAT-CB) với nhãn và khóa riêng; báo cáo dùng view đã che; API Sổ SKĐT/app dùng bộ lọc riêng.
- **Gợi ý dữ liệu**: danh mục mã ICD/XN/thuốc gắn nhãn, có phiên bản.
- **Đánh đổi**: báo cáo phức tạp hơn; phải cập nhật danh mục mã.

### DLCN-P11 — Gói tuân thủ dành cho vendor
- **Giải quyết**: R11, R22, R23
- **Cách làm**: đa tenant cách ly; export toàn bộ dữ liệu khách hàng; xóa có biên bản khi chấm dứt; phiên hỗ trợ từ xa just-in-time có phê duyệt của khách hàng; trang "Trust" công bố số Giấy chứng nhận, DPO, bên xử lý phụ, vùng lưu trữ; báo cáo đánh giá tuân thủ hằng năm.
- **Gợi ý dữ liệu**: `support_session(id, tenant_id, approved_by, started_at, ended_at, recording_uri)`.
- **Đánh đổi**: chi phí vận hành; bù lại là điều kiện để được cấp và giữ Giấy chứng nhận.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| DLCN-A01 | R01 | Điều dưỡng khoa A thử mở hồ sơ khoa B; thử export danh sách người bệnh | Ma trận phân quyền; ảnh bị chặn/không; quy trình xử lý dữ liệu nhạy cảm | BẮT BUỘC |
| DLCN-A02 | R02, R30 | Đối chiếu sổ đăng ký xử lý với module thực tế (CRM, app, nghiên cứu, AI) | Sổ có cột căn cứ; mục đích không có căn cứ | BẮT BUỘC |
| DLCN-A03 | R03 | Đăng ký người bệnh mới: checkbox tick sẵn? tách mục đích? câu "dữ liệu nhạy cảm"? DB có thời điểm, phiên bản, kênh, người thu | Ảnh màn hình; 5 bản ghi mẫu; thử xuất bằng chứng | BẮT BUỘC |
| DLCN-A04 | R03 | Từ chối mục đích phụ, kiểm tra vẫn đăng ký khám được | Ảnh màn hình | BẮT BUỘC |
| DLCN-A05 | R04, R05 | Gửi thử yêu cầu xem và rút đồng ý; đo thời gian; hệ thống có tính hạn 2 ngày làm việc/10/15/20/30 ngày | Log DSR; quy trình | BẮT BUỘC |
| DLCN-A06 | R05, R11 | Rút đồng ý marketing → 15 ngày sau SMS/CRM bên thứ ba còn gửi? | Log gửi tin; xác nhận bên xử lý | BẮT BUỘC |
| DLCN-A07 | R06, R31 | Yêu cầu sao HSBA với tư cách người bệnh và đại diện loại 8_2_a | Biểu mẫu yêu cầu; log cung cấp | BẮT BUỘC |
| DLCN-A08 | R07 | Yêu cầu xóa tài khoản app: kiểm DB, backup, log phụ; với HSBA có thư từ chối nêu lý do | Bảng retention; biên bản hủy; thư phản hồi | BẮT BUỘC |
| DLCN-A09 | R08 | Hồ sơ người bệnh 5 tuổi và 10 tuổi: luồng đồng ý đòi đại diện / cả hai; có xác minh tuổi | Ảnh màn hình; `actor_type` | BẮT BUỘC |
| DLCN-A10 | R09 | Liệt kê tích hợp với bảo hiểm (bảo lãnh, TPA) và cơ sở đối tác; truy ngược yêu cầu bằng văn bản | Danh sách endpoint; 10 hồ sơ bảo lãnh mẫu | BẮT BUỘC |
| DLCN-A11 | R10 | Rà kênh xuất: API, XML, email, Excel, USB; mã hóa khi truyền; thỏa thuận chuyển giao | Danh sách kênh; cấu hình TLS; thỏa thuận đủ nội dung NĐ 356 Đ7 k1 | BẮT BUỘC |
| DLCN-A12 | R11 | Đọc hợp đồng vendor, cloud, SMS, lab ngoài: điều khoản xử lý DLCN, xóa/trả dữ liệu, báo sự cố | Hợp đồng/phụ lục DPA | BẮT BUỘC |
| DLCN-A13 | R12 | Cấu hình mã hóa DB, storage, backup; TLS nội bộ | Ảnh KMS/TDE; kết quả quét TLS | BẮT BUỘC |
| DLCN-A14 | R13, R14 | Bản DPIA đã nộp, biên nhận, kết quả; so với hệ thống thực tế; lần cập nhật gần nhất so với thay đổi | Mẫu 10 + 02a/02b; biên nhận; change log | BẮT BUỘC |
| DLCN-A15 | R15 | Liệt kê mọi thành phần lưu/xử lý ngoài VN (region, backup, log SaaS, email, AI API, đội hỗ trợ) | Sơ đồ hạ tầng; TIA Mẫu 09 + 01a/01b | BẮT BUỘC |
| DLCN-A16 | R16 | `COUNT(DISTINCT patient_id)` có dữ liệu sức khỏe; nếu ≥ 100.000 kiểm phân loại dữ liệu và log ≥ 06 tháng | Kết quả truy vấn; văn bản phân loại | BẮT BUỘC? |
| DLCN-A17 | R17 | Diễn tập lộ dữ liệu: thời gian từ phát hiện tới bản thông báo Mẫu 08; xác định người bệnh bị ảnh hưởng từ log | Quy trình; biên bản diễn tập | BẮT BUỘC |
| DLCN-A18 | R18 | Nơi lưu template sinh trắc, mã hóa, phân quyền; quy trình thông báo 72 giờ; lưu hồ sơ 5 năm | Cấu hình; quy trình | BẮT BUỘC |
| DLCN-A19 | R20, R21 | Quyết định chỉ định DPO; bằng cấp, kinh nghiệm, chứng nhận đào tạo; thỏa thuận bảo mật | Quyết định; CV; chứng chỉ | BẮT BUỘC |
| DLCN-A20 | R22 | Vendor SaaS/app: Giấy chứng nhận (số, ngày, phạm vi theo Đ21); nếu chưa có: biên nhận hồ sơ | Bản sao giấy hoặc biên nhận | BẮT BUỘC (SaaS) / BẮT BUỘC? (on-prem) |
| DLCN-A21 | R23 | Vendor có giấy: báo cáo đánh giá tuân thủ năm gần nhất; khung quản trị rủi ro; màn hình đồng ý nêu tên vendor | Báo cáo; ảnh màn hình | BẮT BUỘC |
| DLCN-A22 | R24 | MFA cho admin, truy cập từ xa, export; giám sát truy cập bất thường | Cấu hình IdP; mẫu cảnh báo | BẮT BUỘC? |
| DLCN-A23 | R25 | Liệt kê tính năng AI: thông báo, opt-out, bác sĩ xác nhận, hồ sơ phân loại rủi ro | Tài liệu mô hình; ảnh UI | BẮT BUỘC |
| DLCN-A24 | R26 | Bộ dữ liệu nghiên cứu/AI đã xuất có định danh trực tiếp? bảng ánh xạ giả danh tách quyền? | Mẫu dữ liệu; quy trình | BẮT BUỘC / NÊN |
| DLCN-A25 | R27 | Rà hợp đồng doanh thu với đối tác (giới thiệu người bệnh, quảng cáo, data partnership) | Hợp đồng; luồng dữ liệu | BẮT BUỘC |
| DLCN-A26 | R28 | CRM: tin tiếp thị chỉ gửi người có đồng ý; có cách hủy; pixel quảng cáo trên trang có dữ liệu sức khỏe | Danh sách chiến dịch; tag manager | BẮT BUỘC |
| DLCN-A27 | R29 | Biển thông báo camera; chính sách tự xóa của VMS | Ảnh; cấu hình | BẮT BUỘC |
| DLCN-A28 | R31 | Tài khoản học viên thử in, tải, sao chép HSBA đang điều trị | Ảnh; log | BẮT BUỘC |
| DLCN-A29 | R32 | Nhân viên không điều trị người bệnh HIV thử tìm XN HIV, B20–B24, ARV; xem bản in tóm tắt, app, dữ liệu gửi Sổ SKĐT | Ảnh; log truy cập | BẮT BUỘC |
| DLCN-A30 | R33 | Số định danh cá nhân là mã định danh y tế; cung cấp dữ liệu cho tổ chức ngoài có 2 lớp chấp thuận | Schema; quy trình | BẮT BUỘC |
| DLCN-A31 | R01, R24 | Log truy cập mức hồ sơ tồn tại, không sửa được; truy vấn log 6 tháng trước | Truy vấn; cấu hình WORM | NÊN (BẮT BUỘC? với dữ liệu cốt lõi) |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 01/07/2021 | Luật 71/2020/QH14 (HIV) có HL — Đ30 mới | BV, PK, phòng XN | Đã qua |
| 01/01/2024 | Luật KCB 15/2023 có HL (Đ10, Đ69) | BV, PK | Đã qua |
| 01/07/2025 | Luật Dữ liệu, NĐ 165, QĐ 20/2025, NĐ 102 có HL | Tất cả; cơ sở y tế kết nối Sổ SKĐT (NĐ 102 Đ23) | Đã qua |
| 01/01/2026 | Luật 91 + NĐ 356 có HL; NĐ 13/2023 hết HL; DPIA/TIA, DPO, SLA quyền chủ thể; Giấy chứng nhận dịch vụ xử lý DLCN (không chuyển tiếp) | Tất cả; vendor SaaS/app | Đã qua |
| ~02/03/2026 | 60 ngày từ 01/01/2026: hạn nộp DPIA/TIA cho hoạt động đang chạy (suy luận) | Bên kiểm soát, vendor | Đã qua |
| 01/07/2026 | Phụ lục IV Luật Đầu tư 143: "Dịch vụ xử lý dữ liệu cá nhân" (STT 198) là ngành nghề có điều kiện | Vendor | Đã qua |
| 19/08/2026 | NĐ 330/2026 có HL: chế tài BVDLCN | Tất cả | Đã qua |
| 25/09/2026 | NĐ 314/2026 (sàn dữ liệu) có HL | Ngoại vi | Đã qua |
| **11/11/2026** | NĐ 363/2026 có HL: chế tài lĩnh vực dữ liệu (phân loại, cốt lõi/quan trọng, log ≥ 06 tháng, chuyển dữ liệu cốt lõi) | BV/nền tảng lớn; ĐVSN y tế công; vendor | Sắp tới |
| 01/03/2027 | Luật 24/2026/QH16 có HL; Phụ lục IV mới, dịch vụ xử lý DLCN ở STT 136 | Vendor | Sắp tới |
| 01/01/2031 | Hết 05 năm tùy chọn cho DN nhỏ/khởi nghiệp (không áp cho bên xử lý dữ liệu nhạy cảm) | — | Tương lai |
| Thường xuyên | Phản hồi chủ thể 02 ngày làm việc; thực hiện 10/15/20/30 ngày; thông báo vi phạm ≤ 72 giờ; cập nhật DPIA/TIA 06 tháng hoặc 10 ngày; nộp DPIA/TIA ≤ 60 ngày khi bắt đầu xử lý/chuyển mới; đánh giá tuân thủ 01 năm/lần (vendor có giấy, cloud, AI) | Như trên | — |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**
- NĐ 13/2023 → Luật 91/2025 + NĐ 356/2025 (01/01/2026). Đồng ý và hồ sơ đánh giá tác động đã nộp theo NĐ 13 vẫn dùng được (Luật 91 Đ39 k1–2). Văn bản còn dẫn NĐ 13 (TT 38/2024/TT-BYT, QĐ 69/2025/QĐ-TTg, QĐ 425/QĐ-BYT) → đọc thành Luật 91 + NĐ 356.
- NĐ 165/2025 Đ16 k2 bản gốc bị **đảo ngược** bởi NĐ 356 Đ42 k3 — trích nguyên bản là lỗi thời.
- Luật Đầu tư 2020 Phụ lục IV → Luật 143/2025 Phụ lục IV (01/07/2026, STT 198) → Luật 24/2026/QH16 Phụ lục IV (01/03/2027, STT 136).
- NĐ 102/2025 căn cứ Luật ANM 2018 và Luật ATTT mạng 2015 — đã bị Luật ANM 116/2025 thay từ 01/07/2026 (xem ANM).

**Bẫy trích dẫn**
1. **Mốc DPIA**: nộp trong 60 ngày từ ngày đầu xử lý (Luật 91 Đ21 k1; NĐ 356 Đ19 k4) **và** cập nhật định kỳ 06 tháng khi có thay đổi (Đ22 k1; NĐ 356 Đ20 k1), 10 ngày với thay đổi lớn (NĐ 356 Đ20 k2).
2. **Số điều NĐ 356**: Đ13 điều kiện nhân sự; Đ14 nhiệm vụ; Đ17 xuyên biên giới; Đ18 hồ sơ TIA; Đ19 DPIA; Đ20 cập nhật; Đ21 danh mục dịch vụ xử lý DLCN; Đ22 điều kiện; Đ23 trách nhiệm; Đ24–27 Giấy chứng nhận; Đ28 nội dung thông báo vi phạm; Đ29 vị trí/sinh trắc; Đ41 ngưỡng 100.000.
3. **72 giờ** báo cơ quan chuyên trách ở Luật 91 Đ23 k1, không phải NĐ 356 Đ29 (Đ29 là báo chủ thể với dữ liệu vị trí/sinh trắc; Đ8 k3 là 72 giờ cho tài chính, ngân hàng).
4. **Mức phạt**: NĐ 330 Đ7 k1 — Mục BVDLCN là mức tổ chức, cá nhân bằng 1/2; ngược với mục an ninh mạng (mức cá nhân, tổ chức × 2). NĐ 363 Đ6 k2: mức cá nhân, tổ chức × 2, trừ Đ8 k1 b, Đ9, Đ10, Đ13 k2, Đ16 k4 là mức tổ chức.
5. NĐ 330 Đ62 k2 không chép ngoại lệ Đ19 k1 của Luật 91 Đ26 k2 — áp dụng theo Luật.
6. NĐ 330 Đ60 k1 c đòi đồng ý kép cho mọi xử lý dữ liệu trẻ từ đủ 7 tuổi; Luật 91 Đ24 k2 chỉ đòi khi xử lý nhằm công bố, tiết lộ đời sống riêng tư.
7. NĐ 356 Đ27 k1 a dẫn "khoản 1, khoản 2 Điều 26" — có vẻ lỗi (điều kiện ở Đ22).
8. QĐ 20/2025 mục 25 (y tế) là dữ liệu cốt lõi nhưng chỉ cho dữ liệu do cơ quan nhà nước quản lý; điểm chạm BV tư/vendor là I.26 b (gốc-OCR, cần đối chiếu bản text).
9. Nơi nhận DPIA: NĐ 330 Đ55 k1 b ghi rõ Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (Bộ Công an); Luật/NĐ 356 chỉ ghi "cơ quan chuyên trách".
10. Thanh tra BYT không có tên trong thẩm quyền xử phạt BVDLCN của NĐ 330 Đ74 (chưa đọc hết Đ72–78).
11. Dữ liệu mã hóa vẫn là DLCN (Luật 91 Đ12 k1).
12. Không dùng hethongphapluat làm nguồn (C24).

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. **Vendor bán bản cài tại chỗ (on-premise)** có truy cập từ xa để bảo trì, đồng bộ, sao lưu hộ: có phải "dịch vụ cung cấp và vận hành hệ thống… thay mặt bên kiểm soát" (NĐ 356 Đ21 k1) không? Hỏi Cục A05. Kết luận cho SaaS/hosted do vendor vận hành là BẮT BUỘC (R22); phần on-premise còn treo.
2. **Không có chuyển tiếp cho Giấy chứng nhận**: vendor đang hoạt động trước 01/01/2026 bị coi là vi phạm từ ngày nào? Ngành STT 198 là "cấp phép trước" hay "hậu kiểm" theo Luật Đầu tư 143 Đ7 k1? Phụ lục IV Luật Đầu tư 2020 có ngành này không?
3. **Căn cứ cho xử lý KCB cốt lõi** (lập HSBA, gửi BHYT, liên thông Sổ SKĐT, báo cáo bệnh truyền nhiễm): Đ19 k1 đ/d hay vẫn cần đồng ý theo Đ26 k1 a?
4. **Đ26 k2 và luồng lâm sàng**: chuyển tuyến, hội chẩn, gửi mẫu tới phòng XN ngoài, bác sĩ gia đình có cần yêu cầu bằng văn bản? Phòng XN ngoài là bên xử lý hay bên thứ ba?
5. **"Yêu cầu bằng văn bản"** cho bảo lãnh viện phí có chấp nhận OTP, ký trên app?
6. **Trẻ em**: Luật 91 Đ24 k2 hay NĐ 330 Đ60 k1 c? Đồng ý của trẻ 7 tuổi trong KCB triển khai thế nào?
7. **BV công lập** có được miễn DPIA như cơ quan nhà nước có thẩm quyền (Luật 91 Đ21 k6, Đ20 k6 a) — suy luận là không.
8. **Bên xử lý có phải nộp DPIA** cho cơ quan chuyên trách: Luật 91 Đ21 k3 nói "lập và lưu trữ theo thỏa thuận"; NĐ 356 Đ19 k1, k4 và NĐ 330 Đ55 k1 b có thể hiểu là phải nộp.
9. **Mốc 60 ngày** cho hoạt động xử lý có từ trước 01/01/2026 (không có hồ sơ theo NĐ 13).
10. **Ngày lịch hay ngày làm việc** cho mốc thực hiện 10/15/20/30 ngày (NĐ 356 Đ5).
11. **Dữ liệu cốt lõi ≥ 100.000 công dân** (QĐ 20 I.26 b, gốc-OCR): sau NĐ 356 Đ42 k3, BV tư/vendor còn nghĩa vụ riêng của Luật Dữ liệu (log ≥ 06 tháng, đánh giá rủi ro hằng năm, chấp thuận trước khi chuyển dữ liệu cốt lõi ra nước ngoài theo NĐ 165 Đ12 k5, NĐ 363 Đ19 k3 b) không?
12. **Dữ liệu nhạy cảm chuyên biệt khác** (tâm thần, IVF, di truyền, ma túy, ghép tạng): xem BAOMAT-CB. Văn bản BYT hướng dẫn Luật HIV Đ30 k7 và VBHN mới nhất của Luật HIV chưa kiểm; Luật 71/2020 mới đọc từ bản sao trên cổng Công an Đắk Lắk.
13. **Chưa đọc chi tiết**: NĐ 330 Đ72–79 (thẩm quyền); các Mẫu 01–10 NĐ 356; NĐ 363 Đ8, 10–18, 20–21, 23–33; QĐ 2623/QĐ-TTg; NĐ 169/347, NĐ 314. Địa chỉ và thủ tục nộp trực tuyến trên Cổng thông tin quốc gia về BVDLCN chưa kiểm.
