import re
with open('day 3/input.txt', 'r') as file:
    total = 0
    do = True
    data = re.findall(r'don\'t\(\)|do\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)', file.read())
    for instruction in data:
        if instruction== 'do()':
            do = True
        elif instruction == 'don\'t()':
            do = False
        elif do == True:
            curr1,curr2 = instruction.strip("mul()").split(',')
            total+= int(curr1) * int(curr2)
        else:
            continue
    print(total)
