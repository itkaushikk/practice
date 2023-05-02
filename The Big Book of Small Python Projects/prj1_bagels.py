import random

print(
    """Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.
I have thought up a number.
You have 10 guesses to get it."""
)

guessed_no = str(random.randint(100, 999))

count = 0
while True:
    print(f"Guess #{count+1}")
    guessed_user = input("> ")

    for index_user in range(len(guessed_user)):
        if guessed_user[index_user] == guessed_no[index_user]:
            print("Fermi", end=" ")
        elif guessed_user[index_user] in guessed_no:
            print("Pico", end=" ")
        else:
            print("Bagels", end=" ")

    print("")
    count += 1
    if count == 10:
        print("sorry, end of chances")
        answer = input("do you want to continue yes or no: ")
        if answer == "no":
            break
    elif guessed_no == guessed_user:
        print("you got it!")
        answer = input("do you want to continue yes or no: ")
        if answer == "no":
            break
