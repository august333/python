import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    
    # 6. Call the turtle .penup() method
    turtle.penup()
    
    # 7. Move the turtle to a new location using .goto(x, y)
    turtle.goto(10, 10)


def turtle_clicked(x, y):
    print('turtle clicked!')
    
    # 8. Make a for loop to run the next instructions 3 times
x=3
for i in x:
    # 9. Make the turtle spin 360 degrees using the .right() method
    turtle.right(360)
    # 10. Use the .color() method and getRandomColor() function to change
    # the color of the turtle,
    turtle.color(get_random_color())


if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(width=7.5, height=0.8, startx=0, starty=0)
    
    # 1. Make a new turtle
    turtle_two = turtle.Turtle()

    # 2. Make your turtle's shape 'turtle', .shape('turtle')
    turtle_two.shape('turtle')
    # 3. Set your turtle's color using .color('green') and .pencolor('blue')
    turtle_two.color('green')
    turtle_two.pencolor('blue')
    # 4. Set and new width, length, and outline of our turtle
    turtle_two.turtlesize(stretch_wid=11, stretch_len=11, outline=0.5)

    # 5. Uncomment the following line and replace 'my_turtle' with your turtle
    turtle_two.onclick(turtle_clicked)

# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screen_clicked)
turtle.done()
