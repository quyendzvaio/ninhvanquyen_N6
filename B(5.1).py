def nhapDS() :
    collect = {}
    print('Ket thuc nhap vao bang cach nhan Enter 2 lan')
    while True :
        key = input(f'ma sinh vien: ')
        if key :
            try :
                values = float(input())
                collect[key] = values
            except ValueError:
                print('Du lieu nhap vao chua hop le! Nhap lai.')
        if key == '':
            break
    return collect

def bosung(c):
    print('nhap bo sung thong tin mot sinh vien')
    key = input(f'ma sinh vien: ')
    value = float(input())
    c[key] = value
    return c

def KT(c) :
    x = [sum (1 for value in c.values() if  3.0 <= value <= 5.0 )]
    print(f'co {x} sinh vien thoa man')

def xoa(c):
    x = [key for key,values in c.items() if values <= 2]
    del x
    print(c)

a = nhapDS()
KT(a)
bosung(a)
xoa(a)