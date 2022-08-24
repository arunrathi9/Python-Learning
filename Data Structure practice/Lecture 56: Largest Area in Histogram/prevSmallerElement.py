def prevSmallerElement(arr, n):
    
    stack = [-1]
    ans = [-1]*n

    for i in range(n):
        curr = arr[i]
        while(stack[-1] != -1 and arr[stack[-1]] > curr):
            stack.pop()

        if stack[-1] != -1:
            ans[i] = stack[-1]
        stack.append(i)
    
    return ans


arr = [2,1,5,6,2,3]
print(prevSmallerElement(arr, len(arr)))