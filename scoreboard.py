from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 15, "bold")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        # self.high_score = 0
        self.write(f"score= {self.score}", align=ALIGNMENT, font=FONT)

    #
    # def reset(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #     self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"score= {self.score}", align=ALIGNMENT, font=FONT)
