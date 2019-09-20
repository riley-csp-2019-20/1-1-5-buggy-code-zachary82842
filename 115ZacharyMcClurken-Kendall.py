#   a115_buggy_image.py
import turtle as trtl

drawer = trtl.Turtle()
drawer.pensize(40)
drawer.circle(20)
legs = 8
length = 100
spacing = 360 / legs
drawer.pensize(5)
start = 0
while (start < legs):
  drawer.goto(0,20)
  drawer.setheading(spacing*start)
  drawer.forward(length)
  start = start + 1


drawer.penup()
drawer.goto(0,60)
drawer.pendown()
drawer.begin_fill()
drawer.circle(20)
drawer.end_fill()

drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop()