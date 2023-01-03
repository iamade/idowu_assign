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