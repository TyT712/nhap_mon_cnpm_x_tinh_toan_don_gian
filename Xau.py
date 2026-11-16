# --- đảo ngược xâu ---
# ---đếm số nguyên âm và phụ âm trong xâu
# ---đếm số lần xuất hiện của 1 ký tự trong xâu
# ---đếm số từ trong xâu
# ---viết hoa chữ cái đầu và viết thường các chữ cái còn lại trong xâu
# ---kiểm tra xâu đối xung
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