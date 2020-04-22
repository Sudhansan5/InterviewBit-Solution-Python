from collections import defaultdict,deque
class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.ans=defaultdict(deque)

    def visit(self,A,level):
        if not A:
            return
        if level % 2 != 0:
            self.ans[level].append(A.val)
        else:
            self.ans[level].appendleft(A.val)
        self.visit(A.left,level+1)
        self.visit(A.right,level+1)

    def Solve(self,A):
        if A:
            self.visit(A,1)
            return [v for v in self.ans.values()]
        return []
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
A=Solution()
print(A.Solve(root))
