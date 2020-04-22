class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def preorder(self,A):
        if not A:
            return
        stack=[]
        ans=[]
        stack.append(A)
        while stack:
            b=stack.pop()
            ans.append(b.val)
            if b.right:
                stack.append(b.right)
            if b.left:
                stack.append(b.left)
        return ans

    def preorder_recursive(self,root,aux):
        if not root:
            return
        aux.append(root.val)
        self.preorder_recursive(root.left,aux)
        self.preorder_recursive(root.right,aux)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
A=Solution()
B=[]
A.preorder_recursive(root,B)
print(B)
print(A.preorder(root))
