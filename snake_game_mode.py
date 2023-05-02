import turtle

choice = 0

wns = turtle.Screen()
wns.title("Game Library")
wns.bgcolor("white")
wns.bgpic("snake.gif")
wns.setup(width=600, height=600)

pens = turtle.Turtle()
pens.speed(0)
pens.color("white")
pens.hideturtle()

# Making options clickable
wns.listen()


def btnclick(x, y):
    wns.listen()
    wns.onkeypress(border_free, "1")
    wns.onkeypress(border, "2")
    wns.onkeypress(walls, "3")
    wns.onkeypress(wab, "4")
    wns.onkeypress(quit, "0")


def border_free():
    choice = 1
    wns.clear()
    wns.bye()


def border():
    choice = 2
    wns.clear()
    wns.bye()


def walls():
    choice = 3
    wns.clear()
    wns.bye()


def wab():
    choice = 4
    wns.clear()
    wns.bye()


# Menu Options
pens.penup()
pens.goto(0, 200)
pens.write("Choose Game Mode!", align='center', font=("Times", 18, "normal"))

pens.penup()
pens.goto(-250, 50)
pens.write("1. Border-free", align='left', font=("Times", 12, "normal"))

pens.penup()
pens.goto(-250, 0)
pens.write("2. Borders", align='left', font=("Times", 12, "normal"))

pens.penup()
pens.goto(-250, -50)
pens.write("3. Walls", align='left', font=("Times", 12, "normal"))

pens.penup()
pens.goto(-250, -100)
pens.write("4. Walls and Borders", align='left', font=("Times", 12, "normal"))

pens.penup()
pens.goto(-250, -150)
pens.write("0. Quit Game", align='left', font=("Times", 12, "normal"))

turtle.onscreenclick(btnclick, 1)
turtle.listen()
wns.mainloop()
