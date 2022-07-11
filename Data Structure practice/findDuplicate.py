## Coding Ninjas
# IMP - ****
def findDuplicate(arr):
    n = len(arr)
    ans = 0

    #XOR ing for all elements in arr
    for i in range(n):
        ans = ans^arr[i]
    
    for i in range(n-1):
        ans = ans^(i+1)

    return ans

print(findDuplicate([1,2,3,2]))