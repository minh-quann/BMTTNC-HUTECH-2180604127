def tinh_tong(chuoi):
  tong_so_duong = 0
  tong_so_am = 0
  for so in chuoi.split():
    try:
      so_nguyen = int(so)
      if so_nguyen > 0:
        tong_so_duong += so_nguyen
      else:
        tong_so_am += so_nguyen
    except ValueError:
      pass
  return tong_so_duong, tong_so_am
chuoi = "12abc989 -123 -34xyz 56"
tong_duong, tong_am = tinh_tong(chuoi)
print(f"Tổng số dương trong chuỗi '{chuoi}' là: {tong_duong}")
print(f"Tổng số âm trong chuỗi '{chuoi}' là: {tong_am}")
