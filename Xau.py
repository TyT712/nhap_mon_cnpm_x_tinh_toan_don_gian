# --- đảo ngược xâu ---
# ---đếm số nguyên âm và phụ âm trong xâu
# ---đếm số lần xuất hiện của 1 ký tự trong xâu
# ---đếm số từ trong xâu
# ---viết hoa chữ cái đầu và viết thường các chữ cái còn lại trong 
def chuan_hoa_ten(ten: str) -> str:
    danh_sach_tu = ten.split()
    tu_da_chuan_hoa = [tu.capitalzie() for tu in danh_sach_tu]
    return " ".join(tu_da_chuan_hoa)
# ---kiểm tra xâu đối xung