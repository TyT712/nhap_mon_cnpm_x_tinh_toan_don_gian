# --- đảo ngược xâu ---
# ---đếm số nguyên âm và phụ âm trong xâu
# ---đếm số lần xuất hiện của 1 ký tự trong xâu
def dem_ky_tu(xau, kt):
    so_lan = xau.count(kt)
    return so_lan
xau = input("Nhập xâu: ")
kt = input("Nhập ký tự cần đếm: ")
ket_qua = dem_ky_tu(xau, kt)
print("Ký tự", kt, "xuất hiện", ket_qua, "lần")
# ---đếm số từ trong xâu
# ---viết hoa chữ cái đầu và viết thường các chữ cái còn lại trong xâu
# ---kiểm tra xâu đối xung