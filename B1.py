#B1
def nhap():
    while True:
        try:
            x = int(input('nhap so luong phan tu cua tuple: '))
            if x>0:
                return x
        except:
            print('nhap lai so luong phan tu cua tuple(n>=0)')

def nhapPT(n):
    a= []
    while True:
        try:
            for i in range(n):
                x= float(input(f'a{i} = '))
                a.append(x)
            break
        except:
            print("phan tu phai la so")
    return tuple(a)

GT = nhap()
b = nhapPT(GT)
c = []
for item in b:
    if b.count(item)%5 == 0 and b.count(item)%10 != 0:
        print(item)
        break

