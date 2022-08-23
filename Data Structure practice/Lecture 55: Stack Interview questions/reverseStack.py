# coding ninjas problem - reverse a stack

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


def insertAtBottom(stack, num):
    if len(stack) == 0:
        stack.append(num)
        return
    
    top = stack[-1]
    stack.pop()
    insertAtBottom(stack, num)
    stack.append(top)
    
def reverseStack(stack) :
	
	# stack is a python list here
	# write your code here 
	# don't return anything 
	# don't print anything

    if len(stack) == 0:
        return

    num = stack[-1]
    stack.pop()

    reverseStack(stack)

    insertAtBottom(stack, num)









# taking input
def takeInput() :

	n = int(input().strip())
	if(n == 0) :
		 return list(), n

	stack = list(map(int,stdin.readline().strip().split(" ")))
	return stack, n


def printStack(stack) :

	while(len(stack) > 0) :

		print(stack.pop(),end = " ")


# main
stack, n = [], 0
reverseStack(stack)
printStack(stack)

stack, n = [0,1,3,4,5], 5
reverseStack(stack)
printStack(stack)