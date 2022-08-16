# binary search using recursion

def binarySearch(arr,s,e,k):

    #base case
    if (s>e):
        return False

    mid = s + (e-s)//2

    if arr[mid] == k:
        return True
    
    if arr[mid]>k:
        return binarySearch(arr, s, mid-1, k)
    
    else:
        return binarySearch(arr, mid+1, e, k)

arr = [2,3,4,5,6]
ans = binarySearch(arr, 0, 4, 6)
print(ans)
ans = binarySearch(arr, 0, 4, 1)
print(ans)