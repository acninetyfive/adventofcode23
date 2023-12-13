import re
import numpy as np

in_file = open("in.txt", "r")

l_one = in_file.readline()
l_two = in_file.readline()
times = [int(x) for x in re.split(r'\s{1,}', l_one.split(":")[1].strip())]
distances = [int(x) for x in re.split(r'\s{1,}', l_two.split(":")[1].strip())]


def check_wins(time, distance):
    last_bad = None
    first_good = None

    if time % 2 == 0:
        upper = time/2
    else:
        upper = time//2 + 1
    if upper * (time - upper) <= distance:
        return 0
    
    lower = 1
    if lower * (time - lower) > distance:
        return time - 1
    
    while lower < upper - 1:
        guess = lower + (upper - lower) // 2
        
        if guess * (time - guess) > distance:
            upper = guess
        else:
            lower = guess
       
    
    return time - 2 * lower - 1
    
    









results = []

for i in range(len(times)):
    results.append(check_wins(times[i], distances[i]))
    #print(results)
    


print(results)
print(np.prod(results))


in_file.close()