def compareFn(a,b, rules):
    #print(a,b)
    if [a,b] in rules:
        return 1
    elif [b,a] in rules:
        return 0
    else:
        return 1
    
def findIncorrectUpdates(rules, updates):
    incorrectUpdates = []
    for update in updates:
        for i in range(len(update)-1):
            correct = True
            for j in range(i+1, len(update)):
                if compareFn(update[i],update[j],rules) == 1:
                    continue
                else:
                    incorrectUpdates.append(update)
                    correct = False
                    break
            if correct == False:
                break
    return incorrectUpdates
    #print(mid)    
    #print(updates)

def processFile(filename):
    with open(filename, 'r') as update:
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
    return rules, updates

def sortUpdate(rules, update):
    sortedUpdate = []
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if compareFn(update[i], update[j], rules) == 0:
                sortedUpdate.append(update[j])
                update[j] = update[i]
                update[i] = sortedUpdate.pop()
                
    return int(update[int(len(update)/2)])


rules, updates = processFile('day 5/input.txt')
incorrectUpdates = findIncorrectUpdates(rules, updates)
print(incorrectUpdates)
mid = 0
for update in incorrectUpdates:
    mid += sortUpdate(rules, update)
print(mid)

