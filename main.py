from turtle import Screen
from paddle import Paddle_1, Paddle_2
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
ball = Ball()
scoreboard = Scoreboard()
paddle_r = Paddle_1()
paddle_l = Paddle_2()
screen.setup(height = 600, width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.onkeypress(key="w", fun = paddle_l.move_up)
screen.onkeypress(key="s", fun = paddle_l.move_down)
screen.onkeypress(key="Up", fun = paddle_r.move_up)
screen.onkeypress(key="Down", fun = paddle_r.move_down)

is_game_on = True
hit_count = 0
sleep = 0.05
while is_game_on:
    screen.update()
    time.sleep(sleep)
    ball.move()
    if hit_count>=3 and sleep>0.01:
        hit_count = 0
        sleep -= 0.01

    if ball.ycor()>185 or ball.ycor()<-280:
        ball.bounce_y()

    if (ball.xcor()>320 and ball.distance(paddle_r)<67) or (ball.xcor()<-320 and ball.distance(paddle_l)<67) :
        if ball.xcor()>355 or ball.xcor()<-355:
            continue
        ball.bounce_x()
        hit_count+=1

    if ball.xcor()>400:
        scoreboard.l_score+=1
        scoreboard.update_scoreboard()
        ball.goto(0,0)
        sleep = 0.05

    if ball.xcor()<-400:
        scoreboard.r_score+=1
        scoreboard.update_scoreboard()
        ball.goto(0,0)
        sleep = 0.05


    if scoreboard.l_score==3 or scoreboard.r_score==3:
        is_game_on = False
        scoreboard.game_over()










screen.exitonclick()