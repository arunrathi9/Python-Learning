# Sort 0 1 2 Dutch National Flag problem

def sort012(arr, n) :
    lo = 0; mid=0; hi = n-1
    while(mid<=hi):
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1
        
        elif arr[mid] == 2:
            arr[hi], arr[mid] = arr[mid], arr[hi]
            hi -= 1

arr = [0,1,2,2,1,0]
sort012(arr, len(arr))
print(arr)