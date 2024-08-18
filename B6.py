# def nhapDS() ->list:
#     c =[]
#     print('nhap cac phan tu cau list')
#     i = 0
#     while True:
#         x = float(input(f'a{i} = '))        
#         try:  
#             x.append(c)
#             i+=1
#         except:
#             print('du lieu nhap vao khong hop le!')
#         if x == '':
#             break
#     return sum(c[i] for i in range(len(c)) if c[i] %2 != 0)

# #(*a) : truyen doi so vi tri,lay cac gia tri cho trc va ket qua cuoi tao thanh 1 tuple,luon phai de vi tri cuoi
# # (**a) : tao thanh mot dict,luon phai de cuoi cung
# # ham long nhau
# def tong1(a,b):
#     def tong2(c,d):
#         return c+d
#     return tong2(a,b) 

# #ham an danh .   lambda doi so : cau lenh(ham lambda khong tai su dung duoc)
# lambda a,b : a+b
# print()
def fibo(n):
    fibo = [0,1]
    for i in range(2,n):
        fibo[i] = fibo[i-1] + fibo[i-2]
        fibo.append(fibo[i])
    return fibo

cube = lambda x:x**3
n = 5
print(list(map(cube,fibo(n))))