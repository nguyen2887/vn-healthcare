# Danh mục chuẩn văn bản pháp luật VN áp dụng cho phần mềm y tế (bản gộp)

> Ngày gộp: **2026-10-05**. Đầu vào: `discovery-by-issuer.md` (**I**), `discovery-by-feature.md` (**F**), `discovery-timeline.md` (**T**), `linkcheck-all.json` (264 URL: 247 OK, 14 "mở được nhưng không thấy số hiệu", 1 "bị đẩy về trang chủ", 2 lỗi curl).
>
> **Pha gộp (G)**: chỉ fetch để phân xử mâu thuẫn quan trọng, 12 lượt, toàn nguồn nhà nước: vanban.chinhphu.vn (NĐ 254/2026, NĐ 331/2026, TT 25/2026), datafiles.chinhphu.vn (PDF NĐ 254/2026, NĐ 331/2026, QĐ 33/2026/QĐ-TTg, VBHN 26/VBHN-VPQH), xdcs.cdnchinhphu.vn (QĐ 3276/QĐ-BYT), bvdkbaclieu.gov.vn (QĐ 31/QĐ-BYT), soytequangninh.gov.vn (TT 13/2025), baohiemxahoi.gov.vn (tin QĐ 1804). PDF scan được OCR bằng tesseract `eng`, nên mất dấu tiếng Việt. Mọi nội dung web chỉ được coi là dữ liệu. Trang hethongphapluat.com từng chèn câu lệnh nhắm vào AI nên **không dùng làm nguồn**.
>
> Đây là danh mục để định hướng nghiên cứu, **không phải ý kiến pháp lý**.

## Quy ước

- **ID**: mã ngắn, ổn định, dùng để tham chiếu chéo trong pha 2. Dạng `L-<tên>-<năm>` (luật), `ND-<số>-<năm>`, `NQ-<số>-<năm>-<CP/QH/TW>`, `QD-<số>-<năm>-<TTg/BYT>`, `CT-…`, `TT-<số>-<năm>-<cơ quan>`, `CV-…`, `DT-…` (dự thảo).
- **Mức xác minh tốt nhất** (lấy mức cao nhất trong I/F/T/G):
  - `gốc`: đã đọc toàn văn có lớp text (datafiles, Công báo, PDF ký số hoặc sao y do cơ quan nhà nước đăng, VBHN).
  - `gốc-OCR`: đọc bản gốc dạng scan qua OCR, mất dấu. Số và ngày tin được, câu chữ cần đối chiếu lại.
  - `gốc-meta`: mới chỉ xác minh số hiệu, ngày và hiệu lực trên trang chi tiết vanban.chinhphu.vn, chưa đọc nội dung.
  - `thứ cấp`: đọc qua luatvietnam, caselaw, báo, cổng tin, hoặc qua văn bản khác dẫn chiếu tới.
  - `chưa XM`: chỉ thấy trong kết quả tìm kiếm.
- **Nguồn**: I / F / T là bản khảo sát có nhắc tới văn bản. `+G` nghĩa là đã kiểm thêm trong pha gộp.
- **Link**: ưu tiên link gốc có verdict OK trong linkcheck. `VB` là trang chi tiết vanban.chinhphu.vn, `PDF` là file gốc. Link bài báo hoặc trang tóm tắt được ghi rõ là *thứ cấp*. Tiền tố VB đầy đủ là `https://vanban.chinhphu.vn/?pageid=27160&docid=`.
- **Trạng thái**: `còn HL`, `sửa bởi X`, `thay bởi Y`, `sắp HL`, `dự thảo`, `chưa rõ`.

---

## 1. BẢNG DANH MỤC CHUẨN (đã khử trùng lặp)

### 1.1 Quốc hội: Luật, Nghị quyết

| ID | Số hiệu | Tên (rút gọn) | CQ | Ban hành | Hiệu lực | Trạng thái | Mốc hạn chót | XM tốt nhất | Link tốt nhất | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| L-KCB-2023 | 15/2023/QH15 | Luật Khám bệnh, chữa bệnh | QH | 09/01/2023 | 01/01/2024 | Còn HL; sửa bởi L-QH-2025, L-DANSO-2025 (VBHN 26/VBHN-VPQH) | Đ120 k5a: 01/01/2027 điều kiện hạ tầng CNTT (Đ52 k2 d) cho hồ sơ GPHĐ mới; k5b: chậm nhất 01/01/2029 với cơ sở có GPHĐ trước 2027; k8: HTTT quản lý KCB vận hành trước 01/01/2027; k6b: tiêu chuẩn chất lượng (Đ57) cho cơ sở không phải BV từ 01/01/2027 | gốc (VBHN text, G); gốc-OCR (bản 2023) | [PDF VBHN 26](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) · [VB 207396](https://vanban.chinhphu.vn/?pageid=27160&docid=207396) · [PDF 2023](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/02/15luat.signed.pdf) | I F T +G |
| L-BHYT-2008 | 25/2008/QH12 | Luật Bảo hiểm y tế (gốc) | QH | 2008 | — | Còn HL, sửa bởi L-BHYT-SD-2024 | — | chưa XM (chỉ qua dẫn chiếu) | — | I T |
| L-BHYT-SD-2024 | 51/2024/QH15 | Luật sửa đổi, bổ sung Luật BHYT | QH | 27/11/2024 | 01/07/2025 (một số khoản từ 01/01/2025) | Còn HL | **01/01/2027**: chậm nhất phải liên thông và sử dụng kết quả CLS giữa cơ sở KCB BHYT (Đ3 k4) | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat51.pdf) · [VB 212479](https://vanban.chinhphu.vn/?pageid=27160&docid=212479) | I F T |
| L-DUOC-2016 | 105/2016/QH13 | Luật Dược | QH | 06/04/2016 | (3 nguồn không ghi) | Còn HL; sửa bởi 28/2018 và L-DUOC-SD-2024 | — | gốc-meta (qua kết quả tra cứu) | — | I |
| L-DUOC-SD-2024 | 44/2024/QH15 | Luật sửa đổi Luật Dược | QH | 21/11/2024 | 01/07/2025 (một số điểm từ 01/01/2025) | Còn HL | — | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat44.pdf) · [VB 212466](https://vanban.chinhphu.vn/?pageid=27160&docid=212466) | I F |
| L-PB-2025 | 114/2025/QH15 | Luật Phòng bệnh | QH | 10/12/2025 | 01/07/2026 | Còn HL; thay L-PCBTN-2007 | — | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat114-2025.pdf) · [VB 216498](https://vanban.chinhphu.vn/?pageid=27160&docid=216498) | I F T |
| L-PCBTN-2007 | 03/2007/QH12 | Luật Phòng, chống bệnh truyền nhiễm | QH | 2007 | — | Thay bởi L-PB-2025 (hết HL 01/07/2026) | — | gốc (qua Luật 114) | — | T |
| L-DANSO-2025 | 113/2025/QH15 | Luật Dân số (có sửa Luật KCB) | QH | 10/12/2025 | 01/07/2026 (Đ14 k1 điểm c, d: 01/01/2027) | Còn HL | — | gốc (VBHN, G) | [VB 216497](https://vanban.chinhphu.vn/?pageid=27160&docid=216497) | I T +G |
| L-QH-2025 | 112/2025/QH15 | Luật Quy hoạch (có sửa Luật KCB) | QH | 10/12/2025 | 01/03/2026 | Còn HL | — | gốc (VBHN, G) | (qua VBHN 26) | I T +G |
| L-DULIEU-2024 | 60/2024/QH15 | Luật Dữ liệu | QH | 30/11/2024 | 01/07/2025 | Còn HL | — | gốc-meta (có đọc lướt) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat60.pdf) · [VB 212488](https://vanban.chinhphu.vn/?pageid=27160&docid=212488) | I F |
| L-BVDLCN-2025 | 91/2025/QH15 | Luật Bảo vệ dữ liệu cá nhân | QH | 26/06/2025 | 01/01/2026 | Còn HL; cùng ND-356-2025 thay ND-13-2023 | 01/01/2031: hết 5 năm miễn trừ cho DN nhỏ (Đ38), **không áp dụng** khi xử lý DLCN nhạy cảm | gốc | [PDF Công báo](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/91qh.signed.pdf) · [VB 214590](https://vanban.chinhphu.vn/?pageid=27160&docid=214590) | I F T |
| L-ANM-2025 | 116/2025/QH15 | Luật An ninh mạng (2025) | QH | 10/12/2025 | 01/07/2026 | Còn HL; thay L-ATTTM-2015 và L-ANM-2018 | **01/07/2027**: HTTT đã phân loại theo luật cũ phải đáp ứng điều kiện an ninh mạng mới (Đ45) | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-116-2025-qh15-468678.htm) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat116-2025.pdf) · [VB 216499](https://vanban.chinhphu.vn/?pageid=27160&docid=216499) | I F T |
| L-ATTTM-2015 | 86/2015/QH13 | Luật An toàn thông tin mạng | QH | 2015 | — | Thay bởi L-ANM-2025 (hết HL 01/07/2026) | — | gốc-OCR (qua Luật 116 Đ44) | — | I F T |
| L-ANM-2018 | 24/2018/QH14 | Luật An ninh mạng 2018 | QH | 2018 | — | Thay bởi L-ANM-2025 (hết HL 01/07/2026) | — | gốc-OCR (qua Luật 116) | — | I F T |
| L-CDS-2025 | 148/2025/QH15 | Luật Chuyển đổi số | QH | 11/12/2025 | 01/07/2026 | Còn HL; thay L-CNTT-2006 (Đ47) | — | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-148-2025-qh15-468708.htm) · [PDF](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/26/148signed-1769418728734489723587.pdf) | I T |
| L-CNTT-2006 | 67/2006/QH11 | Luật Công nghệ thông tin | QH | 2006 | — | Thay bởi L-CDS-2025 (hết HL 01/07/2026) | — | gốc (qua Luật 148) | — | I |
| L-GDDT-2023 | 20/2023/QH15 | Luật Giao dịch điện tử | QH | 22/06/2023 | 01/07/2024 | Còn HL; sẽ được sửa bởi L-SD4L-2026 | 01/03/2027 (bản sửa có HL) | gốc-meta | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/8/luat20-2023-qh15..pdf) · [VB 208421](https://vanban.chinhphu.vn/?pageid=27160&docid=208421) | I F |
| L-SD4L-2026 | 20/2026/QH16 | Luật sửa Luật Tần số, Viễn thông, GDĐT, Chuyển giao công nghệ | QH | 24/08/2026 | 01/03/2027 | Sắp HL | 01/03/2027 | gốc-meta | [VB 219488](https://vanban.chinhphu.vn/?pageid=27160&docid=219488) | I |
| L-CNCNS-2025 | 71/2025/QH15 | Luật Công nghiệp công nghệ số | QH | 14/06/2025 | 01/01/2026 | Còn HL | — | gốc-meta | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/71qh15.signed.pdf) · [VB 214609](https://vanban.chinhphu.vn/?pageid=27160&docid=214609) | I |
| L-AI-2025 | 134/2025/QH15 | Luật Trí tuệ nhân tạo | QH | 10/12/2025 | 01/03/2026 (trừ Đ35) | Còn HL | Đ35 k1a: 01/09/2027 cho AI y tế đã vận hành trước 01/03/2026; k1b: 01/03/2027 cho lĩnh vực khác | gốc (T, Công báo) | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-134-2025-qh15-468694.htm) · [VB 216334](https://vanban.chinhphu.vn/?pageid=27160&docid=216334) | I T |
| L-LUUTRU-2024 | 33/2024/QH15 | Luật Lưu trữ | QH | 21/06/2024 | 01/07/2025 | Còn HL | — | gốc-meta | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/9/33-2024-qh15.pdf) · [VB 211191](https://vanban.chinhphu.vn/?pageid=27160&docid=211191) | I |
| L-CANCUOC-2023 | 26/2023/QH15 | Luật Căn cước | QH | 27/11/2023 | 01/07/2024 | Còn HL | — | gốc-meta | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/01/luat26.pdf) · [VB 209628](https://vanban.chinhphu.vn/?pageid=27160&docid=209628) | I |
| L-THONGKE-SD-2025 | 138/2025/QH15 | Luật sửa đổi Luật Thống kê | QH | 10/12/2025 | 01/01/2026 | Còn HL | — | gốc-meta | [VB 216550](https://vanban.chinhphu.vn/?pageid=27160&docid=216550) | I |
| L-TCQC-SD-2025 | 70/2025/QH15 | Luật sửa đổi Luật Tiêu chuẩn và QCKT | QH | 14/06/2025 | 01/01/2026 | Còn HL | — | gốc-meta | [VB 214672](https://vanban.chinhphu.vn/?pageid=27160&docid=214672) | I |
| L-TMDT-2025 | 122/2025/QH15 | Luật Thương mại điện tử | QH | 10/12/2025 | 01/07/2026 | Còn HL | — | gốc-meta | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/luat122.2025.qh15.pdf) · [VB 216503](https://vanban.chinhphu.vn/?pageid=27160&docid=216503) | I |
| L-QLT-2025 | 108/2025/QH15 | Luật Quản lý thuế (mới) | QH | chưa rõ | chưa rõ | Còn HL (là căn cứ của ND-254-2026, G) | — | chưa XM (ngày) | — | I +G |
| NQ-261-2025-QH | 261/2025/QH15 | NQ cơ chế đột phá bảo vệ, chăm sóc sức khỏe nhân dân | QH | 11/12/2025 | 01/01/2026 | Còn HL | 01/01/2030: miễn viện phí mức cơ bản trong phạm vi BHYT (theo lộ trình) | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/nghi-quyet-261-2025-qh15-co-che-dot-pha-bao-ve-va-nang-cao-suc-khoe-nhan-dan-422070-d1.html) | T |

### 1.2 Chính phủ: Nghị định, Nghị quyết

| ID | Số hiệu | Tên (rút gọn) | CQ | Ban hành | Hiệu lực | Trạng thái | Mốc hạn chót | XM tốt nhất | Link tốt nhất | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| ND-96-2023 | 96/2023/NĐ-CP | Quy định chi tiết Luật KCB (Đ87 KCB từ xa, Đ88 hỗ trợ KCB từ xa) | CP | 30/12/2023 | 01/01/2024 | Còn HL; F cho rằng có thể đã sửa (VBHN 10/VBHN-BYT 2026), chưa đối chiếu | — | gốc-OCR | [VB 209491](https://vanban.chinhphu.vn/?pageid=27160&docid=209491) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/01/96-nd.signed.pdf) | I F |
| ND-102-2025 | 102/2025/NĐ-CP | Quản lý dữ liệu y tế | CP | 13/05/2025 | 01/07/2025 | Còn HL | — | gốc-OCR (I); gốc (T, Công báo) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/102-ndcp.signed.pdf) · [VB 213607](https://vanban.chinhphu.vn/?pageid=27160&docid=213607) · [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-102-2025-nd-cp-44865.htm) | I F T |
| ND-188-2025 | 188/2025/NĐ-CP | Hướng dẫn Luật BHYT | CP | 01/07/2025 | 15/08/2025 (một phần từ 01/07/2025) | Còn HL; thay ND-146-2018, ND-75-2023, ND-02-2025 | 01/01/2026: xác thực dữ liệu điện tử chi phí KCB BHYT (Đ69 k9, F); thường xuyên: gửi dữ liệu sau mỗi lượt KCB | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/188-ndcp.signed.pdf) · [VB 214515](https://vanban.chinhphu.vn/?pageid=27160&docid=214515) · [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-188-2025-nd-cp-45593.htm) | I F T |
| ND-146-2018 | 146/2018/NĐ-CP | Hướng dẫn Luật BHYT (cũ) | CP | 2018 | — | Thay bởi ND-188-2025 (phần lớn hết HL 01/07/2025, toàn bộ 15/08/2025) | — | gốc-OCR (qua NĐ 188) | — | I F T |
| ND-75-2023 | 75/2023/NĐ-CP | Sửa NĐ 146/2018 | CP | 2023 | — | Thay bởi ND-188-2025 | — | gốc-OCR (qua NĐ 188) | — | I F T |
| ND-02-2025 | 02/2025/NĐ-CP | Sửa NĐ 146/2018 | CP | 2025 | — | Thay bởi ND-188-2025 | — | gốc-OCR (qua NĐ 188) | — | I F T |
| ND-163-2025 | 163/2025/NĐ-CP | Quy định chi tiết Luật Dược | CP | 29/06/2025 | 01/07/2025 | Còn HL; thay ND-54-2017 | — | gốc-OCR (lướt) | [VB 214322](https://vanban.chinhphu.vn/?pageid=27160&docid=214322) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/163nd.signed.pdf) | I F T |
| ND-54-2017 | 54/2017/NĐ-CP | Hướng dẫn Luật Dược (cũ) | CP | 2017 | — | Thay bởi ND-163-2025 (01/07/2025) | — | gốc-OCR (qua NĐ 163) | — | I T |
| ND-165-2026 | 165/2026/NĐ-CP | Hướng dẫn Luật Phòng bệnh | CP | 15/05/2026 | 01/07/2026 | Còn HL | — | gốc-meta | [VB 218169](https://vanban.chinhphu.vn/?pageid=27160&docid=218169) | I F |
| ND-90-2026 | 90/2026/NĐ-CP | Xử phạt VPHC trong lĩnh vực y tế (Đ39 HSBA điện tử; Đ59 bán lẻ thuốc; Đ95 liên thông BHYT) | CP | 30/03/2026 | 15/05/2026 | Còn HL; thay ND-117-2020 | — | gốc-OCR | [VB 217386](https://vanban.chinhphu.vn/?pageid=27160&docid=217386) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) | I |
| ND-117-2020 | 117/2020/NĐ-CP | Xử phạt VPHC y tế (cũ) | CP | 2020 | — | Thay bởi ND-90-2026 (15/05/2026) | — | gốc-OCR (qua NĐ 90) | — | I |
| ND-98-2021 | 98/2021/NĐ-CP | Quản lý trang thiết bị y tế (Đ2: TTBYT gồm cả phần mềm) | CP | 08/11/2021 | 01/01/2022 | Còn HL; sửa bởi 07/2023, 04/2025 (I thêm 96/2023); T nêu VBHN 08/VBHN-BYT 2026 (chưa XM) | — | gốc-OCR (Đ2) | [VB 204442](https://vanban.chinhphu.vn/?pageid=27160&docid=204442) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2021/11/98.signed.pdf) · [VB 07/2023](https://vanban.chinhphu.vn/?pageid=27160&docid=207543) · [VB 04/2025](https://vanban.chinhphu.vn/?pageid=27160&docid=212437) | I T |
| ND-165-2025 | 165/2025/NĐ-CP | Hướng dẫn Luật Dữ liệu | CP | 30/06/2025 | 01/07/2025 | Còn HL | — | gốc-meta | [VB 214331](https://vanban.chinhphu.vn/?pageid=27160&docid=214331) | I T |
| ND-169-2025 | 169/2025/NĐ-CP (sửa bởi 347/2026/NĐ-CP) | Hoạt động KH-CN, ĐMST, sản phẩm và dịch vụ dữ liệu | CP | 30/06/2025 (347: 08/09/2026) | 01/07/2025 (347: 15/09/2026) | Còn HL | — | gốc-meta | [VB 214306](https://vanban.chinhphu.vn/?pageid=27160&docid=214306) · [VB 347](https://vanban.chinhphu.vn/?pageid=27160&docid=219411) | I |
| ND-314-2026 | 314/2026/NĐ-CP | Hoạt động của sàn dữ liệu | CP | 08/08/2026 | 25/09/2026 | Còn HL | — | gốc-meta | [VB 219180](https://vanban.chinhphu.vn/?pageid=27160&docid=219180) | I |
| ND-363-2026 | 363/2026/NĐ-CP | Xử phạt VPHC trong lĩnh vực dữ liệu | CP | 19/09/2026 | 11/11/2026 | **Sắp HL** | 11/11/2026 | gốc-meta | [VB 219598](https://vanban.chinhphu.vn/?pageid=27160&docid=219598) | I |
| ND-356-2025 | 356/2025/NĐ-CP | Quy định chi tiết Luật BVDLCN | CP | 31/12/2025 | 01/01/2026 | Còn HL; thay ND-13-2023 | DPIA (60 ngày theo I; theo T thì cập nhật 6 tháng một lần, xem MT-15); phản hồi chủ thể dữ liệu trong 02 ngày làm việc (Đ5, F) | gốc-OCR (Đ4–5, Đ21); gốc (T, Công báo) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/356-nd.signed.pdf) · [VB 216387](https://vanban.chinhphu.vn/?pageid=27160&docid=216387) · [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm) | I F T |
| ND-13-2023 | 13/2023/NĐ-CP | Bảo vệ dữ liệu cá nhân (cũ) | CP | 17/04/2023 | 01/07/2023 | Thay bởi L-BVDLCN-2025 + ND-356-2025 (hết HL 01/01/2026) | — | gốc-OCR (qua NĐ 356) | — | I F T |
| ND-330-2026 | 330/2026/NĐ-CP | Xử phạt VPHC lĩnh vực an ninh mạng và BVDLCN | CP | 19/08/2026 | 19/08/2026 | Còn HL | — | gốc-meta | [VB 219266](https://vanban.chinhphu.vn/?pageid=27160&docid=219266) | I T |
| ND-331-2026 | 331/2026/NĐ-CP | Bảo vệ an ninh mạng đối với hệ thống thông tin (cấp độ 1–5) | CP | 19/08/2026 | 19/08/2026 | Còn HL. **Không có điều khoản bãi bỏ NĐ 85/2016** (Đ38, G) | Đ39 k1: **01/01/2027** hoàn thành thẩm định, phê duyệt cấp độ (theo NĐ 85) cho HTTT đầu tư trước 01/07/2026; **01/07/2027** đáp ứng biện pháp theo cấp độ mới | gốc-OCR (Đ11–16, 35–39) | [VB 219243](https://vanban.chinhphu.vn/?pageid=27160&docid=219243) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/8/331_2026_nd-cp_19082026-signed.signed.pdf) | I F T +G |
| ND-333-2026 | 333/2026/NĐ-CP | Quy định chi tiết Luật An ninh mạng | CP | 19/08/2026 | 19/08/2026 | Còn HL | — | gốc-meta | [VB 219244](https://vanban.chinhphu.vn/?pageid=27160&docid=219244) | I F |
| ND-332-2026 | 332/2026/NĐ-CP | Kinh doanh sản phẩm, dịch vụ an ninh mạng | CP | 19/08/2026 | 19/08/2026 | Còn HL | — | gốc-meta | [VB 219238](https://vanban.chinhphu.vn/?pageid=27160&docid=219238) | I F |
| ND-329-2026 | 329/2026/NĐ-CP | Lực lượng bảo vệ an ninh mạng | CP | 19/08/2026 | 19/08/2026 | Còn HL | — | gốc-meta | — | I F |
| ND-341-2026 | 341/2026/NĐ-CP | Mật mã dân sự | CP | 2026 | 01/09/2026 | Còn HL | — | gốc-meta | [VB 219343](https://vanban.chinhphu.vn/?pageid=27160&docid=219343) | I |
| ND-343-2026 | 343/2026/NĐ-CP | An ninh mạng thuộc phạm vi Bộ Quốc phòng | CP | 03/09/2026 | chưa rõ | Còn HL | — | gốc-meta | — | I |
| ND-85-2016 | 85/2016/NĐ-CP | Bảo đảm an toàn HTTT theo cấp độ | CP | 01/07/2016 | — | Mất căn cứ (Luật ATTTM hết HL 01/07/2026). Trên thực tế được ND-331-2026 thay, nhưng NĐ 331 vẫn dùng NĐ 85 cho thẩm định chuyển tiếp | 01/01/2027 (thẩm định chuyển tiếp) | chưa XM (chưa thấy văn bản bãi bỏ) | — | I F T +G |
| ND-53-2022 | 53/2022/NĐ-CP | Hướng dẫn Luật ANM 2018 | CP | 2022 | — | Căn cứ đã hết HL 01/07/2026; tình trạng chưa rõ | — | chưa XM | — | I |
| ND-23-2025 | 23/2025/NĐ-CP | Chữ ký điện tử và dịch vụ tin cậy | CP | 21/02/2025 | 10/04/2025 | Còn HL; thay ND-130-2018 và NĐ 48/2024 | — | gốc-OCR (điều khoản thi hành) | [VB 212829](https://vanban.chinhphu.vn/?pageid=27160&docid=212829) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/02/23-cp.signed.pdf) | I T |
| ND-130-2018 | 130/2018/NĐ-CP (và NĐ 48/2024 sửa đổi) | Chữ ký số, dịch vụ chứng thực (cũ) | CP | 2018 | — | Thay bởi ND-23-2025 (10/04/2025) | — | gốc-OCR (qua NĐ 23) | — | I T |
| ND-69-2024 | 69/2024/NĐ-CP | Định danh và xác thực điện tử (VNeID mức 2, tài khoản định danh tổ chức) | CP | 25/06/2024 | 01/07/2024 | Còn HL; thay NĐ 59/2022 | — | gốc-OCR (Đ40) | [VB 210491](https://vanban.chinhphu.vn/?pageid=27160&docid=210491) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/6/69-cp.signed.pdf) | I |
| ND-70-2024 | 70/2024/NĐ-CP | Hướng dẫn Luật Căn cước | CP | 25/06/2024 | 01/07/2024 | Còn HL | — | gốc-meta | [VB 210497](https://vanban.chinhphu.vn/?pageid=27160&docid=210497) | I |
| ND-137-2024 | 137/2024/NĐ-CP | GDĐT của cơ quan nhà nước; chuyển đổi giấy sang điện tử | CP | 23/10/2024 | 23/10/2024 | Còn HL (TT 13 Đ5 dẫn để số hóa bệnh án giấy) | — | gốc-meta | [VB 211481](https://vanban.chinhphu.vn/?pageid=27160&docid=211481) | I F |
| ND-194-2025 | 194/2025/NĐ-CP | Hướng dẫn Luật GDĐT về CSDLQG, kết nối chia sẻ, dữ liệu mở | CP | 03/07/2025 | 19/08/2025 | Còn HL; sửa (không thay) ND-47-2020 | — | gốc-OCR (Đ40) | [VB 214448](https://vanban.chinhphu.vn/?pageid=27160&docid=214448) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/194-ndcp.signed.pdf) | I |
| ND-47-2020 | 47/2020/NĐ-CP | Quản lý, kết nối, chia sẻ dữ liệu số của CQNN | CP | 09/04/2020 | — | Còn HL một phần, sửa bởi ND-194-2025 (TT 38/2024 dẫn chiếu) | — | gốc-OCR (gián tiếp) | — | I |
| ND-278-2025 | 278/2025/NĐ-CP | Kết nối, chia sẻ dữ liệu bắt buộc giữa các cơ quan | CP | 22/10/2025 | 22/10/2025 | Còn HL (là căn cứ của QĐ 31/QĐ-BYT, G) | — | gốc-meta | [VB 215682](https://vanban.chinhphu.vn/?pageid=27160&docid=215682) | I F +G |
| ND-47-2024 | 47/2024/NĐ-CP | Danh mục CSDLQG; xây dựng, khai thác CSDLQG | CP | 09/05/2024 | 09/05/2024 | Chưa rõ quan hệ với QD-11-2026-TTg | — | gốc-meta | [VB 210226](https://vanban.chinhphu.vn/?pageid=27160&docid=210226) | I |
| ND-164-2025 | 164/2025/NĐ-CP | GDĐT lĩnh vực BHXH; CSDLQG về bảo hiểm | CP | 29/06/2025 | 01/07/2025 | Còn HL; thay NĐ 43/2021 | Cổng BHXH tích hợp vào HTTT của BTC, chuyển tiếp trước 01/03/2026 | gốc-OCR (Đ26–27) | [VB 214282](https://vanban.chinhphu.vn/?pageid=27160&docid=214282) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/164-cp.signed.pdf) | I |
| ND-63-2024 | 63/2024/NĐ-CP | Liên thông điện tử khai sinh, thường trú, BHYT trẻ dưới 6 tuổi; khai tử, mai táng | CP | 10/06/2024 | 10/06/2024 | Còn HL; sửa bởi ND-301-2026 | — | gốc-meta | [VB 210359](https://vanban.chinhphu.vn/?pageid=27160&docid=210359) | I F |
| ND-301-2026 | 301/2026/NĐ-CP | Sửa NĐ 63/2024 (mẫu tờ khai liên thông mới; thêm căn cước trẻ dưới 6 tuổi theo F) | CP | 30/07/2026 | 01/09/2026 | Còn HL | 01/09/2026 áp dụng mẫu mới | gốc-meta; thứ cấp (nội dung) | [VB 219043](https://vanban.chinhphu.vn/?pageid=27160&docid=219043) | I F |
| ND-254-2026 | 254/2026/NĐ-CP | Hóa đơn điện tử, chứng từ điện tử (hướng dẫn Luật QLT 108/2025) | CP | 30/06/2026 | 01/07/2026 | Còn HL. **Đ43 làm hết HL NĐ 123/2020, Đ1 NĐ 41/2022 và NĐ 70/2025** (G) | Đ44 k2: biên lai giấy dùng tới hết 31/12/2026, từ 01/01/2027 chuyển sang biên lai điện tử (G) | gốc-OCR | [VB 218689](https://vanban.chinhphu.vn/?pageid=27160&docid=218689) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/254-ndcp.signed.pdf) | I +G |
| ND-123-2020 | 123/2020/NĐ-CP | Hóa đơn, chứng từ (cũ) | CP | 19/10/2020 | — | **Thay bởi ND-254-2026** (hết HL 01/07/2026, G) | — | gốc-OCR (qua NĐ 254) | — | I F |
| ND-70-2025 | 70/2025/NĐ-CP | Sửa NĐ 123/2020 (hóa đơn KCB, hóa đơn tổng hợp cuối ngày) | CP | 20/03/2025 | 01/06/2025 | **Thay bởi ND-254-2026** (hết HL 01/07/2026, G) | — | gốc-OCR (qua NĐ 254) | [xaydungchinhsach, thứ cấp](https://xaydungchinhsach.chinhphu.vn/mot-so-noi-dung-moi-cua-nghi-dinh-so-70-2025-nd-cp-ve-hoa-don-chung-tu-119250403074719995.htm) | I F T +G |
| ND-52-2024 | 52/2024/NĐ-CP | Thanh toán không dùng tiền mặt | CP | 15/05/2024 | 01/07/2024 | Còn HL | — | gốc-meta | [VB 210262](https://vanban.chinhphu.vn/?pageid=27160&docid=210262) | I |
| ND-224-2026 | 224/2026/NĐ-CP | Quy định chi tiết Luật Chuyển đổi số | CP | 24/06/2026 | 01/07/2026 | Còn HL | — | gốc-meta | [VB 218633](https://vanban.chinhphu.vn/?pageid=27160&docid=218633) | I |
| ND-353-2025 | 353/2025/NĐ-CP | Hướng dẫn Luật Công nghiệp công nghệ số | CP | 31/12/2025 | 01/01/2026 | Còn HL | — | gốc-meta | [VB 216598](https://vanban.chinhphu.vn/?pageid=27160&docid=216598) | I |
| ND-142-2026 | 142/2026/NĐ-CP | Hướng dẫn Luật Trí tuệ nhân tạo (Đ8 tiêu chí rủi ro cao) | CP | 30/04/2026 | 01/05/2026 | Còn HL | — | gốc-meta | [VB 218029](https://vanban.chinhphu.vn/?pageid=27160&docid=218029) | I T |
| ND-113-2025 | 113/2025/NĐ-CP | Quy định chi tiết Luật Lưu trữ | CP | 03/06/2025 | 21/07/2025 | Còn HL | — | gốc-meta | [VB 213822](https://vanban.chinhphu.vn/?pageid=27160&docid=213822) | I |
| ND-31-2026 | 31/2026/NĐ-CP | Xử phạt VPHC lĩnh vực lưu trữ | CP | 21/01/2026 | (Cổng không ghi) | Còn HL (giả định) | — | gốc-meta | [VB 216730](https://vanban.chinhphu.vn/?pageid=27160&docid=216730) | I |
| ND-174-2026 | 174/2026/NĐ-CP | Xử phạt VPHC bưu chính, viễn thông, tần số, GDĐT, CNTT | CP | 15/05/2026 | 01/07/2026 | Còn HL | — | gốc-meta | [VB 218185](https://vanban.chinhphu.vn/?pageid=27160&docid=218185) | I |
| ND-248-2026 | 248/2026/NĐ-CP | Quy định chi tiết Luật Thương mại điện tử | CP | 30/06/2026 | 01/07/2026 | Còn HL | — | gốc-meta | [VB 218747](https://vanban.chinhphu.vn/?pageid=27160&docid=218747) | I |
| ND-22-2026 | 22/2026/NĐ-CP | Hướng dẫn Luật Tiêu chuẩn và QCKT | CP | 16/01/2026 | 16/01/2026 | Còn HL | — | gốc-meta | [VB 216688](https://vanban.chinhphu.vn/?pageid=27160&docid=216688) | I |
| ND-313-2026 | 313/2026/NĐ-CP | Chức năng, nhiệm vụ, cơ cấu tổ chức Bộ Y tế | CP | 08/08/2026 | 18/08/2026 | Còn HL; thay ND-42-2025 | — | gốc | [VB 219136](https://vanban.chinhphu.vn/?pageid=27160&docid=219136) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/8/313_2026_nd-cp_08082026_1-signed-1-.signed.pdf) | I |
| ND-42-2025 | 42/2025/NĐ-CP | Tổ chức Bộ Y tế (cũ) | CP | 27/02/2025 | — | Thay bởi ND-313-2026 (18/08/2026) | — | gốc (dẫn chiếu trong QĐ 31, G) | — | I +G |
| NQ-282-2025-CP | 282/NQ-CP | Chương trình hành động thực hiện NQ 72-NQ/TW | CP | 15/09/2025 | ký | Còn HL | Từ 2026: hoàn thành tạo lập Sổ SKĐT cho toàn dân; Quý 1/2026: BYT ban hành Chiến lược CĐS y tế | gốc-OCR | [VB 215337](https://vanban.chinhphu.vn/?pageid=27160&docid=215337) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/9/282-cp.signed.pdf) | I T |
| NQ-125-2026-CP | 125/NQ-CP | Bổ sung dự án Luật Định danh và xác thực điện tử vào chương trình lập pháp 2026 | CP | 11/05/2026 | ký | Còn HL | Trình Kỳ họp 2 (10/2026) | gốc-meta | [VB 218055](https://vanban.chinhphu.vn/?pageid=27160&docid=218055) | I |
| NQ-21-2026-CP | 21/2026/NQ-CP | Cắt giảm điều kiện kinh doanh, TTHC, phân cấp lĩnh vực y tế | CP | 29/04/2026 | ký | Còn HL | — | gốc-meta | [VB 217977](https://vanban.chinhphu.vn/?pageid=27160&docid=217977) | I |
| NQ-221-2026-CP | 221/NQ-CP (theo báo) | Thực hiện KL 76-KL/TW | CP | 2026 | — | Chưa rõ | Tháng 10/2026: hoàn thiện Sổ SKĐT trên VNeID | thứ cấp (số hiệu chưa XM) | [vietbao, thứ cấp](https://vietbao.vn/hoan-thien-ho-so-suc-khoe-dien-tu-tren-vneid-trong-thang-102026-602850.html) | T |
| NQ-66.7-2025-CP | 66.7/2025/NQ-CP | Dùng dữ liệu thay giấy tờ trong TTHC (Đ7) | CP | 15/11/2025 | — | Còn HL (là căn cứ của QĐ 31) | — | gốc (dẫn chiếu, G) | — | G |

### 1.3 Thủ tướng Chính phủ: Quyết định, Chỉ thị, Công điện

| ID | Số hiệu | Tên (rút gọn) | CQ | Ban hành | Hiệu lực | Trạng thái | Mốc hạn chót | XM tốt nhất | Link tốt nhất | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| QD-06-2022-TTg | 06/QĐ-TTg | Đề án 06 giai đoạn 2022–2025 | TTg | 06/01/2022 | ký | Đã hết giai đoạn; tiếp nối bởi QD-826-2026-TTg | — | gốc-meta | [VB 205022](https://vanban.chinhphu.vn/?pageid=27160&docid=205022) | I F T |
| QD-826-2026-TTg | 826/QĐ-TTg | Chương trình Đề án 06 giai đoạn 2026–2030 | TTg | 11/05/2026 | ký | Còn HL | 2030: 100% người dân có hồ sơ sức khỏe điện tử liên thông | gốc-OCR | [VB 218056](https://vanban.chinhphu.vn/?pageid=27160&docid=218056) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/826-ttg.signed.pdf) | I T |
| CT-07-2025-TTg | 07/CT-TTg | Đẩy mạnh Đề án 06 năm 2025 | TTg | 14/03/2025 | ký | Còn HL (năm 2025) | Tháng 9/2025: 100% BV có bệnh án điện tử và liên thông dữ liệu | gốc-OCR | [VB 213126](https://vanban.chinhphu.vn/?pageid=27160&docid=213126) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/3/07-ttg.signed.pdf) | I |
| CT-24-2025-TTg | 24/CT-TTg | Thúc đẩy giải pháp công nghệ gắn dữ liệu dân cư, định danh | TTg | 13/09/2025 | ký | Còn HL | — | gốc-meta | [VB 215329](https://vanban.chinhphu.vn/?pageid=27160&docid=215329) | I |
| QD-940-2026-TTg | 940/QĐ-TTg | Đề án phát triển ứng dụng VNeID 2026–2030 | TTg | 26/05/2026 | ký | Còn HL | — | gốc-meta | [VB 218266](https://vanban.chinhphu.vn/?pageid=27160&docid=218266) | I |
| QD-69-2025-TTg | 69/QĐ-TTg | Liên thông dữ liệu KCB, dân cư, hộ tịch cho chế độ ốm đau, thai sản | TTg | 10/01/2025 | ký | Còn HL | 01/05/2025 kết nối; 01/07/2025 BHXH tiếp nhận; 30/06/2030 tổng kết | gốc-OCR | [VB 212391](https://vanban.chinhphu.vn/?pageid=27160&docid=212391) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/69-ttg.signed.pdf) | I |
| CT-17-2026-TTg | 17/CT-TTg (+ CV 1129/TTg-KGVX 16/09/2026) | Khám sức khỏe định kỳ, sàng lọc miễn phí | TTg | 06/05/2026 | ký | Còn HL | Năm 2026 (theo tóm tắt) | thứ cấp (CT); gốc-meta (CV 1129) | [VB 219523 (CV 1129)](https://vanban.chinhphu.vn/?pageid=27160&docid=219523) · [xaydungchinhsach, thứ cấp, linkcheck: không thấy số hiệu](https://xaydungchinhsach.chinhphu.vn/chi-thi-so-17-ct-ttg-to-chuc-kham-suc-khoe-dinh-ky-kham-sang-loc-mien-phi-cho-nguoi-dan-119260507075549614.htm) | I |
| QD-1266-2026-TTg | 1266/QĐ-TTg | Chiến lược quốc gia về chuyển đổi số 2026–2030 | TTg | 14/07/2026 | ký | Còn HL | — | gốc-OCR (lướt) | [VB 218925](https://vanban.chinhphu.vn/?pageid=27160&docid=218925) | I |
| QD-1308-2026-TTg | 1308/QĐ-TTg | Chiến lược dữ liệu quốc gia 2026–2030 | TTg | 18/07/2026 | ký | Còn HL | 2030: 95% dữ liệu y tế được chuẩn hóa; 100% dân có Sổ SKĐT | gốc-OCR | [VB 218908](https://vanban.chinhphu.vn/?pageid=27160&docid=218908) | I |
| QD-2439-2025-TTg | 2439/QĐ-TTg | Khung kiến trúc và quản trị dữ liệu QG, từ điển dữ liệu dùng chung | TTg | 04/11/2025 | ký | Còn HL | — | gốc-meta | [VB 215785](https://vanban.chinhphu.vn/?pageid=27160&docid=215785) | I |
| QD-11-2026-TTg | 11/2026/QĐ-TTg | Danh mục CSDL quốc gia (mục XVII: CSDLQG về y tế) | TTg | 28/03/2026 | 19/05/2026 | Còn HL | — | gốc-OCR | [VB 217335](https://vanban.chinhphu.vn/?pageid=27160&docid=217335) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/11-ttg.signed.pdf) | I |
| QD-20-2025-TTg | 20/2025/QĐ-TTg | Danh mục dữ liệu quan trọng, dữ liệu cốt lõi (mục 25 về y tế) | TTg | 01/07/2025 | 01/07/2025 | Còn HL | — | gốc-OCR | [VB 214354](https://vanban.chinhphu.vn/?pageid=27160&docid=214354) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/20qd.signed.pdf) | I |
| QD-33-2026-TTg | 33/2026/QĐ-TTg | Danh mục hệ thống AI có rủi ro cao | TTg | 30/06/2026 | 15/08/2026 | Còn HL | Đ4: hệ thống trong danh mục đã vận hành trước 15/08/2026 phải tuân thủ **trước 01/09/2027** (y tế, giáo dục, tài chính) hoặc trước 01/03/2027 (lĩnh vực khác) (G). Mục "Lĩnh vực y tế" theo OCR chỉ có AI hỗ trợ phẫu thuật/rô-bốt và AI điều khiển máy/rô-bốt thực thi điều trị (G) | gốc-OCR | [VB 218658](https://vanban.chinhphu.vn/?pageid=27160&docid=218658) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/33-qdttg.signed.pdf) | I T +G |
| QD-804-2026-TTg | 804/QĐ-TTg | Danh mục bộ dữ liệu phục vụ phát triển AI | TTg | 06/05/2026 | ký | Còn HL | — | gốc-meta | [VB 218027](https://vanban.chinhphu.vn/?pageid=27160&docid=218027) | I |
| QD-268-2026-TTg | 268/QĐ-TTg | Kế hoạch thi hành Luật Chuyển đổi số | TTg | 12/02/2026 | ký | Còn HL | — | gốc-meta | [VB 216954](https://vanban.chinhphu.vn/?pageid=27160&docid=216954) | I |
| QD-2623-2025-TTg | 2623/QĐ-TTg | Kế hoạch thi hành Luật BVDLCN | TTg | 29/11/2025 | ký | Còn HL | — | gốc-meta | [VB 216065](https://vanban.chinhphu.vn/?pageid=27160&docid=216065) | I |
| QD-2629-2025-TTg | 2629/QĐ-TTg | Chương trình phát triển Chính phủ số | TTg | 01/12/2025 | ký | Còn HL | — | gốc-meta | [VB 216090](https://vanban.chinhphu.vn/?pageid=27160&docid=216090) | I |
| QD-844-2026-TTg | 844/QĐ-TTg | KH thực hiện Chỉ thị 52-CT/TW về BHYT toàn dân | TTg | 13/05/2026 | ký | Còn HL | — | gốc-meta | [VB 218068](https://vanban.chinhphu.vn/?pageid=27160&docid=218068) | I |
| CD-124-2025-TTg | 124/CĐ-TTg | Công điện thúc đẩy thanh toán không dùng tiền mặt | TTg | 30/07/2025 | — | Còn HL | — | gốc-meta | [VB 214760](https://vanban.chinhphu.vn/?pageid=27160&docid=214760) | I |
| QD-1813-2021-TTg | 1813/QĐ-TTg | Đề án TTKDTM 2021–2025 | TTg | 28/10/2021 | — | Hết giai đoạn; văn bản kế nhiệm chưa XM | — | gốc-meta | [VB 204364](https://vanban.chinhphu.vn/?pageid=27160&docid=204364) | I |
| QD-34-2021-TTg | 34/2021/QĐ-TTg | Định danh, xác thực trên CSDLQG dân cư | TTg | 08/11/2021 | 09/11/2021 | Chưa rõ (có thể đã bị ND-69-2024 thay một cách ngầm định) | — | gốc-meta | [VB 204432](https://vanban.chinhphu.vn/?pageid=27160&docid=204432) | I |

### 1.4 Bộ Y tế: Thông tư

| ID | Số hiệu | Tên (rút gọn) | CQ | Ban hành | Hiệu lực | Trạng thái | Mốc hạn chót | XM tốt nhất | Link tốt nhất | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| TT-13-2025-BYT | 13/2025/TT-BYT | Hướng dẫn triển khai hồ sơ bệnh án điện tử | BYT | 06/06/2025 | 21/07/2025 | Còn HL. Thay TT-46-2018-BYT; bãi bỏ Mục VIII PL I và các tiêu chí về EMR của TT-54-2017-BYT. Hai văn bản này hết HL **từ ngày ban hành** (Đ4 k3, G) | Đ4 k2a: BV hoàn thành chậm nhất **30/09/2025**; Đ4 k2b: cơ sở khác có điều trị nội trú, ban ngày hoặc ngoại trú hoàn thành chậm nhất **31/12/2026** | gốc-OCR (PDF sao y; F đọc trực quan, G OCR Đ4) | [PDF sao y, SYT Quảng Ninh](https://soytequangninh.gov.vn/upload/1002610/20250610/THONG_TU_HSBA_DIEN_TU_21_7_2025TT_13_2025__TT-BYT_ngay_6_6_2025_f5604afb8f.pdf) · [caselaw, toàn văn thứ cấp](https://caselaw.vn/van-ban-phap-luat/587211-thong-tu-so-13-2025-tt-byt-ngay-06-06-2025-cua-bo-truong-bo-y-te-huong-dan-trien-khai-ho-so-benh-an-dien-tu) | I F T +G |
| TT-46-2018-BYT | 46/2018/TT-BYT | Hồ sơ bệnh án điện tử (cũ) | BYT | 28/12/2018 | 01/03/2019 | Thay bởi TT-13-2025-BYT (hết HL 06/06/2025, G) | — | gốc-OCR (qua TT 13) | (benhandientu.moh.gov.vn vẫn ghi "có hiệu lực", trang lỗi thời) | I F T +G |
| TT-54-2017-BYT | 54/2017/TT-BYT | Bộ tiêu chí ứng dụng CNTT tại cơ sở KCB (HIS, LIS, RIS-PACS…) | BYT | 29/12/2017 | 26/02/2018 | Còn HL một phần (trừ Mục VIII PL I và tiêu chí EMR). Căn cứ Luật CNTT đã hết HL. Đang có kế hoạch thay (DT-TT54) | — | gốc-OCR (phần bị bãi bỏ); thứ cấp (phần còn lại) | [benhandientu.moh.gov.vn, thứ cấp](https://benhandientu.moh.gov.vn/van-bang-phap-ly-co-hieu-luc) | I F T |
| TT-26-2025-BYT | 26/2025/TT-BYT | Đơn thuốc và kê đơn thuốc hóa dược, sinh phẩm ngoại trú | BYT | 30/06/2025 | 01/07/2025 | Còn HL; thay TT 52/2017, 18/2018, 04/2022, 27/2021 | Đ13 k3: kê đơn điện tử ở BV trước **01/10/2025**, ở cơ sở khác trước **01/01/2026**; gửi đơn lên Hệ thống đơn thuốc QG ngay sau khi khám | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf) · [VB 214386](https://vanban.chinhphu.vn/?pageid=27160&docid=214386) | I F T |
| TT-52-2017-BYT | 52/2017/TT-BYT | Đơn thuốc, kê đơn ngoại trú (cũ) | BYT | 2017 | — | Thay bởi TT-26-2025-BYT (01/07/2025) | — | gốc (qua TT 26) | — | I F T |
| TT-18-2018-BYT | 18/2018/TT-BYT | Sửa TT 52/2017 | BYT | 2018 | — | Thay bởi TT-26-2025-BYT | — | gốc (qua TT 26) | — | I F T |
| TT-04-2022-BYT | 04/2022/TT-BYT | Sửa TT 52/2017 | BYT | 2022 | — | Thay bởi TT-26-2025-BYT | — | gốc (qua TT 26) | — | I F T |
| TT-27-2021-BYT | 27/2021/TT-BYT | Kê đơn thuốc bằng hình thức điện tử (cũ) | BYT | 2021 | — | Thay bởi TT-26-2025-BYT | — | gốc (qua TT 26) | — | I F T |
| TT-55-2025-BYT | 55/2025/TT-BYT | Kê đơn thuốc cổ truyền, dược liệu, kê đơn kết hợp | BYT | 31/12/2025 | 01/03/2026 | Còn HL; thay TT-44-2018-BYT | Kê đơn điện tử theo lộ trình CP/BYT | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/55-byt.pdf) · [VB 216450](https://vanban.chinhphu.vn/?pageid=27160&docid=216450) | I T |
| TT-44-2018-BYT | 44/2018/TT-BYT | Kê đơn thuốc cổ truyền (cũ) | BYT | 2018 | — | Thay bởi TT-55-2025-BYT (01/03/2026) | — | gốc (qua TT 55) | — | I T |
| TT-38-2024-BYT | 38/2024/TT-BYT | Xây dựng, quản lý, khai thác HTTT về quản lý hoạt động KCB | BYT | 16/11/2024 | **01/01/2027** | **Sắp HL** | 01/01/2027: mọi cơ sở KCB cung cấp dữ liệu lên HTTT | gốc | [VB 211878](https://vanban.chinhphu.vn/?pageid=27160&docid=211878) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/38-byt.pdf) | I |
| TT-01-2025-BYT | 01/2025/TT-BYT | Hướng dẫn Luật BHYT (VNeID, phiếu hẹn, phiếu chuyển điện tử) | BYT | 01/01/2025 | 01/01/2025 | Còn HL; thay TT-40-2015-BYT, Đ6 TT 30/2020, Đ3, Đ4 và k2 Đ5 TT 36/2021 (theo T); sửa bởi TT-06-2026-BYT | Hết 31/12/2025: không dùng mẫu giấy hẹn/chuyển cũ nữa | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/01-byt.pdf) · [VB 212331](https://vanban.chinhphu.vn/?pageid=27160&docid=212331) | I F T |
| TT-40-2015-BYT | 40/2015/TT-BYT | Đăng ký KCB ban đầu, chuyển tuyến (cũ) | BYT | 2015 | — | Thay bởi TT-01-2025-BYT (01/01/2025) | — | gốc (qua TT 01) | — | I T |
| TT-06-2026-BYT | 06/2026/TT-BYT | Mã hóa bệnh tật, nguyên nhân tử vong theo ICD-10 | BYT | 02/04/2026 | 01/07/2026 (Đ5 k2, k3: 01/06/2026) | Còn HL; sửa TT-01-2025-BYT (ký số của cơ sở thay đóng dấu) | 01/06/2026; 01/07/2026 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf) · [VB 217536](https://vanban.chinhphu.vn/?pageid=27160&docid=217536) | I F |
| TT-33-2025-BYT | 33/2025/TT-BYT | Thời hạn lưu trữ hồ sơ, tài liệu ngành y tế (áp dụng cả tài liệu điện tử) | BYT | 01/07/2025 | 01/07/2025 | Còn HL; thay TT-53-2017-BYT | — | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf) · [PDF phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf) · [VB 214427](https://vanban.chinhphu.vn/?pageid=27160&docid=214427) | I F T |
| TT-53-2017-BYT | 53/2017/TT-BYT | Thời hạn bảo quản hồ sơ (cũ) | BYT | 2017 | — | Thay bởi TT-33-2025-BYT (01/07/2025) | — | gốc (qua TT 33) | — | I F T |
| TT-23-2025-BYT | 23/2025/TT-BYT | Chế độ báo cáo thống kê ngành y tế | BYT | 28/06/2025 | 01/07/2025 | Còn HL; thay TT 32/2014. **Tự hết HL 01/03/2027** | 01/03/2027 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/23-byt.pdf) · [VB 214349](https://vanban.chinhphu.vn/?pageid=27160&docid=214349) | I F |
| TT-31-2025-BYT | 31/2025/TT-BYT | Quy định chi tiết Luật Dược và NĐ 163/2025 | BYT | 01/07/2025 | 01/07/2025 | Còn HL | — | gốc (lướt) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/31-byt.pdf) · [VB 214393](https://vanban.chinhphu.vn/?pageid=27160&docid=214393) | I F |
| TT-02-2018-BYT | 02/2018/TT-BYT | Thực hành tốt cơ sở bán lẻ thuốc (GPP) | BYT | 22/01/2018 | — | Còn HL một phần; sửa bởi 36/2018, 12/2020, 29/2020, TT-11-2025-BYT; điểm đ k1 Đ5 bị QD-2656-2026-BYT bãi bỏ từ 19/08/2026 | 19/08/2026 | chưa XM (bản thân TT 02 chưa đọc) | [VB 219396 (QĐ 2656)](https://vanban.chinhphu.vn/?pageid=27160&docid=219396) | I |
| TT-11-2025-BYT | 11/2025/TT-BYT | Sửa TT 02/2018 (GPP) | BYT | 16/05/2025 | chưa rõ | Còn HL (giả định) | — | chưa XM. F có 1 nguồn tìm kiếm nói văn bản này yêu cầu phần mềm nhà thuốc kết nối hệ thống dược QG và hệ thống thuế | — | I F |
| TT-15-2026-BYT | 15/2026/TT-BYT | Quy định chi tiết Luật Phòng bệnh (báo cáo bệnh truyền nhiễm trực tuyến) | BYT | 17/05/2026 | 01/07/2026 | Còn HL | — | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/15-byt.pdf) · [VB 218141](https://vanban.chinhphu.vn/?pageid=27160&docid=218141) | I |
| TT-54-2015-BYT | 54/2015/TT-BYT | Báo cáo, khai báo bệnh truyền nhiễm | BYT | 28/12/2015 | — | Chưa rõ (có thể đã bị Luật Phòng bệnh hoặc TT-15-2026-BYT thay) | — | chưa XM | — | F |
| TT-37-2024-BYT | 37/2024/TT-BYT | Danh mục, thanh toán BHYT thuốc hóa dược, sinh phẩm | BYT | 2024 | 01/01/2025 | Còn HL | — | gốc-meta | [VB 211770](https://vanban.chinhphu.vn/?pageid=27160&docid=211770) | I |
| TT-27-2025-BYT | 27/2025/TT-BYT | Danh mục, thanh toán BHYT thuốc dược liệu, cổ truyền | BYT | 2025 | 01/09/2025 | Còn HL | — | gốc-meta | [VB 214388](https://vanban.chinhphu.vn/?pageid=27160&docid=214388) | I |
| TT-24-2025-BYT | 24/2025/TT-BYT | Sửa TT 04/2017 (danh mục VTYT BHYT) | BYT | 2025 | 01/09/2025 | Còn HL | — | gốc-meta | [VB 214383](https://vanban.chinhphu.vn/?pageid=27160&docid=214383) | I |
| TT-25-2026-BYT | 25/2026/TT-BYT | Sửa TT 01/2013 (quản lý chất lượng xét nghiệm), **TT 32/2023, TT 23/2024 (danh mục kỹ thuật), TT 42/2025** | BYT | 30/06/2026 | 15/08/2026 (theo F thì Đ2, Đ3 từ 01/07/2026) | Còn HL | Đ3: áp dụng Danh mục kỹ thuật Phụ lục 02 TT 23/2024 từ **01/01/2028**; mẫu hồ sơ khám sức khỏe mới | gốc (F, PDF ký số) + gốc-meta (G) | [VB 218704](https://vanban.chinhphu.vn/?pageid=27160&docid=218704) · [PDF ký số, CDC Hà Nội](https://hanoicdc.gov.vn/Uploads/files/44.pdf) | I F +G |
| TT-23-2024-BYT | 23/2024/TT-BYT | Danh mục kỹ thuật trong KCB | BYT | 2024 | — | Còn HL; sửa bởi TT-25-2026-BYT | 01/01/2028 (Phụ lục 02) | gốc (qua TT 25/2026) | — | F +G |
| TT-01-2013-BYT | 01/2013/TT-BYT | Quản lý chất lượng xét nghiệm | BYT | 2013 | — | Còn HL; sửa bởi TT-25-2026-BYT | — | gốc-meta (qua TT 25) | — | I F |
| TT-42-2025-BYT | 42/2025/TT-BYT | Tiêu chuẩn sức khỏe người điều khiển phương tiện giao thông đường sắt | BYT | 2025 | — | Còn HL; sửa bởi TT-25-2026-BYT | — | gốc-meta (G) | — | F +G |
| TT-24-2026-BYT | 24/2026/TT-BYT | Mức độ rủi ro, biện pháp quản lý TTBYT; sửa TT 05/2022 | BYT | 30/06/2026 | 01/07/2026 | Còn HL; thay TT 59/2025/TT-BYT | Kiểm định TTBYT: thiết bị mua sau 30/06/2027 phải kiểm định; mua trước 01/07/2027 phải xong trước 01/01/2028 | gốc | [VB 218703](https://vanban.chinhphu.vn/?pageid=27160&docid=218703) | I |
| TT-30-2023-BYT | 30/2023/TT-BYT | Danh mục 50 bệnh, tình trạng bệnh được KCB từ xa | BYT | 30/12/2023 | 01/01/2024 | Còn HL (theo thứ cấp) | — | thứ cấp | — (chưa có link mở được) | I F |
| TT-32-2023-BYT | 32/2023/TT-BYT | Quy định chi tiết Luật KCB (Chương X HSBA, 82 mẫu) | BYT | 31/12/2023 | 01/01/2024 | Còn HL; sửa bởi TT-25-2026-BYT (G) | — | thứ cấp (F đọc trên hethongphapluat, trang không tin cậy) | — (cần link gốc) | I F +G |
| TT-49-2017-BYT | 49/2017/TT-BYT | Hoạt động y tế từ xa | BYT | 2017 | — | Chưa rõ | — | chưa XM | — | I T |
| TT-48-2017-BYT | 48/2017/TT-BYT | Trích chuyển dữ liệu điện tử KCB BHYT | BYT | 28/12/2017 | 01/03/2018 | Còn HL (vẫn là căn cứ của QĐ 3276 ngày 17/10/2025, G). Có dự thảo thay (DT-TT48) | Dự kiến bị thay từ 01/01/2027 | thứ cấp (nội dung); gốc (dẫn chiếu, G) | [BHXH VN, thứ cấp](https://baohiemxahoi.gov.vn/gioithieu/pages/gioi-thieu-chung.aspx?CateID=0&ItemID=9799) | I F T +G |
| TT-53-2014-BYT | 53/2014/TT-BYT | Điều kiện hoạt động y tế trên môi trường mạng | BYT | 2014 | — | Chưa rõ | — | chưa XM | — | I |
| TT-36-2024-BYT | 36/2024/TT-BYT | Tiêu chuẩn sức khỏe người lái xe; CSDL sức khỏe lái xe | BYT | 16/11/2024 | 01/01/2025 | Còn HL | — | thứ cấp (theo F, PDF gốc bị lỗi xref) | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/thong-tu-36-2024-tt-byt-tieu-chuan-suc-khoe-doi-voi-nguoi-lai-xe-nguoi-dieu-khien-xe-may-chuyen-dung-373779-d1.html) | F |
| TT-25-2025-BYT | 25/2025/TT-BYT | Hướng dẫn Luật BHXH lĩnh vực y tế (giấy nghỉ việc hưởng BHXH, Mẫu 07) | BYT | 30/06/2025 | 01/07/2025 | Còn HL (giả định) | — | chưa XM | — | F |
| TT-17-2012-BYT | 17/2012/TT-BYT | Giấy chứng sinh (mẫu, cấp lại) | BYT | 2012 | — | Chưa rõ | — | chưa XM | — | F |
| TT-24-2020-BYT | 24/2020/TT-BYT | Phiếu chẩn đoán nguyên nhân tử vong, giấy báo tử | BYT | 2020 | — | Chưa rõ | — | chưa XM | — | F |
| TT-20-2017-BYT | 20/2017/TT-BYT (sửa bởi 27/2024/TT-BYT) | Thuốc và nguyên liệu làm thuốc phải kiểm soát đặc biệt | BYT | 2017 | — | Còn HL (TT 26 dẫn chiếu) | — | chưa XM | — | F |

### 1.5 Bộ Y tế: Quyết định, Chỉ thị, Công văn kỹ thuật

| ID | Số hiệu | Tên (rút gọn) | CQ | Ban hành | Hiệu lực | Trạng thái | Mốc hạn chót | XM tốt nhất | Link tốt nhất | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| QD-130-2023-BYT | 130/QĐ-BYT | Chuẩn và định dạng dữ liệu đầu ra (XML) phục vụ giám định, thanh toán BHYT | BYT | 18/01/2023 | áp dụng 01/09/2023 | Còn HL; thay QD-4210-2017-BYT; sửa bởi QD-4750-2023, QD-3176-2024, QD-1931-2026 | — | thứ cấp, có dẫn chiếu trong bản gốc TT 12/2026 | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-130-qd-byt-241607-d1.html) | I F T |
| QD-4750-2023-BYT | 4750/QĐ-BYT | Sửa QĐ 130 (có bảng check-in) | BYT | 29/12/2023 | chính thức 01/07/2024 | Còn HL; sửa bởi QD-3176-2024 | — | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-4750-qd-byt-2023-sua-doi-bo-sung-quyet-dinh-130-qd-byt-286670-d1.html) | I F T |
| QD-3176-2024-BYT | 3176/QĐ-BYT | Sửa QĐ 4750 (thêm MA_DOI_TUONG_KCB…) | BYT | 29/10/2024 | áp dụng đồng bộ 01/01/2025 | Còn HL | — | thứ cấp (caselaw có toàn văn) | [caselaw, thứ cấp](https://caselaw.vn/van-ban-phap-luat/508520-quyet-dinh-so-3176-qd-byt-ngay-29-10-2024-cua-bo-truong-bo-y-te-sua-doi-quyet-dinh-4750-qd-byt-sua-doi-quyet-dinh-130-qd-byt-quy-dinh-chuan-va-dinh-dang-du-lieu-dau-ra-phuc-vu-viec-quan-ly-giam-dinh-thanh-toan-chi-phi-kham-benh-chua-benh-va-giai-quyet-cac-che-do-lien-quan) | I F T |
| QD-1931-2026-BYT | 1931/QĐ-BYT (ngày 29/06/2026) | Sửa chuẩn dữ liệu đầu ra (MUC_HUONG, SO_DANG_KY) | BYT | 29/06/2026 | 01/07/2026 | Còn HL (theo 1 nguồn). Lưu ý trùng số với QĐ 1931/QĐ-BYT năm 2016 | 01/07/2026 | thứ cấp (chỉ 1 nguồn) | [suckhoetreem, thứ cấp](https://suckhoetreem.vn/cuoc-song-so/cap-nhat-chuan-du-lieu-phuc-vu-giam-dinh-kham-chua-benh-va-thanh-toan-bhyt-tu-01-7-2026-131048.html) | T |
| QD-4210-2017-BYT | 4210/QĐ-BYT | Chuẩn dữ liệu đầu ra (cũ) | BYT | 2017 | — | Thay bởi QD-130-2023-BYT | — | thứ cấp | — | I T |
| QD-7603-2018-BYT | 7603/QĐ-BYT | Bộ mã danh mục dùng chung trong KCB và thanh toán BHYT (phiên bản 6) | BYT | 25/12/2018 | — | Còn HL; sửa bởi 4905/2019, 5937/2021, QD-824-2023, QD-2010-2025, QD-3276-2025 | — | gốc-OCR (dẫn chiếu trong TT 12/2026 Đ7) | (dẫn chiếu trong [PDF TT 12/2026](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-btc.pdf)) | I F |
| QD-824-2023-BYT | 824/QĐ-BYT | Bổ sung danh mục mã dùng chung | BYT | 15/02/2023 | — | Còn HL một phần. **Phụ lục 1 (mã loại hình KCB) bị QD-1804-2026 bãi bỏ từ 01/08/2026** (G) | 01/08/2026 | thứ cấp (tin BHXH VN, G) | — | I T +G |
| QD-2010-2025-BYT | 2010/QĐ-BYT | Ban hành tạm thời danh mục mã dùng chung gửi dữ liệu chi phí BHYT | BYT | 19/06/2025 | — | Còn HL một phần. **Phụ lục 6 (mã khoa) bị QD-1804-2026 bãi bỏ từ 01/08/2026** (G) | Cập nhật phần mềm chậm nhất 01/08/2025 | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-2010-qd-byt-2025-ban-hanh-tam-thoi-danh-muc-ma-dung-chung-gui-du-lieu-chi-phi-kham-chua-benh-bhyt-403420-d1.html) | I T +G |
| QD-3276-2025-BYT | 3276/QĐ-BYT | Danh mục mã đối tượng đến KCB và mã nhiên liệu (gửi dữ liệu BHYT) | BYT | 17/10/2025 | — | Còn HL | — | gốc (PDF có text, G) | [PDF](https://xdcs.cdnchinhphu.vn/446259493575335936/2025/10/27/3276-1761531834581496757967.pdf) | I F +G |
| QD-1804-2026-BYT | 1804/QĐ-BYT | Danh mục mã loại hình KCB và mã khoa | BYT | 19/06/2026 | chậm nhất 01/08/2026 | Còn HL | 01/08/2026 | thứ cấp (tin của BHXH VN, có kèm file QĐ; G) | [BHXH VN, thứ cấp](https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=26715&CateID=169) | T +G |
| QD-697-2026-BYT | 697/QĐ-BYT | Mẫu bảng kê chi phí KCB 01/KBCB | BYT | 19/03/2026 | — | Còn HL; thay QĐ 6556/QĐ-BYT 2018 | Phần mềm nâng cấp chậm nhất **01/07/2026** | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-697-qd-byt-2026-ban-hanh-mau-bang-ke-chi-phi-kham-chua-benh-tai-co-so-y-te-429297-d1.html) | F |
| QD-1332-2024-BYT | 1332/QĐ-BYT | Ban hành Sổ sức khỏe điện tử tích hợp VNeID | BYT | 21/05/2024 | ký | Còn HL | — | thứ cấp, có dẫn chiếu trong QĐ 31 và QĐ 1551 bản gốc | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-1332-qd-byt-2024-ban-hanh-so-suc-khoe-dien-tu-phuc-vu-tich-hop-tren-ung-dung-vneid-337262-d1.html) | I F |
| QD-2733-2024-BYT | 2733/QĐ-BYT | Hướng dẫn thực hiện Sổ SKĐT trên VNeID | BYT | 17/09/2024 | ký | Còn HL (QĐ 31 Đ5 dẫn chiếu, G) | — | gốc (chỉ dẫn chiếu); nội dung chưa đọc | — | F +G |
| QD-31-2026-BYT | 31/QĐ-BYT | Công bố khai thác dữ liệu Sổ SKĐT VNeID thay giấy tờ | BYT | 06/01/2026 | ký | Còn HL | Đ5: **từ 01/01/2026** cơ sở KCB phải liên thông dữ liệu Sổ SKĐT VNeID của tất cả người bệnh (G) | gốc (PDF có text, G) | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20260305/691_Quyet-dinh-31-QD-BYT_704c0ca597.pdf) | I F T +G |
| QD-1551-2026-BYT | 1551/QĐ-BYT | Hướng dẫn thu thập, liên thông dữ liệu khám sức khỏe; tạo lập Sổ SKĐT | BYT | 31/05/2026 | ký | Còn HL | 15/07/2026: đồng bộ dữ liệu cũ; thường xuyên: gửi trong 24 giờ sau đợt khám | gốc | [PDF, SYT Lai Châu](https://soyte.laichau.gov.vn/upload/1001027/20260602/2026_05_31_QD_ban_hanh_HD_ket_noi_lien_thong_du_lieu_KSK_Final_signed_2be3f377e1.pdf) · [PDF, SYT Quảng Ngãi](https://syt.quangngai.gov.vn/upload/2006968/20260716/2026_05_31_QD_ban_hanh_HD_ket_noi_lien_thong_du_lieu_KSK_Final.signed.pdf) | I F T |
| QD-1272-2026-BYT | 1272/QĐ-BYT | Kế hoạch KSK định kỳ | BYT | 06/05/2026 | — | Còn HL | — | gốc (dẫn chiếu trong QĐ 1551) | — | I |
| QD-3516-2025-BYT | 3516/QĐ-BYT | Chiến lược chuyển đổi số Bộ Y tế 2025–2030 | BYT | 12/11/2025 | ký | Còn HL | Mục tiêu 2030 | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/thong-tin/quyet-dinh-3516-qd-byt-2025-chien-luoc-chuyen-doi-so-bo-y-te-giai-doan-2025-2030-418662-d1.html) | I |
| QD-586-2026-BYT | 586/QĐ-BYT | Kế hoạch triển khai HSBA điện tử toàn quốc (năm 2026) | BYT | 09/03/2026 | ký | Còn HL; quan hệ với QD-965-2026 chưa rõ | 31/12/2026: 100% cơ sở KCB; **01/01/2027: BV công và tư dừng bệnh án giấy** | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-586-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-427964-d1.html) | I F T |
| QD-965-2026-BYT | 965/QĐ-BYT | Kế hoạch HSBA điện tử 2026–2030 | BYT | 10/04/2026 | ký | Còn HL | 2030: 100% cơ sở KCB không dùng bệnh án giấy | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-965-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-431556-d1.html) | I T |
| CT-04-2026-BYT | 04/CT-BYT | Đẩy mạnh triển khai HSBA điện tử | BYT | 07/04/2026 | ký | Còn HL | Giống QĐ 586 | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/chi-thi-04-ct-byt-2026-day-manh-trien-khai-ho-so-benh-an-dien-tu-tai-co-so-kham-chua-benh-431124-d1.html) | T |
| CT-07-2026-BYT | 07/CT-BYT | Xử lý "điểm nghẽn" chuyển đổi số y tế | BYT | 15/09/2026 | ký | Còn HL | 30/09/2026: đánh giá ATTT/cấp độ (I); tháng 8 và 9/2026: danh mục dữ liệu chủ, cấu trúc CSDLQG y tế (T); chiến dịch 100 ngày Sổ SKĐT | thứ cấp (linkcheck: các bài báo không nêu số hiệu) | [suckhoedoisong, thứ cấp](https://suckhoedoisong.vn/bo-truong-bo-y-te-yeu-cau-day-manh-xu-ly-dut-diem-cac-diem-nghen-chuyen-doi-so-y-te-169260915171532468.htm) | I T |
| QD-2146-2026-BYT | 2146/QĐ-BYT | Khung kiến trúc số Bộ Y tế | BYT | 15/07/2026 | ký | Còn HL; thay QĐ 1928/QĐ-BYT 2023 (Kiến trúc CPĐT BYT 2.1, theo luatvietnam) | 2026–2030 (theo tóm tắt) | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-2146-qd-byt-2026-ban-hanh-khung-kien-truc-so-bo-y-te-440771-d1.html) | I F |
| QD-2113-2026-BYT | 2113/QĐ-BYT | Khung kiến trúc dữ liệu, quản trị dữ liệu, từ điển dữ liệu dùng chung ngành y tế | BYT | 10/07/2026 (theo nguồn tìm kiếm) | ký | Còn HL (?) | — | thứ cấp (nguồn yếu) | [ytesovietnam, không chính thức](https://ytesovietnam.vn/quyet-dinh-2146-2113-khung-kien-truc-so-kien-truc-du-lieu-y-te) | I |
| QD-326-2024-BYT | 326/QĐ-BYT | Quy chế bảo đảm ATTT, ANM của Bộ Y tế | BYT | 07/02/2024 | 07/02/2024 | Còn HL (theo trang BYT) | — | thứ cấp | [benhandientu, thứ cấp](https://benhandientu.moh.gov.vn/van-bang-phap-ly-co-hieu-luc) | I F |
| CV-365-2025-TTYQG | 365/TTYQG-GPQLCL | Yêu cầu kỹ thuật triển khai phần mềm HSBA điện tử | TT Thông tin y tế QG | 06/06/2025 | — | Hướng dẫn kỹ thuật đang áp dụng | — | thứ cấp (trích nguyên văn trong phụ lục tự đánh giá của TTYT Bạc Liêu) | [PDF TTYT Bạc Liêu, linkcheck lỗi SSL](https://ttyttpbaclieu.gov.vn/upload/1000078/fck/files/2_2_1_Ph____l___c_b__o_c__o_____nh_gi___ph___m_m___m_theo_TT13_CV365_aa703.pdf) | I F |
| QD-425-2025-BYT | 425/QĐ-BYT | Quy chế an ninh mạng Hệ thống quản lý kê đơn, bán thuốc theo đơn | BYT | 05/02/2025 | — | Còn HL | — | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/y-te/quyet-dinh-425-qd-byt-2025-quy-che-an-ninh-mang-he-thong-quan-ly-ke-don-thuoc-ban-thuoc-theo-don-391009-d1.html) | F |
| QD-808-2023-BYT | 808/QĐ-BYT | Chuẩn kết nối Hệ thống đơn thuốc quốc gia | BYT | 01/04/2023 | — | Chưa rõ | — | chưa XM | — | F |
| CV-934-2026-TTYQG | 934/TTYQG-DA | Liên thông Hệ thống CSDL dược | TT Thông tin y tế QG | 12/08/2026 | — | Đang áp dụng | — | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/tin-van-ban-moi/co-so-ban-buon-ban-le-thuoc-phai-lien-thong-du-lieu-tu-01-01-2026-len-he-thong-co-so-du-lieu-ve-duoc-186-111475-article.html) | F |
| CV-3656-2026-QLD | 3656/QLD-KD | Đăng ký tài khoản Hệ thống CSDL dược | Cục QLD | 28/09/2026 | — | Đang áp dụng | Đăng ký trước **04/10/2026**; dữ liệu tính từ 01/01/2026 | thứ cấp | [luatvietnam, thứ cấp](https://luatvietnam.vn/tin-van-ban-moi/co-so-kinh-doanh-duoc-khan-truong-dang-ky-tai-khoan-tren-he-thong-co-so-du-lieu-ve-duoc-truoc-04-10-2026-186-112993-article.html) | F |
| QD-232-TTYQG | 232/QĐ-TTYQG | Chuẩn API liên thông CSDL dược | TT Thông tin y tế QG | chưa rõ | — | Chưa rõ | — | chưa XM | — | F |
| QD-1867-BYT | 1867/QĐ-BYT | (liên quan liên thông dữ liệu dược) | BYT | chưa rõ | — | Chưa rõ | — | chưa XM | — | F |
| QD-2656-2026-BYT | 2656/QĐ-BYT | Bãi bỏ điểm đ k1 Đ5 TT 02/2018 (GPP) | BYT | 2026 | bãi bỏ từ 19/08/2026 | Còn HL | 19/08/2026 | gốc | [VB 219396](https://vanban.chinhphu.vn/?pageid=27160&docid=219396) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/2656-byt.signed.pdf) | I |
| QD-1898-2025-BYT | 1898/QĐ-BYT | Chuẩn dữ liệu điện tử giấy chứng sinh | BYT | 09/06/2025 | — | Còn HL | — | thứ cấp | [PBGDPL Cần Thơ, thứ cấp](https://pbgdpl.cantho.gov.vn/quy-dinh-chi-tiet-ve-chuan-va-dinh-dang-du-lieu-dien-tu-giay-chung-sinh-duoc-bo-y-te-quy-dinh-tai-quyet-dinh-1898qd-byt-nam-2025) | F |
| QD-1996-2025-BYT | 1996/QĐ-BYT | Hướng dẫn ghi phiếu chẩn đoán nguyên nhân tử vong | BYT | 2025 | — | Chưa rõ | — | chưa XM | — | F |
| QD-2555-2025-BYT | 2555/QĐ-BYT | Quy trình thủ tục KCB BHYT (VNeID mức 2, VssID, CCCD) | BYT | 12/08/2025 | 15/08/2025 | Còn HL (?) | — | thứ cấp | [BHXH VN, thứ cấp](https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=25292&CateID=169) | T |
| QD-1849-2026-BYT | 1849/QĐ-BYT | Hướng dẫn kỹ thuật mã hóa bệnh tật | BYT | 23/06/2026 | — | Chưa rõ | — | chưa XM | — | F |
| QD-4469-2020-BYT | 4469/QĐ-BYT | Hướng dẫn mã hóa ICD-10 (2020) | BYT | 2020 | — | Chưa rõ (có thể bị TT-06-2026-BYT thay) | — | chưa XM | — | I |
| QD-2427-2025-BYT | 2427/QĐ-BYT | Danh mục mã dùng chung thuật ngữ y học lâm sàng, đợt 1 | BYT | 2025 | — | Chưa rõ | — | chưa XM | — | I |
| QD-2114-2026-BYT | 2114/QĐ-BYT | Kế hoạch xây dựng hệ thống quản lý hoạt động KCB | BYT | 2026 | — | Chưa rõ | — | chưa XM | — | I |
| QD-7713-2016-BYT | 7713/QĐ-BYT | Công bố tiêu chuẩn HL7 (bản tiếng Việt) | BYT | 30/12/2016 | — | Chưa rõ | — | chưa XM | — | I |
| QD-3926-2017-BYT | 3926/QĐ-BYT | HL7 CDA | BYT | 28/08/2017 | — | Chưa rõ | — | chưa XM | — | I |
| QD-4868-2015-BYT | 4868/QĐ-BYT | Đề án thí điểm PACS | BYT | 2015 | — | Chưa rõ | — | chưa XM | — | F |
| QD-1709-2026-BYT | 1709/QĐ-BYT (theo báo) | Chương trình MTQG chăm sóc sức khỏe, dân số và phát triển 2026–2035 | BYT (?) | 12/06/2026 | — | Chưa rõ: CTMTQG thường do TTg hoặc QH phê duyệt, cần kiểm tra lại cơ quan ban hành | 2030: 100% dân có Sổ SKĐT, 100% trạm y tế xã dùng nền tảng số | thứ cấp | [ninhbinh.gov.vn, thứ cấp](https://ninhbinh.gov.vn/tin-trong-nuoc-quoc-te/phe-duyet-chuong-trinh-muc-tieu-quoc-gia-ve-cham-soc-suc-khoe-dan-so-va-phat-trien-giai-doan-202-382026) | T |
| CV-168-2025-BHXH | 168/BHXH-QLT | Thẻ BHYT giấy chỉ cấp cho 3 trường hợp, từ 01/06/2025 | BHXH VN | 2025 | 01/06/2025 | Chưa rõ | — | thứ cấp | [BHXH VN, thứ cấp](https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=24571&CateID=169) | T |

### 1.6 Bộ Tài chính / BHXH, Bộ Công an, Bộ KH&CN (gồm mảng Bộ TT&TT cũ), NHNN

| ID | Số hiệu | Tên (rút gọn) | CQ | Ban hành | Hiệu lực | Trạng thái | Mốc hạn chót | XM tốt nhất | Link tốt nhất | Nguồn |
|---|---|---|---|---|---|---|---|---|---|---|
| TT-12-2026-BTC | 12/2026/TT-BTC | Giám định chi phí KCB BHYT, biểu mẫu thanh toán và quyết toán | BTC | 10/02/2026 | ký; biểu mẫu và danh mục (Đ5–8, Đ10) từ 01/04/2026 | Còn HL | 01/04/2026; tổng hợp tháng, quyết toán quý (thời hạn 15 ngày: chưa đối chiếu, xem MT-14) | gốc-OCR (I); thứ cấp (F, T) | [VB 216997](https://vanban.chinhphu.vn/?pageid=27160&docid=216997) · [PDF scan](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-btc.pdf) | I F T |
| TT-91-2026-BTC | 91/2026/TT-BTC | Hướng dẫn Luật QLT và NĐ 254/2026 về hóa đơn, chứng từ | BTC | 30/06/2026 | 01/07/2026 | Còn HL | — | gốc-meta | [VB 219006](https://vanban.chinhphu.vn/?pageid=27160&docid=219006) | I |
| TT-107-2025-BTC | 107/2025/TT-BTC | Kế toán quỹ BHXH, BHYT | BTC | 2025 | — | Còn HL | — | gốc-meta (qua tìm kiếm) | — | I |
| TT-116-2025-BTC | 116/2025/TT-BTC | Cơ chế tài chính BHXH | BTC | 2025 | — | Còn HL | — | gốc-meta (qua tìm kiếm) | — | I |
| TT-126-2025-BTC | 126/2025/TT-BTC | Quy trình kiểm tra | BTC | 2025 | — | Còn HL | — | gốc-meta (qua tìm kiếm) | — | I |
| TT-47-2026-BCA | 47/2026/TT-BCA | QCVN về an ninh mạng cho HTTT lưu trữ tài liệu điện tử của cơ quan Đảng, Nhà nước | BCA | 12/05/2026 | 01/07/2026 | Còn HL; có áp dụng cho BV công hay không: chưa rõ | — | gốc-meta | [VB 218069](https://vanban.chinhphu.vn/?pageid=27160&docid=218069) | I |
| TT-170-2026-BCA | 170/2026/TT-BCA | QCVN sinh trắc học mống mắt | BCA | 01/10/2026 | chưa rõ | Mới ban hành | — | gốc-meta (thấy trong danh sách) | — | I |
| TT-19-2025-BKHCN | 19/2025/TT-BKHCN | Kiểm toán kỹ thuật chữ ký điện tử, dịch vụ tin cậy | BKHCN | 06/10/2025 | 01/01/2026 | Còn HL | — | gốc-meta | [VB 215589](https://vanban.chinhphu.vn/?pageid=27160&docid=215589) | I |
| TT-53-2025-BKHCN | 53/2025/TT-BKHCN | QCVN dịch vụ chứng thực thông điệp dữ liệu | BKHCN | 31/12/2025 | 01/07/2026 | Còn HL | — | gốc-meta | [VB 216456](https://vanban.chinhphu.vn/?pageid=27160&docid=216456) | I |
| TT-59-2026-BKHCN | 59/2026/TT-BKHCN | Bãi bỏ TT 37/2009, 08/2011, 41/2017/TT-BTTTT | BKHCN | 25/09/2026 | **15/11/2026** | **Sắp HL** | 15/11/2026 | gốc | [VB 219731](https://vanban.chinhphu.vn/?pageid=27160&docid=219731) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/59-bkhcn.signed.pdf) | I |
| TT-41-2017-BTTTT | 41/2017/TT-BTTTT | Sử dụng chữ ký số cho văn bản điện tử trong CQNN | BTTTT | 2017 | — | Bị TT-59-2026-BKHCN bãi bỏ từ 15/11/2026 | 15/11/2026 | gốc (qua TT 59) | — | I |
| TT-05-2026-BKHCN | 05/2026/TT-BKHCN | Khung đạo đức trí tuệ nhân tạo quốc gia | BKHCN | 10/03/2026 | 10/03/2026 | Còn HL | — | gốc-meta | [VB 217165](https://vanban.chinhphu.vn/?pageid=27160&docid=217165) | I |
| TT-34-2025-BKHCN | 34/2025/TT-BKHCN | Sản phẩm, dịch vụ công nghệ số được ưu đãi trong đấu thầu | BKHCN | 15/11/2025 | 01/01/2026 | Còn HL | — | gốc-meta | [VB 216032](https://vanban.chinhphu.vn/?pageid=27160&docid=216032) | I |
| TT-39-2026-BKHCN | 39/2026/TT-BKHCN | Chi phí đầu tư, mua sắm, **thuê dịch vụ** chuyển đổi số dùng NSNN | BKHCN | 01/07/2026 | 01/07/2026 | Còn HL; quan hệ với TT 18/2024/TT-BTTTT chưa rõ | — | gốc-meta | [VB 218792](https://vanban.chinhphu.vn/?pageid=27160&docid=218792) | I |
| TT-41-2026-BKHCN | 41/2026/TT-BKHCN | Phát triển thử nghiệm; quản lý chất lượng đầu tư, thuê dịch vụ CĐS | BKHCN | 01/07/2026 | 01/07/2026 | Còn HL | — | gốc-meta | [VB 218794](https://vanban.chinhphu.vn/?pageid=27160&docid=218794) | I |
| TT-12-2022-BTTTT | 12/2022/TT-BTTTT | Hướng dẫn NĐ 85/2016 (hồ sơ cấp độ) | BTTTT | 2022 | — | Chưa rõ (văn bản căn cứ đã mất căn cứ) | — | chưa XM | — | I F T |
| TT-03-2017-BTTTT | 03/2017/TT-BTTTT | Hướng dẫn NĐ 85/2016 | BTTTT | 2017 | — | Chưa rõ | — | chưa XM | — | I |
| TT-39-2017-BTTTT | 39/2017/TT-BTTTT | Danh mục tiêu chuẩn kỹ thuật ứng dụng CNTT trong CQNN (HD 365 dẫn chiếu) | BTTTT | 2017 | — | Chưa rõ | — | chưa XM | — | F |
| QD-742-2022-BTTTT | 742/QĐ-BTTTT | An toàn phần mềm nội bộ (HD 365 dẫn chiếu) | BTTTT | 2022 | — | Chưa rõ | — | chưa XM | — | F |
| TCVN-12344-2019 | TCVN 12344:2019 (ISO/TS 18530:2014) | Tin học y tế: định danh tự động, ghi nhãn người bệnh và nhân viên y tế | BKHCN | 2019 | — | Tiêu chuẩn tự nguyện | — | thứ cấp (qua tìm kiếm) | — | I |
| TT-15-2024-NHNN | 15/2024/TT-NHNN (sửa bởi 30/2025, 21/2026/TT-NHNN) | Cung ứng dịch vụ thanh toán không dùng tiền mặt | NHNN | 2024 | — | Còn HL | — | gốc-meta (qua tìm kiếm) | — | I |

### 1.7 Văn kiện Đảng (bối cảnh chính sách)

| ID | Số hiệu | Tên | CQ | Ban hành | Trạng thái | Mốc | XM tốt nhất | Link | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| NQ-72-2025-TW | 72-NQ/TW | Giải pháp đột phá bảo vệ, chăm sóc sức khỏe nhân dân | Bộ Chính trị | 09/09/2025 | Còn HL | Từ 2026: KSK ≥1 lần/năm, lập Sổ SKĐT (mốc "năm 2026 hoàn thành CSDL" chưa trích được nguyên văn) | thứ cấp | [xaydungchinhsach, thứ cấp, linkcheck: không thấy số hiệu](https://xaydungchinhsach.chinhphu.vn/nghi-quyet-72-nq-tw-cua-bo-chinh-tri-ve-mot-so-giai-phap-dot-pha-tang-cuong-bao-ve-cham-soc-va-nang-cao-suc-khoe-nhan-dan-119250912060746502.htm) | I T |
| KL-76-2026-TW | 76-KL/TW | Kết luận (NQ 221/NQ-CP thực hiện) | TW | 28/07/2026 | — | — | thứ cấp | — | T |
| CT-52-TW | 52-CT/TW | BHYT toàn dân giai đoạn mới | TW | — | — | — | chưa XM | — | I |

### 1.8 Dự thảo và văn bản đang xây dựng

| ID | Dự thảo | CQ | Tình trạng (tại 05/10/2026) | HL dự kiến | Nội dung liên quan phần mềm | XM | Link tốt nhất | Nguồn |
|---|---|---|---|---|---|---|---|---|
| DT-TT48 | TT về ứng dụng CNTT, CĐS, chia sẻ dữ liệu trong BHYT (thay TT-48-2017-BYT) | BYT | Lấy ý kiến đến **07/10/2026** | 01/01/2027 | Gửi XML ký số **trong 03 giờ** sau lượt khám; chậm nhiều lần thì có thể bị xử phạt VPHC | thứ cấp | [vtv, thứ cấp](https://vtv.vn/de-xuat-co-so-y-te-phai-gui-du-lieu-bhyt-trong-vong-3-gio-sau-kham-cham-nhieu-lan-co-the-bi-xu-phat-100261001082022915.htm) | T |
| DT-CLS-LT | TT danh mục xét nghiệm, CLS và điều kiện sử dụng kết quả liên thông (~441 dịch vụ) | BYT | Lấy ý kiến (báo ngày 24/08/2026) | I: ban đầu 01/07/2026; T: gắn với mốc 01/01/2027 | LIS/RIS/PACS: định danh, thời điểm lấy mẫu, người thực hiện, thời hạn giá trị từ 24 giờ đến 60 ngày; liên thông cả hình ảnh | thứ cấp | [dantri, thứ cấp](https://dantri.com.vn/suc-khoe/de-xuat-hon-400-xet-nghiem-chup-chieu-co-the-duoc-dung-lai-khi-chuyen-vien-20260824223459660.htm) · [tuoitre, thứ cấp](https://tuoitre.vn/de-xuat-nhieu-xet-nghiem-chup-chieu-khong-phai-thuc-hien-lai-khi-chuyen-vien-10026082416552496.htm) | I T |
| DT-BHYT-TUXA | TT thanh toán BHYT cho KCB y học gia đình, tại nhà, từ xa | BYT | Xin ý kiến (CV 7411/SYT-NV Đồng Nai, 03/10/2026) | 01/01/2027 (theo báo) | Thanh toán theo gói; ~50 bệnh ICD-10 KCB từ xa được BHYT chi trả; yêu cầu video, HSBA điện tử, ký số | thứ cấp | [SYT Đồng Nai, thứ cấp](https://syt.dongnai.gov.vn/vi/news/thong-bao/xin-y-kien-gop-y-du-thao-thong-tu-quy-dinh-thanh-toan-bao-hiem-y-te-doi-voi-kham-benh-chua-benh-y-hoc-gia-dinh-tai-nha-tu-xa-44038.html) | I T |
| DT-BTC-CONG | TT BTC hướng dẫn điểm d k2 Đ71 NĐ 188 (Cổng tiếp nhận dữ liệu giám định) | BTC | Dự thảo (baochinhphu 12/2025); có thể đã được gộp vào TT-12-2026-BTC | — | Giao diện HIS gửi dữ liệu sang BHXH | chưa XM | — | I F |
| DT-LUAT-6L | Luật sửa 6 luật (KCB, Dược, BHYT, Trẻ em, Người khuyết tật, Người cao tuổi) | BYT → QH | Trình Kỳ họp 2 QH khóa XVI (10/2026) | chưa rõ | Có thể đụng Đ120 Luật KCB và quy định về HSBA điện tử | thứ cấp | [baochinhphu, thứ cấp, linkcheck: không thấy số hiệu](https://baochinhphu.vn/bo-y-te-chuan-bi-trinh-quoc-hoi-4-du-an-luat-trong-do-co-1-luat-sua-nhieu-luat-102261001180003719.htm) | I T |
| DT-LUAT-DDXT | Luật Định danh và xác thực điện tử | BCA | Lấy ý kiến đến 04/06/2026; trình 10/2026 | chưa rõ | 3 mức xác thực; Open API; lưu nhật ký xác thực ≥5 năm | thứ cấp | [luatvietnam (dự thảo), thứ cấp](https://luatvietnam.vn/tu-phap/du-thao-luat-dinh-danh-va-xac-thuc-dien-tu-2026-436278-d10.html) | I |
| DT-TT54 | TT thay TT-54-2017-BYT (bộ tiêu chí CNTT) và bộ tiêu chuẩn chất lượng BV nâng cao | BYT | Theo kế hoạch xong Q2/2026, **chưa thấy ban hành** | chưa rõ | Chuẩn chức năng HIS/LIS/PACS, tiêu chí bệnh viện thông minh | chưa XM | — | I F T |
| DT-TT23 | Văn bản thay TT-23-2025-BYT (báo cáo thống kê) | BYT | Chưa thấy dự thảo | Phải có trước 01/03/2027 | Phân hệ báo cáo thống kê | — | — | I F |
| DT-DMDL | Danh mục dữ liệu chủ, dữ liệu tham chiếu, từ điển dữ liệu dùng chung ngành y tế (13 CSDL) | BYT | Hạn nội bộ tháng 8/2026; đến 10/2026 vẫn "chưa hoàn thiện" | — | Master data cho HIS | thứ cấp | [suckhoedoisong, thứ cấp, linkcheck: không thấy số hiệu](https://suckhoedoisong.vn/bo-y-te-day-nhanh-tien-do-cac-nhiem-vu-chuyen-doi-so-thao-go-diem-nghen-du-lieu-va-dich-vu-so-169261003100416305.htm) | T |
| DT-CTMTQG | TT hướng dẫn CTMTQG chăm sóc sức khỏe 2026–2035 | BYT | Lấy ý kiến (2026) | chưa rõ | Bác sĩ gia đình gắn HSSK điện tử, nền tảng tư vấn từ xa | chưa XM | — | T |
| DT-QD586-SP | Các sản phẩm theo kế hoạch QĐ 586: danh mục thuật ngữ lâm sàng, hướng dẫn giá RIS-PACS không in phim | BYT | Chưa thấy ban hành | — | EMR, PACS | thứ cấp | — | F |

**Số lượng sau gộp**: 225 dòng có ID, không trùng nhau. Gồm 214 văn bản đã ban hành (trong đó 25 văn bản đã hết HL hoặc bị bãi bỏ, giữ lại để tra chuỗi thay thế; 3 văn kiện Đảng) và 11 dự thảo.

---

## 2. MÂU THUẪN GIỮA CÁC NGUỒN

Dấu **(!)** đánh dấu mâu thuẫn quan trọng, tức là có thể làm trích sai văn bản, sai hạn hoặc sai nghĩa vụ của phần mềm.

| # | Văn bản (ID) | I nói | F nói | T nói | Phân xử |
|---|---|---|---|---|---|
| MT-01 (!) | Hóa đơn điện tử viện phí: ND-254-2026, ND-70-2025, ND-123-2020 | NĐ 254/2026 thay NĐ 123/2020 và NĐ 70/2025 từ 01/07/2026; có điểm m riêng cho KCB | Căn cứ là NĐ 123/2020 sửa bởi NĐ 70/2025, HL 01/06/2025 | NĐ 70/2025 | **Đã phân xử (G)**: Đ43 NĐ 254/2026 (OCR) làm hết HL NĐ 123/2020, Đ1 NĐ 41/2022 và NĐ 70/2025 từ 01/07/2026. **F và T đang trích văn bản đã hết HL.** |
| MT-02 (!) | Ngày TT-46-2018-BYT và Mục VIII TT 54/2017 hết HL | Thay bởi TT 13 (không ghi ngày) | Bị bãi bỏ (không ghi ngày) | 21/07/2025 (ngày TT 13 có HL) | **Đã phân xử (G, gốc-OCR)**: Đ4 k3 TT 13 ghi các văn bản này hết HL "kể từ ngày Thông tư này được ban hành", tức **06/06/2025**. Cần kiểm lại câu chữ có dấu trước khi trích. |
| MT-03 (!) | QD-31-2026-BYT: mức xác minh và phạm vi nghĩa vụ | Thứ cấp (vtv); chỉ nói dữ liệu VNeID có giá trị như giấy | Gốc; Đ5 buộc cơ sở KCB liên thông Sổ SKĐT cho mọi người bệnh từ 01/01/2026 | Số hiệu chưa XM | **Đã phân xử (G, gốc text)**: F đúng. Đ5: cơ sở KCB phải liên thông dữ liệu Sổ SKĐT VNeID "của tất cả các đối tượng người bệnh (theo QĐ 2733/QĐ-BYT) kể từ ngày 01/01/2026". |
| MT-04 (!) | ND-331-2026 có thay ND-85-2016 không | Chưa XM; NĐ 331 vẫn dẫn NĐ 85 | Đ38 bản gốc không có điều khoản bãi bỏ NĐ 85 | "NĐ 331 thay NĐ 85" (thứ cấp) | **Đã phân xử một phần (G)**: Đ38 chỉ quy định hiệu lực; Đ39 k1 còn dùng NĐ 85 để thẩm định cấp độ trong giai đoạn chuyển tiếp. Vậy **không có thay thế chính thức**; NĐ 85 mất căn cứ vì Luật ATTTM hết HL. Nên ghi là "thay thế trên thực tế". Pha 2: tìm văn bản bãi bỏ NĐ 85 và TT 12/2022. |
| MT-05 | Cách tính mốc chuyển tiếp của NĐ 331 | 6 tháng và 12 tháng tính từ 01/07/2026 | Như I | "Cách tính mốc chưa rõ" | **Đã phân xử (G)**: Đ39 k1 tính từ ngày Luật ANM 116/2025 có HL, nên các mốc là **01/01/2027** và **01/07/2027**. Mốc 6 tháng chỉ áp cho HTTT "đang đầu tư, xây dựng trước 01/7/2026". |
| MT-06 | Hạn AI y tế 01/09/2027: căn cứ và đối tượng | QĐ 33/2026 Đ4, áp cho hệ thống vận hành trước khi QĐ có HL (15/08/2026) | — | Luật 134 Đ35 k1a, áp cho AI vận hành trước 01/03/2026 | **Không mâu thuẫn về ngày** (G xác nhận QĐ 33 Đ4). Hai căn cứ có phạm vi khác nhau, nên trích cả hai. Thêm: OCR cho thấy mục "Lĩnh vực y tế" trong danh mục chỉ có AI hỗ trợ phẫu thuật/rô-bốt và AI điều khiển máy thực thi điều trị. Như vậy AI đọc ảnh hay CDSS **có thể không** thuộc danh mục rủi ro cao. Cần xác minh pha 2. |
| MT-07 (!) | QD-1804-2026-BYT thay QĐ 824/2023 và 2010/2025 | Chuỗi QĐ 7603 gồm 2010/2025 vẫn còn HL; TT 12/2026 dẫn đến 3276 | Có nhắc 3276 | "Thay QĐ 824 và QĐ 2010" | **Đã phân xử (G, tin BHXH VN)**: chỉ **bãi bỏ một phần**, gồm Phụ lục 1 QĐ 824/2023 (mã loại hình KCB) và Phụ lục 6 QĐ 2010/2025 (mã khoa), từ 01/08/2026. Các phụ lục khác vẫn còn HL. |
| MT-08 | Chuỗi chuẩn XML BHYT | 130 + 4750 + 3176 | 130 + 4750 + 3176 (+ QĐ 697 bảng kê) | 130 + 4750 + 3176 + **QĐ 1931/2026** | Không mâu thuẫn mà là thiếu sót: I và F không nhắc QĐ 1931/2026. **Cần xác minh pha 2** (mới có 1 nguồn báo, và trùng số với QĐ 1931 năm 2016). |
| MT-09 (!) | Phạm vi TT-25-2026-BYT | Chỉ sửa TT 01/2013 (QLCL xét nghiệm), HL 15/08/2026 | Sửa TT 01/2013, 32/2023, 23/2024, 42/2025; Đ2, Đ3 từ 01/07/2026; Danh mục kỹ thuật PL 02 từ 01/01/2028; mẫu KSK mới | — | **Đã phân xử (G, trích yếu trên vanban)**: sửa 4 thông tư như F nói; HL chung 15/08/2026. Ngày 01/07/2026 cho Đ2, Đ3 mới chỉ có F đọc từ PDF, nên giữ nhưng cần kiểm lại. |
| MT-10 | Mốc CNTT ở Luật KCB Đ120 | Gốc-OCR | Không nhắc | Thứ cấp, "cần đối chiếu bản gốc" | **Đã phân xử (G, VBHN text)**: k5a 01/01/2027, k5b 01/01/2029, k8 HTTT trước 01/01/2027. Tìm thêm k6b (tiêu chuẩn chất lượng cho cơ sở không phải BV từ 01/01/2027) mà cả 3 bản đều bỏ sót. |
| MT-11 | Mức xác minh của TT-13-2025-BYT | Thứ cấp (không tìm thấy bản gốc) | Gốc (PDF sao y của SYT Quảng Ninh) | Gốc-CSDL (caselaw), chưa biết số điều chứa lộ trình | **Đã phân xử (G)**: lộ trình nằm ở **Đ4 k2 a, b**. Mức xác minh tốt nhất là gốc-OCR. |
| MT-12 (!) | Tình trạng TT-48-2017-BYT | Chưa XM | Còn HL (TT 12/2026 viện dẫn) | Còn HL; có dự thảo thay, HL dự kiến 01/01/2027 | **Đã phân xử (G)**: QĐ 3276 ngày 17/10/2025 (gốc) vẫn lấy TT 48/2017 làm căn cứ, nên còn HL tại thời điểm đó. Pha 2 theo dõi DT-TT48. |
| MT-13 (!) | Hạn gửi dữ liệu chi phí BHYT | NĐ 188: "sau khi kết thúc lượt KCB" | TT 48: "ngay sau khi kết thúc", có 7 ngày làm việc để hiệu chỉnh | Dự thảo: **≤ 03 giờ**, có chế tài | Không mâu thuẫn ở hiện tại. Nếu DT-TT48 được ban hành thì yêu cầu kỹ thuật thay đổi lớn: cần hàng đợi gửi gần thời gian thực. **Pha 2 theo dõi.** |
| MT-14 | TT-12-2026-BTC: thời hạn 15 ngày, cổng nộp, mức xác minh | Gốc-OCR; thời hạn 15 ngày "cần đối chiếu" | Thứ cấp: 15 ngày đầu tháng/quý (Đ9–10) | Thứ cấp: nộp qua `gdbhyt.baohiemxahoi.gov.vn`, mẫu 01/BH–03/BH | **Cần xác minh pha 2** (PDF là bản scan): Đ4, Đ7, Đ9, Đ10 và danh sách văn bản bị thay. |
| MT-15 (!) | ND-356-2025: DPIA, thông báo vi phạm, nhân sự | DPIA nộp trong 60 ngày từ khi bắt đầu xử lý | Theo thứ cấp: Đ13 nhân sự, Đ17–19 DPIA 60 ngày, Đ29 thông báo vi phạm 72 giờ; tự nhận tóm tắt có vẻ lẫn lộn | Gốc: Đ20 cập nhật DPIA 6 tháng một lần, thay đổi lớn thì cập nhật trong 10 ngày; Đ21 k4, Đ22, Đ24–26 điều kiện và giấy chứng nhận dịch vụ xử lý DLCN; Đ41 ngưỡng 100.000 chủ thể | Số điều và thời hạn lệch nhau. **Cần xác minh pha 2**: đọc Đ13–29 và Đ41 bản gốc. Hệ quả lớn nhất: vendor SaaS y tế có phải xin giấy chứng nhận "dịch vụ xử lý DLCN" không. |
| MT-16 | Ngưỡng cấp độ của NĐ 331 cho app và HIS | — | Gốc Đ12–13: cấp 3 khi ≥10.000 chủ thể dữ liệu nhạy cảm, hoặc dịch vụ trực tuyến thuộc ngành nghề kinh doanh có điều kiện, hoặc giải quyết TTHC | Thứ cấp: cấp 2 khi <100.000 chủ thể dữ liệu cơ bản hoặc <10.000 chủ thể dữ liệu nhạy cảm; vượt ngưỡng phải đánh giá lại | Hai bản khớp nhau về ngưỡng. Nhận định "nền tảng KCB trực tuyến là cấp 3" là **suy luận của F**. Cần xác minh pha 2. |
| MT-17 | Hạn báo cáo sự cố an ninh mạng (24 và 72 giờ) | — | Thứ cấp (NĐ 331 Đ31) | Nói chung là "báo cáo sự cố" | **Cần xác minh pha 2.** |
| MT-18 | Ngày ban hành ND-330-2026 | 19/08/2026 (vanban) | — | Các báo ghi lệch 19/8 và 26/8 | **Đã phân xử**: lấy 19/08/2026 theo trang VB 219266 (linkcheck OK). |
| MT-19 | L-CDS-2025 có thay Luật CNTT không | Có (gốc-text, Đ47) | — | Chưa XM | **Đã phân xử** theo I. |
| MT-20 | Mức xác minh QD-826-2026-TTg | Gốc-OCR | — | Chỉ thấy snippet | **Đã phân xử** theo I. |
| MT-21 | Nguồn của ND-102-2025 | Gốc-OCR (datafiles) | Thứ cấp (hethongphapluat, trang có chèn lệnh nhắm vào AI) | Gốc (Công báo) | **Đã phân xử**: dùng datafiles hoặc Công báo, bỏ hethongphapluat. Những điều F trích (Đ6, 9, 10, 14, 23) cần đọc lại từ bản gốc. |
| MT-22 | Nguồn của L-ANM-2025 | Gốc-OCR | "Thứ cấp; link vanban chưa mở" | Gốc | **Đã phân xử**: linkcheck xác nhận VB 216499 OK, nên lấy mức gốc. |
| MT-23 (!) | Quan hệ QD-586-2026 và QD-965-2026; mốc 01/01/2027 bỏ bệnh án giấy | Chưa XM | 586 là kế hoạch; mốc 01/01/2027 lấy từ thứ cấp | Hai QĐ song song; thêm CT 04/CT-BYT | Cả 3 bản đều chỉ có thứ cấp. **Cần xác minh pha 2**: mốc 01/01/2027 là nghĩa vụ (có chế tài, xem NĐ 90/2026 Đ39) hay chỉ là mục tiêu kế hoạch. |
| MT-24 (!) | QD-2146-2026-BYT có bắt buộc HL7 FHIR R4, DICOM/DICOMweb không | Chưa có trong bản gốc; chỉ một trang không chính thức nêu | Hai nguồn mâu thuẫn nhau | — | **Cần xác minh pha 2.** Chưa được coi là yêu cầu pháp lý. |
| MT-25 (!) | Phạm vi TT 13 với phòng khám chỉ khám và kê đơn | Cơ sở khác có điều trị ngoại trú, gồm phòng khám tư | Câu chữ chưa rõ với phòng khám không lập HSBA | Phòng khám, TTYT, cơ sở tư | G bổ sung: Luật KCB Đ69 k1 (VBHN) quy định người bệnh "điều trị nội trú, điều trị ban ngày và điều trị ngoại trú" phải được lập HSBA. Vậy câu hỏi là phòng khám có "điều trị ngoại trú" theo nghĩa pháp lý (TT 32/2023) hay không. **Cần xác minh pha 2.** |
| MT-26 | Thời điểm có HL của DT-CLS-LT | Ban đầu dự kiến 01/07/2026 | — | Suy luận gắn với 01/01/2027 | **Cần xác minh pha 2.** |
| MT-27 | Danh sách văn bản sửa ND-98-2021 | 07/2023, 96/2023, 04/2025 | — | 07/2023, 04/2025; VBHN 08/VBHN-BYT 2026 | Lệch nhỏ. **Cần xác minh pha 2** bằng VBHN. |
| MT-28 | Văn bản bị ND-23-2025 thay | NĐ 130/2018 và NĐ 48/2024 (gốc-OCR) | — | "NĐ 130/2018 và văn bản sửa đổi" (thứ cấp) | **Đã phân xử** theo I. |
| MT-29 | Mức xác minh và endpoint của QD-1551-2026 | Gốc; `app.qlhanhnghekcb.gov.vn`, `csdlksk.vn` | Thứ cấp | Gốc; REST `api.emrhub.vn` | Mức xác minh lấy gốc. Endpoint không mâu thuẫn mà bổ sung cho nhau; **pha 2** xác định kênh chính thức (tên miền emrhub không phải tên miền gov.vn). |
| MT-30 | Luồng dữ liệu Sổ SKĐT: QD-2733-2024, QD-31-2026, QD-1551-2026 | — | QĐ 2733 lấy dữ liệu từ CSDL BHYT; QĐ 31 buộc liên thông mọi người bệnh; QĐ 1551 có cổng riêng cho dữ liệu KSK | BHXH chia sẻ dữ liệu khám thường qua Nền tảng điều phối của TTDLQG | **Cần xác minh pha 2**: có một hay nhiều điểm tích hợp. |
| MT-31 | Báo cáo bệnh truyền nhiễm: TT-54-2015 hay TT-15-2026 | TT 15/2026: báo cáo trực tuyến qua HTTT giám sát | TT 54/2015 (chưa XM), có thể đã bị thay | Luật Phòng bệnh thay Luật PCBTN | **Cần xác minh pha 2**: TT 15/2026 có bãi bỏ TT 54/2015 không. |
| MT-32 | Nội dung TT-11-2025-BYT | Sửa GPP (16/05/2025) | Yêu cầu phần mềm nhà thuốc kết nối hệ thống dược QG và thuế (1 nguồn tìm kiếm) | — | **Cần xác minh pha 2.** |
| MT-33 | Nội dung QD-3276-2025 | Mã đối tượng đến KCB, mã nhiên liệu | "27 mã đối tượng" | — | **Đã phân xử (G, gốc)**: đúng tên như I nêu, ngày 17/10/2025. |
| MT-34 (!) | Phụ lục thời hạn lưu trữ của TT-33-2025 | Có PDF phụ lục `33-byt-kem.pdf` | Đã đọc phụ lục (HSBA 10/20/30 năm…); **không thấy dòng riêng cho đơn thuốc** | "PDF datafiles chỉ có 2 trang thân, không kèm phụ lục" | **Đã phân xử**: phụ lục nằm ở file `-kem` (linkcheck OK). Thời hạn lưu đơn thuốc vẫn **cần xác minh pha 2**. |
| MT-35 | Mốc hoàn thành Sổ SKĐT toàn dân | NQ 282: năm 2026; QĐ 826, QĐ 1308: 2030 | — | NQ 221: tháng 10/2026; QĐ 1709: 2030 | Đây là mục tiêu chính sách của nhiều văn bản khác nhau, không phải nghĩa vụ trực tiếp của vendor. Ghi nhận, không cần phân xử. |
| MT-36 | QD-2113-2026 (từ điển dữ liệu đã ký) với DT-DMDL (đến 10/2026 vẫn "chưa hoàn thiện") | QĐ 2113 ký 10/07/2026 (nguồn yếu) | — | Danh mục dữ liệu chủ/từ điển chưa xong | Có thể khung đã ban hành nhưng danh mục chi tiết chưa xong. **Cần xác minh pha 2.** |
| MT-37 | Nội dung CT-07-2026-BYT | Đánh giá ATTT/cấp độ trước 30/09/2026 | — | Danh mục dữ liệu chủ (8/2026), cấu trúc CSDLQG (9/2026), di chuyển hệ thống về TTDLQG | Hai bản bổ sung cho nhau và đều là thứ cấp; linkcheck: bài báo không nêu số hiệu. **Cần xác minh pha 2.** |

**Tổng cộng**: 37 điểm lệch, trong đó **13 điểm quan trọng (!)**. Pha gộp đã phân xử xong 17 điểm, trong đó có 7 điểm quan trọng: MT-01, 02, 03, 07, 09, 12, 34. MT-04 mới phân xử được một phần. Còn 20 điểm chuyển sang pha 2, trong đó 6 điểm quan trọng: MT-04, 13, 15, 23, 24, 25.

---

## 3. CHUỖI THAY THẾ (cũ → mới) và bẫy dẫn chiếu chéo

| Văn bản CŨ (không trích nữa) | → | Văn bản MỚI | Ngày cũ hết HL | Ghi chú |
|---|---|---|---|---|
| TT-46-2018-BYT + Mục VIII PL I và tiêu chí EMR của TT-54-2017-BYT | → | TT-13-2025-BYT | **06/06/2025** (G; T ghi 21/07/2025) | Phần còn lại của TT 54/2017 vẫn HL, chờ DT-TT54 |
| TT-52-2017, TT-18-2018, TT-04-2022, TT-27-2021 (BYT) | → | TT-26-2025-BYT | 01/07/2025 | Lộ trình kê đơn điện tử ở Đ13 k3 TT 26 |
| TT-44-2018-BYT | → | TT-55-2025-BYT | 01/03/2026 | |
| TT-53-2017-BYT | → | TT-33-2025-BYT | 01/07/2025 | |
| TT-40-2015-BYT; Đ6 TT 30/2020; Đ3, Đ4, k2 Đ5 TT 36/2021 | → | TT-01-2025-BYT (sau đó sửa bởi TT-06-2026-BYT) | 01/01/2025 | Thuật ngữ "chuyển tuyến" đổi thành "chuyển cơ sở KCB" |
| TT 32/2014/TT-BYT | → | TT-23-2025-BYT → (văn bản mới, DT-TT23) | 01/07/2025; TT 23 tự hết HL 01/03/2027 | |
| TT 59/2025/TT-BYT | → | TT-24-2026-BYT | 01/07/2026 | Thiết bị y tế, ngoại vi |
| ND-146-2018, ND-75-2023, ND-02-2025 | → | ND-188-2025 | phần lớn 01/07/2025; toàn bộ 15/08/2025 | |
| ND-54-2017 | → | ND-163-2025 | 01/07/2025 | |
| ND-117-2020 | → | ND-90-2026 | 15/05/2026 | |
| ND-13-2023 | → | L-BVDLCN-2025 + ND-356-2025 | 01/01/2026 | Đồng ý đã thu theo NĐ 13 vẫn có giá trị (Luật 91 Đ39) |
| ND-130-2018 + NĐ 48/2024 | → | ND-23-2025 | 10/04/2025 | |
| NĐ 59/2022 | → | ND-69-2024 | 01/07/2024 | |
| NĐ 43/2021 | → | ND-164-2025 | 01/07/2025 | |
| ND-47-2020 | sửa (không thay) bởi | ND-194-2025 | — | |
| **ND-123-2020, Đ1 NĐ 41/2022, ND-70-2025** | → | **ND-254-2026** (+ TT-91-2026-BTC) | **01/07/2026** (G) | F và T vẫn trích NĐ 70/2025 |
| ND-42-2025 | → | ND-313-2026 | 18/08/2026 | |
| L-CNTT-2006 | → | L-CDS-2025 | 01/07/2026 | |
| L-ATTTM-2015 + L-ANM-2018 | → | L-ANM-2025 | 01/07/2026 | Cấp độ đã phê duyệt được giữ, có 12 tháng để nâng chuẩn |
| ND-85-2016 (+ TT-12-2022-BTTTT, TT-03-2017-BTTTT) | → (thực tế) | ND-331-2026 | Không có điều bãi bỏ rõ ràng; NĐ 85 vẫn dùng cho thẩm định chuyển tiếp đến 01/01/2027 | Xem MT-04 |
| ND-53-2022 | → ? | (có thể ND-333-2026) | chưa XM | Pha 2 |
| L-PCBTN-2007 | → | L-PB-2025 | 01/07/2026 | TT-54-2015 → TT-15-2026? (chưa XM) |
| Luật KCB 40/2009/QH12 | → | L-KCB-2023 | 01/01/2024 (Đ120 k2, G) | |
| QD-4210-2017-BYT | → | QD-130-2023-BYT, sửa bởi 4750/2023, 3176/2024, 1931/2026 | — | |
| QĐ 6556/QĐ-BYT 2018 (mẫu bảng kê) | → | QD-697-2026-BYT | Phần mềm nâng cấp trước 01/07/2026 | |
| PL1 của QD-824-2023 + PL6 của QD-2010-2025 | → | QD-1804-2026-BYT | 01/08/2026 | Chỉ bãi bỏ phụ lục, không bãi bỏ cả QĐ |
| QĐ 1928/QĐ-BYT 2023 (Kiến trúc CPĐT BYT 2.1) | → | QD-2146-2026-BYT | 15/07/2026 | Theo luatvietnam |
| TT-41-2017-BTTTT | → (bãi bỏ) | Căn cứ chung là ND-23-2025 | 15/11/2026 (TT-59-2026-BKHCN) | |
| Điểm đ k1 Đ5 TT-02-2018-BYT | → (bãi bỏ) | QD-2656-2026-BYT | 19/08/2026 | |
| QD-4469-2020-BYT (hướng dẫn ICD-10) | → ? | TT-06-2026-BYT / QD-1849-2026-BYT | chưa XM | |
| TT-48-2017-BYT | → (dự thảo) | DT-TT48 | Dự kiến 01/01/2027 | TT 48 hiện vẫn HL |
| Quy trình giám định do BHXH VN ban hành | → | TT-12-2026-BTC | 10/02/2026 | Văn bản bị thay: chưa XM |
| QD-06-2022-TTg (Đề án 06, 2022–2025) | tiếp nối bởi | QD-826-2026-TTg | — | |
| QD-1813-2021-TTg (TTKDTM 2021–2025) | → ? | chưa XM | — | |
| QD-34-2021-TTg | → ? | Có thể là ND-69-2024 | chưa XM | |
| Thủ tục "công nhận HSBA điện tử" theo TT 46/2018 | → | **Không có thủ tục thay thế** | 06/06/2025 | Thực tế: tự đánh giá theo TT 13 và CV 365, rồi tham gia Cổng BAĐT của BYT |

**Bẫy dẫn chiếu chéo** (văn bản mới hoặc đang áp dụng nhưng lại dẫn chiếu văn bản cũ):

1. **TT-26-2025 Đ11** dẫn TT 53/2017 về lưu đơn thuốc, mà TT 53 đã bị TT-33-2025 thay cùng ngày. Phải áp TT 33 theo Đ14 TT 26, nhưng phụ lục TT 33 không có dòng riêng cho "đơn thuốc".
2. **TT-38-2024-BYT** và **QD-69-2025-TTg** vẫn dẫn NĐ 13/2023, nay đã thay bằng Luật 91/2025 và NĐ 356/2025.
3. **CV-365-2025-TTYQG** dẫn NĐ 85/2016, TT 12/2022, TT 39/2017, QĐ 742/2022, đều thuộc khung cũ. Yêu cầu "ATTT tối thiểu cấp độ 2" phải đọc lại theo NĐ 331 (Đ39 k2 coi "an toàn thông tin mạng" tương đương "an ninh mạng").
4. **QD-31-2026, QD-3276-2025** có căn cứ là NĐ 42/2025, nay đã bị NĐ 313/2026 thay. Văn bản vẫn có giá trị, nhưng khi trích về thẩm quyền BYT thì phải dùng NĐ 313.
5. Có **hai "QĐ 1931/QĐ-BYT"**: năm 2016 (tẩy sán lá gan) và ngày 29/06/2026 (chuẩn dữ liệu). Khi trích phải luôn ghi ngày.
6. "QĐ 130/QĐ-BYT" không được trích như bản nguyên gốc, mà phải là bản đã sửa bởi 4750, 3176 (và 1931 nếu xác minh được).
7. **TT-12-2026-BTC Đ7** dẫn chuỗi QĐ 7603 "đến 3276/2025", chưa bao gồm QĐ 1804/2026 (ban hành sau).
8. **benhandientu.moh.gov.vn** vẫn liệt kê TT 46/2018 là "có hiệu lực" (trang chưa cập nhật).
9. **TT-13-2025 Đ2 k3** yêu cầu "tiêu chuẩn kỹ thuật CNTT trong cơ quan nhà nước" (theo CV 365 là TT 39/2017/TT-BTTTT, ban hành dựa trên Luật CNTT đã hết HL).
10. **TT-01-2025** quy định "đóng dấu" trên phiếu hẹn và phiếu chuyển. Từ 01/06/2026, TT-06-2026 thay bằng ký số xác thực của cơ sở. Đây là bẫy khi đọc riêng TT 01.
11. Bệnh viện công đang ký số theo **TT 41/2017/TT-BTTTT**, nhưng TT này bị bãi bỏ từ 15/11/2026, nên phải chuyển căn cứ sang NĐ 23/2025.
12. Thẩm quyền giám định BHYT đã chuyển sang **Bộ Tài chính** (TT 12/2026/TT-BTC). Không trích các quy trình giám định cũ do BHXH VN tự ban hành.
13. **Luật KCB**: trích theo VBHN 26/VBHN-VPQH. Đ52, 69, 112, 120 đã đối chiếu với VBHN (G), nhưng cần kiểm thêm các điều Luật Dân số đã sửa.
14. **ND-188-2025 Đ69 k9** (xác thực dữ liệu từ 01/01/2026) chỉ có F nhắc; I và T bỏ sót.
15. **NĐ 70/2025** vẫn đang được F và T trích. Phải đổi sang NĐ 254/2026.

---

## 4. DÒNG THỜI GIAN HẠN CHÓT (2025 → xa nhất), mốc tham chiếu 2026-10-05

`[QUA]` là đã qua, phần mềm phải đáp ứng rồi. `[TỚI]` là sắp tới. `[?]` là ngày chưa chắc.

| Ngày | Mốc | Nội dung | ID | XM |
|---|---|---|---|---|
| 01/01/2025 | [QUA] | Phiếu hẹn, phiếu chuyển điện tử ký số; một số khoản Luật 51/2024 có HL; QĐ 3176 áp dụng đồng bộ; TT 37/2024 có HL | TT-01-2025-BYT, L-BHYT-SD-2024, QD-3176-2024-BYT, TT-37-2024-BYT | gốc / thứ cấp |
| 10/04/2025 | [QUA] | NĐ 23/2025 về chữ ký điện tử có HL | ND-23-2025 | gốc-OCR |
| 01/05/2025 | [QUA] | BYT, BTP, BCA chuẩn hóa và kết nối dữ liệu KCB cho chế độ ốm đau, thai sản | QD-69-2025-TTg | gốc-OCR |
| 01/06/2025 | [QUA] | NĐ 70/2025 về hóa đơn có HL (đã bị thay từ 01/07/2026); thẻ BHYT giấy hạn chế | ND-70-2025, CV-168-2025-BHXH | thứ cấp |
| 06/06/2025 | [QUA] | TT 13/2025 ban hành; TT 46/2018 và Mục VIII TT 54/2017 hết HL; CV 365 hướng dẫn kỹ thuật EMR | TT-13-2025-BYT, CV-365-2025-TTYQG | gốc-OCR (G) |
| 01/07/2025 | [QUA] | Luật BHYT sửa đổi, Luật Dược sửa đổi, Luật Dữ liệu, Luật Lưu trữ có HL; NĐ 102, 163, 164, 165/2025; TT 26 (đơn thuốc), TT 33 (lưu trữ), TT 23 (thống kê), TT 31; NĐ 188 (một phần); BHXH tiếp nhận dữ liệu theo QĐ 69; QĐ 20/2025/QĐ-TTg | nhiều ID | gốc |
| 21/07/2025 | [QUA] | TT 13/2025 có HL; NĐ 113/2025 (lưu trữ) có HL | TT-13-2025-BYT, ND-113-2025 | gốc-OCR |
| 01/08/2025 | [QUA] | Cập nhật phần mềm theo danh mục mã của QĐ 2010/2025 | QD-2010-2025-BYT | thứ cấp |
| 15/08/2025 | [QUA] | NĐ 188/2025 có HL toàn bộ; quy trình KCB BHYT mới (QĐ 2555) | ND-188-2025, QD-2555-2025-BYT | gốc-OCR / thứ cấp |
| 19/08/2025 | [QUA] | NĐ 194/2025 (kết nối, chia sẻ dữ liệu) có HL | ND-194-2025 | gốc-meta |
| 01/09/2025 | [QUA] | TT 27/2025 và TT 24/2025 (danh mục BHYT) có HL | TT-27-2025-BYT, TT-24-2025-BYT | gốc-meta |
| 30/09/2025 | [QUA] | **Bệnh viện hoàn thành HSBA điện tử** (TT 13 Đ4 k2a); 100% BV có BAĐT và liên thông (CT 07/CT-TTg, tháng 9/2025) | TT-13-2025-BYT, CT-07-2025-TTg | gốc-OCR |
| 01/10/2025 | [QUA] | **Bệnh viện kê đơn điện tử** (hạn là "trước 01/10/2025") | TT-26-2025-BYT | gốc |
| 22/10/2025 | [QUA] | NĐ 278/2025 có HL | ND-278-2025 | gốc-meta |
| 31/12/2025 | [QUA] | Hết dùng mẫu giấy hẹn và giấy chuyển tuyến cũ | TT-01-2025-BYT | gốc |
| 01/01/2026 | [QUA] | **Cơ sở KCB khác kê đơn điện tử**; Luật BVDLCN và NĐ 356 có HL (NĐ 13 hết HL); **liên thông Sổ SKĐT VNeID cho mọi người bệnh** (QĐ 31 Đ5); **xác thực dữ liệu BHYT** (NĐ 188 Đ69 k9); dữ liệu dược được tính từ ngày này; Luật CNCNS, Luật sửa TCQC, Luật sửa Thống kê; NQ 261/2025/QH15 có HL | TT-26-2025-BYT, L-BVDLCN-2025, ND-356-2025, QD-31-2026-BYT, ND-188-2025, CV-3656-2026-QLD | gốc / thứ cấp |
| 06/01/2026 | [QUA] | QĐ 31/QĐ-BYT ký (áp dụng hồi tố từ 01/01/2026) | QD-31-2026-BYT | gốc (G) |
| 01/03/2026 | [QUA] | Luật AI có HL; TT 55/2025 (kê đơn thuốc cổ truyền) có HL; Luật Quy hoạch sửa Luật KCB; hết chuyển tiếp cổng BHXH theo NĐ 164 | L-AI-2025, TT-55-2025-BYT, L-QH-2025, ND-164-2025 | gốc |
| 01/04/2026 | [QUA] | Biểu mẫu giám định, thanh toán, quyết toán theo TT 12/2026/TT-BTC | TT-12-2026-BTC | gốc-OCR |
| 15/05/2026 | [QUA] | NĐ 90/2026 (xử phạt y tế) có HL | ND-90-2026 | gốc-OCR |
| 19/05/2026 | [QUA] | QĐ 11/2026/QĐ-TTg (danh mục CSDLQG) có HL | QD-11-2026-TTg | gốc-OCR |
| 01/06/2026 | [QUA] | Phiếu hẹn, phiếu chuyển điện tử dùng **ký số của cơ sở** thay đóng dấu | TT-06-2026-BYT | gốc |
| 01/07/2026 | [QUA] | Luật ANM 2025, Luật CĐS, Luật TMĐT, Luật Phòng bệnh, Luật Dân số có HL; Luật CNTT, Luật ATTTM, Luật ANM 2018 hết HL; **ICD-10 theo TT 06/2026**; **NĐ 254/2026 về hóa đơn** (NĐ 123, NĐ 70 hết HL); NĐ 165, 224, 248, 174/2026; TT 15/2026, TT 24/2026, TT 91/2026-BTC, TT 39 và 41/2026-BKHCN, TT 53/2025-BKHCN, TT 47/2026-BCA; **hạn nâng cấp phần mềm theo mẫu bảng kê QĐ 697**; QĐ 1931/2026 áp dụng [?]; TT 25/2026 Đ2, Đ3 [?] | nhiều ID | gốc / thứ cấp |
| 15/07/2026 | [QUA] | Đồng bộ xong dữ liệu KSK tồn đọng lên Sổ SKĐT | QD-1551-2026-BYT | gốc |
| 01/08/2026 | [QUA] | Áp dụng mã loại hình KCB và mã khoa mới (QĐ 1804) | QD-1804-2026-BYT | thứ cấp (G) |
| 15/08/2026 | [QUA] | QĐ 33/2026/QĐ-TTg (AI rủi ro cao) có HL; TT 25/2026 có HL | QD-33-2026-TTg, TT-25-2026-BYT | gốc-OCR / gốc-meta |
| 18/08/2026 | [QUA] | NĐ 313/2026 (tổ chức BYT) có HL | ND-313-2026 | gốc |
| 19/08/2026 | [QUA] | NĐ 330, 331, 333, 329, 332/2026 có HL; điểm đ k1 Đ5 TT 02/2018 (GPP) bị bãi bỏ | ND-331-2026, ND-330-2026, QD-2656-2026-BYT | gốc-OCR / gốc |
| 01/09/2026 | [QUA] | NĐ 301/2026: mẫu tờ khai liên thông khai sinh và khai tử mới; NĐ 341/2026 | ND-301-2026 | gốc-meta |
| 30/09/2026 | [QUA] | Đánh giá ATTT/cấp độ các hệ thống (CT 07/CT-BYT) | CT-07-2026-BYT | thứ cấp |
| 04/10/2026 | [QUA] | Hạn đăng ký tài khoản Hệ thống CSDL dược | CV-3656-2026-QLD | thứ cấp |
| **05/10/2026** | — | **Mốc tham chiếu** | | |
| 07/10/2026 | [TỚI] | Hết hạn góp ý dự thảo TT thay TT 48/2017 (gửi dữ liệu ≤ 03 giờ) | DT-TT48 | thứ cấp |
| 10/2026 | [TỚI] | Kỳ họp 2 QH: Luật sửa 6 luật y tế, Luật Định danh và xác thực điện tử; hoàn thiện Sổ SKĐT trên VNeID (NQ 221) | DT-LUAT-6L, DT-LUAT-DDXT, NQ-221-2026-CP | thứ cấp |
| 15/10/2026 | [TỚI] | Hết chiến dịch 100 ngày Sổ SKĐT | CT-07-2026-BYT | thứ cấp |
| 11/11/2026 | [TỚI] | NĐ 363/2026 (xử phạt trong lĩnh vực dữ liệu) có HL | ND-363-2026 | gốc-meta |
| 15/11/2026 | [TỚI] | TT 41/2017/TT-BTTTT bị bãi bỏ (chữ ký số trong CQNN) | TT-59-2026-BKHCN | gốc |
| **31/12/2026** | [TỚI] | **Cơ sở KCB không phải BV có điều trị nội trú, ban ngày hoặc ngoại trú hoàn thành HSBA điện tử** (TT 13 Đ4 k2b); mục tiêu 100% cơ sở KCB (QĐ 586); Sổ SKĐT toàn dân (NQ 282); hết dùng biên lai giấy (NĐ 254 Đ44 k2, chỉ liên quan nếu đơn vị có dùng biên lai) | TT-13-2025-BYT, QD-586-2026-BYT, NQ-282-2025-CP, ND-254-2026 | gốc-OCR / thứ cấp |
| **01/01/2027** | [TỚI] | **TT 38/2024 có HL** (cung cấp dữ liệu lên HTTT quản lý KCB); **Luật KCB Đ120**: k8 HTTT vận hành, k5a điều kiện CNTT cho GPHĐ mới, k6b tiêu chuẩn chất lượng cho cơ sở không phải BV; **liên thông và sử dụng kết quả CLS** (Luật 51/2024 Đ3 k4); **thẩm định cấp độ chuyển tiếp** (NĐ 331 Đ39); **BV dừng bệnh án giấy** (QĐ 586, thứ cấp); [?] TT thay TT 48; [?] TT BHYT cho KCB từ xa; biên lai điện tử | TT-38-2024-BYT, L-KCB-2023, L-BHYT-SD-2024, ND-331-2026, QD-586-2026-BYT, DT-TT48, DT-BHYT-TUXA | gốc / thứ cấp |
| 01/03/2027 | [TỚI] | Luật 20/2026/QH16 (sửa Luật GDĐT…) có HL; **TT 23/2025 (thống kê) hết HL**; AI rủi ro cao ngoài lĩnh vực y tế phải tuân thủ | L-SD4L-2026, TT-23-2025-BYT, QD-33-2026-TTg | gốc-meta / gốc |
| 30/06/2027 | [TỚI] | TTBYT mua sau ngày này phải kiểm định | TT-24-2026-BYT | gốc |
| **01/07/2027** | [TỚI] | **HTTT phải đáp ứng điều kiện an ninh mạng theo cấp độ mới** | L-ANM-2025 Đ45, ND-331-2026 Đ39 | gốc / gốc-OCR (G) |
| **01/09/2027** | [TỚI] | **AI y tế thuộc danh mục rủi ro cao** (vận hành trước 15/08/2026) và AI y tế vận hành trước 01/03/2026 phải tuân thủ | QD-33-2026-TTg Đ4, L-AI-2025 Đ35 | gốc-OCR (G) / gốc |
| 01/01/2028 | [TỚI] | Áp dụng Danh mục kỹ thuật Phụ lục 02 (TT 23/2024 sửa bởi TT 25/2026); xong kiểm định TTBYT mua trước 01/07/2027 | TT-25-2026-BYT, TT-23-2024-BYT, TT-24-2026-BYT | gốc |
| **01/01/2029** | [TỚI] | Cơ sở có GPHĐ trước 2027 phải đáp ứng điều kiện hạ tầng CNTT kết nối HTTT quản lý KCB | L-KCB-2023 Đ120 k5b | gốc (G) |
| 01/01/2030 / 2030 | [TỚI] | Miễn viện phí mức cơ bản theo lộ trình (NQ 261); 100% HSBA không giấy (QĐ 965); 100% dân có Sổ SKĐT; 95% dữ liệu y tế được chuẩn hóa | NQ-261-2025-QH, QD-965-2026-BYT, QD-826-2026-TTg, QD-1308-2026-TTg, QD-1709-2026-BYT | thứ cấp / gốc-OCR |
| 30/06/2030 | [TỚI] | Tổng kết liên thông dữ liệu KCB với BHXH | QD-69-2025-TTg | gốc-OCR |
| 01/01/2031 | [TỚI] | Hết miễn trừ 5 năm cho DN nhỏ theo Luật BVDLCN (không áp dụng khi xử lý dữ liệu sức khỏe) | L-BVDLCN-2025 Đ38 | gốc |
| 01/01/2032 | [TỚI] | Yêu cầu năng lực tiếng Việt với người nước ngoài hành nghề (ngoại vi) | L-KCB-2023 Đ120 k4 | gốc (G) |
| Thường xuyên | — | Gửi đơn thuốc điện tử ngay sau khi khám (nội trú: trước khi ra viện); gửi dữ liệu KSK trong 24 giờ; gửi dữ liệu chi phí BHYT sau mỗi lượt KCB (dự thảo: ≤ 03 giờ); DPIA (60 ngày hay 6 tháng, xem MT-15); phản hồi yêu cầu của chủ thể dữ liệu trong 02 ngày làm việc; báo cáo thống kê trong 05 ngày làm việc sau kỳ; báo cáo ANM định kỳ (chốt số 14/12, gửi trước 25/12, NĐ 331 Đ35 theo F) | TT-26-2025-BYT, QD-1551-2026-BYT, ND-188-2025, ND-356-2025, TT-23-2025-BYT, ND-331-2026 | gốc / thứ cấp |

---

## 5. CỤM CHỦ ĐỀ ĐỀ XUẤT cho pha đào sâu

Các cụm được rút ra từ chính những chỗ dữ liệu dồn lại: văn bản trích chéo nhiều, hạn chót gắn với nhau, và các điểm mâu thuẫn còn treo. Mỗi cụm có khoảng 2–4 văn bản **lõi** phải đọc bản gốc, cộng 7–19 văn bản **tham chiếu** chỉ cần kiểm điều khoản cụ thể. Mục tiêu là mỗi cụm vừa sức một agent trong khoảng 30 phút. Một số văn bản dùng chung giữa các cụm (đánh dấu ↔).

### K1. HSBA điện tử: chức năng EMR, ký số, lưu trữ hồ sơ (18 văn bản)
- **Phạm vi**: nghĩa vụ triển khai EMR (BV và phòng khám), yêu cầu chức năng và phi chức năng, ký và xác nhận điện tử (cá nhân, tổ chức, người bệnh), lưu trữ và thời hạn, quyền người bệnh với HSBA, số hóa bệnh án giấy, chế tài.
- **Lõi**: TT-13-2025-BYT, CV-365-2025-TTYQG, L-KCB-2023 (Đ69), TT-32-2023-BYT (Chương X).
- **Tham chiếu**: TT-33-2025-BYT, QD-586-2026-BYT, QD-965-2026-BYT, CT-04-2026-BYT, TT-54-2017-BYT, DT-TT54, ND-23-2025, L-GDDT-2023 (Đ22 k4), ND-137-2024, TT-59-2026-BKHCN/TT-41-2017-BTTTT, L-LUUTRU-2024 + ND-113-2025, ND-90-2026 (Đ39) ↔.
- **Câu hỏi mở**:
  1. TT 13 Đ1–3 nguyên văn có dấu: tiêu chí thế nào là "triển khai" hoặc "hoàn thành" HSBA điện tử; Đ2 k3 "tiêu chuẩn kỹ thuật CNTT trong CQNN" hiện là văn bản nào.
  2. Phạm vi phòng khám (MT-25): đọc định nghĩa "điều trị ngoại trú" và Chương X (Đ51–52, PL XXVIII–XXIX, 82 mẫu) **bản gốc** TT 32/2023, không dùng hethongphapluat.
  3. CV 365 bản gốc ký số và Phụ lục "Mô tả dữ liệu trao đổi HSBA điện tử" (schema XML/JSON); yêu cầu cloud đặt tại VN; "cấp độ 2" đổi sang khung NĐ 331 thế nào.
  4. QĐ 586, QĐ 965, CT 04: mốc 01/01/2027 bỏ bệnh án giấy là nghĩa vụ hay chỉ là mục tiêu (MT-23); NĐ 90/2026 Đ39 k2 c, d nguyên văn, mức phạt cho cá nhân hay tổ chức.
  5. Thủ tục "công bố triển khai" hoặc tham gia Cổng BAĐT sau khi TT 46 bị bãi bỏ.
  6. Phụ lục TT 33/2025: thời hạn lưu đơn thuốc, ảnh CĐHA, nhật ký hệ thống (audit log); Luật Lưu trữ và NĐ 113/2025 yêu cầu gì về định dạng và hệ thống lưu trữ điện tử chuyên ngành.
  7. Ký số tổ chức (HSM, ký từ xa) cho bệnh viện công sau 15/11/2026; người bệnh ký bằng sinh trắc học hoặc OTP theo Luật GDĐT Đ22 k4.

### K2. Dữ liệu BHYT: chuẩn XML, danh mục mã BHYT, giám định và thanh toán (23 văn bản; nhiều QĐ danh mục mã nhỏ, nếu quá tải thì tách nhóm "danh mục mã" ra)
- **Phạm vi**: luồng HIS gửi BHXH (check-in, XML 130, xác thực, ký số), danh mục dùng chung, bảng kê, tra cứu thẻ, giám định và quyết toán.
- **Lõi**: ND-188-2025 (Đ66–72), TT-12-2026-BTC, QD-130-2023-BYT (+ QD-4750-2023, QD-3176-2024, QD-1931-2026), TT-48-2017-BYT / DT-TT48.
- **Tham chiếu**: L-BHYT-SD-2024, TT-01-2025-BYT, QD-7603-2018-BYT, QD-824-2023-BYT, QD-2010-2025-BYT, QD-3276-2025-BYT, QD-1804-2026-BYT, QD-697-2026-BYT, ND-164-2025, QD-2555-2025-BYT, TT-37-2024/TT-27-2025/TT-24-2025-BYT, DT-BTC-CONG, ND-90-2026 (Đ95) ↔.
- **Câu hỏi mở**:
  1. Bộ bảng XML hiện hành (từ XML0 đến XMLn) sau các QĐ 4750, 3176, 1931; QĐ 1931/2026 bản gốc (MT-08).
  2. QĐ 1804 bản gốc: 16 mã loại hình, 60 mã khoa K01–K60.
  3. TT 12/2026 Đ4, 7, 9, 10: thời hạn 15 ngày, cổng nộp, văn bản bị thay (MT-14).
  4. NĐ 188 Đ69 k9 (xác thực dữ liệu là xác thực người bệnh hay ký số hồ sơ), Đ71 k2 d (cổng), Mẫu số 8 (bảng kê phần mềm và phần cứng trong hợp đồng KCB BHYT), "tiêu chuẩn kết nối đã được xác thực" ở Đ68 k5 (có thủ tục xác thực phần mềm HIS không).
  5. DT-TT48: ngưỡng 03 giờ, quy trình nhắc nhở, cảnh báo, xử phạt; thời điểm ban hành.
  6. QĐ 697 bản gốc: yêu cầu ký số bảng kê.

### K3. Kê đơn điện tử, dược và nhà thuốc (19 văn bản)
- **Phạm vi**: e-prescription (mã đơn, nội dung đơn, thuốc kiểm soát đặc biệt), liên thông Hệ thống đơn thuốc QG, CSDL dược cho nhà thuốc và khoa dược, GPP, bán thuốc online, thuốc cổ truyền.
- **Lõi**: TT-26-2025-BYT, TT-55-2025-BYT, QD-808-2023-BYT / QD-425-2025-BYT.
- **Tham chiếu**: L-DUOC-2016, L-DUOC-SD-2024, ND-163-2025, TT-31-2025-BYT, TT-02-2018-BYT, TT-11-2025-BYT, QD-2656-2026-BYT, CV-934-2026-TTYQG, CV-3656-2026-QLD, QD-232-TTYQG, QD-1867-BYT, TT-20-2017-BYT, L-TMDT-2025 + ND-248-2026, ND-90-2026 (Đ59) ↔.
- **Câu hỏi mở**:
  1. Đặc tả kết nối Hệ thống đơn thuốc QG (QĐ 808/2023 còn là phiên bản hiện hành không; Cục KHCN&ĐT có ban hành đặc tả mới theo TT 26 không).
  2. Nghĩa vụ liên thông CSDL dược của nhà thuốc nằm ở văn bản QPPL nào (NĐ 163, TT 02/2018 sửa bởi TT 11/2025, hay chỉ ở công văn) (MT-32).
  3. QĐ 2656 bãi bỏ nội dung gì của điểm đ k1 Đ5 TT 02/2018.
  4. NĐ 90 Đ59 k2 d nguyên văn.
  5. Lộ trình kê đơn điện tử thuốc cổ truyền (TT 55 Đ10, Đ12).
  6. Sổ theo dõi thuốc kiểm soát đặc biệt dạng điện tử (TT 20/2017 sửa bởi TT 27/2024).
  7. Thời hạn lưu đơn thuốc ↔ K1.

### K4. Sổ SKĐT, VNeID, định danh và giấy tờ điện tử liên thông (Đề án 06) (22 văn bản; nếu quá tải thì tách nhóm "giấy tờ hộ tịch/BHXH" khỏi nhóm "Sổ SKĐT/KSK")
- **Phạm vi**: mã định danh người bệnh, VNeID mức 2, Sổ SKĐT, dữ liệu KSK, giấy chứng sinh, giấy báo tử, giấy nghỉ hưởng BHXH, giấy ra viện, KSK lái xe, tài khoản định danh tổ chức.
- **Lõi**: QD-31-2026-BYT, QD-2733-2024-BYT, QD-1551-2026-BYT, ND-102-2025 (Đ6, 9, 10).
- **Tham chiếu**: QD-1332-2024-BYT, QD-69-2025-TTg, ND-63-2024 + ND-301-2026, QD-1898-2025-BYT, TT-17-2012-BYT, TT-24-2020-BYT, QD-1996-2025-BYT, TT-25-2025-BYT, TT-36-2024-BYT, ND-69-2024, L-CANCUOC-2023/ND-70-2024, QD-826-2026-TTg, CT-17-2026-TTg, QD-940-2026-TTg, DT-LUAT-DDXT, NQ-66.7-2025-CP.
- **Câu hỏi mở**:
  1. QĐ 2733/2024 bản gốc: cấu trúc dữ liệu, kênh kết nối; có một hay nhiều điểm tích hợp (MT-30).
  2. Kênh chính thức của QĐ 1551: `app.qlhanhnghekcb.gov.vn`, `csdlksk.vn` hay `api.emrhub.vn` (MT-29); Phụ lục 01 và 02.
  3. Giấy nghỉ BHXH: TT 25/2025 Đ29 và Mẫu 07 bản gốc (datafiles 404).
  4. Giấy chứng sinh: QĐ 1898 và nội dung NĐ 301 sửa NĐ 63; TT 17/2012 còn HL không.
  5. Giấy báo tử: TT 24/2020, QĐ 1996/2025.
  6. KSK lái xe: TT 36/2024 bản gốc (PDF datafiles lỗi), kết nối với CSDL giao thông.
  7. Người nước ngoài, trẻ chưa có số định danh, người bệnh vô danh: cách định danh.

### K5. HTTT quốc gia, CSDL y tế và báo cáo bắt buộc (18 văn bản)
- **Phạm vi**: HTTT quản lý hoạt động KCB (TT 38/2024, HL 01/01/2027, **chỉ I phát hiện**), CSDLQG về y tế, kết nối chia sẻ bắt buộc, báo cáo thống kê, báo cáo bệnh truyền nhiễm, sự cố y khoa, tiêu chuẩn chất lượng.
- **Lõi**: TT-38-2024-BYT, L-KCB-2023 (Đ112, 120), TT-23-2025-BYT / DT-TT23, TT-15-2026-BYT.
- **Tham chiếu**: ND-102-2025 (Đ12–17, 23) ↔, QD-11-2026-TTg, ND-278-2025, ND-47-2024, ND-194-2025 + ND-47-2020, L-PB-2025 + ND-165-2026, TT-54-2015-BYT, QD-2114-2026-BYT, CT-07-2026-BYT, NQ-282-2025-CP, QD-3516-2025-BYT.
- **Câu hỏi mở**:
  1. TT 38/2024: danh sách trường dữ liệu, thời hạn gửi, chuẩn kết nối, phạm vi cơ sở; HTTT này đã vận hành chưa (QĐ 2114/2026).
  2. NĐ 102/2025 đọc lại từ PDF datafiles các Đ10 k5, Đ14–17, Đ23 (MT-21).
  3. TT 15/2026 có thay TT 54/2015 không; thời hạn báo cáo 24 hay 48 giờ; kênh báo cáo (MT-31).
  4. Văn bản thay TT 23/2025 trước 01/03/2027.
  5. Văn bản hướng dẫn Luật KCB Đ71 về sự cố y khoa hiện hành.
  6. Luật KCB Đ57 và Đ120 k6b: tiêu chuẩn chất lượng áp cho cơ sở không phải BV từ 01/01/2027, có tiêu chí CNTT không.
  7. CT 07/CT-BYT bản gốc (MT-37).

### K6. Mã hóa lâm sàng, danh mục kỹ thuật, kiến trúc và chuẩn liên thông (16 văn bản)
- **Phạm vi**: ICD-10 (kiểm tra hợp lệ theo cột 24–29), danh mục kỹ thuật PL 02 (2028), thuật ngữ lâm sàng, kiến trúc số và kiến trúc dữ liệu ngành, HL7, FHIR, DICOM, TCVN tin học y tế.
- **Lõi**: TT-06-2026-BYT, QD-2146-2026-BYT, QD-2113-2026-BYT, TT-23-2024-BYT + TT-25-2026-BYT (Đ3).
- **Tham chiếu**: QD-1849-2026-BYT, QD-4469-2020-BYT, QD-2427-2025-BYT, QD-7713-2016-BYT, QD-3926-2017-BYT, TCVN-12344-2019, DT-DMDL, QD-2439-2025-TTg, QD-1308-2026-TTg, L-TCQC-SD-2025 + ND-22-2026.
- **Câu hỏi mở**:
  1. QĐ 2146 và QĐ 2113 bản gốc: có bắt buộc HL7 FHIR R4, DICOM/DICOMweb, LOINC, SNOMED không (MT-24); đối tượng áp dụng chỉ là hệ thống của Bộ hay cả cơ sở KCB.
  2. QĐ 7713/2016 và QĐ 3926/2017 về HL7 còn HL không.
  3. Quan hệ QĐ 1849/2026 và QĐ 4469/2020 với TT 06/2026.
  4. Danh mục kỹ thuật PL 02: cấu trúc mã và ánh xạ với mã DVKT BHYT.
  5. QĐ 2427/2025 về thuật ngữ lâm sàng: phạm vi, định dạng.
  6. Lộ trình ICD-11: không thấy văn bản nào, cần xác nhận là chưa có.

### K7. CLS liên thông, LIS, RIS/PACS và phần mềm là thiết bị y tế (11 văn bản)
- **Phạm vi**: mốc 01/01/2027 liên thông kết quả CLS, metadata kết quả, quản lý chất lượng xét nghiệm, lưu ảnh, phân loại phần mềm là TTBYT (SaMD), tiêu chí CNTT cho LIS và RIS-PACS.
- **Lõi**: L-BHYT-SD-2024 (Đ3 k4) ↔, DT-CLS-LT, ND-98-2021 (Đ2) + TT-24-2026-BYT (sửa TT 05/2022).
- **Tham chiếu**: TT-01-2013-BYT + TT-25-2026-BYT (Đ1), TT-54-2017-BYT (nhóm tiêu chí LIS, RIS-PACS) ↔, QD-4868-2015-BYT, DT-QD586-SP (giá RIS-PACS không in phim), TT-33-2025-BYT (lưu ảnh) ↔, QD-2146-2026-BYT (DICOM) ↔.
- **Câu hỏi mở**:
  1. "Theo quy định của Chính phủ" ở Luật 51 Đ3 k4 là văn bản nào (NĐ 188 có điều nào không, hay chờ DT-CLS-LT).
  2. DT-CLS-LT: định dạng trao đổi, liên thông ảnh gốc hay chỉ kết luận, thời hạn giá trị theo từng dịch vụ (MT-26).
  3. NĐ 98/2021 Đ2 và TT 05/2022 (bản sửa bởi TT 24/2026): có quy tắc phân loại rủi ro riêng cho phần mềm không; PACS viewer, CAD, LIS middleware có phải công bố hoặc đăng ký lưu hành không.
  4. Thời hạn lưu ảnh DICOM và phim theo TT 33/2025.
  5. TT 25/2026 Đ1 (sửa TT 01/2013) có yêu cầu gì với LIS (lưu nội kiểm, ngoại kiểm).

### K8. Bảo vệ dữ liệu cá nhân và quản trị dữ liệu y tế (12 văn bản)
- **Phạm vi**: đồng ý xử lý, quyền của chủ thể dữ liệu, dữ liệu sức khỏe là dữ liệu nhạy cảm, cấm chia sẻ cho bảo hiểm, DPIA, chuyển dữ liệu ra nước ngoài, vendor là "dịch vụ xử lý DLCN", dữ liệu quan trọng và cốt lõi, chế tài.
- **Lõi**: L-BVDLCN-2025, ND-356-2025, ND-102-2025 (Đ9–10) ↔.
- **Tham chiếu**: ND-13-2023 (chuyển tiếp), ND-330-2026, ND-363-2026, L-DULIEU-2024 + ND-165-2025, QD-20-2025-TTg, QD-2623-2025-TTg, ND-169-2025, ND-314-2026.
- **Câu hỏi mở**:
  1. NĐ 356: Đ13, Đ17–20 (DPIA 60 ngày hay cập nhật 6 tháng), Đ21 k4 và Đ22–26 (vendor SaaS HIS/EMR hoặc app sức khỏe có cần giấy chứng nhận dịch vụ xử lý DLCN không), Đ29 (thông báo vi phạm 72 giờ), Đ41 (ngưỡng 100.000) (MT-15).
  2. Luật 91: Đ19 k1 (các trường hợp không cần đồng ý, như cấp cứu hay theo luật chuyên ngành), Đ26 k2–3 (bảo lãnh viện phí với bảo hiểm tư nhân), Đ33 k2.
  3. Luật Dữ liệu và QĐ 20/2025: mục 25 là dữ liệu "quan trọng" hay "cốt lõi"; điều kiện chuyển dữ liệu y tế ra nước ngoài.
  4. NĐ 330/2026: mức phạt áp với cơ sở KCB và vendor.

### K9. An ninh mạng và cấp độ HTTT (13 văn bản)
- **Phạm vi**: phân loại cấp độ HIS, EMR, LIS, PACS, app; hồ sơ đề xuất cấp độ; chuyển tiếp đến 2027; giám sát tập trung; báo cáo sự cố; lưu trữ dữ liệu trong nước; quy chế ANM của BYT.
- **Lõi**: L-ANM-2025 (Đ40, 41, 44, 45), ND-331-2026 (Đ11–16, 31, 35, 39), ND-333-2026.
- **Tham chiếu**: ND-85-2016, TT-12-2022-BTTTT, TT-03-2017-BTTTT, ND-53-2022, QD-326-2024-BYT, QD-425-2025-BYT ↔, CT-07-2026-BYT ↔, TT-47-2026-BCA, TT-39-2017-BTTTT / QD-742-2022-BTTTT.
- **Câu hỏi mở**:
  1. Văn bản bãi bỏ chính thức NĐ 85/2016 và TT 12/2022 (MT-04).
  2. NĐ 331 Đ12–13: tiêu chí riêng cho lĩnh vực y tế; app KCB trực tuyến có phải cấp 3 không (MT-16); Đ31 thời hạn báo cáo sự cố (MT-17).
  3. NĐ 333/2026: yêu cầu lưu trữ dữ liệu tại VN (trước đây nằm ở NĐ 53/2022); áp dụng cho SaaS y tế thế nào.
  4. Luật 116 Đ40 k1b: nghĩa vụ kết nối giám sát tập trung với bệnh viện tư; Đ41 định danh IP có áp cho SaaS không.
  5. TT 47/2026/TT-BCA có áp cho BV công (đơn vị sự nghiệp) không.

### K10. KCB từ xa, app sức khỏe và AI (13 văn bản)
- **Phạm vi**: điều kiện KCB từ xa, danh mục bệnh, thanh toán BHYT cho KCB từ xa, app phục vụ người bệnh, AI rủi ro cao trong y tế, đạo đức AI.
- **Lõi**: ND-96-2023 (Đ87–88), TT-30-2023-BYT, L-AI-2025 (Đ35) + QD-33-2026-TTg.
- **Tham chiếu**: L-KCB-2023 (Đ80) ↔, DT-BHYT-TUXA, TT-49-2017-BYT, TT-53-2014-BYT, ND-142-2026, TT-05-2026-BKHCN, QD-804-2026-TTg, NQ-21-2026-CP, DT-CTMTQG.
- **Câu hỏi mở**:
  1. NĐ 96 Đ87 có bị sửa không (VBHN 10/VBHN-BYT 2026; NQ 21/2026 cắt giảm thủ tục).
  2. TT 30/2023 bản gốc: danh mục 50 bệnh theo mã ICD.
  3. TT 49/2017 và TT 53/2014 còn HL không.
  4. QĐ 33/2026: đọc đủ danh mục y tế. OCR mới thấy 2 mục (phẫu thuật/rô-bốt, điều khiển điều trị). CDSS, AI đọc ảnh, chatbot y tế có trong danh mục không (MT-06). NĐ 142/2026 Đ8 tiêu chí rủi ro cao.
  5. App phục vụ người bệnh: tổng hợp nghĩa vụ từ Luật 91 Đ26 k3, NĐ 356 Đ21 k4, NĐ 331 cấp độ ↔ K8, K9.

### K11. Hóa đơn, thanh toán và mua sắm/thuê dịch vụ CNTT (15 văn bản)
- **Phạm vi**: hóa đơn điện tử viện phí và nhà thuốc, biên lai, thanh toán không dùng tiền mặt, miễn viện phí 2030, đấu thầu và thuê HIS/EMR tại bệnh viện công.
- **Lõi**: ND-254-2026, TT-91-2026-BTC, L-CDS-2025 + ND-224-2026.
- **Tham chiếu**: L-QLT-2025, ND-70-2025 / ND-123-2020 (chỉ để tra lịch sử), ND-52-2024, TT-15-2024-NHNN, CD-124-2025-TTg, QD-1813-2021-TTg, TT-34-2025-BKHCN, TT-39-2026-BKHCN, TT-41-2026-BKHCN, NQ-261-2025-QH.
- **Câu hỏi mở**:
  1. NĐ 254 điểm m nguyên văn (hóa đơn tổng hợp cuối ngày, hóa đơn cho BHXH lúc quyết toán); hóa đơn từ máy tính tiền cho phòng khám và nhà thuốc là hộ kinh doanh; Đ44 k2 (biên lai) có áp cho BV công không.
  2. Có nghĩa vụ thanh toán không dùng tiền mặt nào ràng buộc cơ sở KCB không (hiện chỉ thấy chủ trương).
  3. Thuê dịch vụ HIS/EMR bằng NSNN: TT 39/2026 và 41/2026, quan hệ với TT 18/2024/TT-BTTTT; ưu đãi theo TT 34/2025.
  4. NQ 261: logic mức hưởng 100% ảnh hưởng gì tới module viện phí.

**Văn bản ngoại vi** (ít liên quan tới phần mềm, đề xuất loại khỏi trọng tâm và chỉ tra khi cần): L-THONGKE-SD-2025, L-TCQC-SD-2025, ND-22-2026, L-CNCNS-2025, ND-353-2025, L-QH-2025, L-DANSO-2025 (trừ phần sửa Luật KCB), ND-169-2025, ND-314-2026, ND-329-2026, ND-332-2026, ND-341-2026, ND-343-2026, ND-31-2026, ND-174-2026, TT-170-2026-BCA, TT-107/116/126-2025-BTC, QD-268-2026-TTg, QD-2623-2025-TTg, QD-2629-2025-TTg, QD-844-2026-TTg, QD-1266-2026-TTg, QD-34-2021-TTg, CT-24-2025-TTg, QD-1272-2026-BYT, TT-42-2025-BYT, TT-24-2026-BYT (phần thiết bị phần cứng), ND-313-2026 và ND-42-2025 (chỉ là bối cảnh thẩm quyền), NQ-125-2026-CP, NQ-72-2025-TW, KL-76-2026-TW, CT-52-TW, QD-1709-2026-BYT, NQ-221-2026-CP, TT-19-2025-BKHCN, TT-53-2025-BKHCN, L-SD4L-2026 (cho tới khi biết nội dung phần sửa Luật GDĐT). Ngoài ra là 25 văn bản đã hết HL, chỉ giữ để tra chuỗi thay thế.

---

## 6. KHOẢNG TRỐNG (câu hỏi để pha 2 kiểm tra, không phải khẳng định)

1. **Phần mềm là thiết bị y tế (SaMD)**: NĐ 98/2021 Đ2 nói TTBYT gồm cả phần mềm, nhưng không bản nào tìm ra quy tắc phân loại rủi ro cho phần mềm, thủ tục công bố hoặc đăng ký lưu hành, hay yêu cầu hồ sơ kỹ thuật. PACS viewer, CAD, CDSS, LIS middleware có bị coi là TTBYT không?
2. **LIS**: có QCVN hay hướng dẫn nào về định dạng kết quả xét nghiệm, kết nối máy xét nghiệm, mã chỉ số xét nghiệm chuẩn (QĐ 965 có nhắc "danh mục chỉ số XN chuẩn"), LOINC không? TT 01/2013 sửa bởi TT 25/2026 có yêu cầu phần mềm không?
3. **RIS/PACS**: thời hạn lưu ảnh và phim trong phụ lục TT 33/2025; "hướng dẫn giá RIS-PACS không in phim"; định dạng liên thông ảnh theo DT-CLS-LT; các quy định an toàn bức xạ có ràng buộc phần mềm RIS không?
4. **Y học cổ truyền**: ngoài TT 55/2025 (đơn thuốc), có mẫu bệnh án YHCT, danh mục mã bệnh YHCT hay ánh xạ ICD dùng trong HIS không? TT 27/2025 (danh mục BHYT thuốc cổ truyền) đặt yêu cầu gì về master data?
5. **Phòng khám nha khoa, thẩm mỹ, chuyên khoa**: có mẫu HSBA ngoại trú chuyên khoa riêng không (TT 32/2023)? HSBA phẫu thuật thẩm mỹ lưu 20 năm (TT 33) có áp cho phòng khám không? Phòng khám chỉ khám và kê đơn có thuộc TT 13 không (MT-25)?
6. **Nhà thuốc GPP**: nội dung TT 02/2018 sau các lần sửa, TT 11/2025, QĐ 2656: yêu cầu phần mềm và kết nối là gì? Nhà thuốc là hộ kinh doanh có phải dùng hóa đơn từ máy tính tiền theo NĐ 254 không?
7. **Hóa đơn và giá viện phí**: văn bản về giá dịch vụ KCB, niêm yết giá, giá theo yêu cầu (Luật KCB Đ112 k1 đ) mà phần mềm phải đáp ứng. Cả 3 bản đều chưa đụng tới. Biên lai điện tử cho đơn vị sự nghiệp công.
8. **Tiếng Việt và khả năng tiếp cận**: có yêu cầu bắt buộc về ngôn ngữ trên hồ sơ, đơn thuốc, app (tiếng Việt, Unicode TCVN 6909) không? Có chuẩn tiếp cận cho người khuyết tật với app hoặc cổng y tế không (Luật Người khuyết tật nằm trong DT-LUAT-6L)?
9. **Quảng cáo dịch vụ y tế trên app hoặc website**: Luật Quảng cáo và các văn bản của BYT về quảng cáo KCB, thông tin thuốc trên nền tảng số, đánh giá bác sĩ. Không bản nào khảo sát.
10. **Dữ liệu nhạy cảm chuyên biệt**: HIV/AIDS, sức khỏe tâm thần, ma túy, di truyền, sinh sản (IVF), hiến và ghép mô tạng. Có quy định bảo mật riêng ràng buộc phân quyền và chia sẻ trong HIS không?
11. **Tiêm chủng**: hệ thống quản lý tiêm chủng QG và nghĩa vụ kết nối của cơ sở KCB theo Luật Phòng bệnh. Hiện chỉ thấy gián tiếp qua nhóm dữ liệu Sổ SKĐT.
12. **Lưu trữ dữ liệu trong nước và cloud**: CV 365 yêu cầu cloud đặt tại VN, nhưng căn cứ ở luật (Luật ANM 2025, NĐ 333, Luật Dữ liệu) chưa ai đọc.
13. **Quản lý đầu tư và thuê dịch vụ CNTT dùng NSNN** sau Luật CĐS: văn bản trước đây về quản lý đầu tư ứng dụng CNTT còn hiệu lực hay đã bị NĐ 224/2026 và các TT 39, 41/2026 thay?
14. **Chứng nhận hoặc kiểm thử phần mềm HIS trước khi kết nối BHXH**: NĐ 188 Đ68 k5 nói "tiêu chuẩn kết nối đã được xác thực". Có thủ tục xác thực nào không?
15. **Sự cố y khoa**: văn bản hướng dẫn Luật KCB Đ71 (biểu mẫu báo cáo, hệ thống báo cáo) mà phân hệ quản lý sự cố phải đáp ứng.
16. **Tiêu chuẩn chất lượng cơ sở KCB** (Luật KCB Đ57, Đ120 k6b từ 01/01/2027 cho cơ sở không phải BV): có tiêu chí CNTT hoặc dữ liệu không?
17. **Bảo hiểm sức khỏe tư nhân và bảo lãnh viện phí**: Luật Kinh doanh bảo hiểm cùng Luật 91 Đ26 điều chỉnh luồng dữ liệu HIS sang công ty bảo hiểm thế nào?
18. **Chữ ký và xác thực sinh trắc của người bệnh**: các QCVN sinh trắc (TT 170/2026-BCA về mống mắt; trang vanban còn liệt kê QCVN giọng nói) có áp cho ký xác nhận trên HSBA không?
19. **Nhật ký truy cập và thời hạn lưu log**: có văn bản nào quy định thời hạn lưu log truy cập HSBA không (CV 365 chỉ yêu cầu ghi vết; dự thảo Luật ĐD&XTĐT nêu ≥5 năm cho log xác thực)?
20. **Các docid trơn trong mục §12 của I** (219235, 216452, 219586, 219479, 219489, 218842, 216991, 216427, 213682, 216632) chưa được gắn với văn bản nào trong bảng của I. Có thể còn văn bản bị bỏ sót.

---

## 7. LINK CÓ VẤN ĐỀ và đề xuất xử lý

### 7.1 Link có verdict khác OK trong `linkcheck-all.json` (17 URL)

| # | URL | Verdict | Dùng cho | Đề xuất |
|---|---|---|---|---|
| 1 | https://ttyttpbaclieu.gov.vn/upload/1000078/fck/files/2_2_1_Ph____l___c_b__o_c__o_____nh_gi___ph___m_m___m_theo_TT13_CV365_aa703.pdf | LỖI: curl exit 60 (SSL) | CV 365 (F, S4) | **Giữ làm bối cảnh** (nguồn duy nhất trích nguyên văn CV 365). Pha 2 tìm bản gốc CV 365 ký số trên trang của Sở Y tế hoặc TT Thông tin y tế QG; nhic.vn cũng có lỗi SSL |
| 2 | https://hethongphapluat.com/nghi-dinh-102-2025-nd-cp-quy-dinh-quan-ly-du-lieu-y-te.html | LỖI: curl exit 28 (timeout) | NĐ 102/2025 (F, S13) | **Bỏ.** Trang từng chèn chỉ dẫn nhắm vào AI. Thay bằng [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/102-ndcp.signed.pdf) hoặc [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-102-2025-nd-cp-44865.htm). Cũng bỏ trang hethongphapluat của TT 32/2023 (S41, linkcheck OK nhưng nguồn không tin cậy) và tìm bản gốc TT 32 |
| 3 | https://vbpl.vn/TW/Pages/vbpq-van-ban-goc.aspx?ItemID=178219 | BỊ ĐẨY VỀ TRANG CHỦ | TT 13/2025 (T) | **Bỏ.** Thay bằng [PDF sao y, SYT Quảng Ninh](https://soytequangninh.gov.vn/upload/1002610/20250610/THONG_TU_HSBA_DIEN_TU_21_7_2025TT_13_2025__TT-BYT_ngay_6_6_2025_f5604afb8f.pdf) |
| 4 | https://xaydungchinhsach.chinhphu.vn/lo-trinh-trien-khai-ho-so-benh-an-dien-tu-tai-cac-benh-vien-119250610163849953.htm | Không thấy số hiệu | TT 13/2025 (I, T) | **Thay** bằng PDF sao y ở trên; giữ làm bối cảnh |
| 5 | https://xaydungchinhsach.chinhphu.vn/chi-thi-so-17-ct-ttg-to-chuc-kham-suc-khoe-dinh-ky-kham-sang-loc-mien-phi-cho-nguoi-dan-119260507075549614.htm | Không thấy số hiệu | CT 17/CT-TTg (I) | **Thay** bằng trang VB hoặc PDF gốc của CT 17 (pha 2 tìm docid); tạm dùng [VB 219523 (CV 1129)](https://vanban.chinhphu.vn/?pageid=27160&docid=219523) |
| 6 | https://suckhoedoisong.vn/lo-trinh-chuyen-doi-sang-benh-an-dien-tu-169260917103408166.htm | Không thấy số hiệu | QĐ 965 (I) | **Giữ làm bối cảnh**; link chính là luatvietnam (OK), pha 2 tìm bản gốc |
| 7 | https://suckhoedoisong.vn/bo-truong-bo-y-te-yeu-cau-day-manh-xu-ly-dut-diem-cac-diem-nghen-chuyen-doi-so-y-te-169260915171532468.htm | Không thấy số hiệu | CT 07/CT-BYT (I) | **Giữ làm bối cảnh**; pha 2 tìm bản gốc CT 07/CT-BYT |
| 8 | https://suckhoedoisong.vn/bo-y-te-trinh-quoc-hoi-4-du-an-luat-nhieu-chinh-sach-moi-trong-linh-vuc-y-te-169261001083058112.htm | Không thấy số hiệu | DT-LUAT-6L (I) | **Giữ làm bối cảnh** (dự thảo, chưa có số hiệu là bình thường) |
| 9 | https://www.vietnamplus.vn/co-so-kham-chua-benh-gui-du-lieu-dien-tu-cham-co-the-bi-xu-phat-hanh-chinh-post1139262.vnp | Không thấy số hiệu | DT-TT48 (T) | **Giữ làm bối cảnh**; link chính là vtv (OK). Pha 2 tìm toàn văn dự thảo trên cổng lấy ý kiến của BYT |
| 10 | https://baochinhphu.vn/bo-y-te-chuan-bi-trinh-quoc-hoi-4-du-an-luat-trong-do-co-1-luat-sua-nhieu-luat-102261001180003719.htm | Không thấy số hiệu | DT-LUAT-6L (T) | **Giữ làm bối cảnh** |
| 11 | https://www.vietnamplus.vn/bo-y-te-yeu-cau-day-manh-xu-ly-dut-diem-cac-diem-nghen-chuyen-doi-so-y-te-post1136364.vnp | Không thấy số hiệu | CT 07/CT-BYT, DT-DMDL (T) | **Giữ làm bối cảnh** |
| 12 | https://suckhoedoisong.vn/bo-y-te-day-nhanh-tien-do-cac-nhiem-vu-chuyen-doi-so-thao-go-diem-nghen-du-lieu-va-dich-vu-so-169261003100416305.htm | Không thấy số hiệu | DT-DMDL (T) | **Giữ làm bối cảnh** |
| 13 | https://xaydungchinhsach.chinhphu.vn/nghi-dinh-so-23-2025-nd-cp-quy-dinh-ve-chu-ky-dien-tu-va-dich-vu-tin-cay-119250225073330307.htm | Không thấy số hiệu | NĐ 23/2025 (T) | **Thay** bằng [VB 212829](https://vanban.chinhphu.vn/?pageid=27160&docid=212829) và [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/02/23-cp.signed.pdf) |
| 14 | https://suckhoedoisong.vn/bo-y-te-quy-dinh-moi-nhat-danh-muc-ma-kham-chua-benh-ma-khoa-cho-kham-bhyt-169260628130847556.htm | Không thấy số hiệu | QĐ 1804 (T) | **Thay** bằng [tin BHXH VN](https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=26715&CateID=169) (OK, có kèm file QĐ). Pha 2 tải file QĐ 1804 đính kèm |
| 15 | https://xaydungchinhsach.chinhphu.vn/nghi-quyet-72-nq-tw-cua-bo-chinh-tri-ve-mot-so-giai-phap-dot-pha-tang-cuong-bao-ve-cham-soc-va-nang-cao-suc-khoe-nhan-dan-119250912060746502.htm | Không thấy số hiệu | NQ 72-NQ/TW (T) | **Giữ làm bối cảnh** (văn kiện Đảng, ngoại vi) |
| 16 | https://lsvn.vn/de-xuat-benh-vien-hang-i-co-them-02-nam-de-trien-khai-ho-so-benh-an-dien-tu-a150260.html | Không thấy số hiệu | Dự thảo cũ của TT 13 (T, năm 2024) | **Bỏ** (lỗi thời, mốc trong bài đã bị TT 13 thay) |
| 17 | https://baochinhphu.vn/nhung-noi-dung-moi-cua-nghi-dinh-so-70-2025-nd-cp-ve-hoa-don-chung-tu-102250903091616929.htm | Không thấy số hiệu | NĐ 70/2025 (F) | **Bỏ** vì văn bản đã hết HL (MT-01). Thay bằng [VB 218689 (NĐ 254/2026)](https://vanban.chinhphu.vn/?pageid=27160&docid=218689) |

### 7.2 Link có verdict OK nhưng vẫn cần lưu ý

| URL / nhóm | Vấn đề | Đề xuất |
|---|---|---|
| https://vanban.chinhphu.vn/?pageid=27160&docid= (không có số) | Là tiền tố trơn trong mục §12 của I, bị linkcheck tính là OK nhưng vô nghĩa. Các docid liệt kê kèm theo chưa được kiểm từng cái | Bỏ; pha 2 kiểm 10 docid chưa gắn văn bản (khoảng trống #20) |
| https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/36-byt.pdf | HTTP 200 nhưng theo F file PDF hỏng (lỗi xref) | Thử tải lại hoặc sửa PDF; nếu không được thì tạm dùng luatvietnam |
| PDF scan: `15luat.signed.pdf`, `12-btc.pdf`, `331_2026…signed.pdf`, `254-ndcp.signed.pdf`, `33-qdttg.signed.pdf`, `188-ndcp.signed.pdf`, `91qh.signed.pdf`, `356-nd.signed.pdf`… | OK nhưng là bản scan; doc_match = null vì script không đọc được chữ | Giữ làm link gốc. Khi trích phải OCR có dấu (tesseract `vie`) hoặc dùng bản DOCX trên Công báo. Riêng Luật KCB đã có **VBHN text** thay thế |
| https://benhandientu.moh.gov.vn/van-bang-phap-ly-co-hieu-luc | OK nhưng nội dung lỗi thời (vẫn ghi TT 46/2018 còn HL) | Chỉ giữ làm bối cảnh; không dùng để xác định tình trạng hiệu lực |
| https://ytesovietnam.vn/quyet-dinh-2146-2113-khung-kien-truc-so-kien-truc-du-lieu-y-te và https://hl7.org.vn/kien-thuc/fhir-va-bhyt/ | OK nhưng không phải trang chính thức; là nguồn duy nhất của nhận định "bắt buộc FHIR" | Giữ làm bối cảnh có cảnh báo; không trích làm căn cứ pháp lý (MT-24) |
| https://suckhoetreem.vn/…131048.html | Nguồn duy nhất cho QĐ 1931/2026 | Giữ tạm; pha 2 tìm bản gốc |
| https://xdcs.cdnchinhphu.vn/…/3276-….pdf | F ghi "chưa kiểm tra"; linkcheck OK; G xác nhận là bản gốc QĐ 3276 có text | **Nâng lên link gốc** cho QD-3276-2025-BYT |
| https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf | F ghi "chưa kiểm tra"; G xác nhận VBHN Luật KCB có text | **Nâng lên link chính** cho L-KCB-2023 |
| https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat60.pdf | F ghi "chưa kiểm tra"; linkcheck OK | Dùng làm link gốc cho L-DULIEU-2024 |
| Các link luatvietnam, caselaw, báo có verdict OK | OK nhưng là **thứ cấp** | Đã ghi rõ "thứ cấp" trong bảng §1; pha 2 ưu tiên thay bằng bản gốc cho các văn bản lõi |
