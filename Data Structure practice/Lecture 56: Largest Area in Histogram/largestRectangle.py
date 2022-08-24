# Coding ninjas - largest rectangle in a histogram

def nextSmallerElement(arr, n):
    stack = [-1]
    ans = [0] * n
    
    for i in range(n-1, -1, -1):
        while(stack[-1] != -1 and arr[stack[-1]]>=arr[i]):
            stack.pop()
        
        ans[i] = stack[-1]
        stack.append(i)
        
    return ans
    
def prevSmallerElement(arr, n):
    
    stack = [-1]
    ans = [-1]*n

    for i in range(n):
        curr = arr[i]
        while(stack[-1] != -1 and arr[stack[-1]] >= curr):
            stack.pop()

        if stack[-1] != -1:
            ans[i] = stack[-1]
        stack.append(i)
    
    return ans
        
            

def largestRectangle(arr):
    
    n = len(arr)
    
    next = nextSmallerElement(arr, n)
    
    prev = prevSmallerElement(arr, n)
    
    area = -1
    for i in range(n):
        l = arr[i]
        if (next[i] == -1):
            next[i] = n
        b = next[i] - prev[i] - 1 
        new_area = l * b
        area = new_area if new_area > area else area
        
    return area


arr = [2,1,5,6,2,3]
print(largestRectangle(arr))