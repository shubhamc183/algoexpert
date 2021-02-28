# https://www.algoexpert.io/questions/Minimum%20Waiting%20Time

def minimumWaitingTime(queries):
	twt = 0
	queries.sort()
	queries_len = len(queries)
	for i in range(1, queries_len):
		twt += queries[i-1] * (queries_len - i)
	return twt
