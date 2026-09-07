from turtle import *
import random
screen = Screen()
is_race_on = False
all_turtles = []

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make a bet.", prompt="Which turtle will win the race? Pick a color:")
colors = ["red","orange","yellow","green","blue","purple"]
y_coord = [100, 70, 40, 10, -20, -50]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230, y_coord[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                is_race_on = False
                print(f"You won the bet! {winning_turtle} turtle wins the race!")
            else:
                print(f"You lost the bet! {winning_turtle} turtle wins the race!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()