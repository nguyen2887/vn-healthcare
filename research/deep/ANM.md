# ANM — An ninh mạng và cấp độ hệ thống thông tin (K9)

> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: Luật An ninh mạng 116/2025/QH15 và bộ nghị định hướng dẫn ngày 19/8/2026 (NĐ 331 cấp độ HTTT, NĐ 333 chi tiết Luật, NĐ 330 xử phạt), TCVN 14423:2026, chuyển tiếp từ NĐ 85/2016 / NĐ 53/2022 / TT 12/2022, lưu log, lưu trữ dữ liệu trong nước, báo cáo sự cố, sao lưu và khôi phục, quy định riêng của ngành y tế (QĐ 326/QĐ-BYT, TT 13/2025, CV 365, CT 07/CT-BYT). Áp dụng cho HIS, EMR, LIS, RIS/PACS, cổng hoặc app người bệnh, KCB từ xa, SaaS y tế.
>
> **Nguồn đã đọc bản gốc có lớp chữ**: Luật 116 (DOCX Công báo), NĐ 331, NĐ 333, NĐ 330 (DOCX Công báo), TCVN 14423:2026 (PDF có chữ), Luật 64/2025 và Luật 87/2025 (PDF Công báo), Luật 91/2025 (PDF Công báo), NĐ 356/2025 (DOCX Công báo). **Gốc-OCR** (tesseract `eng`, mất dấu): QĐ 326/QĐ-BYT, TT 13/2025/TT-BYT, trang phạm vi của QCVN 12:2026/BCA (TT 47/2026/TT-BCA). **Thứ cấp**: CV 365 (trích lại trong báo cáo của TTYT Bạc Liêu), CT 07/CT-BYT (báo Đại biểu Nhân dân), Luật Đầu tư 143/2025 Phụ lục IV (bài trên xaydungchinhsach.chinhphu.vn), QĐ 1875/QĐ-TTg (vietq.vn). Nội dung web chỉ được dùng làm dữ liệu. Không dùng hethongphapluat.
>
> Đây là tài liệu nghiên cứu, **không phải ý kiến pháp lý**. Các chỗ ghi **(suy luận)** là nhận định của người soạn.

---

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| L-ANM-2025 | 116/2025/QH15 | Luật An ninh mạng | 01/07/2026 | Còn HL. Đ44 k2: Luật ATTTM 86/2015 và Luật ANM 24/2018 hết HL từ 01/07/2026 | Mọi chủ quản HTTT (BV công, BV tư, PK, nhà thuốc), vendor cung cấp dịch vụ trên không gian mạng | gốc (DOCX Công báo) | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-116-2025-qh15-468678.htm) · [PDF datafiles (scan)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat116-2025.pdf) |
| ND-331-2026 | 331/2026/NĐ-CP | Bảo vệ an ninh mạng đối với hệ thống thông tin | 19/08/2026 (Đ38) | Còn HL. **Không có điều bãi bỏ** NĐ 85/2016; Đ39 k1 còn dẫn NĐ 85 cho thẩm định chuyển tiếp | HTTT của cơ quan, tổ chức nhà nước và HTTT cung cấp dịch vụ trực tuyến cho người dân, doanh nghiệp (Đ2). Tổ chức khác: "khuyến khích" | gốc (DOCX Công báo, đọc toàn văn Đ1–40 + phụ lục mẫu) | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-331-2026-nd-cp-470334.htm) · [VB 219243](https://vanban.chinhphu.vn/?pageid=27160&docid=219243) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/8/331_2026_nd-cp_19082026-signed.signed.pdf) |
| ND-333-2026 | 333/2026/NĐ-CP | Quy định chi tiết một số điều và biện pháp thi hành Luật An ninh mạng | 19/08/2026 (Đ30) | Còn HL. **Không có điều bãi bỏ** NĐ 53/2022; Đ31 cho hồ sơ đã nộp theo NĐ 53 tiếp tục giải quyết theo NĐ 53 | Chủ quản HTTT (Đ7, Đ9); DN cung cấp dịch vụ trên mạng viễn thông, Internet, dịch vụ gia tăng (Đ15–20); DN viễn thông/Internet (Đ21–23) | gốc (DOCX Công báo) | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-333-2026-nd-cp-470335.htm) · [VB 219244](https://vanban.chinhphu.vn/?pageid=27160&docid=219244) |
| ND-330-2026 | 330/2026/NĐ-CP | Xử phạt VPHC lĩnh vực an ninh mạng và bảo vệ dữ liệu cá nhân | 19/08/2026 (Đ80) | Còn HL | Mọi tổ chức, cá nhân; Đ2 k2 k nêu rõ "chủ quản HTTT và đơn vị vận hành HTTT" | gốc (đọc Đ2, 4, 7, 21–24, 27, 29, 33, 34, 62, 69, 80–81) | [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-330-2026-nd-cp-470339.htm) · [VB 219266](https://vanban.chinhphu.vn/?pageid=27160&docid=219266) |
| TCVN-14423-2026 | TCVN 14423:2026 | An ninh mạng – Hệ thống thông tin – Yêu cầu cơ bản (xuất bản lần 2, 113 trang) | Ngày công bố: chưa xác minh | Thay TCVN 14423:2025 và **TCVN 11930:2017** (Lời nói đầu). Là "Tiêu chuẩn quốc gia về An ninh mạng – HTTT – Yêu cầu cơ bản" mà NĐ 331 Đ28, 29, 30 viện dẫn | Như NĐ 331; HTTT quan trọng về ANQG áp dụng như cấp độ 5 (mục 1) | gốc (PDF có lớp chữ, bản đăng lại trên cổng UBND xã thuộc Quảng Ngãi; chưa thấy bản trên cổng Bộ KH&CN) | [PDF](https://sontaythuong.quangngai.gov.vn/upload/2007044/20260908/TCVN%2014423%202026%20ANM%20HTTT.pdf) |
| L-BHVB-2025 + sửa 2025 | 64/2025/QH15, 87/2025/QH15 | Luật Ban hành VBQPPL; Luật sửa đổi | 64: 01/04/2025; 87: 01/07/2025 | Còn HL. **Luật 87 Đ1 k22 sửa Đ57 k2**: văn bản quy định chi tiết **hết HL** cùng văn bản được hướng dẫn, trừ khi được công bố tiếp tục HL | Dùng để xác định tình trạng NĐ 85/2016, NĐ 53/2022, TT 12/2022, TT 03/2017 | gốc (PDF Công báo có chữ) | [Luật 64 PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/2/44584/55716-1-2025603-60464-2025-qh15.pdf) · [Luật 87 PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45526/57608-1-2025955-95687-2025-qh15.pdf) |
| ND-85-2016 | 85/2016/NĐ-CP | Bảo đảm an toàn HTTT theo cấp độ | — | **Hết HL từ 01/07/2026 theo Luật 64 Đ57 k2 (sửa bởi Luật 87)**, trừ khi có văn bản công bố tiếp tục HL (chưa tìm thấy). Riêng NĐ 331 Đ39 k1 dẫn chiếu để thẩm định cấp độ cho HTTT đang đầu tư trước 01/07/2026, hạn 01/01/2027 | BV công, HTTT nhà nước (giai đoạn chuyển tiếp) | gốc-meta (qua dẫn chiếu trong NĐ 331, QĐ 326) | — |
| ND-53-2022 | 53/2022/NĐ-CP | Hướng dẫn Luật ANM 2018 (từng chứa nghĩa vụ lưu trữ dữ liệu trong nước) | — | Hết HL theo cùng lập luận; nội dung lưu trữ dữ liệu được NĐ 333 Đ19–20 quy định lại; NĐ 333 Đ31 giữ thủ tục cho hồ sơ đã nộp | — | gốc-meta (qua NĐ 333 Đ31) | — |
| TT-12-2022-BTTTT, TT-03-2017-BTTTT | 12/2022/TT-BTTTT; 03/2017/TT-BTTTT | Hướng dẫn NĐ 85 (hồ sơ cấp độ, yêu cầu theo cấp độ) | — | Hết HL theo cùng lập luận (văn bản được hướng dẫn hết HL). Nội dung hồ sơ nay ở NĐ 331 Đ21–22; yêu cầu kỹ thuật nay ở TCVN 14423:2026 | — | chưa XM (chỉ thấy qua dẫn chiếu trong QĐ 326 và CV 365) | — |
| QD-326-2024-BYT | 326/QĐ-BYT ngày 07/02/2024 | Quy chế bảo đảm ATTT, an ninh mạng của Bộ Y tế (thay QĐ 4159/QĐ-BYT/2014) | Từ ngày ký | Còn HL theo văn bản (chưa thấy văn bản thay); căn cứ ban hành là khung cũ (Luật ATTTM, NĐ 85, TT 12/2022). Phải đọc cùng NĐ 331 và TCVN 14423 | Đơn vị thuộc và trực thuộc BYT (gồm BV trực thuộc Bộ); tổ chức kết nối vào mạng của BYT; nhà cung cấp dịch vụ CNTT, ATTT cho các đơn vị này (Đ1 k2 Quy chế) | gốc-OCR | [PDF (cổng Viện Dược liệu)](http://vienduoclieu.org.vn/Portals/0/QD%20326%20cua%20BYT%20ve%20an%20ninh%20mang.pdf) |
| TT-13-2025-BYT (↔ K1) | 13/2025/TT-BYT | HSBA điện tử | 21/07/2025 | Còn HL | Mọi cơ sở KCB triển khai HSBA điện tử | gốc-OCR (Đ1 k4, Đ2, Đ4 k3) | [PDF sao y, SYT Quảng Ninh](https://soytequangninh.gov.vn/upload/1002610/20250610/THONG_TU_HSBA_DIEN_TU_21_7_2025TT_13_2025__TT-BYT_ngay_6_6_2025_f5604afb8f.pdf) |
| CV-365-2025-TTYQG (↔ K1) | 365/TTYQG-GPQLCL ngày 06/06/2025 | Hướng dẫn triển khai HSBA điện tử | 06/06/2025 | Còn áp dụng trên thực tế; dẫn toàn khung cũ (NĐ 85, TT 12/2022, TCVN 11930, QĐ 742/QĐ-BTTTT, TT 39/2017) | Cơ sở KCB làm HSBA điện tử | thứ cấp (nội dung được trích nguyên văn trong báo cáo TTYT Bạc Liêu, Phần III mục 1.2, 2, 4) | Mở được khi bỏ qua lỗi chứng chỉ SSL: [PDF Bạc Liêu](https://ttyttpbaclieu.gov.vn/upload/1000078/fck/files/2_2_1_Ph____l___c_b__o_c__o_____nh_gi___ph___m_m___m_theo_TT13_CV365_aa703.pdf) |
| CT-07-2026-BYT | 07/CT-BYT (đăng 15/09/2026) | Xử lý "điểm nghẽn" chuyển đổi số y tế | Ký | Còn HL | Theo bài báo: hệ thống ngành y tế; đối tượng cụ thể chưa rõ | thứ cấp | [daibieunhandan.vn, thứ cấp](https://daibieunhandan.vn/bo-y-te-7-nhom-nhiem-vu-day-manh-va-xu-ly-dut-diem-cac-diem-nghen-ve-chuyen-doi-so-y-te-thuc-day-trien-khai-de-an-06-10430624.html) |
| L-BVDLCN-2025 + ND-356-2025 (↔ K8) | 91/2025/QH15; 356/2025/NĐ-CP | Bảo vệ dữ liệu cá nhân | 01/01/2026 | Còn HL | Mọi bên xử lý dữ liệu sức khỏe | gốc (Luật 91 Đ2 k3, Đ26; NĐ 356 Đ4) | [Luật 91 PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf) · [NĐ 356 Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm) |
| TT-47-2026-BCA | 47/2026/TT-BCA (QCVN 12:2026/BCA) | QCVN an ninh mạng cho HTTT lưu trữ tài liệu điện tử trong cơ quan Đảng, Nhà nước | 01/07/2026 | Còn HL | Chỉ HTTT **lưu trữ tài liệu điện tử** (không chứa BMNN) của **cơ quan Đảng, Nhà nước** (QCVN mục 1.1–1.2). Không phải HIS/EMR; BV công là đơn vị sự nghiệp: áp dụng hay không chưa rõ | gốc-OCR (mục 1) | [VB 218069](https://vanban.chinhphu.vn/?pageid=27160&docid=218069) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/47-bca.pdf) |
| L-DAUTU-2025 | 143/2025/QH15, Phụ lục IV (sửa bởi Luật 24/2026/QH16, HL 01/03/2027 theo bài báo) | Danh mục ngành nghề kinh doanh có điều kiện: STT 100 KCB, 101 kinh doanh dược, 103 kinh doanh TBYT | — | Còn HL | Dùng để áp tiêu chí cấp độ 3 của NĐ 331 Đ13 k2 a | thứ cấp (cổng xaydungchinhsach.chinhphu.vn) | [xaydungchinhsach, thứ cấp](https://xaydungchinhsach.chinhphu.vn/danh-muc-nganh-nghe-dau-tu-kinh-doanh-co-dieu-kien-119260910153514547.htm) |
| QD-1875-2026-TTg | 1875/QĐ-TTg ngày 30/09/2026 | Khung kiến trúc an ninh mạng quốc gia phiên bản 1.0 (gắn với TCVN 14423:2026) | 30/09/2026 | Còn HL | Hệ thống chính trị; bối cảnh | thứ cấp | [vietq.vn, thứ cấp](https://vietq.vn/ban-hanh-khung-kien-truc-an-ninh-mang-quoc-gia-gan-yeu-cau-ky-thuat-voi-tcvn-144232026-d244498.html) |
| ND-329/332/327/328-2026 | 329, 332, 327, 328/2026/NĐ-CP | Lực lượng bảo vệ ANM; kinh doanh sản phẩm, dịch vụ ANM; xử lý thông tin xâm phạm ANQG; chống tin giả | 19/08/2026 | Còn HL | Ngoại vi. NĐ 332 liên quan nếu vendor bán dịch vụ ANM (SOC, pentest) | gốc-meta (tiêu đề trên Công báo) | [NĐ 332 Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-332-2026-nd-cp-470329.htm) |

Ghi chú: QĐ 425/QĐ-BYT/2025 (quy chế ANM hệ thống kê đơn) thuộc K3, cụm này không đọc lại. QĐ 742/QĐ-BTTTT/2022 (an toàn phần mềm nội bộ) chỉ thấy qua CV 365, tình trạng chưa xác minh; nội dung của nó trên thực tế được TCVN 14423:2026 mục 5.17 bao phủ cho cấp độ 3 trở lên.

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### Khung chung: hệ thống nào thuộc diện, cấp mấy

#### ANM-R01 — Xác định ranh giới HTTT và không "chia nhỏ để hạ cấp"
- **Căn cứ**: NĐ 331 Đ7 k1–2 (HTTT phải có chức năng nghiệp vụ rõ, có xử lý dữ liệu, có người dùng; ranh giới xác định theo chức năng, dòng dữ liệu, mức phụ thuộc vận hành, phạm vi ảnh hưởng khi sự cố, không theo cách tổ chức hành chính hay hạ tầng vật lý); Đ8 k1 a (mỗi HTTT chỉ có một chủ quản); Đ8 k2 (đáp ứng nhiều tiêu chí thì lấy cấp cao nhất); Đ8 k3 (cấm phân tách hoặc hợp nhất hình thức để hạ cấp).
- **Áp dụng cho**: chủ quản và đơn vị vận hành (BV, PK, vendor SaaS) · **Hiệu lực**: 19/08/2026.
- **Mức**: BẮT BUỘC (với HTTT thuộc phạm vi Đ2 NĐ 331; xem R03).
- **Phần mềm phải**: có tài liệu kiến trúc thể hiện ranh giới hệ thống (thành phần, luồng dữ liệu, phụ thuộc, kết nối ngoài như BHXH, Cổng BAĐT, đơn thuốc quốc gia, VNeID). Nếu HIS, EMR, LIS, PACS chung CSDL hoặc phụ thuộc nhau để vận hành thì về nguyên tắc là một HTTT và lấy cấp cao nhất của các thành phần.
- **Ghi chú / bẫy**: Không thể tách cổng người bệnh (cấp 3) khỏi HIS chỉ trên giấy để HIS ở cấp 2, nếu chúng dùng chung CSDL và phụ thuộc vận hành **(suy luận từ Đ7 k2, Đ8 k3)**.

#### ANM-R02 — Phân loại cấp độ theo tiêu chí NĐ 331 Đ11–15
- **Căn cứ**: Luật 116 Đ8 k1 (5 cấp theo mức tổn hại); NĐ 331 Đ9 (loại thông tin: công cộng, riêng, cá nhân, BMNN; loại HTTT: nội bộ, phục vụ người dân/doanh nghiệp, hạ tầng thông tin, điều khiển công nghiệp, khác). Đ9 k2 b nêu đích danh **y tế** trong nhóm "dịch vụ trực tuyến khác".
  - Đ11: cấp 1 = nội bộ, chỉ xử lý thông tin công cộng.
  - Đ12: cấp 2 = (k1) nội bộ có xử lý thông tin riêng, thông tin cá nhân; (k2 a) dịch vụ trực tuyến **không** thuộc ngành nghề kinh doanh có điều kiện; (k2 b) dịch vụ trực tuyến xử lý dữ liệu của **dưới 100.000** chủ thể (DLCN cơ bản) hoặc **dưới 10.000** chủ thể (DLCN nhạy cảm); (k3) hạ tầng thông tin của một cơ quan, tổ chức.
  - Đ13: cấp 3 = (k2 a) dịch vụ trực tuyến **thuộc danh mục ngành nghề đầu tư kinh doanh có điều kiện**; (k2 b) HTTT giải quyết TTHC; (k2 c) dịch vụ trực tuyến xử lý dữ liệu **từ 100.000** chủ thể (cơ bản) **hoặc từ 10.000** chủ thể (nhạy cảm) trở lên; (k3) hạ tầng thông tin phục vụ cơ quan, tổ chức trong một bộ, ngành, một hoặc vài tỉnh.
  - Đ14: cấp 4 = (k2) HTTT quốc gia phục vụ Chính phủ điện tử hoặc hạ tầng thông tin toàn quốc, yêu cầu vận hành 24/7.
  - Đ15–16: cấp 5 và HTTT quan trọng về ANQG (Luật 116 Đ9 k2 g có liệt kê "HTTT quốc gia thuộc lĩnh vực ... y tế").
  - Dữ liệu sức khỏe là DLCN nhạy cảm: Luật 91/2025 Đ2 k3 + NĐ 356/2025 Đ4 k1 d ("Tình trạng sức khỏe"). KCB (STT 100), kinh doanh dược (STT 101), kinh doanh TBYT (STT 103) thuộc Phụ lục IV Luật Đầu tư 143/2025 (thứ cấp).
- **Áp dụng cho**: mọi chủ quản thuộc phạm vi · **Hiệu lực**: 19/08/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (a) đếm được số **chủ thể dữ liệu duy nhất** có dữ liệu sức khỏe mà dịch vụ trực tuyến xử lý (người bệnh distinct, không phải số lượt khám); (b) gắn nhãn loại thông tin cho từng bảng hoặc trường (công cộng / riêng / cá nhân cơ bản / cá nhân nhạy cảm) để làm thuyết minh cấp độ (NĐ 331 Đ22 k4 b yêu cầu nêu loại thông tin được xử lý).
- **Ghi chú / bẫy** — **kiểm lại câu "≥10.000 người bệnh là cấp 3"**: đúng **một phần**. Ngưỡng 10.000 chỉ nằm trong nhánh **dịch vụ trực tuyến phục vụ người dân, doanh nghiệp** (Đ12 k2 b / Đ13 k2 c) và tính theo **chủ thể dữ liệu nhạy cảm**. HIS nội bộ (chỉ nhân viên dùng) rơi vào Đ12 k1 (cấp 2) **bất kể quy mô**, trừ khi đánh giá rủi ro đẩy lên (Đ10 k5). Ngược lại, dịch vụ trực tuyến thuộc ngành nghề có điều kiện là cấp 3 **dù chỉ có 1 người dùng** (Đ13 k2 a).
- **Bảng áp dụng cho hệ thống y tế (suy luận, chưa có hướng dẫn của BCA hay BYT)**:

| Hệ thống | Loại theo Đ9 k2 | Cấp tối thiểu đề xuất | Lý do |
|---|---|---|---|
| HIS/EMR/LIS/RIS-PACS chỉ dùng nội bộ BV, PK | a (nội bộ) | **2** (Đ12 k1) | Có thông tin cá nhân; không có ngưỡng quy mô ở nhánh nội bộ. Đánh giá rủi ro có thể nâng lên 3 (Đ10 k5) |
| Cổng hoặc app người bệnh (đặt lịch, xem kết quả, HSBA, thanh toán viện phí) | b (dịch vụ trực tuyến, y tế) | **3** nếu ≥10.000 người bệnh có dữ liệu sức khỏe trong hệ thống; nếu dưới ngưỡng thì 2, trừ khi bị coi là "dịch vụ KCB trực tuyến" | Đ13 k2 c; Đ13 k2 a chưa chắc áp được cho app chỉ đặt lịch hay xem kết quả |
| Nền tảng KCB từ xa, tư vấn bác sĩ trực tuyến | b | **3** | Dịch vụ KCB là ngành nghề có điều kiện (STT 100) → Đ13 k2 a |
| Nhà thuốc hoặc sàn bán thuốc trực tuyến | b | **3** | Kinh doanh dược (STT 101) → Đ13 k2 a |
| SaaS HIS/EMR đa khách hàng do vendor vận hành (vendor là chủ quản nền tảng) | b (NĐ 331 Đ3 k5: dịch vụ trực tuyến gồm dịch vụ do DN cung cấp cho tổ chức) | **3** khi tổng người bệnh trên mọi tenant ≥10.000 | Đ13 k2 c; ngưỡng tính trên toàn hệ thống, không theo từng tenant |
| Nền tảng dữ liệu y tế của Sở Y tế phục vụ nhiều cơ sở trong tỉnh | c (hạ tầng thông tin) | **3** | Đ13 k3 |
| Hệ thống quốc gia của BYT (đơn thuốc quốc gia, Sổ SKĐT, CSDLQG y tế) | c hoặc b, phạm vi toàn quốc | **4** (ứng viên) | Đ14 k2 nếu yêu cầu 24/7; có thể vào danh mục ANQG (Luật 116 Đ9 k2 g) |

#### ANM-R03 — Phạm vi áp dụng NĐ 331 (ai bị bắt buộc)
- **Căn cứ**: NĐ 331 Đ2: áp dụng với HTTT "phục vụ ứng dụng CNTT trong hoạt động của cơ quan, tổ chức nhà nước, ứng dụng CNTT trong việc cung cấp dịch vụ trực tuyến phục vụ người dân và doanh nghiệp"; tổ chức khác được "khuyến khích". Luật 116 Đ1 k2 và Đ10 k1 a (xác định cấp độ là nhiệm vụ với HTTT nói chung).
- **Áp dụng cho**: BV công: thuộc diện **(suy luận: hoạt động của đơn vị sự nghiệp công lập là "tổ chức nhà nước")**. BV tư, PK tư: **chỉ** thuộc diện bắt buộc của NĐ 331 với hệ thống cung cấp dịch vụ trực tuyến (cổng, app, KCB từ xa). HIS nội bộ của tư nhân: Luật 116 vẫn yêu cầu xác định cấp độ, còn NĐ 331 chỉ "khuyến khích" → chưa rõ.
- **Mức**: BẮT BUỘC? 
- **Phần mềm phải**: vendor bán cho BV tư nên mặc định đáp ứng tối thiểu cấp 2 TCVN 14423, và cấp 3 cho module trực tuyến của người bệnh.
- **Ghi chú / bẫy**: NĐ 330 Đ24 k1 phạt hành vi "không lập hồ sơ đề xuất cấp độ ... theo quy định". Chữ "theo quy định" đưa ngược về phạm vi Đ2 NĐ 331, nên cần luật sư xác nhận cho BV tư (mục 7).

#### ANM-R04 — Hồ sơ đề xuất cấp độ, thẩm định và phê duyệt
- **Căn cứ**: NĐ 331 Đ18 (thẩm quyền), Đ19 (dự án mới, thuê dịch vụ), Đ20 (HTTT đang vận hành), Đ21 (thành phần hồ sơ), Đ22 (thuyết minh), Đ23 (thẩm định: phản hồi hồ sơ chưa hợp lệ ≤05 ngày làm việc; cấp 3 ≤15 ngày làm việc; cấp 4, 5 ≤25 ngày làm việc), Đ24 (phê duyệt ≤07 ngày làm việc), Đ25 (xác định lại thì làm như lần đầu), Đ37 (khuyến khích phê duyệt trước khi duyệt dự án), Phụ lục Mẫu 01–05.
  - **Cấp 1–2**: đơn vị chuyên trách ANM của chủ quản thẩm định và phê duyệt, báo cáo chủ quản (Đ18 k1).
  - **Cấp 3**: đơn vị chuyên trách ANM của chủ quản thẩm định, **chủ quản phê duyệt** (Đ18 k2). **Không** phải gửi Bộ Công an.
  - **Cấp 4–5**: Bộ Công an chủ trì thẩm định; chủ quản phê duyệt cấp 4; Thủ tướng phê duyệt danh mục cấp 5 (Đ18 k3).
  - Nếu đơn vị chuyên trách đồng thời vận hành hệ thống thì phải giao đơn vị khác thẩm định hoặc lập hội đồng độc lập (Đ18 k4).
- **Áp dụng cho**: chủ quản; vendor phối hợp (Đ19 k2 b) · **Hiệu lực**: 19/08/2026; chuyển tiếp xem R05.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải** (vendor cung cấp được): tài liệu thuyết minh theo Đ22 k3 d gồm mô hình logic và vật lý; danh mục thiết bị và thiết bị mạng (tên/chủng loại, vị trí, mục đích); danh mục ứng dụng/dịch vụ (máy chủ, vị trí, hệ điều hành, mục đích); **quy hoạch vùng mạng và địa chỉ IP private/public**; danh mục loại thông tin xử lý; nhận diện rủi ro sơ bộ; thuyết minh phương án ANM theo từng yêu cầu của cấp độ.
- **Ghi chú / bẫy**: NĐ 330 Đ23 k1 c: **đưa HTTT cấp 3–5 vào vận hành khi chưa được phê duyệt cấp độ** bị phạt 20–30 triệu (cá nhân; tổ chức ×2 theo Đ7 k1, tức 40–60 triệu). Đ30 k6 NĐ 331: hệ thống mới hoặc nâng cấp phải triển khai đủ phương án đã duyệt **trước** khi vận hành.

#### ANM-R05 — Chuyển tiếp: hệ thống đã có cấp độ, đang đầu tư, đang vận hành
- **Căn cứ**: Luật 116 Đ45 k1 (HTTT đã xác định cấp độ theo Luật ATTTM **giữ cấp độ**; trong 12 tháng kể từ 01/07/2026 phải đáp ứng điều kiện, tiêu chuẩn, biện pháp theo luật mới → **01/07/2027**); Đ45 k3 (sản phẩm, giải pháp ATTT đã đưa vào dùng tiếp tục được dùng, 12 tháng phải đáp ứng điều kiện mới → 01/07/2027). NĐ 331 Đ39 k1 (HTTT **đang đầu tư, xây dựng trước 01/07/2026**: hoàn thành thẩm định, phê duyệt cấp độ **theo NĐ 85/2016** trong 6 tháng → **01/01/2027**; trong 12 tháng → **01/07/2027** phải đáp ứng biện pháp theo NĐ 331). NĐ 331 Đ39 k2 (TCVN, QCVN dùng "an toàn thông tin mạng" hay "an toàn HTTT" được hiểu tương đương "an ninh mạng").
- **Áp dụng cho**: chủ quản · **Hạn chót**: 01/01/2027; 01/07/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: lập gap analysis giữa phương án cũ (TCVN 11930:2017) và TCVN 14423:2026 theo cấp đã duyệt; có roadmap nâng cấp xong trước 01/07/2027.
- **Ghi chú / bẫy**: (1) HTTT **đang vận hành mà chưa từng được phê duyệt cấp độ** không có điều chuyển tiếp riêng, nên phải làm ngay theo NĐ 331 Đ20 **(suy luận)**. (2) Bài trên cổng Bộ Công an diễn giải là "hệ thống vận hành trước 01/07/2026"; câu chữ gốc Đ39 k1 là "**đang trong quá trình đầu tư, xây dựng**". Bám câu chữ gốc. (3) "Cấp 2 cũ" (NĐ 85) và "cấp 2 mới" (NĐ 331) dùng tiêu chí khác nhau; Luật 116 Đ45 k1 cho giữ con số cấp, nhưng nội dung yêu cầu phải theo TCVN 14423:2026.

#### ANM-R06 — Đánh giá rủi ro an ninh mạng và đánh giá lại khi vượt ngưỡng
- **Căn cứ**: NĐ 331 Đ10 k2 (bắt buộc đánh giá rủi ro khi: xác định cấp lần đầu; thay đổi chức năng, phạm vi phục vụ, đối tượng sử dụng, loại thông tin, công nghệ; **mở rộng quy mô, tích hợp, kết nối liên thông hoặc chia sẻ dữ liệu**; sự cố nghiêm trọng; có yêu cầu); Đ10 k3 (nội dung tối thiểu a–g); Đ10 k5 (rủi ro cao hơn cấp đã duyệt thì phải đề xuất cấp cao hơn); Đ10 k6 (lưu hồ sơ đánh giá rủi ro); Đ10 k8 (theo quy định của Bộ trưởng BCA, là "Khung quản lý rủi ro ANM", chưa tìm thấy văn bản); Luật 116 Đ10 k1 b.
- **Áp dụng cho**: chủ quản · **Hiệu lực**: 19/08/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (a) có bộ đếm chủ thể dữ liệu (R02) và **cảnh báo** khi tiến gần ngưỡng 10.000 nhạy cảm / 100.000 cơ bản để kích hoạt đánh giá lại; (b) nhật ký thay đổi kết nối liên thông (thêm API đối tác, kết nối BHXH, VNeID, bảo hiểm tư) để làm trigger Đ10 k2 c; (c) danh mục tài sản có xếp hạng quan trọng (Đ10 k3 a).

#### ANM-R07 — Quy chế bảo đảm ANM và phương án ANM
- **Căn cứ**: NĐ 331 Đ28 k1 (ban hành quy định ANM trong thiết kế, xây dựng, vận hành, nâng cấp, hủy bỏ); Đ29 k2 (phương án gồm: an ninh trong thiết kế, vận hành, kiểm tra đánh giá, quản lý rủi ro, giám sát, **dự phòng, ứng phó sự cố, khôi phục sau thảm họa**, kết thúc và hủy bỏ); Đ30 k3–4 (yêu cầu quản lý a–g; yêu cầu kỹ thuật: an toàn mạng, máy chủ, **ứng dụng**, **dữ liệu**); **Đ30 k7 (Quy chế phải được phê duyệt, ban hành TRƯỚC khi hồ sơ cấp độ được phê duyệt)**; NĐ 330 Đ23 k1 a (không ban hành quy định: phạt 20–30 triệu, tổ chức ×2).
- **Áp dụng cho**: chủ quản · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: vendor kèm "bộ tài liệu vận hành an toàn" (cấu hình hardening, ma trận phân quyền mẫu, quy trình backup/restore, quy trình xử lý sự cố, quy trình hủy dữ liệu) để khách hàng đưa vào Quy chế.

#### ANM-R08 — Áp dụng yêu cầu cơ bản theo TCVN 14423:2026
- **Căn cứ**: NĐ 331 Đ28 k1, k4; Đ29 k1; Đ30 k1–2 (yêu cầu cơ bản theo Nghị định **và** "Tiêu chuẩn quốc gia về An ninh mạng – HTTT – Yêu cầu cơ bản" là **tối thiểu**; không gồm an ninh vật lý). TCVN 14423:2026 chia 15 nhóm cho cấp 1 và 2 (mục 3, 4); cấp 3 thêm 5.13 Giám sát và phòng thủ, 5.17 Phát triển ứng dụng an toàn, 5.18 Quản lý kiểm tra ANM; cấp 4, 5 ở mục 6, 7.
- **Áp dụng cho**: HTTT thuộc phạm vi NĐ 331 · **Hạn**: hệ thống mới thì trước khi vận hành; hệ thống cũ thì 01/07/2027.
- **Mức**: BẮT BUỘC? (TCVN tự thân là tự nguyện; ở đây trở thành căn cứ bắt buộc vì được NĐ 331 viện dẫn. Luật 116 Đ10 k3 lại cho cấp 1–2 "theo nhu cầu, khả năng" chọn biện pháp ở k2, nên có độ vênh, xem mục 6.)
- **Phần mềm phải**: xem R09–R20 (đã tách theo nhóm có tác động trực tiếp tới phần mềm).

### Yêu cầu kỹ thuật tác động trực tiếp tới phần mềm

#### ANM-R09 — Quản lý tài khoản và phân quyền
- **Căn cứ**: TCVN 14423:2026 mục 4.6 / 5.6 (cấp 2 / cấp 3): phân loại tài khoản **quản trị / tác nghiệp / kỹ thuật (kết nối hệ thống) / dịch vụ (người thụ hưởng)**; danh sách tài khoản có loại, tên, trạng thái, hệ thống, người quản lý, phòng ban, ngày kích hoạt và vô hiệu hóa, **rà soát ≥1 lần/6 tháng**; mỗi tài khoản gắn một người (dùng chung phải được phê duyệt và truy được trách nhiệm từng thời điểm); **vô hiệu hóa tài khoản không hoạt động sau 45 ngày** hoặc ngay khi đổi nhân sự; đổi hoặc vô hiệu tài khoản mặc định; cấp quyền tối thiểu, phân tách nhiệm vụ; danh sách quyền theo chức danh. Mục 5.4.2.1 d: rà soát cấp độ phân quyền dữ liệu ≥1 lần/6 tháng (cấp 3). NĐ 356/2025 Đ4 k2: xử lý DLCN nhạy cảm phải có **quy định phân quyền giới hạn truy cập**. NĐ 330 Đ62 k1 b: ứng dụng y tế, nền tảng chăm sóc sức khỏe trực tuyến thu thập DLCN nhạy cảm mà không phân quyền giới hạn truy cập bị phạt **50–70 triệu** (tổ chức). QĐ 326/QĐ-BYT Đ8 (gốc-OCR): khóa, thu hồi tài khoản khi chuyển công tác; hạn chế dùng chung tài khoản quản trị.
- **Áp dụng cho**: mọi HIS/EMR/app · **Mức**: BẮT BUỘC (phân quyền với dữ liệu sức khỏe theo NĐ 356 Đ4 k2) / BẮT BUỘC? (các con số 45 ngày, 6 tháng theo TCVN, xem R08).
- **Phần mềm phải**: (a) trường `account_type` ∈ {admin, operator, technical, service}; (b) job tự động vô hiệu hóa tài khoản không đăng nhập >45 ngày (cấu hình được); (c) báo cáo "access review" xuất được theo kỳ 6 tháng; (d) RBAC theo chức danh/khoa, tách quyền quản trị hệ thống khỏi quyền xem dữ liệu bệnh nhân; (e) không có tài khoản mặc định khi bàn giao; (f) tài khoản kỹ thuật (API) tách khỏi tài khoản người.

#### ANM-R10 — Xác thực: MFA và chính sách mật khẩu
- **Căn cứ**: TCVN 14423:2026 mục 3.6/4.6/5.6: **MFA bắt buộc với truy cập từ bên ngoài tổ chức, từ đối tác/bên thứ ba, từ Internet, và với tài khoản quản trị** (có từ cấp 1). Mật khẩu: có MFA thì ≥08 ký tự; không MFA thì **≥14 ký tự** gồm thường, hoa, đặc biệt, số; đổi mật khẩu mặc định; đổi ở lần đăng nhập đầu. Cấp 3: tài khoản quản trị dùng MFA, đổi mật khẩu ≥1 lần/2 tháng, không trùng 10 mật khẩu trước. Mục 4.4.2.4 / 3.4.2.4: mã hóa thông tin xác thực khi lưu. QĐ 326 Đ8 (gốc-OCR): giới hạn số lần đăng nhập sai liên tiếp; giới hạn thời gian chờ đóng phiên; mã hóa thông tin xác thực; không khuyến khích đăng nhập tự động; mật khẩu ≥8 ký tự có độ phức tạp, đổi ≥6 tháng/lần. Luật 116 Đ42 k2 (người dùng tự bảo mật tài khoản số). NĐ 356 Đ4 k1 i: tên đăng nhập và mật khẩu tài khoản định danh điện tử là DLCN nhạy cảm.
- **Áp dụng cho**: mọi hệ thống; đặc biệt HIS truy cập từ xa, cổng bệnh nhân, tài khoản vendor hỗ trợ từ xa · **Mức**: BẮT BUỘC? (qua TCVN được NĐ 331 viện dẫn; QĐ 326 bắt buộc với đơn vị thuộc BYT).
- **Phần mềm phải**: MFA (TOTP, OTP, VNeID, chữ ký số) cho mọi truy cập từ Internet và mọi tài khoản admin; policy mật khẩu cấu hình được (độ dài, lịch sử 10, hết hạn); lockout sau N lần sai; session timeout; hash mật khẩu bằng thuật toán chuyên dụng (argon2id hoặc bcrypt); kênh hỗ trợ từ xa của vendor qua VPN/SSH/TLS (QĐ 326).
- **Ghi chú / bẫy**: QĐ 326 (≥8 ký tự) **thấp hơn** TCVN 14423 (≥14 ký tự nếu không có MFA). Đơn vị BYT phải đáp ứng cả hai, nên lấy mức chặt hơn.

#### ANM-R11 — Nhật ký: nội dung, đồng bộ thời gian, thời hạn lưu
- **Căn cứ**:
  - Luật 116 Đ2 k11 (định nghĩa nhật ký hệ thống: thời gian, người dùng, hoạt động, trạng thái); Đ25 k2 b, d (DN cung cấp dịch vụ trên mạng: lưu nhật ký và thông tin tài khoản, thời gian sử dụng, thanh toán, **IP truy cập**).
  - NĐ 333 Đ16 k6 (DN cung cấp dịch vụ trên mạng: nhật ký tối thiểu gồm tài khoản, **thời gian đăng nhập/đăng xuất, địa chỉ IP, cổng nguồn**, nhật ký xử lý thông tin được đăng tải; truy xuất được **≥12 tháng**); Đ20 k3 (nhật ký phục vụ điều tra lưu **≥12 tháng**).
  - NĐ 330 Đ34 k1 c (không lưu **thông tin thiết bị, IP, thời gian đăng nhập của tài khoản số ≥90 ngày**: phạt 20–30 triệu, tổ chức ×2); Đ23 k2 a (không lưu nhật ký theo quy định: 30–50 triệu, tổ chức ×2); Đ33 k1 c (không bảo đảm thời gian lưu nhật ký phục vụ điều tra: 30–50 triệu, tổ chức ×2); Đ21 k4 h (không lưu, không cung cấp log liên quan IP, máy chủ, DNS: 50–70 triệu, tổ chức ×2).
  - TCVN 14423:2026 mục 4.8 (cấp 2): thu nhật ký truy cập hệ thống, nhật ký ứng dụng, cảnh báo thiết bị bảo mật; trường tối thiểu của nhật ký truy cập là địa chỉ nguồn, đích, tài khoản đích, thời điểm, hành vi; đồng bộ máy chủ thời gian; **dung lượng lưu ≥01 tháng**; rà soát ≥1 lần/năm. Mục 5.8 (cấp 3): thêm nhật ký tiến trình (process, tiến trình cha, lệnh khởi tạo) và MAC; **SIEM hoặc tương đương**; lưu tập trung; **≥03 tháng**; rà soát ≥1 lần/6 tháng. Cấp 4: ≥06 tháng; cấp 5: ≥12 tháng.
  - QĐ 326/QĐ-BYT Đ7 e, Đ8 (gốc-OCR): máy chủ lưu nhật ký hệ thống **≥06 tháng**; phần mềm, ứng dụng lưu nhật ký **≥03 tháng** (thời gian, địa chỉ, tài khoản, nội dung truy nhập và sử dụng, lỗi phát sinh, thông tin đăng nhập quản trị).
- **Áp dụng cho**: mọi HTTT y tế; con số 12 tháng của NĐ 333 áp cho DN cung cấp dịch vụ trên mạng (phạm vi với SaaS y tế, xem mục 7) · **Mức**: BẮT BUỘC (nghĩa vụ lưu nhật ký: Luật 116 Đ25, NĐ 330 Đ34 k1 c) / BẮT BUỘC? (con số cụ thể theo từng loại chủ thể).
- **Phần mềm phải**: (a) audit log ở tầng ứng dụng ghi `ts (UTC, NTP), account_id, account_type, src_ip, src_port, user_agent/device_id, action, object_type, object_id (patient_id/encounter_id), result, reason`; (b) ghi riêng đăng nhập/đăng xuất (IP, cổng nguồn, thiết bị); (c) **lưu tối thiểu 12 tháng** để phủ mọi mức (90 ngày, 3, 6, 12 tháng) **(khuyến nghị)**; (d) chống sửa và xóa (append-only, WORM hoặc hash-chain); (e) xuất sang SIEM (syslog, CEF hoặc JSON); (f) cảnh báo khi kho log sắp đầy (TCVN 5.8).
- **Ghi chú / bẫy**: Chưa có văn bản y tế nào quy định riêng thời hạn lưu **log truy cập HSBA** (khoảng trống #19 của inventory). Phải tách: log an ninh (12 tháng theo khung ANM) và vết sửa HSBA (đi theo HSBA, thời hạn lưu HSBA thuộc K1).

#### ANM-R12 — Mã hóa và toàn vẹn dữ liệu
- **Căn cứ**: TCVN 14423:2026 mục 4.4.2.4 (cấp 2: mã hóa thông tin xác thực và dữ liệu không công khai khi lưu); 5.4.2.4 (cấp 3: mã hóa hoặc biện pháp tương đương khi **lưu** và khi **truyền**, quản lý vòng đời khóa); 5.4.2.5 (lưu dữ liệu quan trọng kèm **mã kiểm tra toàn vẹn**); 5.4.2.7 (tách môi trường xử lý dữ liệu nhạy cảm cao); 5.4.2.8 (dùng **chữ ký số** khi trao đổi dữ liệu nhạy cảm cao). NĐ 330 Đ69 k2 b (cung cấp hoặc **sử dụng** dịch vụ điện toán đám mây mà không mã hóa DLCN khi lưu và khi truyền: **50–70 triệu**, tổ chức); Đ69 k2 c (không xác thực và phân quyền nghiêm ngặt trên cloud). CV 365 Phần III 1.2 a–b (thứ cấp): có khả năng mã hóa dữ liệu lưu trữ; mã hóa, giải mã thông tin người bệnh khi truyền nhận. QĐ 326 Đ8 (gốc-OCR): chỉ dùng giao thức có mã hóa (SSH, SSL, VPN) khi quản trị từ xa; mã hóa dữ liệu trên thiết bị lưu trữ di động.
- **Áp dụng cho**: mọi hệ thống; bắt buộc rõ nhất khi chạy trên cloud · **Mức**: BẮT BUỘC (mã hóa lưu và truyền với DLCN trên cloud: NĐ 330 Đ69) / BẮT BUỘC? (phần còn lại qua TCVN).
- **Phần mềm phải**: TLS cho mọi kết nối (kể cả nội bộ và kết nối máy xét nghiệm hoặc PACS nếu khả thi); mã hóa CSDL hoặc ổ đĩa và bản sao lưu; mã hóa mức trường cho dữ liệu đặc biệt nhạy cảm (HIV, tâm thần, di truyền); quản lý khóa qua KMS hoặc HSM, xoay khóa; hash hoặc chữ ký số cho bản ghi xuất ra (XML/JSON gửi BHXH, Cổng BAĐT).

#### ANM-R13 — Sao lưu và khôi phục
- **Căn cứ**:
  - Luật 116 Đ10 k2 đ ("tổ chức triển khai các biện pháp lưu trữ, sao lưu"), bắt buộc với cấp 3–4 theo Đ10 k4; với cấp 1–2 là "theo nhu cầu" (Đ10 k3).
  - NĐ 331 Đ28 k1 (sao lưu theo TCVN), Đ29 k2 e (phương án phải có **khôi phục sau thảm họa**).
  - TCVN 14423:2026 mục 4.11 (cấp 2): quy định sao lưu gồm file cấu hình, bản dự phòng HĐH máy chủ, CSDL, dữ liệu nghiệp vụ, tần suất và phương pháp cho từng loại; **định kỳ khôi phục thử**; bảo vệ toàn vẹn bản sao lưu; **hạ tầng sao lưu tách biệt với môi trường vận hành**. Mục 5.11 (cấp 3): thêm **sao lưu tự động**, **quy tắc 3-2-1** hoặc tương đương, **mã hóa** bản sao lưu dữ liệu quan trọng, lưu trữ tập trung.
  - TT 13/2025/TT-BYT Đ2 k1 (hạ tầng HSBA phải có giải pháp, thiết bị lưu trữ **bao gồm cả lưu trữ dự phòng**); Đ2 k4 (**sẵn sàng phục hồi** thông tin, dữ liệu và khả năng truy xuất HSBA); Đ4 k3 b (quy chế quản lý, lưu trữ và **an toàn thông tin** HSBA) — gốc-OCR.
  - CV 365 Phần III mục 2 c (thứ cấp): **định kỳ sao lưu 01 bản tại cơ sở KCB**, khuyến nghị thêm 01 bản tại đơn vị cung cấp dịch vụ lưu trữ để phòng khi bị tấn công mạng.
  - QĐ 326 Đ8 (gốc-OCR): hệ thống lưu trữ độc lập với máy chủ dịch vụ để sao lưu dự phòng các loại dữ liệu như trên.
  - NĐ 330 Đ21 k4 đ (không phối hợp khôi phục dữ liệu, kết nối cần thiết khi sự cố: phạt 50–70 triệu, tổ chức ×2).
- **Áp dụng cho**: mọi cơ sở KCB có HSBA điện tử (TT 13); mọi HTTT cấp 3+ (Luật 116) · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: sao lưu tự động (CSDL, file đính kèm/DICOM, cấu hình), mã hóa, bất biến (immutable hoặc offline), ít nhất 1 bản **tại cơ sở KCB** khi chạy cloud (CV 365) hoặc 1 bản **ngoài** cơ sở khi chạy on-prem; công cụ khôi phục có ghi biên bản thử khôi phục định kỳ; RPO/RTO được công bố trong tài liệu.

#### ANM-R14 — Phát triển ứng dụng an toàn, quản lý lỗ hổng, kiểm thử xâm nhập
- **Căn cứ**: TCVN 14423:2026 mục 5.17 (cấp 3+): quy trình phát triển an toàn; **phần mềm thuê khoán phải có cam kết bảo mật, nhà phát triển cung cấp mã nguồn, nếu không thì cung cấp chứng chỉ đánh giá an toàn độc lập hoặc kiểm thử xâm nhập và cam kết chịu trách nhiệm pháp lý**; kênh tiếp nhận báo cáo lỗ hổng từ bên ngoài; kiểm tra dữ liệu vào và ra; chống tấn công phổ biến; kiểm soát thông báo lỗi; **không lưu thông tin xác thực trong mã nguồn**; kiểm tra lỗ hổng mã nguồn và thư viện bên thứ ba trước khi vận hành. Mục 5.7: quét lỗ hổng ≥1 lần/6 tháng; quản lý bản vá; vá máy người dùng ≥1 lần/tháng. Mục 5.18: chương trình kiểm thử xâm nhập (quý, nửa năm, năm hoặc đột xuất). NĐ 331 Đ27 k3 c (đánh giá **an toàn mã nguồn đối với phần mềm nội bộ**), Đ27 k4 (black, gray, white box), Đ31 k2 c (tự đánh giá phải do bộ phận **độc lập với đơn vị vận hành**; trường hợp bắt buộc thuê tổ chức chuyên môn: cấp 5, sau sự cố nghiêm trọng, thay đổi lớn, nghi ngờ tự đánh giá). Luật 116 Đ15 k2 a (chủ quản kiểm tra để khắc phục điểm yếu, lỗ hổng). NĐ 330 Đ27 k1 c (không khắc phục lỗ hổng theo yêu cầu của lực lượng chuyên trách: 25–50 triệu, tổ chức ×2). CV 365 Phần III 1.2 b (thứ cấp): phần mềm HSBA đáp ứng yêu cầu an toàn trước khi sử dụng theo QĐ 742/QĐ-BTTTT.
- **Áp dụng cho**: vendor phần mềm và chủ quản; mức đầy đủ từ cấp 3 · **Mức**: BẮT BUỘC? (qua TCVN); NÊN với cấp 2.
- **Phần mềm phải**: pipeline SAST, SCA, secret scanning, DAST trước mỗi release; SBOM; quy trình patch; `security.txt` hoặc kênh báo lỗ hổng; báo cáo pentest độc lập hoặc ký quỹ mã nguồn để trao cho khách hàng cấp 3.

#### ANM-R15 — Giám sát ANM và kết nối trung tâm giám sát
- **Căn cứ**: Luật 116 Đ40 k1 b (chủ quản HTTT **kết nối hệ thống giám sát ANM, hệ thống phòng chống mã độc tập trung về Trung tâm ANM quốc gia (BCA) hoặc Trung tâm ANM của tỉnh**); NĐ 333 Đ7 k2 (chủ quản tổ chức giám sát, duy trì hệ thống giám sát và phòng chống mã độc tập trung **đáp ứng yêu cầu kết nối, chia sẻ dữ liệu cảnh báo** với cơ quan có thẩm quyền), Đ7 k6 (phối hợp, cung cấp cấu hình khi được yêu cầu); NĐ 331 Đ33 k5 (đơn vị vận hành thiết lập kết nối, đấu nối kỹ thuật phục vụ giám sát), Đ34 k1 e (BCA triển khai hạ tầng giám sát tập trung cho HTTT **cấp 3, 4, 5**); TCVN 14423:2026 mục 5.13 (cấp 3); Luật 116 Đ17 k1 (chủ động phòng chống mã độc), Đ17 k3 (DN cung cấp dịch vụ thư điện tử, truyền đưa, lưu trữ thông tin phải có **hệ thống lọc mã độc**). NĐ 330 Đ23 k2 d (cản trở trao đổi dữ liệu giám sát giữa đơn vị được thuê và lực lượng chuyên trách: 30–50 triệu, tổ chức ×2); Đ22 (mã độc).
- **Áp dụng cho**: chủ quản HTTT; ưu tiên cấp 3+ · **Mức**: BẮT BUỘC? (Luật nói "chủ quản HTTT" chung; cơ chế kết nối và đầu mối cụ thể do BCA hướng dẫn, chưa tìm thấy).
- **Phần mềm phải**: xuất log và cảnh báo theo chuẩn mở (syslog, CEF hoặc JSON) để đẩy về SOC; cho phép lắp agent EDR/giám sát trên máy chủ; với cổng có upload file (ảnh, kết quả xét nghiệm từ người bệnh) thì quét mã độc file tải lên **(suy luận từ Đ17 k3)**.

#### ANM-R16 — Ứng phó và báo cáo sự cố: thời hạn 24h / 72h / ngay lập tức
- **Căn cứ**: Luật 116 Đ40 k1 c (chủ quản báo cáo sự cố với cơ quan chuyên trách BCA hoặc BQP); Đ41 k3 (DN cung cấp dịch vụ trên không gian mạng: khi có sự cố thì **ngay lập tức** triển khai phương án ứng cứu và **báo cáo ngay**); Đ12 k3 (phát hiện hành vi vi phạm pháp luật về ANM thì thông báo lực lượng chuyên trách BCA). **NĐ 331 Đ31 k2 d**: báo cáo nguyên nhân, phạm vi ảnh hưởng, biện pháp khắc phục **trong 72 giờ kể từ khi phát hiện**; sự cố phức tạp thì gửi sơ bộ, sau đó gửi báo cáo cập nhật và báo cáo kết thúc; **sự cố nghiêm trọng phải thông báo ban đầu trong 24 giờ**; sự cố có dấu hiệu xâm phạm ANQG, TTATXH hoặc gây **gián đoạn nghiêm trọng** HTTT thì **báo cáo ngay khi phát hiện**. NĐ 333 Đ9 (quy trình ứng phó cho HTTT quan trọng về ANQG; chủ quản có phương án, thông báo ngay khi vượt khả năng). TCVN 14423:2026 mục 4.15/5.16 (đầu mối chính và dự phòng; quy trình nội bộ; phân nhóm sự cố; diễn tập). NĐ 330 Đ21 k2 a (không báo cáo khi phát hiện sự cố: 20–30 triệu), k3 c (không báo cáo đúng quy trình: 30–50 triệu), k3 d (không có kế hoạch ứng phó: 30–50 triệu), k1 b (không khai báo đầu mối ứng cứu: 10–20 triệu); đây là mức cá nhân, tổ chức ×2. QĐ 326 Đ13: TT Thông tin y tế QG là đơn vị chuyên trách ứng cứu sự cố của BYT.
- **Áp dụng cho**: mọi chủ quản HTTT; vendor SaaS (Đ41 k3) · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: module hoặc quy trình sự cố lưu `detected_at`, phân loại (thường / nghiêm trọng / có dấu hiệu ANQG hoặc gián đoạn nghiêm trọng), tự tính **hạn 24h và 72h**, nơi nhận (BCA hoặc A05, Sở/BYT nếu là đơn vị thuộc ngành), bằng chứng đã gửi; vendor phải báo cho khách hàng (chủ quản) đủ sớm để khách hàng kịp hạn **(suy luận: hợp đồng nên đặt ≤12 giờ)**.
- **Ghi chú / bẫy**: nếu sự cố có lộ DLCN thì còn nghĩa vụ thông báo vi phạm DLCN theo Luật 91/NĐ 356 (thuộc K8, inventory MT-15 ghi 72 giờ, cụm này không xác minh). Hai luồng báo cáo này độc lập nhau.

#### ANM-R17 — Báo cáo định kỳ hằng năm cho Bộ Công an
- **Căn cứ**: NĐ 331 Đ35 (gửi qua hệ thống quản lý văn bản, phần mềm báo cáo của BCA hoặc email; **chốt số liệu 15/12 năm trước – 14/12 năm báo cáo**; đơn vị chuyên trách và đơn vị vận hành gửi chủ quản **trước 20/12**; **chủ quản gửi BCA trước 25/12**); Đ36 (12 nhóm nội dung: danh sách HTTT, cấp đề xuất và phê duyệt, mức triển khai phương án theo từng tiêu chí, Quy chế, kiểm tra đánh giá...); Đ33 k6 (đơn vị vận hành báo cáo định kỳ hoặc đột xuất).
- **Áp dụng cho**: chủ quản; vendor-vận hành cung cấp số liệu · **Hạn**: 25/12/2026 (kỳ đầu, **suy luận**) và hằng năm.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: xuất được báo cáo tuân thủ theo từng yêu cầu của phương án (đã đáp ứng / một phần / chưa, kèm lộ trình) — Đ36 k9, k10.

#### ANM-R18 — Thiết kế khi chạy trên cloud hoặc trung tâm dữ liệu thuê ngoài
- **Căn cứ**: NĐ 331 Đ30 k8 (cấp 3, 4 thuê dịch vụ tại TTDL hoặc cloud: **tách riêng lô-gic** với hệ thống khác và có quản lý truy cập giữa các hệ thống; **tách lô-gic giữa các vùng mạng**; **phân vùng lưu trữ tách lô-gic**); Đ30 k9 (cấp 5: tách **vật lý**); Đ30 k5 (cấp 1–3 khuyến khích dùng chung giải pháp bảo vệ; cấp 4–5 phải thiết kế giới hạn ảnh hưởng lan truyền). NĐ 330 Đ69 k1 b (bên dùng cloud không xác định luồng xử lý DLCN, vai trò và trách nhiệm trong hợp đồng, hoặc không có yêu cầu bảo mật trong hợp đồng: 20–50 triệu, tổ chức). CV 365 Phần III mục 2 đ (thứ cấp): TTDL của nhà cung cấp đáp ứng quy định Bộ KH&CN; khuyến nghị Tier 3 / Rated 3 TIA-942, ISO 27001.
- **Áp dụng cho**: SaaS y tế, BV dùng cloud · **Mức**: BẮT BUỘC (cấp 3–4 trên cloud).
- **Phần mềm phải**: với SaaS đa khách hàng cấp 3 thì mỗi khách hàng (hoặc ít nhất mỗi HTTT cấp 3) có ranh giới lô-gic về mạng (VPC/VNet/subnet riêng, security group), lưu trữ (schema, DB hoặc bucket riêng có khóa riêng), quản lý truy cập liên hệ thống. Mô hình "shared DB + cột tenant_id" khó chứng minh "phân vùng lưu trữ tách lô-gic" **(suy luận, cần BCA hướng dẫn)**.

#### ANM-R19 — Lưu trữ dữ liệu tại Việt Nam
- **Căn cứ**: Luật 116 Đ25 k3 (DN trong và ngoài nước cung cấp dịch vụ trên mạng viễn thông, Internet, dịch vụ gia tăng tại VN, có thu thập, xử lý dữ liệu thông tin cá nhân hoặc dữ liệu do người dùng tại VN tạo ra thì **lưu trữ dữ liệu này tại Việt Nam** trong thời gian Chính phủ quy định). NĐ 333 Đ19 k1 (dữ liệu phải lưu tại VN: thông tin cá nhân của người dùng tại VN; dữ liệu người dùng tạo ra như tên tài khoản, thời gian dùng, thông tin thẻ tín dụng, email, IP đăng nhập/đăng xuất gần nhất, số điện thoại gắn tài khoản); **Đ19 k2 ("Doanh nghiệp trong nước lưu trữ dữ liệu quy định tại khoản 1 Điều này tại Việt Nam")**; Đ19 k5 (hình thức lưu do DN quyết định, phải truy xuất được kịp thời và đạt chuẩn ATTT quốc gia); Đ20 k1 (thời gian lưu tối thiểu 24 tháng, tính từ khi nhận yêu cầu — chủ yếu áp cho cơ chế yêu cầu với DN nước ngoài). NĐ 330 Đ29 k2 c (không lưu dữ liệu tại VN: 50–70 triệu, tổ chức ×2); Đ33 k1 a, b. CV 365 Phần III mục 2 a (thứ cấp): HSBA điện tử triển khai trên hạ tầng tại cơ sở KCB hoặc **cloud đặt tại Việt Nam**.
- **Áp dụng cho**: vendor SaaS và app y tế là DN Việt Nam (phạm vi phụ thuộc định nghĩa "dịch vụ trên mạng" ở NĐ 333 Đ3 k3–5); mọi cơ sở KCB làm HSBA điện tử trên cloud (CV 365, văn bản hướng dẫn chuyên môn) · **Mức**: BẮT BUỘC? (luật nói rõ với "DN cung cấp dịch vụ trên mạng", nhưng việc SaaS y tế có thuộc định nghĩa hẹp ở NĐ 333 Đ3 hay không vẫn chưa rõ) / BẮT BUỘC với EMR theo CV 365 nếu coi CV 365 là điều kiện của BYT.
- **Phần mềm phải**: CSDL chính, file, bản sao lưu và log chứa dữ liệu người dùng VN đặt tại region hoặc DC ở Việt Nam; nếu dùng dịch vụ phụ trợ nước ngoài (email, push notification, analytics, AI API) thì phải lập danh mục luồng dữ liệu ra nước ngoài (đồng thời là nghĩa vụ chuyển DLCN xuyên biên giới, thuộc K8).
- **Ghi chú / bẫy**: Đây là căn cứ ở **tầng luật** cho yêu cầu "cloud đặt tại VN" mà CV 365 nêu (khoảng trống #12 của inventory). Luật 116 Đ25 k3 + NĐ 333 Đ19 k2 không bắt **bản sao duy nhất** ở VN, nên một bản sao ở nước ngoài không bị cấm bởi chính điều này, nhưng lại vướng quy định chuyển DLCN xuyên biên giới (K8) **(suy luận)**.

#### ANM-R20 — Xác thực tài khoản người dùng của dịch vụ trực tuyến
- **Căn cứ**: Luật 116 Đ25 k2 a (xác thực thông tin khi người dùng đăng ký tài khoản số; bảo mật thông tin và tài khoản; cung cấp thông tin người dùng cho BCA **≤24 giờ**, khẩn cấp **≤03 giờ**); NĐ 333 Đ16 k2 (xác thực khi đăng ký; **xác thực tài khoản bằng số điện thoại di động tại Việt Nam**, nếu không có thì bằng **số định danh cá nhân** hoặc định danh điện tử hợp pháp; **chỉ tài khoản đã xác thực mới được đăng tải, chia sẻ, dùng tính năng tương tác**); Đ16 k3 c (cung cấp thông tin trong 24 giờ hoặc 03 giờ); Đ16 k4 b (gỡ thông tin vi phạm trong 24 giờ hoặc 06 giờ). NĐ 330 Đ29 k1 a, b (không xác thực khi đăng ký; không bảo mật thông tin, tài khoản: **30–50 triệu**, tổ chức ×2).
- **Áp dụng cho**: app hoặc cổng người bệnh, nền tảng KCB từ xa, cộng đồng hỏi đáp sức khỏe do DN cung cấp · **Mức**: BẮT BUỘC? (cùng câu hỏi phạm vi "dịch vụ trên mạng" như R19).
- **Phần mềm phải**: đăng ký có OTP SMS số VN hoặc liên kết VNeID; tính năng chat, đăng bài, đánh giá bác sĩ chỉ mở cho tài khoản đã xác thực; công cụ quản trị tra cứu và xuất thông tin tài khoản theo yêu cầu hợp lệ (có log ai tra, khi nào, căn cứ văn bản nào); công cụ ẩn hoặc gỡ nội dung nhanh.

### Tổ chức, nhân sự, vendor, ngành y tế

#### ANM-R21 — Chỉ định bộ phận hoặc nhân sự phụ trách ANM; tập huấn
- **Căn cứ**: Luật 116 Đ40 k2 (chủ quản dùng NSNN: phương án ANM được **thẩm định** khi thiết lập, mở rộng, nâng cấp; **chỉ định cá nhân, bộ phận phụ trách ANM**); NĐ 331 Đ31 k1 (người đứng đầu trực tiếp chịu trách nhiệm; bố trí bộ phận hoặc nhân sự chuyên trách phù hợp cấp độ; chưa có đơn vị chuyên trách thì chỉ định đơn vị CNTT hoặc chuyển đổi số); Đ31 k3 (đào tạo, tuyên truyền, **diễn tập**); Luật 116 Đ34 k2 + NĐ 333 Đ24 k8 b (người trực tiếp quản trị, vận hành HTTT **cấp 3–5 trong cơ quan, tổ chức, DN nhà nước** phải được tập huấn và cấp chứng nhận; hạn 36 tháng từ 19/08/2026 → **19/08/2029**). NĐ 330 Đ21 k3 b (không thành lập hoặc chỉ định đơn vị chuyên trách ứng cứu sự cố: 30–50 triệu, tổ chức ×2).
- **Áp dụng cho**: BV công (NSNN), mọi chủ quản · **Mức**: BẮT BUỘC.
- **Phần mềm phải**: (gián tiếp) vai trò "Security Officer" trong hệ thống có quyền xem log và cảnh báo nhưng không có quyền nghiệp vụ lâm sàng, để tách nhiệm vụ.

#### ANM-R22 — Hợp đồng thuê dịch vụ và trách nhiệm vendor
- **Căn cứ**: NĐ 331 Đ5 k3 a (thuê dịch vụ CNTT: đơn vị vận hành xác định theo hợp đồng; **hợp đồng phải quy định chi tiết trách nhiệm, thẩm quyền về quản trị dữ liệu, kiểm soát truy cập, bảo đảm ANM**); Đ5 k3 b (hết hạn hợp đồng mà hệ thống vẫn chạy); Đ19 k2 b (nhà cung cấp phối hợp cập nhật hồ sơ cấp độ theo hạ tầng thực tế); TCVN 14423:2026 mục 4.14/5.15 (kiểm kê nhà cung cấp, văn bản phân định trách nhiệm, rà soát hằng năm), 5.17.2.1 c (thuê khoán: mã nguồn hoặc chứng chỉ an toàn độc lập kèm cam kết pháp lý). NĐ 330 Đ69 k1 b, c (hợp đồng cloud thiếu luồng xử lý DLCN, vai trò, yêu cầu bảo mật; nhà cung cấp không ràng buộc nhà thầu phụ). CV 365 Phần III mục 2 đ, 4 c (thứ cấp): dữ liệu thuộc sở hữu cơ sở KCB; hết hợp đồng thì **bàn giao toàn bộ dữ liệu kèm đặc tả** và **hủy an toàn** tại nhà cung cấp; cam kết bảo mật. QĐ 326 Đ1 k2 c: nhà cung cấp dịch vụ CNTT, ATTT cho đơn vị BYT thuộc đối tượng của Quy chế.
- **Áp dụng cho**: vendor và cơ sở thuê · **Mức**: BẮT BUỘC (nội dung hợp đồng theo NĐ 331 Đ5 k3 a).
- **Phần mềm phải**: chức năng xuất toàn bộ dữ liệu theo định dạng mở có đặc tả (data dictionary); quy trình và biên bản hủy dữ liệu sau bàn giao (theo NIST SP 800-88 hoặc tương đương **(NÊN)**); trang "trách nhiệm chia sẻ" (shared responsibility matrix) kèm hợp đồng.

#### ANM-R23 — Kết thúc vận hành, hủy bỏ, xóa sạch
- **Căn cứ**: NĐ 331 Đ29 k2 g, Đ30 k3 g (phương án kết thúc vận hành, thanh lý, hủy bỏ); QĐ 326 Đ7 e (xóa sạch dữ liệu trên máy chủ khi chuyển giao hoặc đổi mục đích); TCVN 14423 (quản lý tài sản thông tin: yêu cầu khi tiêu hủy, xóa bỏ, mục 5.4.2.1 a).
- **Mức**: BẮT BUỘC (phải có phương án).
- **Phần mềm phải**: công cụ xóa an toàn dữ liệu của một tenant hoặc một cơ sở (gồm cả bản sao lưu theo vòng đời), có biên bản. Phải đối chiếu với thời hạn lưu HSBA (K1) trước khi xóa.

#### ANM-R24 — Quy chế ATTT/ANM của Bộ Y tế cho đơn vị thuộc Bộ
- **Căn cứ**: QĐ 326/QĐ-BYT/2024 (gốc-OCR): Đ1 k2 (đối tượng), Đ7–Đ8 (mạng, máy chủ, ứng dụng, dữ liệu: log ≥6 tháng ở máy chủ, ≥3 tháng ở ứng dụng; mật khẩu; mã hóa; sao lưu), Đ11 (xác định cấp độ theo NĐ 85, TT 12/2022), Đ13 (TT Thông tin y tế QG là đơn vị chuyên trách ứng cứu sự cố của Bộ; Bộ có Đội ứng cứu).
- **Áp dụng cho**: BV và đơn vị trực thuộc BYT; vendor phục vụ họ · **Mức**: BẮT BUỘC (văn bản quản lý nội bộ ngành còn hiệu lực), nhưng phần dẫn NĐ 85/TT 12 phải đọc thay bằng NĐ 331/TCVN 14423 **(suy luận theo NĐ 331 Đ39 k2 và Luật 87)**.
- **Phần mềm phải**: như R09–R13; cộng thêm giới hạn đăng nhập sai và timeout phiên (Đ8).

#### ANM-R25 — Yêu cầu ATTT riêng cho HSBA điện tử
- **Căn cứ**: TT 13/2025 Đ1 k4 (HSBA tuân thủ pháp luật về ATTT mạng, ANM, bảo vệ DLCN, lưu trữ dữ liệu); Đ2 k1, k4; Đ4 k3 b (cơ sở KCB ban hành **quy chế** lập, cập nhật, quản lý, lưu trữ, sử dụng và **an toàn thông tin** HSBA) — gốc-OCR. CV 365 Phần III mục 4 a–b (thứ cấp): HTTT của cơ sở KCB **tối thiểu cấp độ 2** và có phương án ATTT, lập hồ sơ cấp độ (văn bản viện dẫn TT 12/2022 và TCVN 11930, nay đọc theo NĐ 331 và TCVN 14423). CT 07/CT-BYT (thứ cấp): hoàn thành lập, thẩm định, phê duyệt hồ sơ đề xuất cấp độ cho **100% HTTT đang vận hành trước 30/09/2026**; thiết lập giám sát ATTT tập trung (SOC), diễn tập.
- **Áp dụng cho**: mọi cơ sở KCB làm HSBA điện tử (TT 13); hệ thống ngành y tế (CT 07, đối tượng cụ thể chưa rõ) · **Mức**: BẮT BUỘC (TT 13) / BẮT BUỘC? (CV 365 và CT 07 vì chưa đọc được bản gốc).
- **Phần mềm phải**: hồ sơ cấp độ EMR tối thiểu cấp 2 theo TCVN 14423:2026 mục 4; tài liệu quy chế ATTT HSBA mẫu do vendor cung cấp.

**Tổng hợp mức**: BẮT BUỘC: R01, R02, R04, R05, R06, R07, R13, R16, R17, R18, R21, R22, R23, R24 (14). BẮT BUỘC?: R03, R08, R10, R14, R15, R19, R20 (7). Hỗn hợp BẮT BUỘC / BẮT BUỘC? theo từng nội dung: R09, R11, R12, R25 (4). NÊN thuần: không có mục riêng; các phần NÊN nằm trong R14 (cấp 2), R16 (SLA vendor ≤12h), R22 (chuẩn xóa).

---

## 3. Pattern thiết kế

### P1. Sổ đăng ký HTTT và cấp độ (System & Classification Registry)
- **Giải quyết**: R01, R02, R04, R05, R06, R17.
- **Mô tả**: một module hoặc bảng cấu hình (có thể nằm trong công cụ GRC của BV, hoặc trang quản trị của SaaS) mô tả từng HTTT và căn cứ cấp độ, để sinh thuyết minh Đ22 và báo cáo Đ36.
- **Mô hình dữ liệu gợi ý**:
  - `info_system(id, name, owner_org /*chủ quản*/, operator_org /*đơn vị vận hành*/, system_type ENUM('internal','citizen_service','infrastructure','ics','other') /*Đ9 k2*/, is_online_service BOOL, conditional_business_code /*STT Phụ lục IV, vd 100 KCB*/, handles_tthc BOOL, scope_province_count INT, proposed_level SMALLINT CHECK 1..5, approved_level SMALLINT, approval_decision_no, approval_date, legacy_level_nd85 SMALLINT NULL, legacy_compliance_deadline DATE /*01/07/2027*/)`.
  - `system_component(system_id, component, host, os, zone, ip_private, ip_public, purpose)` → tạo danh mục cho Đ22 k3 d.
  - `data_category(system_id, table_or_field, info_class ENUM('public','private','personal_basic','personal_sensitive','state_secret'))`.
  - `risk_assessment(id, system_id, trigger ENUM('initial','change','integration','incident','authority'), performed_by_unit, independent_of_operator BOOL, result_level, file_ref, date)`.
- **Ràng buộc**: `approved_level >= proposed_level_from_rules` (cảnh báo khi rule tính ra cấp cao hơn cấp đã duyệt); khóa không cho bật cờ "go-live" khi `approved_level>=3 AND approval_date IS NULL` (R04, NĐ 330 Đ23 k1 c).
- **Đánh đổi**: tốn công nhập liệu ban đầu, bù lại xuất được ngay báo cáo 25/12 và hồ sơ cấp độ.

### P2. Bộ đếm chủ thể dữ liệu và cảnh báo ngưỡng
- **Giải quyết**: R02, R06.
- **Mô tả**: job hằng ngày đếm `COUNT(DISTINCT patient_id)` có dữ liệu sức khỏe trong phạm vi dịch vụ trực tuyến (SaaS: cộng mọi tenant); đếm riêng người dùng chỉ có DLCN cơ bản.
- **Dữ liệu**: `subject_counter(system_id, date, sensitive_subjects, basic_subjects)`; ngưỡng cấu hình 10.000 và 100.000; cảnh báo ở 80% → tạo `risk_assessment(trigger='change')`.
- **Đánh đổi**: cần định nghĩa thống nhất "chủ thể" (người bệnh đã khử trùng lặp qua số định danh cá nhân).

### P3. Đường ống nhật ký an ninh bất biến
- **Giải quyết**: R11, R15, R16.
- **Mô tả**: ứng dụng ghi sự kiện có cấu trúc → hàng đợi → kho log append-only (WORM/object lock) + chuỗi hash → SIEM. Đồng bộ NTP mọi node (TCVN 4.8, 5.8).
- **Schema**: `security_event(id ULID, ts_utc, ntp_synced BOOL, account_id, account_type, src_ip INET, src_port INT, device_id, user_agent, action, object_type, object_id, patient_id NULL, result, reason_code, prev_hash, hash)`; chỉ mục `(account_id, ts_utc)`, `(patient_id, ts_utc)`, `(src_ip, ts_utc)`.
- **Retention**: hot 90 ngày (truy vấn nhanh, thỏa NĐ 330 Đ34 k1 c), warm hoặc cold đến **≥12 tháng** (NĐ 333 Đ16 k6, Đ20 k3; TCVN cấp 5). Cảnh báo khi dung lượng còn dưới ngưỡng (TCVN 5.8).
- **Đánh đổi**: chi phí lưu trữ; phải mask dữ liệu nhạy cảm trong payload log (log không chứa nội dung bệnh án, chỉ ID).

### P4. IAM theo loại tài khoản, MFA và vòng đời
- **Giải quyết**: R09, R10, R21.
- **Mô tả**: `account(id, type ENUM('admin','operator','technical','service'), owner_person_id, department, status, activated_at, disabled_at, last_login_at, mfa_enrolled BOOL, shared_approved_by NULL)`; policy engine theo `type` và `network_origin` (nội bộ hoặc Internet): Internet hoặc admin thì bắt buộc MFA. Job `disable_inactive(45d)`. Báo cáo `access_review` mỗi 6 tháng (danh sách tài khoản × quyền × người duyệt).
- **Break-glass** (đặc thù y tế, **NÊN**): quyền khẩn cấp xem hồ sơ ngoài phạm vi khoa, bắt nhập lý do, cảnh báo ngay cho Security Officer, hết hạn tự động. Giữ được nguyên tắc quyền tối thiểu mà không cản cấp cứu.
- **Đánh đổi**: MFA cho máy trạm dùng chung ở khoa phòng: dùng thẻ hoặc token, hoặc giới hạn MFA cho truy cập từ ngoài mạng nội bộ (đúng câu chữ TCVN).

### P5. Mã hóa nhiều lớp và toàn vẹn bản ghi
- **Giải quyết**: R12, R18.
- **Mô tả**: TLS ở mọi kênh; mã hóa lưu (TDE hoặc ổ đĩa) cộng mã hóa mức trường cho nhóm chẩn đoán đặc biệt; khóa mỗi tenant trong KMS (crypto-isolation, hỗ trợ "tách lô-gic lưu trữ" ở Đ30 k8 c); bản ghi xuất ra có `sha256` và chữ ký số của cơ sở (TCVN 5.4.2.5, 5.4.2.8).
- **Đánh đổi**: mã hóa mức trường làm khó tìm kiếm; dùng blind index hoặc token cho trường cần tra cứu.

### P6. Sao lưu 3-2-1 bất biến + diễn tập khôi phục có biên bản
- **Giải quyết**: R13, R16, R22.
- **Mô tả**: snapshot CSDL + WAL/PITR; object storage có object-lock cho file và DICOM; **1 bản tại cơ sở KCB** (appliance hoặc NAS do cơ sở giữ khi chạy SaaS; CV 365) và 1 bản ở DC khác tại VN; mã hóa bằng khóa của cơ sở.
- **Dữ liệu**: `backup_job(id, scope, started_at, finished_at, size, checksum, location, encrypted BOOL, immutable_until)`, `restore_test(id, backup_job_id, tested_at, rto_achieved, rpo_achieved, result, evidence_ref)`; ràng buộc chính sách: mỗi loại dữ liệu có ít nhất 1 `restore_test` thành công trong chu kỳ cấu hình (vd 6 tháng).
- **Đánh đổi**: chi phí băng thông khi đồng bộ bản về cơ sở; PACS dung lượng lớn thì sao lưu theo tầng.

### P7. Sổ sự cố với đồng hồ đếm hạn
- **Giải quyết**: R16, R15.
- **Dữ liệu**: `incident(id, system_id, detected_at, severity ENUM('normal','serious','national_security_or_major_outage'), initial_notice_due = detected_at+24h /*nếu serious*/, report_due = detected_at+72h, immediate_required BOOL, notified_vendor_at, notified_owner_at, reported_bca_at, report_ref, personal_data_breach BOOL /*kích luồng K8*/, status)`.
- **Luồng**: phát hiện → phân loại → (nghiêm trọng) thông báo ban đầu ≤24h → báo cáo ≤72h → cập nhật → báo cáo kết thúc. Cảnh báo T-6h trước mỗi hạn.
- **Đánh đổi**: cần định nghĩa "sự cố nghiêm trọng" nội bộ vì NĐ 331 không định nghĩa; có thể lấy theo phân nhóm sự cố trong TCVN 5.16 và hướng dẫn BCA khi có.

### P8. SaaS đa khách hàng đạt "tách lô-gic" cho cấp 3
- **Giải quyết**: R18, R19, R22.
- **Mô tả**: tối thiểu mỗi khách hàng cấp 3 có: VPC hoặc subnet và security group riêng; CSDL hoặc schema riêng với user DB riêng; bucket hoặc prefix riêng có policy và khóa KMS riêng; tài khoản quản trị vendor đi qua bastion có MFA và ghi phiên. Region tại VN; liệt kê dịch vụ phụ trợ ngoài VN.
- **Đánh đổi**: chi phí cao hơn shared-everything; với khách hàng cấp 2 vẫn có thể dùng mô hình chia sẻ nhưng phải chứng minh kiểm soát truy cập.

### P9. Xác thực tài khoản người bệnh trên app hoặc cổng
- **Giải quyết**: R20, R11.
- **Mô tả**: đăng ký có OTP số điện thoại VN hoặc VNeID; `account.verified_method ENUM('vn_phone','national_id','vneid')`, `verified_at`; middleware chặn tính năng tương tác (chat, đánh giá, đăng bài) nếu chưa xác thực; log đăng nhập (IP, cổng nguồn, thiết bị) ≥12 tháng; công cụ "lawful request" ghi `request_doc_no, requested_by, received_at, fulfilled_at` để chứng minh hạn 24h/3h.
- **Đánh đổi**: giảm tỉ lệ đăng ký; người nước ngoài không có số VN thì dùng định danh điện tử hợp pháp.

### P10. Pipeline phát triển an toàn và gói bằng chứng cho khách hàng
- **Giải quyết**: R14, R22.
- **Mô tả**: CI chạy SAST, SCA (SBOM CycloneDX), secret scan, DAST trên staging; cổng chặn release khi còn lỗi mức cao; mỗi phiên bản phát hành kèm "security evidence pack" (báo cáo quét, pentest độc lập hằng năm, SBOM, danh sách CVE đã vá) để khách hàng cấp 3 đáp ứng TCVN 5.17.2.1 c nếu không nhận mã nguồn.
- **Đánh đổi**: chi phí pentest độc lập; có thể dùng ký quỹ mã nguồn (escrow) thay thế.

### P11. Bàn giao dữ liệu và hủy khi kết thúc hợp đồng
- **Giải quyết**: R22, R23.
- **Mô tả**: API hoặc job xuất toàn bộ dữ liệu một tenant (CSDL dump + file + data dictionary + checksum); quy trình hủy ở mọi bản sao (gồm backup theo hạn hết hiệu lực), biên bản có chữ ký hai bên.
- **Đánh đổi**: backup bất biến không xóa sớm được → hợp đồng cần ghi rõ "hủy khi object-lock hết hạn" và mã hóa bằng khóa riêng để hủy khóa (crypto-shredding).

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| ANM-A01 | R01, R02 | Xem tài liệu kiến trúc; vẽ lại luồng dữ liệu giữa HIS, EMR, LIS, PACS, cổng bệnh nhân; xác định thành phần dùng chung CSDL | Sơ đồ kiến trúc, danh mục kết nối ngoài | Bắt buộc |
| ANM-A02 | R02, R06 | Truy vấn `COUNT(DISTINCT patient_id)` trên dữ liệu mà cổng hoặc app trực tuyến truy cập được; xác định dịch vụ có thuộc STT 100/101/103 Phụ lục IV Luật Đầu tư không | Kết quả truy vấn có ngày; bảng phân loại cấp độ có căn cứ Đ12/Đ13 | Bắt buộc |
| ANM-A03 | R04, R05 | Yêu cầu quyết định phê duyệt hồ sơ cấp độ (số, ngày, người ký đúng thẩm quyền Đ18); với hệ thống cũ, xem quyết định theo NĐ 85 và kế hoạch đáp ứng trước 01/07/2027 | Bản quyết định; hồ sơ đề xuất theo Đ21; ý kiến thẩm định (cấp 3+) | Bắt buộc |
| ANM-A04 | R04 | So ngày go-live (log triển khai, biên bản nghiệm thu) với ngày phê duyệt cấp độ | Biên bản nghiệm thu, quyết định cấp độ | Bắt buộc (cấp 3–5) |
| ANM-A05 | R07 | Xem Quy chế bảo đảm ANM: ngày ban hành có **trước** ngày phê duyệt hồ sơ cấp độ không (Đ30 k7) | Quyết định ban hành Quy chế | Bắt buộc |
| ANM-A06 | R06 | Xem hồ sơ đánh giá rủi ro; đối chiếu với các lần thêm kết nối liên thông (BHXH, VNeID, đối tác) trong 12 tháng | Báo cáo đánh giá rủi ro, change log tích hợp | Bắt buộc |
| ANM-A07 | R09 | Xuất danh sách tài khoản: có phân loại 4 nhóm không; có tài khoản không đăng nhập >45 ngày còn active không; có tài khoản mặc định (admin/admin, sa, root) không | File xuất tài khoản; ảnh chụp cấu hình | Bắt buộc? |
| ANM-A08 | R09 | Chọn 3 người dùng ở 3 khoa, thử truy cập hồ sơ ngoài phạm vi; xem ma trận quyền theo chức danh | Ảnh chụp lỗi từ chối, ma trận RBAC | Bắt buộc |
| ANM-A09 | R10 | Đăng nhập từ Internet và bằng tài khoản quản trị: có bị yêu cầu MFA không; kiểm cấu hình độ dài mật khẩu (≥14 nếu không MFA), lockout, timeout | Ảnh chụp luồng đăng nhập, file cấu hình policy | Bắt buộc? |
| ANM-A10 | R10 | Truy vấn bảng user: mật khẩu lưu dạng hash có salt (argon2/bcrypt/scrypt/PBKDF2), không lưu rõ hoặc MD5/SHA1 trơn | Mẫu bản ghi đã che | Bắt buộc? |
| ANM-A11 | R11 | Thực hiện thao tác xem, sửa hồ sơ bệnh nhân; kiểm tra log có đủ ts, tài khoản, IP, cổng nguồn, hành động, đối tượng không; thử sửa hoặc xóa log bằng quyền DBA | Trích log; kết quả thử sửa log | Bắt buộc |
| ANM-A12 | R11 | Truy vấn log đăng nhập cũ nhất còn truy xuất được (≥90 ngày; ≥12 tháng nếu là DN cung cấp dịch vụ trên mạng); kiểm đồng bộ NTP trên các node | Kết quả truy vấn, cấu hình NTP | Bắt buộc |
| ANM-A13 | R12 | Kiểm cấu hình TLS (phiên bản, cert) của mọi endpoint; kiểm mã hóa lưu trữ CSDL, ổ đĩa, backup; với cloud thì kiểm KMS | Báo cáo quét TLS; ảnh chụp cấu hình mã hóa | Bắt buộc (cloud) / Bắt buộc? |
| ANM-A14 | R13 | Xem lịch sao lưu tự động, nơi đặt bản sao (tại cơ sở + ngoài cơ sở), tính bất biến; yêu cầu biên bản khôi phục thử gần nhất; **thực hiện khôi phục thử một CSDL hoặc ca bệnh trên môi trường test** | Log job backup, biên bản restore, RTO/RPO đo được | Bắt buộc |
| ANM-A15 | R14 | Yêu cầu báo cáo SAST/SCA/pentest gần nhất; kiểm repo có secret không (gitleaks); kiểm kênh báo lỗ hổng | Báo cáo, kết quả quét secret | Bắt buộc? (cấp 3+) / Nên (cấp 2) |
| ANM-A16 | R15 | Kiểm log có được đẩy về SOC hoặc SIEM không; có agent chống mã độc, EDR trên máy chủ không; đã kết nối hoặc có kế hoạch kết nối Trung tâm ANM QG hoặc tỉnh chưa | Ảnh chụp dashboard SIEM, văn bản kết nối | Bắt buộc? |
| ANM-A17 | R16 | Xem kế hoạch ứng phó sự cố; danh sách đầu mối (chính + dự phòng); hồ sơ 1 sự cố gần nhất: thời điểm phát hiện vs thời điểm báo cáo (≤24h/≤72h) | Kế hoạch, sổ sự cố, văn bản báo cáo | Bắt buộc |
| ANM-A18 | R17 | Yêu cầu báo cáo năm gửi BCA (bản gửi trước 25/12) và báo cáo nội bộ trước 20/12 | Bản báo cáo, bằng chứng gửi | Bắt buộc |
| ANM-A19 | R18 | Với cấp 3 trên cloud: kiểm VPC/subnet, security group, DB/schema, bucket, khóa KMS riêng cho hệ thống hoặc khách hàng | Sơ đồ mạng cloud, ảnh chụp console | Bắt buộc |
| ANM-A20 | R19 | Liệt kê vị trí (region/DC) của CSDL, file, backup, log, và dịch vụ bên thứ ba nhận dữ liệu người dùng | Bảng data residency, hợp đồng DC hoặc cloud | Bắt buộc? |
| ANM-A21 | R20 | Tạo tài khoản mới trên app: có OTP số VN hoặc VNeID không; tài khoản chưa xác thực có chat hoặc đăng bài được không | Ảnh chụp luồng đăng ký | Bắt buộc? |
| ANM-A22 | R21 | Quyết định chỉ định bộ phận hoặc nhân sự ANM; danh sách người quản trị hệ thống cấp 3+ và tình trạng tập huấn (hạn 19/08/2029 với tổ chức nhà nước) | Quyết định, chứng nhận tập huấn | Bắt buộc |
| ANM-A23 | R22, R23 | Đọc hợp đồng vendor: có điều khoản quản trị dữ liệu, kiểm soát truy cập, ANM, bàn giao dữ liệu, hủy dữ liệu, nhà thầu phụ, báo sự cố không | Bản hợp đồng, phụ lục SLA | Bắt buộc |
| ANM-A24 | R22 | Thử chức năng xuất toàn bộ dữ liệu một cơ sở kèm data dictionary | File xuất, checksum | Bắt buộc |
| ANM-A25 | R24 | (Đơn vị thuộc BYT) Đối chiếu cấu hình với QĐ 326 Đ7–8: log máy chủ ≥6 tháng, log ứng dụng ≥3 tháng, giới hạn đăng nhập sai, timeout | Cấu hình, trích log | Bắt buộc |
| ANM-A26 | R25 | Có quy chế an toàn thông tin HSBA (TT 13 Đ4 k3 b); hồ sơ cấp độ EMR tối thiểu cấp 2 | Quyết định ban hành quy chế, hồ sơ cấp độ | Bắt buộc |

---

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái (tại 05/10/2026) | Nội dung | Ai phải làm | Căn cứ |
|---|---|---|---|---|
| 01/07/2025 | Đã qua | Luật 87/2025 sửa Luật 64/2025 Đ57 k2: văn bản quy định chi tiết hết HL cùng văn bản được hướng dẫn, trừ khi được công bố tiếp tục HL | — | Luật 87 Đ1 k22 |
| 01/07/2026 | Đã qua | Luật ANM 116 có HL; Luật ATTTM 2015 và Luật ANM 2018 hết HL; **(suy luận)** NĐ 85/2016, NĐ 53/2022, TT 12/2022, TT 03/2017 hết HL theo Luật 64 Đ57 k2 | Mọi chủ quản | Luật 116 Đ44 |
| 01/07/2026 | Đã qua | QCVN 12:2026/BCA (TT 47/2026) có HL | HTTT lưu trữ tài liệu điện tử của cơ quan Đảng, Nhà nước | TT 47/2026 |
| 19/08/2026 | Đã qua | NĐ 327–333/2026 có HL (gồm 330 xử phạt, 331 cấp độ, 333 chi tiết Luật) | Mọi đối tượng | NĐ 331 Đ38; NĐ 333 Đ30; NĐ 330 Đ80 |
| 30/09/2026 | Đã qua | 100% HTTT đang vận hành hoàn thành lập, thẩm định, phê duyệt hồ sơ cấp độ; SOC tập trung | Hệ thống ngành y tế (đối tượng cụ thể chưa rõ) | CT 07/CT-BYT (thứ cấp) |
| 30/09/2026 | Đã qua | Khung kiến trúc ANM quốc gia v1.0 | Hệ thống chính trị | QĐ 1875/QĐ-TTg (thứ cấp) |
| 14/12/2026 | Sắp tới | Chốt số liệu báo cáo ANM năm (kỳ 15/12/2025–14/12/2026) | Chủ quản, đơn vị vận hành | NĐ 331 Đ35 k3 |
| 20/12/2026 | Sắp tới | Đơn vị chuyên trách và đơn vị vận hành gửi báo cáo cho chủ quản | Đơn vị vận hành (kể cả vendor vận hành) | NĐ 331 Đ35 k4 a |
| 25/12/2026 | Sắp tới | Chủ quản gửi báo cáo năm cho Bộ Công an (lặp lại hằng năm) | Chủ quản | NĐ 331 Đ35 k4 b |
| **01/01/2027** | Sắp tới | Hạn hoàn thành thẩm định, phê duyệt cấp độ **theo NĐ 85** cho HTTT đang đầu tư, xây dựng trước 01/07/2026 | Chủ đầu tư, chủ quản | NĐ 331 Đ39 k1 |
| 15/01 hằng năm | Định kỳ | BCA cập nhật danh mục các loại HTTT theo Đ9 k2 trên cổng của BCA → rà soát lại phân loại | Chủ quản theo dõi | NĐ 331 Đ9 k2 e |
| 01/03/2027 | Sắp tới | Luật 24/2026/QH16 sửa Luật Đầu tư có HL (có thể đổi Phụ lục IV, ảnh hưởng tiêu chí Đ13 k2 a) | Theo dõi | thứ cấp |
| **01/07/2027** | Sắp tới | HTTT đã có cấp độ theo luật cũ và HTTT đang đầu tư phải **đáp ứng điều kiện, biện pháp theo luật mới, NĐ 331, TCVN 14423:2026**; sản phẩm và giải pháp ATTT cũ phải đáp ứng điều kiện ANM mới | Chủ quản, đơn vị vận hành, vendor | Luật 116 Đ45 k1, k3; NĐ 331 Đ39 k1 |
| 19/08/2028 | Xa | Cơ quan, tổ chức, DNNN hoàn thành tập huấn cho lực lượng bảo vệ ANM (Luật Đ34 k1) | Cơ quan, tổ chức nhà nước | NĐ 333 Đ24 k8 a |
| 19/08/2029 | Xa | Người trực tiếp quản trị, vận hành HTTT **cấp 3–5** trong cơ quan, tổ chức, DNNN được tập huấn và cấp chứng nhận | BV công có HTTT cấp 3+ | Luật 116 Đ34 k2; NĐ 333 Đ24 k8 b |
| Thường xuyên | — | Đánh giá rủi ro khi có thay đổi hoặc tích hợp; báo cáo sự cố (24h thông báo ban đầu, 72h báo cáo, ngay lập tức với sự cố ANQG/gián đoạn nghiêm trọng); cung cấp thông tin người dùng cho BCA ≤24h (khẩn ≤3h); gỡ nội dung ≤24h (khẩn ≤6h); rà soát tài khoản 6 tháng; vô hiệu tài khoản sau 45 ngày; quét lỗ hổng 6 tháng (cấp 3) | Chủ quản, vendor | NĐ 331 Đ10, Đ31; NĐ 333 Đ16; TCVN 14423 |

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

### Chuỗi thay thế
| Cũ | → | Mới | Ghi chú |
|---|---|---|---|
| Luật ATTTM 86/2015 + Luật ANM 24/2018 | → | Luật ANM 116/2025 | Luật 116 Đ44 k2; hết HL 01/07/2026 |
| NĐ 85/2016 (+ TT 12/2022, TT 03/2017) | → (thực tế) | NĐ 331/2026 + TCVN 14423:2026 | **Không có điều bãi bỏ** trong NĐ 331. Theo Luật 64 Đ57 k2 (sửa bởi Luật 87/2025), NĐ 85 và các TT hướng dẫn **hết HL cùng Luật ATTTM** trừ khi được công bố tiếp tục HL (chưa tìm thấy văn bản công bố). NĐ 331 Đ39 k1 vẫn dẫn NĐ 85 làm thủ tục thẩm định cho HTTT đang đầu tư đến 01/01/2027 |
| NĐ 53/2022 | → | NĐ 333/2026 | Không có điều bãi bỏ; NĐ 333 Đ31 giữ thủ tục NĐ 53 cho hồ sơ đã nộp. Nghĩa vụ lưu trữ dữ liệu tại VN nay ở NĐ 333 Đ19–20 |
| TCVN 11930:2017 (và TCVN 14423:2025) | → | TCVN 14423:2026 | Lời nói đầu của TCVN 14423:2026 |
| QĐ 4159/QĐ-BYT/2014 | → | QĐ 326/QĐ-BYT/2024 | QĐ 326 Đ2; QĐ 326 vẫn dựa trên khung cũ |
| "An toàn thông tin mạng", "an toàn HTTT" trong TCVN, QCVN | ≡ | "An ninh mạng" | NĐ 331 Đ39 k2 |

### Mâu thuẫn inventory đã giải quyết
- **MT-04 (NĐ 331 có thay NĐ 85 không)**: NĐ 331 không bãi bỏ NĐ 85 (đã đọc toàn văn Đ38–40). Inventory viết NĐ 85 "mất căn cứ"; chính xác hơn là **hết hiệu lực từ 01/07/2026 theo Luật 64 Đ57 k2 (bản sửa bởi Luật 87/2025)**, vì Luật 87 đảo nguyên tắc cũ: văn bản hướng dẫn **mặc định hết HL** trừ khi được công bố tiếp tục HL. Ngoại lệ thực tế: NĐ 331 Đ39 k1 dẫn chiếu NĐ 85 cho thủ tục thẩm định chuyển tiếp. Việc dẫn chiếu này có "giữ" NĐ 85 về mặt pháp lý hay chỉ mượn thủ tục thì cần luật sư (mục 7).
- **MT-16 (ngưỡng cấp độ)**: đã đối chiếu gốc Đ12–13. Ngưỡng 10.000 / 100.000 chỉ áp cho **dịch vụ trực tuyến**; HIS nội bộ là cấp 2 không phụ thuộc quy mô; KCB từ xa và bán thuốc online là cấp 3 vì thuộc ngành nghề có điều kiện (**suy luận** dựa trên Phụ lục IV, nguồn thứ cấp). Xem bảng ở R02.
- **MT-17 (hạn báo cáo sự cố)**: đã xác minh gốc NĐ 331 Đ31 k2 d: **24 giờ** (thông báo ban đầu với sự cố nghiêm trọng), **72 giờ** (báo cáo nguyên nhân, phạm vi, biện pháp), **ngay khi phát hiện** (dấu hiệu ANQG, TTATXH hoặc gián đoạn nghiêm trọng).
- **MT-05**: khớp với gốc: 01/01/2027 và 01/07/2027, tính từ ngày Luật 116 có HL.
- **Báo cáo định kỳ (F, mục 4 inventory)**: khớp với gốc NĐ 331 Đ35 (chốt 14/12, gửi BCA trước 25/12); bổ sung mốc nội bộ 20/12.
- **Câu hỏi mở 3 (lưu trữ dữ liệu tại VN)**: nằm ở NĐ 333 Đ19 (DN trong nước phải lưu tại VN), Đ20 (tối thiểu 24 tháng kể từ khi có yêu cầu), cùng Luật 116 Đ25 k3.
- **Câu hỏi mở 4 (Đ40, Đ41)**: Đ40 k1 b (kết nối giám sát) áp cho **mọi chủ quản HTTT**, kể cả BV tư, theo câu chữ luật; cơ chế cụ thể chưa có. Định danh IP (Luật Đ41 k5) được NĐ 333 Chương IV khoanh vào **DN cung cấp dịch vụ viễn thông, Internet** (Đ1 k2, Đ21–23), nên **không áp cho SaaS y tế** thông thường.
- **Câu hỏi mở 5 (TT 47/2026/TT-BCA)**: phạm vi là HTTT **lưu trữ tài liệu điện tử** của **cơ quan Đảng, Nhà nước**. HIS/EMR không phải hệ thống này; BV công là đơn vị sự nghiệp. Coi là **không áp dụng trực tiếp**; chỉ cân nhắc nếu BV vận hành hệ thống lưu trữ hồ sơ, tài liệu hành chính điện tử theo Luật Lưu trữ (mục 7).

### Bẫy trích dẫn
1. "Bệnh viện ≥10.000 người bệnh là cấp 3": sai nếu nói về HIS nội bộ. Ngưỡng chỉ áp cho dịch vụ trực tuyến và tính theo chủ thể DLCN nhạy cảm.
2. "NĐ 331 thay thế NĐ 85": NĐ 331 không có câu nào như vậy; đừng trích "theo Điều 38 NĐ 331, NĐ 85 hết hiệu lực".
3. Bài trên cổng BCA tóm Đ39 k1 là "hệ thống vận hành trước 01/07/2026". Câu chữ gốc là "**đang trong quá trình đầu tư, xây dựng**".
4. Mức phạt NĐ 330: Mục 1–5 (lĩnh vực ANM) là **mức cho cá nhân, tổ chức ×2** (Đ7 k1; trần 100 triệu cá nhân, 200 triệu tổ chức theo Đ7 k3). Mục 6 (BVDLCN, gồm Đ62 dữ liệu sức khỏe, Đ69 cloud) là **mức cho tổ chức**, cá nhân ×1/2. Đừng trích "phạt 20–30 triệu" cho bệnh viện mà không nhân đôi.
5. TCVN 14423:2026 là tiêu chuẩn tự nguyện, chỉ có sức bắt buộc qua viện dẫn của NĐ 331 Đ28–30. Luật 116 Đ10 k3 lại cho cấp 1–2 chọn biện pháp ở Đ10 k2 "theo nhu cầu, khả năng". Khi audit hệ thống cấp 2, ghi "BẮT BUỘC?" thay vì "bắt buộc tuyệt đối" với các con số chi tiết của TCVN.
6. Thời hạn log có nhiều con số với nhiều đối tượng: 90 ngày (NĐ 330 Đ34 k1 c, tài khoản số), 01/03/06/12 tháng (TCVN theo cấp 2/3/4/5, là **dung lượng duy trì**), 12 tháng (NĐ 333 Đ16 k6 và Đ20 k3, DN cung cấp dịch vụ trên mạng), 3/6 tháng (QĐ 326, đơn vị BYT). Không có con số riêng cho log truy cập HSBA.
7. CV 365 dẫn toàn khung cũ (NĐ 85, TT 12/2022, TCVN 11930:2017, QĐ 742/QĐ-BTTTT, TT 39/2017, NĐ 13/2023). Khi viết skill phải đổi sang NĐ 331, TCVN 14423:2026, Luật 91/NĐ 356.
8. QĐ 326/QĐ-BYT: mật khẩu ≥8 ký tự, thấp hơn TCVN 14423 (≥14 nếu không MFA). Không trích QĐ 326 như mức đủ.
9. NĐ 333 Đ20 k1 "tối thiểu 24 tháng": thời gian tính **từ khi DN nhận yêu cầu lưu trữ**. Câu này gắn với cơ chế yêu cầu (chủ yếu với DN nước ngoài); không nên diễn giải thành "mọi DN phải giữ dữ liệu người dùng 24 tháng".
10. NĐ 331 Đ2: với tổ chức tư nhân ngoài phạm vi "dịch vụ trực tuyến", Nghị định chỉ "khuyến khích". Đừng viết "mọi phòng khám tư phải lập hồ sơ cấp độ cho HIS theo NĐ 331" mà không ghi chú.
11. Cấp 3 thẩm định và phê duyệt **nội bộ** (đơn vị chuyên trách + chủ quản), **không** gửi BCA. BCA chỉ thẩm định cấp 4–5 (Đ18). Nhiều tài liệu cũ theo NĐ 85 ghi cấp 3 phải xin ý kiến Bộ TT&TT, nay không còn.

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Tình trạng hiệu lực NĐ 85/2016, TT 12/2022, TT 03/2017, NĐ 53/2022** sau 01/07/2026: chưa tìm thấy văn bản hành chính "công bố tiếp tục có hiệu lực" theo Luật 64 Đ57 k2 (sửa bởi Luật 87). Cần tra Cơ sở dữ liệu quốc gia về pháp luật hoặc hỏi Bộ Công an. Hỏi thêm luật sư: dẫn chiếu NĐ 85 ở NĐ 331 Đ39 k1 có đủ để áp dụng thủ tục NĐ 85 đến 01/01/2027 không.
2. **Phạm vi NĐ 331 với BV tư, PK tư**: HIS nội bộ của tổ chức tư nhân có bắt buộc lập hồ sơ cấp độ không (Đ2 "khuyến khích" vs Luật 116 Đ10 k1 a; NĐ 330 Đ24 k1). **Đơn vị sự nghiệp công lập** có được coi là "tổ chức nhà nước" theo Đ2 và "tổ chức nhà nước" theo Luật Đ34 k2 (tập huấn) không. Cần luật sư hoặc hướng dẫn BCA (NĐ 331 Đ34 k1 b giao BCA hướng dẫn xác định HTTT).
3. **App đặt lịch hoặc xem kết quả có phải "dịch vụ trực tuyến thuộc ngành nghề kinh doanh có điều kiện" (KCB, STT 100) không**, hay chỉ KCB từ xa mới thuộc. Câu trả lời quyết định cấp 2 hay 3 cho cổng người bệnh dưới 10.000 người. Cần hỏi BCA (A05) hoặc BYT.
4. **SaaS y tế có phải "DN cung cấp dịch vụ trên mạng viễn thông, Internet, dịch vụ gia tăng"** theo NĐ 333 Đ3 k3–5 (định nghĩa hẹp: dịch vụ viễn thông, dịch vụ ứng dụng viễn thông, dịch vụ Internet, dịch vụ nội dung trên mạng di động, dịch vụ viễn thông giá trị gia tăng) không? Câu này quyết định nghĩa vụ lưu dữ liệu tại VN (Đ19 k2), xác thực tài khoản (Đ16 k2), log 12 tháng (Đ16 k6). Chưa đọc Luật Viễn thông 24/2023 để xem cloud và SaaS có là "dịch vụ ứng dụng viễn thông" không.
5. **Văn bản BCA còn thiếu**: Khung quản lý rủi ro ANM (NĐ 331 Đ10 k8, Đ34 k1 c); quy định giám sát, ứng phó, khắc phục sự cố (Đ28 k6); biểu mẫu, tiêu chí tự đánh giá (Đ31 k2 c); hướng dẫn xác định HTTT (Đ34 k1 b); định nghĩa "sự cố nghiêm trọng"; đầu mối và kỹ thuật kết nối Trung tâm ANM QG/tỉnh (Luật Đ40 k1 b). Chưa tìm thấy, có thể chưa ban hành tại 05/10/2026.
6. **TCVN 14423:2026**: chưa xác minh số và ngày quyết định công bố của Bộ KH&CN; bản đọc là bản đăng lại trên cổng UBND xã (Quảng Ngãi). Trang tra cứu tieuchuan.vsqi.gov.vn lỗi chứng chỉ SSL, chưa mở được.
7. **CT 07/CT-BYT**: chưa có bản gốc; chưa rõ hạn 30/09/2026 áp cho đơn vị nào (đơn vị thuộc Bộ, Sở Y tế, hay mọi cơ sở KCB kể cả tư nhân) và "cấp độ an toàn thông tin" ở đây theo khung nào.
8. **CV 365**: chưa có bản gốc ký số; yêu cầu "cloud đặt tại VN", "tối thiểu cấp độ 2", "01 bản sao lưu tại cơ sở" chỉ thấy qua bản trích của TTYT Bạc Liêu. Cần tìm trên kcb.vn hoặc nhic.vn (nhic.vn lỗi chứng chỉ khi fetch).
9. **QĐ 326/QĐ-BYT**: đọc qua OCR không dấu; con số 3 và 6 tháng cần đối chiếu bản có dấu. Chưa rõ BYT có kế hoạch thay QĐ 326 theo khung mới không.
10. **Luật Đầu tư 143/2025 Phụ lục IV và Luật 24/2026/QH16**: chỉ xác minh qua bài trên cổng xaydungchinhsach; cần đọc bản gốc để chắc STT 100, 101, 103 còn nguyên sau sửa đổi (HL 01/03/2027) và NQ cắt giảm ngành nghề (bài báo nhắc "NQ 66.17/2026/NQ-CP", chưa xác minh).
11. **Thời hạn lưu log truy cập HSBA** (khoảng trống #19): khung ANM không có con số riêng cho y tế. Cần K1 xác nhận từ TT 32/2023, TT 13/2025 hoặc dự thảo về lưu trữ HSBA.
12. **Luồng báo cáo vi phạm DLCN (K8) và báo cáo sự cố ANM (K9)**: cùng cơ quan đầu mối là BCA (A05) nhưng hai thời hạn và hai mẫu khác nhau. Cần K8 xác nhận thời hạn 72 giờ theo NĐ 356 để thiết kế quy trình gộp.
13. **QCVN 12:2026/BCA (TT 47/2026)**: có áp cho hệ thống lưu trữ hồ sơ, tài liệu điện tử (lưu trữ cơ quan) của BV công không. Cần hỏi BCA hoặc Cục Văn thư lưu trữ.
14. **NĐ 332/2026**: vendor HIS kiêm cung cấp SOC hoặc pentest cho BV có cần giấy phép kinh doanh sản phẩm, dịch vụ ANM không. Cụm này chưa đọc nội dung NĐ 332.
