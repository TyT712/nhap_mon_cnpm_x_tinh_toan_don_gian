# --- đảo ngược xâu ---
# ---đếm số nguyên âm và phụ âm trong xâu
# ---đếm số lần xuất hiện của 1 ký tự trong xâu
# ---đếm số từ trong xâu
def dem_tu(s):
    a = s.split()
    return len(a)

s = input("Nhap xau: ")
print("So tu trong xau la:", dem_tu(s))
# ---viết hoa chữ cái đầu và viết thường các chữ cái còn lại trong xâu
# ---kiểm tra xâu đối xung