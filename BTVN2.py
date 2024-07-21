def nhap():  
    while True:  
        try:  
            n=float(input('nhập dũ liệu đầu vào'))
            return n
        except :  
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.") 

a=nhap()
b=nhap()
print(a+b)
print(f'{a}-{b}')
print(f'{a}*{b}')
print(f'{a}/{b}')
print(f'{a}**{b}')
print(f'{a}%{b}')
if a > b :
    print("a lớn hơn b")
elif a < b :
    print("a nhỏ hơn b")
else :
    print("a bằng b")        
print(f'{a} AND {b}')  
print(f'{a} OR {b}')
print(f'{a} XOR {b}')
print(f'{a} NOT {b}')