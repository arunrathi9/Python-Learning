# implementation of Binary Tree
from collections import deque

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def buildTree(node):

    data = getData()

    if (data == -1):
        return None
    root = Node(data)
    
    print("Enter data for inserting in left node")
    root.left = buildTree(root.left)
    print("Enter data for inserting in right node")
    root.right = buildTree(root.right)
    return root

def getData():
    return strr.pop(0) if len(strr)>0 else None
    
def revlevelOrderTraversal(root):
    d = deque()

    
        
                

node = Node(None)
strr = list(map(int, "1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1".split(" ")))

root = buildTree(node)
revlevelOrderTraversal(root)