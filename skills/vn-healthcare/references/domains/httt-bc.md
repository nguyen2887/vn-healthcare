# HTTT-BC — HTTT quốc gia, CSDL y tế và báo cáo bắt buộc

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám, trạm y tế, cơ sở xét nghiệm, vendor HIS/LIS · Research gốc: `research/deep/HTTT-BC.md`

Phạm vi: cung cấp dữ liệu lên HTTT về quản lý hoạt động KCB (Luật KCB Đ112, TT 38/2024); kết nối CSDL quốc gia về y tế (NĐ 102/2025, QĐ 11/2026/QĐ-TTg); Hệ thống quản lý quốc gia về hành nghề và hoạt động KCB; báo cáo thống kê (TT 23/2025); giám sát bệnh truyền nhiễm và phòng bệnh (Luật Phòng bệnh 2025, TT 15/2026); sự cố y khoa (Luật KCB Đ71, TT 43/2018); tiêu chuẩn chất lượng và mức ứng dụng CNTT. Giao sang domain khác: XML BHYT (BHYT-DATA, BHYT-GD); đơn thuốc quốc gia (DUOC); Sổ SKĐT, KSK, mã định danh (SKDT); giấy báo tử, phiếu CĐNNTV (GIAYTO); an toàn hệ thống (ANM); dữ liệu cá nhân (DLCN); HSBA điện tử (EMR). Tài liệu nghiên cứu, không phải ý kiến pháp lý.

## Tóm tắt nhanh

- **01/01/2027**: TT 38/2024 có hiệu lực; mọi cơ sở KCB phải cung cấp dữ liệu đầy đủ, chính xác, kịp thời lên HTTT quản lý KCB, **cho mọi người bệnh** (cả tự chi trả), gồm dân tộc, nghề nghiệp, ICD-9-CM cho PT/TT, ngày giường HSTC… mà XML BHYT không có.
- Nhưng HTTT chưa sẵn sàng nhận từ HIS: kết nối với HTTT của cơ sở là **giai đoạn 2 (2027–2028)** của QĐ 2114/2026, hướng dẫn kỹ thuật chưa ban hành. Chuẩn bị dữ liệu; đừng hứa "đã kết nối".
- Hạ tầng CNTT kết nối HTTT là **điều kiện cấp GPHĐ**: hồ sơ mới từ 01/01/2027, cơ sở cũ chậm nhất **01/01/2029** (Luật KCB **Đ120 k5**, không phải k6; C05).
- TT 23/2025 (báo cáo thống kê) tự hết hiệu lực **01/03/2027**, văn bản thay chưa ban hành: báo cáo tháng hạn 05 ngày làm việc, kể cả cơ sở tư nhân.
- Từ 01/07/2026 báo cáo bệnh truyền nhiễm theo **TT 15/2026**; TT 54/2015 và TT 17/2019 **đã bị bãi bỏ** (Đ65 k2; C11). Ca nghi ngờ: báo TYT xã trong 24 giờ; tử vong do BTN: 24 giờ. Thời hạn từng bệnh nay nằm ở hướng dẫn chuyên môn Cục Phòng bệnh (chưa tìm thấy).
- Sự cố y khoa (TT 43/2018, còn hiệu lực): NC3 báo cáo bắt buộc; sự cố nghiêm trọng gọi báo trước trong **01 giờ**; RCA đề xuất giải pháp trong 60 ngày; tổng hợp 6 tháng; báo cáo tự nguyện phải ẩn danh được.
- Bẫy: TT 38 **không có** thời hạn gửi theo lượt KCB và không có chuẩn kết nối; đừng gán mốc "24 giờ" cho TT 38.

## Mục lục

- **A. HTTT quản lý KCB (TT 38)**: HTTT-BC-R01 Nghĩa vụ cung cấp dữ liệu lên HTTT quản lý KCB · HTTT-BC-R02 Bộ dữ liệu ra viện của mọi ca · HTTT-BC-R03 Thuốc, DVKT, chỉ số lâm sàng/CLS của mọi lượt · HTTT-BC-R04 Tóm tắt điều trị (TT 38 Đ8 k4) · HTTT-BC-R05 Tử vong và người bệnh nặng xin về · HTTT-BC-R06 Người hành nghề, người thực hành, đăng ký hành nghề · HTTT-BC-R07 Dữ liệu cơ sở: giấy phép, giường, thiết bị, kho · HTTT-BC-R08 Dữ liệu chất lượng, hài lòng, sự cố · HTTT-BC-R09 Hoạt động chuyên môn và tài chính 6/12 tháng · HTTT-BC-R10 Danh mục kỹ thuật, phác đồ · HTTT-BC-R11 Niêm yết giá, công khai thông tin · HTTT-BC-R12 Hạch toán chi phí theo ca bệnh · HTTT-BC-R13 Sửa sai và thông báo thay đổi "ngay" · HTTT-BC-R14 Cung cấp dữ liệu khi khẩn cấp, dịch nhóm A · HTTT-BC-R15 Tai nạn thương tích, trực lễ tết · HTTT-BC-R16 Dùng mã định danh từ CSDL quốc gia · HTTT-BC-R17 Chuẩn đầu ra, hướng dẫn kỹ thuật kết nối · HTTT-BC-R18 Bảo mật, toàn vẹn khi kết nối · HTTT-BC-R19 Hạ tầng CNTT kết nối HTTT là điều kiện GPHĐ
- **B. CSDL quốc gia về y tế**: HTTT-BC-R20 Kết nối CSDL quốc gia về y tế và các CSDL khác · HTTT-BC-R21 Tôn trọng dữ liệu chủ quốc gia
- **C. Báo cáo thống kê (TT 23)**: HTTT-BC-R22 Sổ ghi chép ban đầu theo mẫu · HTTT-BC-R23 Báo cáo thống kê tháng, năm; hạn 05 ngày làm việc · HTTT-BC-R24 Biểu 14/BCT bệnh tật, tử vong theo ICD-10 · HTTT-BC-R25 Chuyển chế độ báo cáo mới trước 01/03/2027
- **D. Giám sát BTN, phòng bệnh (TT 15)**: HTTT-BC-R26 Báo cáo trực tuyến qua HTTT giám sát; dự phòng khi lỗi · HTTT-BC-R27 Ca nghi BTN 24 giờ, tử vong do BTN 24 giờ · HTTT-BC-R28 Giám sát dựa vào sự kiện, chùm ca · HTTT-BC-R29 BKLN, rối loạn tâm thần: 05 ngày làm việc · HTTT-BC-R30 Danh mục BTN nhóm A, B, C mới · HTTT-BC-R31 Bảo mật thông tin người mắc BTN
- **E. Sự cố y khoa (TT 43)**: HTTT-BC-R32 Kênh báo cáo sự cố y khoa, nội dung tối thiểu · HTTT-BC-R33 Thời hạn báo cáo sự cố bắt buộc · HTTT-BC-R34 Phân loại, RCA, tổng hợp định kỳ · HTTT-BC-R35 Bảo mật, ẩn danh người báo cáo sự cố
- **F. Chất lượng, mức ứng dụng CNTT**: HTTT-BC-R36 Tự đánh giá chất lượng hằng năm · HTTT-BC-R37 Mức ứng dụng CNTT theo TT 54/2017

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ23 k2 d, Đ36–38, Đ52 k2 d, Đ57, Đ58, Đ60, Đ71, Đ112, Đ120 | 01/01/2024; mốc riêng ở Đ120 | Còn hiệu lực | gốc | [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 38/2024/TT-BYT (16/11/2024) | HTTT về quản lý hoạt động KCB | 01/01/2027 (Đ13) | Sắp có hiệu lực; 15 điều; không có thời hạn gửi theo lượt, không có chuẩn kết nối | gốc | [VB 211878](https://vanban.chinhphu.vn/?pageid=27160&docid=211878) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/38-byt.pdf) |
| 2114/QĐ-BYT (13/07/2026) | Kế hoạch xây dựng HTTT quản lý KCB; GĐ 2 (2027–2028) kết nối HTTT cơ sở | Từ ngày ký | Còn hiệu lực (kế hoạch) | gốc | [Trang đăng lại](https://bvdkbaclieu.gov.vn/van-ban-phap-quy/quyet-dinh-2114-qd-byt-2026-ve-viec-ban-hanh-ke-hoach-xay-du.html) · [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20260807/803_Quyet-dinh-2114-QD-BYT_96963d54a6.pdf) |
| 1642/KH-BYT (13/11/2025) | Triển khai Hệ thống quản lý quốc gia về hành nghề và hoạt động KCB | Từ ngày ký | Còn hiệu lực (kế hoạch) | thứ cấp (bài chính thức trên kcb.vn) | [kcb.vn](https://kcb.vn/tin-tuc/ke-hoach-trien-khai-he-thong-quan-ly-quoc-gia-ve-hanh-nghe-va-hoat-dong-kham-benh-chua-benh.html?categoryId=101795273) · [HDSD cho cơ sở KCB v1.0](https://cdn.haiphong.gov.vn/gov-hpg/6847/tintuc/2026/1/hdsd_qlhnkcb_cskcb_v1639045285307707584.pdf) |
| 4016/BYT-KCB (02/06/2026) | Cập nhật 100% dữ liệu người hành nghề, cơ sở trên Hệ thống quản lý quốc gia | Từ ngày ký | Văn bản điều hành | thứ cấp | [luatvietnam (thứ cấp)](https://luatvietnam.vn/tin-van-ban-moi/yeu-cau-cap-nhat-100-du-lieu-nguoi-hanh-nghe-kham-chua-benh-tren-he-thong-quan-ly-quoc-gia-186-109411-article.html) |
| 96/2023/NĐ-CP | Chi tiết Luật KCB: Đ6–7 thực hành, Đ27–29 đăng ký hành nghề | 01/01/2024 | Còn hiệu lực; chưa kiểm tra sửa đổi 2025–2026 | thứ cấp (toàn văn đăng lại trên cổng tỉnh) | [laichau.gov.vn](https://laichau.gov.vn/tin-tuc-su-kien/chuyen-de/tin-trong-nuoc/toan-van-nghi-dinh-so-96-2023-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-cua-luat-kham-benh-chua-benh.html) |
| 102/2025/NĐ-CP (13/05/2025) | Quản lý dữ liệu y tế: Đ6, Đ10, Đ14–17, Đ23, Đ24 | 01/07/2025 | Còn hiệu lực | gốc (Công báo có text) | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-102-2025-nd-cp-44865.htm) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/102-ndcp.signed.pdf) |
| 11/2026/QĐ-TTg (28/03/2026) | Danh mục CSDL quốc gia; **mục XVIII** CSDLQG về y tế | 19/05/2026 | Còn hiệu lực | gốc-OCR | [VB 217335](https://vanban.chinhphu.vn/?pageid=27160&docid=217335) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/11-ttg.signed.pdf) |
| 194/2025/NĐ-CP (03/07/2025) | CSDLQG, kết nối chia sẻ dữ liệu; Đ40 k2 a bãi bỏ NĐ 47/2024 | 19/08/2025 | Còn hiệu lực | gốc-OCR | [VB 214448](https://vanban.chinhphu.vn/?pageid=27160&docid=214448) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/194-ndcp.signed.pdf) |
| 278/2025/NĐ-CP (22/10/2025) | Kết nối, chia sẻ dữ liệu bắt buộc giữa cơ quan thuộc hệ thống chính trị | 22/10/2025 | Còn hiệu lực | gốc-OCR (Đ1–Đ6) | [VB 215682](https://vanban.chinhphu.vn/?pageid=27160&docid=215682) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/10/278-cp.signed.pdf) |
| 23/2025/TT-BYT (28/06/2025) | Chế độ báo cáo thống kê ngành y tế; PL I–V | 01/07/2025 | Còn hiệu lực; tự hết hiệu lực 01/03/2027; thay TT 32/2014 | gốc | [VB 214349](https://vanban.chinhphu.vn/?pageid=27160&docid=214349) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/23-byt.pdf) · [PL III](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/2_phuluciii.signed.pdf) · [PL IV](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/2_phuluciv.signed.pdf) |
| Dự thảo TT thay TT 23/2025 | — | Dự kiến xong xây dựng 10/2026 | Dự thảo, chưa có toàn văn | thứ cấp | [suckhoedoisong (báo, bối cảnh)](https://suckhoedoisong.vn/bo-y-te-xay-dung-thong-tu-thay-the-thong-tu-hien-hanh-de-nang-cao-chat-luong-thong-tin-quan-ly-cua-nganh-169260514172322497.htm) |
| 114/2025/QH15 | Luật Phòng bệnh: Đ13, Đ17, Đ45 | 01/07/2026 | Còn hiệu lực; thay Luật PCBTN 2007 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat114-2025.pdf) |
| 15/2026/TT-BYT (17/05/2026) | Chi tiết Luật Phòng bệnh: HTTT giám sát, báo cáo BTN, BKLN, RLTT, dinh dưỡng, thương tích | 01/07/2026 | Còn hiệu lực; Đ65 k2 bãi bỏ TT 54/2015, TT 17/2019, TTLT 16/2013, QĐ 25/2006 | gốc | [VB 218141](https://vanban.chinhphu.vn/?pageid=27160&docid=218141) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/15-byt.pdf) |
| 165/2026/NĐ-CP (15/05/2026) | Chi tiết Luật Phòng bệnh; Đ74 k4 c kết quả KSK lập Sổ SKĐT | 01/07/2026 | Còn hiệu lực | gốc-OCR | [VB 218169](https://vanban.chinhphu.vn/?pageid=27160&docid=218169) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/165-ndcp.signed.pdf) |
| 1965/QĐ-BYT (2026) | Danh mục BTN nhóm A (15), B (47), C (19) | 01/07/2026 (thứ cấp) | Còn hiệu lực | thứ cấp | [CDC Đồng Nai (thứ cấp)](https://dongnaicdc.vn/bo-y-te-ban-hanh-danh-muc-moi-cac-benh-truyen-nhiem-chinh-thuc-ap-dung-tu-ngay-1-7-2026) |
| 43/2018/TT-BYT (26/12/2018) | Phòng ngừa sự cố y khoa | 01/03/2019 | Còn hiệu lực (không thấy văn bản thay) | gốc-OCR | [Trang](https://tulieuvankien.dangcongsan.vn/he-thong-van-ban/van-ban-quy-pham-phap-luat/thong-tu-so-432018tt-byt-ngay-26122018-cua-bo-y-te-huong-dan-phong-ngua-su-co-y-khoa-trong-cac-co-so-kham-benh-chua-5058) · [PDF](https://tulieuvankien.dangcongsan.vn/upload/3000006/20251024/88d890ce0c9460dc40a1a463848996f9TT-43-BYT.pdf) · [luatvietnam, trạng thái (thứ cấp)](https://luatvietnam.vn/y-te/thong-tu-43-2018-tt-byt-phong-ngua-su-co-y-khoa-trong-cac-co-so-kham-benh-chua-benh-169832-d1.html) |
| 35/2024/TT-BYT (16/11/2024) | Tiêu chuẩn chất lượng cơ bản đối với **bệnh viện** | 01/01/2025 | Còn hiệu lực; không có tiêu chí kỹ thuật CNTT | gốc | [PDF, kcb.vn](https://kcb.vn/upload/2005611/20241119/35-TT-BYT_signed_8fd6b.pdf) |
| Dự thảo TT tiêu chuẩn chất lượng cơ sở ngoài BV | — | Dự kiến 01/01/2027 | Dự thảo; báo chí nêu có tiêu chí CNTT, CĐS | thứ cấp | [thanhnien (báo, bối cảnh)](https://thanhnien.vn/phong-kham-tram-y-te-se-phai-danh-gia-chat-luong-hang-nam-185260923095957611.htm) |
| 54/2017/TT-BYT (29/12/2017) | Bộ tiêu chí ứng dụng CNTT tại cơ sở KCB | 27/02/2018 | Còn hiệu lực một phần: Mục VIII PL I và tiêu chí EMR hết hiệu lực 06/06/2025 (TT 13/2025 Đ4 k3 b) | chưa xác minh (chưa đọc gốc) | link chưa kiểm tra được |
| 90/2026/NĐ-CP (30/03/2026) | Xử phạt VPHC y tế: Đ7, Đ38, Đ39 | 15/05/2026 | Còn hiệu lực | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| 07/CT-BYT (09/2026) | Xử lý điểm nghẽn CĐS y tế: 7 nhóm nhiệm vụ | Từ ngày ký | Còn hiệu lực; chưa có bản gốc | thứ cấp | [daibieunhandan (báo, bối cảnh)](https://daibieunhandan.vn/bo-y-te-7-nhom-nhiem-vu-day-manh-va-xu-ly-dut-diem-cac-diem-nghen-ve-chuyen-doi-so-y-te-thuc-day-trien-khai-de-an-06-10430624.html) |
| 2682/QĐ-BYT (22/08/2026, theo kết quả tìm kiếm) | Danh mục thông tin cơ bản của CSDL về hoạt động KCB | Từ ngày ký | chưa xác minh | chưa xác minh | link chưa kiểm tra được |

Đã xử lý trạng thái: NĐ 47/2024 bị NĐ 194/2025 Đ40 k2 a bãi bỏ (19/08/2025); TT 54/2015 bị TT 15/2026 Đ65 k2 b bãi bỏ (01/07/2026). NQ 282/2025/NQ-CP, QĐ 3516/2025/QĐ-BYT chỉ là bối cảnh chiến lược.

**Chế tài (NĐ 90/2026, gốc-OCR, diễn giải; mức cá nhân, tổ chức gấp 2 theo Đ4 k5)**

| Hành vi | Điều khoản | Mức (cá nhân) |
|---|---|---|
| Không báo cáo hoặc báo cáo không đúng về giám sát BTN | Đ7 k2 b | 1–3 triệu |
| Che giấu, không khai báo, khai báo không kịp thời hoặc cố ý khai sai BTN nhóm A | Đ7 k3 a, b | 10–20 triệu |
| Thu chi phí chưa niêm yết công khai | Đ38 k3 b | 1–3 triệu |
| Không gửi danh sách đăng ký hành nghề đã thay đổi | Đ39 k2 a | 3–5 triệu |
| Không bảo đảm điều kiện hoạt động sau khi được cấp GPHĐ (cơ sở khác / PKĐK / BV < 100 giường / 100–500 / > 500) | Đ39 k2 b; k3 b; k4 c; k5 c; k6 d | 3–5 / 10–20 / 20–30 / 30–40 / 40–50 triệu; tước GPHĐ 02–04 tháng (k7 a) |

Không thấy trong NĐ 90 hành vi riêng về "không cung cấp dữ liệu lên HTTT quản lý KCB" hay "không báo cáo sự cố y khoa". Chế tài báo cáo thống kê nằm ở nghị định xử phạt lĩnh vực thống kê (chưa đọc).

## 2. Yêu cầu

### A. HTTT về quản lý hoạt động KCB (Luật KCB Đ112, TT 38/2024)

### HTTT-BC-R01 — Nghĩa vụ cung cấp dữ liệu đầy đủ, chính xác, kịp thời
- **Căn cứ**: Luật KCB Đ112 k3: cơ sở KCB "có trách nhiệm cung cấp đầy đủ, chính xác, kịp thời các thông tin" lên HTTT. TT 38 Đ4 k1: cơ sở có trách nhiệm "chuẩn hóa, thu thập và cung cấp đầy đủ dữ liệu về hoạt động khám bệnh, chữa bệnh tại đơn vị"; Đ15 (khoản cuối, văn bản đánh số nhầm "3") nhắc lại. Luật Đ120 k8: BYT hoàn thành và vận hành HTTT trước 01/01/2027.
- **Áp dụng**: mọi cơ sở KCB (không phân biệt công/tư, BV/PK) · **Hiệu lực/hạn**: 01/01/2027
- **Mức**: BẮT BUỘC (nghĩa vụ; cách gửi, định dạng, tần suất chưa quy định, xem R17)
- **Phần mềm phải**: lớp "xuất dữ liệu quản lý" độc lập với luồng XML BHYT, sinh được toàn bộ nhóm dữ liệu R02–R12 cho mọi người bệnh; nhật ký mỗi lần cung cấp (bộ dữ liệu, kỳ, thời điểm, kết quả).
- **Bẫy**: QĐ 2114: GĐ 1 (2026) chỉ nâng cấp Hệ thống quản lý hành nghề; GĐ 2 (2027–2028) mới kết nối HTTT của cơ sở. Từ 01/01/2027 nghĩa vụ đã có nhưng kênh tự động có thể chưa có (suy luận).

### HTTT-BC-R02 — Bộ dữ liệu ra viện của mọi ca
- **Căn cứ**: TT 38 Đ3 k4, Đ5 k7, Đ8 k1: (a) họ tên, ngày sinh, giới, **dân tộc, nghề nghiệp**, số định danh hoặc số thẻ BHYT; (b) nơi thường trú, **nơi ở hiện nay**, điện thoại; (c) ngày giờ vào, ra, tình trạng ra viện, kết quả điều trị, **cân nặng trẻ em**, **số ngày giường hồi sức cấp cứu/hồi sức tích cực**, nơi chuyển đi, chuyển đến; (d) PT/TT kèm **mã ICD-9 CM**, cả BHYT chi trả và tự chi trả; (đ) chẩn đoán ra viện (bệnh chính, biến chứng, bệnh kèm, nguyên nhân) theo ICD-10; (e) nguyên nhân tử vong chính.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trường bắt buộc có cấu trúc cho dân tộc, nghề nghiệp (theo danh mục), thường trú tách nơi ở hiện tại, cân nặng trẻ em, ngày giường HSCC/HSTC, cơ sở chuyển đi/đến (theo mã); PT/TT mã ICD-9-CM kể cả dịch vụ không BHYT; ICD-10 có phân vai; chặn đóng hồ sơ ra viện khi thiếu.
- **Bẫy**: XML BHYT không có dân tộc, nghề nghiệp, nơi ở hiện tại, ICD-9-CM và không có ca tự chi trả (suy luận theo phạm vi QĐ 130/4750). "Đã gửi XML là đủ" là sai.

### HTTT-BC-R03 — Thuốc, DVKT, chỉ số lâm sàng/CLS của mọi lượt
- **Căn cứ**: TT 38 Đ8 k2 (danh mục thuốc, số lượng, đơn vị, "bao gồm cả thuốc được bảo hiểm y tế chi trả và thuốc người bệnh tự chi trả"), Đ8 k3 (một số chỉ số lâm sàng, CLS có giá trị chẩn đoán, tiên lượng, theo dõi), Đ10 k6 b (số lượng từng DVKT, tách BHYT và tự chi trả).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2027
- **Mức**: BẮT BUỘC (thuốc, DVKT) · BẮT BUỘC? (danh sách "một số chỉ số" chưa ban hành)
- **Phần mềm phải**: thuốc, DVKT lượt tự chi trả mã hóa theo danh mục dùng chung như lượt BHYT; kết quả CLS lưu có cấu trúc (mã chỉ số, giá trị, đơn vị), không chỉ PDF.
- **Bẫy**: nhiều PK tư chỉ mã hóa phần BHYT, dịch vụ "theo yêu cầu" đặt tên tự do: không dùng được khi phải gửi (suy luận).

### HTTT-BC-R04 — Tóm tắt điều trị (TT 38 Đ8 k4)
- **Căn cứ**: TT 38 Đ8 k4: với nội trú, chuyển viện và đối tượng liên quan, tóm tắt gồm (a) tiền sử (dị ứng, bệnh mạn tính, phẫu thuật, sản khoa, **thiết bị cấy ghép**), bệnh sử, tình trạng lúc vào; (b) diễn biến; (c) tình trạng ra viện, kết quả; (d) tóm tắt CLS; (đ) phương pháp điều trị; (e) kế hoạch tiếp theo, **đơn thuốc ngoại trú**, lời dặn, lịch tái khám; (g) liên hệ bác sĩ/cơ sở. NĐ 102 Đ10 k5 b (kết nối Sổ SKĐT).
- **Áp dụng**: cơ sở có nội trú hoặc chuyển viện · **Hiệu lực/hạn**: NĐ 102 từ 01/07/2025; TT 38 từ 01/01/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tóm tắt có cấu trúc đủ 7 nhóm, dị ứng và thiết bị cấy ghép mã hóa; một mô hình tóm tắt dùng chung cho Sổ SKĐT (SKDT-R03), HTTT quản lý KCB, phiếu chuyển (BHYT-GD-R11), tóm tắt HSBA Mẫu 03 (GIAYTO-R15).
- **Bẫy**: trùng dữ liệu HSBA điện tử (EMR-R18, PL CV 365): định nghĩa một mô hình, ánh xạ ra nhiều đích.

### HTTT-BC-R05 — Tử vong và người bệnh nặng xin về
- **Căn cứ**: TT 38 Đ3 k5 (nguyên nhân tử vong tại cơ sở, trên đường đến cơ sở, nặng xin về), Đ5 k8 (thông tin giấy báo tử, chuỗi bệnh lý dẫn đến tử vong kèm ICD-10 và khoảng thời gian theo Phiếu chẩn đoán nguyên nhân tử vong), Đ5 k9 (phiếu thông tin người bệnh nặng xin về), Đ8 k1 e. TT 23/2025 PL IV Biểu 14/BCT có cột nặng xin về, tử vong trước viện, tại viện, số ca được cấp giấy báo tử.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: Biểu 14 đang áp dụng; TT 38 từ 01/01/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trạng thái ra viện phân biệt "tử vong tại viện", "tử vong trước khi đến/trên đường", "nặng xin về"; phiếu nguyên nhân tử vong có chuỗi Ia→Id, II, mỗi dòng ICD-10 và khoảng thời gian; liên kết giấy báo tử đã cấp.
- **Bẫy**: giấy báo tử theo **Mẫu 05 TT 25/2025** (mẫu PL I TT 24/2020 đã hết hiệu lực 01/07/2025); phiếu CĐNNTV vẫn theo TT 24/2020 + QĐ 1996/2025. Chi tiết: GIAYTO-R10, R11.

### HTTT-BC-R06 — Người hành nghề, người thực hành, đăng ký hành nghề
- **Căn cứ**: Luật KCB Đ37 (nội dung đăng ký hành nghề), Đ38 k1 (gửi danh sách khi xin GPHĐ và khi thay đổi), Đ38 k2 b (cơ quan cấp phép công bố trên HTTT trong 05 ngày làm việc), Đ36 k1 (hành nghề nhiều nơi không trùng thời gian), Đ23 k2 d (cơ sở hướng dẫn thực hành đăng ký người thực hành trên HTTT). NĐ 96/2023 Đ27 k12, Đ29 k1 c (thứ cấp-chính thức): người hành nghề nghỉ việc → báo cáo trong **03 ngày làm việc** và tạm dừng dịch vụ thuộc phạm vi người đó nếu chưa có người thay; bổ sung người hành nghề → gửi danh sách trong **10 ngày**, chỉ được hành nghề sau khi hoàn thành đăng ký; Đ7 k1 b, k6 b (đăng tải danh sách người thực hành). TT 38 Đ9 k1–4 (số định danh, số GPHN/CCHN, nơi/ngày cấp, văn bằng, phạm vi, kỹ thuật ngoài phạm vi, thời hạn GPHN; vị trí, thời gian hành nghề ở cơ sở chính và ngoài giờ; điểm CME; người thực hành). CV 4016 (thứ cấp).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng; Hệ thống quản lý quốc gia (`app.qlhanhnghekcb.gov.vn` theo HDSD) đang vận hành
- **Mức**: BẮT BUỘC (đăng ký, thời hạn báo thay đổi) · NÊN (đồng bộ tự động: hệ thống quốc gia hiện chỉ có web và import file)
- **Phần mềm phải**: sổ nhân sự hành nghề đủ trường TT 38 Đ9; lưu lịch hành nghề đã đăng ký (khung giờ, địa điểm), chặn gán người chỉ định, kê đơn, thực hiện DVKT ngoài khung giờ/phạm vi; chặn tài khoản lâm sàng của người chưa hoàn tất đăng ký; nhân sự nghỉ việc → việc "báo cơ quan cấp phép trong 03 ngày làm việc" và cảnh báo dịch vụ mất người phụ trách; xuất file theo mẫu import; quản lý người thực hành (người hướng dẫn tối đa 05 người cùng lúc, NĐ 96 Đ7 k2 b).
- **Bẫy**: số GPHN/CCHN, mã người hành nghề trong XML (`MA_BAC_SI`, BHYT-GD-R17), mã liên thông đơn thuốc (DUOC-R02) và số định danh là các định danh khác nhau của cùng người: lưu và đối soát. NĐ 90 Đ39 k2 a phạt không gửi danh sách thay đổi; Đ38 k4 a phạt hành nghề ngoài thời gian, địa điểm đã đăng ký.

### HTTT-BC-R07 — Dữ liệu cơ sở: giấy phép, giường, thiết bị, kho
- **Căn cứ**: TT 38 Đ10 k1 (tên, mã cơ sở, GPHĐ, phạm vi, người chịu trách nhiệm chuyên môn, hình thức tổ chức, cấp chuyên môn, hạng, chuyên khoa, cơ quan chủ quản, cơ sở thực hành/BHYT, công/tư, giờ làm việc, năm thành lập); Đ10 k2 (giường kế hoạch, đăng ký, thực tế; HSTC, **áp lực âm**, bàn mổ, bàn đẻ; TBYT và hiện trạng; **nhập, xuất, tồn thuốc, hóa chất, sinh phẩm định kỳ 06 và 12 tháng**); Đ10 k3 (khoa, phòng; người hành nghề); Đ3 k8 (HTTT cấp mã cơ sở thống nhất toàn quốc); Đ3 k11 (kiểm kê, khấu hao TBYT).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục giường theo loại có ngày hiệu lực; module TBYT có hiện trạng; báo cáo nhập-xuất-tồn thuốc, hóa chất, sinh phẩm kỳ 6 và 12 tháng; mã cơ sở là cấu hình theo ngày hiệu lực (BHYT-DATA-R24, SKDT-R18).
- **Bẫy**: PK nhỏ thường thiếu module TBYT và hóa chất.

### HTTT-BC-R08 — Dữ liệu chất lượng, hài lòng, sự cố
- **Căn cứ**: TT 38 Đ10 k4 (kết quả đánh giá chất lượng; chất lượng xét nghiệm; hài lòng người bệnh, người nhà, nhân viên; quản lý và phòng ngừa sự cố y khoa), Đ3 k13, k14, k16, Đ5 k2, k3.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2027
- **Mức**: BẮT BUỘC? (có nội dung, chưa có biểu mẫu, chỉ số)
- **Phần mềm phải**: dữ liệu khảo sát hài lòng, phản hồi người bệnh có cấu trúc; module sự cố xuất số liệu tổng hợp (R32–R35).

### HTTT-BC-R09 — Hoạt động chuyên môn và tài chính 6/12 tháng
- **Căn cứ**: TT 38 Đ10 k5 (định kỳ 6 và 12 tháng): (a) chuyên môn: tổng ngày điều trị, ngày điều trị trung bình, nhân lực, dược, mô hình bệnh tật, tử vong, điều dưỡng, PHCN, KSNK, chỉ đạo tuyến; (b) tài chính: thu, chi, trích lập quỹ, cảnh báo rủi ro tài chính, quyết toán BHYT. Đ3 k12.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2027
- **Mức**: BẮT BUỘC (kỳ 6/12 tháng là quy định tần suất rõ duy nhất trong TT 38)
- **Phần mềm phải**: báo cáo kỳ 6 tháng (01/01–30/06) và 12 tháng từ dữ liệu giao dịch; ngày điều trị trung bình tính cùng quy tắc với Biểu 9/BCT.
- **Bẫy**: với cơ sở tư, thu chi, trích lập quỹ là dữ liệu kế toán doanh nghiệp, thường ngoài HIS; khả thi với PK tư chưa rõ (suy luận).

### HTTT-BC-R10 — Danh mục kỹ thuật, phác đồ
- **Căn cứ**: TT 38 Đ10 k6 (a) danh mục DVKT được phê duyệt; (b) số lượng từng DVKT; (c) hướng dẫn chẩn đoán, phác đồ, quy trình kỹ thuật, chăm sóc áp dụng; Đ3 k15, k17.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: danh mục DVKT gắn số quyết định phê duyệt và ngày hiệu lực; chặn chỉ định DVKT chưa được phê duyệt; thống kê theo mã DVKT tách BHYT/tự chi trả.

### HTTT-BC-R11 — Niêm yết giá, công khai thông tin
- **Căn cứ**: Luật KCB Đ60 k3 (công khai giờ làm việc, danh sách người hành nghề và giờ làm của từng người), Đ60 k4 (niêm yết giá dịch vụ KCB, chăm sóc, hỗ trợ theo yêu cầu "tại cơ sở và trên Hệ thống thông tin"). TT 38 Đ3 k3, Đ5 k11, Đ10 k7.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: tại cơ sở đang áp dụng; trên HTTT phụ thuộc chức năng HTTT
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bảng giá có phiên bản theo ngày hiệu lực, tách giá BHYT, tự chi trả, theo yêu cầu, dịch vụ hỗ trợ; xuất bảng giá hiện hành dạng máy đọc được; chặn thu dịch vụ không có trong bảng giá đang niêm yết.
- **Bẫy**: NĐ 90 Đ38 k3 b phạt thu chi phí chưa niêm yết.

### HTTT-BC-R12 — Hạch toán chi phí theo ca bệnh
- **Căn cứ**: TT 38 Đ10 k8: (a) chi nhân công theo mã nhân viên, khoa, tổng thu nhập năm; (b) khấu hao tài sản, TBYT; (c) khấu hao nhà; (d) chi thường xuyên; (đ) chi trực tiếp theo đợt điều trị. Đ3 k10.
- **Áp dụng**: mọi cơ sở KCB (theo câu chữ) · **Hiệu lực/hạn**: 01/01/2027
- **Mức**: BẮT BUỘC? (chưa có phương pháp phân bổ và biểu mẫu)
- **Phần mềm phải**: (chuẩn bị) mô hình gắn chi phí gián tiếp vào khoa và phân bổ về ca; nhân viên, thiết bị, tòa nhà có mã ổn định.

### HTTT-BC-R13 — Sửa sai và thông báo thay đổi "ngay"
- **Căn cứ**: TT 38 Đ4 k2: cơ sở "phải thông báo ngay" cho cơ quan quản lý HTTT khi có thay đổi, bổ sung hoặc phát hiện sai sót trong dữ liệu. NĐ 102 Đ24 k1; NĐ 194 Đ38 k4 (thông báo kịp thời khi dữ liệu đã cung cấp thay đổi hoặc sai). TT 15/2026 Đ4 k1 b (dữ liệu báo cáo thiếu, sai thì kiểm tra, điều chỉnh).
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: NĐ 102, TT 15 đang áp dụng; TT 38 từ 01/01/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bản ghi đã gửi ra ngoài là bất biến; sửa tạo phiên bản mới có lý do và tự đưa vào hàng đợi "gửi bản điều chỉnh" tới mọi đích đã nhận bản cũ; báo cáo "bản ghi bị sửa sau khi gửi".

### HTTT-BC-R14 — Cung cấp dữ liệu khi khẩn cấp, dịch nhóm A
- **Căn cứ**: TT 38 Đ4 k3 (dịch bệnh, thiên tai, khẩn cấp: cung cấp theo yêu cầu; cơ quan yêu cầu nêu loại dữ liệu, mục đích, thời hạn), Đ5 k4 (báo cáo thu dung, điều trị dịch nhóm A "ngay khi có yêu cầu"), Đ3 k18.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2027; báo cáo BTN đang áp dụng (R26–R27)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: truy vấn ad hoc theo nhóm bệnh (ICD-10 hoặc nhóm BTN) xuất danh sách ca, diễn biến, giường đang dùng trong vài giờ; lưu văn bản yêu cầu (loại dữ liệu, mục đích, thời hạn) làm căn cứ chia sẻ (DLCN).

### HTTT-BC-R15 — Tai nạn thương tích, trực lễ tết
- **Căn cứ**: TT 38 Đ5 k5 (báo cáo tai nạn giao thông, thương tích theo mẫu: số ca cấp cứu, tình trạng, nguyên nhân sơ bộ theo ICD-10), Đ5 k6 (báo cáo thường trực lễ, tết; tổng kết sau kỳ nghỉ). TT 15/2026 Đ53 k3: cơ sở KCB báo cáo giám sát thương tích định kỳ 06 tháng và năm cho CDC tỉnh trong **05 ngày làm việc** sau kỳ.
- **Áp dụng**: cơ sở có cấp cứu · **Hiệu lực/hạn**: TT 15 đang áp dụng; TT 38 từ 01/01/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tiếp đón cấp cứu có nguyên nhân bên ngoài (ICD-10 chương XX: V01–Y98), loại tai nạn, nơi xảy ra; báo cáo theo kỳ lễ tết với khoảng ngày cấu hình.

### HTTT-BC-R16 — Dùng mã định danh từ CSDL quốc gia
- **Căn cứ**: TT 38 Đ2 k5 ("Sử dụng mã định danh đối tượng được quản lý đã được cấp bởi các cơ sở dữ liệu quốc gia"). NĐ 102 Đ6 (số định danh cá nhân là mã định danh y tế). NĐ 278 Đ5 k1, k2 (dữ liệu chủ quốc gia là nguồn tin cậy duy nhất; áp trực tiếp cho cơ quan thuộc hệ thống chính trị; diễn giải).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: NĐ 102 đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: khóa người bệnh là số định danh cá nhân (MPI theo SKDT-R05, SKDT-P01); mã cơ sở, mã người hành nghề, mã thuốc, mã TBYT lấy từ nguồn quốc gia, không tự sinh; mã nội bộ chỉ làm khóa kỹ thuật (EMR-R05).

### HTTT-BC-R17 — Chuẩn đầu ra, hướng dẫn kỹ thuật kết nối
- **Căn cứ**: Luật KCB Đ112 k5 a (Bộ trưởng BYT quy định chuẩn định dạng đầu ra). TT 38 Đ6: chuẩn đầu ra thiết kế dựa trên Chương II, "trên nguyên tắc kế thừa các chuẩn đầu ra do Bộ Y tế đã ban hành phục vụ công tác quản lý nhà nước về khám bệnh, chữa bệnh và thanh toán chi phí khám chữa bệnh bảo hiểm y tế". TT 38 Đ3 k1 (nhận qua biểu mẫu, dữ liệu có cấu trúc hoặc API). QĐ 2114 mục IV.2 b (TTYQG ban hành hướng dẫn kỹ thuật kết nối).
- **Áp dụng**: mọi cơ sở KCB, vendor · **Hiệu lực/hạn**: hướng dẫn kỹ thuật chưa ban hành tại 2026-10-06
- **Mức**: BẮT BUỘC? (có nghĩa vụ, chưa có chuẩn)
- **Phần mềm phải**: lớp xuất kiểu adapter có phiên bản; tái dùng bảng chuẩn đã có (XML BHYT, BHYT-DATA-R01; PL CV 365, EMR-R18; dữ liệu KSK QĐ 1551, SKDT-R15); hỗ trợ nhập tay qua cổng, upload file có cấu trúc, gọi API.
- **Bẫy**: (suy luận) câu "kế thừa… thanh toán BHYT" gợi ý XML BHYT là xương sống; phải chuẩn bị phần ngoài XML (R02, R07–R12).

### HTTT-BC-R18 — Bảo mật, toàn vẹn khi kết nối
- **Căn cứ**: TT 38 Đ12 k2 (bảo mật, toàn vẹn, sẵn sàng khi truyền tải và sử dụng), k3, k4. NĐ 102 Đ23 k3 (cơ sở y tế bảo đảm an toàn thông tin, an ninh mạng cho CSDL và kết nối). TT 38 Đ7 (HTTT của BYT lập hồ sơ cấp độ).
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: NĐ 102 đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: TLS cho mọi kết nối ra ngoài; ký số hoặc ít nhất băm toàn vẹn gói gửi; khóa API, tài khoản cổng trong kho bí mật; log gửi không chứa dữ liệu sức khỏe dạng rõ (ANM-R11, R12; DLCN-R10).

### HTTT-BC-R19 — Hạ tầng CNTT kết nối HTTT là điều kiện GPHĐ
- **Căn cứ**: Luật KCB Đ52 k2 d: điều kiện cấp mới GPHĐ gồm cơ sở vật chất, "trong đó hạ tầng công nghệ thông tin phải bảo đảm kết nối với Hệ thống thông tin về quản lý hoạt động khám bệnh, chữa bệnh theo quy định tại khoản 1 Điều 112". **Đ120 k5** a: áp dụng từ 01/01/2027 cho hồ sơ nộp từ ngày đó; k5 b: chậm nhất 01/01/2029 với cơ sở có GPHĐ trước 01/01/2027. Đ121 k13: hồ sơ nộp 2024–2026 không phải đáp ứng điều kiện này. NĐ 90 Đ39 k2 b → k6 d (không bảo đảm điều kiện sau cấp phép).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2027 (mới), 01/01/2029 (cũ)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: có tính năng kết nối HTTT (R01, R17) và bằng chứng kết nối xuất được để nộp kèm hồ sơ GPHĐ (cấu hình, nhật ký gửi thành công, xác nhận của hệ thống nhận).
- **Bẫy**: điều kiện CNTT là **Đ120 k5**; **k6** là tiêu chuẩn chất lượng cơ bản (R36) (C05). Áp chế tài Đ39 cho cơ sở cũ trước 2029 là suy luận. Chưa có văn bản định nghĩa "hạ tầng CNTT bảo đảm kết nối".

### B. CSDL quốc gia về y tế (NĐ 102/2025, QĐ 11/2026)

### HTTT-BC-R20 — Kết nối CSDL quốc gia về y tế và các CSDL khác
- **Căn cứ**: NĐ 102 Đ23 (đối chiếu bản Công báo): k1 tạo lập, thu thập, chuẩn hóa dữ liệu, xây dựng CSDL của đơn vị; k2 "Kết nối, chia sẻ, đồng bộ dữ liệu của đơn vị với Cơ sở dữ liệu quốc gia về y tế, cơ sở dữ liệu của Bộ Y tế, cơ sở dữ liệu về y tế của địa phương và Sổ sức khỏe điện tử tích hợp trên ứng dụng định danh quốc gia"; k3 bảo đảm an toàn. Đ16 k1 d (CSDLQG lấy dữ liệu từ CSDL của cơ sở y tế), Đ14 k4 (phạm vi: chứng sinh, BHYT, phòng bệnh, KCB, chăm sóc sức khỏe, báo tử). QĐ 11/2026 mục XVIII; chia sẻ theo NĐ 278/2025.
- **Áp dụng**: mọi cơ sở y tế · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC (nghĩa vụ) · BẮT BUỘC? (đặc tả kỹ thuật CSDLQG chưa công bố; CT 07 yêu cầu hoàn thiện cấu trúc dữ liệu trong 9/2026, thứ cấp)
- **Phần mềm phải**: dùng chung lớp xuất của R17; nhật ký đồng bộ theo từng đích; đồng bộ lại toàn bộ hoặc theo khoảng thời gian.
- **Bẫy**: CSDLQG về y tế (NĐ 102), HTTT quản lý KCB (TT 38), Hệ thống quản lý hành nghề (KH 1642), Cổng giám định BHYT, Hệ thống đơn thuốc quốc gia, HTTT giám sát phòng bệnh, Sổ SKĐT là **các đích khác nhau**, do đơn vị khác nhau vận hành; chưa có cơ chế "gửi một lần".

### HTTT-BC-R21 — Tôn trọng dữ liệu chủ quốc gia
- **Căn cứ**: NĐ 102 Đ15 (dữ liệu chủ: phạm vi hoạt động cơ sở, chứng chỉ hành nghề, định danh và lưu hành thuốc, TBYT, chứng sinh, KCB, báo tử), Đ10 k3 (dữ liệu chủ có giá trị sử dụng chính thức, tương đương văn bản giấy; diễn giải). NĐ 278 Đ5.
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: NÊN (với phần mềm cơ sở; với hệ thống của cơ quan nhà nước là bắt buộc theo NĐ 278 Đ5 k1)
- **Phần mềm phải**: lấy GPHN, phạm vi hành nghề, số đăng ký thuốc, TBYT từ nguồn quốc gia khi tra được; đánh dấu nguồn và thời điểm đồng bộ; cảnh báo khi dữ liệu nội bộ lệch dữ liệu chủ.

### C. Báo cáo thống kê (TT 23/2025, sắp được thay)

### HTTT-BC-R22 — Sổ ghi chép ban đầu theo mẫu
- **Căn cứ**: TT 23 Đ3 k1 + PL III: A1/CSYT Sổ khám bệnh (TYT, phòng khám; họ tên, giới, ngày sinh, giấy tờ tùy thân, số thẻ BHYT, địa chỉ, dân tộc, nghề nghiệp, triệu chứng, chẩn đoán, phương pháp điều trị, người khám, ghi chú); A2.1/A2.2 tiêm chủng; A3 khám thai; A4 sổ đẻ; A5.1 tránh thai; A5.2 phá thai; A6–A12 cho TYT.
- **Áp dụng**: TYT, PK, khoa sản BV và cơ sở có dịch vụ tương ứng · **Hiệu lực/hạn**: đến 28/02/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: in/xuất sổ theo mẫu từ dữ liệu khám (không nhập hai lần); PK sản phụ khoa có A3, A4, A5.x.

### HTTT-BC-R23 — Báo cáo thống kê tháng, năm; hạn 05 ngày làm việc
- **Căn cứ**: TT 23 Đ4 (kỳ tháng 0h00 ngày 01 đến 24h00 ngày cuối tháng; kỳ năm 01/01–31/12; đột xuất phải có văn bản), Đ5 k1 (đơn vị gửi gồm đơn vị cấp tỉnh, TW và "các cơ sở y tế tư nhân đặt trụ sở trên địa bàn tỉnh"; đơn vị nhận do UBND tỉnh phân công; hạn **05 ngày làm việc** sau kỳ), Đ6 k1 (đầy đủ, chính xác, đúng hạn; cung cấp lại khi được yêu cầu). PL IV: 14 biểu /BCT; với cơ sở KCB quan trọng nhất là Biểu 9 (cơ sở, giường, hoạt động KCB), Biểu 11 (mắc, tử vong BTN gây dịch), Biểu 14 (R24) kỳ tháng (suy luận theo nội dung biểu).
- **Áp dụng**: BV công, BV tư, PK · **Hiệu lực/hạn**: đến 28/02/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh báo cáo theo kỳ dương lịch (múi giờ VN, ranh 24h00 ngày cuối) từ dữ liệu giao dịch, có lịch hạn nộp; lưu snapshot đã nộp (số liệu, truy vấn, phiên bản định nghĩa) để cung cấp lại.
- **Bẫy**: thân TT ghi "05 ngày làm việc", PL IV ghi "05 ngày" (Biểu 2 năm: "15 ngày"): lấy mốc sớm hơn (suy luận). TT 23 Đ5 nhảy từ k2 sang k4.

### HTTT-BC-R24 — Biểu 14/BCT bệnh tật, tử vong theo ICD-10
- **Căn cứ**: TT 23 PL IV Biểu 14/BCT: theo bệnh/nhóm bệnh và mã ICD-10; khoa khám bệnh (tổng, nữ, trẻ < 15 tuổi, tử vong trước viện); nội trú (mắc, tử vong, nữ, trẻ < 15 và < 5 tuổi, nặng xin về, số ca tử vong được cấp giấy báo tử).
- **Áp dụng**: BV và cơ sở có nội trú · **Hiệu lực/hạn**: đến 28/02/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bảng ánh xạ ICD-10 → dòng Biểu 14 có phiên bản; tuổi tính tại ngày vào viện; tách ngoại trú/nội trú.

### HTTT-BC-R25 — Chuyển chế độ báo cáo mới trước 01/03/2027
- **Căn cứ**: TT 23 Đ7 k2 (hết hiệu lực 01/03/2027). Dự thảo TT thay thế dự kiến xong 10/2026 (thứ cấp).
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: 01/03/2027
- **Mức**: BẮT BUỘC? (chưa có văn bản thay; rủi ro khoảng trống)
- **Phần mềm phải**: biểu, chỉ tiêu, kỳ, hạn nộp là cấu hình có ngày hiệu lực; chạy song song biểu cũ (kỳ tháng 02/2027 nộp đầu tháng 03/2027) và biểu mới.
- **Bẫy**: báo cáo kỳ tháng 02/2027 có hạn rơi sau ngày TT 23 hết hiệu lực; cách xử lý chưa rõ (mục 7).

### D. Giám sát bệnh truyền nhiễm và phòng bệnh (Luật Phòng bệnh 2025, TT 15/2026)

### HTTT-BC-R26 — Báo cáo trực tuyến qua HTTT giám sát; dự phòng khi lỗi
- **Căn cứ**: Luật Phòng bệnh Đ13 k7, Đ17 k3 g (cơ sở y tế "Thông tin, báo cáo đầy đủ, chính xác, kịp thời về bệnh truyền nhiễm và dịch bệnh"). TT 15 Đ3 k2 (cập nhật, cung cấp dữ liệu lên HTTT giám sát), Đ4 k2 a (báo cáo trực tuyến), Đ4 k2 b (HTTT sự cố hoặc chưa đủ chức năng: báo cáo bằng văn bản điện tử hoặc giấy, sau đó "phải thực hiện cập nhật, bổ sung dữ liệu" khi đã khắc phục), Đ4 k3, Đ10 k2 a (danh mục, mẫu theo hướng dẫn chuyên môn của Cục Phòng bệnh), Đ66 k2 (hướng dẫn chuyên môn cũ dùng tiếp đến khi có hướng dẫn mới), Đ61 k2 (Cục QLKCB chỉ đạo cơ sở KCB liên thông phần mềm với hệ thống giám sát).
- **Áp dụng**: cơ sở KCB, cơ sở xét nghiệm · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (báo cáo trực tuyến) · BẮT BUỘC? (liên thông tự động HIS ↔ hệ thống giám sát: nhiệm vụ của Cục, chưa có chuẩn)
- **Phần mềm phải**: chẩn đoán hoặc kết quả xét nghiệm thuộc danh mục BTN tạo phiếu báo cáo ca bệnh chờ gửi (hành chính, dịch tễ, lâm sàng, mẫu bệnh phẩm theo TT 15 Đ7 k1 a–đ); theo dõi trạng thái đã nhập lên HTTT giám sát; gửi kênh dự phòng thì đánh dấu "chưa đồng bộ" và nhắc nhập bù.
- **Bẫy**: hệ thống đang chạy là HTQLGS/eCDS (xây theo TT 54/2015); TT 15 không gọi tên, việc eCDS có phải "HTTT giám sát trong phòng bệnh" hay không chưa xác minh.

### HTTT-BC-R27 — Ca nghi BTN 24 giờ, tử vong do BTN 24 giờ
- **Căn cứ**: TT 15 Đ10 k1: phát hiện người nghi ngờ mắc BTN "có trách nhiệm thông báo trong vòng 24 giờ cho Trạm Y tế cấp xã trên địa bàn". Đ10 k2 b: cơ sở KCB báo cáo ca tử vong do hoặc nghi do BTN "trong vòng 24 giờ kể từ khi có trường hợp tử vong". Đ26 k1 d (báo cáo ổ dịch hằng ngày, việc của TYT xã). NĐ 90 Đ7 k2 b.
- **Áp dụng**: cơ sở KCB, cơ sở xét nghiệm · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: đồng hồ 24 giờ từ lúc ghi chẩn đoán nghi ngờ hoặc lúc tử vong; leo thang (bác sĩ → khoa → phòng KHTH) trước hạn; lưu bằng chứng thời điểm gửi.
- **Bẫy**: đích nhận ở Đ10 k1 là **TYT xã**, không phải CDC tỉnh. Thời hạn từng ca theo nhóm bệnh (TT 54/2015 cũ: 24 hoặc 48 giờ) không còn trong thông tư, chuyển sang hướng dẫn chuyên môn Cục Phòng bệnh (chưa tìm thấy).

### HTTT-BC-R28 — Giám sát dựa vào sự kiện, chùm ca
- **Căn cứ**: TT 15 Đ9 k1 a: nguồn thông tin gồm thông báo của cơ sở KCB về chùm ca BTN chưa rõ nguyên nhân, gia tăng bất thường số người bệnh, nhân viên y tế mắc hoặc nghi mắc, sự kiện y tế bất thường; Đ9 k1 b (cung cấp cho TYT xã hoặc CDC tỉnh).
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC? (Đ9 mô tả nguồn, không đặt thời hạn)
- **Phần mềm phải**: (nên) báo cáo số ca theo hội chứng/nhóm ICD-10 theo ngày so ngưỡng nền; cảnh báo chùm ca cùng địa chỉ, đơn vị; cờ "nhân viên y tế" trên hồ sơ.

### HTTT-BC-R29 — BKLN, rối loạn tâm thần: 05 ngày làm việc; số hóa đến 2030
- **Căn cứ**: TT 15 Đ32–33 k1 (cơ sở KCB báo cáo giám sát BKLN về CDC tỉnh trong **05 ngày làm việc** sau kỳ tháng/năm), Đ39–40 k1 (RLTT, như trên), Đ46 k2 a (dinh dưỡng: TYT xã thu từ cơ sở KCB), Đ66 k1 (chậm nhất **01/01/2030** báo cáo BKLN, RLTT, dinh dưỡng, thương tích thực hiện trên HTTT giám sát).
- **Áp dụng**: cơ sở KCB trên địa bàn tỉnh · **Hiệu lực/hạn**: 01/07/2026; 01/01/2030
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: báo cáo kỳ tháng, năm về số người mắc BKLN, RLTT được phát hiện, quản lý (theo mẫu Cục Phòng bệnh khi có); lịch hạn 05 ngày làm việc.

### HTTT-BC-R30 — Danh mục BTN nhóm A, B, C mới
- **Căn cứ**: QĐ 1965/QĐ-BYT năm 2026 (thứ cấp): nhóm A 15, B 47, C 19, áp dụng từ 01/07/2026, bãi bỏ danh mục cũ. NĐ 90 Đ7 k3 (mức phạt riêng nhóm A).
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (nội dung danh mục chưa đọc bản gốc)
- **Phần mềm phải**: danh mục BTN có phiên bản (mã bệnh, nhóm, ICD-10, quy tắc báo cáo), thay danh mục theo Luật PCBTN 2007.

### HTTT-BC-R31 — Bảo mật thông tin người mắc BTN
- **Căn cứ**: Luật Phòng bệnh Đ17 k1 c (quyền riêng tư về tình trạng sức khỏe liên quan BTN, trừ khi luật khác quy định). TT 15 Đ3 k3.
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chỉ vai trò "báo cáo dịch tễ" xem hàng đợi báo cáo BTN; báo cáo tổng hợp không chứa định danh; HIV và bệnh đặc thù theo DLCN-R32.

### E. Sự cố y khoa (Luật KCB Đ71, TT 43/2018, TT 35/2024)

### HTTT-BC-R32 — Kênh báo cáo sự cố; nội dung tối thiểu; lưu mọi báo cáo
- **Căn cứ**: Luật KCB Đ71 k1, k2 (phòng ngừa dựa trên nhận diện, báo cáo, phân tích, khuyến cáo công khai trên HTTT; trách nhiệm người đứng đầu và người làm việc). TT 43 (gốc-OCR, diễn giải): Đ5 k1 a báo cáo tự nguyện với mục 1–6 PL I (NC0–NC2); k1 b báo cáo **bắt buộc** với mục 7–9 (NC3) và sự cố nghiêm trọng (làm chết 01 người bệnh và nghi còn nguy cơ, hoặc ≥ 02 người cùng tình huống/nguyên nhân); k2 a tự nguyện bằng văn bản hoặc báo cáo điện tử, khẩn thì báo trực tiếp/điện thoại rồi ghi nhận lại; k3 a nội dung tối thiểu theo Mẫu PL III (địa điểm, thời điểm, mô tả, đánh giá sơ bộ, tình trạng người bị ảnh hưởng, xử lý ban đầu); k3 b mọi sự cố được báo cáo phải được ghi nhận, lưu giữ vào hồ sơ hoặc hệ thống báo cáo trực tuyến. TT 35/2024 PL Mục V 4.6 (với BV, báo cáo sự cố là tiêu chuẩn chất lượng cơ bản).
- **Áp dụng**: mọi cơ sở KCB (TT 43 Đ1 k3) · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: form điện tử đủ trường PL III (mã sự cố, ngày báo cáo, tự nguyện/bắt buộc, đơn vị báo cáo, đối tượng bị ảnh hưởng, khoa/vị trí, ngày giờ xảy ra, mô tả, đề xuất, xử lý ban đầu, đã thông báo bác sĩ/người nhà/người bệnh, đã ghi vào HSBA); nút "báo sự cố" từ mọi màn hình; kênh riêng cho người không đăng nhập HIS; không cho xóa báo cáo.
- **Bẫy**: TT 43 Đ1 k2 loại trừ sự cố tiêm chủng, ADR, AE thử nghiệm lâm sàng; ADR đi kênh DI&ADR (DUOC). Tách loại để không báo nhầm kênh.

### HTTT-BC-R33 — Thời hạn báo cáo sự cố bắt buộc
- **Căn cứ**: TT 43 (gốc-OCR, diễn giải): Đ5 k2 b (NC3: văn bản hỏa tốc hoặc báo cáo điện tử; sự cố nghiêm trọng: báo trước bằng điện thoại **trong 01 giờ** từ khi phát hiện), Đ5 k3 a (người gây ra/phát hiện → trưởng khoa và bộ phận quản lý sự cố → lãnh đạo → báo ngay cơ quan quản lý), Đ5 k3 b (sự cố nghiêm trọng chia sẻ đến cơ quan quản lý trực tiếp và BYT), Đ8 k1 a (NC2, NC3: báo ngay người đứng đầu), Đ9 k1 b, c (SYT, BYT báo nhanh trong 24 giờ).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phân loại NC3 hoặc "nghiêm trọng" tự gửi cảnh báo (SMS, app) tới lãnh đạo và bộ phận quản lý chất lượng; đồng hồ 01 giờ cho cuộc gọi báo trước, trường "đã gọi lúc, người nhận"; sinh văn bản theo PL III có họ tên người báo cáo (bắt buộc với loại này).

### HTTT-BC-R34 — Phân loại, RCA, tổng hợp định kỳ
- **Căn cứ**: TT 43 (gốc-OCR, diễn giải): Đ7 k1 (3 trục: mức tổn thương PL I [A–I, NC0–NC3], nhóm sự cố Mục II PL IV, nhóm nguyên nhân Mục IV PL IV), Đ7 k2 (NC3 phân loại tiếp theo 28 loại sự cố nghiêm trọng PL II), Đ8 k1 a (bộ phận quản lý sự cố báo cáo người đứng đầu **1 tuần 1 lần**), Đ8 k1 c (nhóm chuyên gia đề xuất giải pháp **trong 60 ngày** từ khi nhận báo cáo phân tích), Đ6 k1 (tổng hợp gửi cơ quan quản lý **6 tháng một lần**: số báo cáo bắt buộc/tự nguyện, tần suất từng loại, kết quả RCA, giải pháp), Đ9 k2 a (phản hồi người báo cáo tại giao ban), Đ11 (kế hoạch khắc phục).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: vòng đời tiếp nhận → phân loại 3 trục → RCA → khuyến cáo → kế hoạch khắc phục → đóng; đồng hồ 60 ngày; báo cáo tuần; báo cáo 6 tháng đủ 4 nội dung Đ6 k1 b; liên kết sự cố với HSBA (hồ sơ liên quan lưu vĩnh viễn, EMR-R22).

### HTTT-BC-R35 — Bảo mật, ẩn danh người báo cáo sự cố
- **Căn cứ**: TT 43 Đ3 k1, k3, Đ12 k3 (gốc-OCR, diễn giải): hồ sơ phòng ngừa sự cố quản lý theo quy chế bảo mật; giữ bí mật, ẩn danh tính cá nhân/cơ sở báo cáo; bộ phận đầu mối được tra cứu và công bố; không dùng cho mục đích khác. NĐ 90/2026 Đ38 (gốc-OCR, chưa xác định số khoản, diễn giải): phạt đăng tải thông tin mang tính quy kết trách nhiệm người hành nghề, cơ sở khi xảy ra sự cố y khoa mà chưa có kết luận của cơ quan có thẩm quyền.
- **Áp dụng**: mọi cơ sở · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: báo cáo tự nguyện ẩn danh được (không lưu user ID vào bản ghi hiển thị; khóa danh tính tách riêng, chỉ bộ phận đầu mối mở được); module sự cố chỉ bộ phận quản lý chất lượng xem; nhật ký truy cập riêng; báo cáo gửi ra ngoài không có tên người báo cáo, trừ báo cáo bắt buộc.

### F. Chất lượng và mức ứng dụng CNTT

### HTTT-BC-R36 — Tự đánh giá chất lượng hằng năm và công khai
- **Căn cứ**: Luật KCB Đ58 k3 (hằng năm tự đánh giá theo tiêu chuẩn cơ bản Đ57 k1 a), Đ58 k5 (công khai tại cơ sở và trên HTTT), **Đ120 k6** (tiêu chuẩn cơ bản áp từ 01/01/2025 với BV; 01/01/2027 với hình thức tổ chức khác). TT 35/2024 Đ1 k3 (BV đánh giá 1 lần/năm trong **quý I** năm sau; đạt khi mọi tiêu chuẩn "Có"), Đ2 k4 c. Dự thảo TT cho cơ sở ngoài BV (thứ cấp): cùng cơ chế, thêm tiêu chí CNTT và CĐS.
- **Áp dụng**: BV (đang áp dụng); PK, TYT, phòng chẩn trị… từ 01/01/2027 khi có TT · **Hiệu lực/hạn**: như trên
- **Mức**: BẮT BUỘC (BV) · BẮT BUỘC? (cơ sở khác: luật đã có mốc, chưa có tiêu chuẩn)
- **Phần mềm phải**: (nên) checklist tự đánh giá kèm bằng chứng theo tiêu chuẩn; xuất kết quả để công khai.
- **Bẫy**: TT 35 chỉ áp cho **bệnh viện** (Đ1 k2) và không có tiêu chí kỹ thuật CNTT (chỉ đòi có phòng/bộ phận CNTT, PL Mục II.9, và báo cáo sự cố). Đừng trích TT 35 cho phòng khám.

### HTTT-BC-R37 — Mức ứng dụng CNTT theo TT 54/2017
- **Căn cứ**: TT 54/2017 (phần còn hiệu lực: hạ tầng, phần mềm quản lý, HIS, RIS-PACS, LIS, phi chức năng, ATTT). TT 13/2025 Đ4 k3 b bãi bỏ Mục VIII PL I và tiêu chí EMR (EMR). TT thay thế chưa ban hành.
- **Áp dụng**: cơ sở KCB, thực tế là BV · **Hiệu lực/hạn**: đang áp dụng một phần
- **Mức**: NÊN (bộ tiêu chí đánh giá; chưa đọc gốc nên chưa xác định nghĩa vụ báo cáo định kỳ)
- **Phần mềm phải**: vendor HIS/LIS/PACS giữ bảng đối chiếu chức năng ↔ tiêu chí TT 54 để hỗ trợ khách hàng tự đánh giá; theo dõi TT thay thế.

**Đếm theo mức chính**: BẮT BUỘC 30 (R01–R07, R09–R11, R13–R16, R18–R20, R22–R24, R26, R27, R29–R36); BẮT BUỘC? 5 (R08, R12, R17, R25, R28); NÊN 2 (R21, R37). Có phần phụ mức thấp hơn: R03, R06, R20, R26, R36.

## 3. Pattern thiết kế

### HTTT-BC-P01 — Hộp thư đi pháp định nhiều đích
- **Giải quyết**: R01, R06, R11, R13, R17, R20, R23, R26, R27, R36
- **Cách làm**: sự kiện nghiệp vụ (ra viện, tử vong, chẩn đoán BTN, sự cố NC3, thay đổi nhân sự, thay đổi giá) ghi outbox trong **cùng transaction** với dữ liệu gốc; bộ phát tán áp quy tắc định tuyến (sự kiện → các đích), tạo một lần gửi cho mỗi đích; adapter riêng cho HTTT quản lý KCB, CSDLQG y tế, Hệ thống quản lý hành nghề, HTTT giám sát, Cổng BHXH, đơn thuốc quốc gia, Sổ SKĐT, kênh thủ công. Cùng hạ tầng với SKDT-P04, GIAYTO-P03.
- **Gợi ý dữ liệu**: `reg_event(event_type, source_table, source_id, source_version, occurred_at, payload_hash)`; `reg_destination(code, operator, transport[api|file|portal_manual], spec_version, active_from, active_to)`; `reg_route(event_type, destination_code, deadline_rule, active_from, active_to)` (`+24h`, `+5 working_days after period_end`, `+1h`); `reg_submission(event_id, destination_code, spec_version, status[pending|sent|acked|rejected|superseded|manual_pending_backfill], due_at, sent_at, ack_at, ack_ref, error_code, attempt, supersedes_submission_id)` với `UNIQUE(event_id, destination_code, source_version)`; chỉ mục `(status, due_at)`, `(destination_code, sent_at)`.
- **Đối soát và công khai**: job hằng ngày so số lượt ra viện trong HIS với số đã gửi thành công cho từng đích, và tổng báo cáo thống kê với dữ liệu chi tiết đã gửi; lệch thì tạo phiếu xử lý (`recon_run(date, destination_code, expected, sent_ok, rejected, missing, report_file)`); kết quả là bằng chứng "đầy đủ, kịp thời" (R13, R20, R23). Bản "hiện hành" của bảng giá, giờ làm việc, danh sách người hành nghề, kết quả tự đánh giá xuất JSON/CSV có chữ ký và ngày hiệu lực qua cùng kênh (R06, R11, R36).
- **Đánh đổi**: thêm bảng và tiến trình nền; tách lỗi từng đích, dễ thêm đích khi TTYQG ra chuẩn; idempotency key = event + đích + phiên bản nguồn. Đích không trả ack (cổng nhập tay) chỉ đối soát được mức "đã xuất".

### HTTT-BC-P02 — Đồng hồ hạn pháp định và leo thang
- **Giải quyết**: R06, R23, R27, R29, R33, R34
- **Cách làm**: dịch vụ lịch dùng chung tính `due_at` theo lịch làm việc VN (ngày nghỉ lễ tết có phiên bản theo năm), múi giờ `Asia/Ho_Chi_Minh`; cảnh báo ở 50%, 80%, 100% hạn; quá hạn tạo bản ghi vi phạm bất biến.
- **Gợi ý dữ liệu**: `vn_holiday(date, kind, source_doc)`; `deadline_alert(submission_id, threshold, notified_to, notified_at)`.
- **Đánh đổi**: "ngày" và "ngày làm việc" lẫn giữa thân TT và phụ lục (R23): lưu cả hai cách tính, cảnh báo theo mốc sớm hơn.

### HTTT-BC-P03 — Kênh dự phòng có nhập bù
- **Giải quyết**: R26 (TT 15 Đ4 k2 b), R33, R17
- **Cách làm**: adapter lỗi quá N lần hoặc đích bảo trì thì cho chuyển lần gửi sang `manual_pending_backfill`, in/xuất file theo mẫu, ghi kênh, lúc, người nhận; đích hoạt động lại thì nhắc nhập bù, chỉ đóng khi có `ack_ref`.
- **Gợi ý dữ liệu**: `manual_delivery(submission_id, channel[paper|email|phone], recipient, delivered_at, evidence_file)`.
- **Đánh đổi**: thêm thao tác người dùng; có bằng chứng tuân thủ khi hệ thống quốc gia lỗi (cùng tinh thần BHYT-GD-R21).

### HTTT-BC-P04 — Động cơ báo cáo thống kê theo định nghĩa có phiên bản
- **Giải quyết**: R09, R15, R22–R25, R29
- **Cách làm**: mỗi biểu là một định nghĩa (chỉ tiêu, truy vấn, ánh xạ ICD-10 → dòng, kỳ, hạn, ngày hiệu lực); mỗi lần nộp lưu snapshot để cung cấp lại (TT 23 Đ6 k1 b). Đổi chế độ 01/03/2027 chỉ là thêm phiên bản.
- **Gợi ý dữ liệu**: `report_def(code, version, legal_basis, period_type, deadline_rule, valid_from, valid_to)` (không chồng lấn hiệu lực trên cùng code); `report_row_map(report_code, version, row_code, icd10_from, icd10_to, label)`; `report_run(report_code, version, period_start, period_end, generated_at, data_hash, approved_by, submitted_at, submission_id)`; `report_cell(run_id, row_code, col_code, value)`.
- **Đánh đổi**: tốn công dựng định nghĩa ban đầu.

### HTTT-BC-P05 — Sổ nhân sự hành nghề có lịch đăng ký và đối soát định danh
- **Giải quyết**: R06, R16, R21; giao BHYT-GD-R17, DUOC-R02
- **Cách làm**: người hành nghề có ba định danh (số định danh, số GPHN/CCHN, mã liên thông đơn thuốc) và các đợt đăng ký tại cơ sở (vị trí, phạm vi, khung giờ, hiệu lực, trạng thái gửi cơ quan cấp phép); mọi y lệnh kiểm tra người thực hiện có đợt đăng ký bao phủ thời điểm.
- **Gợi ý dữ liệu**: `practitioner(cccd UNIQUE, license_no UNIQUE, license_issued_at, license_expiry, rx_link_code UNIQUE NULL)`; `practice_registration(practitioner_id, facility_code, role, scope_codes[], weekly_slots jsonb, valid_from, valid_to, reported_at, report_ref)`; `practice_change_task(registration_id, kind[leave|add], due_at, done_at)`; chặn khung giờ chồng trong cùng cơ sở, khác cơ sở chỉ cảnh báo.
- **Đánh đổi**: chặn cứng theo lịch có thể cản cấp cứu; cần "vượt khung" có lý do (Luật Đ36 k3 có ngoại lệ cấp cứu).

### HTTT-BC-P06 — Bộ phân loại BTN và hàng đợi báo cáo dịch tễ
- **Giải quyết**: R26–R28, R30, R31
- **Cách làm**: luật kích hoạt theo ICD-10, kết quả xét nghiệm dương tính, cờ "nghi ngờ"; tạo phiếu báo cáo với đồng hồ 24 giờ hoặc theo quy tắc Cục Phòng bệnh (cấu hình); bảng điều khiển hội chứng theo ngày cho chùm ca.
- **Gợi ý dữ liệu**: `idd_catalog(disease_code, group[A|B|C], icd10_list[], lab_triggers jsonb, report_rule jsonb, valid_from, source_doc)`; `ido_case_report(encounter_id, disease_code, status[suspected|probable|confirmed|death], trigger_at, due_at, submitted_at, submission_id)`.
- **Đánh đổi**: quy tắc từng bệnh chưa được công bố lại sau khi TT 54/2015 bị bãi bỏ: để cấu hình và ghi nguồn.

### HTTT-BC-P07 — Module sự cố y khoa có ẩn danh và vòng đời RCA
- **Giải quyết**: R08, R32–R35
- **Cách làm**: vault danh tính thay cho xóa hẳn; không có lệnh DELETE; `nc_level = 3` ⇒ `report_type = mandatory`, `reporter_ref NOT NULL`, `serious_type` bắt buộc.
- **Gợi ý dữ liệu**: `incident(code, reported_at, report_type, reporter_ref, reporter_vault_key, affected_type, location, occurred_at, description, initial_action, notified_doctor, notified_family, notified_patient, recorded_in_emr, harm_level[A..I], nc_level[0..3], event_group, cause_group, serious_type[1..28], status, encounter_id)`; `incident_identity_vault(key, user_id)`; `incident_rca(incident_id, team, due_at = received_at + 60d, findings, recommendations)`; `incident_escalation(incident_id, phone_call_at, called_to, written_sent_at)`.
- **Đánh đổi**: ẩn danh làm khó điều tra bổ sung; vault có kiểm soát là điểm cân bằng.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| HTTT-BC-A01 | R01, R17 | Phần mềm xuất được dữ liệu cho HTTT quản lý KCB chưa? Kiến trúc xuất là adapter có phiên bản hay code cứng theo XML BHYT? | Tài liệu kiến trúc, danh sách đích | BẮT BUỘC |
| HTTT-BC-A02 | R02 | 10 hồ sơ ra viện (có tự chi trả): đủ dân tộc, nghề nghiệp, nơi ở hiện tại, cân nặng trẻ em, ngày giường HSTC, ICD-9-CM, ICD-10 theo vai? Tỷ lệ null từng trường 3 tháng | Truy vấn, ảnh màn hình | BẮT BUỘC |
| HTTT-BC-A03 | R03 | Tỷ lệ thuốc, dịch vụ của lượt tự chi trả có mã danh mục dùng chung | Truy vấn | BẮT BUỘC |
| HTTT-BC-A04 | R04 | Tóm tắt ra viện 1 ca nội trú đủ 7 nhóm (a–g), có thiết bị cấy ghép, đơn thuốc ngoại trú, lịch tái khám | Bản in hoặc JSON | BẮT BUỘC |
| HTTT-BC-A05 | R05 | Ca thử "nặng xin về", "tử vong": phân biệt trạng thái? Phiếu nguyên nhân tử vong có chuỗi ICD-10 và khoảng thời gian? Giấy báo tử theo Mẫu 05 TT 25/2025? | Ảnh màn hình, mẫu phiếu | BẮT BUỘC |
| HTTT-BC-A06 | R06 | So tài khoản có quyền chỉ định, kê đơn với danh sách đăng ký hành nghề đã gửi Sở; thử gán y lệnh ngoài khung giờ; nhân sự nghỉ gần nhất đã báo trong 03 ngày làm việc? | Danh sách đối chiếu, log chặn, văn bản báo Sở | BẮT BUỘC |
| HTTT-BC-A07 | R06, R16 | Bảng người hành nghề đủ số định danh, số GPHN, mã liên thông đơn thuốc, không trùng? | Truy vấn trùng/null | BẮT BUỘC |
| HTTT-BC-A08 | R07 | Giường phân loại HSTC, áp lực âm; TBYT có hiện trạng; báo cáo nhập-xuất-tồn 6 tháng chạy được | Báo cáo mẫu | BẮT BUỘC |
| HTTT-BC-A09 | R09, R10 | Báo cáo 6 tháng: ngày điều trị trung bình khớp Biểu 9/BCT? DVKT được chỉ định ngoài danh mục phê duyệt? | Hai báo cáo, truy vấn ngoại lệ | BẮT BUỘC |
| HTTT-BC-A10 | R11 | So bảng giá trong hệ thống với niêm yết tại quầy, website; hóa đơn có dịch vụ ngoài bảng giá hiệu lực | Ảnh niêm yết, truy vấn | BẮT BUỘC |
| HTTT-BC-A11 | R12 | Có mã nhân viên, thiết bị, tòa nhà ổn định để hạch toán theo ca? | Tài liệu, mẫu dữ liệu | NÊN |
| HTTT-BC-A12 | R13 | Sửa hồ sơ đã gửi: có phiên bản mới và hàng đợi gửi lại cho mọi đích? | Log submission trước/sau | BẮT BUỘC |
| HTTT-BC-A13 | R14 | Thời gian xuất danh sách ca theo một nhóm ICD-10 trong 30 ngày | Thời gian chạy, file | BẮT BUỘC |
| HTTT-BC-A14 | R15 | Hồ sơ cấp cứu chấn thương có mã nguyên nhân ngoài V01–Y98? Tỷ lệ thiếu | Truy vấn | BẮT BUỘC |
| HTTT-BC-A15 | R18 | Kết nối ra ngoài có TLS; khóa API lưu ở đâu; log có dữ liệu sức khỏe dạng rõ? | Cấu hình, mẫu log | BẮT BUỘC |
| HTTT-BC-A16 | R19 | Cơ sở xin GPHĐ mới từ 2027 hoặc cơ sở cũ trước 01/01/2029: có bằng chứng kết nối HTTT? | Hồ sơ GPHĐ, nhật ký gửi | BẮT BUỘC |
| HTTT-BC-A17 | R20 | Liệt kê các đích quốc gia đang gửi và tần suất (BHXH, đơn thuốc, Sổ SKĐT, KSK, giám sát BTN, quản lý hành nghề) | Bảng đích, bằng chứng gửi gần nhất | BẮT BUỘC |
| HTTT-BC-A18 | R21 | GPHN, số đăng ký thuốc có ghi nguồn và ngày đồng bộ? | Ảnh màn hình, schema | NÊN |
| HTTT-BC-A19 | R22 | In Sổ khám bệnh A1/CSYT (PK) hoặc A3, A4 (sản) từ hệ thống | Bản in | BẮT BUỘC |
| HTTT-BC-A20 | R23, R24 | Chạy Biểu 9, 11, 14/BCT tháng gần nhất; so bản đã nộp; kiểm bảng ánh xạ ICD-10; ngày nộp so hạn 05 ngày làm việc | Báo cáo, snapshot, biên nhận | BẮT BUỘC |
| HTTT-BC-A21 | R25 | Định nghĩa biểu có ngày hiệu lực? Kế hoạch cho chế độ mới từ 01/03/2027? | Cấu hình, roadmap | BẮT BUỘC? |
| HTTT-BC-A22 | R26, R27 | Ca thử chẩn đoán BTN và tử vong do BTN: có phiếu báo cáo, đồng hồ 24 giờ, cảnh báo? Đối chiếu 3 tháng ca BTN trong HIS với ca đã nhập HTQLGS/eCDS | Log, bảng đối chiếu | BẮT BUỘC |
| HTTT-BC-A23 | R26 | Lần báo cáo giấy khi hệ thống giám sát lỗi đã được ghi và nhập bù? | Sổ dự phòng, trạng thái | BẮT BUỘC |
| HTTT-BC-A24 | R28 | Có báo cáo hội chứng theo ngày, cảnh báo chùm ca? | Ảnh màn hình | NÊN |
| HTTT-BC-A25 | R29, R15 | Báo cáo BKLN, RLTT kỳ tháng gửi CDC tỉnh trong 05 ngày làm việc? Báo cáo thương tích 6 tháng? | Biên nhận gửi | BẮT BUỘC |
| HTTT-BC-A26 | R30 | Danh mục BTN đã cập nhật nhóm A/B/C theo QĐ 1965/2026? | Bảng danh mục, ngày cập nhật | BẮT BUỘC |
| HTTT-BC-A27 | R31 | Ai xem được hàng đợi báo cáo BTN? Báo cáo tổng hợp có lộ định danh? | Ma trận phân quyền | BẮT BUỘC |
| HTTT-BC-A28 | R32 | Form báo sự cố đủ trường PL III TT 43? Người ngoài HIS báo được? Thử xóa một báo cáo | Ảnh form, kết quả thử | BẮT BUỘC |
| HTTT-BC-A29 | R33 | Sự cố NC3 trong năm: thời điểm phát hiện, gọi báo trước (≤ 01 giờ với sự cố nghiêm trọng), báo cơ quan quản lý | Bảng thời gian, văn bản đã gửi | BẮT BUỘC |
| HTTT-BC-A30 | R34 | Mỗi sự cố đủ 3 trục phân loại? RCA xong trong 60 ngày? Có báo cáo tuần và 6 tháng? | Truy vấn, báo cáo | BẮT BUỘC |
| HTTT-BC-A31 | R35 | Báo cáo tự nguyện ẩn danh được? Ai giải mã danh tính? Có log truy cập module sự cố? | Cấu hình quyền, log | BẮT BUỘC |
| HTTT-BC-A32 | R36 | BV: có tự đánh giá TT 35 quý I và đã công khai? Cơ sở ngoài BV: đã chuẩn bị theo dự thảo? | Biên bản, link công khai | BẮT BUỘC (BV) / NÊN (khác) |
| HTTT-BC-A33 | R37 | Có bảng đối chiếu chức năng với TT 54/2017 và mức tự xác định gần nhất? | Bảng đối chiếu | NÊN |
| HTTT-BC-A34 | P01 | Có outbox, submission, đối soát định kỳ; tỷ lệ lỗi và tồn đọng theo đích? | Schema, dashboard | NÊN |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 01/03/2019 | TT 43/2018 sự cố y khoa có hiệu lực | Mọi cơ sở KCB | Đã qua |
| 01/01/2024 | Luật KCB 2023 có hiệu lực | Mọi cơ sở KCB | Đã qua |
| 01/01/2025 | Tiêu chuẩn chất lượng cơ bản cho BV (TT 35/2024; Đ120 k6) | Bệnh viện | Đã qua |
| 01/07/2025 | NĐ 102/2025 và TT 23/2025 có hiệu lực | Mọi cơ sở | Đã qua |
| 19/08/2025; 22/10/2025 | NĐ 194/2025 (NĐ 47/2024 bị bãi bỏ); NĐ 278/2025 có hiệu lực | CQNN | Đã qua |
| 11–12/2025 | KH 1642: cơ sở đăng ký tài khoản, cập nhật dữ liệu trên Hệ thống quản lý hành nghề | Mọi cơ sở KCB | Đã qua |
| Quý I/2026 | BV tự đánh giá TT 35 cho năm 2025 | BV | Đã qua |
| 15/05/2026; 19/05/2026 | NĐ 90/2026 có hiệu lực; QĐ 11/2026/QĐ-TTg (mục XVIII y tế) có hiệu lực | Mọi cơ sở; BYT | Đã qua |
| 02/06/2026 | CV 4016: cập nhật 100% dữ liệu người hành nghề, cơ sở (thứ cấp) | Mọi cơ sở KCB | Đã qua |
| 01/07/2026 | Luật Phòng bệnh, NĐ 165/2026, TT 15/2026; TT 54/2015, TT 17/2019 hết hiệu lực; danh mục BTN mới | Cơ sở KCB, cơ sở xét nghiệm | Đã qua |
| 07–08/2026 | Danh mục nội hàm thông tin CSDL KCB (QĐ 2114 mục II.1); có thể là QĐ 2682 ngày 22/08/2026 (chưa xác minh) | BYT | Đã qua |
| 10/2026 | Dự kiến xong dự thảo TT thay TT 23 (thứ cấp) | BYT | Sắp tới |
| 30/11/2026 | Xử lý dứt điểm nhiệm vụ CĐS quá hạn (CT 07, thứ cấp) | Đơn vị thuộc BYT | Sắp tới |
| 01/01/2027 | TT 38/2024 có hiệu lực; HTTT quản lý KCB phải vận hành (Đ120 k8); điều kiện hạ tầng CNTT cho hồ sơ GPHĐ mới (Đ120 k5 a); tiêu chuẩn chất lượng cho cơ sở ngoài BV (Đ120 k6) nếu TT kịp ban hành | Mọi cơ sở KCB | Sắp tới |
| 2027–2028 | GĐ 2 HTTT quản lý KCB: kết nối HTTT của cơ sở | TTYQG, Cục QLKCB; cơ sở KCB | Sắp tới |
| 01/03/2027 | TT 23/2025 hết hiệu lực; chế độ báo cáo mới (nếu đã ban hành) | Mọi cơ sở | Sắp tới |
| Quý I/2028 | Lần tự đánh giá đầu của cơ sở ngoài BV cho năm 2027 (suy luận) | PK, TYT… | Sắp tới |
| 01/01/2029 | Cơ sở có GPHĐ trước 2027 phải đáp ứng điều kiện hạ tầng CNTT (Đ120 k5 b) | Mọi cơ sở cũ | Sắp tới |
| 01/01/2030 | Báo cáo BKLN, RLTT, dinh dưỡng, thương tích trên HTTT giám sát (TT 15 Đ66 k1) | Cơ sở KCB, TYT | Sắp tới |
| Thường xuyên | Ca nghi BTN: TYT xã 24 giờ; tử vong do BTN: 24 giờ; sự cố nghiêm trọng: gọi trong 01 giờ; tổng hợp sự cố 6 tháng; thống kê tháng, BKLN, RLTT: 05 ngày làm việc; nhân sự nghỉ: 03 ngày làm việc; bổ sung nhân sự: 10 ngày; TT 38 kỳ 6/12 tháng | Mọi cơ sở KCB | — |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**
- TT 54/2015/TT-BYT (khai báo BTN) và TT 17/2019/TT-BYT (giám sát BTN) → **bãi bỏ** bởi TT 15/2026 Đ65 k2 a, b từ 01/07/2026; cùng bị bãi bỏ TTLT 16/2013, QĐ 25/2006/QĐ-BYT (C11).
- Luật PCBTN 03/2007 → Luật Phòng bệnh 114/2025/QH15 (01/07/2026).
- NĐ 47/2024/NĐ-CP (danh mục CSDLQG) → bãi bỏ bởi NĐ 194/2025 Đ40 k2 a (19/08/2025); danh mục nay là QĐ 11/2026/QĐ-TTg.
- NĐ 47/2020 → còn hiệu lực một phần; NĐ 194 Đ40 k2 b bãi bỏ một số điều, Đ40 k3 sửa Đ35 k3.
- TT 32/2014 → TT 23/2025 (01/07/2025) → văn bản mới chưa ban hành (TT 23 hết hiệu lực 01/03/2027).
- TT 54/2017 → bãi bỏ một phần bởi TT 13/2025 (06/06/2025); phần còn lại chờ TT thay.
- TT 43/2018 → chưa bị thay; Luật KCB Đ71 không giao Bộ trưởng quy định chi tiết (suy luận từ câu chữ), nên chưa chắc sẽ có TT thay.
- Giấy báo tử: mẫu PL I TT 24/2020 → Mẫu 05 TT 25/2025 (GIAYTO-R10; C02).

**Bẫy trích dẫn**
1. "Đ120 k6 là điều kiện CNTT": sai. Điều kiện hạ tầng CNTT là **Đ120 k5 a, b** (dẫn Đ52 k2 d); k6 là tiêu chuẩn chất lượng (C05).
2. Lớp text PDF TT 38/2024 trên datafiles đọc nhầm số hiệu thành "39/2024/TT-BVT"; đúng là 38/2024/TT-BYT.
3. TT 38 không có thời hạn gửi theo lượt KCB. Các mốc 24 giờ thuộc BHYT (BHYT-GD-R19), đơn thuốc (DUOC-R12), KSK (SKDT-R15). TT 38 chỉ có "ngay" khi sửa sai (Đ4 k2), "ngay khi có yêu cầu" với dịch nhóm A (Đ5 k4), và kỳ 6/12 tháng.
4. TT 38 còn dẫn NĐ 13/2023 và NĐ 47/2020: NĐ 13 đã được thay bởi Luật 91/2025, NĐ 356/2025; NĐ 47/2020 bị bãi bỏ một phần. TT 38 Đ14 cho phép áp văn bản thay thế.
5. TT 38 Đ15 đánh số khoản "1, 2, 3, 4, 3": trích "Đ15 (khoản cuối)".
6. TT 23 Đ5 không có khoản 3; thân TT "05 ngày làm việc", PL IV "05 ngày".
7. QĐ 11/2026/QĐ-TTg: CSDLQG về y tế ở **mục XVIII**, không phải XVII; OCR đọc năm ký thành "2020", đúng là 28/03/2026.
8. eCDS/HTQLGS xây theo TT 54/2015; hướng dẫn "24 hoặc 48 giờ tùy bệnh" dẫn TT 54/2015 không còn là căn cứ sau 01/07/2026. Căn cứ nay là TT 15/2026 + hướng dẫn chuyên môn Cục Phòng bệnh (Đ66 k2 cho dùng tiếp hướng dẫn chuyên môn cũ đến khi có hướng dẫn thay).
9. Hai văn bản cùng số 165: NĐ 165/2025/NĐ-CP (Luật Dữ liệu) và NĐ 165/2026/NĐ-CP (Luật Phòng bệnh).
10. "HTTT về quản lý hoạt động KCB" (TT 38) ≠ "Hệ thống quản lý quốc gia về hành nghề và hoạt động KCB" (KH 1642). QĐ 2114 nâng cấp hệ thống thứ hai thành phiên bản đầu của hệ thống thứ nhất, nhưng về pháp lý vẫn là hai tên.
11. TT 35/2024 chỉ áp cho bệnh viện.
12. TT 43/2018: báo cáo bắt buộc là mục 7–9 PL I (NC3: G, H, I); NC2 (E, F) vẫn là tự nguyện dù phải báo người đứng đầu ngay. Có nguồn ghi sai "từ NC2".
13. TT 43, NĐ 90, NĐ 194, NĐ 278, QĐ 11 lấy từ OCR: file này chỉ diễn giải; câu trích nguyên văn chỉ từ Luật KCB (VBHN), TT 38, TT 15, TT 23, Luật Phòng bệnh và NĐ 102 (đã đối chiếu bản Công báo).

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. Hướng dẫn kỹ thuật kết nối HTTT quản lý KCB (QĐ 2114 mục IV.2 b): định dạng (dùng lại XML QĐ 130?), phương thức, tần suất (theo lượt hay kỳ), cơ sở tư nhỏ có được nhập tay. Hỏi TTYQG.
2. Từ 01/01/2027 đến khi GĐ 2 vận hành, cơ sở thực hiện nghĩa vụ TT 38 thế nào; có bị coi là vi phạm nếu chưa gửi được. Hỏi Cục QLKCB.
3. Tiêu chí "hạ tầng CNTT bảo đảm kết nối" khi thẩm định GPHĐ từ 01/01/2027; áp NĐ 90 Đ39 cho cơ sở cũ trước 01/01/2029 cần ý kiến luật sư.
4. QĐ 2682/QĐ-BYT (22/08/2026) danh mục thông tin cơ bản CSDL hoạt động KCB: chưa đọc bản gốc; có thể là đặc tả trường quan trọng nhất cho R02–R12.
5. Thời hạn báo cáo từng ca BTN theo nhóm sau khi TT 54/2015 hết hiệu lực (hướng dẫn chuyên môn Cục Phòng bệnh); eCDS có phải HTTT giám sát theo TT 15 không. Hỏi Cục Phòng bệnh/CDC tỉnh.
6. QĐ 1965/QĐ-BYT 2026: cần bản gốc để lập bảng ánh xạ ICD-10.
7. Văn bản thay TT 23/2025 và cách xử lý báo cáo kỳ tháng 02/2027. Hỏi Vụ Kế hoạch – Tài chính.
8. TT 43/2018 còn hiệu lực chỉ dựa trên nguồn thứ cấp và việc không thấy văn bản thay.
9. Tiêu chuẩn chất lượng cơ sở ngoài BV: chưa có toàn văn; nếu không kịp ban hành trước 01/01/2027 thì Đ120 k6 áp thế nào.
10. TT 54/2017: chưa đọc gốc; có nghĩa vụ báo cáo mức ứng dụng CNTT định kỳ không.
11. CT 07/CT-BYT: chưa có bản gốc; ngày ký chính xác; quan hệ với "chiến dịch 100 ngày" Sổ SKĐT mà SKDT ghi theo inventory.
12. NĐ 96/2023: chưa kiểm tra văn bản sửa đổi (NQ 21/2026/NQ-CP về cắt giảm TTHC y tế); thời hạn 03 ngày làm việc, 10 ngày có thể đã đổi.
13. Chế tài thống kê: nghị định xử phạt lĩnh vực thống kê chưa đọc.
14. TT 38 Đ10 k5 b, k8 (thu chi, hạch toán theo ca, chi nhân công theo mã nhân viên) có áp cho cơ sở tư không; dữ liệu thu nhập nhân viên cần căn cứ xử lý DLCN riêng không. Hỏi luật sư.
15. Cổng tiếp nhận dữ liệu y tế của BYT (TT 48 Đ7, NĐ 188 Đ71): quan hệ với HTTT quản lý KCB và CSDLQG chưa rõ (trùng câu hỏi mở 5 của BHYT-GD).
