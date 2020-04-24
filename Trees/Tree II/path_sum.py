class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def Solve(self,A,B):
        if not A:
            return 0
        if B-A.val==0 and not A.left and not A.right:
            return 1
        return self.Solve(A.left,B-A.val) or self.Solve(A.right,B-A.val)

root=Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
A=Solution()
print(A.Solve(root,22))
