# 2 = 2
# 3 = 3
# 4 = 2^2
# 5 = 5
# 6 = 2 * 3
# 7 = 7
# 8 = 2^3
# 9 = 3 * 3
# 10 = 2 * 5
# 2^3 * 3^2 * 5 * 7 = 2520, per example
#
# So the algorithm is: prime factorize each of the numbers from 1 to n,
# count the multiplicity of each prime, and multiply the primes together
# raised to the maximum multiplicity.
#
# This actually may be quickest to do by hand...
# 11 = 11
# 12 = 2^2 * 3
# 13 = 13
# 14 = 2 * 7
# 15 = 3 * 5
# 16 = 2^4
# 17 = 17
# 18 = 2 * 3^2
# 19 = 19
# 20 = 2^2 * 5
#
# Then the number is 19 * 17 * 13 * 11 * 7 * 5 * 3^2 * 2^4
testValue = 19 * 17 * 13 * 11 * 7 * 5 * 3**2 * 2**4

for ii in range(1,21):
    if (testValue % ii) > 0:
        print "Failed!"
    else:
        print "%d//%d = %d" % (testValue,ii,testValue//ii)
