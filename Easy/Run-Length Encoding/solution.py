# https://www.algoexpert.io/questions/Run-Length%20Encoding
def runLengthEncoding(string):
	encoded_string = ""
	last_string = string[0]
	running_count = 1
	for i in range(1, len(string)):
		if string[i] == last_string:
			if running_count == 9:
				encoded_string += "%s%s" % (running_count, last_string)
				running_count = 1
			else:
				running_count += 1
		else:
			encoded_string += "%s%s" % (running_count, last_string)
			last_string = string[i]
			running_count = 1
	encoded_string += "%s%s" % (running_count, last_string)
	return encoded_string


## Algo Expert version which is short and easy
# Time: O(n)
# Space: O(n)
def runLengthEncoding(string):
	encoded_string = ""
	running_count = 1
	string_length = len(string)
	for i in range(1, string_length):
		if string[i-1] != string[i] or running_count == 9:
			encoded_string += "%s%s" % (running_count, string[i-1])
			running_count = 0
		running_count += 1
	encoded_string += "%s%s" % (running_count, string[string_length - 1])
	return encoded_string
