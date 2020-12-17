from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
with open("data.txt") as file:
    highest_score = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 283)
        self.score = 0
        self.highest_score = int(highest_score)
        self.color("white")
        self.hideturtle()
        self.show_score()

    def update_score(self):
        self.clear()
        self.score += 1
        if self.score >= self.highest_score:
            self.highest_score = self.score
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score} Highest score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highest_score))
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)


