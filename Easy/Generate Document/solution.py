
def _insert_in_map(character, _map):
	if character in _map:
		_map[character] += 1
	else:
		_map[character] = 1

# Time Complexity: O(n + m) where n is the length of characters and m is the length of document
# Space Complexity: O(a + b) where a and b are the count of distinct characters in string characters and document respectively
def generateDocument1(characters, document):
    available_map = {}
	required_map = {}
	for _ in characters:
		_insert_in_map(_, available_map)
	for _ in document:
		_insert_in_map(_, required_map)
	for key in required_map.keys():
		if key not in available_map:
			return False
		elif required_map[key] > available_map[key]:
			return False
	return True


# Time Complexity: O(n + m) where n is the length of characters and m is the length of document
# Space Complexity: O(a) where a is the count of distinct characters in string characters
def generateDocument2(characters, document):
    available_map = {}
	required_map = {}
	for _ in characters:
		_insert_in_map(_, available_map)
	for _ in document:
		if _ not in available_map or available_map[_] < 1:
			return False
		available_map[_] -= 1
	return True