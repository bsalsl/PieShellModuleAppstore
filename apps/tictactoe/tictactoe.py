def run():
  global board
  global gamestillgoing
  global winner
  global currentplayer
  board = ["-","-","-",
           "-","-","-",
           "-","-","-"]
  gamestillgoing = True
  winner= None
  
  while True:
    choice = input("Choose whether to be X or 0 (Zero): ")
    choice = choice.upper()
    if choice != "X" and choice != "0":
      print("Invalid Input")
    else:
      currentplayer = choice
      break
  playgame()

    

def displayboard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def playgame():
    displayboard()
    while gamestillgoing:
        handleturn(currentplayer)
        checkifgameover()
        flipplayer()
    if winner == "X" or "0":
        print(winner + " Won!")
    elif winner == None:
        print("Tie.")
def handleturn(player):
    print(player + "'s turn")
    position = input("Choose a postioon form 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position)-1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = player
    displayboard()
def checkifgameover():
    checkifwinner()
    checkiftie()
def checkifwinner():
    global winner
    rowwinner = checkrows()
    columnwinner = checkcolumns()
    diagonalwinner = checkdiagonals()
    if rowwinner:
        winner = rowwinner
    elif columnwinner:
        winner = columnwinner
    elif diagonalwinner:
        winner = diagonalwinner
    else:
        winner = None
def checkrows():
    global gamestillgoing
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        gamestillgoing = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return   
def checkcolumns():
    global gamestillgoing
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        gamestillgoing = False
    if column1:
        return board[0]
    elif column2:
        return board[3]
    elif column3:
        return board[6]
    return
def checkdiagonals():
    global gamestillgoing
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[6] == board[4] == board[2] != "-"
    if diagonal1 or diagonal2:
        gamestillgoing = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return
def checkiftie():
    global gamestillgoing
    if "-" not in board:
        gamestillgoing = False
    return
def flipplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "0"
    elif currentplayer == "0":
        currentplayer = "X"