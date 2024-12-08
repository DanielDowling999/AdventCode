#First thought, a search starting from every 'x', checking each element in every direction. If the
#next is an m, continue in that direction until we reach s or it breaks. Could check if 

#possibly faster solution (and easier to handle) is to get every possible 'word' from x, and 
#then process them all at once. 


with open('day 4/input.txt', 'r') as wordSearch:
    xmasCount = 0
    xmasArray = []
    wordArray = []
    for line in wordSearch:
        wordArray.append(line.strip())
    #print(wordArray)

    rowLen = len(wordArray)
    colLen = len(wordArray[0])

    for i in range(rowLen):
        for j in range(colLen):
            if wordArray[i][j] == 'X':
                #check in all directions including diagonals
                if i >= 3:
                    #vertical up
                    xmasArray.append(wordArray[i][j] + wordArray[i-1][j] + wordArray[i-2][j] + wordArray[i-3][j])
                    if j >= 3:
                        #diagonal up-left
                        xmasArray.append(wordArray[i][j] + wordArray[i-1][j-1] + wordArray[i-2][j-2] + wordArray[i-3][j-3])
                    if j < colLen-3:
                        #diagonal up-right
                        xmasArray.append(wordArray[i][j] + wordArray[i-1][j+1] + wordArray[i-2][j+2] + wordArray[i-3][j+3])
                if i < rowLen-3:
                    #vertical down
                    xmasArray.append(wordArray[i][j] + wordArray[i+1][j] + wordArray[i+2][j] + wordArray[i+3][j])
                    if j >= 3:
                        #diagonal down-left
                        xmasArray.append(wordArray[i][j] + wordArray[i+1][j-1] + wordArray[i+2][j-2] + wordArray[i+3][j-3])
                    if j < colLen-3:
                        #diagonal down-right
                        xmasArray.append(wordArray[i][j] + wordArray[i+1][j+1] + wordArray[i+2][j+2] + wordArray[i+3][j+3])
                
                if j < colLen-3:
                    #horizontal right
                    xmasArray.append(wordArray[i][j] + wordArray[i][j+1] + wordArray[i][j+2] + wordArray[i][j+3])
                if j >= 3:
                    #horizontal left
                    xmasArray.append(wordArray[i][j] + wordArray[i][j-1] + wordArray[i][j-2] + wordArray[i][j-3]) 
    for xmas in xmasArray:
        if xmas == 'XMAS':
            xmasCount += 1
    print(xmasCount)


