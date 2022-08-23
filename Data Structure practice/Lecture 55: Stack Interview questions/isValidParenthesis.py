# coding ninjas - Valid parenthesis

def isValidParenthesis(expression):

    stack = list()
    
    for ch in expression:
        if ch in ['[', '{', '(']:
            stack.append(ch)
            
        else:
            if (len(stack)>0):
                top = stack[-1]
                
                if ((ch == '}' and top == '{') or
                (ch == ')' and top == '(') or 
                (ch == ']' and top == '[')):
                    stack.pop()
                else:
                    return False
            else:
                return False
                    
    
    if len(stack) == 0:
        return True
    else:
        return False




# Main Code

str = "{})"
ans = isValidParenthesis(str)

if ans:
    print("Balanced")
    
else:
    print("Not Balanced")