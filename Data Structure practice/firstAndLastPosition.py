# Coding Ninja problem

def firstOccurence(arr, n, key):
    s=0;e=n-1; ans = -1
    mid = s + (e-s)//2
    while(s<=e):
        if arr[mid] == key:
            ans = mid
            e = mid - 1
        elif arr[mid] < key:
            s = mid + 1
        elif arr[mid] > key:
            e = mid - 1
        mid = s + (e-s)//2

    return ans

def lastOccurence(arr, n, key):
    s=0;e=n-1; ans = -1
    mid = s + (e-s)//2
    while(s<=e):
        if arr[mid] == key:
            ans = mid
            s = mid + 1
        elif arr[mid] < key:
            s = mid + 1
        elif arr[mid] > key:
            e = mid - 1
        mid = s + (e-s)//2

    return ans

def firstAndLastPosition(arr, n, key):
    res = []
    res.append(firstOccurence(arr, n, key))
    res.append(lastOccurence(arr,n,key))

    return res

arr = [1,2,3,3,3,3,3,3,5]
print(firstAndLastPosition(arr, len(arr), 3))