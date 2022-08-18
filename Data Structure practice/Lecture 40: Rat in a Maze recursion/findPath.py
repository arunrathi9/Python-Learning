# GFG problem - Rat in a Maze I

def isSafe(x,y,n,visited_arr,m):

    if x<=n-1 and x>=0 and y<=n-1 and y>=0 and visited_arr[x][y] == 0 and m[x][y] == 1:
        return True
    else:
        return False

def solve(matrix, visited_arr, x, y, path, ans, n):

    if x==n-1 and y==n-1:
        ans.append("".join(path))
        return

    visited_arr[x][y] = 1

    # possible movement - D L R U

    # Down
    new_x = x + 1
    new_y = y
    if isSafe(new_x,new_y,n,visited_arr, matrix):
        path.append("D")
        solve(matrix, visited_arr, new_x,new_y,path,ans,n)
        path.pop()

    # Left
    new_x = x
    new_y = y - 1
    if isSafe(new_x,new_y,n,visited_arr, matrix):
        path.append("L")
        solve(matrix, visited_arr, new_x,new_y,path,ans,n)
        path.pop()

    # Right
    new_x = x
    new_y = y + 1
    if isSafe(new_x,new_y,n,visited_arr, matrix):
        path.append("R")
        solve(matrix, visited_arr, new_x,new_y,path,ans,n)
        path.pop()

    # Up
    new_x = x - 1
    new_y = y
    if isSafe(new_x,new_y,n,visited_arr, matrix):
        path.append("U")
        solve(matrix, visited_arr, new_x,new_y,path,ans,n)
        path.pop()

    visited_arr[x][y] = 0

def findPath(matrix, n):

    if matrix[0][0] == 0:
        return []
    visited_arr = [[0 for j in range(n)] for i in range(n)]
    src_row = 0
    src_col = 0

    path = []
    ans = []

    solve(matrix, visited_arr, src_row, src_col, path, ans, n)
    return ans

matrix = [[1,0,0,0], [1,1,0,1], [1,1,0,0], [0,1,1,1]]
n = len(matrix)
ans = findPath(matrix, n)
print(sorted(ans) if len(ans)>0 else -1)

matrix = [[1,0], [1,0]]
n = len(matrix)
ans = findPath(matrix, n)
print(sorted(ans) if len(ans)>0 else -1)