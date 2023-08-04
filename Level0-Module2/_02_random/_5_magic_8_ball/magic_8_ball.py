import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    r = print("Ask me a question!")
    input()
    # Make a variable and initialize it to a random number between 0 and 3
    random_num = random.randint(0, 3)
    # If the random number is 0
    # tell the user "Yes"
    if random_num == 0:
        print("Signs point to yes.")

    # If the random number is 1
        # tell the user "No"
if random_num == 1:
        print("No.")
    # If the random number is 2
if random_num == 2:
        print("Maybe you should ask Google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
if random_num == 3:
        print("lol no")
        # write your own answer
