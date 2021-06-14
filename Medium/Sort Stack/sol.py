# n: len of stack
# T.C: O(n^2): if all pop and push are done; pre-sorted stack
# S.C: O(n): n level stack call
def insert(top, stack):
    if stack == [] or top > stack[-1]:
        stack.append(top)
    else:
        second_top = stack.pop()
        insert(top, stack)
        stack.append(second_top)
    return stack

def sortStack(stack):
    if stack == []:
        return []
    top = stack.pop()
    return insert(top, sortStack(stack))
