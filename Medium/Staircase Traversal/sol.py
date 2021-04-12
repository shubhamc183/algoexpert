# T.C: O(k^n), K is the maxstep
# S.C: O(n) for the recursive n call in function stack
#  |	                 rec(n)
#  |			/      \ 
#  | Height is N   rec(n-1) rec(n-2) ... K(as maximum breadth, maxSteps)	
#  |              /
#\ | /         ..
# \|/      rec(1)  rec(0)
#  .
def staircaseTraversal1(height, maxSteps):
    if height <= 1:
        return 1
    ways = 0
    for i in range(1, min(height, maxSteps) + 1):
        ways += staircaseTraversal(height - i, maxSteps)
    return ways

# Memoization with recursion
# T.C: O(k*n): as N will be the depth of recursion(for once) and,
# k times we will loop (visualize horizontally) to sum the values
# Space: O(n) i.e O(n) space for recursive calls + O(n) Space for hash map
def staircaseTraversal2(height, maxSteps):
    return stair_case_util(height, maxSteps, {0: 1, 1: 1})

def stair_case_util(height, maxSteps, memoization):
    if height in memoization:
        return memoization[height]
    ways = 0
    for i in range(1, min(height, maxSteps) + 1):
        ways += stair_case_util(height - i, maxSteps, memoization)
    memoization[height] = ways
    return ways

# Memoization with iteration
# T.C: O(k*n)
# S.C: O(n)
def staircaseTraversal3(height, maxSteps):
    ways = [0 for _ in range(height + 1)]
    ways[0], ways[1] = 1, 1
    for current_height in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= current_height:
            ways[current_height] += ways[current_height - step]
            step += 1
    return ways[height]

