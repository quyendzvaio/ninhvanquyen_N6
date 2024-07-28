def chuan_hoa(name):    
    name = ' '.join(name.strip().split())  
    words = name.split()    
    normalized_words = []  
    
    for word in words:  
        first_char = word[0].upper() if word else ''    
        normalized_word = first_char + word[1:]  
        normalized_words.append(normalized_word)  
    return ' '.join(normalized_words)  

input_name = input("Nhập họ và tên cần chuẩn hóa: ")  
ten_chuan = chuan_hoa(input_name)  
print("Chuỗi họ tên đã được chuẩn hóa là:", ten_chuan)