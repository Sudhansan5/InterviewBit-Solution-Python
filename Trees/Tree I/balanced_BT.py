class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.ans=0

    def height(self,A):
        if not A:
            return 0
        l=self.height(A.left)
        r=self.height(A.right)
        self.ans=max(self.ans,abs(l-r))
        return max(l,r)+1

    def isBalanced(self,A):
        if not A:
            return 1
        self.height(A)
        if self.ans > 0:
            return 0
        return 1

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
A=Solution()
print(A.isBalanced(root))
