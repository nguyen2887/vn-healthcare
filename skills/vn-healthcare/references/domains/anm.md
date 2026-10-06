# ANM — An ninh mạng và cấp độ hệ thống thông tin

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám, nhà thuốc (chủ quản HTTT); vendor HIS/EMR/LIS/RIS-PACS, cổng/app người bệnh, KCB từ xa, SaaS y tế (đơn vị vận hành) · Research gốc: `research/deep/ANM.md`

Phạm vi: Luật An ninh mạng 116/2025/QH15 và bộ nghị định ngày 19/08/2026 (NĐ 331 cấp độ HTTT, NĐ 333 chi tiết Luật, NĐ 330 xử phạt), TCVN 14423:2026, chuyển tiếp từ khung cũ (NĐ 85/2016, NĐ 53/2022, TT 12/2022), nhật ký, lưu dữ liệu trong nước, báo cáo sự cố, sao lưu và khôi phục, quy định ngành y tế (QĐ 326/QĐ-BYT, TT 13/2025, CV 365, CT 07/CT-BYT). Tài liệu nghiên cứu, không phải ý kiến pháp lý.

## Tóm tắt nhanh

- Khung cũ đã hết: Luật ATTT mạng 2015 + Luật ANM 2018 hết HL 01/07/2026; **NĐ 85/2016, NĐ 53/2022, TT 12/2022, TT 03/2017 hết HL cùng ngày** (Luật 64/2025 Đ57 k2 sửa bởi Luật 87/2025). NĐ 85 chỉ còn được dẫn làm thủ tục thẩm định chuyển tiếp ở NĐ 331 Đ39 k1 — ANM-R05.
- Phân cấp (NĐ 331 Đ11–15): HIS/EMR nội bộ = **cấp 2** bất kể quy mô; dịch vụ trực tuyến (cổng/app người bệnh) xử lý dữ liệu nhạy cảm của **≥ 10.000** chủ thể = cấp 3; KCB từ xa, bán thuốc online = cấp 3 vì thuộc ngành nghề kinh doanh có điều kiện (suy luận) — ANM-R02.
- Đưa HTTT cấp 3–5 vào vận hành khi chưa phê duyệt cấp độ: 20–30 triệu (cá nhân), tổ chức gấp đôi; Quy chế ANM phải ban hành **trước** khi phê duyệt hồ sơ cấp độ — ANM-R04, R07.
- Báo cáo sự cố ANM: thông báo ban đầu **24 giờ** (sự cố nghiêm trọng), báo cáo **72 giờ**, **ngay khi phát hiện** nếu có dấu hiệu xâm phạm ANQG hoặc gián đoạn nghiêm trọng — ANM-R16.
- Hạn sắp tới: **25/12/2026** chủ quản gửi báo cáo năm cho Bộ Công an (nội bộ trước 20/12); **01/01/2027** thẩm định cấp độ cho HTTT đang đầu tư; **01/07/2027** mọi HTTT cũ phải đáp ứng NĐ 331 + TCVN 14423:2026 — ANM-R05, R17.
- Kỹ thuật tối thiểu (TCVN 14423:2026): MFA cho truy cập từ Internet/đối tác và tài khoản quản trị; mật khẩu ≥ 14 ký tự nếu không MFA; vô hiệu tài khoản không hoạt động 45 ngày; sao lưu tách biệt có khôi phục thử — ANM-R09, R10, R13.
- Bẫy: mức phạt các mục an ninh mạng của NĐ 330 là **mức cá nhân**, tổ chức × 2 (ngược với mục BVDLCN); "≥ 10.000 người bệnh = cấp 3" sai nếu nói về HIS nội bộ (C19).

## Mục lục

- Khung chung: R01 ranh giới HTTT, không chia nhỏ hạ cấp · R02 phân loại cấp độ · R03 phạm vi NĐ 331 · R04 hồ sơ cấp độ, thẩm định, phê duyệt · R05 chuyển tiếp · R06 đánh giá rủi ro · R07 Quy chế và phương án ANM · R08 TCVN 14423:2026
- Kỹ thuật: R09 tài khoản, phân quyền · R10 MFA, mật khẩu · R11 nhật ký · R12 mã hóa, toàn vẹn · R13 sao lưu, khôi phục · R14 phát triển an toàn, lỗ hổng, pentest · R15 giám sát ANM · R16 sự cố 24h/72h/ngay · R17 báo cáo năm cho BCA · R18 cloud, TTDL thuê ngoài · R19 lưu dữ liệu tại VN · R20 xác thực tài khoản dịch vụ trực tuyến
- Tổ chức, ngành y tế: R21 bộ phận phụ trách ANM, tập huấn · R22 hợp đồng thuê dịch vụ · R23 kết thúc vận hành, xóa sạch · R24 QĐ 326/QĐ-BYT · R25 ATTT cho HSBA điện tử
- Pattern: P01–P11 · Audit: A01–A26

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| Luật 116/2025/QH15 | Luật An ninh mạng | 01/07/2026 | Còn HL; Đ44 k2: Luật ATTT mạng 86/2015 và Luật ANM 24/2018 hết HL từ 01/07/2026 | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-116-2025-qh15-468678.htm) |
| NĐ 331/2026/NĐ-CP | Bảo vệ ANM đối với HTTT (cấp độ) | 19/08/2026 | Còn HL; không có điều bãi bỏ NĐ 85; Đ39 k1 dẫn NĐ 85 cho thẩm định chuyển tiếp | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-331-2026-nd-cp-470334.htm) · [VB 219243](https://vanban.chinhphu.vn/?pageid=27160&docid=219243) |
| NĐ 333/2026/NĐ-CP | Chi tiết Luật An ninh mạng | 19/08/2026 | Còn HL; Đ31 giữ thủ tục NĐ 53 cho hồ sơ đã nộp | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-333-2026-nd-cp-470335.htm) · [VB 219244](https://vanban.chinhphu.vn/?pageid=27160&docid=219244) |
| NĐ 330/2026/NĐ-CP | Xử phạt VPHC an ninh mạng và BVDLCN | 19/08/2026 | Còn HL | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-330-2026-nd-cp-470339.htm) · [VB 219266](https://vanban.chinhphu.vn/?pageid=27160&docid=219266) |
| TCVN 14423:2026 | ANM – HTTT – Yêu cầu cơ bản (lần 2, 113 trang) | Ngày công bố chưa xác minh | Thay TCVN 14423:2025 và TCVN 11930:2017; là tiêu chuẩn NĐ 331 Đ28–30 viện dẫn | gốc (bản đăng lại trên cổng UBND xã, Quảng Ngãi) | [PDF](https://sontaythuong.quangngai.gov.vn/upload/2007044/20260908/TCVN%2014423%202026%20ANM%20HTTT.pdf) |
| Luật 64/2025/QH15, Luật 87/2025/QH15 | Ban hành VBQPPL; Luật sửa đổi | 64: 01/04/2025; 87: 01/07/2025 | Còn HL; Luật 87 Đ1 k22 sửa Đ57 k2: văn bản quy định chi tiết hết HL cùng văn bản được hướng dẫn, trừ khi được công bố tiếp tục HL | gốc | [Luật 64 PDF](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/2/44584/55716-1-2025603-60464-2025-qh15.pdf) · [Luật 87 PDF](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45526/57608-1-2025955-95687-2025-qh15.pdf) |
| NĐ 85/2016/NĐ-CP | Bảo đảm an toàn HTTT theo cấp độ (cũ) | — | **Hết HL từ 01/07/2026** (C07); chỉ còn được NĐ 331 Đ39 k1 dẫn cho thẩm định chuyển tiếp đến 01/01/2027 | gốc-meta | — |
| NĐ 53/2022/NĐ-CP | Hướng dẫn Luật ANM 2018 | — | **Hết HL từ 01/07/2026** (C07); nội dung lưu dữ liệu nay ở NĐ 333 Đ19–20 | gốc-meta | — |
| TT 12/2022/TT-BTTTT; TT 03/2017/TT-BTTTT | Hướng dẫn NĐ 85 | — | **Hết HL từ 01/07/2026** (C07); hồ sơ nay ở NĐ 331 Đ21–22, kỹ thuật ở TCVN 14423:2026 | chưa xác minh | — |
| QĐ 326/QĐ-BYT (07/02/2024) | Quy chế ATTT, ANM của Bộ Y tế (thay QĐ 4159/2014) | Từ ngày ký | Còn HL theo văn bản; căn cứ là khung cũ — đọc cùng NĐ 331, TCVN 14423 | gốc-OCR có dấu (Đ7–8 đã đối chiếu) | [PDF (cổng Viện Dược liệu)](http://vienduoclieu.org.vn/Portals/0/QD%20326%20cua%20BYT%20ve%20an%20ninh%20mang.pdf) |
| TT 13/2025/TT-BYT | HSBA điện tử | 21/07/2025 | Còn HL | gốc-OCR (Đ1 k4, Đ2, Đ4 k3) | [PDF sao y, SYT Quảng Ninh](https://soytequangninh.gov.vn/upload/1002610/20250610/THONG_TU_HSBA_DIEN_TU_21_7_2025TT_13_2025__TT-BYT_ngay_6_6_2025_f5604afb8f.pdf) |
| CV 365/TTYQG-GPQLCL (06/06/2025) | Hướng dẫn kỹ thuật triển khai HSBA điện tử (không phải VBQPPL) | 06/06/2025 | Còn áp dụng; dẫn toàn khung cũ (NĐ 85, TT 12/2022, TCVN 11930, QĐ 742/QĐ-BTTTT) | gốc (bản ký số, đã đối chiếu các câu dẫn ở R12, R13, R18, R19, R22, R25) | [PDF, UBND Sơn Tịnh – Quảng Ngãi đăng lại](https://sontinh.quangngai.gov.vn/upload/2006782/20260423/H%C6%AF%E1%BB%9ANG%20D%E1%BA%AAN%20K%E1%BB%B8%20THU%E1%BA%ACT%20TRI%E1%BB%82N%20KHAI.pdf) |
| CT 07/CT-BYT (đăng 15/09/2026) | Xử lý "điểm nghẽn" chuyển đổi số y tế | Ký | Còn HL; đối tượng cụ thể chưa rõ | thứ cấp | [daibieunhandan.vn (báo, bối cảnh)](https://daibieunhandan.vn/bo-y-te-7-nhom-nhiem-vu-day-manh-va-xu-ly-dut-diem-cac-diem-nghen-ve-chuyen-doi-so-y-te-thuc-day-trien-khai-de-an-06-10430624.html) |
| Luật 91/2025 + NĐ 356/2025 | Bảo vệ DLCN (dữ liệu sức khỏe nhạy cảm) | 01/01/2026 | Còn HL — xem DLCN | gốc | [NĐ 356 Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm) |
| TT 47/2026/TT-BCA (QCVN 12:2026/BCA) | QCVN ANM cho HTTT lưu trữ tài liệu điện tử của cơ quan Đảng, Nhà nước | 01/07/2026 | Còn HL; không phải HIS/EMR | gốc-OCR (mục 1) | [VB 218069](https://vanban.chinhphu.vn/?pageid=27160&docid=218069) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/47-bca.pdf) |
| Luật 143/2025/QH15 Phụ lục IV; Luật 24/2026/QH16 | Ngành nghề kinh doanh có điều kiện: hiện hành STT 150 KCB, 151 kinh doanh dược, 154 kinh doanh TBYT; từ 01/03/2027 STT 100, 101, 103 | Phụ lục IV Luật 143: 01/07/2026; Luật 24: 01/03/2027 | Còn HL / sắp HL | gốc (Luật 143); gốc-OCR (Luật 24) | [Luật 143 PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat143-2025.pdf) · [Luật 24 VB 219356](https://vanban.chinhphu.vn/?pageid=27160&docid=219356) |
| QĐ 1875/QĐ-TTg (30/09/2026) | Khung kiến trúc ANM quốc gia v1.0 (gắn TCVN 14423:2026) | 30/09/2026 | Còn HL; bối cảnh | thứ cấp | [vietq.vn (báo, bối cảnh)](https://vietq.vn/ban-hanh-khung-kien-truc-an-ninh-mang-quoc-gia-gan-yeu-cau-ky-thuat-voi-tcvn-144232026-d244498.html) |
| NĐ 327, 328, 329, 332/2026 | Xử lý thông tin xâm phạm ANQG; chống tin giả; lực lượng bảo vệ ANM; kinh doanh sản phẩm, dịch vụ ANM | 19/08/2026 | Còn HL; ngoại vi (NĐ 332 nếu vendor bán SOC, pentest) | gốc-meta | [NĐ 332 Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-332-2026-nd-cp-470329.htm) |

QĐ 425/QĐ-BYT (quy chế ANM Hệ thống đơn thuốc QG) thuộc DUOC. QĐ 742/QĐ-BTTTT/2022 (an toàn phần mềm nội bộ) chỉ thấy qua CV 365; nội dung thực tế được TCVN 14423:2026 mục 5.17 bao phủ từ cấp 3.

## 2. Yêu cầu

### Khung chung: hệ thống nào thuộc diện, cấp mấy

### ANM-R01 — Xác định ranh giới HTTT, không chia nhỏ để hạ cấp
- **Căn cứ**: NĐ 331 Đ7 k1–2 (ranh giới theo chức năng, dòng dữ liệu, mức phụ thuộc vận hành, phạm vi ảnh hưởng khi sự cố — không theo tổ chức hành chính hay hạ tầng vật lý); Đ8 k1 a (mỗi HTTT một chủ quản); Đ8 k2 (đáp ứng nhiều tiêu chí thì lấy cấp cao nhất); Đ8 k3 (cấm phân tách hoặc hợp nhất hình thức để hạ cấp).
- **Áp dụng**: chủ quản và đơn vị vận hành (BV, PK, vendor SaaS) · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC (với HTTT thuộc phạm vi NĐ 331 Đ2; xem R03)
- **Phần mềm phải**: tài liệu kiến trúc thể hiện ranh giới (thành phần, luồng dữ liệu, phụ thuộc, kết nối ngoài: BHXH, Cổng BAĐT, đơn thuốc QG, VNeID). HIS, EMR, LIS, PACS chung CSDL hoặc phụ thuộc vận hành thì về nguyên tắc là một HTTT, lấy cấp cao nhất.
- **Bẫy**: không thể tách cổng người bệnh (cấp 3) khỏi HIS chỉ trên giấy để HIS ở cấp 2 nếu dùng chung CSDL và phụ thuộc vận hành (suy luận từ Đ7 k2, Đ8 k3).

### ANM-R02 — Phân loại cấp độ theo NĐ 331 Đ11–15
- **Căn cứ**: Luật 116 Đ8 k1 (5 cấp); NĐ 331 Đ9 (loại thông tin; loại HTTT: nội bộ, phục vụ người dân/DN, hạ tầng thông tin, điều khiển công nghiệp, khác; Đ9 k2 b nêu đích danh y tế trong nhóm dịch vụ trực tuyến). Đ11: cấp 1 = nội bộ, chỉ thông tin công cộng. Đ12: cấp 2 = (k1) nội bộ có thông tin riêng, thông tin cá nhân; (k2 a) dịch vụ trực tuyến không thuộc ngành nghề kinh doanh có điều kiện; (k2 b) dịch vụ trực tuyến xử lý dữ liệu của dưới 100.000 chủ thể (DLCN cơ bản) hoặc dưới 10.000 chủ thể (DLCN nhạy cảm); (k3) hạ tầng thông tin của một cơ quan. Đ13: cấp 3 = (k2 a) dịch vụ trực tuyến thuộc danh mục ngành nghề đầu tư kinh doanh có điều kiện; (k2 b) HTTT giải quyết TTHC; (k2 c) dịch vụ trực tuyến xử lý dữ liệu từ 100.000 chủ thể (cơ bản) hoặc từ 10.000 chủ thể (nhạy cảm); (k3) hạ tầng thông tin trong một bộ, ngành, một hoặc vài tỉnh. Đ14 k2: cấp 4 = HTTT quốc gia phục vụ Chính phủ điện tử hoặc hạ tầng toàn quốc, vận hành 24/7. Đ15–16: cấp 5, HTTT quan trọng về ANQG (Luật 116 Đ9 k2 g liệt kê HTTT quốc gia lĩnh vực y tế). Dữ liệu sức khỏe là DLCN nhạy cảm (NĐ 356 Đ4 k1 d — DLCN-R01). KCB, kinh doanh dược, kinh doanh TBYT thuộc Phụ lục IV Luật Đầu tư 143/2025 (STT 150, 151, 154; từ 01/03/2027 là STT 100, 101, 103 theo Luật 24/2026).
- **Áp dụng**: mọi chủ quản thuộc phạm vi · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: đếm được số **chủ thể dữ liệu duy nhất** có dữ liệu sức khỏe mà dịch vụ trực tuyến xử lý (người bệnh distinct, không phải lượt khám); gắn nhãn loại thông tin cho bảng/trường (công cộng/riêng/cá nhân cơ bản/cá nhân nhạy cảm) để làm thuyết minh (Đ22 k4 b).
- **Bẫy** (C19): ngưỡng 10.000/100.000 chỉ nằm trong nhánh **dịch vụ trực tuyến phục vụ người dân, doanh nghiệp** và tính theo chủ thể. HIS nội bộ (chỉ nhân viên dùng) rơi vào Đ12 k1 = cấp 2 **bất kể quy mô**, trừ khi đánh giá rủi ro đẩy lên (Đ10 k5). Dịch vụ trực tuyến thuộc ngành nghề có điều kiện là cấp 3 dù chỉ có một người dùng (Đ13 k2 a).

Bảng áp dụng cho hệ thống y tế (suy luận, chưa có hướng dẫn BCA/BYT):

| Hệ thống | Loại (Đ9 k2) | Cấp tối thiểu đề xuất | Lý do |
|---|---|---|---|
| HIS/EMR/LIS/RIS-PACS chỉ dùng nội bộ | nội bộ | 2 | Đ12 k1; không có ngưỡng quy mô ở nhánh nội bộ; đánh giá rủi ro có thể nâng lên 3 |
| Cổng/app người bệnh (đặt lịch, xem kết quả, HSBA, thanh toán) | dịch vụ trực tuyến | 3 nếu ≥ 10.000 người bệnh có dữ liệu sức khỏe; dưới ngưỡng là 2, trừ khi bị coi là "dịch vụ KCB trực tuyến" | Đ13 k2 c; Đ13 k2 a chưa chắc áp cho app chỉ đặt lịch/xem kết quả |
| Nền tảng KCB từ xa, tư vấn bác sĩ trực tuyến | dịch vụ trực tuyến | 3 | KCB là ngành nghề có điều kiện → Đ13 k2 a |
| Nhà thuốc hoặc sàn bán thuốc trực tuyến | dịch vụ trực tuyến | 3 | Kinh doanh dược là ngành nghề có điều kiện → Đ13 k2 a |
| SaaS HIS/EMR đa khách hàng do vendor vận hành | dịch vụ trực tuyến (NĐ 331 Đ3 k5) | 3 khi tổng người bệnh trên mọi tenant ≥ 10.000 | Đ13 k2 c; ngưỡng tính trên toàn hệ thống |
| Nền tảng dữ liệu y tế của Sở Y tế cho nhiều cơ sở | hạ tầng thông tin | 3 | Đ13 k3 |
| Hệ thống quốc gia của BYT (đơn thuốc QG, Sổ SKĐT, CSDLQG y tế) | hạ tầng/dịch vụ toàn quốc | 4 (ứng viên) | Đ14 k2 nếu yêu cầu 24/7; có thể vào danh mục ANQG |

### ANM-R03 — Phạm vi áp dụng NĐ 331
- **Căn cứ**: NĐ 331 Đ2 (áp dụng với HTTT phục vụ hoạt động của cơ quan, tổ chức nhà nước và HTTT cung cấp dịch vụ trực tuyến cho người dân, doanh nghiệp; tổ chức khác được "khuyến khích"). Luật 116 Đ1 k2, Đ10 k1 a.
- **Áp dụng**: BV công thuộc diện (suy luận: ĐVSN công lập là "tổ chức nhà nước"); BV tư, PK tư bắt buộc với hệ thống cung cấp dịch vụ trực tuyến (cổng, app, KCB từ xa); HIS nội bộ của tư nhân: Luật 116 yêu cầu xác định cấp độ, NĐ 331 chỉ "khuyến khích" → chưa rõ · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC?
- **Phần mềm phải**: vendor bán cho BV tư mặc định đáp ứng tối thiểu cấp 2 TCVN 14423, cấp 3 cho module trực tuyến của người bệnh.
- **Bẫy**: NĐ 330 Đ24 k1 phạt "không lập hồ sơ đề xuất cấp độ … theo quy định" — "theo quy định" đưa ngược về phạm vi Đ2 NĐ 331; cần luật sư xác nhận cho BV tư (§7).

### ANM-R04 — Hồ sơ đề xuất cấp độ, thẩm định và phê duyệt
- **Căn cứ**: NĐ 331 Đ18 (cấp 1–2: đơn vị chuyên trách ANM của chủ quản thẩm định và phê duyệt; cấp 3: đơn vị chuyên trách thẩm định, **chủ quản phê duyệt**, không gửi BCA; cấp 4–5: BCA chủ trì thẩm định; đơn vị chuyên trách đồng thời vận hành thì giao đơn vị khác hoặc hội đồng độc lập thẩm định), Đ19 (dự án mới, thuê dịch vụ), Đ20 (HTTT đang vận hành), Đ21 (thành phần hồ sơ), Đ22 (thuyết minh), Đ23 (thẩm định: hồ sơ chưa hợp lệ ≤ 05 ngày làm việc; cấp 3 ≤ 15; cấp 4, 5 ≤ 25), Đ24 (phê duyệt ≤ 07 ngày làm việc), Đ25, Đ30 k6 (hệ thống mới/nâng cấp triển khai đủ phương án đã duyệt trước khi vận hành), Phụ lục Mẫu 01–05. NĐ 330 Đ23 k1 c (đưa HTTT cấp 3–5 vào vận hành khi chưa được phê duyệt cấp độ: 20–30 triệu, cá nhân; tổ chức × 2).
- **Áp dụng**: chủ quản; vendor phối hợp (Đ19 k2 b) · **Hiệu lực/hạn**: 19/08/2026; chuyển tiếp xem R05
- **Mức**: BẮT BUỘC
- **Phần mềm phải** (vendor cung cấp được): tài liệu theo Đ22 k3 d — mô hình logic và vật lý; danh mục thiết bị, thiết bị mạng; danh mục ứng dụng/dịch vụ (máy chủ, vị trí, HĐH, mục đích); quy hoạch vùng mạng, IP private/public; danh mục loại thông tin; nhận diện rủi ro sơ bộ; thuyết minh phương án theo từng yêu cầu của cấp độ.
- **Bẫy**: tài liệu cũ theo NĐ 85 ghi cấp 3 phải xin ý kiến Bộ TT&TT — nay không còn; cấp 3 thẩm định, phê duyệt nội bộ.

### ANM-R05 — Chuyển tiếp: hệ thống đã có cấp độ, đang đầu tư, đang vận hành
- **Căn cứ**: Luật 116 Đ45 k1 (HTTT đã xác định cấp độ theo Luật ATTT mạng giữ cấp độ; trong 12 tháng từ 01/07/2026 phải đáp ứng điều kiện, tiêu chuẩn, biện pháp theo luật mới → **01/07/2027**), Đ45 k3 (sản phẩm, giải pháp ATTT đã dùng tiếp tục dùng, 12 tháng đáp ứng điều kiện mới). NĐ 331 Đ39 k1 (HTTT **đang trong quá trình đầu tư, xây dựng** trước 01/07/2026: hoàn thành thẩm định, phê duyệt cấp độ theo NĐ 85/2016 trong 6 tháng → **01/01/2027**; trong 12 tháng → 01/07/2027 đáp ứng biện pháp theo NĐ 331), Đ39 k2 (TCVN, QCVN dùng "an toàn thông tin mạng"/"an toàn HTTT" hiểu tương đương "an ninh mạng"). Luật 64/2025 Đ57 k2 (sửa bởi Luật 87/2025 Đ1 k22): NĐ 85/2016, TT 12/2022, TT 03/2017, NĐ 53/2022 hết HL từ 01/07/2026 cùng luật gốc (C07).
- **Áp dụng**: chủ quản · **Hiệu lực/hạn**: 01/01/2027; 01/07/2027
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: gap analysis giữa phương án cũ (TCVN 11930:2017) và TCVN 14423:2026 theo cấp đã duyệt; roadmap nâng cấp xong trước 01/07/2027.
- **Bẫy**: (1) HTTT đang vận hành mà chưa từng được phê duyệt cấp độ không có điều chuyển tiếp riêng → làm ngay theo NĐ 331 Đ20 (suy luận). (2) Bài trên cổng BCA diễn giải Đ39 k1 là "hệ thống vận hành trước 01/07/2026"; câu chữ gốc là "đang trong quá trình đầu tư, xây dựng" — bám câu chữ gốc. (3) "Cấp 2 cũ" (NĐ 85) và "cấp 2 mới" (NĐ 331) dùng tiêu chí khác nhau; Luật 116 Đ45 k1 giữ con số cấp, nhưng yêu cầu theo TCVN 14423:2026. (4) Dẫn chiếu NĐ 85 ở Đ39 k1 chỉ để mượn thủ tục thẩm định chuyển tiếp; không coi NĐ 85 là còn HL chung.

### ANM-R06 — Đánh giá rủi ro ANM và đánh giá lại khi vượt ngưỡng
- **Căn cứ**: NĐ 331 Đ10 k2 (bắt buộc đánh giá rủi ro khi: xác định cấp lần đầu; thay đổi chức năng, phạm vi, đối tượng, loại thông tin, công nghệ; mở rộng quy mô, tích hợp, kết nối liên thông, chia sẻ dữ liệu; sự cố nghiêm trọng; có yêu cầu), k3 (nội dung tối thiểu), k5 (rủi ro cao hơn cấp đã duyệt thì đề xuất cấp cao hơn), k6 (lưu hồ sơ), k8 (Khung quản lý rủi ro ANM của BCA — chưa thấy); Luật 116 Đ10 k1 b.
- **Áp dụng**: chủ quản · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bộ đếm chủ thể (R02) cảnh báo khi tiến gần 10.000 nhạy cảm/100.000 cơ bản; nhật ký thay đổi kết nối liên thông (API đối tác, BHXH, VNeID, bảo hiểm tư) làm trigger Đ10 k2; danh mục tài sản có xếp hạng quan trọng.

### ANM-R07 — Quy chế bảo đảm ANM và phương án ANM
- **Căn cứ**: NĐ 331 Đ28 k1 (quy định ANM trong thiết kế, xây dựng, vận hành, nâng cấp, hủy bỏ); Đ29 k2 (phương án gồm: an ninh trong thiết kế, vận hành, kiểm tra đánh giá, quản lý rủi ro, giám sát, dự phòng, ứng phó sự cố, khôi phục sau thảm họa, kết thúc và hủy bỏ); Đ30 k3–4 (yêu cầu quản lý; kỹ thuật: mạng, máy chủ, ứng dụng, dữ liệu); **Đ30 k7 (Quy chế phải được phê duyệt, ban hành trước khi hồ sơ cấp độ được phê duyệt)**. NĐ 330 Đ23 k1 a (không ban hành quy định: 20–30 triệu, cá nhân; tổ chức × 2).
- **Áp dụng**: chủ quản · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: vendor kèm bộ tài liệu vận hành an toàn (hardening, ma trận phân quyền mẫu, quy trình backup/restore, xử lý sự cố, hủy dữ liệu) để khách hàng đưa vào Quy chế.

### ANM-R08 — Áp dụng yêu cầu cơ bản theo TCVN 14423:2026
- **Căn cứ**: NĐ 331 Đ28 k1, k4; Đ29 k1; Đ30 k1–2 (yêu cầu cơ bản theo Nghị định và Tiêu chuẩn quốc gia "An ninh mạng – HTTT – Yêu cầu cơ bản" là tối thiểu; không gồm an ninh vật lý). TCVN 14423:2026: 15 nhóm cho cấp 1–2 (mục 3, 4); cấp 3 thêm 5.13 giám sát và phòng thủ, 5.17 phát triển ứng dụng an toàn, 5.18 quản lý kiểm tra ANM; cấp 4, 5 ở mục 6, 7.
- **Áp dụng**: HTTT thuộc phạm vi NĐ 331 · **Hiệu lực/hạn**: hệ thống mới trước khi vận hành; hệ thống cũ 01/07/2027
- **Mức**: BẮT BUỘC? (TCVN tự thân là tự nguyện, bắt buộc qua viện dẫn của NĐ 331; Luật 116 Đ10 k3 cho cấp 1–2 chọn biện pháp "theo nhu cầu, khả năng" — có độ vênh)
- **Phần mềm phải**: xem R09–R20.

### Yêu cầu kỹ thuật tác động trực tiếp tới phần mềm

### ANM-R09 — Quản lý tài khoản và phân quyền
- **Căn cứ**: TCVN 14423:2026 mục 4.6/5.6 (phân loại tài khoản quản trị/tác nghiệp/kỹ thuật/dịch vụ; danh sách tài khoản có loại, trạng thái, người quản lý, ngày kích hoạt và vô hiệu; rà soát ≥ 1 lần/6 tháng; mỗi tài khoản gắn một người, dùng chung phải được phê duyệt; vô hiệu tài khoản không hoạt động sau 45 ngày hoặc ngay khi đổi nhân sự; đổi/vô hiệu tài khoản mặc định; quyền tối thiểu, phân tách nhiệm vụ); 5.4.2.1 d (rà soát phân quyền dữ liệu ≥ 1 lần/6 tháng, cấp 3). QĐ 326 Đ8: khóa, thu hồi tài khoản khi chuyển công tác; hạn chế dùng chung tài khoản quản trị. Nghĩa vụ phân quyền với dữ liệu sức khỏe và mức phạt (NĐ 356 Đ4 k2; NĐ 330 Đ62 k1 b): xem DLCN-R01.
- **Áp dụng**: mọi HIS/EMR/app · **Hiệu lực/hạn**: 19/08/2026; hệ thống cũ 01/07/2027
- **Mức**: BẮT BUỘC (phân quyền giới hạn với dữ liệu sức khỏe — DLCN-R01) · BẮT BUỘC? (các con số 45 ngày, 6 tháng theo TCVN — R08)
- **Phần mềm phải**: `account_type` ∈ {admin, operator, technical, service}; job vô hiệu tài khoản không đăng nhập > 45 ngày (cấu hình được); báo cáo access review theo kỳ 6 tháng; RBAC theo chức danh/khoa, tách quyền quản trị hệ thống khỏi quyền xem dữ liệu người bệnh; không còn tài khoản mặc định khi bàn giao; tài khoản API tách khỏi tài khoản người.

### ANM-R10 — Xác thực: MFA và chính sách mật khẩu
- **Căn cứ**: TCVN 14423:2026 mục 3.6/4.6/5.6 (MFA bắt buộc với truy cập từ bên ngoài tổ chức, từ đối tác/bên thứ ba, từ Internet, và với tài khoản quản trị — có từ cấp 1; mật khẩu ≥ 08 ký tự nếu có MFA, **≥ 14 ký tự** gồm thường, hoa, đặc biệt, số nếu không MFA; đổi mật khẩu mặc định và ở lần đăng nhập đầu; cấp 3: quản trị dùng MFA, đổi ≥ 1 lần/2 tháng, không trùng 10 mật khẩu trước); 3.4.2.4/4.4.2.4 (mã hóa thông tin xác thực khi lưu). QĐ 326 Đ8 (giới hạn số lần đăng nhập sai liên tiếp; giới hạn thời gian chờ đóng phiên; mã hóa thông tin xác thực; không khuyến khích đăng nhập tự động; mật khẩu ≥ 8 ký tự có chữ hoa, thường, số, ký tự đặc biệt, đổi tối thiểu 06 tháng/lần). Luật 116 Đ42 k2. MFA cho xử lý dữ liệu lớn (NĐ 356 Đ9 k3 b; NĐ 330 Đ66 k2 b): xem DLCN-R24.
- **Áp dụng**: mọi hệ thống; đặc biệt HIS truy cập từ xa, cổng người bệnh, tài khoản vendor hỗ trợ từ xa · **Hiệu lực/hạn**: như R09
- **Mức**: BẮT BUỘC? (qua TCVN được NĐ 331 viện dẫn; QĐ 326 bắt buộc với đơn vị thuộc BYT)
- **Phần mềm phải**: MFA (TOTP, OTP, VNeID, chữ ký số) cho mọi truy cập từ Internet và mọi tài khoản admin; policy mật khẩu cấu hình được (độ dài, lịch sử 10, hết hạn); lockout sau N lần sai; session timeout; hash mật khẩu bằng thuật toán chuyên dụng (argon2id, bcrypt); hỗ trợ từ xa của vendor qua VPN/SSH/TLS.
- **Bẫy**: QĐ 326 (≥ 8 ký tự) thấp hơn TCVN 14423 (≥ 14 nếu không MFA). Đơn vị BYT phải đáp ứng cả hai → lấy mức chặt hơn.

### ANM-R11 — Nhật ký: nội dung, đồng bộ thời gian, thời hạn lưu
- **Căn cứ**:
  - Luật 116 Đ2 k11 (nhật ký hệ thống: thời gian, người dùng, hoạt động, trạng thái); Đ25 k2 b, d (DN cung cấp dịch vụ trên mạng: lưu nhật ký, thông tin tài khoản, thời gian sử dụng, thanh toán, IP truy cập).
  - NĐ 333 Đ16 k6 (DN cung cấp dịch vụ trên mạng: nhật ký tối thiểu gồm tài khoản, thời gian đăng nhập/đăng xuất, địa chỉ IP, cổng nguồn; truy xuất được ≥ 12 tháng); Đ20 k3 (nhật ký phục vụ điều tra ≥ 12 tháng).
  - NĐ 330 Đ34 k1 c (không lưu thông tin thiết bị, IP, thời gian đăng nhập của tài khoản số ≥ 90 ngày: 20–30 triệu); Đ23 k2 a (không lưu nhật ký theo quy định: 30–50 triệu); Đ33 k1 c (30–50 triệu); Đ21 k4 h (không lưu, không cung cấp log liên quan IP, máy chủ, DNS: 50–70 triệu) — mức cá nhân, tổ chức × 2.
  - TCVN 14423:2026 mục 4.8 (cấp 2: nhật ký truy cập, ứng dụng, cảnh báo thiết bị bảo mật; trường tối thiểu nguồn, đích, tài khoản, thời điểm, hành vi; đồng bộ máy chủ thời gian; dung lượng lưu ≥ 01 tháng; rà soát ≥ 1 lần/năm); 5.8 (cấp 3: thêm nhật ký tiến trình và MAC; SIEM hoặc tương đương; lưu tập trung ≥ 03 tháng; rà soát ≥ 1 lần/6 tháng); cấp 4 ≥ 06 tháng; cấp 5 ≥ 12 tháng.
  - QĐ 326 Đ7 e (máy chủ lưu nhật ký hệ thống tối thiểu 06 tháng), Đ8 (phần mềm, ứng dụng lưu nhật ký tối thiểu 03 tháng: thời gian, địa chỉ, tài khoản, nội dung truy nhập và sử dụng, lỗi, đăng nhập quản trị).
- **Áp dụng**: mọi HTTT y tế; con số 12 tháng của NĐ 333 áp cho DN cung cấp dịch vụ trên mạng (SaaS y tế có thuộc diện không: §7) · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC (nghĩa vụ lưu nhật ký: Luật 116 Đ25, NĐ 330 Đ34 k1 c) · BẮT BUỘC? (con số cụ thể theo từng loại chủ thể)
- **Phần mềm phải**: audit log tầng ứng dụng ghi `ts (UTC, NTP), account_id, account_type, src_ip, src_port, user_agent/device_id, action, object_type, object_id, result, reason`; ghi riêng đăng nhập/đăng xuất (IP, cổng nguồn, thiết bị); chống sửa xóa (append-only, WORM, hash-chain); xuất sang SIEM (syslog, CEF, JSON); cảnh báo kho log sắp đầy (TCVN 5.8).
- **Thời hạn lưu (hợp nhất C22)**: log an ninh hệ thống — khung ANM có các mức 90 ngày / 01–03–06–12 tháng / 3–6 tháng (QĐ 326) tùy đối tượng; khuyến nghị lưu ≥ 12 tháng để phủ mọi mức (NÊN). Log truy cập HSBA — không có quy định riêng; **NÊN (suy luận)** lưu bằng thời hạn lưu HSBA liên quan, tối thiểu 05 năm: chủ là BAOMAT-CB-R22. Tách hai loại log; vết sửa HSBA đi theo HSBA (EMR).

### ANM-R12 — Mã hóa và toàn vẹn dữ liệu
- **Căn cứ**: TCVN 14423:2026 mục 4.4.2.4 (cấp 2: mã hóa thông tin xác thực và dữ liệu không công khai khi lưu); 5.4.2.4 (cấp 3: mã hóa khi lưu và khi truyền, quản lý vòng đời khóa); 5.4.2.5 (mã kiểm tra toàn vẹn cho dữ liệu quan trọng); 5.4.2.7 (tách môi trường xử lý dữ liệu nhạy cảm cao); 5.4.2.8 (chữ ký số khi trao đổi dữ liệu nhạy cảm cao). CV 365 (khả năng mã hóa dữ liệu lưu trữ; mã hóa, giải mã thông tin người bệnh khi truyền nhận). QĐ 326 Đ7–8 (quản trị từ xa qua giao thức mã hóa SSH, SSL/TLS, VPN; mã hóa dữ liệu trên thiết bị lưu trữ di động). Mã hóa DLCN trên cloud (NĐ 356 Đ12 k4; NĐ 330 Đ69 k2 b, 50–70 triệu): xem DLCN-R12.
- **Áp dụng**: mọi hệ thống; rõ nhất khi chạy cloud · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC (DLCN trên cloud — DLCN-R12) · BẮT BUỘC? (phần còn lại qua TCVN)
- **Phần mềm phải**: TLS mọi kết nối (kể cả nội bộ, máy xét nghiệm, PACS nếu khả thi); mã hóa CSDL/ổ đĩa và bản sao lưu; mã hóa mức trường cho dữ liệu đặc biệt nhạy cảm (HIV, tâm thần, di truyền); KMS/HSM, xoay khóa; hash hoặc chữ ký số cho bản ghi xuất ra (XML/JSON gửi BHXH, Cổng BAĐT).

### ANM-R13 — Sao lưu và khôi phục
- **Căn cứ**:
  - Luật 116 Đ10 k2 đ (biện pháp lưu trữ, sao lưu), bắt buộc với cấp 3–4 (Đ10 k4); cấp 1–2 "theo nhu cầu" (Đ10 k3).
  - NĐ 331 Đ28 k1, Đ29 k2 e (khôi phục sau thảm họa).
  - TCVN 14423:2026 mục 4.11 (cấp 2: quy định sao lưu cấu hình, HĐH, CSDL, dữ liệu nghiệp vụ; định kỳ khôi phục thử; bảo vệ toàn vẹn bản sao lưu; hạ tầng sao lưu tách biệt môi trường vận hành); 5.11 (cấp 3: sao lưu tự động, quy tắc 3-2-1 hoặc tương đương, mã hóa bản sao lưu dữ liệu quan trọng, lưu tập trung).
  - TT 13/2025 Đ2 k1 (hạ tầng HSBA có lưu trữ dự phòng), Đ2 k4 (sẵn sàng phục hồi, truy xuất HSBA), Đ4 k3 b — gốc-OCR, chỉ diễn giải.
  - CV 365: định kỳ sao lưu dữ liệu gồm 01 bản tại cơ sở KCB; khuyến nghị thêm 01 bản tại đơn vị cung cấp dịch vụ lưu trữ.
  - QĐ 326 Đ8: hệ thống/phương tiện lưu trữ độc lập với hệ thống máy chủ dịch vụ để sao lưu dự phòng.
  - NĐ 330 Đ21 k4 đ (không phối hợp khôi phục dữ liệu khi sự cố: 50–70 triệu, cá nhân; tổ chức × 2).
- **Áp dụng**: mọi cơ sở KCB có HSBA điện tử (TT 13); mọi HTTT cấp 3+ (Luật 116) · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sao lưu tự động (CSDL, file đính kèm/DICOM, cấu hình), mã hóa, bất biến (immutable hoặc offline); ít nhất 1 bản tại cơ sở KCB khi chạy cloud (CV 365) hoặc 1 bản ngoài cơ sở khi chạy on-prem; công cụ khôi phục có biên bản thử định kỳ; công bố RPO/RTO.

### ANM-R14 — Phát triển ứng dụng an toàn, quản lý lỗ hổng, kiểm thử xâm nhập
- **Căn cứ**: TCVN 14423:2026 mục 5.17 (cấp 3+: quy trình phát triển an toàn; phần mềm thuê khoán phải có cam kết bảo mật và nhà phát triển cung cấp mã nguồn, nếu không thì cung cấp chứng chỉ đánh giá an toàn độc lập hoặc kiểm thử xâm nhập kèm cam kết chịu trách nhiệm pháp lý; kênh tiếp nhận báo cáo lỗ hổng; kiểm tra dữ liệu vào/ra; kiểm soát thông báo lỗi; không lưu thông tin xác thực trong mã nguồn; kiểm tra lỗ hổng mã nguồn và thư viện bên thứ ba trước khi vận hành); 5.7 (quét lỗ hổng ≥ 1 lần/6 tháng; quản lý bản vá; vá máy người dùng ≥ 1 lần/tháng); 5.18 (chương trình pentest). NĐ 331 Đ27 k3 c (đánh giá an toàn mã nguồn phần mềm nội bộ), k4; Đ31 k2 c (tự đánh giá do bộ phận độc lập với đơn vị vận hành; thuê tổ chức chuyên môn khi cấp 5, sau sự cố nghiêm trọng, thay đổi lớn, nghi ngờ tự đánh giá). Luật 116 Đ15 k2 a. NĐ 330 Đ27 k1 c (không khắc phục lỗ hổng theo yêu cầu lực lượng chuyên trách: 25–50 triệu, cá nhân; tổ chức × 2).
- **Áp dụng**: vendor và chủ quản; đầy đủ từ cấp 3 · **Hiệu lực/hạn**: 19/08/2026; hệ thống cũ 01/07/2027
- **Mức**: BẮT BUỘC? (cấp 3+, qua TCVN) · NÊN (cấp 2)
- **Phần mềm phải**: pipeline SAST, SCA, secret scanning, DAST trước mỗi release; SBOM; quy trình patch; `security.txt` hoặc kênh báo lỗ hổng; báo cáo pentest độc lập hoặc ký quỹ mã nguồn cho khách hàng cấp 3.

### ANM-R15 — Giám sát ANM và kết nối trung tâm giám sát
- **Căn cứ**: Luật 116 Đ40 k1 b (chủ quản HTTT kết nối hệ thống giám sát ANM, phòng chống mã độc tập trung về Trung tâm ANM quốc gia hoặc của tỉnh); Đ17 k1, k3 (DN cung cấp dịch vụ thư điện tử, truyền đưa, lưu trữ thông tin phải có hệ thống lọc mã độc). NĐ 333 Đ7 k2 (duy trì giám sát và phòng chống mã độc tập trung đáp ứng yêu cầu kết nối, chia sẻ dữ liệu cảnh báo), k6. NĐ 331 Đ33 k5 (đơn vị vận hành thiết lập kết nối), Đ34 k1 e (BCA triển khai giám sát tập trung cho HTTT cấp 3, 4, 5). TCVN 14423:2026 mục 5.13. NĐ 330 Đ23 k2 d (cản trở trao đổi dữ liệu giám sát: 30–50 triệu, cá nhân), Đ22.
- **Áp dụng**: chủ quản HTTT; ưu tiên cấp 3+ · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC? (luật nói chủ quản HTTT chung; cơ chế kết nối và đầu mối do BCA hướng dẫn, chưa thấy)
- **Phần mềm phải**: xuất log và cảnh báo theo chuẩn mở (syslog, CEF, JSON) để đẩy về SOC; cho phép cài agent EDR/giám sát trên máy chủ; cổng có upload file từ người bệnh thì quét mã độc file tải lên (suy luận từ Đ17 k3).

### ANM-R16 — Ứng phó và báo cáo sự cố: 24 giờ / 72 giờ / ngay lập tức
- **Căn cứ**: Luật 116 Đ40 k1 c (chủ quản báo cáo sự cố với cơ quan chuyên trách BCA hoặc BQP); Đ41 k3 (DN cung cấp dịch vụ trên không gian mạng: khi có sự cố ngay lập tức triển khai ứng cứu và báo cáo ngay); Đ12 k3. **NĐ 331 Đ31 k2 d**: báo cáo nguyên nhân, phạm vi ảnh hưởng, biện pháp khắc phục trong **72 giờ** kể từ khi phát hiện; sự cố phức tạp gửi sơ bộ rồi cập nhật và kết thúc; sự cố nghiêm trọng thông báo ban đầu trong **24 giờ**; sự cố có dấu hiệu xâm phạm ANQG, TTATXH hoặc gây gián đoạn nghiêm trọng HTTT báo cáo **ngay khi phát hiện**. NĐ 333 Đ9. TCVN 14423:2026 mục 4.15/5.16 (đầu mối chính và dự phòng; quy trình; phân nhóm sự cố; diễn tập). NĐ 330 Đ21 k1 b (không khai báo đầu mối ứng cứu: 10–20 triệu), k2 a (không báo cáo khi phát hiện sự cố: 20–30 triệu), k3 c, d (không báo cáo đúng quy trình; không có kế hoạch ứng phó: 30–50 triệu) — mức cá nhân, tổ chức × 2. QĐ 326 Đ13 (TT Thông tin y tế QG là đơn vị chuyên trách ứng cứu sự cố của BYT).
- **Áp dụng**: mọi chủ quản HTTT; vendor SaaS (Đ41 k3) · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: module/quy trình sự cố lưu `detected_at`, phân loại (thường/nghiêm trọng/dấu hiệu ANQG hoặc gián đoạn nghiêm trọng), tự tính hạn 24h và 72h, nơi nhận (BCA hoặc Cục A05; Sở/BYT nếu là đơn vị trong ngành), bằng chứng đã gửi; vendor báo khách hàng đủ sớm để kịp hạn (NÊN — suy luận: hợp đồng đặt ≤ 12 giờ).
- **Bẫy**: sự cố có lộ DLCN còn nghĩa vụ thông báo vi phạm DLCN trong 72 giờ theo Luật 91 Đ23 — xem DLCN-R17. Hai luồng độc lập, khác mẫu.

### ANM-R17 — Báo cáo định kỳ hằng năm cho Bộ Công an
- **Căn cứ**: NĐ 331 Đ35 (gửi qua hệ thống quản lý văn bản, phần mềm báo cáo của BCA hoặc email; chốt số liệu 15/12 năm trước – 14/12 năm báo cáo; đơn vị chuyên trách và đơn vị vận hành gửi chủ quản trước 20/12; chủ quản gửi BCA trước 25/12); Đ36 (12 nhóm nội dung: danh sách HTTT, cấp đề xuất và phê duyệt, mức triển khai phương án, Quy chế, kiểm tra đánh giá…); Đ33 k6.
- **Áp dụng**: chủ quản; vendor vận hành cung cấp số liệu · **Hiệu lực/hạn**: 25/12/2026 (kỳ đầu, suy luận) và hằng năm
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: xuất báo cáo tuân thủ theo từng yêu cầu của phương án (đã đáp ứng/một phần/chưa, kèm lộ trình) — Đ36 k9, k10.

### ANM-R18 — Chạy trên cloud hoặc trung tâm dữ liệu thuê ngoài
- **Căn cứ**: NĐ 331 Đ30 k8 (cấp 3, 4 thuê TTDL hoặc cloud: tách riêng lô-gic với hệ thống khác, quản lý truy cập giữa các hệ thống; tách lô-gic giữa các vùng mạng; phân vùng lưu trữ tách lô-gic), k9 (cấp 5: tách vật lý), k5. CV 365 (TTDL của nhà cung cấp đạt tối thiểu Tier 3/Rated 3 TIA-942, ISO 27001 hoặc tương đương). Hợp đồng cloud về DLCN (NĐ 356 Đ12 k2; NĐ 330 Đ69 k1 b): xem DLCN-R12.
- **Áp dụng**: SaaS y tế, BV dùng cloud · **Hiệu lực/hạn**: 19/08/2026; hệ thống cũ 01/07/2027
- **Mức**: BẮT BUỘC (cấp 3–4 trên cloud)
- **Phần mềm phải**: SaaS đa khách hàng cấp 3: mỗi khách hàng (hoặc mỗi HTTT cấp 3) có ranh giới lô-gic về mạng (VPC/VNet/subnet, security group), lưu trữ (schema, DB hoặc bucket riêng, khóa riêng), quản lý truy cập liên hệ thống.
- **Bẫy**: mô hình "shared DB + cột tenant_id" khó chứng minh "phân vùng lưu trữ tách lô-gic" (suy luận, cần BCA hướng dẫn).

### ANM-R19 — Lưu trữ dữ liệu tại Việt Nam
- **Căn cứ**: Luật 116 Đ25 k3 (DN trong và ngoài nước cung cấp dịch vụ trên mạng viễn thông, Internet, dịch vụ gia tăng tại VN, có thu thập, xử lý thông tin cá nhân hoặc dữ liệu do người dùng tại VN tạo ra, phải lưu dữ liệu này tại VN trong thời gian Chính phủ quy định). NĐ 333 Đ19 k1 (dữ liệu phải lưu tại VN: thông tin cá nhân người dùng tại VN; dữ liệu người dùng tạo ra như tên tài khoản, thời gian dùng, thẻ tín dụng, email, IP đăng nhập/đăng xuất gần nhất, số điện thoại gắn tài khoản), k2 ("Doanh nghiệp trong nước lưu trữ dữ liệu quy định tại khoản 1 Điều này tại Việt Nam"), k5 (hình thức lưu do DN quyết định); Đ20 k1 (tối thiểu 24 tháng, tính từ khi nhận yêu cầu). NĐ 330 Đ29 k2 c (không lưu dữ liệu tại VN: 50–70 triệu, cá nhân; tổ chức × 2), Đ33 k1 a, b. CV 365: HSBA điện tử triển khai trên hạ tầng tại cơ sở KCB hoặc trên hạ tầng điện toán đám mây (Cloud) đặt tại Việt Nam.
- **Áp dụng**: vendor SaaS và app y tế là DN Việt Nam (phạm vi phụ thuộc định nghĩa "dịch vụ trên mạng" ở NĐ 333 Đ3 k3–5); cơ sở KCB làm HSBA điện tử trên cloud (CV 365) · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC? (SaaS y tế có thuộc định nghĩa hẹp ở NĐ 333 Đ3 hay không chưa rõ) · BẮT BUỘC? (EMR theo CV 365 — hướng dẫn kỹ thuật mà TT 13 Đ6 k3 a buộc cơ sở làm theo; xem EMR)
- **Phần mềm phải**: CSDL chính, file, bản sao lưu, log chứa dữ liệu người dùng VN đặt ở region/DC tại VN; dịch vụ phụ trợ nước ngoài (email, push, analytics, AI API) phải lập danh mục luồng ra nước ngoài (đồng thời là TIA — DLCN-R15).
- **Bẫy**: Luật 116 Đ25 k3 + NĐ 333 Đ19 k2 không bắt bản sao duy nhất ở VN; một bản sao ở nước ngoài không bị cấm bởi chính điều này nhưng vướng quy định chuyển DLCN xuyên biên giới (suy luận).

### ANM-R20 — Xác thực tài khoản người dùng của dịch vụ trực tuyến
- **Căn cứ**: Luật 116 Đ25 k2 a (xác thực khi đăng ký tài khoản số; bảo mật thông tin, tài khoản; cung cấp thông tin người dùng cho BCA ≤ 24 giờ, khẩn cấp ≤ 03 giờ). NĐ 333 Đ16 k2 (xác thực tài khoản bằng số điện thoại di động tại VN, nếu không có thì số định danh cá nhân hoặc định danh điện tử hợp pháp; chỉ tài khoản đã xác thực mới được đăng tải, chia sẻ, dùng tính năng tương tác), k3 c, k4 b (gỡ thông tin vi phạm trong 24 giờ hoặc 06 giờ). NĐ 330 Đ29 k1 a, b (không xác thực khi đăng ký; không bảo mật tài khoản: 30–50 triệu, cá nhân; tổ chức × 2).
- **Áp dụng**: app/cổng người bệnh, nền tảng KCB từ xa, cộng đồng hỏi đáp sức khỏe do DN cung cấp · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC? (cùng câu hỏi phạm vi "dịch vụ trên mạng" như R19)
- **Phần mềm phải**: đăng ký có OTP SMS số VN hoặc liên kết VNeID; chat, đăng bài, đánh giá bác sĩ chỉ mở cho tài khoản đã xác thực; công cụ tra cứu, xuất thông tin tài khoản theo yêu cầu hợp lệ (log ai tra, khi nào, căn cứ văn bản nào); công cụ ẩn/gỡ nội dung nhanh. Định danh người bệnh trong KCB từ xa: TELE.

### Tổ chức, nhân sự, vendor, ngành y tế

### ANM-R21 — Chỉ định bộ phận/nhân sự phụ trách ANM; tập huấn
- **Căn cứ**: Luật 116 Đ40 k2 (chủ quản dùng NSNN: phương án ANM được thẩm định khi thiết lập, mở rộng, nâng cấp; chỉ định cá nhân, bộ phận phụ trách ANM); NĐ 331 Đ31 k1 (người đứng đầu chịu trách nhiệm; bộ phận/nhân sự chuyên trách phù hợp cấp độ; chưa có thì chỉ định đơn vị CNTT hoặc chuyển đổi số), k3 (đào tạo, diễn tập); Luật 116 Đ34 k2 + NĐ 333 Đ24 k8 b (người trực tiếp quản trị, vận hành HTTT cấp 3–5 trong cơ quan, tổ chức, DN nhà nước được tập huấn, cấp chứng nhận trong 36 tháng từ 19/08/2026 → 19/08/2029). NĐ 330 Đ21 k3 b (không thành lập/chỉ định đơn vị chuyên trách ứng cứu sự cố: 30–50 triệu, cá nhân; tổ chức × 2).
- **Áp dụng**: BV công (NSNN), mọi chủ quản · **Hiệu lực/hạn**: 19/08/2026; tập huấn 19/08/2029
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: vai trò "Security Officer" xem log và cảnh báo nhưng không có quyền nghiệp vụ lâm sàng (tách nhiệm vụ). Lực lượng thường trực ANM cho HTTT y tế: BAOMAT-CB-R27.

### ANM-R22 — Hợp đồng thuê dịch vụ và trách nhiệm vendor
- **Căn cứ**: NĐ 331 Đ5 k3 a (thuê dịch vụ CNTT: hợp đồng phải quy định chi tiết trách nhiệm, thẩm quyền về quản trị dữ liệu, kiểm soát truy cập, bảo đảm ANM), k3 b; Đ19 k2 b. TCVN 14423:2026 mục 4.14/5.15 (kiểm kê nhà cung cấp, văn bản phân định trách nhiệm, rà soát hằng năm), 5.17.2.1 c. CV 365: khi kết thúc hợp đồng, đơn vị cung cấp dịch vụ bàn giao toàn bộ dữ liệu cho cơ sở KCB và dữ liệu phải được hủy bỏ an toàn tại nhà cung cấp; cam kết bảo mật. QĐ 326 Đ1 k2 c (nhà cung cấp dịch vụ CNTT, ATTT cho đơn vị BYT thuộc đối tượng). DPA về DLCN: DLCN-R11.
- **Áp dụng**: vendor và cơ sở thuê · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC (nội dung hợp đồng theo NĐ 331 Đ5 k3 a)
- **Phần mềm phải**: xuất toàn bộ dữ liệu theo định dạng mở có data dictionary; quy trình và biên bản hủy dữ liệu sau bàn giao (theo NIST SP 800-88 hoặc tương đương — NÊN); ma trận trách nhiệm chia sẻ kèm hợp đồng.

### ANM-R23 — Kết thúc vận hành, hủy bỏ, xóa sạch
- **Căn cứ**: NĐ 331 Đ29 k2 g, Đ30 k3 g (phương án kết thúc vận hành, thanh lý, hủy bỏ); QĐ 326 Đ7 (xóa sạch dữ liệu trên máy chủ khi chuyển giao hoặc đổi mục đích); TCVN 14423:2026 mục 5.4.2.1 a.
- **Áp dụng**: chủ quản, vendor · **Hiệu lực/hạn**: 19/08/2026
- **Mức**: BẮT BUỘC (phải có phương án)
- **Phần mềm phải**: công cụ xóa an toàn dữ liệu của một tenant/cơ sở (gồm bản sao lưu theo vòng đời), có biên bản; đối chiếu thời hạn lưu HSBA (EMR-R22) trước khi xóa.

### ANM-R24 — Quy chế ATTT/ANM của Bộ Y tế cho đơn vị thuộc Bộ
- **Căn cứ**: QĐ 326/QĐ-BYT/2024: Đ1 k2 (đối tượng: đơn vị thuộc, trực thuộc BYT; tổ chức kết nối mạng BYT; nhà cung cấp dịch vụ CNTT, ATTT cho các đơn vị này), Đ7–Đ8 (mạng, máy chủ, ứng dụng, dữ liệu: log máy chủ ≥ 06 tháng, log ứng dụng ≥ 03 tháng; mật khẩu; mã hóa; sao lưu độc lập), Đ11 (xác định cấp độ theo NĐ 85, TT 12/2022), Đ13 (TT Thông tin y tế QG chuyên trách ứng cứu sự cố của Bộ).
- **Áp dụng**: BV và đơn vị trực thuộc BYT; vendor phục vụ họ · **Hiệu lực/hạn**: từ 07/02/2024
- **Mức**: BẮT BUỘC (văn bản quản lý nội bộ ngành còn hiệu lực); phần dẫn NĐ 85/TT 12 đọc thay bằng NĐ 331/TCVN 14423 (suy luận theo NĐ 331 Đ39 k2 và Luật 87 — C07)
- **Phần mềm phải**: như R09–R13; thêm giới hạn đăng nhập sai và timeout phiên (Đ8).

### ANM-R25 — Yêu cầu ATTT riêng cho HSBA điện tử
- **Căn cứ**: TT 13/2025 Đ1 k4 (HSBA tuân thủ pháp luật ATTT mạng, ANM, BVDLCN, lưu trữ), Đ2 k1, k4, Đ4 k3 b (cơ sở KCB ban hành quy chế lập, cập nhật, quản lý, lưu trữ, sử dụng và an toàn thông tin HSBA) — gốc-OCR, chỉ diễn giải. CV 365: HTTT của cơ sở KCB tối thiểu đáp ứng cấp độ 2 và có phương án bảo đảm ATTT (văn bản viện dẫn khung cũ, nay đọc theo NĐ 331, TCVN 14423). CT 07/CT-BYT (thứ cấp): hoàn thành lập, thẩm định, phê duyệt hồ sơ cấp độ cho 100% HTTT đang vận hành trước 30/09/2026; giám sát ATTT tập trung (SOC), diễn tập.
- **Áp dụng**: mọi cơ sở KCB làm HSBA điện tử (TT 13); hệ thống ngành y tế (CT 07, đối tượng chưa rõ) · **Hiệu lực/hạn**: 21/07/2025; CT 07: 30/09/2026 (đã qua)
- **Mức**: BẮT BUỘC (TT 13; cấp độ 2 tối thiểu theo CV 365) · BẮT BUỘC? (CT 07 — chưa có bản gốc)
- **Phần mềm phải**: hồ sơ cấp độ EMR tối thiểu cấp 2 theo TCVN 14423:2026 mục 4; tài liệu quy chế ATTT HSBA mẫu do vendor cung cấp. Yêu cầu chức năng HSBA điện tử: xem EMR.

**Tổng hợp mức** (theo mức chính): BẮT BUỘC 14 (R01, R02, R04, R05, R06, R07, R13, R16, R17, R18, R21, R22, R23, R24) · BẮT BUỘC? 7 (R03, R08, R10, R14, R15, R19, R20) · hỗn hợp BẮT BUỘC/BẮT BUỘC? 4 (R09, R11, R12, R25). Phần NÊN nằm trong R11 (lưu log ≥ 12 tháng; log HSBA theo thời hạn HSBA), R14 (cấp 2), R16 (SLA vendor ≤ 12 giờ), R22 (chuẩn xóa).

## 3. Pattern thiết kế

### ANM-P01 — Sổ đăng ký HTTT và cấp độ
- **Giải quyết**: R01, R02, R04, R05, R06, R17
- **Cách làm**: module/bảng cấu hình (trong GRC của BV hoặc trang quản trị SaaS) mô tả từng HTTT và căn cứ cấp độ; sinh thuyết minh Đ22 và báo cáo Đ36; khóa cờ "go-live" khi `approved_level >= 3 AND approval_date IS NULL`; cảnh báo khi cấp tính theo rule cao hơn cấp đã duyệt.
- **Gợi ý dữ liệu**: `info_system(id, name, owner_org, operator_org, system_type ENUM('internal','citizen_service','infrastructure','ics','other'), is_online_service, conditional_business_code, handles_tthc, scope_province_count, proposed_level CHECK 1..5, approved_level, approval_decision_no, approval_date, legacy_level_nd85, legacy_compliance_deadline)`; `system_component(system_id, component, host, os, zone, ip_private, ip_public, purpose)`; `data_category(system_id, table_or_field, info_class)`; `risk_assessment(id, system_id, trigger, performed_by_unit, independent_of_operator, result_level, file_ref, date)`.
- **Đánh đổi**: tốn công nhập liệu ban đầu; bù lại xuất ngay báo cáo 25/12 và hồ sơ cấp độ.

### ANM-P02 — Bộ đếm chủ thể dữ liệu và cảnh báo ngưỡng
- **Giải quyết**: R02, R06
- **Cách làm**: job hằng ngày `COUNT(DISTINCT patient_id)` có dữ liệu sức khỏe trong phạm vi dịch vụ trực tuyến (SaaS: cộng mọi tenant); đếm riêng chủ thể chỉ có DLCN cơ bản; cảnh báo ở 80% ngưỡng → tạo `risk_assessment(trigger='change')`.
- **Gợi ý dữ liệu**: `subject_counter(system_id, date, sensitive_subjects, basic_subjects)`; ngưỡng cấu hình 10.000 và 100.000.
- **Đánh đổi**: cần định nghĩa thống nhất "chủ thể" (khử trùng lặp qua số định danh cá nhân).

### ANM-P03 — Đường ống nhật ký an ninh bất biến
- **Giải quyết**: R11, R15, R16
- **Cách làm**: sự kiện có cấu trúc → hàng đợi → kho append-only (WORM/object lock) + chuỗi hash → SIEM; NTP mọi node. Retention: nóng 90 ngày (NĐ 330 Đ34 k1 c), ấm/lạnh đến ≥ 12 tháng (NÊN). Log truy cập hồ sơ HSBA tách riêng theo BAOMAT-CB-P4 (thời hạn theo HSBA, tối thiểu 5 năm).
- **Gợi ý dữ liệu**: `security_event(id ULID, ts_utc, ntp_synced, account_id, account_type, src_ip INET, src_port, device_id, user_agent, action, object_type, object_id, patient_id NULL, result, reason_code, prev_hash, hash)`; chỉ mục `(account_id, ts_utc)`, `(patient_id, ts_utc)`, `(src_ip, ts_utc)`.
- **Đánh đổi**: chi phí lưu trữ; log chỉ chứa ID, không chứa nội dung bệnh án.

### ANM-P04 — IAM theo loại tài khoản, MFA và vòng đời
- **Giải quyết**: R09, R10, R21
- **Cách làm**: policy engine theo `type` và nguồn mạng (nội bộ/Internet): Internet hoặc admin thì bắt buộc MFA; job `disable_inactive(45d)`; báo cáo access review mỗi 6 tháng. Phá kính (NÊN): quyền khẩn cấp ngoài phạm vi khoa, bắt nhập lý do, cảnh báo Security Officer, tự hết hạn (chi tiết: BAOMAT-CB-R20).
- **Gợi ý dữ liệu**: `account(id, type ENUM('admin','operator','technical','service'), owner_person_id, department, status, activated_at, disabled_at, last_login_at, mfa_enrolled, shared_approved_by NULL)`.
- **Đánh đổi**: máy trạm dùng chung ở khoa: dùng thẻ/token, hoặc giới hạn MFA cho truy cập từ ngoài mạng nội bộ (đúng câu chữ TCVN).

### ANM-P05 — Mã hóa nhiều lớp và toàn vẹn bản ghi
- **Giải quyết**: R12, R18
- **Cách làm**: TLS mọi kênh; TDE/ổ đĩa + mã hóa mức trường cho nhóm chẩn đoán đặc biệt; khóa mỗi tenant trong KMS (hỗ trợ "tách lô-gic lưu trữ" Đ30 k8); bản ghi xuất ra có `sha256` và chữ ký số của cơ sở.
- **Gợi ý dữ liệu**: `key_registry(tenant_id, key_id, purpose, created_at, rotated_at, destroyed_at)`.
- **Đánh đổi**: mã hóa mức trường làm khó tìm kiếm; dùng blind index/token.

### ANM-P06 — Sao lưu 3-2-1 bất biến + diễn tập khôi phục có biên bản
- **Giải quyết**: R13, R16, R22
- **Cách làm**: snapshot CSDL + WAL/PITR; object-lock cho file và DICOM; 1 bản tại cơ sở KCB (appliance/NAS do cơ sở giữ khi chạy SaaS — CV 365) và 1 bản ở DC khác tại VN; mã hóa bằng khóa của cơ sở; mỗi loại dữ liệu có ít nhất 1 lần khôi phục thử thành công trong chu kỳ cấu hình (ví dụ 6 tháng).
- **Gợi ý dữ liệu**: `backup_job(id, scope, started_at, finished_at, size, checksum, location, encrypted, immutable_until)`; `restore_test(id, backup_job_id, tested_at, rto_achieved, rpo_achieved, result, evidence_ref)`.
- **Đánh đổi**: băng thông đồng bộ bản về cơ sở; PACS lớn thì sao lưu theo tầng.

### ANM-P07 — Sổ sự cố với đồng hồ đếm hạn
- **Giải quyết**: R15, R16
- **Cách làm**: phát hiện → phân loại → (nghiêm trọng) thông báo ban đầu ≤ 24h → báo cáo ≤ 72h → cập nhật → kết thúc; cảnh báo T-6h trước mỗi hạn; cờ `personal_data_breach` kích luồng DLCN (DLCN-P08).
- **Gợi ý dữ liệu**: `incident(id, system_id, detected_at, severity ENUM('normal','serious','national_security_or_major_outage'), initial_notice_due, report_due, immediate_required, notified_vendor_at, notified_owner_at, reported_bca_at, report_ref, personal_data_breach, status)`.
- **Đánh đổi**: NĐ 331 không định nghĩa "sự cố nghiêm trọng" — tạm lấy phân nhóm sự cố TCVN 5.16 đến khi BCA hướng dẫn.

### ANM-P08 — SaaS đa khách hàng đạt "tách lô-gic" cho cấp 3
- **Giải quyết**: R18, R19, R22
- **Cách làm**: mỗi khách hàng cấp 3 có VPC/subnet và security group riêng; CSDL hoặc schema riêng với user DB riêng; bucket/prefix riêng có policy và khóa KMS riêng; quản trị vendor qua bastion có MFA và ghi phiên; region tại VN; liệt kê dịch vụ phụ trợ ngoài VN.
- **Gợi ý dữ liệu**: `tenant_isolation(tenant_id, vpc_id, db_schema, bucket, kms_key_id, level)`.
- **Đánh đổi**: chi phí cao hơn shared-everything; khách hàng cấp 2 có thể dùng chung nhưng phải chứng minh kiểm soát truy cập.

### ANM-P09 — Xác thực tài khoản người bệnh trên app/cổng
- **Giải quyết**: R11, R20
- **Cách làm**: OTP số điện thoại VN hoặc VNeID khi đăng ký; middleware chặn tính năng tương tác nếu chưa xác thực; log đăng nhập (IP, cổng nguồn, thiết bị); công cụ "lawful request" chứng minh hạn 24h/3h.
- **Gợi ý dữ liệu**: `account.verified_method ENUM('vn_phone','national_id','vneid')`, `verified_at`; `lawful_request(request_doc_no, requested_by, received_at, fulfilled_at)`.
- **Đánh đổi**: giảm tỉ lệ đăng ký; người nước ngoài không có số VN dùng định danh điện tử hợp pháp.

### ANM-P10 — Pipeline phát triển an toàn và gói bằng chứng cho khách hàng
- **Giải quyết**: R14, R22
- **Cách làm**: CI chạy SAST, SCA (SBOM CycloneDX), secret scan, DAST trên staging; chặn release khi còn lỗi mức cao; mỗi phiên bản kèm "security evidence pack" (báo cáo quét, pentest độc lập hằng năm, SBOM, CVE đã vá) để khách hàng cấp 3 đáp ứng TCVN 5.17.2.1 c khi không nhận mã nguồn.
- **Gợi ý dữ liệu**: `release_evidence(release_id, sbom_uri, sast_report, dast_report, pentest_ref, open_high_count)`.
- **Đánh đổi**: chi phí pentest độc lập; có thể ký quỹ mã nguồn thay thế.

### ANM-P11 — Bàn giao dữ liệu và hủy khi kết thúc hợp đồng
- **Giải quyết**: R22, R23
- **Cách làm**: API/job xuất toàn bộ dữ liệu một tenant (dump CSDL + file + data dictionary + checksum); hủy ở mọi bản sao gồm backup khi hết hạn khóa; biên bản ký hai bên.
- **Gợi ý dữ liệu**: `offboarding(tenant_id, export_uri, export_checksum, handed_over_at, destruction_completed_at, minutes_uri)`.
- **Đánh đổi**: backup bất biến không xóa sớm được → hợp đồng ghi "hủy khi object-lock hết hạn" và mã hóa bằng khóa riêng để crypto-shredding.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| ANM-A01 | R01, R02 | Vẽ lại luồng dữ liệu HIS, EMR, LIS, PACS, cổng người bệnh; thành phần dùng chung CSDL | Sơ đồ kiến trúc, danh mục kết nối ngoài | BẮT BUỘC |
| ANM-A02 | R02, R06 | `COUNT(DISTINCT patient_id)` trên dữ liệu cổng/app truy cập được; dịch vụ có thuộc ngành nghề có điều kiện (KCB, dược, TBYT) | Kết quả truy vấn có ngày; bảng phân loại có căn cứ Đ12/Đ13 | BẮT BUỘC |
| ANM-A03 | R04, R05 | Quyết định phê duyệt cấp độ (số, ngày, thẩm quyền Đ18); hệ thống cũ: quyết định theo NĐ 85 và kế hoạch đáp ứng trước 01/07/2027 | Quyết định; hồ sơ Đ21; ý kiến thẩm định (cấp 3+) | BẮT BUỘC |
| ANM-A04 | R04 | So ngày go-live với ngày phê duyệt cấp độ | Biên bản nghiệm thu, quyết định cấp độ | BẮT BUỘC (cấp 3–5) |
| ANM-A05 | R07 | Quy chế ANM ban hành trước ngày phê duyệt hồ sơ cấp độ? (Đ30 k7) | Quyết định ban hành Quy chế | BẮT BUỘC |
| ANM-A06 | R06 | Hồ sơ đánh giá rủi ro đối chiếu các lần thêm kết nối (BHXH, VNeID, đối tác) trong 12 tháng | Báo cáo đánh giá rủi ro, change log tích hợp | BẮT BUỘC |
| ANM-A07 | R09 | Xuất danh sách tài khoản: phân loại 4 nhóm? tài khoản > 45 ngày không đăng nhập còn active? tài khoản mặc định (admin/admin, sa, root)? | File tài khoản; ảnh cấu hình | BẮT BUỘC? |
| ANM-A08 | R09 | 3 người dùng ở 3 khoa thử truy cập hồ sơ ngoài phạm vi; ma trận quyền theo chức danh | Ảnh từ chối, ma trận RBAC | BẮT BUỘC |
| ANM-A09 | R10 | Đăng nhập từ Internet và bằng tài khoản quản trị có bị yêu cầu MFA; cấu hình độ dài mật khẩu, lockout, timeout | Ảnh luồng đăng nhập, file policy | BẮT BUỘC? |
| ANM-A10 | R10 | Mật khẩu lưu dạng hash có salt (argon2/bcrypt/scrypt/PBKDF2), không rõ hoặc MD5/SHA1 trơn | Mẫu bản ghi đã che | BẮT BUỘC? |
| ANM-A11 | R11 | Xem, sửa hồ sơ; log có ts, tài khoản, IP, cổng nguồn, hành động, đối tượng; thử sửa/xóa log bằng quyền DBA | Trích log; kết quả thử | BẮT BUỘC |
| ANM-A12 | R11 | Log đăng nhập cũ nhất còn truy xuất (≥ 90 ngày; ≥ 12 tháng nếu là DN dịch vụ trên mạng); đồng bộ NTP | Kết quả truy vấn, cấu hình NTP | BẮT BUỘC |
| ANM-A13 | R12 | Quét TLS mọi endpoint; mã hóa CSDL, ổ đĩa, backup; KMS khi chạy cloud | Báo cáo quét TLS; ảnh cấu hình | BẮT BUỘC (cloud) / BẮT BUỘC? |
| ANM-A14 | R13 | Lịch sao lưu tự động, vị trí bản sao, tính bất biến; biên bản khôi phục thử gần nhất; tự khôi phục thử một CSDL/ca bệnh trên test | Log backup, biên bản restore, RTO/RPO đo được | BẮT BUỘC |
| ANM-A15 | R14 | Báo cáo SAST/SCA/pentest gần nhất; quét secret repo (gitleaks); kênh báo lỗ hổng | Báo cáo, kết quả quét | BẮT BUỘC? (cấp 3+) / NÊN (cấp 2) |
| ANM-A16 | R15 | Log đẩy về SOC/SIEM? agent chống mã độc/EDR? kế hoạch kết nối Trung tâm ANM QG/tỉnh | Ảnh dashboard SIEM, văn bản kết nối | BẮT BUỘC? |
| ANM-A17 | R16 | Kế hoạch ứng phó; đầu mối chính + dự phòng; hồ sơ 1 sự cố gần nhất: phát hiện vs báo cáo (≤ 24h/≤ 72h) | Kế hoạch, sổ sự cố, văn bản báo cáo | BẮT BUỘC |
| ANM-A18 | R17 | Báo cáo năm gửi BCA (trước 25/12) và báo cáo nội bộ (trước 20/12) | Bản báo cáo, bằng chứng gửi | BẮT BUỘC |
| ANM-A19 | R18 | Cấp 3 trên cloud: VPC/subnet, security group, DB/schema, bucket, khóa KMS riêng | Sơ đồ mạng cloud, ảnh console | BẮT BUỘC |
| ANM-A20 | R19 | Vị trí (region/DC) của CSDL, file, backup, log, dịch vụ bên thứ ba nhận dữ liệu người dùng | Bảng data residency, hợp đồng DC/cloud | BẮT BUỘC? |
| ANM-A21 | R20 | Tạo tài khoản mới trên app: OTP số VN hoặc VNeID? tài khoản chưa xác thực chat/đăng bài được? | Ảnh luồng đăng ký | BẮT BUỘC? |
| ANM-A22 | R21 | Quyết định chỉ định bộ phận/nhân sự ANM; danh sách người quản trị hệ thống cấp 3+ và tình trạng tập huấn | Quyết định, chứng nhận tập huấn | BẮT BUỘC |
| ANM-A23 | R22, R23 | Hợp đồng vendor: quản trị dữ liệu, kiểm soát truy cập, ANM, bàn giao, hủy dữ liệu, nhà thầu phụ, báo sự cố | Hợp đồng, phụ lục SLA | BẮT BUỘC |
| ANM-A24 | R22 | Thử xuất toàn bộ dữ liệu một cơ sở kèm data dictionary | File xuất, checksum | BẮT BUỘC |
| ANM-A25 | R24 | (Đơn vị thuộc BYT) cấu hình theo QĐ 326 Đ7–8: log máy chủ ≥ 6 tháng, log ứng dụng ≥ 3 tháng, giới hạn đăng nhập sai, timeout | Cấu hình, trích log | BẮT BUỘC |
| ANM-A26 | R25 | Quy chế ATTT HSBA (TT 13 Đ4 k3 b); hồ sơ cấp độ EMR tối thiểu cấp 2 | Quyết định ban hành, hồ sơ cấp độ | BẮT BUỘC |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 01/07/2025 | Luật 87/2025 sửa Luật 64/2025 Đ57 k2: văn bản quy định chi tiết hết HL cùng văn bản được hướng dẫn, trừ khi được công bố tiếp tục HL | — | Đã qua |
| 01/07/2026 | Luật ANM 116 có HL; Luật ATTT mạng 2015, Luật ANM 2018 hết HL; NĐ 85/2016, NĐ 53/2022, TT 12/2022, TT 03/2017 hết HL (C07) | Mọi chủ quản | Đã qua |
| 01/07/2026 | QCVN 12:2026/BCA (TT 47/2026) có HL | HTTT lưu trữ tài liệu điện tử của cơ quan Đảng, Nhà nước | Đã qua |
| 19/08/2026 | NĐ 327–333/2026 có HL (330 xử phạt, 331 cấp độ, 333 chi tiết Luật) | Mọi đối tượng | Đã qua |
| 30/09/2026 | 100% HTTT đang vận hành hoàn thành hồ sơ cấp độ; SOC tập trung (CT 07, thứ cấp; đối tượng chưa rõ) | Hệ thống ngành y tế | Đã qua |
| 14/12/2026 | Chốt số liệu báo cáo ANM năm (15/12/2025–14/12/2026) | Chủ quản, đơn vị vận hành | Sắp tới |
| trước 20/12/2026 | Đơn vị chuyên trách, đơn vị vận hành (kể cả vendor vận hành) gửi báo cáo cho chủ quản | Đơn vị vận hành | Sắp tới |
| trước 25/12/2026 | Chủ quản gửi báo cáo năm cho Bộ Công an (lặp lại hằng năm) | Chủ quản | Sắp tới |
| 01/01/2027 | Hạn hoàn thành thẩm định, phê duyệt cấp độ (thủ tục NĐ 85) cho HTTT đang đầu tư, xây dựng trước 01/07/2026 | Chủ đầu tư, chủ quản | Sắp tới |
| 15/01 hằng năm | BCA cập nhật danh mục loại HTTT (Đ9 k2 e) → rà soát lại phân loại | Chủ quản theo dõi | Định kỳ |
| 01/03/2027 | Luật 24/2026/QH16 có HL: Phụ lục IV mới (KCB STT 100, dược STT 101, TBYT STT 103) | Theo dõi | Sắp tới |
| 01/07/2027 | HTTT đã có cấp độ theo luật cũ và HTTT đang đầu tư phải đáp ứng luật mới, NĐ 331, TCVN 14423:2026; sản phẩm, giải pháp ATTT cũ đáp ứng điều kiện mới | Chủ quản, đơn vị vận hành, vendor | Sắp tới |
| 19/08/2028 | Cơ quan, tổ chức, DNNN hoàn thành tập huấn cho lực lượng bảo vệ ANM (NĐ 333 Đ24 k8 a) | Cơ quan, tổ chức nhà nước | Xa |
| 19/08/2029 | Người quản trị, vận hành HTTT cấp 3–5 trong cơ quan, tổ chức, DNNN được tập huấn, cấp chứng nhận | BV công có HTTT cấp 3+ | Xa |
| Thường xuyên | Đánh giá rủi ro khi thay đổi/tích hợp; sự cố 24h/72h/ngay; cung cấp thông tin người dùng cho BCA ≤ 24h (khẩn ≤ 3h); gỡ nội dung ≤ 24h (khẩn ≤ 6h); rà soát tài khoản 6 tháng; vô hiệu tài khoản 45 ngày; quét lỗ hổng 6 tháng (cấp 3) | Chủ quản, vendor | — |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**

| Cũ | Mới | Ghi chú |
|---|---|---|
| Luật ATTT mạng 86/2015 + Luật ANM 24/2018 | Luật ANM 116/2025 | Luật 116 Đ44 k2; hết HL 01/07/2026 |
| NĐ 85/2016 (+ TT 12/2022, TT 03/2017) | NĐ 331/2026 + TCVN 14423:2026 | NĐ 331 không có điều bãi bỏ; NĐ 85 và các TT hướng dẫn hết HL từ 01/07/2026 cùng Luật ATTT mạng theo Luật 64 Đ57 k2 (sửa bởi Luật 87) — C07. NĐ 331 Đ39 k1 vẫn dẫn NĐ 85 làm thủ tục thẩm định chuyển tiếp đến 01/01/2027 |
| NĐ 53/2022 | NĐ 333/2026 | Hết HL 01/07/2026 (C07); NĐ 333 Đ31 giữ thủ tục NĐ 53 cho hồ sơ đã nộp; lưu dữ liệu tại VN nay ở NĐ 333 Đ19–20 |
| TCVN 11930:2017 (và TCVN 14423:2025) | TCVN 14423:2026 | Lời nói đầu TCVN 14423:2026 |
| QĐ 4159/QĐ-BYT/2014 | QĐ 326/QĐ-BYT/2024 | QĐ 326 vẫn dựa trên khung cũ |
| "An toàn thông tin mạng", "an toàn HTTT" trong TCVN, QCVN | ≡ "an ninh mạng" | NĐ 331 Đ39 k2 |
| Luật Đầu tư 143/2025 Phụ lục IV (KCB 150, dược 151, TBYT 154) | Luật 24/2026/QH16 Phụ lục IV (KCB 100, dược 101, TBYT 103) | Từ 01/03/2027 |

**Bẫy trích dẫn**
1. "Bệnh viện ≥ 10.000 người bệnh là cấp 3": sai nếu nói về HIS nội bộ (C19). Ngưỡng chỉ áp cho dịch vụ trực tuyến, tính theo chủ thể DLCN nhạy cảm.
2. "NĐ 331 thay thế NĐ 85": NĐ 331 không có câu nào như vậy. Viết đúng: NĐ 85 hết HL từ 01/07/2026 theo Luật 64 Đ57 k2 (sửa bởi Luật 87); NĐ 331 là khung mới.
3. Bài trên cổng BCA tóm NĐ 331 Đ39 k1 là "hệ thống vận hành trước 01/07/2026"; câu chữ gốc là "đang trong quá trình đầu tư, xây dựng".
4. Mức phạt NĐ 330: Mục 1–5 (an ninh mạng) là **mức cá nhân**, tổ chức × 2 (Đ7 k1; trần 100 triệu cá nhân, 200 triệu tổ chức). Mục 6 (BVDLCN, gồm Đ62 dữ liệu sức khỏe, Đ69 cloud) là **mức tổ chức**, cá nhân × 1/2. Đừng trích "20–30 triệu" cho bệnh viện mà không nhân đôi.
5. TCVN 14423:2026 tự thân là tự nguyện; bắt buộc qua viện dẫn của NĐ 331 Đ28–30. Luật 116 Đ10 k3 cho cấp 1–2 chọn biện pháp "theo nhu cầu, khả năng" → khi audit cấp 2 ghi BẮT BUỘC? cho các con số chi tiết.
6. Thời hạn log (C22): 90 ngày (NĐ 330 Đ34 k1 c, tài khoản số); 01/03/06/12 tháng (TCVN cấp 2/3/4/5 — dung lượng duy trì); 12 tháng (NĐ 333 Đ16 k6, Đ20 k3 — DN dịch vụ trên mạng); 03/06 tháng (QĐ 326 — đơn vị BYT). Không có con số riêng cho log truy cập HSBA → NÊN lưu theo thời hạn HSBA, tối thiểu 05 năm (suy luận, BAOMAT-CB-R22).
7. CV 365 dẫn toàn khung cũ (NĐ 85, TT 12/2022, TCVN 11930:2017, QĐ 742/QĐ-BTTTT, TT 39/2017, NĐ 13/2023). Đọc thành NĐ 331, TCVN 14423:2026, Luật 91/NĐ 356.
8. QĐ 326: mật khẩu ≥ 8 ký tự, thấp hơn TCVN 14423 (≥ 14 nếu không MFA). Không trích QĐ 326 như mức đủ.
9. NĐ 333 Đ20 k1 "tối thiểu 24 tháng" tính từ khi DN nhận yêu cầu lưu trữ, gắn với cơ chế yêu cầu (chủ yếu DN nước ngoài); không diễn giải thành "mọi DN phải giữ dữ liệu người dùng 24 tháng".
10. NĐ 331 Đ2: với tổ chức tư nhân ngoài phạm vi dịch vụ trực tuyến, Nghị định chỉ "khuyến khích". Đừng viết "mọi phòng khám tư phải lập hồ sơ cấp độ cho HIS theo NĐ 331" mà không ghi chú.
11. Cấp 3 thẩm định và phê duyệt nội bộ (đơn vị chuyên trách + chủ quản), không gửi BCA; BCA chỉ thẩm định cấp 4–5 (Đ18).
12. STT ngành nghề có điều kiện: "KCB STT 100, dược STT 101" là số thứ tự của Luật 24/2026 (HL 01/03/2027); hiện hành theo Luật 143/2025 là STT 150, 151 (TBYT 154). Kết luận cấp 3 cho KCB từ xa/bán thuốc online không đổi.
13. Định danh IP (Luật 116 Đ41 k5) được NĐ 333 Chương IV khoanh vào DN viễn thông, Internet — không áp cho SaaS y tế thông thường.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. **Văn bản "công bố tiếp tục có hiệu lực"** cho NĐ 85, TT 12/2022, TT 03/2017, NĐ 53/2022 theo Luật 64 Đ57 k2: chưa tìm thấy (C07 coi là hết HL). Hỏi luật sư: dẫn chiếu NĐ 85 ở NĐ 331 Đ39 k1 có đủ để áp thủ tục NĐ 85 đến 01/01/2027.
2. **Phạm vi NĐ 331 với BV tư, PK tư** (HIS nội bộ: Đ2 "khuyến khích" vs Luật 116 Đ10 k1 a; NĐ 330 Đ24 k1). ĐVSN công lập có phải "tổ chức nhà nước" theo NĐ 331 Đ2 và Luật 116 Đ34 k2 không. Cần luật sư hoặc hướng dẫn BCA (NĐ 331 Đ34 k1 b).
3. **App đặt lịch/xem kết quả có phải "dịch vụ trực tuyến thuộc ngành nghề kinh doanh có điều kiện" (KCB)** hay chỉ KCB từ xa — quyết định cấp 2 hay 3 cho cổng dưới 10.000 người. Hỏi Cục A05 hoặc BYT.
4. **SaaS y tế có phải "DN cung cấp dịch vụ trên mạng viễn thông, Internet, dịch vụ gia tăng"** theo NĐ 333 Đ3 k3–5 không — quyết định nghĩa vụ lưu dữ liệu tại VN (Đ19 k2), xác thực tài khoản (Đ16 k2), log 12 tháng (Đ16 k6). Chưa đọc Luật Viễn thông 24/2023.
5. **Văn bản BCA còn thiếu**: Khung quản lý rủi ro ANM (NĐ 331 Đ10 k8, Đ34 k1 c); quy định giám sát, ứng phó, khắc phục sự cố (Đ28 k6); biểu mẫu tự đánh giá (Đ31 k2 c); hướng dẫn xác định HTTT (Đ34 k1 b); định nghĩa "sự cố nghiêm trọng"; đầu mối, kỹ thuật kết nối Trung tâm ANM QG/tỉnh. Có thể chưa ban hành tại 06/10/2026.
6. **TCVN 14423:2026**: số và ngày quyết định công bố của Bộ KH&CN chưa xác minh; bản đọc là bản đăng lại trên cổng UBND xã.
7. **CT 07/CT-BYT**: chưa có bản gốc; hạn 30/09/2026 áp cho ai và "cấp độ ATTT" theo khung nào.
8. **TT 13/2025** chỉ có bản OCR không dấu cho Đ1 k4, Đ2, Đ4 k3 — chỉ diễn giải; đối chiếu bản có dấu (xem EMR).
9. **QĐ 326/QĐ-BYT**: BYT có kế hoạch thay theo khung mới không.
10. **Luồng báo cáo vi phạm DLCN (DLCN-R17) và sự cố ANM (R16)**: cùng đầu mối BCA nhưng hai mẫu, hai quy trình — cần hướng dẫn để gộp.
11. **QCVN 12:2026/BCA (TT 47/2026)**: có áp cho hệ thống lưu trữ hồ sơ, tài liệu hành chính điện tử của BV công không. Hỏi BCA hoặc Cục Văn thư lưu trữ.
12. **NĐ 332/2026**: vendor HIS kiêm cung cấp SOC/pentest cho BV có cần giấy phép kinh doanh sản phẩm, dịch vụ ANM không — chưa đọc nội dung.
