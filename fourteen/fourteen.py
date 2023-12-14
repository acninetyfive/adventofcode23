import numpy as np

in_file = open("in.txt", "r")
#part 1 answer is 106517


def get_numbered_grid(f):
    g = []

    for line in f.readlines():
        g.append([int(x) for x in line
                  .strip('\n')
                  .replace("#","5")
                  .replace(".", "0")
                  .replace("O", "1")])

    return np.array(g)


def bin_line(length, line, reverse=False):

    if reverse:
        l = reversed(line)
    else:
        l = line[:]

    c = np.where(l == 5)
    cubes = c[0]

    round_bins = []

    #all round rocks, add one to pretend there's a cube at -1
    round_bins.append((length + 1, np.count_nonzero(l == 1)))

    i = 0
    #count round rocks past each cube
    while i < len(cubes):
        round = np.count_nonzero(line[cubes[i]:] == 1)
        round_bins.append((length - cubes[i], round))

        i += 1
    
    return round_bins


def score_grid(grid):

    scores = []

    for col in range(len(grid[0])):
        score = 0
        rounds = np.where(grid[:,col] == 1)
        for r in rounds[0]:
            score += len(grid[:,col]) - r
        scores.append(score)

        

    return scores

def roll_north(grid):
    for col in range(len(grid[0])):
        cubes = np.where(grid[:,col] == 5)
        cubes = cubes[0]
        if len(cubes) == 0:
            grid[:,col] = -np.sort(-grid[:, col])
        else:
            c = 0
            while c <= len(cubes):
                if c == 0:
                    sort_start = 0
                else:
                    sort_start = cubes[c-1] + 1
                if c == len(cubes):
                    sort_end = len(grid[:,col])
                else:
                    sort_end = cubes[c]

                grid[:,col][sort_start:sort_end] = -np.sort(-grid[:,col][sort_start:sort_end])
                c += 1


def roll_south(grid):
    for col in range(len(grid[0])):
        cubes = np.where(grid[:,col] == 5)
        cubes = cubes[0]
        if len(cubes) == 0:
            grid[:,col] = np.sort(grid[:, col])
        else:
            c = 0
            while c <= len(cubes):
                if c == 0:
                    sort_start = 0
                else:
                    sort_start = cubes[c-1] + 1
                if c == len(cubes):
                    sort_end = len(grid[:,col])
                else:
                    sort_end = cubes[c]

                grid[:,col][sort_start:sort_end] = np.sort(grid[:,col][sort_start:sort_end])
                c += 1


def roll_east(grid):
    for row in range(len(grid)):
        cubes = np.where(grid[row,:] == 5)
        cubes = cubes[0]
        if len(cubes) == 0:
            grid[row,:] = np.sort(grid[row, :])
        else:
            c = 0
            while c <= len(cubes):
                if c == 0:
                    sort_start = 0
                else:
                    sort_start = cubes[c-1] + 1
                if c == len(cubes):
                    sort_end = len(grid[row,:])
                else:
                    sort_end = cubes[c]

                grid[row,:][sort_start:sort_end] = np.sort(grid[row,:][sort_start:sort_end])
                c += 1


def roll_west(grid):
    for row in range(len(grid)):
        cubes = np.where(grid[row,:] == 5)
        cubes = cubes[0]
        if len(cubes) == 0:
            grid[row,:] = -np.sort(-grid[row, :])
        else:
            c = 0
            while c <= len(cubes):
                if c == 0:
                    sort_start = 0
                else:
                    sort_start = cubes[c-1] + 1
                if c == len(cubes):
                    sort_end = len(grid[row,:])
                else:
                    sort_end = cubes[c]

                grid[row,:][sort_start:sort_end] = -np.sort(-grid[row,:][sort_start:sort_end])
                c += 1


def cycle(grid):
    roll_north(grid)

    roll_west(grid)
    
    roll_south(grid)   
    
    roll_east(grid)


    



grid = get_numbered_grid(in_file)

runs = 1000

for i in range(runs):
    print(i)
    cycle(grid)

scores = score_grid(grid)

print(sum(scores))


in_file.close()