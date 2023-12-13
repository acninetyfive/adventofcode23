

in_file = open("test.txt", "r")



def check_valid(springs, coordinates, index):
    s = 0
    c = 0
    block_size = 0

    while s < len(springs):
        if springs[s] == "?":
            return "?"
        if springs[s] == "#":
            if c > index:
                return False
            while s < len(springs) and springs[s] == "#":
                block_size += 1
                s += 1
                if block_size > coordinates[c]:
                    return False
            if block_size < coordinates[c]:
                if s < len(springs) and springs[s] == "?":
                    return "?"
                return False
            if block_size == coordinates[c]:
                block_size = 0
                c += 1

                if c == index:
                    while s < len(springs):
                        if springs[s] == "#":
                            return False
                        if springs[s] == "?":
                            return "?"
                        s += 1
                    return True
                
                else:
                    if s == len(springs):
                        return False
                    if not(springs[s] == "." or springs[s] =="?"):
                        return False
        else:
            s += 1
                     
    return False


global p_counter

def find_all_per(springs, coordinates, start):
    global p_counter
    s = start
    c = 0
    ci = 0
    while s < len(springs): 
        if springs[s] == "?":
            a = springs[:s] + "." + springs[s+1:]
            va = check_valid(a, coordinates, len(coordinates))
            #print("a", a, va)
            #if va == "?":
            find_all_per(a, coordinates, s+1)
            #elif va == True:
            #p_counter += 1

            b = springs[:s] + "#" + springs[s+1:]
            #vb = check_valid(b, coordinates, len(coordinates))
            #print("b", b, vb)
            #if vb == "?":
            find_all_per(b, coordinates, s+1)
            #elif vb == True:
            #p_counter += 1
        s += 1
    
    if check_valid(springs, coordinates, len(coordinates)):
        p_counter += 1
        
    
    return p_counter

    



result_list = []

k = 0

for line in in_file.readlines():
    print(k)
    k += 1
    p_counter = 0
    springs, coord_str = line.split(" ")
    coordinates = [int(s) for s in coord_str.split(",")]
    #print("initial", springs, coordinates)
    result_list.append(find_all_per(springs, coordinates, 0))
    #print(result_list)
    #print("-------")
    

print(sum(result_list))

in_file.close()