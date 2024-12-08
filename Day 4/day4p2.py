with open('day 4/input.txt', 'r') as wordSearch:
    xMasCount = 0
    xMasArray = []
    wordArray = []
    for line in wordSearch:
        wordArray.append(line.strip())

    rowLen = len(wordArray)
    colLen = len(wordArray[0])

    #check every 'a' as the center, for an m and s on both sides.
    for i in range(rowLen):
        for j in range(colLen):
            if wordArray[i][j] == 'A':
                #check the diagonals
                left = False
                right = False
                if i >= 1 and j >= 1 and i < rowLen-1 and j<colLen-1:
                    if wordArray[i-1][j-1] == 'M':
                        if wordArray[i+1][j+1] == 'S':
                            left = True
                    elif wordArray[i-1][j-1] == 'S':
                        if wordArray[i+1][j+1] == 'M':
                            left = True
                    if left == True:
                        if wordArray[i-1][j+1] == 'M':
                            if wordArray[i+1][j-1] == 'S':
                                right = True
                        elif wordArray[i-1][j+1] == 'S':
                            if wordArray[i+1][j-1] == 'M':
                                right = True
                    if right == True:
                        xMasCount+=1
    
    print(xMasCount)

