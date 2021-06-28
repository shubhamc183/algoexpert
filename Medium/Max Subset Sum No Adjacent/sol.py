# T.C: O(n)
# S.C: O(n)
def maxSubsetSumNoAdjacent1(array):
    array_len = len(array)
    if array_len == 0:
        return 0
    elif array_len == 1:
        return array[0]
    max_subset_sum = array[:]
    max_subset_sum[1] = max(array[0], array[1])
    for i in range(2, array_len):
        max_subset_sum[i] = max(max_subset_sum[i-1], max_subset_sum[i-2] + array[i])
    return max_subset_sum[-1]

# T.C: O(n)
# S.C: O(1)
def maxSubsetSumNoAdjacent(array):
    array_len = len(array)
    if array_len == 0:
        return 0
    elif array_len == 1:
        return array[0]
    sum_till_second_last, sum_till_last = array[0], max(array[0], array[1])
    for i in range(2, array_len):
        _ = max(sum_till_last, sum_till_second_last + array[i])
        sum_till_second_last, sum_till_last = sum_till_last, _
    return max(sum_till_last, sum_till_second_last)