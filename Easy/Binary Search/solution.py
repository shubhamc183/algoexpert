# https://www.algoexpert.io/questions/Binary%20Search


# Time: O(nlog(n))
# Space: O(1)
def binarySearch(array, target):
	left_index = 0
	right_index = len(array) - 1
	while left_index <= right_index:
		middle_index = (left_index +right_index) // 2
		if array[middle_index] == target:
			return middle_index
		elif array[middle_index] > target:
			right_index = middle_index - 1
		else:
			left_index = middle_index + 1
	return -1
