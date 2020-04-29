class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self,root):
        self.aux = []
        self.index = -1
        self.bst(root)

    def bst(self,root):
        if not root:
            return
        self.bst(root.left)
        self.aux.append(root.val)
        self.bst(root.right)

    def next(self):
        self.index += 1
        return self.aux[self.index]

    def hasNext(self):
        n=len(self.aux)
        return self.index + 1 < n

root=Node(10)
root.left=Node(5)
root.right=Node(15)
root.left.left=Node(4)
root.left.right=Node(9)
root.right.left=Node(14)
root.right.right=Node(19)

A=Solution(root)
while A.hasNext():
    print(A.next())
