# coding ninjas - Sort a stack

def insertSort(stack, top):
    if len(stack) == 0:
        stack.append(top)
        return
    
    if (stack[-1] < top):
        stack.append(top)
        return
    
    num = stack[-1]
    stack.pop()
    
    insertSort(stack, top)
    stack.append(num)
    

def sortStack(stack):
    # given data structure is a python list 
    # as list have all the similar operations available so use them
    # Write your code here
    
    if len(stack) == 0:
        return
    
    top = stack[-1]
    stack.pop()
    
    sortStack(stack)
    
    insertSort(stack, top)

stack = [5,-2,9, -7,3]
sortStack(stack)
print(stack)