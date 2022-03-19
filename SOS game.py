# SOS Game
# By : Mohamed Wael Ibrahim
# Date : 1/3/2022

# First we need to create a board which we will play on:
board = ["-","-","-","-",
         "-","-","-","-",
         "-","-","-","-",
         "-","-","-","-",]
# "game_running" makes the game in infinite loop untill its end.
game_running = True

# Function screen() is for printing the board.
# The numbers in right side is to  make it easy to player to choose the place.
def screen(board):
    print("\t     *******")
    print("\t  "+board[0]+" | "+board[1]+" | "+board[2]+" | "+board[3]+"  | "+ "1 2 3 4")
    print("\t ---------------")
    print("\t  "+board[4]+" | "+board[5]+" | "+board[6]+" | "+board[7]+"  | "+ "5 6 7 8")
    print("\t ---------------")
    print("\t  "+board[8]+" | "+board[9]+" | "+board[10]+" | "+board[11]+"  | "+ "9 10 11 12")
    print("\t ---------------")
    print("\t  "+board[12]+" | "+board[13]+" | "+board[14]+" | "+board[15]+"  | "+ "13 14 15 16")
    print("\t     *******")
    return("")

# Here we will start the game with Player 1:
# it designed to take a char and place from player and check if it achieve SOS statement.  
def player1_turn(board):
    while game_running:
        place = int(input("Player 1, Enter a number 1-16: "))
        char = input("Player 1, Enter 'S' or 'O': ")
        if char.islower:
            char = char.upper()
        # Here you can choose a small letter not only capital letter.
        print("")
        if place >=1 and place <=16 and board[place-1]=="-" and char == 'S' or char == 'O':
            board[place-1] = char
            if board[place-1] == "S" or board[place-1] == "O":
                # calling a function score_check and make sure that the current function is True.
                if score_check(board,place) == True:
                    return True
                break
            # End of function and return it as True.
                
        else :
            while(char != 'S' and char != 'O' and place not in range(1,17)):
                print("wrong choice!, try again")
                place = int(input("Enter a number 1-16: "))
                char = input("Enter 'S' or 'O': ")
    return("")

# After taking player 1 turn and check the SOS statement as player 1
def player2_turn(board):
    while game_running:
        place = int(input("Player 2, Enter a number 1-16: "))
        char = input("Player 2, Enter 'S' or 'O': ")
        if char.islower:
            char = char.upper()
        print("")
        if place >=1 and place <=16 and board[place-1]=="-" and char == 'S' or char == 'O':
            board[place-1] = char
            if board[place-1] == "S" or board[place-1] == "O":
                if score_check(board,place) == True:
                    return True
                break
        
        else :
            while(char != 'S' and char != 'O' and place not in range(1,17)):
                print("wrong choice!, try again")
                place = int(input("Enter a number 1-16: "))
                char = input("Enter 'S' or 'O': ")
    return("")

def score_check(board,place):

# Here we start checking horizontally
    if (place - 1) - 2 >= 0:
        if board[(place-1)-2]=='S' and board[(place-1)-1]=='O' and board[(place-1)]=='S':
            return True

    if (place - 1) + 2 <= 15:
        if board[place-1]=='S' and board[(place-1)+1]=='O' and board[(place-1)+2]=='S':
            return True
    
    if (place - 1) + 1 <= 11 and (place - 1) - 1 >= 1:
        if board[(place-1)-1]=='S' and board[(place-1)]=='O' and board[(place-1)+1]=='S':
            return True
        
# start checking vertically 
    if (place-1)-2 >= 0:
        if board[(place-1)]=='S' and board[(place-1)-4]=='O' and board[(place-1)-8]=='S':
            return True
    
    if (place - 1) + 2 <= 13:
        if board[(place-1)]=='S' and board[(place-1)+4]=='O' and board[(place-1)+8]=='S':
            return True
            
    if (place - 1) + 1 <= 13 and (place - 1) - 1 >= 0:
        if board[(place-1)-4]=='S' and board[(place-1)]=='O' and board[(place-1)+4]=='S':
            return True

# start checking diagonally
    if (place - 1)  >= 10 :
        if board[(place-1)]=='S' and board[(place-1)-5]=='O' and board[(place-1)-10]=='S':
            return True

    if (place - 1)  <= 5 :
        if board[(place-1)]=='S' and board[(place-1)+5]=='O' and board[(place-1)+10]=='S':
            return True

    if (place - 1) >= 5 and (place - 1) <= 10 :
        if board[(place-1)-5]=='S' and board[(place-1)]=='O' and board[(place-1)+5]=='S':
            return True

    if (place - 1) <= 13 and (place - 1) >= 3 :
        if board[(place-1)]=='S' and board[(place-1)-3]=='O' and board[(place-1)-6]=='S':
            return True
    
    if (place - 1) >= 2 and (place - 1) <= 6:
        if board[(place-1)]=='S' and board[(place-1)+3]=='O' and board[(place-1)+6]=='S':
            return True
        
    if (place - 1) >= 5 and (place - 1) <= 10:
        if board[(place-1)-3]=='S' and board[(place-1)]=='O' and board[(place-1)+3]=='S':
            return True
        
# print a board to see score
def score_board():
    # Take a player1_points/player2_points from the last function.
    global player1_points
    global player2_points
    print("\tPlayer1 VS Player2")
    print("\t     " + str(player1_score) + "  |  " + str(player2_score))
    return ("\n")

# Here a function to make sure that the game will end, And it only will happen if the board is full
def complete(board):
    count = 0
    for i in board :
        if i == "-":
            count += 1
        if i in range(len(board)):
            if i != "-":
                game_running = False
                break
    if count == 0:
        return True

# The final function is collecting the game elements and functions and running it 
while game_running:

    player1_score = 0
    player2_score = 0
    score_board()

    while game_running:

        screen(board)
        if player1_turn(board) == True:
            player1_score = player1_score + 1
        score_board()

        screen(board)
        if player2_turn(board) == True:
            player2_score = player2_score + 1
        score_board()
            
            
        if complete(board) == True:
            if player1_score > player2_score:
                print("*** Player 1 wins ***")
                print("")
                game_running = False
                
            elif player2_score > player1_score:
                print("*** Player 2 wins ***")
                print("")
                game_running = False
                
            elif player1_score == player2_score:
                print("\t*** Draw ***")
                print("")
                game_running = False