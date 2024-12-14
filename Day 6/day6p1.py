with open('day 6/input.txt','r') as zone:
    patrolMap = []
    for line in zone:
        patrolMap.append(line.strip())
    #print(patrolMap)

    for i in range(len(patrolMap)):
        for j in range(len(patrolMap[0])):
            if patrolMap[i][j] == '^':
                currPos = [i, j]
                break
    #currPos is y,x
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
            uniquePos.add(tuple(currPos))

                
    print(len(uniquePos)+1)


