
# sample code for the Sieve of Eratosthenes

def sieve(limit):
	composites = []
	primes = []
	for i in range(2,limit+1):				# Iterate from 2 up to the limit
		if i not in composites:				# check if number is not already marked
			primes.append(i)				# add the unmarked number to the prime list!
			for j in range(i*i,limit+1,i):	# starting at i squared, find multiples
				composites.append(j)		# mark these numbers as non-prime
			composites = composites[composites.index(i):]
	return primes

if __name__ == "__main__":		# if you run this file, it'll print the sieve.
	print(sieve(100))			# if you import it, this line is not executed.
