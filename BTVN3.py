def T1(n):  
    total = 0  
    for i in range(1, 2 * n + 2):  
        if i % 2 == 0:  
            total -= i  
        else:  
            total += i  
    return total  

def T2(n):  
    total = 0.0  
    for i in range(1, n + 1):  
        total += 1 / i  
    return total  

def nhap():  
    while True:  
        try:  
            n = int(input('Nhập vào một số nguyên dương : '))  
            if n > 0:  
                return n  
            else:  
                print("Nhập lại một số nguyên dương (lớn hơn 0): ")  
        except :  
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

def KT(a, b, c):   
    delta = b ** 2 - 4 * a * c  
    
    if delta > 0:  
        r1 = (-b + delta ** 0.5) / (2 * a)  
        r2 = (-b - delta ** 0.5) / (2 * a)  
        return f"Có hai nghiệm phân biệt: x1 = {r1}, x2 = {r2}"  
    elif delta == 0:  
        r = -b / (2 * a)  
        return f"Có một nghiệm duy nhất: x = {r}"  
    else:  
        return "Không có nghiệm thực"  
 
GT = nhap()
Tong1 = T1(GT)
print(f"Tổng S(n) = {Tong1}")
Tong2 = T2(GT)
print(f"Tổng S(n)* = {Tong2}")
x = nhap()
y = nhap()
z = nhap()
KT(x,y,z)