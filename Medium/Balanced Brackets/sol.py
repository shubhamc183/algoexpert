# T.C: O(n)
# S.C: O(n)
def balancedBrackets(string):
    stack = []
    openers = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    closers = {
        ')': 1,
        '}': 1,
        ']': 1
    }
    for c in string:
        if c in openers and c not in closers:
            stack.append(c)
        elif c in closers:
            if not stack:
                return False
            top = stack.pop()
            if openers[top] != c:
                return False
    if stack:
        return False
    return True

