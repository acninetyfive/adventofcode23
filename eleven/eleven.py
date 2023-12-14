import numpy as np
from scipy.spatial.distance import cityblock



#define vectors
A = [2, 4, 4, 6]
B = [5, 5, 7, 8]

#calculate Manhattan distance between vectors
cityblock(A, B)

def get_grid(f):
    return np.array(
        [[x for x in line.strip("\n")] for line in f.readlines()]
    )


def expand_space(g):
    #rows
    r = 0
    while r < len(g):
        if "#" not in g[r,:]:
            g = np.insert(g, r, np.array(["." * len(g[0])]), axis=0)
            r += 1
        r += 1
    
    #columns
    c = 0
    while c < len(g[0]):
        if "#" not in g[:,c]:
            g = np.insert(g, c, np.array(["." * len(g)]), axis=1)
            c += 1
        c += 1
    
    return g


def mega_expand_space(g, x):
    expansion_rows = []
    expansion_columns = []
    #rows
    r = 0
    while r < len(g):
        if "#" not in g[r,:]:
            expansion_rows.append(r)
        r += 1
    
    #columns
    c = 0
    while c < len(g[0]):
        if "#" not in g[:,c]:
            expansion_columns.append(c)
            c += 1
        c += 1
    
    g_arr = np.where(g == "#")
    galaxies = np.array([g_arr[0], g_arr[1]])

    for i in range(len(galaxies[0])):
        ex = np.count_nonzero(expansion_rows < galaxies[0][i])
        galaxies[0][i] = galaxies[0][i] + ex * (x - 1)

    for i in range(len(galaxies[1])):
        ex = np.count_nonzero(expansion_columns < galaxies[1][i])
        galaxies[1][i] = galaxies[1][i] + ex * (x - 1)
    
    return galaxies


def get_distances(galaxies):
    distances = []

    a = 0
    while a < len(galaxies[0]) - 1:
        b = a + 1
        while b < len(galaxies[0]):
            d = cityblock([galaxies[0][a], galaxies[1][a]], [galaxies[0][b], galaxies[1][b]])
            distances.append(d)
            b += 1
            
        a += 1
    
    return distances


in_file = open("in.txt")

grid = get_grid(in_file)


print()

gal = mega_expand_space(grid, 1000000)

print("expanded", len(gal[0]))

d = get_distances(gal)

print(sum(d))

