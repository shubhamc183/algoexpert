# T.C: O(n^2) in all cases
# S.C: O(1)
def selectionSort(array):
    array_len = len(array)
    for i in range(array_len - 1):
        min_idx = i
        for j in range(i+1, array_len):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
