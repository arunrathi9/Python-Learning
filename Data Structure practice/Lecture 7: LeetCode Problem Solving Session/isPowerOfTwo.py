# Leetcode problem - Power of Two

def isPowerOfTwo(n: int) -> bool:
#         ans = 1

#         while (ans<n):
#             ans *= 2

#         if ans == n:
#             return True
        
#         return False
        while(n>1):
            n = n/2
        return (n==1)
    
print(isPowerOfTwo(20))
print(isPowerOfTwo(32))