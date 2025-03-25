import turtle

# Create a turtle object
flower = turtle.Turtle()

# Set the speed of the turtle
flower.speed(10)

# Set the color of the flower
flower.color("red")

# Draw the flower shape
for _ in range(36):
    flower.forward(100)
    flower.right(45)
    flower.forward(100)
    flower.right(135)
    flower.forward(100)
    flower.right(45)
    flower.forward(100)
    flower.right(135)
    flower.right(10)

# Hide the turtle
flower.hideturtle()

# Exit the turtle graphics window
turtle.done()
