# O(n) for both T.C and S.C
def spiralTraverse(array):
    width, hieght, sol = len(array[0]), len(array), []
    start_i, start_j, end_i, end_j = 0, 0, hieght - 1, width - 1
    while start_i <= end_i and start_j <= end_j:
        for j in range(start_j, end_j+1):
            sol.append(array[start_i][j])
        for i in range(start_i+1, end_i):
            sol.append(array[i][end_j])
        if start_i != end_i: # case where there is only one row
            for j in range(end_j, start_j-1, -1):
                sol.append(array[end_i][j])
        if start_j != end_j: # case where there is only one column
            for i in range(end_i-1, start_i, -1):
                sol.append(array[i][start_j])
        start_i += 1
        start_j += 1
        end_i -= 1
        end_j -= 1
    return sol
