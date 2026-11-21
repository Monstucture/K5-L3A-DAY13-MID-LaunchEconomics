# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: MID · Lớp: L3A · Phạm vi pilot đề xuất: `noi_dia` + `hang_nang`

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ**, gấp 16,3× hoá đơn token (275 đ). Trong phạm vi pilot, cộng chi phí cố định: 4.599 đ [simulated] | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | Gấp đôi: **làm lại +51,8%** · xem lại +40,7% · lương (+25%) +23,1%. Token chỉ +5,6% [simulated] | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | **0,49×** của 12.000 đ (cả hệ thống). Bất lợi: xem lại 100% thì 0,98×–1,03×; `quoc_te` 1,88× nên loại [simulated] | Giả lập | Người kiểm số |
| 4 · Ba chỉ số | Trong đợt chạy thử: chính **82,83%** · bỏ qua gợi ý 27,12% · mở lại 7 ngày 4,25%. Chưa có đối chứng | Xong, có bằng chứng | Người gán nhãn |
| 5 · Bảng lỗi | 20 ca, đủ 5 loại. Đồng thuận: chờ bộ nhãn 2. Sửa trước pilot: ca 7, 20 (hoàn sai/trùng), ca 5, 17 (lỗi ngầm) | Chưa | Người gán nhãn |
| 6 · Pilot plan | Chia theo nhân viên **20 + 20**, ngẫu nhiên. Đủ mẫu cho mức chênh 6 điểm (859/nhóm). Bất lợi: power 0,64 nếu chênh thật chỉ 5 điểm | Chưa | Team lead |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ · xem lại 100%: 0,98×–1,03× · khối lượng còn nửa: 0,48× [simulated] | Giả lập | Người kiểm số |

**Đề xuất: Go có điều kiện.** Kiểm tra trước ngày bắt đầu pilot, trừ khi ghi khác:

1. Khoá chống trùng + đối soát sổ cái mỗi giờ, 0 ca hoàn hai lần. *Kỹ sư trưởng agent*
2. Ký chấp nhận mức chênh 6 điểm, power 0,64. *Giám đốc vận hành*
3. Bật đủ event có `trace_id`; thay phút simulated bằng phút đo thật, cuối tuần 1. *PM trợ lý hoàn phí*
4. Giảm xem lại theo bậc khi sửa + bỏ < 15%, kiểm tra cuối bước 0.25. *Trưởng nhóm CSKH*
5. Kiểm tra mẫu 100 đơn/tuần, ngưỡng 1% đơn hoàn lệch. *Kế toán trưởng*
