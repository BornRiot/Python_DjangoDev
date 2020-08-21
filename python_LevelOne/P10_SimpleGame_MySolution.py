"""This is my attempt to solve the random numbers challenge in python game"""
import random

# Display welcome message to player
print("Welcome Code Breaker! Lets see if you can break my 3 digit number!")
print("Code has been generated, please guess a 3 digit number ")
guess = list(input("What is your guess?: "))
print(guess)

# Create a range of numbers and shuffle to create a list of 3 random numbers
digits = list(range(10))
random.shuffle(digits)

# Create an mty list and assign numbers from ordinal list to a new list 
games_list = []
for x in digits[:3]:
    games_list.append(x)

playersMatch = []  # May not need this list
print(games_list)
while guess != games_list:
    for i in guess:
        if i == games_list[0] or i == games_list[1] or i == games_list[2]:
            print(games_list[i])
            print("Close")
        elif i != games_list[0] and i != games_list[1] and i != games_list[2]:
            print(i)
            print(games_list)
            print("Nope ")
            list(input("Please try and enter a new guess  "))
            continue
        else:

            print(games_list)
            print("Nope!")
            guess = list(input("Please try again to enter a correct digit: "))


# ----------------------------------------------- Below this line are possible functions and
# other code that may possibly be correct to use and solve the problem
# return a[-(len(b)):] == b or a == b[-(len(a)):]:
# for x in guess:
#     if guess[0] == games_list[0] or guess[1] == games_list[1] or guess[2] == games_list[2]:
#         print("close")
def code_cracker(my_list):
    if my_list[2] == 1:
        print("Don't do anything for now")
