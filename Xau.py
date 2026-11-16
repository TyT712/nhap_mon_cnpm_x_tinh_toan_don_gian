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
# ---đếm số từ trong xâu
# ---viết hoa chữ cái đầu và viết thường các chữ cái còn lại trong xâu
# ---kiểm tra xâu đối xung