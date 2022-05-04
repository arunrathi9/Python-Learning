'''
next_permutation : find next lexicographically greater permutation
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
'''
arr = [1, 2, 3, 6, 5, 4]
asc_arr = True

for i in range(len(arr), 2,-1):
    if arr[i-1] > arr[i-2]:
        temp = min(arr[i:])
        arr[i-1] = arr[i-2]
        arr[i-2] = temp
        asc_arr = False
        break

if asc_arr == True:
    arr = sorted(arr)

print(arr)