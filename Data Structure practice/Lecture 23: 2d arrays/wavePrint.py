# coding ninjas problem

# TC - O(n*m)
def wavePrint(arr, nRows, mCols):
    
    # Return a list of integers denoting the sine wave of the matrix
    res = []
    for col in range(mCols):
        
        if col%2 == 0:
            # even index - top to bottom
            for row in range(nRows):
                res.append(arr[row][col])
        else:
            #odd index - bottom to top
            for row in range(nRows-1, -1,-1):
                res.append(arr[row][col])

    return res

print(wavePrint([[1,2,3], [4,5,6], [7,8,9]], 3, 3))
print(wavePrint([[1]], 1, 1))
print(wavePrint([[1,2]], 1, 2))