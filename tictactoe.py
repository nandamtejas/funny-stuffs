import random



def displayboard(board):
    '''This displays the board'''
    a = ' | '
    n = '\n'
    b = '----------'
    d = board[7] + a + board[8] + a + board[7] + n + b + n+ board[4] + a + board[5] + a + board[6] + n + b + n + board[1] + a + board[2] + a + board[3]
    print(d)

def playerchoice():
    choice = input("Enter your choice: [X or O]: ")
    if choice not in ['X','O']:
        return "Choose 'X' or 'O'"
    if choice == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    

def wincheck(board, mark):
    comb = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(1,5,9)]
    for i,j,k in comb:
        if board[i] == board[j] == board[k] == mark:
            return board[i] == board[j] == board[k] == mark

def spacecheck(board, index):
    if board[index] == '-':
        return True

def fullspacecheck(board):
    for i in range(1,10):
        if spacecheck(board, i):
            return True
    return False   

def markposition(board, index, mark):
    return board[index] = mark

def duplicateboard(board):
    duplicate = []
    for i in board:
        duplicate.append(i)

def computerchoice(board):
    if playerletter == 'X':
        completter = 'O'
    else:
        completter = 'X'
    d_board = duplicateboard(board)

    # check computer wins
    if wincheck(d_board, completter):
        return "Computer wins"
    
    # check player wins
    if wincheck(d_board, playerletter):
        return "Player wins"
    
    # computer move
    index = random.randint(1,10)
    markposition(d_board, index, completter)

def playagain():
    choice = input("Will you play again? say YES/NO: ")
    if choice.lower().startswith('y'):
        return True
    return False

print("TIC TAC TOE!!")
board = ['-'] * 10
playermark, computermark = playerchoice()

while True:
