import sys
def fib(i):
	a,b = 0,1
	for j in range(i-1): a,b = b,a+b
	print b

if __name__ == "__main__":
	fib(int(sys.argv[1]))
