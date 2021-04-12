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

# Classic Problem of Sliding Window!!
# Single Loop
# T.C: O(n)
# S.C: O(n)
def staircaseTraversal4(height, maxSteps):
    ways = [0 for _ in range(height + 1)]
    ways[0], ways[1] = 1, 1
    sum_of_last_max_steps = 0
    for current_height in range(2, height + 1):
        if current_height == 2:
            sum_of_last_max_steps = sum(ways[max(0, current_height - maxSteps) : current_height])
        else:
            sum_of_last_max_steps += ways[current_height - 1]
        if current_height - maxSteps >= 0:
            sum_of_last_max_steps -= ways[current_height -1 - maxSteps]
        ways[current_height] = sum_of_last_max_steps
    return ways[height]

# Cleaner Approach by AlgoExpert
# Classic Problem of Sliding Window!!
# T.C: O(n)
# S.C: O(n)
def staircaseTraversal(height, maxSteps):
    ways_to_reach = [1]
    sliding_number_of_ways = 0
    for current_height in range(1, height + 1):
        start_of_window = current_height - maxSteps - 1
        end_of_window = current_height - 1
        if start_of_window >= 0:
            sliding_number_of_ways -= ways_to_reach[start_of_window]
        sliding_number_of_ways += ways_to_reach[end_of_window]
        ways_to_reach.append(sliding_number_of_ways)
    return ways_to_reach[height]

