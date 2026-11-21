# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Long · Người gắn nhãn 2: thành viên 3 (GitHub CTNone) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Hệ thống | Ngầm | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Ngữ cảnh | Không | Giới hạn hệ thống |
| 5 | Ngầm | Giới hạn hệ thống | Không | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Ngữ cảnh | Giới hạn hệ thống | Không | Do người dùng |
| 10 | Giới hạn hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Hệ thống | Không | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Hệ thống | Không | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Giới hạn hệ thống | Do người dùng | Không | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 12 / 20 = 60%. Dưới 80%, nên nhóm đã viết lại định nghĩa bên dưới.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

**Định nghĩa viết lại (hỏi theo thứ tự, dừng ở câu đầu tiên trả lời "có"):**

1. Đầu vào của khách sai (nhập sai, chọn sai mục, bấm nhầm)? → **Do người dùng**, kể cả khi trợ lý lẽ ra nên gợi ý.
2. Việc nằm ngoài khả năng hoặc phạm vi (thiếu dữ liệu, ngoài phạm vi, dạng đầu vào không xử lý được)? → **Giới hạn hệ thống**.
3. Trợ lý làm đúng thiết kế và chính sách, chỉ giả định không khớp hoàn cảnh khách? → **Ngữ cảnh**.
4. Trợ lý làm sai thiết kế hoặc chính sách, và đã có người thấy (khách, nhân viên, ngân hàng)? → **Hệ thống**.
5. Có sai (về tiền hoặc chi phí) nhưng không ai thấy cho tới khi kiểm tra mẫu? → **Ngầm**.

**Từng ca không trùng:**

- Ca 3 → Ngữ cảnh: hoàn về ví đúng thiết kế, chỉ giả định "khách biết tiền về ví" không khớp; không phải Hệ thống vì không vi phạm gì, không phải Ngầm vì khách đã báo.
- Ca 5 → Ngầm: hoàn thừa tiền, không khách nào báo, chỉ lộ ra khi kiểm tra mẫu; không phải Giới hạn vì trợ lý có dữ liệu giá sau giảm.
- Ca 9 → Do người dùng: gốc lỗi là khách nhập mã sàn TMĐT; việc trợ lý không gợi ý ghi ở cột khắc phục.
- Ca 10 → Ngữ cảnh: từ chối đúng chính sách bất khả kháng, chỉ lời hứa "giao 24 giờ" trên app không khớp hoàn cảnh bão.
- Ca 12 → Ngầm: kết quả đúng nhưng chi phí token gấp 3 lần suốt 3 tuần mà không ai thấy; "sai" có thể là sai về chi phí.
- Ca 14 → Do người dùng: khách bấm nhầm nút xác nhận; hệ thống làm đúng theo thao tác của khách.
- Ca 16 → Ngữ cảnh: gửi ngay khi xong là đúng thiết kế, chỉ giả định "giờ nào gửi cũng được" không khớp lúc 2 giờ sáng.
- Ca 4 → Giới hạn hệ thống: LogiX không có dữ liệu chặng do hãng nước ngoài giao, nên dù cố gắng cũng không trả lời được; không phải Ngữ cảnh vì không có kết quả nào được đưa ra.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_transfer_rejected` có `reason = sai_so_tai_khoan`, theo `trace_id`; cảnh báo khi quá 1% số lệnh hoàn/ngày | Kiểm tra độ dài và định dạng số tài khoản theo ngân hàng trước khi tạo lệnh; sai thì hỏi lại khách, đọc lại 4 số cuối để khách xác nhận |  Người gắn nhãn 1 |
| 20 | Hệ thống | Đối soát mỗi giờ: hai bản ghi hoàn tiền cùng `ma_don` trong sổ cái; ngưỡng 0 ca | Thêm khoá chống trùng theo `ma_don` cho lệnh hoàn; yêu cầu gửi lại trong lúc đang xử lý thì trả trạng thái "đang xử lý", không tạo lệnh mới |  Người viết code |
| 18 | Ngữ cảnh | Theo tuần: tỉ lệ `mo_lai_trong_7_ngay` vì lý do "số tiền" mà nhân viên kiểm tra thấy tính đúng; ngưỡng 3% số yêu cầu đã hoàn | Mẫu tin nhắn luôn ghi cách tính, ví dụ "phí giao 30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ" |  Người gắn nhãn 2 |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` có `reason = ngoai_12_thang`, đếm theo tuần và theo loại yêu cầu | Giữ cách nói rõ giới hạn và chuyển nhân viên kèm tóm tắt; kiểm tra tuổi đơn ngay ở bước đầu để chuyển sớm, không gọi tool thừa |  Team lead |
| 5 | Ngầm | Kiểm tra mẫu 100 đơn có mã giảm giá mỗi tuần: so số tiền hoàn với số khách thực trả; ngưỡng 1% đơn lệch. Thêm event `refund_gt_paid` khi số hoàn lớn hơn số đã trả | Tính hoàn dựa trên số tiền sau giảm từ sổ cái, không dùng giá niêm yết; chặn lệnh khi số hoàn lớn hơn số đã trả và chuyển nhân viên |  Người kiểm số |
