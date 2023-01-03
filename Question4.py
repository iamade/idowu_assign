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


