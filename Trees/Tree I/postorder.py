class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def postorder(self,root,aux):
        if not root:
            return
        self.postorder(root.left,aux)
        self.postorder(root.right,aux)
        aux.append(root.val)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
A=Solution()
B=[]
A.postorder(root,B)
print(B)
