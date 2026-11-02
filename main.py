# tính giai thừa
# kiểm tra số nguyên tố
def nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input("Nhap n: "))
if nguyen_to(n):
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")
# kiểm tra số chẵn lẽ
# kiểm tra số hoàn hảo
# tính tổng bình phương tới n