#Question 1
def Exercise1(num):
    # Length of the array
    n = len(num) 
    # Base case
    if(n == 1):
        print(0)
        return
    # memory allocation for temporary arrays
    R = [0] * n
    L = [0] * n
    # Memory allocation for the product array
    ans=[0] * n
    # the left most element of the left array is always 1
    L[0] = 1
    # the right most element of right array is always 1
    R[n-1] = 1
    # create the left array
    for i in range(1, n):
        L[i] = num[i-1] * L[i-1]
    # create the right array
    for j in range(n-2, -1,-1):
        R[j] = num[j + 1] * R[j + 1]

    # create the product array using
    for i in range(n):
        ans[i] = L[i] * R[i]
    # print the constructed prod array
    for i in range(n):
        return ans
    

num=[1,2,3,4]
print('Question 1:', Exercise1(num))


#Question 2
def Exercise2(matrix):
    result = []
    rows, columns = len(matrix), len(matrix[0])
    up = left = 0
    right = columns - 1
    down = rows - 1

    while len(result) < rows * columns:
        # Travserve from left to right
        for col in range(left, right+1):
            result.append(matrix[up][col])
 
        # Traverse downwards
        for row in range(up +1, down +1):
            result.append(matrix[row][right])

        # make sure we are now on a differenet row
        if up != down:
            # Traverse from right to left
            for col in range(right - 1, left -1, -1):
                result.append(matrix[down][col])

        # make sure we are now on a differenet column
        if left != right:
            # Traverse upwards
            for row in range(down - 1, up, -1):
                result.append(matrix[row][left])

        left += 1
        right -= 1
        up += 1
        down -= 1
    return result        

matrix = [[1,2,3],[4,5,6],[7,8,9]] 
print('Question 2:',Exercise2(matrix))


#Question 3
def Exercise3(nums1, nums2, nums3, nums4):
    counter = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            for k in range(len(nums3)):
                for l in range(len(nums4)):
                    if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                        counter += 1
    return counter

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1, 2]
nums4 = [0, 2]

print('Question3', Exercise3(nums1,nums2, nums3, nums4))

#Question 4
def Exercise4(height):
    n = len(height)
    maxarea = 0
    left = 0
    right = n - 1
    while left < right:
        maxarea = max(maxarea, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxarea

height = [1,8,6,2,5,4,3,8,3,7]
print(Exercise4(height))

# Question 5
def Exercise5(nums):
    if not nums:
        return 0
    nums.sort()
    longest_seq = 1
    current_seq = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_seq += 1
        elif nums[i] == nums[i - 1]:
            continue
        else:
            longest_seq =  max(longest_seq, current_seq)
            current_seq = 1
    return max(longest_seq, current_seq)


nums = [0,3,7,2,5,8,4,6,0,1]
print(Exercise5(nums))