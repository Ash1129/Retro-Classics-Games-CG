import turtle

wns = turtle.Screen()
wns.title("Game Library")
wns.bgcolor("white")
wns.bgpic("retro.gif")
wns.setup(width=600, height=600)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()


def pacman():
    wns.clear()
    import pacman


def snake():
    wns.clear()
    import snake


def dotgame():
    wns.clear()
    import DotGame


# Menu Options
pen.penup()
pen.goto(0, 200)
pen.write("Welcome to our Game Library!", align='center', font=("Times", 18, "normal"))

pen.penup()
pen.goto(-250, 50)
pen.write("1. Pacman", align='left', font=("Times", 12, "normal"))

pen.penup()
pen.goto(-250, 0)
pen.write("2. Snake", align='left', font=("Times", 12, "normal"))

pen.penup()
pen.goto(-250, -50)
pen.write("3. Dot-Game", align='left', font=("Times", 12, "normal"))

pen.penup()
pen.goto(-250, -100)
pen.write("0. Quit Game", align='left', font=("Times", 12, "normal"))

# Making options clickable
wns.listen()
wns.onkeypress(pacman, "1")
wns.onkeypress(snake, "2")
wns.onkeypress(dotgame, "3")
wns.onkeypress(dotgame, "3")
wns.onkeypress(quit, "0")

turtle.listen()
wns.mainloop()
