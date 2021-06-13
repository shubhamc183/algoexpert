# T.C: O(n)
# S.C: O(1)
def isValidSubsequence(array, sequence):
    array_len, sequence_len, i, j = len(array), len(sequence), 0, 0
    while i < array_len and j < sequence_len:
        if array[i] == sequence[j]:
            j += 1
        i += 1
    return True if j == sequence_len else False
