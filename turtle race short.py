#Turtle Race
#Frank Rusinovich

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

#create the race course
for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

#turtle 1: ada
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
  ada.right(36)

#turtle 2: bob
bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(72):
  bob.left(5)

#start the race!
for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
