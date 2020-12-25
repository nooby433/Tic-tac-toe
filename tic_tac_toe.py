#---------Dual Player Tic Tac Toe app------------
board = [ "-", "-", "-",  #creating a list of inputs for positioning the board
          "-", "-", "-",
          "-", "-", "-"]
#creating a list of all the possible inputs for input function
num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#global variables used during the project
game_going = True
current_player = "X"
winner = None

#defining the positions and structure for the board
def play_board() :
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#defining what happens during the turn of a player
def handle_turn(player):
    #Showing whose turn this is
    print(player + " 's Turn")
    #Asking for the input
    position = input("Choose a number between 1-9: ")
    #Creating a boolean so that player can't override a previously selected position
    valid = False
    # first while loop to check valid boolean
    while not valid:
    #second while loop to ensure that no other inputs are added
     while position not in num_list:
         position = input("Invalid input. Choose a number between 1-9: ")
    #if input is correct second loop breakes and continues.
     position = int(position) - 1
     #making sure that position is not already taken. first Loop brakes if input is correct.
     if board[position] == "-":
         valid = True
     else:
         print("Position already taken. Choose another number")
    board[position] = player
    play_board()

def start_game():
    play_board()
    #Creating a while loop so that the game continues till tie or a winner is found.
    while game_going:
            handle_turn(current_player)
            check_game_over()
            flip_player()
#Printing out the winner or if its a tie.
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    else:
        print("Tie.")

#defining wether a game is over or not
def check_game_over():
    check_winner()
    game_tied()
    return

#checking wether there is a winner.
def check_winner():
    global winner
    #Any one of the rows had a winner.
    row_winner = row_check()
    #Any one of the coloumns had a winner.
    coloumn_winner = coloumn_check()
    #Any one of the diagonals had a winner.
    diagonal_winner = diagonal_check()
    #assigning the value of the winner(if any) to global variable winner.
    if row_winner:
        winner = row_winner
    elif coloumn_winner:
        winner = coloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return

#Checking wether there is a winner in rows
def row_check():
    global game_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    #in case of winner setting the global variable false so that he game ends.
    if row1 or row2 or row3:
        game_going = False
    #returning the winner X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

#Checking wether there is a winner in coloumns.
def coloumn_check():
    global game_going
    coloumn1 = board[0] == board[3] == board[6] != "-"
    coloumn2 = board[1] == board[4] == board[7] != "-"
    coloumn3 = board[2] == board[5] == board[8] != "-"
    #in case of winner setting the global variable false so that he game ends.
    if coloumn1 or coloumn2 or coloumn3:
        game_going = False
    #returning the winner X or O
    if coloumn1:
        return board[0]
    elif coloumn2:
        return board[1]
    elif coloumn3:
        return board[2]
    return

#Checking wether there is a winner in diagonals.
def diagonal_check():
    global game_going
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    #in case of winner setting the global variable false so that he game ends.
    if diagonal1 or diagonal2:
        game_going = False
    #returning the winner X or O
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return

#Checking wether the game is tied.
def game_tied():
    global game_going
    #if all the spaces are filled and no function defined above works it means that we have tied.
    #so to break the game global variable has been assigned false
    if "-" not in board:
        game_going = False
    return

#changing the players after every turn.
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

#calling to start the game.
start_game()
