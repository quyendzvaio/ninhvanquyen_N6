
#import thu vien nay de dictionary duoc fomat dep hon
my_dict = {
    'name':'Q',
    'age':'20',
    'score' : {
        'math': '10',
        'eng' : '1'
    }
}
print(my_dict['name'])
print(my_dict['score']['math'])

#truy xuat phan tu trong dictionary
for (key,value) in my_dict.items():
    print(key,value)