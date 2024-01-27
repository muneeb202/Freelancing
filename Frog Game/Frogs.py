
def print_board(board):
    print()
    for ch in board:
        print(ch, end='  ')
    print('\n' + '-  ' * len(board))
    for i in range(1, len(board) + 1):
        print(i, end='  ')
    print()

def isValid(board, start, end):
    try:
        startnum = int(start)
        endnum = int(end)
    except ValueError:
        print("\nEnter a number!")
        return False

    startnum -= 1
    endnum -= 1
    
    if startnum < 0 or startnum >= len(board) or endnum < 0 or endnum > len(board):
        print("\nEnter positions on the board!")
        return False
    
    if endnum == startnum:
        print("\nCannot move to the same position!")
        return False
    
    if board[endnum] != ' ':
        print("\nCannot move to a filled position!")
        return False

    if abs(startnum - endnum) > 2:
        print("\nCannot move more than 2 spaces!")
        return False

    if (board[startnum] == 'F' and endnum < startnum) or (board[startnum] == 'T' and endnum > startnum):
        print("\nCannot move in both directions!")
        return False

    return True


def move(board, start, end):
    startnum = int(start) - 1
    endnum = int(end) - 1

    board[endnum] = board[startnum]
    board[startnum] = ' '


def hasFinished(board):
    if board[0: int(len(board) / 2)] != ['T'] * int(len(board) / 2):
        return False

    if board[int(len(board) / 2) + 1:] != ['F'] * int(len(board) / 2):
        return False
    return True


def run_game(board):
    
    print("\nEnter e (exit) or r (reset) at any point!")
    while hasFinished(board) is False:
        print('\n' + '*' * 20)
        print_board(board)
        start = input("\nFrom: ").strip().lower()

        if start == 'r':
            return False
        elif start == 'e':
            return True
        
        end = input("\nTo:   ").strip().lower()
        if end == 'r':
            return False
        elif end == 'e':
            return True
        
        if isValid(board, start, end):
            move(board, start, end)

    return True


def demonstration(board):
    print("\nGoal: Swap places of all Toads (T) and Frogs (F)\n\n ---------- Rules ----------\n+ Can move only in one direction"
    "\n+ Can only move to next position if empty\n+ Can jump over a Frog or Toad to an empty position\n"
    "\n\n -------- How to Play --------\n+ Enter position to move from\n+ Enter position to move to\n+ Enter \'e\' to exit or \'r\' to reset the game at any point\n")
    
    print("\n\t\t\tSAMPLE EXECUTION\n")
    print_board(board)

    print("\nFrom: 3\nTo: 4")
    if isValid(board, 3, 4):
        move(board, "3", "4")
    print_board(board)

    print("\nFrom: 5\nTo: 3")
    if isValid(board, 5, 3):
        move(board, "5", "3")
    print_board(board)


def main():
    game = ['F', 'F', 'F', ' ', 'T', 'T', 'T']

    while True:

        print("\n1 : Play game\n2 : Run demonstration\n3 : Exit Program")
        opt = input("\nEnter option: ").strip()

        if opt == '1':
            while run_game(game.copy()) is False:
                print('\nResetting Game!')
            print('\nGame Finished!')

        elif opt == '2':
            demonstration(game.copy())

        elif opt == '3':
            print("\nExiting Program!\n")
            break

        else:
            print("\nIncorrect Option Entered! Try Again")




if __name__ == "__main__":
    main()