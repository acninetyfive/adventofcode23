in_file = open("in.txt", "r") 


cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_game_possible(rounds):
    for round in rounds:
        subrounds = round.split(",")

        for subround in subrounds:
            i = 1
            count_string = ""
            while subround[i].isdigit():
                count_string += subround[i]
                i += 1
            count = int(count_string)
            color = subround[i+1:]
            
            if cubes[color] < count:
                return False
    return True

def fewest_cubes(rounds):

    max_color_dict = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for round in rounds:
        subrounds = round.split(",")

        for subround in subrounds:
            i = 1
            count_string = ""
            while subround[i].isdigit():
                count_string += subround[i]
                i += 1
            count = int(count_string)
            color = subround[i+1:]

            if max_color_dict[color] < count:
                max_color_dict[color] = count
            
            
    return max_color_dict
        


playable_games = []

cube_powers = []


for line in in_file:
    game_number_string = ""
    i = 5
    while line[i] != ":":
        game_number_string += line[i]
        i += 1
    game_number = int(game_number_string)
    
    rounds_string = line[i + 1:]

    rounds = rounds_string.strip("\n").split(";")

    cubes_dict = fewest_cubes(rounds)

    cube_power = cubes_dict["red"] * cubes_dict["green"] * cubes_dict["blue"]
    cube_powers.append(cube_power)


print(sum(cube_powers))







in_file.close()