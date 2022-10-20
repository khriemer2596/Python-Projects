# Simple Pong 
# uses turtle module

import turtle
import winsound

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_left = 0
score_right = 0

# Left Paddle
left = turtle.Turtle() # object.Class
left.speed(0)
left.shape("square")
left.color("white")
left.penup() # penup prevents program from drawing lines while moving
left.shapesize(stretch_wid=5, stretch_len=1) # default square 20 x 20; this will multiply the dimensions
left.goto(-350,0) # about half of the window pixels

# Right Paddle
right = turtle.Turtle() # object.Class
right.speed(0)
right.shape("square")
right.color("white")
right.penup() # penup prevents program from drawing lines while moving
right.shapesize(stretch_wid=5, stretch_len=1) # default square 20 x 20; this will multiply the dimensions
right.goto(350,0) # about half of the window pixels

# Ball
ball = turtle.Turtle() # object.Class
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup() # penup prevents program from drawing lines while moving
ball.goto(0,0) 
ball.dx = 0.25 # delta x of the ball in pixels
ball.dy = 0.25 # delta y of the ball in pixels

# Pen
pen = turtle.Turtle() # to draw the scoreboard
pen.speed(0)
pen.color("white")
pen.penup() # every turtle starts dead center of screen
pen.hideturtle()
pen.goto(0,260) # scoreboard location
pen.write("Left: 0  Right: 0", align="center", font=("Courier", 24, "normal"))


# Function
def left_up():
    y = left.ycor() # part of turtle. returns y coordinate
    y += 20 #adds pixels to y coord
    left.sety(y)

def left_down():
    y = left.ycor() # part of turtle. returns y coordinate
    y -= 20 #adds pixels to y coord
    left.sety(y)

def right_up():
    y = right.ycor() # part of turtle. returns y coordinate
    y += 20 #adds pixels to y coord
    right.sety(y)

def right_down():
    y = right.ycor() # part of turtle. returns y coordinate
    y -= 20 #adds pixels to y coord
    right.sety(y)

# Keyboard binding
win.listen() # tells window to listen to keyboard input
win.onkeypress(left_up,"w") # when user presses w, it'll call that function
win.onkeypress(left_down,"s")
win.onkeypress(right_up,"Up") # up arrow
win.onkeypress(right_down,"Down") # down arrow

# Main game loop
while True:
    win.update() # update screen every time loop goes

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290: # top
        ball.sety(290)
        ball.dy *= -1 # reverses direction of ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290: # bottom
        ball.sety(-290)
        ball.dy *= -1 # reverses direction of ball
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 390: # right
        ball.goto(0,0) # point
        ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write("Left: {}  Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390: # left
        ball.goto(0,0) # point
        ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write("Left: {}  Right: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))
    
    # Paddle and Ball collisions
    if ball.xcor() > 340 and (ball.xcor() < 350) and (ball.ycor() < right.ycor() + 40 and ball.ycor() > right.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() < -340 and (ball.xcor() > -350) and (ball.ycor() < left.ycor() + 40 and ball.ycor() > left.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

