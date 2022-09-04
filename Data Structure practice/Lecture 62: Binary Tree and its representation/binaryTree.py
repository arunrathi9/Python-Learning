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

def inOrder(root):

    if (root is None):
        return

    inOrder(root.left)
    print(root.val, end=" ")
    inOrder(root.right)                

def preOrder(root):

    if (root is None):
        return

    print(root.val, end=" ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):

    if (root is None):
        return

    postOrder(root.left)
    postOrder(root.right)
    print(root.val, end=" ")

def buildfromLevelOrder(root):
    print("Enter the root node: ")
    root = Node(int(input()))
    q = deque()
    q.append(root)
    while(len(q)>0):
        temp = q.popleft()

        # left node
        print("Enter the value for left node: ", temp.val)
        leftnode = int(input())
        if (leftnode != -1):
            temp.left = Node(leftnode)
            root.left = Node(leftnode)
            q.append(temp.left)

        # right node
        print("Enter the value for right1 node: ", temp.val)
        right_node = int(input())
        if(right_node != -1):
            temp.right = Node(right_node)
            root.right = Node(right_node)
            q.append(temp.right)
    
    return root

root = Node(None)
# strr = list(map(int, "1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1".split(" ")))

# root = buildTree(node)
# levelOrderTraversal(root)
# inOrder(root)
# print()
# preOrder(root)
# print()
# postOrder(root)
root = buildfromLevelOrder(root)
levelOrderTraversal(root)