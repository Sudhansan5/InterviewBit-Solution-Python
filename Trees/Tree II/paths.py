class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.ans=[]

    def dfs(self,root,path):
        if not root:
            return
        if not root.left and not root.right:
            self.ans.append(path+str(root.val))
        self.dfs(root.left,path+str(root.val)+'->')
        self.dfs(root.right,path+str(root.val)+'->')

    def Solve(self,A):
        self.dfs(A,'')
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
