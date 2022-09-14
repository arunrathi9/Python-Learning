# coding ninjas - count digits

def countDigit(n: int) -> int:
    ans = 0
    while(n>0):
        ans += 1
        n = n//10
        
    return ans

print(countDigit(12345))