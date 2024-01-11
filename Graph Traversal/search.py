from random import randint
import time

start = []                          # start state 
goal = []
visited = {}

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



def print_arr(arr):                                             # print array in a grid format
    print('-' * 19)
    for i, num in enumerate(arr[:-1]):    
        print('| ', num, end='  ')
        if (i+1) % 3 == 0:
            print('|')
    print('-' * 19)



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



def bfs(queue):
    st = time.time()
    queue.append((start, None, ''))                             # add start state to queue (state, predecessor, move)
    first = 0                                                   # queue head position
    while True:
        if len(queue) == first:
            print('Goal Not Found!')
            break

        puzzle, prev, path = queue[first]                       # get next state to be traversed
        tup = tuple(puzzle)
        first += 1
        
        if tup in visited:                                      # state already visited
            continue

        visited[tup] = (prev, path)                             # mark state as visited

        if puzzle == goal:                                      # goal reached
            total, path = print_path(tup)
            print(f'\nTotal moves -> {total}\nPath        -> {path}\nTime Taken  -> {time.time() - st}')
            break

        if puzzle[-1] > 2:                                      # move up 
            queue.append((move(puzzle.copy(), -3), tup, 'U '))    

        if puzzle[-1] < 6:                                      # move down
            queue.append((move(puzzle.copy(), 3), tup, 'D '))  

        if puzzle[-1] % 3 != 0:                                 # move left
            queue.append((move(puzzle.copy(), -1), tup, 'L '))  

        if (puzzle[-1] + 1) % 3 != 0:                           # move right
            queue.append((move(puzzle.copy(), 1), tup, 'R '))  
 

