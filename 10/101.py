#!/usr/local/bin/python3
#==========
# 101.py
#==========

import sys

sys.setrecursionlimit(10000)

matrix = []

# (y,x)
start = None

max_x = None
max_y = None

valid_pipe_char = { '|', '-', 'L', 'J', '7', 'F', 'S' }

max_steps = 0

pos_min_steps_dict = {}

verbose = True

def valid_position (pos):

    y = pos[0]
    x = pos[1]

    if y < 0 or y > max_y:
        return False

    if x < 0 or x > max_x:
        return False

    return True

    
def valid_start_move (curr, nxt):

    curr_y = curr[0]
    curr_x = curr[1]

    curr_c = matrix[curr_y][curr_x]

    nxt_y = nxt[0]
    nxt_x = nxt[1]


    # ensure we're not moving off the board

    if not valid_position((nxt_y,nxt_x)):
        return False


    nxt_c = matrix[nxt_y][nxt_x]

    diff_y = nxt_y - curr_y
    diff_x = nxt_x - curr_x

    if diff_x and diff_y:
        print ("INVALID MOVE - both X and Y CANNOT CHANGE")
        sys.exit(-1)

    if diff_x > 0:      # right (east)
        if nxt_c == '-' or nxt_c == 'J' or nxt_c == '7':
            return True
    elif diff_x < 0:    # left (west)
        if nxt_c == '-' or nxt_c == 'L' or nxt_c == 'F':
            return True
    elif diff_y < 0:    # up (north)
        if nxt_c == '|' or nxt_c == '7' or nxt_c == 'F':
            return True
    elif diff_y > 0:    # down (south)
        if nxt_c == '|' or nxt_c == 'L' or nxt_c == 'W':
            return True

    return False
        

def dfs (pos, visited, path, num_steps):

    y = pos[0]
    x = pos[1]

    verbose and print ("dfs: ENTER"
        " y", y
        ," x", x 
        ," char", matrix[y][x] 
        ," path", path
        ," visited", visited
        ," num_steps", num_steps
        )


    if pos == start and num_steps > 1:
        # we found path
        print ("dfs: PATH FOUND")
        return True
    
    if num_steps > 1 and start in visited:
        visited.remove(start)

    if pos in pos_min_steps_dict:
        if num_steps < pos_min_steps_dict[pos]:
            pos_min_steps_dict[pos] = num_steps
            print ("dfs: min steps to ", pos, " is ", num_steps)
    else:
        pos_min_steps_dict[pos] = num_steps
        print ("dfs: min steps to ", pos, " is ", num_steps)


    nxt = []

    if matrix[y][x] == '|':

        nxt.append((y-1,x))
        nxt.append((y+1,x))

    elif matrix[y][x] == '-':

        nxt.append((y,x-1))
        nxt.append((y,x+1))

    elif matrix[y][x] == 'L':

        nxt.append((y-1,x))
        nxt.append((y,x+1))

    elif matrix[y][x] == 'J':

        nxt.append((y-1,x))
        nxt.append((y,x-1))

    elif matrix[y][x] == '7':

        nxt.append((y+1,x))
        nxt.append((y,x-1))

    elif matrix[y][x] == 'F':

        nxt.append((y+1,x))
        nxt.append((y,x+1))

    else:

        print ("INVALID CHARACTER - ", matrix[y][x])
        sys.exit(-1)


    for n in nxt:
   
        if valid_position(n) and n not in visited:
        
            visited.add(n)
            path.append(n)

            rc = dfs(n, visited, path, num_steps+1)

            if rc:
                return rc

            path.pop()
            visited.remove(n)



def find_loop ():

    y = start[0]
    x = start[1]

    path = []

    path.append(start)

    visited = set()

    for pos in [(y,x-1), (y,x+1), (y-1,x), (y+1,x)]:

        if valid_start_move (start, pos):

            path.clear()
            path.append(start)

            visited.clear()
            visited.add(start)

            visited.add(pos)
            path.append(pos)

            verbose and print ("\nfind_loop: pos=", pos)

            dfs (pos, visited, path, 1)

            path.pop()
            visited.remove(pos)


#==========
# main
#==========

# parse input, load matrix


y = 0


for line in sys.stdin:

    line = line.rstrip()

    x = line.find('S')

    if x != -1:
        start = (y,x)

    matrix.append(line)

    y = y + 1


max_x = len(matrix[0]) - 1
max_y = len(matrix) - 1


# print matrix

print ("matrix")

sum = 0

for line in matrix:

    print (line)

print ("")

print ("max_x=",max_x)
print ("max_y=",max_y)

print ("")

print ("start=",start)

print ("")

find_loop()


max_value = 0

for x in pos_min_steps_dict:
    print ("pos:", x, " min steps:", pos_min_steps_dict[x])
    if pos_min_steps_dict[x] > max_value:
        max_value = pos_min_steps_dict[x]

print ("max value:", max_value)
 




