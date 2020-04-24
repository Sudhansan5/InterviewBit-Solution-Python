class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def find(self,A,val):
        if not A:
            return 0
        if A.val==val:
            return 1
        if (A.left and self.find(A.left,val) )or (A.right and self.find(A.right,val)):
            return 1
        return 0

    def lcs(self,A,B,C):
        if not A:
            return
        if A.val==B or A.val==C:
            return A
        l=self.lcs(A.left,B,C)
        r=self.lcs(A.right,B,C)
        if l and r:
            return A
        return l if l else r

    def Solve(self,A,B,C):
        a=self.find(A,B)
        b=self.find(A,C)
        if not a or not b:
            return -1
        c=self.lcs(A,B,C)
        return c.val if c else -1

root=Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
A=Solution()
B=10
C=5
print(A.Solve(root,B,C))
