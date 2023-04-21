import random

def guess_number():
    number = random.randint(1,10)
    return number

gussed_number = guess_number()

user_number = 0

while user_number != gussed_number:
    user_input = input("guess number: ")
    if int(user_input) == gussed_number:
        print("you are correct")
        break
    else:
        print("better luck next time")

