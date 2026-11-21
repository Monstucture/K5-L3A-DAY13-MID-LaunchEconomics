# Báo cáo cá nhân — Phạm Cát Tân - 2A202603678

## 1. Thông tin thành viên

- Họ tên: Phạm Cát Tân
- MSSV: 2A202603678
- Email: tanpham090921@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code

## 2. Phần việc phụ trách

Viết và chạy `src/lab13.py` cho nhiệm vụ A, B và D1, và điền `report/team/bang_chi_phi.md`. Ngoài ra tính tỉ lệ mở lại hiện tại (D3) để nhóm đặt luật an toàn trong `pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- A1: ba hàm số lần chạy kỳ vọng, tỉ lệ thành công, hệ số chi phí; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2: hàm `mo_hinh` cộng token và tool trên mọi lần chạy (kể cả lỗi), cộng xem lại và làm lại (simulated), chia cho số việc thành công. Kết quả: 4.472 đ mỗi việc thành công, gấp khoảng 16,3 lần hoá đơn token và tool chia số yêu cầu (275 đ) [simulated].
- A3: tách theo loại; `quoc_te` tốn 22.515 đ, gấp 1,88× baseline 12.000 đ, và tỉ lệ ok giảm từ 30,0% xuống 11,4% rồi 2,2% qua ba lần chạy [simulated].
- A4: cộng chi phí cố định 40 triệu đ/tháng vào phạm vi noi_dia + hang_nang: 4.599 đ (0,38×) ở 45.000 yêu cầu/tháng, 5.784 đ (0,48×) ở một nửa khối lượng [simulated].
- B1 đến B4: chín kịch bản độ nhạy, xếp hạng (làm lại, xem lại, lương), giới hạn chạy lại 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ), xem lại 100% ra 0,98× đến 1,03× baseline [simulated].
- D1: năm câu cỡ mẫu (1.251 theo yêu cầu; theo nhân viên cần 42 người mỗi nhóm, vượt số người có; 1.000 và 300 là trần theo cụm; m ≥ 299 cho mức chênh 6 điểm).
- D3: tỉ lệ `mo_lai_trong_7_ngay` hiện tại 4,25% (toàn bộ) và 3,97% (phạm vi noi_dia + hang_nang).

## 4. Bằng chứng

- Commit `e4ecf86` ("lab13") và `344b0b6` ("người viết code") sửa `src/lab13.py`, `report/team/bang_chi_phi.md`, `TEAM.md`.
- `cd src && python3 lab13.py` in ba phép thử ĐẠT, bảng A2, A3, A4, B1 đến B4, D1, D3.
- `report/team/bang_chi_phi.md` đủ các bảng A1 đến B4, mọi số từ cột `_simulated` có nhãn simulated.

## 5. Công cụ AI đã dùng

Claude Code (trong VS Code). Dùng để đọc tài liệu hướng dẫn, viết các phần A3, B, D1, A4, D3 trong `lab13.py` và soạn `bang_chi_phi.md`. Tôi kiểm tra bằng cách chạy lại `lab13.py` và đối chiếu từng số với tài liệu hướng dẫn trong sai số 2%.

## 6. Tự đánh giá

Phần code và số liệu của nhiệm vụ A, B, D1 đã xong, chạy hết không lỗi và khớp đáp án tham chiếu. Chưa làm: bảng lỗi (nhiệm vụ C) và hồ sơ launch (nhiệm vụ E) do người khác phụ trách. Cần nhờ một thành viên chạy lại `lab13.py` trên máy khác để xác nhận.
