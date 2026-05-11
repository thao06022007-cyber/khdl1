# --- 1. KHAI BÁO SỐ LIỆU (Bạn có thể sửa số ở đây) ---
so_tien_ban_dau = 10000000  # Ví dụ: 10 triệu đồng
lai_suat_nam = 6            # Ví dụ: Lãi suất 6%/năm

# --- 2. CÔNG THỨC TÍNH TOÁN ---
# Đổi lãi suất năm (%) sang lãi suất tháng (số thập phân)
lai_suat_thang = (lai_suat_nam / 100) / 12

print(f"Số vốn ban đầu: {so_tien_ban_dau:,.0f} VNĐ")
print(f"Lãi suất hàng năm: {lai_suat_nam}%")
print("-" * 40)

# --- 3. VÒNG LẶP TÍNH LỢI NHUẬN 12 THÁNG ---
so_tien_hien_tai = so_tien_ban_dau

for thang in range(1, 13):
    # Tiền lãi tháng này = Tiền đang có * lãi suất tháng
    lai_thang_nay = so_tien_hien_tai * lai_suat_thang
    
    # Cộng dồn lãi vào gốc (Lãi kép)
    so_tien_hien_tai = so_tien_hien_tai + lai_thang_nay
    
    # In kết quả từng tháng
    print(f"Tháng {thang}: {so_tien_hien_tai:,.0f} VNĐ")

# --- 4. TỔNG KẾT ---
tong_loi_nhuan = so_tien_hien_tai - so_tien_ban_dau
print("-" * 40)
print(f"TỔNG KẾT SAU 1 NĂM:")
print(f"Số tiền cuối cùng: {so_tien_hien_tai:,.0f} VNĐ")
print(f"Tiền lãi thu được: {tong_loi_nhuan:,.0f} VNĐ")