with open('day 1/input.txt', 'r') as file:
    totalDistance = 0
    nums1 = {}
    nums2 = {}
    for line in file:
        num1, num2 = line.split('   ')
        num1 = int(num1)
        num2 = int(num2)
        if num1 in nums1:
            nums1[num1] += 1
        else:
            nums1[num1] = 1
        if num2 in nums2:
            nums2[num2] += 1
        else:
            nums2[num2] = 1
    for key in nums1:
        totalDistance += nums1[key]*key*(nums2[key] if key in nums2 else 0)
    print(totalDistance)

#make a hash table of left and right
#check how many of left(i) is in the right table
#similarity score = numLeft*left*(numRight)