# Leetcode - Spiral matrix print

# TC - O(n*m)

def spiralOrder(arr):

    row = len(arr); col = len(arr[0])

    #indexes
    starting_row = 0; starting_col = 0
    ending_row = row-1; ending_col = col-1

    count = 0; total = row * col
    res = []

    while(count < total):

        # starting row
        for i in range(starting_col, ending_col+1):
            if count < total:
                res.append(arr[starting_row][i])
                count += 1
        starting_row += 1

        # end col
        for j in range(starting_row,ending_row+1):
            if count < total:
                res.append(arr[j][ending_col])
                count += 1
        ending_col -= 1

        # end row
        for i in range(ending_col, starting_col-1, -1):
            if count < total:
                res.append(arr[ending_row][i])
                count += 1
        ending_row -= 1

        # first col
        for j in range(ending_row, starting_row-1, -1):
            if count < total:
                res.append(arr[j][starting_col])
                count += 1
        starting_col += 1
        
        

    return res

        
#arr = [[1,2,3],[4,5,6],[7,8,9]]
arr = [[1,2,3,4],[5,6, 7,8],[9, 10,11,12]]

print(spiralOrder(arr))