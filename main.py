# tính giai thừa
def tinhgiaithua(n):
    if n < 0:
        return "Không có giai thừa cho số âm."
    if n==0 or n==1: 
        return 1
    ket_qua= 1
    for i in range (2,n+1):
        ket_qua += i
        return ket_qua 
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
# kiếm tra số chẵn lẽ
# kiêm tra số hoàn hảo
# tính tổng bình phương tới n