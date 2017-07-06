# create all palindromes in appropriate range
thousands = range(100,1000)     # first three digits
ones = map(lambda x: int(x/100), thousands)
tens = map(lambda x: int((x % 100)/10), thousands)
hundreds = map(lambda x: x % 10, thousands)
palindromes = map(lambda th,hu,te,on: th*1000 + hu*100 + te*10 + on,\
                      thousands,hundreds,tens,ones)

palindromes.sort()              # order palindromes

# check for solutions in order
found = False
breakPoint = (999+100)/2
while not found:
    num = palindromes.pop()     # gets last palindrome and removes from list
    p1 = int(num**0.5)
    if p1 >= breakPoint:        
        while p1 < 1000:
            p2 = num//p1
            if not(num % p1) and (p2 < 1000):   # if solution
                found = True
                break
            p1 += 1
    if p1 < breakPoint:
        while p1 > 99:
            p2 = num//p1
            if not(num % p1) and (p2 < 1000):   # if solution
                found = True
                break
            p1 -= 1

print "%d times %d is %d" % (p1, p2, p1*p2)
