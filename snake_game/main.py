from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

is_on = True
while is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

screen.exitonclick()