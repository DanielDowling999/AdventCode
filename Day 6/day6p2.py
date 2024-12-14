import time
t1 = time.time()

def createMap(filename):
    with open(filename,'r') as zone:
        patrolMap = []
        for line in zone:
            patrolMap.append(list(line.strip()))
        #print(patrolMap)

        for i in range(len(patrolMap)):
            for j in range(len(patrolMap[0])):
                if patrolMap[i][j] == '^':
                    currPos = [i, j]
                    #currPos is y,x
                    break
    return patrolMap, currPos

def checkRoute(patrolMap, currPos, p2):
#direction is -j for up, j for down, -1 for left and 1 for right
    leaving = False
    direction = -1j
    uniquePos = set()
    while not leaving:
        if (currPos[0] == 0 and direction == -1j) or (currPos[0] == len(patrolMap)-1 and direction == 1j) or (currPos[1] == 0 and direction == -1) or (currPos[1] == len(patrolMap[0])-1 and direction == 1):
            leaving = True
        else:
            match direction:
                case -1j:
                    if patrolMap[currPos[0]-1][currPos[1]] == '#':
                        direction = 1
                    else:
                        currPos[0] = currPos[0] -1
                case 1:
                    if patrolMap[currPos[0]][currPos[1]+1] == '#':
                        direction = 1j
                    else:
                        currPos[1] = currPos[1] + 1
                case 1j:
                    if patrolMap[currPos[0]+1][currPos[1]] == '#':
                        direction = -1
                    else:
                        currPos[0] = currPos[0] + 1
                case -1:
                    if patrolMap[currPos[0]][currPos[1]-1] == '#':
                        direction = -1j
                    else:
                        currPos[1] = currPos[1] - 1
                case _:
                    print("Error: Guard is trapped in a box!")
                    break
            if p2 == False:
                uniquePos.add(tuple(currPos))
            else:
                fullPos = tuple([currPos[0], currPos[1], direction])
                if fullPos in uniquePos:
                    return 1
                else:
                    uniquePos.add(fullPos)
    if not p2:
        print(len(uniquePos)+1)

        return uniquePos
    else:
        return 0       


patrolMap, currPos = createMap('day 6/input.txt')
startY = currPos[0]
startX = currPos[1]
guardRoute = checkRoute(patrolMap, currPos, False)
loops = 0
#print(guardRoute)
for pos in guardRoute:
    if not(pos[0] == startY and pos[1] == startX):
        patrolMap[pos[0]][pos[1]] = '#'
        loops+=checkRoute(patrolMap, [startY, startX], True)
    patrolMap[pos[0]][pos[1]] = '.'
print(loops)
t2 = time.time()
print(t2 - t1)

#create guard's path.
#check if placing a # on each part of the path creates a loop
#if it does, count it.
#if it doesn't, move onto next

#how to check:
#Option 1: record direction with the co-ordinates. If we've already travelled in this direction
#through this co-ordinate, then we know we have looped.