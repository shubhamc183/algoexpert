# Time Complexity: O(nlog(n) + mlog(m))
# Space Complexity: O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    minimum_diff = 10**10
    first_element, second_element = None, None
    for first in arrayOne:
        _ = 10**10
        _second_element = None
        for second in arrayTwo:
            if first != second and _ > abs(first - second):
                _ = abs(first - second)
                _second_element = second
            elif first == second:
                return [first, second]
        if minimum_diff > _:
            minimum_diff = _
            first_element = first
            second_element = _second_element
    return [first_element, second_element]

# Cleaner
# Time Complexity: O(nlog(n) + mlog(m))
# Space Complexity: O(1)
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    len_one, len_two = len(arrayOne), len(arrayTwo)
    i_one, i_two = 0, 0
    smallest, current = 10**10, 10**10
    smallest_pair = []
    while i_one < len_one and i_two < len_two:
        first_number = arrayOne[i_one]
        second_number = arrayTwo[i_two]
        if first_number < second_number:
            current = second_number - first_number
            i_one += 1
        elif first_number > second_number:
            current = first_number - second_number
            i_two += 1
        else:
            return [first_number, second_number]
        if smallest > current:
            smallest = current
            smallest_pair = [first_number, second_number]
    return smallest_pair

