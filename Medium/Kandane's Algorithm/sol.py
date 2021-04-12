# Time Complexity: O(n)
# Space Complexity: O(1)
def kadanesAlgorithm(array):
    _ans = -float('inf')
    sum_till_here = 0
    for a in array:
        sum_till_here += a
        _ans = max(_ans, sum_till_here)
        if sum_till_here < 0:
            sum_till_here = 0
    return _ans

