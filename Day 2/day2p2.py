def bf(levels):
    for i in range(len(levels)):
        nLevel = levels[:i] + levels[i+1:]
        if is_it_valid(nLevel):
            return 1
    return 0

def is_it_valid(levels):
    ascension = None
    for i in range(len(levels)-1):
        if levels[i] > levels[i+1] and (ascension == False or ascension == None) and abs(levels[i] - levels[i+1]) <=3:
            ascension = False
            continue
        elif levels[i] < levels[i+1] and (ascension == True or ascension == None) and abs(levels[i] - levels[i+1]) <=3:
            ascension = True
            continue
        else:
            return False
    return True

def reportTester(levels, pDamp):
    valid = is_it_valid(levels)
    if not valid:
            ans = bf(levels)
            return ans
    return 1    

with open('day 2/input.txt', 'r') as file:
    safeReports = 0
    for report in file:
        safeReports += reportTester([int(level) for level in report.split(' ')], False)
    print(safeReports)

"""
Testing edge cases
print(reportTester([48, 46, 47, 49, 51, 54, 56], False))
print(reportTester([1,1,2,3,4,5], False))
print(reportTester([1,2,3,4,5,5], False))
print(reportTester([5,1,2,3,4,5], False))
print(reportTester([1,4,3,2,1], False))
print(reportTester([1,6,7,8,9], False))
print(reportTester([1,2,3,4,3], False))
print(reportTester([9,8,7,6,7], False))
print(reportTester([7,10,8,10,11], False))
print(reportTester([29,28,27,25,26,25,22,20], False))"""