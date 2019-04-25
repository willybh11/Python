
def fib(n):
	return 1 if n <= 1 else fib(n-1)+fib(n-2)

def pal_2(word,index=0):# 2 parameters
    return 1 if index > len(word)/2 else 0 if word[index] != word[-index-1] else pal(word,index+1)

def pal_1(word):        # 1 parameter
    return 1 if len(word) < 2 else 0 if word[-1] != word[0] else pal(word[1:-1])

def dig(n):
    return 1 if abs(n) < 10 else dig(n/10) + 1

def fac(n):
    return 1 if n <= 1 else fac(n-1)*n
