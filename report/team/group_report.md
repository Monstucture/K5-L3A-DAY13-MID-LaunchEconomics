# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: MID
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu hỏi cho Gate 2a: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra được quyết định. Nhóm tính mọi số bằng `src/lab13.py` trên mẫu 1.200 yêu cầu (1.624 lần chạy), đối chiếu với hướng dẫn chi tiết, rồi ghép vào một trang hồ sơ.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): tử số cộng token + tool của mọi lần chạy kể cả lỗi, cộng giờ xem lại và làm lại; mẫu số chỉ đếm việc thành công. Tách theo loại và cộng chi phí cố định 40 triệu đ/tháng.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): 9 kịch bản đổi từng yếu tố, một cặp, giới hạn chạy lại 1–3 lần, xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo 5 loại PAIR, viết lại định nghĩa vì đồng thuận dưới 80%, bảng khắc phục 5 ca.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu cho 3 cách chia rồi chọn chia theo nhân viên 20 + 20, ba luật dừng.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): ba chỉ số, 9 event có `trace_id`, 3 dòng rủi ro kinh tế, hồ sơ bảy mục.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- Chi phí mỗi việc thành công 4.472 đ, gấp 16,3× hoá đơn token chia số yêu cầu (275 đ) [simulated].
- Cả hệ thống 0,49× của 12.000 đ; xem lại 100% thì 0,98×–1,03× [simulated]. `quoc_te` 1,88× nên loại khỏi pilot.
- Yếu tố nhạy nhất: làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%) [simulated].
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%.
- Pilot: chia theo nhân viên 20 + 20, mức chênh 6 điểm (859 mỗi nhóm, m ≥ 299); power khoảng 0,64 nếu chênh thật chỉ 5 điểm.
- **Đề xuất: Go có điều kiện** cho phạm vi `noi_dia` + `hang_nang`, 5 điều kiện có người phụ trách.
- Kết quả duyệt chéo từ hội đồng: điền sau buổi duyệt chéo.

## 5. Khó khăn và cách xử lý

- Nhóm có 3 người cho 4 vai: người viết code kiêm kiểm số, người gắn nhãn 1 kiêm giữ hồ sơ.
- Đồng thuận nhãn chỉ 12/20 = 60%: nhóm viết lại định nghĩa theo thứ tự câu hỏi và ghi quy tắc cho từng ca không trùng trong `bang_loi.md`.
- 20 + 20 nhân viên không đủ mẫu cho mức chênh 5 điểm (tối đa 1.000 < 1.251): chấp nhận mức chênh 6 điểm và ghi rõ power 0,64.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; cần thay bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chưa kết luận được tác động của trợ lý so với 0,70.
- Pilot chỉ phát hiện chắc chắn mức chênh từ 6 điểm trở lên.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu statsmodels, `NormalIndPower`.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`.
