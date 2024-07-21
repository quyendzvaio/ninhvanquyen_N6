def fibonacci(n):  
    Fibo = []  
    if n <= 0:  
        return Fibo   
    elif n == 1:  
        Fibo.append(0)  
        return Fibo   
    else:  
        Fibo.append(0)  
        Fibo.append(1) 
        for i in range(2, n): 
            Fibo[0] = 0
            Fibo[1] = 1 
            Fibo[2] = 1 
            Fibo[3] = 2
            Fibo[i] = Fibo[i-1] + Fibo[i-2] 
            Fibo.append(Fibo[i])  
    
    return Fibo  

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

GT = nhap()
T = fibonacci(GT)
print(T)