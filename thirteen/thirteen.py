import numpy as np

in_file = open("in.txt", "r")

def count_diffs_v(a, b):
    if len(a) > len(b):
        a = a[len(a) - len(b):]
    if len(a) < len(b):
        b = b[:len(a)]
    return (a != b[::-1]).sum()

def count_diffs_h(a, b):
    if len(a) > len(b):
        a = a[len(a) - len(b):]
    if len(a) < len(b):
        b = b[:len(a)]
    return (a != b[::-1]).sum()


def find_horizontal(grid):
    r = 0
    while r < len(grid) - 1:
        up_r = r 
        down_r = r + 1
        
        c = 0
        diffs = 0
        while c < len(grid[0]) and diffs <= 1:
            d = count_diffs_h(grid[:up_r + 1, c], grid[down_r:,c])
            c += 1
            diffs += d           
        if diffs == 1:
            return r + 1
        
        r += 1

    return None


def find_vertical(grid):
    c = 0
    while c < len(grid[0]) - 1:
        left_c = c 
        right_c = c + 1

        r = 0
        diffs = 0
        while r < len(grid) and diffs <= 1:
            d = count_diffs_v(grid[r, :left_c + 1], grid[r, right_c:])
            r += 1
            diffs += d
        if diffs == 1:
            return c + 1
        
        c += 1

    return None




results = []
g = []

i = 0

for line in in_file.readlines():
    if line.strip("\n") != "":
        g.append(list(line.strip()))
    else:
        grid = np.array(g)
        h = find_horizontal(grid)
        if h is not None:
            results.append(h * 100)
        else:
            v = find_vertical(grid)
            if v is not None:
                results.append(v)
            else:
                print("grid error:", i)
                raise Exception("No reflection")
        g = []
        i += 1

i += 1
grid = np.array(g)
h = find_horizontal(grid)
if h is not None:
    results.append(h * 100)
else:
    v = find_vertical(grid)
    if v is not None:
        results.append(v)
    else:
        print("grid error:", i)
        raise Exception("No reflection")


print(results)
print(sum(results))


in_file.close()