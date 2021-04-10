# Time Complexity: O(nlogn) for sorting
# Space Complexity: O(1)
def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for c in coins:
        if c > change + 1:
            return change + 1
	change += c
    return change + 1
