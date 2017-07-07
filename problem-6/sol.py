# Let's think about this even smaller than 10. Arrange the values in a matrix 
# with M_{nm} = n * m. Then the 2 x 2 matrix looks like:
#
#   1 2
#   - -
# 1|1 2
# 2|2 4
#
# with the value (1 + 4 + 2*2) - 1 - 4 = 4. For a 3 x 3 matrix, we have
#
#   1 2 3
#   - - -
# 1|1 2 3
# 2|2 4 6
# 3|3 6 9
#
# (1 + 4 + 9 + 2*2 + 2*3 + 2*6) - 1 - 4 - 9 = 4 + 6 + 12 = 24. 
#
# Maybe one more is useful for context.
#
#   1 2  3  4
#   - -  -  - 
# 1|1 2  3  4
# 2|2 4  6  8
# 3|3 6  9 12
# 4|4 8 12 16
#
# 2 * (2 + 3 + 4 + 6 + 8 + 12) = 70.
#
# So basically we're always adding up that upper triangle of the
# matrix: 2 + 3 + 4 + ... + N + 2*3 + 2*4 + ... 2*N + ... + (N-1)*N

cumulativeSum = 0
N = 100
for ii in range(1,N+1):
    for jj in range(ii+1,N+1):
        cumulativeSum += ii * jj

print cumulativeSum * 2
