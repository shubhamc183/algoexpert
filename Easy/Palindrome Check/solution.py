# https://www.algoexpert.io/questions/Palindrome%20Check

# Time: O(n)
# Space: O(1)
def isPalindrome(string):
	string_length = len(string)
	for i in range(int(string_length/2) + 1):
		if string[i] != string[string_length - i - 1]:
			return False
    return True

# Time: O(n)
# Space: O(1)
# Binary Search Style
def isPalindrome(string):
	i = 0
	j = len(string) - 1
	while i < j:
		if string[i] != string[j]:
			return False
		i += 1
		j -= 1
	return True

