from turtle import Turtle, Screen
import random as rd


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Yellow")
        self.speed(0)
        x = rd.randint(-280, 280)
        y = rd.randint(-280, 280)
        self.goto(x, y)

    def old_food(self):
        self.hideturtle()








