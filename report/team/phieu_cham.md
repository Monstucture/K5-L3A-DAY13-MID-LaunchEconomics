# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): MID (L3A)
- Nhóm được chấm: D2HL (L3A)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 7 | Nêu đủ ba con số bất lợi: xem lại 100% = 0,98×–1,03×, power 0,64, ca 7 và 20 chưa sửa; mỗi cái có điều kiện, người phụ trách và ngày. Chưa xử lý: lỗi ngầm (ca 5, 17) không có điều kiện kiểm tra mẫu, mà chỉ số mở lại 7 ngày không bắt được; điều kiện 4 cần sửa + bỏ < 15% trong khi hiện là 27,12%, không nói nếu không đạt thì sao. Lý do chính 0,38× tính ở 45.000 yêu cầu/tháng, không phải khối lượng lúc pilot. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 9 | Nhãn [simulated] có ở mục 1, 2, 3, 7, ở ngưỡng 8.000 đ và trong `simulated_inputs`. Phạm vi thu hẹp về `noi_dia` + `hang_nang` có số: loại `quoc_te` 1,88× (thành công 27,3%) và `doi_tac` 0,85×. Người phụ trách mục 2 và 4 ghi tên người (Duyên, Linh), không phải vai trò có quyền quyết định. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20, ngẫu nhiên, phân tầng theo depot; mức chênh 6 điểm (859/nhóm, m ≥ 299, DE 6,96); 3 luật dừng đủ bốn vế, có ngưỡng và người tắt. Nhưng: bước 20 người chỉ 1 tuần, trong phạm vi ~30,7 yêu cầu/người/ngày nên cần ~10 ngày cho 299; cộng 7 ngày chờ mở lại thì khó đủ dữ liệu vào `decision_date` 2027-01-05. Luật an toàn "3 ngày" đo bằng chỉ số 7 ngày; luật lệch 2 điểm áp dụng từ bước 4 người (lệch ngẫu nhiên ≥ 2 điểm ~56/1.000 lần). |
| **Tổng** | | | | **26 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ khớp số của chính nhóm và nêu đủ con số bất lợi (0,98×–1,03× khi xem lại 100%, power 0,64, ca 7 và 20 chưa sửa), mỗi cái có điều kiện, người phụ trách và ngày kiểm tra; phạm vi thu hẹp có số (loại `quoc_te` 1,88×, `doi_tac` 0,85×). Trước khi bắt đầu cần thêm: (1) bước 20 người kéo dài ~10 ngày để đạt 299 yêu cầu/người và dời `decision_date` cho đủ 7 ngày theo dõi mở lại; (2) điều kiện kiểm tra mẫu để bắt lỗi ngầm (ca 5, 17); (3) viết trước quyết định khi kết quả không có ý nghĩa thống kê (power 0,64).

**Một câu hỏi cho đội trình:** Bước 20 người chỉ chạy một tuần, mỗi người khoảng 30,7 yêu cầu trong phạm vi mỗi ngày: làm sao đạt 299 yêu cầu mỗi người và còn đủ 7 ngày theo dõi mở lại trước `decision_date` 2027-01-05?

**Câu hỏi thêm:**

1. Power chỉ 0,64 nếu tác động thật là 5 điểm, tức khoảng 1/3 khả năng pilot không thấy gì: ngày 2027-01-05 kết quả không có ý nghĩa thống kê thì nhóm quyết định Go, kéo dài hay dừng, và quy tắc đó đã viết trước chưa?
2. Lỗi ngầm như ca 5 (14 đơn hoàn thừa ~12.000 đ) và ca 17 (212 đơn sai giá) không làm khách mở lại: chỉ số an toàn "mở lại 7 ngày" bắt chúng bằng cách nào, khi bốn điều kiện không có kiểm tra mẫu?
3. Tỉ lệ sửa + bỏ hiện là 27,12%, điều kiện 4 cần xuống dưới 15% mới giảm xem lại: nếu không xuống được thì xem lại vẫn 100%, chi phí 0,98×–1,03× [simulated]; lúc đó pilot còn đáng chạy tiếp không?
4. Ở bước 4 người, 40 triệu đ tiền thuê chia cho khoảng 3.375 việc thành công là ~11.900 đ/việc, tổng ~15.300 đ [simulated]: luật dừng "chi phí > 8.000 đ" có cộng tiền thuê không? Nếu có thì pilot dừng ngay bước đầu.

**Câu trả lời của đội trình (ghi lại tại buổi):** ...
