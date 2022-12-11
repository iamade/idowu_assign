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
print(Exercise1(num))