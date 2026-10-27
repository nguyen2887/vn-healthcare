# Bộ câu hỏi phỏng vấn theo vai — khảo sát ngoại trú

> Kiểm tra lần cuối: 2026-10-27 · Phạm vi: phòng khám (dịch vụ / BHYT), khoa khám bệnh bệnh viện, chuỗi phòng khám · Nhãn và VP-id: `../business/variation-points.md` · Luồng tham chiếu: `../business/flows/ngoai-tru.md`

## Nguyên tắc hỏi

1. **Hỏi việc họ làm hôm qua**, không hỏi "quy trình của anh chị là gì". Người ta kể quy trình lý tưởng; kể hôm qua thì ra việc thật.
2. **Luôn hỏi ngoại lệ**: "khi nào thì không làm vậy?", "lần gần nhất bị trục trặc là gì?". Ngoại lệ là chỗ phần mềm hay vỡ.
3. **Đếm**: bao nhiêu lượt/ngày, bao nhiêu lần/tuần, mất bao lâu. Không có số thì ưu tiên sai.
4. **Xin xem màn hình và giấy** đang dùng; chụp ảnh mẫu in. Lời kể và giấy hay lệch nhau.
5. Câu 🪤 là câu **bẫy**: hỏi gián tiếp để lộ chỗ lệch chuẩn. Không hỏi thẳng "có vi phạm không".
6. Câu 📎 là câu **xin tài liệu**.
7. Điều họ nói là dữ liệu as-is, không phải sự thật về luật. Lệch luật chỉ ghi khi có ID trong `references/domains/`.

---

## 1. Tiếp đón / lễ tân

**Mục tiêu**: hiểu cách định danh người bệnh, luồng BHYT ở quầy, thời điểm thu tiền, hàng đợi, và nơi dữ liệu bị nhập hai lần. Đây là vai biết rõ nhất người bệnh "không chuẩn" (không giấy tờ, trẻ em, người nước ngoài, bỏ về).

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Sáng nay người bệnh đầu tiên đến, anh/chị làm những gì theo thứ tự, trên màn hình nào? | B1 |
| 2 | Tìm người bệnh cũ bằng gì: tên, SĐT, số thẻ, CCCD? Khi tìm ra hai hồ sơ cùng tên thì làm sao? 🪤 | VP-TD-01, VP-TD-02 |
| 3 | Người bệnh không mang giấy tờ gì, hoặc trẻ sơ sinh chưa có số định danh: tạo hồ sơ kiểu gì? Sau này có số thì ai gộp? | VP-TD-02, `SKDT-R10`, `SKDT-R11` |
| 4 | Người nước ngoài tuần trước đến khám, nhập thế nào? | `SKDT-R12` |
| 5 | Có photo hay scan CCCD/thẻ BHYT không? Vì sao? Ai yêu cầu? 🪤 | VP-TD-10, `BHYT-GD-R04` |
| 6 | Người bệnh BHYT đưa VNeID trên điện thoại, không có thẻ giấy: nhận không? Tra thẻ bằng gì, kết quả ghi vào đâu? | VP-TD-06, `BHYT-GD-R01`, `BHYT-GD-R02` |
| 7 | Lần gần nhất Cổng BHYT không tra được thì làm gì với người bệnh đang đứng đó? | `BHYT-GD-R03` |
| 8 | Người bệnh đến khám dịch vụ, khám xong mới đưa thẻ BHYT: có chuyển được không? Ai quyết? | VP-TD-07, `BHYT-GD-R06` |
| 9 | Thu tiền khám lúc nào — trước khi vào phòng hay sau? Có trường hợp nào không thu trước? 🪤 | VP-TD-08 |
| 10 | Số thứ tự cấp ở đâu, in ra hay đọc miệng? Ai gọi người bệnh vào phòng? | VP-TD-04 |
| 11 | Người già, thai phụ, trẻ nhỏ, cấp cứu: được ưu tiên bằng cách nào? Có ghi lại không? | VP-TD-05, `CHUYENKHOA-R39` |
| 12 | Người bệnh đặt hẹn trước chiếm bao nhiêu phần trăm? Hẹn qua kênh nào? Đến trễ xử lý sao? | VP-TD-03 |
| 13 | Giấy đồng ý xử lý thông tin cá nhân: người bệnh ký ở đâu, lúc nào? Trẻ em thì ai ký? | VP-TD-09, `DLCN-R03`, `DLCN-R08` |
| 14 | Khi anh/chị đi ăn trưa, ai ngồi quầy, đăng nhập bằng tài khoản nào? 🪤 | VP-DM-05, `BHYT-GD-R17` |
| 15 | Một ngày đông nhất bao nhiêu lượt? Khi đó bước nào tắc? | — |
| 16 | Ngoài phần mềm, còn ghi sổ hay Excel gì không? Ghi gì vào đó? 🪤 | — |
| 17 | 📎 Cho xem phiếu khám/phiếu tiếp đón đang in, sổ tiếp đón, mẫu đồng ý. | VP-GT-06 |

## 2. Bác sĩ

**Mục tiêu**: cách ghi hồ sơ thật (ai gõ, gõ lúc nào), chẩn đoán và mã ICD, chỉ định, kê đơn, ký, và điểm bác sĩ ghét nhất ở phần mềm hiện tại. Bác sĩ là người quyết định phần mềm sống hay chết sau go-live.

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Ca gần nhất hôm qua: từ lúc người bệnh vào đến lúc ra, anh/chị bấm những gì, viết tay những gì? | B4 |
| 2 | Khi đông bệnh, ai nhập bệnh sử và khám cho anh/chị? Nhập bằng tài khoản ai? Anh/chị ký lúc nào? 🪤 | VP-KH-03, `EMR-R04` |
| 3 | Lượt nào thì mở bệnh án ngoại trú, lượt nào chỉ phiếu khám và đơn? Ai quyết? | VP-KH-01, `EMR-R02` |
| 4 | Điều trị nhiều buổi (PHCN, YHCT, liệu trình) theo dõi thành một đợt hay từng lượt rời? | VP-KH-01 |
| 5 | Chẩn đoán gõ chữ hay chọn mã ICD? Có bệnh nào hay phải gõ tự do vì không tìm thấy mã? 🪤 | VP-KH-04, `MA-LT-R01` |
| 6 | Bệnh chính, bệnh kèm, biến chứng phân biệt thế nào trên màn hình? | `MA-LT-R03` |
| 7 | Có bao giờ cần sửa hồ sơ sau khi đã lưu/ký? Lần gần nhất là vì sao, sửa kiểu gì? 🪤 | VP-KH-06, `EMR-R10` |
| 8 | Chỉ định xét nghiệm/chụp: có bị phần mềm chặn dịch vụ nào không? Dịch vụ mới của cơ sở ai thêm vào? | VP-KH-05, `MA-LT-R14` |
| 9 | Trước khi chỉ định, anh/chị có xem kết quả cũ của người bệnh không? Khi nào chỉ định lại dù có kết quả cũ? | VP-CLS-04, `CLS-R06` |
| 10 | Dịch vụ ngoài BHYT hoặc theo yêu cầu: ai báo người bệnh phần phải trả thêm, lúc nào? 🪤 | VP-KH-11, `BHYT-GD-R35` |
| 11 | Kê đơn: thuốc hay dùng có mẫu sẵn không? Có khi nào kê xong người bệnh quay lại xin đổi thuốc — xử lý sao? 🪤 | VP-DT-01, VP-DT-02, `DUOC-R09` |
| 12 | Có kê thuốc gây nghiện/hướng thần không? Quy trình khác gì? | VP-DT-03, `DUOC-R07` |
| 13 | Phần mềm có cảnh báo dị ứng/tương tác không? Có từng cảnh báo sai làm anh/chị tắt luôn? | VP-DT-07, `DUOC-R34` |
| 14 | Anh/chị ký điện tử bằng gì: USB token, ký qua điện thoại, hay chưa ký? Ký từng phiếu hay ký dồn cuối buổi? 🪤 | VP-KH-08, `EMR-R06`, `DUOC-R11` |
| 15 | Người bệnh ký đồng ý thủ thuật bằng gì? | VP-KH-09, `EMR-R09` |
| 16 | Hẹn tái khám ghi ở đâu: trong đơn hay phiếu riêng? Giấy nghỉ hưởng BHXH ai ký? | VP-GT-01, VP-GT-02 |
| 17 | Người bệnh khám thêm chuyên khoa khác cùng ngày: anh/chị thấy được phần khám bên kia không? | VP-KH-07, VP-KH-10 |
| 18 | Ba điều phần mềm hiện tại làm anh/chị mất thời gian nhất? | — |
| 19 | 📎 Cho xem một bệnh án ngoại trú và một phiếu khám đã in (che tên người bệnh). | VP-KH-02 |

## 3. Điều dưỡng / thư ký y khoa

**Mục tiêu**: lộ phần "nhập hộ" và tài khoản chung, đo sinh hiệu, thực hiện thủ thuật, dẫn người bệnh đi CLS, và việc giấy tờ phát sinh sau khám. Điều dưỡng thường là người thực sự vận hành phần mềm.

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Hôm qua anh/chị đứng ở đâu, làm gì trên phần mềm? Đăng nhập tài khoản của ai? 🪤 | VP-KH-03, VP-DM-05 |
| 2 | Sinh hiệu đo ở đâu, ghi vào đâu? Ai nhập vào máy? | B3 |
| 3 | Phần nào trong bệnh án anh/chị nhập, phần nào bác sĩ nhập? Bác sĩ có xem lại trước khi ký không? 🪤 | `EMR-R04` |
| 4 | Thủ thuật tại phòng (tiêm, thay băng, khí dung): ghi nhận ở đâu, ai tính tiền? | VP-KH-09 |
| 5 | Người bệnh đi xét nghiệm/chụp: ai dẫn, họ cầm giấy gì, thu tiền ở đâu trước? | VP-CLS-02 |
| 6 | Kết quả CLS về, ai báo bác sĩ? Kết quả bất thường nặng thì sao? | VP-CLS-05, `CLS-R13` |
| 7 | Giấy nghỉ ốm, giấy hẹn, giấy chuyển: ai soạn, ai ký, in mấy bản? | VP-GT-01, VP-GT-02, `GIAYTO-R04` |
| 8 | Khi người bệnh xin sao bệnh án hoặc kết quả cũ, ai nhận yêu cầu, mất bao lâu? | VP-GT-05, `EMR-R14` |
| 9 | Người bệnh bỏ về giữa chừng không thanh toán: xử lý sao? | VP-VP-11, `BHYT-GD-R33` |
| 10 | Dữ liệu nào anh/chị phải nhập hai lần (phần mềm + sổ, hoặc hai phần mềm)? 🪤 | — |
| 11 | Bác sĩ nghỉ đột xuất, người bệnh đã lấy số: chuyển phòng kiểu gì? | VP-TD-04 |
| 12 | Cuối ngày anh/chị phải làm gì để "đóng sổ"? | B8 |
| 13 | 📎 Cho xem sổ ghi tay đang dùng ở phòng khám. | — |

## 4. Kỹ thuật viên cận lâm sàng

**Mục tiêu**: luồng mẫu/ca chụp từ chỉ định đến trả kết quả, máy nào nối phần mềm, ai duyệt kết quả, sửa kết quả, gửi ngoài. Chi tiết luồng: `../business/flows/cls.md`.

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Chỉ định đến chỗ anh/chị bằng cách nào: màn hình, giấy, người bệnh cầm phiếu? | VP-CLS-03 |
| 2 | Người bệnh chưa đóng tiền có được lấy mẫu/chụp không? Ai cho phép? 🪤 | VP-CLS-02 |
| 3 | Máy nào đẩy kết quả thẳng vào phần mềm, máy nào phải gõ tay? Gõ tay mất bao lâu/ca? | VP-CLS-03, `CLS-R17` |
| 4 | Ai ký duyệt kết quả trước khi trả? Có khi nào trả trước duyệt sau? 🪤 | `CLS-R13` |
| 5 | Kết quả đã trả mà phát hiện sai: sửa kiểu gì, người bệnh/bác sĩ biết không? | VP-CLS-05, `CLS-R14` |
| 6 | Giá trị nguy kịch: báo ai, bằng gì, có ghi lại không? | `CLS-R13` |
| 7 | Xét nghiệm nào gửi phòng xét nghiệm ngoài? Kết quả về bằng file, API hay giấy? Nhập lại vào đâu? | VP-CLS-01, `CLS-R08` |
| 8 | Phiếu kết quả in ra ghi tên người thực hiện, thời gian lấy mẫu không? | `CLS-R02`, `CLS-R12` |
| 9 | Kết quả trả cho người bệnh qua kênh nào (giấy, Zalo, app)? Ai gửi? Có xác nhận đúng người? | VP-CLS-06 |
| 10 | Nội kiểm/ngoại kiểm ghi ở đâu? Khi nội kiểm không đạt vẫn trả kết quả không? 🪤 | `CLS-R09`, `CLS-R11` |
| 11 | Chụp X-quang/CT: ảnh lưu ở đâu, in phim hay không, giữ bao lâu? | `CLS-R18`, `CLS-R20` |
| 12 | Chỉ định trùng (vừa làm tuần trước) có hay gặp không? Anh/chị có báo lại bác sĩ? | VP-CLS-04 |
| 13 | 📎 Cho xem một phiếu kết quả xét nghiệm và một phiếu CĐHA đã in; danh sách máy. | — |

## 5. Dược sĩ / quầy thuốc

**Mục tiêu**: có quầy cấp phát hay không, đối chiếu đơn, thay thuốc, kho lô/hạn, liên thông dược, thuốc kiểm soát đặc biệt. Chi tiết: `../business/flows/ke-don-cap-phat.md`.

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Quầy thuốc này của cơ sở hay thuê ngoài? Bán cho người ngoài không? | VP-DT-04 |
| 2 | Đơn đến quầy bằng gì: màn hình, mã đơn, giấy? Có đơn viết tay không? 🪤 | VP-DT-01, `DUOC-R04` |
| 3 | Khi cấp, anh/chị đối chiếu gì với đơn? Quét mã thuốc hay nhìn bằng mắt? | `DUOC-R20` |
| 4 | Thuốc trong đơn hết hàng: làm gì? Có đổi sang thuốc khác không, ghi lại ở đâu, báo bác sĩ không? 🪤 | VP-DT-05, `DUOC-R24` |
| 5 | Bệnh nhân cầm đơn từ nơi khác đến mua: nhập đơn kiểu gì? Thuốc kê đơn không có đơn thì sao? 🪤 | `DUOC-R22`, `DUOC-R23` |
| 6 | Nhập kho ghi lô, hạn dùng từng dòng không? Xuất theo lô nào? | VP-DT-06, `DUOC-R25` |
| 7 | Liên thông lên CSDL dược quốc gia đang làm bằng phần mềm nào? Có khớp với phần mềm khám không? | `DUOC-R26` |
| 8 | Có thuốc gây nghiện/hướng thần/tiền chất không? Sổ theo dõi, báo cáo, nhận lại thuốc thừa làm sao? | VP-DT-03, `DUOC-R18`, `DUOC-R19`, `DUOC-R30` |
| 9 | Thuốc nào thuộc thầu BHYT, thuốc nào ngoài thầu? Phân biệt ở đâu? | VP-DM-02 |
| 10 | Bệnh nhân trả lại thuốc, đổi thuốc đã bán: xử lý kho và hóa đơn thế nào? | VP-VP-08 |
| 11 | Hóa đơn quầy thuốc xuất từ máy tính tiền hay phần mềm viện phí? | `TC-MS-R06` |
| 12 | Kiểm kê bao lâu một lần, lệch thì xử lý sao? | — |
| 13 | 📎 Cho xem danh mục thuốc (Excel), một phiếu nhập kho, một đơn đã cấp phát. | VP-DM-02 |

## 6. Thu ngân

**Mục tiêu**: bảng giá thật đang dùng, thời điểm thu, phiếu thu/hóa đơn, hoàn tiền, gói, bảo lãnh, chốt ca. Chi tiết: `../business/flows/vien-phi-bhyt.md`.

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Một người bệnh dịch vụ hôm qua: thu mấy lần, mỗi lần ở bước nào? BHYT thì khác gì? | VP-TD-08, VP-CLS-02 |
| 2 | Có mấy bảng giá (BHYT, dịch vụ, theo yêu cầu, gói)? Khi giá đổi ai sửa, có hiệu lực từ khi nào? | VP-VP-01, `TC-MS-R17` |
| 3 | Mỗi lần thu có in phiếu thu không? Hóa đơn điện tử xuất lúc nào, cho ai? Cuối ngày có hóa đơn tổng hợp không? 🪤 | VP-VP-05, `TC-MS-R02` |
| 4 | Người bệnh BHYT trả phần cùng chi trả: phần mềm tự tính hay anh/chị nhập? Có khi nào tính lại bằng tay? 🪤 | VP-VP-03, `BHYT-GD-R10` |
| 5 | Trước khi thu tiền người bệnh BHYT có tra lại thẻ không? Ai bấm? | VP-VP-04, `BHYT-GD-R07` |
| 6 | Dịch vụ ngoài BHYT: người bệnh được báo phần chênh lệch ở đâu, có ký không? | VP-KH-11, `TC-MS-R18` |
| 7 | Hoàn tiền (hủy dịch vụ, chụp không được): ai duyệt, hoàn kiểu gì, hóa đơn đã xuất xử lý sao? | VP-VP-08, `TC-MS-R09` |
| 8 | Có bán gói/liệu trình trả trước không? Hóa đơn lập lúc thu hay lúc dùng? Người bệnh bỏ dở gói thì sao? | VP-VP-06, `TC-MS-R04` |
| 9 | Giảm giá, miễn phí cho ai? Ai quyết, ghi ở đâu? 🪤 | VP-VP-07 |
| 10 | Bảo lãnh viện phí với công ty bảo hiểm nào? Gửi hồ sơ cho họ bằng gì, người bệnh có ký giấy yêu cầu không? 🪤 | VP-VP-07, `TC-MS-R27`, `DLCN-R09` |
| 11 | Chuyển khoản/QR/thẻ: đối soát với ngân hàng ai làm, bao lâu một lần? | VP-VP-12, `TC-MS-R26` |
| 12 | Người bệnh hỏi "sao tốn nhiều vậy": anh/chị in được bảng chi tiết không? | `TC-MS-R20` |
| 13 | Bảng kê chi phí BHYT (01/KBCB) người bệnh ký bằng gì? | VP-VP-10, `BHYT-DATA-R21` |
| 14 | Chốt ca cần in gì, bàn giao tiền thế nào? Mấy ca một ngày? | VP-VP-13 |
| 15 | 📎 Bảng giá hiện hành (mọi loại), một phiếu thu, một hóa đơn, báo cáo chốt ca. | VP-VP-01 |

## 7. Kế toán / người làm BHYT và giám định

**Mục tiêu**: XML gửi Cổng khi nào, ai sửa hồ sơ lỗi, xuất toán gần đây vì gì, danh mục và thầu, quyết toán. Đây là nơi phần mềm "sai" được đo bằng tiền.

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Hồ sơ XML gửi Cổng lúc nào: ngay sau lượt, cuối ngày, hay cuối tháng? Ai bấm? 🪤 | VP-VP-09, `BHYT-GD-R19`, `BHYT-GD-R20` |
| 2 | Check-in (XML0) có gửi khi người bệnh bắt đầu khám không? | `BHYT-DATA-R03` |
| 3 | Cổng trả lỗi thì ai xem, sửa ở đâu, gửi lại bằng gì? Tháng trước bao nhiêu hồ sơ lỗi? | `BHYT-GD-R22`, `BHYT-DATA-R06` |
| 4 | Ba lý do xuất toán gần nhất là gì? Lỗi do phần mềm hay do người? 🪤 | `BHYT-GD-R23`, `BHYT-GD-R29` |
| 5 | File XML được ký số bằng chứng thư của ai? Đăng ký trên Cổng chưa? | `BHYT-DATA-R07` |
| 6 | Danh mục dịch vụ, thuốc, vật tư (Mẫu 01–06/DM) ai gửi BHXH duyệt, cập nhật bao lâu một lần? Có file Excel gốc? | VP-DM-01, VP-DM-02, `BHYT-GD-R28` |
| 7 | Cơ sở xếp cấp chuyên môn kỹ thuật nào, bao nhiêu điểm? Mức hưởng ngoại trú thay đổi 01/07/2026 đã cập nhật chưa? | VP-VP-03, `BHYT-GD-R10` |
| 8 | Cơ sở tư: giá BHYT lấy theo bảng giá HĐND tỉnh nào? Phần chênh lệch hạch toán ra sao? | VP-VP-02, `TC-MS-R18` |
| 9 | Báo cáo 01/BH, 02/BH lập từ phần mềm hay Excel? | `BHYT-GD-R25` |
| 10 | Giám định viên xin hồ sơ bệnh án, cung cấp trong bao lâu, bằng gì? | `BHYT-GD-R24` |
| 11 | Hóa đơn cho BHXH lập khi nào? | `TC-MS-R03` |
| 12 | Báo cáo gửi Sở Y tế hằng tháng/quý: mẫu nào, lấy số từ đâu, mất bao lâu? | VP-DM-07, `HTTT-BC-R23` |
| 13 | Sổ SKĐT VNeID: lượt không BHYT hiện có gửi không? Ai theo dõi tỷ lệ gửi? 🪤 | VP-GT-04, `SKDT-R01` |
| 14 | Đơn thuốc điện tử gửi Hệ thống đơn thuốc quốc gia: có báo cáo đơn chưa gửi không? | VP-DT-01, `DUOC-R12` |
| 15 | 📎 Biên bản giám định/quyết toán kỳ gần nhất, danh mục 01–06/DM, file kết quả thầu, một hồ sơ bị xuất toán. | — |

## 8. Chủ cơ sở / giám đốc

**Mục tiêu**: mục tiêu thật của dự án (tăng lượt, giảm xuất toán, qua thanh tra, mở chi nhánh), cái họ muốn thấy mỗi sáng, ràng buộc ngân sách/thời gian, ai có quyền chốt yêu cầu, kế hoạch tuân thủ các mốc sắp tới.

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Vì sao đổi/làm phần mềm lúc này? Điều gì xảy ra nếu 6 tháng nữa vẫn như cũ? | — |
| 2 | Mỗi sáng anh/chị muốn nhìn thấy con số nào? Hiện lấy số đó bằng cách nào, tin được không? | VP-DM-07 |
| 3 | Ba lần gần nhất bị thanh tra/giám định/khách phàn nàn là vì chuyện gì? 🪤 | — |
| 4 | Kế hoạch bệnh án điện tử trước 31/12/2026 đến đâu rồi? Ai phụ trách? | `EMR-R01`, `EMR-R02` |
| 5 | Có định mở thêm chi nhánh, thêm BHYT, thêm nội trú/ban ngày trong 1–2 năm không? | VP-DM-06 |
| 6 | Ai là người được quyền chốt "làm thế này" khi các khoa bất đồng? | — |
| 7 | Nhân sự nào sẽ ngồi học và cấu hình phần mềm? Họ có thời gian không? | — |
| 8 | Dữ liệu phần mềm cũ: cần chuyển hết, chuyển một phần hay giữ tra cứu? | — |
| 9 | Hợp đồng với vendor hiện tại: ai sở hữu dữ liệu, có lấy về được không? | `EMR-R26`, `TC-MS-R32`, `DLCN-R11` |
| 10 | Đã có bộ phận/người phụ trách bảo vệ dữ liệu cá nhân, hồ sơ DPIA chưa? | `DLCN-R13`, `DLCN-R20`, `DLCN-R21` |
| 11 | Quy chế bệnh án điện tử, quy chế ký số của cơ sở đã ban hành chưa? | `EMR-R25` |
| 12 | Có chính sách giảm giá, gói, hoa hồng giới thiệu nào phần mềm phải hỗ trợ? | VP-VP-06, VP-VP-07 |
| 13 | Ngân sách và mốc go-live mong muốn? Cái nào cứng hơn? | — |
| 14 | 📎 Giấy phép hoạt động, danh mục kỹ thuật được duyệt, hợp đồng BHYT, sơ đồ tổ chức. | VP-KH-05, VP-DM-03 |

## 9. IT / người quản trị phần mềm hiện tại

**Mục tiêu**: hiện trạng hệ thống, tích hợp đang có, dữ liệu cần di chuyển, tài khoản và phân quyền thật, hạ tầng, sự cố. Người này biết chỗ phần mềm cũ bị "chữa cháy" bằng tay.

| # | Câu hỏi | Gắn |
|---|---|---|
| 1 | Đang dùng những phần mềm nào (khám, kho, kế toán, HĐĐT, LIS, PACS, đơn thuốc QG, Cổng BHYT)? Cái nào nối với cái nào, nối kiểu gì? | VP-CLS-03, VP-VP-05 |
| 2 | Việc gì anh/chị phải làm bằng tay mỗi ngày/tuần để các hệ thống khớp nhau? 🪤 | — |
| 3 | Bao nhiêu tài khoản đang hoạt động, bao nhiêu người thật? Tài khoản người nghỉ việc đã khóa chưa? 🪤 | VP-DM-05, `EMR-R11` |
| 4 | Phân quyền hiện chia theo gì? Ai được xem toàn bộ hồ sơ? | VP-KH-07 |
| 5 | Máy chủ đặt ở đâu (tại chỗ, cloud VN, cloud nước ngoài)? Sao lưu bao lâu một lần, đã thử khôi phục chưa? | `EMR-R21`, `EMR-R26`, `DLCN-R15` |
| 6 | Chứng thư số: ai có, loại gì, hết hạn khi nào? Ký số tổ chức có chưa? | VP-KH-08, `EMR-R07`, `EMR-R08` |
| 7 | Nhật ký truy cập hồ sơ có không, giữ bao lâu, ai xem được? | `EMR-R12` |
| 8 | Sự cố gần nhất (mất mạng, mất điện, Cổng lỗi) xử lý sao, mất bao lâu? | `BHYT-GD-R03`, `BHYT-GD-R21` |
| 9 | Dữ liệu cũ xuất ra được định dạng gì? Có tài liệu cấu trúc không? | — |
| 10 | Danh mục (dịch vụ, thuốc, ICD, mã khoa) ai cập nhật, lấy nguồn từ đâu? | VP-DM-01, `MA-LT-R09` |
| 11 | Mẫu in nào đã tự chỉnh so với bản gốc của vendor? Vì sao? | VP-GT-06 |
| 12 | Cấp độ an toàn hệ thống thông tin đã xác định/phê duyệt chưa? | ANM (xem `applicability.md`) |
| 13 | 📎 Sơ đồ hệ thống, danh sách tài khoản theo vai, cấu hình tích hợp, tài liệu phần mềm cũ. | — |

---

## 15 câu "giờ đầu tiên" — khi chỉ gặp được một người

Dùng khi chỉ có một buổi với một người (thường là chủ hoặc quản lý). Mục tiêu: xác định loại cơ sở, các điểm biến thiên lớn, và danh sách người cần gặp tiếp.

1. Cơ sở là gì: phòng khám đa khoa/chuyên khoa, có BHYT không, có nội trú/ban ngày không, mấy chi nhánh? → chọn domain qua `applicability.md`, lọc VP.
2. Một ngày bao nhiêu lượt, bao nhiêu phần trăm BHYT, bao nhiêu phòng khám, bao nhiêu bác sĩ (cơ hữu/thỉnh giảng)?
3. Kể một ca người bệnh BHYT hôm qua từ cổng vào đến ra về: ai làm gì, ở đâu. (VP-TD, VP-VP)
4. Rồi một ca dịch vụ: khác chỗ nào? (VP-TD-08)
5. Thu tiền ở bước nào, mấy lần? (VP-TD-08, VP-CLS-02) 🪤
6. Ai gõ bệnh án thực tế, bác sĩ ký bằng gì, lúc nào? (VP-KH-03, VP-KH-08) 🪤
7. Xét nghiệm/chụp làm tại chỗ hay gửi ngoài? Máy có nối phần mềm không? (VP-CLS-01, VP-CLS-03)
8. Có quầy thuốc không, của ai? Đơn thuốc gửi lên quốc gia lúc nào? (VP-DT-04, VP-DT-01) 🪤
9. XML BHYT gửi lúc nào, tháng trước xuất toán bao nhiêu, vì gì? (VP-VP-09) 🪤
10. Hóa đơn điện tử xuất kiểu gì, nhà cung cấp nào? (VP-VP-05)
11. Có gói, liệu trình, giảm giá, bảo lãnh bảo hiểm không? (VP-VP-06, VP-VP-07)
12. Bệnh án điện tử trước 31/12/2026 tính thế nào? Ký số bác sĩ có chưa? (`EMR-R01`, `EMR-R02`, VP-KH-08)
13. Ba điều làm anh/chị bực nhất với phần mềm hiện tại; ba điều tuyệt đối không được mất khi đổi.
14. Mẫu giấy nào "không được sai một chữ" (giấy nghỉ, phiếu chuyển, bảng kê) và mẫu nào nội bộ? (VP-GT-06) 📎
15. Tuần tới tôi gặp được ai: một bác sĩ đông bệnh nhất, một điều dưỡng lâu năm, thu ngân ca sáng, người làm BHYT, IT? Xin trước: bảng giá, danh mục dịch vụ, danh mục thuốc, mẫu in, báo cáo tháng. 📎

Sau giờ đầu tiên, mọi điểm VP chưa được trả lời ghi vào bảng giả định với trạng thái **chưa xác nhận** — không tự điền bằng thông lệ như thể khách đã nói.
