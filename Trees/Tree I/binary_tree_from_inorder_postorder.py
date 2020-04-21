class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def buildTree(self,A,B):
        if not A or not B:
            return
        node=Node(B.pop())
        index=A.index(node.val)
        node.right=self.buildTree(A[index+1:],B)
        node.left=self.buildTree(A[:index],B)
        return node

    def print_node(self,root):
        if root:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)

A=[2,1,3]
B=[2,3,1]
C=Solution()
D=C.buildTree(A,B)
print(C.print_node(D))
