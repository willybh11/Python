# m y   e y e s   h a v e   b e e n   o p e n e d   t o   t h e   t r u e   r e a l i t y   o f   t h e   w o r l d
from time import clock
start = clock()

n,k = 3,True
while k: (n,k) = (n,False) if not any([not any((n-2*(sq**2)) % i == 0 for i in range(3, int((n-2*(sq**2))**0.5 + 1), 2) ) for sq in range(-1, int((n/2)**0.5)+1)]) else (n+2,k)
print 'Answer:',n

print clock()-start
