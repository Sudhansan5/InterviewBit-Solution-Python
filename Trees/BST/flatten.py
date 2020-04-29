class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def flatten(self,A):
        if not A:
            return
        self.flatten(A.left)
        self.flatten(A.right)

        l = A.left
        r = A.right
        A.left=None
        A.right=l
        tmp=A

        while tmp.right:
            tmp = tmp.right
        tmp.right = r

        return A

    def print_node(self,root):
        if root:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)

    def Solve(self,A):
        b=self.flatten(A)
        self.print_node(b)

root=Node(1)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(3)
root.left.right=Node(4)
root.right.right=Node(6)

A=Solution()
A.Solve(root)
