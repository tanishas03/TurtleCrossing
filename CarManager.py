import random
from turtle import Turtle
COLORS = ["red", "blue", "yellow", "orange", "purple", "green"]
MOVING_DISTANCE = 5


class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = MOVING_DISTANCE
        self.hideturtle()

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car_ in self.all_cars:
            car_.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVING_DISTANCE







