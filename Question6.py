def Exercise6(nums):
    nums.sort()
    for ele in range(1, len(nums)):
        if nums[ele] == nums[ele - 1]:
            return nums[ele]

print(Exercise6([1,3,4,2,2]))
print(Exercise6([3,1,3,4,2]))

    