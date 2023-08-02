from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete

# Make a new window variable, window = Tk()
window = Tk()
 # Hide the window using the window's .withdraw() method
window.withdraw()

# 1. Make a variable equal to a positive number less than 4 using random.randint(0, 3)
res = random.randint(0, 3)
# 2. Print your variable to the console
print(res)
# 3. Get the user to enter something that they think is awesome
simpledialog.askstring(title=window, prompt="Enter something you think is awesome!")
# 4. If your variable is  0
# -- tell the user whatever they entered is awesome!
if res == '0':
    messagebox.showinfo(message="I agree!")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
if res == '1':
    messagebox.showinfo(message="That is okay")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
if res == '2':
    messagebox.showinfo(message="That is boring.")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
if res == '3':
    messagebox.showinfo(message="I don't know what that is.")
    window.mainloop()
