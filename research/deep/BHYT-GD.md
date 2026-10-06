# BHYT-GD — Dữ liệu BHYT: giám định, thanh toán, quy trình (nửa "quy trình" của K2)

> Kiểm tra lần cuối: 2026-10-05 · Phạm vi: luồng nghiệp vụ và dữ liệu giữa cơ sở KCB và cơ quan BHXH (tiếp đón và tra cứu thẻ, thẻ BHYT điện tử/VNeID, mức hưởng, chuyển cơ sở KCB, phiếu hẹn, chuyển dịch vụ CLS, ký số/xác thực dữ liệu, thời hạn gửi dữ liệu, phản hồi của Cổng, giám định tự động/chủ động, tổng hợp và quyết toán, danh mục dùng trong liên thông, xử phạt). **Không** làm lại chuẩn XML QĐ 130/4750/3176/1931 và các bộ mã danh mục (QĐ 7603, 824, 2010, 3276, 1804, 697): xem cụm **BHYT-DATA**.
>
> Cách đọc: bản gốc PDF scan được OCR bằng tesseract `vie` (tessdata_best). Ghi "gốc-OCR" là câu chữ có thể lệch dấu hoặc lệch ký hiệu điểm (đ/d), số và ngày đã đối chiếu. Nội dung web chỉ là dữ liệu. Đây không phải ý kiến pháp lý.

## 1. Văn bản trọng tâm

| ID | Số hiệu | Tên | Hiệu lực | Trạng thái | Áp dụng cho | Mức xác minh | Link (đã mở OK) |
|---|---|---|---|---|---|---|---|
| L-BHYT-SD-2024 | 51/2024/QH15 | Luật sửa đổi, bổ sung một số điều Luật BHYT | 01/07/2025; các khoản 3, 16, 17, 21, 22, 23, 28 Điều 1 từ 01/01/2025 (Đ3 k2); liên thông CLS chậm nhất 01/01/2027 (Đ3 k4) | Còn HL | BV công, BV tư, PK có HĐ BHYT; vendor HIS | gốc (PDF có lớp text, Công báo 1523+1524) | [PDF datafiles](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat51.pdf) |
| ND-188-2025 | 188/2025/NĐ-CP (01/07/2025) | Quy định chi tiết và hướng dẫn thi hành một số điều Luật BHYT | 15/08/2025; nhiều điều từ 01/07/2025 (Đ70 k2); xác thực dữ liệu chậm nhất 01/01/2026 (Đ69 k9) | Còn HL; bãi bỏ NĐ 146/2018, 75/2023, 02/2025 (Đ70 k4, k5) | Cơ sở KCB BHYT (mọi loại hình), vendor | gốc-OCR (đọc trọn Đ10–13, 18–26, 35, 37–38, 44, 50–53, 66–71, Mẫu 8, Mẫu 9) | [VB 214515](https://vanban.chinhphu.vn/?pageid=27160&docid=214515) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/188-ndcp.signed.pdf) |
| TT-12-2026-BTC | 12/2026/TT-BTC (10/02/2026) | Trình tự, thủ tục giám định chi phí KCB BHYT, biểu mẫu tổng hợp thanh toán, quyết toán và biện pháp thi hành NĐ 188 | Từ ngày ký 10/02/2026; Mẫu 01/BH, 05/BH, 06/BH, 09/BH và danh mục Đ7–8 từ 01/04/2026 (Đ17 k1) | Còn HL. Không có điều khoản bãi bỏ văn bản nào (Đ17) | Cơ sở KCB có HĐ BHYT; BHXH | gốc-OCR (đọc trọn Đ1–17, Phụ lục I, liệt kê Phụ lục II) | [VB 216997](https://vanban.chinhphu.vn/?pageid=27160&docid=216997) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-btc.pdf) |
| TT-48-2017-BYT | 48/2017/TT-BYT (28/12/2017) | Trích chuyển dữ liệu điện tử trong quản lý và thanh toán chi phí KCB BHYT | 01/03/2018 (Đ14) | Còn HL; được TT 12/2026 Đ4 k2 và Đ9 k1 viện dẫn trực tiếp; có dự thảo thay (DT-TT48) | Cơ sở KCB BHYT, vendor | gốc-OCR (bản có chữ ký số "VOffice Bộ Y tế" ngày 29/12/2017, đăng lại trên trang TTYT huyện Ninh Sơn; chưa thấy trên datafiles) | [PDF bản ký số do TTYT Ninh Sơn đăng](http://trungtamyteninhson.vn/wp-content/uploads/2025/10/TT48.pdf) |
| DT-TT48 | Dự thảo TT quy định ứng dụng CNTT, chuyển đổi số, chia sẻ dữ liệu trong lĩnh vực BHYT (thay TT 48/2017) | — | Dự kiến 01/01/2027; góp ý đến 07/10/2026 | Dự thảo | Cơ sở KCB, BHXH, vendor | thứ cấp (chưa tìm được toàn văn dự thảo) | [vtv](https://vtv.vn/de-xuat-co-so-y-te-phai-gui-du-lieu-bhyt-trong-vong-3-gio-sau-kham-cham-nhieu-lan-co-the-bi-xu-phat-100261001082022915.htm) · [vietnamplus](https://www.vietnamplus.vn/co-so-kham-chua-benh-gui-du-lieu-dien-tu-cham-co-the-bi-xu-phat-hanh-chinh-post1139262.vnp) · [baohaiphong](https://baohaiphong.vn/de-xuat-phat-co-so-kham-chua-benh-cham-gui-du-lieu-bao-hiem-y-te-554711.html) |
| ND-90-2026 | 90/2026/NĐ-CP (30/03/2026) | Xử phạt VPHC trong lĩnh vực y tế (Mục BHYT: Đ81–95) | 15/05/2026 | Còn HL; thay NĐ 117/2020 | Cơ sở KCB, cá nhân người hành nghề, BHXH | gốc-OCR (đọc Đ4, Đ84–95, Đ111) | [VB 217386](https://vanban.chinhphu.vn/?pageid=27160&docid=217386) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| TT-01-2025-BYT | 01/2025/TT-BYT | Hướng dẫn Luật BHYT (lưu trú, đăng ký ban đầu, chuyển người bệnh, phiếu hẹn, phiếu chuyển) | 01/01/2025 (Đ15 k1) | Còn HL; sửa bởi TT 06/2026 (Đ5 k2) | BV, PK BHYT | gốc (PDF có text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/01-byt.pdf) |
| TT-06-2026-BYT | 06/2026/TT-BYT (02/04/2026) | Mã hóa bệnh tật, nguyên nhân tử vong theo ICD-10 (Đ5 k2 sửa mẫu phiếu của TT 01) | 01/07/2026; Đ5 k2, k3 từ 01/06/2026 | Còn HL | BV, PK | gốc (PDF có text) | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf) |
| ND-164-2025 | 164/2025/NĐ-CP (29/06/2025) | Giao dịch điện tử lĩnh vực BHXH và CSDL quốc gia về bảo hiểm | 01/07/2025 (Đ27 k1) | Còn HL; NĐ 43/2021 hết HL; không áp dụng NĐ 166/2016 với BHXH bắt buộc, tự nguyện (Đ27 k3) | BYT/cơ sở KCB chia sẻ dữ liệu (Đ25 k2) | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/164-cp.signed.pdf) |
| **TT-09-2026-BTC** (mới) | 09/2026/TT-BTC (03/02/2026) | Tạo lập, sử dụng sổ BHXH, thẻ BHYT bản điện tử | Từ ngày ký | Còn HL (theo tin BHXH VN) | Cơ sở KCB (tiếp nhận thẻ điện tử) | thứ cấp (chưa mở được bản gốc; datafiles đoán đường dẫn 404) | [tin BHXH VN](https://baohiemxahoi.gov.vn/tintuc/Pages/chuyen-doi-so.aspx?ItemID=26155&CateID=0) · [xaydungchinhsach](https://xaydungchinhsach.chinhphu.vn/su-dung-so-bhxh-ban-dien-tu-de-giai-quyet-cac-che-do-bhxh-bao-hiem-that-nghiep-119260209100523582.htm) |
| QD-2555-2025-BYT | 2555/QĐ-BYT (12/08/2025) | Thủ tục hành chính KCB BHYT (xuất trình VNeID mức 2, VssID, căn cước) | 15/08/2025 | Còn HL (?) | Cơ sở KCB | thứ cấp | [tin BHXH VN](https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=25292&CateID=169) |
| **HD-BHXH-PL01-3176** (mới) | Phụ lục 01 "Hướng dẫn liên thông dữ liệu theo QĐ 3176/QĐ-BYT", kèm Công văn số …/BHXH-CNTT năm 2026 (số và ngày để trống trong bản đăng) | Hướng dẫn kỹ thuật: đăng ký chứng thư số trên Cổng, API token, check-in, gửi XML, ký `CHUKYDONVI` SHA256 | Ký số 07/01/2026 (theo tên file) | Hướng dẫn kỹ thuật, không phải VBQPPL | Vendor HIS | thứ cấp (bản do UBND xã Khánh Cường, Quảng Ngãi đăng lại) | [PDF](https://khanhcuong.quangngai.gov.vn/upload/2007018/20260128/PL01_li%C3%AAn%20th%C3%B4ng%20d%E1%BB%AF%20li%E1%BB%87u_3176_k%C3%BD%20s%E1%BB%91_07012026%20(1).pdf) |
| DT-BTC-CONG | Dự thảo TT BTC về Cổng tiếp nhận dữ liệu (hướng dẫn điểm d k2 Đ71 NĐ 188) | — | — | **Đã được hấp thụ vào TT 12/2026/TT-BTC** (Đ1 k1 điểm a viện dẫn đúng điểm d k2 Đ71; Đ2–4 khớp nội dung dự thảo: cổng gdbhyt, tài khoản quản trị, phản hồi tự động) | — | gốc-OCR (qua TT 12) + thứ cấp (dự thảo) | [baochinhphu (dự thảo)](https://baochinhphu.vn/de-xuat-quy-dinh-ve-cong-tiep-nhan-du-lieu-thuoc-he-thong-thong-tin-giam-dinh-bhyt-cua-bhxh-viet-nam-102251204180503834.htm) |

Dẫn chiếu sang cụm khác: chuẩn XML 130/4750/3176/1931, mã MUC_HUONG, MA_LOAI_KCB, mã khoa, mã đối tượng, bảng kê 01/KBCB (QĐ 697) → **BHYT-DATA**. Liên thông CLS chi tiết (DT-CLS-LT, LIS/PACS) → **K7**. Ký số, HSBA → **K1**. Hóa đơn điện tử (NĐ 254/2026) → **K11**. VNeID, Sổ SKĐT → **K4**.

## 2. Yêu cầu pháp lý → yêu cầu phần mềm

### A. Tiếp đón, thẻ BHYT, tra cứu

#### BHYT-GD-R01 — Chấp nhận mọi hình thức xuất trình thẻ, không đòi thẻ giấy
- **Căn cứ**: Luật 51/2024 Điều 1 k14 (sửa Đ16 k1 Luật BHYT): thẻ BHYT "được cấp bằng bản điện tử, bản giấy và có giá trị pháp lý như nhau". NĐ 188 Đ11 k1: BHXH cấp thẻ bản điện tử, bản giấy chỉ khi người tham gia đề nghị. NĐ 188 Đ37 k1: xuất trình bằng (a) căn cước/CCCD/VNeID mức 2 đã tích hợp thẻ, hoặc (b) thẻ điện tử hoặc giấy; thẻ chưa có ảnh thì kèm giấy tờ nhân thân. Đ37 k2: trẻ dưới 6 tuổi chỉ cần thẻ hoặc mã số BHYT, chưa có thẻ thì giấy chứng sinh. TT 09/2026/TT-BTC (thứ cấp): cơ sở KCB không được yêu cầu thẻ giấy khi người bệnh dùng thẻ điện tử.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: Đ37 từ 15/08/2025 (không thuộc danh sách Đ70 k2)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: màn hình tiếp đón nhận định danh bằng số định danh cá nhân (quét QR căn cước), mã số BHYT, hoặc dữ liệu thẻ từ VNeID/VssID; không có trường "bắt buộc ảnh/scan thẻ giấy"; lưu `hinh_thuc_xuat_trinh` (CCCD | VNeID | VssID | thẻ giấy | mã số | giấy chứng sinh | giấy hẹn trả thẻ); nhánh riêng cho trẻ dưới 6 tuổi và người hiến bộ phận cơ thể (Đ37 k4).
- **Ghi chú / bẫy**: NĐ 188 Đ10 k3: thông tin thẻ đồng bộ theo mã số BHYT **và** số căn cước, nên khóa tra cứu có thể là cả hai. Đối tượng quân đội, công an (điểm a–d k3 Đ12 Luật) chưa có thông tin thẻ trên hệ thống thì vẫn phải xuất trình thẻ giấy (Đ37 k1 b), đừng chặn cứng "chỉ thẻ điện tử". CV 168/BHXH-QLT (thẻ giấy chỉ cấp 3 trường hợp từ 01/06/2025) đã bị NĐ 188 Đ11 thay về nội dung.

#### BHYT-GD-R02 — Tra cứu thẻ trên Cổng tiếp nhận dữ liệu và lưu kết quả
- **Căn cứ**: TT 12/2026 Đ4 k1: tra cứu thông tin thẻ, lịch sử KCB "ngay khi người bệnh đến khám bệnh, trong quá trình điều trị hoặc khi kết thúc lần khám bệnh, chữa bệnh". Đ4 k2: Cổng phản hồi tự động thông tin thẻ, số tiền cùng chi trả lũy kế trong năm tài chính, thẻ bị thu hồi/tạm giữ/tạm khóa, lịch sử KCB. TT 48/2017 Đ13 k2 (tra cứu thẻ là trách nhiệm cơ sở); Đ6 k2 điểm a (lịch sử KCB tối thiểu 06 tháng: thời gian, bệnh chính, bệnh kèm ICD-10/YHCT, tình trạng). TT 12 Đ2 k1: Cổng tại `https://gdbhyt.baohiemxahoi.gov.vn`.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 10/02/2026 (TT 12); TT 48 từ 01/03/2018
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: gọi tra cứu thẻ ở 3 thời điểm (tiếp đón, trong điều trị khi cần, trước khi kết thúc lượt hoặc ra viện); lưu nguyên phản hồi (mã kết quả, thời điểm, payload) gắn với lượt KCB; cảnh báo chặn khi thẻ bị thu hồi/tạm khóa; hiển thị lịch sử KCB cho bác sĩ.
- **Ghi chú / bẫy**: Dự thảo cổng (thứ cấp) nêu "6 lần khám gần nhất trong 12 tháng", nhưng TT 12 bản gốc không ghi con số này mà dẫn sang TT 48 Đ6 k2a (06 tháng). Phải theo bản gốc.

#### BHYT-GD-R03 — Quy trình dự phòng khi VNeID/VssID/Cổng lỗi
- **Căn cứ**: NĐ 188 Đ38 k2: không xuất trình được thẻ điện tử do lỗi VNeID/VssID/Internet thì (a) người bệnh cung cấp mã số thẻ; Cổng không tra cứu được thì cơ sở ghi nhận mã số, **vẫn tiếp nhận** và tra cứu lại sau; (b) đến khi kết thúc lượt hoặc ra viện mà hệ thống vẫn lỗi thì gửi BHXH toàn bộ hồ sơ KCB, thông tin liên hệ người bệnh "kèm ảnh màn hình tra cứu".
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trạng thái lượt KCB `the_chua_xac_minh`; hàng đợi tra cứu lại tự động; lưu bằng chứng lỗi (ảnh chụp màn hình hoặc log có timestamp, mã lỗi); xuất gói hồ sơ cho BHXH khi ra viện mà thẻ vẫn chưa xác minh.
- **Ghi chú / bẫy**: không được từ chối tiếp nhận chỉ vì Cổng lỗi.

#### BHYT-GD-R04 — Không đặt thêm thủ tục; sao chụp giấy tờ phải có đồng ý
- **Căn cứ**: NĐ 188 Đ38 k3: cơ sở KCB và BHXH "không được quy định thêm thủ tục" ngoài Điều 38; nếu cần sao chụp thẻ, giấy tờ thì cơ sở tự sao chụp sau khi người bệnh hoặc người giám hộ đồng ý, không yêu cầu người bệnh tự sao chụp hoặc trả phí. NĐ 90/2026 Đ95 k1 a (gây khó khăn, cản trở KCB BHYT: 500.000–1.000.000 đ cá nhân).
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: chức năng scan giấy tờ phải là tùy chọn, có trường ghi nhận đồng ý (người đồng ý, thời điểm); không thu phí sao chụp trong bảng giá.

#### BHYT-GD-R05 — Mã thẻ tạm cho trẻ dưới 6 tuổi và người hiến bộ phận cơ thể
- **Căn cứ**: NĐ 188 Đ50 k1 a: dùng chức năng tra cứu mã thẻ BHYT tạm thời trên Cổng; chưa có thì nhập đủ thông tin trên Cổng để Cổng cấp tự động mã thẻ tạm. Đ37 k2: trẻ vừa sinh, cha mẹ hoặc thân nhân ký xác nhận trên HSBA.
- **Áp dụng cho**: cơ sở có khám nhi, sản, ghép tạng · **Hiệu lực**: 01/07/2025 (Đ50 thuộc Đ70 k2)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: luồng lấy hoặc đề nghị cấp mã thẻ tạm; liên kết mã thẻ tạm với mã thẻ chính thức khi có; trường xác nhận của cha/mẹ trên HSBA của trẻ sơ sinh.

#### BHYT-GD-R06 — Xuất trình thẻ muộn và cấp cứu
- **Căn cứ**: NĐ 188 Đ38 k1 và Đ50 k6: xuất trình muộn thì quỹ chỉ thanh toán từ thời điểm xuất trình (trừ cấp cứu); phần trước đó thanh toán trực tiếp (Đ55–57). Luật 51 Điều 1 k23 (Đ28 k1) và NĐ 188 Đ37 k5: cấp cứu thì xuất trình trước khi kết thúc đợt điều trị.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 01/01/2025 (Đ28 Luật), 15/08/2025 (NĐ 188 Đ37–38)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu `thoi_diem_xuat_trinh_the`; tách chi phí trước và sau mốc này (trừ ca cấp cứu); in chứng từ cho phần người bệnh tự chi trả để làm hồ sơ thanh toán trực tiếp.

#### BHYT-GD-R07 — Kiểm tra lại quyền lợi, mức hưởng trước khi kết thúc lượt
- **Căn cứ**: NĐ 188 Đ21 k1: nhiều mức hưởng thì hưởng mức cao nhất; k2: mức hưởng mới tính từ thời điểm thẻ mới có giá trị; cơ sở "có trách nhiệm kiểm tra quyền lợi, mức hưởng ... trước khi kết thúc lượt khám bệnh, chữa bệnh, ra viện". NĐ 90 Đ90 (xác định quyền lợi không đúng thông tin trên thẻ: 200.000 đ đến 7.000.000 đ theo giá trị vi phạm, mức cá nhân).
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bắt buộc tra cứu lại thẻ (R02) trước khi chốt ra viện hoặc thanh toán; nếu mức hưởng đổi trong đợt điều trị nội trú thì chia giai đoạn theo ngày hiệu lực thẻ mới; chọn mức hưởng cao nhất khi có nhiều thẻ (XML cho phép nhiều thẻ trong một hồ sơ, TT 48 Đ4 k3 b).

#### BHYT-GD-R08 — Thẻ hết hạn khi đang điều trị
- **Căn cứ**: NĐ 188 Đ50 k4: thẻ còn hạn khi vào, hết hạn khi đang điều trị nội trú, ban ngày hoặc ngoại trú thì quỹ vẫn thanh toán đến khi ra viện, tối đa 15 ngày kể từ ngày thẻ hết hạn.
- **Áp dụng cho**: cơ sở có điều trị nội trú, ban ngày, ngoại trú · **Hiệu lực**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tính ngày được hưởng = min(ngày ra, ngày hết hạn thẻ + 15 ngày); cảnh báo khi vượt; phần vượt chuyển sang người bệnh tự trả.

#### BHYT-GD-R09 — Miễn cùng chi trả (5 năm liên tục và vượt 6 tháng lương cơ sở)
- **Căn cứ**: Luật 51 Điều 1 k17 (Đ22 k1 d Luật BHYT). NĐ 188 Đ18 k2: hưởng 100% từ thời điểm đồng thời đủ hai điều kiện đến hết 31/12; điểm b: BHXH tổng hợp số tiền cùng chi trả lũy kế và thời điểm đủ 5 năm, công bố trên Cổng, cơ sở KCB căn cứ đó để xác định thời điểm miễn; điểm c: công thức quy đổi khi lương cơ sở đổi trong năm. TT 12 Đ4 k2 (Cổng phản hồi số lũy kế).
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 01/07/2025 (Đ18 thuộc Đ70 k2)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lấy số cùng chi trả lũy kế từ Cổng tại tiếp đón; cộng dồn chi phí cùng chi trả trong lượt hiện tại; tự động chuyển mức hưởng sang 100% từ thời điểm vượt ngưỡng, kể cả giữa lượt; lượt vắt qua 01/01 thì tính theo từng năm.
- **Ghi chú / bẫy**: Luật mới dùng "mức tham chiếu"; Luật 51 Đ3 k5 b: mức tham chiếu áp dụng theo mức lương cơ sở cho đến khi Chính phủ quyết định khác. Tham số hóa, đừng hard-code.

#### BHYT-GD-R10 — Mức hưởng theo cấp chuyên môn kỹ thuật và lộ trình 2026
- **Căn cứ**: Luật 51 Điều 1 k17 (Đ22 k1, k3, k4, k5 Luật BHYT; hiệu lực 01/01/2025 theo Đ3 k2). NĐ 188 Đ19: từ 01/01/2025 ngoại trú tại cơ sở cấp cơ bản dưới 50 điểm hoặc tạm xếp cấp cơ bản được 100% mức hưởng; **từ 01/07/2026** được 50% mức hưởng khi ngoại trú tại (k2) cơ sở cấp cơ bản 50 đến dưới 70 điểm, (k3) cơ sở cấp cơ bản trước 01/01/2025 là tuyến tỉnh/TW, (k4) cơ sở cấp chuyên sâu trước 01/01/2025 là tuyến tỉnh. TT 01/2025 Đ4: trường hợp lưu trú (dưới 30 ngày, có khai báo lưu trú) và giấy tờ phải xuất trình, gồm thông tin lưu trú trên VNeID mức 2. Luật Đ22 k5: cấp cứu 100% tại bất kỳ cơ sở nào.
- **Áp dụng cho**: mọi cơ sở KCB BHYT (đặc biệt BV tỉnh cũ, BV tư cấp cơ bản/chuyên sâu) · **Hiệu lực**: 01/01/2025; mốc 01/07/2026 [QUA]
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấu hình theo cơ sở: cấp CMKT (ban đầu/cơ bản/chuyên sâu), số điểm xếp cấp, cờ "trước 01/01/2025 là tuyến huyện/tỉnh/TW"; bảng quy tắc tỷ lệ % mức hưởng theo (cấp, nội/ngoại trú, đúng/không đúng nơi đăng ký, lý do: cấp cứu, chuyển đúng trình tự, lưu trú, tạm trú, bệnh hiếm theo Đ22 k4 a); quy tắc có ngày hiệu lực để thay đổi mà không phải sửa code.
- **Ghi chú / bẫy**: cách mã hóa MUC_HUONG, MA_LYDO_VVIEN trong XML thuộc **BHYT-DATA** (QĐ 1931/2026 sửa MUC_HUONG từ 01/07/2026). NĐ 188 Đ35 k2 e: cơ sở phải công khai kết quả xếp cấp kèm số điểm trên website và tại nơi đón tiếp.

#### BHYT-GD-R11 — Phiếu chuyển cơ sở KCB (thay "giấy chuyển tuyến")
- **Căn cứ**: Luật 51 Điều 1 k22–23 (Đ27, Đ28 k3 Luật BHYT). TT 01/2025 Đ9 (các trường hợp chuyển đúng trình tự), Đ12 k1: Phiếu chuyển theo Phụ lục VI, bản giấy hoặc điện tử, giá trị 10 ngày làm việc kể từ ngày ký; k2: bệnh thuộc Phụ lục III giá trị 01 năm, hết hạn khi đang điều trị thì dùng đến hết đợt; k4: nhiều đợt điều trị thì từ đợt 2 phải có phiếu hẹn; k5: chỉ cần phiếu của cơ sở trực tiếp chuyển. Ghi chú Phụ lục VI: phiếu hiển thị trên VNeID và ký số đầy đủ có giá trị tương đương bản giấy. TT 06/2026 Đ5 k2: "(Ký tên, đóng dấu)" trên mẫu phiếu chuyển được thay bằng ký số xác thực của cơ sở với bản điện tử, **từ 01/06/2026**.
- **Áp dụng cho**: BV, PK BHYT · **Hiệu lực**: 01/01/2025; ký số cơ sở 01/06/2026 [QUA]
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phát hành phiếu chuyển điện tử theo Phụ lục VI có chữ ký số người ký và chữ ký số cơ sở; tính `han_su_dung` (10 ngày làm việc hoặc 1 năm theo mã bệnh Phụ lục III, có lịch ngày nghỉ); tiếp nhận phiếu đến (ghi số phiếu, mã cơ sở chuyển, ngày ký) và kiểm tra còn hạn; dữ liệu đẩy sang XML giấy chuyển tuyến (XML13, xem BHYT-DATA) và hiển thị trên VNeID qua luồng của K4.
- **Ghi chú / bẫy**: TT 01 đọc riêng vẫn ghi "đóng dấu" (bẫy, xem mục 6). Thuật ngữ đã đổi từ "chuyển tuyến" sang "chuyển cơ sở KCB", nhưng tên bảng XML vẫn dùng "giấy chuyển tuyến".

#### BHYT-GD-R12 — Phiếu hẹn khám lại
- **Căn cứ**: Luật 51 Điều 1 k23 (Đ28 k2). TT 01/2025 Đ11: ghi trên Phiếu hẹn (Phụ lục V) hoặc trong đơn thuốc, giấy ra viện; bản điện tử có chữ ký số của bác sĩ điều trị; mỗi phiếu dùng 01 lần; ghi vào sổ hẹn hoặc dữ liệu điện tử để đối chiếu; chỉ hẹn khám lại một lần sau khi kết thúc một đợt điều trị (k5). TT 06/2026 Đ5 k2: dấu treo trên mẫu phiếu hẹn được thay bằng ký số xác thực của cơ sở với bản điện tử, từ 01/06/2026.
- **Áp dụng cho**: BV, PK BHYT · **Hiệu lực**: 01/01/2025; 01/06/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phiếu hẹn có ID duy nhất, trạng thái `da_su_dung` (khóa sau lần dùng đầu tiên); ký số bác sĩ và cơ sở; chặn tạo phiếu hẹn thứ hai cho cùng đợt điều trị đã kết thúc; đẩy XML14 (BHYT-DATA).

#### BHYT-GD-R13 — Chuyển người bệnh hoặc mẫu bệnh phẩm để làm dịch vụ CLS
- **Căn cứ**: Luật 51 Điều 1 k25 (Đ31 k3 Luật BHYT). NĐ 188 Đ44: k1 chỉ chuyển đến cơ sở được phê duyệt đủ điều kiện; cơ sở nhận không được chuyển tiếp sang cơ sở thứ ba; k2 a: DVCLS đã được phê duyệt nhưng tạm không làm được thì điền **Mẫu số 9** (Phiếu chuyển dịch vụ CLS) và gửi BHXH danh sách DVCLS đã chuyển; k2 b: DVCLS chưa được phê duyệt thì cần hợp đồng nguyên tắc và danh sách gửi BHXH **trước khi thực hiện**; k3: cơ sở chuyển tổng hợp chi phí vào hồ sơ người bệnh; người bệnh phải trả thêm thì báo và được đồng ý trước; k4: giá thanh toán.
- **Áp dụng cho**: cơ sở chuyển và cơ sở nhận DVCLS (gồm phòng xét nghiệm tư) · **Hiệu lực**: 01/07/2025 (Đ44 thuộc Đ70 k2)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: in hoặc phát hành Mẫu số 9 (lý do: hỏng máy, thiếu hóa chất, thiếu người, khác; người bệnh hay mẫu; thông tin thẻ, MA_LOAI_KCB, chẩn đoán); nhập kết quả và giá của cơ sở thực hiện vào dòng DVKT của hồ sơ gốc; báo cáo danh sách DVCLS đã chuyển theo kỳ; ghi nhận đồng ý của người bệnh khi phát sinh chi phí ngoài.

#### BHYT-GD-R14 — Liên thông và sử dụng kết quả CLS giữa cơ sở KCB BHYT
- **Căn cứ**: Luật 51 Đ3 k4: chậm nhất **01/01/2027** thực hiện liên thông, sử dụng kết quả CLS liên thông giữa các cơ sở KCB BHYT phù hợp yêu cầu chuyên môn "theo quy định của Chính phủ". Luật 51 Điều 1 k3 (Đ6 k3): BYT quy định về CNTT, chuyển đổi số, chia sẻ dữ liệu và việc liên thông, sử dụng kết quả CLS.
- **Áp dụng cho**: mọi cơ sở KCB BHYT có CLS · **Hiệu lực**: 01/01/2027 [TỚI]
- **Mức**: BẮT BUỘC? Mốc là luật định, nhưng NĐ 188 (đã đọc) **không có điều nào** quy định chi tiết việc liên thông kết quả CLS. Dự thảo của BYT (DT-CLS-LT) vẫn đang lấy ý kiến.
- **Phần mềm phải**: (chuẩn bị) lưu kết quả CLS có định danh người bệnh, thời điểm lấy mẫu, người thực hiện, mã dịch vụ chuẩn; có khả năng nhận kết quả từ cơ sở khác và đánh dấu "kết quả liên thông, không tính phí lại". Chi tiết → **K7**.

### B. Kết nối, tài khoản, xác thực

#### BHYT-GD-R15 — Điều kiện ký hợp đồng: chuẩn kết nối, xác thực dữ liệu, kê khai HIS
- **Căn cứ**: NĐ 188 Đ22 k2: điều kiện ký HĐ là "bảo đảm tiêu chuẩn kết nối, liên thông dữ liệu khám bệnh, chữa bệnh bảo hiểm y tế với hệ thống thông tin, giám định ... theo quy định của Bộ trưởng Bộ Y tế và xác thực dữ liệu" (gốc-OCR). Đ26 k1 h: hồ sơ ký HĐ có **Bảng kê danh mục thiết bị phần mềm, phần cứng** theo **Mẫu số 8**. Mẫu 8 gồm: (I) phần cứng gồm máy chủ, máy trạm, thiết bị lưu trữ, UPS, mạng LAN, mạng Internet, khác (ký hiệu, hãng, xuất xứ, năm sản xuất, cấu hình, tình trạng); (II) HIS gồm tên phần mềm, thời điểm bắt đầu sử dụng, nhà cung cấp, nguồn gốc (thuê/mua/tự phát triển), tình trạng sử dụng. Đ68 k5 b: duy trì tiêu chuẩn kết nối "đã được xác thực" trong suốt quá trình thực hiện HĐ. Đ35 k2 d: thiết lập hạ tầng CNTT, nâng cấp HIS theo chuẩn dữ liệu đầu vào và đầu ra, trích chuyển, giao dịch điện tử.
- **Áp dụng cho**: mọi cơ sở KCB ký HĐ BHYT, kể cả PK tư · **Hiệu lực**: 01/07/2025 (Đ22–36 thuộc Đ70 k2)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: vendor cung cấp hồ sơ để điền Mẫu 8 (tên, phiên bản, nhà cung cấp, mô hình thuê/mua); HIS xuất được dữ liệu đúng chuẩn QĐ 130/3176 và ký số (R18) trước ngày ký HĐ.
- **Ghi chú / bẫy**: **Khoảng trống #14 đã kiểm**: trong NĐ 188, TT 12/2026, TT 48/2017 **không có** thủ tục chứng nhận, kiểm thử hay "xác thực phần mềm HIS" trước khi kết nối. Mẫu 8 chỉ là kê khai. Theo hướng dẫn kỹ thuật BHXH (HD-BHXH-PL01), trên thực tế cần (1) tài khoản Cổng, (2) **đăng ký chứng thư số** trên Cổng (Quản trị hệ thống > Danh mục chứng thư số), (3) gửi được XML hợp lệ. Suy luận: "đã được xác thực" ở Đ68 k5 b nhiều khả năng là việc kết nối được BHXH chấp nhận lúc ký HĐ, không phải chứng nhận phần mềm. Chưa xác minh, xem mục 7.

#### BHYT-GD-R16 — Tài khoản Cổng tiếp nhận dữ liệu: quản trị, phân quyền, không dùng chung
- **Căn cứ**: TT 12/2026 Đ3 k1–4: mỗi cơ sở 01 tài khoản quản trị cấp ngay sau khi ký HĐ lần đầu, khai báo theo **Mẫu 08/BH** (mã cơ sở, tên, tỉnh, xã, địa điểm, mã đơn vị BHXH, email, họ tên, số căn cước, điện thoại người đại diện); BHXH đối chiếu trong 01 ngày làm việc; tài khoản quản trị tạo, phân quyền, hủy quyền các tài khoản giao dịch. Đ16 k3 b: cơ sở quản lý tài khoản quản trị, phân quyền "đúng mục đích, không sử dụng chung tài khoản"; bảo đảm ATTT, bảo vệ thông tin cá nhân người bệnh. TT 48 Đ13 k4: báo BHXH khi đổi người được ủy quyền quản lý, xác thực điện tử, sử dụng tài khoản.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 10/02/2026
- **Mức**: BẮT BUỘC (cho cơ sở). Yêu cầu với phần mềm là BẮT BUỘC? vì luật nói về tài khoản Cổng, còn HIS thường gọi API bằng một tài khoản kỹ thuật.
- **Phần mềm phải**: lưu thông tin xác thực Cổng trong kho bí mật (không lưu plaintext trong DB hoặc config); mỗi lời gọi API ghi `nguoi_dung_HIS`, `tai_khoan_cong`, `ma_giao_dich`; hỗ trợ nhiều tài khoản giao dịch theo vai trò (tra cứu thẻ, tra lịch sử, gửi hồ sơ, danh mục); quy trình xoay vòng mật khẩu khi đổi người phụ trách.
- **Ghi chú / bẫy**: theo HD-BHXH-PL01, API token gửi `password` mã hóa MD5 viết hoa. Đó là yêu cầu của BHXH, không phải thực hành tốt. Đừng dùng MD5 để lưu mật khẩu nội bộ.

#### BHYT-GD-R17 — Tài khoản HIS cá nhân, cấm mượn tài khoản để chỉ định hoặc kê đơn
- **Căn cứ**: NĐ 90/2026 Đ95 k1 c: phạt 500.000–1.000.000 đ (mức cá nhân; tổ chức gấp đôi theo Đ4 k5) hành vi "sử dụng tài khoản truy cập hệ thống phần mềm quản lý bệnh viện cấp cho người khác hoặc cho người khác mượn tài khoản" để khám, chỉ định CLS, phẫu thuật, thủ thuật, kê đơn. TT 12 Đ10 k1 g: giám định tự động rà phạm vi hành nghề, thời gian làm việc của người hành nghề.
- **Áp dụng cho**: mọi cơ sở dùng HIS · **Hiệu lực**: 15/05/2026
- **Mức**: BẮT BUỘC (hành vi bị phạt; phần mềm phải cho phép phát hiện và ngăn chặn)
- **Phần mềm phải**: tài khoản định danh theo người; xác thực mạnh (MFA hoặc ký số khi ký y lệnh); phát hiện phiên đồng thời ở nhiều máy; audit log ai chỉ định, ai kê đơn; mã người hành nghề (MA_BAC_SI/CCHN) ghi vào XML lấy từ tài khoản đăng nhập, không cho chọn tự do; kiểm tra lịch làm việc và phạm vi hành nghề (danh mục nhân lực 02/DM, R28) trước khi cho chỉ định.

#### BHYT-GD-R18 — Ký số, xác thực dữ liệu đề nghị thanh toán
- **Căn cứ**: NĐ 188 Đ69 k9: "Việc triển khai xác thực dữ liệu điện tử chi phí khám bệnh, chữa bệnh bảo hiểm y tế thực hiện chậm nhất từ ngày 01 tháng 01 năm 2026." Đ35 k2 c: gửi dữ liệu sau mỗi lượt, ký số bảng tổng hợp tháng và quý, xác thực dữ liệu điện tử. TT 12 Đ2 k2: tài liệu, dữ liệu gửi Cổng "phải được ký số, xác thực theo quy định của pháp luật về giao dịch điện tử"; Đ9 k1: hồ sơ đề nghị thanh toán ký số xác thực theo Đ35 k2 c và Đ69 k9 NĐ 188. TT 48 Đ7 k1 b: xác thực trước khi gửi bởi người được giao hoặc ủy quyền. Kỹ thuật (HD-BHXH-PL01): mỗi file XML (check-in XML0 và hồ sơ XML1–15) có thẻ `<CHUKYDONVI>` theo XSD trên Cổng, giải thuật SHA256, chứng thư số phải được đăng ký trước trên Cổng.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: chậm nhất 01/01/2026 [QUA]
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: ký số tổ chức (chữ ký đơn vị) từng hồ sơ XML trước khi gửi; quản lý chứng thư số (ngày hết hạn, cảnh báo trước 30 ngày, đăng ký chứng thư mới lên Cổng); xác minh chữ ký trước khi gửi; lưu bản XML đã ký đúng như đã gửi (bất biến, có hash).
- **Ghi chú / bẫy**: **Câu hỏi mở K2-4 đã giải quyết**: "xác thực dữ liệu" ở Đ69 k9 là xác thực (ký số) dữ liệu chi phí của cơ sở. Không phải xác thực sinh trắc người bệnh. Căn cứ là TT 12 Đ9 k1 dẫn ngược Đ69 k9 làm căn cứ ký số hồ sơ thanh toán, và hướng dẫn kỹ thuật của BHXH. TT 48 Đ6 k3 cho phép dữ liệu "phục vụ quản lý" không cần xác thực, nhưng hướng dẫn BHXH hiện yêu cầu ký cả XML check-in. Nên ký mọi thứ.

### C. Gửi dữ liệu, thời hạn, phản hồi

#### BHYT-GD-R19 — Gửi dữ liệu ngay sau mỗi lượt KCB (hiện hành)
- **Căn cứ**: TT 48 Đ6 k1: gửi dữ liệu lên Cổng "ngay sau khi kết thúc lần khám bệnh hoặc kết thúc đợt điều trị ngoại trú hoặc kết thúc đợt điều trị nội trú", trừ trường hợp Đ8. TT 48 Đ13 k7: kết thúc vào ngày không tổ chức KCB BHYT (nghỉ, lễ, Tết) thì gửi vào ngày làm việc kế tiếp; k8: được gửi dữ liệu thanh toán cùng lúc với dữ liệu quản lý. NĐ 188 Đ35 k2 c: gửi "sau khi kết thúc lượt khám bệnh, chữa bệnh". TT 48 Đ5: 4 phương thức (web service; đồng bộ từ phần mềm máy trạm; nhập trực tiếp; FTP), kết quả đầu ra phải như nhau.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 01/03/2018; NĐ 188 từ 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sự kiện "kết thúc lượt" (ra viện, kết thúc khám) tự đưa hồ sơ vào hàng đợi gửi; gửi trạng thái check-in khi bắt đầu lượt (API `checkInKcbQd3176`, HD-BHXH-PL01); retry có backoff; lưu `maGiaoDich`, `thoiGianTiepNhan` của Cổng (bằng chứng thời điểm gửi, TT 12 Đ2 k3).
- **Ghi chú / bẫy**: TT 12 Đ9 k2 a: Cổng tự phản hồi trong 06 giờ với hồ sơ gửi không đúng thời hạn, nên trễ hạn đã bị đo tự động.

#### BHYT-GD-R20 — Cửa sổ hiệu chỉnh 07 ngày làm việc, gửi kỳ cuối tháng trước ngày 05
- **Căn cứ**: TT 48 Đ7 k1: trong 07 ngày làm việc kể từ ngày kết thúc KCB, (a) kiểm tra, đối chiếu, hiệu chỉnh, (b) xác thực, (c) gửi dữ liệu đề nghị thanh toán đến **Cổng tiếp nhận dữ liệu y tế của Bộ Y tế và Cổng giám định BHYT**; (d) phát sinh cuối tháng, quý, năm thì gửi trước ngày 05 của tháng kế tiếp. TT 48 Đ13 k9: được hiệu chỉnh dữ liệu đã gửi nếu nêu rõ lý do và thống nhất với BHXH. TT 12 Đ9 k1: Bảng kê chi tiết gửi theo thời hạn Đ7 hoặc Đ8 TT 48.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: hiện hành đến khi TT thay TT 48 có hiệu lực
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trạng thái hồ sơ `nhap → da_gui_quan_ly → da_hieu_chinh → da_ky → da_gui_thanh_toan`; đếm ngược 07 ngày làm việc (lịch nghỉ lễ có cấu hình); cảnh báo hồ sơ cuối tháng phải gửi trước ngày 05; mọi lần hiệu chỉnh sau khi gửi phải có `ly_do` và tham chiếu văn bản hoặc thống nhất với BHXH.
- **Ghi chú / bẫy**: nghĩa vụ gửi song song lên **Cổng BYT** (TT 48 Đ7 k1 c; NĐ 188 Đ71 k1 c cũng nói "hệ thống tiếp nhận dữ liệu KCB BHYT của Bộ Y tế") thường bị bỏ quên. Tình trạng vận hành của Cổng BYT hiện nay: chưa xác minh.

#### BHYT-GD-R21 — Gửi chậm có lý do hợp lệ và bằng chứng sự cố
- **Căn cứ**: TT 48 Đ8 k1: được gửi chậm khi (a) sự cố khách quan, bất khả kháng làm hạ tầng CNTT không đáp ứng, (b) mất điện, mất Internet; k2: bên xảy ra sự cố phải báo ngay cho bên kia (điện thoại, email, văn bản) và gửi ngay khi khắc phục xong; k3: với điểm b thì hình thức, thời gian gửi do hai thủ trưởng quyết định, ghi trong HĐ và báo cáo cơ quan quản lý. TT 12 Đ2 k4: BHXH báo bảo trì Cổng trước tối thiểu 12 giờ, báo sự cố và thời điểm hoạt động lại chậm nhất 01 giờ sau khi khắc phục; thời hạn gửi được gia hạn tương ứng thời gian Cổng ngừng.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: nhật ký sự cố (nguồn: HIS, mạng, điện, Cổng; bắt đầu, kết thúc, người báo, kênh báo); đánh dấu hồ sơ gửi trễ gắn với sự cố; tự cộng thời gian Cổng ngừng vào hạn gửi; lưu thông báo bảo trì hoặc sự cố lấy từ Cổng.

#### BHYT-GD-R22 — Xử lý phản hồi tự động của Cổng
- **Căn cứ**: TT 12 Đ9 k2: Cổng phản hồi tự động (a) chậm nhất 06 giờ với hồ sơ gửi không đúng thời hạn; (b) chậm nhất 24 giờ với hồ sơ sai cấu trúc hoặc định dạng, "ghi rõ lỗi sai của từng trường thông tin"; (c) chậm nhất 48 giờ khi Bảng tổng hợp lệch Bảng kê chi tiết hoặc Báo cáo quyết toán không khớp Bảng tổng hợp. Đ9 k3: trong 02 ngày làm việc kể từ khi nhận phản hồi (b) hoặc (c), cơ sở gửi bản điều chỉnh kèm văn bản ghi rõ số liệu sửa. TT 48 Đ7 k3 c: lỗi cảnh báo hoặc từ chối được thông báo chi tiết theo từng trường của từng bảng XML.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 10/02/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kéo phản hồi lỗi (API hoặc màn hình "Kết quả gửi hồ sơ XML") và ánh xạ lỗi về hồ sơ, bảng XML, trường; hàng việc "sửa lỗi Cổng" có hạn 02 ngày làm việc; sinh văn bản giải trình số liệu điều chỉnh.

#### BHYT-GD-R23 — Kết quả giám định tự động và Bảng kê chi tiết điều chỉnh (Mẫu 09/BH)
- **Căn cứ**: TT 12 Đ10: Hệ thống giám định rà 11 nội dung (a thẻ; b mức hưởng; c phạm vi thanh toán theo danh mục cơ sở; d mức thanh toán; đ tỷ lệ, điều kiện thanh toán; e phạm vi chuyên môn, thời gian hoạt động của cơ sở; g phạm vi hành nghề, thời gian làm việc của người hành nghề; h khoảng cách giữa các lần KCB; i hợp lý theo tiêu chí BYT; k số liệu thống nhất trong bảng kê; m số lượng thuốc, TBYT so với số đã mua sắm hoặc điều chuyển). k2: kết quả trong **07 ngày làm việc**. k3: trong **03 ngày làm việc** cơ sở gửi tài liệu chứng minh hoặc **Bảng kê chi tiết điều chỉnh theo Mẫu 09/BH**. k4: điều chỉnh vẫn sai thì từ chối. Mẫu 09/BH: Cổng điền cột A–Q (XML1_ID, ID chi phí, số bảng XML, mã liên kết, số thứ tự trong file gốc, mã bệnh nhân…); cơ sở điền cột T, R, S, (1), trạng thái "2" hoặc "3" khi tự đề nghị điều chỉnh hoặc bổ sung; ký số.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: Mẫu 09/BH từ 01/04/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: nhập kết quả giám định theo dòng chi phí; workflow giải trình trong 03 ngày làm việc; sinh Mẫu 09/BH ký số; giữ liên kết dòng chi phí ↔ XML1_ID/ID chi phí của Cổng (cần lưu ID do Cổng trả về).
- **Ghi chú / bẫy**: tự kiểm trước khi gửi theo đúng 11 nội dung trên là cách giảm xuất toán hiệu quả nhất (xem pattern P5).

#### BHYT-GD-R24 — Giám định chủ động: cung cấp HSBA và tài liệu trong 03 ngày làm việc
- **Căn cứ**: TT 12 Đ11 k3 a: BHXH báo trước tối thiểu 03 ngày làm việc; cơ sở cung cấp đủ hồ sơ, tài liệu trong 03 ngày làm việc kể từ khi nhận yêu cầu. Đ5 k2 và Đ12 k4: cơ sở chịu trách nhiệm về tính trung thực, khớp đúng giữa Bảng kê, Bảng tổng hợp, Báo cáo quyết toán và HSBA.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 10/02/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: từ danh sách hồ sơ BHXH yêu cầu (theo MA_LK hoặc mã thẻ, ngày), xuất trọn gói HSBA điện tử đã ký, y lệnh, kết quả CLS, phiếu công khai thuốc, hóa đơn; đối chiếu tự động mỗi dòng XML2/XML3 với y lệnh và phiếu thực hiện trong HSBA.

#### BHYT-GD-R25 — Bảng tổng hợp hằng tháng (01/BH) và Báo cáo quyết toán hằng quý (02/BH)
- **Căn cứ**: Luật 51 Điều 1 k26 (Đ32 k2 a Luật BHYT): trong 15 ngày đầu mỗi tháng gửi bản tổng hợp đề nghị thanh toán tháng trước; trong 15 ngày đầu mỗi quý gửi báo cáo quyết toán quý trước. TT 12 Đ5 k1 b, c; Đ9 k1 (nhắc lại thời hạn); Phụ lục I Mẫu 01/BH: 4 mục theo MA_LOAI_KCB (I ngoại trú: 01, 06, 07; II điều trị ngoại trú: 02, 05, 08; III điều trị ban ngày: 04, 09; IV nội trú: 03), cột lấy từ chỉ tiêu XML1 QĐ 3176 (SO_NGAY_DTRI, T_TONGCHI_BV, T_TONGCHI_BH, T_BHTT, T_BNCCT, T_NGUONKHAC, T_BNTT), ràng buộc cột 2 = 3 + 6 + 7 và cột 3 = 4 + 5, tiền làm tròn đến đồng; Mẫu 02/BH tổng hợp từ 01/BH các tháng trong quý. TT 12 Đ9 k4: cơ sở ký HĐ cho nhiều cơ sở trực thuộc thì gửi tổng hợp cho cả nhóm (Phần A, B, C…). NĐ 90 Đ94: gửi báo cáo quyết toán chậm thì phạt 500.000 đ đến 7.000.000 đ (mức cá nhân, tổ chức ×2).
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: Mẫu 01/BH từ 01/04/2026; quyết toán quý I/2026 được dùng mẫu cũ (TT 12 Đ17 k2)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh 01/BH, 02/BH trực tiếp từ đúng tập XML1 đã gửi (không nhập tay); kiểm tra ràng buộc cột trước khi ký; ký số người lập, kế toán trưởng, thủ trưởng; nhắc hạn ngày 15.
- **Ghi chú / bẫy**: Mẫu 01/BH dẫn MA_LOAI_KCB theo **Phụ lục 1 QĐ 824/2023**, phụ lục này bị QĐ 1804/2026 bãi bỏ từ 01/08/2026. Theo TT 12 Đ17 k3 (văn bản viện dẫn bị thay thì áp dụng văn bản thay thế) phải dùng bảng mã QĐ 1804. Ánh xạ cụ thể → BHYT-DATA.

#### BHYT-GD-R26 — Biên bản giám định, biên bản quyết toán, hóa đơn
- **Căn cứ**: TT 12 Đ12 k2: trong 02 ngày làm việc kể từ khi nhận Biên bản giám định (03/BH), cơ sở ký và gửi lại; không đồng ý thì ghi rõ căn cứ pháp lý. Đ14 k3: trong 02 ngày làm việc kể từ khi nhận Biên bản quyết toán (06/BH), gửi biên bản đã ký **và hóa đơn điện tử khớp số quyết toán**, hoàn trả phần tạm ứng thừa. Đ14 k6: quyết toán chênh lệch với hóa đơn đã xuất thì lập hóa đơn điện tử mới cho số chênh lệch. Đ15 k1: BHXH thanh toán trong 03 ngày làm việc. NĐ 188 Đ51 k2: từ chối thanh toán phải nêu căn cứ, lý do, số tiền trong biên bản giám định, gồm cả khoản bị trả tự động khi gửi dữ liệu.
- **Áp dụng cho**: mọi cơ sở KCB BHYT (phân hệ tài chính kế toán) · **Hiệu lực**: 06/BH từ 01/04/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: theo dõi từng biên bản (nhận, hạn ký, đã ký); đối soát số quyết toán với hóa đơn BHYT đã xuất; tạo hóa đơn điều chỉnh hoặc bổ sung; sổ theo dõi xuất toán theo từng hồ sơ và lý do để khiếu nại (NĐ 188 Đ51 k3).
- **Ghi chú / bẫy**: TT 12 Đ14 k6 viện dẫn NĐ 123/2020 sửa bởi NĐ 70/2025, cả hai đã hết hiệu lực từ 01/07/2026 (thay bởi NĐ 254/2026). Áp dụng NĐ 254/2026 theo TT 12 Đ17 k3. Chi tiết → K11.

#### BHYT-GD-R27 — Cảnh báo gia tăng chi và tự rà soát
- **Căn cứ**: TT 12 Đ13: trước ngày 15 hằng tháng BHXH cảnh báo qua Cổng (3 mức: tăng thấp, tăng cao, tăng rất cao); trong 10 ngày cơ sở rà soát, xác định nguyên nhân, có giải pháp. NĐ 188 Đ35 k1 b, k2 đ.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 10/02/2026
- **Mức**: BẮT BUỘC (tổ chức); NÊN (công cụ phần mềm)
- **Phần mềm phải** (NÊN): báo cáo chi bình quân theo lượt, theo khoa, theo bác sĩ, theo nhóm chi phí; so cùng kỳ; drill-down đến hồ sơ để trả lời cảnh báo trong 10 ngày.

#### BHYT-GD-R28 — Danh mục sử dụng trong liên thông (6 mẫu 01–06/DM) và cập nhật
- **Căn cứ**: TT 12 Đ7 k1: danh mục mã hóa theo QĐ 7603/2018 và các QĐ sửa (4905/2019, 5937/2021, 824/2023, 2010/2025, 3276/2025); chuẩn định dạng theo Phụ lục II gồm 01/DM bộ phận chuyên môn (mã khoa hoặc bàn khám, ví dụ "K0809", "K02.D35"), 02/DM nhân lực (chức danh, số CCHN, ngày cấp, phạm vi chuyên môn…), 03/DM thuốc, máu, chế phẩm máu, 04/DM thiết bị y tế, 05/DM dịch vụ KCB, 06/DM thiết bị y tế dùng để thực hiện DVKT. Đ7 k2: sau khi ký HĐ lần đầu, lập danh mục, **ký số**, gửi qua Cổng, khớp hồ sơ HĐ. Đ7 k3: áp dụng từ ngày HĐ có hiệu lực; thuốc, TBYT không sớm hơn hiệu lực hợp đồng mua sắm. Đ8: cập nhật khi ký phụ lục hoặc thay đổi (NĐ 188 Đ24 k2, k3); BHXH xử lý tối đa 05 ngày làm việc; bị từ chối thì gửi lại trong 15 ngày; thuốc, TBYT mua cấp cứu áp dụng theo ngày hóa đơn; phát hiện sai lệch với danh mục dùng chung thì hai bên sửa hoặc hủy trong 05 ngày làm việc.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 01/04/2026 (Đ17 k1)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: master data có `ngay_ap_dung_BHXH` và trạng thái duyệt của Cổng cho từng mục; chặn hoặc cảnh báo khi kê thuốc, DVKT chưa được Cổng chấp nhận tại ngày y lệnh; xuất 6 danh mục đúng định dạng và ký số; lưu lịch sử phiên bản danh mục.
- **Ghi chú / bẫy**: mã và cấu trúc trường → BHYT-DATA. Mẫu 07/BH dẫn mã khoa theo PL6 QĐ 2010/2025, phụ lục này bị QĐ 1804/2026 bãi bỏ từ 01/08/2026.

### D. Toàn vẹn dữ liệu và chế tài

#### BHYT-GD-R29 — Dữ liệu chi phí phản ánh trung thực, truy vết được
- **Căn cứ**: NĐ 188 Đ68 k5 c (chịu trách nhiệm về tính chính xác, hợp pháp của dữ liệu); TT 48 Đ13 k1, k3; TT 12 Đ5 k2. NĐ 90: Đ85 (kê khống để chiếm đoạt, 200.000 đ đến 5.000.000 đ), Đ86 (kê khống, kê tăng gây thiệt hại, 200.000 đ đến 20.000.000 đ), Đ88 (áp sai giá, giá chưa duyệt, ghi sai chủng loại, hàm lượng, cách dùng, đơn vị, tên DVKT, hoặc đã chi từ nguồn khác: 300.000 đ đến 50.000.000 đ), Đ95 k3 (lạm dụng chỉ định: 1.000.000 đ đến 40.000.000 đ); tất cả là mức cá nhân, tổ chức ×2 (Đ4 k5); trần BHYT 75 triệu đ cá nhân, 150 triệu đ tổ chức (Đ4 k3); kèm biện pháp hoàn trả quỹ.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 15/05/2026 (NĐ 90)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi dòng chi phí XML2/XML3 truy vết được tới y lệnh (người chỉ định, thời điểm) và phiếu thực hiện hoặc phát thuốc (người thực hiện); giá lấy từ bảng giá đã duyệt có hiệu lực theo ngày; cấm sửa trực tiếp số lượng, giá ở bảng kê mà không qua y lệnh; audit log bất biến cho mọi chỉnh sửa sau khi kết thúc lượt.

#### BHYT-GD-R30 — Kết nối, liên thông và tạo lập chứng từ điện tử là nghĩa vụ có chế tài
- **Căn cứ**: NĐ 90 Đ95 k4 b: phạt 1.000.000–3.000.000 đ (cá nhân; tổ chức 2.000.000–6.000.000 đ) hành vi "không kết nối, liên thông dữ liệu, tạo lập chứng từ điện tử về khám bệnh, chữa bệnh theo quy định về giao dịch điện tử trong lĩnh vực bảo hiểm y tế". NĐ 188 Đ67 k5, Đ68 k5 a.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 15/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dashboard độ phủ: tỷ lệ lượt KCB BHYT đã gửi, đã ký, đã được tiếp nhận; danh sách lượt chưa gửi quá hạn.
- **Ghi chú / bẫy**: hiện **không có** điều riêng phạt "chậm gửi XML" trong NĐ 90 (đã đọc Đ81–95). Đ94 chỉ phạt chậm **báo cáo quyết toán**. Chế tài chậm gửi trong DT-TT48 sẽ cần căn cứ xử phạt mới (xem R34, mục 7).

#### BHYT-GD-R31 — Bảo mật dữ liệu BHYT và hồ sơ thuộc bí mật nhà nước
- **Căn cứ**: NĐ 188 Đ66 k1, k3; TT 48 Đ9 (bảo mật, toàn vẹn, quyền riêng tư thông tin y tế trên mạng); TT 12 Đ16 k3 b (bảo vệ thông tin cá nhân người bệnh); TT 12 Đ9 k5: hồ sơ đề nghị thanh toán thuộc bí mật nhà nước thì lập, gửi theo pháp luật bảo vệ bí mật nhà nước.
- **Áp dụng cho**: mọi cơ sở; đặc biệt BV quân đội, công an, cơ sở có đối tượng mật · **Hiệu lực**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cờ `bi_mat_nha_nuoc` trên hồ sơ để loại khỏi luồng gửi Cổng thông thường; mã hóa khi truyền (TLS); phân quyền xem dữ liệu BHYT. Phần chung về DLCN → K8.

#### BHYT-GD-R32 — Phát hiện và báo vi phạm sử dụng thẻ
- **Căn cứ**: NĐ 188 Đ12 k4: phát hiện vi phạm (thu hồi, gian lận, cho mượn thẻ) thì cơ sở KCB thông báo BHXH. NĐ 90 Đ84 (mượn thẻ: 1.000.000 đ đến 5.000.000 đ, xử phạt người vi phạm).
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: đối chiếu ảnh, thông tin nhân thân khi tiếp đón; chức năng "báo nghi vấn thẻ" lưu bằng chứng và trạng thái thông báo BHXH.

#### BHYT-GD-R33 — Ký xác nhận khi người bệnh không làm thủ tục thanh toán
- **Căn cứ**: TT 48 Đ13 k6: người bệnh hoặc đại diện không làm thủ tục thanh toán thì cơ sở ký xác nhận chi phí, thủ trưởng chịu trách nhiệm pháp lý về việc ký và dữ liệu gửi đi.
- **Áp dụng cho**: mọi cơ sở KCB BHYT · **Hiệu lực**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trạng thái "người bệnh bỏ về hoặc không ký"; luồng ký thay của người được thủ trưởng ủy quyền (ký số), có lý do.

#### BHYT-GD-R34 — Chuẩn bị cho TT thay TT 48 (gửi trong 03 giờ, khóa dữ liệu)
- **Căn cứ**: DT-TT48 (thứ cấp, dự thảo): gửi dữ liệu chi phí "đã được ký xác thực" lên Cổng "trong vòng tối đa 03 giờ kể từ thời điểm kết thúc lượt KCB", trừ các trường hợp được gửi chậm; trong 15 ngày cơ sở kiểm tra, đối chiếu trước khi đề nghị thanh toán; dữ liệu đã gửi đề nghị thanh toán không được thay đổi (trừ một số trường hợp); Cổng trả kết quả giám định chi tiết trong 15 ngày; chế tài theo bậc: nhắc tự động hằng tháng, BHXH nhắc bằng văn bản lần 1 và lần 2, tiếp tục vi phạm thì xử phạt VPHC.
- **Áp dụng cho**: mọi cơ sở KCB BHYT, vendor · **Hiệu lực**: dự kiến 01/01/2027 [TỚI]
- **Mức**: NÊN (đến khi ban hành; nên làm ngay vì thời gian chuẩn bị ngắn)
- **Phần mềm phải**: pipeline gần thời gian thực: ký số tự động bằng chứng thư tổ chức (HSM hoặc ký số từ xa), không chờ thao tác tay; SLA giám sát `t_gui - t_ket_thuc_luot ≤ 3h` cho từng hồ sơ; tách "gửi sớm (3h)" với "đề nghị thanh toán (≤ 15 ngày)"; khóa bất biến sau đề nghị thanh toán, mọi thay đổi sau đó chỉ qua luồng điều chỉnh có lý do.
- **Ghi chú / bẫy**: mốc 03 giờ mâu thuẫn với cửa sổ 07 ngày làm việc hiện hành (TT 48 Đ7) và mốc trước ngày 05 cho kỳ cuối tháng. Hệ thống phải cấu hình được cả hai chế độ theo ngày hiệu lực.

#### BHYT-GD-R35 — KCB theo yêu cầu và chi phí ngoài phạm vi phải thông báo trước
- **Căn cứ**: NĐ 188 Đ20: quỹ trả theo phạm vi và mức hưởng; người bệnh trả phần chênh lệch; k2: cơ sở phải công khai các khoản ngoài phạm vi, phần chênh lệch "và phải thông báo trước cho người bệnh". NĐ 188 Đ35 k2 i: không thu thêm chi phí đã nằm trong kết cấu giá.
- **Áp dụng cho**: BV, PK có dịch vụ theo yêu cầu · **Hiệu lực**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: khi chỉ định dịch vụ theo yêu cầu hoặc ngoài danh mục cho người có thẻ, hiển thị và ghi nhận xác nhận đã thông báo (người bệnh ký); tách đúng T_BNTT (người bệnh tự trả) với T_BNCCT (cùng chi trả).

**Tổng**: 35 yêu cầu. BẮT BUỘC 31 (R01–R13, R15, R17–R26, R28–R33, R35); BẮT BUỘC? 2 (R14, R16); NÊN 2 (R27 phần phần mềm, R34).

## 3. Pattern thiết kế

**P1. Mô hình "lượt KCB BHYT" và nhật ký thẻ** (R02, R03, R06, R07, R08, R09)
- Bảng `bhyt_the_tra_cuu(id, luot_kcb_id, thoi_diem, nguon {CONG|VNEID|THU_CONG}, ma_the, so_dinh_danh, ket_qua_ma, payload_json, hash, nguoi_thuc_hien)`, append-only.
- `luot_kcb`: `thoi_diem_xuat_trinh_the`, `trang_thai_the {DA_XAC_MINH|CHUA_XAC_MINH|LOI_CONG}`, `muc_huong_ap_dung` dạng bảng con `(tu_thoi_diem, den_thoi_diem, ty_le, can_cu)` để chia giai đoạn (đổi thẻ, vượt ngưỡng cùng chi trả, thẻ hết hạn + 15 ngày).
- Ràng buộc: không cho chốt ra viện khi chưa có bản ghi tra cứu `thoi_diem ≥ ngay_ra - X` (X cấu hình).
- Đánh đổi: lưu payload Cổng là lưu dữ liệu cá nhân, cần quy định thời hạn lưu và phân quyền (K8).

**P2. Hàng đợi gửi Cổng bền vững (outbox) có SLA** (R18, R19, R20, R21, R30, R34)
- `bhyt_outbox(id, luot_kcb_id, loai {CHECKIN|XML130|DANH_MUC|TONG_HOP_01BH|QUYET_TOAN_02BH|DIEU_CHINH_09BH}, phien_ban, xml_da_ky_blob, sha256, trang_thai {CHO_KY|DA_KY|DA_GUI|CONG_NHAN|LOI|CAN_SUA}, ma_giao_dich_cong, thoi_gian_tiep_nhan_cong, han_gui, so_lan_thu, su_co_id)`.
- Ghi outbox trong cùng transaction với sự kiện "kết thúc lượt"; worker ký số rồi gửi, retry theo backoff; `han_gui` tính theo chế độ hiện hành (07 ngày làm việc) hoặc chế độ dự thảo (03 giờ), có ngày chuyển chế độ.
- Index `(trang_thai, han_gui)` cho cảnh báo quá hạn. Bảng `su_co(id, nguon, bat_dau, ket_thuc, kenh_bao, nguoi_bao, bang_chung)` để tự gia hạn (TT 12 Đ2 k4, TT 48 Đ8).
- Đánh đổi: ký số tự động bằng chứng thư tổ chức nhanh nhưng phải quản lý khóa (HSM, phân quyền gọi ký).

**P3. Bản ghi bất biến + điều chỉnh có lý do** (R20, R23, R29, R34)
- Bản XML đã gửi không bao giờ bị ghi đè; mỗi lần sửa tạo `phien_ban + 1` với `ly_do`, `can_cu (phan_hoi_cong_id | van_ban_BHXH)`, `nguoi_sua`. Mẫu 09/BH sinh từ diff giữa phiên bản gốc và phiên bản điều chỉnh, giữ `XML1_ID`/`ID chi phí` do Cổng cấp.
- Đánh đổi: tăng dung lượng lưu trữ, đổi lại có bằng chứng khi bị xuất toán hoặc thanh tra.

**P4. Bộ quy tắc mức hưởng có hiệu lực theo thời gian** (R07, R09, R10, R35)
- `quy_tac_muc_huong(id, hieu_luc_tu, hieu_luc_den, cap_cmkt, tuyen_cu, diem_tu, diem_den, loai_kcb, dieu_kien {DUNG_TUYEN|CAP_CUU|LUU_TRU|TAM_TRU|BENH_HIEM|TU_DEN}, ty_le, can_cu_phap_ly)`; `cau_hinh_co_so(cap, diem_xep_cap, tuyen_truoc_2025, hieu_luc_tu)`.
- Engine trả về tỷ lệ kèm căn cứ (ví dụ "NĐ 188 Đ19 k2") để in ra cho người bệnh và để audit.
- Đánh đổi: bảng quy tắc phức tạp hơn code cứng, nhưng mốc 01/07/2026 cho thấy luật đổi theo lộ trình.

**P5. Bộ tự giám định trước khi gửi ("pre-giám định")** (R23, R25, R28, R29, R17)
- Chạy cùng 11 nhóm kiểm tra của TT 12 Đ10 k1 trước khi ký: thẻ và mức hưởng; danh mục đã được Cổng chấp nhận tại ngày y lệnh; giá có hiệu lực; tỷ lệ, điều kiện thanh toán; người chỉ định có CCHN, phạm vi, ca làm việc (02/DM); khoảng cách giữa các lần khám; tổng XML1 khớp chi tiết XML2/XML3; số lượng thuốc, TBYT xuất ≤ số trúng thầu hoặc điều chuyển.
- Kết quả lưu `kiem_tra_truoc_gui(luot_kcb_id, ma_quy_tac, muc_do, thong_diep)`; lỗi nặng thì chặn ký.
- Đánh đổi: quy tắc của BHXH (TT 12 Đ16 k1 c) chưa công khai đầy đủ nên chỉ làm được xấp xỉ; cần cập nhật khi BHXH công bố (NĐ 188 Đ71 k9 i: BHXH phải công khai yêu cầu tiếp nhận dữ liệu trước khi áp dụng).

**P6. Master data danh mục 2 trạng thái: nội bộ và Cổng** (R28)
- `danh_muc_item(..., trang_thai_noi_bo, trang_thai_cong {CHUA_GUI|CHO_DUYET|AP_DUNG|TU_CHOI}, ngay_ap_dung_cong, ly_do_tu_choi, han_gui_lai)`; job theo dõi hạn 05 ngày làm việc (BHXH) và 15 ngày (gửi lại).
- Ràng buộc: kê đơn hoặc chỉ định BHYT chỉ lấy mục `AP_DUNG` có `ngay_ap_dung_cong ≤ ngay_y_lenh`; ngoại lệ thuốc cấp cứu theo ngày hóa đơn.

**P7. Danh tính người hành nghề gắn với chữ ký y lệnh** (R16, R17)
- Đăng nhập cá nhân + MFA; y lệnh ký số cá nhân hoặc ký điện tử có xác thực lại; MA_BAC_SI trong XML lấy từ phiên đăng nhập; phát hiện một tài khoản hoạt động trên ≥ 2 máy hoặc IP đồng thời; báo cáo y lệnh ngoài ca làm việc.
- Đánh đổi: thao tác nhiều hơn ở buồng khám đông; dùng thẻ hoặc sinh trắc để đăng nhập nhanh.

**P8. Lịch hạn nghĩa vụ BHYT (compliance calendar)** (R20, R22–R27)
- Bảng `nghia_vu_han(loai, doi_tuong_id, moc_bat_dau, han, don_vi {GIO|NGAY|NGAY_LAM_VIEC}, can_cu, trang_thai)` với các loại: sửa lỗi Cổng 02 ngày làm việc; giải trình giám định 03 ngày làm việc; cung cấp HSBA 03 ngày làm việc; ký biên bản 02 ngày làm việc; rà soát cảnh báo 10 ngày; 01/BH ngày 15 hằng tháng; 02/BH ngày 15 đầu quý; gửi kỳ cuối tháng trước ngày 05.
- Cần lịch ngày làm việc (nghỉ lễ, Tết) cấu hình theo năm.

## 4. Checklist audit

| ID kiểm tra | Yêu cầu | Cách kiểm tra trên phần mềm có sẵn | Bằng chứng cần thu | Mức |
|---|---|---|---|---|
| GD-A01 | R01 | Tiếp đón thử 5 ca: chỉ CCCD gắn chip; chỉ VNeID; chỉ mã số thẻ; thẻ giấy; trẻ < 6 tuổi chỉ có giấy chứng sinh. Có ca nào bị chặn không? | Ảnh màn hình từng ca, cấu hình trường bắt buộc | Bắt buộc |
| GD-A02 | R02 | Xem log: mỗi lượt BHYT có bản ghi tra cứu Cổng lúc tiếp đón và trước ra viện không? Truy vấn tỷ lệ lượt không có tra cứu | SQL đếm lượt thiếu tra cứu; mẫu payload phản hồi | Bắt buộc |
| GD-A03 | R03 | Ngắt kết nối Cổng (môi trường test), tiếp đón ca BHYT: hệ thống có cho tiếp nhận, đánh dấu chưa xác minh, tra lại sau và lưu bằng chứng lỗi không? | Log, trạng thái lượt, file ảnh hoặc log lỗi | Bắt buộc |
| GD-A04 | R04 | Có trường bắt buộc scan thẻ hoặc CCCD không? Có ghi nhận đồng ý sao chụp không? Bảng giá có phí sao chụp không? | Cấu hình form, bảng giá | Bắt buộc |
| GD-A05 | R05 | Thử ca trẻ sơ sinh chưa có thẻ: có chức năng lấy hoặc đề nghị mã thẻ tạm qua Cổng không? | Ảnh màn hình, XML gửi đi có mã thẻ tạm | Bắt buộc |
| GD-A06 | R06 | Ca xuất trình thẻ ngày thứ 2 của đợt nội trú (không cấp cứu): chi phí ngày 1 có bị đưa vào BHYT không? | Bảng kê, XML2/XML3 theo ngày | Bắt buộc |
| GD-A07 | R07, R08 | Ca nội trú có thẻ hết hạn giữa đợt: kiểm tra mức hưởng sau ngày hết hạn + 15. Ca đổi thẻ (đổi mức hưởng) giữa đợt | XML1 MUC_HUONG, bảng kê theo giai đoạn | Bắt buộc |
| GD-A08 | R09 | Ca có cùng chi trả lũy kế gần ngưỡng: hệ thống có tự chuyển 100% khi vượt không? Lương cơ sở có tham số hóa không? | Cấu hình tham số, bảng kê | Bắt buộc |
| GD-A09 | R10 | Xem cấu hình cấp CMKT, điểm, cờ tuyến cũ của cơ sở; chạy ca ngoại trú không đúng nơi đăng ký ở cơ sở thuộc NĐ 188 Đ19 k2–4 sau 01/07/2026 | Cấu hình, kết quả tỷ lệ, căn cứ in ra | Bắt buộc |
| GD-A10 | R11 | Phát hành phiếu chuyển điện tử: có ký số bác sĩ và ký số cơ sở (sau 01/06/2026) không? Hạn 10 ngày làm việc hoặc 1 năm có tính đúng không? Còn chữ "đóng dấu" trên mẫu điện tử không? | File phiếu (PDF/XML) đã ký, kiểm chữ ký | Bắt buộc |
| GD-A11 | R12 | Dùng lại một phiếu hẹn đã dùng: có bị chặn không? Tạo phiếu hẹn thứ 2 cho cùng đợt đã kết thúc: có bị chặn không? | Log, thông báo lỗi | Bắt buộc |
| GD-A12 | R13 | Có in hoặc phát hành Mẫu số 9 NĐ 188 không? Chi phí DVCLS chuyển đi có vào hồ sơ người bệnh của cơ sở chuyển không? Có báo cáo danh sách DVCLS chuyển gửi BHXH không? | Mẫu in, XML3/XML4, báo cáo | Bắt buộc |
| GD-A13 | R14 | Hỏi lộ trình liên thông CLS 01/01/2027 của vendor; kiểm tra kết quả CLS có đủ định danh, thời điểm, người thực hiện, mã chuẩn không | Tài liệu lộ trình, mẫu dữ liệu | Bắt buộc? |
| GD-A14 | R15 | Đối chiếu Mẫu 8 trong hồ sơ HĐ BHYT với HIS đang chạy (tên, nhà cung cấp, mô hình thuê/mua). HIS có còn khớp sau khi nâng cấp hoặc đổi vendor không? | Bản Mẫu 8 đã nộp, HĐ BHYT | Bắt buộc |
| GD-A15 | R16 | Thông tin xác thực Cổng lưu ở đâu (plaintext trong DB hoặc config?) Log có ghi người dùng HIS gây ra mỗi lời gọi Cổng không? Có quy trình đổi mật khẩu khi đổi người phụ trách không? | Ảnh cấu hình (che bí mật), log, quy trình | Bắt buộc? |
| GD-A16 | R17 | Có tài khoản dùng chung ("bacsi", "khoaxx") không? Thử đăng nhập một tài khoản trên 2 máy cùng lúc. MA_BAC_SI trong XML có trùng người đăng nhập ký y lệnh không? | Danh sách user, log phiên, mẫu XML + audit | Bắt buộc |
| GD-A17 | R18 | Mở 1 file XML đã gửi: có `<CHUKYDONVI>` hợp lệ (SHA256, chứng thư còn hạn, đã đăng ký trên Cổng) không? Có cảnh báo chứng thư sắp hết hạn không? | File XML, kết quả verify chữ ký, danh mục chứng thư trên Cổng | Bắt buộc |
| GD-A18 | R19, R20 | Truy vấn phân bố `thoi_gian_tiep_nhan_cong - thoi_diem_ket_thuc_luot`; tỷ lệ > 07 ngày làm việc; hồ sơ cuối tháng gửi sau ngày 05. Có gửi Cổng BYT không? | SQL thống kê, báo cáo "hồ sơ gửi chậm" trên Cổng | Bắt buộc |
| GD-A19 | R21 | Có nhật ký sự cố (mất mạng, Cổng lỗi) và bằng chứng đã thông báo BHXH không? | Sổ hoặc bảng sự cố, email | Bắt buộc |
| GD-A20 | R22 | Lấy 3 phản hồi lỗi gần nhất từ Cổng: thời gian từ khi nhận đến khi gửi bản sửa có ≤ 02 ngày làm việc không? Có văn bản giải trình không? | Log phản hồi, bản sửa | Bắt buộc |
| GD-A21 | R23 | Có sinh Mẫu 09/BH ký số không? HIS có lưu XML1_ID/ID chi phí do Cổng cấp không? | File 09/BH, bảng mapping | Bắt buộc |
| GD-A22 | R24 | Diễn tập: chọn 10 hồ sơ ngẫu nhiên, xuất trọn HSBA + chứng từ trong bao lâu? Mỗi dòng XML2/XML3 có khớp y lệnh trong HSBA không? | Thời gian xuất, biên bản đối chiếu | Bắt buộc |
| GD-A23 | R25 | Sinh 01/BH tháng gần nhất: tổng có khớp tổng XML1 đã gửi không? Kiểm ràng buộc cột 2 = 3 + 6 + 7, cột 3 = 4 + 5. Có dùng MA_LOAI_KCB theo QĐ 1804 sau 01/08/2026 không? | File 01/BH, SQL đối chiếu | Bắt buộc |
| GD-A24 | R26 | Số quyết toán quý gần nhất có khớp hóa đơn điện tử BHYT không? Hóa đơn chênh lệch có lập theo NĐ 254/2026 không? | Biên bản 06/BH, hóa đơn | Bắt buộc |
| GD-A25 | R27 | Có báo cáo chi bình quân theo khoa, bác sĩ để trả lời cảnh báo không? | Báo cáo mẫu | Nên |
| GD-A26 | R28 | Kê thử một thuốc hoặc DVKT có trong danh mục nội bộ nhưng chưa được Cổng áp dụng: hệ thống có chặn hoặc cảnh báo không? Danh mục gửi Cổng có ký số không? | Ảnh màn hình, file 01–06/DM | Bắt buộc |
| GD-A27 | R29 | Thử sửa số lượng hoặc giá trên bảng kê sau khi kết thúc lượt mà không qua y lệnh: có được không? Có audit log không? | Log, kết quả thử | Bắt buộc |
| GD-A28 | R30 | Tỷ lệ lượt KCB BHYT trong kỳ chưa có XML được Cổng tiếp nhận | SQL đối chiếu với danh sách trên Cổng | Bắt buộc |
| GD-A29 | R31 | Có cơ chế loại hồ sơ bí mật nhà nước khỏi luồng gửi Cổng thường không? Kết nối Cổng có TLS không? | Cấu hình, tài liệu | Bắt buộc |
| GD-A30 | R32, R33 | Có chức năng báo thẻ nghi vấn; có luồng ký xác nhận khi người bệnh bỏ về không? | Ảnh màn hình, log | Bắt buộc |
| GD-A31 | R34 | Đo p95 thời gian từ kết thúc lượt đến khi Cổng tiếp nhận; ký số có cần thao tác tay không? Hồ sơ có bị khóa sau đề nghị thanh toán không? | Thống kê, mô tả luồng ký | Nên |
| GD-A32 | R35 | Ca dịch vụ theo yêu cầu cho người có thẻ: có phiếu thông báo trước và chữ ký người bệnh không? T_BNTT có tách khỏi T_BNCCT không? | Phiếu, XML1 | Bắt buộc |

## 5. Dòng thời gian & đối tượng

| Mốc | Trạng thái | Nội dung | Căn cứ | Ai phải làm |
|---|---|---|---|---|
| 01/03/2018 | [QUA] | TT 48 có hiệu lực: gửi ngay sau lượt, 07 ngày làm việc hiệu chỉnh, 4 phương thức | TT 48 Đ14 | Cơ sở KCB, vendor |
| 01/01/2025 | [QUA] | Luật 51: thủ tục KCB, chuyển người bệnh, mức hưởng theo cấp; TT 01/2025 (phiếu hẹn, phiếu chuyển điện tử) | Luật 51 Đ3 k2; TT 01 Đ15 | Cơ sở KCB, vendor |
| 01/07/2025 | [QUA] | Luật 51 có hiệu lực chung; NĐ 188 các Điều 1–11, 14–15, 17–19, 22–36, 39–44, 49–50, 54–61, 69–72; NĐ 164 | NĐ 188 Đ70 k2; NĐ 164 Đ27 | Cơ sở KCB, BHXH |
| 15/08/2025 | [QUA] | NĐ 188 có hiệu lực toàn bộ (Đ37–38 thủ tục, xuất trình, Cổng lỗi; Đ12 thu hồi thẻ…); NĐ 146/75/02 hết hiệu lực | NĐ 188 Đ70 k1, k5 | Cơ sở KCB |
| 31/12/2025 | [QUA] | Hạn chót ngừng dùng mẫu giấy hẹn và giấy chuyển tuyến cũ (theo NĐ 146/75): dùng đến khi BHXH và cơ sở cập nhật xong dữ liệu theo mẫu mới, nhưng không muộn hơn 31/12/2025 | TT 01 Đ15 k5 đ | Cơ sở KCB, vendor |
| **01/01/2026** | [QUA] | **Chậm nhất triển khai xác thực (ký số) dữ liệu điện tử chi phí KCB BHYT** | NĐ 188 Đ69 k9 | Cơ sở KCB, vendor |
| 03/02/2026 | [QUA] | TT 09/2026/TT-BTC: thẻ BHYT điện tử, không đòi thẻ giấy | TT 09/2026 (thứ cấp) | Cơ sở KCB |
| 10/02/2026 | [QUA] | TT 12/2026 có hiệu lực: Cổng, tài khoản, tra cứu, phản hồi 06h/24h/48h, giám định tự động/chủ động | TT 12 Đ17 | Cơ sở KCB, BHXH |
| 01/04/2026 | [QUA] | Mẫu 01/BH, 05/BH, 06/BH, 09/BH; danh mục 01–06/DM theo TT 12 | TT 12 Đ17 k1 | Cơ sở KCB, vendor |
| 15/05/2026 | [QUA] | NĐ 90/2026 xử phạt (Đ84–95 BHYT; Đ95 k1 c mượn tài khoản HIS; Đ95 k4 b không kết nối) | NĐ 90 | Cơ sở KCB, người hành nghề |
| 01/06/2026 | [QUA] | Phiếu hẹn, phiếu chuyển điện tử ký số của cơ sở thay đóng dấu | TT 06/2026 Đ5 k2 | Cơ sở KCB, vendor |
| 01/07/2026 | [QUA] | Mức hưởng ngoại trú 50% ở một số cơ sở (NĐ 188 Đ19 k2–4); QĐ 1931 sửa MUC_HUONG (BHYT-DATA) | NĐ 188 Đ19 | Cơ sở KCB, vendor |
| 01/08/2026 | [QUA] | Mã loại hình KCB, mã khoa theo QĐ 1804 (ảnh hưởng 01/BH, 07/BH) | QĐ 1804 (BHYT-DATA) | Vendor |
| **07/10/2026** | [TỚI] | Hết hạn góp ý dự thảo TT thay TT 48 (03 giờ) | DT-TT48 | Vendor, cơ sở KCB (góp ý) |
| Hằng tháng, ngày 15 | — | Gửi Bảng tổng hợp 01/BH tháng trước; BHXH gửi cảnh báo gia tăng chi | Luật Đ32 k2 a; TT 12 Đ9, Đ13 | Cơ sở KCB |
| Hằng quý, ngày 15 | — | Gửi Báo cáo quyết toán 02/BH quý trước; BHXH thông báo kết quả trong 30 ngày (quý 4: 60 ngày) | Luật Đ32 k2 a, b | Cơ sở KCB |
| **01/01/2027** | [TỚI] | Liên thông và sử dụng kết quả CLS giữa cơ sở KCB BHYT (luật định); dự kiến TT thay TT 48 có hiệu lực (gửi ≤ 03 giờ, có chế tài) | Luật 51 Đ3 k4; DT-TT48 | Mọi cơ sở KCB BHYT, vendor |

## 6. Chuỗi thay thế & bẫy trích dẫn của cụm

1. **NĐ 146/2018 (+75/2023, 02/2025) → NĐ 188/2025**: phần lớn hết hiệu lực 01/07/2025, toàn bộ 15/08/2025 (NĐ 188 Đ70 k4, k5). TT 01/2025 Đ4 k2 a vẫn dẫn "Điều 15 NĐ 146/2018". Theo TT 01 Đ15 k4, đọc sang điều tương ứng của NĐ 188 (Đ37–38).
2. **TT 48/2017 vẫn còn hiệu lực** và là căn cứ thời hạn gửi Bảng kê theo TT 12/2026 Đ9 k1. Đừng coi TT 48 đã bị thay chỉ vì có dự thảo.
3. **"Đ69 k9 NĐ 188" là điều khoản chuyển tiếp**, không phải điều về CNTT. Các điều về CNTT là Chương XI Đ66–68. Đ71 k2 d là nhiệm vụ của **Bộ Tài chính** ban hành biểu mẫu và trình tự giám định, được thực hiện bằng TT 12/2026. Đó không phải điều quy định "cổng".
4. **DT-BTC-CONG đã thành TT 12/2026/TT-BTC**. Đừng trích dự thảo riêng.
5. **Thẩm quyền giám định đã chuyển sang Bộ Tài chính** (TT 12). TT 12 không tuyên bãi bỏ quy trình giám định cũ của BHXH VN. Tình trạng các QĐ nội bộ cũ của BHXH VN: chưa xác minh, không nên trích.
6. **TT 01/2025 đọc riêng là bẫy**: mẫu phiếu ghi "đóng dấu". Từ 01/06/2026, bản điện tử dùng ký số của cơ sở (TT 06/2026 Đ5 k2).
7. **TT 12 tự dẫn tới văn bản đã chết**: Đ14 k6 dẫn NĐ 123/2020 và NĐ 70/2025 (đều hết hiệu lực 01/07/2026, thay bởi NĐ 254/2026). Mẫu 01/BH dẫn PL1 QĐ 824/2023 và Mẫu 07/BH dẫn PL6 QĐ 2010/2025 (cả hai bị QĐ 1804/2026 bãi bỏ từ 01/08/2026). Áp dụng văn bản thay thế theo TT 12 Đ17 k3.
8. **"6 lần khám trong 12 tháng"** là chữ của dự thảo cổng (báo chí). Bản gốc TT 12 Đ4 k2 dẫn TT 48 Đ6 k2 a: lịch sử 06 tháng gần nhất.
9. **"Xác thực dữ liệu" ≠ xác thực sinh trắc người bệnh**. Đó là ký số, xác thực hồ sơ chi phí của cơ sở (R18).
10. **"Chuyển tuyến" → "chuyển cơ sở KCB"** (Luật 51, TT 01). Tên bảng XML vẫn là "giấy chuyển tuyến" (BHYT-DATA).
11. **NĐ 117/2020 → NĐ 90/2026** (15/05/2026). Mức phạt ghi trong Chương II là mức **cá nhân**; tổ chức gấp đôi (NĐ 90 Đ4 k5). Trích mức phạt cho bệnh viện phải nhân 2.
12. **NĐ 166/2016 (GDĐT BHXH, BHYT)** là căn cứ ban hành TT 48. NĐ 164/2025 Đ27 k3 chỉ ghi "không áp dụng" NĐ 166 với GDĐT trong **BHXH bắt buộc, tự nguyện**. Phần BHYT của NĐ 166 còn áp dụng hay không: chưa xác minh (mục 7).
13. Ký hiệu điểm trong bản OCR NĐ 188 Đ35 k2 bị lặp "đ" hai lần. Thứ tự đúng là c (gửi dữ liệu, ký số, xác thực), d (hạ tầng, nâng cấp HIS), đ (rà soát chi phí tăng cao). Trích "Đ35 k2 d" cho nghĩa vụ nâng cấp HIS.

## 7. Chưa xác minh / cần luật sư / cần hỏi cơ quan

1. **Toàn văn DT-TT48**: chưa tìm thấy trên cổng BYT hoặc chinhphu.vn. Cần biết: danh sách "trường hợp được gửi chậm"; định nghĩa "kết thúc lượt KCB" với nội trú; cơ chế khóa dữ liệu sau 15 ngày; có quy định kiểm thử hoặc công nhận phần mềm không; có còn nghĩa vụ gửi song song lên Cổng BYT không. **Hỏi BYT (Vụ BHYT)**.
2. **Căn cứ xử phạt chậm gửi dữ liệu theo DT-TT48**: NĐ 90 không có hành vi "chậm gửi dữ liệu XML" (chỉ có Đ94 chậm báo cáo quyết toán và Đ95 k4 b "không kết nối, liên thông"). NĐ 90 Đ111 chỉ cho Giám đốc BHXH xử phạt vi phạm về đóng BHYT và Đ83–86, nên dự thảo nói "cơ quan BHXH thực hiện xử phạt" cần căn cứ mới. Suy luận, **cần luật sư**: chậm gửi hiện có bị quy vào Đ95 k4 b được không.
3. **Thủ tục "xác thực" kết nối HIS** (NĐ 188 Đ22 k2, Đ68 k5 b): không tìm thấy thủ tục chứng nhận hoặc kiểm thử phần mềm trong văn bản quy phạm. "Quy định của Bộ trưởng BYT" về tiêu chuẩn kết nối ở Đ22 k2 hiện là văn bản nào (TT 48? QĐ 130?). **Hỏi BHXH VN (Trung tâm CNTT) và BYT**. BHXH có môi trường test (sandbox) chính thức không: chưa xác minh.
4. **Số và ngày Công văn BHXH-CNTT kèm "Phụ lục 01 hướng dẫn liên thông dữ liệu theo QĐ 3176"** (bản đăng để trống số). Cần bản gốc từ BHXH VN. Thông tin về XSD `CHUKYDONVI` nằm trên mục Trợ giúp của Cổng (cần tài khoản).
5. **Cổng tiếp nhận dữ liệu y tế của Bộ Y tế** (TT 48 Đ7 k1 c; NĐ 188 Đ71 k1 c): còn vận hành và còn bắt buộc gửi song song không, quan hệ với HTTT quản lý KCB của TT 38/2024 (K5).
6. **TT 09/2026/TT-BTC**: chưa đọc bản gốc (điều khoản cụ thể về nghĩa vụ của cơ sở KCB, văn bản bị thay).
7. **Liên thông CLS 01/01/2027**: Luật 51 Đ3 k4 giao **Chính phủ** quy định, nhưng NĐ 188 không có nội dung này; dự thảo hiện có là thông tư của BYT. Nếu đến 01/01/2027 chưa có văn bản chi tiết thì nghĩa vụ áp dụng thế nào. **Cần luật sư** (phối hợp K7).
8. **QĐ 2555/QĐ-BYT** (thủ tục KCB BHYT): mới thứ cấp. Cần bản gốc để đối chiếu với NĐ 188 Đ37–38.
9. **Phần BHYT của NĐ 166/2016** còn hiệu lực không (xem mục 6 bẫy 12). Ảnh hưởng tới căn cứ của TT 48 và chuẩn GDĐT BHYT.
10. **Mẫu 02/BH** không nằm trong danh sách áp dụng từ 01/04/2026 ở TT 12 Đ17 k1, nhưng Đ17 k2 cho dùng mẫu cũ đến hết quyết toán quý I/2026. Suy ra áp dụng từ quyết toán quý II/2026. Đây là suy luận.
11. Bản TT 48 dùng ở đây là bản ký số VOffice BYT do TTYT Ninh Sơn đăng lại (OCR đọc số hiệu thành "49", ngày bị nhiễu). Nên thay bằng bản trên Công báo hoặc CSDL quốc gia về pháp luật nếu tìm được.
