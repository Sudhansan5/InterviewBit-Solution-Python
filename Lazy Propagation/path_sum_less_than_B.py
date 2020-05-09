class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def del_node(self,A,sum,B):
        if not A:
            if sum >= B:
                return True
            return False
        l=self.del_node(A.left,sum+A.val,B)
        r=self.del_node(A.right,sum+A.val,B)
        if not l:
            A.left=None
        if not r:
            A.right=None
        return l if l else r

    def Solve(self,A,B):
        if self.del_node(A,0,B):
            return A
        return None

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(3)
root.left.right=Node(4)
root.right.right=Node(5)

A=Solution()
B=7
print(A.Solve(root,B))
