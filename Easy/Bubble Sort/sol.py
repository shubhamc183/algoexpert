# T.C: O(n^2)
# S.C: O(1)
def bubbleSort(array):
    array_len = len(array)
    for i in range(array_len):
        for j in range(i+1, array_len):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array
