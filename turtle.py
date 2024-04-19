import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the speed of the turtle (0 is the fastest)
pen.width(2)  # Set the width of the lines

# Define a function to draw a colorful square
def draw_colorful_square():
    r = random.random()  # Generate a random value for the red component
    g = random.random()  # Generate a random value for the green component
    b = random.random()  # Generate a random value for the blue component
    pen.color(r, g, b)  # Set the pen color
    for _ in range(4):
        pen.forward(50)
        pen.right(90)

# Move the turtle to the starting position
pen.penup()
pen.goto(-200, 200)
pen.pendown()

# Draw the grid of colorful squares
for _ in range(5):  # Repeat the pattern 5 times horizontally
    for _ in range(5):  # Repeat the pattern 5 times vertically
        draw_colorful_square()
        pen.forward(60)  # Move the turtle to the next position
    pen.backward(300)  # Move the turtle back to the start of the row
    pen.right(90)  # Turn the turtle to start the next row
    pen.forward(60)  # Move the turtle to the next row
    pen.left(90)  # Turn the turtle to face the right direction again

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
