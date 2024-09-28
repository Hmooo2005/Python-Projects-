import turtle
# print(dir(turtle))
#=========================================================

#Triangle
# turtle.forward(200)
# turtle.left(90)
# turtle.forward(200)
# turtle.left(135)
# turtle.forward(282.842712474619)

#============================================================

#Square
# num = 4
# while num > 0:
#     turtle.forward(200)
#     turtle.left(90)
#     num -= 1

#=================================================================
    
#Rectangle
# num = 2
# while num > 0:
#     turtle.forward(200)
#     turtle.left(90)
#     turtle.forward(100)
#     turtle.left(90)
#     num -= 1
    
#=================================================================

# Circle
# num = 360
# while num > 0:
#     turtle.forward(2)
#     turtle.left(1)
#     num -= 1
    
#=================================================================

#Star
# num = 5
# while num > 0:
#     turtle.forward(200)
#     if num ==2:
#         turtle.left(141)
#     elif num == 5:
#         turtle.left(150)
#     else:
#         turtle.left(140)
#     num -= 1

#==================================================================

count = 400
while count > 0:
    if count == 400:
        turtle.right(0)
    else:
        turtle.right(1)
    turtle.forward(200)
    turtle.right(90)
    count-=1




turtle.exitonclick()