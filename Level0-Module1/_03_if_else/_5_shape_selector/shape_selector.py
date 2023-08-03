import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

# if __name__ == '__main__':
    # window = Tk()
    # window.withdraw()

    # Make a new turtle
    # turtle_eight = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
shape = input("Enter a shape to draw.")

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    turtle_eight = turtle.Turtle()
    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'Square' or shape == 'square' or shape == 'rectangle' or shape == 'Rectangle':
        i = 0
        for i in range(4):
            turtle_eight.forward(100)
            turtle_eight.right(90)

    if shape == 'circle' or shape == 'Circle':
        turtle_eight.circle(33)

    if shape == 'pentagon' or shape == 'Pentagon':
        i = 0
        for i in range(5):
            turtle_eight.forward(93)
            turtle_eight.right(72)

    if shape == 'hexagon' or shape == 'Hexagon':
        i = 0
        for i in range(6):
            turtle_eight.forward(91)
            turtle_eight.right(60)

    # Call the turtle .done() method
turtle.done()
