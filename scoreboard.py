from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.highest_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(0, 270)
        self.write(f"Score: {self.score}", False, "center", ('Arial', 18, 'normal'))
        self.setposition(0, 250)
        self.write(f"Highest score: {self.highest_score}", False, "center", ('Arial', 9, 'normal'))


    def reset(self):
        if self.score > self.highest_score:
            with open("data.txt" , "w") as file:
                self.highest_score = self.score
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()



    def add_score(self):
        self.score += 1
        self.update_scoreboard()
