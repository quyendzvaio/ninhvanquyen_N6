def nhap() :
    chuoi = str(input(f'nhap chuoi: '))
    return chuoi

def xu_ly(a) :
    my_dict = {}
    for char in a :
        key = char
        value = a.count(key)
        my_dict[key] = value
    print(my_dict)

c = nhap()
xu_ly(c)
            