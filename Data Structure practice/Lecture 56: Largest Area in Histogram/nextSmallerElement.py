# coding ninjas - Next smaller element

def nextSmallerElement(arr,n):
    
    stack = [-1]
    ans = [0] * n
    
    for i in range(n-1, -1, -1):
        while(stack[-1]>=arr[i]):
            stack.pop()
        
        ans[i] = stack[-1]
        stack.append(arr[i])
        
    return ans

def idxNextSmallerElement(arr,n):
    
    stack = [-1]
    ans = [0] * n
    
    for i in range(n-1, -1, -1):
        curr = arr[i]
        while(stack[-1] != -1 and arr[stack[-1]]>curr):
            stack.pop()
        
        ans[i] = stack[-1]
        stack.append(i)
        
    return ans

arr = [2,1,4,3]
print(nextSmallerElement(arr, 4))

arr = [2,1,5,6,2,3]
print(idxNextSmallerElement(arr, 6))