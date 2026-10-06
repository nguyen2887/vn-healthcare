# Brief biên tập: research → references của skill `vn-healthcare`

Mốc tham chiếu: **2026-10-06**. Skill nằm tại `skills/vn-healthcare/`. Bạn chuyển file research `research/deep/<CODE>.md` thành `skills/vn-healthcare/references/domains/<code-viết-thường>.md`.

Người đọc file đích là **một agent AI đang giúp dev thiết kế hoặc audit phần mềm y tế**. Nó sẽ mở đúng file domain khi cần, nên file phải: chính xác, gọn, tra cứu nhanh theo ID, không kể lể quá trình research.

## Đầu vào bắt buộc đọc

1. `research/deep/<CODE>.md` (nguồn chính).
2. `research/deep/_CORRECTIONS.md` — áp mọi dòng liên quan domain của bạn.
3. `research/deep/linkcheck-deep-all.json` — verdict từng URL.
4. Khi cần dẫn chiếu chéo: các file `research/deep/*.md` khác (chỉ đọc phần liên quan).

## Quy tắc

- **Không thêm sự kiện mới chưa xác minh.** Được phép WebFetch để: (a) đối chiếu câu trích nguyên văn đang dựa OCR mất dấu (C21) với bản có dấu; (b) thay link lỗi bằng link gốc mở được. Nếu không đối chiếu được → chỉ diễn giải, bỏ nguyên văn.
- **ID ổn định**: giữ đúng số `<CODE>-Rnn` của research (không đánh số lại, vì domain khác đang dẫn chiếu). Chuẩn hóa tiền tố: TELE-AI dùng `TELE-Rnn`; các domain khác giữ mã như tên file. Pattern: `<CODE>-Pnn`. Audit: `<CODE>-Ann`.
- **Mức**: chỉ dùng `BẮT BUỘC`, `BẮT BUỘC?`, `NÊN`. Mục có hai mức thì tách phần.
- **Suy luận** của research phải giữ nhãn "(suy luận)".
- **Link**: chỉ giữ URL có verdict OK, hoặc URL bạn vừa tự mở được và trang chứa đúng văn bản. Ưu tiên link gốc (datafiles.chinhphu.vn, vanban.chinhphu.vn, congbao.chinhphu.vn, moh.gov.vn, kcb.vn, baohiemxahoi.gov.vn). Bài báo chỉ giữ khi là nguồn duy nhất (dự thảo), ghi "(báo, bối cảnh)". Link chết/không khớp mà không thay được → bỏ link, giữ số hiệu + "link chưa kiểm tra được".
- **Địa chỉ hệ thống/API** (vd `https://api.emrhub.vn`) viết trong backtick, không làm link.
- Trùng lặp với domain khác: giữ yêu cầu ở domain "chủ", domain kia ghi "xem <ID>".
- Tiếng Việt có dấu đầy đủ. Không emoji.

## Khung file đích (bắt buộc)

```
# <CODE> — <Tên domain>

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: <BV công / BV tư / phòng khám / nhà thuốc / vendor…> · Research gốc: `research/deep/<CODE>.md`

## Tóm tắt nhanh
5–8 gạch đầu dòng: nghĩa vụ nặng nhất, hạn chót gần nhất (ngày cụ thể), bẫy dễ sai nhất.

## Mục lục
(liệt kê ID + tiêu đề ngắn của mọi yêu cầu, để tra nhanh)

## 1. Văn bản
| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
(Xác minh: gốc / gốc-OCR / thứ cấp / chưa xác minh)

## 2. Yêu cầu
### <CODE>-R01 — <tiêu đề ngắn>
- **Căn cứ**: <số hiệu> Đ.. k.. đ.. — diễn giải (trích ≤ 2 câu nếu đã đối chiếu bản có dấu)
- **Áp dụng**: … · **Hiệu lực/hạn**: …
- **Mức**: BẮT BUỘC | BẮT BUỘC? | NÊN
- **Phần mềm phải**: hành vi kiểm chứng được
- **Bẫy**: (nếu có)

## 3. Pattern thiết kế
### <CODE>-P01 — <tên>
- **Giải quyết**: <ID R>
- **Cách làm**: …
- **Gợi ý dữ liệu**: bảng/trường/ràng buộc/chỉ mục (ngắn, không dạy thiết kế từ đầu)
- **Đánh đổi**: …

## 4. Checklist audit
| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |

## 5. Mốc thời gian
| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới (so với 2026-10-06) |

## 6. Bẫy trích dẫn và chuỗi thay thế

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan
```

Độ dài mục tiêu: 250–450 dòng mỗi file. Cắt phần kể quá trình research, giữ nguyên chất liệu yêu cầu.

## Sau khi viết xong mỗi file

Chạy: `python3 scripts/check_links.py <file đích>` và sửa đến khi chỉ còn link thật sự là "báo, bối cảnh" hoặc đã ghi chú. Báo lại số link còn vấn đề và lý do.

## Trả về cho điều phối

Mỗi domain: số yêu cầu theo mức, các sửa đã áp từ `_CORRECTIONS.md`, câu trích OCR đã đối chiếu/đã bỏ, link còn vấn đề, mâu thuẫn mới phát hiện giữa domain (nếu có). Dưới 250 từ mỗi domain.
