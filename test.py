# import math
# from turtle import*
# speed(10)
# bgcolor('black')

# def h1(a):
#     return 15*math.sin(a)**3

# def h2(a):
#     return 13*math.cos(a) - 6*\
#     math.cos(2*a) - 3*\
#     math.cos(3*a) - \
#     math.cos(4*a)
# penup()
# goto(0,0)
# pendown()
# for i in range(2000):
#     goto(h1(i)*20 , h2(i)*20)
#     for i in range(2):
#         color('#FF6699')
#     goto(0,0)

# penup()
# goto(-180, -40)
# pendown()
# color('pink')
# write('do dang iu', font= ('Comic SanS MS'))
# hideturtle()
# done()
    
import turtle  
list = ['red','yellow','orange','pink','white']

def draw_heart():  
    for i in range(5) :

        turtle.fillcolor(list[i])  # Chọn màu đỏ để tô màu trái tim  
        turtle.begin_fill()      # Bắt đầu quá trình tô màu  
        
        turtle.left(140)         # Quay bút vẽ về phía trái  
        turtle.forward(224 + i*20)      # Di chuyển bút vẽ về phía trước 224 đơn vị  
        turtle.circle(-112 + i*20, 200) # Vẽ một phần vòng tròn với bán kính -112 và góc 200 độ  
        turtle.left(120)         # Quay bút vẽ 120 độ sang trái  
        turtle.circle(-112 + i*20, 200) # Vẽ một phần vòng tròn khác  
        turtle.forward(224)      # Di chuyển bút vẽ về phía trước 224 đơn vị  
        
        turtle.end_fill()        # Kết thúc quá trình tô màu  

turtle.speed(1)              # Thiết lập tốc độ vẽ  
draw_heart()                 # Gọi hàm để vẽ hình trái tim  
turtle.hideturtle()          # Ẩn bút vẽ (để không hiển thị bút khi vẽ xong)  
turtle.done()               # Kết thúc đồ họa Turtle

# import turtle  

# def draw_star(size): 
#     turtle.begin_fill() 
#     for _ in range(5):             # Lặp lại 5 lần để vẽ ngôi sao 5 cánh 
#         turtle.forward(size)       # Di chuyển bút vẽ về phía trước với kích thước đã chỉ định  
#         turtle.right(144)          # Quay bút vẽ 144 độ sang phải  
#     turtle.end_fill()
# turtle.speed(1)                   # Thiết lập tốc độ vẽ  
# turtle.fillcolor('yellow')
# draw_star(200)                    # Gọi hàm để vẽ ngôi sao với kích thước 100  
# turtle.hideturtle()               # Ẩn bút vẽ  
# turtle.done()                     # Kết thúc đồ họa Turtle

# import turtle  

# def draw_circle(radius):  
#     turtle.circle(radius)          # Sử dụng hàm circle để vẽ hình tròn với bán kính đã chỉ định  

# turtle.speed(1)                   # Thiết lập tốc độ vẽ  
# draw_circle(100)                   # Gọi hàm để vẽ hình tròn với bán kính 100  
# turtle.hideturtle()                # Ẩn bút vẽ  
# turtle.done()                      # Kết thúc đồ họa Turtle

# import turtle  

# def draw_rectangle(color, x, y, width, height):  
#     turtle.penup()                  # Nhấc bút lên để không vẽ  
#     turtle.goto(x, y)               # Đưa bút đến vị trí (x, y)  
#     turtle.pendown()                # Đặt bút xuống để vẽ  
#     turtle.fillcolor(color)         # Chọn màu tô  
#     turtle.begin_fill()             # Bắt đầu tô màu  
#     for _ in range(2):              # Vẽ hình chữ nhật  
#         turtle.forward(width)       # Vẽ chiều dài  
#         turtle.left(90)             # Quay 90 độ  
#         turtle.forward(height)      # Vẽ chiều cao  
#         turtle.left(90)             # Quay 90 độ  
#     turtle.end_fill()               # Kết thúc tô màu  

# def draw_star(size):  
#     for _ in range(5):              # Vẽ 5 cánh của ngôi sao  
#         turtle.forward(size)        # Di chuyển về phía trước  
#         turtle.right(144)           # Quay 144 độ  

# # Thiết lập  
# turtle.speed(3)                    # Tốc độ vẽ nhanh nhất  
# turtle.bgcolor('white')            # Màu nền trắng  

# # Vẽ cờ đỏ  
# draw_rectangle('red', -150, 100, 300, 200)  

# # Vẽ sao vàng  
# turtle.penup()  
# turtle.goto(-20, 210)                 # Đưa bút đến vị trí vẽ sao  
# turtle.pendown()  
# turtle.color('yellow')             # Chọn màu vàng  
# turtle.begin_fill()                # Bắt đầu tô màu  
# draw_star(50)                      # Vẽ ngôi sao với kích thước 50  
# turtle.end_fill()                  # Kết thúc tô màu  

# # Kết thúc  
# turtle.hideturtle()                # Ẩn bút vẽ  
# turtle.done()                      # Kết thúc đồ họa Turtle