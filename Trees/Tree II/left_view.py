from collections import defaultdict,deque
class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.ans=defaultdict(deque)

    def left_view(self,A,level):
        if not A:
            return
        self.ans[level].append(A.val)
        self.left_view(A.left,level+1)
        self.left_view(A.right,level+1)

    def left_view_(self,A,vis,level,aux):
        if not A:
            return
        if level not in vis:
            vis[level]=True
            aux.append(A.val)
        self.left_view_(A.left,vis,level+1,aux)
        self.left_view_(A.right,vis,level+1,aux)
        return aux

    def Solve(self,A):
        self.left_view(A,1)
        return self.left_view_(A,{},1,[])
        #return [v[0] for v in self.ans.values()]

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
