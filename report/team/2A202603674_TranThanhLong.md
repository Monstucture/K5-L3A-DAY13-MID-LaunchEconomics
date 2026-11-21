# Báo cáo cá nhân — Trần Thanh Long - 2A202603674

## 1. Thông tin thành viên

- Họ tên: Trần Thanh Long
- MSSV: 2A202603674
- Email: 26ai.longtt2@vinuni.edu.vn
- Vai trong nhóm: người gắn nhãn 1, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi, so nhãn, viết quy tắc phân biệt, bảng khắc phục 5 ca (`report/team/bang_loi.md`).
- Nhiệm vụ E: đặc tả chỉ số, danh sách event, rủi ro kinh tế (`report/team/chi_so.md`); hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`).
- Ghép hồ sơ cuối: `report/team/pilot_plan.yaml` (từ số D1 của người viết code), `report/team/group_report.md`, `TEAM.md`.

## 3. Đóng góp cụ thể

- Gắn nhãn 20 ca độc lập với người gắn nhãn 2; đồng thuận 12/20 = 60%, dưới 80% nên viết lại định nghĩa thành 5 câu hỏi theo thứ tự và ghi lý do cho 8 ca không trùng.
- Bảng khắc phục 5 ca, mỗi loại một ca (1, 20, 18, 19, 5), mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách.
- Tính thử ba chỉ số từ `logix_requests.csv`: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200); 9 event có `trace_id`; 3 dòng rủi ro kinh tế lấy số từ bảng độ nhạy [simulated].
- Hồ sơ launch bảy mục, đề xuất Go có điều kiện cho phạm vi `noi_dia` + `hang_nang`, nêu hai con số bất lợi: xem lại 100% thì 0,98×–1,03× [simulated], power 0,64 nếu chênh thật chỉ 5 điểm.
- `pilot_plan.yaml`: chia theo nhân viên 20 + 20, mức chênh 6 điểm (859 mỗi nhóm, m ≥ 299), 3 luật dừng đủ bốn vế.

## 4. Bằng chứng

- Commit `579e28e`, `436ace1` (`bang_loi.md`), `eab11a4` (`chi_so.md`), `5b5cfc6` (`ho_so_launch_v0.md`), `9513d0a`; PR #1, #2, #4, #5, #6 vào `main`.
- `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi; không còn dấu `?` ngoài chú thích.
- `grep -rni production report/team` không in gì.

## 5. Công cụ AI đã dùng

- **Claude (Claude Code):** giải thích yêu cầu đề và cách chia vai cho nhóm 3 người; soạn nháp bảng khắc phục, `chi_so.md`, hồ sơ launch, `pilot_plan.yaml`, `group_report.md`; giải thích ý nghĩa từng mục hồ sơ.
- Không dùng AI để gắn nhãn độc lập: hai bộ nhãn do hai người tự gắn, AI chỉ điền cột "Trùng?" sau khi đã so và đề xuất quy tắc phân biệt để nhóm thống nhất.
- Cách tự kiểm tra: ba chỉ số tính lại bằng pandas khớp 994/1.200, 48/177, 51/1.200; mọi số chi phí và cỡ mẫu đối chiếu với output `src/lab13.py` của người viết code; kiểm tra file YAML bằng `yaml.safe_load`; tự sửa nhãn thống nhất ca 3 (Ngữ cảnh) cho khớp định nghĩa.

## 6. Tự đánh giá

