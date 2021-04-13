# T.C: O(n)
# S.C: O(n)
def reverseWordsInString(string):
    sol = ""
    i = len(string) - 1
    while i >= 0:
        if string[i] == ' ':
            sol += ' '
            i -= 1
            continue
        _end_idx = i
        while i >= 0 and string[i] != ' ':
            i -= 1
        for _i in range(i + 1, _end_idx + 1):
            sol += string[_i]
    return sol

# Other solution can be
# 1) Reverse the whole string and then un-reverse just the words
