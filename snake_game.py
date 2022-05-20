from turtle import *
import turtle
from random import randrange
from freegames import square, vector

wn = turtle.Screen()
wn.title("snake game (mahadev)")
wn.bgcolor('black')
wn.tracer(0)

Snake = turtle.Turtle()
Snake.color("black")
Snake.speed(0)
Snake.penup()
Snake.setpos(-140,200)
Snake.write("HUNGRY SNAKE", font=("Algerian",30,"bold") )
Snake.penup()
Snake.hideturtle()
Snake.screen.bgpic("s22.gif")
  
 

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

 
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "return True if head inside boundaries."
    return -360< head.x < 345 and -290 < head.y < 290
     

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        print("GAME OVER")
        square(head.x, head.y, 10,'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        

    clear()

    for body in snake:
        square(body.x, body.y, 10, "black")

    square(food.x, food.y, 10, 'blue')
    update()
    ontimer(move, 150)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
