# We already have the basis for this from problem 3. But the way I wrote it
# originally is inefficient... we should only check primes up to the sqrt(c).
# I make the small modification below.

import math

def nextPrime(primeList):
    '''Determines and appends next prime number if primeList consists 
    of primes in order.'''
    def isPrime(c):
        '''Determines if c is prime.'''
        testPrimes = [x for x in primeList if x <= math.sqrt(c)]
        remainders = map(lambda x: c % x, testPrimes)
        if any(map(lambda x: not(x), remainders)): # if any remainders are zero
            return False
        else:
            return True
        
    biggestKnownPrime = max(primeList)
    candidate = biggestKnownPrime + 1
    while not isPrime(candidate):
        candidate += 1
        
    primeList.append(candidate) # append next prime...
    return primeList            # ... and return list

primes = [2]
while len(primes) < 10001:
    primes = nextPrime(primes)
    print primes[-1]
