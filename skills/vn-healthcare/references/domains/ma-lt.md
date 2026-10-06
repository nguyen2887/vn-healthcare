# MA-LT — Mã hóa lâm sàng, danh mục kỹ thuật, kiến trúc và chuẩn liên thông

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công, BV tư, phòng khám, đơn vị trực thuộc BYT (phần kiến trúc), vendor HIS/EMR/LIS/RIS-PACS · Research gốc: `research/deep/MA-LT.md`

Phạm vi: ICD-10 theo TT 06/2026 và QĐ 1849/2026; ICD-11; Danh mục kỹ thuật TT 23/2024 (sửa bởi TT 25/2026); mã chỉ số CLS (QĐ 1227, tham chiếu LOINC); thuật ngữ lâm sàng (QĐ 2427/2493/2805, tham chiếu SNOMED CT); Khung kiến trúc số BYT (QĐ 2146/2026), QĐ 2113/2026; HL7 v2/CDA, FHIR, DICOM; TCVN tin học y tế; phần mã hóa của schema `HoSoBenhAn` (CV 365).
Không lặp: chuẩn XML BHYT, mã DVKT/khám/giường BHYT → BHYT-DATA (R17, R20). Kết xuất `HoSoBenhAn` góc EMR → EMR-R18, EMR-R19. Liên thông kết quả CLS, LIS/PACS chi tiết, thời hạn lưu ảnh → CLS. Cấp độ ATTT → ANM. Tài liệu định hướng kỹ thuật, không phải ý kiến pháp lý.

## Tóm tắt nhanh

- **ICD-10 TT 06/2026 áp dụng từ 01/07/2026**, chọn bộ mã theo **ngày kết thúc lượt**; mã cũ trong HSBA đã lưu vẫn có giá trị pháp lý, không được ghi đè (MA-LT-R04).
- Phụ lục TT 06 có **29 cột**, 15.844 dòng, 3.531 mã 5 ký tự. Nạp đủ cột, không chỉ mã + tên (MA-LT-R01).
- **Bẫy lớn nhất**: cột 26 ("không được sử dụng") cấm ở **mọi vị trí**; cột 27 chỉ dùng cho nguyên nhân tử vong. Không chỉ chặn ở bệnh chính (MA-LT-R02).
- TT 06 còn chứa hai quy định không về ICD, áp từ 01/06/2026: ký số tổ chức thay đóng dấu trên phiếu hẹn/phiếu chuyển điện tử; Q87.11 → Q87.1 (MA-LT-R07, R08).
- Danh mục kỹ thuật: **PL 01 TT 23 dùng đến hết 31/12/2027; PL 02 (theo hệ cơ quan) áp dụng từ 01/01/2028** (TT 25/2026 đã lùi mốc cũ 30/06–01/07/2026). PL 02 không có cột mã riêng, chỉ có "mã liên kết" N–N (MA-LT-R12, R13).
- **FHIR/DICOM**: QĐ 2146/2026 nhắc HL7 FHIR R4 và DICOM 3.0 trong lộ trình đến 2030, chỉ áp cho đơn vị thuộc/trực thuộc BYT. Không văn bản nào buộc cơ sở KCB nói chung dùng FHIR hay DICOM. Cả câu "QĐ 2146 bắt buộc FHIR" lẫn "QĐ 2146 không nhắc FHIR" đều sai (MA-LT-R20).
- Mã pháp định cho chỉ số CLS và thuật ngữ lâm sàng là **mã dùng chung 7 số của BYT**; LOINC/SNOMED CT chỉ là cột tham chiếu (MA-LT-R16, R17).

## Mục lục

| ID | Tiêu đề |
|---|---|
| MA-LT-R01 | Nạp đúng, đủ danh mục ICD-10 TT 06 |
| MA-LT-R02 | Quy tắc cột 24–29 theo đúng nghĩa từng cột |
| MA-LT-R03 | Định nghĩa bệnh chính, kèm theo, biến chứng, di chứng |
| MA-LT-R04 | Chuyển tiếp phiên bản ICD theo ngày kết thúc lượt |
| MA-LT-R05 | Mã kép †/* và mã bổ sung |
| MA-LT-R06 | Mã hóa nguyên nhân tử vong |
| MA-LT-R07 | Q87.11 → Q87.1 |
| MA-LT-R08 | Ký số tổ chức trên phiếu hẹn, phiếu chuyển điện tử |
| MA-LT-R09 | Kiểm định khi nạp danh mục chuẩn |
| MA-LT-R10 | ICD-11 chưa có nghĩa vụ |
| MA-LT-R11 | Hỗ trợ nhân viên mã hóa lâm sàng |
| MA-LT-R12 | Dùng PL 01 TT 23 đến 31/12/2027 |
| MA-LT-R13 | Chuẩn bị PL 02 TT 23 từ 01/01/2028 |
| MA-LT-R14 | Chỉ định trong phạm vi chuyên môn được duyệt |
| MA-LT-R15 | Liên kết ba lớp mã DVKT |
| MA-LT-R16 | Mã chỉ số CLS QĐ 1227 (tham chiếu LOINC) |
| MA-LT-R17 | Thuật ngữ lâm sàng QĐ 2427/2493/2805; VNCODE/SNOMED |
| MA-LT-R18 | Giấy phép SNOMED CT, LOINC |
| MA-LT-R19 | Điền mã chuẩn trong `HoSoBenhAn` (CV 365) |
| MA-LT-R20 | HL7 FHIR: không có nghĩa vụ chung |
| MA-LT-R21 | HL7 v2 và DICOM cho RIS-PACS, LIS (TT 54) |
| MA-LT-R22 | Tài liệu HL7 v2/CDA tiếng Việt: tham khảo |
| MA-LT-R23 | Đơn vị thuộc BYT: tuân thủ Khung kiến trúc số |
| MA-LT-R24 | Từ điển dữ liệu, QCVN cấu trúc thông điệp đang xây dựng |
| MA-LT-R25 | TCVN tin học y tế (tự nguyện) |
| MA-LT-R26 | Tự xác định mức CNTT theo TT 54 |
| MA-LT-P01…P08 | Pattern: terminology service, concept map, rule engine, snapshot, dual-coding PL01/PL02, integration engine, pipeline nạp danh mục, sổ giấy phép |
| MA-LT-A01…A25 | Checklist audit |

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 06/2026/TT-BYT (02/04/2026) | Mã hóa bệnh tật, nguyên nhân tử vong theo ICD-10 (thân + PL 1.271 trang) | 01/07/2026; Đ5 k2, k3 từ 01/06/2026 | Còn HL; sửa TT 01/2025 | gốc | [PDF thân](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf) · [PDF PL](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt-kem.pdf) · [VB 217536](https://vanban.chinhphu.vn/?pageid=27160&docid=217536) |
| 1849/QĐ-BYT (23/06/2026) | Tài liệu hướng dẫn kỹ thuật mã hóa ICD-10 (PL1–PL5) | Từ ngày ký | Còn HL; chấm dứt "Hướng dẫn mã hóa" của QĐ 4469/2020 (Đ2) | thứ cấp (phần QĐ); phụ lục chưa đọc | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-1849-qd-byt-2026-huong-dan-ky-thuat-ma-hoa-benh-tat-va-nguyen-nhan-tu-vong-theo-icd-10-438487-d1.html) |
| 4469/QĐ-BYT (28/10/2020) | Bảng phân loại và Hướng dẫn mã hóa ICD-10 cũ | — | Hết tác dụng thực tế: danh mục thay bởi TT 06 từ 01/07/2026; hướng dẫn hết HL 23/06/2026 | gốc-meta | — |
| 23/2024/TT-BYT (18/10/2024) | Danh mục kỹ thuật trong KCB (PL 01: 19.438 dòng có mã; PL 02: 9.128 dòng theo hệ cơ quan) | 18/10/2024 | Còn HL; sửa bởi TT 25/2026 Đ3; thay TT 43/2013, TT 21/2017 | gốc | [PDF](https://bvdkbaclieu.gov.vn/upload/1000079/20241031/457_Thong_tu-23-2024-TT-BYT_fb58669347.pdf) |
| 25/2026/TT-BYT (30/06/2026) | Sửa TT 01/2013, TT 32/2023, TT 23/2024, TT 42/2025 | 15/08/2026; **Đ2, Đ3 từ 01/07/2026** (Đ6 k2) | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/25-byt.signed.pdf) · [VB 218704](https://vanban.chinhphu.vn/?pageid=27160&docid=218704) |
| 1227/QĐ-BYT (11/04/2025) | Mã dùng chung chỉ số CLS Đợt 1 (2.964 chỉ số, cột LOINC tham chiếu) | Từ ngày ký | Còn HL | thứ cấp (QĐ) + gốc (PL01 huyết học) | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-1227-qd-byt-2025-danh-muc-ma-dung-chung-doi-voi-ky-thuat-thuat-ngu-chi-so-can-lam-sang-397987-d1.html) · [PL01 PDF](https://benhviennhi.gialai.gov.vn/Upload/FileUpload/6388058958597263931571.Phu%20luc%2001_Huyet%20hoc-Truyen%20mau_Dot%201.signed.signed.pdf) |
| 2427/QĐ-BYT (25/07/2025) | Thuật ngữ y học lâm sàng Đợt 1 (giải phẫu) | Từ ngày ký | Còn HL | thứ cấp; PL chưa đọc | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-2427-qd-byt-cua-bo-y-te-ve-viec-ban-hanh-danh-muc-ma-dung-chung-thuat-ngu-y-hoc-lam-sang-dot-1-406662-d1.html) |
| 2493/QĐ-BYT (04/08/2025) | Thuật ngữ lâm sàng Đợt 2 (bất thường hình thái, 5.155 mục, mã `62xxxxx` + SNOMED CT tham chiếu) | Từ ngày ký | Còn HL | gốc | [QĐ PDF](https://qppl.dienbien.gov.vn/qlvb/vbpq.nsf/3d0f058120469ad34725726600365420/F07AA555C171647547258CE3002E2102/$file/02.%20Quyet%20dinh_DM%20thuat%20ngu%20LS%20-%20Dot%202.signed.pdf) · [PL01 PDF](https://qppl.dienbien.gov.vn/qlvb/vbpq.nsf/3d0f058120469ad34725726600365420/F07AA555C171647547258CE3002E2102/$file/03.%20Danh%20muc%20thuat%20ngu%20LS%20Dot%202%20-%20Bat%20thuong%20hinh%20thai.pdf) |
| 2805/QĐ-BYT (04/09/2025) | Thuật ngữ lâm sàng Đợt 3 (dị ứng, phát hiện) | Từ ngày ký | Còn HL | thứ cấp; PL chưa đọc | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-2805-qd-byt-cua-bo-y-te-ve-viec-ban-hanh-danh-muc-ma-dung-chung-thuat-ngu-y-hoc-lam-sang-dot-3-410581-d1.html) |
| 2146/QĐ-BYT (15/07/2026) | Khung kiến trúc số Bộ Y tế | Từ ngày ký | Còn HL; không có điều khoản bãi bỏ QĐ 1928/2023, QĐ 4152/2024 | thứ cấp (toàn văn) + gốc-meta | [luatvietnam](https://luatvietnam.vn/y-te/quyet-dinh-2146-qd-byt-2026-ban-hanh-khung-kien-truc-so-bo-y-te-440771-d1.html) · [SYT Nghệ An 4849/SYT-VP](https://datafiles.nghean.gov.vn/nan-ubnd/2882/quantritintuc20268/thu_moi_bao_gia_ttdl_y_te2026020260819074621545_Signed.pdf) |
| 2113/QĐ-BYT (10/07/2026) | Khung kiến trúc dữ liệu, quản trị dữ liệu, Từ điển dữ liệu dùng chung BYT v1.0 | chưa xác minh | Còn HL (theo văn bản dẫn chiếu) | gốc-meta; nội dung chưa đọc | [SYT Nghệ An 4849/SYT-VP](https://datafiles.nghean.gov.vn/nan-ubnd/2882/quantritintuc20268/thu_moi_bao_gia_ttdl_y_te2026020260819074621545_Signed.pdf) |
| 54/2017/TT-BYT (29/12/2017) | Bộ tiêu chí ứng dụng CNTT tại cơ sở KCB (định nghĩa HL7, CDA, CCD, DICOM) | **27/02/2018** (Đ6, đã đối chiếu ảnh bản gốc) | Còn HL một phần: tiêu chí EMR hết HL 06/06/2025 (TT 13/2025 Đ4 k3). Căn cứ ban hành chỉ là NĐ 75/2017 | gốc-OCR + thứ cấp | [PDF bản gốc, vbpl](https://vbpl-bientap-gateway.moj.gov.vn/api/qtdc/public/doc/minio/buckets/vbpl/128249/VanBanGoc_tt-2017-54-1.pdf/download) · [luatvietnam](https://luatvietnam.vn/y-te/thong-tu-54-2017-tt-byt-bo-y-te-158564-d1.html) |
| 7713/QĐ-BYT (30/12/2016); 3926/QĐ-BYT (28/08/2017) | Công bố tài liệu HL7 v2 và HL7 CDA tiếng Việt | chưa xác minh | Chưa thấy bãi bỏ | gốc-meta (qua QĐ 5969/QĐ-BYT 2021) | [QĐ 5969 PDF](https://file.medinet.gov.vn/data/soytehcm/trungtamytehocmon/attachments/2022_2/5969-qd-bytkehoachudcnttgiai_doan_20212025_82202214.pdf) |
| 365/TTYQG-GPQLCL (06/06/2025) | Yêu cầu kỹ thuật phần mềm HSBA điện tử + PL `HoSoBenhAn` | Từ khi ban hành | Còn áp dụng | gốc | [PDF](https://sontinh.quangngai.gov.vn/upload/2006782/20260423/H%C6%AF%E1%BB%9ANG%20D%E1%BA%AAN%20K%E1%BB%B8%20THU%E1%BA%ACT%20TRI%E1%BB%82N%20KHAI.pdf) |
| 102/2025/NĐ-CP (13/05/2025) | Quản lý dữ liệu y tế (Đ18 k2: BYT ban hành QCVN CSDL) | 01/07/2025 | Còn HL | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/5/102-ndcp.signed.pdf) |
| 39/2017/TT-BTTTT (15/12/2017) | Danh mục tiêu chuẩn kỹ thuật CNTT trong CQNN (CV 365 dẫn); không có HL7/DICOM | 01/07/2018 | mst.gov.vn ghi còn HL; quan hệ với Luật CĐS chưa xác minh | gốc | [PDF](https://mic.mediacdn.vn/Upload/VanBan/tt39-2017.pdf) |
| TCVN 12344:2019 (IDT ISO/TS 18530:2014) | Phân định NVYT và người bệnh (vòng tay, thẻ, GS1) | — | Còn hiệu lực; tự nguyện | gốc | [vsqi](https://tieuchuan.vsqi.gov.vn/tieuchuan/view?sohieu=TCVN+12344%3A2019) |
| 1928/QĐ-BYT (21/04/2023) + 4152/QĐ-BYT (31/12/2024) | Kiến trúc CPĐT BYT 2.1 | — | Bị QĐ 2146 thay trên thực tế (gọi là "kiến trúc hiện tại"); không nhắc HL7/FHIR/DICOM | gốc | link chưa kiểm tra được (nhic.vn lỗi chứng chỉ TLS) |

Truy vết (chưa đọc riêng): QĐ 3725/QĐ-BYT 2017 (CNTT trong xét nghiệm, xem CLS); QĐ 6085/QĐ-BYT 2019; QĐ 3090/QĐ-BKHCN 2025, QĐ 292/QĐ-BKHCN 2025, QĐ 2439/QĐ-TTg 2025 (căn cứ QĐ 2146); TT 50/2014/TT-BYT (phân loại PTTT); TCVN 13996:2024 (UDI).
Nguồn không chính thức, không dùng làm căn cứ: VN Core FHIR IG `fhir.hl7.org.vn` (doanh nghiệp duy trì, tự ghi không phải chuẩn quốc gia được phê duyệt); `ytesovietnam.vn`; công cụ tra cứu `icd.kcb.vn` của Cục QLKCB (ICD-10 TT 06, YHCT, LOINC, UCOD; là công cụ, không phải văn bản).

## 2. Yêu cầu

### A. ICD-10 (TT 06/2026, QĐ 1849/2026)

### MA-LT-R01 — Nạp đúng, đủ danh mục ICD-10 của TT 06
- **Căn cứ**: TT 06/2026 Đ3 (ban hành danh mục tại Phụ lục); Đ7 k5 b: cơ sở KCB cập nhật danh mục mã bệnh ICD-10 vào phần mềm quản lý bệnh viện để ghi chép, mã hóa; Đ7 k3 a: BHXH cập nhật lên Cổng giám định.
- **Nội dung Phụ lục (gốc, phân tích máy)**: 15.844 dòng, 29 cột: 1 STT; 2–5 chương; 6–8 khối; 9–14 tiểu khối cấp 1, 2; 15–17 nhóm 3 ký tự; **18 mã bệnh** (có chấm, có hậu tố †/*); **19 mã không dấu** (bỏ chấm, bỏ †/*); 20–21 tên và hướng dẫn mã hóa bổ sung WHO 2019 (Anh); 22–23 tên và hướng dẫn bổ sung (Việt); 24–29 cờ quy tắc (ô cờ chứa lại chính mã bệnh, không phải dấu X). 2.090 mã 3 ký tự, 10.222 mã 4 ký tự, **3.531 mã 5 ký tự** (vd B18.00, M00.00), 111 mã †, 807 mã *; chương XXII có U00–U85.
- **Áp dụng**: mọi cơ sở KCB, vendor HIS/EMR/PK · **Hiệu lực/hạn**: 01/07/2026.
- **Mức**: BẮT BUỘC (cơ sở KCB BHYT). BẮT BUỘC? với cơ sở không KCB BHYT: Đ7 k5 ghi "cơ sở khám bệnh, chữa bệnh" không giới hạn nhưng căn cứ ban hành chỉ là Luật BHYT, NĐ 188 (suy luận: nên áp như bắt buộc; CV 365 cũng dùng `maicd` cho mọi HSBA).
- **Phần mềm phải**: nạp đủ 29 cột; giữ cả dạng có chấm (cột 18) và không chấm (cột 19); lưu tên Anh, Việt, hướng dẫn bổ sung; gắn phiên bản "TT 06/2026" và ngày hiệu lực; có thủ tục cập nhật khi BYT sửa danh mục (Đ7 k2 c).
- **Bẫy**: dòng 15.750 ghi `U13/9` (đúng là `U13.9`; cột 19 vẫn `U139`) → bộ nạp phải phát hiện, sửa có ghi chú. VN Core FHIR IG ghi "16.052 codes", không khớp 15.844 dòng gốc; đừng dùng số bên thứ ba để kiểm đủ. Trường `maicd` CV 365 dài 7, `MA_BENH_CHINH` XML ≤ 7 (BHYT-DATA-R20): đừng cắt mã 5 ký tự còn 4.

### MA-LT-R02 — Quy tắc cột 24–29: áp đúng nghĩa từng cột
- **Căn cứ**: TT 06 Đ4 k2: cột 24 mã không được dùng là bệnh chính; 25 không khuyến khích dùng là bệnh chính; 26 mã không được sử dụng vì có mã 4 hoặc 5 ký tự cụ thể hơn; 27 chỉ dùng mã hóa nguyên nhân tử vong; 28 chỉ/chủ yếu ở nữ; 29 chỉ/chủ yếu ở nam. Số mã (gốc): c24 2.427 (807 mã *, mã nguyên nhân ngoài V–Y, B95–B97, Z37…); c25 221 (B90–B94, I15, I69…); c26 2.119; c27 12 (O95, O96*, O97*, P95, P96.4, S18); c28 931; c29 143.
- **Áp dụng**: như R01 · **Hiệu lực/hạn**: 01/07/2026.
- **Mức**: BẮT BUỘC (nguyên tắc mã hóa). Chặn/cảnh báo tự động trong phần mềm: NÊN (văn bản không buộc phần mềm chặn, nhưng là cách kiểm soát duy nhất ở quy mô).
- **Phần mềm phải**: cột 26 chặn ở **mọi vị trí** (bệnh chính, kèm theo, nguyên nhân tử vong); cột 27 chỉ cho phép ở trường nguyên nhân tử vong; cột 24 chặn ở bệnh chính, cho phép ở bệnh kèm theo; cột 25 yêu cầu xác nhận khi làm bệnh chính; cột 28, 29 cảnh báo khi lệch giới tính (không chặn cứng).
- **Bẫy**: BHYT-DATA-R20 trước đây chỉ chặn 24, 26, 27 ở `MA_BENH_CHINH`; đã sửa theo câu chữ TT 06 (cột 26 cấm mọi vị trí, cột 27 chỉ nguyên nhân tử vong). Quy tắc Cổng BHXH chưa đối chiếu (mục 7).

### MA-LT-R03 — Bệnh chính, kèm theo, biến chứng, di chứng theo định nghĩa TT 06
- **Căn cứ**: TT 06 Đ4 k3 a: bệnh chính là bệnh người bệnh đến KCB và được chẩn đoán xác định khi kết thúc lượt; nhiều bệnh thì chọn bệnh dùng nhiều nguồn lực (chi phí, dịch vụ, nhân lực) nhất; chưa xác định thì lấy triệu chứng chính. Đ4 k3 b–d (kèm theo, biến chứng, di chứng); Đ7 k5 c.
- **Áp dụng**: như R01 · **Hiệu lực/hạn**: 01/07/2026.
- **Mức**: BẮT BUỘC (định nghĩa); hỗ trợ phần mềm: NÊN.
- **Phần mềm phải**: tách chẩn đoán vào viện/sơ bộ khỏi chẩn đoán ra viện; bệnh chính chốt khi kết thúc lượt; hiển thị chi phí/dịch vụ theo từng chẩn đoán (nếu y lệnh gắn chẩn đoán) để hỗ trợ chọn bệnh "nhiều nguồn lực nhất"; phân loại kèm theo/biến chứng/di chứng; ghi vết người đổi bệnh chính và lý do.
- **Bẫy**: tiêu chí "nhiều nguồn lực nhất" khác quy tắc main condition của WHO; không copy logic DRG/ICD-10-AM nước ngoài.

### MA-LT-R04 — Chuyển tiếp phiên bản ICD theo ngày kết thúc lượt; không ghi đè mã cũ
- **Căn cứ**: TT 06 Đ6 k1 (áp TT 06 khi văn bản cũ khác; mã cũ bị hủy thì chọn tên bệnh phù hợp nhất trong danh mục mới); k2 (vào trước 01/07/2026, kết thúc lượt từ ngày đó → dùng mã TT 06); k3 (mã đã ghi theo văn bản cũ và đang lưu vẫn có giá trị pháp lý). QĐ 1849 PL4 (mã QĐ 4469 bị hủy), PL5 (mã mới).
- **Áp dụng**: như R01 · **Hiệu lực/hạn**: 01/07/2026 (đã qua; còn tác dụng với dữ liệu lịch sử, báo cáo so sánh).
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: chọn bộ mã theo ngày kết thúc lượt; lượt vắt qua 01/07/2026 phải mã lại bằng bộ mới trước khi chốt; HSBA đã đóng giữ mã cũ kèm phiên bản; báo cáo nhiều năm dùng bảng chuyển đổi PL4/PL5, không sửa dữ liệu gốc. Đầu ra XML: BHYT-DATA-R20.
- **Bẫy**: QĐ 1849 PL4, PL5 chưa đọc được; lấy từ BYT hoặc Cổng BHXH trước khi viết migration.

### MA-LT-R05 — Mã kép (†/*) và mã bổ sung
- **Căn cứ**: TT 06 PL cột 18 (†, *), cột 21/23 (khoảng 200 mã có "Use additional code…"), cột 24 (807 mã * không làm bệnh chính); Đ4 k4: kỹ thuật mã hóa theo hướng dẫn chuyên môn của BYT → QĐ 1849 PL2 (nguyên tắc), PL3 (thuốc, hóa chất cho chương XIX, XX); QĐ 1849 Đ2 buộc cơ sở, NVYT triển khai hướng dẫn.
- **Áp dụng**: như R01 · **Hiệu lực/hạn**: 23/06/2026 (QĐ 1849), 01/07/2026 (TT 06).
- **Mức**: BẮT BUỘC? (nghĩa vụ có trong QĐ 1849 Đ2, nhưng nội dung PL2 chưa đọc).
- **Phần mềm phải**: chọn mã † thì gợi ý mã * tương ứng; mã * buộc đi kèm mã † làm bệnh chính; hiển thị hướng dẫn bổ sung (cột 23) ngay khi chọn; chương XIX hỗ trợ thêm mã nguyên nhân ngoài chương XX; có danh mục thuốc/hóa chất PL3 để tra mã ngộ độc.
- **Bẫy**: XML BHYT chỉ có 1 `MA_BENH_CHINH` và `MA_BENH_KT` ≤ 12 mã → mã * và mã nguyên nhân ngoài đi vào `MA_BENH_KT`; XML và CV 365 không có trường liên kết cặp †/*, cần giữ cặp thì lưu nội bộ (suy luận).

### MA-LT-R06 — Mã hóa nguyên nhân tử vong
- **Căn cứ**: TT 06 Đ1 (phạm vi gồm nguyên nhân tử vong), Đ4 k2 (cột 27); QĐ 1849.
- **Áp dụng**: cơ sở có người bệnh tử vong (BV, PK có cấp cứu) · **Hiệu lực/hạn**: 01/07/2026.
- **Mức**: BẮT BUỘC (dùng mã TT 06). Quy trình chọn nguyên nhân gốc: BẮT BUỘC? (quy tắc ở PL2 QĐ 1849, chưa đọc).
- **Phần mềm phải**: trường nguyên nhân tử vong tách khỏi chẩn đoán (chuỗi trực tiếp → trung gian → gốc nếu mẫu giấy báo tử yêu cầu); mã cột 27 chỉ cho phép ở trường này; lưu mã nguyên nhân ngoài V–Y cho tử vong do chấn thương.
- **Bẫy**: công cụ "UCOD Việt Nam" trên `icd.kcb.vn` là công cụ, không phải nghĩa vụ. Mẫu giấy báo tử, liên thông khai tử: xem GIAYTO.

### MA-LT-R07 — Sửa Q87.11 → Q87.1 trong danh mục TT 01/2025
- **Căn cứ**: TT 06 Đ5 k3: sửa mã Q87.11 (Hội chứng Prader Willi) tại Phụ lục 3 TT 01/2025/TT-BYT thành Q87.1.
- **Áp dụng**: cơ sở KCB BHYT, vendor · **Hiệu lực/hạn**: 01/06/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: mọi bảng tham chiếu dựng từ PL 3 TT 01/2025 dùng Q87.1; dữ liệu trước 01/06/2026 giữ nguyên.
- **Bẫy**: Q87.11 không có trong Phụ lục TT 06 (chỉ Q87, Q87.0–Q87.5, Q87.8).

### MA-LT-R08 — Ký số tổ chức trên phiếu hẹn khám lại và phiếu chuyển cơ sở bản điện tử
- **Căn cứ**: TT 06 Đ5 k2: phần đóng dấu ở Mẫu phiếu hẹn (PL V TT 01/2025) và ký tên, đóng dấu ở Mẫu phiếu chuyển (PL VI) được thay bằng ký số xác thực của cơ sở KCB đối với bản điện tử.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/06/2026.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: phát hành phiếu hẹn, phiếu chuyển điện tử có chữ ký số tổ chức (không chỉ hình dấu). Chi tiết chữ ký số tổ chức: EMR-R08.
- **Bẫy**: điều khoản ký số nằm trong thông tư "mã hóa ICD", dễ sót khi tra theo chủ đề.

### MA-LT-R09 — Kiểm định khi nạp danh mục chuẩn
- **Căn cứ**: TT 06 Đ7 k5 b; thực tế lỗi nguồn (`U13/9`). (Suy luận cho QĐ 1227, 2427, 2493, 2805, TT 23 phát hành dạng PDF/xlsx.)
- **Áp dụng**: vendor · **Hiệu lực/hạn**: thường xuyên.
- **Mức**: NÊN.
- **Phần mềm phải**: nạp bằng script có kiểm định dạng mã, trùng mã, số dòng so bản công bố, đối chiếu cột có/không dấu, diff với phiên bản trước; lưu tệp nguồn (hash) và biên bản nạp.

### MA-LT-R10 — ICD-11: chưa có nghĩa vụ; ICD-10 TT 06 là bộ mã pháp định duy nhất
- **Căn cứ**: không tìm thấy văn bản buộc dùng ICD-11 (đến 05/10/2026). QĐ 2146 Phần IX.1.2 a (lộ trình 2025–2026, tiếp tục đến 2030) đặt mục tiêu chuẩn hóa dữ liệu theo ICD-10, ICD-11, SNOMED CT, LOINC, RxNorm: nhiệm vụ của BYT, không phải nghĩa vụ cơ sở KCB.
- **Áp dụng**: — · **Hiệu lực/hạn**: —.
- **Mức**: dữ liệu gửi BHYT và CV 365 dùng ICD-10 TT 06: BẮT BUỘC (xem R01). Chuẩn bị kiến trúc đa hệ mã: NÊN.
- **Phần mềm phải**: không dùng ICD-10-CM, ICD-10-AM, ICD-11 thay ICD-10 TT 06 ở trường chẩn đoán chính thức; ICD-11 nếu dùng thì ở trường phụ qua bảng ánh xạ (MA-LT-P02).

### MA-LT-R11 — Hỗ trợ nhân viên chuyên trách mã hóa lâm sàng
- **Căn cứ**: TT 06 Đ7 k5 d: khuyến khích từng bước bố trí nhân viên chuyên trách mã hóa lâm sàng để hướng dẫn, kiểm tra, giám sát.
- **Áp dụng**: cơ sở KCB · **Hiệu lực/hạn**: 01/07/2026.
- **Mức**: NÊN.
- **Phần mềm phải**: vai trò "mã hóa lâm sàng" có hàng đợi rà soát trước khi chốt/gửi; sửa mã có vết; báo cáo tỷ lệ lỗi mã theo khoa, bác sĩ.

### B. Danh mục kỹ thuật (TT 23/2024 sửa bởi TT 25/2026)

### MA-LT-R12 — Đến hết 31/12/2027 dùng Phụ lục 01 TT 23
- **Căn cứ**: TT 23 Đ1 k1 a (sửa bởi TT 25 Đ3 k1): PL 01 thực hiện đến hết 31/12/2027. TT 23 Đ4 k4 (bổ sung bởi TT 25 Đ3 k2): STT kỹ thuật theo chương của TT 43/2013, TT 21/2017 ở cột 2 PL 01 tiếp tục dùng làm mã kỹ thuật (trừ mã "BS_"); kỹ thuật đã phân loại PTTT theo TT 50/2014 tiếp tục áp mức đó.
- **Cấu trúc PL 01 (gốc)**: STT (19.438 dòng); **mã kỹ thuật** `chương.STT` (vd `1.1`) hoặc `BS_chương.STT` (khoảng 1.232 mã); tên chương (28 chương theo chuyên khoa); tên kỹ thuật.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 18/10/2024 → 31/12/2027.
- **Mức**: BẮT BUỘC.
- **Phần mềm phải**: danh mục DVKT nội bộ gắn mã PL 01 (kể cả BS_), giữ mức PTTT (TT 50/2014); ánh xạ sang mã DVKT BHYT `CC.KKKK.GGGG` (QĐ 2010, xem BHYT-DATA-R17).
- **Bẫy**: TT 23 bản gốc ghi PL 01 "đến 30/6/2026", PL 02 "từ 01/7/2026"; TT 25 (Đ3 hiệu lực 01/07/2026) đã lùi mốc và bỏ hai cụm ngày trên tiêu đề phụ lục (Đ3 k4, k5). Tài liệu trước 07/2026 ghi sai mốc.

### MA-LT-R13 — Chuẩn bị chuyển sang Phụ lục 02 từ 01/01/2028
- **Căn cứ**: TT 23 Đ1 k1 b (sửa bởi TT 25 Đ3 k1): PL 02 thực hiện từ 01/01/2028; Đ1 k4: PL 02 xếp theo hệ cơ quan và cấu trúc giải phẫu; Đ5 k4 b (sửa bởi TT 25 Đ3 k3): cơ sở KCB chuẩn bị điều kiện để thực hiện PL 02 từ 01/01/2028.
- **Cấu trúc PL 02 (gốc)**: STT (9.128 dòng); STT trong chương; tên chương (30 chương theo hệ cơ quan); **"Mã liên kết"** (trỏ về mã PL 01); tên kỹ thuật. **Không có cột mã kỹ thuật riêng.** Quan hệ PL 02 ↔ PL 01 là N–N (vd STT 16 và 17 cùng liên kết 10.39; STT 35 "2.129;"); nhiều dòng trống mã liên kết (kỹ thuật mới).
- **Áp dụng**: mọi cơ sở KCB, vendor HIS · **Hiệu lực/hạn**: chuẩn bị từ nay; áp dụng 01/01/2028.
- **Mức**: BẮT BUỘC (cơ sở phải chuẩn bị). Cách thiết kế phần mềm: NÊN.
- **Phần mềm phải**: lưu PL 02 như hệ mã riêng hiệu lực từ 01/01/2028; khóa tạm `(chương, STT chương)` cho tới khi BYT công bố mã chính thức (suy luận); crosswalk N–N có trạng thái "trống liên kết"; báo cáo kỹ thuật cơ sở đang làm mà PL 02 không còn hoặc tách/gộp; chạy song song hai mã giai đoạn chuyển (MA-LT-P05).
- **Bẫy**: chưa có văn bản về mã DVKT BHYT và giá DVKT theo PL 02 (mục 7). TT 23 Đ4 k3 (sửa): cơ sở có GPHĐ tiếp tục làm kỹ thuật đã duyệt đến 31/12/2027 không phải điều chỉnh giấy phép → suy luận: từ 2028 có thể phải rà lại phạm vi chuyên môn theo PL 02.

### MA-LT-R14 — Chỉ cho chỉ định kỹ thuật trong phạm vi chuyên môn được phê duyệt
- **Căn cứ**: TT 23 Đ5 k4 a (sửa bởi TT 25): cơ sở bảo đảm điều kiện thực hiện danh mục kỹ thuật đã được phê duyệt; Đ4 k3 (sửa). TT 32/2023 PL XII (sửa bởi TT 25 Đ2 k1): kỹ thuật "*" của điều dưỡng chỉ làm khi người chịu trách nhiệm chuyên môn kỹ thuật cho phép bằng văn bản, tối đa đến 31/12/2029.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng; điều dưỡng "*" đến 31/12/2029.
- **Mức**: BẮT BUỘC? (nghĩa vụ của cơ sở; ràng buộc trong phần mềm là cách thực thi, suy luận).
- **Phần mềm phải**: DVKT của cơ sở có cờ "đã phê duyệt" + số quyết định + ngày; chặn/cảnh báo chỉ định ngoài danh mục; điều dưỡng làm kỹ thuật "*" phải có văn bản cho phép cá nhân còn hạn.

### MA-LT-R15 — Liên kết ba lớp mã: DVKT nội bộ ↔ mã TT 23 ↔ mã BHYT / mã chỉ số CLS
- **Căn cứ**: TT 23 + TT 25 (R12, R13); QĐ 2010/2025 Đ1, Đ3 (BHYT-DATA-R17); QĐ 1227 PL (cột mã KT TT 23); CV 365 PL mục V `machidinh`, mục VII `machiso`.
- **Áp dụng**: cơ sở KCB, vendor · **Hiệu lực/hạn**: đang áp dụng.
- **Mức**: BẮT BUỘC với cơ sở KCB BHYT (qua XML); NÊN với phần còn lại.
- **Phần mềm phải**: một dịch vụ nội bộ ánh xạ được tới mã PL 01 (sau 2028 là PL 02), mã DVKT BHYT, và (xét nghiệm, CĐHA) một hoặc nhiều mã chỉ số QĐ 1227; mỗi ánh xạ có ngày hiệu lực và văn bản nguồn (MA-LT-P02).

### C. Danh mục mã dùng chung lâm sàng (LOINC, SNOMED CT)

### MA-LT-R16 — Mã chỉ số CLS theo QĐ 1227/2025 (tham chiếu LOINC)
- **Căn cứ**: QĐ 1227 Đ1 (danh mục để thống nhất thuật ngữ, chuẩn hóa dữ liệu, ứng dụng CNTT trong bệnh án điện tử, liên thông kết quả CLS, dữ liệu KCB, BHYT); Đ2 (áp dụng thống nhất, toàn bộ cơ sở KCB công và tư). PL01 (gốc): **mã dùng chung 7 số** (`1000001`…), tên chỉ số, mã KT TT 23, **mã LOINC tham chiếu** + 6 trục LOINC, đơn vị. QĐ 2010/2025 Đ3: XML4 dùng mã chỉ số QĐ 1227 (BHYT-DATA-R17).
- **Áp dụng**: BV công, BV tư, PK có xét nghiệm/CĐHA; vendor HIS/LIS/RIS · **Hiệu lực/hạn**: 11/04/2025.
- **Mức**: BẮT BUỘC với dữ liệu XML4 BHYT. BẮT BUỘC? với HSBA và liên thông kết quả CLS (Đ2 "áp dụng thống nhất" nhưng không có chế tài; CV 365 `machiso` không nêu hệ mã).
- **Phần mềm phải**: danh mục chỉ số LIS/RIS ánh xạ tới mã 7 số; lưu LOINC làm mã phụ; đơn vị theo danh mục hoặc có bảng quy đổi; điền `machiso` bằng mã QĐ 1227 (suy luận). Phía vận hành LIS (mã máy, cờ "chưa có mã 1227"): CLS-R07.
- **Bẫy**: QĐ 1227 là "Đợt 1"; chưa thấy đợt sau. Chỉ số chưa có mã thì XML4 tạm dùng PL11 QĐ 7603 (QĐ 2010 Đ3). LOINC chỉ là tham chiếu; mã pháp định là mã 7 số. Không có văn bản nào bắt dùng LOINC.

### MA-LT-R17 — Thuật ngữ y học lâm sàng (QĐ 2427, 2493, 2805) và trường VNCODE/SNOMED của CV 365
- **Căn cứ**: QĐ 2427/2025 Đ1, Đ2 (thuật ngữ giải phẫu; ghi nhận thống nhất trong bệnh án điện tử, liên thông KCB–BHYT–Sổ SKĐT; mọi cơ sở KCB công, tư). QĐ 2493/2025 Đ1–Đ3 (bất thường hình thái; PL01 gốc: mã 7 số `6200001`…`6205155`, tên Việt, **mã tham chiếu SNOMED CT**, tên Anh). QĐ 2805/2025 Đ1–Đ3 (dị ứng, phát hiện). CV 365 PL mục III (khám cơ quan, 25.x): `dauchung_ma` gồm `VNCODE` (chuỗi 25, thuật ngữ lâm sàng Việt Nam) và `SNOMED` (chuỗi 25, thuật ngữ quốc tế).
- **Áp dụng**: BV công, BV tư, PK; vendor EMR · **Hiệu lực/hạn**: 25/07/2025, 04/08/2025, 04/09/2025.
- **Mức**: BẮT BUỘC? (QĐ ghi "áp dụng thống nhất", không chế tài; CV 365 PL III.1.1 h buộc dùng danh mục dùng chung của BYT).
- **Phần mềm phải**: kho thuật ngữ nạp đủ các đợt; trường triệu chứng/khám cơ quan chọn được thuật ngữ có mã (VNCODE = mã 7 số, suy luận) và tự điền SNOMED CT tham chiếu; vẫn giữ văn bản tự do (`dauchung`, `dauchung_ghichu`).
- **Bẫy**: ví dụ trong PL CV 365 (`VNCODE` "12587", `SNOMED` "9987888") không khớp dạng mã `62xxxxx` của QĐ 2493 → chỉ là minh họa. Quan hệ chính thức VNCODE ↔ mã dùng chung chưa có văn bản (mục 7).

### MA-LT-R18 — Giấy phép thuật ngữ quốc tế (SNOMED CT, LOINC)
- **Căn cứ**: không có văn bản VN nào về giấy phép. QĐ 1227, 2493 đưa mã LOINC, SNOMED CT vào phụ lục; QĐ 2146 nêu SNOMED CT, LOINC, RxNorm, UMLS.
- **Áp dụng**: vendor · **Hiệu lực/hạn**: —.
- **Mức**: NÊN (rủi ro hợp đồng/sở hữu trí tuệ, không phải luật y tế).
- **Phần mềm phải**: sổ đăng ký hệ mã ngoài (nguồn, phiên bản, điều kiện giấy phép); không phân phối tệp SNOMED CT/LOINC đầy đủ khi chưa rõ giấy phép; chỉ dùng tập con BYT đã công bố đến khi xác nhận (MA-LT-P08).
- **Bẫy**: tư cách thành viên SNOMED International của VN chưa xác minh (mục 7).

### D. Kiến trúc và chuẩn liên thông

### MA-LT-R19 — Điền mã chuẩn đúng trong gói `HoSoBenhAn` (CV 365)
- **Căn cứ**: CV 365 PL III.1.1 d (kết xuất XML/JSON theo phụ lục), III.1.1 h (danh mục dùng chung BYT), IV.1. Trường mã hóa (gốc): `khambenh_chandoanvaovienmaicd`, `maicd` (chuỗi 7), `tenicd` (255), `maicd_khac` (100), `tenicd_khac`; `VNCODE`, `SNOMED` (25); `machidinh`, `machiso` (255); `mathuocvattu_byt` (255) cạnh `mathuocvattu_bv`. Ví dụ dùng mã ICD có chấm ("R10.4").
- **Áp dụng**: cơ sở có HSBA điện tử; vendor EMR · **Hiệu lực/hạn**: từ 06/06/2025.
- **Mức**: BẮT BUỘC? (giá trị pháp lý của CV 365: EMR-R18).
- **Phần mềm phải**: `maicd` lấy cột 18 TT 06 (có chấm, bỏ †/*; suy luận từ ví dụ); `maicd_khac` nhiều mã phân cách thống nhất với XML (";"); `machiso` = mã QĐ 1227; `VNCODE`/`SNOMED` theo R17; `mathuocvattu_byt` là mã BYT/BHYT, không phải mã nội bộ.
- **Bẫy**: schema không có trường hệ mã (`system`) hay phiên bản; nên kèm metadata phiên bản ở lớp vận chuyển (suy luận). Phần còn lại schema: EMR-R18.

### MA-LT-R20 — HL7 FHIR: không có nghĩa vụ chung; QĐ 2146 chỉ đặt lộ trình cho BYT
- **Căn cứ** (toàn văn QĐ 2146, thứ cấp): Phần I.2: áp dụng cho đơn vị thuộc, trực thuộc BYT; khuyến khích Sở Y tế; bộ ngành, địa phương khác tham chiếu. Phần IX.1.2 a (lộ trình 2025–2026, tiếp tục đến 2030): xây dựng cơ chế liên thông dữ liệu đáp ứng HL7 FHIR R4, DICOM V3.0 (QĐ ghi "ISO 12052:2026"). IX.1.1 mục III.11: hệ thống liên thông theo chuẩn quốc tế, đầu mối TTYQG, 2026–2030. VII.2.6 b, c: liệt kê HL7 FHIR, OMOP CDM, SNOMED, LOINC, RxNorm… dạng ví dụ. VII.2.4 b: định dạng trao đổi XML/JSON, từ điển dữ liệu. QĐ 1928/2023 (bản trước) không nhắc HL7/FHIR/DICOM.
- **Áp dụng**: BV/đơn vị trực thuộc BYT; BV công địa phương, BV tư, PK: không có nghĩa vụ · **Hiệu lực/hạn**: 15/07/2026; không có hạn chót FHIR cụ thể (lộ trình đến 2030).
- **Mức**:
  - BẮT BUỘC? — đơn vị trực thuộc BYT, ở mức "tuân thủ khung" (xem R23).
  - NÊN — mọi đối tượng còn lại: kiến trúc sẵn sàng FHIR.
- **Phần mềm phải**: thêm được façade FHIR R4 (4.0.1) mà không đổi mô hình lõi: ID ổn định, mã có `system` + `version`, tách Patient/Encounter/Condition/Observation/ServiceRequest/MedicationRequest; không ghi "tuân thủ FHIR theo quy định" trong tài liệu chào bán.
- **Bẫy**: "QĐ 2146 không nhắc FHIR" (tóm tắt luatvietnam) là sai; "QĐ 2146 bắt buộc FHIR R4 và DICOM" (ytesovietnam, VN Core FHIR IG) là nói quá. Ấn bản ISO 12052:2026 chưa xác minh.

### MA-LT-R21 — HL7 v2 và DICOM cho RIS-PACS, LIS (TT 54/2017)
- **Căn cứ**: TT 54 Đ2 k8–k11 (định nghĩa HL7, HL7 CDA, CCD, DICOM). PL I nhóm IV RIS-PACS mức cơ bản: TC 67 giao diện 2 chiều với máy CĐHA; TC 68 RIS chuyển chỉ định vào máy CĐHA theo HL7; TC 70 hỗ trợ HL7 bản tin, DICOM; TC 74 xuất DICOM ra CD/DVD kèm viewer hoặc đường dẫn web; nâng cao: TC 76–79 (xử lý ảnh, JPEG2000, xem web, hội chẩn). Nhóm V LIS: TC 84 kết nối máy xét nghiệm 2 chiều (cơ bản), TC 88 liên thông HIS (nâng cao), không nêu chuẩn. Nhóm VI: TC 109 áp dụng tiêu chuẩn trong nước hoặc quốc tế (HL7, HL7 CDA, DICOM, ICD-10…). Đ4 k3: thiếu 1 tiêu chí thì xếp mức thấp hơn.
- **Áp dụng**: cơ sở KCB có GPHĐ khi tự xác định mức CNTT; vendor RIS-PACS, LIS · **Hiệu lực/hạn**: 27/02/2018, phần không thuộc EMR còn HL.
- **Mức**:
  - BẮT BUỘC? — khi cơ sở công bố đạt mức theo TT 54 (bộ tiêu chí xếp mức, không phải điều kiện hoạt động).
  - NÊN — với người mua chưa cần xếp mức.
- **Phần mềm phải**: RIS nhận order từ HIS và đẩy worklist xuống máy (HL7 v2 ORM/OMI hoặc DICOM MWL); PACS lưu DICOM gốc, xuất CD/DVD kèm viewer hoặc link web; báo cáo CĐHA đồng bộ 2 chiều với HIS. Chi tiết tiêu chí LIS/RIS và DICOM: CLS-R17, CLS-R19, CLS-R21.
- **Bẫy**: TT 54 không nêu phiên bản HL7 hay DICOM. Tiêu chí EMR của TT 54 (gồm TC 144 HL7 CDA/CCD) đã hết HL → không còn căn cứ đòi CDA. Liên thông kết quả CLS từ 01/01/2027, thời hạn lưu ảnh: CLS-R01, CLS-R18.

### MA-LT-R22 — Tài liệu HL7 v2 và HL7 CDA tiếng Việt (QĐ 7713/2016, 3926/2017): tham khảo
- **Căn cứ**: QĐ 5969/QĐ-BYT 2021 (gốc) mô tả QĐ 7713 công bố tài liệu HL7 bản tin và QĐ 3926 công bố tài liệu HL7 CDA tiếng Việt để áp dụng vào phần mềm y tế; QĐ 5969 giao nâng cấp LGSP BYT trao đổi theo HL7 (2022–2023).
- **Áp dụng**: — · **Hiệu lực/hạn**: chưa xác minh.
- **Mức**: NÊN.
- **Phần mềm phải**: làm giao diện HL7 v2 thì có thể dùng thuật ngữ tài liệu tiếng Việt; không coi là chuẩn bắt buộc.
- **Bẫy**: bản gốc hai QĐ chưa đọc (`ehealth.gov.vn` không phân giải DNS); phiên bản HL7 v2.x chưa xác minh.

### MA-LT-R23 — Đơn vị thuộc BYT: tuân thủ Khung kiến trúc số và Khung kiến trúc dữ liệu
- **Căn cứ**: QĐ 2146 Đ2 (TTYQG đầu mối), Phần I.2, III.1 (tuân thủ QĐ 3090/QĐ-BKHCN, QĐ 292/QĐ-BKHCN, QĐ 2439/QĐ-TTg; tiêu chuẩn, quy chuẩn bắt buộc), VII.2.3 b (ứng dụng dùng chung tuân thủ bộ tiêu chuẩn giao diện, API chuẩn hóa), VII.2.4 b (nhập một lần, dùng nhiều nơi; từ điển dữ liệu, chuẩn hóa danh mục), VIII.2 (kết nối qua LGSP), IX.2.6. QĐ 2113 (chưa đọc). CV 365 PL III.1.3 b: phần mềm HSBA tuân thủ Khung Kiến trúc CPĐT/kiến trúc cấp bộ/CQĐT cấp tỉnh hiện hành.
- **Áp dụng**: BV/đơn vị trực thuộc BYT; BV công địa phương theo kiến trúc CQĐT tỉnh; BV tư, PK: tham chiếu · **Hiệu lực/hạn**: 15/07/2026.
- **Mức**: BẮT BUỘC? (QĐ hành chính nội bộ ngành, không phải VBQPPL).
- **Phần mềm phải**: với khách hàng trực thuộc BYT: tài liệu ánh xạ sản phẩm vào các lớp kiến trúc QĐ 2146 (người dùng, kênh, ứng dụng, dữ liệu, hạ tầng/ANM, hỗ trợ); API mở, XML/JSON; tích hợp LGSP BYT khi được yêu cầu; danh mục theo từ điển dữ liệu khi QĐ 2113 và danh mục dữ liệu chủ hoàn thiện.

### MA-LT-R24 — Từ điển dữ liệu, danh mục dùng chung và QCVN cấu trúc thông điệp đang xây dựng
- **Căn cứ**: NĐ 102/2025 Đ18 k2 (gốc-OCR, chỉ diễn giải): giao BYT ban hành QCVN về CSDL quốc gia về y tế và các CSDL chuyên ngành. QĐ 2146 IX.1.1: tiêu chuẩn, QCVN cấu trúc thông điệp trao đổi dữ liệu (Cục KHCN&ĐT, 2026); Từ điển dữ liệu ngành (2026–2027); danh mục dữ liệu dùng chung (2026–2030).
- **Áp dụng**: tương lai, mọi hệ thống trao đổi với CSDL QG về y tế · **Hiệu lực/hạn**: chưa ban hành (đến 05/10/2026).
- **Mức**: NÊN (theo dõi).
- **Phần mềm phải**: lớp xuất/nhập theo "hợp đồng dữ liệu" có phiên bản để khi QCVN ra chỉ thêm adapter (MA-LT-P06).

### MA-LT-R25 — TCVN tin học y tế (tự nguyện)
- **Căn cứ**: TCVN 12344:2019 (IDT ISO/TS 18530:2014), còn hiệu lực: phân định và làm nhãn người bệnh, NVYT trên vòng tay, thẻ, dùng AIDC + GS1. TCVN là tự nguyện trừ khi được viện dẫn bắt buộc (nguyên tắc chung, chưa đọc lại điều khoản Luật Tiêu chuẩn và QCKT).
- **Áp dụng**: BV định danh người bệnh bằng mã vạch/RFID · **Hiệu lực/hạn**: đang có hiệu lực.
- **Mức**: NÊN.
- **Phần mềm phải**: nếu in vòng tay/nhãn: mã định danh người bệnh duy nhất, mã vạch 2D theo GS1, dữ liệu tối thiểu theo tiêu chuẩn.
- **Bẫy**: chưa rà hết TCVN nhóm ICS 35.240.80; TCVN 13239:2024 (QĐ 2146 nêu) chưa xác định tên.

### MA-LT-R26 — Tự xác định mức ứng dụng CNTT theo TT 54 (phần còn hiệu lực)
- **Căn cứ**: TT 54 Đ3 (8 nhóm tiêu chí), Đ4 (nguyên tắc), Đ5 k1–k3 (người đứng đầu ra quyết định xác định mức, gửi cấp trên, chịu trách nhiệm; xác định lại nếu cấp trên phát hiện sai).
- **Áp dụng**: cơ sở KCB có GPHĐ · **Hiệu lực/hạn**: đang áp dụng, chờ thông tư thay (dự thảo thay TT 54).
- **Mức**: BẮT BUỘC? (nghĩa vụ xác định mức có trong Đ5; giá trị thực tế sau khi tiêu chí EMR bị bỏ chưa rõ).
- **Phần mềm phải**: vendor cung cấp ma trận đáp ứng từng tiêu chí (HIS, LIS, RIS-PACS, phi chức năng) kèm bằng chứng HL7/DICOM/ICD-10 cho TC 70, 109.

**Tổng hợp mức** (theo mức cao nhất của mục): BẮT BUỘC 11 (R01, R02, R03, R04, R06, R07, R08, R12, R13, R15, R16); BẮT BUỘC? 8 (R05, R14, R17, R19, R20, R21, R23, R26); NÊN 7 (R09, R10, R11, R18, R22, R24, R25). R10 có phần BẮT BUỘC dẫn về R01.

## 3. Pattern thiết kế

### MA-LT-P01 — Dịch vụ thuật ngữ đa hệ mã có hiệu lực theo ngày
- **Giải quyết**: R01, R04, R10, R12, R13, R16, R17
- **Cách làm**: mọi bộ mã (ICD-10 TT 06, TT 23 PL01/PL02, QĐ 1227, QĐ 2427/2493/2805, mã BHYT, LOINC, SNOMED CT, ICD-11) là code system có phiên bản; khái niệm có khoảng hiệu lực; mọi tra cứu kèm ngày. API `resolve(system, code, as_of)`, `search(system, text, as_of)`, `validate(system, code, as_of, context)`.
- **Gợi ý dữ liệu**: `code_system(id, uri, name, publisher, legal_doc, license_note)` (vd `vn-icd10-tt06`, `vn-dmkt-tt23-pl01`, `vn-cls-qd1227`); `code_system_version(system_id, version, legal_doc_no, valid_from, valid_to, source_file_hash, loaded_at)` + exclusion constraint chống chồng `daterange`; `concept(version_id, code, code_alt, display_vi, display_en, parent_code, attrs jsonb, status)` unique `(version_id, code)`; ICD-10: `code_alt` = cột 19, `attrs` = cột 20–29 (`c24…c29`, `dagger`, `asterisk`).
- **Đánh đổi**: tốn công nạp, kiểm; đổi lại không phải sửa mã cũ khi văn bản thay.

### MA-LT-P02 — Ánh xạ mã nội bộ ↔ mã chuẩn có hiệu lực theo ngày (concept map)
- **Giải quyết**: R12, R13, R15, R16, R17, R19
- **Cách làm**: dịch vụ nội bộ không buộc chết vào một mã chuẩn; khi chốt hồ sơ gọi `map(source, target_system, as_of)`; nhiều kết quả hoặc `unmatched` → hàng đợi người mã hóa (R11).
- **Gợi ý dữ liệu**: `concept_map(source_system, source_code, target_system, target_version_id, target_code, equivalence ENUM('equal','wider','narrower','related','unmatched'), valid_from, valid_to, basis_doc, created_by)`; chỉ mục `(source_system, source_code, valid_from)`; cho phép N–N.
- **Đánh đổi**: phải chốt quy tắc `as_of` cho từng hệ mã: ICD theo ngày kết thúc lượt (TT 06 Đ6 k2); DVKT theo ngày y lệnh (suy luận; xem BHYT-DATA mục 7).

### MA-LT-P03 — Bộ kiểm tra chẩn đoán theo luật TT 06 (rule engine)
- **Giải quyết**: R02, R03, R05, R06
- **Cách làm**: luật khai báo dạng dữ liệu sinh từ cờ cột 24–29 và †/*: `c26 ANY BLOCK`, `c27 NOT_DEATH_CAUSE BLOCK`, `c24 PRIMARY BLOCK`, `c25 PRIMARY CONFIRM`, `c28 sex=M WARN`, `asterisk require paired_dagger_primary`. Chạy ở 3 điểm: lúc chọn mã (UI), lúc chốt lượt, lúc sinh XML/CV 365 (chặn cuối).
- **Gợi ý dữ liệu**: `coding_rule(rule_code, scope, action, source_column, version_id)`; log vượt cảnh báo `(encounter_id, rule_code, user_id, reason, at)`.
- **Đánh đổi**: chặn cứng có thể tắc ca thật (vd cột 28 với người chuyển giới) → cột 28/29 chỉ cảnh báo, ghi lý do vượt.

### MA-LT-P04 — Ảnh chụp mã hóa theo lượt KCB
- **Giải quyết**: R03, R04, R19
- **Cách làm**: kết thúc lượt thì đóng băng chẩn đoán; sửa sau chốt là thêm bản ghi mới có lý do, không update.
- **Gợi ý dữ liệu**: `encounter_diagnosis(encounter_id, role ENUM('primary','secondary','complication','sequela','death_cause','admission'), system, version_id, code, display, coder_id, coded_at, reason_change)`.
- **Đánh đổi**: tăng dung lượng; đổi lại đáp ứng TT 06 Đ6 k3 và ghi vết (EMR-R10, EMR-R12).

### MA-LT-P05 — Chuyển PL 01 → PL 02 (dual-coding)
- **Giải quyết**: R12, R13, R14
- **Cách làm**: nạp PL 02 với `valid_from = 2028-01-01`; crosswalk N–N từ cột "mã liên kết"; báo cáo sẵn sàng 2028: (a) dịch vụ có mã PL01 mà không dòng PL02 nào trỏ tới; (b) mã PL01 tách nhiều kỹ thuật PL02; (c) kỹ thuật PL02 trống liên kết. Giai đoạn chuyển lưu cả mã PL01 và khóa PL02.
- **Gợi ý dữ liệu**: khóa tạm PL02 `(chapter_no, chapter_seq)` chỉ nằm trong bảng map, không nhúng vào dữ liệu giao dịch.
- **Đánh đổi**: khóa tạm có thể đổi khi BYT/BHXH ban hành mã chính thức.

### MA-LT-P06 — Cổng tích hợp với adapter theo chuẩn
- **Giải quyết**: R16, R19, R20, R21, R23, R24
- **Cách làm**: mô hình lõi trung lập; adapter: XML BHYT; JSON/XML `HoSoBenhAn` CV 365; HL7 v2 (ORM/OMI–ORU) cho LIS/RIS; DICOM (MWL, C-STORE/C-FIND, DICOMweb) cho PACS; façade FHIR R4 khi có yêu cầu; adapter QCVN khi ban hành.
- **Gợi ý dữ liệu**: `interface_message(channel, standard, standard_version, direction, payload_ref, hash, status, ack, created_at)`; mọi mã gửi đi kèm `system` + `version` nội bộ.
- **Đánh đổi**: thêm một tầng; đổi lại không viết lại lõi khi BYT chọn chuẩn.

### MA-LT-P07 — Đường ống nạp danh mục chuẩn có kiểm định
- **Giải quyết**: R01, R09, R16, R17, R24
- **Cách làm**: tải tệp gốc (PDF/xlsx) → trích bảng → kiểm (số dòng, mẫu mã, trùng, cột có/không dấu, diff version trước) → biên bản (lỗi nguồn như `U13/9`, cách xử lý) → duyệt → kích hoạt theo `valid_from`.
- **Gợi ý dữ liệu**: `catalog_load(system, version, source_url, source_hash, row_count, errors jsonb, approved_by, activated_at)`.
- **Đánh đổi**: PDF 1.271 trang khó trích; xin bản xlsx/CSV từ Cổng BHXH hoặc `icd.kcb.vn` nhưng vẫn đối chiếu bản gốc pháp lý.

### MA-LT-P08 — Sổ đăng ký giấy phép hệ mã ngoài
- **Giải quyết**: R18
- **Cách làm**: chặn xuất toàn bộ SNOMED CT/LOINC khi chưa có giấy phép; chỉ xuất mã đã dùng trong hồ sơ.
- **Gợi ý dữ liệu**: `code_system.license_note`, cờ `redistributable`.
- **Đánh đổi**: hạn chế tính năng tra cứu đầy đủ cho đến khi rõ giấy phép.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| MA-LT-A01 | R01 | Đếm danh mục ICD đang hiệu lực, so 15.844 dòng; kiểm có cột không dấu, tên Anh, hướng dẫn bổ sung, 6 cờ 24–29 | Kết quả truy vấn, tệp nguồn đã nạp | BẮT BUỘC |
| MA-LT-A02 | R01, R09 | Tìm `U13.9`, `U139`, `U13/9`; tìm mã 5 ký tự (M00.00, I70.00) và U07.1 | Kết quả tìm | NÊN |
| MA-LT-A03 | R02 | Thử: B95.0 (c24) làm bệnh chính; A00 (c26) ở bệnh kèm theo; O96.0 (c27) làm bệnh kèm theo; B90.0 (c25) làm bệnh chính; C53.0 (c28) cho người bệnh nam | Ảnh màn hình chặn/cảnh báo, log | BẮT BUỘC (dùng đúng mã) / NÊN (chặn tự động) |
| MA-LT-A04 | R03, R04 | Lượt nội trú vào 30/06/2026 ra 02/07/2026: kiểm bộ mã khi chốt; HSBA đóng trước 01/07/2026: mã cũ còn nguyên, có phiên bản | Ảnh màn hình, bản ghi `encounter_diagnosis` | BẮT BUỘC |
| MA-LT-A05 | R04 | Hỏi bảng chuyển đổi QĐ 4469 → TT 06 (PL4, PL5 QĐ 1849): nguồn, ngày nạp, số dòng | Tài liệu, tệp map | BẮT BUỘC |
| MA-LT-A06 | R05 | Chọn A17.0† và G01*: có gợi ý cặp, hiển thị hướng dẫn bổ sung; mã * làm bệnh chính bị chặn | Ảnh màn hình | BẮT BUỘC? |
| MA-LT-A07 | R06 | Ca tử vong: có trường nguyên nhân tử vong riêng; mã cột 27 chỉ cho phép ở đây | Ảnh màn hình, giấy báo tử xuất ra | BẮT BUỘC |
| MA-LT-A08 | R07 | Tìm Q87.11 trong mọi danh mục | Kết quả = 0 với dữ liệu sau 01/06/2026 | BẮT BUỘC |
| MA-LT-A09 | R08 | Xuất phiếu hẹn, phiếu chuyển điện tử; kiểm chữ ký số tổ chức (chứng thư, thời điểm ký) | PDF đã ký, kết quả kiểm chữ ký | BẮT BUỘC |
| MA-LT-A10 | R11 | Có vai trò mã hóa lâm sàng, hàng đợi rà soát, báo cáo lỗi mã | Ảnh phân quyền, báo cáo | NÊN |
| MA-LT-A11 | R12 | Mỗi DVKT có mã PL01 (kể cả BS_), mức PTTT TT 50; truy vấn dịch vụ thiếu mã | Kết quả truy vấn | BẮT BUỘC |
| MA-LT-A12 | R13 | Đã nạp PL02 chưa, crosswalk N–N, báo cáo sẵn sàng 2028 | Tài liệu thiết kế, báo cáo thử | BẮT BUỘC (cơ sở chuẩn bị) / NÊN (cách làm) |
| MA-LT-A13 | R14 | Chỉ định DVKT ngoài danh mục phê duyệt; điều dưỡng chỉ định kỹ thuật "*" không có văn bản cho phép | Ảnh chặn/cảnh báo | BẮT BUỘC? |
| MA-LT-A14 | R15 | 20 dịch vụ ngẫu nhiên: đủ map nội bộ → TT 23 → mã BHYT → (CLS) mã QĐ 1227, có ngày hiệu lực | Bảng mẫu | BẮT BUỘC (BHYT) |
| MA-LT-A15 | R16 | Tỷ lệ chỉ số LIS có mã 7 số QĐ 1227; LOINC lưu kèm; đơn vị khớp | Truy vấn, tỷ lệ % | BẮT BUỘC (XML4) / BẮT BUỘC? |
| MA-LT-A16 | R17 | Màn hình khám cơ quan chọn được thuật ngữ có mã; xuất CV 365 thấy `VNCODE`, `SNOMED` có giá trị | Tệp JSON/XML xuất | BẮT BUỘC? |
| MA-LT-A17 | R18 | Hỏi giấy phép SNOMED CT/LOINC; sản phẩm có phân phối tệp đầy đủ không | Văn bản trả lời, hợp đồng | NÊN |
| MA-LT-A18 | R19 | Xuất 1 HSBA theo CV 365: `maicd` có chấm, ≤ 7; `machiso` là mã QĐ 1227; `mathuocvattu_byt` không phải mã nội bộ | Tệp xuất + kết quả validate | BẮT BUỘC? |
| MA-LT-A19 | R20 | Tài liệu chào bán có ghi "bắt buộc FHIR theo QĐ 2146" không (sai căn cứ); nếu có FHIR: 4.0.1, CapabilityStatement | Tài liệu, endpoint `/metadata` | NÊN |
| MA-LT-A20 | R21 | RIS-PACS nhận order HL7/MWL; lưu DICOM gốc; xuất CD/DVD kèm viewer hoặc link web | Log HL7, DICOM conformance statement | BẮT BUỘC? (nếu khai mức TT 54) |
| MA-LT-A21 | R21 | LIS kết nối 2 chiều máy xét nghiệm, nhận chỉ định HIS, đồng bộ kết quả | Danh sách máy đã kết nối, log | BẮT BUỘC? (nếu khai mức TT 54) |
| MA-LT-A22 | R23 | (Khách hàng trực thuộc BYT) tài liệu ánh xạ vào Khung kiến trúc số 2146; kết nối LGSP | Tài liệu kiến trúc | BẮT BUỘC? |
| MA-LT-A23 | R24 | Lớp tích hợp có phiên bản hợp đồng dữ liệu, thêm adapter không sửa lõi | Tài liệu kiến trúc, mã nguồn | NÊN |
| MA-LT-A24 | R26 | Có quyết định xác định mức CNTT theo TT 54; ma trận đáp ứng tiêu chí của vendor | Quyết định, báo cáo gửi cấp trên | BẮT BUỘC? |
| MA-LT-A25 | R09 | Có biên bản nạp danh mục (nguồn, hash, số dòng, lỗi) cho mỗi lần cập nhật | Biên bản | NÊN |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |
|---|---|---|---|
| 27/02/2018 | TT 54 có hiệu lực (tiêu chí HL7/DICOM cho RIS-PACS) | Cơ sở KCB tự xác định mức | Đã qua |
| 18/10/2024 | TT 23 có HL; TT 43/2013, TT 21/2017 hết HL | Cơ sở KCB, vendor | Đã qua |
| 11/04/2025 | QĐ 1227 mã chỉ số CLS | Mọi cơ sở KCB | Đã qua |
| 06/06/2025 | CV 365 (schema `HoSoBenhAn`); tiêu chí EMR TT 54 hết HL | Cơ sở có EMR, vendor | Đã qua |
| 25/07, 04/08, 04/09/2025 | Thuật ngữ lâm sàng Đợt 1, 2, 3 | Mọi cơ sở KCB | Đã qua |
| 01/06/2026 | Ký số tổ chức trên phiếu hẹn/phiếu chuyển điện tử; Q87.11 → Q87.1 | Cơ sở KCB BHYT | Đã qua |
| 23/06/2026 | QĐ 1849 có HL; Hướng dẫn mã hóa QĐ 4469 hết HL | Cơ sở KCB, NVYT | Đã qua |
| 01/07/2026 | ICD-10 TT 06 áp dụng (theo ngày kết thúc lượt); TT 25 Đ2, Đ3 có HL | Mọi cơ sở KCB; BHXH cập nhật Cổng | Đã qua |
| 10/07/2026 | QĐ 2113 Khung KT dữ liệu, từ điển dữ liệu BYT 1.0 | Đơn vị thuộc BYT (suy luận) | Đã qua |
| 15/07/2026 | QĐ 2146 Khung kiến trúc số BYT | Đơn vị thuộc, trực thuộc BYT; TTYQG | Đã qua |
| 15/08/2026 | TT 25 có HL chung | — | Đã qua |
| 2026 (kế hoạch) | QCVN cấu trúc thông điệp CSDL QG về y tế | BYT | Đang chờ |
| 2026–2027 | Từ điển dữ liệu ngành y tế | TTYQG | Đang chờ |
| **31/12/2027** | Hết PL 01 TT 23; hết thời gian giữ kỹ thuật đã duyệt không cần điều chỉnh GPHĐ | Mọi cơ sở KCB | Sắp tới |
| **01/01/2028** | Áp dụng PL 02 TT 23 | Mọi cơ sở KCB, vendor; BHXH (mã DVKT, chưa có văn bản) | Sắp tới |
| 31/12/2029 | Hết thời gian điều dưỡng làm kỹ thuật "*" theo văn bản cho phép | Cơ sở KCB | Sắp tới |
| 2030 | Mục tiêu lộ trình FHIR R4, DICOM, ICD-11, SNOMED CT, LOINC | BYT, TTYQG | Sắp tới |

## 6. Bẫy trích dẫn và chuỗi thay thế

**Chuỗi thay thế**

| Cũ | Mới | Từ ngày | Ghi chú |
|---|---|---|---|
| Danh mục ICD-10 QĐ 4469/QĐ-BYT (2020) | Phụ lục TT 06/2026 | 01/07/2026 | TT 06 Đ6 k1; không có câu "bãi bỏ QĐ 4469" |
| Hướng dẫn mã hóa ICD-10 của QĐ 4469 | QĐ 1849/QĐ-BYT | 23/06/2026 | QĐ 1849 Đ2 |
| Q87.11 (PL 3 TT 01/2025) | Q87.1 | 01/06/2026 | TT 06 Đ5 k3 |
| TT 43/2013, TT 21/2017 | TT 23/2024 PL 01 | 18/10/2024 | STT cũ vẫn là mã kỹ thuật (TT 25 Đ3 k2) |
| TT 23 PL 01 "đến 30/06/2026", PL 02 "từ 01/07/2026" | PL 01 đến 31/12/2027; PL 02 từ 01/01/2028 | 01/07/2026 | TT 25 Đ3 k1, k4, k5 |
| KT CPĐT BYT 2.0 (QĐ 6085/2019) → 2.1 (QĐ 1928/2023) + QĐ 4152/2024 | Khung kiến trúc số BYT (QĐ 2146/2026) | 15/07/2026 | Không có điều khoản bãi bỏ; QĐ 2146 gọi là "kiến trúc hiện tại" |
| Tiêu chí EMR TT 54/2017 (gồm TC 144 HL7 CDA/CCD) | TT 13/2025 + CV 365 | 06/06/2025 | Tiêu chí HIS, LIS, RIS-PACS, phi chức năng còn HL |

**Bẫy trích dẫn**

1. **FHIR/DICOM**: QĐ 2146 nhắc HL7 FHIR R4 / DICOM 3.0 trong lộ trình đến 2030, áp cho đơn vị trực thuộc BYT; không văn bản nào buộc cơ sở KCB nói chung dùng FHIR/DICOM. Sai cả hai chiều: "QĐ 2146 bắt buộc FHIR" và "không văn bản nào nhắc FHIR".
2. `ytesovietnam.vn` và VN Core FHIR IG không phải nguồn chính thức; IG tự ghi là bản nháp; con số 16.052 mã không khớp 15.844 dòng gốc.
3. Mọi tài liệu trước 07/2026 nói "PL 02 TT 23 áp dụng từ 01/7/2026" là lỗi thời.
4. TT 25/2026 hiệu lực chung 15/08/2026 nhưng Đ2, Đ3 từ 01/07/2026.
5. TT 06 chứa hai quy định không về ICD (ký số phiếu hẹn/chuyển; Q87.11).
6. Cột 26 không chỉ cấm ở bệnh chính; cột 27 chỉ dùng cho nguyên nhân tử vong. Tóm tắt "cột 24–29 chỉ áp cho bệnh chính" là đọc thiếu.
7. XML1 bản 2023 vẫn dẫn QĐ 4469; từ 01/07/2026 áp TT 06.
8. TT 54/2017 chỉ có căn cứ NĐ 75/2017, không dẫn Luật CNTT → lập luận "TT 54 hết HL theo Luật CNTT" không đứng. Ngày hiệu lực là **27/02/2018** (Đ6 bản gốc), không phải 26/02/2018 như một số tài liệu.
9. TT 54 không nêu phiên bản HL7/DICOM; "ISO 12052:2026" trong QĐ 2146 chưa xác minh, đừng chép vào hợp đồng như chuẩn đã kiểm.
10. Hai nhóm "danh mục mã dùng chung" khác nhau: (a) bộ mã BHYT (QĐ 7603 → 3276, 2010, 1804…; BHYT-DATA); (b) danh mục lâm sàng của Cục QLKCB (QĐ 1227, 2427, 2493, 2805), mã 7 số gắn LOINC/SNOMED. Đừng trộn.
11. QĐ 2113 (khung v1.0, 10/07/2026) và danh mục dữ liệu chủ "chưa hoàn thiện" không mâu thuẫn: QĐ 2146 còn xếp từ điển dữ liệu ngành 2026–2027 và danh mục dùng chung 2026–2030 (suy luận, chưa đọc QĐ 2113).
12. Hai số "2113" năm 2026: QĐ 2113/QĐ-BKHCN (14/04/2026, sở hữu trí tuệ) khác QĐ 2113/QĐ-BYT. Luôn ghi cơ quan ban hành.
13. Người ký: QĐ 2146 và các QĐ thuật ngữ do TT Nguyễn Tri Thức ký; QĐ 1849 do TTTT Vũ Mạnh Hà; TT 06, TT 23 do TT Trần Văn Thuấn.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. QĐ 2113/QĐ-BYT: chưa có toàn văn (phạm vi, nội dung từ điển dữ liệu, có nhắc FHIR/HL7 không). Thử TTYQG, Cổng TTĐT BYT.
2. QĐ 1849 PL2–PL5 chưa đọc: cần cho R04 (mã hủy/mã mới), R05 (†/*, mã bổ sung), R06 (chọn nguyên nhân tử vong gốc).
3. Cổng giám định BHXH chặn cột 26/27 ở `MA_BENH_KT` hay chỉ `MA_BENH_CHINH`? Hỏi BHXH VN (liên quan BHYT-DATA-R20).
4. ICD có chấm hay không chấm trong XML BHYT: CV 365 ví dụ có chấm; đối chiếu XSD Cổng (BHYT-DATA).
5. TT 06 có ràng buộc cơ sở không ký hợp đồng BHYT không (căn cứ chỉ Luật BHYT, NĐ 188): cần luật sư.
6. Mã kỹ thuật chính thức PL 02 TT 23, mã DVKT BHYT và giá sau 01/01/2028: chưa có văn bản. Hỏi Cục QLKCB, Vụ BHYT.
7. `dmkt.kcb.vn` (trả về rỗng) chưa kiểm tra được.
8. QĐ 7713/2016, QĐ 3926/2017: bản gốc, phiên bản HL7 v2.x, hiệu lực chưa xác minh.
9. Giấy phép SNOMED CT, LOINC: VN có là thành viên SNOMED International; vendor thương mại có cần Affiliate License. Cần luật sư sở hữu trí tuệ + hỏi Cục QLKCB.
10. Quan hệ `VNCODE` (CV 365) với mã dùng chung 7 số: hỏi TTYQG/Cục QLKCB.
11. QĐ 1227 các đợt sau; phụ lục QĐ 2427, 2805 và PL CĐHA, hóa sinh, vi sinh của QĐ 1227 chưa đọc.
12. QCVN cấu trúc thông điệp CSDL QG về y tế: chưa ban hành đến 05/10/2026.
13. Thông tư thay TT 54 (dự thảo): chưa ban hành; nếu ban hành có thể đặt chuẩn HL7/DICOM/FHIR cụ thể.
14. TT 39/2017/TT-BTTTT: quan hệ với Luật CĐS và các TT BKHCN 2026 chưa xác minh.
15. TCVN 13239:2024 chưa xác định tên; danh mục ICS 35.240.80 chưa rà hết.
16. Văn bản gốc danh mục mã bệnh YHCT hiện hành (`MA_BENH_YHCT`) chưa xác định.
17. TT 54: nghĩa vụ báo cáo hằng năm (theo tóm tắt luatvietnam) và đơn vị nhận sau khi Cục CNTT BYT tổ chức lại: chưa đối chiếu điều khoản.
