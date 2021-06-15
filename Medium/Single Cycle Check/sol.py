# T.C: O(n)
# S.C: O(n)
def hasSingleCycle(array):
    i, array_len, visited_indexes = 0, len(array), {}
    while i not in visited_indexes:
        visited_indexes[i] = 1
        i = (i + array[i]) % array_len
    if i == 0 and len(visited_indexes) == array_len:
        return True
    return False

# T.C: O(n)
# S.C: O(1)
def hasSingleCycle(array):
    number_of_visited_elements, current_index, array_len = 0, 0, len(array)
    while number_of_visited_elements < array_len:
        if number_of_visited_elements > 0 and current_index == 0:
            return False
        number_of_visited_elements += 1
        current_index = (current_index + array[current_index]) % array_len
    return current_index == 0
