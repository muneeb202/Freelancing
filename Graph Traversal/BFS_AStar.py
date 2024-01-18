from queue import PriorityQueue
from random import randint

start = [7, 2, 4, 5, 0, 6, 8, 3, 1, 4]                          # start state
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0]
visited = {}
SIZE = 3


def print_arr(arr):                                             # print array in a grid format
    print('-' * 19)
    for i, num in enumerate(arr[:-1]):
        print('| ',num if num != 0 else ' ', end='  ')
        if (i+1) % 3 == 0:
            print('|')
    print('-' * 19)


def random_start():
    moves = randint(20, 50)                                     # randomize number of moves to be made
    count = 0                                                   # changes made so far
    puzzle = goal.copy()                                        # start from goal state

    while count != moves:
        step = randint(1, 4)                                    # choose random move from U, D, L, R
        count += 1                                              # update count of changes
        if step == 1 and puzzle[-1] > 2:                        # move up
            move(puzzle, -3)
        elif step == 2 and puzzle[-1] < 6:                      # move down
            move(puzzle, 3)
        elif step == 3 and puzzle[-1] % 3 != 0:                 # move left
            move(puzzle, -1)
        elif step == 4 and (puzzle[-1] + 1) % 3 != 0:           # move right
            move(puzzle, 1)
        else:
            count -= 1                                          # no move made (invalid)
    return puzzle                                               # return updated start state


def print_path(final):                                          # print predecessors first using recursion
    if final is None:
        return -1, ''                                           # base case (start state)
    prev, step = visited[final][0], visited[final][1]           # get predecessor, and move made from visited dict
    count, path = print_path(prev)                              # call function for predecessor
    print_arr(final)                                            # print puzzle, after predecessor
    return count + 1, path + step                               # return updated total moves, and solution path


def move(puzzle, step):                                         # move blank tile in puzzle
                                                                # blank tile, other tile = other tile, blank tile
    puzzle[puzzle[-1]], puzzle[puzzle[-1] + step] = puzzle[puzzle[-1] + step], puzzle[puzzle[-1]]
    puzzle[-1] += step                                          # update position of blank tile
    return puzzle                                               # return update state


def heuristic(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += abs((arr[i] // SIZE) - (i//SIZE)) + abs((arr[i] % SIZE) - (i % SIZE))      # sum of manhattan distance of each number from goal
    return total


def BestFirstSearch():
    openlist = PriorityQueue()
    openlist.put((0, start, None, ''))                              # f(n), g(n), state, predecessor, Path
    states = 0

    while True:
        if openlist.empty():
            print('Goal Not Found!')
            break

        _, puzzle, prev, path = openlist.get()                 # get next state to be traversed
        tup = tuple(puzzle)

        if tup in visited:                                      # state already visited
            continue
        states += 1

        visited[tup] = (prev, path)                             # mark state as visited

        if puzzle == goal:                                      # goal reached
            total, path = print_path(tup)
            print(f'\nTotal Visited : {states}\nTotal moves -> {total}\nPath        -> {path}')
            break

        if puzzle[-1] > 2:                                      # move up
            nextmove = move(puzzle.copy(), -3)
            openlist.put((heuristic(nextmove), nextmove, tup, 'U '))

        if puzzle[-1] < 6:                                      # move down
            nextmove = move(puzzle.copy(), 3)
            openlist.put((heuristic(nextmove), nextmove, tup, 'D '))

        if puzzle[-1] % 3 != 0:                                 # move left
            nextmove = move(puzzle.copy(), -1)
            openlist.put((heuristic(nextmove), nextmove, tup, 'L '))

        if (puzzle[-1] + 1) % 3 != 0:                           # move right
            nextmove = move(puzzle.copy(), 1)
            openlist.put((heuristic(nextmove), nextmove, tup, 'R '))


def AStarSearch():
    openlist = PriorityQueue()
    openlist.put((0, 0, start, None, ''))                       # f(n), g(n), state, predecessor, Path
    states = 0

    while True:
        if openlist.empty():
            print('Goal Not Found!')
            break

        _, cost, puzzle, prev, path = openlist.get()            # get next state to be traversed
        tup = tuple(puzzle)
        cost += 1

        if tup in visited:                                      # state already visited
            continue
        states += 1

        visited[tup] = (prev, path)                             # mark state as visited

        if puzzle == goal:                                      # goal reached
            total, path = print_path(tup)
            print(f'\nTotal Visited : {states}\nTotal moves -> {total}\nPath        -> {path}')
            break

        if puzzle[-1] > 2:                                      # move up
            nextmove = move(puzzle.copy(), -3)
            openlist.put((cost + heuristic(nextmove), cost, nextmove, tup, 'U '))

        if puzzle[-1] < 6:                                      # move down
            nextmove = move(puzzle.copy(), 3)
            openlist.put((cost + heuristic(nextmove), cost, nextmove, tup, 'D '))

        if puzzle[-1] % 3 != 0:                                 # move left
            nextmove = move(puzzle.copy(), -1)
            openlist.put((cost + heuristic(nextmove), cost, nextmove, tup, 'L '))

        if (puzzle[-1] + 1) % 3 != 0:                           # move right
            nextmove = move(puzzle.copy(), 1)
            openlist.put((cost + heuristic(nextmove), cost, nextmove, tup, 'R '))


if __name__ == '__main__':

    while True:
        print('\n------ Initial State ------\n')
        print_arr(start)
        opt = input('\nEnter 1 to generate random new state > ')
        if opt == '1':
            start = random_start()
            print('\n------ New Initial State ------\n')
            print_arr(start)

        print('\n\n------ Menu ------\n1 -> A Star Search\n2 -> Best First Search\n3 -> Exit')
        opt = input('\nEnter Option > ').strip()

        if opt == '1':
            AStarSearch()
        elif opt == '2':
            BestFirstSearch()
        else:
            break
        visited.clear()