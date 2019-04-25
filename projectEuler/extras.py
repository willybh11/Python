def test5(n):
    for i in [11,13,14,16,17,18,19,20]:
        if n%i != 0: return False
    return True

def isprime(n):
    if n%2==0: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0: return False
    return True

def primeRange(n):
    workingList = [2]
    for i in range(3,n,2):
        if isprime(i): workingList.append(i)
    return workingList
    
def factorPtest(factors,n):
    if n in factors: return True
    for i in factors:
        if n%i == 0:
            return False
    return True
