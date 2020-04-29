#cartesian tree is a heap ordered binary tree, where the root is greater than all the elements in the subtree
class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def buildTree(self,A,s,e):
        if s > e:
            return
        n = max(A[s:e+1])
        i = A.index(n)
        root = Node(A[i])
        root.left = self.buildTree(A,s,i-1)
        root.right = self.buildTree(A,i+1,e)
        return root

    def print_node(self,root):
        if root:
            self.print_node(root.left)
            print(root.val)
            self.print_node(root.right)

    def Solve(self,A):
        n=len(A)
        m = self.buildTree(A,0,n-1)
        self.print_node(m)

A=[1,2,3]
B=Solution()
B.Solve(A)
