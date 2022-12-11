def Reverse(x):
    rev = 0
    while x != 0:
        a = x % 10
        rev = rev * 10 + a
        x = x //10
    return rev


print(Reverse(123))