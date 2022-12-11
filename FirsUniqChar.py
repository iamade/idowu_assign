# from collections import Counter
import collections


def FirsUniqChar(s):
    index = -1
    fnc = ''
    for i in s:
        if s.count(i) ==  1:
            fnc += i
            break
        else:
            index += 1
    if index == 1:
        return -1
    else:
        return fnc 

    # This one does not check other character
    # count = collections.Counter(s)
    # for idx, ch in enumerate(s):
    #     if count[ch] == 1:
    #         return idx, ch
    #     else:
    #         return -1

    


print(FirsUniqChar('Lv Love Python'))
        
