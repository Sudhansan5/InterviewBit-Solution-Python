from collections import defaultdict,deque
class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.ans=defaultdict(deque)

    def right_view(self,A,level):
        if not A:
            return
        self.ans[level].append(A.val)
        self.right_view(A.left,level+1)
        self.right_view(A.right,level+1)

    def right_view_(self,A,level,vis,aux):
        if not A:
            return
        if level not in vis:
            vis[level]=True
            aux.append(A.val)
        self.right_view_(A.right,level+1,vis,aux)
        self.right_view_(A.left,level+1,vis,aux)
        return aux

    def Solve(self,A):
        self.right_view(A,1)
        #return [v[-1] for v in self.ans.values()]
        return self.right_view_(A,1,{},[])

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
