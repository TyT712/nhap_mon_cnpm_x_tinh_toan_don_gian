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
