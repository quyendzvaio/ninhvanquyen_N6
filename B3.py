def nhap():  
    while True:  
        try:  
            x = int(input('Nhập số lượng thành viên: '))  
            if x > 0:  
                return x  
        except :  
            print('Số lượng thành viên không hợp lệ. Vui lòng nhập lại.')  

def nhapDS(n):  
    c = {}  
    for i in range(n):  
        while True:  
            try:  
                key = input()  
                values = float(input()) 
                c[key] = values 
                break   
            except:  
                print('Nhập không hợp lệ. Vui lòng nhập lại.')  
    return c


a = nhap()
b = nhapDS(a)  
m = min(b.values())  

for key, values in b.items():  
    if values == m:  
        ten = key 
        break  

print(f'Thành viên có số điểm thấp nhất: {ten}')