import random

user_input = int(input("enter a number between 1 and 10 and computer will guess it: "))

guess_number = 0
while user_input != guess_number:
    guess_number = random.randint(1,10)
    if user_input == guess_number:
        print(f"number you have entered is {guess_number}")
