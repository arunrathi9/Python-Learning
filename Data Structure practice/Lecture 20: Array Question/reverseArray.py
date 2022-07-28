# Coding Ninjas - Reverse an Array

def reverseArr(arr, m):
    s = m+1
    e = len(arr)-1
    while(s<e):
        temp = arr[s]
        arr[s] = arr[e]
        arr[e] = temp
        s += 1
        e -= 1
    
    return arr


arr = [1,2,3,4,5,6]
print(reverseArr(arr, 3))