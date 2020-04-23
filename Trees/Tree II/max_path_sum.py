class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.ans=float('-inf')

    def path_sum(self,A):
        if not A:
            return 0
        l=max(0,self.path_sum(A.left))
        r=max(0,self.path_sum(A.right))
        self.ans=max(self.ans,l+A.val+r)
        return max(l,r,0)+A.val

    def Solve(self,A):
        self.path_sum(A)
        return self.ans

root=Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
A=Solution()
print(A.Solve(root))
