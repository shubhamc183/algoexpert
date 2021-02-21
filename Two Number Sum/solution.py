# https://www.algoexpert.io/questions/Two%20Number%20Sum

def twoNumberSum(array, targetSum):
    array_length = len(array)
	for i in range(array_length - 1):
		for j in range(i+1, array_length):
			if array[i] + array[j] == targetSum:
				return ([array[i], array[j]])
	return []
