# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhân viên nhóm can thiệp được mở bằng trợ lý | Số `agent_suggestion_shown` theo `staff_id` nhóm can thiệp, chia số `refund_request_created` giao cho nhóm đó | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra; ngưỡng 1% | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Đợt chạy thử không có nhóm đối chứng, nên con số này chưa cho biết tác động của trợ lý so với mức 0,70 khi chỉ có nhân viên.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi lệnh hoàn vào sổ cái |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `refund_request_created` (mẫu số), `ticket_closed` (đóng trong 24 giờ), `ticket_reopened` (mở lại trong 7 ngày).
- Dùng (bỏ qua gợi ý): `staff_review_decision` với quyet_dinh là sua hoặc bo, chia tổng `staff_review_decision`.
- An toàn (lỗi lọt đến khách): `ticket_reopened` trong 7 ngày, chia `refund_request_created`.
- Dùng (tự đề xuất): `agent_suggestion_shown` theo staff_id, chia `refund_request_created` có arm là nhóm can thiệp.
- An toàn (tự đề xuất): `audit_sample_checked` có so_tien_da_hoan khác so_tien_dung.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.414 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] | % yêu cầu được xem lại vẫn > 50% ở cuối tuần 4 | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
