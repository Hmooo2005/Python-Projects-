import turtle

window = turtle.Screen()
window.title("Abkar🦄")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


loh1= turtle.Turtle()
loh1.speed(0)
loh1.shape("square")
loh1.color("blue")
loh1.shapesize(stretch_wid=5, stretch_len=1)
loh1.penup()
loh1.goto(-350,0)

loh2= turtle.Turtle()
loh2.speed(0)
loh2.shape("square")
loh2.color("red")
loh2.shapesize(stretch_wid=5, stretch_len=1)
loh2.penup()
loh2.goto(350,0)

ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = -1

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player1: {score1}   Player2: {score2}", align="center", font=("Courier",24,"normal"))


def loh1_up():
    y = loh1.ycor()
    y += 20
    loh1.sety(y)

def loh1_down():
    y = loh1.ycor()
    y -= 20
    loh1.sety(y)

def loh2_up():
    y = loh2.ycor()
    y += 20
    loh2.sety(y)

def loh2_down():
    y = loh2.ycor()
    y -= 20
    loh2.sety(y)

window.listen()
window.onkeypress(loh1_up, "w")
window.onkeypress(loh1_down, "s")
window.onkeypress(loh2_up, "i")
window.onkeypress(loh2_down, "k")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <- 290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player1: {score1}   Player2: {score2}", align="center", font=("Courier",24,"normal"))


    if ball.xcor() <- 390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player1: {score1}   Player2: {score2}", align="center", font=("Courier",24,"normal"))


    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < loh2.ycor() + 40 and ball.ycor() > loh2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < loh1.ycor() + 40 and ball.ycor() > loh1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
