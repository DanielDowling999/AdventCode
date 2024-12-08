with open('day 2/input.txt', 'r') as file:
    safeReports = 0
    levels = []
    ascension = 0 # 1 for increasing, -1 for decreasing
    numReports = 0
    for report in file:
        unsafe = False
        numReports+=1
        ascension = 0
        levels = [int(level) for level in report.split(' ')]
        for i in range(1, len(levels)):
            if levels[i] > levels[i-1] and (ascension == 1 or ascension == 0) and abs(levels[i] - levels[i-1]) <=3:
                if ascension == 0:
                    ascension = 1
                continue
            elif levels[i] < levels[i-1] and (ascension == -1 or ascension == 0) and abs(levels[i] - levels[i-1]) <=3:
                if ascension == 0:
                    ascension = -1
                continue
            else:
                unsafe = True
                break 
        if unsafe:
            continue     
        safeReports += 1
print(safeReports)
print(numReports)