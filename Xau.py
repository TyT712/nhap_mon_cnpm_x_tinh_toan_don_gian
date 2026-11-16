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
def dem_tu(s):
    a = s.split()
    return len(a)

s = input("Nhap xau: ")
print("So tu trong xau la:", dem_tu(s))
# ---viết hoa chữ cái đầu và viết thường các chữ cái còn lại trong xâu
# ---viết hoa chữ cái đầu và viết thường các chữ cái còn lại trong 
def chuan_hoa_ten(ten: str) -> str:
    danh_sach_tu = ten.split()
    tu_da_chuan_hoa = [tu.capitalzie() for tu in danh_sach_tu]
    return " ".join(tu_da_chuan_hoa)
# ---kiểm tra xâu đối xung