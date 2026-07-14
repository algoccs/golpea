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

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist <= 30:
            return True
        else:
            return False
    
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def move(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)

player = Sprite(0, -100, 'circle', 'orange', 5)
goal = Sprite(0, 120, 'triangle', 'green', 0)
enemy1 = Sprite(-150, 0, 'square', 'red', 10)
enemy1.set_move(-150, 0, 150, 0)
enemy2 = Sprite(150, 70, 'square', 'red', 10)
enemy2.set_move(150, 70, -150, 70)


scr = player.getscreen()
scr.listen()

scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

points = 0

while points < 3:
    enemy1.move()
    enemy2.move()


    if player.is_collide(goal):
        points += 1
        player.goto(0, -100)
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        goal.hideturtle()
        break

if points == 3:
    enemy1.hideturtle()
    enemy2.hideturtle()
    player.hideturtle()
    # RENDERIZAR SU TEXTO DE VICTORIA
else:
    # RENDERIZAR SU TEXTO DE DERROTA
    goal.hideturtle()

exitonclick()
