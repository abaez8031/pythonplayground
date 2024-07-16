#####Turtle Intro######

from turtle import Turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(50):
#   timmy_the_turtle.forward(5)
#   timmy_the_turtle.penup()
#   timmy_the_turtle.forward(5)
#   timmy_the_turtle.pendown()

def draw_shape(sides):
  angle = 360 / sides
  for _ in range(sides):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(angle)

for sides in range(3,11):
  draw_shape(sides)
