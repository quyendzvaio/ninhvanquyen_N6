#B1
def nhap():
    while True:
        try:
            x = int(input('nhap quang duong chu rua can di'))
            if x>0:
                return x
        except:
            print('nhap lai quang duong(quang duong>=0)')

a = nhap()
if a/3 != 0:
    print('so buoc toi thieu chu rua can di = ', int(a/3)+1)
else:
    print('so buoc toi thieu can di = ',a/3)