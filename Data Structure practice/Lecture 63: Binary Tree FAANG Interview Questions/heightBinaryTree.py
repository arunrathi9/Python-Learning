# gfg - height of binary tree

class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        
        if root is None:
            return 0
        
        h_left = self.height(root.left)
        h_right = self.height(root.right)
        
        ans = max(h_left, h_right) + 1
        
        return ans
        
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
        print(ob.height(root))