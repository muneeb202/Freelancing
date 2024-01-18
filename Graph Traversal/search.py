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
 


def dfs(stack):
    st = time.time()
    stack.append((start, None, 0))                              # add start state to the stack (state, predecessor, moves so far)

    while True:
        if len(stack) == 0:                                     # if no more possible moves, no goal found
            print('Goal Not Found!')                    
            break
        
        puzzle, prev, moves = stack.pop()                       # get next state to be traversed
        tup = tuple(puzzle)

        if tup in visited:                                      # state already visited
            continue

        visited[tup] = prev                                     # mark state as visited

        if puzzle == goal:                                      # goal reached
            print(f'Total moves -> {moves}\nTime Taken  -> {time.time() - st}')
            # print(f'\nTotal moves -> {print_path(tup)}')
            # while visited[tup] is not None:
            #     print_arr(tup)
            #     tup = visited[tup]
            break

        if puzzle[-1] % 3 != 0:                                 # move left
            stack.append((move(puzzle.copy(), -1), tup, moves + 1)) 

        if puzzle[-1] < 6:                                      # move down
            stack.append((move(puzzle.copy(), 3), tup, moves + 1))   

        if puzzle[-1] > 2:                                      # move up 
            stack.append((move(puzzle.copy(), -3), tup, moves + 1))   

        if (puzzle[-1] + 1) % 3 != 0:                           # move right
            stack.append((move(puzzle.copy(), 1), tup, moves + 1)) 



def dls(maxdepth, stack):
    stack.append((start, None, 1, ''))                          # add start state to stack (state, predecessor, depth, move)
    end = True                                                  # True: no goal possible, False: Goal not found at current depth

    while True:
        if len(stack) == 0:                                     # if stack empty, return status of end
            return None, end

        puzzle, prev, depth, step = stack.pop()                 # traverse next state
        tup = tuple(puzzle)

        if tup in visited:                                      # state already visited
            _, _, old_depth = visited[tup]                      # get depth of already visited state
            if old_depth < depth:                               # if older path was shorter, ignore state. Else shorter path found
                continue

        visited[tup] = (prev, step, depth)                      # mark state as visited

        if puzzle == goal:                                      # if goal found, return ending state
            return tup, False 
        
        if depth + 1 > maxdepth:                                # if current depth is max
            end = False                                         # do not end search
            continue                                            # instead, dont visit children (below max depth)

        if puzzle[-1] > 2:                                      # move up 
            stack.append((move(puzzle.copy(), -3), tup, depth + 1, 'U '))  

        if puzzle[-1] < 6:                                      # move down
            stack.append((move(puzzle.copy(), 3), tup, depth + 1, 'D '))   

        if puzzle[-1] % 3 != 0:                                 # move left
            stack.append((move(puzzle.copy(), -1), tup, depth + 1, 'L '))

        if (puzzle[-1] + 1) % 3 != 0:                           # move right
            stack.append((move(puzzle.copy(), 1), tup, depth + 1, 'R ')) 



def ids():
    st = time.time()
    count = 0                                                   # current max depth
    while True:
        count += 1                                              # increase depth
        visited.clear()                                         # clear visited states, i.e. start anew
        result, end = dls(count, [])                            # try finding goal till current max depth
        
        if result != None:                                      # if goal found
            total, path = print_path(result)                    # print solution path
            print(f'\nTotal moves -> {total}\nPath        -> {path}\nTime Taken  -> {time.time() - st}')
            break
        elif end == True:                                       # if unable to go beyond current max depth i.e. no goal possible
            print('Max depth reached! Goal Not Found')
            break


if __name__ == '__main__':

    try:
        while len(start := [int(n) for n in input('\nEnter start state > ')]) != 9:
            print('Enter 9 digits! Try Again\n')
    except ValueError:
        print('Enter 9 digits! Try Again\n')
    
    try:
        while len(goal := [int(n) for n in input('\nEnter goal state  > ')]) != 9:
            print('Enter 9 digits! Try Again\n')
    except ValueError:
        print('Enter 9 digits! Try Again\n')

    for i, n in enumerate(start):
        if n == 0:
            start.append(i)
            break

    for i, n in enumerate(goal):
        if n == 0:
            goal.append(i)
            break


    print('\n------ Initial State ------\n')
    print_arr(start)
    opt = input('\nEnter 1 to generate random new state > ')
    if opt == '1':
        start = random_start()
        print('\n------ New Initial State ------\n')
        print_arr(start)

    while True:
        print('\n\n------ Menu ------\n1 -> Breadth First Search\n2 -> Depth First Search\n3 -> Iterative Deepening Search\n4 -> Exit')
        opt = input('\nEnter Option > ').strip()

        if opt == '1':
            bfs([])
        elif opt == '2':
            dfs([])
        elif opt == '3':
            ids()
        else:
            break
        visited.clear()
