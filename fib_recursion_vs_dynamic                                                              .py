import timeit

def fib(n, memo):
	if memo[n] is not None:
		return memo[n]
	if n == 1 or n == 2:
		result=1
	else:
		result = fib(n-1, memo) + fib(n-2, memo)
	memo[n] = result
	return result

def fib_memo(n):
	memo = [None] * (n+1)
	return fib(n, memo)

#print(fib_memo(100))


def fib_tree(n):
	start = [1,1,2]
	if n <= 3:
		return start[n-1]
	else:
		for x in range(4, n+1):
			a,b,c=start
			start[0] = b
			start[1] = c
			start[2] = b+c
	return start[-1]

#print(fib_tree(100))

def test(n):
	print(timeit.timeit("fib_tree(1000)", number=n, globals=globals()))
	
	# there should be an error, so no panik
	print(timeit.timeit("fib_memo(1000)", number=n, globals=globals()))

test(100)