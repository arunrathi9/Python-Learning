# Code Studio - Find Unique
# Problem Statement:
# In a given array of integers, all the elements are duplicated except one element.
# Also elements are not sorted. Find the Unique Array Element in an optimal way.

# T C - O(n)

def findUnique(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans = ans^arr[i]
    
    return ans

print(findUnique([2,3,4,3,2]))