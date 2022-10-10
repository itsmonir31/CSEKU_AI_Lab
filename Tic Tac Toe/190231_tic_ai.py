#program for tic tac toe human vs AI


def printBoard(board):              #function for printing board everytime
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("\n")


def spaceIsFree(position):          #funtion will check the free spaces
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):     #put 'x' or 'o' in the board
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("AI wins!")
                exit()
            else:
                print("You wins!")
                exit()
        return
    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():
    #Check row
    for i in range(1,8,3):
        if(board[i] == board[i+1] and board[i] == board[i+2] and board[i] !=' '):
            return True
    #Check column
    for i in range(1,4):
        if(board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] !=' '):
            return True
    #check Diagonal
    if (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    # Check row
    for i in range(1, 8, 3):
        if (board[i] == board[i + 1] and board[i] == board[i + 2] and board[i] == mark):
            return True

    # Check column
    for i in range(1, 4):
        if (board[i] == board[i + 3] and board[i + 3] == board[i + 6] and board[i] == mark):
            return True

    #check diagonal
    if (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
        
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


#human move
def playerMove():      
    position = int(input("Player Move:  "))
    insertLetter(player, position)
    return


#computer move
def compMove():
    print("Computer Move: ")
    bestScore = -999
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = computerMove
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(computerMove, bestMove)
    return

# this function is responsible for the main thing of ai
# it will check before computer move and maximize the possible score of computer
# and check for minimizing the chances of human
def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(computerMove)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):          #for computer miximize
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = computerMove
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:                       #for computer miximize
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}      #putting white spaces in board

printBoard(board)
print("Computers Moves first.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
computerMove = 'X'


global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()