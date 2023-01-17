from turtle import Turtle
PADDLE_XCOR = 355
PADDLE_YCOR = -10
PADDLE_WIDTH = 4
PADDLE_LENGTH = 0.8
PADDLE_MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()



    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH)
        self.color("white")
        self.speed("fast")
        self.penup()

    def move_up(self):
        if self.ycor()<145:
            self.goto(self.xcor(), self.ycor() + PADDLE_MOVE_DISTANCE)

    def move_down(self):
        if self.ycor()>-250:
            self.goto(self.xcor(), self.ycor() - PADDLE_MOVE_DISTANCE)


class Paddle_1(Paddle):
    def __init__(self):
        super().__init__()
        self.create_paddle()
        self.goto(PADDLE_XCOR,PADDLE_YCOR)






class Paddle_2(Paddle):
    def __init__(self):
        super().__init__()
        self.create_paddle()
        self.goto(-PADDLE_XCOR,PADDLE_YCOR)


