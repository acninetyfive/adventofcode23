
in_file = open("in.txt", "r") 

calibration_values = []
digits_spelled = {"z":["zero"], 
                  "o":["one"], 
                  "t": ["two", "three"], 
                  "f": ["four", "five"], 
                  "s": ["six", "seven"], 
                  "e": ["eight"], 
                  "n": ["nine"]
                }

word_to_digit = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def number_from_digits(first_digit, last_digit):
    return int(first_digit+last_digit)

def check_spelled_digit(line, start):

    for digit in digits_spelled[line[start]]:
        i = 1
        while i < len(digit) and start + i < len(line):
            if line[start + i] != digit[i]:
                break
            i += 1
            if i == len(digit):
                return (word_to_digit[digit], 0)
            
    return (None, 0)


for line in in_file:
    first_digit = None
    last_digit = None
    i = 0
    while i < len(line):
        if line[i].isdigit():
            if first_digit is None:
                first_digit = line[i]
                last_digit = line[i]
            else:
                last_digit = line[i]
        elif line[i] in digits_spelled:
            spelled_digit, offset = check_spelled_digit(line, i)
            i += offset
            if spelled_digit is not None:
                if first_digit is None:
                    first_digit = spelled_digit
                    last_digit = spelled_digit
                else:
                    last_digit = spelled_digit

        i += 1
    calibration_values.append(number_from_digits(first_digit, last_digit))
    #print(calibration_values)
    #input()           

    

in_file.close()

print("Done!")
print(len(calibration_values))
print(sum(calibration_values))
