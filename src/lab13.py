"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]

    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm để so hai tỉ lệ p1 và p2 (z chính xác, làm tròn lên)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc):
    """DE = 1 + (m - 1) × ICC, m là số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def co_mau_hieu_dung(c, m, icc):
    """Cỡ mẫu hiệu dụng mỗi nhóm khi chia theo c cụm, mỗi cụm m yêu cầu."""
    return c * m / he_so_thiet_ke(m, icc)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
    print('\nA3 · Chi phí mỗi việc thành công theo loại [simulated]')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'lan_chay/yc':>12s} {'cps (d)':>10s} {'/12.000':>8s}")
    for loai, nhom in reqs.groupby('loai'):
        r = mo_hinh(runs, nhom)
        n = len(nhom)
        so_lan = runs['request_id'].isin(nhom['request_id']).sum() / n
        print(f"{loai:10s} {n:6d} {r['thanh_cong'] / n:9.1%} {so_lan:12.2f} "
              f"{r['cps']:10,.0f} {r['cps'] / BASELINE:7.2f}x")

    # ---------- A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
    CO_DINH_THANG, YC_THANG = 40_000_000, 45_000
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pv = mo_hinh(runs, pham_vi)
    ti_le_pv = r_pv['thanh_cong'] / len(reqs)  # 900 / 1.200
    print(f"\nA4 · Chi phí cố định, phạm vi noi_dia + hang_nang [simulated]: "
          f"{r_pv['thanh_cong']} việc thành công, tổng {r_pv['tong']:,.0f} đ, cps {r_pv['cps']:,.0f} đ")
    for ten, yc in (('45.000 yc/tháng', YC_THANG), ('một nửa khối lượng', YC_THANG / 2)):
        viec = yc * ti_le_pv
        cd = CO_DINH_THANG / viec
        print(f'  {ten:20s} {viec:8,.0f} việc/tháng · cố định {cd:6,.0f} đ/việc · '
              f"cps + cố định {r_pv['cps'] + cd:6,.0f} đ = {(r_pv['cps'] + cd) / BASELINE:.2f}×")

    # ---------- D3 · Tỉ lệ mở lại hiện tại (chỉ số an toàn), tính TRƯỚC khi đặt luật dừng ----------
    pv_mask = reqs['loai'].isin(['noi_dia', 'hang_nang'])
    print('\nD3 · Tỉ lệ mo_lai_trong_7_ngay hiện tại (chạy thử, chưa có nhóm đối chứng)')
    print(f"  toàn bộ: {reqs['mo_lai_trong_7_ngay'].mean():.2%} ({reqs['mo_lai_trong_7_ngay'].sum()}/{len(reqs)})")
    print(f"  phạm vi noi_dia + hang_nang: {reqs.loc[pv_mask, 'mo_lai_trong_7_ngay'].mean():.2%} "
          f"({reqs.loc[pv_mask, 'mo_lai_trong_7_ngay'].sum()}/{pv_mask.sum()})")
    for loai, nhom in reqs.groupby('loai'):
        print(f"  {loai:10s} {nhom['mo_lai_trong_7_ngay'].mean():6.2%} ({nhom['mo_lai_trong_7_ngay'].sum()}/{len(nhom)})")

    # Chạy lại có giúp không: tỉ lệ lần chạy ok theo từng lần thử
    print('\nTỉ lệ lần chạy ok theo lần thử (attempt) và loại')
    lan = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    lan['ok'] = (lan['status'] == 'ok').astype(int)
    print(lan.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))

    # ---------- Nhiệm vụ B1 · Đổi từng yếu tố ----------
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print('\nB1 · Bảng độ nhạy [simulated]')
    print(f"{'Kịch bản':26s} {'cps (đ)':>9s} {'thay đổi':>9s}")
    print(f"{'Gốc (A2)':26s} {goc:9,.0f}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:26s} {cps:9,.0f} {(cps / goc - 1) * 100:+8.1f}%')

    # ---------- B2 · Đổi một cặp ----------
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Giá token gấp đôi + xem lại gấp đôi: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%)')
    # Xếp hạng theo mức tăng khi gấp đôi (lương: +25% nên quy về cùng thang chỉ để tham khảo)
    print('Xếp hạng: 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên (rồi tới giá token)')

    # ---------- B3 · Giới hạn chạy lại: chi phí cả hệ thống ----------
    print('\nB3 · Giới hạn chạy lại [simulated]')
    print(f"{'Giới hạn':>9s} {'Tổng trợ lý':>12s} {'Không TC':>9s} {'Cả hệ thống':>12s} {'cps':>8s}")
    for k in (1, 2, 3):
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - r['thanh_cong']
        he_thong = r['tong'] + BASELINE * khong_tc
        print(f"{k:>7d} l {r['tong']:12,.0f} {khong_tc:9d} {he_thong:12,.0f} {r['cps']:8,.0f}")

    # ---------- B4 · Xem lại tất cả (chỉ noi_dia + hang_nang) ----------
    PHUT_XEM, PHUT_LAM_DE = 5, 9
    sub = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    sub_runs = runs[runs['request_id'].isin(sub['request_id'])]
    n_xem = sub_runs.loc[sub_runs['status'] == 'ok', 'request_id'].nunique()
    lam_lai = sub[sub['ket_qua'] == 'lam_lai']
    tien_run = (sub_runs['tokens_in'] / 1000 * GIA_VAO + sub_runs['tokens_out'] / 1000 * GIA_RA
                + sub_runs['tool_calls'] * GIA_TOOL).sum()
    tc = (sub['ket_qua'] == 'thanh_cong').sum()
    # Trung bình phút làm lại trên TOÀN BỘ ca lam_lai (mọi loại), theo hướng dẫn
    phut_lam_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'\nB4 · Xem lại 100% [simulated]: {len(sub)} yêu cầu, {n_xem} có lần chạy ok, '
          f'{len(lam_lai)} ca làm lại, {tc} việc thành công')
    for nhan, phut_lam in (('đề cho 9 phút/ca', PHUT_LAM_DE), (f'dữ liệu {phut_lam_tb:.1f} phút/ca', phut_lam_tb)):
        tong = n_xem * PHUT_XEM * LUONG_PHUT + len(lam_lai) * phut_lam * LUONG_PHUT + tien_run
        cps = tong / tc
        hoa_von = (BASELINE * tc - tien_run - len(lam_lai) * phut_lam * LUONG_PHUT) / (n_xem * LUONG_PHUT)
        print(f'  {nhan:24s} tổng {tong:12,.0f} đ · cps {cps:7,.0f} đ = {cps / BASELINE:.2f}× · hoà vốn xem lại ≤ {hoa_von:.1f} phút')
    # ---------- Nhiệm vụ D1 · Cỡ mẫu theo ba cách chia ----------
    # D1 (baseline 0,70; alpha 0,05; power 0,8; ICC 0,02):
    # a) Chia theo yêu cầu: 1.251 yêu cầu mỗi nhóm.
    # b) Theo nhân viên, m=75: DE=2,48; cần 3.103 yêu cầu/nhóm,
    #    tương đương 42 nhân viên/nhóm (84 tổng), vượt 40 nhân viên hiện có.
    # c) 20 nhân viên/nhóm: trần hiệu dụng c/ICC = 1.000 < 1.251.
    # d) 6 depot/nhóm: trần hiệu dụng c/ICC = 300.
    # e) Chấp nhận MDE 6 điểm: 859/nhóm; 20 nhân viên/nhóm cần m>=299
    #    yêu cầu/người (DE=6,96). Nếu tác động thật chỉ 5 điểm, power khoảng 0,64.
    # D2: đối chứng chạy cùng tuần/depot; phân nhân viên ngẫu nhiên có seed,
    #    phân tầng theo depot; hạn chế chia sẻ bằng quyền truy cập theo tài khoản
    #    và log staff_id; chốt chỉ số/ngưỡng/dừng/ngày quyết định trước; 20 cụm/nhóm.
    # Chọn chia theo nhân viên, chấp nhận phát hiện được mức 6 điểm thay vì 5.
    # Cho sẵn: baseline 0,70; mục tiêu +5 điểm; alpha 0,05; power 0,8; ICC 0,02; 40 nhân viên, 12 depot.
    ICC, NV_TONG = 0.02, 40
    n_a = co_mau(0.70, 0.75)
    print(f'\nD1 · Cỡ mẫu (cỡ mẫu theo yêu cầu: dữ liệu lab là simulated)')
    print(f'a · Chia theo yêu cầu: {n_a:,} yêu cầu mỗi nhóm')

    m = 75
    de = he_so_thiet_ke(m, ICC)
    n_b = math.ceil(n_a * de)
    nv_moi_nhom = math.ceil(n_b / m)
    print(f'b · Theo nhân viên, m={m}: DE={de:.2f}, n={n_b:,} mỗi nhóm → {nv_moi_nhom} người mỗi nhóm, '
          f'tổng {2 * nv_moi_nhom} {">" if 2 * nv_moi_nhom > NV_TONG else "<="} {NV_TONG}: '
          f'{"KHÔNG đủ người" if 2 * nv_moi_nhom > NV_TONG else "đủ người"}')

    tran_c = 20 / ICC
    print(f'c · 20 nhân viên mỗi nhóm: tối đa {tran_c:,.0f} {"<" if tran_c < n_a else ">="} {n_a:,}: '
          f'{"KHÔNG đạt" if tran_c < n_a else "đạt"}')
    print(f'd · 6 depot mỗi nhóm: tối đa {6 / ICC:,.0f}')

    n_e = co_mau(0.70, 0.76)
    m_e = min(k for k in range(1, 5000) if co_mau_hieu_dung(20, k, ICC) >= n_e)
    print(f'e · Mức chênh 6 điểm ({n_e:,}/nhóm), 20 người mỗi nhóm: m ≥ {m_e} yêu cầu mỗi người '
          f'(DE {he_so_thiet_ke(m_e, ICC):.2f})')

    # Đối chiếu độc lập bằng statsmodels (cần pip install statsmodels)
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        n_sm = NormalIndPower().solve_power(proportion_effectsize(0.75, 0.70), alpha=0.05, power=0.8)
        print(f'   (đối chiếu statsmodels, arcsine: {math.ceil(n_sm):,}/nhóm — công thức khác nên lệch nhẹ)')
    except ImportError:
        print('   (bỏ qua đối chiếu statsmodels: chưa cài)')
