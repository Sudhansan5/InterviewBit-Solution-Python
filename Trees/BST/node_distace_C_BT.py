from collections import defaultdict, deque
class Node:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def __init__(self):
        self.graph=defaultdict(list)

    def build_graph(self,parent,child):
        if parent and child:
            self.graph[parent.val].append(child.val)
            self.graph[child.val].append(parent.val)

        if child.left:
            self.build_graph(child,child.left)
        if child.right:
            self.build_graph(child,child.right)

    def Solve(self,A,B,C):
        self.build_graph(None,A)
        q=deque()
        q.append((B,1))
        vis=set([B])
        ans=[]
        while q:
            i,j=q.popleft()
            for node in self.graph[i]:
                if node not in vis:
                    if j==C:
                        ans.append(node)
                    q.append((node,j+1))
                    vis.add(node)
        return ans if len(q) < C else [B]

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.left.left.left=Node(8)

A=Solution()
B=3
C=0
print(A.Solve(root,B,C))
