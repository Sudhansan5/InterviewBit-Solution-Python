class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.count=0

    def dfs(self,A,B):
        if not A:
            return
        if A.val > B:
            self.count += 1
        self.dfs(A.left,max(A.val,B))
        self.dfs(A.right,max(A.val,B))

    def Solve(self,A):
        maxx=float('-inf')
        self.dfs(A,maxx)
        return self.count

root=Node(4)
root.left=Node(5)
root.right=Node(2)
root.right.left=Node(3)
root.right.right=Node(6)
A=Solution()
print(A.Solve(root))
