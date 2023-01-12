from collections import deque

def Exercise8(nums, k):
    q = deque()
    result = []
    for i, num in enumerate(nums):
        while q and nums[q[-1]] < num:
            q.pop()
        q.append(i)
        if q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            result.append(nums[q[0]])
    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3 
print(Exercise8(nums, k))