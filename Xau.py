# --- đảo ngược xâu ---
# ---đếm số nguyên âm và phụ âm trong xâu
def dem_nguyen_am_va_phu_am(s):
    nguyen_am = "ueaoiUEAOI"
    so_nguyen_am = 0
    so_phu_am = 0
    for char in s:
        if char.isalpha():
            if char in nguyen_am:
                so_nguyen_am += 1
            else:
                so_phu_am += 1            
    return so_nguyen_am, so_phu_am
if __name__ == "__main__":
    s = input("Nhập vào một xâu cần kiểm tra: ")
    vowels, consonants = dem_nguyen_am_va_phu_am(s)
    print(f"Số lượng nguyên âm: {vowels}")
    print(f"Số lượng phụ âm: {consonants}")
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
# ---kiểm tra xâu đối xung
s = input("Nhập xâu: ")

s = s[::-1]

print("Xâu đảo ngược là:", s)
def kiem_tra_doi_xung_2(s):
  s = s.lower().replace(" ", "")
  left = 0
  right = len(s) - 1

  while left < right:
    if s[left] != s[right]:
      return False  # Khác nhau thì không phải xâu đối xứng
    left += 1
    right -= 1

  return True  # Duyệt hết mà không sai thì là xâu đối xứng
# ---viết hoa chữ cái đầu và viết thường các chữ cái còn lại trong 
def chuan_hoa_ten(ten: str) -> str:
    danh_sach_tu = ten.split()
    tu_da_chuan_hoa = [tu.capitalzie() for tu in danh_sach_tu]
    return " ".join(tu_da_chuan_hoa)
# ---kiểm tra xâu đối xung
