
# import sys
from primesSieve import sieve 		# put 'primes_sieve.py' in the same directory as this file!

def main():

	limit = 50 # int(sys.argv[1])

	primes = sieve(limit)

	primesSet = set(primes)

	odds = set(range(3,limit,2))
	
	oddComposites = odds - primesSet

	print("Limit:\t\t",			limit)
	print("Primes Set:\t",		primesSet)
	print("Odds:\t\t",			odds)
	print("Odd Composites:\t",	oddComposites)

if __name__ == "__main__":
	main()