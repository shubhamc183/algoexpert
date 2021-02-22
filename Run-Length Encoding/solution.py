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

