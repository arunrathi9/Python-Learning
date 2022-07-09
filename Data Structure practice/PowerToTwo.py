#LeetCode: Problem Solution
'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
'''

def CheckPowertotwo(n):
    ans = 1

    while (ans<n):
        ans *= 2

    if ans == n:
        return True
    else:
        return False

print(CheckPowertotwo(5))
print(CheckPowertotwo(16))