import turtle

wns = turtle.Screen()
wns.title("Game Library")
wns.bgcolor("white")
wns.bgpic("snake.gif")
wns.setup(width=600, height=600)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()

delay = 0

def button(length):
    for i in range(4):
        pen.forward(length)
        pen.left(90)


def slow():
    wns.clear()
    delay = 0.1
    # import snake


def medium():
    wns.clear()
    delay = 0.05
    # import snake


def fast():
    wns.clear()
    delay = 0.01
    # import snake


# Menu Options
pen.penup()
pen.goto(0, 200)
pen.write("Choose Game Speed!", align='center', font=("Times", 18, "normal"))

pen.penup()
pen.goto(-250, 50)
pen.write("1. Slow", align='left', font=("Times", 12, "normal"))

pen.penup()
pen.goto(-250, 0)
pen.write("2. Medium", align='left', font=("Times", 12, "normal"))

pen.penup()
pen.goto(-250, -50)
pen.write("3. Fast", align='left', font=("Times", 12, "normal"))

pen.penup()
pen.goto(-250, -100)
pen.write("0. Quit Game", align='left', font=("Times", 12, "normal"))

# Making options clickable
wns.listen()


def btnclick(x, y):
    wns.listen()
    wns.onkeypress(slow, "1")
    wns.onkeypress(medium, "2")
    wns.onkeypress(fast, "3")
    wns.onkeypress(quit, "0")


turtle.onscreenclick(btnclick, 1)
turtle.listen()
wns.mainloop()
