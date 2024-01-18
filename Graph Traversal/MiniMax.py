import os
import time
from queue import PriorityQueue

def prRed(skk): print("\033[91m{}\033[00m" .format(skk), end='')            # print in red
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk), end='')           # print in blue


''' initialise the game board according to size'''

def initialise_board(size):
    board = [[0 for i in range(size)]]
    for i in range(size - 1):
        board.append([0 for j in range(size - 1)])     
        board.append([0 for j in range(size)])
    return board


''' print the board in a proper colored format'''

def print_board(board):
    colors = [prCyan, prRed]
    edges =[['   ', ' | ', '---'], ['   ', '---', ' | ']]
    size = (len(board) + 1) // 2
    for num in range(size): print(f'  {num} ', end='')

    prRed('\n--' + 'o---'*(size-1) + 'o--\n')                                       
    for i, row in enumerate(board):
        prCyan('| ' * (i%2))
        for player in row:
            colors[i%2]('o')
            colors[player%2](edges[i%2][player])
        colors[i%2]('o')
        prCyan(' |' * (i%2))
        print(f'    {i}')
    prRed('--' + 'o---'*(size-1) + 'o--\n')


''' make move on board for player and return success status'''

def makemove(board, coord, player):
    try:
        row, col = int(coord[0]), int(float(coord[1]))
        if board[row][col] == 0:
            board[row][col] = player
            return True
        return False
    except (IndexError, ValueError):
        return False


''' return valid/empty connected fences from current position '''

def emptyPositions(board, visited, player, row, col):
    valid = []
    def addValid(i, j):
        if (i, j) not in visited and 0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] != (player % 2) + 1:
            valid.append((i, j))

    offset = player - 1
    if (row % 2 == 0 and player == 1) or (row % 2 == 1 and player == 2):
        addValid(row - 2, col)
        addValid(row - 1, col - 1 + offset)
        addValid(row - 1, col + offset)
        addValid(row + 2, col)
        addValid(row + 1, col - 1 + offset)
        addValid(row + 1, col + offset)
    else:
        addValid(row - 1, col - offset)
        addValid(row - 1, col - offset + 1)
        addValid(row + 1, col - offset)
        addValid(row + 1, col - offset + 1)
        addValid(row, col - 1)
        addValid(row, col + 1) 
    return valid


''' add position to the queue (update empty path if necessary)'''

def add_queue(queue, cost, empty, board, position):
    if board[position[0]][position[1]] == 0:
        queue.put((cost + 1, position, empty.union({position})))        # increase cost and update if position is empty
    else:
        queue.put((cost, position, empty))


''' return shortest possible distance for red to win (A*) '''

def shortest_distance_red(board):
    queue = PriorityQueue()
    visited = {}
    for i, player in enumerate(board[0]):                               # add all valid position for red at top row
        if player != 2: add_queue(queue, 0, set(), board, (0, i))

    while True:
        if queue.empty():                                               # if no path found
            return 100, set()

        heuristic, (row, col), emptyset = queue.get()                   # get current position

        if (row, col) in visited:                                       # skip if visited
            continue

        visited[(row, col)] = True                                      # mark position as visited

        if row == len(board) - 1:                                       # if reached bottom row, path is shortest
            return heuristic, emptyset

        for position in emptyPositions(board, visited, 1, row, col):    # add all valid positions from current position
            add_queue(queue, heuristic, emptyset, board, position)


''' return shortest possible distance for blue to win (A*) '''

def shortest_distance_blue(board):
    queue = PriorityQueue()
    visited = {}
    for i in range(0, len(board), 2):                                   # add all valid positions for blue from left side
        if board[i][0] != 1: add_queue(queue, 0, set(), board, (i, 0))

    while True:
        if queue.empty():
            return 100, set()

        heuristic, (row, col), emptyset = queue.get()

        if (row, col) in visited:
            continue

        visited[(row, col)] = True

        if col == len(board[0]) - 1:                                    # if reached right side, return distance and empty positions
            return heuristic, emptyset

        for position in emptyPositions(board, visited, 2, row, col):    # add valid positions
            add_queue(queue, heuristic, emptyset, board, position)


''' recursive alpha beta pruning function for AI optimal move'''

def alpha_beta_pruning(board, move, alpha, beta, maxPlayer, depth):
    (red, rmoves), (blue, bmoves) = shortest_distance_red(board), shortest_distance_blue(board)         # get distance and empty positions for blue and red
    if depth == 0 or blue == 0 or red == 0:                                                             # if depth is 0 or winner found
        return (red - blue) * (depth + 1), move                                                         # return total score for state
  
    if maxPlayer:
        maxValue, maxMove = -999999, None
        for (i, j) in rmoves.union(bmoves):                                                             # best move will always be in shortest path for either player
            board[i][j] = 2                                                                             # mark temporary move at position 
            value, _ = alpha_beta_pruning(board, (i, j), alpha, beta, False, depth - 1)                 # call recursive function for minplayer
            board[i][j] = 0                                                                             # unmark move
            maxValue = max(maxValue, value)                                                             # if new best move found
            if maxValue == value:                                                                       # save move as best move
                maxMove = (i, j)
            alpha = max(alpha, value)                                                                   # update alpha

            if alpha > beta:                                                                            # prune unnecessary states
                return maxValue, maxMove
        return (maxValue, maxMove) if maxMove is not None else ((red - blue) * (depth + 1), move)       # return bestmove

    minValue, minMove = 99999999, None
    for (i, j) in rmoves.union(bmoves):
        board[i][j] = 1
        value, _ = alpha_beta_pruning(board, (i, j), alpha, beta, True, depth - 1)
        board[i][j] = 0
        minValue = min(minValue, value)
        if minValue == value:
            minMove = (i, j)
        beta = min(beta, value)
    return (minValue, minMove) if minMove is not None else ((red - blue) * (depth + 1), move)


''' call alpha beta pruning and return result'''

def minimax(board, depth):
    return alpha_beta_pruning(board, (0, 0), -9999999, 9999999, True, depth)[1]


''' main game loop and I/O operations '''

if __name__ == '__main__':
    boardsize, difficulty = None, None
    opt = input('\nBoard Size:\n1 -> Small (5 x 5)\n2 -> Medium (8 x 8)\n\nEnter Option : ').strip()
    if opt == '1':
        boardsize = 5
    else:
        boardsize = 8

    opt = input('\nDifficulty:\n1 -> Easy\n2 -> Hard\n\nEnter Option : ').strip()
    if opt == '1':
        difficulty = 1
    else:
        difficulty = 2
    
    gameboard = initialise_board(boardsize)
    current_player = 0


    while True:
        os.system('cls')
        print_board(gameboard)

        if current_player % 2 == 0:
            current_move = input('\nEnter row and column to place fence (e.g. 3 4) : ').split()
            if not makemove(gameboard, current_move, 1):
                print('\n *** Invalid Move, Try Again ***')
                time.sleep(1)
                continue
        else:
            current_move = minimax(gameboard, difficulty)
            makemove(gameboard, current_move, 2)

        if (current_player % 2 == 0 and shortest_distance_red(gameboard)[0] == 0) or (current_player % 2 == 1 and shortest_distance_blue(gameboard)[0] == 0):
            os.system('cls')
            print_board(gameboard)
            print('\n\n*** '+ ('BLUE' if current_player % 2 else 'RED') + ' WINS ***\n')
            break
        current_player += 1
        print('\n')