# Leetcode - palindrome number
# 121 - true
# -121 = false

class Solution:
    def reverse(self, x):
        ans = 0
        while(x>0):
            digit = x%10
            ans = ans * 10 + digit
            x //= 10
        return ans
    
    def isPalindrome(self, x: int) -> bool:
        return True if self.reverse(x) == x else False

print(Solution().isPalindrome(121))