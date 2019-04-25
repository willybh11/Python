
# import sys

def sieve(limit):
	pass	# put your code here that returns a list of primes!

def main():

	limit = 50 # int(sys.argv[1])

	primes = sieve(limit)

	primesSet = set(primes)

	odds = set(range(3,limit,2))
	
	oddCompositesSet = odds - primesSet

	oddCompositesList = list(oddCompositesSet)

	print("Limit:\t\t",			limit)
	print("Primes Set:\t",		primesSet)
	print("Odds:\t\t",			odds)
	print("Odd Composites:\t",	oddCompositesList)

if __name__ == "__main__":
	main()