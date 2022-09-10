from heightBinaryTree import buildTree

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here1
        if root1 is None and root2 is None:
            return True
            
        if root1 is None and root2 is not None:
            return False
        
        if root1 is not None and root2 is None:
            return False
            
        left = self.isIdentical(root1.left, root2.left)
        right = self.isIdentical(root1.right, root2.right)
        
        value = True if root1.data == root2.data else False
            
        if left and right and value:
            return True
    
        return False

t = int(input())
for _ in range(0, t):
    s1 = input()
    s2 = input()
    head1 = buildTree(s1)
    head2 = buildTree(s2)
    if Solution().isIdentical(head1, head2):
        print("Yes")
    else:
        print("No")