# set matrix zero
# problem statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

#matrix = [[1,1,1], [1,0,1], [1,1,1]]
#matrix = [[1,2,3,4], [5,0,7,8], [0,11,12,13], [13,14,15,0]]
matrix = [[-4,2,6,7,0], [8,6,8,6,0], [2,3,-9,6,1]]
#matrix = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
#matrix = [[0,1,2,5], [3,4,5,2], [1,3,1,0]]
# sol - [[1,0,1], [0,0,0], [1,0,1]

# brute force method: TC O((n*m)*(n+m)) SC = O(1)
row = len(matrix)
col = len(matrix[0])

# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == 0:
#             for m in range(row):
#                 if matrix[m][j] == 0:
#                     continue
#                 matrix[m][j] = -1
#             for n in range(col):
#                 if matrix[i][n] == 0:
#                     continue
#                 matrix[i][n] = -1

# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == -1:
#             matrix[i][j] = 0

# print(matrix)

# method 2: better approach - taking two dummy arrays
# dummy_rowarr = [-1]*row
# dummy_colarr = [-1]*col

# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == 0:
#             dummy_rowarr[i] = 0
#             dummy_colarr[j] = 0

# for i in range(row):
#     for j in range(col):
#         if dummy_rowarr[i] == 0 or dummy_colarr[j] == 0:
#             matrix[i][j] = 0

# print(matrix)

# method 3 - best approach - taking first row n col as dummy arrays
col1 = 1
for i in range(row):
    if matrix[i][0] == 0:
        col1 = 0
    for j in range(1,col):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0

for i in range(row-1, -1,-1):
    for j in range(col-1, 0,-1):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0
    if col1 == 0: matrix[i][0] = 0

print(matrix)


