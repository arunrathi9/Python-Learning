# coding ninja problem - check palindrome

def checkPalindrome(s, i, j):
    if (i>j):
        return True
    if s[i] != s[j]:
        return False
    
    return checkPalindrome(s, i+1, j-1)
    
def isPalindrome(s: str) -> bool:
    # Write your code here.
    return checkPalindrome(s, 0, len(s)-1)
    

print(isPalindrome("racecar"))
print(isPalindrome("Arun"))