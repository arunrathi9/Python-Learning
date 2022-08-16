# Sorting Algorithm - Merge Sort

# TC - O(n*log(n))
def merge(arr, s, e):

    mid = s + (e-s)//2

    len1 = mid - s + 1
    len2 = e - mid

    arr1 = []
    arr2 = []

    # copy to new array
    main_arr_index = s
    for i in range(len1):
        arr1.append(arr[main_arr_index])
        main_arr_index += 1
    
    for j in range(len2):
        arr2.append(arr[main_arr_index])
        main_arr_index += 1

    # merge
    idx1 = 0
    idx2 = 0
    main_arr_index = s
    while(idx1 < len1 and idx2 < len2):
        if arr1[idx1] < arr2[idx2]:
            arr[main_arr_index] = arr1[idx1]
            main_arr_index += 1
            idx1 += 1
        else:
            arr[main_arr_index] = arr2[idx2]
            main_arr_index += 1
            idx2 += 1
    
    while(idx1<len1):
        arr[main_arr_index] = arr1[idx1]
        main_arr_index += 1
        idx1 += 1
    
    while(idx2<len2):
        arr[main_arr_index] = arr2[idx2]
        main_arr_index += 1
        idx2 += 1


def mergeSort(arr, s, e):

    if (s>=e):
        return

    mid = s + (e-s)//2

    mergeSort(arr, s, mid)

    mergeSort(arr, mid+1, e)

    merge(arr, s, e)

arr = [38, 27, 43, 3, 9, 82, 10]
mergeSort(arr, 0, len(arr)-1)
print(arr)

arr = [38, 27, 43, 3, 9, 82, 10,22,2,4,5,2,3,55,77,45,99]
mergeSort(arr, 0, len(arr)-1)
print(arr)

arr = [3, 4, 1, 6, 2, 5, 7]
mergeSort(arr, 0, len(arr)-1)
print(arr)
