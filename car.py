from turtle import Turtle
import random

COLOURS = ["red", "orange", "purple", "green", "blue", "yellow", "black"]
DISTANCE_INCREMENT = 10


class Car:
    def __init__(self):
        self.cars = []
        self.starting_move_distance = 5

    def create_car(self):
        # Generate a random number
        random_number = random.randint(1, 6)
        # If the random number is gotten, create a car
        if random_number == 2:
            # Car attributes
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.color(random.choice(COLOURS))
            y = random.randint(-250, 250)
            new_car.goto(400, y)
            self.cars.append(new_car)

    def move_cars(self):
        # Use the list of the cars and move them all
        for car in self.cars:
            car.backward(self.starting_move_distance)

    def increase_move_distance(self):
        # Increase the speed by the constant amount
        self.starting_move_distance += DISTANCE_INCREMENT
