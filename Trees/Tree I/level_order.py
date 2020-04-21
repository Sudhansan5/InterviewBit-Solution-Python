class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def level_order(self,root,aux):
        if not root:
            return
        q=[]
        q.append(root)
        while q:
            b=q.pop(0)
            aux.append(b.val)
            if b.left:
                q.append(b.left)
            if b.right:
                q.append(b.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
A=Solution()
B=[]
A.level_order(root,B)
print(B)
