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
print(Exercise2(matrix))
