def Exercise7(s: str, k: int) -> int:
    max_len = 0
    left = 0
    char_count = {}
    for right in range(len(s)):
        char = s[right]
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

s = "eceba"
k = 2

print(Exercise7(s, k))