# BHYT-GD — Giám định, thanh toán và quy trình dữ liệu BHYT

> Kiểm tra lần cuối: 2026-10-28 · Áp dụng: BV công, BV tư, phòng khám có hợp đồng KCB BHYT; cơ sở/phòng xét nghiệm nhận chuyển DVCLS; vendor HIS · Research gốc: `research/deep/BHYT-GD.md`

Không phải ý kiến pháp lý. Phạm vi: tiếp đón và tra cứu thẻ, mức hưởng, chuyển cơ sở, phiếu hẹn, chuyển DVCLS, tài khoản Cổng, ký số/xác thực, thời hạn gửi, phản hồi Cổng, giám định tự động/chủ động, tổng hợp và quyết toán, xử phạt. Chuẩn XML, bộ mã, bảng kê 697 → **BHYT-DATA**. Liên thông CLS chi tiết → **CLS**. Hóa đơn → **TC-MS**. VNeID, Sổ SKĐT → **SKDT**. HSBA, ký số chung → **EMR**.

## Tóm tắt nhanh

- **Đang có hiệu lực (TT 48/2017)**: gửi dữ liệu "ngay sau" khi kết thúc lượt (không có số giờ); hiệu chỉnh, ký, gửi đề nghị thanh toán trong **07 ngày làm việc**; phát sinh cuối tháng, quý, năm gửi **trước ngày 05** tháng kế tiếp. TT 12/2026 dẫn lại các mốc này.
- **Dự thảo, chưa ban hành** (thay TT 48, góp ý đến **07/10/2026**, dự kiến **01/01/2027**): gửi dữ liệu đã ký **≤ 03 giờ** sau khi kết thúc lượt; 15 ngày đối chiếu trước khi đề nghị thanh toán; khóa dữ liệu sau đề nghị thanh toán; chế tài theo bậc. Hiện là NÊN chuẩn bị, không phải nghĩa vụ.
- Ký số (xác thực) dữ liệu chi phí bắt buộc chậm nhất **01/01/2026** (NĐ 188 Đ69 k9). "Xác thực dữ liệu" là ký số hồ sơ của cơ sở, **không** phải xác thực sinh trắc người bệnh.
- TT 12/2026/TT-BTC (Bộ Tài chính) là văn bản giám định hiện hành: Cổng phản hồi 06/24/48 giờ; cơ sở sửa lỗi trong **02 ngày làm việc**; giải trình giám định tự động **03 ngày làm việc** (Mẫu 09/BH); 01/BH ngày 15 hằng tháng, 02/BH ngày 15 đầu quý.
- Không được đòi thẻ giấy; Cổng lỗi vẫn phải tiếp nhận người bệnh (NĐ 188 Đ37–38).
- Chế tài NĐ 90/2026 (mức tổ chức ×2): không kết nối, liên thông, tạo chứng từ điện tử (Đ95 k4 b); mượn tài khoản HIS để chỉ định, kê đơn (Đ95 k1 c). **Không** có điều riêng phạt "chậm gửi XML"; chỉ phạt chậm báo cáo quyết toán (Đ94).
- Hạn luật định gần nhất: **01/01/2027** liên thông, sử dụng kết quả CLS giữa cơ sở KCB BHYT (Luật 51/2024 Đ3 k4), nhưng chưa có văn bản chi tiết.
- Bẫy: TT 12 tự dẫn tới văn bản đã chết (NĐ 123/2020, NĐ 70/2025 → NĐ 254/2026; PL1 QĐ 824, PL6 QĐ 2010 → QĐ 1804); TT 01/2025 đọc riêng còn ghi "đóng dấu".

## Mục lục

| ID | Tiêu đề |
|---|---|
| BHYT-GD-R01 | Chấp nhận mọi hình thức xuất trình thẻ |
| BHYT-GD-R02 | Tra cứu thẻ trên Cổng và lưu kết quả |
| BHYT-GD-R03 | Dự phòng khi VNeID/VssID/Cổng lỗi |
| BHYT-GD-R04 | Không đặt thêm thủ tục; sao chụp phải có đồng ý |
| BHYT-GD-R05 | Mã thẻ tạm trẻ dưới 6 tuổi, người hiến bộ phận |
| BHYT-GD-R06 | Xuất trình thẻ muộn và cấp cứu |
| BHYT-GD-R07 | Kiểm tra lại mức hưởng trước khi kết thúc lượt |
| BHYT-GD-R08 | Thẻ hết hạn khi đang điều trị |
| BHYT-GD-R09 | Miễn cùng chi trả |
| BHYT-GD-R10 | Mức hưởng theo cấp CMKT, lộ trình 2026 |
| BHYT-GD-R11 | Phiếu chuyển cơ sở KCB |
| BHYT-GD-R12 | Phiếu hẹn khám lại |
| BHYT-GD-R13 | Chuyển người bệnh/mẫu làm DVCLS |
| BHYT-GD-R14 | Liên thông kết quả CLS từ 01/01/2027 |
| BHYT-GD-R15 | Điều kiện ký hợp đồng: kết nối, Mẫu 8 |
| BHYT-GD-R16 | Tài khoản Cổng |
| BHYT-GD-R17 | Tài khoản HIS cá nhân, cấm mượn |
| BHYT-GD-R18 | Ký số, xác thực dữ liệu đề nghị thanh toán |
| BHYT-GD-R19 | Gửi dữ liệu sau mỗi lượt (hiện hành) |
| BHYT-GD-R20 | Cửa sổ 07 ngày làm việc, kỳ cuối tháng trước ngày 05 (hiện hành) |
| BHYT-GD-R21 | Gửi chậm có lý do và bằng chứng sự cố |
| BHYT-GD-R22 | Xử lý phản hồi tự động của Cổng |
| BHYT-GD-R23 | Giám định tự động, Mẫu 09/BH |
| BHYT-GD-R24 | Giám định chủ động: cung cấp HSBA trong 03 ngày làm việc |
| BHYT-GD-R25 | Bảng tổng hợp 01/BH, quyết toán 02/BH |
| BHYT-GD-R26 | Biên bản giám định, quyết toán, hóa đơn |
| BHYT-GD-R27 | Cảnh báo gia tăng chi |
| BHYT-GD-R28 | Danh mục 01–06/DM: duyệt và áp dụng |
| BHYT-GD-R29 | Dữ liệu chi phí trung thực, truy vết được |
| BHYT-GD-R30 | Kết nối, liên thông là nghĩa vụ có chế tài |
| BHYT-GD-R31 | Bảo mật; hồ sơ bí mật nhà nước |
| BHYT-GD-R32 | Báo vi phạm sử dụng thẻ |
| BHYT-GD-R33 | Ký xác nhận khi người bệnh không làm thủ tục |
| BHYT-GD-R34 | Chuẩn bị cho dự thảo thay TT 48 (03 giờ) |
| BHYT-GD-R35 | Chi phí ngoài phạm vi phải thông báo trước |
| BHYT-GD-R36 | Tiền khám nhiều chuyên khoa và định mức lượt khám/bàn khám |
| BHYT-GD-R37 | Chi phí một lần KCB thấp |
| BHYT-GD-R38 | Trần gói thiết bị y tế 45 tháng lương cơ sở, stent phủ thuốc |
| BHYT-GD-R39 | Lương cơ sở (mức tham chiếu) theo giai đoạn |
| BHYT-GD-R40 | Quyền lợi nhóm quân đội, công an, cơ yếu, dân quân thường trực |
| BHYT-GD-R41 | Ngày giường điều trị nội trú, giường lưu |
| BHYT-GD-R42 | Nhiều can thiệp trong một lần phẫu thuật, DVKT dừng giữa chừng |
| BHYT-GD-R43 | Vận chuyển người bệnh |
| BHYT-GD-R44 | Máu, chế phẩm máu, vận chuyển máu |
| BHYT-GD-R45 | Kháng sinh dấu (*) chỉ được quỹ trả khi kê đúng quy trình |

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 51/2024/QH15 | Luật sửa đổi Luật BHYT | 01/07/2025; một số khoản từ 01/01/2025 (Đ3 k2); liên thông CLS chậm nhất 01/01/2027 (Đ3 k4) | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat51.pdf) |
| 188/2025/NĐ-CP (01/07/2025) | Chi tiết Luật BHYT | 15/08/2025; nhiều điều từ 01/07/2025 (Đ70 k2) | Còn HL; bãi bỏ NĐ 146/2018, 75/2023, 02/2025 | gốc-OCR (Đ68–Đ70 đối chiếu ảnh ở BHYT-DATA) | [VB 214515](https://vanban.chinhphu.vn/?pageid=27160&docid=214515) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/188-ndcp.signed.pdf) |
| 12/2026/TT-BTC (10/02/2026) | Giám định chi phí KCB BHYT, biểu mẫu tổng hợp, quyết toán | Từ ngày ký; Mẫu 01/BH, 05/BH, 06/BH, 09/BH, danh mục Đ7–8 từ 01/04/2026 (Đ17 k1) | Còn HL; không bãi bỏ văn bản nào | gốc-OCR (Đ5–Đ9 đối chiếu ảnh ở BHYT-DATA) | [VB 216997](https://vanban.chinhphu.vn/?pageid=27160&docid=216997) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-btc.pdf) |
| 48/2017/TT-BYT (28/12/2017) | Trích chuyển dữ liệu điện tử KCB BHYT | 01/03/2018 | **Còn HL**; TT 12 Đ4 k2, Đ9 k1 dẫn trực tiếp | gốc-ảnh (Đ2–Đ8), gốc-OCR | [PDF ký số BYT, SYT Hà Tĩnh](https://soyte.hatinh.gov.vn/upload/1000030/20171027/4e5899d541ea00e83dd2fce1579631cdtt-2017-48-1_1.pdf) · [bản ký số, TTYT Ninh Sơn](http://trungtamyteninhson.vn/wp-content/uploads/2025/10/TT48.pdf) |
| Dự thảo TT ứng dụng CNTT, CĐS, chia sẻ dữ liệu BHYT (thay TT 48/2017) | Gửi ≤ 03 giờ, 15 ngày đối chiếu, khóa dữ liệu, chế tài theo bậc | Dự kiến 01/01/2027; góp ý đến 07/10/2026 | **Dự thảo** | thứ cấp (chưa có toàn văn) | [vtv (báo, bối cảnh)](https://vtv.vn/de-xuat-co-so-y-te-phai-gui-du-lieu-bhyt-trong-vong-3-gio-sau-kham-cham-nhieu-lan-co-the-bi-xu-phat-100261001082022915.htm) · [baohaiphong (báo, bối cảnh)](https://baohaiphong.vn/de-xuat-phat-co-so-kham-chua-benh-cham-gui-du-lieu-bao-hiem-y-te-554711.html) |
| 90/2026/NĐ-CP (30/03/2026) | Xử phạt VPHC y tế (mục BHYT Đ81–95); thay NĐ 117/2020 | 15/05/2026 | Còn HL | gốc-OCR (Đ95 k4 đã đối chiếu ảnh trang, xem GIAYTO) | [VB 217386](https://vanban.chinhphu.vn/?pageid=27160&docid=217386) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| 01/2025/TT-BYT | Hướng dẫn Luật BHYT (lưu trú, chuyển người bệnh, phiếu hẹn, phiếu chuyển) | 01/01/2025 | Còn HL; sửa bởi TT 06/2026 Đ5 k2 | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/01-byt.pdf) |
| 35/2016/TT-BYT (28/09/2016), sửa bởi 39/2024/TT-BYT (17/11/2024) | Danh mục, tỷ lệ, điều kiện thanh toán DVKT BHYT; TT 39 Đ1 k4 bổ sung Đ4a–4d: tiền khám nhiều chuyên khoa, định mức 65 lượt/bàn khám | TT 39: 01/01/2025 | Còn HL; TT 39 sửa, không thay TT 35 | gốc (TT 39, ký số) | [VB 211771](https://vanban.chinhphu.vn/?pageid=27160&docid=211771) · [PDF TT 39](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/39-byt.pdf) |
| 161/2026/NĐ-CP (15/05/2026) | Lương cơ sở 2.530.000 đ/tháng (Đ3 k2); thay NĐ 73/2024 (Đ6) | 01/07/2026 | Còn HL | gốc-ảnh | [VB 218107](https://vanban.chinhphu.vn/?pageid=27160&docid=218107) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/161-ndcp.signed.pdf) |
| 2275/BHXH-CSYT (30/06/2026) | Mức hưởng BHYT theo LCS mới: chi phí thấp, trần TBYT, lũy kế; chi phí thấp ở cơ sở 50% | 01/07/2026 | Hướng dẫn BHXH | gốc | [PDF, BHXH VN](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26762/CV%202275.pdf) |
| 04/2017/TT-BYT sửa bởi 24/2025/TT-BYT (30/06/2025); VBHN 14/VBHN-BYT | Danh mục, tỷ lệ, điều kiện thanh toán TBYT; Đ3 k2 b, c: trần gói 45 tháng LCS, stent phủ thuốc | TT 24: 01/09/2025 | Còn HL; căn cứ cũ NĐ 146 | gốc | [VB 214383](https://vanban.chinhphu.vn/?pageid=27160&docid=214383) · [PDF TT 24](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/24-byt.pdf) · [VBHN 14](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/8/14-vbhn-byt.pdf) |
| 70/2015/NĐ-CP sửa bởi 74/2025/NĐ-CP | BHYT quân đội, công an, cơ yếu: không áp tỷ lệ, mức thanh toán; chi phí ngoài phạm vi | NĐ 74: 01/07/2025 | Còn HL (NĐ 188 Đ15 k2 dẫn) | NĐ 74: gốc-ảnh; NĐ 70: thứ cấp | [VB 213303](https://vanban.chinhphu.vn/?pageid=27160&docid=213303) · [PDF NĐ 74](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/4/74-2025-nd-cp-1-.signed.pdf) |
| 15/2023/TT-BYT | Giá, thanh toán máu, chế phẩm máu; vận chuyển máu ≤ 17.000 đ/đơn vị | 15/09/2023 | Còn HL; bảng giá Đ3 bị QĐ 3833/QĐ-BYT (2024) thay (thứ cấp) | gốc-ảnh | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/7/15-byt.pdf) |
| 37/2024/TT-BYT | Thanh toán thuốc BHYT; Đ10 k5 kháng sinh (*) | hiện hành | Còn HL | gốc-ảnh | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/11/37-byt.pdf) |
| 15/2023/QH15 (VBHN 26/VBHN-VPQH, 26/02/2026) | Luật KCB: Đ7 k2 (cấm từ chối, cố ý chậm cấp cứu), Đ40 (trường hợp được từ chối), Đ77 k2 (giường lưu) | 01/01/2024 | Còn HL | gốc | [PDF VBHN](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 06/2026/TT-BYT (02/04/2026) | ICD-10; Đ5 k2 sửa mẫu phiếu TT 01 (ký số thay đóng dấu) | 01/07/2026; Đ5 k2, k3 từ 01/06/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/06-byt.pdf) |
| 164/2025/NĐ-CP | GDĐT lĩnh vực BHXH, CSDL quốc gia về bảo hiểm | 01/07/2025 | Còn HL; NĐ 43/2021 hết HL | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/164-cp.signed.pdf) |
| 09/2026/TT-BTC (03/02/2026) | Tạo lập, sử dụng sổ BHXH, thẻ BHYT bản điện tử; Đ6 k3 không đòi thẻ giấy, cơ sở phải tra giá trị thẻ; Đ8 k2 thẻ trên VssID cấp trước đó vẫn có giá trị như bản giấy | 03/02/2026 (Đ9 k1) | Còn HL; không áp cho đối tượng BQP, BCA quản lý (Đ1 k1 b) | gốc-ảnh (bản sao y ký số BHXH VN; không có trên vanban.chinhphu.vn) | [VB BHXH ItemID 4992](https://baohiemxahoi.gov.vn/vanban/Pages/default.aspx?ItemID=4992) · [PDF](https://baohiemxahoi.gov.vn:4545/File_Server_BHXH/documents/N409.pdf) |
| 2555/QĐ-BYT (12/08/2025) | Công bố TTHC "KCB BHYT" (các trường hợp xuất trình thẻ); thay QĐ 7291/2018, 4524/2023, 160/2025 | 15/08/2025 | Còn HL; QĐ công bố TTHC, không phải VBQPPL, chép lại NĐ 188 Đ37–38 → trích NĐ 188 | nội dung: bản BYT không số đính kèm tin BHXH VN; số, ngày: tin BHXH VN | [PDF đính kèm tin BHXH VN](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/25292/Quy%E1%BA%BFt%20%C4%91%E1%BB%8Bnh%202555_Q%C4%90-BYT%20c%E1%BB%A7a%20B%E1%BB%99%20Y%20t%E1%BA%BF%20v%E1%BB%81%20vi%E1%BB%87c%20c%C3%B4ng%20b%E1%BB%91%20th%E1%BB%A7%20t%E1%BB%A5c%20h%C3%A0nh%20ch%C3%ADnh%20m%E1%BB%9Bi%20ban%20h%C3%A0nh%2C%20%C4%91%C6%B0%E1%BB%A3c%20s%E1%BB%ADa%20%C4%91%E1%BB%95i%2C%20b%E1%BB%95%20sung%20.pdf) |
| 497/BHXH-CNTT (21/02/2019) | Hàm `KQNhanLichSuKCB2019` của Cổng giám định: thông tin thẻ, thẻ cũ/mới, lịch sử KCB, lịch sử tra cứu; bảng mã kết quả tra thẻ | Từ ngày ký | Hướng dẫn kỹ thuật, không phải VBQPPL; chưa thấy thay thế; căn cứ cũ NĐ 146/2018 | gốc-ảnh (bản scan có chữ ký, dấu, bên thứ ba đăng lại) | [PDF, BV Phụ sản Thanh Hóa](https://benhvienphusanthanhhoa.vn/?call=file.download&file_id=635682781) |
| 1804/BHXH-QLT (04/08/2025) + 2036/BHXH-CSYT (22/08/2025) | Số định danh cá nhân/CCCD thay mã số BHXH (mã số 10 số dùng song song trong thời gian chuyển đổi); PL I mã đối tượng tham gia kèm mức hưởng tính bằng %; CV 2036: cơ sở KCB tra bằng ĐDCN, quyền lợi cao nhất | 01/08/2025 | Hướng dẫn nghiệp vụ BHXH; chưa thấy thay thế. **Khác QĐ 1804/QĐ-BYT** | CV 1804: gốc-ảnh (thân, bản sao y đăng lại), thứ cấp (PL I, bản không số); CV 2036: gốc | [CV 1804, ebh.vn](https://ebh.vn/Download/vanbanphapquy/cong-van-1804-bhxh-qlt-482025.pdf) · [CV 2036, BHXH VN](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/25348/CV%202036%20cua%20BHXH%20VN.pdf) |
| 1666/QĐ-BHXH (03/12/2020) | Mẫu thẻ BHYT: mã số 10 ký tự (mã số BHXH); in mã mức hưởng 1–5, K1/K2/K3, thời điểm đủ 05 năm, mã vạch 2 chiều | 01/04/2021; thay QĐ 1313/2014 | Chưa thấy thay thế; căn cứ hiện hành Luật BHYT Đ16 k5 | gốc-ảnh (bản scan có chữ ký, ebh.vn đăng lại) | [PDF](https://ebh.vn/Download/vanbanphapquy/quyet-dinh-1666-qd-bhxh-ban-hanh-mau-the-bao-hiem-y-te.pdf) |
| 1351/QĐ-BHXH (16/11/2015), sửa bởi 1697/QĐ-BHXH (27/11/2023) | Mã thẻ 15 ký tự (4 ô); 1697 sửa Đ2: mã đối tượng, ký hiệu mức hưởng | 1697: 03/12/2023 | Văn bản nghiệp vụ BHXH; căn cứ NĐ 146/2018 đã hết HL; chưa thấy bãi bỏ; hiệu lực sau NĐ 188 chưa xác minh | 1697: gốc-ảnh; 1351: thứ cấp | [QĐ 1697, BHXH VN](https://baohiemxahoi.gov.vn:4545/File_Server_BHXH/documents/9542_BHXHVN_1697-Q%C4%90-BHXH_27112023.pdf) |
| Phụ lục 01 "Hướng dẫn liên thông dữ liệu theo QĐ 3176" kèm CV …/BHXH-CNTT (số, ngày để trống) | Đăng ký chứng thư, API token, check-in, gửi XML, `CHUKYDONVI` SHA256 | Ký số 07/01/2026 (theo tên file) | Hướng dẫn kỹ thuật, không phải VBQPPL | thứ cấp (bản đăng lại) | [PDF, UBND xã Khánh Cường](https://khanhcuong.quangngai.gov.vn/upload/2007018/20260128/PL01_li%C3%AAn%20th%C3%B4ng%20d%E1%BB%AF%20li%E1%BB%87u_3176_k%C3%BD%20s%E1%BB%91_07012026%20(1).pdf) |

Dự thảo TT BTC về Cổng tiếp nhận dữ liệu (hướng dẫn NĐ 188 Đ71 k2 d) **đã được hấp thụ vào TT 12/2026**; không trích dự thảo riêng.

### Đang có hiệu lực và dự thảo: so sánh thời hạn gửi

| Nội dung | Đang có hiệu lực (TT 48/2017 + TT 12/2026) | Dự thảo thay TT 48 (chưa ban hành) |
|---|---|---|
| Gửi dữ liệu sau lượt | "Ngay sau" khi kết thúc lượt (TT 48 Đ6 k1), không định lượng giờ | ≤ 03 giờ từ khi kết thúc lượt, dữ liệu đã ký |
| Hiệu chỉnh và đề nghị thanh toán | Trong 07 ngày làm việc; kỳ cuối tháng/quý/năm trước ngày 05 (TT 48 Đ7 k1) | 15 ngày kiểm tra, đối chiếu trước khi đề nghị thanh toán |
| Sửa sau khi gửi | Được, nêu lý do và thống nhất với BHXH (TT 48 Đ13 k9) | Dữ liệu đã đề nghị thanh toán không được đổi (trừ một số trường hợp) |
| Kết quả giám định | Tự động 07 ngày làm việc (TT 12 Đ10 k2) | Chi tiết trong 15 ngày |
| Chế tài chậm gửi | Không có điều riêng trong NĐ 90 | Nhắc tự động → BHXH nhắc văn bản 2 lần → xử phạt VPHC (cần căn cứ mới) |
| Mức trong file này | R19, R20: BẮT BUỘC | R34: NÊN |

## 2. Yêu cầu

### BHYT-GD-R01 — Chấp nhận mọi hình thức xuất trình thẻ
- **Căn cứ**: Luật 51/2024 Đ1 k14 (sửa Đ16 k1 Luật BHYT): thẻ BHYT "được cấp bằng bản điện tử, bản giấy và có giá trị pháp lý như nhau". NĐ 188 Đ11 k1 (bản giấy chỉ khi người tham gia đề nghị); Đ37 k1 (xuất trình căn cước/VNeID mức 2 đã tích hợp thẻ, hoặc thẻ điện tử/giấy; thẻ chưa có ảnh kèm giấy tờ nhân thân), k2 (trẻ dưới 6 tuổi chỉ cần thẻ hoặc mã số; chưa có thì giấy chứng sinh), k4 (người hiến bộ phận). TT 09/2026/TT-BTC Đ6 k3: cơ sở "không yêu cầu người tham gia cung cấp thẻ bảo hiểm y tế bản giấy khi khám bệnh, chữa bệnh bằng thẻ bảo hiểm y tế bản điện tử và có trách nhiệm tra cứu giá trị sử dụng thẻ"; Đ8 k2 (thẻ trên VssID cấp trước 03/02/2026 vẫn có giá trị như bản giấy). CV 1804/BHXH-QLT, CV 2036/BHXH-CSYT: tra bằng số định danh cá nhân, mã số BHXH 10 số dùng song song. QĐ 1666/QĐ-BHXH Đ3 k1 (mẫu thẻ 2021).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tiếp đón nhận số định danh (quét QR căn cước), mã số BHYT (10 số theo mẫu thẻ 2021, 15 ký tự theo mã thẻ cũ và dữ liệu Cổng), dữ liệu VNeID/VssID; ký hiệu mức hưởng 1–5 và K1/K2/K3 in trên thẻ giấy chỉ để đối chiếu, mức hưởng áp dụng lấy theo Cổng; không có trường bắt buộc ảnh/scan thẻ giấy; lưu `hinh_thuc_xuat_trinh`; nhánh riêng trẻ dưới 6 tuổi và người hiến.
- **Bẫy**: thông tin thẻ đồng bộ theo cả mã số BHYT và số căn cước (NĐ 188 Đ10 k3). Quân đội, công an chưa có thông tin thẻ trên hệ thống vẫn xuất trình thẻ giấy (Đ37 k1 b) — đừng chặn cứng "chỉ thẻ điện tử".

### BHYT-GD-R02 — Tra cứu thẻ trên Cổng và lưu kết quả
- **Căn cứ**: TT 12/2026 Đ4 k1 (tra cứu thẻ, lịch sử KCB khi người bệnh đến, trong điều trị hoặc khi kết thúc lượt), k2 (Cổng trả thông tin thẻ, cùng chi trả lũy kế trong năm, thẻ bị thu hồi/tạm giữ/tạm khóa, lịch sử KCB); Đ2 k1 (Cổng `https://gdbhyt.baohiemxahoi.gov.vn`). TT 48 Đ13 k2; Đ6 k2 a (lịch sử KCB tối thiểu 06 tháng). Luật BHYT Đ16 k4 a (Luật 51 không sửa): thẻ đã hết thời hạn sử dụng thì không có giá trị sử dụng; Đ16 k3 b: tham gia liên tục thì giá trị nối tiếp. CV 497/BHXH-CNTT (hàm `KQNhanLichSuKCB2019`): mã kết quả 000 thẻ đúng; 001, 002 thẻ BQP, BCA quản lý → kiểm thẻ và giấy tờ tùy thân; 003, 004 thẻ cũ được cấp thẻ mới → dùng `maTheMoi`, `gtTheTuMoi`, `gtTheDenMoi`; 010 hết giá trị; 050 không có thông tin thẻ; 051–053 mã thẻ sai; 060, 061 sai họ tên; 070 sai ngày sinh; 110 đã thu hồi; 120–124 đã báo giảm; 130 trẻ em không xuất trình thẻ; 100, 101, 205, 401 lỗi hệ thống, tham số, xác thực.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 10/02/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tra cứu ở 3 thời điểm (tiếp đón, khi cần trong điều trị, trước khi kết thúc lượt/ra viện); lưu nguyên phản hồi gắn lượt KCB; cảnh báo chặn khi thẻ thu hồi/tạm khóa (110, 120–124); 001, 002 kiểm thẻ và giấy tờ tùy thân theo chính mô tả mã; 050–070 cũng chuyển sang kiểm giấy tờ thay vì chặn cứng (suy luận: BQP, BCA có thể chưa có dữ liệu trên hệ thống, NĐ 188 Đ37 k1; không chặn người có quyền hưởng, NĐ 90 Đ95 k1 a); 100, 101, 205, 401 đi nhánh Cổng lỗi R03; so hạn thẻ với **thời điểm đến khám**; hiển thị lịch sử KCB cho bác sĩ. Phần dữ liệu đưa vào XML, bảng kê: BHYT-DATA-R04.
- **Bẫy**: "6 lần khám trong 12 tháng" là chữ của dự thảo cổng; TT 12 bản gốc dẫn TT 48 Đ6 k2 a (06 tháng).

### BHYT-GD-R03 — Dự phòng khi VNeID/VssID/Cổng lỗi
- **Căn cứ**: NĐ 188 Đ38 k2: không xuất trình được thẻ điện tử do lỗi thì người bệnh cung cấp mã số thẻ; Cổng không tra được thì cơ sở ghi nhận mã số, **vẫn tiếp nhận** và tra lại sau; đến khi kết thúc lượt mà vẫn lỗi thì gửi BHXH hồ sơ KCB, thông tin liên hệ người bệnh kèm ảnh màn hình tra cứu.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trạng thái `the_chua_xac_minh`; hàng đợi tra lại tự động; lưu bằng chứng lỗi (ảnh màn hình hoặc log có timestamp, mã lỗi); xuất gói hồ sơ cho BHXH khi ra viện mà thẻ vẫn chưa xác minh.
- **Bẫy**: không được từ chối tiếp nhận chỉ vì Cổng lỗi.

### BHYT-GD-R04 — Không đặt thêm thủ tục; sao chụp phải có đồng ý
- **Căn cứ**: NĐ 188 Đ38 k3 (không quy định thêm thủ tục; cần sao chụp thì cơ sở tự sao chụp sau khi người bệnh đồng ý, không bắt người bệnh tự sao, không thu phí); NĐ 90 Đ95 k1 a (gây khó khăn, cản trở KCB BHYT).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: scan giấy tờ là tùy chọn, có trường ghi nhận đồng ý (người đồng ý, thời điểm); bảng giá không có phí sao chụp.

### BHYT-GD-R05 — Mã thẻ tạm trẻ dưới 6 tuổi, người hiến bộ phận
- **Căn cứ**: NĐ 188 Đ50 k1 a (tra mã thẻ tạm trên Cổng; chưa có thì nhập thông tin để Cổng cấp tự động); Đ37 k2 (trẻ vừa sinh: cha mẹ hoặc thân nhân ký xác nhận trên HSBA).
- **Áp dụng**: cơ sở có nhi, sản, ghép tạng · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: luồng lấy/đề nghị mã thẻ tạm; liên kết mã tạm với mã chính thức; trường xác nhận của cha/mẹ trên HSBA trẻ sơ sinh.

### BHYT-GD-R06 — Xuất trình thẻ muộn và cấp cứu
- **Căn cứ**: NĐ 188 Đ38 k1, Đ50 k6 (xuất trình muộn: quỹ trả từ thời điểm xuất trình, trừ cấp cứu; phần trước thanh toán trực tiếp theo Đ55–57); Luật 51 Đ1 k23 (Đ28 k1) và NĐ 188 Đ37 k5 (cấp cứu xuất trình trước khi kết thúc đợt). Luật KCB Đ7 k2 (cấm "từ chối hoặc cố ý chậm cấp cứu người bệnh", trừ Đ40; kể cả khi được từ chối vẫn phải sơ cứu, cấp cứu đến khi chuyển giao, Đ40 k1).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/01/2025; 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lưu `thoi_diem_xuat_trinh_the`; tách chi phí trước/sau mốc (trừ cấp cứu); in chứng từ phần tự trả để người bệnh làm thanh toán trực tiếp. Lượt cấp cứu không bị chặn bởi tra thẻ, tạm ứng hay giấy tờ: mọi bước bắt buộc ở tiếp đón có nhánh bỏ qua cho cấp cứu, ghi lại để bổ sung sau (suy luận từ Đ7 k2).

### BHYT-GD-R07 — Kiểm tra lại mức hưởng trước khi kết thúc lượt
- **Căn cứ**: NĐ 188 Đ21 k1 (nhiều mức hưởng thì lấy mức cao nhất), k2 (mức mới tính từ khi thẻ mới có giá trị; cơ sở phải kiểm tra quyền lợi, mức hưởng trước khi kết thúc lượt, ra viện); NĐ 90 Đ90 (xác định quyền lợi sai thông tin trên thẻ).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bắt buộc tra lại thẻ (R02) trước khi chốt ra viện/thanh toán; chia giai đoạn mức hưởng theo ngày thẻ mới; chọn mức cao nhất khi nhiều thẻ (TT 48 Đ4 k3 b).

### BHYT-GD-R08 — Thẻ hết hạn khi đang điều trị
- **Căn cứ**: NĐ 188 Đ50 k4 (thẻ còn hạn khi vào, hết hạn khi đang điều trị nội trú, ban ngày, ngoại trú: quỹ trả đến khi ra viện, tối đa 15 ngày từ ngày thẻ hết hạn).
- **Áp dụng**: cơ sở có điều trị · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: ngày được hưởng = min(ngày ra, ngày hết hạn + 15); phần vượt chuyển người bệnh tự trả, có cảnh báo.
- **Bẫy**: 15 ngày chỉ áp cho thẻ **còn hạn khi vào** rồi hết hạn trong đợt. Thẻ đã hết hạn lúc tiếp đón thì không có giá trị (Luật BHYT Đ16 k4 a); không có "ân hạn" ở tiếp đón (chữ "ân hạn" không có trong văn bản nào). Thẻ tham gia liên tục có giá trị nối tiếp (Đ16 k3 b): Cổng trả 003/004 thì lấy hạn thẻ mới.

### BHYT-GD-R09 — Miễn cùng chi trả
- **Căn cứ**: Luật 51 Đ1 k17 (Đ22 k1 d Luật BHYT); NĐ 188 Đ18 k2 (100% từ khi đồng thời đủ 5 năm liên tục và cùng chi trả lũy kế vượt ngưỡng, đến hết 31/12; điểm b: BHXH công bố lũy kế và thời điểm đủ 5 năm trên Cổng, cơ sở căn cứ đó; điểm c: quy đổi khi lương cơ sở đổi); TT 12 Đ4 k2.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: lấy lũy kế từ Cổng khi tiếp đón; cộng dồn cùng chi trả trong lượt; tự chuyển 100% từ thời điểm vượt ngưỡng, kể cả giữa lượt; lượt vắt qua 01/01 tính theo từng năm.
- **Bẫy**: luật dùng "mức tham chiếu", tạm theo lương cơ sở đến khi Chính phủ quyết định khác (Luật 51 Đ3 k5 b) — tham số hóa.

### BHYT-GD-R10 — Mức hưởng theo cấp CMKT, lộ trình 2026
- **Căn cứ**: Luật 51 Đ1 k17 (Đ22 k1, k3, k4, k5); NĐ 188 Đ19 (từ 01/01/2025 ngoại trú tại cơ sở cấp cơ bản dưới 50 điểm hoặc tạm xếp cấp cơ bản: 100% mức hưởng; **từ 01/07/2026** 50% mức hưởng khi ngoại trú tại k2 cơ sở cấp cơ bản 50 đến dưới 70 điểm, k3 cơ sở cấp cơ bản trước 01/01/2025 là tuyến tỉnh/TW, k4 cơ sở cấp chuyên sâu trước 01/01/2025 là tuyến tỉnh); TT 01/2025 Đ4 (lưu trú dưới 30 ngày, VNeID mức 2); Luật Đ22 k5 (cấp cứu tại bất kỳ cơ sở nào được hưởng 100% **mức hưởng** của thẻ theo k1, tức 80/95/100% tùy đối tượng; không phải quỹ trả 100% chi phí); NĐ 188 Đ35 k2 e (công khai kết quả xếp cấp kèm điểm).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/01/2025; 01/07/2026 (đã qua)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cấu hình cơ sở: cấp CMKT, điểm xếp cấp, cờ tuyến cũ trước 01/01/2025; bảng quy tắc tỷ lệ theo (cấp, nội/ngoại trú, đúng/không đúng nơi đăng ký, lý do: cấp cứu, chuyển đúng trình tự, lưu trú, tạm trú, bệnh hiếm Đ22 k4 a, nơi sinh sống K1/K2/K3 khi nội trú cấp chuyên sâu Đ22 k4 b) có ngày hiệu lực. Ánh xạ sang mã đối tượng KCB PL1 QĐ 3276 (`BHYT-DATA-R16`): NĐ 188 Đ19 k1 → 1.12, k2 → 1.13, k3 → 1.14, k4 → 1.18; Luật Đ22 k4 b → 3.6. Không còn lý do "thông tuyến".
- **Bẫy**: mã hóa `MUC_HUONG` trong XML: BHYT-DATA-R11.

### BHYT-GD-R11 — Phiếu chuyển cơ sở KCB
- **Căn cứ**: Luật 51 Đ1 k22–23 (Đ27, Đ28 k3); TT 01/2025 Đ9, Đ12 k1 (Phiếu chuyển PL VI, giấy hoặc điện tử, giá trị 10 ngày làm việc từ ngày ký), k2 (bệnh PL III: 01 năm; hết hạn khi đang điều trị dùng đến hết đợt), k4, k5; ghi chú PL VI (phiếu trên VNeID ký số đầy đủ tương đương bản giấy); TT 06/2026 Đ5 k2 (bản điện tử dùng ký số xác thực của cơ sở thay "ký tên, đóng dấu" từ 01/06/2026).
- **Áp dụng**: BV, PK BHYT · **Hiệu lực/hạn**: 01/01/2025; 01/06/2026 (đã qua)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phát hành phiếu chuyển điện tử PL VI có ký số người ký và ký số cơ sở; tính `han_su_dung` (10 ngày làm việc hoặc 01 năm theo PL III, có lịch nghỉ); tiếp nhận phiếu đến và kiểm còn hạn; đẩy XML13 (BHYT-DATA-R26) và hiển thị VNeID qua luồng SKDT.
- **Bẫy**: TT 01 đọc riêng còn ghi "đóng dấu". Thuật ngữ đổi sang "chuyển cơ sở KCB", tên bảng XML vẫn "giấy chuyển tuyến".

### BHYT-GD-R12 — Phiếu hẹn khám lại
- **Căn cứ**: Luật 51 Đ1 k23 (Đ28 k2); TT 01/2025 Đ11 (ghi trên Phiếu hẹn PL V hoặc trong đơn thuốc, giấy ra viện; bản điện tử có ký số bác sĩ; mỗi phiếu dùng 01 lần; ghi sổ hẹn hoặc dữ liệu điện tử; k5 chỉ hẹn một lần sau khi kết thúc một đợt); TT 06/2026 Đ5 k2 (ký số cơ sở thay dấu từ 01/06/2026).
- **Áp dụng**: BV, PK BHYT · **Hiệu lực/hạn**: 01/01/2025; 01/06/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phiếu hẹn có ID duy nhất, khóa `da_su_dung` sau lần dùng đầu; ký số bác sĩ và cơ sở; chặn phiếu hẹn thứ hai cho cùng đợt đã kết thúc; đẩy XML14.

### BHYT-GD-R13 — Chuyển người bệnh/mẫu làm DVCLS
- **Căn cứ**: Luật 51 Đ1 k25 (Đ31 k3); NĐ 188 Đ44 k1 (chỉ chuyển đến cơ sở được phê duyệt; cơ sở nhận không chuyển tiếp sang bên thứ ba), k2 a (DVCLS đã phê duyệt nhưng tạm không làm được: điền **Mẫu số 9** và gửi BHXH danh sách), k2 b (DVCLS chưa phê duyệt: hợp đồng nguyên tắc và danh sách gửi BHXH trước khi làm), k3 (cơ sở chuyển tổng hợp chi phí vào hồ sơ; người bệnh trả thêm thì báo và được đồng ý trước), k4 (giá).
- **Áp dụng**: cơ sở chuyển và nhận DVCLS (gồm phòng xét nghiệm tư) · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: phát hành Mẫu số 9 (lý do; người bệnh hay mẫu; thẻ, `MA_LOAI_KCB`, chẩn đoán); nhập kết quả và giá của cơ sở thực hiện vào dòng DVKT hồ sơ gốc; báo cáo danh sách DVCLS đã chuyển; ghi nhận đồng ý khi phát sinh chi phí ngoài.

### BHYT-GD-R14 — Liên thông kết quả CLS từ 01/01/2027
- **Căn cứ**: Luật 51 Đ3 k4 (chậm nhất 01/01/2027 liên thông, sử dụng kết quả CLS giữa cơ sở KCB BHYT theo quy định của Chính phủ); Đ1 k3 (Đ6 k3: BYT quy định CNTT, chia sẻ dữ liệu, liên thông CLS).
- **Áp dụng**: mọi cơ sở KCB BHYT có CLS · **Hiệu lực/hạn**: 01/01/2027 (sắp tới)
- **Mức**: BẮT BUỘC? (mốc luật định nhưng NĐ 188 không có điều chi tiết; dự thảo của BYT đang lấy ý kiến)
- **Phần mềm phải**: (chuẩn bị) kết quả CLS có định danh người bệnh, thời điểm lấy mẫu, người thực hiện, mã dịch vụ chuẩn; nhận kết quả từ cơ sở khác và đánh dấu "kết quả liên thông, không tính phí lại". Chi tiết: CLS.

### BHYT-GD-R15 — Điều kiện ký hợp đồng: kết nối, Mẫu 8
- **Căn cứ**: NĐ 188 Đ22 k2 (điều kiện ký HĐ: bảo đảm tiêu chuẩn kết nối, liên thông dữ liệu với hệ thống giám định theo quy định của Bộ trưởng BYT và xác thực dữ liệu); Đ26 k1 h (hồ sơ ký HĐ có bảng kê thiết bị phần mềm, phần cứng **Mẫu số 8**: phần cứng — máy chủ, máy trạm, lưu trữ, UPS, LAN, Internet; HIS — tên, thời điểm dùng, nhà cung cấp, nguồn gốc thuê/mua/tự phát triển, tình trạng); Đ68 k5 b (duy trì tiêu chuẩn kết nối đã được xác thực trong suốt HĐ); Đ35 k2 d (hạ tầng CNTT, nâng cấp HIS theo chuẩn dữ liệu).
- **Áp dụng**: mọi cơ sở ký HĐ BHYT, kể cả PK tư · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: vendor cung cấp thông tin điền Mẫu 8; HIS xuất đúng chuẩn QĐ 130/3176 và ký số (R18) trước ngày ký HĐ.
- **Bẫy**: NĐ 188, TT 12, TT 48 **không có** thủ tục chứng nhận, kiểm thử hay "xác thực phần mềm HIS". Thực tế: tài khoản Cổng + đăng ký chứng thư số trên Cổng + gửi được XML hợp lệ. "Đã được xác thực" (Đ68 k5 b) nhiều khả năng là kết nối được BHXH chấp nhận lúc ký HĐ (suy luận).

### BHYT-GD-R16 — Tài khoản Cổng
- **Căn cứ**: TT 12/2026 Đ3 k1–4 (01 tài khoản quản trị cấp sau khi ký HĐ lần đầu, khai **Mẫu 08/BH**; BHXH đối chiếu trong 01 ngày làm việc; tài khoản quản trị tạo, phân quyền, hủy tài khoản giao dịch); Đ16 k3 b (đúng mục đích, không dùng chung tài khoản, ATTT, bảo vệ thông tin người bệnh); TT 48 Đ13 k4 (báo BHXH khi đổi người được ủy quyền).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 10/02/2026
- **Mức**: BẮT BUỘC (cơ sở) · BẮT BUỘC? (yêu cầu lên phần mềm, vì HIS thường gọi API bằng một tài khoản kỹ thuật)
- **Phần mềm phải**: thông tin xác thực Cổng trong kho bí mật (không plaintext trong DB/config); mỗi lời gọi API ghi `nguoi_dung_HIS`, `tai_khoan_cong`, `ma_giao_dich`; nhiều tài khoản giao dịch theo vai trò; quy trình xoay mật khẩu khi đổi người phụ trách.
- **Bẫy**: API token gửi mật khẩu MD5 viết hoa là yêu cầu của BHXH; đừng dùng MD5 để lưu mật khẩu nội bộ.

### BHYT-GD-R17 — Tài khoản HIS cá nhân, cấm mượn
- **Căn cứ**: NĐ 90/2026 Đ95 k1 c (phạt hành vi dùng tài khoản phần mềm quản lý bệnh viện cấp cho người khác hoặc cho người khác mượn tài khoản để khám, chỉ định CLS, phẫu thuật, thủ thuật, kê đơn; 500.000–1.000.000 đ cá nhân, tổ chức ×2; diễn giải từ bản OCR); TT 12 Đ10 k1 g (giám định tự động rà phạm vi hành nghề, thời gian làm việc).
- **Áp dụng**: mọi cơ sở dùng HIS · **Hiệu lực/hạn**: 15/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tài khoản định danh theo người; xác thực mạnh (MFA hoặc ký số khi ký y lệnh); phát hiện phiên đồng thời nhiều máy; audit ai chỉ định, ai kê đơn; `MA_BAC_SI` lấy từ tài khoản đăng nhập, không chọn tự do; kiểm lịch làm việc và phạm vi hành nghề (02/DM) trước khi cho chỉ định.

### BHYT-GD-R18 — Ký số, xác thực dữ liệu đề nghị thanh toán
- **Căn cứ**: NĐ 188 Đ69 k9 ("Việc triển khai xác thực dữ liệu điện tử chi phí khám bệnh, chữa bệnh bảo hiểm y tế thực hiện chậm nhất từ ngày 01 tháng 01 năm 2026."); Đ35 k2 c (gửi dữ liệu sau mỗi lượt, ký số bảng tổng hợp tháng, quý, xác thực dữ liệu); TT 12 Đ2 k2 (tài liệu, dữ liệu gửi Cổng phải ký số theo pháp luật GDĐT), Đ9 k1 (hồ sơ đề nghị thanh toán "được ký số xác thực theo quy định tại điểm c khoản 2 Điều 35 và khoản 9 Điều 69"); TT 48 Đ7 k1 b. Kỹ thuật: BHYT-DATA-R07.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/01/2026 (đã qua)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: ký số tổ chức từng hồ sơ XML trước khi gửi; quản lý chứng thư (hạn, cảnh báo trước 30 ngày, đăng ký chứng thư mới lên Cổng); xác minh chữ ký trước khi gửi; lưu bản đã ký đúng như đã gửi (bất biến, có hash).
- **Bẫy**: "xác thực dữ liệu" là ký số hồ sơ chi phí, không phải xác thực sinh trắc người bệnh (căn cứ: TT 12 Đ9 k1 dẫn ngược Đ69 k9). TT 48 Đ6 k3 cho dữ liệu "phục vụ quản lý" không cần xác thực, nhưng hướng dẫn BHXH yêu cầu ký cả XML0 — nên ký mọi thứ. Đặc tả ghi "bắt buộc ký từ 01/12/2024 theo CV 3700/BHXH-CNTT" là sai căn cứ: CV 3700 là đề nghị BHXH gửi BYT (dẫn QĐ 2733, thí điểm Sổ SKĐT), BYT trả lời bằng CV 7506/BYT-BH đòi lộ trình; mốc ràng buộc là NĐ 188 Đ69 k9 (01/01/2026).

### BHYT-GD-R19 — Gửi dữ liệu sau mỗi lượt (đang có hiệu lực)
- **Căn cứ**: TT 48 Đ6 k1 (gửi "ngay sau khi kết thúc lần khám bệnh hoặc kết thúc đợt điều trị ngoại trú hoặc kết thúc đợt điều trị nội trú", trừ Đ8); Đ13 k7 (kết thúc vào ngày nghỉ, lễ, Tết thì gửi ngày làm việc kế tiếp), k8 (gửi dữ liệu thanh toán cùng lúc dữ liệu quản lý); Đ5 (4 phương thức, kết quả như nhau). NĐ 188 Đ35 k2 c.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/03/2018; đến khi văn bản thay TT 48 có hiệu lực
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sự kiện kết thúc lượt tự đưa hồ sơ vào hàng đợi gửi; check-in khi bắt đầu lượt (BHYT-DATA-R03); retry có backoff; lưu `maGiaoDich`, `thoiGianTiepNhan` làm bằng chứng thời điểm (TT 12 Đ2 k3).
- **Bẫy**: TT 12 Đ9 k2 a: Cổng phản hồi trong 06 giờ với hồ sơ gửi không đúng thời hạn → trễ hạn đã bị đo tự động.

### BHYT-GD-R20 — Cửa sổ 07 ngày làm việc, kỳ cuối tháng trước ngày 05 (đang có hiệu lực)
- **Căn cứ**: TT 48 Đ7 k1 (trong 07 ngày làm việc từ ngày kết thúc KCB: a kiểm tra, hiệu chỉnh; b xác thực; c gửi đề nghị thanh toán đến Cổng tiếp nhận dữ liệu y tế của BYT **và** Cổng giám định BHYT; d phát sinh cuối tháng, quý, năm gửi trước ngày 05 tháng kế tiếp); Đ13 k9 (hiệu chỉnh đã gửi: lý do, thống nhất BHXH); TT 12 Đ9 k1.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trạng thái `nhap → da_gui_quan_ly → da_hieu_chinh → da_ky → da_gui_thanh_toan`; đếm ngược 07 ngày làm việc theo lịch nghỉ; cảnh báo kỳ cuối tháng trước ngày 05; mọi hiệu chỉnh sau gửi có `ly_do` và tham chiếu.
- **Bẫy**: nghĩa vụ gửi song song Cổng BYT (TT 48 Đ7 k1 c; NĐ 188 Đ71 k1 c) hay bị quên; tình trạng vận hành Cổng BYT chưa xác minh (xem HTTT-BC).

### BHYT-GD-R21 — Gửi chậm có lý do và bằng chứng sự cố
- **Căn cứ**: TT 48 Đ8 k1 (sự cố bất khả kháng; mất điện, mất Internet), k2 (báo ngay bên kia; gửi ngay khi khắc phục), k3 (mất điện/mạng: hình thức, thời gian do hai thủ trưởng quyết, ghi trong HĐ). TT 12 Đ2 k4 (BHXH báo bảo trì trước ≥ 12 giờ; báo sự cố và thời điểm hoạt động lại ≤ 01 giờ sau khắc phục; hạn gửi gia hạn tương ứng).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: nhật ký sự cố (nguồn HIS/mạng/điện/Cổng; bắt đầu, kết thúc, người báo, kênh báo); gắn hồ sơ trễ với sự cố; tự cộng thời gian Cổng ngừng vào hạn; lưu thông báo bảo trì của Cổng.

### BHYT-GD-R22 — Xử lý phản hồi tự động của Cổng
- **Căn cứ**: TT 12 Đ9 k2 (Cổng phản hồi: a ≤ 06 giờ khi gửi sai thời hạn; b ≤ 24 giờ khi sai cấu trúc, định dạng, ghi rõ lỗi từng trường; c ≤ 48 giờ khi Bảng tổng hợp lệch Bảng kê hoặc Báo cáo quyết toán lệch Bảng tổng hợp), k3 (trong 02 ngày làm việc gửi bản điều chỉnh kèm văn bản ghi rõ số liệu sửa); TT 48 Đ7 k3 c.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 10/02/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kéo phản hồi lỗi, ánh xạ về hồ sơ, bảng, trường; hàng việc "sửa lỗi Cổng" hạn 02 ngày làm việc; sinh văn bản giải trình số liệu.

### BHYT-GD-R23 — Giám định tự động, Mẫu 09/BH
- **Căn cứ**: TT 12 Đ10 k1 (11 nội dung: thẻ; mức hưởng; phạm vi theo danh mục cơ sở; mức thanh toán; tỷ lệ, điều kiện; phạm vi chuyên môn, thời gian hoạt động cơ sở; phạm vi hành nghề, thời gian làm việc người hành nghề; khoảng cách giữa các lần KCB; hợp lý theo tiêu chí BYT; số liệu thống nhất trong bảng kê; số lượng thuốc, TBYT so với mua sắm/điều chuyển), k2 (kết quả trong 07 ngày làm việc), k3 (trong 03 ngày làm việc cơ sở gửi tài liệu chứng minh hoặc Bảng kê chi tiết điều chỉnh **Mẫu 09/BH**), k4 (vẫn sai thì từ chối). Mẫu 09/BH: Cổng điền cột A–Q (XML1_ID, ID chi phí, số bảng, mã liên kết, STT trong file gốc…); cơ sở điền cột T, R, S, (1), trạng thái "2"/"3" khi tự đề nghị điều chỉnh, bổ sung; ký số.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: Mẫu 09/BH từ 01/04/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: nhập kết quả giám định theo dòng chi phí; workflow giải trình 03 ngày làm việc; sinh Mẫu 09/BH ký số; lưu XML1_ID/ID chi phí do Cổng trả về.

### BHYT-GD-R24 — Giám định chủ động: cung cấp HSBA trong 03 ngày làm việc
- **Căn cứ**: TT 12 Đ11 k3 a (BHXH báo trước ≥ 03 ngày làm việc; cơ sở cung cấp đủ hồ sơ trong 03 ngày làm việc từ khi nhận yêu cầu); Đ5 k2, Đ12 k4 (trung thực, khớp giữa Bảng kê, Bảng tổng hợp, Báo cáo quyết toán, HSBA).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 10/02/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: từ danh sách BHXH yêu cầu (MA_LK hoặc mã thẻ, ngày) xuất trọn gói HSBA đã ký, y lệnh, kết quả CLS, phiếu công khai thuốc, hóa đơn; đối chiếu tự động mỗi dòng XML2/XML3 với y lệnh và phiếu thực hiện. Cấp quyền tạm cho giám định viên: EMR-R15.

### BHYT-GD-R25 — Bảng tổng hợp 01/BH, quyết toán 02/BH
- **Căn cứ**: Luật 51 Đ1 k26 (Đ32 k2 a: 15 ngày đầu mỗi tháng gửi tổng hợp tháng trước; 15 ngày đầu mỗi quý gửi quyết toán quý trước); TT 12 Đ5 k1 b, c, Đ9 k1, k4 (HĐ cho nhiều cơ sở trực thuộc thì tổng hợp cả nhóm); PL I Mẫu 01/BH (4 mục theo `MA_LOAI_KCB`: I 01, 06, 07; II 02, 05, 08; III 04, 09; IV 03; cột lấy từ XML1: `SO_NGAY_DTRI`, `T_TONGCHI_BV`, `T_TONGCHI_BH`, `T_BHTT`, `T_BNCCT`, `T_NGUONKHAC`, `T_BNTT`; ràng buộc cột 2 = 3 + 6 + 7, cột 3 = 4 + 5; làm tròn đồng); Mẫu 02/BH tổng hợp từ 01/BH. NĐ 90 Đ94 (chậm báo cáo quyết toán).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/BH từ 01/04/2026; quyết toán quý I/2026 dùng mẫu cũ (TT 12 Đ17 k2)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh 01/BH, 02/BH từ đúng tập XML1 đã gửi (không nhập tay); kiểm ràng buộc cột trước khi ký; ký số người lập, kế toán trưởng, thủ trưởng; nhắc hạn ngày 15.
- **Bẫy**: Mẫu 01/BH dẫn `MA_LOAI_KCB` theo PL1 QĐ 824/2023 (bị QĐ 1804 bỏ từ 01/08/2026) → dùng QĐ 1804 theo TT 12 Đ17 k3 (BHYT-DATA-R14). QĐ 1804 có thêm mã 10–16 mà 4 nhóm I–IV chưa có chỗ; chưa có hướng dẫn xếp nhóm (rà đến 10/2026). Hồ sơ 01/BH gửi Cổng là danh sách từng hồ sơ có `MA_LOAI_KCB` (Tài liệu kỹ thuật TT 12) → giữ mã gốc, không tự tạo nhóm "Khác"; mẫu in xếp theo bản chất khám/điều trị (suy luận), hỏi BHXH tỉnh.

### BHYT-GD-R26 — Biên bản giám định, quyết toán, hóa đơn
- **Căn cứ**: TT 12 Đ12 k2 (02 ngày làm việc ký, gửi lại Biên bản giám định 03/BH; không đồng ý ghi rõ căn cứ); Đ14 k3 (02 ngày làm việc gửi Biên bản quyết toán 06/BH đã ký và hóa đơn điện tử khớp số quyết toán, hoàn trả tạm ứng thừa), k6 (chênh lệch thì lập hóa đơn điện tử mới cho phần chênh); Đ15 k1 (BHXH thanh toán trong 03 ngày làm việc). NĐ 188 Đ51 k2 (từ chối phải nêu căn cứ, lý do, số tiền), k3.
- **Áp dụng**: mọi cơ sở KCB BHYT (phân hệ tài chính) · **Hiệu lực/hạn**: 06/BH từ 01/04/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: theo dõi từng biên bản (nhận, hạn ký, đã ký); đối soát số quyết toán với hóa đơn BHYT; tạo hóa đơn điều chỉnh/bổ sung; sổ xuất toán theo hồ sơ và lý do để khiếu nại.
- **Bẫy**: TT 12 Đ14 k6 dẫn NĐ 123/2020 sửa bởi NĐ 70/2025 — cả hai hết HL từ 01/07/2026, thay bởi **NĐ 254/2026** (áp theo TT 12 Đ17 k3; xem TC-MS).

### BHYT-GD-R27 — Cảnh báo gia tăng chi
- **Căn cứ**: TT 12 Đ13 (trước ngày 15 hằng tháng BHXH cảnh báo 3 mức; trong 10 ngày cơ sở rà soát, xác định nguyên nhân, có giải pháp); NĐ 188 Đ35 k1 b, k2 đ.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 10/02/2026
- **Mức**: BẮT BUỘC (tổ chức rà soát) · NÊN (công cụ phần mềm)
- **Phần mềm phải**: báo cáo chi bình quân theo lượt, khoa, bác sĩ, nhóm chi phí; so cùng kỳ; drill-down đến hồ sơ.

### BHYT-GD-R28 — Danh mục 01–06/DM: duyệt và áp dụng
- **Căn cứ**: TT 12 Đ7 k1–3 (danh mục theo QĐ 7603 và các QĐ sửa; định dạng PL II; ký số, gửi sau ký HĐ lần đầu; áp dụng từ ngày HĐ có hiệu lực, thuốc/TBYT không sớm hơn hợp đồng mua sắm); Đ8 (cập nhật theo NĐ 188 Đ24 k2, k3; BHXH xử lý ≤ 05 ngày làm việc; bị từ chối gửi lại trong 15 ngày; thuốc, TBYT mua cấp cứu theo ngày hóa đơn; sai lệch sửa/hủy trong 05 ngày làm việc).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/04/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: master data có `ngay_ap_dung_BHXH` và trạng thái duyệt Cổng từng mục; chặn hoặc cảnh báo khi kê thuốc, DVKT chưa được chấp nhận tại ngày y lệnh; lưu lịch sử phiên bản. Định dạng file, mô hình 2 dòng: BHYT-DATA-R19.
- **Bẫy**: Mẫu 07/BH dẫn mã khoa PL6 QĐ 2010 (bỏ từ 01/08/2026) → dùng QĐ 1804.

### BHYT-GD-R29 — Dữ liệu chi phí trung thực, truy vết được
- **Căn cứ**: NĐ 188 Đ68 k5 c; TT 48 Đ13 k1, k3; TT 12 Đ5 k2. NĐ 90 (mức cá nhân, tổ chức ×2 theo Đ4 k5; trần BHYT 75 triệu cá nhân, 150 triệu tổ chức theo Đ4 k3; kèm hoàn trả quỹ): Đ85 kê khống để chiếm đoạt (200.000–5.000.000 đ); Đ86 kê khống, kê tăng (200.000–20.000.000 đ); Đ88 áp sai giá, giá chưa duyệt, ghi sai chủng loại/hàm lượng/đơn vị/tên DVKT, hoặc đã chi từ nguồn khác (300.000–50.000.000 đ); Đ95 k3 lạm dụng chỉ định (1.000.000–40.000.000 đ).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 15/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi dòng XML2/XML3 truy vết tới y lệnh (người, thời điểm) và phiếu thực hiện/phát thuốc; giá lấy từ bảng giá đã duyệt theo ngày; cấm sửa trực tiếp số lượng, giá trên bảng kê không qua y lệnh; audit log bất biến cho mọi sửa sau kết thúc lượt.

### BHYT-GD-R30 — Kết nối, liên thông là nghĩa vụ có chế tài
- **Căn cứ**: NĐ 90 Đ95 k4 b (đã đối chiếu ảnh trang): phạt 1.000.000–3.000.000 đ (tổ chức 2.000.000–6.000.000 đ) hành vi "không kết nối, liên thông dữ liệu, tạo lập chứng từ điện tử về khám bệnh, chữa bệnh theo quy định về giao dịch điện tử trong lĩnh vực bảo hiểm y tế". NĐ 188 Đ67 k5, Đ68 k5 a.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 15/05/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: dashboard độ phủ: tỷ lệ lượt BHYT đã gửi, đã ký, đã được tiếp nhận; danh sách lượt chưa gửi quá hạn.
- **Bẫy**: không có điều riêng phạt chậm gửi XML (đã đọc Đ81–95); Đ94 chỉ phạt chậm báo cáo quyết toán.

### BHYT-GD-R31 — Bảo mật; hồ sơ bí mật nhà nước
- **Căn cứ**: NĐ 188 Đ66 k1, k3; TT 48 Đ9; TT 12 Đ16 k3 b; TT 12 Đ9 k5 (hồ sơ thuộc bí mật nhà nước lập, gửi theo pháp luật bảo vệ bí mật nhà nước).
- **Áp dụng**: mọi cơ sở; đặc biệt BV quân đội, công an · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: cờ `bi_mat_nha_nuoc` loại hồ sơ khỏi luồng gửi Cổng thông thường; TLS; phân quyền xem dữ liệu BHYT. DLCN chung: DLCN; XML: BHYT-DATA-R25.

### BHYT-GD-R32 — Báo vi phạm sử dụng thẻ
- **Căn cứ**: NĐ 188 Đ12 k4 (phát hiện vi phạm — thu hồi, gian lận, cho mượn thẻ — thì thông báo BHXH); NĐ 90 Đ84 (mượn thẻ).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: đối chiếu ảnh, nhân thân khi tiếp đón; chức năng "báo nghi vấn thẻ" lưu bằng chứng và trạng thái thông báo BHXH.

### BHYT-GD-R33 — Ký xác nhận khi người bệnh không làm thủ tục
- **Căn cứ**: TT 48 Đ13 k6 (người bệnh/đại diện không làm thủ tục thanh toán thì cơ sở ký xác nhận chi phí; thủ trưởng chịu trách nhiệm).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: hiện hành
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: trạng thái "người bệnh bỏ về/không ký"; luồng ký số thay của người được thủ trưởng ủy quyền, có lý do.

### BHYT-GD-R34 — Chuẩn bị cho dự thảo thay TT 48 (03 giờ)
- **Căn cứ**: **Dự thảo, chưa ban hành** (thứ cấp, báo): gửi dữ liệu chi phí đã ký xác thực lên Cổng tối đa 03 giờ từ khi kết thúc lượt, trừ trường hợp được gửi chậm; 15 ngày kiểm tra, đối chiếu trước khi đề nghị thanh toán; dữ liệu đã đề nghị thanh toán không được thay đổi (trừ một số trường hợp); kết quả giám định chi tiết trong 15 ngày; chế tài theo bậc.
- **Áp dụng**: mọi cơ sở KCB BHYT, vendor · **Hiệu lực/hạn**: dự kiến 01/01/2027
- **Mức**: NÊN (đến khi ban hành; nên làm ngay vì thời gian chuẩn bị ngắn)
- **Phần mềm phải**: pipeline gần thời gian thực, ký số tự động bằng chứng thư tổ chức (HSM hoặc ký từ xa); giám sát `t_gui − t_ket_thuc_luot ≤ 3h` từng hồ sơ; tách "gửi sớm" với "đề nghị thanh toán (≤ 15 ngày)"; khóa bất biến sau đề nghị thanh toán, mọi thay đổi sau đó qua luồng điều chỉnh có lý do.
- **Bẫy**: 03 giờ mâu thuẫn với 07 ngày làm việc và mốc ngày 05 đang hiện hành (R19, R20). Không viết "phải gửi trong 3 giờ" như nghĩa vụ hiện tại. Hệ thống cấu hình được cả hai chế độ theo ngày hiệu lực.

### BHYT-GD-R35 — Chi phí ngoài phạm vi phải thông báo trước
- **Căn cứ**: NĐ 188 Đ20 (quỹ trả theo phạm vi, mức hưởng; k2 cơ sở công khai khoản ngoài phạm vi, phần chênh lệch và phải thông báo trước cho người bệnh); Đ35 k2 i (không thu thêm chi phí đã trong kết cấu giá).
- **Áp dụng**: BV, PK có dịch vụ theo yêu cầu · **Hiệu lực/hạn**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: khi chỉ định dịch vụ theo yêu cầu/ngoài danh mục cho người có thẻ, hiển thị và ghi nhận xác nhận đã thông báo (người bệnh ký); tách đúng `T_BNTT` với `T_BNCCT`.
- **Bẫy**: nhóm quân đội, công an, cơ yếu (Luật Đ12 k3 a–đ) không tự trả chi phí ngoài phạm vi trong giới hạn NĐ 70/2015 Đ10 k2 (sửa bởi NĐ 74/2025), xem `BHYT-GD-R40`.

### BHYT-GD-R36 — Tiền khám nhiều chuyên khoa và định mức lượt khám/bàn khám
- **Căn cứ**: TT 35/2016 Đ4b (bổ sung bởi TT 39/2024 Đ1 k4): k1 vào nội trú qua khoa khám bệnh thì tính tiền khám theo k3, vào thẳng khoa lâm sàng không đăng ký khám thì không thanh toán tiền khám; k2 khám chuyên khoa tại khoa lâm sàng tính như khám tại khoa khám bệnh; k3 trong cùng một lần đến khám (có thể sang ngày tiếp theo) "từ lần khám thứ 02 chỉ tính 30% mức giá của 01 lần khám bệnh", tổng không quá 02 lần giá một lần khám; k4 khám lại trong ngày do bất thường là lần thứ 02 trở đi, trừ cấp cứu tính lần mới; k5 bàn khám trên **65 lượt/08 giờ** thì BHXH chỉ trả 50% giá khám từ lượt thứ 66, kéo dài tối đa 03 tháng liên tiếp thì không trả từ lượt 66 (giờ khám dài hơn thì quy đổi, ví dụ 10 giờ = 81 lượt). Đ4d k7 (quy tắc k5 chỉ áp giữa BHXH và cơ sở, **không** dùng để tính cùng chi trả của người bệnh), k8 (thiên tai, thảm họa, dịch bệnh có thông báo: trả theo thực tế). PL QĐ 697 Phần Một IV.3 quy ra tỷ lệ theo dịch vụ: lần 1 = 100%, lần 2–4 = 30%, lần 5 = 10%, từ lần 6 = 0%. TT 39 Đ2 k4: lượt trước 01/01/2025 áp văn bản cũ.
- **Áp dụng**: cơ sở KCB BHYT có khám bệnh · **Hiệu lực/hạn**: 01/01/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: đánh số thứ tự lần khám trong một lần đến khám (kể cả kéo sang ngày sau) và áp tỷ lệ theo dịch vụ ở cột 6 bảng kê (`BHYT-DATA-R21`); khám lại trong ngày tính lần 2+, cấp cứu tính lần mới; đếm lượt theo bàn khám và giờ tổ chức khám thực tế, cảnh báo trước ngưỡng; phần giảm do vượt định mức tách khỏi tiền cùng chi trả của người bệnh; cờ thời kỳ thiên tai, dịch để tắt quy tắc định mức.
- **Bẫy**: TT 22/2023 hết HL nhưng định mức 65 lượt và quy tắc 30% **vẫn còn**, căn cứ là TT 35 Đ4b (TT 39). Viết tắt "100/30/10/0" là sai, lần 3 và 4 vẫn 30%.

### BHYT-GD-R37 — Chi phí một lần KCB thấp
- **Căn cứ**: Luật 51 Đ1 k17 (Đ22 k1 b: 100% khi chi phí một lần KCB thấp hơn mức Chính phủ quy định); NĐ 188 Đ17 k1 (thấp hơn **15% mức lương cơ sở**), k2 (áp cả cho các trường hợp Luật Đ22 k3, k4, k5); CV 2275/BHXH-CSYT (30/06/2026) mục 1, 2: ở cơ sở có tỷ lệ theo nơi KCB dưới 100% (mã 1.13, 1.14, 1.18 = 50%), lượt có tổng chi dưới 15% LCS thì quỹ trả tổng chi × tỷ lệ nơi KCB, không phải 100%.
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 15/08/2025; ngưỡng đổi theo LCS (`BHYT-GD-R39`)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: so tổng chi BHYT của lượt với 0,15 × LCS theo ngày (so sánh chặt, dưới ngưỡng); dưới ngưỡng thì mức hưởng theo đối tượng = 100% nhưng **vẫn nhân** tỷ lệ theo nơi KCB; ghi ngưỡng đã dùng vào ảnh chụp kết quả tính.
- **Bẫy**: "chi phí thấp thì quỹ trả 100%" là sai ở cơ sở hưởng 50%/40%. CV 6872/BYT-BH mà một số đặc tả dẫn không tìm thấy ở đâu; căn cứ là NĐ 188 Đ17 và CV 2275.

### BHYT-GD-R38 — Trần gói thiết bị y tế 45 tháng lương cơ sở, stent phủ thuốc
- **Căn cứ**: TT 04/2017 Đ3 k2 b, c sửa bởi TT 24/2025 Đ1 k3 a, b (HL 01/09/2025; VBHN 14/VBHN-BYT): mỗi lần sử dụng DVKT là một gói TBYT, quỹ trả tối đa **45 tháng LCS × mức hưởng**; stent động mạch vành phủ thuốc: stent thứ 2 trả ½ giá, tối đa 18.000.000 đ; thứ 3, 4 trả ⅓, tối đa 12.000.000 đ mỗi stent; từ thứ 5 không trả; stent 2–4 tính ngoài gói. PL QĐ 697 mục 11 (gói TBYT). NĐ 70/2015 Đ2, Đ11 sửa bởi NĐ 74/2025 Đ1 k2, k10: nhóm quân đội, công an, cơ yếu, dân quân thường trực "không áp dụng tỷ lệ, mức thanh toán" → không áp trần.
- **Áp dụng**: cơ sở có DVKT dùng TBYT · **Hiệu lực/hạn**: 01/09/2025; trần đổi theo LCS (`BHYT-GD-R39`)
- **Mức**: BẮT BUỘC · BẮT BUỘC? (miễn trần cho nhóm NĐ 188 Đ16: chỉ có ở PL QĐ 697 mục 11; NĐ 188 Đ16 chỉ miễn tỷ lệ, VBHN 14 không còn câu miễn trần của TT 04 bản gốc)
- **Phần mềm phải**: gom TBYT theo từng lần DVKT thành gói; trần quỹ = 45 × LCS(ngày kết thúc DVKT) × mức hưởng; bỏ TBYT có tỷ lệ riêng ra khỏi tổng gói; quy tắc stent theo thứ tự; nhóm miễn trần cấu hình theo mã đối tượng, không hard-code; phần vượt trần chuyển người bệnh trả.
- **Bẫy**: "TT 24/2025 Đ1 k1" (PL QĐ 697, nhiều đặc tả) là dẫn sai, đúng là Đ1 k3 a. "NĐ 70 Điều 2" là **NĐ 70/2015/NĐ-CP** (BHYT quân đội, công an, cơ yếu), không phải NĐ 70/2025 (hóa đơn, đã hết HL). Không còn "trần DVKT cao chi phí lớn" riêng trong luật hiện hành (Luật 51 viết lại Đ22 và bỏ cụm này).

### BHYT-GD-R39 — Lương cơ sở (mức tham chiếu) theo giai đoạn
- **Căn cứ**: Luật 51 Đ3 k5 b (mức tham chiếu tạm theo lương cơ sở đến khi Chính phủ quy định khác); NĐ 161/2026/NĐ-CP Đ3 k2 (LCS **2.530.000 đ/tháng từ 01/07/2026**), Đ6 (thay NĐ 73/2024, LCS 2.340.000 đ); NĐ 188 Đ17 k1, Đ18 k2 a, c (quy đổi lũy kế khi LCS đổi), Đ57 (ngoại trú lấy ngày KCB, nội trú lấy ngày ra viện để xác định mức thanh toán); CV 2275/BHXH-CSYT (30/06/2026).
- **Áp dụng**: mọi cơ sở KCB BHYT · **Hiệu lực/hạn**: 2.340.000 đ đến 30/06/2026; 2.530.000 đ từ 01/07/2026
- **Mức**: BẮT BUỘC (bảng tham số, Đ57, Đ18 k2 c) · BẮT BUỘC? (ngày chốt LCS cho chi phí thấp và trần TBYT của lượt vắt qua mốc)
- **Phần mềm phải**: bảng `luong_co_so(tu_ngay, den_ngay, muc)`; mọi ngưỡng sinh từ bảng (0,15 × chi phí thấp; 6 × miễn cùng chi trả; 45 × trần gói TBYT); không hard-code số tiền. Lượt vắt qua mốc: chi phí thấp theo ngày kết thúc lượt/ra viện, trần TBYT theo ngày kết thúc từng DVKT (theo tiền lệ CV 3687/BYT-BH năm 2024, đọc qua CV 1311/BHXH Bình Định; năm 2026 chưa có văn bản chuyển tiếp, giữ cấu hình được và hỏi BHXH tỉnh).
- **Bẫy**: quy tắc kiểu "LCS theo ngày ra viện cho mọi ngưỡng" lệch ít nhất với trần TBYT và lũy kế cùng chi trả (Đ18 k2 c có công thức quy đổi riêng).

### BHYT-GD-R40 — Quyền lợi nhóm quân đội, công an, cơ yếu, dân quân thường trực
- **Căn cứ**: Luật BHYT Đ22 k1 a (Luật 51 Đ1 k17), đối tượng Đ12 k3 a–đ; NĐ 70/2015 Đ2, Đ10 k2, Đ11 sửa bởi NĐ 74/2025 Đ1 k2, k9, k10 (100%; không áp tỷ lệ, mức thanh toán do BYT quy định; chi phí ngoài phạm vi được quỹ trả nếu là thuốc, hóa chất, TBYT được cấp phép lưu hành và DVKT được phê duyệt theo chỉ định chuyên môn, không thuộc Luật Đ23; tự đi không đúng nơi thì 100/50/40% theo Đ11 k3); NĐ 188 Đ15 k2.
- **Áp dụng**: cơ sở KCB BHYT tiếp nhận nhóm này · **Hiệu lực/hạn**: 01/07/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: xác định nhóm theo mã đối tượng hoặc kết quả Cổng (không chỉ theo ký tự thẻ); không áp trần gói TBYT (`BHYT-GD-R38`); chi phí ngoài phạm vi đủ điều kiện NĐ 70 Đ10 k2 tính vào phần quỹ, không gán mặc định `T_BNTT`.
- **Bẫy**: ký hiệu mức hưởng "5" trên thẻ chỉ có căn cứ ở QĐ 1351/QĐ-BHXH (thứ cấp); thẻ BQP, BCA có thể chưa có dữ liệu trên Cổng (mã 001, 002 — `BHYT-GD-R02`).

### BHYT-GD-R41 — Ngày giường điều trị nội trú, giường lưu
- **Căn cứ**: TT 35/2016 Đ4c (bổ sung bởi TT 39/2024 Đ1 k4): k1 số ngày = ngày ra − ngày vào, **+1** khi tử vong, nặng xin về, chuyển cơ sở, hoặc đã qua cấp cứu rồi chuyển nơi khác tiếp tục nội trú; trên 04 giờ đến dưới 24 giờ tính 01 ngày; từ 04 giờ trở xuống không tính tiền giường (cấp cứu vào thẳng không tính giường hồi sức); k2 hai khoa trong ngày mỗi khoa ½; từ ba khoa lấy trung bình khoa giá cao nhất và thấp nhất trong các khoa nằm trên 04 giờ; k3 giường ngoại khoa, bỏng tối đa 10 ngày sau phẫu thuật, chuyển viện thì nơi nhận được 10 trừ số ngày nơi chuyển (nơi chuyển ghi ngày phẫu thuật trên giấy chuyển); k4 ghép 02 người ½, 03 người ⅓; băng ca, giường gấp 50%; giường hồi sức tích cực phải đủ điều kiện. PL QĐ 697 mục 2.1–2.3 và mục (9). Giường lưu: Luật KCB Đ77 k2 (PKĐK tư nhân vùng khó khăn, biên giới, hải đảo; PKĐK khu vực; nhà hộ sinh; trạm y tế xã; tối đa 72 giờ trừ bất khả kháng); QĐ 2010 PL3 mã `TYT.1925`, `PKKV.1925`.
- **Áp dụng**: cơ sở có điều trị nội trú, giường lưu · **Hiệu lực/hạn**: 01/01/2025 (TT 39 Đ2 k4: vào trước, ra sau mốc thì áp văn bản cũ)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tính ngày giường theo giờ vào/ra từng khoa, không theo ngày lịch; cờ tử vong/nặng xin về/chuyển viện để +1; bộ đếm 10 ngày sau phẫu thuật mang theo giấy chuyển; hệ số ghép giường, băng ca; tách "tổng số ngày điều trị" (để in) khỏi "số ngày giường thanh toán"; giường lưu chỉ bật cho loại cơ sở Đ77 k2, cảnh báo quá 72 giờ. Hệ số giường điều trị ban ngày lấy từ văn bản giá đã duyệt của cơ sở, không hard-code.
- **Bẫy**: TT 22/2023 hết HL nhưng quy tắc ngày giường **vẫn còn**, căn cứ là TT 35 Đ4c (TT 39). Hệ số 0,3 cho giường ban ngày không có trong thông tư nào, nó nằm trong văn bản giá của từng cơ sở (chưa đọc hết ảnh TT 21/2024 để loại trừ hẳn). Cách đếm ngày giường lưu PL 697 chỉ ghi "theo quy định của BYT", chưa thấy văn bản riêng (tạm áp Đ4c, suy luận).

### BHYT-GD-R42 — Nhiều can thiệp trong một lần phẫu thuật, DVKT dừng giữa chừng
- **Căn cứ**: TT 35/2016 Đ4d k2 (TT 39/2024 Đ1 k4): trả theo giá phẫu thuật phức tạp nhất, giá cao nhất; phẫu thuật phát sinh cùng kíp 50%, thay kíp 80%; thủ thuật phát sinh 80%; k11 giá phẫu thuật đã gồm gây mê/gây tê (trừ Mắt). PL QĐ 697 mục 7 (ghi ở cột tỷ lệ thanh toán theo dịch vụ). NĐ 188 Đ48: DVKT chỉ định nhưng không thể tiếp tục thì không kê DVKT, quỹ trả thuốc, TBYT, vật tư thực tế đã dùng.
- **Áp dụng**: cơ sở có phẫu thuật, thủ thuật · **Hiệu lực/hạn**: 01/01/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: gắn DVKT vào một ca phẫu thuật; đánh dấu DVKT chính (100%) và DVKT phát sinh với cờ cùng kíp / thay kíp / thủ thuật (50/80/80%); cờ "DVKT dừng giữa chừng" bỏ dòng DVKT, giữ thuốc, vật tư thực tế.

### BHYT-GD-R43 — Vận chuyển người bệnh
- **Căn cứ**: Luật BHYT Đ21 k1 b (Luật 51 Đ1 k16): đối tượng Đ12 k3 a, b, c, d, đ, e, h, i, o, r khi đang nội trú hoặc cấp cứu phải chuyển cơ sở; NĐ 188 Đ14 k1–k5: có giá vận chuyển được duyệt thì theo giá (cơ sở tư nhân tham chiếu giá cơ sở nhà nước); chưa có giá thì theo km thực tế, **0,2 lít xăng/km**, giá xăng tại thời điểm chuyển ghi trên giấy chuyển, **không áp tỷ lệ, mức hưởng**; trả cả chiều đi và về cho nơi chuyển; nhiều người một xe tính như một người; người bệnh tự túc thì trả một chiều; Đ50 k2. PL QĐ 697 mục 12. QĐ 3276 PL2: mã nhiên liệu.
- **Áp dụng**: cơ sở có chuyển người bệnh · **Hiệu lực/hạn**: 15/08/2025
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kiểm đối tượng và điều kiện (nội trú/cấp cứu + chuyển cơ sở); ba nhánh tính tiền (giá được duyệt, định mức xăng, tự túc); dòng vận chuyển không nhân mức hưởng; ghi giá xăng và km trên giấy chuyển.
- **Bẫy**: PL QĐ 697 vẫn dẫn "Đ27 Luật BHYT", căn cứ phạm vi đúng là Đ21 k1 b.

### BHYT-GD-R44 — Máu, chế phẩm máu, vận chuyển máu
- **Căn cứ**: Luật BHYT Đ21 k2 đ (Luật 51); TT 35/2016 Đ4a k1 a (máu, chế phẩm máu tính ngoài giá ngày giường, theo thực tế), Đ4d k5, k12 (TT 39); TT 15/2023/TT-BYT Đ3 k10–11, Đ5 k1–2 (vận chuyển máu tối đa 17.000 đ/đơn vị; xét nghiệm NAT, kháng thể bất thường cộng vào giá đơn vị máu), Đ7 (HL 15/09/2023, thay TT 17/2020); PL QĐ 697 mục 8 (tỷ lệ theo dịch vụ 100%, tỷ lệ BHYT 100%). Giá tối đa đơn vị máu: QĐ 3833/QĐ-BYT (19/12/2024) thay bảng giá Đ3 TT 15 (thứ cấp, chưa có bản gốc).
- **Áp dụng**: cơ sở có truyền máu · **Hiệu lực/hạn**: 15/09/2023
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kê máu theo đơn vị (mã PL9 QĐ 7603); giá không vượt giá tối đa; vận chuyển máu ≤ 17.000 đ/đơn vị; tách dòng máu khỏi giá giường.
- **Bẫy**: QĐ 3176 và nhiều HIS còn dẫn TT 17/2020 (hết HL 15/09/2023).

### BHYT-GD-R45 — Kháng sinh dấu (*) chỉ được quỹ trả khi kê đúng quy trình
- **Căn cứ**: TT 37/2024/TT-BYT Đ10 k5: thuốc có dấu (*) phải hội chẩn trước khi dùng, trừ cấp cứu; kháng sinh (*) quỹ trả khi kê đúng quy trình quản lý sử dụng kháng sinh của BYT; QĐ 5631/QĐ-BYT (31/12/2020, tài liệu chuyên môn, chưa có văn bản thay) mục 4.2: duyệt trước khi dùng hoặc trong 24–48 giờ với cấp cứu/ngoài giờ; mỗi lần duyệt không quá 14 ngày; PL2 ngoại lệ khoa.
- **Áp dụng**: cơ sở kê kháng sinh BHYT · **Hiệu lực/hạn**: TT 37/2024 hiện hành
- **Mức**: BẮT BUỘC (điều kiện thanh toán) · NÊN (cách phần mềm chặn/cảnh báo)
- **Phần mềm phải**: cờ thuốc (*) theo danh mục BHYT; phiếu yêu cầu/duyệt kháng sinh gắn đơn; cảnh báo hoặc chặn đưa vào hồ sơ thanh toán khi thiếu duyệt (trừ cấp cứu có duyệt bù); hạn 14 ngày mỗi lần duyệt.
- **Bẫy**: QĐ 5631 chỉ có bản đăng lại (thứ cấp); danh mục thuốc BHYT mới dự kiến 2026 (chưa ban hành) có thể đổi danh sách (*).

**Tổng**: 45 yêu cầu. BẮT BUỘC 41 (R01–R13, R15, R17–R26, R28–R33, R35–R45; R38, R39 có phần BẮT BUỘC?); BẮT BUỘC? 2 (R14; R16 phần yêu cầu phần mềm); NÊN 2 (R27 phần công cụ phần mềm; R34 dự thảo).

## 3. Pattern thiết kế

### BHYT-GD-P01 — Lượt KCB BHYT và nhật ký thẻ
- **Giải quyết**: R02, R03, R06, R07, R08, R09
- **Cách làm**: mọi tra cứu thẻ append-only; mức hưởng lưu dạng giai đoạn để chia khi đổi thẻ, vượt ngưỡng cùng chi trả, thẻ hết hạn + 15 ngày; không cho chốt ra viện khi chưa có tra cứu `thoi_diem ≥ ngay_ra − X` (X cấu hình).
- **Gợi ý dữ liệu**: `bhyt_the_tra_cuu(id, luot_kcb_id, thoi_diem, nguon{CONG|VNEID|THU_CONG}, ma_the, so_dinh_danh, ket_qua_ma, payload_json, hash, nguoi_thuc_hien)`; `luot_kcb(thoi_diem_xuat_trinh_the, trang_thai_the{DA_XAC_MINH|CHUA_XAC_MINH|LOI_CONG})`; `muc_huong_giai_doan(luot_kcb_id, tu_thoi_diem, den_thoi_diem, ty_le, can_cu)`.
- **Đánh đổi**: lưu payload Cổng là lưu dữ liệu cá nhân, cần thời hạn lưu và phân quyền (DLCN).

### BHYT-GD-P02 — Hàng đợi gửi Cổng (outbox) có SLA
- **Giải quyết**: R18, R19, R20, R21, R30, R34
- **Cách làm**: ghi outbox cùng transaction với "kết thúc lượt"; worker ký rồi gửi, retry backoff; `han_gui` tính theo chế độ hiện hành (07 ngày làm việc, trước ngày 05) hoặc chế độ dự thảo (03 giờ), có ngày chuyển chế độ; sự cố tự gia hạn.
- **Gợi ý dữ liệu**: `bhyt_outbox(id, luot_kcb_id, loai{CHECKIN|XML130|DANH_MUC|TONG_HOP_01BH|QUYET_TOAN_02BH|DIEU_CHINH_09BH}, phien_ban, xml_da_ky_blob, sha256, trang_thai{CHO_KY|DA_KY|DA_GUI|CONG_NHAN|LOI|CAN_SUA}, ma_giao_dich_cong, thoi_gian_tiep_nhan_cong, han_gui, che_do_han{TT48|DU_THAO_3H}, so_lan_thu, su_co_id)`, index `(trang_thai, han_gui)`; `su_co(id, nguon, bat_dau, ket_thuc, kenh_bao, nguoi_bao, bang_chung)`.
- **Đánh đổi**: ký tự động bằng chứng thư tổ chức nhanh nhưng phải quản lý khóa (HSM, phân quyền gọi ký).

### BHYT-GD-P03 — Bản ghi bất biến, điều chỉnh có lý do
- **Giải quyết**: R20, R23, R29, R34
- **Cách làm**: XML đã gửi không ghi đè; mỗi lần sửa `phien_ban + 1` với lý do và căn cứ; Mẫu 09/BH sinh từ diff giữa bản gốc và bản điều chỉnh, giữ XML1_ID/ID chi phí của Cổng.
- **Gợi ý dữ liệu**: `ho_so_phien_ban(ma_lk, phien_ban, ly_do, can_cu{phan_hoi_cong_id|van_ban_bhxh}, nguoi_sua, sha256)`.
- **Đánh đổi**: tốn lưu trữ; đổi lại có bằng chứng khi bị xuất toán. Mô hình snapshot chi tiết: BHYT-DATA-P05.

### BHYT-GD-P04 — Bộ quy tắc mức hưởng theo thời gian
- **Giải quyết**: R07, R09, R10, R35
- **Cách làm**: engine trả tỷ lệ kèm căn cứ (ví dụ "NĐ 188 Đ19 k2") để in cho người bệnh và audit.
- **Gợi ý dữ liệu**: `quy_tac_muc_huong(id, hieu_luc_tu, hieu_luc_den, cap_cmkt, tuyen_cu, diem_tu, diem_den, loai_kcb, dieu_kien{DUNG_TUYEN|CAP_CUU|LUU_TRU|TAM_TRU|BENH_HIEM|TU_DEN}, ty_le, can_cu_phap_ly)`; `cau_hinh_co_so(cap, diem_xep_cap, tuyen_truoc_2025, hieu_luc_tu)`.
- **Đánh đổi**: phức tạp hơn code cứng, nhưng mốc 01/07/2026 cho thấy luật đổi theo lộ trình.

### BHYT-GD-P05 — Tự giám định trước khi gửi
- **Giải quyết**: R23, R25, R28, R29, R17
- **Cách làm**: chạy 11 nhóm kiểm tra của TT 12 Đ10 k1 trước khi ký: thẻ, mức hưởng; danh mục đã chấp nhận tại ngày y lệnh; giá có hiệu lực; tỷ lệ, điều kiện; người chỉ định có CCHN, phạm vi, ca làm việc (02/DM); khoảng cách giữa các lần khám; tổng XML1 khớp chi tiết; số lượng thuốc, TBYT ≤ số mua sắm/điều chuyển. Lỗi nặng thì chặn ký.
- **Gợi ý dữ liệu**: `kiem_tra_truoc_gui(luot_kcb_id, ma_quy_tac, muc_do, thong_diep, thoi_diem)`.
- **Đánh đổi**: quy tắc BHXH chưa công khai đủ nên chỉ xấp xỉ; cập nhật khi BHXH công bố (NĐ 188 Đ71 k9 i).

### BHYT-GD-P06 — Danh mục hai trạng thái: nội bộ và Cổng
- **Giải quyết**: R28
- **Cách làm**: kê đơn/chỉ định BHYT chỉ lấy mục `AP_DUNG` có `ngay_ap_dung_cong ≤ ngay_y_lenh`; ngoại lệ thuốc cấp cứu theo ngày hóa đơn; job theo dõi hạn 05 ngày làm việc và 15 ngày gửi lại.
- **Gợi ý dữ liệu**: `danh_muc_item(..., trang_thai_noi_bo, trang_thai_cong{CHUA_GUI|CHO_DUYET|AP_DUNG|TU_CHOI}, ngay_ap_dung_cong, ly_do_tu_choi, han_gui_lai)`.
- **Đánh đổi**: chậm đưa dịch vụ mới vào dùng cho đến khi Cổng chấp nhận.

### BHYT-GD-P07 — Danh tính người hành nghề gắn chữ ký y lệnh
- **Giải quyết**: R16, R17
- **Cách làm**: đăng nhập cá nhân + MFA; y lệnh ký số cá nhân hoặc xác thực lại; `MA_BAC_SI` từ phiên đăng nhập; phát hiện một tài khoản trên ≥ 2 máy/IP đồng thời; báo cáo y lệnh ngoài ca.
- **Gợi ý dữ liệu**: `phien_dang_nhap(user_id, device, ip, bat_dau, ket_thuc)`; `y_lenh(nguoi_chi_dinh_id, phien_id, chu_ky_id)`.
- **Đánh đổi**: thao tác nhiều hơn ở buồng khám đông; dùng thẻ hoặc sinh trắc để đăng nhập nhanh.

### BHYT-GD-P08 — Lịch hạn nghĩa vụ BHYT
- **Giải quyết**: R20, R22–R27
- **Cách làm**: một bảng hạn chung cho: sửa lỗi Cổng 02 ngày làm việc; giải trình giám định 03 ngày làm việc; cung cấp HSBA 03 ngày làm việc; ký biên bản 02 ngày làm việc; rà soát cảnh báo 10 ngày; 01/BH ngày 15 hằng tháng; 02/BH ngày 15 đầu quý; kỳ cuối tháng trước ngày 05.
- **Gợi ý dữ liệu**: `nghia_vu_han(loai, doi_tuong_id, moc_bat_dau, han, don_vi{GIO|NGAY|NGAY_LAM_VIEC}, can_cu, trang_thai)`; lịch ngày làm việc cấu hình theo năm.
- **Đánh đổi**: phải duy trì lịch nghỉ lễ hằng năm.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| BHYT-GD-A01 | R01 | Tiếp đón 5 ca: chỉ CCCD gắn chip; chỉ VNeID; chỉ mã số; thẻ giấy; trẻ < 6 tuổi chỉ có giấy chứng sinh — ca nào bị chặn | Ảnh từng ca, cấu hình trường bắt buộc | BẮT BUỘC |
| BHYT-GD-A02 | R02 | Mỗi lượt có tra cứu lúc tiếp đón và trước ra viện; tỷ lệ lượt thiếu tra cứu | SQL, mẫu payload | BẮT BUỘC |
| BHYT-GD-A03 | R03 | Ngắt Cổng (test), tiếp đón ca BHYT: vẫn tiếp nhận, đánh dấu chưa xác minh, tra lại, lưu bằng chứng lỗi | Log, trạng thái lượt | BẮT BUỘC |
| BHYT-GD-A04 | R04 | Có trường bắt buộc scan thẻ/CCCD; có ghi nhận đồng ý; bảng giá có phí sao chụp | Cấu hình form, bảng giá | BẮT BUỘC |
| BHYT-GD-A05 | R05 | Ca sơ sinh chưa có thẻ: lấy/đề nghị mã thẻ tạm qua Cổng | Ảnh, XML có mã tạm | BẮT BUỘC |
| BHYT-GD-A06 | R06 | Xuất trình thẻ ngày 2 đợt nội trú (không cấp cứu): chi phí ngày 1 có vào BHYT không | Bảng kê, XML2/XML3 theo ngày | BẮT BUỘC |
| BHYT-GD-A07 | R07, R08 | Thẻ hết hạn giữa đợt: mức hưởng sau hạn + 15 ngày; đổi thẻ giữa đợt | XML1 `MUC_HUONG`, bảng kê | BẮT BUỘC |
| BHYT-GD-A08 | R09, R39 | Lũy kế gần ngưỡng: tự chuyển 100% khi vượt; giá trị lương cơ sở lấy từ bảng theo ngày (2.340.000 đến 30/06/2026, 2.530.000 từ 01/07/2026) | Cấu hình, bảng kê | BẮT BUỘC |
| BHYT-GD-A09 | R10 | Cấu hình cấp CMKT, điểm, cờ tuyến cũ; ca ngoại trú không đúng nơi đăng ký ở cơ sở thuộc NĐ 188 Đ19 k2–4 sau 01/07/2026 | Cấu hình, tỷ lệ, căn cứ in ra | BẮT BUỘC |
| BHYT-GD-A10 | R11 | Phiếu chuyển điện tử: ký số bác sĩ và cơ sở (sau 01/06/2026); hạn 10 ngày làm việc/01 năm đúng; còn chữ "đóng dấu" không | File phiếu đã ký | BẮT BUỘC |
| BHYT-GD-A11 | R12 | Dùng lại phiếu hẹn đã dùng; tạo phiếu hẹn thứ 2 cho đợt đã kết thúc — có bị chặn | Log, thông báo lỗi | BẮT BUỘC |
| BHYT-GD-A12 | R13 | Có Mẫu số 9; chi phí DVCLS chuyển đi vào hồ sơ cơ sở chuyển; báo cáo danh sách chuyển | Mẫu in, XML3/XML4 | BẮT BUỘC |
| BHYT-GD-A13 | R14 | Lộ trình liên thông CLS 01/01/2027 của vendor; kết quả CLS đủ định danh, thời điểm, người thực hiện, mã chuẩn | Tài liệu, mẫu dữ liệu | BẮT BUỘC? |
| BHYT-GD-A14 | R15 | Mẫu 8 trong hồ sơ HĐ còn khớp HIS đang chạy (tên, nhà cung cấp, thuê/mua) | Mẫu 8 đã nộp, HĐ | BẮT BUỘC |
| BHYT-GD-A15 | R16 | Thông tin xác thực Cổng lưu ở đâu; log có người dùng HIS cho mỗi lời gọi; quy trình đổi mật khẩu | Ảnh cấu hình (che bí mật), log | BẮT BUỘC? |
| BHYT-GD-A16 | R17 | Tài khoản dùng chung; đăng nhập 1 tài khoản trên 2 máy; `MA_BAC_SI` trùng người ký y lệnh | Danh sách user, log phiên, XML + audit | BẮT BUỘC |
| BHYT-GD-A17 | R18 | File đã gửi có `<CHUKYDONVI>` hợp lệ; cảnh báo chứng thư sắp hết hạn | File XML, kết quả verify | BẮT BUỘC |
| BHYT-GD-A18 | R19, R20 | Phân bố `thoi_gian_tiep_nhan_cong − thoi_diem_ket_thuc_luot`; tỷ lệ > 07 ngày làm việc; kỳ cuối tháng sau ngày 05; có gửi Cổng BYT | SQL, báo cáo gửi chậm trên Cổng | BẮT BUỘC |
| BHYT-GD-A19 | R21 | Nhật ký sự cố và bằng chứng đã thông báo BHXH | Bảng sự cố, email | BẮT BUỘC |
| BHYT-GD-A20 | R22 | 3 phản hồi lỗi gần nhất: sửa trong ≤ 02 ngày làm việc; có văn bản giải trình | Log phản hồi, bản sửa | BẮT BUỘC |
| BHYT-GD-A21 | R23 | Sinh Mẫu 09/BH ký số; lưu XML1_ID/ID chi phí của Cổng | File 09/BH, bảng mapping | BẮT BUỘC |
| BHYT-GD-A22 | R24 | Diễn tập 10 hồ sơ: thời gian xuất trọn HSBA + chứng từ; XML2/XML3 khớp y lệnh | Thời gian, biên bản đối chiếu | BẮT BUỘC |
| BHYT-GD-A23 | R25 | 01/BH tháng gần nhất khớp tổng XML1 đã gửi; ràng buộc cột; `MA_LOAI_KCB` theo QĐ 1804 sau 01/08/2026 | File 01/BH, SQL | BẮT BUỘC |
| BHYT-GD-A24 | R26 | Số quyết toán quý khớp hóa đơn BHYT; hóa đơn chênh lệch lập theo NĐ 254/2026 | Biên bản 06/BH, hóa đơn | BẮT BUỘC |
| BHYT-GD-A25 | R27 | Báo cáo chi bình quân theo khoa, bác sĩ | Báo cáo mẫu | NÊN |
| BHYT-GD-A26 | R28 | Kê thuốc/DVKT có trong danh mục nội bộ nhưng chưa được Cổng áp dụng: bị chặn/cảnh báo; danh mục gửi có ký số | Ảnh, file 01–06/DM | BẮT BUỘC |
| BHYT-GD-A27 | R29 | Sửa số lượng/giá trên bảng kê sau kết thúc lượt không qua y lệnh: có được không; có audit | Log, kết quả thử | BẮT BUỘC |
| BHYT-GD-A28 | R30 | Tỷ lệ lượt BHYT trong kỳ chưa có XML được Cổng tiếp nhận | SQL đối chiếu Cổng | BẮT BUỘC |
| BHYT-GD-A29 | R31 | Cơ chế loại hồ sơ bí mật nhà nước khỏi luồng thường; TLS | Cấu hình | BẮT BUỘC |
| BHYT-GD-A30 | R32, R33 | Chức năng báo thẻ nghi vấn; luồng ký xác nhận khi người bệnh bỏ về | Ảnh, log | BẮT BUỘC |
| BHYT-GD-A31 | R34 | p95 thời gian kết thúc lượt → Cổng tiếp nhận; ký có cần thao tác tay; hồ sơ có khóa sau đề nghị thanh toán | Thống kê, mô tả luồng ký | NÊN |
| BHYT-GD-A32 | R35 | Dịch vụ theo yêu cầu cho người có thẻ: phiếu thông báo trước có chữ ký; `T_BNTT` tách `T_BNCCT` | Phiếu, XML1 | BẮT BUỘC |
| BHYT-GD-A33 | R36 | Lượt khám 4 chuyên khoa ra tỷ lệ 100/30/30/30; khám lại trong ngày tính lần 2; bàn khám lượt 66 trở đi: tiền cùng chi trả của người bệnh không đổi | Bảng kê, XML3 | BẮT BUỘC |
| BHYT-GD-A34 | R37, R38, R39 | Lượt vào 28/06/2026, ra 03/07/2026, 2 DVKT dùng TBYT trước và sau 01/07: trần gói theo LCS của ngày kết thúc từng DVKT (× mức hưởng); chi phí thấp so với 15% LCS mới; lũy kế quy đổi theo NĐ 188 Đ18 k2 c; ở cơ sở 50% chi phí thấp vẫn nhân 50% | Bảng kê, cấu hình | BẮT BUỘC? |
| BHYT-GD-A35 | R40 | Thẻ QN/CA: không áp trần gói TBYT; chi phí ngoài phạm vi đủ điều kiện vào phần quỹ | Bảng kê, XML1 | BẮT BUỘC |
| BHYT-GD-A36 | R41 | Ca chuyển 3 khoa trong ngày; ca 3 giờ không tính giường; ca tử vong +1; ca chuyển viện sau mổ ngày 6 → nơi nhận tối đa 4 ngày giường ngoại | Bảng kê, XML3 | BẮT BUỘC |
| BHYT-GD-A37 | R42, R43, R44 | Ca mổ có phẫu thuật phát sinh cùng kíp 50%, thay kíp 80%; dòng vận chuyển không nhân mức hưởng; máu tính ngoài giá giường, vận chuyển ≤ 17.000 đ/đơn vị | Bảng kê | BẮT BUỘC |
| BHYT-GD-A38 | R45 | Kháng sinh (*) không có phiếu duyệt bị cảnh báo trước khi đưa vào hồ sơ thanh toán | Đơn thuốc, XML2 | BẮT BUỘC |
## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới |
|---|---|---|---|
| 01/03/2018 | TT 48 có HL: gửi ngay sau lượt, 07 ngày làm việc, 4 phương thức | Cơ sở, vendor | Đã qua |
| 01/01/2025 | Luật 51 (thủ tục KCB, chuyển người bệnh, mức hưởng theo cấp); TT 01/2025 | Cơ sở, vendor | Đã qua |
| 01/07/2025 | Luật 51 HL chung; nhiều điều NĐ 188 (Đ70 k2); NĐ 164 | Cơ sở, BHXH | Đã qua |
| 15/08/2025 | NĐ 188 HL toàn bộ (Đ37–38); NĐ 146/2018, 75/2023, 02/2025 hết HL | Cơ sở | Đã qua |
| 31/12/2025 | Hạn cuối dùng mẫu giấy hẹn, giấy chuyển tuyến cũ (TT 01 Đ15 k5 đ) | Cơ sở, vendor | Đã qua |
| 01/01/2026 | Chậm nhất ký số (xác thực) dữ liệu chi phí KCB BHYT (NĐ 188 Đ69 k9) | Cơ sở, vendor | Đã qua |
| 03/02/2026 | TT 09/2026/TT-BTC: thẻ BHYT điện tử, không đòi thẻ giấy (Đ6 k3) | Cơ sở | Đã qua |
| 10/02/2026 | TT 12/2026 có HL: Cổng, tài khoản, phản hồi 06/24/48 giờ, giám định | Cơ sở, BHXH | Đã qua |
| 01/04/2026 | Mẫu 01/BH, 05/BH, 06/BH, 09/BH; danh mục 01–06/DM | Cơ sở, vendor | Đã qua |
| 15/05/2026 | NĐ 90/2026 xử phạt (Đ84–95) | Cơ sở, người hành nghề | Đã qua |
| 01/06/2026 | Phiếu hẹn, phiếu chuyển điện tử ký số cơ sở thay dấu (TT 06/2026 Đ5 k2) | Cơ sở, vendor | Đã qua |
| 01/07/2026 | Mức hưởng ngoại trú 50% ở một số cơ sở (NĐ 188 Đ19 k2–4); NĐ 254/2026 thay NĐ 123/2020 | Cơ sở, vendor | Đã qua |
| 01/08/2026 | Mã loại hình, mã khoa QĐ 1804 (ảnh hưởng 01/BH, 07/BH) | Vendor | Đã qua |
| **07/10/2026** | Hết góp ý dự thảo thay TT 48 (03 giờ) | Vendor, cơ sở góp ý | Sắp tới (ngày mai) |
| Hằng tháng, ngày 15 | Gửi 01/BH tháng trước; BHXH cảnh báo gia tăng chi | Cơ sở | Định kỳ |
| Hằng quý, ngày 15 | Gửi 02/BH quý trước; BHXH thông báo kết quả trong 30 ngày (quý 4: 60 ngày) | Cơ sở | Định kỳ |
| **01/01/2027** | Liên thông, sử dụng kết quả CLS giữa cơ sở KCB BHYT (luật định); dự kiến văn bản thay TT 48 có HL (dự thảo) | Mọi cơ sở KCB BHYT, vendor | Sắp tới |

## 6. Bẫy trích dẫn và chuỗi thay thế

1. **NĐ 146/2018 (+75/2023, 02/2025) → NĐ 188/2025**: phần lớn hết HL 01/07/2025, toàn bộ 15/08/2025. TT 01/2025 Đ4 k2 a còn dẫn "Điều 15 NĐ 146/2018" → đọc sang NĐ 188 Đ37–38 (TT 01 Đ15 k4).
2. **TT 48/2017 vẫn còn hiệu lực**; đừng coi đã bị thay vì có dự thảo. Mốc "03 giờ" chỉ là dự thảo.
3. NĐ 188 **Đ69 là điều khoản chuyển tiếp**; điều về CNTT là Chương XI Đ66–68. Đ71 k2 d là nhiệm vụ của Bộ Tài chính ban hành biểu mẫu, trình tự giám định (đã thực hiện bằng TT 12/2026), không phải điều quy định "cổng".
4. Dự thảo TT BTC về Cổng đã thành TT 12/2026; không trích dự thảo riêng.
5. Thẩm quyền ban hành trình tự giám định đã sang Bộ Tài chính (TT 12). TT 12 không bãi bỏ quy trình cũ của BHXH VN; trạng thái các QĐ nội bộ cũ: chưa xác minh, không nên trích.
6. TT 01/2025 đọc riêng: mẫu phiếu ghi "đóng dấu"; từ 01/06/2026 bản điện tử dùng ký số cơ sở (TT 06/2026 Đ5 k2).
7. TT 12 tự dẫn văn bản đã chết: Đ14 k6 dẫn NĐ 123/2020, NĐ 70/2025 (hết HL 01/07/2026, thay bởi NĐ 254/2026); Mẫu 01/BH dẫn PL1 QĐ 824/2023 và Mẫu 07/BH dẫn PL6 QĐ 2010/2025 (bị QĐ 1804 bỏ từ 01/08/2026). Áp văn bản thay thế theo TT 12 Đ17 k3.
8. "6 lần khám trong 12 tháng" là chữ dự thảo; bản gốc TT 12 Đ4 k2 dẫn TT 48 Đ6 k2 a (06 tháng).
9. "Xác thực dữ liệu" ≠ xác thực sinh trắc người bệnh.
10. "Chuyển tuyến" → "chuyển cơ sở KCB" (Luật 51, TT 01); tên bảng XML vẫn "giấy chuyển tuyến".
11. NĐ 117/2020 → NĐ 90/2026 (15/05/2026). Mức phạt Chương II là mức cá nhân; tổ chức ×2 (Đ4 k5).
12. NĐ 166/2016 (căn cứ ban hành TT 48): NĐ 164/2025 Đ27 k3 chỉ ghi "không áp dụng" với BHXH bắt buộc, tự nguyện; phần BHYT còn áp dụng không: chưa xác minh.
13. Bản OCR NĐ 188 Đ35 k2 lặp ký hiệu "đ"; thứ tự đúng c (gửi, ký số, xác thực), d (hạ tầng, nâng cấp HIS), đ (rà soát chi tăng). Trích "Đ35 k2 d" cho nghĩa vụ nâng cấp HIS.
14. NĐ 90/2026 chỉ có bản OCR: trừ Đ95 k4 đã đối chiếu ảnh trang, các điều khác chỉ diễn giải.
15. **CV 1804/BHXH-QLT** (BHXH VN, 04/08/2025: số định danh thay mã số BHXH, mã đối tượng tham gia, mức hưởng %) **≠ QĐ 1804/QĐ-BYT** (BYT, 2026: loại hình KCB, mã khoa). Luôn ghi đủ ký hiệu cơ quan.
16. Ba hệ "mức hưởng" khác nhau: % theo PL I CV 1804; ký hiệu 1–5 in trên thẻ (QĐ 1351 sửa bởi 1697, mẫu QĐ 1666); `MUC_HUONG` trong XML (`BHYT-DATA-R11`). Đặc tả bắt "nhập mức hưởng 1–5 theo thẻ in" có căn cứ ở QĐ 1666, không phải CV 1804; mức áp dụng vẫn lấy theo Cổng.
17. API thông tin thẻ kèm QĐ 241/QĐ-BTC (05/02/2026) dành cho hệ thống giải quyết TTHC của bộ, tỉnh, không phải API tra thẻ của Cổng giám định (CV 497/BHXH-CNTT).
18. Trang `baohiemxahoi.gov.vn` không chết: lỗi "từ chối truy cập" là do server dùng TLS renegotiation cũ (curl/OpenSSL 3 cần bật `UnsafeLegacyRenegotiation`). `check_links.py` có thể báo chết giả.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

1. **Toàn văn dự thảo thay TT 48**: chưa thấy trên cổng BYT hoặc chinhphu.vn. Cần: danh sách trường hợp được gửi chậm; định nghĩa "kết thúc lượt" với nội trú; cơ chế khóa sau 15 ngày; có kiểm thử/công nhận phần mềm không; còn gửi song song Cổng BYT không — hỏi BYT (Vụ BHYT).
2. **Căn cứ xử phạt chậm gửi theo dự thảo**: NĐ 90 không có hành vi chậm gửi XML; Đ111 chỉ cho Giám đốc BHXH xử phạt vi phạm đóng BHYT và Đ83–86 → dự thảo nói "BHXH xử phạt" cần căn cứ mới. Chậm gửi hiện có bị quy vào Đ95 k4 b được không — luật sư.
3. **Thủ tục "xác thực" kết nối HIS** (NĐ 188 Đ22 k2, Đ68 k5 b): không thấy thủ tục chứng nhận/kiểm thử phần mềm; "quy định của Bộ trưởng BYT" về tiêu chuẩn kết nối là văn bản nào (TT 48? QĐ 130?); BHXH có sandbox chính thức không — hỏi BHXH VN (Trung tâm CNTT) và BYT.
4. Số, ngày Công văn BHXH-CNTT kèm Phụ lục 01 hướng dẫn liên thông QĐ 3176; XSD `CHUKYDONVI` nằm ở mục Trợ giúp của Cổng (cần tài khoản).
5. Cổng tiếp nhận dữ liệu y tế của BYT (TT 48 Đ7 k1 c; NĐ 188 Đ71 k1 c): còn vận hành, còn bắt buộc gửi song song không; quan hệ với HTTT quản lý KCB của TT 38/2024 (HTTT-BC).
6. Bản ký của QĐ 2555/QĐ-BYT (có số, ngày) chưa tìm thấy; nội dung đã đối chiếu bản BYT không số (2026-10-27). TT 09/2026/TT-BTC đã đọc bản sao y.
7. **Liên thông CLS 01/01/2027**: Luật 51 Đ3 k4 giao Chính phủ quy định, NĐ 188 không có; dự thảo hiện có là thông tư BYT. Nếu đến hạn chưa có văn bản chi tiết thì áp dụng thế nào — luật sư (phối hợp CLS).
8. Phần BHYT của NĐ 166/2016 còn hiệu lực không (bẫy 12).
9. Mẫu 02/BH không nằm trong danh sách áp dụng từ 01/04/2026 (TT 12 Đ17 k1) nhưng Đ17 k2 cho dùng mẫu cũ hết quyết toán quý I/2026 → suy ra áp dụng từ quyết toán quý II/2026 (suy luận).
10. Bản TT 48 trên datafiles/Công báo chưa tìm thấy; đang dùng bản ký số do SYT Hà Tĩnh và TTYT Ninh Sơn đăng lại.
11. QĐ 1351/QĐ-BHXH: chưa mở bản gốc (nhất là Đ2, ký hiệu mức hưởng 5); QĐ 1351, 1697 còn hiệu lực sau NĐ 188 và CV 1804 không. Mã kết quả 052, 053 (ký tự thứ 3, thứ 4–5) giả định mã thẻ 15 ký tự: khi tra bằng mã số 10 số hoặc số định danh có còn trả không — hỏi BHXH VN (Trung tâm CNTT).
