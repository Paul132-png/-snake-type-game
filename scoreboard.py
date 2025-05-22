from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,270)
        self.hideturtle()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.score = 0

    def update(self):
        self.clear()
        self.write(f"My score: {self.score}  High score: {self.highscore}", move=False, align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update()
    def increase_score(self):
        self.score += 1
        self.update()