class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def merge(self,A,B):
        if not A and not B:
            return
        if not A:
            return B
        if not B:
            return A
        left=self.merge(A.left,B.left)
        right=self.merge(A.right,B.right)
        node=Node(A.val+B.val)
        node.left=left
        node.right=right
        return node

    def print_node(self,root):
        if root:
            print(root.val)
            self.print_node(root.left)
            self.print_node(root.right)


root1=Node(1)
root1.left=Node(2)
root1.right=Node(3)
root1.left.left=Node(4)

root2 = Node(2)
root2.left = Node(4)
root2.right = Node(1)
root2.left.right = Node(2)
root2.right.right = Node(3)

A=Solution()
b=A.merge(root1,root2)
A.print_node(b)
