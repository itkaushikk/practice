import random
user_input = input("enter r or p or s: ")
computer_choice = ["r","p","s"][random.randint(0,2)]

if user_input == computer_choice:
    print("tie")
elif user_input == "r" and computer_choice == "s":
    print("you won")
elif user_input == "p" and computer_choice == "r":
    print("you won")
elif user_input == "s" and computer_choice == "p":
    print("you won")
else:
    print("you lost")