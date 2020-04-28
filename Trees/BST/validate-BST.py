class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.isBST=0
        self.min=float('inf')
        self.max=float('-inf')

class Solution:
    def check_bst(self,A):
        curr=BST()
        if not A:
            curr.isBST=1
            return curr
        l=self.check_bst(A.left)
        r=self.check_bst(A.right)
        print(l.min,l.isBST,l.max)
        curr.min = min(A.val,l.min)
        curr.max = max(A.val,r.max)

        if l.isBST and r.isBST and l.max < A.val and r.min > A.val:
            curr.isBST=1
        else:
            curr.isBST=0
        return curr

    def check(self,A,min,max):
        if not A:
            return 1
        if A.val <= min or A.val >= max:
            return 0
        l=self.check(A.left,min,A.val)
        r=self.check(A.right,A.val,max)
        return l and r

    def Solve(self,A):
        B=self.check_bst(A)
        return B.isBST
        #return self.check(A,float('-inf'),float('inf'))

root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(4)
root.left.right=Node(9)
root.right.left=Node(14)
root.right.right=Node(19)
A=Solution()
print(A.Solve(root))
