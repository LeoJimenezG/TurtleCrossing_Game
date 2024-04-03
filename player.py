from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):
    # Initial configuration
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_forward(self):
        # Get the current "y" axis position and increment
        y = self.ycor() + MOVE_DISTANCE
        # Move to new position
        self.goto(0, y)

    def restart_position(self):
        self.goto(STARTING_POSITION)
