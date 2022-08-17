# Quick Sort Algorithm implementation using Recursion

def partition(arr,s,e):
    pivot = arr[s]

    count = 0
    for i in range(s+1, e+1):
        if arr[i]<=pivot:
            count += 1
    
    pivot_idx = s + count
    temp = arr[pivot_idx]
    arr[pivot_idx] = pivot
    arr[s] = temp

    while(s<pivot_idx and e>pivot_idx):

        while(arr[s] <= arr[pivot_idx]):
            s += 1

        while(arr[e] > arr[pivot_idx]):
            e -= 1

        if s<pivot_idx and e>pivot_idx:
            temp = arr[s]
            arr[s] = arr[e]
            arr[e] = temp
            s += 1
            e -= 1

    return pivot_idx


def quickSort(arr, s, e):
    
    if s>e:
        return

    pivot_idx = partition(arr, s, e)

    quickSort(arr, s, pivot_idx-1)

    quickSort(arr, pivot_idx+1, e)

arr = [6, 6, -6, -2, -4, -6, 2, -6  ]
quickSort(arr, 0, len(arr)-1)
print(arr)

# 6
# 7
# 9 9 9 8 2 3 -6 
# 8
# 6 6 -6 -2 -4 -6 2 -6 
# 6
# 0 9 -4 -9 -9 -7 
# 4
# 1 -8 -8 2 
# 6
# 3 -8 0 6 -1 -5 
# 3
# 0 3 -5