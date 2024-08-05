def nhap():
    while True:
        try:
            n=int(input('nhap so nguyen duong N = '))
            if n>=0 :
                return n
        except :
            print('nhap lai so nguyen N(N >= 0)')

def nhapPT(n):
    a=[]
    while True:
        try:
            PT = [int(input(f'a[{i}] = ')) for i in range(n)]
            a.append(PT)
            break
        except:
            print('Phan tu nhap vao khong hop le') 
    return a     

def KT(a, x):    
    dem = sum(1 for i in range(a) if i==x) 
    if dem > 0:   
        print(f"{x} xuat hien {dem} có trong danh sách.")  
        return True, dem  
    else:  
        print(f"{x} không có trong danh sách.")  
        return False, dem   


def thay_the(a):    
    new=[8, 5, 4, 0, 1, 3]
    a[2:8]=new
    print(a)
    return a 

def find(a):  
    print(f'max = {max(a)}')
    print(f'min = {min(a)}')   

def insert(a, y):  
    # Chèn số Y vào đầu list.  
    a.insert(0, y)  

def check_sorted(a):  
    if a == sorted(a):  
        print("TĂNG")  
    elif a == sorted(a.reverse()):  
        print("GIẢM")  
    else:  
        print("NO")  

def create_new_list(a, n):  
    new_list = []  
    newPT = [sum(a[0:i]) for i in range(1, n + 1)]  
    new_list.append(newPT)  
    return new_list  

def sort_list(n):  
    # Sắp xếp list theo thứ tự tăng dần và theo giá trị tuyệt đối.  
    sorted_list = sorted(n)  # Sắp xếp theo giá trị  
    sorted_abs_list = sorted(n, key=abs)  # Sắp xếp theo giá trị tuyệt đối  
    return sorted_list, sorted_abs_list  

def main():  
    N=nhap() 
    b=nhapPT(N)  
    x = int(input("Nhập số X để kiểm tra số lần xuất hiện: "))  
    KT(b, x)   
    thay_the(b)   
    find(b)  
    y = int(input("Nhập số Y để chèn vào đầu list: "))  
    insert(b, y)  
    print("List sau khi chèn Y:", b)  
    
    check_sorted(b)  

    new_list = create_new_list(b, N)  
    print("List mới:", new_list)  

    list1 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]  
    sorted_list, sorted_abs_list = sort_list(list1)  
    print("List sau khi sắp xếp theo thứ tự tăng dần:", sorted_list)  
    print("List sau khi sắp xếp theo thứ tự tăng dần của giá trị tuyệt đối:", sorted_abs_list)  

if __name__ == "__main__":  
    main()


