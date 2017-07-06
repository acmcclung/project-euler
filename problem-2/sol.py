def fib(n):
    '''Gives the fibonacci numbers below n.'''
    fibList = [1, 2]            # generative fibonacci list
    nextVal = 3
    while nextVal < n :
        fibList.append(nextVal)
        nextVal = fibList[len(fibList)-1] + fibList[len(fibList)-2]

    return fibList

def isEven(n):
    '''Returns boolean revealing parity.'''
    return not(n % 2)


lst = fib(4e6)
print sum([x for x in lst if isEven(x)])
