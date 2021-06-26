def _binary_search(array, target, array_len):
    left, right = 0, array_len - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# T.C: O( n + m + n(logm)) ==> ~ O(n log(m))
def searchInSortedMatrix2(matrix, target):
    width, hieght, = len(matrix[0]), len(matrix)
    for i in range(hieght):
        idx = _binary_search(matrix[i], target, width)
        if idx != -1:
            return [i, idx]
    return [-1, -1]

# T.C: O(n + m)
# S.C: O(1)
def searchInSortedMatrix(matrix, target):
    width, hieght, = len(matrix[0]), len(matrix)
    i, j = 0, width - 1
    while i < hieght and j >= 0:
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]
