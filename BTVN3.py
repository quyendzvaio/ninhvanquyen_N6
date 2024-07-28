def xoa_phan_tu_chan(s):  
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 0])  

def xen_ke(s1, s2):  
    k=[]
    for i in range(len(s1)+len(s2))
        k.append(s1[i])
        s1 = s1[i:]
        k.append(s2[i])
        s2 = s2[i:]
    return k 

def swap(s1, s2):  
    if len(s1) >= 2 and len(s2) >= 2:  
        swapped_s1 = s2[0:2] + s1[2:] 
        swapped_s2 = s1[0:2] + s2[2:]   
        return swapped_s1, swapped_s2  
    else:  
        return None  

def main():  
    s1 = input("Nhập chuỗi s1: ")  
    s2 = input("Nhập chuỗi s2: ")  

    s3 = xoa_phan_tu_chan(s1)  
    print("Chuỗi s3 : ", s3)  

    s4 = xen_ke(s1, s2)  
    print("Chuỗi s4 : ", s4)  

    swapped_result = swap(s1, s2)  
    if swapped_result:  
        swapped_s1, swapped_s2 = swapped_result  
        print("Chuỗi sau khi đổi chỗ 2 ký tự đầu tiên: s1 =", swapped_s1, "và s2 =", swapped_s2)  
    else:  
        print("Một trong hai chuỗi cần dài ít nhất 2 ký tự để đổi chỗ.")  

if __name__ == "__main__":  
    main()