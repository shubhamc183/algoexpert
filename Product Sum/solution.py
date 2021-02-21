# https://www.algoexpert.io/questions/Product%20Sum

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
	return calculate_sub_special_array(1, array)


def calculate_sub_special_array(depth, sub_element):
	sub_sum = 0
	for element in sub_element:
		if type(element) == int:
			sub_sum += element
			continue
		sub_sum += (depth + 1) * calculate_sub_special_array(depth + 1, element)
	return sub_sum


# Algo Expert Solution
# Here, they used default parameter to make one function solution and,
# multiplied sub sum to depth and end which made the code much more clear
def productSum(array, depth=1):
	_sum = 0
	for element in array:
		if type(element) == list:
			_sum += productSum(element, depth+1)
		else:
			_sum += element
	return _sum * depth