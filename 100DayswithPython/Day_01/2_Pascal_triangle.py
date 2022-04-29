#Problem Statement: Given an integer N, return the first N rows of Pascal’s triangle.
#In Pascal’s triangle, each number is the sum of the two numbers directly above it.

# TC: O(n^2) in worst case.
n = 5

matrix = list([] for a in range(n)) # O(n)

for i in range(n): # O(n)
    matrix[i].extend([1]*(i+1)) # O(n)
    matrix[i][0] = matrix[i][i] = 1 # O(n)

    for j in range(1,i): # O(n*j)
        matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j] # O(n*j)

print(matrix)