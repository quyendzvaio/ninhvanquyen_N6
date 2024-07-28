def ma_tran(a, n, m):    
    if n * m > len(a):  
        return "NO"   
    ma_tran = []  
    for i in range(n):  
        cat = a[:n]
        ma_tran.append(cat)  
        a = a[n:]
    return ma_tran  
  
def nhap():
    while True:
        try:
            n=int(input('nhap so luong phan tu k = '))
            if n>=0 :
                return n
        except:
            print('Nhap lai. So pha tu k khong hop le (k >= 0)') 

def nhapPT(n):
    a=[]
    while True:
        try:
            PT = [int(input(f'a[{i}] = ')) for i in range(n)]
            a.append(PT)
        except:
            print('Phan tu nhap vao khong hop le') 
    return a 
  
k = nhap()
a = nhapPT(k)  
n = int(input("Nhập số dòng của ma trận: "))  
m = int(input("Nhập số cột của ma trận: "))   
ket_qua = tao_ma_tran(a, n, m)  
print(ket_qua)