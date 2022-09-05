# Geeks for Geeks - check for balanced tree

# Method 1 - T.C -> O(n^2)
# #Function to check whether a binary tree is balanced or not.
# class Solution:
    
#     def height(self, root):
        
#         if root is None:
#             return 0
            
#         h_left = self.height(root.left)
#         h_right = self.height(root.right)
        
#         ans = max(h_left, h_right) + 1
        
#         return ans
        
#     def isBalanced(self,root):
    
#         if root is None:
#             return True
            
#         left = self.isBalanced(root.left)
#         right = self.isBalanced(root.right)
        
#         diff = True if abs(self.height(root.left) - self.height(root.right)) <= 1 else False
        
#         if (left and right and diff):
#             return 1
#         else:
#             return 0

# Method 2 - TC -> O(n)

#Function to check whether a binary tree is balanced or not.
class Solution:
    
    def isBalancedFast(self,root):
        
        ans = [True, 0]

        if root is None:
            return [True, 0]
            
        left = self.isBalancedFast(root.left)
        right = self.isBalancedFast(root.right)

        left_ans = left[0]
        right_ans = right[0]

        ans[1] = max(left[1], right[1]) + 1

        diff = True if abs(left[1] - right[1]) <= 1 else False
        
        if (left[0] and right[0] and diff):
            ans[0] = True
        else:
            ans[0] = False
        
        return ans

    def isBalanced(self,root):
        
        return self.isBalancedFast(root)[0]


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
        ob = Solution()
        if ob.isBalanced(root):
            print(1)
        else:
            print(0)