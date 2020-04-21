class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def isBalanced(self,A):
        if not A:
            return 0
        else:
            h1=self.isBalanced(A.left)
            h2=self.isBalanced(A.right)
            if abs(h1-h2) <= 1:
                return 1
            else:
                return 0
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
A=Solution()
print(A.isBalanced(root))
