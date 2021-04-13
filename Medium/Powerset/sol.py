# Using Bits Magic
# T.C: O(n * 2^n)
# S.C: O(n * 2^n)
def powerset1(array):
    solution = []
    array_len = len(array)
    for i in range(2**array_len):
        bit, j, _ = i, 0, []
        while bit and j < array_len:
            if bit & 1:
                _.insert(0, array[j])
            j += 1
            bit = bit >> 1
        solution.append(_)
    return solution


# Using Iteration
# T.C: O(n * 2^n)
# S.C: O(n * 2^n)
def powerset(array):
    solution = [ [] ]
    for a in array:
        for i in range(len(solution)):
            solution.append(solution[i] + [a])
    return solution

