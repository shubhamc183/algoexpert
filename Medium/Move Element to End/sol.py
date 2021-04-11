# First solution:
# Time Complexity: O(n)
# Space Complexity: O(n); max, if all the number are distinct
# Save occurance of number other toMove in hash
# Maintain count of toMove
# Place number other than toMove in any order by interating over hash,
# and then place toMove count times at end
def moveElementToEnd1(array, toMove):
    # Write your code here.
    pass

## Better approach with less Space Complexity?
# Time Complexity: O(n)
# Space Complexity: O(1)
def moveElementToEnd2(array, toMove):
    count = 0
    array_len = len(array)
    for a in array:
        if a == toMove:
            count += 1
        left_index, right_index = 0, array_len - 1
    while count > 0:
        if array[right_index] == toMove:
            right_index -= 1
            count -= 1
            continue
        while array[left_index] != toMove:
            left_index += 1
        array[left_index] = array[right_index]
        array[right_index] = toMove
        left_index += 1
        right_index -= 1
        count -= 1
    return array

# Simple SolN
# Time Complexity: O(n)
# Space Complexity: O(1)
def moveElementToEnd(array, toMove):
    array_len = len(array)
    i, j = 0, array_len - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array

