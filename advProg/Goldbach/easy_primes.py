# # custom primechecker, very pythonic and terrible-looking
def isPrime(n): ## NOTE: this primechecker does not include 2
     return not any(n % i == 0 for i in range(3, int(n**0.5 + 1), 2) )
