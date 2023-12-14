import numpy as np

in_file = open("in.txt", "r")



def bin_line(length, line, reverse=False):

    if reverse:
        l = reversed(line)
    else:
        l = line[:]

    c = np.where(l == "#")
    cubes = c[0]

    round_bins = []

    #all round rocks, add one to pretend there's a cube at -1
    round_bins.append((length + 1, np.count_nonzero(l == 'O')))

    i = 0
    #count round rocks past each cube
    while i < len(cubes):
        round = np.count_nonzero(line[cubes[i]:] == 'O')
        round_bins.append((length - cubes[i], round))

        i += 1
    
    return round_bins


def score_grid(grid):

    scores = []

    for col in range(len(grid[0])):
        #print("col", col)

        bins = bin_line(len(grid), grid[:,col])

        b = list(reversed(bins))

        score = 0

        counted_rocks = 0

        for i in range(len(b)):
            active_rocks = b[i][1] - counted_rocks

            score += sum(range(b[i][0] - active_rocks, b[i][0]))
                            
            counted_rocks += active_rocks
        
        scores.append(score)

    return scores


def adjust_line(line, bins, reverse=False):

    if reverse:
        b = reversed(bins)
    else:
        b = bins[:]

    line[0] = "%"



    print("line", line)
    print("bins", bins)
    print()


def cycle(grid):
    col = 1
    



g = []

for line in in_file.readlines():
    g.append([x for x in line.strip('\n')])

grid = np.array(g)

scores = score_grid(grid)


print(scores)
print(sum(scores))




in_file.close()