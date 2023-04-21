import random

def initial_print():
    print("tic tac toe index")
    print("| 0 | 1 | 2 |")
    print("| 3 | 4 | 5 |")
    print("| 6 | 7 | 8 |")
    
def display(index_play):
    index = 0
    
    for r in range(3):
        output = ""
        for i in range(3):
            if i == 0:
                output = "| " + str(index_play[index]) + " |"
            else:
                output = output + " " + str(index_play[index]) + " |"
            index += 1
        print(output)

def check_winner(index_play, player):
    
    for r in range(0,3):
        start_index = 3 * r
        end_index = start_index + 3
        
        is_winner = True
        for i in range(start_index,end_index):
            if index_play[i] != player:
                is_winner = False
        
        if is_winner:
            return is_winner
    
    is_winner = True
    for i in range(0,3):
        if index_play[(3*i)+i] != player:
            is_winner = False
    if is_winner:
        return is_winner
   
    is_winner = True 
    for i in range(0,3):
        if index_play[2-i] != player:
            is_winner = False
    if is_winner:
        return is_winner
    
    return False

initial_print()

index_play = [" "," "," "," "," "," "," "," "," "]
indexes = [0,1,2,3,4,5,6,7,8]
while True:
    if indexes == []:
        break
    
    user_input = input("X's turn. input move 0-8: ")
    
    if index_play[int(user_input)] != " ":
        print("index already occupied. pick other move")
    
    index_play[int(user_input)] = "X"
    indexes.remove(int(user_input))
    display(index_play)
    
    is_winner = check_winner(index_play, "X")
    if is_winner:
        print("you won")
        break
    
    print("O's turn, computer move")
    computer_input = random.choice(indexes)
    index_play[int(computer_input)] = "O"
    indexes.remove(int(computer_input))
    display(index_play)
    is_winner = check_winner(index_play, "X")
    if is_winner:
        print("you lost")
        break