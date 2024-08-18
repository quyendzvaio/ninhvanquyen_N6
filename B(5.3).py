import random  

def create_student_accounts(N):    
    departments = ["CNTT", "KHMT", "KTPM", "HTTT"]    
    accounts = {}  
    for i in range(N):    
        student_id = f"20236{i+1:04d}" 
        random_department = random.choice(departments)  
        password = f"{random_department}{student_id}"
        accounts[f"Account{i+1}"] = {  
            "Username": student_id,  
            "Password": password  
        }
    return accounts  

N = int(input("Nhập số lượng tài khoản sinh viên (10 <= N <= 100000): "))  

if 10 <= N <= 100000:  
    student_accounts = create_student_accounts(N)  
    for account, info in student_accounts.items():  
        print(f"{account}: {info}")  
else:  
    print("Số lượng tài khoản sinh viên phải nằm trong khoảng từ 10 đến 100000.")