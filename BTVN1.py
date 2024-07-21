def total(n):  
    T = 0  
    while True:  
        if n > 10:  
            T = T + n % 10  
            n //= 10  
        else:  
            T = T + n  
            break    
    return T  

def nhap():  
    while True:  
        try:  
            n = int(input('Nhập vào một số nguyên dương n: '))  
            if n > 0:  
                return n  
            else:  
                print("Nhập lại một số nguyên dương n (n > 0): ")  
        except :  
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")   

def tong_uoc(n):  
    TU = 0  
    for i in range(1, n + 1): 
        if n % i == 0:  
            TU += i  
    return TU  
  
def KT(x, y, z):  
    if x + y > z and x + z > y and y + z > x:  
        if x == y and y == z:  
            print("tam giác đều")  
        elif x == y or y == z or x == z:  
            print("tam giác cân")  
        else:    
            a, b, c = sorted([x, y, z])  
            if c ** 2 == a ** 2 + b ** 2:  
                print("tam giác vuông")  
            elif c ** 2 > a ** 2 + b ** 2:  
                print("tam giác tù")  
            else:  
                print("tam giác nhọn")  
    else:  
        print("không phải là tam giác")  
  
GT = nhap()  
T1 = total(GT)  
print(f"Tổng các chữ số trong số nguyên n = {T1}")  
T2 = tong_uoc(GT)  
print(f"Tổng các ước của n = {T2}")  

x = nhap()  
y = nhap()  
z = nhap()  
KT(x, y, z)  
