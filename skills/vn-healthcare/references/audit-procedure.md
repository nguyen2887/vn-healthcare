# Quy trình audit phần mềm y tế theo pháp luật Việt Nam

> Kiểm tra lần cuối: 2026-10-06

Mục tiêu audit: chỉ ra phần mềm đang **thiếu gì so với nghĩa vụ pháp lý**, có bằng chứng, xếp theo mức độ và hạn chót — đủ để đội phát triển lập kế hoạch sửa, và đủ để cơ sở KCB/vendor trả lời khi bị kiểm tra.

## 1. Phạm vi

Ghi rõ trước khi bắt đầu:
- Sản phẩm, phiên bản, môi trường được audit (production / staging / mã nguồn).
- Đối tượng sử dụng (BV công/tư, phòng khám, nhà thuốc) và mô hình triển khai (SaaS / tại chỗ).
- Domain áp dụng (theo `applicability.md`) và domain loại trừ kèm lý do.
- Ngày audit và ngày "Kiểm tra lần cuối" của skill. Nếu cách nhau > 90 ngày, xác minh lại trạng thái các văn bản then chốt trước.

## 2. Thu bằng chứng

Với mỗi mục checklist `<CODE>-Ann`, ưu tiên bằng chứng khách quan theo thứ tự:
1. **Mã nguồn / schema CSDL / migration**: có trường, ràng buộc, bảng lịch sử, trigger chống sửa đè…
2. **Cấu hình và log**: log gửi dữ liệu lên cổng, log truy cập, chính sách lưu trữ, cấu hình ký số.
3. **Thao tác trên UI**: thử luồng thật (sửa bệnh án đã ký, kê đơn N, gửi XML lỗi…).
4. **Tài liệu, hợp đồng, quy chế**: DPA với cơ sở, quy chế bệnh án điện tử, hồ sơ cấp độ, giấy chứng nhận.
5. Phỏng vấn người vận hành — chỉ là bằng chứng phụ.

Khi có quyền truy cập codebase: grep/đọc code để kiểm chứng, trích file:dòng làm bằng chứng. Không suy đoán "chắc là có".

**Đọc luồng nghiệp vụ, không chỉ dò checklist.** Nhiều nghĩa vụ pháp lý (bệnh án không sửa đè, đơn đã gửi không sửa, truy vết ai làm gì, chỉ người có thẩm quyền mới kê/ký) chỉ đúng khi logic code đúng — có bảng `versions` hay cột `signed` chưa đủ. Với codebase thật, kiểm thêm:
- **Chuyển trạng thái** của hồ sơ, đơn thuốc, phiếu chỉ định, kết quả: có chặn thao tác trên trạng thái sai không (cấp phát đơn nháp/đã hủy, "hồi sinh" bản ghi đã hủy, sửa sau khi hoàn tất/khóa qua API phụ)?
- **Danh tính người thực hiện** (người kê, ký, duyệt, đọc kết quả, thời điểm ký) lấy từ phiên đăng nhập phía server hay từ dữ liệu client gửi lên? Hash/chữ ký do client tự cung cấp có được kiểm lại không?
- **Phân quyền endpoint nhạy cảm**: xác nhận đã gửi cổng BHYT/đơn thuốc, ký, khóa/mở khóa hồ sơ, xuất dữ liệu.
- **Xóa dây chuyền** (CASCADE) có làm mất lịch sử phiên bản hoặc nhật ký không.
- **Cấu hình môi trường**: mock/fake (lưu trữ, ký số, cổng) có thể chạy ở production không; giá trị cứng thay cho biến môi trường.

Chỉ ghi "điểm làm tốt" khi đã xác minh bằng code; một khẳng định an toàn sai còn nguy hiểm hơn bỏ sót. **Lần theo tới chỗ thực thi** trước khi kết luận một cơ chế đang hoạt động: hàm kiểm tra có thực sự được gọi ở luồng đó không; cấu hình hiệu lực là giá trị được truyền khi module khởi tạo (DI/factory), không phải tên biến hay file cấu hình mẫu; lifecycle hook có chạy với scope đó không. Không suy ra từ tên hàm, comment hay tài liệu.

**Codebase lớn — audit nhiều lượt rồi gộp.** Một lượt đọc không phủ hết một repo vài trăm/nghìn file; mỗi lần chạy sẽ soi một góc khác nhau. Hãy chia ít nhất 3 lượt, mỗi lượt một trọng tâm, rồi gộp và khử trùng:
1. **Pháp lý**: đối chiếu checklist các domain áp dụng (lưu trữ, ký số, liên thông, dữ liệu cá nhân, mã hóa, giấy tờ).
2. **Luồng nghiệp vụ**: trạng thái, danh tính người thực hiện, khóa sau hoàn tất, xóa dây chuyền (mục trên).
3. **Bảo mật & vận hành**: xác thực/phân quyền mọi endpoint đọc-ghi dữ liệu người bệnh, cách ly giữa cơ sở (tenant), lộ dữ liệu qua log/lỗi/API, cấu hình môi trường và triển khai (mock ở production, container, cổng mở, lưu trữ ở nước ngoài).

Nếu môi trường cho phép chạy subagent song song, giao mỗi lượt cho một subagent (kèm danh sách module/thư mục cần đọc) rồi tự gộp; nếu không, làm tuần tự. Ghi rõ trong "Phạm vi" phần nào của repo đã đọc và phần nào chưa.

## 3. Chấm điểm

| Kết quả | Khi nào |
|---|---|
| Đạt | Có bằng chứng đáp ứng đủ yêu cầu |
| Một phần | Đáp ứng một phần (vd có log nhưng không chống sửa) |
| Không đạt | Có bằng chứng là thiếu hoặc làm sai |
| Không áp dụng | Yêu cầu không áp cho đối tượng/tính năng này (ghi lý do) |
| Chưa đủ bằng chứng | Không truy cập được để kiểm |

Mức nghiêm trọng của một lỗi — chấm chặt để thứ tự ưu tiên còn ý nghĩa:
- **Nghiêm trọng**: `BẮT BUỘC` đã quá hạn **và** (có chế tài/xử phạt, hoặc chặn cấp phép/thanh toán BHYT, hoặc làm lộ dữ liệu nhạy cảm/ảnh hưởng an toàn người bệnh).
- **Cao**: `BẮT BUỘC` đã quá hạn nhưng không thuộc trường hợp trên, hoặc có hạn trong 6 tháng tới.
- **Trung bình**: `BẮT BUỘC` hạn xa hơn, hoặc `BẮT BUỘC?` có rủi ro lớn.
- **Thấp**: `NÊN`, hoặc `BẮT BUỘC?` rủi ro nhỏ.

Nếu có hơn ~7 lỗi Nghiêm trọng, rà lại: nhiều khả năng đang chấm quá tay; gộp các lỗi cùng gốc (vd nhiều trường thiếu cùng do không có cơ chế phiên bản) thành một lỗi.

## 4. Báo cáo — gọn, hành động được

Người đọc báo cáo là đội phát triển và chủ cơ sở/vendor, không phải người viết skill. Báo cáo phải đọc trong 10–15 phút và biết ngay phải sửa gì trước. Vì vậy:

- **Thân báo cáo chỉ gồm lỗi thật** (Không đạt, Một phần), gộp theo gốc rễ, sắp theo mức × hạn. Mỗi lỗi: hiện trạng + bằng chứng (file:dòng, bảng/cột, cấu hình), căn cứ (số hiệu + điều/khoản + **link**), mức, hạn, đề xuất sửa cụ thể.
- **"Chưa đủ bằng chứng" không liệt kê từng mục**: gom thành danh sách **câu hỏi gửi khách** (≤ 15 câu, nhóm theo chủ đề), mỗi câu nói rõ cần tài liệu/bằng chứng gì.
- **Đạt / Không áp dụng** chỉ báo số lượng ở tóm tắt.
- Viết bằng ngôn ngữ của người đọc. Mã ID nội bộ của skill (`EMR-R10`, `DLCN-A04`…) chỉ xuất hiện ở dòng "Tham chiếu skill" cuối mỗi lỗi và ở phụ lục — không dùng trong tiêu đề, câu văn hay bảng tóm tắt, vì khách không biết skill và sẽ thấy đó là nhiễu. Tương tự, không nêu "đã kiểm N mục checklist"; chỉ báo kết quả (số lỗi theo mức).
- Chỉ xuất bảng checklist đầy đủ (mọi mục, kể cả Đạt) khi người dùng yêu cầu "bản đầy đủ".
- Gọn là **gộp**, không phải **bỏ**: mọi lỗi có bằng chứng đều phải còn trong báo cáo (lỗi mức Thấp/Trung bình có thể gom vào bảng ngắn). Chỉ "Chưa đủ bằng chứng" mới được chuyển thành câu hỏi.
- Những điểm xuyên suốt dễ bị rơi khi rút gọn — luôn có trong báo cáo (thành lỗi hoặc thành câu hỏi gửi khách):
  - Tách dữ liệu giữa các khách hàng/cơ sở trong hệ thống multi-tenant (ràng buộc unique, truy vấn, phân quyền có lọc theo cơ sở không).
  - Quy trình phát hiện và báo vi phạm dữ liệu / sự cố an ninh mạng trong hạn luật định.
  - Đồng ý xử lý dữ liệu của trẻ em và người đại diện.
  - Người bệnh không có CCCD/số định danh (trẻ em, người nước ngoài, vô danh) và tiếp đón bằng thẻ BHYT.
  - Vai trò pháp lý của vendor (thỏa thuận xử lý dữ liệu, giấy chứng nhận) khi phần mềm do bên thứ ba vận hành.

```
# Báo cáo audit tuân thủ — <sản phẩm> <phiên bản>
Ngày audit: … · Skill vn-healthcare kiểm tra lần cuối: <ngày> · Phạm vi: …

## Tóm tắt điều hành
- Kết quả: Không đạt x · Một phần y · Đạt z · Không áp dụng w · Chưa đủ bằng chứng v
- 3–5 việc phải làm ngay (1 dòng mỗi việc, kèm hạn và căn cứ)

## Lỗi cần sửa (theo mức nghiêm trọng)
### [Nghiêm trọng] <tên lỗi bằng lời thường>
- Hiện trạng & bằng chứng: …
- Căn cứ: <số hiệu> Đ.. k.. — [link] · Mức: BẮT BUỘC / BẮT BUỘC? · Hạn: …
- Đề xuất sửa: … (pattern tham khảo)
- Tham chiếu skill: <ID>
(… các mức tiếp theo, có thể dùng bảng cho mức Trung bình/Thấp)

## Câu hỏi cần khách cung cấp bằng chứng
## Chưa rõ về pháp lý (BẮT BUỘC?, suy luận, dự thảo) — nên hỏi ai
## Phạm vi không bao gồm
## Phụ lục: văn bản đã dùng (số hiệu, trạng thái, link)
```

## 5. Lưu ý

- Không tính `BẮT BUỘC?` là "Không đạt" chắc chắn; báo như rủi ro kèm lý do chưa rõ.
- Với mục phụ thuộc dự thảo, ghi "chuẩn bị" thay vì "vi phạm".
- Nêu rõ những gì audit **không** bao gồm (vd không kiểm thử xâm nhập, không đánh giá chất lượng lâm sàng).
