# most naive way
sumOfMultiples = 0
threeMultiple = 0
fiveMultiple = 0

while threeMultiple < 1000:
    sumOfMultiples += threeMultiple
    threeMultiple += 3

while fiveMultiple < 1000:
    sumOfMultiples += fiveMultiple
    fiveMultiple += 5

print sumOfMultiples

# slightly more thought put into it
def sumTo(n):
    '''Gives the sum of 1 to n'''
    return n * (1 + n)/2

print sumTo(199) * 5 + sumTo(333) * 3
