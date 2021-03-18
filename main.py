
board = [' ' for x in range (10)]

def inserletter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):                                          #board and letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def playerMove():
    run = True
    while run:
        move = input('Please select a position from 1 to 9')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    inserletter('X', move)
                else:
                    print('Select a free space')
            else:
                print('Please choose a valid number')
        except:
            print('Please type a number')


def main():
    print('Welcome to Tic Tac Toe')
    printBoard()

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print("O's WON!")
            break

        if not (isWinner(board, 'X')):
            compMove()
            printBoard()
        else:
            print("X's WON!")
            break

    if isBoardFull(board):
        print('Tie Game')

