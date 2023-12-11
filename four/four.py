import re

in_file = open("in.txt", "r")

winners = []

tickets = {}

i = 0
for line in in_file.readlines():
    ticket = line.split(":")[1]
    win_num_str, my_num_str = ticket.split("|")

    win_num = set(re.split(r'\s{1,}', win_num_str.strip()))
    my_num = re.split(r'\s{1,}', my_num_str.strip())
    
    tickets[i] = [1, win_num, my_num]
    i += 1

ticket_count = 0
for i in range(len(tickets)):
    ticket_count += tickets[i][0]

    matches = 0

    for n in tickets[i][2]:
        if n in tickets[i][1]:
            matches += 1
    
    j = 1
    while j <= matches:
        tickets[i + j][0] += tickets[i][0] 
        j += 1
    

print(ticket_count)

in_file.close