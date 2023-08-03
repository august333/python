"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""

score= 0

ans1 = input("What belongs to you, but other people use it more than you?")

if ans1 == 'Your name' or 'your name':
    score += 1

ans2 = input("What has many keys but can't open any door?")

if ans2 == "a keyboard" or ans2 == 'A keyboard' or ans2 == "A piano" or ans2 == "a piano":
    score += 1

ans3 = input("What runs around the whole yard without moving?")

if ans3 == "A fence" or ans3 == "a fence":
    score += 1

if score == 3:
    print('You got all of the riddles correct!');

if score == 2:
    print('You got two out of three riddles correct!');

if score == 1:
    print('You got one out of three riddles correct!');

if score == 0:
    print('You got no riddles correct!');



