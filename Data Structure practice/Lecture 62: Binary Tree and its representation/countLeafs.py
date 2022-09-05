'''
    Following is the Binary Tree Node class structure.
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

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
    
    #print("Enter data for inserting in left node")
    root.left = buildTree(root.left)
    #print("Enter data for inserting in right node")
    root.right = buildTree(root.right)
    return root

def getData():
    return strr.pop(0) if len(strr)>0 else None

def inOrder(root):
    global count
    
    if root is None:
        return
    
    inOrder(root.left)
    
    if (root.left is None and root.right is None):
        count += 1
        
    #print(root.data, root.right, count)
    inOrder(root.right)
    return count
    
def noOfLeafNodes(root):
    # Write your code here.
    global count
    count = 0
    count = inOrder(root)
    return count

strr = list(map(int, "20 10 5 -1 -1 15 13 -1 -1 -1 35 30 -1 -1 42 -1 -1".split(" ")))
root = Node(None)
root = buildTree(root)
print(noOfLeafNodes(root))