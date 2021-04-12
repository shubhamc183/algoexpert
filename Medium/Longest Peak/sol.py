# Cleaner and simpler
# T.C: O(n)
# S.C: O(1)
def longestPeak(array):
    array_len = len(array)
    longest_peak = 0
    for i in range(1, array_len - 1):
        # If peak is at ith index
        if array[i-1] < array[i] > array[i+1]:
            _i = i - 1
            while _i - 1 >= 0 and array[_i] > array[_i -1]:
                _i -= 1
            _j = i + 1
            while _j + 1 < array_len and array[_j] > array[_j + 1]:
                _j += 1
            longest_peak = max(longest_peak, _j - _i + 1)
            i = _j
    return longest_peak

