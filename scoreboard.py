from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.beautify()
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Contour", 40, 'normal'))
        self.goto(+200, 200)
        self.write(self.r_score, align="center", font=("Contour", 40, 'normal'))


    def update_scoreboard(self):
        self.clear()
        self.beautify()
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Contour", 40, 'normal'))
        self.goto(+200, 200)
        self.write(self.r_score, align="center", font=("Contour", 40, 'normal'))



    def beautify(self):
        for i in range(190,-301,-10):
            self.goto(0,i)
            self.write("|",align="center",font=("Countour",5,'bold'))

        for i in range(400,-401,-10):
            self.goto(i, 190)
            self.write("-", align="center", font=("Countour", 5, 'bold'))

        self.goto(0,200)
        self.write("PONG!", align="center", font=("Comic Sans MS",50,'bold'))


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over. " , align="center", font=("Contour",30,'normal'))







