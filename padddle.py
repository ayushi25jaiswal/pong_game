from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=0.5)
        self.penup()
        self.goto(x_cor, y_cor)
        self.speed("fastest")

    def up(self):
        y_cor = self.ycor() + 40
        self.goto(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - 40
        self.goto(self.xcor(), y_cor)