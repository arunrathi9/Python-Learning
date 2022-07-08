# Leetcode: Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer 
# range [-231, 231 - 1], then return 0.

def reverseInt(n):

    min = -1*2**31
    max = 2**31 - 1

    neg = False
    if n < 0:
        neg = True
        n *= -1
    ans = 0
    while(n>0):
        last_digit = n%10
        ans = ans*10 + last_digit
        n = n//10
    
    if neg:
        ans *= -1
    
    if ans<max and ans>min:
        print(ans)
    else:
        print(0)


n = 1234567899
reverseInt(n)  
