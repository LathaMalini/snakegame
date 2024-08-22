import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("welcome to my snake game...")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")

    #collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        is_game_on = False
        scoreboard.goto(0,0)
        scoreboard.write("GameOver", font=("courier", 20, "bold"), align="center")

    #collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)< 10:
            is_game_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("GameOver", font=("courier", 20, "bold"), align="center")


screen.exitonclick()

