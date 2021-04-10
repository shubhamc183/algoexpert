# Time Complexity: O(n)
# Space Complexity: O(1)
def isMonotonic(array):
    array_len = len(array)
    increasing_or_constant, decreasing_or_constant = True, True
    for i in range(1, array_len):
        if increasing_or_constant is False and decreasing_or_constant is False:
            return False
        if increasing_or_constant and array[i] < array[i-1]:
            increasing_or_constant = False
        if decreasing_or_constant and array[i] > array[i-1]:
            decreasing_or_constant = False
    return increasing_or_constant or decreasing_or_constant

