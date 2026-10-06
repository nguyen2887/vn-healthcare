# TC-MS — Hóa đơn, giá dịch vụ, thanh toán, bảo hiểm thương mại, mua sắm và thuê dịch vụ công nghệ số

> Kiểm tra lần cuối: 2026-10-06 · Áp dụng: BV công (ĐVSNCL, dùng NSNN), BV tư, phòng khám, nhà thuốc, đơn vị y tế công có thu phí/lệ phí, nền tảng đặt khám, vendor HIS/POS/HĐĐT/SaaS · Research gốc: `research/deep/TC-MS.md`

Phạm vi: hóa đơn điện tử, chứng từ điện tử (NĐ 254/2026, TT 91/2026-BTC); chế tài hóa đơn (NĐ 125/2020 sửa bởi NĐ 310/2025); giá dịch vụ KCB và minh bạch chi phí; thanh toán không tiền mặt và ranh giới giấy phép trung gian thanh toán (NĐ 52/2024); bảo hiểm sức khỏe thương mại; NQ 261/2025; đầu tư, mua sắm, thuê dịch vụ công nghệ số bằng NSNN (Luật 148/2025, NĐ 224/2026, TT 39 và 41/2026-BKHCN, TT 34/2025-BKHCN). Không lặp: niêm yết giá trên HTTT (HTTT-BC-R11), bảng kê 01/KBCB (BHYT-DATA-R21), hóa đơn BHYT gắn biên bản quyết toán (BHYT-GD-R26), thông báo trước chi phí ngoài phạm vi BHYT (BHYT-GD-R35), mức hưởng theo cấp CMKT (BHYT-GD-R10), cấm chia dữ liệu cho bảo hiểm thương mại (DLCN-R09), hợp đồng thuê dịch vụ theo NĐ 331 (ANM-R22, R23).

## Tóm tắt nhanh

- **Từ 01/07/2026 hóa đơn theo NĐ 254/2026 + TT 91/2026**; NĐ 123/2020, NĐ 70/2025, TT 32/2025 hết HL. "Điểm m" (phiếu thu từng giao dịch, hóa đơn tổng hợp cuối ngày cho dịch vụ KCB) nay ở **NĐ 254 Đ9 k4 m**.
- **Mọi khoản thu phải có phiếu thu lưu trên hệ thống**; khách không lấy hóa đơn thì cuối ngày lập một hóa đơn tổng hợp kèm bảng kê. Phần BHYT lập hóa đơn cho BHXH **tại thời điểm được thanh, quyết toán**, không lập tại quầy.
- **Không còn "hủy hóa đơn"**: hóa đơn sai chỉ thông báo (Mẫu 04/SS-HĐĐT), điều chỉnh hoặc thay thế; lần xử lý sau phải theo hình thức lần đầu (TT 91 Đ10). Hóa đơn máy tính tiền sai chỉ được thay thế.
- **Hạn gần nhất: 31/12/2026** hết dùng biên lai giấy; từ **01/01/2027** đơn vị thu phí, lệ phí phải dùng biên lai điện tử (NĐ 254 Đ44 k2). Viện phí là giá dịch vụ, dùng hóa đơn, không dùng biên lai (suy luận).
- **Bảng giá thống nhất toàn quốc (TT 13, 21, 22/2023) hết HL từ 01/01/2025**; giá phải lấy từ văn bản phê duyệt giá của chính cơ sở (QĐ BYT, NQ HĐND hoặc cơ sở tự quyết).
- **Vendor không được giữ tiền người bệnh** hay làm cổng thanh toán khi không có giấy phép trung gian thanh toán; tiền phải đi thẳng vào tài khoản cơ sở (NĐ 52/2024 Đ8 k5, k7).
- **Chỉ gửi dữ liệu cho DNBH/TPA khi có yêu cầu bằng văn bản của chính người bệnh** (Luật 91/2025 Đ26 k2); văn bản điện tử hợp lệ nếu truy cập, tham chiếu được (Luật 20/2023 Đ9 k1).
- **Mua sắm CNTT bằng NSNN**: NĐ 73/2019 + NĐ 82/2024 → NĐ 45/2026 (01/03/2026) → NĐ 224/2026 (01/07/2026). Ưu tiên thuê dịch vụ sẵn có; cấm thuê để nâng cấp hệ thống đã mua; hết hợp đồng thuê phải bàn giao toàn bộ dữ liệu rồi xóa tại nhà cung cấp.

## Mục lục

**A. Hóa đơn, chứng từ**: R01 loại hóa đơn theo người bán · R02 phiếu thu, hóa đơn tổng hợp cuối ngày · R03 hóa đơn cho BHXH, hóa đơn chênh lệch · R04 tạm ứng, thu trước · R05 nội dung hóa đơn, bảng kê · R06 hóa đơn máy tính tiền · R07 ký hiệu, số · R08 gửi hóa đơn đúng hạn · R09 xử lý hóa đơn sai · R10 sự cố · R11 lưu trữ, toàn vẹn · R12 ủy nhiệm lập hóa đơn · R13 vendor giải pháp HĐĐT · R14 biên lai phí, lệ phí · R15 chứng từ khấu trừ TNCN · R16 hóa đơn SaaS theo kỳ
**B. Giá, minh bạch chi phí**: R17 danh mục giá có nguồn · R18 giá theo yêu cầu, chênh lệch, tư nhân BHYT · R19 niêm yết, kê khai · R20 giải thích chi phí · R21 thu phải có căn cứ · R22 NQ 261: 100%, 2030 · R23 hạch toán riêng dịch vụ theo yêu cầu
**C. Thanh toán**: R24 hỗ trợ không tiền mặt · R25 ranh giới giấy phép TGTT · R26 đối soát
**D. Bảo hiểm thương mại**: R27 chỉ gửi DNBH khi người bệnh yêu cầu bằng văn bản · R28 toàn vẹn chứng từ bồi thường · R29 tách bên trả · R30 người bệnh tự lấy hồ sơ
**E. Mua sắm, thuê CNTT bằng NSNN**: R31 dịch vụ sẵn có/không sẵn có · R32 sở hữu, bàn giao, xóa dữ liệu · R33 SLA, báo cáo dịch vụ · R34 vận hành thử · R35 bàn giao mã nguồn, bảo hành · R36 nguyên tắc kiến trúc · R37 yêu cầu tối thiểu hệ thống số · R38 ưu đãi sản phẩm số VN · R39 báo cáo hoàn thành, hiệu quả

## 1. Văn bản

| Số hiệu | Tên ngắn | Hiệu lực | Trạng thái | Xác minh | Link |
|---|---|---|---|---|---|
| 254/2026/NĐ-CP (30/06/2026) | HĐĐT, chứng từ điện tử (chi tiết Luật QLT 108/2025) | 01/07/2026 | Còn HL; Đ43 k2: hết HL NĐ 123/2020, Đ1 NĐ 41/2022, NĐ 70/2025 | gốc-OCR (đối chiếu lại Đ6, Đ9 k4 m, PL mục a.3, Đ44 k2) | [VB 218689](https://vanban.chinhphu.vn/?pageid=27160&docid=218689) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/254-ndcp.signed.pdf) |
| 91/2026/TT-BTC (30/06/2026) | Hướng dẫn HĐĐT, chứng từ điện tử | 01/07/2026 | Còn HL; Đ25 k2: hết HL TT 32/2025/TT-BTC | gốc-OCR | [VB 219006](https://vanban.chinhphu.vn/?pageid=27160&docid=219006) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/91-btc.signed.pdf) |
| 125/2020/NĐ-CP sửa bởi 102/2021, 310/2025, 291/2026 | Xử phạt thuế, hóa đơn | NĐ 310: 16/01/2026; NĐ 291: 21/07/2026 | Còn HL; NĐ 291 chỉ thêm Đ19a, không đụng hóa đơn | gốc (NĐ 310); gốc-OCR (NĐ 291); NĐ 125 gốc chưa đọc | [NĐ 310 Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-310-2025-nd-cp-46755.htm) · [VB 216102](https://vanban.chinhphu.vn/?pageid=27160&docid=216102) · [VB 218956 (NĐ 291)](https://vanban.chinhphu.vn/?pageid=27160&docid=218956) |
| 15/2023/QH15 (VBHN 26/VBHN-VPQH) | Luật KCB: Đ9 k1, Đ12 k2, Đ44 k5, Đ59 k3, Đ60 k4, Đ110, Đ111, Đ112 | 01/01/2024 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/3/26-vbhn-vpqh.pdf) |
| 96/2023/NĐ-CP | Đ119 giá dịch vụ KCB | 01/01/2024 | Còn HL (văn bản sửa 2025–2026 chưa kiểm) | gốc (bản đăng lại) | [VB 209491](https://vanban.chinhphu.vn/?pageid=27160&docid=209491) · [Toàn văn, laichau.gov.vn](https://laichau.gov.vn/tin-tuc-su-kien/chuyen-de/tin-trong-nuoc/toan-van-nghi-dinh-so-96-2023-nd-cp-quy-dinh-chi-tiet-mot-so-dieu-cua-luat-kham-benh-chua-benh.html) |
| 21/2024/TT-BYT (17/10/2024) | Phương pháp định giá dịch vụ KCB; Đ10, Đ15 k5 | 17/10/2024 | Còn HL; Đ11 k2: TT 13, 21, 22/2023 hết HL 01/01/2025 | gốc-OCR | [VB 211506](https://vanban.chinhphu.vn/?pageid=27160&docid=211506) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/10/21-byt.pdf) |
| 90/2026/NĐ-CP | Xử phạt y tế: Đ38 k3 b, Đ85–86 | 15/05/2026 | Còn HL | gốc-OCR | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/90-ndcp.signed.pdf) |
| 52/2024/NĐ-CP (15/05/2024) | Thanh toán không dùng tiền mặt: Đ3 k17–18, Đ8, Đ22 | 01/07/2024 | Còn HL; văn bản sửa chưa thấy | gốc-OCR | [VB 210262](https://vanban.chinhphu.vn/?pageid=27160&docid=210262) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2024/5/52-nd-cp.signed.pdf) |
| 124/CĐ-TTg (30/07/2025) | Công điện thúc đẩy TTKDTM | — | Chỉ đạo, không phải QPPL | gốc-OCR | [VB 214760](https://vanban.chinhphu.vn/?pageid=27160&docid=214760) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/124cd.signed.pdf) |
| 1813/QĐ-TTg (2021) | Đề án TTKDTM 2021–2025 | — | Hết giai đoạn; đề án kế nhiệm chưa xác minh | gốc-meta | [VB 204364](https://vanban.chinhphu.vn/?pageid=27160&docid=204364) |
| 08/2022/QH15 | Luật Kinh doanh bảo hiểm: Đ9 k4, Đ11 k3, Đ20 k2 i, Đ30, Đ31 | 01/01/2023 | Còn HL (sửa đổi chưa kiểm) | gốc | [VB 206242](https://vanban.chinhphu.vn/?pageid=27160&docid=206242) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2022/07/08-2022-qh15..pdf) |
| 91/2025/QH15 | Luật BVDLCN: Đ26 (sức khỏe, bảo hiểm) | 01/01/2026 | Còn HL | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/91qh.signed.pdf) |
| 20/2023/QH15 | Luật Giao dịch điện tử: Đ9 k1, Đ13 | 01/07/2024 | Còn HL (Luật 20/2026/QH16 sửa từ 01/03/2027, không đụng Đ9, Đ13 theo BAOMAT-CB-R26) | gốc | [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2023/8/luat20-2023-qh15..pdf) |
| 261/2025/QH15 (11/12/2025) | Cơ chế đột phá chăm sóc sức khỏe: mức hưởng 100%, miễn viện phí 2030 | 01/01/2026; 01/01/2030 | Còn HL | thứ cấp (HL xác nhận qua QĐ 388/QĐ-TTg) | [luatvietnam (thứ cấp)](https://luatvietnam.vn/y-te/nghi-quyet-261-2025-qh15-co-che-dot-pha-bao-ve-va-nang-cao-suc-khoe-nhan-dan-422070-d1.html) · [VB 217137 (QĐ 388)](https://vanban.chinhphu.vn/?pageid=27160&docid=217137) |
| 148/2025/QH15 | Luật Chuyển đổi số: Đ7, Đ8, Đ23 k3, Đ47–48 | 01/07/2026 | Còn HL; thay Luật CNTT | gốc | [Công báo](https://congbao.chinhphu.vn/van-ban/luat-so-148-2025-qh15-468708.htm) |
| 224/2026/NĐ-CP (24/06/2026) | Chi tiết Luật CĐS; Chương VI Đ36–69 (đầu tư, mua sắm, thuê bằng NSNN) | 01/07/2026 | Còn HL; Đ90 k2: hết HL NĐ 45/2026, NĐ 42/2022, NĐ 64/2007; Đ91 chuyển tiếp | gốc-OCR | [VB 218633](https://vanban.chinhphu.vn/?pageid=27160&docid=218633) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/224-ndcp.signed.pdf) |
| 45/2026/NĐ-CP (26/01/2026) | Quản lý đầu tư ứng dụng CNTT dùng NSNN | 01/03/2026 | **Hết HL 01/07/2026**, trừ dự án chuyển tiếp; đã thay NĐ 73/2019, NĐ 82/2024, NQ 04/2025/NQ-CP | gốc | [VB 216790](https://vanban.chinhphu.vn/?pageid=27160&docid=216790) · [Công báo](https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-45-2026-nd-cp-468868.htm) |
| 39/2026/TT-BKHCN | Chi phí đầu tư, mua sắm, thuê dịch vụ CĐS | 01/07/2026 | Còn HL; thay TT 18/2024/TT-BTTTT | gốc-OCR | [VB 218792](https://vanban.chinhphu.vn/?pageid=27160&docid=218792) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/39-bkhcn.signed.pdf) |
| 41/2026/TT-BKHCN | Chất lượng, nghiệm thu, thuê dịch vụ CĐS: Đ14–16, PL VI, PL VIII | 01/07/2026 | Còn HL; thay TT 16/2024/TT-BTTTT | gốc-OCR | [VB 218794](https://vanban.chinhphu.vn/?pageid=27160&docid=218794) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/41-bkhcn.signed.pdf) |
| 34/2025/TT-BKHCN | Ưu đãi sản phẩm, dịch vụ công nghệ số VN khi thuê, mua bằng NSNN | 01/01/2026 | Còn HL; thay TT 40/2020/TT-BTTTT | gốc-OCR | [VB 216032](https://vanban.chinhphu.vn/?pageid=27160&docid=216032) · [PDF](https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/11/34-bkhcn.pdf) |
| 697/QĐ-BYT | Mẫu bảng kê chi phí KCB (chi tiết BHYT-DATA-R21) | 19/03/2026 | Còn HL | gốc | [PDF (file BHXH đặt tên "QĐ 967")](https://baohiemxahoi.gov.vn/content/tintuc/Lists/News/Attachments/26339/Q%C4%90%20967.pdf) |

Văn bản được dẫn nhưng chưa đọc gốc: TT 15/2024/TT-NHNN (sửa bởi 30/2025, 21/2026), Luật Giá 16/2023 và NĐ 85/2024 (sửa bởi NĐ 128/2026, thứ cấp), NĐ 87/2024 (xử phạt giá), Luật thuế GTGT 48/2024, NĐ 174/2016 (lưu tài liệu kế toán), TT 94/2026/TT-BTC (rủi ro cao về hóa đơn), NĐ 104/2026/NĐ-CP (chi thường xuyên), TT 67/2023/TT-BTC.

## 2. Yêu cầu

### A. Hóa đơn điện tử, chứng từ điện tử

### TC-MS-R01 — Loại hóa đơn theo người bán: có mã, không mã, máy tính tiền
- **Căn cứ**: NĐ 254 Đ2 k1 (người bán gồm ĐVSNCL có bán hàng, cung cấp dịch vụ); Đ6 k1 a (tổ chức, HKD dùng HĐĐT có mã, trừ b, c); Đ6 k1 b (**doanh nghiệp** trong các lĩnh vực có "y tế", đủ hạ tầng phần mềm thì được dùng HĐĐT không mã, trừ trường hợp rủi ro cao); Đ6 k1 c (bán trực tiếp người tiêu dùng, gồm bán lẻ, dùng HĐĐT từ máy tính tiền; đã đăng ký theo a hoặc b thì không bắt buộc); Đ6 k1 d (HKD doanh thu năm trên 01 tỷ đồng dùng HĐĐT có mã hoặc từ máy tính tiền). TT 91 Đ11 k2 (người dùng HĐ không mã bị xác định rủi ro cao chuyển sang có mã trong 10 ngày làm việc); Đ6 k2 a (đăng ký đối chiếu sinh trắc người đại diện).
- **Áp dụng**: BV công, BV tư, PK, nhà thuốc, vendor HIS/POS · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (phân loại theo Đ6) / BẮT BUỘC? (hai điểm suy luận ở Bẫy)
- **Phần mềm phải**: cấu hình người bán theo pháp nhân/MST: `invoice_mode ∈ {CQT_CODE, NO_CODE, CASH_REGISTER}` kèm căn cứ và ngày hiệu lực; chuyển chế độ khi cơ quan thuế thông báo mà không mất chuỗi số; cấu hình ký hiệu và chế độ riêng cho từng điểm bán (quầy viện phí, nhà thuốc BV, căng tin).
- **Bẫy**: (1) BV công là ĐVSNCL, không phải "doanh nghiệp" nên mặc định HĐĐT có mã (suy luận). (2) Dịch vụ KCB không có trong danh sách Đ6 k1 c; nhà thuốc là bán lẻ nên thuộc diện máy tính tiền, trừ khi đã đăng ký HĐĐT thường (suy luận). Vendor không làm thay bước xác nhận sinh trắc của người đại diện.

### TC-MS-R02 — Phiếu thu từng giao dịch; hóa đơn tổng hợp cuối ngày (NĐ 254 Đ9 k4 m)
- **Căn cứ**: NĐ 254 Đ9 k4 m (diễn giải, gốc-OCR đã đối chiếu): cơ sở KCB dùng phần mềm quản lý KCB và viện phí, mỗi giao dịch KCB, chụp, chiếu, xét nghiệm có in phiếu thu và lưu trên hệ thống CNTT; khách không lấy hóa đơn thì cuối ngày căn cứ thông tin KCB và phiếu thu lập HĐĐT tổng hợp cho dịch vụ trong ngày; khách yêu cầu thì lập HĐĐT giao khách. Đ9 k2 (dịch vụ: thời điểm hoàn thành, hoặc thời điểm thu tiền nếu thu trước). Chế tài: NĐ 125 Đ24 k2–3 sửa bởi NĐ 310 Đ1 k14: lập sai thời điểm từ 500.000–1.500.000 đồng (01 số hóa đơn) tăng dần tới 50–70 triệu (từ 100 số); không lập hóa đơn tới 60–80 triệu (từ 50 số); buộc lập hóa đơn.
- **Áp dụng**: mọi cơ sở KCB có phần mềm viện phí · **Hiệu lực/hạn**: 01/07/2026 (kế thừa NĐ 70/2025 từ 01/06/2025)
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mọi khoản thu sinh phiếu thu có số, thời điểm, người thu, phương thức, liên kết lượt KCB và dòng dịch vụ; quầy cho chọn "lấy hóa đơn ngay"; job cuối ngày gom mọi phiếu thu chưa lập hóa đơn thành hóa đơn tổng hợp kèm bảng kê (R05), không bỏ sót phiếu bị hủy, hoàn trong ngày; cảnh báo khi job chưa chạy hoặc lỗi; báo cáo đối chiếu ngày (tổng phiếu thu = hóa đơn cá nhân + tổng hợp ± điều chỉnh).
- **Bẫy**: "cuối ngày" là ngày dương lịch của phiếu thu; mốc 06:00–05:59 ở Đ9 k4 q chỉ cho casino. Với HĐ có mã, hóa đơn tổng hợp phải được cấp mã mới coi là đã lập. Mức phạt NĐ 125 áp cho cá nhân hay tổ chức: chưa đọc NĐ 125 Đ7 (mục 7).

### TC-MS-R03 — Hóa đơn cho BHXH tại thời điểm thanh, quyết toán; hóa đơn chênh lệch
- **Căn cứ**: NĐ 254 Đ9 k4 m đoạn 2 (lập hóa đơn cho BHXH tại thời điểm được BHXH thanh, quyết toán chi phí KCB BHYT). TT 91 Đ10 k5 a.2 (giá trị thay đổi theo kết luận cơ quan có thẩm quyền → hóa đơn mới cho số chênh lệch, giảm ghi âm, tăng ghi dương); Đ10 k6 d. TT 12/2026/TT-BTC Đ14 k3: xem BHYT-GD-R26.
- **Áp dụng**: cơ sở KCB có hợp đồng BHYT · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tách công nợ BHXH khỏi phần người bệnh trả; không lập hóa đơn phần BHYT tại quầy; có Biên bản quyết toán (06/BH) thì sinh hóa đơn cho BHXH theo số quyết toán; xuất toán, bổ sung sau quyết toán → hóa đơn chênh lệch tham chiếu biên bản.
- **Bẫy**: người bệnh hưởng 100% (R22) không có khoản thu tại quầy nên không có hóa đơn cá nhân.

### TC-MS-R04 — Tạm ứng, thu trước, hoàn ứng
- **Căn cứ**: NĐ 254 Đ9 k2 (thu trước hoặc trong khi cung cấp dịch vụ thì lập hóa đơn khi thu tiền, trừ tiền đặt cọc theo Bộ luật Dân sự để bảo đảm hợp đồng). TT 91 Đ10 k5 c.4 (đã lập hóa đơn khi thu trước, sau đó hủy hoặc chấm dứt một phần → điều chỉnh).
- **Áp dụng**: BV, PK có tạm ứng nội trú, gói trả trước (thai sản, KSK) · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC? (tạm ứng viện phí là "thu trước" hay "đặt cọc" chưa có hướng dẫn: hỏi cơ quan thuế)
- **Phần mềm phải**: `advance_type ∈ {DEPOSIT_GUARANTEE, PREPAYMENT}` cấu hình theo ý kiến cơ quan thuế của cơ sở; PREPAYMENT lập hóa đơn khi thu, ra viện lập hóa đơn phần chênh lệch hoặc điều chỉnh giảm phần hoàn; DEPOSIT_GUARANTEE chỉ phiếu thu, lập hóa đơn khi bù trừ; gói trả trước luôn PREPAYMENT (suy luận).
- **Bẫy**: bảo lãnh viện phí qua phong tỏa tài khoản ngân hàng không phát sinh khoản thu trước khi giải tỏa nên không sinh hóa đơn ở bước phong tỏa (suy luận; cổng bảo lãnh chỉ có nguồn báo).

### TC-MS-R05 — Nội dung hóa đơn dịch vụ KCB và bảng kê kèm hóa đơn
- **Căn cứ**: NĐ 254 Đ10 k1 (chỉ tiêu bắt buộc; người mua ghi MST hoặc mã ĐVQHNS hoặc số định danh cá nhân); Phụ lục: người mua không cung cấp thông tin ghi "Bán cho người tiêu dùng"; tên dịch vụ tiếng Việt, có mã thì ghi cả mã; dịch vụ KCB thuộc nhóm được lập hóa đơn kèm bảng kê, bảng kê lưu cùng hóa đơn, hóa đơn ghi "kèm theo bảng kê số…, ngày…"; có bảng kê thì hóa đơn không nhất thiết có đơn giá; tiếng nước ngoài đặt trong ngoặc hoặc dòng dưới, cỡ nhỏ hơn.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hóa đơn tổng hợp và hóa đơn cho BHXH kèm bảng kê của người bán, liên kết hai chiều số hóa đơn ↔ số bảng kê; ô người mua nhận số định danh 12 số; mặc định "Bán cho người tiêu dùng"; tên dịch vụ lấy từ danh mục giá có mã.
- **Bẫy**: bảng kê kèm hóa đơn thuế khác bảng kê 01/KBCB (BHYT-DATA-R21). Dịch vụ y tế thuộc diện không chịu thuế GTGT (Luật 48/2024 chưa đọc gốc): cấu hình thuế suất theo mặt hàng (thuốc bán lẻ khác dịch vụ).

### TC-MS-R06 — Hóa đơn từ máy tính tiền (nhà thuốc, quầy bán lẻ)
- **Căn cứ**: NĐ 254 Đ3 k3–4; Đ8 k9 (không bắt buộc chữ ký số); Đ10 k4 (nội dung tối thiểu; người mua nếu yêu cầu; mã cơ quan thuế hoặc dữ liệu để tra cứu, gửi qua tin nhắn, email, đường dẫn hoặc mã QR); Đ15 k3 (cuối ngày gửi dữ liệu đến cơ quan thuế). TT 91 PL I (ký tự thứ tư "M"); Đ10 k1 c (sai chỉ được thay thế).
- **Áp dụng**: nhà thuốc (DN, HKD > 1 tỷ hoặc tự đăng ký), quầy bán lẻ trong BV · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (khi dùng chế độ máy tính tiền)
- **Phần mềm phải**: POS in/hiển thị hóa đơn có dấu hiệu máy tính tiền, mã tra cứu hoặc QR; gửi dữ liệu cuối ngày; lỗi chỉ cho thay thế; mỗi giao dịch bán gắn sổ kho thuốc (DUOC-R25).

### TC-MS-R07 — Ký hiệu mẫu, ký hiệu, số hóa đơn
- **Căn cứ**: TT 91 Đ4 k1–2, PL I: ký hiệu mẫu 1 chữ số (1 GTGT; 2 bán hàng; 5 tem/vé/phiếu thu điện tử có nội dung hóa đơn; 8, 9 hóa đơn tích hợp biên lai); ký hiệu 6 ký tự: C/K + 2 số năm + chữ loại (T thường; M máy tính tiền; L cấp từng lần…) + 2 ký tự tự đặt.
- **Áp dụng**: mọi người bán · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: sinh ký hiệu theo năm lập; dùng 2 ký tự cuối phân biệt quầy; không tái dùng số.

### TC-MS-R08 — Gửi hóa đơn cho người mua và cơ quan thuế đúng hạn; cổng tra cứu
- **Căn cứ**: NĐ 254 Đ12 k1–3 (HĐ có mã: ký, gửi cấp mã, gửi người mua); Đ15 k3 (gửi người mua ngay sau khi có mã); Đ16 k3 a.3 (HĐ không mã: gửi người mua và cơ quan thuế chậm nhất ngày làm việc tiếp theo); Đ16 k3 b.2 (qua tổ chức truyền nhận); Đ17 k2 d (người bán công khai cách tra cứu, nhận file gốc); Đ18 k1 c.
- **Áp dụng**: mọi người bán · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: hàng đợi trạng thái `created → signed → sent_to_tax → coded → delivered`, cảnh báo quá hạn theo lịch ngày làm việc; cổng tra cứu hóa đơn cho người bệnh (mã in trên phiếu thu, QR, SMS/email/app) chỉ trả hóa đơn, không lộ thông tin bệnh án (suy luận từ DLCN).

### TC-MS-R09 — Hóa đơn sai: thông báo, điều chỉnh, thay thế; không "hủy"
- **Căn cứ**: TT 91 Đ10 k1 a (sai tên, địa chỉ mà không sai MST, số tiền, thuế suất, hàng hóa → thông báo người mua, không lập lại, gửi Mẫu 04/SS-HĐĐT); k1 b (sai MST, tên hàng, số tiền, thuế suất → điều chỉnh hoặc thay thế; người mua là tổ chức/HKD thì có văn bản thỏa thuận; người mua là cá nhân thì thông báo cho người mua hoặc trên website; nhiều hóa đơn sai cùng người mua trong tháng → một hóa đơn điều chỉnh kèm Mẫu 01/BK-ĐCTT); k1 c (máy tính tiền chỉ thay thế); k3 (cơ quan thuế phát hiện sai, Mẫu 01/TB-RSĐT); k6 a (lần sau theo hình thức lần đầu); k6 c (tăng ghi dương, giảm ghi âm). Đ24 k2 (hóa đơn lập theo văn bản cũ vẫn điều chỉnh, thay thế theo quy định).
- **Áp dụng**: mọi người bán · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không có nút xóa/hủy sau khi gửi cơ quan thuế; luồng sửa chọn 1 trong 3 nhánh, khóa nhánh theo lần đầu; lưu bằng chứng thỏa thuận hoặc thông báo; hóa đơn điều chỉnh tham chiếu hóa đơn gốc, mang dấu âm/dương; hoàn viện phí → điều chỉnh giảm.
- **Bẫy**: nhiều HIS cũ còn chức năng "hủy hóa đơn" theo tập quán NĐ 51/2010, NĐ 123/2020: điểm audit quan trọng. Sửa hóa đơn ngoài luồng làm hỏng tính toàn vẹn hồ sơ bồi thường (R28).

### TC-MS-R10 — Sự cố khi không lập, cấp mã, truyền được hóa đơn
- **Căn cứ**: NĐ 254 Đ14 k1 (liên hệ cơ quan thuế, nhà cung cấp), k3 (nhà cung cấp lỗi phải thông báo người bán), k4 (hệ thống thuế lỗi → chuyển dữ liệu HĐ không mã trong 02 ngày làm việc từ khi Cục Thuế thông báo hoạt động lại), k5 (bất khả kháng → lập, gửi trong 03 ngày làm việc từ khi khắc phục; ghi sổ, lưu tài liệu chứng minh).
- **Áp dụng**: mọi người bán; vendor HĐĐT · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: kênh HĐĐT lỗi vẫn thu tiền và in phiếu thu (đủ điều kiện điểm m), xếp hàng hóa đơn chờ; nhật ký sự cố (bắt đầu, kết thúc, nguồn, thông báo của Cục Thuế); job gửi bù trong hạn 02/03 ngày làm việc.

### TC-MS-R11 — Lưu trữ, toàn vẹn, in và tra cứu hóa đơn, chứng từ
- **Căn cứ**: NĐ 254 Đ5 k1 (an toàn, toàn vẹn, lưu đủ thời hạn theo pháp luật kế toán), k2 (lưu dạng thông điệp dữ liệu theo Luật GDĐT Đ13, sẵn sàng in hoặc tra cứu khi có yêu cầu), k4 (bản chuyển sang giấy khớp nội dung; không có hiệu lực giao dịch trừ hóa đơn máy tính tiền); Đ16 k4, Đ29 k4. Luật 20/2023 Đ13 k1. NĐ 174/2016 Đ12–13: tài liệu kế toán lưu tối thiểu 10 năm (thứ cấp).
- **Áp dụng**: mọi người bán · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (lưu, toàn vẹn) / BẮT BUỘC? (con số thời hạn cụ thể)
- **Phần mềm phải**: lưu XML gốc đã ký, mã cơ quan thuế, thông điệp phản hồi bất biến kèm PDF; băm chống sửa; in "bản chuyển đổi" có ghi chú; xuất hàng loạt cho thanh tra; khi đổi vendor phải bàn giao kho XML (R32).

### TC-MS-R12 — Ủy nhiệm lập hóa đơn (nền tảng, chuỗi PK, vendor lập hộ)
- **Căn cứ**: NĐ 254 Đ4 k5; Đ19 (bên nhận ủy nhiệm lập trong phạm vi, thể hiện bên ủy nhiệm là người bán, gửi cơ quan thuế, lưu trữ, bảo mật; không dùng dữ liệu hóa đơn ngoài phạm vi ủy nhiệm). TT 91 Đ9 k2 (nội dung hợp đồng ủy nhiệm), k3 (thông báo Mẫu 01/ĐKTĐ-HĐĐT, kể cả khi chấm dứt trước hạn).
- **Áp dụng**: nền tảng đặt khám/khám từ xa thu hộ rồi lập hóa đơn, chuỗi PK, vendor · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (khi có ủy nhiệm)
- **Phần mềm phải**: hóa đơn ủy nhiệm hiển thị cả hai bên; cấu hình ủy nhiệm có hiệu lực theo hợp đồng; dữ liệu hóa đơn từng bên tách biệt, không dùng cho phân tích, marketing của nền tảng.

### TC-MS-R13 — Vendor tự cung cấp giải pháp HĐĐT
- **Căn cứ**: TT 91 Đ12 k1 (tổ chức cung cấp giải pháp: pháp nhân VN; công khai thông tin; ≥05 nhân sự ĐH CNTT; truyền nhận với cơ quan thuế qua tổ chức nhận, truyền, lưu trữ; ghi nhật ký truyền nhận để đối soát; sao lưu, khôi phục; kết quả kiểm thử kết nối), k2 (tổ chức nhận, truyền, lưu trữ: ≥05 năm hoạt động, ký quỹ ≥05 tỷ, ≥20 nhân sự, TTDL chính và dự phòng cách ≥20 km…), k3 (Cục Thuế công khai danh sách). NĐ 254 Đ3 k9, Đ20.
- **Áp dụng**: vendor HIS/POS tự xây module phát hành HĐĐT · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC? (bắt buộc nếu vendor đứng tên tổ chức cung cấp giải pháp; không áp nếu chỉ gọi API nhà cung cấp đã công khai, suy luận)
- **Phần mềm phải**: hoặc tích hợp nhà cung cấp HĐĐT có tên trên trang Cục Thuế (khuyến nghị), hoặc tự đăng ký theo k1 và có nhật ký truyền nhận đối soát được.

### TC-MS-R14 — Biên lai thu phí, lệ phí điện tử
- **Căn cứ**: NĐ 254 Đ4 k2 (thu thuế, phí, lệ phí phải lập biên lai điện tử); Đ4 k6, Đ25 (ủy nhiệm lập biên lai; thông báo cơ quan thuế chậm nhất 03 ngày trước; niêm yết tại nơi thu); Đ4 k7 (tích hợp biên lai và hóa đơn khi một khách vừa nộp phí vừa trả dịch vụ); Đ23 k2 (số tối đa 8 chữ số, bắt đầu 01/01, kết thúc 31/12; chữ ký số); Đ29 k3 b (gửi bảng tổng hợp trong ngày lập); Đ44 k2 (biên lai giấy dùng hết 31/12/2026; từ 01/01/2027 tiêu hủy biên lai giấy chưa dùng, chuyển sang biên lai điện tử). TT 91 Đ4 k6 d (Mẫu 01/TH-BLĐT), PL I (ký hiệu mẫu 8, 9).
- **Áp dụng**: đơn vị y tế công có khoản thu phí, lệ phí thuộc NSNN (danh mục cụ thể chưa xác minh); không áp cho viện phí (suy luận) · **Hiệu lực/hạn**: 01/07/2026; xong trước 01/01/2027
- **Mức**: BẮT BUỘC (với đơn vị thu phí, lệ phí)
- **Phần mềm phải**: module biên lai điện tử chuỗi số theo năm; gửi bảng tổng hợp trong ngày; hóa đơn tích hợp biên lai (ký hiệu 8/9) khi cùng giao dịch; không in biên lai giấy từ 01/01/2027.

### TC-MS-R15 — Chứng từ khấu trừ thuế TNCN điện tử
- **Căn cứ**: NĐ 254 Đ4 k2; Đ23 k1; Đ24 k1–3 (lập khi khấu trừ; HĐLĐ dưới 03 tháng: mỗi lần hoặc gộp khi cá nhân yêu cầu; từ 03 tháng: một chứng từ/năm); Đ29 k3 a (gửi người bị khấu trừ và cơ quan thuế ngay trong ngày lập).
- **Áp dụng**: BV, PK trả thu nhập cho người hành nghề ngoài biên chế; vendor HRM · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (khi phần mềm có chức năng chi trả thu nhập)
- **Phần mềm phải**: sinh chứng từ khấu trừ ký số, gửi cơ quan thuế trong ngày; liên kết bảng chấm công, ca khám.

### TC-MS-R16 — Hóa đơn của vendor SaaS bán theo kỳ
- **Căn cứ**: NĐ 254 Đ9 k4 a (dịch vụ CNTT, công nghệ số, nền tảng số bán theo kỳ cho tổ chức: lập khi hoàn thành đối soát nhưng chậm nhất ngày 07 tháng sau hoặc 07 ngày từ khi kết thúc kỳ quy ước).
- **Áp dụng**: vendor SaaS bán cho BV, PK · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: xuất báo cáo đối soát sử dụng theo kỳ (lượt, user, dung lượng) làm căn cứ hóa đơn và nghiệm thu (khớp R33).

### B. Giá dịch vụ KCB và minh bạch chi phí

### TC-MS-R17 — Danh mục giá theo loại giá, nguồn thẩm quyền, có phiên bản
- **Căn cứ**: Luật KCB Đ110 k5 b (BYT quy định giá cho cơ sở thuộc BYT, bộ khác), k6 (HĐND tỉnh cho cơ sở nhà nước địa phương, không vượt giá BYT), k7 (cơ sở nhà nước áp giá cụ thể cho người không có thẻ; tự quyết giá theo yêu cầu, kê khai, niêm yết), k8 (tư nhân tự quyết, kê khai, niêm yết), k9 (PPP). NĐ 96 Đ119 k1 (giá khám, ngày giường, DVKT), k2 (4 loại giá: BHYT; NSNN; ngoài danh mục BHYT không theo yêu cầu; theo yêu cầu), k9. TT 21/2024 Đ9 k3–4; Đ11 k2 (TT 13, 21, 22/2023 hết HL 01/01/2025).
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi dòng giá có `price_category` (4 loại), `legal_source` (QĐ BYT / NQ HĐND / QĐ cơ sở), `effective_from/to`, mã DVKT; không cài sẵn "bảng giá thống nhất toàn quốc"; áp giá theo ngày thực hiện; phiên bản bất biến; liên kết HTTT-BC-R11.
- **Bẫy**: cài sẵn bảng giá TT 22/2023 là dùng văn bản hết HL. Quy tắc áp giá khi giá đổi giữa đợt điều trị: chưa xác minh văn bản hiện hành.

### TC-MS-R18 — Giá theo yêu cầu, phần chênh lệch; cơ sở tư nhân có BHYT
- **Căn cứ**: NĐ 96 Đ119 k7 c (dịch vụ theo yêu cầu: quỹ trả phần trong phạm vi hưởng, người bệnh trả chênh lệch), k8 (cơ sở tư nhân BHYT được thanh toán theo giá do HĐND tỉnh phê duyệt cho cơ sở nhà nước trên địa bàn; chênh lệch người bệnh tự trả), k7 a–b. TT 21/2024 Đ10.
- **Áp dụng**: BV công có dịch vụ theo yêu cầu; BV, PK tư có hợp đồng BHYT · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mỗi dòng chi phí giữ giá cơ sở thu và giá tham chiếu BHYT (tư nhân: giá HĐND địa bàn); `chênh lệch = giá thu − mức quỹ trả` vào phần người bệnh trả; thông báo trước và lưu xác nhận theo BHYT-GD-R35.

### TC-MS-R19 — Niêm yết, kê khai giá; chặn thu chi phí chưa niêm yết
- **Căn cứ**: Luật KCB Đ60 k4; Đ110 k7–8. TT 21/2024 Đ15 k5 c. NĐ 90/2026 Đ38 k3 b (yêu cầu người bệnh thanh toán chi phí chưa niêm yết công khai: 1–3 triệu). Yêu cầu chính: HTTT-BC-R11.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải** (bổ sung HTTT-BC-R11): cờ `is_published` và ngày niêm yết từng dòng giá; chặn hoặc đòi phê duyệt có lý do khi chỉ định, thu dịch vụ chưa niêm yết; xuất bảng giá theo yêu cầu cho hồ sơ kê khai (nội dung hồ sơ theo Luật Giá chưa đọc).

### TC-MS-R20 — Thông tin và giải thích chi tiết chi phí cho người bệnh
- **Căn cứ**: Luật KCB Đ9 k1; Đ12 k2: người bệnh "được cung cấp và giải thích chi tiết về các khoản chi trả dịch vụ khám bệnh, chữa bệnh khi có yêu cầu"; Đ18. Bảng kê 01/KBCB: BHYT-DATA-R21.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: 01/01/2024
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: bảng chi phí lũy kế theo dòng (dịch vụ, ngày, số lượng, đơn giá, quỹ trả, người bệnh trả, chênh lệch) ở mọi thời điểm của đợt điều trị, xem được trên cổng/app; ghi nhật ký lần cung cấp.

### TC-MS-R21 — Mọi khoản thu phải gắn dịch vụ thực tế và giá hiệu lực
- **Căn cứ**: Luật KCB Đ44 k5, Đ59 k3. NĐ 90/2026 Đ85–86 (kê khống, kê tăng). Liên quan BHYT-GD-R29.
- **Áp dụng**: mọi cơ sở KCB · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không có dòng thu tự do không gắn dịch vụ trong danh mục giá; dòng chi phí sinh từ y lệnh/phiếu thực hiện; sửa số lượng, đơn giá sau khi chốt chỉ qua phê duyệt có nhật ký.

### TC-MS-R22 — Mức hưởng 100% theo NQ 261 và lộ trình miễn viện phí 2030
- **Căn cứ** (thứ cấp, luatvietnam): NQ 261/2025/QH15 Đ2 k1 a (người thuộc hộ cận nghèo, người từ đủ 75 tuổi… hưởng 100% từ 01/01/2026), k1 c, k2 (miễn viện phí mức cơ bản theo lộ trình), Đ9 k2 (từ 01/01/2030). Tham số hóa mức hưởng: BHYT-GD-R10.
- **Áp dụng**: cơ sở KCB BHYT · **Hiệu lực/hạn**: 01/01/2026; 01/01/2030
- **Mức**: BẮT BUỘC? (nguồn thứ cấp; nhóm đối tượng chi tiết chưa đọc)
- **Phần mềm phải**: `benefit_rule` theo nhóm đối tượng, mã quyền lợi, ngày hiệu lực; không hard-code tỷ lệ; lượt có phần người bệnh trả = 0 không sinh phiếu thu, hóa đơn cá nhân, chỉ vào hóa đơn cho BHXH (R03); sẵn sàng cho khái niệm "mức cơ bản".

### TC-MS-R23 — Hạch toán riêng dịch vụ theo yêu cầu (BV công)
- **Căn cứ**: TT 21/2024 Đ15 k5 d (hạch toán, theo dõi riêng doanh thu, chi phí dịch vụ theo yêu cầu); Đ15 k5 b (giường theo yêu cầu ≤20% giường bình quân năm trước, trừ khu riêng; chuyên gia dành ≥70% thời gian cho người bệnh không dùng dịch vụ theo yêu cầu).
- **Áp dụng**: BV công có dịch vụ theo yêu cầu · **Hiệu lực/hạn**: 17/10/2024
- **Mức**: BẮT BUỘC (nghĩa vụ cơ sở) / NÊN (báo cáo tự kiểm ngưỡng 20%/70%)
- **Phần mềm phải**: `revenue_stream = ON_DEMAND` trên dòng chi phí, phiếu thu, hóa đơn; báo cáo doanh thu tách luồng; báo cáo tỷ lệ giường và thời gian chuyên gia.

### C. Thanh toán không dùng tiền mặt

### TC-MS-R24 — Hỗ trợ thanh toán không tiền mặt
- **Căn cứ**: CĐ 124/CĐ-TTg mục 1, mục 3 a. Không tìm thấy QPPL buộc cơ sở KCB thu không tiền mặt; mục tiêu "hơn 90%" chỉ thấy trên báo.
- **Áp dụng**: mọi cơ sở KCB
- **Mức**: NÊN
- **Phần mềm phải**: hỗ trợ QR chuyển khoản động, thẻ, ví, thu qua app; không ép một kênh; phương thức thanh toán là trường bắt buộc trên phiếu thu.

### TC-MS-R25 — Vendor không thu hộ, giữ tiền, làm cổng thanh toán khi không có giấy phép TGTT
- **Căn cứ**: NĐ 52/2024 Đ3 k17 (dịch vụ hỗ trợ thu hộ, chi hộ), k18 (cổng thanh toán điện tử); Đ22 k1, k2 b (vốn tối thiểu 50 tỷ cho ví, thu hộ chi hộ, cổng thanh toán), k2 đ (hệ thống đạt an toàn HTTT cấp độ 3); Đ8 k7 (cấm cung ứng TGTT khi chưa được NHNN cấp phép), k5 (cấm mua, bán, thuê, cho thuê, mượn tài khoản thanh toán), k4 (cấm tiết lộ thông tin giao dịch trái quy định).
- **Áp dụng**: vendor HIS, nền tảng đặt khám, app sức khỏe · **Hiệu lực/hạn**: 01/07/2024
- **Mức**: BẮT BUỘC (cấm TGTT không phép) / BẮT BUỘC? (xếp mô hình cụ thể vào "thu hộ": cần ý kiến NHNN hoặc luật sư)
- **Phần mềm phải**: tiền đi thẳng vào tài khoản cơ sở (QR động mang tài khoản cơ sở, hoặc qua ngân hàng/TGTT có phép mà cơ sở ký hợp đồng); vendor chỉ sinh yêu cầu thanh toán và nhận thông báo kết quả để đối soát; không có tài khoản trung gian của vendor; khóa API ngân hàng thuộc cơ sở.
- **Bẫy**: nền tảng thu tiền khám vào tài khoản công ty rồi chuyển lại cho PK dễ rơi vào "thu hộ, chi hộ" hoặc "cho mượn tài khoản" (suy luận); muốn làm phải hợp tác TGTT có phép và xử lý cả ủy nhiệm lập hóa đơn (R12).

### TC-MS-R26 — Đối soát thanh toán điện tử với phiếu thu, hóa đơn
- **Căn cứ**: NĐ 254 Đ9 k4 m; Đ40 k2 (ngân hàng, tổ chức cung ứng dịch vụ thanh toán cung cấp dữ liệu giao dịch cho cơ quan thuế khi có yêu cầu) → dữ liệu ngân hàng có thể bị đối chiếu với hóa đơn (suy luận).
- **Áp dụng**: mọi cơ sở có thu không tiền mặt · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: NÊN (đối soát tự động); có phiếu thu cho mọi giao dịch là BẮT BUỘC (R02)
- **Phần mềm phải**: mỗi giao dịch ngân hàng ánh xạ 1–1 phiếu thu (mã tham chiếu trong nội dung chuyển khoản); xử lý thiếu, thừa, chuyển nhầm, hoàn tiền bằng hóa đơn điều chỉnh; báo cáo giao dịch ngân hàng chưa có phiếu thu.

### D. Bảo hiểm sức khỏe thương mại, bảo lãnh viện phí

### TC-MS-R27 — Chỉ gửi dữ liệu cho DNBH/TPA khi người bệnh yêu cầu bằng văn bản
- **Căn cứ**: Luật 91/2025 Đ26 k1 a; Đ26 k2: "không cung cấp dữ liệu cá nhân cho bên thứ ba là tổ chức cung cấp dịch vụ chăm sóc sức khỏe hoặc dịch vụ bảo hiểm sức khỏe, bảo hiểm nhân thọ, trừ trường hợp có yêu cầu bằng văn bản của chủ thể dữ liệu cá nhân" hoặc Đ19 k1; Đ26 k3. Luật 20/2023 Đ9 k1 (thông điệp dữ liệu đáp ứng yêu cầu văn bản nếu truy cập, sử dụng được để tham chiếu). Luật KDBH Đ20 k2 i, Đ11 k3. Chặn luồng xuất: DLCN-R09.
- **Áp dụng**: BV, PK có bảo lãnh viện phí; app kết nối DNBH · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: mẫu "Yêu cầu cung cấp thông tin cho DNBH" điện tử do người bệnh khởi tạo, ký (chữ ký điện tử, OTP gắn định danh), ghi DNBH/TPA nhận, đợt điều trị, loại tài liệu, thời hạn; lưu nguyên thông điệp dữ liệu; API sang DNBH kiểm tra yêu cầu còn hiệu lực trước mỗi lần gửi; chỉ gửi đúng phạm vi.
- **Bẫy**: điều khoản "ủy quyền cho DNBH thu thập hồ sơ y tế" trong hợp đồng bảo hiểm không chắc thay được yêu cầu gửi tới cơ sở KCB (cần luật sư).

### TC-MS-R28 — Toàn vẹn hồ sơ, hóa đơn dùng cho bồi thường bảo hiểm
- **Căn cứ**: Luật KDBH Đ9 k4 b: cấm "giả mạo tài liệu, cố ý làm sai lệch thông tin trong hồ sơ yêu cầu bồi thường, trả tiền bảo hiểm"; k4 a. NĐ 254 Đ3 k7 (hóa đơn không đúng giá trị thực tế, hóa đơn khống là sử dụng không hợp pháp). TT 91 Đ10 (R09).
- **Áp dụng**: mọi cơ sở phát hành chứng từ cho người bệnh đi bồi thường · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: không in lại hóa đơn, bảng kê, giấy ra viện với số liệu khác bản đã phát hành; bản in lại ghi "bản sao" và thời điểm in; chặn tách/gộp hóa đơn ngoài quy tắc R02; nhật ký mọi lần in, xuất chứng từ.

### TC-MS-R29 — Tách khoản phải thu theo bên trả
- **Căn cứ**: NĐ 254 Đ9 k4 m; Luật KCB Đ111 (quỹ hỗ trợ KCB); Luật KDBH Đ31 k1 (bồi thường trong thời hạn thỏa thuận, không có thì 15 ngày từ khi đủ hồ sơ).
- **Áp dụng**: BV, PK · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: NÊN
- **Phần mềm phải**: `payer` cho từng dòng chi phí; công nợ DNBH theo thư bảo lãnh, theo dõi hạn; người mua trên hóa đơn phần bảo lãnh cấu hình theo hướng dẫn thuế (mục 7); phần tự trả lập hóa đơn riêng.

### TC-MS-R30 — Người bệnh tự lấy gói chứng từ bồi thường
- **Căn cứ**: Luật KDBH Đ30 k1 (thời hạn nộp hồ sơ bồi thường 01 năm từ sự kiện bảo hiểm); Luật KCB Đ12 (sao chụp HSBA, tóm tắt HSBA, giải thích chi phí).
- **Áp dụng**: BV, PK · **Hiệu lực/hạn**: đang áp dụng
- **Mức**: NÊN
- **Phần mềm phải**: người bệnh tự tải gói chứng từ (hóa đơn, bảng kê, giấy ra viện, tóm tắt HSBA) qua cổng/app sau xác thực, ít nhất 01 năm sau ra viện; cung cấp cho chính chủ thể nên không vướng Luật 91 Đ26 k2.

### E. Đầu tư, mua sắm, thuê dịch vụ công nghệ số bằng NSNN

### TC-MS-R31 — Phân loại dịch vụ công nghệ số sẵn có / không sẵn có
- **Căn cứ**: NĐ 224 Đ3 k1 (sẵn có: nhà cung cấp phát triển, công bố, cung cấp rộng rãi; dùng theo điều kiện công bố), k2 (không sẵn có: xây theo yêu cầu riêng); Đ36 k1 (Chương VI áp cho dự án, nhiệm vụ có NSNN ≥30% hoặc lớn nhất), k4 (ưu tiên thuê dịch vụ sẵn có; không thuê dịch vụ để nâng cấp, mở rộng hệ thống đã đầu tư, mua sắm); Đ65 k1 b (thuê sẵn có: không lập dự án/kế hoạch thuê, thuê nhiều năm, giá theo báo giá); Đ65 k3, Đ67 (không sẵn có: lập, thẩm định ≤20 ngày làm việc, phê duyệt ≤03 ngày làm việc kế hoạch thuê); Đ38 (danh mục phần mềm phổ biến; nhà cung cấp công bố tên, giá, không nâng khống giá).
- **Áp dụng**: BV công dùng NSNN; vendor HIS/EMR/LIS/PACS SaaS · **Hiệu lực/hạn**: 01/07/2026 (dự án đã quyết định theo NĐ 45/2026 tiếp tục theo NĐ 45, Đ91 k2)
- **Mức**: BẮT BUỘC (bên dùng NSNN) / BẮT BUỘC? (vendor phải có tài liệu để bên mua chứng minh)
- **Phần mềm phải** (vendor): công bố gói dịch vụ, điều kiện sử dụng, bảng giá niêm yết (Đ67 k3 đ dùng giá niêm yết làm căn cứ dự toán); tách cấu hình (sẵn có) khỏi phát triển riêng (không sẵn có) trong báo giá; đa tenant, cấu hình không sửa mã nguồn.
- **Bẫy**: "thuê HIS" nhưng viết riêng cho một BV là dịch vụ không sẵn có → cần kế hoạch thuê theo Đ67; thuê để nâng cấp hệ thống đã mua bị cấm.

### TC-MS-R32 — Sở hữu, bàn giao toàn bộ dữ liệu khi hết thuê; xóa tại nhà cung cấp
- **Căn cứ**: NĐ 224 Đ57 k2 (hết thời gian thuê, nhà thầu bàn giao toàn bộ thông tin, dữ liệu hình thành cho chủ đầu tư); Đ67 k2 đ (kế hoạch thuê xác định sở hữu dữ liệu, phương án quản lý, chuyển giao), k7; Đ39 k4 b. TT 41 Đ15 k4 a (hợp đồng thống nhất phương pháp chuyển giao; thống kê, kiểm tra dữ liệu trước chuyển giao; sao lưu; đối soát sau chuyển giao; **xóa toàn bộ** dữ liệu tại hệ thống nhà cung cấp sau chuyển giao; cam kết sau chuyển giao), k4 b–c; Đ16 k2 c (biên bản bàn giao dữ liệu Mẫu số 4 PL VIII là tài liệu nghiệm thu). Bổ sung ANM-R22, ANM-R23.
- **Áp dụng**: vendor SaaS và BV công thuê bằng NSNN; BV tư, PK: NÊN (suy luận) · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: xuất toàn bộ dữ liệu tenant (CSDL, tệp, HSBA đã ký, XML HĐĐT, nhật ký) ở định dạng mở có từ điển dữ liệu; thống kê trước/sau (số bản ghi, checksum); xóa có biên bản (kể cả bản sao lưu theo vòng đời) chỉ sau khi bên thuê xác nhận đối soát; dữ liệu phải còn đủ thời hạn lưu HSBA phía bên thuê trước khi xóa phía vendor.

### TC-MS-R33 — SLA, giám sát, báo cáo kết quả cung cấp dịch vụ
- **Căn cứ**: TT 41 Đ14 k1 (6 nhóm tiêu chí: chức năng; hiệu năng; an ninh mạng, dữ liệu, DLCN; phi chức năng; hài lòng; quản lý dịch vụ); PL VI (truy xuất dữ liệu, hỗ trợ người khuyết tật, số lần gián đoạn, thời gian khôi phục, báo cáo dịch vụ, quản lý thay đổi, khôi phục dữ liệu); Đ15 k3 (bên thuê giám sát; nhà cung cấp báo cáo kết quả định kỳ, đột xuất); Đ16 (nghiệm thu dựa trên Mẫu 2, 3, 4 PL VIII). NĐ 224 Đ67 k6.
- **Áp dụng**: vendor cho thuê, BV công · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (khi thuê bằng NSNN)
- **Phần mềm phải**: đo, lưu uptime, sự cố, thời gian khôi phục, kết quả thử khôi phục, phiên bản triển khai; xuất báo cáo kỳ theo Mẫu 2 PL VIII (nội dung mẫu chưa đọc chi tiết); kênh phản hồi người dùng.

### TC-MS-R34 — Vận hành thử trước nghiệm thu
- **Căn cứ**: TT 41 Đ15 k1 (vận hành thử tại ít nhất một đơn vị thụ hưởng; biên bản Mẫu 1 PL VIII); NĐ 224 Đ67 k5, Đ65 k7 a.
- **Áp dụng**: BV công; vendor · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: tenant vận hành thử tách biệt nhưng cùng phiên bản chính thức; kịch bản kiểm thử nghiệp vụ (XML BHYT, HĐĐT, ký số) và báo cáo kết quả.

### TC-MS-R35 — Phần mềm nội bộ đặt hàng: bàn giao mã nguồn, tài liệu; bảo hành
- **Căn cứ**: NĐ 224 Đ57 k1 a–b (tài liệu kết nối; thiết kế, bộ cài, mã nguồn, hướng dẫn vận hành, đào tạo, bảo trì); Đ59 (bảo hành tối thiểu 24 tháng cho dự án quan trọng quốc gia, nhóm A, bảo lãnh 3%; 12 tháng cho nhóm B, C, bảo lãnh 5%; không áp cho thuê dịch vụ); Đ60 k3.
- **Áp dụng**: BV công đặt hàng phần mềm riêng bằng NSNN; vendor · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC
- **Phần mềm phải**: build tái lập từ mã nguồn bàn giao; danh mục thành phần bên thứ ba và giấy phép; tài liệu API kết nối.

### TC-MS-R36 — Nguyên tắc kiến trúc hệ thống số
- **Căn cứ**: Luật 148/2025 Đ7 (nền tảng dùng chung, cloud, chuẩn mở, API, an ninh từ thiết kế, dữ liệu làm trung tâm, mô-đun); k8 (CQNN có trách nhiệm tuân thủ, tổ chức khác được khuyến khích); Đ23 k3. NĐ 224 Đ23 k2 a (cloud xem xét đầu tiên), k2 b (thiết kế phần mềm không giới hạn theo quy mô người dùng), k3 b, k4 a, k5 a–b (mô hình thực thể dữ liệu; dữ liệu chủ chỉ lưu ở một hệ thống), k6 a–b (cho hủy bỏ thao tác; giao diện điều chỉnh cỡ), k7 a; Đ24 k1.
- **Áp dụng**: dự án CĐS của CQNN; BV công dùng NSNN qua Chương VI (suy luận); BV tư, PK · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC? (BV công là ĐVSNCL, không phải CQNN theo nghĩa hẹp) / NÊN (khu vực tư)
- **Phần mềm phải**: hồ sơ thiết kế có mô hình thực thể và bản đồ API; không khóa license theo số người dùng ở mức kỹ thuật; master data một nguồn chính; có hoàn tác cho thao tác nhập liệu khi an toàn.

### TC-MS-R37 — Yêu cầu tối thiểu với hệ thống số, nền tảng số phục vụ lợi ích công
- **Căn cứ**: Luật 148/2025 Đ8 k1 (bắt buộc cho hệ thống CQNN, hệ thống số phục vụ lợi ích công, dịch vụ số thiết yếu), k2–k5, k6 (nhật ký hoạt động, truy vết), k7 (tiếp cận tối thiểu cho người khuyết tật, người cao tuổi), k8. NĐ 224 Đ25 k2; Đ27 k1–2 (nền tảng số: áp cho nền tảng vận hành từ 01/07/2027; nền tảng vận hành trước đó đáp ứng không chậm hơn 31/12/2028); Đ26.
- **Áp dụng**: HIS BV công có thể là "hệ thống số phục vụ lợi ích công"; nền tảng đặt khám nhiều bên có thể là "nền tảng số" (suy luận) · **Hiệu lực/hạn**: 01/07/2026; 01/07/2027; 31/12/2028
- **Mức**: BẮT BUỘC? (định nghĩa "phục vụ lợi ích công" chưa có hướng dẫn BKHCN)
- **Phần mềm phải**: nhật ký hoạt động bất biến, truy vết được; RPO/RTO công bố; cổng người bệnh đạt tiếp cận tương đương WCAG (CHUYENKHOA-R38); kế hoạch nâng cấp trước 31/12/2028 nếu là nền tảng số.

### TC-MS-R38 — Hồ sơ hưởng ưu đãi sản phẩm, dịch vụ công nghệ số Việt Nam
- **Căn cứ**: TT 34/2025 Đ3 (doanh nghiệp VN có trụ sở tại VN hoặc cá nhân VN; cam kết hỗ trợ, bảo hành, nâng cấp), Đ5 k1–2 (thiết kế, mã nguồn thuộc tổ chức/cá nhân VN, hoặc phát triển trên mã nguồn mở được quyền khai thác; chứng minh bằng GCN quyền tác giả hoặc tài liệu khác), Đ6 k3 (cập nhật trên HTTT quốc gia về công nghiệp công nghệ số), Đ7.
- **Áp dụng**: vendor VN dự thầu gói NSNN · **Hiệu lực/hạn**: 01/01/2026
- **Mức**: NÊN (điều kiện hưởng ưu đãi)
- **Phần mềm phải**: SBOM và hồ sơ quyền tác giả theo phiên bản; tài liệu cam kết hậu mãi.

### TC-MS-R39 — Báo cáo hoàn thành và hiệu quả dự án, nhiệm vụ
- **Căn cứ**: NĐ 224 Đ68 k1 a (trong 20 ngày từ nghiệm thu hoặc đưa dịch vụ vào dùng, chủ đầu tư cung cấp thông tin hoàn thành), k2 a (tháng 01 hằng năm, thông tin đánh giá hiệu quả); Đ58.
- **Áp dụng**: BV công; vendor hỗ trợ · **Hiệu lực/hạn**: 01/07/2026
- **Mức**: BẮT BUỘC (nghĩa vụ BV công) / NÊN (chức năng phần mềm)
- **Phần mềm phải**: báo cáo số liệu khai thác theo năm (người dùng hoạt động, lượt KCB, tỷ lệ HSBA điện tử, số HĐĐT).

## 3. Pattern thiết kế

### TC-MS-P01 — Sổ phiếu thu là nguồn sự thật, hóa đơn là phép chiếu
- **Giải quyết**: R02, R03, R04, R05, R26
- **Cách làm**: mọi dòng tiền vào tạo `receipt` trước; HĐĐT sinh từ receipt theo quy tắc (cá nhân ngay, tổng hợp cuối ngày, BHXH khi quyết toán); không sinh hóa đơn trực tiếp từ dòng chi phí; job cuối ngày idempotent.
- **Gợi ý dữ liệu**: `receipt(facility_id, cashier_id, encounter_id, payer_type, amount, method, bank_ref, received_at, advance_type, status)`; `receipt_line(receipt_id, charge_line_id, amount)`; `invoice(seller_id, mode, template_no, series, number, kind IN ('INDIVIDUAL','DAILY_SUMMARY','BHXH_SETTLEMENT','ADJUST','REPLACE'), buyer_*, issued_at, signed_at, cqt_code, status)`; `invoice_receipt(invoice_id, receipt_id)` với `UNIQUE(receipt_id)` khi kind cá nhân/tổng hợp; chỉ mục `(facility_id, received_at::date) WHERE NOT invoiced`.
- **Đánh đổi**: hai lớp chứng từ tăng lưu trữ nhưng là điều kiện để dùng điểm m.

### TC-MS-P02 — Hóa đơn chỉ-thêm và chuỗi điều chỉnh
- **Giải quyết**: R09, R11, R28
- **Cách làm**: hóa đơn đã gửi cơ quan thuế bất biến; sửa = bản ghi mới ADJUST/REPLACE trỏ hóa đơn gốc, hoặc NOTICE (không đổi số tiền).
- **Gợi ý dữ liệu**: `invoice_correction(original_invoice_id, method IN ('NOTICE','ADJUST','REPLACE'), reason, agreement_doc_id, buyer_notice_ref)`; ràng buộc method mọi lần sửa cùng hóa đơn gốc = method lần đầu; `mode = CASH_REGISTER ⇒ method = REPLACE`; `xml_signed`, `xml_hash`, `cqt_response_xml` dạng WORM.
- **Đánh đổi**: báo cáo doanh thu phải cộng theo chuỗi.

### TC-MS-P03 — Outbox gửi HĐĐT có cửa sổ sự cố
- **Giải quyết**: R08, R10
- **Cách làm**: hóa đơn ký xong vào outbox; tính hạn theo lịch ngày làm việc; khi có sự cố thì tạm dừng đếm hạn và đặt hạn gửi bù 02/03 ngày làm việc sau khi đóng sự cố.
- **Gợi ý dữ liệu**: `invoice_outbox(invoice_id, attempt, last_error, due_at)`; `incident(source, started_at, ended_at, evidence_doc_id, tax_notice_ref)`; `workday_calendar`.
- **Đánh đổi**: phải cập nhật lịch nghỉ lễ hằng năm.

### TC-MS-P04 — Danh mục giá có nguồn pháp lý và phiên bản
- **Giải quyết**: R17, R18, R19, R21, R23
- **Cách làm**: bảng giá gắn văn bản phê duyệt; dòng chi phí chụp giá tại thời điểm thực hiện.
- **Gợi ý dữ liệu**: `price_list(facility_id, legal_source_type, legal_ref, effective_from, effective_to)`; `price_item(price_list_id, service_code, category, unit_price, bhyt_reference_price, published_at, declared_at)`; `charge_line(price_item_id, unit_price_snapshot, bhyt_price_snapshot, revenue_stream)`; không chồng lấn hiệu lực cho cùng (facility, service_code, category); `published_at ≤ service_date`.
- **Đánh đổi**: tư nhân BHYT phải nạp thêm bảng giá HĐND địa bàn.

### TC-MS-P05 — Tách bên trả và quy tắc mức hưởng tham số
- **Giải quyết**: R03, R18, R22, R29
- **Cách làm**: mỗi `charge_line` phân bổ thành nhiều `charge_allocation(payer_type, amount, rule_id)` theo `benefit_rule`; phần PATIENT thu tại quầy; BHXH chờ quyết toán; INSURER theo thư bảo lãnh.
- **Gợi ý dữ liệu**: `benefit_rule(group_code, benefit_code, rate, cap, effective_from, effective_to)`.
- **Đánh đổi**: thẻ BHYT đổi giữa đợt (BHYT-GD-R07, R08) phải tính lại cả phần đã thu → sinh điều chỉnh.

### TC-MS-P06 — Thanh toán thẳng vào tài khoản cơ sở (QR động)
- **Giải quyết**: R24, R25, R26
- **Cách làm**: HIS tạo `payment_intent` → QR mang tài khoản cơ sở và `ref_code` → ngân hàng/TGTT có phép gửi webhook hoặc HIS truy vấn sao kê bằng API của cơ sở → khớp `ref_code` → chốt receipt.
- **Gợi ý dữ liệu**: `payment_intent(receipt_draft_id, amount, ref_code)`; `bank_txn(bank_ref UNIQUE, amount, ref_code, matched_receipt_id)`; khóa API trong kho bí mật của tenant.
- **Đánh đổi**: vendor không gộp được phí thu hộ; đổi lại tránh vùng giấy phép TGTT.

### TC-MS-P07 — Cổng dữ liệu bảo hiểm có "yêu cầu bằng văn bản"
- **Giải quyết**: R27, R28, R30 (cùng DLCN-R09)
- **Cách làm**: API outbound kiểm tra yêu cầu hợp lệ cho từng tài liệu; chỉ gửi bản đã phát hành (hash khớp).
- **Gợi ý dữ liệu**: `insurer_disclosure_request(patient_id, insurer_id, scope, valid_until, signed_payload, signature_method, revoked_at)`; `disclosure_log(request_id, doc_id, doc_hash, sent_at, endpoint)`.
- **Đánh đổi**: thêm một bước cho người bệnh; nên cho khởi tạo trên app trước khi nhập viện.

### TC-MS-P08 — Bộ "rời đi" (exit kit) của tenant
- **Giải quyết**: R32, R11 (cùng ANM-R22, R23)
- **Cách làm**: lệnh xuất toàn bộ dữ liệu tenant (CSV/Parquet + DDL, tệp HSBA PDF/A đã ký, XML HĐĐT, XML BHYT, nhật ký) kèm `manifest.json` (bảng, số bản ghi, checksum) và từ điển dữ liệu; biên bản đối soát hai bên (Mẫu 4 PL VIII TT 41) rồi mới chạy `tenant_purge` có biên bản.
- **Gợi ý dữ liệu**: `export_job(tenant_id, manifest_hash, completed_at)`; `purge_job(tenant_id, approved_by_customer_at, executed_at, report_id)`.
- **Đánh đổi**: phải duy trì từ điển dữ liệu theo phiên bản; làm từ đầu rẻ hơn làm lúc hết hợp đồng.

### TC-MS-P09 — Đo SLA và báo cáo dịch vụ định kỳ
- **Giải quyết**: R16, R33, R34, R37, R39
- **Cách làm**: giám sát độc lập hệ thống chính; báo cáo kỳ tự sinh: uptime, số gián đoạn, MTBF, thời gian khôi phục, thử khôi phục, thay đổi, số liệu khai thác.
- **Gợi ý dữ liệu**: `sla_probe(ts, service, status, latency)`; `incident` (dùng chung P03); `restore_test(ts, backup_id, rto, rpo, result)`; `release(version, deployed_at, change_ticket)`.
- **Đánh đổi**: thêm hạ tầng giám sát.

### TC-MS-P10 — Biên lai và hóa đơn tích hợp cho đơn vị thu phí, lệ phí
- **Giải quyết**: R14
- **Cách làm**: chuỗi số biên lai reset 01/01; hóa đơn tích hợp khi cùng giao dịch; job gửi Mẫu 01/TH-BLĐT trong ngày.
- **Gợi ý dữ liệu**: `fee_receipt(series_year, number ≤ 99999999, fee_type, amount, payer, signed_at)`; `invoice.kind = INTEGRATED_FEE` (ký hiệu mẫu 8/9).
- **Đánh đổi**: hai loại chứng từ song song trong một quầy.

## 4. Checklist audit

| ID | Yêu cầu | Cách kiểm tra | Bằng chứng | Mức |
|---|---|---|---|---|
| TC-MS-A01 | R01 | Cấu hình chế độ hóa đơn và căn cứ; BV công dùng không mã thì hỏi văn bản chấp thuận | Ảnh cấu hình, thông báo chấp nhận | BẮT BUỘC |
| TC-MS-A02 | R02 | Một ngày: tổng phiếu thu so với hóa đơn cá nhân + tổng hợp; phiếu thu không gắn hóa đơn | SQL, hóa đơn tổng hợp | BẮT BUỘC |
| TC-MS-A03 | R02 | Log job cuối ngày 30 ngày; ngày có phiếu thu mà không có hóa đơn tổng hợp | Log, danh sách ngày | BẮT BUỘC |
| TC-MS-A04 | R03 | Hóa đơn cho BHXH so với Biên bản quyết toán 06/BH quý gần nhất | Biên bản, hóa đơn | BẮT BUỘC |
| TC-MS-A05 | R04 | Ca nội trú có tạm ứng: thời điểm lập hóa đơn, xử lý hoàn ứng | Phiếu thu, hóa đơn | BẮT BUỘC? |
| TC-MS-A06 | R05 | XML hóa đơn tổng hợp có "kèm theo bảng kê số…"; bảng kê đủ chỉ tiêu; người mua trống ghi "Bán cho người tiêu dùng" | XML, bảng kê | BẮT BUỘC |
| TC-MS-A07 | R06 | Nhà thuốc: ký hiệu "M", QR tra cứu, gửi cuối ngày; thử sửa → chỉ thay thế | Ảnh hóa đơn, log | BẮT BUỘC |
| TC-MS-A08 | R07 | Ký hiệu năm 2026 dạng "1C26T.."/"2K26T.."; không trùng số | Danh sách ký hiệu | BẮT BUỘC |
| TC-MS-A09 | R08 | Hóa đơn không mã gửi muộn hơn ngày làm việc tiếp theo; độ trễ gửi người mua sau khi có mã | Truy vấn, log | BẮT BUỘC |
| TC-MS-A10 | R08 | Tra cứu hóa đơn bằng mã trên phiếu thu; website công khai cách tra cứu | Ảnh | BẮT BUỘC |
| TC-MS-A11 | R09 | Thử "hủy" hóa đơn đã gửi; thử điều chỉnh rồi chọn thay thế cùng hóa đơn gốc | Kết quả thử | BẮT BUỘC |
| TC-MS-A12 | R09 | Hóa đơn điều chỉnh cho người mua cá nhân có bằng chứng thông báo | Bằng chứng | BẮT BUỘC |
| TC-MS-A13 | R10 | Sổ sự cố HĐĐT; hóa đơn gửi bù trong hạn 02/03 ngày làm việc | Sổ, log | BẮT BUỘC |
| TC-MS-A14 | R11 | 5 hóa đơn 2026: XML gốc đã ký, mã cơ quan thuế, hash khớp; in bản chuyển đổi | File, bản in | BẮT BUỘC |
| TC-MS-A15 | R12 | Hợp đồng ủy nhiệm đủ nội dung TT 91 Đ9 k2; Mẫu 01/ĐKTĐ-HĐĐT; hóa đơn ghi hai bên | Hợp đồng, mẫu | BẮT BUỘC |
| TC-MS-A16 | R13 | Vendor tự phát hành có tên trên trang Cục Thuế; có nhật ký truyền nhận | Ảnh, log | BẮT BUỘC? |
| TC-MS-A17 | R14 | Còn in biên lai giấy; kế hoạch chuyển trước 31/12/2026; số reset 01/01 | Mẫu, kế hoạch | BẮT BUỘC |
| TC-MS-A18 | R15 | Chứng từ khấu trừ TNCN điện tử gửi cơ quan thuế trong ngày | Chứng từ, log | BẮT BUỘC |
| TC-MS-A19 | R16 | Ngày lập hóa đơn vendor so với kỳ đối soát (≤ ngày 07 tháng sau) | Hóa đơn, biên bản | BẮT BUỘC |
| TC-MS-A20 | R17 | Mỗi dòng giá có loại, văn bản, ngày hiệu lực; còn sót bảng giá TT 22/2023 | Xuất bảng giá | BẮT BUỘC |
| TC-MS-A21 | R18 | Ca dịch vụ theo yêu cầu cho người có thẻ: chênh lệch đúng; PK tư dùng giá HĐND địa bàn | Bảng chi phí, NQ HĐND | BẮT BUỘC |
| TC-MS-A22 | R19 | Chỉ định/thu dịch vụ chưa niêm yết | Kết quả thử | BẮT BUỘC |
| TC-MS-A23 | R20 | Bảng chi phí lũy kế giữa đợt nội trú tại quầy và trên app | Bản in, ảnh | BẮT BUỘC |
| TC-MS-A24 | R21 | Dòng thu không gắn mã dịch vụ; sửa đơn giá sau chốt không phê duyệt | Truy vấn, log | BẮT BUỘC |
| TC-MS-A25 | R22 | Ca ≥75 tuổi/cận nghèo năm 2026: hưởng 100%, không sinh phiếu thu | XML1, phiếu thu | BẮT BUỘC? |
| TC-MS-A26 | R23 | Báo cáo doanh thu tách dịch vụ theo yêu cầu; tỷ lệ giường | Báo cáo | BẮT BUỘC |
| TC-MS-A27 | R25 | Lần theo dòng tiền QR: tiền vào tài khoản ai; vendor có tài khoản trung gian | Sao kê, hợp đồng | BẮT BUỘC |
| TC-MS-A28 | R26 | Đối chiếu một ngày giao dịch ngân hàng với phiếu thu | Sao kê, truy vấn | NÊN |
| TC-MS-A29 | R27 | 10 hồ sơ bảo lãnh: truy ra yêu cầu của người bệnh đúng phạm vi, còn hạn (cùng DLCN-A10) | Yêu cầu đã ký, log | BẮT BUỘC |
| TC-MS-A30 | R28 | In lại chứng từ đã phát hành có nhãn "bản sao", số liệu không đổi | Kết quả thử, log in | BẮT BUỘC |
| TC-MS-A31 | R29 | Ca bảo lãnh: tách công nợ DNBH, hóa đơn phần bảo lãnh và tự trả | Công nợ, hóa đơn | NÊN |
| TC-MS-A32 | R31 | Hợp đồng thuê HIS bằng NSNN: phân loại sẵn có; kế hoạch thuê được duyệt; có hạng mục thuê để nâng cấp | Hợp đồng, QĐ | BẮT BUỘC |
| TC-MS-A33 | R32 | Điều khoản sở hữu, chuyển giao dữ liệu theo TT 41 Đ15 k4 a; chạy thử xuất toàn bộ dữ liệu | Hợp đồng, gói xuất | BẮT BUỘC |
| TC-MS-A34 | R33 | Báo cáo dịch vụ kỳ gần nhất có uptime, sự cố, khôi phục, thử sao lưu | Báo cáo Mẫu 2 | BẮT BUỘC |
| TC-MS-A35 | R34 | Biên bản vận hành thử trước nghiệm thu | Mẫu 1 PL VIII | BẮT BUỘC |
| TC-MS-A36 | R35 | Đã nhận mã nguồn, build lại được; bảo lãnh bảo hành | Biên bản, kết quả build | BẮT BUỘC |
| TC-MS-A37 | R36 | Hồ sơ thiết kế có mô hình thực thể, danh mục API; license giới hạn kỹ thuật số user | Tài liệu | BẮT BUỘC? |
| TC-MS-A38 | R37 | Quản trị viên sửa/xóa được nhật ký không; cổng người bệnh hỗ trợ trình đọc màn hình | Kết quả thử | BẮT BUỘC? |
| TC-MS-A39 | R38 | GCN quyền tác giả, thông tin trên HTTT quốc gia về công nghiệp công nghệ số | Giấy tờ | NÊN |
| TC-MS-A40 | R39 | BV gửi thông tin hoàn thành trong 20 ngày, báo cáo hiệu quả tháng 01 | Văn bản | BẮT BUỘC |

## 5. Mốc thời gian

| Ngày | Sự kiện | Ai phải làm | Đã qua/sắp tới |
|---|---|---|---|
| 01/01/2023 | Luật KDBH 08/2022 HL | DNBH; cơ sở có bảo lãnh viện phí | Đã qua |
| 01/01/2024 | Luật KCB (Đ12, Đ60 k4, Đ110); NĐ 96 Đ119 | Mọi cơ sở KCB | Đã qua |
| 01/07/2024 | NĐ 52/2024 HL | Vendor tích hợp thanh toán | Đã qua |
| 17/10/2024 | TT 21/2024/TT-BYT HL | BV công | Đã qua |
| 01/01/2025 | TT 13, 21, 22/2023/TT-BYT hết HL (hết bảng giá thống nhất) | Vendor gỡ bảng giá cài sẵn | Đã qua |
| 01/01/2026 | Luật 91/2025 (Đ26); NQ 261 mức hưởng 100%; TT 34/2025 (TT 40/2020 hết HL) | Cơ sở KCB; vendor | Đã qua |
| 16/01/2026 | NĐ 310/2025 sửa NĐ 125/2020 (khung phạt hóa đơn) | Mọi người bán | Đã qua |
| 01/03/2026 | NĐ 45/2026 thay NĐ 73/2019, NĐ 82/2024; NQ 04/2025/NQ-CP hết HL | BV công có dự án CNTT | Đã qua |
| 01/07/2026 | NĐ 254 + TT 91 (NĐ 123/2020, NĐ 70/2025, TT 32/2025 hết HL); Luật 148 + NĐ 224 (NĐ 45/2026 hết HL; Luật CNTT hết HL); TT 39/2026 (thay TT 18/2024); TT 41/2026 (thay TT 16/2024) | Mọi người bán; BV công; vendor | Đã qua |
| 21/07/2026 | NĐ 291/2026 sửa NĐ 125/2020 (chỉ trao đổi thông tin thuế) | — | Đã qua |
| 31/12/2026 | Hết dùng biên lai giấy (NĐ 254 Đ44 k2) | Đơn vị y tế công thu phí, lệ phí | Sắp tới |
| 01/01/2027 | Tiêu hủy biên lai giấy chưa dùng; bắt buộc biên lai điện tử | Như trên | Sắp tới |
| tháng 01/2027 | Báo cáo hiệu quả dự án, nhiệm vụ CĐS hằng năm (NĐ 224 Đ68 k2 a) | BV công | Sắp tới |
| 01/07/2027 | Yêu cầu tối thiểu với nền tảng số mới vận hành (NĐ 224 Đ27 k2) | Chủ quản nền tảng số phục vụ lợi ích công | Sắp tới |
| 31/12/2028 | Nền tảng số vận hành trước 01/07/2027 phải đáp ứng | Như trên | Sắp tới |
| 01/01/2030 | Miễn viện phí mức cơ bản theo lộ trình (NQ 261, thứ cấp) | Cơ sở KCB BHYT; vendor HIS | Sắp tới |

## 6. Bẫy trích dẫn và chuỗi thay thế

| Cũ | Mới | Từ ngày | Căn cứ |
|---|---|---|---|
| NĐ 123/2020, Đ1 NĐ 41/2022, NĐ 70/2025 | NĐ 254/2026 | 01/07/2026 | NĐ 254 Đ43 k2 |
| TT 32/2025/TT-BTC | TT 91/2026/TT-BTC | 01/07/2026 | TT 91 Đ25 k2 |
| NĐ 125/2020 | sửa bởi NĐ 102/2021 → NĐ 310/2025 (16/01/2026) → NĐ 291/2026 (21/07/2026) | — | — |
| TT 13, 21, 22/2023/TT-BYT (giá) | hết HL, không có bảng giá thống nhất mới | 01/01/2025 | TT 21/2024 Đ11 k2 |
| NĐ 73/2019 + NĐ 82/2024 (+ NQ 04/2025/NQ-CP) | NĐ 45/2026 | 01/03/2026 | NĐ 45 Đ41 k1–3 |
| NĐ 45/2026, NĐ 42/2022, NĐ 64/2007 | NĐ 224/2026 | 01/07/2026 | NĐ 224 Đ90 k2; chuyển tiếp Đ91 |
| TT 18/2024/TT-BTTTT (chi phí) | TT 39/2026/TT-BKHCN | 01/07/2026 | TT 39 Đ10 k2, k4 |
| TT 16/2024/TT-BTTTT (triển khai, nghiệm thu, thuê) | TT 41/2026/TT-BKHCN | 01/07/2026 | TT 41 Đ20 k2, k4 |
| TT 40/2020/TT-BTTTT | TT 34/2025/TT-BKHCN | 01/01/2026 | TT 34 Đ8 k2 |
| Luật CNTT 67/2006 | Luật Chuyển đổi số 148/2025 | 01/07/2026 | Luật 148 Đ47 k2, Đ48 |
| QĐ 1813/QĐ-TTg | đề án kế nhiệm chưa xác minh | — | CĐ 124 mục 3 a |

**Bẫy trích dẫn**
1. "Điểm m NĐ 70/2025" → nay là **NĐ 254 Đ9 k4 m**. TT 12/2026/TT-BTC Đ14 k6 vẫn dẫn NĐ 123/NĐ 70 (xem BHYT-GD).
2. "Hủy hóa đơn điện tử" không còn là cách xử lý hóa đơn sai trong TT 91 Đ10. Chữ "hủy" chỉ còn ở trách nhiệm bên nhận ủy nhiệm (NĐ 254 Đ19 k1 e) và tiêu hủy hóa đơn hết hạn lưu (Đ3 k8).
3. "Luật KCB Đ110–112 về giá": chỉ **Đ110** là giá (gồm giá theo yêu cầu ở k7–k8). Đ111 là Quỹ hỗ trợ KCB; Đ112 là HTTT quản lý KCB. Niêm yết giá là **Đ60 k4**.
4. "Biên lai viện phí": viện phí BV công là giá dịch vụ (suy luận: không phải phí, lệ phí) → hóa đơn, không biên lai. Mốc 31/12/2026 chỉ cho phí, lệ phí.
5. **"NĐ 224/2026 thay NĐ 73/2019" là sai**: NĐ 73 bị NĐ 45/2026 thay từ 01/03/2026; NĐ 224 thay NĐ 45. Dự án quyết định theo NĐ 45 trước 01/07/2026 vẫn theo NĐ 45.
6. "Bảng giá BHYT theo hạng bệnh viện (TT 22/2023)" hết HL 01/01/2025; đừng trích mức giá khám cũ làm giá hiện hành.
7. "Máy tính tiền bắt buộc cho phòng khám": NĐ 254 Đ6 k1 c không liệt kê dịch vụ y tế; PK là HKD chỉ chịu Đ6 k1 d. Nhà thuốc bán lẻ mới thuộc Đ6 k1 c.
8. "Thuê dịch vụ CNTT" (NĐ 73, TT 16/2024) → nay là "thuê dịch vụ công nghệ số" sẵn có/không sẵn có (NĐ 224 Đ3 k1–2).
9. TT 39/2026 làm TT 18/2024 hết HL (trừ dự án chuyển tiếp).
10. NĐ 291/2026 không sửa điều phạt hóa đơn; khung phạt hiện hành ở NĐ 125 Đ24 theo NĐ 310/2025.

## 7. Chưa xác minh / cần hỏi luật sư hoặc cơ quan

**Hỏi cơ quan thuế (Cục Thuế, Bộ Tài chính) bằng văn bản**
1. Tạm ứng viện phí là "thu tiền trước" (lập hóa đơn khi thu, NĐ 254 Đ9 k2) hay "đặt cọc" (không lập)? Phần mềm để hai chế độ cấu hình được (R04).
2. BV công (ĐVSNCL) dùng HĐĐT có mã hay được dùng không mã (Đ6 k1 b chỉ nói "doanh nghiệp")?
3. HKD doanh thu ≤ 1 tỷ (nhà thuốc, PK nhỏ) có bắt buộc HĐĐT không: Đ6 k1 a và Đ6 k1 d đọc cùng nhau chưa nhất quán.
4. Người mua ghi trên hóa đơn khi DNBH bảo lãnh viện phí (người bệnh hay DNBH); hóa đơn khi doanh nghiệp trả tiền KSK cho nhân viên.
5. Thuế GTGT với dịch vụ y tế và loại hóa đơn (GTGT ghi KCT hay hóa đơn bán hàng) theo phương pháp tính thuế của cơ sở (Luật 48/2024 chưa đọc gốc).
6. Danh mục khoản phí, lệ phí đơn vị y tế công thu (ai chịu biên lai điện tử): đọc Luật Phí và lệ phí 2015, NĐ 362/2025.
7. Thời hạn lưu HĐĐT: NĐ 174/2016 Đ12–13 (5/10 năm) mới đọc thứ cấp; kiểm Luật Kế toán và nghị định hiện hành.
8. Khung phạt NĐ 125 Đ24 (sửa bởi NĐ 310) áp cho cá nhân hay tổ chức (NĐ 125 Đ7 chưa đọc).
9. TT 94/2026/TT-BTC (tiêu chí rủi ro cao về hóa đơn) chưa đọc.

**Hỏi Ngân hàng Nhà nước hoặc luật sư về thanh toán**
10. Vendor dùng QR, tài khoản ảo, đối soát thay bệnh viện có rơi vào "dịch vụ hỗ trợ thu hộ, chi hộ" hoặc "cổng thanh toán điện tử" (NĐ 52 Đ3 k17–18) không. TT 15/2024/TT-NHNN và các TT sửa 30/2025, 21/2026, tiêu chuẩn QR của NHNN chưa đọc.
11. Đề án TTKDTM kế nhiệm QĐ 1813 và mục tiêu không tiền mặt trong y tế; căn cứ pháp lý của "Cổng bảo lãnh thanh toán viện phí" (chỉ có nguồn báo).

**Hỏi Bộ KH&CN**
12. "Hệ thống số phục vụ lợi ích công" (Luật 148 Đ8 k1; NĐ 224 Đ27) có gồm HIS của BV công, BV tư có BHYT không; hướng dẫn yêu cầu tối thiểu (NĐ 224 Đ27 k3) đã ban hành chưa.
13. Danh mục phần mềm phổ biến ngành y tế (NĐ 224 Đ38 k2 a) đã công bố chưa. Nội dung Mẫu 1–5 PL VIII và PL VI đầy đủ của TT 41 chưa đọc chi tiết.

**Hỏi BYT hoặc kiểm tra thêm văn bản**
14. NQ 261/2025 bản gốc, nhóm hưởng 100% chính xác, văn bản hướng dẫn; định nghĩa "miễn viện phí ở mức cơ bản".
15. Quy tắc áp giá khi giá đổi giữa đợt điều trị sau khi TT 22/2023 hết HL (có thể trong từng QĐ/NQ giá hoặc NĐ 188/2025).
16. NĐ 96/2023 có bị sửa, thay trong 2025–2026 không; Đ119 trích theo bản 2023.
17. Luật Giá 16/2023, NĐ 85/2024 (sửa bởi NĐ 128/2026), NĐ 87/2024: nội dung hồ sơ kê khai giá dịch vụ KCB chưa rõ. NĐ 104/2026/NĐ-CP (chi thường xuyên) chưa đọc.

**Cần luật sư**
18. NĐ 224 Chương VI có áp cho BV công tự chủ chi từ nguồn thu sự nghiệp không (Đ36 k1 chỉ nói NSNN ≥30% hoặc lớn nhất); quan hệ với Luật Đấu thầu.
19. Điều khoản bên mua bảo hiểm ủy quyền cho DNBH thu thập hồ sơ y tế có thay "yêu cầu bằng văn bản của chủ thể" (Luật 91 Đ26 k2) khi DNBH trực tiếp đề nghị cơ sở KCB không; mặc định phần mềm đòi yêu cầu từ chính người bệnh (R27).
