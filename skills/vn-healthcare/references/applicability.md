# Áp dụng: loại phần mềm / cơ sở → domain cần đọc

> Kiểm tra lần cuối: 2026-10-06

Ký hiệu: **●** đọc chính (gần như chắc chắn áp dụng) · **○** đọc nếu phần mềm có tính năng tương ứng · trống = thường không liên quan.

## Ma trận

| Loại phần mềm | EMR | BHYT-DATA | BHYT-GD | DUOC | DLCN | ANM | SKDT | GIAYTO | HTTT-BC | MA-LT | CLS | TELE | CHUYENKHOA | TC-MS | BAOMAT-CB |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HIS bệnh viện (công/tư) | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ○ | ○ | ● | ● |
| EMR (phân hệ/sản phẩm riêng) | ● | ○ | ○ | ○ | ● | ● | ○ | ● | ○ | ● | ○ | | ○ | | ● |
| CIS / phần mềm phòng khám | ● | ○ | ○ | ● | ● | ● | ● | ○ | ● | ● | ○ | ○ | ● | ● | ○ |
| LIS (xét nghiệm) | ○ | ○ | | | ● | ● | | | ○ | ● | ● | ○ | | | ● |
| RIS / PACS | ○ | ○ | | | ● | ● | | | | ○ | ● | ○ | | ○ | ● |
| Nhà thuốc / chuỗi nhà thuốc | | | | ● | ● | ○ | | | | | | ○ | ○ | ● | ○ |
| Khám từ xa / app người bệnh | ● | ○ | ○ | ● | ● | ● | ○ | ○ | | ○ | | ● | ● | ○ | ○ |
| Thành phần AI (CDSS, đọc ảnh, chatbot) | | | | | ● | ● | | | | | ● | ● | | | ○ |

Cột BHYT-DATA/BHYT-GD với CIS phòng khám: **●** nếu phòng khám có hợp đồng khám chữa bệnh BHYT.

## Ghi chú theo đối tượng

**Bệnh viện công**: thêm TC-MS phần thuê/mua sắm dịch vụ CNTT bằng ngân sách (NĐ 224/2026), WCAG cho cổng/app (CHUYENKHOA), và các kế hoạch Bộ Y tế giao chỉ tiêu (timeline).

**Bệnh viện tư, phòng khám**: nghĩa vụ dữ liệu và liên thông gần như giống bệnh viện công (Sổ SKĐT, đơn thuốc quốc gia, TT 38/2024 từ 01/01/2027). Phòng khám chỉ khám và kê đơn vẫn nên coi là thuộc diện bệnh án điện tử từ 31/12/2026 (EMR, mức `BẮT BUỘC?`).

**Nhà thuốc**: phần mềm là điều kiện đạt GPP; liên thông CSDL dược; hóa đơn từ máy tính tiền (TC-MS).

**Vendor phần mềm (mọi loại)** — luôn đọc thêm:
- DLCN: vendor SaaS vận hành hệ thống xử lý dữ liệu sức khỏe thay cơ sở KCB thuộc diện phải có Giấy chứng nhận đủ điều kiện kinh doanh dịch vụ xử lý dữ liệu cá nhân (`DLCN-R22`); thỏa thuận xử lý dữ liệu với từng cơ sở; cấm tự chia dữ liệu cho bảo hiểm thương mại (`DLCN-R09`).
- ANM: lưu trữ dữ liệu tại Việt Nam, tách lô-gic khi chạy cloud cho hệ thống cấp 3.
- TC-MS: không giữ tiền / thu hộ khi không có giấy phép trung gian thanh toán; nghĩa vụ bàn giao và xóa dữ liệu khi hết hợp đồng thuê.
- CLS: kiểm tra phần mềm có rơi vào định nghĩa thiết bị y tế không trước khi bán.

## Câu hỏi nhanh để chọn domain

- Có ghi nhận thông tin khám/chữa bệnh của người bệnh không? → EMR, MA-LT, DLCN, ANM.
- Có thanh toán BHYT không? → BHYT-DATA, BHYT-GD.
- Có kê đơn hoặc bán thuốc không? → DUOC.
- Có cấp giấy tờ (ra viện, chứng sinh, báo tử, nghỉ BHXH, khám sức khỏe) không? → GIAYTO.
- Có định danh người bệnh bằng CCCD/VNeID, đẩy dữ liệu lên Sổ SKĐT không? → SKDT.
- Có xét nghiệm, chẩn đoán hình ảnh, kết quả cận lâm sàng không? → CLS.
- Có tương tác trực tuyến với người bệnh, app, quảng cáo, AI không? → TELE, CHUYENKHOA.
- Có thu tiền, xuất hóa đơn, bảng giá không? → TC-MS.
- Có HIV, sản khoa/siêu âm thai, IVF, ghép tạng, tâm thần, methadone không? → BAOMAT-CB.
- Cơ sở có phải báo cáo lên hệ thống của Bộ (thống kê, truyền nhiễm, sự cố, người hành nghề) không? → HTTT-BC.
