# Diameter of a Binary Tree - Geeks For Geeks

class Solution:
    
    def diameterFast(self, root):
        
        ans = [0,0]
        
        if root is None:
            return [0, 0]
            
        left = self.diameterFast(root.left)
        right = self.diameterFast(root.right)
        
        op1 = left[0]
        op2 = right[0]
        op3 = left[1] + right[1] + 1
        
        ans[0] = max(op1, op2, op3)
        ans[1] = max(left[1], right[1]) + 1
        
        return ans
        
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        
        return self.diameterFast(root)[0]

# driver code

from collections import deque

# Binary Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to Build Tree
def buildTree(s):
    #corner case
    if (len(s)==0 or s[0] == "N"):
        return None
    
    # creating list of strings from input
    # string after splitting by space

    ip = list(map(str, s.split()))

    # create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # push the root to queue
    q.append(root)
    size = size + 1

    # starting from the second element
    i = 1
    while(size>0 and i < len(ip)):
        # get and remove the front of queue
        currNode = q[0]
        q.popleft()
        size -= 1

        # Get the current node's value from the string
        currVal = ip[i]

        # if the left child is not null
        if (currVal != "N"):

            # Create the left child for the curr node
            currNode.left = Node(int(currVal))

            # push it to queue
            q.append(currNode.left)
            size += 1

        # for the right child
        i += 1
        if(i>=len(ip)):
            break
        currVal = ip[i]

        # if the right child is not null
        if (currVal != "N"):

            # Create the left child for the curr node
            currNode.right = Node(int(currVal))

            # push it to queue
            q.append(currNode.right)
            size += 1
        
        i += 1
    return root

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        ob = Solution().diameter(root)
        print(ob)