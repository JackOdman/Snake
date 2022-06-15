from turtle import Turtle
FONT = ("Courier", 30, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.file = open("Scoreboard.txt", 'r')
        self.score = 0
        self.high_score = int(self.file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            with open("Scoreboard.txt", mode="w") as new_score:
                new_score.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def new_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.goto(0, 0)
        self.penup()
        self.write("Game Over", align="center", font=FONT)
        self.file.close()
