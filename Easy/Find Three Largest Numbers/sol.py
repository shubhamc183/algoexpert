# Time Complexity: O(n)
# Space Complexity: O(1)
def findThreeLargestNumbers(array):
    three_largest = [None, None, None]
    for number in array:
        update_largest(three_largest, number)
    return three_largest

def update_largest(three_largest, number):
    if three_largest[2] is None or number > three_largest[2]:
        update_array(three_largest, 2, number)
    elif three_largest[1] is None or number > three_largest[1]:
        update_array(three_largest, 1, number)
    elif three_largest[0] is None or number > three_largest[0]:
        update_array(three_largest, 0, number)

def update_array(array, index, number):
    for i in range(index):
        array[i] = array[i+1]
    array[index] = number

