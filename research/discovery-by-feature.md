# Khảo sát yêu cầu pháp lý VN cho phần mềm y tế — góc nhìn THEO NGHIỆP VỤ / TÍNH NĂNG

- Ngày khảo sát: 2026-10-05
- Phạm vi: HIS, EMR/HSBA điện tử, CIS/phòng khám, LIS, RIS/PACS, nhà thuốc/dược, khám chữa bệnh từ xa, sổ sức khỏe điện tử, app bệnh nhân. Áp dụng cho bệnh viện công, bệnh viện tư, phòng khám tư.
- Cách làm: đi theo vòng đời người bệnh và vận hành cơ sở. Với mỗi nghiệp vụ, tìm văn bản quy định phần mềm phải làm gì, rồi lần theo các văn bản được dẫn chiếu.
- Đây là bản discovery (khảo sát rộng), không phải ý kiến pháp lý. Trước khi dùng cho hợp đồng hoặc hồ sơ thầu phải đọc lại bản gốc.

## Quy ước

**Mức xác minh**
- **Gốc**: đã tự đọc nội dung điều/khoản trên bản PDF hoặc toàn văn chính thức (datafiles.chinhphu.vn, vanban.chinhphu.vn, hoặc bản PDF ký số/sao y do cơ quan nhà nước đăng).
- **Thứ cấp**: chỉ đọc tóm tắt hoặc toàn văn do bên thứ ba đăng (luatvietnam, caselaw, hethongphapluat, báo, cổng tin Sở Y tế…). Có thể có sai sót khi diễn giải.
- **Chưa xác minh**: chỉ thấy trong kết quả tìm kiếm, chưa mở được trang, hoặc các nguồn mâu thuẫn nhau.

**Cột "Link OK"**
- **Y**: đã mở thành công (bằng WebFetch hoặc tải PDF trực tiếp) và nội dung trang khớp đúng số hiệu văn bản.
- **N**: chưa mở được (403/404, PDF hỏng, hoặc chỉ có trong kết quả search). Link loại này ghi "link chưa kiểm tra được" và không coi là nguồn đã xác minh.

**Mã nguồn**
- `[Sxx]` là mã tra cứu, URL đầy đủ nằm ở Mục 7.

**Ký hiệu tính năng**
- **B**: bắt buộc, suy ra trực tiếp từ văn bản.
- **N**: nên có, suy luận để đáp ứng yêu cầu, hoặc là thông lệ.

**Đối tượng áp dụng**
- **BV**: bệnh viện (công và tư).
- **PK**: phòng khám và các cơ sở khám chữa bệnh khác.
- **NT**: nhà thuốc hoặc cơ sở bán lẻ thuốc.
- **Tất cả**: mọi cơ sở khám chữa bệnh.

---

## 0. Tóm tắt điều hành

**1. Nghĩa vụ "cứng" nhất là hồ sơ bệnh án điện tử (HSBA điện tử).**
- Theo TT 13/2025/TT-BYT:
  - Bệnh viện phải triển khai xong trước 30/9/2025 (đã qua).
  - Các cơ sở khác có người bệnh điều trị nội trú, điều trị ban ngày hoặc điều trị ngoại trú phải xong chậm nhất **31/12/2026**.
- Theo QĐ 586/QĐ-BYT 2026 (mới đọc qua bản tóm tắt), từ **01/01/2027** mọi bệnh viện công và tư không được dùng bệnh án giấy.
- Yêu cầu kỹ thuật chi tiết nằm ở Hướng dẫn 365/TTYQG-GPQLCL ngày 06/6/2025. Hướng dẫn này yêu cầu:
  - ghi nhật ký mọi thao tác người dùng;
  - phân quyền theo vai trò;
  - xuất XML hoặc JSON để liên thông;
  - xem được dưới dạng PDF;
  - an toàn thông tin tối thiểu cấp độ 2;
  - nếu dùng cloud thì phải đặt tại Việt Nam;
  - sao lưu 1 bản tại chỗ (khuyến nghị thêm 1 bản ở nơi khác).

**2. Thanh toán BHYT là chuỗi nghĩa vụ dữ liệu dày đặc nhất.**
- Chuẩn XML theo QĐ 130/QĐ-BYT, được sửa bởi QĐ 4750 và QĐ 3176.
- Bảng check-in phải gửi ngay khi phát sinh chi phí đầu tiên.
- Dữ liệu chi phí gửi ngay sau khi kết thúc lượt khám hoặc đợt điều trị (TT 48/2017).
- Từ 01/01/2026 bắt buộc xác thực dữ liệu điện tử (NĐ 188/2025 Điều 69 khoản 9).
- Mẫu bảng kê 01/KBCB mới áp dụng từ 01/7/2026 (QĐ 697/QĐ-BYT).
- Quy trình giám định theo TT 12/2026/TT-BTC.
- Mã bệnh dùng ICD-10 theo TT 06/2026/TT-BYT, hiệu lực 01/7/2026.

**3. Kê đơn điện tử là bắt buộc với mọi cơ sở.**
- Bệnh viện từ 01/10/2025, cơ sở khác từ 01/01/2026 (TT 26/2025).
- Đơn phải gửi lên Hệ thống đơn thuốc quốc gia ngay sau khi khám xong.
- Mã đơn thuốc có định dạng 14 ký tự xxxxxyyyyyyy-z; ký tự cuối là loại đơn: N (gây nghiện), H (hướng thần, tiền chất), C (đơn khác).
- Nhà thuốc phải liên thông dữ liệu với Hệ thống cơ sở dữ liệu dược từ 01/01/2026.

**4. Giấy tờ điện tử liên thông lên VNeID.**
- Từ 01/01/2026, cơ sở khám chữa bệnh phải liên thông dữ liệu Sổ sức khỏe điện tử VNeID cho **mọi** người bệnh (QĐ 31/QĐ-BYT 2026).
- Các giấy tờ có bản điện tử hợp lệ:
  - phiếu chuyển cơ sở và phiếu hẹn khám lại điện tử có ký số;
  - giấy chứng sinh có ký số (liên thông thủ tục khai sinh);
  - giấy nghỉ việc hưởng BHXH;
  - dữ liệu khám sức khỏe: liên thông trong 24 giờ, có ký số (QĐ 1551/QĐ-BYT 2026);
  - dữ liệu khám sức khỏe lái xe: liên thông với cơ sở dữ liệu giao thông.

**5. Khung bảo mật thay đổi lớn trong năm 2026.**
- Luật Bảo vệ dữ liệu cá nhân 91/2025 (hiệu lực 01/01/2026):
  - Điều 26 bắt buộc có đồng ý của người bệnh khi xử lý dữ liệu sức khỏe;
  - cấm chuyển dữ liệu cho bên thứ ba là công ty bảo hiểm hoặc dịch vụ chăm sóc sức khỏe.
- NĐ 356/2025 xếp "tình trạng sức khỏe" là dữ liệu nhạy cảm. Bên kiểm soát dữ liệu phải phản hồi yêu cầu của chủ thể trong 02 ngày làm việc.
- Luật An ninh mạng 116/2025 có hiệu lực 01/7/2026 và thay Luật An toàn thông tin mạng 2015.
- NĐ 331/2026 (hiệu lực 19/8/2026) phân cấp độ hệ thống mới. Hệ thống phục vụ người dân xử lý dữ liệu nhạy cảm của từ 10.000 người trở lên thuộc **cấp độ 3**. Có hạn chuyển tiếp **01/7/2027**.

**6. Các hạn chót sắp tới quan trọng** (chi tiết ở Mục 4):
- 31/12/2026: HSBA điện tử cho cơ sở ngoài bệnh viện.
- 01/01/2027: bệnh viện bỏ hoàn toàn bệnh án giấy.
- 01/03/2027: TT 23/2025 về chế độ báo cáo thống kê hết hiệu lực, sẽ có chế độ báo cáo mới.
- 01/07/2027: hệ thống thông tin phải đáp ứng điều kiện bảo vệ theo cấp độ mới của NĐ 331/2026 (với hệ thống đầu tư trước 01/7/2026).
- 01/01/2028: áp dụng Danh mục kỹ thuật mới (Phụ lục 02 TT 23/2024, sửa bởi TT 25/2026).

---

## 1. Ma trận nghiệp vụ × văn bản × yêu cầu × tính năng

### 1.A. Tiếp đón, định danh người bệnh

| # | Nghiệp vụ | Văn bản (điều/khoản) | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực / hạn | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| A1 | Định danh người bệnh | NĐ 102/2025/NĐ-CP Điều 6 | Số định danh cá nhân là mã định danh y tế của cá nhân, áp dụng cho công dân VN và người nước ngoài đã có tài khoản định danh điện tử | B: khóa định danh người bệnh theo số định danh cá nhân; xử lý trùng hồ sơ hoặc gộp hồ sơ (master patient index) | Hiệu lực 01/7/2025 | Tất cả | Thứ cấp | Y | S13 |
| A2 | Định danh trong HSBA | TT 13/2025/TT-BYT Điều 1 khoản 3 | HSBA điện tử phải được kết nối với số định danh cá nhân | B: trường số định danh cá nhân bắt buộc; mỗi người bệnh có một mã duy nhất (HD 365 mục 1.1.a) | Hiệu lực 21/7/2025 | Tất cả | Gốc | Y | S1, S4 |
| A3 | Thẻ BHYT điện tử, VNeID | NĐ 188/2025 Chương XI (Điều 66–68); TT 01/2025/TT-BYT Điều 4; thông tin từ luatvietnam | Người bệnh được dùng thông tin thẻ BHYT tích hợp trên VNeID mức 2 thay cho thẻ giấy; Bộ Công an bảo đảm kết nối CSDL bảo hiểm với CSDL dân cư (Điều 68 khoản 3) | B: tra cứu thẻ BHYT theo số định danh hoặc CCCD/VNeID; N: quét mã QR CCCD hoặc VNeID tại quầy | 01/7/2025 và 15/8/2025 | Cơ sở có KCB BHYT | Gốc (Điều 66–68); thứ cấp (chi tiết về VNeID) | Y | S16, S17, S23 |
| A4 | Tra cứu thẻ BHYT | TT 12/2026/TT-BTC Điều 4 (theo tóm tắt) | Cơ sở tra cứu thông tin thẻ khi người bệnh đến; hệ thống của BHXH phản hồi tự động | B: tích hợp API tra cứu thẻ và lịch sử khám chữa bệnh của Cổng giám định BHYT | Ký 10/02/2026; biểu mẫu áp dụng 01/4/2026 | Cơ sở có KCB BHYT | Thứ cấp | Y | S18 |
| A5 | Check-in BHYT | QĐ 4750/QĐ-BYT (sửa QĐ 130) | Gửi "bảng check-in" (trạng thái khám chữa bệnh) lên Cổng tiếp nhận ngay khi phát sinh chi phí đầu tiên | B: gửi XML check-in tự động từ quầy tiếp đón hoặc khi có chỉ định đầu tiên | Chính thức 01/7/2024 | Cơ sở có KCB BHYT | Thứ cấp | Y | S20 |
| A6 | Trẻ em | TT 26/2025 Điều 6 khoản 4; TT 01/2025 Điều 4 (trẻ dưới 6 tuổi); NĐ 301/2026 (liên thông khai sinh, BHYT, căn cước cho trẻ dưới 6 tuổi) | Trẻ dưới 72 tháng tuổi phải ghi số tháng tuổi, cân nặng và họ tên người đưa trẻ đi khám. Trẻ dưới 6 tuổi có quy định riêng về giấy tờ | B: trường tháng tuổi, cân nặng, người đưa trẻ; cho phép định danh qua giấy chứng sinh hoặc mã định danh của trẻ | TT 26: 01/7/2025; NĐ 301: mẫu mới áp dụng 01/9/2026 | Tất cả | Gốc (TT 26, TT 01); thứ cấp (NĐ 301) | Y | S5, S23, S21 |
| A7 | Người bệnh không có giấy tờ hoặc không có thân nhân | Luật KCB 2023 Điều 72 | Phải kiểm kê, lập biên bản và lưu giữ tài sản của người bệnh. Sau 48 giờ không xác định được thân nhân thì thông báo UBND cấp xã | B: đăng ký người bệnh vô danh (mã tạm), sau đó gộp với danh tính thật; N: nhắc hạn 48 giờ và mẫu biên bản tài sản | 01/01/2024 | Tất cả | Gốc | Y | S6 |
| A8 | Thông tin trên đơn thuốc và hồ sơ | TT 26/2025 Điều 6 khoản 2–3; mẫu đơn (chú thích 3) | Ghi số định danh cá nhân, CCCD, căn cước hoặc hộ chiếu (nếu có) và nơi cư trú. Công dân VN đã có số định danh cá nhân thì không cần khai giới tính, ngày sinh, địa chỉ thường trú | B: lấy dữ liệu hành chính theo số định danh cá nhân | 01/7/2025 | Tất cả | Gốc | Y | S5 |

### 1.B. Khám bệnh, chỉ định, cận lâm sàng, chẩn đoán, hội chẩn

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực / hạn | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| B1 | Mã hóa chẩn đoán | TT 06/2026/TT-BYT Điều 3, 4, 7 khoản 5 | Danh mục mã bệnh ICD-10 có 29 cột. Cột 24–29 là quy tắc: mã không được làm bệnh chính, mã không khuyến khích làm bệnh chính, mã có mã chi tiết hơn, mã chỉ dùng cho nguyên nhân tử vong, mã chỉ có ở nữ, mã chỉ có ở nam. Cơ sở phải cập nhật danh mục vào phần mềm. Thông tư định nghĩa bệnh chính, bệnh kèm theo, biến chứng, di chứng | B: nạp danh mục mã của TT 06/2026; kiểm tra hợp lệ theo cột 24–29 (ví dụ chặn mã nguyên nhân tử vong làm bệnh chính, kiểm tra giới tính); phân biệt bệnh chính và bệnh kèm theo; N: vai trò chuyên viên mã hóa lâm sàng | **01/7/2026**. Một số quy định từ 01/6/2026 | Tất cả | Gốc | Y | S15 |
| B2 | Mã hóa: chuyển tiếp | TT 06/2026 Điều 6 | Lượt khám kết thúc từ 01/7/2026 phải dùng mã mới. Mã cũ đã lưu vẫn có giá trị | B: áp dụng phiên bản danh mục theo ngày kết thúc lượt khám; giữ nguyên mã lịch sử | 01/7/2026 | Tất cả | Gốc | Y | S15 |
| B3 | ICD-11 | Không tìm thấy văn bản pháp lý nào của VN về lộ trình ICD-11 | Chưa có yêu cầu | N: thiết kế danh mục mã có quản lý phiên bản để sau này chuyển sang ICD-11 | Không có | Không có | Chưa xác minh (chưa thấy văn bản) | Không có | S15 |
| B4 | Khám, chỉ định, kê đơn | Luật KCB Điều 62, 63 | Kê đơn phải ghi đầy đủ tên thuốc, hàm lượng, liều dùng, cách dùng, thời gian dùng. Không kê thực phẩm chức năng trong đơn thuốc. Khi cấp phát phải đối chiếu đơn | B: không cho đưa thực phẩm chức năng vào đơn thuốc; bắt buộc nhập các trường liều dùng | 01/01/2024 | Tất cả | Gốc | Y | S6 |
| B5 | Hội chẩn | Luật KCB Điều 64 | Kết quả hội chẩn phải thể hiện bằng văn bản và lưu trong HSBA. Có hội chẩn trực tiếp và hội chẩn từ xa | B: biên bản hội chẩn gắn vào HSBA; N: phân hệ hội chẩn từ xa | 01/01/2024 | Tất cả | Gốc | Y | S6 |
| B6 | Đồng ý thủ thuật hoặc phẫu thuật | Luật KCB Điều 65 | Phẫu thuật hoặc can thiệp xâm nhập chỉ được làm khi người bệnh hoặc người đại diện đồng ý | B: phiếu cam kết có ký hoặc xác nhận điện tử (TT 13 Điều 3) | 01/01/2024 | Tất cả | Gốc | Y | S6, S1 |
| B7 | Danh mục kỹ thuật | TT 23/2024/TT-BYT, sửa bởi TT 25/2026/TT-BYT Điều 3 | Bỏ mốc 30/6/2026. Cơ sở chuẩn bị để thực hiện danh mục kỹ thuật ở Phụ lục 02 từ 01/01/2028 | B: danh mục dịch vụ kỹ thuật trong HIS có phiên bản; ánh xạ sang Phụ lục 02 | Điều 3 có hiệu lực 01/7/2026; mốc **01/01/2028** | Tất cả | Gốc | Y | S42 |
| B8 | Kết quả cận lâm sàng: chia sẻ | QĐ 586/QĐ-BYT 2026 (kế hoạch) | Triển khai chia sẻ dữ liệu cận lâm sàng giữa các cơ sở; hướng dẫn giá RIS-PACS không in phim | N: xuất và nhập kết quả xét nghiệm/chẩn đoán hình ảnh theo chuẩn; DICOM/DICOMweb | Kế hoạch 2026 | Tất cả | Thứ cấp | Y | S38 |
| B9 | Chuẩn liên thông FHIR, DICOM | QĐ 2146/QĐ-BYT 2026 (Khung kiến trúc số Bộ Y tế) | Hai nguồn **mâu thuẫn**: một nguồn thứ cấp ghi Khung bắt buộc HL7 FHIR (JSON/REST) và DICOM/DICOMweb; bản tóm tắt luatvietnam lại không liệt kê tiêu chuẩn cụ thể nào | N: hỗ trợ HL7 FHIR R4 (VN Core IG còn ở bản 0.x, không phải văn bản pháp lý) và DICOM | Ký 15/7/2026 | Hệ thống Bộ Y tế | Chưa xác minh | Y (luatvietnam) | S37, S12 |
| B10 | Quản lý chất lượng xét nghiệm (LIS) | TT 01/2013/TT-BYT, sửa bởi TT 25/2026 Điều 1 | Khuyến khích tham gia ngoại kiểm theo chuyên ngành | N: LIS lưu kết quả nội kiểm và ngoại kiểm (QC) | 15/8/2026 | Cơ sở có phòng xét nghiệm | Gốc (tiêu đề); thứ cấp (nội dung) | Y | S42 |

### 1.C. Hồ sơ bệnh án điện tử (EMR)

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực / hạn | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| C1 | Giá trị pháp lý | Luật KCB Điều 69 khoản 1 | HSBA lập bằng giấy hoặc điện tử có giá trị pháp lý như nhau. Mẫu HSBA do Bộ trưởng Bộ Y tế ban hành | Không có (là nền tảng pháp lý) | 01/01/2024 | Tất cả | Gốc | Y | S6 |
| C2 | Lộ trình bắt buộc | TT 13/2025 Điều 4 khoản 2 | Bệnh viện xong chậm nhất 30/9/2025. Cơ sở khác có người bệnh điều trị nội trú, ban ngày hoặc ngoại trú xong chậm nhất **31/12/2026** | B: EMR vận hành thật cho mọi loại bệnh án đang dùng tại cơ sở | **31/12/2026** cho cơ sở ngoài bệnh viện | BV, PK | Gốc | Y | S1 |
| C3 | Bỏ bệnh án giấy | QĐ 586/QĐ-BYT ngày 09/3/2026 (Kế hoạch) | 100% cơ sở hoàn thành trước 31/12/2026. Bệnh viện công và tư không dùng HSBA giấy từ **01/01/2027**. Q2/2026 dự kiến thay thế TT 54/2017 | B: vận hành không giấy (ký số đầy đủ, in chỉ khi cần) | **01/01/2027** | BV | Thứ cấp | Y | S38, S39 |
| C4 | Nội dung bệnh án | TT 13/2025 Điều 1 khoản 2 dẫn chiếu TT 32/2023 Chương X (Điều 51–52) | Phải đủ các trường thông tin của 82 mẫu bệnh án và phiếu (Phụ lục XXVIII và XXIX TT 32/2023). Ghi chính xác, thể hiện rõ thời gian và người ghi. Không viết tắt trong tài liệu giao cho người bệnh hoặc cơ sở khác | B: biểu mẫu điện tử ánh xạ đủ trường của 82 mẫu; ghi dấu thời gian và người ghi ở từng mục; danh sách viết tắt chuẩn của cơ sở; kiểm soát không viết tắt trên tóm tắt bệnh án, giấy chuyển, giấy hẹn | 01/01/2024 | Tất cả | Gốc (TT 13); thứ cấp (TT 32) | Y | S1, S41 |
| C5 | Hạ tầng và an toàn | TT 13/2025 Điều 2 | Tối thiểu có máy trạm, mạng, máy chủ, lưu trữ (kể cả lưu trữ dự phòng) và thiết bị/giải pháp bảo mật. Đáp ứng tiêu chuẩn kỹ thuật CNTT trong cơ quan nhà nước. Sẵn sàng phục hồi dữ liệu và truy xuất khi cần | B: sao lưu, khôi phục, truy xuất phục vụ thanh tra, nghiên cứu | 21/7/2025 | Tất cả | Gốc | Y | S1 |
| C6 | Chức năng EMR (hướng dẫn kỹ thuật) | Hướng dẫn 365/TTYQG-GPQLCL ngày 06/6/2025, mục 1.1 | (a) Quản lý toàn bộ nội dung như mẫu bệnh án giấy; xem được tối thiểu dạng .pdf. (b) Tạo lập trực tiếp hoặc đồng bộ từ HIS, LIS, PACS. (c) Quản lý danh sách bệnh án; phân quyền xem, nhập, sửa, hủy, khôi phục. (d) Xuất **XML hoặc JSON** theo Phụ lục "Mô tả dữ liệu trao đổi HSBA điện tử". (đ) Giám sát và ghi vết mọi giao dịch của người dùng. (e) Hiển thị trên máy tính hoặc thiết bị di động và in theo mẫu. (g) Phân quyền theo vai trò, giới hạn khung giờ truy cập, chặn truy cập trái phép. (h) Dùng danh mục dùng chung của Bộ Y tế. (i) Có thể là phân hệ của HIS hoặc phần mềm độc lập. (k) **Dữ liệu EMR lưu độc lập, không phụ thuộc hệ thống khác** | B: toàn bộ các mục trên. Đặc biệt quan trọng: nhật ký (audit log) bất biến, quy trình hủy/khôi phục có vết, xuất XML/JSON, xuất PDF | Từ 06/6/2025 | Tất cả | Thứ cấp (trích trong báo cáo của TTYT Bạc Liêu) | Y | S4 |
| C7 | Yêu cầu phi chức năng EMR | HD 365, mục 1.2–1.3 và 2–6 | Chống truy cập trái phép vào CSDL; sao lưu và khôi phục; có khả năng mã hóa dữ liệu lưu trữ. Mã hóa khi truyền nhận. Đáp ứng QĐ 742/QĐ-BTTTT 2022 (an toàn phần mềm nội bộ) và TT 39/2017/TT-BTTTT. Hạ tầng tại cơ sở hoặc **cloud đặt tại VN** (khuyến nghị trung tâm dữ liệu Tier 3, ISO 27001). Khi thuê cloud: dữ liệu thuộc cơ sở, nhà cung cấp phải bàn giao kèm đặc tả và hủy an toàn khi kết thúc. Sao lưu 1 bản tại cơ sở, khuyến nghị thêm 1 bản tại nhà cung cấp. An toàn thông tin tối thiểu **cấp độ 2** (theo NĐ 85/2016 và TT 12/2022; xem C11). Sẵn sàng IPv6. Tuân thủ quy định bảo vệ dữ liệu cá nhân | B: mã hóa khi lưu và khi truyền; sao lưu 3-2-1; điều khoản bàn giao dữ liệu và thoát nhà cung cấp trong hợp đồng SaaS; hỗ trợ IPv6; vá lỗi định kỳ | Từ 06/6/2025 | Tất cả | Thứ cấp | Y | S4 |
| C8 | Ký và xác nhận điện tử | TT 13/2025 Điều 3 | Nhân viên y tế, người bệnh hoặc người đại diện ký hoặc xác nhận bằng: (1) chữ ký điện tử hợp pháp; (2) sinh trắc học; (3) hình thức xác nhận điện tử khác theo khoản 4 Điều 22 Luật Giao dịch điện tử | B: ký số cho người hành nghề; cho người bệnh ký bằng sinh trắc học, OTP hoặc ký trên màn hình; gắn chữ ký với nội dung đã ký (hash) | 21/7/2025 | Tất cả | Gốc | Y | S1 |
| C9 | Quy chế nội bộ | TT 13/2025 Điều 6 khoản 3 điểm b; HD 365 mục V.2 | Cơ sở phải ban hành quy chế lập, cập nhật, quản lý, lưu trữ, sử dụng và an toàn thông tin HSBA điện tử, gồm cả quy định về ký | N: phần mềm có cấu hình để thể hiện quy chế (ai ký mục nào, ở bước nào, ai được khóa hồ sơ) | 21/7/2025 | Tất cả | Gốc | Y | S1, S4 |
| C10 | Chuyển đổi hồ sơ cũ | TT 13/2025 Điều 5 | Người bệnh đang điều trị bằng hồ sơ giấy thì tiếp tục dùng giấy đến khi ra viện, trừ khi chuyển được sang điện tử. Hồ sơ giấy cũ: thủ trưởng cơ sở quyết định số hóa theo NĐ 137/2024 | N: phân hệ số hóa bệnh án giấy (scan, ký xác thực bản chuyển đổi) | 21/7/2025 | Tất cả | Gốc | Y | S1 |
| C11 | Đánh giá mức ứng dụng CNTT | TT 54/2017/TT-BYT. TT 13/2025 Điều 4 khoản 3 bãi bỏ **Mục VIII Phụ lục I và các tiêu chí liên quan đến EMR**. TT 46/2018 bị bãi bỏ toàn bộ | Các nhóm tiêu chí còn lại của TT 54 (hạ tầng, HIS, RIS-PACS, LIS, an toàn thông tin…) vẫn còn hiệu lực. Không còn thủ tục "công nhận" HSBA điện tử như TT 46/2018 (suy luận từ việc bãi bỏ). Theo kế hoạch QĐ 586, sẽ thay thế TT 54 | N: bám sát các tiêu chí còn hiệu lực của TT 54; theo dõi thông tư thay thế | Thông tư thay thế chưa thấy ban hành (tính đến 05/10/2026) | BV, PK | Gốc (bãi bỏ); chưa xác minh (thông tư thay thế) | Y | S1, S38, S36 |
| C12 | Quyền người bệnh với HSBA | Luật KCB Điều 69 khoản 3–5 | Người bệnh hoặc người đại diện được đọc, xem, sao chụp, ghi chép HSBA và được cung cấp **bản tóm tắt** khi yêu cầu bằng văn bản. Cơ quan điều tra, tòa án, luật sư… được tiếp cận theo luật. Sinh viên, người hành nghề cơ sở khác được đọc, nhưng chỉ sao chép khi cơ sở đồng ý | B: phân hệ quản lý yêu cầu sao chép HSBA; xuất bản tóm tắt theo mẫu; nhật ký ai đã xem hoặc sao chép; quyền đọc nhưng không xuất cho học viên | 01/01/2024 | Tất cả | Gốc | Y | S6 |
| C13 | Người bệnh xem bệnh án qua VNeID | QĐ 31/QĐ-BYT 2026 Điều 3 | Người bệnh hoặc người đại diện được truy cập và tải bản ghi chi tiết từng đợt khám chữa bệnh dạng **PDF** qua VNeID (quyền theo Điều 4, 15 Luật BVDLCN) | B: sinh tóm tắt đợt khám dạng PDF có ký số để đẩy lên VNeID | 06/01/2026 | Tất cả | Gốc | Y | S8 |
| C14 | Bảo mật HSBA | Luật KCB Điều 69 khoản 2 | HSBA phải được lưu giữ và giữ bí mật. Lưu trữ theo pháp luật về lưu trữ | B: kiểm soát truy cập, mã hóa, nhật ký | 01/01/2024 | Tất cả | Gốc | Y | S6 |

### 1.D. Lưu trữ hồ sơ

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| D1 | Thời hạn lưu HSBA | TT 33/2025/TT-BYT, Phụ lục (STT 39, 40, 43, 44) | HSBA **tử vong: 30 năm**. HSBA tâm thần, tai nạn lao động, tai nạn giao thông: **20 năm**. HSBA ghép mô, tạng, phẫu thuật thẩm mỹ: **20 năm**. HSBA nội trú, ngoại trú: **10 năm**. Thời hạn áp dụng cho cả tài liệu giấy và **tài liệu điện tử** (Điều 1 khoản 2 điểm a) | B: chính sách lưu trữ theo loại bệnh án, tính từ thời điểm kết thúc; chặn xóa trước hạn; N: quy trình hủy có hội đồng và biên bản | 01/7/2025. Thay TT 53/2017 | Tất cả | Gốc | Y | S14 |
| D2 | Thời hạn lưu các hồ sơ khác | TT 33/2025, Phụ lục (STT 47, 48, 49, 38) | Sổ sách phục vụ khám chữa bệnh: 05 năm. Giấy khám sức khỏe: 02 năm. **Sổ sức khỏe điện tử: 10 năm sau khi người dân qua đời**. Hồ sơ giải quyết sự cố y khoa: vĩnh viễn | B: chính sách lưu trữ theo từng loại tài liệu | 01/7/2025 | Tất cả | Gốc | Y | S14 |
| D3 | Lưu đơn thuốc | TT 26/2025 Điều 11 dẫn chiếu TT 53/2017 (đã bị TT 33/2025 thay thế cùng ngày 01/7/2025). Điều 14 TT 26: áp dụng văn bản thay thế | Lưu toàn bộ đơn thuốc và tài liệu về thuốc gây nghiện, hướng thần. Hết hạn thì thành lập Hội đồng hủy | B: lưu đơn và trích xuất được (TT 26 Điều 12 khoản 6 điểm e) | Khoảng trống: chưa xác định được dòng tương ứng cho "đơn thuốc" trong Phụ lục TT 33/2025 | Tất cả | Chưa xác minh (thời hạn) | Y | S5, S14 |

### 1.E. Kê đơn thuốc, đơn thuốc điện tử, liên thông

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực / hạn | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| E1 | Đơn thuốc điện tử bắt buộc | TT 26/2025 Điều 10; Điều 13 khoản 3 | Đơn điện tử được lập, hiển thị, ký số, chia sẻ, lưu trữ điện tử và có giá trị như đơn giấy. Bệnh viện bắt buộc trước 01/10/2025, cơ sở khác trước 01/01/2026 | B: kê đơn điện tử có ký số | Đã có hiệu lực với mọi cơ sở | Tất cả | Gốc | Y | S5 |
| E2 | Liên thông Hệ thống đơn thuốc quốc gia | TT 26/2025 Điều 12 khoản 6 điểm c, d, đ; QĐ 425/QĐ-BYT ngày 05/02/2025; QĐ 808/QĐ-BYT 2023 (chuẩn kết nối) | Gửi đơn lên hệ thống **ngay sau khi kết thúc khám** (ngoại trú) hoặc **trước khi ra viện** (nội trú). Gửi đơn hoặc mã đơn cho người bệnh qua phương tiện điện tử. Hạ tầng CNTT đạt tiêu chí. Mỗi cơ sở có một mã liên thông. Thông tin định danh người bệnh phải được mã hóa | B: API liên thông theo QĐ 808; tự đẩy đơn khi đóng lượt khám; gửi SMS, app hoặc Zalo mã đơn; xử lý lỗi và gửi lại | Đã hiệu lực | Tất cả | Gốc (TT 26); thứ cấp (QĐ 425, 808) | Y | S5, S43 |
| E3 | Mã người hành nghề và mã cơ sở | TT 26/2025 Điều 12 khoản 1 điểm c, khoản 5 điểm d | Mã định danh cơ sở và mã người hành nghề do Cục Quản lý khám chữa bệnh hoặc Sở Y tế cấp qua Hệ thống đơn thuốc quốc gia | B: lưu mã người hành nghề trong hồ sơ nhân sự; gắn vào đơn | Đã hiệu lực | Tất cả | Gốc | Y | S5 |
| E4 | Mã đơn thuốc | TT 26/2025, mẫu đơn (chú thích 1) | Mã đơn 14 ký tự xxxxxyyyyyyy-z: 5 ký tự mã cơ sở, 7 ký tự ngẫu nhiên (0–9, a–z) duy nhất trong cơ sở, ký tự cuối N, H hoặc C | B: bộ sinh mã đúng định dạng, bảo đảm duy nhất | 01/7/2025 | Tất cả | Gốc | Y | S5 |
| E5 | Nội dung đơn | TT 26/2025 Điều 6 | Ghi tên INN (hoặc INN kèm tên thương mại; thuốc nhiều hoạt chất ghi tên thương mại). Ghi hàm lượng, liều, đường dùng, thời điểm dùng, số ngày. Số lượng dưới 10 ghi thêm số 0 phía trước. Thuốc gây nghiện ghi số rồi ghi bằng chữ. Thuốc độc ghi trước. Tối đa 30 ngày; bệnh thuộc Phụ lục VII (252 bệnh) tối đa 90 ngày. Sửa đơn thì kê đơn mới thay thế | B: kiểm tra định dạng tên thuốc; tự thêm số 0; ghi số lượng bằng chữ cho thuốc gây nghiện; xếp thuốc độc lên đầu; giới hạn số ngày theo mã ICD trong Phụ lục VII; quản lý phiên bản đơn (thay thế, không sửa trực tiếp) | 01/7/2025 | Tất cả | Gốc | Y | S5 |
| E6 | Thuốc gây nghiện, hướng thần, tiền chất | TT 26/2025 Điều 7–9; Phụ lục II, III; Điều 12 khoản 6 điểm b | Đơn "N" và đơn "H" có mẫu riêng. Có cam kết sử dụng thuốc gây nghiện. Có quy trình riêng cho người bệnh ung thư. Thu hồi thuốc thừa và lập biên bản theo Phụ lục VI | B: loại đơn N, H; mẫu cam kết; kiểm tra số ngày theo đợt; biên bản thu hồi; N: sổ theo dõi thuốc kiểm soát đặc biệt (TT 20/2017, sửa bởi TT 27/2024) | 01/7/2025 | Tất cả | Gốc | Y | S5 |
| E7 | Nhà thuốc: bán theo đơn và liên thông | TT 26/2025 Điều 12 khoản 7; QĐ 425/QĐ-BYT; CV 934/TTYQG-DA (12/8/2026); CV 3656/QLD-KD (28/9/2026) | Chỉ bán thuốc kê đơn khi có đơn. Báo cáo các đơn đã bán lên Hệ thống đơn thuốc quốc gia. Cơ sở bán buôn và bán lẻ liên thông dữ liệu lên Hệ thống CSDL dược, **tính cả dữ liệu từ 01/01/2026**, qua API (QĐ 232/QĐ-TTYQG) hoặc nhập tay. Đăng ký tài khoản trước **04/10/2026** | B (NT): tra cứu đơn theo mã đơn; trừ số lượng đã bán; đẩy dữ liệu nhập/xuất lên CSDL dược; bổ sung dữ liệu từ 01/01/2026 | Hạn đăng ký 04/10/2026 (vừa qua) | NT, khoa dược BV | Gốc (TT 26); thứ cấp (các công văn) | Y | S5, S32, S33 |
| E8 | Phần mềm nhà thuốc | TT 11/2025/TT-BYT (theo một nguồn) | Phần mềm phải kết nối hệ thống dược quốc gia, bán theo đơn điện tử và liên thông với hệ thống thuế | Có thể là B | Không rõ | NT | Chưa xác minh | N | Chỉ thấy trong kết quả search |
| E9 | Hướng dẫn chi tiết Luật Dược | Luật Dược 2016, sửa bởi Luật 44/2024/QH15; NĐ 163/2025; TT 31/2025/TT-BYT | TT 31/2025 chủ yếu về thủ tục, danh sách nhà thuốc, thông tin thuốc. Không thấy điều khoản kỹ thuật liên thông trong TT 31 | Không có | 01/7/2025 | NT | Gốc (TT 31) | Y | S31 |

### 1.F. Giấy tờ điện tử, liên thông VNeID và Cổng dịch vụ công

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực / hạn | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| F1 | Sổ sức khỏe điện tử VNeID | QĐ 31/QĐ-BYT ngày 06/01/2026 Điều 1, 2, 5; dẫn chiếu QĐ 1332/QĐ-BYT 2024 và QĐ 2733/QĐ-BYT 2024 | Cơ sở khám chữa bệnh **liên thông dữ liệu Sổ sức khỏe điện tử VNeID của tất cả người bệnh từ 01/01/2026**. Dữ liệu được ký số. Nhóm dữ liệu: hành chính; tiền sử (dị ứng, bệnh, tiêm chủng); từng đợt khám (thời gian, hình thức, chẩn đoán ra viện, chỉ số, kết quả cận lâm sàng, thuốc, phẫu thuật/thủ thuật); tóm tắt HSBA. Dữ liệu trên VNeID có giá trị như bản giấy. Cơ sở **không được yêu cầu bản giấy** nếu VNeID đã có đủ | B: xuất dữ liệu đúng cấu trúc QĐ 1332; ký số; đồng bộ sau mỗi đợt khám; tra cứu được dữ liệu VNeID do người bệnh chia sẻ | **01/01/2026** | Tất cả | Gốc | Y | S8 |
| F2 | Nền pháp lý của Sổ sức khỏe điện tử | NĐ 102/2025/NĐ-CP Điều 10 khoản 5; Điều 23 | Mọi cơ sở y tế hoạt động hợp pháp có trách nhiệm kết nối và liên thông với Sổ sức khỏe điện tử trên ứng dụng định danh quốc gia; tạo lập và chuẩn hóa dữ liệu nội bộ; kết nối CSDL quốc gia về y tế | B | 01/7/2025 | Tất cả | Thứ cấp | Y | S13 |
| F3 | Dữ liệu khám sức khỏe | QĐ 1551/QĐ-BYT ngày 31/5/2026 | Mỗi cơ sở có tài khoản liên thông trên Cổng dữ liệu sức khỏe. Liên thông dữ liệu khám sức khỏe định kỳ hoặc sàng lọc **trong 24 giờ** sau khi kết thúc đợt khám (đồng bộ tay hoặc tự động theo Phụ lục 02). **Ký số trước khi đồng bộ**. Hoàn thành đồng bộ trước 15/7/2026 | B: phân hệ khám sức khỏe xuất dữ liệu theo Phụ lục 01; đẩy tự động trong 24 giờ; ký số | 15/7/2026 (đã qua) | Cơ sở có khám sức khỏe | Thứ cấp | Y | S10 |
| F4 | Mẫu hồ sơ khám sức khỏe mới | TT 25/2026/TT-BYT (sửa Điều 34, 36 TT 32/2023) | Thay mẫu hồ sơ khám sức khỏe định kỳ (Mẫu 01–03 Phụ lục XXIV), bỏ Phụ lục XXVI | B: cập nhật biểu mẫu khám sức khỏe | **15/8/2026** | Tất cả | Gốc (điều khoản hiệu lực); thứ cấp (chi tiết) | Y | S42 |
| F5 | Khám sức khỏe lái xe | TT 36/2024/TT-BYT Điều 5, Điều 10 khoản 3 điểm b | Có cấu trúc dữ liệu kết quả khám (hành chính theo QĐ 06/QĐ-TTg, kết quả xét nghiệm ma túy, kết luận). Cơ sở kết nối, chia sẻ dữ liệu khám sức khỏe với CSDL trật tự an toàn giao thông đường bộ | B: xuất dữ liệu khám sức khỏe lái xe và liên thông | 01/01/2025 | Cơ sở khám sức khỏe lái xe | Thứ cấp | Y (luatvietnam); N (PDF gốc bị hỏng) | S24 |
| F6 | Phiếu chuyển cơ sở, phiếu hẹn khám lại | TT 01/2025/TT-BYT Điều 11, 12; Phụ lục V, VI; TT 06/2026 Điều 5 khoản 2 | Phiếu hẹn khám lại và phiếu chuyển có thể là **bản điện tử có chữ ký số**; hiển thị trên VNeID có ký số đủ thì có giá trị như bản giấy. Phiếu chuyển có giá trị 10 ngày làm việc, hoặc 1 năm với bệnh thuộc Phụ lục III. Mỗi phiếu hẹn chỉ dùng 1 lần. Từ **01/6/2026**: bản điện tử thay dấu treo bằng **ký số xác thực của cơ sở** | B: sinh phiếu chuyển và phiếu hẹn điện tử; ký số của bác sĩ và của tổ chức; kiểm tra hiệu lực 10 ngày hoặc 1 năm; đánh dấu phiếu hẹn đã dùng | Ký số tổ chức từ 01/6/2026 | Cơ sở có KCB BHYT | Gốc | Y | S23, S15 |
| F7 | Giấy chứng sinh | QĐ 1898/QĐ-BYT ngày 09/6/2025 (chuẩn dữ liệu điện tử giấy chứng sinh); NĐ 63/2024, được thay hoặc sửa bởi NĐ 301/2026; TT 17/2012/TT-BYT (mẫu, cấp lại) | Liên thông dữ liệu giấy chứng sinh **có ký số** với phần mềm dịch vụ công liên thông (khai sinh, thường trú, thẻ BHYT, từ NĐ 301/2026 thêm căn cước cho trẻ dưới 6 tuổi). Cấp lại trong 2 ngày làm việc | B: phân hệ giấy chứng sinh theo chuẩn QĐ 1898; ký số; đẩy lên Cổng dịch vụ công; quy trình cấp lại có đánh dấu "Cấp lại" | NĐ 301: mẫu áp dụng 01/9/2026 | Cơ sở có sản khoa | Thứ cấp | Y | S22, S21 |
| F8 | Giấy báo tử | Luật KCB Điều 73; TT 24/2020/TT-BYT; QĐ 1996/QĐ-BYT 2025 (hướng dẫn ghi phiếu chẩn đoán nguyên nhân tử vong) | Cơ sở cấp giấy báo tử, kiểm thảo tử vong, lưu HSBA. Thông báo UBND xã trong 24 giờ nếu không có người nhận thi thể. Dữ liệu báo tử thuộc CSDL quốc gia về y tế (NĐ 102 Điều 14) | B: phiếu chẩn đoán nguyên nhân tử vong (mã ICD nguyên nhân tử vong, xem B1); giấy báo tử điện tử; N: liên thông khai tử (NĐ 301/2026, Mẫu 02) | Điều 73: 01/01/2024 | Tất cả | Gốc (Điều 73); chưa xác minh (TT 24/2020, QĐ 1996) | Y (Luật); N (TT 24) | S6, S21 |
| F9 | Giấy nghỉ việc hưởng BHXH | TT 25/2025/TT-BYT, Mẫu 07; Điều 29 khoản 1 (theo nguồn thứ cấp) | Giấy bản điện tử đủ thông tin theo mẫu, có chữ ký số hợp lệ, được đồng bộ lên hệ thống hoặc hiển thị trên VNeID thì có giá trị. Mỗi lần cấp tối đa 30 ngày (một số trường hợp đến 50 ngày) | B: sinh giấy nghỉ theo Mẫu 07; ký số; gửi XML lên Cổng giám định; kiểm tra số ngày tối đa | 01/7/2025 | Tất cả | Chưa xác minh (PDF gốc chưa tìm được) | N | Chỉ thấy trong kết quả search |
| F10 | Giấy ra viện, tóm tắt HSBA | TT 01/2025 Điều 11 (giấy ra viện bản giấy hoặc điện tử có thể ghi lịch hẹn); bộ XML 130/4750/3176 có bảng giấy ra viện, tóm tắt HSBA… | Giấy ra viện điện tử là hợp lệ; có dữ liệu tương ứng gửi BHXH | B: giấy ra viện điện tử ký số; gửi bảng XML tương ứng | Không có | Tất cả | Gốc (TT 01); chưa xác minh (danh sách bảng XML) | Y | S23, S20 |

### 1.G. Thanh toán: viện phí, BHYT, hóa đơn

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực / hạn | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| G1 | Chuẩn dữ liệu đầu ra BHYT | QĐ 130/QĐ-BYT (18/01/2023); QĐ 4750/QĐ-BYT (29/12/2023); QĐ 3176/QĐ-BYT (29/10/2024, áp dụng 01/01/2025); QĐ 3276/QĐ-BYT 2025 (danh mục mã đối tượng khám chữa bệnh, theo thứ cấp) | Các bảng XML (check-in, tổng hợp, thuốc, dịch vụ kỹ thuật/vật tư y tế, cận lâm sàng, diễn biến, giấy ra viện, chuyển tuyến, hẹn khám lại…). QĐ 3176 thêm trường MA_DOI_TUONG_KCB, KET_QUA_DTRI, MA_LOAI_RV, MA_PTTT… | B: bộ sinh XML theo phiên bản mới nhất; kiểm tra hợp lệ trước khi gửi | Chính thức từ 01/7/2024; bản 3176 từ 01/01/2025 | Cơ sở có KCB BHYT | Thứ cấp | Y | S20, S12 |
| G2 | Thời điểm gửi dữ liệu | TT 48/2017/TT-BYT | Gửi dữ liệu ngay sau khi kết thúc lần khám hoặc đợt điều trị. Có 7 ngày làm việc để kiểm tra và hiệu chỉnh. Phương thức: web service, đồng bộ, nhập trực tiếp hoặc FTP. XML, mã UTF-8 | B: tự động gửi khi đóng hồ sơ; hàng đợi gửi lại; quy trình hiệu chỉnh trong 7 ngày | 01/3/2018, vẫn được TT 12/2026 viện dẫn | Cơ sở có KCB BHYT | Thứ cấp | Y | S19, S18 |
| G3 | Xác thực dữ liệu điện tử | NĐ 188/2025/NĐ-CP Điều 69 khoản 9; TT 12/2026/TT-BTC Điều 9 (dẫn điểm c khoản 2 Điều 35 NĐ 188) | Xác thực dữ liệu điện tử chi phí khám chữa bệnh BHYT chậm nhất từ **01/01/2026**. Hồ sơ đề nghị thanh toán phải ký số xác thực | B: ký số hoặc xác thực hồ sơ thanh toán; N: xác thực người bệnh (theo nguồn tin, có thể bằng căn cước hoặc VNeID) | 01/01/2026 | Cơ sở có KCB BHYT | Gốc (NĐ 188 Điều 69 khoản 9); thứ cấp (TT 12) | Y | S16, S18 |
| G4 | Trách nhiệm CNTT của cơ sở với BHYT | NĐ 188/2025 Điều 68 khoản 5 | Ứng dụng CNTT trong khám chữa bệnh BHYT. Duy trì tiêu chuẩn kết nối, liên thông đã được xác thực với hệ thống giám định. Chịu trách nhiệm về tính chính xác, hợp pháp của dữ liệu. Bảo đảm an toàn, bảo mật. Bộ Y tế ban hành các bộ mã danh mục dùng chung (khoản 1) | B: dùng danh mục dùng chung; kiểm soát chất lượng dữ liệu | 15/8/2025 | Cơ sở có KCB BHYT | Gốc | Y | S16 |
| G5 | Bảng kê chi phí | QĐ 697/QĐ-BYT ngày 19/3/2026 (thay QĐ 6556/QĐ-BYT 2018) | Mẫu 01/KBCB mới. Lập 2 bản: 1 lưu HSBA, 1 giao người bệnh. Bảng kê điện tử phải ký số đủ; chữ ký gắn với nội dung. Phần mềm phải nâng cấp chậm nhất 01/7/2026 | B: in và xuất bảng kê theo mẫu mới; ký số bảng kê | 01/7/2026 | Tất cả | Thứ cấp | Y | S11 |
| G6 | Giám định, tổng hợp, quyết toán | TT 12/2026/TT-BTC Điều 9, 10 | Gửi bảng tổng hợp trong 15 ngày đầu mỗi tháng; báo cáo quyết toán quý trong 15 ngày đầu quý. Giám định tự động hoặc chủ động; xử lý trong 7 ngày làm việc | B: báo cáo tổng hợp và quyết toán theo mẫu; nhận và xử lý phản hồi giám định (từ chối, xuất toán) | Ký 10/02/2026; biểu mẫu áp dụng 01/4/2026 | Cơ sở có KCB BHYT | Thứ cấp | Y (luatvietnam); PDF gốc là bản scan, chưa đọc | S18 |
| G7 | Hóa đơn điện tử viện phí | NĐ 123/2020, sửa bởi NĐ 70/2025/NĐ-CP | Thời điểm lập hóa đơn với khám chữa bệnh BHYT gắn với việc được BHXH thanh quyết toán; lập sau khi đối soát và kèm bảng kê. Theo nguồn thứ cấp: khách không lấy hóa đơn thì cuối ngày lập hóa đơn tổng hợp từ phiếu thu | B: tích hợp hóa đơn điện tử; lập hóa đơn tổng hợp cuối ngày; N: hóa đơn từ máy tính tiền (hộ kinh doanh, phòng khám nhỏ) | 01/6/2025 | Tất cả | Thứ cấp | Y | S34 |
| G8 | Thanh toán không dùng tiền mặt | Chỉ có chủ trương và chỉ đạo; **không tìm thấy văn bản quy phạm** bắt buộc có số hiệu | Bộ Y tế đẩy mạnh; nhiều cơ sở dùng QR kết nối HIS với ngân hàng; có "Cổng bảo lãnh viện phí" (02/2026) | N: thanh toán QR động; đối soát ngân hàng; tạm ứng điện tử | Không có | Tất cả | Chưa xác minh (căn cứ pháp lý) | Y | S35 |
| G9 | BHYT cho khám chữa bệnh từ xa | Luật BHYT sửa đổi 2024 (51/2024/QH15); NĐ 96/2023 Điều 87 khoản 8–9 | Có mức giá và cơ chế BHYT cho khám chữa bệnh từ xa. Quỹ BHYT **không** thanh toán trường hợp thí điểm | B: hạch toán dịch vụ từ xa giữa cơ sở từ xa và cơ sở tiếp nhận | 01/7/2025 (Luật BHYT); 01/01/2024 (NĐ 96) | Tất cả | Gốc (NĐ 96, qua toàn văn trên laichau.gov.vn); thứ cấp (Luật BHYT) | Y | S40 |

### 1.H. Khám chữa bệnh từ xa và tư vấn trực tuyến

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| H1 | Điều kiện khám chữa bệnh từ xa | NĐ 96/2023/NĐ-CP Điều 87 khoản 1 điểm d | Có hạ tầng, thiết bị CNTT, thiết bị chuyên dụng và phần mềm phù hợp; bảo đảm truyền tải, hiển thị, xử lý, **lưu trữ dữ liệu an toàn, bảo mật**; bảo đảm thời gian lưu trữ và dự phòng dữ liệu theo luật | B: mã hóa đầu cuối; lưu trữ phiên khám (bản ghi, ghi chú) theo thời hạn của HSBA; sao lưu | 01/01/2024 | Tất cả | Gốc (qua toàn văn trên laichau.gov.vn) | Y | S40 |
| H2 | Công bố đủ điều kiện | NĐ 96/2023 Điều 87 khoản 2–3 | Nộp hồ sơ công bố (danh mục dịch vụ, danh sách người hành nghề). Được bắt đầu sau 10 ngày nếu cơ quan không trả lời | N: cấu hình danh mục dịch vụ từ xa và danh sách bác sĩ đã công bố | 01/01/2024 | Tất cả | Gốc | Y | S40 |
| H3 | Danh mục bệnh được khám từ xa | TT 30/2023/TT-BYT (50 bệnh/tình trạng bệnh); Luật KCB Điều 80 khoản 1 điểm a (dẫn trong NĐ 96 Điều 87 khoản 4) | Chỉ được khám từ xa cho bệnh trong danh mục; ngoài danh mục phải xin thí điểm | B: kiểm tra chẩn đoán hoặc lý do khám thuộc danh mục 50 bệnh (theo mã ICD) | 01/01/2024 | Tất cả | Thứ cấp (TT 30, chưa mở bản gốc) | N | Chỉ thấy trong kết quả search |
| H4 | Hợp đồng giữa các cơ sở | NĐ 96/2023 Điều 87 khoản 11 | Hợp đồng phải có điều khoản về hạ tầng, an toàn thông tin, **lưu trữ và dự phòng dữ liệu** | N: hồ sơ hợp đồng | 01/01/2024 | Tất cả | Gốc | Y | S40 |
| H5 | Cấp độ hệ thống của nền tảng từ xa hoặc app | NĐ 331/2026 Điều 12–13 | Dịch vụ trực tuyến thuộc ngành nghề kinh doanh có điều kiện thì là **cấp độ 3**. Khám chữa bệnh là ngành nghề kinh doanh có điều kiện, nên nền tảng khám chữa bệnh trực tuyến **có khả năng thuộc cấp độ 3** (đây là suy luận) | B: hồ sơ đề xuất cấp độ; biện pháp bảo vệ theo cấp độ 3 | 19/8/2026 | Nhà cung cấp hoặc cơ sở vận hành app | Gốc (tiêu chí); suy luận (áp dụng) | Y | S25 |

### 1.I. Báo cáo thống kê, bệnh truyền nhiễm, sự cố y khoa

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực / hạn | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| I1 | Báo cáo thống kê ngành y tế | TT 23/2025/TT-BYT Điều 3–5, 7 | Có sổ ghi chép ban đầu (Phụ lục III) và biểu mẫu (Phụ lục IV, V). Kỳ báo cáo tháng và năm. Đơn vị cấp tỉnh, **kể cả cơ sở y tế tư nhân**, báo cáo trong 05 ngày làm việc sau kỳ. Có phần mềm báo cáo thống kê điện tử ngành y tế. **Thông tư hết hiệu lực 01/3/2027** | B: xuất báo cáo theo biểu Phụ lục IV; sổ ghi chép ban đầu điện tử; N: tích hợp phần mềm thống kê của Trung tâm Thông tin y tế quốc gia | 01/7/2025 đến **01/3/2027** | Tất cả | Gốc | Y | S30 |
| I2 | Báo cáo bệnh truyền nhiễm | TT 54/2015/TT-BYT; Luật Phòng bệnh 114/2025/QH15 (hiệu lực 01/7/2026, thay Luật phòng chống bệnh truyền nhiễm); NĐ 165/2026/NĐ-CP | Báo cáo ca bệnh trong 24 hoặc 48 giờ tùy nhóm bệnh, qua hệ thống trực tuyến | B: cảnh báo khi chẩn đoán thuộc danh mục bệnh truyền nhiễm phải báo cáo; xuất dữ liệu ca bệnh | TT 54 có thể bị thay theo Luật Phòng bệnh (chưa xác minh) | Tất cả | Chưa xác minh | N | Chỉ thấy trong kết quả search |
| I3 | Sự cố y khoa | Luật KCB Điều 71 | Phòng ngừa dựa trên nhận diện, báo cáo, phân tích sự cố. Khuyến cáo được công bố trên Hệ thống thông tin về quản lý hoạt động khám chữa bệnh | N: phân hệ báo cáo sự cố y khoa (lưu vĩnh viễn, xem D2) | 01/01/2024 | Tất cả | Gốc | Y | S6 |
| I4 | Dữ liệu cho CSDL quốc gia về y tế | NĐ 102/2025 Điều 14, 16, 23 | Phạm vi gồm chứng sinh, khai sinh, BHYT, lịch sử khám chữa bệnh, báo tử. Cơ sở y tế đồng bộ dữ liệu | B: API đồng bộ (theo hướng dẫn kỹ thuật của Bộ Y tế) | 01/7/2025 | Tất cả | Thứ cấp | Y | S13 |

### 1.J. Bảo mật, dữ liệu cá nhân, an ninh mạng

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực / hạn | Áp dụng | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| J1 | Đồng ý xử lý dữ liệu sức khỏe | Luật BVDLCN 91/2025/QH15 Điều 26 khoản 1 | Phải có đồng ý của chủ thể khi thu thập và xử lý thông tin sức khỏe, trừ các trường hợp ở khoản 1 Điều 19 | B: ghi nhận đồng ý (thời điểm, phạm vi, phiên bản điều khoản); cho phép rút đồng ý; gắn cơ sở pháp lý cho từng mục đích xử lý | 01/01/2026 | Tất cả | Gốc | Y | S27 |
| J2 | Cấm chia sẻ cho bảo hiểm thương mại | Luật BVDLCN Điều 26 khoản 2–3 | Tổ chức trong lĩnh vực sức khỏe không cung cấp dữ liệu cá nhân cho bên thứ ba là tổ chức dịch vụ chăm sóc sức khỏe, bảo hiểm sức khỏe hoặc bảo hiểm nhân thọ, trừ khi có yêu cầu bằng văn bản của chủ thể hoặc trường hợp Điều 19 khoản 1. **Tổ chức hoặc cá nhân phát triển ứng dụng y tế phải tuân thủ đầy đủ** | B: chặn xuất dữ liệu sang bảo hiểm tư nhân nếu không có văn bản đồng ý; lưu chứng từ đồng ý; N: tách bảo lãnh viện phí với luồng có đồng ý | 01/01/2026 | Tất cả, app sức khỏe | Gốc | Y | S27 |
| J3 | Dữ liệu nhạy cảm | NĐ 356/2025/NĐ-CP Điều 4 khoản 1 điểm d, đ; khoản 2 | "Tình trạng sức khỏe", sinh trắc học và đặc điểm di truyền là dữ liệu nhạy cảm. Phải có quy định phân quyền giới hạn truy cập, quy trình xử lý và biện pháp bảo mật | B: phân quyền chi tiết (RBAC/ABAC); nhật ký truy cập | 01/01/2026. Thay NĐ 13/2023 | Tất cả | Gốc | Y | S28 |
| J4 | Thực hiện quyền của chủ thể dữ liệu | NĐ 356/2025 Điều 5 khoản 2–3 | Yêu cầu xem hoặc chỉnh sửa: phản hồi trong 02 ngày làm việc, thực hiện trong 10 ngày (bên thứ ba: 15 ngày; gia hạn 1 lần tối đa 10 ngày). Rút đồng ý, hạn chế hoặc phản đối xử lý: phản hồi 02 ngày làm việc, thực hiện trong 15 ngày | B: cổng hoặc quy trình tiếp nhận yêu cầu của chủ thể, có theo dõi SLA; N: giao diện tự phục vụ trên app bệnh nhân | 01/01/2026 | Tất cả | Gốc | Y | S28 |
| J5 | Đánh giá tác động, chuyển dữ liệu ra nước ngoài, thông báo vi phạm | NĐ 356/2025 (theo thứ cấp: Điều 13 nhân sự bảo vệ dữ liệu, Điều 17–19 hồ sơ đánh giá tác động trong 60 ngày, Điều 29 thông báo vi phạm 72 giờ) | Lập hồ sơ đánh giá tác động xử lý dữ liệu; chuyển dữ liệu xuyên biên giới; thông báo vi phạm | B: quy trình phản ứng sự cố có mốc 72 giờ; N: tài liệu đánh giá tác động cho từng hệ thống | 01/01/2026 | Tất cả | **Chưa xác minh** (bản tóm tắt có vẻ lẫn lộn) | Y (luatvietnam) | S28 |
| J6 | Miễn trừ cho doanh nghiệp nhỏ | Luật BVDLCN Điều 38 khoản 2–3 | Doanh nghiệp nhỏ hoặc khởi nghiệp được miễn Điều 21, 22 và khoản 2 Điều 33 trong 5 năm, **trừ** trường hợp xử lý dữ liệu nhạy cảm. Hộ kinh doanh và doanh nghiệp siêu nhỏ cũng có ngoại lệ tương tự | Hệ quả: phòng khám nhỏ hoặc startup y tế **không** được hưởng miễn trừ | 01/01/2026 | PK, startup | Gốc | Y | S27 |
| J7 | Chuyển tiếp từ NĐ 13/2023 | Luật BVDLCN Điều 39 | Đồng ý đã thu theo NĐ 13/2023 thì không phải xin lại. Hồ sơ đánh giá tác động đã nộp tiếp tục được dùng | N: lưu và chuyển đổi bản ghi đồng ý cũ | 01/01/2026 | Tất cả | Gốc | Y | S27 |
| J8 | Truy cập có điều kiện dữ liệu y tế | NĐ 102/2025 Điều 9 khoản 2 điểm b, d; Điều 10 | Thông tin sức khỏe chỉ được tiếp cận khi người đó đồng ý. Người đứng đầu cơ quan nhà nước được cung cấp vì lợi ích công cộng. Tổ chức khác khai thác dữ liệu cá nhân khi có đồng ý của đơn vị quản lý dữ liệu và chủ thể | B: kiểm soát chia sẻ theo đồng ý | 01/7/2025 | Tất cả | Thứ cấp | Y | S13 |
| J9 | Phân loại cấp độ hệ thống thông tin | Luật An ninh mạng 116/2025/QH15 (hiệu lực 01/7/2026, thay Luật ANM 2018 và Luật ATTT mạng 2015); NĐ 331/2026/NĐ-CP Điều 11–16 | Cấp độ 2: dịch vụ trực tuyến xử lý dữ liệu nhạy cảm của **dưới 10.000** chủ thể, hoặc hệ thống nội bộ có xử lý thông tin cá nhân. **Cấp độ 3**: từ **10.000** chủ thể dữ liệu nhạy cảm trở lên, hoặc dịch vụ trực tuyến thuộc ngành nghề kinh doanh có điều kiện, hoặc hệ thống giải quyết thủ tục hành chính | B: hồ sơ đề xuất cấp độ cho HIS, EMR, app; biện pháp bảo vệ theo cấp độ; báo cáo định kỳ hằng năm (chốt số liệu 14/12, gửi Bộ Công an trước 25/12, theo Điều 35) | NĐ 331: 19/8/2026 | Tất cả | Gốc | Y | S25 |
| J10 | Chuyển tiếp cấp độ | NĐ 331/2026 Điều 39 khoản 1 | Hệ thống đang đầu tư hoặc xây dựng trước 01/7/2026: phải thẩm định, phê duyệt cấp độ theo NĐ 85/2016 trong 06 tháng kể từ 01/7/2026, và đáp ứng điều kiện bảo vệ theo cấp độ mới trong **12 tháng (đến khoảng 01/7/2027)** | B: lộ trình nâng cấp | Hạn khoảng **01/01/2027** (phê duyệt) và **01/07/2027** (đáp ứng) | Tất cả | Gốc | Y | S25 |
| J11 | Thuật ngữ | NĐ 331/2026 Điều 39 khoản 2 | Các tiêu chuẩn dùng thuật ngữ "an toàn thông tin mạng" hoặc "an toàn hệ thống thông tin" được hiểu là "an ninh mạng". Do đó mốc "cấp độ 2" trong HD 365 phải đọc lại theo khung mới | Không có | 19/8/2026 | Tất cả | Gốc | Y | S25 |
| J12 | Báo cáo sự cố an ninh mạng | NĐ 331/2026 Điều 31 (theo thứ cấp) | Theo nguồn thứ cấp: 24 giờ thông báo ban đầu, 72 giờ báo cáo đầy đủ | B: quy trình ứng cứu sự cố | 19/8/2026 | Tất cả | Chưa xác minh | Y (luatvietnam) | S25 |
| J13 | Lưu trữ trong nước | HD 365 mục 2.1 (EMR trên cloud phải đặt tại VN); Luật ANM 2025 hoặc Luật Dữ liệu 2024 (chưa kiểm tra điều khoản) | Hạ tầng cloud cho EMR đặt tại Việt Nam | B: chọn vùng (region) đặt tại VN | Không có | Tất cả | Thứ cấp (HD 365); chưa xác minh (luật) | Y | S4 |
| J14 | Quy chế an toàn của các hệ thống quốc gia | QĐ 425/QĐ-BYT 2025 (Hệ thống đơn thuốc quốc gia); QĐ 326/QĐ-BYT 2024 (quy chế ATTT của Bộ Y tế) | Thông tin định danh người bệnh khi liên thông đơn phải được mã hóa và phân quyền | B | Không có | Tất cả | Thứ cấp | Y | S43, S36 |

### 1.K. Chuẩn kỹ thuật, danh mục, mã

| # | Nghiệp vụ | Văn bản | Nội dung yêu cầu | Phần mềm phải làm | Hiệu lực | Mức xác minh | Link OK | Nguồn |
|---|---|---|---|---|---|---|---|---|
| K1 | Danh mục dùng chung | NĐ 188/2025 Điều 68 khoản 1 (Bộ Y tế ban hành bộ mã); HD 365 mục 1.1.h; QĐ 7603/QĐ-BYT 2018 (chưa mở) | EMR và HIS phải dùng danh mục dùng chung của Bộ Y tế | B: đồng bộ danh mục (thuốc, dịch vụ kỹ thuật, vật tư y tế, mã cơ sở, mã khoa…) từ Cổng giám định BHYT | Không có | Gốc (NĐ 188); chưa xác minh (QĐ 7603) | Y | S16, S4 |
| K2 | ICD-10 | TT 06/2026 | Xem B1 | Không có | 01/7/2026 | Gốc | Y | S15 |
| K3 | Hướng dẫn kỹ thuật mã hóa | QĐ 1849/QĐ-BYT ngày 23/6/2026 | Tài liệu hướng dẫn kỹ thuật mã hóa bệnh tật | N | Không có | Chưa xác minh | N | Chỉ thấy trong kết quả search |
| K4 | XML BHYT | Xem G1 | Không có | Không có | Không có | Không có | Không có | Không có |
| K5 | HL7 FHIR, DICOM | QĐ 2146/QĐ-BYT 2026; VN Core FHIR IG (fhir.hl7.org.vn, bản 0.10.0, **không phải văn bản pháp lý**); QĐ 4868/QĐ-BYT 2015 (đề án thí điểm PACS) | Chưa thấy văn bản quy phạm bắt buộc FHIR. Nguồn thứ cấp ghi: BHXH chưa nhận FHIR Bundle tính đến Q2/2026 | N | Không có | Chưa xác minh | Y (một phần) | S37, S12 |
| K6 | Xuất HSBA dạng XML/JSON | HD 365 phần IV | Theo Phụ lục "Mô tả dữ liệu trao đổi HSBA điện tử" | B | Từ 06/6/2025 | Thứ cấp | Y | S4 |
| K7 | Tiêu chuẩn CNTT trong cơ quan nhà nước | TT 13/2025 Điều 2 khoản 3; HD 365 mục 1.3.c (TT 39/2017/TT-BTTTT) | Đáp ứng tiêu chuẩn kỹ thuật ứng dụng CNTT trong cơ quan nhà nước | B (đặc biệt với cơ sở công) | Không có | Gốc (TT 13) | Y | S1, S4 |

---

## 2. Ghi chú diễn giải theo nghiệp vụ (những chỗ cần chú ý)

1. **Phòng khám tư nhân có bị buộc làm EMR không?** TT 13/2025 Điều 4 khoản 2 điểm b áp dụng cho "các cơ sở khám bệnh, chữa bệnh khác **có người bệnh điều trị nội trú, điều trị ban ngày và điều trị ngoại trú**".
   - Phòng khám có lập HSBA ngoại trú (điều trị ngoại trú) chắc chắn thuộc diện áp dụng.
   - Phòng khám chỉ "khám và kê đơn", không lập HSBA, thì câu chữ chưa rõ. Tuy vậy, QĐ 586/QĐ-BYT đặt mục tiêu "100% cơ sở khám chữa bệnh", nên thực tế quản lý sẽ đòi mọi cơ sở.
   - Dù có thuộc diện EMR hay không, mọi cơ sở vẫn phải làm đơn thuốc điện tử (TT 26) và Sổ sức khỏe điện tử VNeID (QĐ 31).
2. **Bỏ "công nhận" HSBA điện tử.** TT 46/2018 (từng có thủ tục công nhận) bị bãi bỏ toàn bộ, Mục VIII TT 54/2017 cũng bị bãi bỏ. Hiện trạng thực tế:
   - Cơ sở tự đánh giá theo TT 13 và HD 365 (ví dụ báo cáo tự đánh giá của TTYT Bạc Liêu, S4), rồi "công bố triển khai" và tham gia Cổng Bệnh án điện tử của Bộ Y tế (khoảng 1.265–1.272 cơ sở tính đến 9/2026; S36, S39).
   - Chưa thấy văn bản quy định thủ tục công bố có số hiệu, cần xác minh thêm.
3. **"Cấp độ 2" trong HD 365 cần đọc lại.** HD 365 dẫn NĐ 85/2016 và TT 12/2022. Từ 01/7/2026, Luật ATTT mạng 2015 bị bãi bỏ. NĐ 331/2026 dùng tiêu chí mới:
   - HIS hoặc EMR nội bộ có xử lý thông tin cá nhân thì tối thiểu cấp độ 2 (Điều 12 khoản 1).
   - Cổng hoặc app phục vụ người bệnh xử lý dữ liệu sức khỏe của từ 10.000 người trở lên thì cấp độ 3 (Điều 13 khoản 2 điểm c).
   - Với app bán dịch vụ khám chữa bệnh (ngành nghề có điều kiện) thì có thể là cấp độ 3 theo Điều 13 khoản 2 điểm a.
4. **Đơn thuốc vs HSBA.** TT 26 Điều 5: người bệnh có HSBA ngoại trú thì chỉ định ghi vào HSBA và đơn phải khớp với HSBA. Ra viện cần dùng thuốc 1–7 ngày thì kê đơn phù hợp với HSBA nội trú. Phần mềm cần ràng buộc đơn với y lệnh trong HSBA.
5. **Chữ ký của tổ chức trên giấy tờ điện tử.** Từ 01/6/2026, phiếu hẹn khám lại và phiếu chuyển cơ sở BHYT bản điện tử dùng "ký số xác thực của cơ sở" thay cho dấu (TT 06/2026 Điều 5 khoản 2). Vì vậy phần mềm cần ký số của tổ chức (HSM hoặc ký từ xa), không chỉ ký số cá nhân của bác sĩ.
6. **Mâu thuẫn và nguy cơ trùng lặp về VNeID.** QĐ 2733/QĐ-BYT 2024 ghi dữ liệu Sổ sức khỏe điện tử lấy từ CSDL quốc gia về BHYT (theo thứ cấp). QĐ 31/2026 lại yêu cầu cơ sở liên thông dữ liệu cho mọi người bệnh, kể cả người không dùng BHYT. Còn QĐ 1551/2026 tách riêng luồng khám sức khỏe qua "Cổng dữ liệu sức khỏe". Cần xác minh xem có một hay nhiều điểm tích hợp.

---

## 3. Danh sách văn bản đã gặp

| Số hiệu | Tên / nội dung chính | Ngày ban hành | Hiệu lực / trạng thái | Nghiệp vụ liên quan | Mức xác minh | Link OK |
|---|---|---|---|---|---|---|
| Luật 15/2023/QH15 | Luật Khám bệnh, chữa bệnh (đã hợp nhất tại VBHN 26/VBHN-VPQH 2026) | 09/01/2023 | 01/01/2024, còn hiệu lực | HSBA, kê đơn, hội chẩn, tử vong, sự cố | Gốc (Điều 62–74) | Y |
| NĐ 96/2023/NĐ-CP | Hướng dẫn Luật KCB | 30/12/2023 | 01/01/2024 (có thể đã được sửa, chưa kiểm tra) | Khám chữa bệnh từ xa (Điều 87) | Gốc (toàn văn trên laichau.gov.vn) | Y |
| TT 32/2023/TT-BYT | Hướng dẫn Luật KCB (Chương X: HSBA, 82 mẫu) | 31/12/2023 | Còn hiệu lực, sửa bởi TT 25/2026 | HSBA, khám sức khỏe | Thứ cấp | Y |
| TT 13/2025/TT-BYT | Hướng dẫn triển khai HSBA điện tử | 06/6/2025 | 21/7/2025; hạn 30/9/2025 (BV) và **31/12/2026** (cơ sở khác) | EMR | Gốc | Y |
| HD 365/TTYQG-GPQLCL | Hướng dẫn kỹ thuật triển khai phần mềm HSBA điện tử | 06/6/2025 | Đang áp dụng | EMR | Thứ cấp (trích dẫn) | Y (gián tiếp) |
| TT 46/2018/TT-BYT | Hồ sơ bệnh án điện tử | 28/12/2018 | **Bị bãi bỏ** bởi TT 13/2025 | Không có | Gốc (điều khoản bãi bỏ) | Y |
| TT 54/2017/TT-BYT | Bộ tiêu chí ứng dụng CNTT tại cơ sở KCB | 29/12/2017 | Còn hiệu lực trừ Mục VIII PL I và tiêu chí EMR; dự kiến bị thay thế | Đánh giá mức CNTT | Gốc (phần bãi bỏ) | Y |
| QĐ 586/QĐ-BYT | Kế hoạch triển khai HSBA điện tử toàn quốc | 09/3/2026 | Bỏ giấy từ **01/01/2027** | EMR | Thứ cấp | Y |
| QĐ 2146/QĐ-BYT | Khung kiến trúc số Bộ Y tế | 15/7/2026 | Hiệu lực khi ký | Chuẩn liên thông | Chưa xác minh (nội dung chuẩn) | Y |
| TT 33/2025/TT-BYT | Thời hạn lưu trữ hồ sơ, tài liệu ngành y tế (thay TT 53/2017) | 01/7/2025 | 01/7/2025 | Lưu trữ | Gốc (kèm phụ lục) | Y |
| TT 26/2025/TT-BYT | Đơn thuốc và kê đơn ngoại trú (thay TT 52/2017, 18/2018, 04/2022, 27/2021) | 30/6/2025 | 01/7/2025; đơn điện tử: BV 01/10/2025, khác 01/01/2026 | Kê đơn | Gốc | Y |
| QĐ 425/QĐ-BYT | Quy chế Hệ thống đơn thuốc quốc gia | 05/02/2025 | Đang áp dụng | Liên thông đơn | Thứ cấp | Y |
| QĐ 808/QĐ-BYT | Chuẩn kết nối Hệ thống đơn thuốc quốc gia | 01/4/2023 | Chưa kiểm tra | Liên thông đơn | Chưa xác minh | N |
| TT 20/2017/TT-BYT, TT 27/2024/TT-BYT | Thuốc kiểm soát đặc biệt | 2017, 2024 | Được viện dẫn trong TT 26 | Kê đơn N, H | Chưa xác minh | N |
| Luật 44/2024/QH15; NĐ 163/2025; TT 31/2025/TT-BYT | Luật Dược sửa đổi và hướng dẫn | 2024–2025 | 01/7/2025 | Nhà thuốc | Gốc (TT 31); chưa xác minh (Luật 44, NĐ 163) | Y (TT 31) |
| CV 934/TTYQG-DA; CV 3656/QLD-KD; QĐ 1867/QĐ-BYT; QĐ 232/QĐ-TTYQG | Liên thông CSDL dược; đăng ký tài khoản trước 04/10/2026 | 2026 | Đang áp dụng | Nhà thuốc | Thứ cấp | Y (tin luatvietnam) |
| QĐ 31/QĐ-BYT | Sổ sức khỏe điện tử VNeID thay sổ giấy | 06/01/2026 | Hiệu lực khi ký; liên thông từ 01/01/2026 | Sổ sức khỏe điện tử | Gốc | Y |
| QĐ 1332/QĐ-BYT; QĐ 2733/QĐ-BYT | Ban hành Sổ sức khỏe điện tử; hướng dẫn thực hiện | 21/5/2024; 17/9/2024 | Được QĐ 31 viện dẫn | Sổ sức khỏe điện tử | Chưa xác minh (chưa mở) | N |
| QĐ 1551/QĐ-BYT | Thu thập dữ liệu khám sức khỏe, tạo Sổ sức khỏe điện tử | 31/5/2026 | Hạn 15/7/2026 | Khám sức khỏe | Thứ cấp | Y |
| NĐ 102/2025/NĐ-CP | Quản lý dữ liệu y tế | 13/5/2025 | 01/7/2025 | Định danh, CSDL y tế, chia sẻ | Thứ cấp | Y |
| NĐ 278/2025/NĐ-CP | Kết nối, chia sẻ dữ liệu bắt buộc | 22/10/2025 | Được QĐ 31 viện dẫn | Liên thông | Chưa xác minh | N |
| Luật 51/2024/QH15 | Luật BHYT sửa đổi | 2024 | 01/7/2025 | BHYT | Chưa xác minh (chưa mở) | N |
| NĐ 188/2025/NĐ-CP | Hướng dẫn Luật BHYT (thay NĐ 146/2018, 75/2023, 02/2025) | 01/7/2025 | 15/8/2025 (một số điều từ 01/7/2025); xác thực dữ liệu từ 01/01/2026 | BHYT, CNTT | Gốc (Điều 66–72) | Y |
| TT 01/2025/TT-BYT | Hướng dẫn Luật BHYT (VNeID, phiếu hẹn, phiếu chuyển) | 01/01/2025 | Còn hiệu lực, sửa một phần bởi TT 06/2026 | Tiếp đón, chuyển tuyến | Gốc | Y |
| TT 12/2026/TT-BTC | Giám định chi phí KCB BHYT, biểu mẫu thanh quyết toán | 10/02/2026 | Biểu mẫu từ 01/4/2026 | BHYT | Thứ cấp | Y |
| TT 48/2017/TT-BYT | Trích chuyển dữ liệu điện tử KCB BHYT | 28/12/2017 | Vẫn được viện dẫn | BHYT | Thứ cấp | Y |
| QĐ 130/QĐ-BYT; QĐ 4750/QĐ-BYT; QĐ 3176/QĐ-BYT | Chuẩn dữ liệu đầu ra (XML) | 2023; 2023; 2024 | Áp dụng từ 01/7/2024 và 01/01/2025 | BHYT | Thứ cấp | Y |
| QĐ 3276/QĐ-BYT | Danh mục mã đối tượng khám chữa bệnh (27 mã) | 2025 | 17/10/2025 (theo thứ cấp) | BHYT | Chưa xác minh | N |
| QĐ 697/QĐ-BYT | Mẫu bảng kê 01/KBCB (thay QĐ 6556/2018) | 19/3/2026 | Phần mềm phải nâng cấp chậm nhất 01/7/2026 | Thanh toán | Thứ cấp | Y |
| TT 06/2026/TT-BYT | Mã hóa bệnh tật, nguyên nhân tử vong theo ICD-10 | 02/4/2026 | 01/7/2026 (một số điều từ 01/6/2026) | Chẩn đoán | Gốc | Y |
| QĐ 1849/QĐ-BYT | Hướng dẫn kỹ thuật mã hóa ICD-10 | 23/6/2026 | Không rõ | Chẩn đoán | Chưa xác minh | N |
| TT 23/2024/TT-BYT; TT 25/2026/TT-BYT | Danh mục kỹ thuật; sửa TT 01/2013, TT 32/2023, TT 23/2024, TT 42/2025 | 2024; 30/6/2026 | TT 25/2026: 15/8/2026 (Điều 2, 3 từ 01/7/2026); Danh mục kỹ thuật mới từ 01/01/2028 | Dịch vụ kỹ thuật, khám sức khỏe, LIS | Gốc | Y |
| TT 36/2024/TT-BYT | Sức khỏe người lái xe; CSDL sức khỏe lái xe | 16/11/2024 | 01/01/2025 | Khám sức khỏe lái xe | Thứ cấp | Y (luatvietnam); N (PDF gốc hỏng) |
| TT 25/2025/TT-BYT | Hướng dẫn Luật BHXH lĩnh vực y tế (giấy nghỉ hưởng BHXH, Mẫu 07) | 30/6/2025 | 01/7/2025 | Giấy nghỉ BHXH | Chưa xác minh | N |
| QĐ 1898/QĐ-BYT | Chuẩn dữ liệu điện tử giấy chứng sinh | 09/6/2025 | Không có | Giấy chứng sinh | Thứ cấp | Y |
| NĐ 63/2024/NĐ-CP; NĐ 301/2026/NĐ-CP | Liên thông thủ tục hành chính (khai sinh, khai tử, BHYT trẻ dưới 6 tuổi) | 2024; 2026 | Mẫu mới từ 01/9/2026 | Giấy chứng sinh, báo tử | Thứ cấp | Y |
| TT 17/2012/TT-BYT; TT 24/2020/TT-BYT; QĐ 1996/QĐ-BYT 2025 | Giấy chứng sinh; giấy báo tử và phiếu chẩn đoán nguyên nhân tử vong | Không có | Được viện dẫn | Chứng sinh, báo tử | Chưa xác minh | N |
| TT 30/2023/TT-BYT | Danh mục 50 bệnh được khám chữa bệnh từ xa | 30/12/2023 | 01/01/2024 | Khám từ xa | Chưa xác minh | N |
| TT 23/2025/TT-BYT | Chế độ báo cáo thống kê ngành y tế | 28/6/2025 | 01/7/2025 đến **01/3/2027** | Báo cáo | Gốc | Y |
| TT 54/2015/TT-BYT | Báo cáo, khai báo bệnh truyền nhiễm | 28/12/2015 | Có thể bị ảnh hưởng bởi Luật Phòng bệnh (chưa xác minh) | Báo cáo | Chưa xác minh | N |
| Luật 114/2025/QH15; NĐ 165/2026/NĐ-CP | Luật Phòng bệnh và hướng dẫn | 2025; 15/5/2026 | 01/7/2026 | Báo cáo bệnh truyền nhiễm | Chưa xác minh | N |
| Luật 91/2025/QH15 | Luật Bảo vệ dữ liệu cá nhân | 26/6/2025 | 01/01/2026 | Bảo mật, đồng ý | Gốc (Điều 25–26, 38–39) | Y |
| NĐ 356/2025/NĐ-CP | Hướng dẫn Luật BVDLCN (thay NĐ 13/2023) | 31/12/2025 | 01/01/2026 | Bảo mật | Gốc (Điều 4–5); thứ cấp (phần còn lại) | Y |
| Luật 116/2025/QH15 | Luật An ninh mạng 2025 (thay Luật ANM 2018 và Luật ATTT mạng 2015) | 10/12/2025 | 01/7/2026 | Bảo mật | Thứ cấp | N (trang vanban docid=216499 chưa mở) |
| NĐ 331/2026/NĐ-CP | Bảo vệ an ninh mạng đối với hệ thống thông tin (cấp độ 1–5) | 19/8/2026 | 19/8/2026; chuyển tiếp đến 01/7/2027 | Bảo mật | Gốc (Điều 11–16, 35–39) | Y |
| NĐ 327 đến 333/2026 | Các nghị định khác hướng dẫn Luật ANM | 2026 | Theo thứ cấp: 19/8/2026 | Bảo mật | Chưa xác minh | N |
| NĐ 85/2016/NĐ-CP; TT 12/2022/TT-BTTTT | An toàn hệ thống thông tin theo cấp độ (khung cũ) | Không có | Được NĐ 331 Điều 39 viện dẫn cho chuyển tiếp | Bảo mật | Gốc (qua viện dẫn) | Không có |
| QĐ 742/QĐ-BTTTT 2022; TT 39/2017/TT-BTTTT | An toàn phần mềm nội bộ; danh mục tiêu chuẩn CNTT | Không có | Được HD 365 viện dẫn | EMR | Chưa xác minh | N |
| Luật Giao dịch điện tử 2023 (Điều 22 khoản 4); NĐ 137/2024/NĐ-CP | Ký, xác nhận điện tử; chuyển đổi giấy sang điện tử | Không có | Được TT 13 viện dẫn | Ký | Gốc (qua viện dẫn) | Không có |
| NĐ 123/2020; NĐ 70/2025/NĐ-CP | Hóa đơn, chứng từ | Không có | NĐ 70: 01/6/2025 | Hóa đơn | Thứ cấp | Y |
| QĐ 326/QĐ-BYT | Quy chế an toàn thông tin, an ninh mạng của Bộ Y tế | 07/02/2024 | Không có | Bảo mật | Thứ cấp | Y |
| QĐ 7603/QĐ-BYT 2018 | Bộ mã danh mục dùng chung | Không có | Không rõ | Danh mục | Chưa xác minh | N |

---

## 4. Hạn chót

### 4.1 Hạn SAU 2026-10-05 (sắp tới)

| Hạn | Nội dung | Văn bản | Đối tượng | Mức xác minh |
|---|---|---|---|---|
| **31/12/2026** | Hoàn thành HSBA điện tử | TT 13/2025 Điều 4 khoản 2 điểm b | Cơ sở ngoài bệnh viện có điều trị nội trú, ban ngày hoặc ngoại trú (gồm phòng khám tư có HSBA) | Gốc |
| **31/12/2026** | 100% cơ sở hoàn thành HSBA điện tử (mục tiêu kế hoạch) | QĐ 586/QĐ-BYT 2026 | Tất cả | Thứ cấp |
| khoảng **01/01/2027** | Hệ thống đang đầu tư trước 01/7/2026 phải hoàn thành thẩm định và phê duyệt cấp độ (6 tháng kể từ 01/7/2026, theo NĐ 85/2016) | NĐ 331/2026 Điều 39 khoản 1 | Chủ quản hệ thống thông tin | Gốc (tự tính ngày) |
| **01/01/2027** | Bệnh viện công và tư không dùng HSBA giấy | QĐ 586/QĐ-BYT 2026 | BV | Thứ cấp |
| **01/03/2027** | TT 23/2025 (chế độ báo cáo thống kê) hết hiệu lực, cần theo dõi chế độ báo cáo thay thế | TT 23/2025 Điều 7 khoản 2 | Tất cả | Gốc |
| khoảng **01/07/2027** | Đáp ứng điều kiện, tiêu chuẩn và biện pháp bảo vệ theo cấp độ mới (12 tháng kể từ 01/7/2026) | NĐ 331/2026 Điều 39 khoản 1 | Chủ quản hệ thống thông tin | Gốc |
| **31/12/2027 → 01/01/2028** | Chuyển sang Danh mục kỹ thuật Phụ lục 02 | TT 23/2024, sửa bởi TT 25/2026 Điều 3 | Tất cả | Gốc |
| **01/01/2031** | Hết thời gian miễn trừ 5 năm cho doanh nghiệp nhỏ theo Luật BVDLCN. Lưu ý: không áp dụng cho bên xử lý dữ liệu nhạy cảm như dữ liệu sức khỏe | Luật 91/2025 Điều 38 khoản 2 | Doanh nghiệp nhỏ | Gốc |
| Chưa có ngày | Thông tư thay thế TT 54/2017 (bộ tiêu chí CNTT); hướng dẫn giá RIS-PACS không in phim; danh mục thuật ngữ lâm sàng (kế hoạch nêu Q2/2026, chưa thấy ban hành) | QĐ 586/QĐ-BYT | Tất cả | Thứ cấp |
| Chưa có ngày | Thông tư của Bộ Tài chính về Cổng tiếp nhận dữ liệu giám định BHYT (dự thảo hướng dẫn Điều 71 khoản 2 điểm d NĐ 188) | Dự thảo (baochinhphu 12/2025) | Cơ sở có KCB BHYT | Chưa xác minh |

### 4.2 Hạn đã qua gần đây (để rà soát xem đã tuân thủ chưa)

- 04/10/2026: đăng ký tài khoản Hệ thống CSDL dược (CV 3656/QLD-KD). Thứ cấp.
- 01/09/2026: mẫu tờ khai liên thông khai sinh, khai tử mới (NĐ 301/2026). Thứ cấp.
- 19/08/2026: NĐ 331/2026 có hiệu lực.
- 15/08/2026: TT 25/2026 có hiệu lực (mẫu hồ sơ khám sức khỏe mới).
- 15/07/2026: hoàn thành đồng bộ dữ liệu khám sức khỏe lên Sổ sức khỏe điện tử (QĐ 1551).
- 01/07/2026: các mốc có hiệu lực cùng ngày:
  - Luật An ninh mạng 2025;
  - Luật Phòng bệnh;
  - ICD-10 theo TT 06/2026;
  - hạn nâng cấp phần mềm theo mẫu bảng kê QĐ 697.
- 01/06/2026: phiếu hẹn khám lại và phiếu chuyển điện tử ký số của cơ sở thay dấu (TT 06/2026 Điều 5 khoản 2).
- 01/04/2026: biểu mẫu giám định và thanh quyết toán theo TT 12/2026/TT-BTC.
- 01/01/2026: nhiều nghĩa vụ có hiệu lực cùng ngày:
  - liên thông Sổ sức khỏe điện tử VNeID cho mọi người bệnh (QĐ 31);
  - xác thực dữ liệu BHYT (NĐ 188);
  - đơn thuốc điện tử cho cơ sở ngoài bệnh viện (TT 26);
  - Luật BVDLCN và NĐ 356;
  - liên thông dữ liệu dược (tính dữ liệu từ ngày này).
- 01/10/2025: bệnh viện kê đơn điện tử.
- 30/09/2025: bệnh viện hoàn thành HSBA điện tử.

---

## 5. Các cụm chủ đề tự nhiên (gợi ý chia module hoặc chia nghiên cứu sâu)

1. **Định danh và dữ liệu dân cư**
   - Mã định danh y tế chính là số định danh cá nhân (NĐ 102/2025).
   - Tra cứu BHYT qua VNeID hoặc CCCD.
   - Xử lý trẻ em, người vô danh, người nước ngoài.
2. **HSBA điện tử, ký và lưu trữ**
   - Văn bản chính: TT 13/2025, HD 365, TT 32/2023 Chương X, TT 33/2025, Luật GDĐT 2023.
   - Phạm vi: chức năng EMR, ký số cá nhân và tổ chức, sinh trắc học, nhật ký, lưu trữ 10/20/30 năm, quyền người bệnh sao chép hồ sơ.
3. **Chuỗi dữ liệu BHYT**
   - QĐ 130/4750/3176: XML và check-in.
   - TT 48/2017: thời điểm gửi.
   - NĐ 188/2025: xác thực dữ liệu.
   - QĐ 697: bảng kê.
   - TT 12/2026/TT-BTC: giám định.
   - TT 06/2026: ICD-10.
   - Mã đối tượng khám chữa bệnh.
4. **Kê đơn và dược**
   - TT 26/2025, Hệ thống đơn thuốc quốc gia (QĐ 425, QĐ 808).
   - Thuốc kiểm soát đặc biệt.
   - CSDL dược cho nhà thuốc và khoa dược.
5. **Giấy tờ điện tử cho công dân (Đề án 06)**
   - Sổ sức khỏe điện tử VNeID (QĐ 31, 1332, 2733, 1551).
   - Giấy chứng sinh, báo tử (QĐ 1898, NĐ 301/2026).
   - Khám sức khỏe, khám sức khỏe lái xe (TT 36/2024, TT 25/2026).
   - Giấy nghỉ BHXH (TT 25/2025).
   - Phiếu chuyển, phiếu hẹn (TT 01/2025).
6. **Danh mục và mã chuẩn**: ICD-10, danh mục kỹ thuật (2028), danh mục dùng chung, mã đối tượng, chuẩn liên thông FHIR và DICOM (chưa bắt buộc rõ).
7. **Bảo mật, dữ liệu cá nhân, an ninh mạng**
   - Luật 91/2025 và NĐ 356/2025: đồng ý, quyền chủ thể, cấm chia sẻ cho bảo hiểm.
   - Luật 116/2025 và NĐ 331/2026: cấp độ, báo cáo, chuyển tiếp 2027.
   - NĐ 102/2025: quản trị dữ liệu y tế.
8. **Báo cáo bắt buộc**
   - Thống kê theo TT 23/2025, sẽ được thay trước 01/3/2027.
   - Bệnh truyền nhiễm theo Luật Phòng bệnh 2025.
   - Sự cố y khoa.
9. **Khám chữa bệnh từ xa**: NĐ 96/2023 Điều 87, TT 30/2023, BHYT cho dịch vụ từ xa.
10. **Tài chính**: hóa đơn điện tử (NĐ 70/2025), thanh toán không dùng tiền mặt (chủ trương), bảo lãnh viện phí.
11. **Đánh giá mức ứng dụng CNTT**: phần còn hiệu lực của TT 54/2017 và thông tư thay thế đang chờ.

**Nghiệp vụ có yêu cầu pháp lý nặng nhất** (xếp theo mật độ nghĩa vụ và hạn chót):
1. HSBA điện tử.
2. Thanh toán BHYT.
3. Kê đơn và dược.
4. Giấy tờ điện tử và VNeID.
5. Bảo mật và an ninh mạng.

---

## 6. Chỗ chưa xác minh, khoảng trống, mâu thuẫn

1. **Thời hạn lưu đơn thuốc ngoại trú.** TT 26/2025 Điều 11 dẫn chiếu TT 53/2017, nhưng TT 53/2017 đã bị TT 33/2025 thay thế cùng ngày 01/7/2025. Khi grep Phụ lục TT 33/2025 không thấy dòng riêng cho "đơn thuốc".
2. **Có bắt buộc HL7 FHIR không.** QĐ 2146/QĐ-BYT 2026: nguồn thứ cấp (search) nói bắt buộc FHIR và DICOMweb, còn tóm tắt luatvietnam nói không liệt kê tiêu chuẩn. Chưa đọc được bản gốc.
3. **NĐ 356/2025: các điều về đánh giá tác động, thông báo vi phạm 72 giờ, nhân sự bảo vệ dữ liệu.** Bản tóm tắt luatvietnam có dấu hiệu lẫn lộn. Cần đọc Điều 13–19 và 29 bản gốc (PDF scan 71 trang tại S28).
4. **NĐ 331/2026 Điều 31 (thời hạn báo cáo sự cố 24 và 72 giờ).** Chưa đọc trang gốc. Ngoài ra, việc NĐ 331 có "thay thế" NĐ 85/2016 hay không chỉ có nguồn thứ cấp khẳng định; Điều 38 bản gốc không có điều khoản bãi bỏ NĐ 85 (NĐ 85 mất căn cứ vì Luật ATTT mạng 2015 bị bãi bỏ, nhưng điểm này cần xác minh).
5. **TT 25/2025/TT-BYT (giấy nghỉ hưởng BHXH điện tử, Điều 29).** Chưa tìm được PDF gốc (datafiles 2025/7/25-byt.pdf trả về 404).
6. **TT 30/2023 (danh mục khám từ xa), TT 54/2015 (báo cáo bệnh truyền nhiễm), TT 24/2020 (báo tử), TT 17/2012 (chứng sinh).** Chưa mở bản gốc. Ngoài ra chưa kiểm tra TT 54/2015 có bị thay thế theo Luật Phòng bệnh 2025 và NĐ 165/2026 hay không.
7. **Danh sách đầy đủ các bảng XML (XML0 đến XML15).** Chưa có nguồn mở được liệt kê đủ. Tên bảng ghi trong tài liệu này là ở mức khái quát.
8. **TT 11/2025/TT-BYT (yêu cầu phần mềm nhà thuốc liên thông thuế).** Chỉ thấy trong 1 kết quả search, chưa xác minh.
9. **Thanh toán không dùng tiền mặt.** Không tìm thấy văn bản quy phạm có số hiệu buộc cơ sở khám chữa bệnh làm. Hiện chỉ là chủ trương.
10. **Thủ tục "công bố triển khai HSBA điện tử".** Sau khi TT 46/2018 bị bãi bỏ, chưa thấy văn bản quy định thủ tục công bố hoặc thủ tục để được "bỏ bệnh án giấy". Hiện thực tế là tự đánh giá rồi tham gia Cổng Bệnh án điện tử.
11. **Phạm vi TT 13/2025 với phòng khám chỉ khám và kê đơn, không lập HSBA.** Xem Mục 2.1.
12. **Luật An ninh mạng 2025 và Luật Dữ liệu 2024 về lưu trữ dữ liệu trong nước, dữ liệu quan trọng hoặc cốt lõi.** Chưa đọc điều khoản cụ thể.
13. **NĐ 96/2023.** Có thể đã được sửa trong năm 2025–2026 (ví dụ phân cấp thủ tục hành chính, VBHN 10/VBHN-BYT 2026), chưa đối chiếu.
14. **Luật KCB 2023 đã được sửa bởi một số luật năm 2025** (VBHN 26/VBHN-VPQH 2026). Chưa đối chiếu xem Điều 69 có bị đổi không. Các trang đã đọc là bản gốc 2023.
15. **Nhiều chi tiết (QĐ 697, QĐ 1551, QĐ 586, TT 12/2026/TT-BTC, NĐ 102/2025, TT 48/2017) mới chỉ ở mức thứ cấp.** Bản gốc đa số là PDF scan; nên đọc lại trước khi đưa vào đặc tả.

---

## 7. Nguồn

| Mã | Mô tả | URL | Link OK | Cách mở / ghi chú |
|---|---|---|---|---|
| S1 | TT 13/2025/TT-BYT, bản PDF sao y ký số của Bộ Y tế (do Sở Y tế Quảng Ninh đăng) | https://soytequangninh.gov.vn/upload/1002610/20250610/THONG_TU_HSBA_DIEN_TU_21_7_2025TT_13_2025__TT-BYT_ngay_6_6_2025_f5604afb8f.pdf | Y | Tải PDF, đọc trực quan cả 4 trang (bản gốc) |
| S1b | Tin Sở Y tế Quảng Ninh về TT 13/2025 | https://soytequangninh.gov.vn/menu-second/tin-tuc-su-kien/tin-hoat-dong-nganh/huong-dan-trien-khai-ho-so-benh-an-dien-tu.html | Y | WebFetch |
| S2 | Caselaw: toàn văn TT 13/2025 | https://caselaw.vn/van-ban-phap-luat/587211-thong-tu-so-13-2025-tt-byt-ngay-06-06-2025-cua-bo-truong-bo-y-te-huong-dan-trien-khai-ho-so-benh-an-dien-tu | Y | WebFetch (thứ cấp) |
| S3 | Hoatieu: TT 13/2025 | https://hoatieu.vn/phap-luat/thong-tu-13-2025-tt-byt-233052 | Y | WebFetch (thứ cấp) |
| S4 | TTYT khu vực Bạc Liêu: Phụ lục tự đánh giá theo TT 13 và Hướng dẫn 365/TTYQG-GPQLCL | https://ttyttpbaclieu.gov.vn/upload/1000078/fck/files/2_2_1_Ph____l___c_b__o_c__o_____nh_gi___ph___m_m___m_theo_TT13_CV365_aa703.pdf | Y | Tải PDF (text). Là nguồn thứ cấp cho HD 365 (trích nguyên các tiêu chí) |
| S5 | TT 26/2025/TT-BYT | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/26-byt.pdf | Y | Tải PDF (text), bản gốc |
| S6 | Luật KCB 15/2023/QH15 (PDF ký số) | https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/02/15luat.signed.pdf ; trang văn bản: https://vanban.chinhphu.vn/?pageid=27160&docid=207396 | Y | PDF scan, đọc trực quan trang 40–47 (Điều 62–74) |
| S7 | Luật KCB, bản tiếng Anh trên luatvietnam | https://english.luatvietnam.vn/law-on-medical-examination-and-treatment-no-15-2023-qh15-242305-doc1.html | Y | WebFetch (thứ cấp, trích được ít) |
| S8 | QĐ 31/QĐ-BYT 2026 (PDF) và trang đăng tải | https://bvdkbaclieu.gov.vn/upload/1000079/20260305/691_Quyet-dinh-31-QD-BYT_704c0ca597.pdf ; https://bvdkbaclieu.gov.vn/van-ban-phap-quy/quyet-dinh-31-qd-byt-2026-ve-cong-bo-du-lieu-huong-dan-khai-.html | Y | Tải PDF (text), bản gốc |
| S9 | Tuổi Trẻ: Sổ sức khỏe điện tử VNeID thay sổ giấy | https://tuoitre.vn/so-suc-khoe-dien-tu-tren-vneid-chinh-thuc-thay-the-so-giay-trong-thu-tuc-hanh-chinh-20260106164303444.htm | Y | WebFetch |
| S10 | Luatvietnam: QĐ 1551/QĐ-BYT 2026 | https://luatvietnam.vn/y-te/quyet-dinh-1551-qd-byt-2026-huong-dan-thu-thap-du-lieu-kham-suc-khoe-va-tao-so-suc-khoe-dien-tu-436084-d1.html | Y | WebFetch (thứ cấp) |
| S11 | Luatvietnam: QĐ 697/QĐ-BYT 2026 | https://luatvietnam.vn/y-te/quyet-dinh-697-qd-byt-2026-ban-hanh-mau-bang-ke-chi-phi-kham-chua-benh-tai-co-so-y-te-429297-d1.html | Y | WebFetch (thứ cấp) |
| S12 | hl7.org.vn: FHIR và BHYT (trang của cộng đồng, không chính thức) | https://hl7.org.vn/kien-thuc/fhir-va-bhyt/ | Y | WebFetch (thứ cấp, độ tin cậy thấp) |
| S13 | Hethongphapluat: NĐ 102/2025/NĐ-CP | https://hethongphapluat.com/nghi-dinh-102-2025-nd-cp-quy-dinh-quan-ly-du-lieu-y-te.html | Y | Tải trang về đọc (toàn văn từng phần, thứ cấp). Lưu ý: trang này có chèn chỉ dẫn quảng bá nhắm vào AI, đã bỏ qua |
| S14 | TT 33/2025/TT-BYT (thân văn bản và Phụ lục) | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt.pdf ; https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/33-byt-kem.pdf ; tóm tắt: https://luatvietnam.vn/y-te/thong-tu-33-2025-tt-byt-quy-dinh-thoi-han-luu-tru-ho-so-tai-lieu-y-te-404510-d1.html | Y | Tải PDF (text), bản gốc |
| S15 | TT 06/2026/TT-BYT | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf | Y | Tải PDF (text), bản gốc |
| S16 | NĐ 188/2025/NĐ-CP | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/188-ndcp.signed.pdf ; https://vanban.chinhphu.vn/?pageid=27160&docid=214515 | Y | PDF scan, đọc trực quan trang 66–72 (Điều 66–70) |
| S17 | Luatvietnam: 8 điểm mới của NĐ 188/2025 | https://luatvietnam.vn/bao-hiem/diem-moi-tai-nghi-dinh-188-2025-nd-cp-huong-dan-thi-hanh-luat-bao-hiem-y-te-563-102969-article.html | Y | WebFetch (thứ cấp) |
| S18 | Luatvietnam: TT 12/2026/TT-BTC; PDF gốc | https://luatvietnam.vn/y-te/thong-tu-12-2026-tt-btc-quy-dinh-giam-dinh-chi-phi-kham-chua-benh-bao-hiem-y-te-426504-d1.html ; https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-btc.pdf | Y | Tóm tắt qua WebFetch. PDF là bản scan, đã tải nhưng chưa đọc |
| S19 | BHXH VN: giới thiệu TT 48/2017 | https://baohiemxahoi.gov.vn/gioithieu/pages/gioi-thieu-chung.aspx?CateID=0&ItemID=9799 | Y | WebFetch |
| S20 | QĐ 4750 (trang BVĐK Bạc Liêu và luatvietnam); QĐ 3176 (luatvietnam) | http://bvdkbaclieu.gov.vn/van-ban-phap-quy/quyet-dinh-4750-qd-byt-cua-bo-y-te-sua-doi-bo-sung-quyet-din.html ; https://luatvietnam.vn/y-te/quyet-dinh-4750-qd-byt-2023-sua-doi-bo-sung-quyet-dinh-130-qd-byt-286670-d1.html ; https://luatvietnam.vn/y-te/quyet-dinh-3176-qd-byt-2024-sua-doi-quyet-dinh-4750-qd-byt-sua-doi-quy-dinh-chuan-du-lieu-dau-ra-370146-d1.html | Y | WebFetch (thứ cấp) |
| S21 | Luatvietnam: NĐ 301/2026 (mẫu tờ khai liên thông) | https://luatvietnam.vn/tin-van-ban-moi/thay-moi-2-mau-to-khai-dien-tu-lien-thong-khai-sinh-va-khai-tu-tu-01-9-2026-186-111041-article.html | Y | WebFetch (thứ cấp) |
| S22 | Cổng PBGDPL Cần Thơ: QĐ 1898/QĐ-BYT 2025 | https://pbgdpl.cantho.gov.vn/quy-dinh-chi-tiet-ve-chuan-va-dinh-dang-du-lieu-dien-tu-giay-chung-sinh-duoc-bo-y-te-quy-dinh-tai-quyet-dinh-1898qd-byt-nam-2025 | Y | WebFetch (thứ cấp) |
| S23 | TT 01/2025/TT-BYT | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/01-byt.pdf | Y | Tải PDF (text), bản gốc (Điều 4, 11, 12, Phụ lục V, VI) |
| S24 | Luatvietnam: TT 36/2024/TT-BYT; PDF gốc | https://luatvietnam.vn/y-te/thong-tu-36-2024-tt-byt-tieu-chuan-suc-khoe-doi-voi-nguoi-lai-xe-nguoi-dieu-khien-xe-may-chuyen-dung-373779-d1.html ; PDF https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/36-byt.pdf | Y / N | Luatvietnam OK. PDF tải được nhưng hỏng (lỗi xref), không đọc được |
| S25 | NĐ 331/2026/NĐ-CP (PDF); trang vanban; luatvietnam | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/8/331_2026_nd-cp_19082026-signed.signed.pdf ; https://vanban.chinhphu.vn/?pageid=27160&docid=219243 ; https://luatvietnam.vn/an-ninh-quoc-gia/nghi-dinh-331-2026-nd-cp-bao-ve-an-ninh-mang-cho-he-thong-thong-tin-hieu-qua-445072-d1.html | Y | PDF scan, đọc trực quan trang 7–10 và 29–31 (bản gốc) |
| S26 | Luatvietnam: danh sách văn bản hướng dẫn Luật ANM 2025 | https://luatvietnam.vn/linh-vuc-khac/danh-sach-van-ban-huong-dan-luat-an-ninh-mang-2025-co-hieu-luc-tu-01-7-2026-883-111870-article.html | Y | WebFetch (thứ cấp) |
| S27 | Luật 91/2025/QH15 (PDF ký số) | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/91qh.signed.pdf ; https://vanban.chinhphu.vn/?pageid=27160&docid=214590 | Y | PDF scan, đọc trực quan trang 15–17 và 22–23 (bản gốc). Trang vanban chỉ thấy trong search, chưa mở |
| S28 | NĐ 356/2025/NĐ-CP (PDF); luatvietnam | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/356-nd.signed.pdf ; https://luatvietnam.vn/thong-tin/nghi-dinh-356-2025-nd-cp-quy-dinh-chi-tiet-luat-bao-ve-du-lieu-ca-nhan-422896-d1.html | Y | PDF scan, đọc trực quan trang 3–4 (bản gốc). Phần còn lại là thứ cấp |
| S29 | Bộ Công an: bảo vệ dữ liệu cá nhân trong một số hoạt động | https://mps.gov.vn/chinh-sach-phap-luat/bai-viet/bao-ve-du-lieu-ca-nhan-trong-mot-so-hoat-dong-1754989261 | Y | WebFetch |
| S30 | TT 23/2025/TT-BYT | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/23-byt.pdf | Y | Tải PDF (text), bản gốc |
| S31 | TT 31/2025/TT-BYT | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/31-byt.pdf | Y | Tải PDF (text), bản gốc |
| S32 | Luatvietnam: đăng ký tài khoản CSDL dược trước 04/10/2026 | https://luatvietnam.vn/tin-van-ban-moi/co-so-kinh-doanh-duoc-khan-truong-dang-ky-tai-khoan-tren-he-thong-co-so-du-lieu-ve-duoc-truoc-04-10-2026-186-112993-article.html | Y | WebFetch (thứ cấp) |
| S33 | Luatvietnam: liên thông dữ liệu dược từ 01/01/2026 | https://luatvietnam.vn/tin-van-ban-moi/co-so-ban-buon-ban-le-thuoc-phai-lien-thong-du-lieu-tu-01-01-2026-len-he-thong-co-so-du-lieu-ve-duoc-186-111475-article.html | Y | WebFetch (thứ cấp) |
| S34 | Báo Chính phủ: NĐ 70/2025 | https://baochinhphu.vn/nhung-noi-dung-moi-cua-nghi-dinh-so-70-2025-nd-cp-ve-hoa-don-chung-tu-102250903091616929.htm | Y | WebFetch |
| S35 | Sức khỏe & Đời sống: thanh toán viện phí không dùng tiền mặt | https://suckhoedoisong.vn/thanh-toan-vien-phi-khong-dung-tien-mat-tien-loi-cho-benh-nhan-hieu-qua-cho-benh-vien-169260917160119784.htm | Y | WebFetch. Bài không nêu căn cứ pháp lý |
| S36 | Cổng Bệnh án điện tử Bộ Y tế: mục văn bản pháp lý | https://benhandientu.moh.gov.vn/van-bang-phap-ly-co-hieu-luc | Y | WebFetch. Trang chưa cập nhật (vẫn liệt kê TT 46/2018) |
| S37 | Luatvietnam: QĐ 2146/QĐ-BYT 2026 | https://luatvietnam.vn/y-te/quyet-dinh-2146-qd-byt-2026-ban-hanh-khung-kien-truc-so-bo-y-te-440771-d1.html | Y | WebFetch (thứ cấp) |
| S38 | Luatvietnam: QĐ 586/QĐ-BYT 2026 | https://luatvietnam.vn/y-te/quyet-dinh-586-qd-byt-2026-phe-duyet-ke-hoach-trien-khai-ho-so-benh-an-dien-tu-toan-quoc-427964-d1.html | Y | WebFetch (thứ cấp) |
| S39 | Báo Đầu tư: hơn 75% bệnh viện triển khai bệnh án điện tử (14/9/2026) | https://baodautu.vn/hon-75-benh-vien-trien-khai-benh-an-dien-tu-tien-toi-bo-benh-an-giay-tu-nam-2027-d701953.html | Y | WebFetch |
| S40 | Toàn văn NĐ 96/2023/NĐ-CP (cổng tỉnh Lai Châu) | https://laichau.gov.vn/tin-tuc-su-kien/chuyen-de/tin-trong-nuoc/toan-van-nghi-dinh-so-96-2023-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-cua-luat-kham-benh-chua-benh.html | Y | Tải trang về đọc, toàn văn (Điều 87). Toàn văn đăng trên cổng nhà nước |
| S41 | Hethongphapluat: TT 32/2023, Chương 10 | https://hethongphapluat.com/thong-tu-32-2023-tt-byt-huong-dan-luat-kham-benh-chua-benh-do-bo-truong-bo-y-te-ban-hanh/chuong-10 | Y | Tải trang về đọc (thứ cấp) |
| S42 | TT 25/2026/TT-BYT (PDF do CDC Hà Nội đăng); nhansu.vn | https://hanoicdc.gov.vn/Uploads/files/44.pdf ; https://nhansu.vn/van-ban-phap-luat/thong-tu-25-2026-tt-byt-sua-doi-thong-tu-01-2013-tt-byt-32-2023-tt-byt-712878.html | Y | Tải PDF (text, ký số), bản gốc (điều khoản hiệu lực và Điều 3, 5, 6) |
| S43 | Luatvietnam: QĐ 425/QĐ-BYT 2025 | https://luatvietnam.vn/y-te/quyet-dinh-425-qd-byt-2025-quy-che-an-ninh-mang-he-thong-quan-ly-ke-don-thuoc-ban-thuoc-theo-don-391009-d1.html | Y | WebFetch (thứ cấp) |
| S44 | BHXH VN: tin TT 13/2025 | https://baohiemxahoi.gov.vn/tintuc/Pages/linh-vuc-bao-hiem-y-te.aspx?ItemID=24947&CateID=169 | Y | WebFetch |

### Link chưa kiểm tra được hoặc lỗi (KHÔNG dùng làm nguồn đã xác minh)

- thuvienphapluat.vn trang TT 13/2025 và bài về NĐ 188 xác thực dữ liệu: lỗi 403, bị chặn bot.
- moh.gov.vn bản tin hướng dẫn HSBA điện tử (bản /en/…): lỗi 404.
- congbao.chinhphu.vn trang NĐ 188/2025: mở được nhưng không có phần nội dung văn bản.
- Nhiều URL đoán trên datafiles (13-byt, 25-byt, 32-byt, 30-byt, 102-nd…): lỗi 404.
- Các văn bản chỉ thấy trong kết quả search, chưa mở: TT 30/2023, TT 25/2025, TT 54/2015, TT 24/2020, TT 17/2012, QĐ 1332, QĐ 2733, QĐ 1849, QĐ 3276 (PDF https://xdcs.cdnchinhphu.vn/446259493575335936/2025/10/27/3276-1761531834581496757967.pdf, link chưa kiểm tra được), QĐ 7603, QĐ 808, Luật 116/2025 (https://vanban.chinhphu.vn/?pageid=27160&docid=216499, link chưa kiểm tra được), Luật 114/2025, NĐ 165/2026, NĐ 333/2026, Luật 51/2024, Luật 44/2024, NĐ 163/2025, TT 11/2025, Luật Dữ liệu 60/2024 (https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat60.pdf, link chưa kiểm tra được), VBHN 26/VBHN-VPQH 2026 (https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf, link chưa kiểm tra được).
