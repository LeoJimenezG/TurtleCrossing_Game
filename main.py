import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Score

# Screen properties
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightgrey")
screen.title("Turtle Crossing")
screen.tracer(0)

# Ask if user wants to play
user_play = screen.textinput(title="Turtle Crossing", prompt="Dou you want to play? Y/N").upper()
if user_play == "Y":
    game_on = True
else:
    game_on = False

player = Player()
car = Car()
score = Score()

# Move-set
screen.listen()
screen.onkey(key="Up", fun=player.move_forward)


# Extra function to use and avoid being
# able to move the turtle after game over
def nothing():
    pass


# Maintain the game on
collision = False
while game_on:
    time.sleep(0.1)
    screen.update()
    # Create cars as long as the user has not lost
    if not collision:
        car.create_car()
        car.move_cars()

    # Check if the player collied with any car
    for i in car.cars:
        if player.distance(i) < 25:
            collision = True
            screen.onkey(key="Up", fun=nothing)
            score.game_over()

    # Check if the player has reached the finish line
    if player.ycor() > 250:
        score.increment_score()
        player.restart_position()
        car.increase_move_distance()
