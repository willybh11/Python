
n = 138902663
while not all(int(str(n*n)[x*2]) == x+1 for x in range(9)): n -= 2
print (n*10,"in",(n*10)**2)

# n is the ROUNDED ODD square root of the highest possible number, 19293949596979899
# we will subtract from n until its square meets the criteria of the problem:
# 1_2_3_4_5_6_7_8_9_0

# < int(str(n*n)[x*2]) == x+1 > checks if the x'th NON-VARIABLE value in the number
# is equal to x ( +1 because of the first number is 1, not 0)

# < for x in range(9) > repeats the above evaluation.
# A generator is ultimately returned, but all() does not care.

# for each iteration in the while loop, we subtract 2 so the number remians odd.
# Our square has a trailing digit of 9. Any such number has a root ending in 3 or 7.
# we know it ends in a 9 because squares that end in 0 must have a root with a trailing 0.
# we also know that the digit before the last must also be 0, as 10 squared is 100.

# < all() > returns TRUE if EVERY value in the list or generator evaluates to TRUE.
# if they are all TRUE, we want to return FALSE instead (hence the < not >,
# in order to break the while loop.

# at this point, n almost equal to our number. 
# we ignored the trailing 0 initally for the sake of simplicity and optimization.
# we multiply the number by 10 to give us the final answer.

# In theory, this method could be further optimized by decreasing n by
# alternating n-6 and n-4, which would ONLY check numbers ending in 3s and 7s.
