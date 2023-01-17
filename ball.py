from turtle import Turtle
BALL_RADIUS = 0.8
BALL_SPEED = 4


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=BALL_RADIUS,stretch_len=BALL_RADIUS)
        self.penup()
        self.speed(BALL_SPEED)
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)


    def bounce_y(self):
        self.y_move *=-1


    def bounce_x(self):
        self.x_move*=-1





