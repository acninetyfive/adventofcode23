
in_file = open("in.txt", "r") 

def is_symbol(c):
    if c.isdigit():
        return False
    if c == ".":
        return False
    return True

def check_valid(grid, start, end):
    #print("valid?", start, end)
    top_row = None
    bottom_row = None
    start_col = None
    end_col = None

    if start[0] > 0:
        top_row = start[0] - 1
    if start[0] < len(grid) - 1:
        bottom_row = start[0] + 1

    if start[1] > 0:
        start_col = start[1] - 1
    else:
        start_col = start[1]
    
    if end[1] < len(grid[0]) - 1:
        end_col = end[1] + 1
    else:
        end_col = end[1]

    if top_row is not None:
        for i in range(start_col, end_col + 1):
            if is_symbol(grid[top_row][i]):
                return True
    
    if bottom_row is not None:
        for i in range(start_col, end_col + 1):
            if is_symbol(grid[bottom_row][i]):
                return True
    
    if is_symbol(grid[start[0]][start_col]):
        return True
    if is_symbol(grid[start[0]][end_col]):
        return True
    
    return False


def get_all_numbers(grid):

    numbers = []

    for r in range(len(grid)):
        i = 0
        num_string = ""
        num_start = None
        num_end = None
        while i < len(grid[r]):
            if grid[r][i].isdigit():
                if num_start is None:
                    num_start = (r, i)
                    num_end = (r, i)
                else:
                    num_end = (r, i)
                num_string += grid[r][i]
            else:
                if num_start is not None:
                    if check_valid(grid, num_start, num_end):
                        numbers.append(int(num_string))
                num_start = None
                num_end = None
                num_string = ""
            i += 1
        if num_start is not None:
            if check_valid(grid, num_start, num_end):
                numbers.append(int(num_string))

    return numbers

def find_ratio(grid, gear):
    
    adj_nums = []

    left = None
    right = None
    top = None
    bottom = None

    if gear[0] > 0:
        top = gear[0] - 1
    else:
        top = gear[0]
    if gear[0] < len(grid) - 1:
        bottom = gear[0] + 1
    else:
        bottom = gear[0]

    if gear[1] > 0:
        left = gear[1] - 1
    else: 
        left = gear[1]
    if gear[1] < len(grid[0]) + 1:
        right = gear[1] + 1
    else:
        right = gear[1]


    #check left side
    if grid[gear[0]][left].isdigit():
        num = ""
        i = left
        while i >= 0 and grid[gear[0]][i].isdigit():
            num = grid[gear[0]][i] + num
            i -= 1
        adj_nums.append(int(num))
    
    #check right side
    if grid[gear[0]][right].isdigit():
        num = ""
        i = right
        while i < len(grid[0]) and grid[gear[0]][i].isdigit():
            num = num + grid[gear[0]][i]
            i += 1
        adj_nums.append(int(num))

    #check top side
    i = left
    while i <= right:
        if grid[top][i].isdigit():
            num = ""
            #go left
            j = i
            while j >= 0 and grid[top][j].isdigit():
                num = grid[top][j] + num
                j -= 1

            #go right
            k = i + 1
            while k < len(grid[0]) and grid[top][k].isdigit():
                num = num + grid[top][k]
                k += 1
            adj_nums.append(int(num))
            if len(adj_nums) > 2:
                return None
            
            i = k
        else:
            i += 1

    #check bottom side
    i = left
    while i <= right:
        if grid[bottom][i].isdigit():
            num = ""
            #go left
            j = i
            while j >= 0 and grid[bottom][j].isdigit():
                num = grid[bottom][j] + num
                j -= 1

            #go right
            k = i + 1
            while k < len(grid[0]) and grid[bottom][k].isdigit():
                num = num + grid[bottom][k]
                k += 1
            adj_nums.append(int(num))
            if len(adj_nums) > 2:
                return None
            
            i = k
        else:
            i += 1
    
    if len(adj_nums) == 2:
        return adj_nums[0] * adj_nums[1]
    return None



    


def find_gears(grid):
    gear_ratios = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "*":
                ratio = find_ratio(grid, (r, c))
                if ratio is not None:
                    gear_ratios.append(ratio)
    
    return gear_ratios



def init_grid(f):
    grid = []

    for line in f.readlines():
        row = list(line.strip('\n'))
        grid.append(row)

    return grid

        
grid = init_grid(in_file)


#num_list = get_all_numbers(grid)

print(sum(find_gears(grid)))



in_file.close()