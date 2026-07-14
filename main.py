from turtle import *
from random import randint


class Sprite(Turtle):
    def __init__(self, x, y, shape, color, step):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
        
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
        
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
        
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())


player = Sprite(0, -100, 'circle', 'orange', 5)
goal = Sprite(0, 120, 'triangle', 'green', 0)
enemy1 = Sprite(-150, 0, 'square', 'red', 5)
enemy2 = Sprite(150, 70, 'square', 'red', 5)


scr = player.getscreen()
scr.listen()

scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

exitonclick()
