"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
num1 = input("Enter a number!")
num2 = input("Enter another number!")

a = int(num1)
b = int(num2)

operation = input("Would you like to add, subtract, multiply, or divide?")
if operation == 'Add' or operation == 'add':
    print(a+b)

if operation == 'Subtract' or operation == 'subtract':
    print(a-b)

if operation == 'Multiply' or operation == 'multiply':
    print(a*b)

if operation == 'Divide' or operation == 'divide':
    print(a/b)
