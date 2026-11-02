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
# kiếm tra số chẵn lẽ
def kiemtrachanle(x):
    if x % 2 == 0:
        print(x," là số chẵn")
    else:
        print(x," là số lẻ")
# kiêm tra số hoàn hảo
# tính tổng bình phương tới n
def kiem_tra_so_hoan_hao(n):
    # Số hoàn hảo phải là số nguyên dương lớn hơn 1
    if n <= 1:
        return False
    tong_uoc = 0
    # Duyệt qua các số từ 1 đến n - 1 để tìm các ước số
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
            
    # Nếu tổng các ước bằng chính n thì đó là số hoàn hảo
    return tong_uoc == n
