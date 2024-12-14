def compareFn(a,b, rules):
    #print(a,b)
    if [a,b] in rules:
        return 1
    elif [b,a] in rules:
        return 0
    else:
        return 1
with open('day 5/input.txt', 'r') as update:
    rules = []
    updates = []
    line = update.readline()
    while line != '\n':
        rules.append((line.strip().split('|')))
        line = next(update)
    #print(rules)
    line = next(update)
    while line != '\n':
        try:
            updates.append(line.strip().split(','))
            line = next(update)
        except:
            break
    mid = 0
    for update in updates:
        for i in range(len(update)-1):
            correct = True
            for j in range(i+1, len(update)):
                if compareFn(update[i],update[j],rules) == 1:
                    continue
                else:
                    print("line: ", update, " broken")
                    correct = False
                    break
            if correct == False:
                break
        if correct:
            addMid = int(update[int(len(update)/2)])
            mid += addMid
    print(mid)    
    #print(updates)