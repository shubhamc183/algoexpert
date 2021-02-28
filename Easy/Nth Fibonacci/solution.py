# Time: O(n)
# Space: O(n)
def getNthFib(n):
  # We can also use dict to key track
	if n == 1:
		return 0
	elif n == 2:
		return 1
    fib_array = [0] * n
	fib_array[1] = 1
    for i in range(2, n):
		fib_array[i] = fib_array[i-1] + fib_array[i-2]
	return fib_array[n-1]

# We can reduce Space complexity by keeping the track of last 2 values
# Time: O(n)
# Space: O(1)
def getNthFib(n):
	last_two = [0, 1]
	for i in range(2, n):
		new_fib = last_two[0] + last_two[1]
		last_two[0] = last_two[1]
		last_two[1] = new_fib
	return last_two[1] if n > 1 else last_two[0]

