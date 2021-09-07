from turtle import Screen
from padddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
bol = Ball()
score_board = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on :
    time.sleep(0.1)
    screen.update()
    bol.move()

    # Detect collision with wall
    if bol.ycor() > 280 or bol.ycor() < -280:
        bol.bounce_y()

    # Detect collision with paddle
    if bol.distance(r_paddle) < 20 or bol.distance(l_paddle) < 20:
        bol.bounce_x()

    # Detect R paddle misses
    if bol.xcor() > 380:
        bol.refresh_game()
        score_board.l_point()

    # Detect L paddle misses:
    if bol.xcor() < -380:
        bol.refresh_game()
        score_board.r_point()

screen.exitonclick()