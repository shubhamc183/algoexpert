# For worst Solution Time Complexity will be O(n*n) but Space Complexity O(n)


# Time Complexity: O(n)
# Space Complexity: O(n)
def arrayOfProducts1(array):
    array_len = len(array)
    pro_from_left, pro_from_right = [1 for _ in range(array_len)], [1 for _ in range(array_len)]
    solution = []
    for i in range(array_len):
        if i == 0:
            pro_from_left[i] = array[i]
            pro_from_right[array_len -i - 1]  = array[array_len - i -1]
        else:
            pro_from_left[i] = pro_from_left[i-1] * array[i]
            pro_from_right[array_len -i - 1] = pro_from_right[array_len -i ] * array[array_len - i -1]
    for i in range(array_len):
        if i == 0:
            solution.append(pro_from_right[i+1])
        elif i == array_len - 1:
            solution.append(pro_from_left[i-1])
        else:
        solution.append(pro_from_left[i-1] * pro_from_right[i+1])
    return solution


# Better & Cleaner approach by AlgoExpert
# Time Complexity: O(n)
# Space Complexity: O(n)
def arrayOfProducts(array):
    array_len = len(array)
    solution = [ 1 for _ in range(array_len)]
    product_for_left, product_for_right = 1, 1

    for i in range(array_len):
        solution[i] = product_for_left
        product_for_left *= array[i]

    for i in reversed(range(array_len)):
        solution[i] *= product_for_right
        product_for_right *= array[i]

    return solution

