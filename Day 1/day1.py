with open('day 1/input.txt', 'r') as file:
    totalDistance = 0
    nums1 = []
    nums2 = []
    for line in file:
        num1, num2 = line.split('   ')
        nums1.append(int(num1))
        nums2.append(int(num2))
    nums1.sort()
    nums2.sort()
    for i in range(len(nums1)):
        totalDistance += abs(nums1[i] - nums2[i])
    print(totalDistance)