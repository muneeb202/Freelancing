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


