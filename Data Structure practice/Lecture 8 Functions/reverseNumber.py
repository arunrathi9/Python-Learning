# coding ninjas - reverse a number

def reverseNumber(n):
    ans = 0
    while(n>0):
        digit = n%10
        ans = ans * 10 + digit
        n //= 10
    
    return ans

print(reverseNumber(1234))