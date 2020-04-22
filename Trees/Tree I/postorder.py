class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def postorder(self,A):
        if not A:
            return
        stack=[]
        ans=[]
        stack.append(A)
        while stack:
            b=stack.pop()
            ans.insert(0,b.val)
            if b.left:
                stack.append(b.left)
            if b.right:
                stack.append(b.right)
        return ans

    def postorder_recursive(self,root,aux):
        if not root:
            return
        self.postorder_recursive(root.left,aux)
        self.postorder_recursive(root.right,aux)
        aux.append(root.val)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
A=Solution()
B=[]
A.postorder_recursive(root,B)
print(B)
print(A.postorder(root))
