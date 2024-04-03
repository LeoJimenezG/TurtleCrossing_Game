from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Score(Turtle):
    # Initial configuration
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-380, y=250)
        self.score = 0
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    # Increment and update the score
    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    # Show the game over message
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align="center", font=FONT)
