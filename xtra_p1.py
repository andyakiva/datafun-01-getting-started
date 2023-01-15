"""
Optional bonus. See course site for details.

"""

"""
Andy Asher
01/14/2023
Optional Bonus Project - Game Bot
"""

import random

# Change the name below to a name of your choice

name = "GameBotAndy"

# Fix the code below to print the name using an f-string

print()
print(f"Hello, I'm {name}, your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function

user_choice = input("Type your selection (wolf, eagle, or snake): ")

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!
if user_choice == buddy_choice:
    print("We tied!")

if user_choice == "wolf" and buddy_choice == "eagle":
    print("You won!")

if user_choice == "wolf" and buddy_choice == "snake":
    print("You lose, try again!")

if user_choice == "snake" and buddy_choice == "wolf":
    print("You won!")

if user_choice == "snake" and buddy_choice == "eagle":
    print("You lose, try again!")

if user_choice == "eagle" and buddy_choice == "snake":
    print("You won!")

if user_choice == "eagle" and buddy_choice == "wolf":
    print("You lose, try again!")

# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------
"""
(base) andy@andy-Inspiron-15-3511:~/Documents/DataAnalytics/datafun-01-getting-started$ /home/andy/miniconda3/bin/python /home/andy/Documents/DataAnalytics/datafun-01-getting-started/xtra_p1.py

Hello, I'm GameBotAndy, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Type your selection (wolf, eagle, or snake): snake

You said snake.
I said eagle.

You lose, try again!
(base) andy@andy-Inspiron-15-3511:~/Documents/DataAnalytics/datafun-01-getting-started$ 
(base) andy@andy-Inspiron-15-3511:~/Documents/DataAnalytics/datafun-01-getting-started$ /home/andy/miniconda3/bin/python /home/andy/Documents/DataAnalytics/datafun-01-getting-started/xtra_p1.py

Hello, I'm GameBotAndy, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Type your selection (wolf, eagle, or snake): wolf

You said wolf.
I said snake.

You lose, try again!
(base) andy@andy-Inspiron-15-3511:~/Documents/DataAnalytics/datafun-01-getting-started$ /home/andy/miniconda3/bin/python /home/andy/Documents/DataAnalytics/datafun-01-getting-started/xtra_p1.py

Hello, I'm GameBotAndy, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Type your selection (wolf, eagle, or snake): wolf

You said wolf.
I said wolf.

We tied!
(base) andy@andy-Inspiron-15-3511:~/Documents/DataAnalytics/datafun-01-getting-started$ /home/andy/miniconda3/bin/python /home/andy/Documents/DataAnalytics/datafun-01-getting-started/xtra_p1.py

Hello, I'm GameBotAndy, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Type your selection (wolf, eagle, or snake): eagle

You said eagle.
I said snake.

You won!



"""
