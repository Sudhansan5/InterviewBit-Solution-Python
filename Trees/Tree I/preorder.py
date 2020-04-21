class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def preorder(self,root,aux):
        if not root:
            return
        aux.append(root.val)
        self.preorder(root.left,aux)
        self.preorder(root.right,aux)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
A=Solution()
B=[]
A.preorder(root,B)
print(B)
