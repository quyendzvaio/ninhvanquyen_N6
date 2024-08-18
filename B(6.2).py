def nhap():
    while True:
        try:
            n = int(input('nhap vao so hang cau ma tran: '))
            m = int(input('nhap vao so cot cua ma tran: '))
            if n < 0 or m < 0:
                print('so hang va cot cua ma tran khong duoc nho hon 0(<0)')
            elif n == 0 or m == 0:
                print('')
            else:
                 return n,m
        except:
                print('Dinh dang ve so hang va so cot cua ma tran khong hop le! Nhap lai.')

def input_matrix(n,m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            while True:
                    x = float(input(''))
                    row.append(x)
                    break
                    if x :
                        try:
                              matrix.append(x)
                        except:
                             print('Phan tu cau ma tran la nhung so thuc,nhap lai.')
    return matrix

def out_put_chuyenvi(n, m, matrix):  
    print("Ma tran chuyen vi:")  
    matrix_CV = []  
    for i in range(m):  
        row_CV = []  
        for j in range(n):  
            row_CV.append(matrix[j][i]) 
        matrix_CV.append(row_CV)  
 
    for row in matrix_CV:  
        print(' '.join(map(str, row)))

n,m = nhap()
matrix = input_matrix(n,m)
out_put_chuyenvi(n,m,matrix)