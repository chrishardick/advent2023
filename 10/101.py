#!/usr/local/bin/python3
#==========
# 101.py
#==========

import sys

matrix = []

# (y,x)
start = None

max_x = None
max_y = None

valid_pipe_char = { '|', '-', 'L', 'J', '7', 'F', 'S' }

max_steps = 0

pos_min_steps_dict = {}

verbose = False

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
        if nxt_c == '|' or nxt_c == 'L' or nxt_c == 'J':
            return True

    return False
        

def dfs_iter (pos, visited, path, num_steps):

    stack = []

    stack.append((pos,num_steps))

    while len(stack) != 0:

        curr = stack.pop()

        curr_pos        = curr[0]
        lcl_num_steps   = curr[1]

        y = curr_pos[0]
        x = curr_pos[1]

        visited.add(curr_pos)
        path.append(curr_pos)

        verbose and print ("dfs_iter: ENTER"
            " y", y
            ," x", x 
            ," char", matrix[y][x] 
            ," path", path
            ," visited", visited
            ," num_steps", num_steps
            )

        if curr_pos == start and lcl_num_steps > 1:
            # we found path
            #print ("dfs_iter: PATH FOUND. path=", path)
            return True
    
        if lcl_num_steps > 1 and start in visited:
            visited.remove(start)

        if curr_pos in pos_min_steps_dict:
            if lcl_num_steps < pos_min_steps_dict[curr_pos]:
                pos_min_steps_dict[curr_pos] = lcl_num_steps
                verbose and print ("dfs_iter: min steps to ", curr_pos, " is ", lcl_num_steps)
        else:
            pos_min_steps_dict[curr_pos] = lcl_num_steps
            verbose and print ("dfs_iter: min steps to ", curr_pos, " is ", lcl_num_steps)

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

                stack.append((n,lcl_num_steps+1))


def find_loop ():

    y = start[0]
    x = start[1]

    path = []

    visited = set()

    for pos in [(y,x-1), (y,x+1), (y-1,x), (y+1,x)]:

        if valid_start_move (start, pos):

            path.clear()
            path.append(start)

            visited.clear()
            visited.add(start)

            visited.add(pos)
            path.append(pos)

            print ("\nfind_loop: pos=", pos)

            dfs_iter (pos, visited, path, 1)


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
    verbose and print ("pos:", x, " min steps:", pos_min_steps_dict[x])
    if pos_min_steps_dict[x] > max_value:
        max_value = pos_min_steps_dict[x]

print ("max value:", max_value)
