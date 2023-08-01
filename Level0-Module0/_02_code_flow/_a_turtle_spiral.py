import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # Make a new turtle
    turtle_three = turtle.Turtle()
    # This code sets our shape to a turtle
    turtle_three.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    turtle_three.speed(7)
    # Set your turtle's color using .color('green')
    turtle_three.color('green')
    # Use a loop to repeat a the code below 50 times
i = 0
for i in range(50):
        # Set the turtle color to a random color
        turtle_three.color(get_random_color())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        turtle_three.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        turtle_three.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        turtle_three.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!
        i+1
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
