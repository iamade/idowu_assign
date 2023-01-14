def Exercise9(s, t):
    if not s or not t:
        return ""
    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0) + 1
    left, right = 0, 0
    min_len = float("inf")
    min_start = 0
    count = len(t_count)
    for right in range(len(s)):
        if s[right] in t_count:
            t_count[s[right]] -= 1
            if t_count[s[right]] == 0:
                count -= 1
        while count == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            if s[left] in t_count:
                t_count[s[left]] += 1
                if t_count[s[left]] > 0:
                    count += 1
            left += 1
    if min_len == float("inf"):
        return ""
    else:
        return s[min_start:min_start+min_len]

s = "a"
t = "a"
print('Question 9', Exercise9(s, t))