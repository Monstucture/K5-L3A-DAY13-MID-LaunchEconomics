# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated (có cộng xem lại, làm lại) |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 275 | | đo từ trace |

- Chi phí mỗi việc thành công gấp khoảng 16,3 lần "hoá đơn chia số yêu cầu" (4.472 đ so với 275 đ), vì hoá đơn bỏ sót giờ của nhân viên [simulated].
- Khoản lớn nhất là làm lại: 2.264.000 đ, chiếm 51,8% tổng chi phí; xem lại chiếm 40,7%; token và tool cộng lại chỉ 7,5% [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- `quoc_te` không đáng để trợ lý xử lý: 22.515 đ, gấp 1,88× chi phí 12.000 đ của nhân viên tự làm [simulated].
- Chạy lại tới 3 lần không giúp: tỉ lệ lần chạy ok của `quoc_te` giảm từ 30,0% (lần 1) xuống 11,4% (lần 2) và 2,2% (lần 3). Lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Trong phạm vi: 900 việc thành công trên 1.200 yêu cầu của mẫu, tổng 3.072.513 đ, tức 3.414 đ mỗi việc thành công. Chi phí cố định 40.000.000 đ/tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Chi phí cố định không đổi kết luận ở khối lượng đầy đủ (0,38×) và cả khi chỉ còn một nửa (0,48×, vẫn dưới 1×), nhưng làm cố định mỗi việc tăng gấp đôi khi khối lượng giảm. Hồ sơ launch phải ghi rõ con số đã cộng cố định hay chưa, và ở khối lượng nào.

## B1 · Đổi từng yếu tố

Chi phí gốc (A2): 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ [simulated] | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (+46,3%) [simulated], đúng bằng tổng hai tác động riêng (5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%) [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Mọi số tiền đều [simulated].

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ), rẻ hơn giới hạn 3 lần 136.365 đ và giới hạn 1 lần 548.561 đ.
- Không trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ): tối ưu riêng chỉ số đó đẩy thêm 85 yêu cầu sang nhân viên so với giới hạn 2 lần.

## B4 · Nếu phải xem lại tất cả

Phạm vi `noi_dia` + `hang_nang`: 982 yêu cầu, 948 có lần chạy ok (mỗi yêu cầu xem lại 5 phút), 48 ca làm lại, 900 việc thành công.

- Chi phí mỗi việc thành công khi xem lại 100%: 11.743 đ = 0,98× của 12.000 đ nếu làm lại 9 phút mỗi ca. Với 15,3 phút mỗi ca (trung bình thật của cột `phut_lam_lai_simulated` trên mọi ca làm lại) là 12.415 đ = 1,03× [simulated]. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (15,3 phút).
- Xem lại 100% thì trợ lý gần như không tiết kiệm được gì, vì tiền xem lại chiếm khoảng 90% chi phí. Pilot phải học được tỉ lệ xem lại giảm an toàn xuống bao nhiêu và mỗi lần xem lại có ngắn hơn 5 phút được không.
