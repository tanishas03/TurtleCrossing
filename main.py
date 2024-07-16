import time
from turtle import Screen
from Player import Player
from Scoreboard import Scoreboard
from CarManager import Car

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
player = Player()
score = Scoreboard()
car = Car()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    # Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect successful crossing
    if player.at_finish_line():
        player.go_to_start()
        car.level_up()
        score.increment()

screen.exitonclick()
