import turtle
from random import *
from turtle import *

from freegames import vector

print("Welcome to Snakes:")
print("Choose Game Mode:")
print("\t\t1. Easy")
print("\t\t2. Medium")
print("\t\t3. Hard")
choice = (int(input("Game Mode: ")))

print("Choose speed level:")
print("\t\t1. Slow")
print("\t\t2. Medium")
print("\t\t3. Fast")
delay = (int(input("Game Mode: ")))

# Difficulty modes
if choice == 1:
    choice = 2
elif choice == 2:
    choice = 3
elif choice == 3:
    choice = 4

# Speed modes
if delay == 1:
    delay = 50
elif delay == 2:
    delay = 25
elif choice == 3:
    delay = 15

dots = vector(0, 0)
balls = []

wn = turtle.Screen()
wn.title("Dot Game")
wn.bgcolor("Green")
wn.setup(width=600, height=600)
wn.bgpic("dotgame.gif")


# Move bird up in response to screen tap.
def tap(x, y):
    up = vector(0, 30)
    dots.move(up)


# Return True if point on screen.
def inside(point):
    return -300 < point.x < 300 and -300 < point.y < 300


# Draw screen objects.
def draw(alive):
    clear()
    goto(dots.x, dots.y)
    if alive:
        dot(10, 'blue')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()


# Update object positions.
def move():
    # Move balls downwards
    dots.y -= 5

    # Move balls left
    for ball in balls:
        ball.x -= 3

    # Difficulty probability of the number of balls on screen
    if 0 <= randrange(0, 10) < choice:
        y = randrange(-299, 299)
        ball = vector(299, y)
        balls.append(ball)

    # Removing balls from the screen
    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(dots):
        draw(False)
        return

    # Hitting the balls
    for ball in balls:
        if abs(ball - dots) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, delay)


hideturtle()
penup()
tracer(False)
onscreenclick(tap)
move()
mainloop()
