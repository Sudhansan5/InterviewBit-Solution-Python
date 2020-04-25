class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.isBST=False
        self.min=float('inf')
        self.max=float('-inf')
        self.size=0

class Solution:
    def check_bst(self,A):
        curr=BST()
        if not A:
            curr.isBST=True
            return curr
        l=self.check_bst(A.left)
        r=self.check_bst(A.right)

        curr.min = min(A.val,l.min)
        curr.max = max(A.val,r.max)

        if l.isBST and r.isBST and l.max <= A.val and r.min >= A.val:
            curr.size = l.size + r.size + 1
            curr.isBST=True
        else:
            curr.size= max(l.size,r.size)
            curr.isBST=False
        return curr

    def Solve(self,A):
        b=self.check_bst(A)
        return b.size

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
