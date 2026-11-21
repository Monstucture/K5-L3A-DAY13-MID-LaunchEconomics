# Báo cáo cá nhân — Chu Than Nhat - 2A202603649

## 1. Thông tin thành viên

- Họ tên: Chu Than Nhat
- MSSV: 2A202603649
- Email: Chưa cung cấp
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người kiểm số, người gắn nhãn 1

## 2. Phần việc phụ trách

Kiểm tra số liệu A và B, gắn nhãn độc lập 20 ca với vai trò người gắn nhãn 1, phối hợp hoàn thiện `report/team/bang_loi.md`, kiểm tra cỡ mẫu D1 và điền `report/team/pilot_plan.yaml`. Bổ sung hai rủi ro kinh tế vào `report/team/chi_so.md` theo bảng độ nhạy.

## 3. Đóng góp cụ thể

- Đối chiếu phép tính A2: tổng chi phí 4.373.585 đ chia 978 việc thành công, xấp xỉ 4.472 đ/việc.
- Rà bảng A2–A4 và các kịch bản B1–B4; kiểm tra thứ hạng các yếu tố ảnh hưởng chi phí.
- Gắn nhãn 20 ca độc lập trước khi so với người gắn nhãn 2; phối hợp thống nhất nhãn và cách khắc phục sau bước so sánh.
- Kiểm tra số cỡ mẫu D1 và dùng kết quả đã xác nhận trong kế hoạch pilot.
- Bổ sung rủi ro kinh tế trong `chi_so.md` dựa trên các kết quả độ nhạy.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`: phép đối chiếu CPS A2 và bảng kết quả A, B.
- `report/team/bang_loi.md`: hồ sơ đối chiếu; hiện còn thiếu nhãn người 2, cột đồng thuận và các ô thống nhất.
- `report/team/pilot_plan.yaml`: thông số cỡ mẫu D1 và luật dừng.
- `report/team/chi_so.md`: các rủi ro kinh tế lấy từ bảng độ nhạy.

## 5. Công cụ AI đã dùng

Dùng ChatGPT để giải thích yêu cầu, công thức và chuẩn bị checklist. Tự đối chiếu các phép tính với `docs/du_lieu_va_cong_thuc.md`, kết quả trong `src/lab13.py` và các bảng nhóm; các con số dùng cột `_simulated` được giữ nhãn simulated.

## 6. Tự đánh giá

Đã thực hiện phần kiểm số và gắn nhãn độc lập theo phân công. Trước khi nộp, cần bổ sung email và cùng người gắn nhãn 2 nhập đủ kết quả so nhãn vào `bang_loi.md`; các đóng góp vào D/E cần được đối chiếu với hồ sơ cuối của nhóm.
