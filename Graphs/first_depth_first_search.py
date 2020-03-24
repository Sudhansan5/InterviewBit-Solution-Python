from _collections import defaultdict
class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def Solve(self,A,B,C):
        n=len(A)
        for i in range(n):
            self.graph[A[i]].append(i+1)
        vis=[0]*(n+1)
        q=[]
        q.append(C)
        vis[C]=1
        while q:
            a=q.pop(0)
            for i in self.graph[a]:
                if not vis[i]:
                    q.append(i)
                    vis[i]=1
        return vis[B]

A=[1,1,1,3,3,2,2,7,6]
B=9
C=1

D=Solution()
print(D.Solve(A,B,C))
