print '''
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
    '''

def problem():
    n,P = 600851475143,[]
    for a in range(3,int(n**0.5)+1,2):
        if n%a == 0:
            for i in range(2,int(n**0.5)+1):
                if n%i==0: continue
                P.append(a)
    print max(P)

problem()
