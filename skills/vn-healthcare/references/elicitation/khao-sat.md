# Quy trình khảo sát nghiệp vụ

> Kiểm tra lần cuối: 2026-10-27 · Phạm vi: ngoại trú (phòng khám, khoa khám bệnh) · Dùng cùng `questions-by-role.md`, `../business/variation-points.md`, `../business/flows/*.md`, mẫu đầu ra trong `../deliverables/templates.md`

Agent **không có mặt tại cơ sở**. Agent làm ba việc: chuẩn bị trước khảo sát, hướng dẫn người đi khảo sát ghi chú sao cho dùng được, và tổng hợp sau khảo sát. Mọi thứ ở giữa là của con người.

Nguyên tắc xuyên suốt: **ghi chú không nói thì là "chưa xác nhận"**. Không điền chỗ trống bằng thông lệ rồi viết như khách đã nói. Thông lệ chỉ được dùng làm mặc định khi có nhãn `[THÔNG LỆ]` và nằm trong bảng giả định chờ khách xác nhận.

## A. Chuẩn bị (agent làm, trước khi đi)

### A1. Xác định loại cơ sở
Hỏi người dùng (hoặc lấy từ thông tin đã có) đúng 6 thứ:
1. Loại: phòng khám đa khoa / chuyên khoa (ghi chuyên khoa) / khoa khám bệnh BV / chuỗi (số chi nhánh).
2. Có hợp đồng BHYT không; cấp CMKT và điểm nếu biết.
3. Có CLS tại chỗ không (xét nghiệm, CĐHA); có quầy thuốc không.
4. Có điều trị ban ngày / theo đợt (PHCN, YHCT, liệu trình) không.
5. Phần mềm đang dùng (tên, từ năm nào) và lý do thay/sửa.
6. Mục tiêu dự án theo lời chủ: tuân thủ / giảm xuất toán / tăng lượt / mở rộng.

Không có câu trả lời → ghi giả định, đánh dấu để hỏi trong giờ đầu tiên.

### A2. Lọc điểm biến thiên và chọn domain luật
- Mở `applicability.md` → danh sách domain áp dụng.
- Mở `variation-points.md` → giữ các dòng có cột "Loại cơ sở" khớp. Kết quả là **bảng VP của dự án**, mỗi dòng trạng thái ban đầu `chưa hỏi`.
- Các dòng `[LUẬT]` không cần hỏi "có làm không" mà hỏi "đang làm bằng gì" để tìm lệch.

### A3. Chọn vai cần gặp và thời lượng

| Thời lượng có | Gặp ai | Đầu ra tối thiểu |
|---|---|---|
| 1 buổi (2–3 giờ) | Chủ/quản lý + 1 người vận hành chính (thường thu ngân kiêm tiếp đón ở PK nhỏ). Dùng 15 câu "giờ đầu tiên" | Loại cơ sở chốt, luồng chính 1 ca BHYT + 1 ca dịch vụ, danh sách người gặp tiếp, tài liệu xin |
| 1 ngày | Thêm: 1 bác sĩ đông bệnh, 1 điều dưỡng, thu ngân, người làm BHYT; đi theo 2–3 người bệnh thật từ cổng đến ra về | As-is đủ các bước B0–B9, bảng VP điền ≥ 60%, ảnh mẫu in |
| 3 ngày | Thêm: CLS, dược, IT, ca chiều/tối, chi nhánh thứ hai; ngồi quan sát giờ cao điểm; xem màn hình phần mềm cũ | As-is có số liệu (lượt/giờ, thời gian chờ), bảng VP ≥ 90%, danh mục và bảng giá thật, danh sách lệch luật đã kiểm bằng giấy tờ |

Khoa khám bệnh BV: nhân đôi thời gian vì nhiều phòng, nhiều điểm thu, có phòng giấy tờ riêng.

### A4. Tài liệu xin trước (gửi khách trước ngày khảo sát)
- Bảng giá mọi loại đang áp dụng (BHYT, dịch vụ, theo yêu cầu, gói) kèm ngày hiệu lực. (VP-VP-01)
- Danh mục dịch vụ kỹ thuật được duyệt; danh mục thuốc, vật tư; kết quả thầu nếu BHYT. (VP-DM-01, VP-DM-02)
- Danh sách bác sĩ kèm số giấy phép hành nghề, phạm vi, cơ hữu/thỉnh giảng. (VP-DM-04)
- Mọi mẫu đang in: phiếu khám, phiếu chỉ định, phiếu kết quả, đơn thuốc, phiếu thu, bảng kê, giấy hẹn, giấy nghỉ, giấy chuyển. (VP-GT-06)
- Sơ đồ phòng, ca làm việc. (VP-DM-03)
- Báo cáo gửi Sở/BHXH kỳ gần nhất; biên bản giám định gần nhất. (VP-DM-07)
- Giấy phép hoạt động, hợp đồng BHYT, quy chế bệnh án điện tử nếu có. (`EMR-R25`)
- Sơ đồ hệ thống, danh sách tài khoản theo vai.

Khách không gửi được ≥ 3 mục đầu → báo người dùng: khảo sát sẽ ra nhiều "chưa xác nhận", nên dời hoặc chấp nhận.

### A5. Soạn gói phỏng vấn
Với mỗi vai sẽ gặp: lấy bộ câu trong `questions-by-role.md`, bỏ câu không áp dụng (vd không có quầy thuốc thì bỏ vai 5), thêm câu từ bảng VP của dự án chưa có vai nào hỏi. Mỗi gói ≤ 20 câu, câu bẫy 🪤 giữ nguyên, câu 📎 gom cuối.

## B. Trong khảo sát — hướng dẫn cho người đi

Agent không đi được, nên ghi chú phải đủ để agent tái dựng. Đưa người đi khảo sát 6 quy tắc này:

1. **Ghi theo bước luồng, không ghi theo thứ tự nói.** Dùng tên bước B0–B9 của `flows/ngoai-tru.md` (hoặc bước của luồng con) làm tiêu đề. Người ta kể lộn xộn; mình xếp lại tại chỗ.
2. **Với mỗi bước ghi 5 thứ**: ai làm · trên công cụ gì (phần mềm nào, sổ, Excel, giấy) · dữ liệu vào/ra · mất bao lâu, bao nhiêu lần/ngày · họ than gì.
3. **Chép nguyên văn** câu nói quan trọng, trong ngoặc kép, kèm vai người nói. Đặc biệt câu trả lời cho câu bẫy 🪤 và câu "khi nào thì không làm vậy". Đừng diễn giải tại chỗ.
4. **Chụp ảnh**: mọi mẫu in (che tên người bệnh), màn hình phần mềm ở từng bước, sổ tay, bảng giá dán tường, thông báo dán quầy. Đặt tên ảnh theo bước.
5. **Đếm**: lượt/ngày theo loại, số phòng hoạt động theo ca, thời gian chờ ở giờ cao điểm, số hồ sơ Cổng lỗi tháng trước, số lần hoàn tiền tuần trước.
6. **Đánh dấu ngay**: `?` = chưa hỏi được · `!` = nghe có vẻ lệch luật (chỉ đánh dấu, không kết luận tại chỗ) · `≠` = hai người nói khác nhau.

Định dạng ghi chú gợi ý (text thuần là đủ):

```
## B1 Tiếp đón — nguồn: lễ tân A (ca sáng), 27/10
- Ai/công cụ: lễ tân, phần mềm X màn "Tiếp nhận" + sổ tay
- Vào/ra: CCCD hoặc đọc tên+SĐT → hồ sơ, phiếu khám in
- Số: ~120 lượt/ngày, 70% BHYT, chờ 15–30' lúc 8–9h
- Nguyên văn: "bệnh cũ thì em gõ số điện thoại, nhanh hơn" (A)  !
- Nguyên văn: "trưa chị B ngồi thay, dùng máy em luôn" (A)  !
- ? chưa hỏi: gộp hồ sơ trùng ai làm
- Ảnh: B1-phieu-kham.jpg, B1-man-hinh.jpg
```

## C. Sau khảo sát — agent tổng hợp

Đầu vào: ghi chú/transcript/ảnh do người dùng dán. Đầu ra: theo mẫu trong `../deliverables/templates.md`. Thứ tự làm:

### C1. Dựng luồng as-is
- Đi theo B0–B9 của luồng tham chiếu. Với mỗi bước: có ghi chú → điền bước, vai, công cụ, dữ liệu, số, đau. Không có ghi chú → bước ghi **"chưa khảo sát"**, không điền bằng luồng tham chiếu.
- Bước khách có mà luồng tham chiếu không có (vd "duyệt giảm giá của quản lý") → thêm bước, đánh dấu *bước riêng của khách*.
- Mỗi bước có ghi nguồn (vai, ngày). Hai nguồn mâu thuẫn (`≠`) → ghi cả hai, đưa vào câu hỏi xác nhận.
- Vẽ mermaid as-is; nhánh phụ (bỏ về, Cổng lỗi, hoàn tiền) chỉ vẽ nếu ghi chú có.

### C2. Điền bảng VP của dự án
Mỗi dòng VP một trong bốn trạng thái:
- **Đã trả lời** — có câu trả lời, ghi nguồn và nguyên văn nếu có.
- **Mâu thuẫn** — hai nguồn khác nhau.
- **Chưa xác nhận** — không có trong ghi chú. Nếu lớp `[THÔNG LỆ]` thì điền mặc định thông lệ vào cột "giả định", vẫn là chưa xác nhận.
- **Không áp dụng** — ghi lý do (vd không có quầy thuốc).

Dòng `[LUẬT]` mà câu trả lời cho thấy khách làm khác → sang C4.

### C3. Bảng giả định và câu hỏi còn thiếu
- Mỗi VP chưa xác nhận → một dòng giả định: giả định gì, lớp, hệ quả nếu sai, ai trả lời được.
- Gom câu hỏi còn thiếu **theo vai** để lần gặp sau hỏi một lượt. ≤ 15 câu mỗi vai; nhiều hơn thì khảo sát chưa đủ, báo người dùng.

### C4. Lệch luật phát hiện sớm
- Chỉ ghi khi (a) có nguyên văn hoặc ảnh làm bằng chứng và (b) có ID trong `references/domains/`. Thiếu một trong hai → để ở "cần kiểm", không phải lỗi.
- Mỗi dòng: hiện trạng (nguyên văn/ảnh), căn cứ (ID, số hiệu, điều khoản, link lấy từ file domain), mức theo domain, hệ quả thực tế (xuất toán, phạt, chặn cấp phép), hướng sửa (đổi quy trình / cấu hình / tính năng).
- Mức `BẮT BUỘC?` ghi là rủi ro, không phải vi phạm.
- Đây là bản sơ bộ; bản đầy đủ làm ở gap analysis sau khi có phần mềm hiện có để đối chiếu.

### C5. Viết báo cáo khảo sát
Theo mẫu (1) trong `templates.md`. Tóm tắt điều hành **không được chắc hơn** phần chi tiết: VP chưa xác nhận thì tóm tắt cũng ghi chưa xác nhận; lệch luật mức `BẮT BUỘC?` thì tóm tắt ghi rủi ro.

## D. Vòng xác nhận với khách

1. Gửi khách: luồng as-is (mermaid + bảng) và bảng giả định. Không gửi danh sách lệch luật ở vòng này nếu chưa có buổi giải thích; gửi lạnh dễ bị phản ứng.
2. Yêu cầu khách đánh dấu từng bước: đúng / sai (sửa thành gì) / thiếu. Từng giả định: đúng / sai / không biết (ai biết).
3. Cập nhật as-is và bảng VP; giả định được xác nhận chuyển thành "đã trả lời, nguồn: xác nhận của <ai> ngày <ngày>".
4. Buổi trình bày lệch luật: đi từng mục với căn cứ và link, hỏi khách có lý do nào mình chưa biết (có khi họ có văn bản của Sở). Ghi phản hồi.
5. Chốt phiên bản as-is có chữ ký/duyệt của người được chủ ủy quyền (xem câu 6 vai chủ cơ sở). Từ đây mới sang to-be và gap analysis.

## Checklist: đủ điều kiện kết thúc khảo sát

- [ ] 6 câu loại cơ sở (A1) đều có câu trả lời từ khách, không phải giả định.
- [ ] Luồng as-is có đủ B1, B4, B8 và nhánh thu tiền; mỗi bước có nguồn.
- [ ] Đã đi theo ít nhất 1 ca BHYT và 1 ca dịch vụ thật (nếu cơ sở có BHYT).
- [ ] Bảng VP: ≥ 80% dòng áp dụng ở trạng thái đã trả lời hoặc không áp dụng; **mọi dòng `[LUẬT]`** có trạng thái khác "chưa hỏi".
- [ ] Có ảnh/bản của: bảng giá, danh mục dịch vụ, mẫu phiếu khám, mẫu đơn thuốc, mẫu phiếu thu/hóa đơn, bảng kê BHYT (nếu có BHYT).
- [ ] Đã gặp ít nhất: 1 bác sĩ, 1 người tiếp đón/thu ngân, 1 người làm BHYT (nếu có BHYT), chủ/người có quyền chốt.
- [ ] Mọi `≠` đã có kế hoạch xác nhận; mọi `!` đã được phân thành lệch luật có ID hoặc "cần kiểm".
- [ ] Khách đã xác nhận as-is (vòng D) hoặc có ngày hẹn xác nhận.
- [ ] Danh sách câu hỏi còn thiếu ≤ 15 câu mỗi vai.

Thiếu mục nào → ghi rõ trong báo cáo khảo sát phần "Phạm vi chưa khảo sát", không bù bằng suy đoán.
