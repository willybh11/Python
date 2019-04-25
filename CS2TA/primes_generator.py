
def primes(limit):
	x = [False] * (n + 1)
	for i in range(2, limit +1):
		if x[i]: continue
		yield i
		for j in range(2*i,limit+1,i):
			x[j] = True


print(list(primes(100)))
