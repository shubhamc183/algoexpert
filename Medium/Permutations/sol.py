# T.C: O(n^2 * n!)
# S.C: O(n * n!)
def getPermutations1(array):
    permutations = []
    permutation_util(array, [], permutations)
    return permutations

def permutation_util1(array, current_permutations, permutations):
    # Base case: if array is empty and current_permutations has something
    if not len(array) and len(current_permutations):
        permutations.append(current_permutations)
    for i in range(len(array)):
        new_array = array[:i] + array[i+1:]
        new_permutations = current_permutations + [array[i]]
        permutation_util(new_array, new_permutations, permutations)

# Better time complexity: instead of making new array we can swap number back n forth
# T.C: O(n * n!)
# S.C: O(n * n!)
def getPermutations(array):
    permutations = []
    permutation_util(0, array, permutations)
    return permutations

def permutation_util(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array.copy())
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            permutation_util(i+1, array, permutations)
            array[i], array[j] = array[j], array[i]	
