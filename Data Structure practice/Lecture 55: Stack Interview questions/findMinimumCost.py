# coding ninjas problem - Minimum cost to make string valid

def findMinimumCost(str):
    
    # string of odd length
    if (len(str)%2 == 1):
        return -1
    
    stack = []
    
    for ch in str:
        
        if ch == '{':
            stack.append(ch)
            
        else:
            
            if (len(stack) > 0 and stack[-1] == '{'):
                stack.pop()
            else:
                stack.append(ch)
                
    # invalid string is remaining
    a = 0
    b = 0
    
    while(len(stack) > 0):
        if (stack[-1] == '}'):
            a += 1
        else:
            b += 1
        stack.pop()
        
    ans = (a+1)//2 + (b+1)//2
    
    return ans
                
    
print(findMinimumCost("{{{}"))