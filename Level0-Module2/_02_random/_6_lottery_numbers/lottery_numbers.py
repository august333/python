import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
rand_one = random.randint(0, 9)
rand_two = random.randint(0, 9)
rand_three = random.randint(0, 9)
rand_four = random.randint(0, 9)
rand_five = random.randint(0, 9)
rand_six = random.randint(0, 9)
r_one = rand_one
r_two = rand_two
    # TODO 2) Display the selected numbers to the user in a pop-up
# messagebox.showinfo(title='Lottery Ticket!', message=

text = rand_one, rand_two, rand_three, rand_four, rand_five, rand_six

text_list = list(text)
print(text_list)

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
