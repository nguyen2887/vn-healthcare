# MA-LT — Mã hóa lâm sàng, danh mục kỹ thuật, kiến trúc và chuẩn liên thông

> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: cụm K6 của inventory (mục 5). Gồm: ICD-10 theo TT 06/2026 (cấu trúc 29 cột, quy tắc cột 24–29, mã kép, mã bổ sung, chuyển tiếp) và tài liệu kỹ thuật QĐ 1849/2026; lộ trình ICD-11; Danh mục kỹ thuật TT 23/2024 với Phụ lục 01/02 và mốc 01/01/2028 (TT 25/2026 Đ3); danh mục mã dùng chung chỉ số cận lâm sàng (LOINC) và thuật ngữ lâm sàng (SNOMED CT); Khung kiến trúc số BYT (QĐ 2146/2026), Khung kiến trúc dữ liệu (QĐ 2113/2026); HL7 v2/CDA, FHIR, DICOM: văn bản nào nhắc, mức ràng buộc, cho ai; TCVN tin học y tế; phần mã hóa của schema `HoSoBenhAn` (CV 365).
>
> Không lặp lại: chuẩn XML BHYT, mã DVKT/khám/giường BHYT (QĐ 2010), mã khoa, mã đối tượng → cụm **BHYT-DATA** (đặc biệt R17, R20). Kết xuất `HoSoBenhAn` ở góc EMR → **EMR-R18, EMR-R19**. LIS/RIS-PACS chi tiết, thời hạn lưu ảnh → cụm K7. ATTT cấp độ → **ANM**.
>
> **Quy ước mức xác minh**: `gốc` = đọc toàn văn có lớp text từ nguồn nhà nước (datafiles, vanban, cổng .gov.vn, PDF ký số); `gốc-OCR` = OCR tesseract `eng`, mất dấu; `thứ cấp-toàn văn` = toàn văn đăng trên CSDL luật tư nhân (luatvietnam), có đủ căn cứ, điều khoản, người ký, nhưng không phải bản của cơ quan ban hành; `thứ cấp` = báo, tóm tắt; `gốc-meta` = mới xác minh số, ngày, trích yếu qua văn bản nhà nước khác; `chưa XM`. Chỗ ghi **(suy luận)** là ý kiến người nghiên cứu. Tài liệu định hướng kỹ thuật, **không phải ý kiến pháp lý**.

---

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| TT-06-2026-BYT | 06/2026/TT-BYT, 02/04/2026, ký: TT Trần Văn Thuấn | Quy định về mã hóa bệnh tật, nguyên nhân tử vong theo ICD-10 (thân 5 trang + Phụ lục 1.271 trang) | 01/07/2026; Đ5 k2, k3 từ 01/06/2026 | Còn HL; sửa TT 01/2025 (phiếu hẹn, phiếu chuyển: ký số thay đóng dấu; Q87.11 → Q87.1) | BV công, BV tư, PK (mọi cơ sở KCB; xem R01 về cơ sở không KCB BHYT); vendor HIS | gốc (thân + phụ lục, đã phân tích máy toàn bộ 15.844 dòng) | [PDF thân](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf) · [PDF Phụ lục](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt-kem.pdf) · [VB 217536](https://vanban.chinhphu.vn/?pageid=27160&docid=217536) |
| QD-1849-2026-BYT | 1849/QĐ-BYT, 23/06/2026, ký: TTTT Vũ Mạnh Hà | Ban hành tài liệu hướng dẫn kỹ thuật mã hóa bệnh tật, nguyên nhân tử vong theo ICD-10 (PL1 giới thiệu chương/khối; PL2 nguyên tắc mã hóa; PL3 thuốc, hóa chất hỗ trợ mã hóa chương XIX, XX; PL4 mã của QĐ 4469 bị hủy; PL5 mã mới bổ sung) | Từ ngày ký | Còn HL; **chấm dứt "Hướng dẫn mã hoá bệnh tật theo ICD-10" của QĐ 4469/2020** (Đ2) | Cơ sở KCB, NVYT, BHXH | thứ cấp-toàn văn (phần Quyết định); **phụ lục chưa đọc** | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-1849-qd-byt-2026-huong-dan-ky-thuat-ma-hoa-benh-tat-va-nguyen-nhan-tu-vong-theo-icd-10-438487-d1.html) |
| QD-4469-2020-BYT | 4469/QĐ-BYT, 28/10/2020 | Bảng phân loại ICD-10 và Hướng dẫn mã hóa ICD-10 | — | **Hết tác dụng thực tế**: danh mục bị TT 06 thay từ 01/07/2026 (TT 06 Đ6 k1); phần hướng dẫn hết HL từ 23/06/2026 (QĐ 1849 Đ2) | — | gốc-meta (qua QĐ 1849, BHYT-DATA) | — |
| TT-23-2024-BYT | 23/2024/TT-BYT, 18/10/2024, ký: TT Trần Văn Thuấn | Ban hành Danh mục kỹ thuật trong KCB (PL 01: 19.438 kỹ thuật, có mã; PL 02: 9.128 kỹ thuật xếp theo hệ cơ quan, chỉ có "mã liên kết") | 18/10/2024 (Đ3 k1) | Còn HL; sửa bởi TT 25/2026 Đ3; thay TT 43/2013, TT 21/2017 | Mọi cơ sở KCB | gốc (PDF do BV ĐK Bạc Liêu đăng, thân + cấu trúc 2 phụ lục) | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20241031/457_Thong_tu-23-2024-TT-BYT_fb58669347.pdf) |
| TT-25-2026-BYT | 25/2026/TT-BYT, 30/06/2026 | Sửa TT 01/2013, TT 32/2023, **TT 23/2024**, TT 42/2025 | 15/08/2026; **Đ2, Đ3 từ 01/07/2026** (Đ6 k2) | Còn HL | Mọi cơ sở KCB | gốc (PDF ký số VPCP) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/25-byt.signed.pdf) · [VB 218704](https://vanban.chinhphu.vn/?pageid=27160&docid=218704) |
| QD-1227-2025-BYT | 1227/QĐ-BYT, 11/04/2025, ký: TT Nguyễn Tri Thức | Danh mục mã dùng chung đối với kỹ thuật, thuật ngữ chỉ số cận lâm sàng (Đợt 1): 2.964 chỉ số (huyết học-truyền máu 1.022; hóa sinh 447; vi sinh 174; GPB 81; điện quang 1.240), có cột **tham chiếu LOINC** và mã KT TT 23 | Từ ngày ký | Còn HL | BV công, BV tư, PK (Đ2: toàn bộ cơ sở KCB công lập và tư nhân) | thứ cấp-toàn văn (Quyết định) + gốc (PL01 huyết học, bản Sở Y tế Gia Lai sao gửi) + thứ cấp (số lượng chỉ số) | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-1227-qd-byt-2025-danh-muc-ma-dung-chung-doi-voi-ky-thuat-thuat-ngu-chi-so-can-lam-sang-397987-d1.html) · [PL01 PDF](https://benhviennhi.gialai.gov.vn/Upload/FileUpload/6388058958597263931571.Phu%20luc%2001_Huyet%20hoc-Truyen%20mau_Dot%201.signed.signed.pdf) · [SYT Quảng Ninh, thứ cấp](https://soytequangninh.gov.vn/menu-second/tin-tuc-su-kien/tin-hoat-dong-nganh/ban-hanh-danh-muc-chi-so-can-lam-sang-ap-dung-trong-benh-an-.html) |
| QD-2427-2025-BYT | 2427/QĐ-BYT, 25/07/2025 | Danh mục mã dùng chung thuật ngữ y học lâm sàng – Đợt 1 (thuật ngữ giải phẫu) | Từ ngày ký | Còn HL | Toàn bộ cơ sở KCB công, tư (Đ2) | thứ cấp-toàn văn (Quyết định); PL chưa đọc | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-2427-qd-byt-cua-bo-y-te-ve-viec-ban-hanh-danh-muc-ma-dung-chung-thuat-ngu-y-hoc-lam-sang-dot-1-406662-d1.html) |
| QD-2493-2025-BYT (**mới**) | 2493/QĐ-BYT, 04/08/2025 | Thuật ngữ y học lâm sàng – Đợt 2 (bất thường hình thái, 5.155 thuật ngữ, mã 7 số `62xxxxx` + **mã tham chiếu SNOMED CT**) | Từ ngày ký | Còn HL | Toàn bộ cơ sở KCB công, tư (Đ2) | gốc (PDF ký số + file xlsx do UBND Điện Biên đăng) | [QĐ PDF](https://qppl.dienbien.gov.vn/qlvb/vbpq.nsf/3d0f058120469ad34725726600365420/F07AA555C171647547258CE3002E2102/$file/02.%20Quyet%20dinh_DM%20thuat%20ngu%20LS%20-%20Dot%202.signed.pdf) · [PL01 PDF](https://qppl.dienbien.gov.vn/qlvb/vbpq.nsf/3d0f058120469ad34725726600365420/F07AA555C171647547258CE3002E2102/$file/03.%20Danh%20muc%20thuat%20ngu%20LS%20Dot%202%20-%20Bat%20thuong%20hinh%20thai.pdf) |
| QD-2805-2025-BYT (**mới**) | 2805/QĐ-BYT, 04/09/2025 | Thuật ngữ y học lâm sàng – Đợt 3 (dị ứng – allergy; phát hiện – finding) | Từ ngày ký | Còn HL | Toàn bộ cơ sở KCB công, tư (Đ2) | thứ cấp-toàn văn (Quyết định); PL chưa đọc | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-2805-qd-byt-cua-bo-y-te-ve-viec-ban-hanh-danh-muc-ma-dung-chung-thuat-ngu-y-hoc-lam-sang-dot-3-410581-d1.html) |
| QD-2146-2026-BYT | 2146/QĐ-BYT, 15/07/2026, ký: TT Nguyễn Tri Thức | Ban hành Khung kiến trúc số Bộ Y tế | Từ ngày ký (Đ3) | Còn HL; **không có điều khoản thay thế/bãi bỏ** QĐ 1928/2023 hay QĐ 4152/2024 | **Đơn vị thuộc, trực thuộc BYT**; khuyến khích Sở Y tế; bộ ngành, địa phương, tổ chức khác "tham chiếu" (Phần I.2) | thứ cấp-toàn văn (đủ căn cứ, 4 điều, phụ lục ~4.600 dòng) + gốc-meta (thư Sở Y tế Nghệ An dẫn số, ngày) | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-2146-qd-byt-2026-ban-hanh-khung-kien-truc-so-bo-y-te-440771-d1.html) · [SYT Nghệ An 4849/SYT-VP](https://datafiles.nghean.gov.vn/nan-ubnd/2882/quantritintuc20268/thu_moi_bao_gia_ttdl_y_te2026020260819074621545_Signed.pdf) |
| QD-2113-2026-BYT | 2113/QĐ-BYT, 10/07/2026 | Khung kiến trúc dữ liệu, Khung quản trị, quản lý dữ liệu và Từ điển dữ liệu dùng chung của Bộ Y tế (phiên bản 1.0) | chưa XM | Còn HL (theo các văn bản dẫn chiếu) | chưa XM (suy luận: như QĐ 2146) | gốc-meta (thư 4849/SYT-VP Nghệ An ghi "QĐ số 2113/QĐ-BYT ngày 10/07/2026 của Bộ trưởng Bộ Y tế"); **nội dung chưa đọc được** | [SYT Nghệ An](https://datafiles.nghean.gov.vn/nan-ubnd/2882/quantritintuc20268/thu_moi_bao_gia_ttdl_y_te2026020260819074621545_Signed.pdf) · [vietbao, thứ cấp](https://vietbao.vn/bo-y-te-chuan-hoa-du-lieu-tao-nen-tang-du-lieu-quoc-gia-ve-y-te-607792.html) |
| TT-54-2017-BYT | 54/2017/TT-BYT, 29/12/2017 | Bộ tiêu chí ứng dụng CNTT tại cơ sở KCB (8 nhóm, 146 tiêu chí; định nghĩa HL7, HL7 CDA, CCD, DICOM) | 27/02/2018 (Đ6) | Còn HL một phần: tiêu chí EMR hết HL theo TT 13/2025 Đ4 k3 (xem EMR). Căn cứ ban hành **chỉ là NĐ 75/2017** (không dẫn Luật CNTT). Có dự thảo thay (DT-TT54) | Cơ sở KCB đã có GPHĐ (Đ1 k2) | thứ cấp-toàn văn | [luatvietnam](https://luatvietnam.vn/y-te/thong-tu-54-2017-tt-byt-bo-y-te-158564-d1.html) |
| QD-7713-2016-BYT | 7713/QĐ-BYT, 30/12/2016 | **Công bố tài liệu** tiêu chuẩn quốc tế giao thức bản tin HL7 (bản tiếng Việt) | chưa XM | Chưa thấy văn bản bãi bỏ (chưa XM) | (công bố tài liệu, không phải nghĩa vụ) | gốc-meta (QĐ 5969/QĐ-BYT 2021 nêu số, ngày, trích yếu) | [QĐ 5969 PDF, medinet](https://file.medinet.gov.vn/data/soytehcm/trungtamytehocmon/attachments/2022_2/5969-qd-bytkehoachudcnttgiai_doan_20212025_82202214.pdf) |
| QD-3926-2017-BYT | 3926/QĐ-BYT, 28/08/2017 | **Công bố tài liệu** tiêu chuẩn kiến trúc tài liệu lâm sàng HL7 CDA phiên bản tiếng Việt "áp dụng vào phần mềm ứng dụng trong lĩnh vực y tế" | chưa XM | Chưa thấy văn bản bãi bỏ (chưa XM) | như trên | gốc-meta (như trên) | như trên |
| CV-365-2025-TTYQG | 365/TTYQG-GPQLCL, 06/06/2025 | Hướng dẫn yêu cầu kỹ thuật phần mềm HSBA điện tử + Phụ lục `HoSoBenhAn` | từ khi ban hành | Còn áp dụng (hướng dẫn kỹ thuật) | Cơ sở KCB, vendor EMR | gốc (đã đọc lại phần mã hóa của phụ lục) | [PDF, UBND Sơn Tịnh](https://sontinh.quangngai.gov.vn/upload/2006782/20260423/H%C6%AF%E1%BB%9ANG%20D%E1%BA%AAN%20K%E1%BB%B8%20THU%E1%BA%ACT%20TRI%E1%BB%82N%20KHAI.pdf) |
| ND-102-2025 | 102/2025/NĐ-CP, 13/05/2025 | Quản lý dữ liệu y tế (phần liên quan: Đ18 k2 giao BYT ban hành QCVN về CSDL QG về y tế, CSDL chuyên ngành) | 01/07/2025 | Còn HL | BYT (nghĩa vụ ban hành) | gốc-OCR (PDF scan datafiles) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/102-ndcp.signed.pdf) |
| TT-39-2017-BTTTT | 39/2017/TT-BTTTT, 15/12/2017 | Danh mục tiêu chuẩn kỹ thuật về ứng dụng CNTT trong CQNN (CV 365 III.1.3 c dẫn chiếu) | 01/07/2018 | mst.gov.vn ghi "còn hiệu lực"; quan hệ với Luật CĐS chưa XM | CQNN; EMR theo CV 365 | gốc (PDF trên mic.mediacdn.vn, lớp text lỗi font) — **không có HL7/DICOM**, chỉ XML, JSON, XML Signature/Encryption… | [PDF](https://mic.mediacdn.vn/Upload/VanBan/tt39-2017.pdf) |
| TCVN-12344-2019 | TCVN 12344:2019 (IDT ISO/TS 18530:2014) | Tin học y tế – Gán, làm nhãn phân định và thu nhận dữ liệu tự động – Phân định nhân viên y tế và bệnh nhân (vòng tay, thẻ; GS1) | — | "A – Còn hiệu lực" | Tự nguyện | gốc (cơ sở dữ liệu TCVN của Viện TCCL VN) | [vsqi](https://tieuchuan.vsqi.gov.vn/tieuchuan/view?sohieu=TCVN+12344%3A2019) |
| QD-1928-2023-BYT | 1928/QĐ-BYT, 21/04/2023 (+ QĐ 4152/QĐ-BYT 31/12/2024 sửa đổi) | Kiến trúc CPĐT Bộ Y tế phiên bản 2.1 | — | Bị QĐ 2146 thay **trên thực tế** (QĐ 2146 Phần VI, VIII gọi là "Kiến trúc hiện tại"), không có điều khoản bãi bỏ | Đơn vị thuộc BYT | gốc (PDF ký số, lớp text lỗi font); **không nhắc HL7/FHIR/DICOM** | [PDF, nhic.vn](https://nhic.vn/wp-content/uploads/2023/11/2023.04.21-QD-1928-Kien-truc-CPDT-Bo-Y-te-phien-ban-2.1.signed.pdf) |

Văn bản nhắc tới để truy vết (chưa đọc riêng): QĐ 3725/QĐ-BYT 16/08/2017 (hướng dẫn ứng dụng CNTT trong quản lý xét nghiệm, thuộc cụm K7); QĐ 6085/QĐ-BYT 30/12/2019 (KT CPĐT BYT 2.0); QĐ 3090/QĐ-BKHCN 08/10/2025 (Khung kiến trúc tổng thể quốc gia số) và QĐ 292/QĐ-BKHCN 25/03/2025 (KT CPS VN 4.0) là căn cứ của QĐ 2146; QĐ 2439/QĐ-TTg 04/11/2025 (Khung KT dữ liệu QG); TT 50/2014/TT-BYT (phân loại phẫu thuật, thủ thuật, vẫn dùng qua mã PL 01 TT 23); TCVN 13996:2024 (mã số mã vạch, UDI thiết bị y tế, QĐ 2146 nhắc); TCVN 14423 (an ninh mạng, xem ANM).

Nguồn không chính thức đã mở để phân xử (không dùng làm căn cứ): [VN Core FHIR IG v0.10.0](https://fhir.hl7.org.vn/) (Omi HealthTech, tự ghi "not an officially approved national … standard"); [ytesovietnam.vn](https://ytesovietnam.vn/quyet-dinh-2146-2113-khung-kien-truc-so-kien-truc-du-lieu-y-te); [icd.kcb.vn](https://icd.kcb.vn/) (ứng dụng "Hệ thống quản lý mã hóa lâm sàng" của Cục QLKCB, có menu ICD-10 TT 06, ICD-10 song ngữ, YHCT, ICF, LOINC Table, UCOD, DRG; đây là công cụ tra cứu, không phải văn bản).

Kiểm link: 27/27 URL trong file trả 200 (`linkcheck-MA-LT.json`). Lưu ý: nhic.vn (chứng chỉ hết hạn) và tieuchuan.vsqi.gov.vn (thiếu chuỗi chứng chỉ) chỉ mở được khi bỏ kiểm tra TLS; luatvietnam chặn bot, phải gửi header trình duyệt.

---

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### A. ICD-10 (TT 06/2026, QĐ 1849/2026)

### MA-LT-R01 — Nạp đúng, đủ Danh mục ICD-10 của TT 06 vào phần mềm
- **Căn cứ**: TT 06 Đ3 (ban hành Danh mục mã bệnh theo ICD-10 tại Phụ lục); Đ7 k5 b: cơ sở KCB "Cập nhật danh mục mã bệnh theo ICD-10 … vào phần mềm quản lý bệnh viện để thực hiện ghi chép, mã hóa bệnh"; Đ7 k3 a: BHXH cập nhật danh mục lên Cổng giám định. BHXH (bài 08/06/2026) nhắc cơ sở phối hợp vendor HIS cập nhật.
- **Nội dung Phụ lục (gốc, phân tích máy)**: 15.844 dòng, 29 cột: 1 STT; 2 STT chương; 3 phạm vi mã chương; 4–5 tên chương Anh/Việt; 6–8 mã khối, tên khối Anh/Việt; 9–11 tiểu khối cấp 1; 12–14 tiểu khối cấp 2; 15–17 nhóm 3 ký tự; **18 mã bệnh** (có dấu chấm, có hậu tố † hoặc *); **19 mã bệnh không dấu** (bỏ dấu chấm, bỏ †/*); 20 tên bệnh WHO 2019 (Anh); 21 hướng dẫn mã hóa bổ sung WHO 2019 (Anh); 22 tên bệnh (Việt); 23 hướng dẫn mã hóa bổ sung (Việt); 24–29 cờ quy tắc (ô cờ chứa lại chính mã bệnh, không phải dấu X). Phân bố: 2.090 mã 3 ký tự, 10.222 mã 4 ký tự, **3.531 mã 5 ký tự** (ví dụ B18.00, I70.00, M00.00), 111 mã †, 807 mã *; chương XXII có mã U00–U85 (gồm các mã tạm thời U07–U49 dành cho WHO dùng khẩn cấp).
- **Áp dụng cho**: mọi cơ sở KCB và vendor HIS/EMR/PK · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (cơ sở KCB BHYT). **BẮT BUỘC?** với cơ sở không KCB BHYT: Đ7 k5 ghi "cơ sở khám bệnh, chữa bệnh" không giới hạn, nhưng căn cứ ban hành chỉ là Luật BHYT và NĐ 188 (suy luận: rủi ro thấp, nên áp như bắt buộc; mặt khác CV 365 PL dùng `maicd` cho mọi HSBA).
- **Phần mềm phải**: nạp đủ 29 cột (không chỉ mã + tên); giữ cả dạng có chấm (cột 18) và không chấm (cột 19); lưu tên Anh + Việt + hướng dẫn mã hóa bổ sung; gắn phiên bản "TT 06/2026" và ngày hiệu lực; có thủ tục cập nhật khi BYT sửa danh mục (TT 06 Đ7 k2 c giao Cục QLKCB đề xuất cập nhật mã).
- **Ghi chú / bẫy**:
  - Lỗi dữ liệu nguồn: dòng 15.750 ghi mã `U13/9` (lẽ ra `U13.9`; cột 19 vẫn đúng `U139`). Bộ nạp phải phát hiện và sửa có ghi chú, không nuốt lặng.
  - VN Core FHIR IG (không chính thức) ghi "16.052 codes"; Phụ lục gốc có 15.844 dòng. Đừng dùng con số của bên thứ ba để kiểm đủ.
  - Mã 5 ký tự: trường `maicd` của CV 365 dài 7, `MA_BENH_CHINH` XML ≤ 7 (BHYT-DATA-R20) → vừa với "M00.00"; đừng cắt còn 4 ký tự.

### MA-LT-R02 — Quy tắc cột 24–29: áp dụng đúng nghĩa từng cột (không chỉ cho bệnh chính)
- **Căn cứ**: TT 06 Đ4 k2: cột 24 "mã không được dùng là bệnh chính"; 25 "không được khuyến khích dùng là bệnh chính"; 26 "mã không được sử dụng vì có mã 4 hoặc 5 ký tự cụ thể hơn"; 27 "chỉ sử dụng để mã hóa nguyên nhân tử vong"; 28 "chỉ có hoặc chủ yếu có ở nữ giới"; 29 "… ở nam giới".
- **Số mã trong từng cột (gốc, phân tích máy)**: cột 24: 2.427 mã (807 mã *, khoảng 1.549 mã nguyên nhân ngoài V–Y, B95–B97, Z37, R65, U…); cột 25: 221 mã (B90–B94 di chứng, I15, I69, các mã T…); cột 26: 2.119 mã (1.630 mã 3 ký tự có tiểu mục + mã 4 ký tự có mã 5 ký tự); cột 27: 12 mã (O95, O96*, O97*, P95, P96.4, S18); cột 28: 931 mã; cột 29: 143 mã. Còn 11.564 mã không nằm ở cột 24, 26, 27.
- **Áp dụng cho**: như R01 · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (nguyên tắc mã hóa). Phần mềm tự động chặn/cảnh báo: NÊN (văn bản không buộc phần mềm phải chặn) nhưng là cách duy nhất kiểm soát được ở quy mô.
- **Phần mềm phải**:
  - Cột 26: chặn ở **mọi vị trí** (bệnh chính, kèm theo, nguyên nhân tử vong), vì câu chữ là "không được sử dụng", không giới hạn ở bệnh chính.
  - Cột 27: chỉ cho phép trong trường nguyên nhân tử vong; chặn ở chẩn đoán bệnh chính và bệnh kèm theo.
  - Cột 24: chặn ở bệnh chính, cho phép ở bệnh kèm theo.
  - Cột 25: cảnh báo, yêu cầu xác nhận khi chọn làm bệnh chính.
  - Cột 28, 29: cảnh báo khi lệch giới tính người bệnh ("chủ yếu" nên không chặn cứng).
- **Ghi chú / bẫy**: tinh chỉnh **BHYT-DATA-R20** (bản đó chỉ chặn 24, 26, 27 ở `MA_BENH_CHINH`). Theo câu chữ TT 06, 26 và 27 rộng hơn. Đây là suy luận từ câu chữ; nếu Cổng BHXH có quy tắc khác thì cần đối chiếu (mục 7).

### MA-LT-R03 — Xác định bệnh chính, bệnh kèm theo, biến chứng, di chứng theo định nghĩa của TT 06
- **Căn cứ**: TT 06 Đ4 k3 a: bệnh chính là bệnh mà người bệnh đến KCB "và được chẩn đoán xác định khi kết thúc lượt"; nhiều bệnh thì bệnh nào "phải sử dụng nhiều nguồn lực (chi phí, dịch vụ, nhân lực) nhất"; chưa chẩn đoán xác định thì lấy triệu chứng chính hoặc rối loạn, bất thường. Đ4 k3 b (bệnh kèm theo: có ảnh hưởng chăm sóc, kéo dài nằm viện hoặc dùng thêm nguồn lực), c (biến chứng), d (di chứng). Đ7 k5 c: áp mã "phù hợp với chẩn đoán bệnh, tình trạng của người bệnh".
- **Áp dụng cho**: như R01 · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (định nghĩa); hỗ trợ phần mềm: NÊN.
- **Phần mềm phải**: tách chẩn đoán vào viện/sơ bộ khỏi chẩn đoán ra viện; bệnh chính **chốt khi kết thúc lượt**; khi có nhiều bệnh, hiển thị tổng chi phí/dịch vụ theo từng chẩn đoán (nếu chỉ định có gắn chẩn đoán) để hỗ trợ chọn bệnh "nhiều nguồn lực nhất"; cho phép phân loại bệnh kèm theo/biến chứng/di chứng; ghi vết người đổi bệnh chính và lý do.
- **Ghi chú / bẫy**: tiêu chí "nhiều nguồn lực nhất" khác quy tắc WHO (main condition là bệnh chủ yếu được điều trị). Đừng copy logic DRG/ICD-10-AM nước ngoài.

### MA-LT-R04 — Chuyển tiếp phiên bản ICD theo ngày kết thúc lượt; không ghi đè mã cũ
- **Căn cứ**: TT 06 Đ6 k1 (văn bản cũ khác thì áp TT 06 từ ngày có hiệu lực; mã cũ bị hủy thì cơ sở chọn "tên bệnh phù hợp nhất" trong danh mục mới); k2 (vào trước 01/07/2026, kết thúc lượt trong hoặc sau ngày đó → dùng mã TT 06); k3 (mã đã ghi trong HSBA theo văn bản cũ và đang lưu trữ "vẫn có giá trị pháp lý"). QĐ 1849 PL4 (mã của QĐ 4469 bị hủy) và PL5 (mã mới) là nguồn để lập bảng chuyển đổi.
- **Áp dụng cho**: như R01 · **Hiệu lực**: 01/07/2026 (đã qua; còn tác dụng với dữ liệu lịch sử, báo cáo so sánh).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: chọn bộ mã theo ngày kết thúc lượt; lượt vắt qua 01/07/2026 phải mã lại bằng bộ mới trước khi chốt; HSBA đã đóng giữ nguyên mã cũ kèm phiên bản; báo cáo thống kê nhiều năm dùng bảng chuyển đổi PL4/PL5 thay vì sửa dữ liệu gốc. Chi tiết dữ liệu đầu ra BHYT: xem **BHYT-DATA-R20**.
- **Ghi chú / bẫy**: QĐ 1849 PL4, PL5 **chưa đọc được** (luatvietnam yêu cầu đăng nhập); cần lấy từ BYT hoặc Cổng BHXH trước khi viết migration.

### MA-LT-R05 — Mã kép (†/*) và mã bổ sung theo hướng dẫn WHO trong Phụ lục
- **Căn cứ**: TT 06 Phụ lục cột 18 (hậu tố †, *), cột 21/23 ("hướng dẫn mã hóa bổ sung WHO2019", 200 mã có câu "Use additional code…"), cột 24 (807 mã * không được làm bệnh chính); TT 06 Đ4 k4: kỹ thuật mã hóa "thực hiện theo hướng dẫn chuyên môn kỹ thuật của Bộ Y tế" → QĐ 1849 PL2 (nguyên tắc mã hóa) và PL3 (thuốc, hóa chất hỗ trợ mã hóa chương XIX, XX); QĐ 1849 Đ2 đoạn 1 buộc cơ sở và NVYT "triển khai áp dụng hướng dẫn kỹ thuật".
- **Áp dụng cho**: như R01 · **Hiệu lực**: 23/06/2026 (QĐ 1849), 01/07/2026 (TT 06).
- **Mức**: BẮT BUỘC? (nghĩa vụ áp dụng hướng dẫn có trong QĐ 1849 Đ2, nhưng nội dung PL2 chưa đọc).
- **Phần mềm phải**: khi chọn mã † gợi ý/đòi mã * tương ứng (lấy từ cột 20–23); khi chọn mã * buộc đi kèm mã † làm bệnh chính; hiển thị hướng dẫn mã hóa bổ sung (cột 23) ngay khi chọn mã; với chấn thương/ngộ độc (chương XIX) hỗ trợ thêm mã nguyên nhân ngoài (chương XX); có danh mục thuốc/hóa chất PL3 QĐ 1849 để tra mã ngộ độc.
- **Ghi chú / bẫy**: XML BHYT chỉ có 1 `MA_BENH_CHINH` và `MA_BENH_KT` ≤ 12 mã (BHYT-DATA-R20) → mã * và mã nguyên nhân ngoài đi vào `MA_BENH_KT`. Cặp †/* không có trường liên kết trong XML hay CV 365; nếu cần giữ cặp thì lưu nội bộ (suy luận).

### MA-LT-R06 — Mã hóa nguyên nhân tử vong
- **Căn cứ**: TT 06 Đ1 (phạm vi gồm "nguyên nhân tử vong"), Đ4 k2 d (cột 27); QĐ 1849 (tên tài liệu gồm "nguyên nhân tử vong").
- **Áp dụng cho**: cơ sở KCB có người bệnh tử vong (BV, PK có cấp cứu) · **Hiệu lực**: 01/07/2026.
- **Mức**: BẮT BUỘC (dùng mã TT 06 cho nguyên nhân tử vong); quy trình chọn nguyên nhân gốc: BẮT BUỘC? (quy tắc chi tiết nằm ở PL2 QĐ 1849, chưa đọc).
- **Phần mềm phải**: có trường nguyên nhân tử vong tách khỏi chẩn đoán bệnh (chuỗi nguyên nhân trực tiếp → trung gian → gốc nếu mẫu giấy báo tử yêu cầu); cho phép mã cột 27 chỉ ở trường này; lưu mã nguyên nhân ngoài V–Y cho tử vong do chấn thương.
- **Ghi chú / bẫy**: icd.kcb.vn có công cụ "UCOD Việt Nam" (chọn nguyên nhân tử vong gốc). Đây là công cụ, không phải nghĩa vụ. Mẫu giấy báo tử, liên thông khai tử thuộc cụm K4.

### MA-LT-R07 — Sửa mã Q87.11 → Q87.1 trong danh mục của TT 01/2025
- **Căn cứ**: TT 06 Đ5 k3: sửa mã Q87.11 (Hội chứng Prader Willi) tại "Phụ lục 3" TT 01/2025/TT-BYT thành Q87.1, hiệu lực 01/06/2026.
- **Áp dụng cho**: cơ sở KCB BHYT, vendor · **Hiệu lực**: 01/06/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: mọi bảng tham chiếu dựng từ Phụ lục 3 TT 01/2025 (danh mục bệnh dùng cho quy định của TT 01; tên phụ lục chưa đối chiếu) phải dùng Q87.1; dữ liệu trước 01/06/2026 giữ nguyên.
- **Ghi chú / bẫy**: Q87.11 không tồn tại trong Phụ lục TT 06 (đã kiểm: chỉ có Q87, Q87.0–Q87.5, Q87.8). Đây là ví dụ mã "nội bộ VN" bị gỡ.

### MA-LT-R08 — Ký số của cơ sở trên phiếu hẹn khám lại và phiếu chuyển cơ sở KCB bản điện tử
- **Căn cứ**: TT 06 Đ5 k2: "(Đóng dấu treo của cơ sở KCB)" ở Mẫu phiếu hẹn (Phụ lục V TT 01/2025) và "(Ký tên, đóng dấu)" ở Mẫu phiếu chuyển (Phụ lục VI) "được thay thế bằng ký số xác thực của cơ sở khám bệnh, chữa bệnh đối với bản điện tử", từ 01/06/2026.
- **Áp dụng cho**: cơ sở KCB BHYT · **Hiệu lực**: 01/06/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: phát hành phiếu hẹn và phiếu chuyển điện tử có chữ ký số tổ chức (không chỉ hình dấu). Chi tiết chữ ký số tổ chức: **EMR-R08**.
- **Ghi chú / bẫy**: điều khoản về ký số nằm trong thông tư "mã hóa ICD", dễ bị bỏ sót khi tra theo chủ đề.

### MA-LT-R09 — Kiểm định khi nạp danh mục chuẩn (dữ liệu nguồn có lỗi)
- **Căn cứ**: TT 06 Đ7 k5 b (cập nhật danh mục vào phần mềm); thực tế dữ liệu nguồn (R01: `U13/9`). (Suy luận cho các danh mục khác: QĐ 1227, 2427, 2493, 2805, TT 23 phát hành dạng PDF/xlsx.)
- **Áp dụng cho**: vendor · **Hiệu lực**: thường xuyên.
- **Mức**: NÊN.
- **Phần mềm phải**: nạp bằng script có kiểm: định dạng mã, trùng mã, số dòng so với bản công bố, đối chiếu cột có dấu/không dấu, so diff với phiên bản trước; lưu tệp nguồn (hash) và biên bản nạp.

### MA-LT-R10 — ICD-11: chưa có nghĩa vụ; ICD-10 TT 06 là bộ mã pháp định duy nhất
- **Căn cứ**: Không tìm thấy văn bản nào buộc dùng ICD-11 (tìm trên vanban, BHXH, kcb, nhic, luatvietnam đến 05/10/2026). QĐ 2146 Phần IX.1.2 a (lộ trình ngắn hạn 2025–2026): "Chuẩn hóa dữ liệu y tế đáp ứng các tiêu chuẩn quốc tế ICD-10, ICD-11, SNOMED CT, LOINC, RxNorm. Lộ trình thực hiện tiếp tục đến năm 2030." Đây là nhiệm vụ của BYT, không phải nghĩa vụ của cơ sở KCB.
- **Áp dụng cho**: — · **Hiệu lực**: —.
- **Mức**: NÊN (chuẩn bị kiến trúc đa hệ mã); dữ liệu gửi BHYT, CV 365: BẮT BUỘC dùng ICD-10 TT 06.
- **Phần mềm phải**: không dùng ICD-10-CM, ICD-10-AM hay ICD-11 thay cho ICD-10 TT 06 ở trường chẩn đoán chính thức; nếu muốn dùng ICD-11 thì để ở trường phụ qua bảng ánh xạ (Pattern P2).

### MA-LT-R11 — Hỗ trợ nhân viên chuyên trách mã hóa lâm sàng
- **Căn cứ**: TT 06 Đ7 k5 d: "Khuyến khích từng bước bố trí nhân viên chuyên trách về mã hoá lâm sàng để hướng dẫn, kiểm tra, giám sát…"; BHXH nhắc lại (bài 08/06/2026).
- **Áp dụng cho**: cơ sở KCB · **Hiệu lực**: 01/07/2026.
- **Mức**: NÊN.
- **Phần mềm phải**: vai trò "mã hóa lâm sàng" có hàng đợi rà soát hồ sơ trước khi chốt/gửi; sửa mã có vết; báo cáo tỷ lệ lỗi mã theo khoa, bác sĩ.

### B. Danh mục kỹ thuật (TT 23/2024 sửa bởi TT 25/2026)

### MA-LT-R12 — Đến hết 31/12/2027 dùng Phụ lục 01 TT 23 làm danh mục và mã kỹ thuật
- **Căn cứ**: TT 23 Đ1 k1 a (sửa bởi TT 25 Đ3 k1): PL 01 "được thực hiện đến hết ngày 31 tháng 12 năm 2027". TT 23 Đ4 k4 (bổ sung bởi TT 25 Đ3 k2): STT kỹ thuật theo chương của TT 43/2013 và TT 21/2017 tại cột 2 PL 01 "được tiếp tục sử dụng làm mã kỹ thuật" (trừ mã "BS_…"); kỹ thuật đã phân loại PTTT theo TT 50/2014 tiếp tục áp mức phân loại đó qua mã ở cột 2 (ví dụ 2.10 chọc tháo dịch màng phổi; 5.92 xóa xăm laser Ruby).
- **Cấu trúc PL 01 (gốc)**: cột 1 STT (19.438 dòng), cột 2 **mã kỹ thuật** dạng `chương.STT` (ví dụ `1.1`) hoặc `BS_chương.STT` cho kỹ thuật bổ sung (khoảng 1.232 mã BS_), cột 3 tên chương (28 chương theo chuyên khoa, ví dụ "01. Hồi sức cấp cứu và chống độc", "28. Phẫu thuật tạo hình thẩm mỹ"), cột 4 tên kỹ thuật.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: 18/10/2024 → 31/12/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: danh mục DVKT nội bộ gắn mã kỹ thuật PL 01 (kể cả mã BS_), giữ mức phân loại PTTT (TT 50/2014); ánh xạ sang mã DVKT BHYT `CC.KKKK.GGGG` (QĐ 2010, xem **BHYT-DATA-R17**).
- **Ghi chú / bẫy**: TT 23 bản gốc ghi PL 01 "đến ngày 30/6/2026" và PL 02 "từ ngày 01/7/2026". TT 25 (hiệu lực Đ3 từ 01/07/2026) đã **lùi** sang 31/12/2027 / 01/01/2028 và bãi bỏ hai cụm từ ngày trên tiêu đề phụ lục (TT 25 Đ3 k4, k5). Tài liệu viết trước 07/2026 sẽ ghi sai mốc.

### MA-LT-R13 — Chuẩn bị chuyển sang Phụ lục 02 từ 01/01/2028
- **Căn cứ**: TT 23 Đ1 k1 b (sửa bởi TT 25 Đ3 k1): PL 02 "được thực hiện từ ngày 01 tháng 01 năm 2028"; TT 23 Đ1 k4: kỹ thuật PL 02 "được sắp xếp theo hệ cơ quan và cấu trúc giải phẫu"; TT 23 Đ5 (sửa bởi TT 25 Đ3 k3): Cục QLKCB, Sở Y tế đôn đốc, **cơ sở KCB "Chuẩn bị các điều kiện để thực hiện danh mục kỹ thuật quy định tại Phụ lục số 02 … từ ngày 01 tháng 01 năm 2028"** (k4 b).
- **Cấu trúc PL 02 (gốc)**: cột 1 STT (9.128 dòng), cột 2 STT của chương, cột 3 tên chương (30 chương theo hệ cơ quan: 1. Thần kinh, 2. Tuần hoàn, 3. Hô hấp, 4. Tiêu hóa, …, 18. YHCT, 20. Tâm thần, 24. Hóa sinh, 28. Vi sinh, 30. Dinh dưỡng lâm sàng…), **cột 4 "Mã liên kết"** (trỏ về mã PL 01), cột 5 tên kỹ thuật. **Không có cột "mã kỹ thuật" riêng.** Quan hệ PL 02 ↔ PL 01 là N–N: một mã PL 01 xuất hiện ở nhiều dòng PL 02 (ví dụ STT 16 và 17 cùng liên kết 10.39); một dòng có thể liên kết nhiều mã (ví dụ STT 35 "2.129;"); nhiều dòng để trống mã liên kết (kỹ thuật mới, ví dụ STT 36 "Chọc dịch não tủy qua thóp").
- **Áp dụng cho**: mọi cơ sở KCB; vendor HIS · **Hiệu lực**: chuẩn bị từ nay; áp dụng 01/01/2028.
- **Mức**: BẮT BUỘC (cơ sở phải chuẩn bị); thiết kế phần mềm: NÊN.
- **Phần mềm phải**: lưu PL 02 như một hệ mã riêng có hiệu lực từ 01/01/2028; khóa đề xuất `(chương, STT chương)` hoặc STT toàn bảng **cho tới khi BYT công bố mã chính thức** (suy luận); bảng crosswalk PL 01 ↔ PL 02 lưu N–N, có trạng thái "trống liên kết"; báo cáo danh sách kỹ thuật cơ sở đang làm mà PL 02 không còn hoặc tách/gộp; chạy song song hai mã trong giai đoạn chuyển.
- **Ghi chú / bẫy**:
  - **Chưa có văn bản** quy định mã DVKT BHYT (QĐ 2010 `CC.KKKK.GGGG`, gốc từ chương/STT TT 43) sẽ đổi thế nào khi PL 02 có hiệu lực, cũng chưa có giá DVKT theo PL 02 (mục 7).
  - TT 23 Đ4 k3 (sửa): cơ sở đã có GPHĐ tiếp tục làm kỹ thuật đã duyệt "đến ngày 31 tháng 12 năm 2027 mà không phải thực hiện thủ tục điều chỉnh giấy phép hoạt động" → suy luận: từ 2028 có thể phải rà lại phạm vi chuyên môn theo PL 02.

### MA-LT-R14 — Chỉ cho chỉ định kỹ thuật trong phạm vi chuyên môn đã được phê duyệt
- **Căn cứ**: TT 23 Đ5 k4 a (sửa bởi TT 25): cơ sở "Bảo đảm cơ sở vật chất, nhân lực, trang thiết bị thực hiện danh mục kỹ thuật đã được cấp có thẩm quyền phê duyệt"; Đ4 k3 (sửa) về kỹ thuật đã được phê duyệt trong phạm vi hoạt động chuyên môn. TT 32/2023 PL XII (sửa bởi TT 25 Đ2 k1): kỹ thuật "*" của điều dưỡng chỉ được làm khi người chịu trách nhiệm chuyên môn kỹ thuật cho phép bằng văn bản, tối đa đến 31/12/2029.
- **Áp dụng cho**: mọi cơ sở KCB · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC? (nghĩa vụ của cơ sở; ràng buộc trong phần mềm là cách thực thi, suy luận).
- **Phần mềm phải**: danh mục DVKT của cơ sở có cờ "đã phê duyệt" + số quyết định + ngày; chặn/cảnh báo chỉ định ngoài danh mục; với điều dưỡng, kiểm tra kỹ thuật "*" theo văn bản cho phép cá nhân còn hạn.

### MA-LT-R15 — Liên kết ba lớp mã: DVKT nội bộ ↔ mã TT 23 ↔ mã BHYT/mã chỉ số CLS
- **Căn cứ**: TT 23 + TT 25 (R12, R13); QĐ 2010/2025 Đ1, Đ3 (BHYT-DATA-R17); QĐ 1227 PL (cột "Mã KT TT23" + "Tên kỹ thuật trong PL 01 TT 23"); CV 365 PL mục V `machidinh`, mục VII `machiso`.
- **Áp dụng cho**: cơ sở KCB, vendor · **Hiệu lực**: đang áp dụng.
- **Mức**: BẮT BUỘC (cơ sở KCB BHYT, qua XML); NÊN với phần còn lại.
- **Phần mềm phải**: một dịch vụ nội bộ có thể ánh xạ tới: mã kỹ thuật PL 01 (và sau 2028 là PL 02), mã DVKT BHYT, và (với xét nghiệm, CĐHA) một hoặc nhiều mã chỉ số QĐ 1227. Mỗi ánh xạ có ngày hiệu lực và văn bản nguồn (Pattern P2).

### C. Danh mục mã dùng chung lâm sàng (LOINC, SNOMED CT)

### MA-LT-R16 — Mã chỉ số cận lâm sàng theo QĐ 1227/2025 (có tham chiếu LOINC)
- **Căn cứ**: QĐ 1227 Đ1 (danh mục để "thống nhất thuật ngữ chuyên môn, chuẩn hoá dữ liệu, ứng dụng CNTT trong bệnh án điện tử, liên thông kết quả cận lâm sàng, dữ liệu KCB, BHYT"); Đ2 (áp dụng thống nhất toàn quốc, toàn bộ cơ sở KCB công lập và tư nhân). PL01 (gốc): cột STT, **mã dùng chung 7 số** (`1000001`…), tên kỹ thuật/chỉ số, mã KT TT23, tên kỹ thuật trong PL 01 TT 23, **mã LOINC tham chiếu**, tên LOINC và 6 trục LOINC (thành phần, thuộc tính, thời gian, hệ mẫu, thang đo, phương pháp), đơn vị tính. QĐ 2010/2025 Đ3: XML4 BHYT dùng tên, mã chỉ số ở cột mã dùng chung QĐ 1227 (BHYT-DATA-R17).
- **Áp dụng cho**: BV công, BV tư, PK có xét nghiệm/CĐHA; vendor HIS/LIS/RIS · **Hiệu lực**: từ 11/04/2025.
- **Mức**: BẮT BUỘC (dữ liệu XML4 BHYT); BẮT BUỘC? cho HSBA và liên thông kết quả CLS (Đ2 nói "áp dụng thống nhất" nhưng không có chế tài; CV 365 `machiso` không nêu hệ mã).
- **Phần mềm phải**: danh mục chỉ số LIS/RIS ánh xạ 1–1 tới mã dùng chung 7 số; lưu thêm LOINC làm mã phụ; đơn vị theo cột đơn vị của danh mục (hoặc có bảng quy đổi); điền `machiso` (CV 365) bằng mã dùng chung QĐ 1227 (suy luận).
- **Ghi chú / bẫy**: QĐ 1227 là "Đợt 1"; các đợt sau (nếu có) **chưa tìm thấy**. Chỉ số chưa có mã thì XML4 tạm dùng PL11 QĐ 7603 (QĐ 2010 Đ3). LOINC chỉ là "tham chiếu"; mã pháp định là mã 7 số.

### MA-LT-R17 — Thuật ngữ y học lâm sàng (QĐ 2427, 2493, 2805) và trường VNCODE/SNOMED của CV 365
- **Căn cứ**:
  - QĐ 2427/2025 Đ1 (thuật ngữ giải phẫu, "chuẩn hóa về ngôn ngữ, mã hóa và phân cấp theo phân loại quốc tế"; nhằm ghi nhận thống nhất trong bệnh án điện tử, liên thông KCB–BHYT–Sổ SKĐT), Đ2 (toàn bộ cơ sở KCB công, tư).
  - QĐ 2493/2025 Đ1–Đ3 (bất thường hình thái; Cục QLKCB tổng hợp góp ý, cập nhật danh mục). PL01 (gốc): **mã dùng chung 7 số** (`6200001`…`6205155`, 5.155 thuật ngữ), tên Việt, **mã tham chiếu SNOMED CT**, tên Anh (FSN SNOMED), phân nhóm.
  - QĐ 2805/2025 Đ1–Đ3 (dị ứng, phát hiện).
  - CV 365 PL mục III (khám bệnh các cơ quan, mục 25.x): mỗi dấu hiệu/triệu chứng có `dauchung_ma` gồm **`VNCODE`** (chuỗi 25, "Thuật ngữ lâm sàng (Việt Nam)") và **`SNOMED`** (chuỗi 25, "Thuật ngữ lâm sàng (Quốc tế)").
- **Áp dụng cho**: BV công, BV tư, PK; vendor EMR · **Hiệu lực**: từ 25/07/2025, 04/08/2025, 04/09/2025.
- **Mức**: BẮT BUỘC? (QĐ ghi "áp dụng thống nhất", không có chế tài; CV 365 PL III.1.1 h buộc dùng "danh mục dùng chung theo quy định của Bộ Y tế").
- **Phần mềm phải**: có kho thuật ngữ lâm sàng nạp đủ các đợt; trường triệu chứng/khám cơ quan cho phép chọn thuật ngữ có mã (VNCODE = mã dùng chung 7 số, suy luận) và tự điền SNOMED CT tham chiếu; vẫn giữ văn bản tự do (`dauchung`, `dauchung_ghichu`).
- **Ghi chú / bẫy**: CV 365 ban hành 06/06/2025, trước QĐ 2493, 2805; ví dụ trong phụ lục CV 365 (`VNCODE` "12587", `SNOMED` "9987888") **không khớp** dạng mã 7 số `62xxxxx` của QĐ 2493 → coi ví dụ là minh họa. Quan hệ chính thức VNCODE ↔ "mã dùng chung" chưa có văn bản xác nhận (mục 7).

### MA-LT-R18 — Bản quyền/giấy phép thuật ngữ quốc tế (SNOMED CT, LOINC)
- **Căn cứ**: Không có văn bản VN nào nói về giấy phép. Các QĐ 1227, 2493 đưa mã LOINC, SNOMED CT vào phụ lục; QĐ 2146 nêu SNOMED CT, LOINC, RxNorm, UMLS.
- **Áp dụng cho**: vendor · **Hiệu lực**: —.
- **Mức**: NÊN (rủi ro pháp lý hợp đồng/sở hữu trí tuệ, không phải luật y tế).
- **Phần mềm phải**: sổ đăng ký hệ mã ngoài (nguồn, phiên bản, điều kiện giấy phép); không phân phối tệp SNOMED CT/LOINC đầy đủ khi chưa rõ giấy phép; chỉ dùng tập con BYT đã công bố cho đến khi xác nhận.
- **Ghi chú / bẫy**: tư cách thành viên SNOMED International của VN và điều kiện dùng mã SNOMED trong sản phẩm thương mại: **chưa xác minh** (cần luật sư, mục 7).

### D. Kiến trúc và chuẩn liên thông

### MA-LT-R19 — Điền mã chuẩn đúng trong gói `HoSoBenhAn` (CV 365)
- **Căn cứ**: CV 365 PL III.1.1 d (kết xuất XML/JSON theo Phụ lục), III.1.1 h (dùng danh mục dùng chung BYT), mục IV.1 (kết xuất khi có yêu cầu). Trường mã hóa trong phụ lục (gốc): `khambenh_chandoanvaovienmaicd`, `maicd` (chuỗi 7), `tenicd` (255), `maicd_khac` (100), `tenicd_khac`; `VNCODE`, `SNOMED` (25); `machidinh`, `machiso` (255); `mathuocvattu_byt` (255) bên cạnh `mathuocvattu_bv`. Ví dụ trong phụ lục dùng mã ICD **có dấu chấm** ("R10.4").
- **Áp dụng cho**: cơ sở KCB có HSBA điện tử; vendor EMR · **Hiệu lực**: từ 06/06/2025.
- **Mức**: BẮT BUỘC? (xem EMR-R18 về giá trị pháp lý của CV 365).
- **Phần mềm phải**: `maicd` lấy cột 18 TT 06 (có chấm, bỏ †/*; suy luận từ ví dụ); `maicd_khac` nhiều mã phân cách theo quy ước thống nhất với XML (";"); `machiso` = mã QĐ 1227; `VNCODE`/`SNOMED` theo R17; `mathuocvattu_byt` = mã BYT/BHYT, không để mã nội bộ.
- **Ghi chú / bẫy**: schema không có trường hệ mã (`system`) hay phiên bản → bên nhận phải tự hiểu; nên kèm metadata phiên bản ở lớp vận chuyển (suy luận). Phần còn lại của schema: **EMR-R18**.

### MA-LT-R20 — HL7 FHIR: không có nghĩa vụ pháp lý cho cơ sở KCB; QĐ 2146 chỉ đặt lộ trình cho BYT
- **Căn cứ (đã đọc toàn văn QĐ 2146)**:
  - Phần I.2 phạm vi: áp dụng cho "các đơn vị thuộc, trực thuộc Bộ Y tế. Khuyến khích Sở Y tế … áp dụng"; bộ ngành, địa phương khác "tham chiếu".
  - Phần IX.1.2 a (lộ trình ngắn hạn 2025–2026): "Xây dựng cơ chế liên thông dữ liệu đáp ứng tiêu chuẩn quốc tế HL7 FHIR R4, DICOM V3.0 (ISO 12052:2026). Lộ trình thực hiện tiếp tục đến năm 2030."
  - Phần IX.1.1 mục III.11: nhiệm vụ "Xây dựng hệ thống liên thông dữ liệu theo chuẩn quốc tế", đầu mối **TTYQG**, 2026–2030.
  - Phần VII.2.6 b và c (lớp hỗ trợ): "Tuân thủ, áp dụng các tiêu chuẩn quốc tế, tiêu chuẩn mở … (VD: HL7 FHIR, OMOP CDM, SNOMED, LOINC, RxNorm, OpenHIE, ISO/IEC 27701, TCVN 13239:2024, TCVN 14423:2025,...)" — liệt kê dạng ví dụ.
  - Phần VII.2.4 b (lớp dữ liệu): tuân thủ tiêu chuẩn về "cấu trúc và định dạng trao đổi (XML/JSON), từ điển dữ liệu".
  - Phần IX.2.6: đơn vị thuộc, trực thuộc BYT triển khai CNTT "bảo đảm tuân thủ Khung kiến trúc số Bộ Y tế".
  - QĐ 1928/2023 (KT CPĐT 2.1, bản trước) **không** nhắc HL7/FHIR/DICOM.
- **Áp dụng cho**: BV trực thuộc BYT (BẮT BUỘC? tuân thủ khung, nhưng FHIR là lộ trình đến 2030); BV công địa phương, BV tư, PK: không có nghĩa vụ.
- **Mức**: NÊN (mọi đối tượng); BẮT BUỘC? cho đơn vị trực thuộc BYT ở mức "tuân thủ khung", không có hạn chót FHIR cụ thể.
- **Phần mềm phải**: kiến trúc cho phép thêm façade FHIR R4 (4.0.1) mà không đổi mô hình lõi: ID ổn định, mã có `system` + `version`, tách tài nguyên Patient/Encounter/Condition/Observation/ServiceRequest/MedicationRequest; không cam kết "tuân thủ FHIR theo quy định" khi chào bán.
- **Ghi chú / bẫy**: luatvietnam tóm tắt và một lần đọc máy của trang này ghi QĐ 2146 "không nhắc FHIR" → **sai**; ytesovietnam và VN Core FHIR IG nói QĐ 2146 "mandating FHIR R4 and DICOM" → **nói quá** (IG tự thừa nhận đây là "guidance/roadmap at ministry level"). "ISO 12052:2026" là câu chữ trong QĐ 2146; ấn bản ISO 12052 năm 2026 chưa xác minh.

### MA-LT-R21 — DICOM và HL7 v2 cho RIS-PACS, LIS (TT 54/2017)
- **Căn cứ (TT 54, thứ cấp-toàn văn)**:
  - Đ2 k8 (HL7: giao thức quản lý, trao đổi, tích hợp thông tin y tế điện tử), k9 (HL7 CDA dựa trên XML), k10 (CCD), k11 (DICOM).
  - PL I nhóm IV (RIS-PACS), mức **cơ bản**: TC 67 giao diện 2 chiều với thiết bị CĐHA (CT, MRI, X-quang, DSA, siêu âm); TC 68 interface với HIS: "RIS chuyển thông tin chỉ định vào máy chẩn đoán hình ảnh theo tiêu chuẩn HL7"; PACS chuyển hình DICOM sang JPEG cho RIS/HIS; liên thông 2 chiều báo cáo CĐHA; **TC 70 "Hỗ trợ tiêu chuẩn HL7 bản tin, DICOM"**; TC 74 kết xuất DICOM ra CD/DVD kèm phần mềm xem hoặc đường dẫn web. Mức **nâng cao**: TC 76 biên tập xử lý ảnh DICOM; TC 77 nén JPEG2000; TC 78 xem DICOM qua WebView; TC 79 hội chẩn đa điểm.
  - Nhóm V (LIS): TC 84 kết nối máy xét nghiệm 2 chiều (cơ bản), TC 88 liên thông HIS (nâng cao) — **không nêu chuẩn** (HL7/ASTM).
  - Nhóm VI (phi chức năng), mức nâng cao: TC 107 kết nối Cổng giám định BHYT; TC 108 liên thông HIS, LIS, PACS, EMR; **TC 109 "Áp dụng các tiêu chuẩn trong nước hoặc tiêu chuẩn quốc tế (tiêu chuẩn HL7, HL7 CDA, DICOM, ICD-10,...)"**.
  - Đ4 k3: phải đạt tất cả tiêu chí ở một mức; thiếu 1 tiêu chí thì xếp mức thấp hơn. Đ5: người đứng đầu ra quyết định xác định mức, báo cáo cấp trên và Cục CNTT (nay là đơn vị kế nhiệm).
- **Áp dụng cho**: cơ sở KCB có GPHĐ khi tự đánh giá mức CNTT; vendor RIS-PACS · **Hiệu lực**: 27/02/2018, phần không thuộc EMR còn HL.
- **Mức**: BẮT BUỘC? (TT 54 là VBQPPL còn hiệu lực một phần nhưng là **bộ tiêu chí để xếp mức**, không phải điều kiện hoạt động; muốn công bố RIS-PACS đạt mức cơ bản thì phải có HL7 + DICOM). NÊN với người mua chưa cần xếp mức.
- **Phần mềm phải**: RIS: nhận order từ HIS và đẩy worklist xuống máy (HL7 v2 ORM/OMI hoặc DICOM MWL); PACS: lưu DICOM gốc, xuất CD/DVD kèm viewer hoặc link web, có web viewer; báo cáo CĐHA đồng bộ 2 chiều với HIS. Mức nâng cao: JPEG2000, xem web, hội chẩn.
- **Ghi chú / bẫy**: TT 54 **không nêu phiên bản** HL7 (v2.x) hay DICOM. Tiêu chí EMR trong TT 54 (gồm TC 144 "kết xuất bệnh án điện tử theo tiêu chuẩn HL7 CDA, CCD") đã hết HL theo TT 13/2025 → không còn căn cứ đòi CDA. Thời hạn lưu ảnh, liên thông kết quả CLS từ 01/01/2027: cụm K7.

### MA-LT-R22 — Tài liệu HL7 v2 và HL7 CDA tiếng Việt (QĐ 7713/2016, 3926/2017): tham khảo, không bắt buộc
- **Căn cứ**: QĐ 5969/QĐ-BYT 31/12/2021 (gốc) mô tả: QĐ 7713/QĐ-BYT 30/12/2016 "công bố tài liệu tiêu chuẩn quốc tế giao thức bản tin HL7"; QĐ 3926/QĐ-BYT 28/08/2017 "công bố tài liệu tiêu chuẩn kiến trúc tài liệu lâm sàng HL7 CDA phiên bản tiếng Việt áp dụng vào phần mềm ứng dụng trong lĩnh vực y tế". QĐ 5969 còn giao nâng cấp LGSP BYT "trao đổi dữ liệu theo tiêu chuẩn HL7" (2022–2023).
- **Áp dụng cho**: — · **Hiệu lực**: chưa XM.
- **Mức**: NÊN.
- **Phần mềm phải**: nếu làm giao diện HL7 v2 thì có thể dùng tài liệu tiếng Việt làm thuật ngữ; không coi là chuẩn bắt buộc.
- **Ghi chú / bẫy**: bản gốc hai QĐ chưa đọc (ehealth.gov.vn của Cục CNTT cũ không còn phân giải DNS), phiên bản HL7 v2.x chưa XM.

### MA-LT-R23 — Hệ thống của đơn vị thuộc BYT: tuân thủ Khung kiến trúc số và Khung kiến trúc dữ liệu
- **Căn cứ**: QĐ 2146 Đ2 (TTYQG đầu mối hướng dẫn), Phần I.2, Phần III.1 (nguyên tắc: tuân thủ QĐ 3090/QĐ-BKHCN, QĐ 292/QĐ-BKHCN, QĐ 2439/QĐ-TTg, QĐ 1132/QĐ-TTg; "Tuân thủ các tiêu chuẩn, quy chuẩn kỹ thuật bắt buộc áp dụng"), Phần VII.2.3 b ("Các ứng dụng, nền tảng nghiệp vụ dùng chung bắt buộc tuân thủ bộ tiêu chuẩn giao diện …, API chuẩn hóa"), VII.2.4 b ("dữ liệu nhập một lần – dùng nhiều nơi"; áp dụng chung từ điển dữ liệu, tiêu chuẩn mã hóa, chuẩn hóa danh mục), VIII.2 (100% hệ thống kết nối qua trục LGSP), IX.2.6. QĐ 2113 (nội dung chưa đọc). CV 365 PL III.1.3 b: phần mềm HSBA điện tử "Tuân thủ Khung Kiến trúc Chính phủ điện tử Việt Nam, Kiến trúc Chính phủ điện tử cấp bộ hoặc Kiến trúc Chính quyền điện tử cấp tỉnh hiện hành".
- **Áp dụng cho**: BV/đơn vị trực thuộc BYT (BẮT BUỘC?); BV công địa phương theo kiến trúc CQĐT tỉnh; BV tư, PK: tham chiếu.
- **Mức**: BẮT BUỘC? (QĐ hành chính nội bộ ngành, không phải VBQPPL).
- **Phần mềm phải**: với khách hàng trực thuộc BYT: tài liệu ánh xạ sản phẩm vào lớp kiến trúc của QĐ 2146 (người dùng – kênh – ứng dụng – dữ liệu – hạ tầng/ANM – hỗ trợ); API mở, XML/JSON; tích hợp qua LGSP BYT khi được yêu cầu; danh mục theo từ điển dữ liệu khi QĐ 2113/DT-DMDL hoàn thiện.

### MA-LT-R24 — Danh mục dữ liệu dùng chung, từ điển dữ liệu và QCVN cấu trúc thông điệp đang xây dựng
- **Căn cứ**: NĐ 102/2025 Đ18 k2 (gốc-OCR): BYT "Xây dựng, ban hành quy chuẩn kỹ thuật quốc gia về Cơ sở dữ liệu quốc gia về y tế, các cơ sở dữ liệu chuyên ngành y tế"; QĐ 2146 IX.1.1: I.1 "Xây dựng, ban hành tiêu chuẩn, quy chuẩn kỹ thuật cấu trúc thông điệp dữ liệu trao đổi dữ liệu của CSDL Quốc gia về Y tế và các CSDL chuyên ngành y tế" (Cục KHCN&ĐT, 2026); III.3 Từ điển dữ liệu ngành (2026–2027); III.4 danh mục dữ liệu dùng chung (2026–2030). TTYQG (nhic.vn 26/08/2026): bốn nhóm tiêu chuẩn đang nghiên cứu (cơ quan tổ chức y tế; nhân lực; dược, TBYT; thông tin sức khỏe cá nhân).
- **Áp dụng cho**: tương lai, mọi hệ thống trao đổi với CSDL QG về y tế · **Hiệu lực**: chưa ban hành (đến 05/10/2026 chưa tìm thấy QCVN).
- **Mức**: NÊN (theo dõi).
- **Phần mềm phải**: thiết kế lớp xuất/nhập theo "hợp đồng dữ liệu" có phiên bản, để khi QCVN ra chỉ thêm một adapter (Pattern P6).

### MA-LT-R25 — TCVN tin học y tế (tự nguyện)
- **Căn cứ**: TCVN 12344:2019 (IDT ISO/TS 18530:2014), còn hiệu lực: tiêu chí phân định và làm nhãn người bệnh (SoC) và nhân viên y tế trên vòng tay, thẻ…, dùng AIDC kết hợp GS1. Luật Tiêu chuẩn và QCKT (sửa 2025): TCVN là tự nguyện trừ khi được viện dẫn bắt buộc (nguyên tắc chung, chưa đọc lại điều khoản).
- **Áp dụng cho**: BV có định danh người bệnh bằng mã vạch/RFID · **Mức**: NÊN.
- **Phần mềm phải**: nếu in vòng tay/nhãn mẫu: mã định danh người bệnh duy nhất, mã vạch 2D theo GS1, dữ liệu tối thiểu theo tiêu chuẩn.
- **Ghi chú / bẫy**: chưa rà hết danh mục TCVN nhóm ICS 35.240.80; TCVN 13239:2024 mà QĐ 2146 nêu chưa xác định được tên.

### MA-LT-R26 — Tự xác định mức ứng dụng CNTT theo TT 54 (phần còn hiệu lực) và bằng chứng chuẩn
- **Căn cứ**: TT 54 Đ3 (8 nhóm tiêu chí, PL I), Đ4 (nguyên tắc), Đ5 k1–k3 (người đứng đầu ra quyết định xác định mức, gửi cấp trên; chịu trách nhiệm; xác định lại nếu cấp trên phát hiện sai). Tóm tắt luatvietnam: báo cáo định kỳ tháng 12 hằng năm (chưa đọc điều khoản cụ thể).
- **Áp dụng cho**: cơ sở KCB có GPHĐ · **Hiệu lực**: đang áp dụng, chờ DT-TT54.
- **Mức**: BẮT BUỘC? (nghĩa vụ xác định mức có trong Đ5; giá trị thực tế sau khi tiêu chí EMR bị bỏ và TT 13 thay chưa rõ).
- **Phần mềm phải**: vendor cung cấp ma trận đáp ứng từng tiêu chí (HIS, LIS, RIS-PACS, phi chức năng), kèm bằng chứng HL7/DICOM/ICD-10 cho TC 70, 109.

**Tổng hợp mức** (26 yêu cầu, tính theo mức cao nhất ghi ở mục): BẮT BUỘC: 11 (R01, R02, R03, R04, R06, R07, R08, R12, R13, R15, R16); BẮT BUỘC?: 8 (R05, R14, R17, R19, R20 — phần đơn vị trực thuộc BYT, R21, R23, R26); NÊN: 7 (R09, R10, R11, R18, R22, R24, R25). Nhiều mục có mức kép theo đối tượng (ví dụ R01 bắt buộc với cơ sở BHYT, bắt buộc? với cơ sở không BHYT; R20 chỉ là NÊN với BV tư, PK) — đã ghi trong từng mục.

---

## 3. Pattern thiết kế

### P1. Dịch vụ thuật ngữ đa hệ mã có hiệu lực theo ngày (Terminology Service) — R01, R04, R10, R12, R13, R16, R17
- **Mô tả**: mọi bộ mã (ICD-10 TT 06, TT 23 PL01, TT 23 PL02, QĐ 1227, QĐ 2427/2493/2805, mã BHYT, LOINC, SNOMED CT, ICD-11 nếu dùng) là "code system" có phiên bản; mỗi khái niệm có khoảng hiệu lực; tra cứu luôn kèm ngày.
- **Mô hình dữ liệu gợi ý**:
  - `code_system(id, uri, name, publisher, legal_doc, license_note)` — ví dụ `vn-icd10-tt06`, `vn-dmkt-tt23-pl01`, `vn-dmkt-tt23-pl02`, `vn-cls-qd1227`, `vn-ttls-qd2493`, `loinc`, `snomedct`.
  - `code_system_version(id, system_id, version, legal_doc_no, valid_from, valid_to, source_file_hash, loaded_at)`; ràng buộc: các version cùng system không chồng lấn ngày (exclusion constraint trên `daterange(valid_from, valid_to)`).
  - `concept(id, version_id, code, code_alt, display_vi, display_en, parent_code, attrs jsonb, status)`; unique `(version_id, code)`; ICD-10: `code_alt` = cột 19, `attrs` = cột 20–29 (gồm cờ `c24…c29`, `dagger`, `asterisk`, `additional_coding_vi`).
  - API `resolve(system, code, as_of)`, `search(system, text, as_of)`, `validate(system, code, as_of, context)`.
- **Đánh đổi**: tốn công nạp và kiểm định; đổi lại không bao giờ phải sửa mã cũ trong hồ sơ khi văn bản thay.

### P2. Lớp ánh xạ mã nội bộ ↔ mã chuẩn có hiệu lực theo ngày (Concept Map) — R12, R13, R15, R16, R17, R19
- **Mô tả**: dịch vụ nội bộ (giá, máy, khoa) không bị buộc chết vào một mã chuẩn; ánh xạ là dữ liệu có ngày và có nguồn.
- **Mô hình**: `concept_map(id, source_system, source_code, target_system, target_version_id, target_code, equivalence ENUM('equal','wider','narrower','related','unmatched'), valid_from, valid_to, basis_doc, created_by)`; chỉ mục `(source_system, source_code, valid_from)`; cho phép N–N (cần cho TT 23 PL01↔PL02 và mã liên kết nhiều giá trị).
- **Luồng**: khi chốt hồ sơ, `map(source, target_system, as_of = ngày y lệnh/kết thúc lượt)`; nếu ra nhiều kết quả hoặc `unmatched` thì đưa vào hàng đợi người mã hóa (R11).
- **Đánh đổi**: cần quy tắc chọn `as_of` cho từng hệ mã (ICD theo ngày kết thúc lượt — TT 06 Đ6 k2; DVKT theo ngày y lệnh — suy luận; xem BHYT-DATA mục 7.4).

### P3. Bộ kiểm tra chẩn đoán theo luật TT 06 (rule engine) — R02, R03, R05, R06
- **Mô tả**: luật khai báo dạng dữ liệu, sinh từ cờ cột 24–29 + cờ †/*: `{rule: 'c26', scope: 'ANY', action: 'BLOCK'}`, `{rule: 'c27', scope: 'NOT_DEATH_CAUSE', action: 'BLOCK'}`, `{rule: 'c24', scope: 'PRIMARY', action: 'BLOCK'}`, `{rule: 'c25', scope: 'PRIMARY', action: 'CONFIRM'}`, `{rule: 'c28', when: 'sex=M', action: 'WARN'}`, `{rule: 'asterisk', require: 'paired_dagger_primary'}`.
- **Vị trí chạy**: lúc bác sĩ chọn mã (UI), lúc chốt lượt, lúc sinh XML/CV 365 (chặn cuối).
- **Đánh đổi**: chặn cứng có thể tắc ca thật (ví dụ mã cột 28 cho người chuyển giới) → cột 28/29 chỉ cảnh báo, có ghi lý do vượt.

### P4. Ảnh chụp mã hóa theo lượt KCB (encounter coding snapshot) — R03, R04, R19
- **Mô tả**: khi kết thúc lượt, đóng băng `encounter_diagnosis(encounter_id, role ENUM('primary','secondary','complication','sequela','death_cause','admission'), system, version_id, code, display, coder_id, coded_at, reason_change)`; sửa sau chốt là thêm bản ghi mới có lý do, không update.
- **Đánh đổi**: tăng dung lượng; đổi lại đáp ứng TT 06 Đ6 k3 (mã cũ giữ giá trị) và ghi vết (EMR-R10, R12).

### P5. Chuyển đổi danh mục kỹ thuật PL 01 → PL 02 (dual-coding) — R12, R13, R14
- **Mô tả**: nạp PL 02 với `valid_from = 2028-01-01`; crosswalk N–N từ cột "mã liên kết"; báo cáo "sẵn sàng 2028": (a) dịch vụ cơ sở đang dùng có mã PL01 nhưng không có dòng PL02 trỏ tới; (b) một mã PL01 tách thành nhiều kỹ thuật PL02 (cần chọn); (c) kỹ thuật PL02 trống liên kết (mới). Trong giai đoạn chuyển, mỗi dịch vụ lưu cả mã PL01 và khóa PL02.
- **Đánh đổi**: khóa PL02 tạm (chương + STT chương) có thể phải đổi khi BYT/BHXH ban hành mã chính thức → giữ khóa tạm trong bảng map, không nhúng vào dữ liệu giao dịch.

### P6. Cổng tích hợp với adapter theo chuẩn (integration engine) — R16, R19, R20, R21, R23, R24
- **Mô tả**: mô hình lõi trung lập; adapter xuất/nhập: (1) XML BHYT (BHYT-DATA); (2) JSON/XML `HoSoBenhAn` CV 365; (3) HL7 v2 (ORM/OMI–ORU) cho LIS/RIS; (4) DICOM (MWL, C-STORE/C-FIND, DICOMweb WADO-RS/STOW-RS/QIDO-RS) cho PACS; (5) façade FHIR R4 cho đối tác/BYT khi có yêu cầu; (6) adapter QCVN cấu trúc thông điệp khi ban hành.
- **Dữ liệu**: `interface_message(id, channel, standard, standard_version, direction, payload_ref, hash, status, ack, created_at)`; mọi mã gửi đi kèm `system` + `version` nội bộ để truy nguyên dù chuẩn đích không có trường hệ mã.
- **Đánh đổi**: thêm một tầng; đổi lại không phải viết lại lõi khi BYT chọn chuẩn (FHIR hay QCVN riêng).

### P7. Đường ống nạp danh mục chuẩn có kiểm định — R01, R09, R16, R17, R24
- **Mô tả**: tải tệp gốc (PDF/xlsx) → trích bảng → kiểm (số dòng, mẫu mã, trùng, đối chiếu cột có dấu/không dấu, so diff với version trước) → biên bản (lỗi nguồn như `U13/9`, cách xử lý) → duyệt → kích hoạt theo `valid_from`.
- **Đánh đổi**: PDF 1.271 trang khó trích; nên xin bản xlsx/CSV từ Cổng BHXH hoặc icd.kcb.vn khi có, nhưng vẫn đối chiếu với bản gốc pháp lý.

### P8. Sổ đăng ký giấy phép hệ mã ngoài — R18
- **Mô tả**: `code_system.license_note`, cờ `redistributable`; chặn xuất toàn bộ SNOMED CT/LOINC ra khỏi hệ thống khi chưa có giấy phép; chỉ xuất mã đã dùng trong hồ sơ.

---

## 4. Checklist audit

| ID kiểm tra | Yêu cầu (ID R) | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| MA-LT-A01 | R01 | `SELECT count(*)` danh mục ICD đang hiệu lực; so 15.844 dòng (hoặc số mã lá); kiểm có cột không dấu, tên Anh, hướng dẫn bổ sung, 6 cờ 24–29 | Kết quả truy vấn, ảnh màn hình danh mục, tệp nguồn đã nạp | Bắt buộc |
| MA-LT-A02 | R01, R09 | Tìm mã `U13.9`, `U139`, `U13/9`; tìm mã 5 ký tự (M00.00, I70.00) và mã U07.1 | Kết quả tìm | Nên |
| MA-LT-A03 | R02 | Thử chọn: B95.0 (cột 24) làm bệnh chính; A00 (cột 26) ở bệnh kèm theo; O96.0 (cột 27) làm bệnh kèm theo; B90.0 (cột 25) làm bệnh chính; C53.0 (cột 28) cho người bệnh nam | Ảnh màn hình chặn/cảnh báo; log | Bắt buộc (dùng đúng mã) / Nên (chặn tự động) |
| MA-LT-A04 | R03, R04 | Mở lượt nội trú vào 30/06/2026 ra 02/07/2026: kiểm bộ mã dùng khi chốt; mở HSBA đóng trước 01/07/2026: mã cũ còn nguyên, có ghi phiên bản | Ảnh màn hình, bản ghi DB `encounter_diagnosis` | Bắt buộc |
| MA-LT-A05 | R04 | Hỏi vendor bảng chuyển đổi mã QĐ 4469 → TT 06 (PL4, PL5 QĐ 1849): nguồn, ngày nạp, số dòng | Tài liệu, tệp map | Bắt buộc |
| MA-LT-A06 | R05 | Chọn A17.0† và G01*: hệ thống có gợi ý cặp, có hiển thị "hướng dẫn mã hóa bổ sung"; chọn mã * làm bệnh chính bị chặn | Ảnh màn hình | Bắt buộc? |
| MA-LT-A07 | R06 | Tạo ca tử vong: có trường nguyên nhân tử vong riêng; cho phép mã cột 27 chỉ ở trường này | Ảnh màn hình, mẫu giấy báo tử xuất ra | Bắt buộc |
| MA-LT-A08 | R07 | Tìm Q87.11 trong mọi danh mục (bệnh dài ngày, chuyển tuyến…) | Kết quả tìm = 0 sau 01/06/2026 | Bắt buộc |
| MA-LT-A09 | R08 | Xuất phiếu hẹn khám lại và phiếu chuyển cơ sở bản điện tử; kiểm chữ ký số tổ chức (chứng thư, thời điểm ký) | PDF đã ký, kết quả kiểm chữ ký | Bắt buộc |
| MA-LT-A10 | R11 | Có vai trò mã hóa lâm sàng, hàng đợi rà soát, báo cáo lỗi mã | Ảnh màn hình phân quyền, báo cáo | Nên |
| MA-LT-A11 | R12 | Danh mục DVKT: mỗi dịch vụ có mã PL01 TT 23 (kể cả BS_), mức PTTT TT 50; truy vấn dịch vụ thiếu mã | Kết quả truy vấn | Bắt buộc |
| MA-LT-A12 | R13 | Hỏi kế hoạch PL02: đã nạp PL02 chưa, crosswalk N–N, báo cáo sẵn sàng 2028 | Tài liệu thiết kế, báo cáo thử | Bắt buộc (cơ sở chuẩn bị) / Nên (cách làm) |
| MA-LT-A13 | R14 | Thử chỉ định một DVKT ngoài danh mục phê duyệt; điều dưỡng chỉ định kỹ thuật "*" không có văn bản cho phép | Ảnh màn hình chặn/cảnh báo | Bắt buộc? |
| MA-LT-A14 | R15 | Lấy 20 dịch vụ ngẫu nhiên: đủ map nội bộ → TT 23 → mã BHYT → (CLS) mã QĐ 1227, có ngày hiệu lực | Bảng mẫu | Bắt buộc (BHYT) |
| MA-LT-A15 | R16 | Danh mục chỉ số LIS: tỷ lệ chỉ số có mã 7 số QĐ 1227; LOINC lưu kèm; đơn vị khớp | Truy vấn, tỷ lệ % | Bắt buộc (XML4) / Bắt buộc? |
| MA-LT-A16 | R17 | Màn hình khám cơ quan: có chọn thuật ngữ có mã; xuất CV 365 thấy `VNCODE`, `SNOMED` có giá trị | Tệp JSON/XML xuất | Bắt buộc? |
| MA-LT-A17 | R18 | Hỏi vendor giấy phép SNOMED CT/LOINC; sản phẩm có phân phối tệp đầy đủ không | Văn bản trả lời, hợp đồng | Nên |
| MA-LT-A18 | R19 | Xuất 1 HSBA theo CV 365: `maicd` đúng dạng có chấm, ≤ 7; `machiso` là mã QĐ 1227; `mathuocvattu_byt` không phải mã nội bộ | Tệp xuất + kết quả validate schema tự dựng | Bắt buộc? |
| MA-LT-A19 | R20 | Kiểm tài liệu chào bán: có ghi "bắt buộc FHIR theo QĐ 2146" không (sai căn cứ); nếu có FHIR: phiên bản 4.0.1, CapabilityStatement | Tài liệu, endpoint `/metadata` | Nên |
| MA-LT-A20 | R21 | RIS-PACS: nhận order HL7/MWL từ HIS; lưu DICOM gốc; xuất CD/DVD kèm viewer hoặc link web; xem web | Log HL7, DICOM conformance statement, thử xuất | Bắt buộc? (nếu khai mức TT 54) |
| MA-LT-A21 | R21 | LIS: kết nối 2 chiều máy xét nghiệm, nhận chỉ định HIS, đồng bộ kết quả | Danh sách máy đã kết nối, log | Bắt buộc? (nếu khai mức TT 54) |
| MA-LT-A22 | R23 | (Khách hàng trực thuộc BYT) tài liệu ánh xạ vào Khung kiến trúc số 2146; kết nối LGSP | Tài liệu kiến trúc | Bắt buộc? |
| MA-LT-A23 | R24 | Lớp tích hợp có phiên bản hợp đồng dữ liệu, thêm được adapter mới mà không sửa lõi | Tài liệu kiến trúc, mã nguồn | Nên |
| MA-LT-A24 | R26 | Có quyết định xác định mức CNTT theo TT 54 của cơ sở; ma trận đáp ứng tiêu chí của vendor | Quyết định, báo cáo gửi cấp trên | Bắt buộc? |
| MA-LT-A25 | R09 | Có biên bản nạp danh mục (nguồn, hash, số dòng, lỗi) cho mỗi lần cập nhật ICD/DMKT/QĐ 1227 | Biên bản | Nên |

---

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái (so với 05/10/2026) | Sự kiện | Ai phải làm | Nguồn |
|---|---|---|---|---|
| 30/12/2016; 28/08/2017 | đã qua | Công bố tài liệu HL7, HL7 CDA tiếng Việt | — (tham khảo) | QĐ 7713, 3926 (gốc-meta) |
| 27/02/2018 | đã qua | TT 54 có HL (tiêu chí HL7/DICOM cho RIS-PACS) | Cơ sở KCB tự xác định mức | TT 54 Đ6 |
| 18/10/2024 | đã qua | TT 23 có HL; TT 43/2013, TT 21/2017 hết HL | Cơ sở KCB, vendor | TT 23 Đ3 |
| 11/04/2025 | đã qua | QĐ 1227: mã chỉ số CLS (LOINC tham chiếu) | Mọi cơ sở KCB | QĐ 1227 Đ2, Đ4 |
| 06/06/2025 | đã qua | CV 365 (schema `HoSoBenhAn` có `maicd`, `VNCODE`, `SNOMED`) | Cơ sở có EMR, vendor | CV 365 |
| 25/07, 04/08, 04/09/2025 | đã qua | Thuật ngữ lâm sàng Đợt 1, 2, 3 | Mọi cơ sở KCB | QĐ 2427, 2493, 2805 |
| 01/08/2025 | đã qua | Mã DVKT BHYT dùng chung (gốc TT 23) | Cơ sở KCB BHYT | QĐ 2010 (BHYT-DATA) |
| 01/06/2026 | đã qua | Ký số cơ sở trên phiếu hẹn/phiếu chuyển điện tử; Q87.11 → Q87.1 | Cơ sở KCB BHYT | TT 06 Đ5 k2, k3 |
| 23/06/2026 | đã qua | QĐ 1849 có HL; Hướng dẫn mã hóa QĐ 4469 hết HL | Cơ sở KCB, NVYT | QĐ 1849 Đ2 |
| 01/07/2026 | đã qua | **ICD-10 TT 06** áp dụng (theo ngày kết thúc lượt); TT 25 Đ2, Đ3 có HL (lùi mốc PL 02) | Mọi cơ sở KCB; BHXH cập nhật Cổng | TT 06 Đ5 k1, Đ6 k2; TT 25 Đ6 k2 |
| 10/07/2026 | đã qua | QĐ 2113 Khung KT dữ liệu, từ điển dữ liệu BYT 1.0 | Đơn vị thuộc BYT (suy luận) | gốc-meta |
| 15/07/2026 | đã qua | QĐ 2146 Khung kiến trúc số BYT; lộ trình FHIR R4, DICOM V3.0, ICD-10/11, SNOMED CT, LOINC đến 2030 | Đơn vị thuộc, trực thuộc BYT; TTYQG | QĐ 2146 |
| 15/08/2026 | đã qua | TT 25 có HL chung | — | TT 25 Đ6 k1 |
| 2026 (kế hoạch) | đang chờ | TC/QCVN cấu trúc thông điệp CSDL QG về y tế; CSDL QG về y tế | BYT (Cục KHCN&ĐT, TTYQG) | QĐ 2146 IX.1.1; NĐ 102 Đ18 k2 |
| 2026–2027 | đang chờ | Từ điển dữ liệu ngành y tế | TTYQG | QĐ 2146 IX.1.1 III.3 |
| **31/12/2027** | sắp tới | Hết PL 01 TT 23; hết thời gian giữ kỹ thuật đã duyệt không cần điều chỉnh GPHĐ | Mọi cơ sở KCB | TT 23 Đ1 k1 a, Đ4 k3 (sửa) |
| **01/01/2028** | sắp tới | Áp dụng **PL 02 TT 23** (9.128 kỹ thuật theo hệ cơ quan) | Mọi cơ sở KCB, vendor; BHXH (mã DVKT, chưa có văn bản) | TT 23 Đ1 k1 b, Đ5 (sửa) |
| 31/12/2029 | xa | Hết thời gian cho phép điều dưỡng làm kỹ thuật "*" theo văn bản của người chịu trách nhiệm chuyên môn | Cơ sở KCB | TT 32 PL XII (sửa bởi TT 25 Đ2 k1) |
| 2030 | xa | Hoàn thành lộ trình FHIR R4, DICOM, chuẩn hóa ICD-11, SNOMED CT, LOINC (mục tiêu của BYT) | BYT, TTYQG | QĐ 2146 IX.1.2 |

---

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

**Chuỗi thay thế**

| Cũ | → | Mới | Từ ngày | Ghi chú |
|---|---|---|---|---|
| Danh mục ICD-10 QĐ 4469/QĐ-BYT (28/10/2020) | → | Phụ lục TT 06/2026 | 01/07/2026 | Theo TT 06 Đ6 k1 (áp TT 06 khi khác văn bản cũ); không có câu "bãi bỏ QĐ 4469" trong TT 06 |
| "Hướng dẫn mã hoá bệnh tật theo ICD-10" của QĐ 4469 | → | QĐ 1849/QĐ-BYT | 23/06/2026 | QĐ 1849 Đ2 đoạn 2 |
| Mã Q87.11 (PL 3 TT 01/2025) | → | Q87.1 | 01/06/2026 | TT 06 Đ5 k3 |
| TT 43/2013, TT 21/2017 (danh mục kỹ thuật, phân tuyến) | → | TT 23/2024 PL 01 | 18/10/2024 | STT cũ vẫn là mã kỹ thuật (TT 25 Đ3 k2) |
| TT 23 PL 01 "đến 30/06/2026", PL 02 "từ 01/07/2026" | → | PL 01 đến 31/12/2027; PL 02 từ 01/01/2028 | 01/07/2026 | TT 25 Đ3 k1, k4, k5 |
| KT CPĐT BYT 1.0 (2015) → 2.0 (QĐ 6085/2019) → 2.1 (QĐ 1928/2023) + QĐ 4152/2024 | → | Khung kiến trúc số BYT (QĐ 2146/2026) | 15/07/2026 | **Không có điều khoản bãi bỏ**; QĐ 2146 Phần VI gọi QĐ 1928/4152 là "kiến trúc hiện tại" cần nâng cấp |
| Tiêu chí EMR của TT 54/2017 (gồm TC 144 HL7 CDA/CCD) | → | TT 13/2025 + CV 365 | 06/06/2025 (xem EMR) | Tiêu chí HIS, LIS, RIS-PACS, phi chức năng của TT 54 còn HL |

**Bẫy trích dẫn**

1. **"QĐ 2146 bắt buộc FHIR R4 và DICOM"**: sai về phạm vi. Câu FHIR R4/DICOM nằm ở **lộ trình triển khai của BYT** (IX.1.2 a), văn bản chỉ áp dụng cho đơn vị thuộc, trực thuộc BYT (I.2). Ngược lại, "QĐ 2146 không nhắc FHIR" (tóm tắt luatvietnam, đọc máy) cũng sai. Đây là phân xử **MT-24**.
2. **ytesovietnam.vn và VN Core FHIR IG (fhir.hl7.org.vn)** không phải nguồn chính thức. IG do doanh nghiệp duy trì, tự ghi là bản nháp. Con số "16.052 mã ICD-10 VN" của IG không khớp Phụ lục gốc (15.844 dòng).
3. **TT 23/2024 bản gốc** ghi mốc 30/06/2026 và 01/07/2026, đã bị TT 25 lùi. Mọi tài liệu, báo, slide trước 07/2026 nói "PL 02 áp dụng từ 01/7/2026" là lỗi thời.
4. **TT 25/2026**: hiệu lực chung 15/08/2026 nhưng **Đ2, Đ3 từ 01/07/2026** (Đ6 k2, gốc). Xác nhận MT-09.
5. **TT 06 chứa hai quy định không về ICD** (ký số phiếu hẹn/chuyển; Q87.11). Tra theo chủ đề "ký số" dễ sót.
6. **"Mã không được sử dụng" (cột 26)** không chỉ cấm ở bệnh chính. Tóm tắt nào ghi "cột 24–29 chỉ áp cho bệnh chính" là đọc thiếu.
7. **QĐ 4469 vẫn được XML1 bản 2023 dẫn** (BHYT-DATA bẫy 7); từ 01/07/2026 áp TT 06.
8. **TT 54/2017**: inventory ghi "căn cứ Luật CNTT đã hết HL". Bản toàn văn chỉ có căn cứ NĐ 75/2017 (chức năng BYT). Lập luận "TT 54 hết HL theo Luật CNTT" không đứng.
9. **TT 54 không nêu phiên bản HL7/DICOM**; QĐ 2146 nêu "HL7 FHIR R4" và "DICOM V3.0 (ISO 12052:2026)" — ấn bản ISO 12052:2026 chưa xác minh, đừng chép vào hợp đồng như chuẩn đã kiểm.
10. **Hai nhóm "danh mục mã dùng chung" khác nhau**: (a) bộ mã BHYT (QĐ 7603 → 3276, 2010, 1804…; BHYT-DATA); (b) danh mục lâm sàng của Cục QLKCB (QĐ 1227, 2427, 2493, 2805), mã 7 số, gắn LOINC/SNOMED. Đừng trộn.
11. **"Từ điển dữ liệu" QĐ 2113 (ký 10/07/2026) và DT-DMDL (danh mục dữ liệu chủ, "chưa hoàn thiện" đến 10/2026)** không mâu thuẫn: QĐ 2113 là khung phiên bản 1.0; QĐ 2146 IX.1.1 còn xếp "Từ điển dữ liệu ngành y tế" 2026–2027 và "danh mục dữ liệu dùng chung toàn ngành" 2026–2030 (phân xử **MT-36**, mức suy luận vì chưa đọc QĐ 2113).
12. **Hai số "2113" năm 2026**: QĐ 2113/QĐ-BKHCN (14/04/2026, thủ tục sở hữu trí tuệ) khác QĐ 2113/QĐ-BYT. Luôn ghi cơ quan ban hành.
13. **Người ký**: QĐ 2146 và các QĐ thuật ngữ do Thứ trưởng Nguyễn Tri Thức ký "KT. Bộ trưởng"; QĐ 1849 do TTTT Vũ Mạnh Hà ký; TT 06, TT 23 do TT Trần Văn Thuấn ký.

---

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **QĐ 2113/QĐ-BYT (10/07/2026)**: chưa có toàn văn. Cần: phạm vi áp dụng (đơn vị thuộc BYT hay cả cơ sở KCB), nội dung từ điển dữ liệu (thực thể, trường, kiểu), có nhắc chuẩn trao đổi (FHIR/HL7) không. Nguồn nên thử: TTYQG (nhic.vn), Cổng TTĐT BYT, luatvietnam (cần tài khoản).
2. **QĐ 1849 Phụ lục 2–5**: chưa đọc. Cần cho R04 (bảng mã hủy/mã mới), R05 (quy tắc †/*, mã bổ sung), R06 (quy tắc chọn nguyên nhân tử vong gốc).
3. **Quy tắc Cổng giám định BHXH về cột 24–29**: Cổng chặn cột 26/27 ở `MA_BENH_KT` hay chỉ ở `MA_BENH_CHINH`? Hỏi BHXH VN (Trung tâm Giám định BHYT và TTĐT). Liên quan tinh chỉnh BHYT-DATA-R20.
4. **ICD dạng có chấm hay không chấm trong XML BHYT**: CV 365 ví dụ có chấm; TT 06 có cả hai cột. Đối chiếu XSD Cổng (BHYT-DATA).
5. **TT 06 có ràng buộc cơ sở KCB không ký hợp đồng BHYT không** (căn cứ chỉ Luật BHYT, NĐ 188): cần ý kiến luật sư; thực tế nên áp dụng.
6. **Mã kỹ thuật chính thức của PL 02 TT 23 và mã DVKT BHYT sau 01/01/2028**: chưa có văn bản. Hỏi Cục QLKCB, Vụ BHYT. Cũng chưa rõ giá DVKT theo PL 02.
7. **dmkt.kcb.vn** (chuyển hướng `/nmprp/pl1/`, trả về rỗng): chưa kiểm tra được; có thể là tra cứu danh mục kỹ thuật chính thức.
8. **QĐ 7713/2016, QĐ 3926/2017**: bản gốc, phiên bản HL7 v2.x, tình trạng hiệu lực chưa xác minh (ehealth.gov.vn không phân giải được).
9. **Giấy phép SNOMED CT và LOINC**: VN có là thành viên SNOMED International không; BYT đưa mã SNOMED vào QĐ 2493 với điều kiện sử dụng nào; vendor thương mại dùng có cần Affiliate License không. **Cần luật sư sở hữu trí tuệ** + hỏi Cục QLKCB.
10. **Quan hệ `VNCODE` (CV 365) với mã dùng chung 7 số (QĐ 2427/2493/2805)**: chưa có văn bản nói rõ. Hỏi TTYQG/Cục QLKCB.
11. **QĐ 1227 các đợt sau, QĐ 2427/2805 phụ lục**: chưa đọc nội dung phụ lục 2427, 2805 và PL CĐHA, hóa sinh, vi sinh của 1227.
12. **QCVN cấu trúc thông điệp CSDL QG về y tế** (NĐ 102 Đ18 k2; QĐ 2146 nhiệm vụ I.1, hạn 2026): chưa ban hành đến 05/10/2026. Theo dõi.
13. **DT-TT54** (thay bộ tiêu chí CNTT): chưa thấy ban hành; nếu ban hành có thể đặt chuẩn HL7/DICOM/FHIR cụ thể cho HIS/LIS/PACS.
14. **TT 39/2017/TT-BTTTT** (CV 365 dẫn): mst.gov.vn ghi còn hiệu lực; quan hệ với Luật CĐS và các TT BKHCN 2026 chưa xác minh. Văn bản này không chứa HL7/DICOM.
15. **TCVN 13239:2024** (QĐ 2146 nêu) chưa xác định tên; danh mục TCVN tin học y tế (ICS 35.240.80) chưa rà hết.
16. **Mã bệnh YHCT**: QĐ 2146 phụ lục liệt kê "Danh mục mã bệnh y học cổ truyền"; icd.kcb.vn có mục "YHCT"; XML có `MA_BENH_YHCT`. Văn bản gốc của danh mục YHCT hiện hành chưa xác định (khoảng trống #4 inventory).
17. **TT 54 nghĩa vụ báo cáo tháng 12 hằng năm** (theo tóm tắt luatvietnam) và đơn vị nhận báo cáo sau khi Cục CNTT BYT được tổ chức lại: chưa đối chiếu điều khoản.
