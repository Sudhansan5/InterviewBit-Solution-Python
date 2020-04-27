class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def isSymmetric(self,A,B):
        if not A and not B:
            return True
        if A and B:
            return A.val==B.val and self.isSymmetric(A.left,B.right) and self.isSymmetric(A.right,B.left)
        return False
        
    def Solve(self,A):
        return self.isSymmetric(A,A)

root=Node(11)
root.left=Node(8)
root.right=Node(19)
root.left.left=Node(1)
root.left.right=Node(17)
root.right.left=Node(12)
root.right.right=Node(30)
root.right.right.left=Node(25)
root.right.right.right=Node(35)

A=Solution()
print(A.Solve(root))
