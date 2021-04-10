# Time Complexity: O(nlogn)
# Space Complexity: O(n)
def sortedSquaredArray1(array):
  solution = []
	for a in array:
		solution.append(a**2)
    return sorted(solution)


# Time Complexity: O(n)
# Space Complexity: O(n)
def sortedSquaredArray(array):
	array_length = len(array)
	solution = []
	left = 0
	for i in range(array_length):
		if array[i] < 0:
			left = i
		else:
			break
	right = left + 1
	while left > -1 and right < array_length:
		if array[right] == 0 or abs(array[left]) > array[right]:
			solution.append(array[right]**2)
			right += 1
		else:
			solution.append(array[left]**2)
			left -= 1
	# leftovers
	while left > -1:
		solution.append(array[left]**2)
		left -= 1
	while right < array_length:
		solution.append(array[right]**2)
		right += 1
	return solution


# Cleaner
# Time Complexity: O(n)
# Space Complexity: O(n)
def sortedSquaredArray(array):
	array_length = len(array)
	left = 0
	right = array_length - 1
	solution = [0 for _ in array]
	for i in reversed(range(array_length)):
		if abs(array[left]) >= abs(array[right]):
			solution[i] = array[left]**2
			left += 1
		else:
			solution[i] = array[right]**2
			right -= 1
	return solution
