# coding ninja problem - delete middle element from stack

def solve(inputStack, count, N):
    
    if count == N//2:
        inputStack.pop()
        return
    
    top = inputStack[-1]
    inputStack.pop()
    count += 1
    
    solve(inputStack, count, N)

    inputStack.append(top)
    
def deleteMiddle(inputStack, N):
    solve(inputStack, 0, N)

N = 5
inputStack = [1,2,3,4,5]
deleteMiddle(inputStack, N)
print(inputStack)

N = 6
inputStack = [1,2,3,4,5,6]
deleteMiddle(inputStack, N)
print(inputStack)