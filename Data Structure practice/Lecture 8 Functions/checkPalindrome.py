# coding ninjas - check palindrome
# eg. racecar

def checkPalindrome(s, i):
    j = len(s)-i-1
    if (i>j):
        return True
    if s[i] != s[j]:
        return False
    
    return checkPalindrome(s, i+1)
    
def isPalindrome(s: str) -> bool:
    # Write your code here.
    return checkPalindrome(s, 0)