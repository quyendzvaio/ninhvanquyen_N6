# class person:
#     sound = 'voice' #biến intance
#     salary = 1.7
#     def __init__(self,name,age,coet): #khởi tạo self(bắt buộc)
#         self._name = name #biến class,kieu protect
#         self.__age = age #biến class,bien nay duoc private
#         self.coet = 0.6 #kieu pulic
#     def sleep(self):
#         print(self._name + 'is sleeping')

# student = person('Q ',20, 0.6) #student là một đối tượng
# student.sleep()
# print(student.coet)
# class nv:
#     _super_.peson

class Person:  
    def __init__(self, name, birt, address):  
        self.name = name  
        self.birt = birt  
        self.address = address  

    def infor(self):  
        return self.name, self.birt, self.address  

class KYSU(Person):  
    def __init__(self, name, birt, address, major, year):  
        super().__init__(name, birt, address)  # Gọi __init__ của lớp Person để khởi tạo các thuộc tính chung  
        self.major = major  
        self.year = year  

    def SV(self):  
        return self.major, self.year  

    def __str__(self):  
        person_info = self.infor()  # Gọi phương thức infor từ lớp cơ sở  
        return f"Name: {person_info[0]}, Birth: {person_info[1]}, Address: {person_info[2]}, Major: {self.major}, Year: {self.year}"  

# Tạo một instance của KYSU  
Q = KYSU('Q', 24, 'BG', 'IT', 2026)  
print(Q)  # In thông tin về đối tượng KYSU

