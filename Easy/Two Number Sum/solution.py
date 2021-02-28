# https://www.algoexpert.io/questions/Two%20Number%20Sum


# Time: O(n^2)
# Space: O(1)
def twoNumberSum(array, targetSum):
  array_length = len(array)
	for i in range(array_length - 1):
		for j in range(i+1, array_length):
			if array[i] + array[j] == targetSum:
				return ([array[i], array[j]])
	return []


# Time: O(n)
# Space: O(n)
def twoNumberSum(array, targetSum):
	number_map = {}
	for number in array:
		if targetSum - number in number_map:
			return [number, targetSum - number]
		number_map[number] = 1
	return []


# Time: O(nlog(n))
# Space: O(1)
def twoNumberSum(array, targetSum):
	array.sort()
	array_len = len(array)
	left, right = 0, array_len - 1
	while left < right:
		if array[left] + array[right] == targetSum:
			return [array[left], array[right]]
		elif array[left] + array[right] > targetSum:
			right -= 1
		else:
			left += 1
	return []
