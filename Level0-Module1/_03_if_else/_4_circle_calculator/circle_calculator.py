# Write a Python program that asks the user for the radius of a circle.
import math

radius = input("enter a radius for your circle.")
r = int(radius)
# Next, ask the user if they would like to calculate the area or circumference of a circle.
c = input("would you like to calculate the area or the circumference of your circle?")
# If they choose area, display the area of the circle using the radius.
if c == 'area' or c == 'Area':
    area = (r*r*3.14159)
    print(area)

# Otherwise, display the circumference of the circle using the radius.
if c == 'circumference' or c == 'Circumference':
    Circumference = (2*3.14159*r)
    print(Circumference)
