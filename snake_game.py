# PySnake.game
Simple Snake Game

# Snake Game by Siam Salman
import turtle
import time
import random

delay=0.1


#scoreboard

your_score = 0
high_score = 0

#Screen Set up
wn = turtle.Screen()
wn.title("সাপ খেলা")
wn.bgcolor("black")
wn.setup(width=660, height=560)
wn.tracer(0) #this line stop the update (for soln, game loop)

#Snake Head

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.shapesize(.9,1.7)
head.color("blue","green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(-160,-100)

segments = []

#score board
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,235)
score.write("Your Score: 0      I     High Score: 0", align="center" , font=("Arial", 24, "normal"))


#functions

def go_up():
 if head.direction != "down":
  head.direction = "up"

def go_down():
 if head.direction != "up":
  head.direction = "down"

def go_left():
 if head.direction != "right":
  head.direction = "left"

def go_right():
 if head.direction != "left":
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

#Key Set Up
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Game loop
while True:
 wn.update()

#collision with border
 if head.xcor()>310 or head.xcor()<-310 or head.ycor()>235 or head.ycor()<-255:
  time.sleep(1)
  head.goto(0,0)
  head.direction = "stop"

  for segment in segments:
   segment.goto(1000, 1000)

  # clear segments list
   segments.clear()

  #reset score & delay
  your_score = 0
    delay = 0.1

  score.clear()
  score.write("Your Score:{}     I     High Score: {}".format(your_score, high_score), align="center",
              font=("Arial", 24, "normal"))

 #collision with food

    if head.distance(food) < 20:
    #moving food
    x = random.randrange(-310, 310,20)
    y = random.randrange(-255, 235,20)
    food.goto(x, y)

   # snake body segment
    body = turtle.Turtle()
    body.speed(0)
    body.shape("circle")
    body.color("indigo")
    body.penup()
    segments.append(body)

    # shorten the delay
    delay -= 0.001

    # increase score
    your_score += 10

    if your_score > high_score:
        high_score = your_score

    score.clear()
    score.write("Your Score:{}     I     High Score: {}".format(your_score, high_score), align="center",
                    font=("Arial", 24, "normal"))

# move the end segments first in reverse order
 for index in range(len(segments) - 1, 0, -1):
     x = segments[index - 1].xcor()
     y = segments[index - 1].ycor()
     segments[index].goto(x, y)

 #move the body 0 to head
  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

move()

 #collision with body
 for segment in segments:
    if segment.distance(head) <20:
      time.sleep(1)
     head.goto(0, 0)
     head.direction = "stop"

     # hide segments
     for segment in segments:
        segment.goto(1000, 1000)

     # clear segments list
     segments.clear()
     # reset score & delay
     your_score = 0
     delay = 0.1
     # update score
     score.clear()
     score.write("Your Score: {}      I     High Score: {}".format(your_score, high_score), align="center",
               font=("Arial", 24, "normal"))

time.sleep(delay)


wn.mainloop()
#শেষ 
