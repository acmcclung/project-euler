def nextPrime(primeList):
    '''Determines and appends next prime number if primeList consists 
    of primes in order.'''
    def isPrime(c):
        '''Determines if c is prime.'''
        remainders = map(lambda x: c % x, primeList)
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

# There is probably a clever recursive way to do this...

def primeFactors(num):
    '''Returns list of prime factors of num.'''
    facts = []
    primes = [2]
    while max(primes)**2 < num:
        while not(num % max(primes)): # if divisible by largest known prime...
            facts.append(max(primes)) # ... append it as a factor...
            num = num//max(primes)    # ... reduce...
        primes = nextPrime(primes)    # ... and look for next prime
    
    if num is not 1:
        facts.append(num)
    
    return facts

val = 600851475143

print max(primeFactors(val))
