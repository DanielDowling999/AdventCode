with open('day 5/input.txt', 'r') as update:
    ruleDict = {}
    line = update.readline()
    middle = 0
    while line != '\n':
        r1,r2 = line.strip().split('|')
        #print(r1, r2)
        if r1 in ruleDict:
            ruleDict[r1].append(r2)
        else:
            ruleDict[r1] = [r2]
        line = next(update)
        #print(line)
    #print(ruleDict['23'])
    line = next(update)
    while line !='\n':
        line = line.strip().split(',')
        try:
            line = next(update) 
        except:
            break
    print(middle)