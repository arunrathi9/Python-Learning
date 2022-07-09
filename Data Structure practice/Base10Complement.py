# Leetcode
# Problem statement: 
'''The complement of an integer is the integer you get when you flip all the 
0's to 1's and all the 1's to 0's in its binary representation.'''

#TC - O(n)
#Learning - Always check variable constraint and edge cases

def Complement(n):
    m = n
    mask = 0

    #edge cases
    if n==0:
        return 1

    while(m):
        mask = mask<<1 | 1
        m = m >> 1
    
    return ~n & mask

print(Complement(5))