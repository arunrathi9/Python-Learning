# leetcode problem - search a 2d matrix II

# TC - 

def searchMatrix(arr, target):

    row_index = 0
    col = len(arr[0])-1
    row = len(arr)

    while(row_index < row and col >= 0):
        element = arr[row_index][col]

        if element == target:
            return True
        elif element > target:
            col -= 1
        else:
            row_index += 1
    
    return False

arr = [[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]
print(searchMatrix(arr, 5))
print(searchMatrix(arr, 20))