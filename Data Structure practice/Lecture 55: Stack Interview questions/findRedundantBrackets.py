# coding ninjas problem - Redundant Bracket

def findRedundantBrackets(s:str):
	
	# Return boolean True or False.
    stack = []
    for ch in s:
        if ch in ['(', '*', '+', '-', '/']:
            stack.append(ch)

        else:
            if ch == ')':
                is_redundant = True

                while(stack[-1] != '('):
                    if stack[-1] in ['*', '+', '-', '/']:
                        is_redundant = False
                    stack.pop()
                
                if is_redundant:
                    return True
                stack.pop()
            
    
    return False

#s = "(a+b*c) + (c))"
s = "(a*b+(c/d))"
print(findRedundantBrackets(s))