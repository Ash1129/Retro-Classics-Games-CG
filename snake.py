import turtle
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.bgpic("snake.gif")
wn.tracer(0)  # Turns off the screen updates

print("Welcome to Snakes:")
print("Choose Game Mode:")
print("\t\t1. Borders-Free")
print("\t\t2. Borders")
print("\t\t3. Walls and Borders-Free")
print("\t\t4. Walls and Borders")
choice = (int(input("Game Mode: ")))

print("Choose speed level:")
print("\t\t1. Easy")
print("\t\t2. Medium")
print("\t\t3. Hard")
delay = (int(input("Game Mode: ")))

if delay == 1:
    delay = 0.1
elif delay == 2:
    delay = 0.05
elif delay == 3:
    delay = 0.01

border = turtle.Turtle()
border.hideturtle()

# Draw border
if choice == 2 or choice == 4:
    border.color("red")
    border.penup()
    border.setposition(-300, -290)
    border.pendown()
    border.pensize(10)
    for side in range(4):
        border.forward(590)
        border.left(90)
    border.hideturtle()

# Draw walls
if choice == 3 or choice == 4:
    # Down
    border.color("red")
    border.penup()
    border.setposition(-160, -200)
    border.pendown()
    border.pensize(5)
    border.forward(300)
    border.hideturtle()

    # Up
    border.color("red")
    border.penup()
    border.setposition(-160, 200)
    border.pendown()
    border.pensize(5)
    border.forward(300)
    border.hideturtle()

    # Left
    border.color("red")
    border.penup()
    border.setposition(-240, 160)
    border.pendown()
    border.pensize(5)
    border.right(90)
    border.forward(310)
    border.hideturtle()

    # Right
    border.color("red")
    border.penup()
    border.setposition(240, 160)
    border.pendown()
    border.pensize(5)
    border.forward(310)
    border.hideturtle()

# Score
score = 0
high_score = 0

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
head.left(90)
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("triangle")
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        if head.direction == "right":
            head.left(90)
        if head.direction == "left":
            head.right(90)

        head.direction = "up"


def go_down():
    if head.direction != "up":
        if head.direction == "right":
            head.right(90)
        if head.direction == "left":
            head.left(90)
        if head.direction == "stop":
            head.left(180)

        head.direction = "down"


def go_left():
    if head.direction != "right":
        if head.direction == "up":
            head.left(90)
        if head.direction == "down":
            head.right(90)
        if head.direction == "stop":
            head.left(90)

        head.direction = "left"


def go_right():
    if head.direction != "left":
        if head.direction == "up":
            head.right(90)
        if head.direction == "down":
            head.left(90)
        if head.direction == "stop":
            head.right(90)

        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def segment_move():
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)


    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    if choice == 3 or choice == 4:
        if head.xcor() == -240:
            if -140 < head.ycor() < 160:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()
                # Reset the score
                score = 0
                # Reset the delay
                delay = 0.1
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

        elif head.xcor() == 240:
            if -140 < head.ycor() < 160:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()
                # Reset the score
                score = 0
                # Reset the delay
                delay = 0.1
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

        elif head.ycor() == 200:
            if -160 < head.xcor() < 140:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()
                # Reset the score
                score = 0
                # Reset the delay
                delay = 0.1
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

        elif head.ycor() == -200:
            if -160 < head.xcor() < 140:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()
                # Reset the score
                score = 0
                # Reset the delay
                delay = 0.1
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                          font=("Courier", 24, "normal"))

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        if choice == 2 or choice == 4:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()
            # Reset the score
            score = 0
            # Reset the delay
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

        elif choice == 1 or choice == 3:
            if head.xcor() > 290:
                head.goto(head.xcor() - 600, head.ycor())
                segment_move()
            elif head.xcor() < -290:
                head.goto(head.xcor() + 600, head.ycor())
                segment_move()
            elif head.ycor() > 290:
                head.goto(head.xcor(), head.ycor() - 600)
                segment_move()
            elif head.ycor() < -290:
                head.goto(head.xcor(), head.ycor() + 600)
                segment_move()

    count = 0
    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        count += 1
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("black")
        new_segment.penup()
        pen.write("{}".format(count), align="center", font=("Courier", 12, "normal"))
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order

    segment_move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()
            # Reset the score
            score = 0
            # Reset the delay
            delay = 0.1
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
