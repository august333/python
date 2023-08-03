import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    r = simpledialog.askinteger(title=window, prompt="Enter a number.")
    ra = int(r)
    # Make a new turtle
    turtle_seven = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    turtle_seven.circle(ra)

    # Call the turtle .penup() method
    turtle_seven.penup()
    # Move your turtle to a new x,y position using .goto()
    turtle_seven.goto(32, 33)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = math.pi
    # Write the area of your circle using the turtle .write() method
    turtle_seven.write(arg="area = " + str(area), move=True, align='left', font=('Arial', 8, 'normal'))

    # Hide your turtle

    # Call turtle.done()
    turtle.done()
