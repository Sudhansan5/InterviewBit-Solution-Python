class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class TreeDetails:
    def __init__(self):
        self.node=None

class Solution:
    def isNodePresent(self,root,node):
        if not root:
            return False
        if root.val == node:
            return True
        return self.isNodePresent(root.left,node) or self.isNodePresent(root.right,node)

    def find_lca(self,root,n1,n2,lca):
        if not root:
            return False

        if root.val == n1 or root.val == n2:
            lca.node=root.val
            return True

        l = self.find_lca(root.left,n1,n2,lca)
        r = self.find_lca(root.right,n1,n2,lca)

        if l and r:
            lca.node=root.val

        return l if l else r

    def Solve(self,A,B,C):
        lca=TreeDetails()
        if self.isNodePresent(A,B) and self.isNodePresent(A,C):
            self.find_lca(A,B,C,lca)
            return lca.node
        return -1

root=Node(11)
root.left=Node(90)
root.right=Node(4)
root.left.left=Node(60)
root.left.right=Node(3)
root.right.left=Node(8)
root.right.right=Node(20)

A=Solution()
B=60
C=3
print(A.Solve(root,B,C))
