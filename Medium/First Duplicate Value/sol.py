# Time Complexity: O(n)
# Space Complexity: O(n)
def firstDuplicateValue1(array):
    seen = {}
    for a in array:
        if a in seen:
            return a
        else:
            seen[a] = 1
    return -1


# Time Complexity: O(n)
# Space Complexity: O(1)
# Since we can mutate the given array
# Let's mark the visited number's index by multiply it by -1
# without losing the data
def firstDuplicateValue(array):
    for a in array:
        a = abs(a)
        if array[a-1] < 0:
            return a
        array[a-1] *= -1
    return -1
		
