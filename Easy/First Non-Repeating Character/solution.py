
# Time Complexity: O(N), n is the length of the string and  d is the number of disctinct characters in string
# Space Complexity: O(1), constant 26 letter hashmap at max
def firstNonRepeatingCharacter1(string):
  string_length = len(string)
	have_seen = {}
	for i in range(string_length):
		if string[i] not in have_seen:
			have_seen[string[i]] = i
		else:
			have_seen[string[i]] = -1
	solution = None
	for _key, _value in have_seen.items():
		if _value == -1:
			continue
		if solution is None:
			solution = _value
		solution = min(_value, solution)
    return -1 if solution is None else solution


## Cleaner Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def firstNonRepeatingCharacter(string):
	characters_count = {}
	for c in string:
		characters_count[c] = characters_count.get(c, 0) + 1
	for i in range(len(string)):
		if characters_count.get(string[i], 0) == 1:
			return i
	return -1