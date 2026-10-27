# Điểm biến thiên giữa các cơ sở — và cách phân lớp

> Kiểm tra lần cuối: 2026-10-27 · Phạm vi đợt này: luồng ngoại trú (phòng khám, khoa khám bệnh), có hoặc không có BHYT. Nội trú: chưa làm.

File này là **cột sống nghiệp vụ** của skill. Nó trả lời câu hỏi mà mọi dự án phần mềm y tế đều vấp: *khách này khác "chuẩn" ở đâu, và chỗ khác đó được phép khác hay không?* Mỗi điểm biến thiên được xếp vào một trong ba lớp; lớp quyết định BA được làm gì với nó.

## Ba lớp — quy ước nhãn dùng trong toàn bộ `references/business/`, `elicitation/`, `deliverables/`

| Nhãn | Nghĩa | BA được làm gì | Nguồn chấp nhận |
|---|---|---|---|
| `[LUẬT]` | Pháp luật quy định; kèm ID yêu cầu (`EMR-R10`, `BHYT-GD-R19`…) trỏ về file domain | **Không được bỏ, không cho khách tắt.** Khách làm khác thì ghi là **lệch luật**, không phải "đặc thù" | Chỉ các file `references/domains/*.md` (đã có căn cứ và link). Không trích luật ở đây mà không có ID |
| `[THÔNG LỆ]` | Cách làm phổ biến ở nhiều cơ sở VN, không có văn bản bắt buộc. Có thể có hướng dẫn BYT không phải VBQPPL (vd QĐ 1313/2013 về quy trình khám bệnh tại khoa khám bệnh — hiệu lực chưa xác minh, chỉ áp dụng bệnh viện) | Dùng làm **mặc định** khi khách chưa nói gì; luôn ghi rõ là thông lệ, luôn xác nhận lại với khách | Kinh nghiệm triển khai, hướng dẫn ngành, quy chế mẫu. Phải ghi "(thông lệ)" |
| `[HỎI]` | Đặc thù từng cơ sở; không có mặc định đúng cho mọi nơi | **Phải hỏi khách**, không được giả định. Khi chưa có câu trả lời → ghi vào bảng giả định với trạng thái "chưa xác nhận" | Chỉ khách hàng |

Hai luật bất di bất dịch:
1. **Không có nhãn thì không được khẳng định.** Mọi câu "viện thường làm X", "phòng khám phải Y" trong đầu ra BA đều mang một trong ba nhãn.
2. **Tóm tắt không được chắc hơn chi tiết.** Một điểm `[HỎI]` chưa được khách trả lời thì ở phần tóm tắt cũng phải là "chưa xác nhận", không được viết như đã chốt.

Khi một điểm có cả phần luật lẫn phần tùy chọn (rất hay gặp), tách làm hai dòng: phần cứng `[LUẬT]`, phần mềm `[HỎI]`. Ví dụ: tra thẻ BHYT trước khi kết thúc lượt là `[LUẬT]` (`BHYT-GD-R07`); ai bấm nút tra — thu ngân hay bác sĩ — là `[HỎI]`.

## Dùng file này thế nào

- **Trước khảo sát**: lọc các dòng theo loại cơ sở, lấy cột "Câu hỏi" ghép với bộ câu hỏi theo vai trong `references/elicitation/questions-by-role.md`.
- **Sau khảo sát**: mỗi dòng `[HỎI]` phải có câu trả lời hoặc nằm trong bảng giả định. Mỗi dòng `[LUẬT]` mà khách đang làm khác → lỗi tuân thủ trong gap analysis.
- **Bàn giao cho thiết kế**: bảng này (đã điền câu trả lời của khách) chính là danh sách "cái gì cần linh động, cái gì không" mà đội thiết kế phần mềm nhận. Skill này không quyết định *làm sao* để linh động (cấu hình, workflow engine, plugin…); đó là việc của skill thiết kế.

## Bảng điểm biến thiên — luồng ngoại trú

ID: `VP-<luồng>-<số>`. Luồng: `TD` tiếp đón, `KH` khám, `CLS` cận lâm sàng, `DT` kê đơn–cấp phát, `VP` viện phí–BHYT, `GT` giấy tờ, `HS` hồ sơ, `DM` danh mục–vận hành. Cột "Loại cơ sở" ghi nơi điểm này hay khác nhau nhất: PK-DV (phòng khám thuần dịch vụ), PK-BHYT (phòng khám có hợp đồng BHYT), BV (khoa khám bệnh bệnh viện), CHUỖI (nhiều chi nhánh).

### Tiếp đón, định danh, hàng đợi

| ID | Điểm biến thiên | Lớp | Căn cứ / mặc định | Câu hỏi khảo sát | Loại cơ sở |
|---|---|---|---|---|---|
| VP-TD-01 | Nhận diện người bệnh bằng số định danh/căn cước/thẻ BHYT, kể cả không BHYT | `[LUẬT]` | `SKDT-R04`, `SKDT-R05`, `EMR-R05`, `BHYT-GD-R01` | — (không hỏi có làm không; hỏi *đang làm bằng gì*) | tất cả |
| VP-TD-02 | Người không có số định danh (trẻ sơ sinh, người nước ngoài, vô danh): mã tạm và gộp hồ sơ | `[LUẬT]` phần phải xử lý được · `[HỎI]` quy trình gộp của cơ sở | `SKDT-R10`–`R13`, `EMR-R05` | Ai được gộp hồ sơ trùng? Có duyệt không? | tất cả |
| VP-TD-03 | Kênh đặt hẹn (gọi điện, app, Zalo, walk-in) và có giữ chỗ/ưu tiên hẹn không | `[HỎI]` | — | Tỷ lệ hẹn trước / walk-in? Hẹn trễ xử lý sao? | PK-DV, CHUỖI |
| VP-TD-04 | Hàng đợi: một hàng chung hay theo phòng; số thứ tự cấp lúc nào | `[THÔNG LỆ]` BV cấp số tại tiếp đón rồi phân phòng (QĐ 1313, hướng dẫn) · `[HỎI]` PK | — | Số thứ tự cấp ở đâu? Có màn hình gọi số? Bác sĩ tự gọi hay điều dưỡng gọi? | tất cả |
| VP-TD-05 | Nhóm ưu tiên khám (cấp cứu, <6 tuổi, thai, khuyết tật nặng, ≥75, người có công) | `[LUẬT]` phải có ưu tiên · `[HỎI]` cách ưu tiên (phòng riêng, chèn hàng, hệ số) | `CHUYENKHOA-R39` | Cơ sở ưu tiên bằng cách nào? Có thêm nhóm riêng (VIP, gói)? | tất cả |
| VP-TD-06 | Tra cứu thẻ BHYT trên Cổng khi tiếp đón, lưu phản hồi | `[LUẬT]` | `BHYT-GD-R02`, `BHYT-DATA-R04` | Khi Cổng lỗi thì làm gì? (`BHYT-GD-R03`) | PK-BHYT, BV |
| VP-TD-07 | Người bệnh đến không xuất trình thẻ, xuất trình muộn, cấp cứu | `[LUẬT]` | `BHYT-GD-R06`, `BHYT-GD-R33` | Có cho "bổ sung thẻ sau" không? Ai duyệt chuyển dịch vụ → BHYT? | PK-BHYT, BV |
| VP-TD-08 | Thu tiền khám trước hay sau khám | `[THÔNG LỆ]` PK-DV thu trước; BV BHYT thu sau/đồng chi trả cuối lượt · `[HỎI]` | `TC-MS-R02` (mọi khoản thu phải có phiếu thu) | Thu khám lúc nào? Thu CLS lúc nào? Có cho nợ/thanh toán gộp cuối lượt? | tất cả |
| VP-TD-09 | Đồng ý xử lý dữ liệu cá nhân: lấy lúc nào, hình thức, trẻ em/người đại diện | `[LUẬT]` phải có · `[HỎI]` kênh lấy (giấy, ký tablet, OTP) | `DLCN-R02`, `R03`, `R08` | Hiện đang lấy đồng ý ở đâu? Có mẫu không? | tất cả |
| VP-TD-10 | Sao chụp giấy tờ tùy thân / thẻ | `[LUẬT]` không đặt thêm thủ tục; sao chụp phải có đồng ý | `BHYT-GD-R04` | Hiện có photo CCCD không? Vì sao? | tất cả |

### Khám, chẩn đoán, hồ sơ

| ID | Điểm biến thiên | Lớp | Căn cứ / mặc định | Câu hỏi khảo sát | Loại cơ sở |
|---|---|---|---|---|---|
| VP-KH-01 | Lượt khám có mở HSBA ngoại trú hay chỉ phiếu khám + đơn | `[LUẬT]` ranh giới chưa rõ (`BẮT BUỘC?`) · `[HỎI]` cơ sở đang làm gì | `EMR-R02`, `EMR-R01` | Loại lượt nào đang mở bệnh án ngoại trú? Điều trị theo đợt (PHCN, YHCT, thủ thuật) quản lý sao? | PK |
| VP-KH-02 | Mẫu bệnh án/phiếu khám theo chuyên khoa | `[LUẬT]` đúng mẫu TT 32 · `[HỎI]` trường thêm của cơ sở | `EMR-R03`, `CHUYENKHOA-R09`, `R12` | Đang dùng mẫu nào? Có trường tự thêm? In ra đúng mẫu hay bản nội bộ? | tất cả |
| VP-KH-03 | Người ghi, thời điểm ghi; ai được nhập hộ bác sĩ | `[LUẬT]` phải lưu người ghi thật, server cấp thời gian · `[HỎI]` thực tế có điều dưỡng/thư ký nhập hộ không | `EMR-R04`, `BHYT-GD-R17` | Ai gõ bệnh án thực tế? Có dùng chung tài khoản? Bác sĩ ký lúc nào? | tất cả |
| VP-KH-04 | Chẩn đoán bằng ICD-10 TT 06/2026; bệnh chính/kèm/biến chứng | `[LUẬT]` | `MA-LT-R01`–`R05`, `BHYT-DATA-R20` | Bác sĩ tự chọn mã hay có người mã hóa? Có bệnh "ngoài ICD" đang nhập tự do? | tất cả |
| VP-KH-05 | Chỉ định trong phạm vi chuyên môn được duyệt của cơ sở và người hành nghề | `[LUẬT]` | `MA-LT-R14`, `DUOC-R01` | Danh mục kỹ thuật được duyệt có cập nhật trong phần mềm? Ai duy trì? | tất cả |
| VP-KH-06 | Sửa bệnh án sau khi lưu / sau khi ký | `[LUẬT]` không sửa đè, có vết | `EMR-R10`, `EMR-R06` | Hiện sửa kiểu gì? Có "mở khóa" không? Ai mở? | tất cả |
| VP-KH-07 | Phân quyền xem hồ sơ giữa phòng/khoa; phá kính | `[LUẬT]` `BẮT BUỘC?` · `[HỎI]` mức chặt | `EMR-R11`, `DLCN-R01` | Bác sĩ phòng A có cần xem hồ sơ phòng B? Khi nào? | BV, CHUỖI |
| VP-KH-08 | Ký điện tử của bác sĩ: token, ký từ xa, HSM; ký từng phiếu hay ký khi đóng lượt | `[LUẬT]` phải là chữ ký số/điện tử hợp pháp, ảnh chữ ký không được · `[HỎI]` phương thức và thời điểm | `EMR-R06`, `R07`, `DUOC-R11` | Bác sĩ có chứng thư số chưa? Loại gì? Chấp nhận ký theo lô cuối buổi? | tất cả |
| VP-KH-09 | Xác nhận của người bệnh (đồng ý thủ thuật, cam kết) | `[LUẬT]` | `EMR-R09`, `CHUYENKHOA-R11` | Người bệnh ký bằng gì? Có lưu bằng chứng? | PK chuyên khoa, BV |
| VP-KH-10 | Khám nhiều chuyên khoa trong một lượt; khám lại trong ngày | `[THÔNG LỆ]` · `[HỎI]` tính một lượt hay nhiều, thu tiền khám thế nào | `BHYT-DATA-R21` (tỷ lệ tiền khám 100/30/10/0) | Người bệnh khám 2–3 phòng/ngày thì tính sao? BHYT có hợp nhất lượt? | BV, PK đa khoa |
| VP-KH-11 | Dịch vụ theo yêu cầu / ngoài phạm vi BHYT: thông báo trước và ghi nhận | `[LUẬT]` | `BHYT-GD-R35`, `TC-MS-R18` | Hiện ai báo giá chênh lệch cho người bệnh? Lưu ở đâu? | PK-BHYT, BV |

### Cận lâm sàng

| ID | Điểm biến thiên | Lớp | Căn cứ / mặc định | Câu hỏi khảo sát | Loại cơ sở |
|---|---|---|---|---|---|
| VP-CLS-01 | CLS làm tại chỗ hay gửi ngoài; kết quả nhận về dạng gì | `[HỎI]` · `[LUẬT]` phần kết quả gửi ngoài | `CLS-R08`, `BHYT-GD-R13` | Xét nghiệm nào gửi ngoài? Nhận kết quả qua file, API, giấy? | PK |
| VP-CLS-02 | Thu tiền CLS trước khi lấy mẫu / chụp | `[THÔNG LỆ]` thu trước ở PK-DV; BHYT đúng tuyến không thu từng dịch vụ · `[HỎI]` | `TC-MS-R02` | Có lấy mẫu trước thu sau không? Ai duyệt? | tất cả |
| VP-CLS-03 | Có LIS/RIS-PACS riêng hay nhập tay; kết nối máy | `[HỎI]` · `[LUẬT]` nội dung tối thiểu phiếu kết quả, người thực hiện, ký duyệt | `CLS-R02`, `R12`, `R13`, `R17` | Máy nào nối, máy nào nhập tay? Ai duyệt kết quả? | tất cả |
| VP-CLS-04 | Dùng lại kết quả cũ / liên thông, cảnh báo trùng | `[LUẬT]` `BẮT BUỘC?` (dự thảo, mốc 01/01/2027) · `[HỎI]` thói quen chỉ định lại | `CLS-R01`, `R03`, `R06` | Bác sĩ có xem kết quả cũ không? Chỉ định lại vì sao? | PK-BHYT, BV |
| VP-CLS-05 | Sửa kết quả sau phát hành; giá trị nguy kịch báo ai | `[LUẬT]` | `CLS-R13`, `R14` | Hiện có quy trình báo giá trị nguy kịch? Ai nhận? | tất cả |
| VP-CLS-06 | Trả kết quả cho người bệnh: giấy, Zalo, app, cổng | `[HỎI]` · `[LUẬT]` bảo mật, đồng ý khi gửi qua kênh ngoài | `DLCN-R10`, `DLCN-R28` | Trả kết quả qua kênh nào? Có xác thực người nhận? | tất cả |

### Kê đơn, cấp phát, nhà thuốc

| ID | Điểm biến thiên | Lớp | Căn cứ / mặc định | Câu hỏi khảo sát | Loại cơ sở |
|---|---|---|---|---|---|
| VP-DT-01 | Đơn điện tử, mã đơn 14 ký tự, gửi Hệ thống đơn thuốc QG ngay sau khám | `[LUẬT]` | `DUOC-R04`, `R11`, `R12` | Hiện gửi ngay hay gom? Có theo dõi đơn lỗi? | tất cả |
| VP-DT-02 | Đơn đã gửi không sửa; sửa = kê đơn mới | `[LUẬT]` | `DUOC-R09` | Hiện sửa đơn kiểu gì? Tần suất? | tất cả |
| VP-DT-03 | Thuốc N/H: đơn riêng, số ngày, hồ sơ kèm | `[LUẬT]` | `DUOC-R06`–`R08`, `R32` | Cơ sở có kê thuốc N/H không? | PK chuyên khoa, BV |
| VP-DT-04 | Cấp phát tại chỗ hay người bệnh mua ngoài; đối chiếu khi cấp | `[HỎI]` có quầy hay không · `[LUẬT]` nếu có quầy phải đối chiếu đơn | `DUOC-R20`, `R22`, `R23` | Có nhà thuốc trong cơ sở? Của cơ sở hay thuê? Bán cho người ngoài không? | tất cả |
| VP-DT-05 | Thay thế thuốc tại quầy | `[LUẬT]` | `DUOC-R24` | Dược sĩ có đổi thuốc không? Ghi nhận ở đâu? | có quầy |
| VP-DT-06 | Kho thuốc: lô, hạn, nguồn gốc, liên thông CSDL dược | `[LUẬT]` | `DUOC-R25`, `R26`, `R31` | Đang quản kho bằng gì? Nhập lô/hạn từng phiếu không? | có quầy |
| VP-DT-07 | Cảnh báo liều, tương tác, dị ứng | `[LUẬT]` mức theo domain | `DUOC-R34` | Có danh sách dị ứng theo người bệnh? Bác sĩ có bị chặn hay chỉ cảnh báo? | tất cả |
| VP-DT-08 | Gửi đơn/mã đơn cho người bệnh | `[LUẬT]` | `DUOC-R14` | Gửi qua kênh nào? | tất cả |

### Viện phí, BHYT, hóa đơn

| ID | Điểm biến thiên | Lớp | Căn cứ / mặc định | Câu hỏi khảo sát | Loại cơ sở |
|---|---|---|---|---|---|
| VP-VP-01 | Bảng giá: nhiều loại giá (BHYT, dịch vụ, theo yêu cầu, gói), có phiên bản theo ngày | `[LUẬT]` | `TC-MS-R17`, `R19`, `R21` | Có bao nhiêu bảng giá? Ai đổi giá? Đổi có hiệu lực từ khi nào? | tất cả |
| VP-VP-02 | Giá tham chiếu BHYT cho cơ sở tư; phần chênh lệch | `[LUẬT]` | `TC-MS-R18` | Giá BHYT lấy theo HĐND tỉnh nào? | PK-BHYT tư |
| VP-VP-03 | Mức hưởng theo cấp CMKT, đúng/không đúng nơi đăng ký, các trường hợp 100% | `[LUẬT]` | `BHYT-GD-R10`, `R09`, `BHYT-DATA-R11` | Cơ sở xếp cấp nào, điểm bao nhiêu? | PK-BHYT, BV |
| VP-VP-04 | Tra lại thẻ và mức hưởng trước khi kết thúc lượt | `[LUẬT]` | `BHYT-GD-R07` | — | PK-BHYT, BV |
| VP-VP-05 | Phiếu thu mỗi giao dịch; hóa đơn tổng hợp cuối ngày; hóa đơn theo yêu cầu | `[LUẬT]` | `TC-MS-R02`, `R05`, `R08` | Đang xuất hóa đơn kiểu gì? Nhà cung cấp HĐĐT nào? | tất cả |
| VP-VP-06 | Tạm ứng / gói trả trước (thai sản, KSK, liệu trình) | `[LUẬT]` `BẮT BUỘC?` cách lập hóa đơn · `[HỎI]` cơ sở có bán gói không | `TC-MS-R04` | Có gói/liệu trình trả trước? Hoàn tiền thế nào? | PK-DV, CHUỖI |
| VP-VP-07 | Miễn giảm, chiết khấu, bảo hiểm thương mại/bảo lãnh | `[HỎI]` · `[LUẬT]` chỉ gửi dữ liệu cho DNBH khi người bệnh yêu cầu bằng văn bản | `TC-MS-R27`–`R30`, `DLCN-R09` | Có bảo lãnh viện phí với công ty bảo hiểm nào? Quy trình? Ai được giảm giá? | PK-DV, BV tư |
| VP-VP-08 | Hoàn tiền, hủy dịch vụ đã thu | `[LUẬT]` hóa đơn điều chỉnh/thay thế, không "hủy" · `[HỎI]` ai duyệt hoàn | `TC-MS-R09` | Hoàn tiền cần ai duyệt? Hoàn tiền mặt hay chuyển khoản? | tất cả |
| VP-VP-09 | Check-in XML0 khi phát sinh chi phí đầu tiên; gửi XML ngay sau kết thúc lượt | `[LUẬT]` | `BHYT-DATA-R03`, `BHYT-GD-R19`, `R20` | Hiện gửi ngay hay cuối ngày/cuối tháng? Ai xử lý hồ sơ Cổng trả lỗi? | PK-BHYT, BV |
| VP-VP-10 | Bảng kê 01/KBCB điện tử ký số | `[LUẬT]` | `BHYT-DATA-R21` | Người bệnh ký bảng kê bằng gì? | PK-BHYT, BV |
| VP-VP-11 | Người bệnh bỏ về không thanh toán | `[LUẬT]` ký thay có ủy quyền · `[HỎI]` tần suất, ai ký | `BHYT-GD-R33` | — | PK-BHYT, BV |
| VP-VP-12 | Thanh toán không tiền mặt, đối soát | `[LUẬT]` hỗ trợ; vendor không thu hộ | `TC-MS-R24`–`R26` | Dùng cổng thanh toán nào? Đối soát ai làm? | tất cả |
| VP-VP-13 | Ca làm việc thu ngân: chốt ca, bàn giao tiền | `[THÔNG LỆ]` · `[HỎI]` | — | Mấy ca/ngày? Chốt ca cần in gì? | tất cả |

### Giấy tờ, kết thúc lượt, liên thông

| ID | Điểm biến thiên | Lớp | Căn cứ / mặc định | Câu hỏi khảo sát | Loại cơ sở |
|---|---|---|---|---|---|
| VP-GT-01 | Giấy nghỉ hưởng BHXH (Mẫu 07): ai ký, giới hạn ngày, XML11 | `[LUẬT]` | `GIAYTO-R12`, `R04` | Ai được ký giấy nghỉ? Có cấp lại khi sai? | PK-BHYT, BV |
| VP-GT-02 | Phiếu hẹn khám lại, phiếu chuyển cơ sở: hai chữ ký số, dùng 1 lần | `[LUẬT]` | `BHYT-GD-R11`, `R12`, `GIAYTO-R17` | Hẹn khám lại ghi ở đâu (đơn, phiếu riêng)? | PK-BHYT, BV |
| VP-GT-03 | Giấy khám sức khỏe: mẫu, 24 giờ liên thông | `[LUẬT]` | `GIAYTO-R18`, `SKDT-R15` | Có khám sức khỏe đoàn/lái xe không? | PK |
| VP-GT-04 | Gửi dữ liệu Sổ SKĐT VNeID cho mọi lượt, kể cả dịch vụ | `[LUẬT]` | `SKDT-R01`, `R02` | Lượt không BHYT hiện có gửi không? | tất cả |
| VP-GT-05 | Tóm tắt, sao chụp hồ sơ theo yêu cầu người bệnh | `[LUẬT]` | `EMR-R14`, `DLCN-R06` | Ai tiếp nhận yêu cầu? Mất bao lâu? | tất cả |
| VP-GT-06 | Mẫu in nội bộ (phiếu khám, phiếu chỉ định, toa) khác mẫu BYT | `[THÔNG LỆ]` PK hay có mẫu riêng · `[LUẬT]` mẫu bắt buộc phải đúng khi là giấy tờ pháp lý | `EMR-R13`, `GIAYTO-R01` | Gửi tao mẫu đang in. Mẫu nào là "bắt buộc đúng", mẫu nào nội bộ? | tất cả |

### Danh mục, vận hành, tổ chức

| ID | Điểm biến thiên | Lớp | Căn cứ / mặc định | Câu hỏi khảo sát | Loại cơ sở |
|---|---|---|---|---|---|
| VP-DM-01 | Danh mục dịch vụ: mã nội bộ ↔ mã BHYT ↔ mã tương đương TT 23 | `[LUẬT]` | `MA-LT-R15`, `BHYT-DATA-R17`, `R19` | Danh mục hiện có bao nhiêu dòng? Ai ánh xạ mã? Có file Excel? | tất cả |
| VP-DM-02 | Danh mục thuốc, vật tư, thầu | `[LUẬT]` | `BHYT-DATA-R18`, `DUOC-R31` | Có kết quả thầu? Thuốc ngoài thầu xử lý sao? | PK-BHYT, BV |
| VP-DM-03 | Sơ đồ phòng/khoa, mã khoa QĐ 1804 | `[LUẬT]` mã khoa cho XML · `[HỎI]` cơ cấu phòng thực tế | `BHYT-DATA-R15` | Vẽ sơ đồ phòng, ai ngồi đâu, ca nào | tất cả |
| VP-DM-04 | Người hành nghề: giấy phép, phạm vi, mã liên thông, đăng ký hành nghề | `[LUẬT]` | `DUOC-R02`, `HTTT-BC-R06` | Danh sách bác sĩ kèm số GPHN, bác sĩ thỉnh giảng/ca lẻ? | tất cả |
| VP-DM-05 | Tài khoản cá nhân, không dùng chung, phân quyền theo vai | `[LUẬT]` | `BHYT-GD-R17`, `EMR-R11` | Hiện có bao nhiêu tài khoản? Ai dùng chung? | tất cả |
| VP-DM-06 | Nhiều chi nhánh: mã cơ sở riêng, dữ liệu tách, danh mục chung hay riêng | `[LUẬT]` mỗi cơ sở KCB một mã, dữ liệu gửi theo mã · `[HỎI]` quản trị chung | `BHYT-DATA-R24`, `SKDT-R18` | Mỗi chi nhánh một giấy phép? Dùng chung bảng giá? Người bệnh khám chéo? | CHUỖI |
| VP-DM-07 | Báo cáo gửi Sở/Bộ, báo cáo nội bộ, báo cáo cho chủ | `[LUẬT]` báo cáo bắt buộc · `[HỎI]` báo cáo quản trị | `HTTT-BC-R23`, `R27`, `R32` | Hằng tháng nộp báo cáo nào, cho ai, mẫu gì? Chủ muốn xem gì mỗi sáng? | tất cả |
| VP-DM-08 | Vận hành SaaS: ai giữ dữ liệu, DPA, giấy chứng nhận vendor | `[LUẬT]` | `DLCN-R11`, `R22`, `EMR-R26`, `TC-MS-R32` | Đã ký DPA chưa? | vendor |

## Những "đặc thù" khách hay xin mà thực ra là lệch luật

BA gặp các yêu cầu này nên nói thẳng là không làm được theo cách đó, kèm ID, và đề xuất cách hợp lệ:

| Khách xin | Vì sao không | Thay bằng |
|---|---|---|
| "Cho sửa đơn thuốc đã gửi, bệnh nhân đổi ý" | `DUOC-R09` | Kê đơn mới thay thế, đơn cũ chuyển trạng thái thay thế |
| "Dán ảnh chữ ký bác sĩ vào toa cho nhanh" | `EMR-R06`, `DUOC-R11` | Ký số từ xa (remote signing) để không cần token |
| "Gom XML gửi cuối tháng cho đỡ lỗi" | `BHYT-GD-R19`, `R20` | Gửi ngay sau lượt, hàng đợi gửi lại tự động, màn hình hồ sơ lỗi |
| "Một tài khoản chung cho cả phòng" | `BHYT-GD-R17`, `EMR-R04` | Tài khoản cá nhân, đăng nhập nhanh (thẻ, PIN) |
| "Lượt dịch vụ không cần gửi Sổ SKĐT" | `SKDT-R01` | Gửi mọi lượt, chỉ khác bộ bảng |
| "Xóa hẳn bệnh án nhập nhầm" | `EMR-R10`, `R24` | Hủy có lý do, giữ vết |
| "Gửi danh sách bệnh nhân cho công ty bảo hiểm đối tác" | `DLCN-R09`, `TC-MS-R27` | Chỉ khi người bệnh yêu cầu bằng văn bản, từng ca |
| "Lưu 5 năm rồi xóa cho nhẹ" | `EMR-R22` | 10/20/30 năm theo loại |
| "Photo CCCD lưu hồ sơ" | `BHYT-GD-R04`, `DLCN-R30` | Lưu số định danh và nguồn xác thực, không lưu ảnh nếu không cần |
