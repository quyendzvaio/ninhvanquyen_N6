def nhap():
    while True:
        try:
            x = int(input('nhap so luong thanh vien'))
            if x>0:
                return x
        except:
            print('so luong thanh vien khong hop le')

def nhapDS(n):
    DS = []
    for i in range(n):
        x = float(input(f'thanh vien thu {i+1} co so diem: '))
        DS.append(x)
    return dict(DS)

a = nhap()
b = nhapDS(a)
print('ban ngu nhat la:',min(b.(values)))