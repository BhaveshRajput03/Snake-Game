#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import time
import random

# Screen setup
window = turtle.Screen()
window.title("Snake Game by Sneha")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  # Turns off the screen updates

# Snake setup
snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Snake body (list to store the positions of snake segments)
snake_body = []

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score
score = 0

# Function to change direction
def move_up():
    if snake.direction != "down":
        snake.direction = "up"

def move_down():
    if snake.direction != "up":
        snake.direction = "down"

def move_left():
    if snake.direction != "right":
        snake.direction = "left"

def move_right():
    if snake.direction != "left":
        snake.direction = "right"

# Function for moving the snake
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings
window.listen()
window.onkey(move_up, "w")
window.onkey(move_down, "s")
window.onkey(move_left, "a")
window.onkey(move_right, "d")

# Game loop
while True:
    window.update()

    # Check for collision with border
    if (snake.xcor() > 290 or snake.xcor() < -290 or
        snake.ycor() > 290 or snake.ycor() < -290):
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"
        
        # Reset snake body
        for segment in snake_body:
            segment.goto(1000, 1000)  # Move segments off screen
        snake_body.clear()

        score = 0  # Reset score
    
    # Check for collision with food
    if snake.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        snake_body.append(new_segment)

        # Increase the score
        score += 10
        print(f"Score: {score}")

    # Move the end segments of the snake body first in reverse order
    for index in range(len(snake_body) - 1, 0, -1):
        x = snake_body[index - 1].xcor()
        y = snake_body[index - 1].ycor()
        snake_body[index].goto(x, y)

    # Move segment 0 to the position of the head
    if len(snake_body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].goto(x, y)

    move()

    # Check for collision with the body
    for segment in snake_body:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            
            # Reset snake body
            for segment in snake_body:
                segment.goto(1000, 1000)
            snake_body.clear()

            score = 0  # Reset score
    
    time.sleep(0.1)  # Control the game speed


# In[ ]:




