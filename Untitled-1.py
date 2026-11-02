def tong_binh_phuong(n):
    s = 0
    for i in range(1, n + 1):
        s += i**2
    return s

n = int(input("Nhập n: "))
print("Tổng bình phương từ 1 đến", n, "là:", tong_binh_phuong(n))