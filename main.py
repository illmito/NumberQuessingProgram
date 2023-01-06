import random
from art import logo

number_chosen = random.choice(range(1, 100))
print(number_chosen)

print(logo)
print("Welcome to the number guessing game")

# Set the amount of guesses user will have
difficulty = input("Choose a difficulty. type 'easy' or 'hard': ").lower()
guesses = 0

if difficulty == 'easy':
    guesses = 10
elif difficulty == 'hard':
    guesses = 5

# notifies user of attempts and difficulty setting

print(f"You have selected {difficulty}, this means you will be given {guesses} guesses. ")
print("im thinking of a number between 1 and 100:")

# This will loop through the user input guesses and
# keeps track of attempts left.

active_game = True
while active_game is not False:
    user_guess = int(input("Please make a guess. "))
    if user_guess > number_chosen:
        print(f"{user_guess}: Your Guess is too High!")
        guesses -= 1
        print(f"Attempts remain: {guesses}")
    if user_guess < number_chosen:
        print(f"{user_guess}: Your Guess is too Low!")
        guesses -= 1
        print(f"Attempts remain: {guesses}")
    if user_guess == number_chosen:
        print(f"{user_guess} is correct! ")
        active_game = False
    elif guesses == 0:
        print("No More Attempts left, You Lose!")
        active_game = False