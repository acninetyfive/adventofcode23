import numpy as np

in_file = open("test.txt", "r")


def pipe_path(grid, start):
    valid_ups = set(["|", "F", "7"])
    valid_downs = set(["|", "L", "J"])
    valid_lefts = set(["-", "L", "F"])
    valid_rights = set(["-", "J", "7"])

    
    steps = 0
    pos = []
    last_move = None

    
    if start[0] > 0 and grid[start[0] - 1, start[1]][0] in valid_ups:
        pos = [start[0] - 1, start[1]]
        last_move = "up"
    elif start[1] < len(grid[0]) and grid[start[0], start[1] + 1][0] in valid_rights:
        pos = [start[0], start[1] + 1]
        last_move = "right"
    elif start[0] < len(grid) and grid[start[0] + 1, start[1]][0] in valid_downs:
        pos = [start[0] + 1, start[1]]
        last_move = "down"
    elif start[1] > 0 and grid[start[0], start[1] - 1][0] in valid_lefts:
        pos = [start[0], start[1] + 1]
        last_move = "left"
        raise Exception("Only one move off start")

    steps += 1

    #print(steps, pos, grid[pos[0], pos[1]], last_move)

    while grid[pos[0], pos[1]][0] != "S":
        curr_pipe = grid[pos[0], pos[1]][0]

        if curr_pipe == "-":
            if last_move == "right":
                move = "right"
            else:
                move = "left"
        
        elif curr_pipe == "|":
            if last_move == "up":
                move = "up"
            else:
                move = "down"
        
        elif curr_pipe == "L":
            if last_move == "left":
                move = "up"
            else:
                move = "right"
        
        elif curr_pipe == "J":
            if last_move == "right":
                move = "up"
            else:
                move = "left"
        
        elif curr_pipe == "7":
            if last_move == "right":
                move = "down"
            else:
                move = "left"
        
        elif curr_pipe == "F":
            if last_move == "left":
                move = "down"
            else:
                move = "right"
        
        last_move = move

        grid[pos[0], pos[1]] = "^"

        if move == "up":
            pos = [pos[0] - 1, pos[1]]
        elif move == "down":
            pos = [pos[0] + 1, pos[1]]
        elif move == "right":
            pos = [pos[0], pos[1] + 1]
        elif move == "left":
            pos = [pos[0], pos[1] - 1]

        steps += 1
        #print(steps, pos, grid[pos[0], pos[1]], last_move)
    grid[pos[0], pos[1]] = "^"
    
    return steps





g = [list(line.strip("\n")) for line in in_file.readlines()]
grid = np.array(g)

start = np.where(grid == 'S')

p = pipe_path(grid, start)
print(p, p//2)

for r in grid:
    print(r)

print()

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r,c] != "^":
            grid[r,c] = "0"

#top
for c in range(len(grid[0])):
    if grid[0,c] == "0":
        grid[0,c] = 1

#bottom
for c in range(len(grid[0])):
    if grid[len(grid) - 1,c] == "0":
        grid[len(grid) - 1,c] = 1

#left
for r in range(len(grid)):
    if grid[r,0] == "0":
        grid[r,0] = 1

#right
for r in range(len(grid)):
    if grid[r, len(grid[0]) - 1] == "0":
        grid[r, len(grid[0]) - 1] = 1



for r in grid:
    print(r)