# leetcode - Find All Duplicates in an Array

# TC - O(n)
# SC - O(n)

def findAllDuplicates(arr):

    unique_arr = set(arr)
    n=len(arr)
    ans = []
    for val in arr:
        if val in unique_arr:
            unique_arr.remove(val)
            continue
        ans.append(val)
    
    return ans

print(findAllDuplicates([1,2,1,2,3,5]))