class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def buildTree(self,A,B):
        if not A or not B:
            return
        node=Node(A.pop(0))
        index=B.index(node.val)
        node.left=self.buildTree(A,B[:index])
        node.right=self.buildTree(A,B[index+1:])
        return node

    def print_node(self,root):
        if root:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)

A=[1,2,3]
B=[2,1,3]
C=Solution()
D=C.buildTree(A,B)
C.print_node(D)
