# n1 = input("").split()
# N = int(n1[0])
# X = int(n1[1])
# l = []
# l2 = []
# for n in range(X):
#     n2 = input("").split()
#     l.extend(n2)
# for m in l:
#     l2.append(int(m))

# k = N
# for num in range(N):
#     print(sum((l2[N-k::5]))/X)
#     k -= 1


# import turtle
# big_line = 100
# little_line = 50
# angle = 90
# turtle.left(angle)
# turtle.forward(big_line)
# count = 0
# while count < 4:
#     turtle.right(angle//2)
#     if count != 3:
#         turtle.forward(little_line)
#     else:
#         turtle.forward(big_line)
#     count = count + 1
# turtle.right(90)
# turtle.forward(130)


# import turtle
# count = 0
# while(count < 180):
#     turtle.forward(2)
#     turtle.right(1)
#     count = count + 1
# turtle.right(45)
# turtle.forward(300)
# turtle.left(90)
# turtle.back(150)
# turtle.right(45)
# turtle.back(250)
# import turtle
# def drawSquare ( ttl , x , y , length ) :
#     ttl . penup ()
#     # raise the pen
#     ttl . goto (x , y )
#     # move to starting position
#     ttl . setheading (0)
#     # point turtle east
#     ttl . pendown ()
#     # lower the pen
#     for count in range (4) :
# # draw 4 sides :
#         ttl . forward ( length )
#         ttl . right (90)
#     ttl . penup ()
# # raise the pen
# Bob = turtle . Turtle ()
# Bob . speed (10)
# Bob . pensize (3)
# drawSquare ( Bob , 0 , 0 , 100 )
# turtle . done ()


# import math

# print(dir(math))
# مساحة المستطيل

# high = int(input("Write the High: "))
# width = int(input("Write the Width: "))
# mostatil = high * width
# print('misaht-almostatil = high X width')
# print(f'misaht-almostatil = {high} X {width} = {mostatil}')
#===========================================================================

#مساحة المثلث
# high_of_base = int(input("Write the High of the Base: "))
# high = int(input("Write the High: "))
# triangle_area = (1/2) * high_of_base * high
# print("triangle_area = (1/2) X high_of_base *X high")
# print(f"triangle_area = (1/2) X {high_of_base} X {high} = {triangle_area}")
#===========================================================================

#مساحة المربع
# high_of_rib = int(input("Write the High of the Rib: "))
# square_area = high_of_rib * high_of_rib
# print("square_area = High of rib X High of rib")
# print(f"square_area = {high_of_rib} X {high_of_rib} = {square_area}")
#===========================================================================

# print("But a number in your Head Between 1 and 10")
# choose_number = int(input("Done? "))
# print("add the number to him self")
# choose_number = int(input("Done? "))
# print("Your Father give you the same number")
# choose_number = int(input("Done? "))
# print("Through Half of It in the sea")
# choose_number = int(input("Done? "))
# print("Return to your father What he Give you")
# choose_number = int(input("Done? "))

# choose_number = int(input("Done? "))
#===========================================================================

# from turtle import *

# def move_turtle(x,y):
#     penup()
#     goto(x,y)
#     pendown()

# def turtle_head(xx,yy):
#     penup()
#     home()
#     goto(xx,yy)
#     pendown()

# pensize(5)

# # green triangle
# turtle_head(-120,-60)
# begin_fill()
# color('green')
# left(90)
# forward(120)
# right(127)    # tri
# forward(100)  #    ang
# right(107)    #       le
# forward(100)
# end_fill()

# # red part
# turtle_head(-120,60)
# begin_fill()
# color('red')
# forward(240)
# right(90)
# forward(40)
# right(90)
# forward(182)
# end_fill()

# #balck part
# turtle_head(-120,-60)
# begin_fill()
# color('black')
# forward(240)
# left(90)
# forward(40)
# left(90)
# forward(182)
# end_fill()

# exitonclick()

def main() :
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: ") )
    for i in range(10) :
        x = 3.9 * x * (1-x)
        print(x)
main()