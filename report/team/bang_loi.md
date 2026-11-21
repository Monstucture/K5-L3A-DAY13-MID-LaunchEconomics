# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Long · Người gắn nhãn 2: ... (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Hệ thống | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Ngữ cảnh | ... | ... | ... |
| 10 | Giới hạn hệ thống | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Giới hạn hệ thống | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `bank_transfer_rejected` có `reason = sai_so_tai_khoan`, theo `trace_id`; cảnh báo khi quá 1% số lệnh hoàn/ngày | Kiểm tra độ dài và định dạng số tài khoản theo ngân hàng trước khi tạo lệnh; sai thì hỏi lại khách, đọc lại 4 số cuối để khách xác nhận | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: hai bản ghi hoàn tiền cùng `ma_don` trong sổ cái; ngưỡng 0 ca | Thêm khoá chống trùng theo `ma_don` cho lệnh hoàn; yêu cầu gửi lại trong lúc đang xử lý thì trả trạng thái "đang xử lý", không tạo lệnh mới | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo tuần: tỉ lệ `mo_lai_trong_7_ngay` vì lý do "số tiền" mà nhân viên kiểm tra thấy tính đúng; ngưỡng 3% số yêu cầu đã hoàn | Mẫu tin nhắn luôn ghi cách tính, ví dụ "phí giao 30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ" | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` có `reason = ngoai_12_thang`, đếm theo tuần và theo loại yêu cầu | Giữ cách nói rõ giới hạn và chuyển nhân viên kèm tóm tắt; kiểm tra tuổi đơn ngay ở bước đầu để chuyển sớm, không gọi tool thừa | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra mẫu 100 đơn có mã giảm giá mỗi tuần: so số tiền hoàn với số khách thực trả; ngưỡng 1% đơn lệch. Thêm event `refund_gt_paid` khi số hoàn lớn hơn số đã trả | Tính hoàn dựa trên số tiền sau giảm từ sổ cái, không dùng giá niêm yết; chặn lệnh khi số hoàn lớn hơn số đã trả và chuyển nhân viên | Kế toán trưởng |
