def pivot(arr):
    s = 0; e = len(arr)-1
    mid = s + (e-s)//2
    while(s<e):
        if arr[mid] >= arr[0]:
            s = mid + 1
        else:
            e = mid

        mid = s + (e-s)//2

    return s

def binarySearch(arr, key):
    s = 0; n = len(arr); e = n-1
    mid = s + (e-s)//2

    while (s<=e):
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            s = mid + 1
        elif arr[mid] > key:
            e = mid - 1
        mid = s + (e-s)//2
    
    return -1

def search(arr, target):
    n = len(arr)

    pivot_ = pivot(arr)
    if arr[pivot_] <= target and target <= arr[n-1]:
        return pivot_ + binarySearch(arr[pivot_:n], target)
            
    else:
        return binarySearch(arr[:pivot_], target)

arr = [8, 9, 2, 4, 5, 6, 7]
print(search(arr, 2))
print(search(arr, 5))