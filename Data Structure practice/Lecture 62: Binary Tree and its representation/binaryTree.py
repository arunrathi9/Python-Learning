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
    
def levelOrderTraversal(root):
    d = deque()
    d.append(root)
    d.append(None)

    while (len(d)>0):
        temp = d.popleft()

        if temp is None:
            print()
            if (len(d)>0):
                d.append(None)
        else:
            print(temp.val, end = " ")

            if (temp.left != None):
                d.append(temp.left)
            
            if (temp.right != None):
                d.append(temp.right)
                

node = Node(None)
strr = list(map(int, "1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1".split(" ")))

root = buildTree(node)
levelOrderTraversal(root)