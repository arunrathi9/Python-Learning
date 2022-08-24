# Geeks For Geeks - Celebrity Problem

def celebrity(M, n):
        
    #step 1: insert in stack
    stack = []
    for i in range(n):
        stack.append(i)
    
    #step 2: find potential candidate    
    while(len(stack) != 1):
        a = stack[-1]
        stack.pop()
        b = stack[-1]
        stack.pop()
        
        if (M[a][b] == 1):
            stack.append(b)
        else:
            stack.append(a)
    candidate = stack[-1]
    
    #step 3: Single element can be potential celebrity, verify it
    
    #row check
    #rowCheck = False
    zeroCount = 0
    for i in range(n):
        if M[candidate][i] == 0:
            zeroCount += 1
    
    # if zeroCount == n:
    #     rowCheck = True
    if zeroCount != n:
        return -1
        
    # col check
    #colCheck = False
    zeroCount = 0
    for i in range(n):
        if M[i][candidate] == 1:
            zeroCount += 1
            
    # if zeroCount == n-1:
    #     colCheck = True
    if zeroCount != n-1:
        return -1
    
    # result
    # if rowCheck and colCheck:
    #     return candidate
    # else:
    #     return -1
    return candidate

M = [[0,1,0], [0,0,0], [0,1,0]]
print(celebrity(M, len(M)))

M = [[0,1], [1,0]]
print(celebrity(M, len(M)))