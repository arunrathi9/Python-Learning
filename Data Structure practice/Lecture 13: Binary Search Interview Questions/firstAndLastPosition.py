# coding ninjas - First and Last Position of an element in sorted array

def firstAndLastPosition(arr, key):
    
    # empty arr
    n = len(arr)
    if n == 0:
        return [-1,-1]

    # left part
    s = 0
    e = n-1
    left = -1
    while(s<=e):
        mid = s + (e-s)//2
        if arr[mid] == key:
            left = mid
            e = mid - 1
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid - 1
    
    # right part
    s = 0
    e = n-1
    right = -1
    while(s<=e):
        mid  = s + (e-s)//2
        if arr[mid] == key:
            right = mid
            s = mid + 1
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid - 1

    return [left, right]





arr = [5,7,7,8,8,10]
key = 8
print(firstAndLastPosition(arr, key))

arr = [5,7,7,8,8,10]
key = 6
print(firstAndLastPosition(arr, key))