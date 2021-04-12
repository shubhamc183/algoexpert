# Time Complexity: O(n^2)
# Space Complexity: O(n) if all the numbers are stored in the solution array
def threeNumberSum(array, targetSum):
    array.sort()
    solution = []
    array_len = len(array)
    for i in range(array_len - 2):
        _i, _j, _to_make = i + 1, array_len - 1, targetSum - array[i]
        while _i < _j:
            if array[_i] + array[_j] == _to_make:
                solution.append([array[i], array[_i], array[_j]])
                _i, _j = _i + 1, _j - 1
            elif array[_i] + array[_j] > _to_make:
                _j -= 1
            else:
                _i += 1
    return solution

