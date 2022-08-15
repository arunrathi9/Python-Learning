# Leetcode - search a 2d matrix

# TC - O(log(n*m))

def searchMatrix(arr, target):

    col = len(arr[0])
    s = 0
    e = len(arr)*col - 1
    
    while (s <= e):
        mid = s + (e-s)//2
        if arr[mid//col][mid%col] == target:
            return True
        
        elif arr[mid//col][mid%col] < target:
            s = mid + 1

        elif arr[mid//col][mid%col] > target:
            e = mid - 1

    return False

arr = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]

print(searchMatrix(arr, 16))
print(searchMatrix(arr, 34))
print(searchMatrix(arr, 4))