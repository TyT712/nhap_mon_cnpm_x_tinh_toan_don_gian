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
# kiếm tra số chẵn lẽ
# kiêm tra số hoàn hảo
# tính tổng bình phương tới n